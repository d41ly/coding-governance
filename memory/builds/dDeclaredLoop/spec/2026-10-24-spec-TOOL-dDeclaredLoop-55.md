# TOOL-dDeclaredLoop-55 — the `loop termination` leg declares no guard, so no input it reads can skip it

**Status:** CLOSED · rev-4 · 2026-11-16 · node d · Tier-2 · base ed497191 · streams tooling · order 35 · advances TOOL-dDeclaredLoop-35

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-24-build-TOOL-dDeclaredLoop-1-agent-ledger.md](../build/2026-10-24-build-TOOL-dDeclaredLoop-1-agent-ledger.md) | journal | TOOL-dDeclaredLoop-1 TOOL-dDeclaredLoop-2 TOOL-dDeclaredLoop-3 TOOL-dDeclaredLoop-4 TOOL-dDeclaredLoop-5 TOOL-dDeclaredLoop-6 TOOL-dDeclaredLoop-7 TOOL-dDeclaredLoop-8 TOOL-dDeclaredLoop-9 TOOL-dDeclaredLoop-10 TOOL-dDeclaredLoop-11 TOOL-dDeclaredLoop-12 TOOL-dDeclaredLoop-13 TOOL-dDeclaredLoop-14 TOOL-dDeclaredLoop-15 TOOL-dDeclaredLoop-16 TOOL-dDeclaredLoop-17 TOOL-dDeclaredLoop-18 TOOL-dDeclaredLoop-19 TOOL-dDeclaredLoop-20 TOOL-dDeclaredLoop-21 TOOL-dDeclaredLoop-22 TOOL-dDeclaredLoop-23 TOOL-dDeclaredLoop-24 TOOL-dDeclaredLoop-25 TOOL-dDeclaredLoop-26 TOOL-dDeclaredLoop-27 TOOL-dDeclaredLoop-28 TOOL-dDeclaredLoop-29 TOOL-dDeclaredLoop-30 TOOL-dDeclaredLoop-31 TOOL-dDeclaredLoop-32 TOOL-dDeclaredLoop-33 TOOL-dDeclaredLoop-34 TOOL-dDeclaredLoop-36 TOOL-dDeclaredLoop-37 TOOL-dDeclaredLoop-38 TOOL-dDeclaredLoop-39 TOOL-dDeclaredLoop-40 TOOL-dDeclaredLoop-41 TOOL-dDeclaredLoop-42 TOOL-dDeclaredLoop-43 TOOL-dDeclaredLoop-44 TOOL-dDeclaredLoop-45 TOOL-dDeclaredLoop-46 TOOL-dDeclaredLoop-47 TOOL-dDeclaredLoop-48 TOOL-dDeclaredLoop-49 TOOL-dDeclaredLoop-50 TOOL-dDeclaredLoop-51 TOOL-dDeclaredLoop-52 TOOL-dDeclaredLoop-53 TOOL-dDeclaredLoop-54 TOOL-dDeclaredLoop-56 TOOL-dDeclaredLoop-57 TOOL-dDeclaredLoop-58 TOOL-dDeclaredLoop-59 TOOL-dDeclaredLoop-60 TOOL-dDeclaredLoop-61 TOOL-dDeclaredLoop-62 TOOL-dDeclaredLoop-63 TOOL-dDeclaredLoop-64 TOOL-dDeclaredLoop-65 TOOL-dDeclaredLoop-66 TOOL-dDeclaredLoop-67 TOOL-dDeclaredLoop-68 TOOL-dDeclaredLoop-69 TOOL-dDeclaredLoop-70 TOOL-dDeclaredLoop-71 TOOL-dDeclaredLoop-72 TOOL-dDeclaredLoop-73 TOOL-dDeclaredLoop-74 TOOL-dDeclaredLoop-75 TOOL-dDeclaredLoop-76 TOOL-dDeclaredLoop-77 TOOL-dDeclaredLoop-78 TOOL-dDeclaredLoop-79 TOOL-dDeclaredLoop-80 TOOL-dDeclaredLoop-81 TOOL-dDeclaredLoop-82 TOOL-dDeclaredLoop-83 TOOL-dDeclaredLoop-84 TOOL-dDeclaredLoop-85 TOOL-dDeclaredLoop-86 TOOL-dDeclaredLoop-87 TOOL-dDeclaredLoop-88 TOOL-dDeclaredLoop-89 TOOL-dDeclaredLoop-90 TOOL-dDeclaredLoop-91 TOOL-dDeclaredLoop-92 TOOL-dDeclaredLoop-93 TOOL-dDeclaredLoop-94 TOOL-dDeclaredLoop-95 TOOL-dDeclaredLoop-96 TOOL-dDeclaredLoop-97 TOOL-dDeclaredLoop-98 TOOL-dDeclaredLoop-99 TOOL-dDeclaredLoop-100 TOOL-dDeclaredLoop-112 |
| [2026-10-24-build-TOOL-dDeclaredLoop-36-promoted-fix-return.md](../build/2026-10-24-build-TOOL-dDeclaredLoop-36-promoted-fix-return.md) | research | TOOL-dDeclaredLoop-36 TOOL-dDeclaredLoop-37 TOOL-dDeclaredLoop-38 TOOL-dDeclaredLoop-39 TOOL-dDeclaredLoop-40 TOOL-dDeclaredLoop-41 TOOL-dDeclaredLoop-42 TOOL-dDeclaredLoop-43 TOOL-dDeclaredLoop-44 TOOL-dDeclaredLoop-45 TOOL-dDeclaredLoop-46 TOOL-dDeclaredLoop-47 TOOL-dDeclaredLoop-48 TOOL-dDeclaredLoop-49 TOOL-dDeclaredLoop-50 TOOL-dDeclaredLoop-51 TOOL-dDeclaredLoop-52 TOOL-dDeclaredLoop-53 TOOL-dDeclaredLoop-54 TOOL-dDeclaredLoop-56 |
| [2026-10-24-build-TOOL-dDeclaredLoop-55-deviation-551.md](../build/2026-10-24-build-TOOL-dDeclaredLoop-55-deviation-551.md) | deviation | — |
| [2026-11-16-build-TOOL-dDeclaredLoop-55-1-acceptance-ledger.md](../build/2026-11-16-build-TOOL-dDeclaredLoop-55-1-acceptance-ledger.md) | journal | — |
| [2026-10-24-prompt-TOOL-dDeclaredLoop-36-promoted-fix-brief.md](../prompts/2026-10-24-prompt-TOOL-dDeclaredLoop-36-promoted-fix-brief.md) | research | TOOL-dDeclaredLoop-36 TOOL-dDeclaredLoop-37 TOOL-dDeclaredLoop-38 TOOL-dDeclaredLoop-39 TOOL-dDeclaredLoop-40 TOOL-dDeclaredLoop-41 TOOL-dDeclaredLoop-42 TOOL-dDeclaredLoop-43 TOOL-dDeclaredLoop-44 TOOL-dDeclaredLoop-45 TOOL-dDeclaredLoop-46 TOOL-dDeclaredLoop-47 TOOL-dDeclaredLoop-48 TOOL-dDeclaredLoop-49 TOOL-dDeclaredLoop-50 TOOL-dDeclaredLoop-51 TOOL-dDeclaredLoop-52 TOOL-dDeclaredLoop-53 TOOL-dDeclaredLoop-54 TOOL-dDeclaredLoop-56 |
| [2026-10-25-prompt-TOOL-dDeclaredLoop-1-dorderedcharter-crosscheck.md](../prompts/2026-10-25-prompt-TOOL-dDeclaredLoop-1-dorderedcharter-crosscheck.md) | research | TOOL-dDeclaredLoop-1 TOOL-dDeclaredLoop-2 TOOL-dDeclaredLoop-3 TOOL-dDeclaredLoop-4 TOOL-dDeclaredLoop-5 TOOL-dDeclaredLoop-6 TOOL-dDeclaredLoop-12 TOOL-dDeclaredLoop-16 TOOL-dDeclaredLoop-17 TOOL-dDeclaredLoop-18 TOOL-dDeclaredLoop-22 TOOL-dDeclaredLoop-24 TOOL-dDeclaredLoop-25 TOOL-dDeclaredLoop-26 TOOL-dDeclaredLoop-27 TOOL-dDeclaredLoop-28 TOOL-dDeclaredLoop-33 TOOL-dDeclaredLoop-34 TOOL-dDeclaredLoop-46 TOOL-dDeclaredLoop-56 |
| [2026-11-16-prompt-TOOL-dDeclaredLoop-55-1-spec-writer.md](../prompts/2026-11-16-prompt-TOOL-dDeclaredLoop-55-1-spec-writer.md) | journal | — |
| [2026-11-16-prompt-TOOL-dDeclaredLoop-55-build-brief.md](../prompts/2026-11-16-prompt-TOOL-dDeclaredLoop-55-build-brief.md) | journal | — |
| [2026-11-16-prompt-TOOL-dDeclaredLoop-55-reground-brief.md](../prompts/2026-11-16-prompt-TOOL-dDeclaredLoop-55-reground-brief.md) | research | — |
| [2026-10-24-review-TOOL-dDeclaredLoop-36-spec-audit.md](../reviews/2026-10-24-review-TOOL-dDeclaredLoop-36-spec-audit.md) | spec-audit | TOOL-dDeclaredLoop-36 TOOL-dDeclaredLoop-37 TOOL-dDeclaredLoop-38 TOOL-dDeclaredLoop-39 TOOL-dDeclaredLoop-40 TOOL-dDeclaredLoop-41 TOOL-dDeclaredLoop-42 TOOL-dDeclaredLoop-43 TOOL-dDeclaredLoop-44 TOOL-dDeclaredLoop-45 TOOL-dDeclaredLoop-46 TOOL-dDeclaredLoop-47 TOOL-dDeclaredLoop-48 TOOL-dDeclaredLoop-49 TOOL-dDeclaredLoop-50 TOOL-dDeclaredLoop-51 TOOL-dDeclaredLoop-52 TOOL-dDeclaredLoop-53 TOOL-dDeclaredLoop-54 TOOL-dDeclaredLoop-56 |
| [2026-11-17-review-TOOL-dDeclaredLoop-1-closing-diff-round1.md](../reviews/2026-11-17-review-TOOL-dDeclaredLoop-1-closing-diff-round1.md) | diff-review | TOOL-dDeclaredLoop-1 TOOL-dDeclaredLoop-2 TOOL-dDeclaredLoop-3 TOOL-dDeclaredLoop-4 TOOL-dDeclaredLoop-5 TOOL-dDeclaredLoop-6 TOOL-dDeclaredLoop-7 TOOL-dDeclaredLoop-8 TOOL-dDeclaredLoop-9 TOOL-dDeclaredLoop-10 TOOL-dDeclaredLoop-11 TOOL-dDeclaredLoop-12 TOOL-dDeclaredLoop-13 TOOL-dDeclaredLoop-14 TOOL-dDeclaredLoop-15 TOOL-dDeclaredLoop-16 TOOL-dDeclaredLoop-17 TOOL-dDeclaredLoop-18 TOOL-dDeclaredLoop-19 TOOL-dDeclaredLoop-20 TOOL-dDeclaredLoop-21 TOOL-dDeclaredLoop-22 TOOL-dDeclaredLoop-23 TOOL-dDeclaredLoop-24 TOOL-dDeclaredLoop-25 TOOL-dDeclaredLoop-26 TOOL-dDeclaredLoop-27 TOOL-dDeclaredLoop-28 TOOL-dDeclaredLoop-29 TOOL-dDeclaredLoop-30 TOOL-dDeclaredLoop-31 TOOL-dDeclaredLoop-32 TOOL-dDeclaredLoop-33 TOOL-dDeclaredLoop-34 TOOL-dDeclaredLoop-36 TOOL-dDeclaredLoop-37 TOOL-dDeclaredLoop-38 TOOL-dDeclaredLoop-39 TOOL-dDeclaredLoop-40 TOOL-dDeclaredLoop-41 TOOL-dDeclaredLoop-42 TOOL-dDeclaredLoop-43 TOOL-dDeclaredLoop-44 TOOL-dDeclaredLoop-45 TOOL-dDeclaredLoop-46 TOOL-dDeclaredLoop-47 TOOL-dDeclaredLoop-48 TOOL-dDeclaredLoop-49 TOOL-dDeclaredLoop-50 TOOL-dDeclaredLoop-51 TOOL-dDeclaredLoop-52 TOOL-dDeclaredLoop-53 TOOL-dDeclaredLoop-54 TOOL-dDeclaredLoop-56 TOOL-dDeclaredLoop-57 TOOL-dDeclaredLoop-58 TOOL-dDeclaredLoop-59 TOOL-dDeclaredLoop-60 TOOL-dDeclaredLoop-61 TOOL-dDeclaredLoop-62 TOOL-dDeclaredLoop-63 TOOL-dDeclaredLoop-64 TOOL-dDeclaredLoop-65 TOOL-dDeclaredLoop-66 TOOL-dDeclaredLoop-67 TOOL-dDeclaredLoop-68 TOOL-dDeclaredLoop-69 TOOL-dDeclaredLoop-70 TOOL-dDeclaredLoop-71 TOOL-dDeclaredLoop-72 TOOL-dDeclaredLoop-73 TOOL-dDeclaredLoop-74 TOOL-dDeclaredLoop-75 TOOL-dDeclaredLoop-76 TOOL-dDeclaredLoop-77 TOOL-dDeclaredLoop-78 TOOL-dDeclaredLoop-79 TOOL-dDeclaredLoop-80 TOOL-dDeclaredLoop-81 TOOL-dDeclaredLoop-82 TOOL-dDeclaredLoop-83 TOOL-dDeclaredLoop-84 TOOL-dDeclaredLoop-85 TOOL-dDeclaredLoop-86 TOOL-dDeclaredLoop-87 TOOL-dDeclaredLoop-88 TOOL-dDeclaredLoop-89 TOOL-dDeclaredLoop-90 TOOL-dDeclaredLoop-91 TOOL-dDeclaredLoop-92 TOOL-dDeclaredLoop-93 TOOL-dDeclaredLoop-94 TOOL-dDeclaredLoop-95 TOOL-dDeclaredLoop-96 TOOL-dDeclaredLoop-97 TOOL-dDeclaredLoop-98 TOOL-dDeclaredLoop-99 TOOL-dDeclaredLoop-100 TOOL-dDeclaredLoop-112 |
| [2026-11-17-review-TOOL-dDeclaredLoop-1-closing-diff-round2.md](../reviews/2026-11-17-review-TOOL-dDeclaredLoop-1-closing-diff-round2.md) | diff-review | TOOL-dDeclaredLoop-1 TOOL-dDeclaredLoop-2 TOOL-dDeclaredLoop-3 TOOL-dDeclaredLoop-4 TOOL-dDeclaredLoop-5 TOOL-dDeclaredLoop-6 TOOL-dDeclaredLoop-7 TOOL-dDeclaredLoop-8 TOOL-dDeclaredLoop-9 TOOL-dDeclaredLoop-10 TOOL-dDeclaredLoop-11 TOOL-dDeclaredLoop-12 TOOL-dDeclaredLoop-13 TOOL-dDeclaredLoop-14 TOOL-dDeclaredLoop-15 TOOL-dDeclaredLoop-16 TOOL-dDeclaredLoop-17 TOOL-dDeclaredLoop-18 TOOL-dDeclaredLoop-19 TOOL-dDeclaredLoop-20 TOOL-dDeclaredLoop-21 TOOL-dDeclaredLoop-22 TOOL-dDeclaredLoop-23 TOOL-dDeclaredLoop-24 TOOL-dDeclaredLoop-25 TOOL-dDeclaredLoop-26 TOOL-dDeclaredLoop-27 TOOL-dDeclaredLoop-28 TOOL-dDeclaredLoop-29 TOOL-dDeclaredLoop-30 TOOL-dDeclaredLoop-31 TOOL-dDeclaredLoop-32 TOOL-dDeclaredLoop-33 TOOL-dDeclaredLoop-34 TOOL-dDeclaredLoop-36 TOOL-dDeclaredLoop-37 TOOL-dDeclaredLoop-38 TOOL-dDeclaredLoop-39 TOOL-dDeclaredLoop-40 TOOL-dDeclaredLoop-41 TOOL-dDeclaredLoop-42 TOOL-dDeclaredLoop-43 TOOL-dDeclaredLoop-44 TOOL-dDeclaredLoop-45 TOOL-dDeclaredLoop-46 TOOL-dDeclaredLoop-47 TOOL-dDeclaredLoop-48 TOOL-dDeclaredLoop-49 TOOL-dDeclaredLoop-50 TOOL-dDeclaredLoop-51 TOOL-dDeclaredLoop-52 TOOL-dDeclaredLoop-53 TOOL-dDeclaredLoop-54 TOOL-dDeclaredLoop-56 TOOL-dDeclaredLoop-57 TOOL-dDeclaredLoop-58 TOOL-dDeclaredLoop-59 TOOL-dDeclaredLoop-60 TOOL-dDeclaredLoop-61 TOOL-dDeclaredLoop-62 TOOL-dDeclaredLoop-63 TOOL-dDeclaredLoop-64 TOOL-dDeclaredLoop-65 TOOL-dDeclaredLoop-66 TOOL-dDeclaredLoop-67 TOOL-dDeclaredLoop-68 TOOL-dDeclaredLoop-69 TOOL-dDeclaredLoop-70 TOOL-dDeclaredLoop-71 TOOL-dDeclaredLoop-72 TOOL-dDeclaredLoop-73 TOOL-dDeclaredLoop-74 TOOL-dDeclaredLoop-75 TOOL-dDeclaredLoop-76 TOOL-dDeclaredLoop-77 TOOL-dDeclaredLoop-78 TOOL-dDeclaredLoop-79 TOOL-dDeclaredLoop-80 TOOL-dDeclaredLoop-81 TOOL-dDeclaredLoop-82 TOOL-dDeclaredLoop-83 TOOL-dDeclaredLoop-84 TOOL-dDeclaredLoop-85 TOOL-dDeclaredLoop-86 TOOL-dDeclaredLoop-87 TOOL-dDeclaredLoop-88 TOOL-dDeclaredLoop-89 TOOL-dDeclaredLoop-90 TOOL-dDeclaredLoop-91 TOOL-dDeclaredLoop-92 TOOL-dDeclaredLoop-93 TOOL-dDeclaredLoop-94 TOOL-dDeclaredLoop-95 TOOL-dDeclaredLoop-96 TOOL-dDeclaredLoop-97 TOOL-dDeclaredLoop-98 TOOL-dDeclaredLoop-99 TOOL-dDeclaredLoop-100 TOOL-dDeclaredLoop-112 |

