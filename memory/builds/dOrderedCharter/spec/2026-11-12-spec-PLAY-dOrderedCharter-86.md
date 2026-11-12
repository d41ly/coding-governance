# PLAY-dOrderedCharter-86 — the run guard finds the driver by its file name, and the opt-in pack's self-test leg gets its pending row

**Status:** CLOSED · rev-1 · 2026-11-12 · node a · Tier-1 · base 1f82d4bdc · streams tooling · order 47 · advances PLAY-dOrderedCharter-38

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-25-build-PLAY-dOrderedCharter-1-agent-ledger.md](../build/2026-10-25-build-PLAY-dOrderedCharter-1-agent-ledger.md) | journal | PLAY-dOrderedCharter-1 PLAY-dOrderedCharter-2 PLAY-dOrderedCharter-3 PLAY-dOrderedCharter-4 PLAY-dOrderedCharter-5 PLAY-dOrderedCharter-6 PLAY-dOrderedCharter-7 PLAY-dOrderedCharter-8 PLAY-dOrderedCharter-9 PLAY-dOrderedCharter-10 PLAY-dOrderedCharter-11 PLAY-dOrderedCharter-12 PLAY-dOrderedCharter-13 PLAY-dOrderedCharter-14 PLAY-dOrderedCharter-15 PLAY-dOrderedCharter-16 PLAY-dOrderedCharter-17 PLAY-dOrderedCharter-18 PLAY-dOrderedCharter-19 PLAY-dOrderedCharter-20 PLAY-dOrderedCharter-21 PLAY-dOrderedCharter-22 PLAY-dOrderedCharter-23 PLAY-dOrderedCharter-24 PLAY-dOrderedCharter-25 PLAY-dOrderedCharter-26 PLAY-dOrderedCharter-27 PLAY-dOrderedCharter-28 PLAY-dOrderedCharter-29 PLAY-dOrderedCharter-30 PLAY-dOrderedCharter-31 PLAY-dOrderedCharter-32 PLAY-dOrderedCharter-33 PLAY-dOrderedCharter-34 PLAY-dOrderedCharter-35 PLAY-dOrderedCharter-36 PLAY-dOrderedCharter-37 PLAY-dOrderedCharter-39 PLAY-dOrderedCharter-40 PLAY-dOrderedCharter-41 PLAY-dOrderedCharter-42 PLAY-dOrderedCharter-43 PLAY-dOrderedCharter-44 PLAY-dOrderedCharter-45 PLAY-dOrderedCharter-46 PLAY-dOrderedCharter-47 PLAY-dOrderedCharter-48 PLAY-dOrderedCharter-49 PLAY-dOrderedCharter-50 PLAY-dOrderedCharter-51 PLAY-dOrderedCharter-52 PLAY-dOrderedCharter-53 PLAY-dOrderedCharter-54 PLAY-dOrderedCharter-55 PLAY-dOrderedCharter-61 PLAY-dOrderedCharter-62 PLAY-dOrderedCharter-63 PLAY-dOrderedCharter-64 PLAY-dOrderedCharter-65 PLAY-dOrderedCharter-67 PLAY-dOrderedCharter-68 PLAY-dOrderedCharter-69 PLAY-dOrderedCharter-70 PLAY-dOrderedCharter-71 PLAY-dOrderedCharter-72 PLAY-dOrderedCharter-73 PLAY-dOrderedCharter-74 PLAY-dOrderedCharter-75 PLAY-dOrderedCharter-76 PLAY-dOrderedCharter-77 PLAY-dOrderedCharter-78 PLAY-dOrderedCharter-80 PLAY-dOrderedCharter-81 PLAY-dOrderedCharter-82 PLAY-dOrderedCharter-83 PLAY-dOrderedCharter-84 PLAY-dOrderedCharter-85 PLAY-dOrderedCharter-87 |
| [2026-11-12-build-PLAY-dOrderedCharter-86-1-builder-return.md](../build/2026-11-12-build-PLAY-dOrderedCharter-86-1-builder-return.md) | journal | — |
| [2026-11-12-build-PLAY-dOrderedCharter-86-ledger.md](../build/2026-11-12-build-PLAY-dOrderedCharter-86-ledger.md) | journal | — |
| [2026-11-12-prompt-PLAY-dOrderedCharter-86-1-spec-writer.md](../prompts/2026-11-12-prompt-PLAY-dOrderedCharter-86-1-spec-writer.md) | journal | — |
| [2026-11-12-prompt-PLAY-dOrderedCharter-86-build-brief.md](../prompts/2026-11-12-prompt-PLAY-dOrderedCharter-86-build-brief.md) | journal | — |
| [2026-11-12-prompt-PLAY-dOrderedCharter-86-spec-brief.md](../prompts/2026-11-12-prompt-PLAY-dOrderedCharter-86-spec-brief.md) | research | — |

