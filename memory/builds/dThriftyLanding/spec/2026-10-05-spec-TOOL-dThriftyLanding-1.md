# TOOL-dThriftyLanding-1 — the runner skips a leg whose declared doc reads did not move

**Status:** CLOSED · rev-1 · 2026-10-05 · node d · Tier-2 · base c3ef6742 · streams tooling · order 1

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-05-build-TOOL-dThriftyLanding-1-1-acceptance-ledger.md](../build/2026-10-05-build-TOOL-dThriftyLanding-1-1-acceptance-ledger.md) | journal | — |
| [2026-10-05-prompt-TOOL-dThriftyLanding-1-0-run-mandate.md](../prompts/2026-10-05-prompt-TOOL-dThriftyLanding-1-0-run-mandate.md) | journal | — |
| [2026-10-05-prompt-TOOL-dThriftyLanding-1-1-build-brief.md](../prompts/2026-10-05-prompt-TOOL-dThriftyLanding-1-1-build-brief.md) | journal | — |

<!-- /gen:spec-records -->

## 1. Goal

A leg in `tools/gate-legs.json` declares nothing about which non-code files it reads, so the runner
cannot tell a leg a doc edit can move from one it cannot. This unit gives a leg an optional
`doc_reads` list, and gives the runner a docs mode, `GATE_DOCS_BASE=<sha>`, in which a leg that
declares `doc_reads` runs only when one of those paths moved since that sha. The hook that sets the
mode is `TOOL-dThriftyLanding-3`; this unit is the runner half and stands alone.

## 2. Scope (IN)

- **S1** — The manifest parser carries `doc_reads` as a NINTH row field, appended after `signature`.
  Absent reads as empty; present is the comma-joined list behind a leading `=`, so a declared empty
  list, which means "reads no doc path", is distinct from no declaration. A non-list reads as absent.
  `{prefix}` resolves as it does for a guard. Observed by AC1 and AC2.
- **S2** — `GATE_DOCS_BASE` resolves through `git rev-parse --verify`. Resolved, and with `GATE_FULL`
  unset, the guard pass decides each leg that is not held and declares `doc_reads` by those paths
  alone: it runs when a path moved between that sha and the working tree, or when any commit in
  `<sha>..HEAD` touched one. A declared empty list skips. Unresolved, the mode is off and the runner
  says so on stderr. A leg that declares nothing keeps today's guard rule. Observed by AC1 to AC4.
- **S3** — A docs skip is reported as `GATE skip  <leg>  (docs-only: no path it reads moved)`, keeps
  the two-space tail contract, and counts in `skips`. The full-green stamp, which requires zero
  skips, is therefore never written by a docs run. Observed by AC1 and AC5.
- **S4** — The canary's manifest key-set pin, arm 1a of `run-gates.test.sh`, admits `doc_reads`, and
  arm 1b's tracked-path rule covers every `doc_reads` element: one that names no tracked path would
  skip its leg on every doc push. Observed by AC6.
- **S5** — `KIT_RUN_GATES_VERSION` moves to 1.25, the floor the deployer reads in
  `TOOL-dThriftyLanding-4`. Observed by AC7.

## 3. Non-goals (OUT)

- Which push is doc-only, and who may set `GATE_DOCS_BASE` at the boundary: `TOOL-dThriftyLanding-3`.
- Any leg's actual `doc_reads` value: `TOOL-dThriftyLanding-5`.
- A change to how `guard` is evaluated. A guard still diffs the run's own base against the tree.
- Held legs: a held leg stays held under the docs mode, as under every mode.

### Edges

- **hands-off** `TOOL-dThriftyLanding-3` — the hook sets `GATE_DOCS_BASE` to R on a doc-only push.
- **hands-off** `TOOL-dThriftyLanding-4` — the deployer emits `doc_reads` above runner 1.25.

## 4. Design

### Evidence

Read at base `c3ef6742`. `tools/run-gates/run-gates.sh` parses the manifest in one inline python
program into `\x1e`-separated rows, eight fields, each appended after the last so an older reader is
not misled. The guard pass runs serially before dispatch: it marks a held leg `ondemand`, then calls
`changed` on a guarded leg's pathspecs and marks it `skip`. `changed` returns true under `GATE_FULL`
or with no base. `report_one` prints `GATE skip` and counts `skips`; the stamp block requires
`skips = 0`. The canary pins the key set at arm 1a and the guard tracked-path rule at arm 1b.