<!-- /gen:spec-records -->

## 1. Goal

The round-1 spec audit (`memory/builds/dDeclaredLoop/reviews/2026-10-24-review-TOOL-dDeclaredLoop-1-spec-audit.md`)
confirmed finding **id 55 at HIGH**, its item **H20**, alone in that item: `TOOL-dDeclaredLoop-33`'s
`loop termination` leg was guarded by `{prefix}/loop/` alone, while the composition it checks reads the
repository's overlay, the scenarios, the policy catalogue and each build's recorded changes, the class
`memory/gotchas/held-suite-guard-misses-a-sibling-kit.md`. A guarded leg's reuse key hashes only its
guards (`tools/run-gates/README.md@16312f6fb579:370`), so an input outside them skips the leg on a
scoped bar or reuses a stale green, and the push certifies termination it never checked. This unit
takes the report's second option, no guard. `TOOL-dDeclaredLoop-33` rev-6 writes its leg on that option
(its S10 and §8 F10), so the row lands with no guard at order 34; this unit, at order 35, writes
nothing and observes that the landed row and the loop kit's descriptor hold the property (§8 F3). It
repairs `TOOL-dDeclaredLoop-33`.

## 2. Scope (IN)

- **S1** — The `loop termination` row of `tools/gate-legs.json`, which `TOOL-dDeclaredLoop-33` S10 lands
  at order 34, carries no `guard` key, so the runner runs it on every bar and keys its reuse on the
  working-tree fingerprint, which covers every tracked input the composition reads; and
  `tools/loop/kit.toml` holds no `[[gate_leg]]` table of that name, the leg being gov's own
  `[[exempt_leg]]` in `tools/govkit/registry.toml` by the same item, so `govkit apply` emits no copy of
  it to an adopter. That unit's committed spec writes both, so this unit's pass writes no byte of either
  and observes them on the tree order 34 leaves (§8 F3). Observed by AC1, AC2.

