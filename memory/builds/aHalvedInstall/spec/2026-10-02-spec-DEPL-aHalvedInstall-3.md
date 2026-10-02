# DEPL-aHalvedInstall-3 — every kit with an adopter decides whether `update` re-renders it

**Status:** OPEN · rev-1 · 2026-10-02 · node a · Tier-1 · base cd90f7fa · streams deployer · order 3

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-02-prompt-DEPL-aHalvedInstall-3-2-build-brief.md](../prompts/2026-10-02-prompt-DEPL-aHalvedInstall-3-2-build-brief.md) | journal | — |

<!-- /gen:spec-records -->

## 1. Goal

`playbook-render`'s adopter writes the charter region from the engine's bytes, and its `[check]`
compares that region against a fresh render. It declares no `[[regenerate]]`, so every renderer
change lands, the region goes one vintage stale, the check reds and `update` rolls the kit back — at
every adopter, on every renderer change. Selfcheck's 3b-ii arm requires `[[regenerate]]` only of a
kit shipping a `rendered` ROW, and this kit renders through its adopter alone, so it was outside the
population. This unit gives `playbook-render` its block and widens the arm: every descriptor with a
non-empty `[adopt].argv` declares `[[regenerate]]` or states in `[adopt] why_no_regenerate` why an
update never needs to re-run it.

## 2. Scope (IN)

- **S1** — `tools/playbook/kit.toml` declares `[[regenerate]]` with the adopter's own write argv,
  `adopt-playbook.sh --target .`, and `writes = ["AGENTS.md"]` so a rollback restores the region.
  Observed by AC1 and AC2.
- **S2** — A selfcheck arm beside 3b-ii in `tools/govkit/govkit.py`: a descriptor whose
  `[adopt].argv` is non-empty and that declares neither `[[regenerate]]` nor a non-blank
  `[adopt] why_no_regenerate` is a finding naming the entry. Observed by AC3.
- **S3** — Each of the six descriptors the arm reds at base states its reason: `agent-instructions`,
  `codebase-map`, `agent-cap`, `process-monitor`, `run-gates` and `settings-merge`. Each reason is
  read from that adopter, not assumed. Observed by AC4.
- **S4** — The version of every kit whose shipped bytes move is bumped where `govkit epoch` names it.
  Observed by AC5.

## 3. Non-goals (OUT)

- The arm does not check that a declared argv re-renders anything; `update`'s outcome probes and the
  kit's `[check]` own that, as 3b-ii's header already says of its own half.
- No change to `update`'s handling of a kit without a block: it already runs a declared block and
  declines a `rendered`-row kit without one.

### Edges

none

## 4. Design

### Evidence

Read at base `cd90f7fa`. Seven descriptors carry a non-empty `[adopt].argv` and no `[[regenerate]]`.
`render_playbook.py`'s write path is idempotent: it re-renders the `gov:playbook` region and writes
it, whatever the file held. The others, from their own headers: `adopt-process-monitor.sh` and
`adopt-run-gates.sh` write nothing; `adopt-agent-instructions.sh` writes `@AGENTS.md` pointer
wiring, which no engine byte derives; `adopt-codebase-map.sh --scaffold` seeds a project conf once;
`settings-merge.py` merges hook fragments into settings, which `update`'s fragment step already
re-runs for a landed fragment.

### Files touched (estimate)

- `tools/govkit/govkit.py`
- `tools/playbook/kit.toml`
- `tools/agent-instructions/kit.toml`
- `tools/codebase-map/kit.toml`
- `tools/hooks/kit.toml`
- `tools/process-monitor/kit.toml`
- `tools/run-gates/kit.toml`
- `tools/govkit/entries/settings-merge.kit.toml`

### Alternatives rejected

- **Widening 3b-ii's predicate to "has a `[check]` argv".** It would miss a kit whose stale render
  reds a gate leg rather than its check, and it still guesses at a fact only the kit's author knows.
  A declared absence is the repo's own idiom: `[check] none` and `why_no_adopter`.

## 5. Production-readiness checklist

- security — N/A: descriptor data and a selfcheck arm.
- perf / scale — `update` now runs one more adopter argv for a target holding `playbook-render`.
- error / empty / loading states — a render refusal goes through the regenerate's existing outcome
  handling and is named with its stderr.
- observability — the arm notes how many adopter-bearing descriptors declare each answer.
- risks — a target with no `.governance/deploy.toml` makes the adopter refuse; `update` only runs
  over an installed target, which has one.
- testing — the arm observed red at base on all seven, then on one staged blank reason.
- migration — none.
- user docs — the playbook kit README names the regenerate.

## 6. Acceptance criteria

- **AC1** — When `python tools/govkit/govkit.py selfcheck` runs, it names no `playbook-render`
  finding, and `tools/playbook/kit.toml` carries a `[[regenerate]]` block.
  Red when: the block is removed, which S2's arm reds.
- **AC2** — When `bash tools/playbook/adopt-playbook.sh --target .` runs twice over an adopted
  fixture, the second run leaves the charter byte-identical.
  Red when: the write path appends rather than replaces its region.
- **AC3** — When selfcheck runs at base descriptors with the arm added, it names seven entries.
  Red when: the arm reads `[check]` rather than `[adopt]`, and names a different set.
- **AC4** — When `python tools/govkit/govkit.py selfcheck` runs with every reason stated, it names none; with one reason blanked, it
  names that entry.
  Red when: a whitespace-only reason is accepted.
- **AC5** — When `python tools/govkit/govkit.py epoch` runs at the pass's commit, it reports no
  unbumped move.
  Red when: a touched kit's version marker is left.

## 7. Gates

`govkit selfcheck` · `kit epoch (shipped bytes move, the version moves)` · `playbook render selftest` · `playbook render wiring` · `govkit selftest` · `govkit acceptance matrix` · `govkit refusal join` · `recall floor arms` · `agent-cap self-test` · `scratch-guard self-test` · `verifier fan-out self-test` · `review-join self-test` · `hook destinations self-test` · `agent-instructions self-test` · `codebase-map kit selftest` · `codebase-map gate coverage` · `codebase-map adopter e2e`

New arm: tools/govkit/govkit.py · a descriptor with an adopter and neither answer · none

## 8. Open questions

none

## 9. Revision log

- rev-1 · 2026-10-02 · initial draft, from the owner's second observation and the descriptors at base.

## 10. Reuse audit

`python tools/codebase-map/reuse_lookup.py "a kit whose adopter re-renders declares a regenerate step"`
ranked name-stem neighbours only and printed `unscanned layers: .sh`. The seam extended is
selfcheck's 3b-ii arm and its decision record TOOL-bQuiltedLantern-1, which closed the rendered-ROW
population; this unit closes the adopter-only population beside it. The recall probe also returned
TOOL-dRetiredFork-29, whose measured rollbacks at two adopters are the same mechanism.

Recall terms used: govkit update conflict rollback regenerate rendered vintage stale partial install hole discharge absent key

The question passed with them: "why does govkit update leave a kit half-installed when one row conflicts, and why does a renderer change roll back a kit".