### Files touched (estimate)

- `tools/run-gates/run-gates.sh`
- `tools/run-gates/run-gates.test.sh`

### Alternatives rejected

- **Reuse `guard` for the doc push.** A guard must name every path a leg reads, code included; the
  dominant leg reads the whole memory tree and its kit, so a guard broad enough to be correct skips
  nothing on the commonest doc push here. `doc_reads` asks only which DOC paths a leg reads, which is
  the one question a doc-only push poses.
- **Reuse the input-key reuse path, `GATE_REUSE`.** An unguarded leg is keyed on the whole-tree
  fingerprint, which moves on any doc edit, so it reuses nothing on the population this build is for.
- **Skip by chunk.** A chunk names the kind of check, not what it reads: `declarations` holds both
  code-only legs and legs that read every build record.

## 5. Production-readiness checklist

- perf / scale — one `git diff` and at most one `git log` per declaring leg, only in the docs mode.
- security — the mode narrows a run, so `TOOL-dThriftyLanding-3` scrubs it from the boundary's
  environment and sets it itself; nothing here reads it from a file.
- error / empty / loading states — an unresolved base turns the mode off; a failing git call runs
  the leg.
- observability — every docs skip is a named line, and the summary counts it.
- testing — each arm is observed RED against the base runner first.
- migration — none: an undeclared leg is unchanged, and the mode is unset by default.
- user docs — the run-gates README, in `TOOL-dThriftyLanding-6`.
- risks — a `doc_reads` list missing a path its leg reads skips that leg on a doc push until the
  next full bar; the push boundary's lag bound limits that window.

## 6. Acceptance criteria

- **AC1** — When a fixture bar runs with `GATE_DOCS_BASE` at a commit before a change to the fixture's
  notes/a.md, a leg declaring only notes/b.md prints `GATE skip` with `docs-only`, a leg declaring
  the notes/ directory runs, and the summary counts the skip.
  Red when: the base runner runs both, because it reads no `doc_reads`.
- **AC2** — When the same fixture leg declares `doc_reads: []`, it is skipped; with the key removed,
  it runs.
  Red when: an empty list and an absent key read the same.
- **AC3** — When the full-bar flag is also set in the fixture, every leg prints `GATE ok`.
  Red when: the docs mode narrows a run that asked for the whole bar.
- **AC4** — When the doc path moved in a commit inside the range and was restored by a later one,
  the declaring leg prints `GATE ok`.
  Red when: only the net diff is read, so a reverted touch skips the leg.
- **AC5** — When a docs run is green, `gate-full-green` is not rewritten.
  Red when: a narrowed run stamps a full green.
- **AC6** — When the canary runs over a manifest whose `doc_reads` names an untracked path, arm 1b
  fails naming the leg; over a manifest carrying a valid `doc_reads`, arm 1a passes.
  Red when: the key-set pin refuses the new key, or an untracked doc path passes.
- **AC7** — When `grep -n '^KIT_RUN_GATES_VERSION=' tools/run-gates/run-gates.sh` runs, it prints
  `1.25`, and the `kit version markers` leg passes.
  Red when: the shipped runner moved and its version did not.

## 7. Gates

`run-gates canary` · `run-gates evidence` · `kit version markers` · `kit epoch (shipped bytes move, the version moves)` · `spec tokens (a spec's own names resolve)`

New arm: tools/run-gates/run-gates.test.sh · a manifest leg with `doc_reads` under `GATE_DOCS_BASE`, run by the base runner · none

## 8. Open questions

none

## 9. Revision log

- rev-1 · 2026-10-05 · initial draft, from the owner's prompt and the runner's guard pass at base.

## 10. Reuse audit

The seam extended is the runner's serial guard pass and its row parser, the shape `subject` and
`signature` were added in. `python tools/codebase-map/reuse_lookup.py "scope the push-boundary bar to
the legs a doc-only diff can affect"` printed `unscanned layers: .sh` and named the run-gates seam
`KITDIR`/`LEGS_FILE` and its decisions, `TOOL-aPacedTurnstile-1` onward. The recall query returned
the push-boundary specs that built the bounded obligation and the open ask `TOOL-aTimedTurnstile-2`,
which asked for guards to diff-scope the bar and records that they landed for few legs.

Recall terms used: pre-push GATE_FULL scoped gate full green stamp guard lag bound records-only landing push-main.sh leg manifest merge second parent