## 3. Non-goals (OUT)

- Writing the leg's row, its `[[exempt_leg]]` row or the descriptor: `TOOL-dDeclaredLoop-33` S10's, its
  §8 F10 (a) landing them with no guard.
- A guard list enumerating every input: `memory/builds/` alone is touched by nearly every commit, so the
  list would run the leg on almost every bar while depending on a path set that grows with each new input.
- A manifest check comparing each guarded leg's `reads` with its guard, the finding's left-shift: not named
  by any clause of this build; the class is recorded at the close.
- The lasting arm that holds the no-guard property: `TOOL-dDeclaredLoop-67` S31's, at order 38.
- The rule set and the per-level terminal sets: `TOOL-dDeclaredLoop-33` and `-54`.

### Edges

- **consumes-from** `TOOL-dDeclaredLoop-33` — the `loop termination` leg row and its `[[exempt_leg]]` row, which land with no guard and no descriptor table (its S10, §8 F10)
- **hands-off** `TOOL-dDeclaredLoop-67` — the round-2 minors ids 2, 44 and 46: this pass keeps the loop termination leg green; the AC10 clause that unit's S1 rules on and the lasting no-guard arm are scope items of that unit

## 4. Design

### Evidence

- The reuse key: "for a guarded leg the `git ls-files -s` of its guards plus the walk rows under them …
  for an unguarded leg the working-tree fingerprint" (`tools/run-gates/README.md@16312f6fb579:370`), so
  an unguarded leg is never reused across a change to any tracked file; and "what lineage reuse does not
  check: that a reused leg's guard names every input the leg reads" (`@16312f6fb579:399`).
