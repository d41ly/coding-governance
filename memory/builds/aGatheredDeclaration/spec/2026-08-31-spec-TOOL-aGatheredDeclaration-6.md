# TOOL-aGatheredDeclaration-6 — every reader moves, and the second entry point closes

**Status:** OPEN · rev-1 · 2026-08-31 · node a · Tier-2 · base 44734f15 · streams tooling · order 6

<!-- gen:spec-records -->

*No record names this unit.*

<!-- /gen:spec-records -->

## 1. Goal

Move every reader of `tools/gate-legs.json` onto `gate-legs.toml`, retire the JSON, and make
`tools/run-gates/run-gates.sh` the SINGLE gate entry point by folding the second one into it. Until
this lands, unit 2's dual-format branch is carrying a format nobody should still be reading.

## 2. Scope (IN)

- **S1** — `tools/govkit/govkit.py`: the emitter writes `gate-legs.toml` and the selfcheck joins
  `[[gate_leg]]` descriptor rows against it. The `[gate_runner_seed]` block gains the new file name.
- **S2** — `.githooks/pre-push`: reads the TOML for its manifest-moved test and its blob compare.
  This is also where `TOOL-aBoundedCeiling-7` is fixed — the hook hardcodes `tools/gate-legs.json`
  and `tools/run-gates/gate-fingerprint.sh` while the install prefix is configurable, so a target at
  another prefix has a hook that cannot find its own gate.
- **S3** — `tools/drift-audit/drift_signals.py` and its `.template.py` twin.
- **S4** — `tools/codebase-map/map_extractors.py`, whose `_gate_legs` inventory keys the map's
  `gate-legs` population.
- **S5** — the SECOND ENTRY POINT closes: `tools/unattended/run-unattended-gates.sh` becomes a thin
  call into `run-gates.sh --leg`, naming the seven legs it holds, rather than a parallel dispatcher.
- **S6** — the carriers that NAME the entry point to a session: `AGENTS.md`'s merge-bar section,
  `coding-governance-agents.template.md`, and whatever `tools/playbook/` renders from them. The
  command block gains the sharding verbs and drops nothing.
- **S7** — `tools/gate-legs.json` is deleted, and unit 2's dual-format branch keeps its JSON arm for
  adopters while gov itself carries no JSON. The deprecation line becomes the only thing pointing at
  it.
- **S8** — the `run-gates` map dossier at `memory/map/features/run-gates.md` is refreshed: its
  `[paths]` globs and its `[claims]` gain the new file, which the map's coverage gate requires in
  the same commit as the claim edit.

## 3. Non-goals (OUT)

- Removing the JSON arm from the loader. Adopters upgrade on their own schedule; unit 7 is the tool,
  not a deadline.
- Changing what any of these readers CONCLUDES. Each reads a different file and reaches the same
  verdict; a reader whose behaviour changes here is a defect, not a feature.
- Fixing `TOOL-aBoundedCeiling-7`'s sibling problems. Only the two hardcoded paths this unit already
  has to touch are in scope; the row stays open for the rest if any remain.

## 4. Design

### Inventory

| reader | what it reads it for | change |
|---|---|---|
| `run-gates.sh` | dispatch | done in unit 2 |
| `govkit.py` | emit + selfcheck join | S1 |
| `.githooks/pre-push` | manifest-moved force, blob compare | S2 |
| `drift_signals.py` (+ template) | dead-path signal over leg argv | S3 |
| `map_extractors.py` | the `gate-legs` inventory | S4 |
| `run-unattended-gates.sh` | its own dispatch | S5, folded away |

### Migration

Ordered, and the order matters: S1 through S4 land first with the JSON still present, so each
reader is proven against a tree where both files exist and agree. S7 deletes the JSON last. A reader
moved and a file deleted in one commit gives a red no bisect can localise.

### Rollout

S5 is the only behaviour change a person will notice: `bash tools/unattended/run-unattended-gates.sh`
keeps its name and its output shape and stops being a second dispatcher. Its seven leg names move
into the declaration as `opt_in = true` rows carrying the 2026-08-23 owner ruling as their comment.

### Files touched (estimate)

`tools/govkit/govkit.py` · `tools/govkit/registry.toml` · `.githooks/pre-push` ·
`.githooks/pre-push.test.sh` · `tools/drift-audit/drift_signals.py` + `.template.py` ·
`tools/codebase-map/map_extractors.py` · `tools/unattended/run-unattended-gates.sh` · `AGENTS.md` ·
`coding-governance-agents.template.md` · `memory/map/features/run-gates.md` · `tools/gate-legs.json`
(deleted) · the affected suites.

### Alternatives rejected

**Move every reader in unit 2's commit.** One commit touching the runner, the deployer, the hook,
two audits and the charter is a diff no closing review can localise a finding in. The dual-format
branch exists precisely so this can be a second landing.

