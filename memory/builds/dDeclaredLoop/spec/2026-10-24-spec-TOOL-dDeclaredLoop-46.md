# TOOL-dDeclaredLoop-46 — the `stage` claim follows the whole manifest-key path: descriptors, emitter, runner floor and selfcheck

**Status:** DEFERRED · rev-2 · 2026-10-24 · node d · Tier-2 · base ed497191 · streams tooling · order 20 · advances TOOL-dDeclaredLoop-35

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-24-build-TOOL-dDeclaredLoop-1-agent-ledger.md](../build/2026-10-24-build-TOOL-dDeclaredLoop-1-agent-ledger.md) | journal | TOOL-dDeclaredLoop-1 TOOL-dDeclaredLoop-2 TOOL-dDeclaredLoop-3 TOOL-dDeclaredLoop-4 TOOL-dDeclaredLoop-5 TOOL-dDeclaredLoop-6 TOOL-dDeclaredLoop-7 TOOL-dDeclaredLoop-8 TOOL-dDeclaredLoop-9 TOOL-dDeclaredLoop-10 TOOL-dDeclaredLoop-11 TOOL-dDeclaredLoop-12 TOOL-dDeclaredLoop-13 TOOL-dDeclaredLoop-14 TOOL-dDeclaredLoop-15 TOOL-dDeclaredLoop-16 TOOL-dDeclaredLoop-17 TOOL-dDeclaredLoop-18 TOOL-dDeclaredLoop-19 TOOL-dDeclaredLoop-20 TOOL-dDeclaredLoop-21 TOOL-dDeclaredLoop-22 TOOL-dDeclaredLoop-23 TOOL-dDeclaredLoop-24 TOOL-dDeclaredLoop-25 TOOL-dDeclaredLoop-26 TOOL-dDeclaredLoop-27 TOOL-dDeclaredLoop-28 TOOL-dDeclaredLoop-29 TOOL-dDeclaredLoop-30 TOOL-dDeclaredLoop-31 TOOL-dDeclaredLoop-32 TOOL-dDeclaredLoop-33 TOOL-dDeclaredLoop-34 TOOL-dDeclaredLoop-36 TOOL-dDeclaredLoop-37 TOOL-dDeclaredLoop-38 TOOL-dDeclaredLoop-39 TOOL-dDeclaredLoop-40 TOOL-dDeclaredLoop-41 TOOL-dDeclaredLoop-42 TOOL-dDeclaredLoop-43 TOOL-dDeclaredLoop-44 TOOL-dDeclaredLoop-45 TOOL-dDeclaredLoop-47 TOOL-dDeclaredLoop-48 TOOL-dDeclaredLoop-49 TOOL-dDeclaredLoop-50 TOOL-dDeclaredLoop-51 TOOL-dDeclaredLoop-52 TOOL-dDeclaredLoop-53 TOOL-dDeclaredLoop-54 TOOL-dDeclaredLoop-55 TOOL-dDeclaredLoop-56 TOOL-dDeclaredLoop-57 TOOL-dDeclaredLoop-58 TOOL-dDeclaredLoop-59 TOOL-dDeclaredLoop-60 TOOL-dDeclaredLoop-61 TOOL-dDeclaredLoop-62 TOOL-dDeclaredLoop-63 TOOL-dDeclaredLoop-64 TOOL-dDeclaredLoop-65 TOOL-dDeclaredLoop-66 TOOL-dDeclaredLoop-67 |
| [2026-10-24-build-TOOL-dDeclaredLoop-36-promoted-fix-return.md](../build/2026-10-24-build-TOOL-dDeclaredLoop-36-promoted-fix-return.md) | research | TOOL-dDeclaredLoop-36 TOOL-dDeclaredLoop-37 TOOL-dDeclaredLoop-38 TOOL-dDeclaredLoop-39 TOOL-dDeclaredLoop-40 TOOL-dDeclaredLoop-41 TOOL-dDeclaredLoop-42 TOOL-dDeclaredLoop-43 TOOL-dDeclaredLoop-44 TOOL-dDeclaredLoop-45 TOOL-dDeclaredLoop-47 TOOL-dDeclaredLoop-48 TOOL-dDeclaredLoop-49 TOOL-dDeclaredLoop-50 TOOL-dDeclaredLoop-51 TOOL-dDeclaredLoop-52 TOOL-dDeclaredLoop-53 TOOL-dDeclaredLoop-54 TOOL-dDeclaredLoop-55 TOOL-dDeclaredLoop-56 |
| [2026-10-24-build-TOOL-dDeclaredLoop-46-deviation-461.md](../build/2026-10-24-build-TOOL-dDeclaredLoop-46-deviation-461.md) | deviation | — |
| [2026-10-24-prompt-TOOL-dDeclaredLoop-36-promoted-fix-brief.md](../prompts/2026-10-24-prompt-TOOL-dDeclaredLoop-36-promoted-fix-brief.md) | research | TOOL-dDeclaredLoop-36 TOOL-dDeclaredLoop-37 TOOL-dDeclaredLoop-38 TOOL-dDeclaredLoop-39 TOOL-dDeclaredLoop-40 TOOL-dDeclaredLoop-41 TOOL-dDeclaredLoop-42 TOOL-dDeclaredLoop-43 TOOL-dDeclaredLoop-44 TOOL-dDeclaredLoop-45 TOOL-dDeclaredLoop-47 TOOL-dDeclaredLoop-48 TOOL-dDeclaredLoop-49 TOOL-dDeclaredLoop-50 TOOL-dDeclaredLoop-51 TOOL-dDeclaredLoop-52 TOOL-dDeclaredLoop-53 TOOL-dDeclaredLoop-54 TOOL-dDeclaredLoop-55 TOOL-dDeclaredLoop-56 |
| [2026-10-24-review-TOOL-dDeclaredLoop-36-spec-audit.md](../reviews/2026-10-24-review-TOOL-dDeclaredLoop-36-spec-audit.md) | spec-audit | TOOL-dDeclaredLoop-36 TOOL-dDeclaredLoop-37 TOOL-dDeclaredLoop-38 TOOL-dDeclaredLoop-39 TOOL-dDeclaredLoop-40 TOOL-dDeclaredLoop-41 TOOL-dDeclaredLoop-42 TOOL-dDeclaredLoop-43 TOOL-dDeclaredLoop-44 TOOL-dDeclaredLoop-45 TOOL-dDeclaredLoop-47 TOOL-dDeclaredLoop-48 TOOL-dDeclaredLoop-49 TOOL-dDeclaredLoop-50 TOOL-dDeclaredLoop-51 TOOL-dDeclaredLoop-52 TOOL-dDeclaredLoop-53 TOOL-dDeclaredLoop-54 TOOL-dDeclaredLoop-55 TOOL-dDeclaredLoop-56 |