- An absent `guard` key is the unguarded form: the gov canary's no-guard arm for `memory hygiene` tests
  `"guard" in rows[0]` (`tools/run-gates/run-gates.gov.test.sh@40f06044824a:501`), the model
  `TOOL-dDeclaredLoop-67` S31 names for this leg's lasting arm.
- `TOOL-dDeclaredLoop-33` rev-6 S10 writes the leg with no `guard`, as gov's own `[[exempt_leg]]`, and its
  S1 reads the composition through `tools/loop/loop_items.py#read_composed_items`, which composes the
  repository's overlay with gov's rows and joins the rows a build's scenarios activate; through
  `tools/loop/composition.py#read_step_composition`, which resolves a build's pinned composition from its
  moves; through `tools/loop/adapt.py#read_flow_rows`, a build's own flow changes; and its wait rule reads
  the catalogue through `tools/policy/policy.py#derive_bounds`. The overlay, the scenario rows, the change
  records and the catalogue all lie outside `{prefix}/loop/`.
- At the tip `a7b10569` no `loop` row of `tools/gate-legs.json` carries `guard`, the loop descriptor's
  `[[gate_leg]]` tables are `loop definition` and `loop transition tables` alone, and the registry's
  `[[exempt_leg]]` rows hold every other `loop` leg (a `json.load` and `tomllib` probe over the files
  `git show` extracted on 2026-11-16).