<!-- /gen:spec-records -->

## 1. Goal

The fifth close bar, run over `948b91720`, has two product reds. The first is
`install-prefix (shipped surface)`, which reds on three literal spellings of the unattended kit's
driver that PLAY-dOrderedCharter-84 added to the policy kit. The second is `core meta-check`, which
reds on the `spec-audit opt-in pack self-test` leg because the leg has no `enforces` and no pending
row. This unit clears both reds. The guard finds the driver by its file name at any depth, and the
pending list gets the row that the meta-check's own message names.

## 2. Scope (IN)

- **S1** — In `tools/policy/guard.py`, `check_run_mandate` changes its `git grep` pathspec at HEAD
  from `":(glob)**/unattended/unattended.sh"` to `":(glob)**/unattended.sh"`. The grep pattern, the
  HEAD read and the one-set rule do not change. Observed by AC1, AC2 and AC3.
- **S2** — In `tools/policy/check_policy.py`, the `GUARD_RUN` cases set `driver_rel` to
  `"vendor/gov/run/unattended.sh"` in place of `"tools/unattended/unattended.sh"`. That is a driver
  under a foreign prefix whose home is renamed. It is still a literal, so the case still reads no
  source file. Observed by AC1, AC2 and AC3.
- **S3** — In `tools/policy/README.md`, the terminal-set clause changes
  `` `unattended/unattended.sh` at `HEAD` `` to `` `unattended.sh` at `HEAD` at any depth ``.
  Observed by AC1.
- **S4** — `tools/playbook/core-pending.txt` gets the row `leg`, `spec-audit opt-in pack self-test`,
  `dWitnessedBar`, joined by TABs, directly after the `review-join self-test` row. Observed by AC4.

## 3. Non-goals (OUT)

- An `enforces` list on the `spec-audit opt-in pack self-test` row of `tools/gate-legs.json`, or any
  other edit to that file.
- Routing the guard through an inline `resolve_kit_dir`. The guard reads HEAD alone and imports no
  other kit (section 4).
- A version bump of the policy or playbook kit. PLAY-dOrderedCharter-84 changed the guard without
  one, and `kit epoch (shipped bytes move, the version moves)` was not among the close bar's reds.
- An edit to `help/policy.md`. It says "the unattended driver at `HEAD`" and names no path, so it
  stays accurate.
- The close bar's other four reds, which belong to other units (the brief's prompt).

## 4. Design

### Evidence

Read at `1f82d4bdc`. A role agent's scratch guard refuses both legs, so each figure comes from the
legs' own code. The ban figures come from the counter's Python, which
`tools/check-install-prefix.sh` carries in its `BAN_PY` heredoc. The probe feeds it the population
the shell derives and the templates from `govkit.py shipped`. The meta-check figures come from
`run_meta_check` in `tools/playbook/core.py`. Every probe ran over two `git archive` copies of HEAD:
the base copy, and a pass copy carrying S1 to S4.