<!-- /gen:spec-records -->

## 1. Goal

The round-1 spec audit (`memory/builds/dDeclaredLoop/reviews/2026-10-24-review-TOOL-dDeclaredLoop-1-spec-audit-round1.md`)
confirmed finding **id 25 at HIGH**, its item **H11**, alone in that item; its canary half is id 36
(item M17, MEDIUM), batched into `TOOL-dDeclaredLoop-56`. `TOOL-dDeclaredLoop-4` S2 adds `stage` to every
`tools/gate-legs.json` row "on the pattern of dOrderedCharter-7 S2's `enforces`" and stops there. The
run-gates canary pins its key set in two `KNOWN` copies without it (`tools/run-gates/run-gates.test.sh:244`,
:580); govkit builds an adopter's rows from a fixed key set (`tools/govkit/govkit.py:4400-4450`), so
`stage` never reaches an adopter, where `loop stage coverage` then reds every leg unclaimed; and selfcheck
7h compares descriptor and manifest on `subject` and its siblings (:2785-2830) with no `stage` arm, so
the two can disagree silently. This unit takes the report's fix for the emitter and descriptor half.
It repairs `TOOL-dDeclaredLoop-4`.

## 2. Scope (IN)

- **S1** — The key admitted: `stage` joins both `KNOWN` sets in `tools/run-gates/run-gates.test.sh`, and
  `KIT_RUN_GATES_VERSION` in `tools/run-gates/run-gates.sh` moves to the next minor, the first version
  whose canary admits it. Observed by AC1.
- **S2** — The descriptors: every `[[gate_leg]]` row of every kit descriptor (26 files and 68 rows at
  base, `git grep -c '^\[\[gate_leg\]\]'` over `tools/*kit.toml` and `tools/govkit/entries/`, PINNED
  2026-10-24) and of `tools/loop/kit.toml` declares `stage`, its value the manifest row's.
  Observed by AC2.
- **S3** — The emitter: `write_gate_legs` carries the descriptor row's `stage` into the adopter's row
  when the target's installed runner is at `STAGE_FLOOR_RUN_GATES` or later, the version S1 sets, through
  `check_target_reads_subject(..., floor=STAGE_FLOOR_RUN_GATES)` as `doc_reads` and `ceiling` travel;
  below the floor it omits the key and prints one line naming the leg and the floor. Observed by AC3.