### Write set

None. The pass writes no product file; its acceptance ledger line records AC1 and AC2.

### Files touched (estimate)

- none: the pass reads the leg manifest, the loop descriptor and the registry, and writes none of them.

### Alternatives rejected

- **The report's first option, a guard over every path read.** Correct only while the list stays complete,
  and it misses the next input added; no guard cannot miss one.
- **Writing the row here, one order after unit 33.** Unit 33's §8 F10 rejects it: the leg would skip what
  it grades for an order.

## 5. Production-readiness checklist

- security — closes a certification gap at the push, landed by `TOOL-dDeclaredLoop-33` and observed here.
- perf / scale — the leg runs on every bar; its cost and ceiling are `TOOL-dDeclaredLoop-33` §5's.
- error / empty / loading states — AC1 counts the rows, so an absent row is a red, never a pass.
- observability — the runner prints the leg on every bar.
- risks — a slow leg runs on doc-only pushes too; unit 33's ceiling row bounds it.
- testing — AC1 and AC2 as probes on the tree order 34 leaves; no arm is minted, the lasting one being
  `TOOL-dDeclaredLoop-67` S31's.
- migration — none.
- user docs — none; no verb, flag or page moves.

### The sweep: what the change reaches, and what keeps each green

Read on `branch/unattended-declared-loop-d56bf0` at `a7b10569` through `git show`; the probes ran over
files extracted from it; the reuse lookup ran on this worktree's main at `179486e8`, and the
spec-token checker on a scratch index of the tip's tree, where every path this spec names is tracked.
This spec is written on `TOOL-dDeclaredLoop-33`'s committed rev-6 spec (order 34), which
lands the row and the `[[exempt_leg]]` row this unit reads.