- The ban red (PINNED, the counter over the base copy and the worktree): exit 1 with three hits.
  They are `tools/policy/README.md:378` and `tools/policy/guard.py@ec8de420:237`, each spelling
  `unattended/unattended.sh`, and `tools/policy/check_policy.py@4820db46:2449`, spelling
  `tools/unattended/unattended.sh`. The summary reads 508 files graded and 7 renders left out. Rule
  3 of the predicate counts a kit segment followed by a file under any lead,
  `tools/check-install-prefix.sh@401a476d:52`.
- The meta-check red (PINNED, `run_meta_check` over the worktree): exit 1 with one red,
  `leg 'spec-audit opt-in pack self-test' carries no enforces and no pending row`, from
  `tools/playbook/core.py@854477bd:327`. The leg row is `tools/gate-legs.json@83fb3a5f:783`, with no `guard` and no
  `enforces`. It arrived with TOOL-dFairHearing-16 at `886c11fea`.
- The pass measured (PINNED, the same probes over the pass copy): the counter exits 0 with 0
  spellings on 0 lines, still 508 files graded and 7 renders. `run_meta_check` returns 0 with
  `leg 146` pending, where the base has 145.

### The ban (S1, S2, S3)

The counter drains a kit segment only after `{prefix}/`, `{kit}/`, `{{TOOL_ROOT}}`, `<prefix>/` or
`<tool-root>/`, `tools/check-install-prefix.sh@401a476d:405`. None of these fits the guard. The guard greps
HEAD at every depth, so it has no prefix to spell. The remedy that keeps its rules is to drop the
kit segment and match the driver by its file name. The probe over each new line counts nothing.
`**/unattended.sh` and `**/unattended/unattended.sh` select the same one declaration at HEAD:
`tools/unattended/unattended.sh@2a59172f:993`, `PHASES_TERMINAL="LANDED ABORTED"` (PINNED, `git grep` over
both pathspecs). `**/` also matches at the root: a toy repository holding `unattended.sh` and
`vendor/gov/run/unattended.sh` returned both. No other tracked file is named `unattended.sh`
(PINNED, `git ls-tree -r` at HEAD).

The fixture's driver moves to `vendor/gov/run/unattended.sh`. Only the new pathspec finds it there,
which makes the fixture observe S1. With the base pathspec, both `guard-run-live` scenarios print
`WRONG: exit 1` (PINNED, the pass copy with S1 reverted).

### The pending row (S4)

The pending list's header names the arming build of every leg row: dWitnessedBar, which owns the
gate-leg kind, `tools/playbook/core-pending.txt:4`. The four kit self-test legs beside this one in
`tools/gate-legs.json` are `tier2-review self-test`, `unattended-build self-test`,
`review-join self-test` and `review-replay selftest`. Each of them has a `dWitnessedBar` pending
row, `tools/playbook/core-pending.txt:137`, and none has `enforces`. None of the 25 legs that have
`enforces` is a kit self-test (PINNED, a read of the manifest). The row goes between
`review-join self-test` and `review-replay selftest`, in manifest order. The list is shrink-only
once seeded, but a new leg has needed a new row before: PLAY-dOrderedCharter-39 added
`agent-instructions wiring` at `ee40561c9`. TOOL-dFairHearing-16 shipped the leg. It is not the
leg's arming build, because the header gives that role to the owner of the gate-leg kind.

### What it does not check

The guard now reads every file named `unattended.sh` at HEAD that declares `PHASES_TERMINAL`, not
only one under a directory named `unattended`. This adds no admission path. The base pathspec
already matched at any depth, so a committed decoy cost the same before. A second declaration with a
different set still refuses as `not one set of phase tokens`. The ban does not check that a file
name is unique to one kit. A future kit shipping its own `unattended.sh` would join the guard's
read.

### Inventory

Nothing is minted.

### Files touched (estimate)

- `tools/policy/guard.py` (S1)
- `tools/policy/check_policy.py` (S2)
- `tools/policy/README.md` (S3)
- `tools/playbook/core-pending.txt` (S4)

## 5. Acceptance criteria