- **S4** — The correspondence: selfcheck 7h gains a `stage` arm beside its `subject` arm, failing a
  descriptor row whose `stage` differs from the manifest row's, or is absent where the manifest row
  carries one. Observed by AC4.
- **S5** — An adopter runner below the floor carries no row with `stage`, and `loop stage coverage` reads
  that population as `gate leg · unarmed — no row carries a stage claim`, never green and never red, the
  leg's own zero-population rule (`TOOL-dDeclaredLoop-4` S5). Observed by AC5.

## 3. Non-goals (OUT)

- A near-miss control pair in the canary (a misspelled key refused beside the admitted one): id 36's
  item in `TOOL-dDeclaredLoop-56`.
- The `stage` values themselves and their seed: `TOOL-dDeclaredLoop-4` S6, and for legs added after it,
  id 9's item in `TOOL-dDeclaredLoop-56`.
- An adopter's own legs: an adopter row gov did not emit is the adopter's to claim, which the coverage
  leg names as unclaimed.

### Edges

- **consumes-from** `TOOL-dDeclaredLoop-4` — the `stage` field on each `tools/gate-legs.json` row and `loop stage coverage`, whose claims this unit carries to descriptors and adopters
- **hands-off** `TOOL-dDeclaredLoop-56` — the `stage` key admitted to both canary key sets, beside which that unit's id 36 item adds the near-miss control pair
- **hands-off** `TOOL-dDeclaredLoop-67` — the round-2 minors ids 5, 21, 42, 43 and 44: this pass keeps the loop stage coverage leg green and moves the run-gates README marker with the version; AC2's TOML observation is a scope item of that unit

## 4. Design

### Evidence

- `KNOWN` holds `name argv guard impure reads chunk subject ceiling signature doc_reads` in both copies
  (`tools/run-gates/run-gates.test.sh:244`, :580), PINNED 2026-10-24.
- The floor pattern: `DOC_READS_FLOOR_RUN_GATES = (1, 25)` and `CEILING_FLOOR_RUN_GATES = (1, 2)`
  (`tools/govkit/govkit.py:6011-6017`), each read through `check_target_reads_subject` before its key is
  written (:4436-4450); the runner is at 1.43 (`tools/run-gates/run-gates.sh:36`).
- 7h's correspondence reads one dict per manifest field (:2793-2803) and compares the descriptor's value
  per leg (:2820-2830); `stage` is one more dict and one more compare.

### Inventory

| Minted | Kind | Where |
|---|---|---|
| `STAGE_FLOOR_RUN_GATES` | constant | `tools/govkit/govkit.py` |
| `stage` | key of a `[[gate_leg]]` descriptor row | every kit descriptor |

### Files touched (estimate)

- `tools/run-gates/run-gates.test.sh`
- `tools/run-gates/run-gates.sh`
- `tools/govkit/govkit.py`
- `tools/govkit/selftest.py`
- `tools/loop/kit.toml`
- `tools/agent-instructions/kit.toml`
- `tools/branch-reconcile/kit.toml`
- `tools/codebase-map/kit.toml`
- `tools/drift-audit/kit.toml`
- `tools/gate-lint/kit.toml`
- `tools/lexicon/kit.toml`
- `tools/memory-recall/kit.toml`
- `tools/memory-tree/kit.toml`
- `tools/playbook/kit.toml`
- `tools/process-monitor/kit.toml`
- `tools/roles/kit.toml`
- `tools/run-gates/kit.toml`
- `tools/runlog/kit.toml`
- `tools/unattended/kit.toml`
- `tools/workflows/kit.toml`
- `tools/govkit/entries/`

### Alternatives rejected

- **Keeping the claims out of the manifest, as `[[leg]]` rows in `tools/loop/loop.toml`.** It avoids the
  canary but makes a second table keyed by leg name beside the manifest, two spellings of one fact with
  nothing comparing them.
- **Falling back to gov's manifest in the emitter.** govkit carries `ceiling` verbatim from the
  descriptor with no manifest fallback for the reason its comment gives (:4444-4447); `stage` follows.

## 5. Production-readiness checklist

- security — no new surface.
- perf / scale — one key per row.
- error / empty / loading states — below the floor the key is omitted with a printed line, and the
  coverage leg reads that population unarmed.
- observability — the emitter's line names the leg and the floor.
- risks — a runner version bump ships with the same commit as the key, so no target meets a key its
  canary predates.