| Reached | Readers and populations | What keeps it green |
|---|---|---|
| the `loop termination` row of `tools/gate-legs.json` | the runner's selection and reuse key, `tools/run-gates/py_reads.py`, `tools/run-gates/measure_legs.py`, `tools/govkit/govkit.py`, the spec-token checker's leg join, `run-gates gov canary` | written by `TOOL-dDeclaredLoop-33`; this pass writes no byte of it |
| `tools/loop/kit.toml` | `govkit apply`, `govkit selfcheck`, `govkit selftest` | not edited |
| `tools/govkit/registry.toml` | `govkit selfcheck`, `govkit selftest` | not edited |
| `tools/govkit/subject-pins.tsv`, `tools/govkit/usage.toml`, help anchors | `govkit selftest`, `help page commands` | no leg, verb or flag is minted here |
| the verdict-epoch `DELEGATES` | `tools/memory-tree/check-verdict-epoch.sh` | no delegate module is edited |
| the kickoff manifest's `watch:` line | `memory/guides/SESSION-KICKOFF.md`, `kickoff-manifest ratchet` | `tools/gate-legs.json` is on it, and this pass does not edit it, so no re-stamp is owed |
| the rendered map | `memory/map/generated/`, `codebase-map coverage + freshness` | no code symbol moves |
| the install-prefix ban | `tools/check-install-prefix.sh` | no shipped file is edited |
| `VERB_OFFENDER_PIN` | `lexicon naming predicates` | no function name is minted, so no `--suggest` run is owed |
| `SHARED_RECORDS` in `.unattended.conf` | `memory/DECISIONS.md`, `memory/project/readme-contract.txt` | no decision row is owed: no census, ceiling or contract moves |
| the refusal census and families | `REFUSAL_CEILINGS` and `ARMS_FLOORS` in `.memory-tree.conf`, `tools/unattended/unattended.families.txt`, `tools/memory-tree/check-arms.py` | no shell script is edited; `git diff --name-only <base>.. -- '*.sh'` prints nothing |
| this spec's `### Edges` block | `TOOL-dDeclaredLoop-67` AC21, its §4 table naming `loop termination` for this unit | the hands-off bullet names the loop termination leg |