## 5. Production-readiness checklist

- security — `.githooks/pre-push` is a trust boundary and S2 changes what it reads. Its selftest
  covers the classification arms and must still pass unchanged.
- perf / scale — S5 removes a duplicate dispatcher. No other reader is on a hot path.
- a11y, i18n — N/A.
- error / empty / loading states — each moved reader keeps its existing refusal for an absent or
  malformed manifest; a reader that silently tolerated an absent JSON must not silently tolerate an
  absent TOML.
- observability — N/A beyond what unit 3 adds.
- risks — a partially moved reader set is the whole risk, and the ordered migration is the answer.
  `check-dead-paths.sh` is the backstop: a carrier still naming the deleted JSON reds.
- testing + left-shift gates — each moved reader's own suite, plus the dead-path leg.
- migration / rollback — revert S7 first; the loader's JSON arm makes that sufficient.
- user docs — S6.

## 6. Acceptance criteria

- **AC1** — When `python tools/govkit/govkit.py` emits a target's manifest, the file written is
  `<prefix>/gate-legs.toml` and its rows match the selected descriptors' `[[gate_leg]]` blocks,
  asserted in `tools/govkit/selftest.py`.
- **AC2** — When `.githooks/pre-push` runs in a target installed at a prefix other than `tools`, it
  resolves the manifest and the fingerprint helper at that prefix, asserted in
  `.githooks/pre-push.test.sh` with a scratch repo installed at `scripts/`. Observed RED first —
  this is `TOOL-aBoundedCeiling-7`.
- **AC3** — When `python tools/drift-audit/drift_report.py` runs, its gate-legs signal reports the
  same population from the TOML that it reported from the JSON, asserted by running both at the
  commit where both files exist.
- **AC4** — When `python tools/codebase-map/reuse_lookup.py` runs, the `gate-legs` inventory key
  count is unchanged across the format move, asserted the same way.
- **AC5** — When `bash tools/unattended/run-unattended-gates.sh` runs, it dispatches through
  `run-gates.sh --leg` and its seven leg names appear in the runner's own summary, asserted by
  grepping for the runner's report tail rather than for a message this script prints.
- **AC6** — When `bash tools/check-dead-paths.sh` runs after S7, no carrier names
  `tools/gate-legs.json`, asserted by the leg's own green.
- **AC7** — When `bash tools/run-gates/run-gates.sh` runs on this tree with no JSON present, it is
  GREEN and its leg count is unchanged.
- **AC8** — When `python tools/codebase-map/check_map.py` runs, the `run-gates` dossier claims the
  new file and no unclaimed key remains, asserted by the map coverage leg.

## 7. Gates

`run-gates canary` · `run-gates gov canary` · `govkit selfcheck` · `pre-push hook selftest` ·
`drift-audit selftest` · `codebase-map coverage` · `dead paths` · `unattended kit gate` ·
`check-wiring`. No new leg.

## 8. Open questions

- **F1 — does `run-unattended-gates.sh` survive at all, or is `--leg` enough?** With unit 3 landed,
  `bash tools/run-gates/run-gates.sh --leg "<name>" --leg "<name>" …` is the same command with the
  names spelled out. Keeping the wrapper is a named entry point an adopter's docs can point at;
  deleting it is one fewer thing. Recommendation: keep it, because it is what the kit's own
  descriptor names as the compensating check for legs held off the bar, and a compensating check
  that becomes a spelled-out argument list is one nobody runs.
  RESOLVED (agent, 2026-08-31, delegated): keep it as a thin wrapper. It satisfies the stated
  requirement — one dispatcher — while keeping the named check the exemption depends on.

## 9. Revision log

- rev-1 · 2026-08-31 · initial draft.

## 10. Reuse audit

No new seam. Every change here is at a reader that already exists and already resolves its own path;
the work is changing what each resolves TO. The one place a seam is being CREATED rather than
extended is S5, and it consumes unit 3's `--leg`, which is why the two are separate units in the
same build rather than one.

The reader inventory in §4 was derived by grepping `gate-legs` across the tree, which is the
exhaustive form of the question a map probe answers by ranking. **The grep is the evidence here and
the probe is not**, stated so the difference is visible rather than implied.

The recall probe run for `TOOL-aGatheredDeclaration-7` reaches this unit and changes it:
`memory/builds/dUnstalledConvoy/reviews/2026-08-24-review-TOOL-dUnstalledConvoy-26-spec-rev2.md:328`
records that on an upgrade re-apply `govkit.py:2510-2512` fires `a leg that vanished is not a leg
that passed` once per MIGRATED leg, naming the wrong cause. S1 moves the emitter, so every leg in
every target becomes a migrated leg exactly once. **AC1 is not sufficient on its own for that**, and
the S1 work must either avoid the branch or the build must record that adopters meet it once. It is
carried as a known consequence rather than silently discovered at an adopter.