| Leg | Criteria |
|---|---|
| `install-prefix (shipped surface)` | AC1 |
| `policy fixtures` | AC2, AC3 |
| `core meta-check` | AC4 |

- **AC1** — When `bash tools/check-install-prefix.sh` runs over the tree after the pass, it exits 0
  and its last line is
  `install-prefix: clean — 508 tracked file(s) graded, 7 render(s) left out as matching their template, 0 kit-path spelling(s) on 0 line(s)`.
  At the base it exits 1, names the three hits of section 4, and its summary opens
  `install-prefix: RED`.
  Red when: any of the three files still spells the driver under its kit segment.
  figure: PINNED, the counter's own Python over the pass copy at `1f82d4bdc`.
  permission: the main loop runs it; a role agent's scratch guard refuses this leg.
- **AC2** — When `python tools/policy/check_policy.py --fixture guard-run-live` runs after the pass,
  it exits 0, prints no line holding `WRONG`, and its last line is
  `policy-fixture: 80 assertion(s) executed · 0 wrong`.
  Red when: the guard still greps under the kit segment, so the fixture's driver goes unread and
  both scenarios exit 1.
  figure: PINNED, the case over the pass copy, and over that copy with S1 reverted, at `1f82d4bdc`.
- **AC3** — When `python tools/policy/check_policy.py --fixture guard-run-terminal` runs after the
  pass, it exits 0, prints no line holding `WRONG`, and its last line is
  `policy-fixture: 81 assertion(s) executed · 0 wrong`.
  Red when: the guard still greps under the kit segment, so the landed and aborted scenarios refuse
  for a missing driver and not for a terminal phase.
  figure: PINNED, the case over the pass copy, and over that copy with S1 reverted, at `1f82d4bdc`.
- **AC4** — When `python tools/playbook/core.py meta-check` runs over the tree after the pass, it
  exits 0, prints no line opening `core: red`, and prints
  `core: pending · principle 36 · practice 40 · leg 146 · kind 13` and
  `core: meta-check · green · 42 principles, 171 legs, 17 kinds · core.bypass with-hooks-report`. At
  the base it exits 1 and prints the red section 4 quotes.
  Red when: the row is missing, misspells the leg's name, or is not three TAB-separated cells.
  figure: PINNED, `run_meta_check` over the pass copy at `1f82d4bdc`.
  permission: the main loop runs it, as for AC1.

## 6. Gates

`install-prefix (shipped surface)` · `core meta-check` · `policy fixtures` · `govkit acceptance matrix` · `playbook render selftest` · `spec tokens (a spec's own names resolve)`

The guarded legs on the line are those the four touched files trip. `policy fixtures` comes from
`tools/policy/`, and `govkit acceptance matrix` and `playbook render selftest` from
`tools/playbook/` (DERIVED, the spec-token check's `--legs-for` over the four paths). The two red
legs carry no guard and run on every change.

## 7. Open questions

none

## 8. Revision log

- rev-1 · 2026-11-12 · initial draft, from
  `2026-11-12-prompt-PLAY-dOrderedCharter-86-spec-brief.md`. The brief's two options for the
  meta-check red resolved by the pending list's own header: a pending leg row, armed by
  dWitnessedBar. The ban's remedy is the file-name pathspec, because no drained token fits a glob
  that reads every depth.

## 9. Reuse audit

This unit extends existing seams and adds no mechanism. The guard keeps its own HEAD-only
`git grep`. The fixture keeps its literal layout. The pending list takes one more row of the shape
its siblings use, which the meta-check's message names as the remedy, `tools/playbook/core.py@854477bd:327`.
No existing seam fits a sibling-kit lookup at HEAD. `resolve_kit_dir` answers from the working
tree's receipt and probes, `tools/lib/resolve_kit_dir.py@00b26e94:18`, so it would break the guard's rule
that it reads HEAD alone.

Recall terms used:
`install-prefix ban kit segment drained token resolve_kit_dir PHASES_TERMINAL run mandate guard HEAD glob core-pending meta-check enforces arming build gate-leg kind`