- testing — AC1 to AC5 as probes on scratch targets; the arms under §7, observed at the close.
- migration — an adopter gains `stage` on its next `update` once its runner reaches the floor.
- user docs — `tools/run-gates/README.md`'s manifest key list names `stage`.

## 6. Acceptance criteria

- **AC1** — When a probe stages a scratch `gate-legs.json` whose rows carry `stage` and runs the `KNOWN`
  set extracted from each canary copy, `run-gates.test.sh:244` and `run-gates.test.sh:580`, over it,
  both copies admit every key.
  Red when: one copy of `KNOWN` lacks `stage`, so the canary reds every row.
- **AC2** — When `python tools/govkit/govkit.py selfcheck` runs on the built tree, its 7h arm passes,
  and `git grep -c 'stage =' -- 'tools/*kit.toml' 'tools/govkit/entries/*'` counts one per `[[gate_leg]]`
  row.
  Red when: a descriptor row omits `stage` while its manifest row carries one.
- **AC3** — When a probe applies the default selection into two scratch targets, one with a runner at
  1.43 and one at the new version, the second target's `gate-legs.json` rows carry `stage` and the
  first's carry none, with one omission line per leg printed.
  Red when: the key is written into a runner that predates it, which reds that adopter's canary.
  cost: two scratch installs, seconds each.
- **AC4** — When a scratch descriptor's `stage` differs from its manifest row's, selfcheck 7h fails naming
  the leg, the descriptor's value and the manifest's.
  Red when: 7h compares `subject` alone, so the two disagree silently.
- **AC5** — When `python stage_coverage.py` runs in the first AC3 target, it prints the gate-leg
  kind as `unarmed — no row carries a stage claim` and exits 0.
  Red when: every emitted leg is printed unclaimed and the leg exits 1 in an adopter below the floor.

## 7. Gates

`run-gates canary` · `run-gates gov canary` · `govkit selftest` · `govkit refusal join` · `govkit acceptance matrix` · `govkit selfcheck` · `recall floor arms` · `codebase-map kit selftest` · `codebase-map gate coverage` · `codebase-map adopter e2e` · `shell-hygiene selftest` · `agent-instructions self-test` · `verifier fan-out self-test` · `tier2-review self-test` · `unattended-build self-test` · `review-join self-test` · `drift-audit selftest` · `runlog selftest` · `pre-push run-log line` · `run-gates run-log line` · `branch-reconcile selftest` · `lexicon selftest` · `playbook render selftest` · `memory hygiene` · `spec tokens (a spec's own names resolve)`

New arm: tools/govkit/selftest.py · covers AC3 AC4 · the emitter under each runner version and a descriptor whose `stage` disagrees, staged against the base emitter, which writes no `stage` · none

## 8. Open questions

- **F1 — Which binding line does a unit the spec audit promoted carry?** RESOLVED (agent, 2026-10-24,
  delegated): `**Derived:** PLAY-dClosedLoop-2`, rung 3, as `TOOL-dDeclaredLoop-36` §8 F1 records.
  widens: none · relaxes: none
- **F2 — Does the canary's `KNOWN` change belong here or with id 36?** The report calls id 36 the canary
  half. Options: (a) both `KNOWN` copies here, id 36's item adding the near-miss control pair; (b) the
  copies with id 36. (b) leaves S3's floor naming a runner version no unit has shipped until order 36.
  RESOLVED (agent, 2026-10-24, delegated): (a), rung 3. widens: none · relaxes: none

## 9. Revision log

- rev-1 · 2026-10-24 · initial draft, promoted from the round-1 spec audit's id 25 (HIGH, item H11).
- rev-2 · 2026-10-24 · §3 · the Edges block gains the hands-off bullets mirroring the
  consumes-from edges of TOOL-dDeclaredLoop-67, written by the round-2 spec audit's disposal; nothing else moved.

## 10. Reuse audit

The seams are govkit's runner-floor pattern, `check_target_reads_subject` with a `floor=` argument
(`tools/govkit/govkit.py:6063`), and selfcheck 7h's per-field correspondence (:2785); this unit adds one
constant, one emitted key and one compare to each. `python tools/codebase-map/reuse_lookup.py "a manifest
key carried to adopters under a runner version floor"` ranked `key`, `keys`, `manifest` and
`read_conf_key`, none of which gates an emitted key on the target's runner, so the floor pattern was
found by reading the emitter.

Recall terms used: gate-legs stage KNOWN canary write_gate_legs runner floor selfcheck 7h descriptor gate_leg doc_reads ceiling