## 6. Acceptance criteria

- **AC1** — When a `python -c` probe loads `tools/gate-legs.json` with `json.load` on the tree order 34
  leaves, keeps the rows whose `name` is `loop termination` and prints their count and, for each,
  whether it holds `guard`, it prints `1 [False]`: one row of that name, carrying no `guard` key.
  Red when: the row carries a `guard`, so an overlay-only change skips the leg; or no row exists, a
  probe that grades nothing.
- **AC2** — When a `python -c` probe loads `tools/loop/kit.toml` and `tools/govkit/registry.toml` with
  `tomllib` on the same tree and prints the names of the descriptor's `gate_leg` tables equal to `loop
  termination`, then the count of the registry's `exempt_leg` rows of that name, it prints `[] 1`: no
  descriptor table names the leg, and one `[[exempt_leg]]` row does.
  Red when: the descriptor ships the leg, so `govkit apply` emits it, guard and all, to adopters.

## 7. Gates

`run-gates canary` · `run-gates gov canary` · `measure-legs selftest` · `memory hygiene` · `spec tokens (a spec's own names resolve)`

## 8. Open questions

- **F1 — Which binding line does a unit the spec audit promoted carry?** RESOLVED (agent, 2026-10-24,
  delegated): `**Derived:** PLAY-dClosedLoop-2`, rung 3, as `TOOL-dDeclaredLoop-36` §8 F1 records.
  widens: none · relaxes: none
- **F2 — A complete guard, or none?** Options: (a) a guard over every path the composition reads; (b) no
  guard. (a) is complete only until the next input is added and runs on almost every bar anyway. RESOLVED
  (agent, 2026-10-24, delegated): (b), rung 3. widens: none · relaxes: none
- **F3 — What does this unit's pass do once `TOOL-dDeclaredLoop-33` lands the row with no guard?**
  Options: (a) it writes nothing and observes AC1 and AC2 on the tree order 34 leaves, its ledger line
  the record; (b) it takes `TOOL-dDeclaredLoop-67` S31's lasting arm forward to order 35, a sibling's
  scope moved, which a re-ground may not do; (c) the run closes this unit unbuilt, satisfied by unit
  33's landing, a status move outside a spec. (a) keeps the unit, its order and its status, and leaves
  (c) the run's at dispatch. Recommendation (a); the spec body is written on it.
  RESOLVED (agent, 2026-11-16, delegated): (a).

## 9. Revision log

- rev-1 · 2026-10-24 · initial draft, promoted from the round-1 spec audit's id 55 (HIGH, item H20).
- rev-2 · 2026-10-24 · §3 · the Edges block gains the hands-off bullets mirroring the
  consumes-from edges of TOOL-dDeclaredLoop-67, written by the round-2 spec audit's disposal; nothing else moved.
- rev-3 · 2026-11-16 · §1 · S1 · §3 · §4 · §5 · AC1 · AC2 · §8 F3 · §10 · re-grounded at the tip of
  branch/unattended-declared-loop-d56bf0 (`a7b10569`), per the brief
  prompts/2026-11-16-prompt-TOOL-dDeclaredLoop-55-1-spec-writer.md: TOOL-dDeclaredLoop-33 rev-6 lands the
  row with no guard and the leg as gov's own exempt row with no descriptor table, so this pass writes
  nothing and observes (F3); AC2 reads the descriptor's absent table; the review record's path; the
  README citation blob-pinned; §5's sweep.
- rev-4 · 2026-11-16 · §8 F3 · the fork the body is written on carries its resolution mark, (a); nothing else
  moves.

## 10. Reuse audit

The seam is the runner's own unguarded-leg rule, documented at `tools/run-gates/README.md@16312f6fb579:370`;
this unit adds nothing to it. `python tools/codebase-map/reuse_lookup.py "a gate leg guard covering every
path it reads"`, re-run on this worktree's main on 2026-11-16, ranked `read_text`, `read`, `read_bytes`,
`legs` and `leg`, none a guard-completeness check, so no existing seam fits one and this unit needs none.

Recall terms used: loop termination leg guard reuse key working-tree fingerprint reads overlay scenario catalogue sibling kit exempt_leg
