# TOOL-dThriftyLanding-4 — the deployer carries a leg's doc reads to an adopter's manifest

**Status:** CLOSED · rev-2 · 2026-10-05 · node d · Tier-2 · base c3ef6742 · streams tooling · order 4

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-05-build-TOOL-dThriftyLanding-1-runlog-58509c21.md](../build/2026-10-05-build-TOOL-dThriftyLanding-1-runlog-58509c21.md) | journal | TOOL-dThriftyLanding-1 TOOL-dThriftyLanding-2 TOOL-dThriftyLanding-3 TOOL-dThriftyLanding-5 TOOL-dThriftyLanding-6 TOOL-dThriftyLanding-8 TOOL-dThriftyLanding-9 TOOL-dThriftyLanding-10 TOOL-dThriftyLanding-11 TOOL-dThriftyLanding-12 |
| [2026-10-05-build-TOOL-dThriftyLanding-4-1-acceptance-ledger.md](../build/2026-10-05-build-TOOL-dThriftyLanding-4-1-acceptance-ledger.md) | journal | — |
| [2026-10-05-prompt-TOOL-dThriftyLanding-4-1-build-brief.md](../prompts/2026-10-05-prompt-TOOL-dThriftyLanding-4-1-build-brief.md) | journal | — |
| [2026-10-05-review-TOOL-dThriftyLanding-1-closing-diff-round1.md](../reviews/2026-10-05-review-TOOL-dThriftyLanding-1-closing-diff-round1.md) | diff-review | TOOL-dThriftyLanding-1 TOOL-dThriftyLanding-2 TOOL-dThriftyLanding-3 TOOL-dThriftyLanding-5 TOOL-dThriftyLanding-6 |

<!-- /gen:spec-records -->

## 1. Goal

An adopter's leg manifest is written by `govkit` from the `[[gate_leg]]` rows of the kit descriptors,
and the writer copies `name`, `argv`, `subject` and `guard` only. A `doc_reads` declared on a kit's
leg would stop at this repository's edge, so an adopter's doc push would still pay every kit leg.
This unit makes the writer carry `doc_reads`, only into a target whose runner reads it, and makes
selfcheck hold a descriptor's `doc_reads` and gov's manifest row equal, as it already holds `subject`.

## 2. Scope (IN)

- **S1** — `write_gate_legs` asks a pure helper, `derive_doc_reads`, which resolves each `doc_reads`
  element with `resolve_tokens`. When every
  element resolves and each matches a tracked path in the target, the row carries the resolved list;
  a declared empty list is carried as `[]`. When any element fails, the row carries NO `doc_reads`,
  so the leg runs on every doc push. Dropping one element instead would narrow the leg. Observed by
  AC1 and AC2.
- **S2** — The key is emitted only when the target's installed runner declares
  `KIT_RUN_GATES_VERSION` at or above 1.25, read as `check_target_reads_subject` reads its floor, so
  an older canary's key-set pin is never redded by an install. Observed by AC3.
- **S3** — Selfcheck's leg-correspondence block, 7h, fails when a descriptor's `doc_reads`, with
  `{memory_root}` resolved to gov's memory root, differs from gov's manifest row for that leg, in
  either direction, presence included. Observed by AC4.
- **S4** — `GATE_DOC_PATHS` joins `POLICY_KEYS`, the repo-local gate-policy keys selfcheck 7h3 refuses
  in any file a kit ships: which paths are non-code is each repository's answer, and an adopter must
  never inherit gov's by a kit copying the file that holds it. Observed by AC5.

## 3. Non-goals (OUT)

- Which kit legs declare `doc_reads`, and with what: `TOOL-dThriftyLanding-5`.
- An adopter's own legs: they are theirs to declare in their manifest.
- `guard` emission: unchanged.

### Edges

- **consumes-from** `TOOL-dThriftyLanding-1` — runner 1.25 is the floor S2 reads.
- **hands-off** `TOOL-dThriftyLanding-5` — the descriptors' values.

## 4. Design

### Evidence

Read at base `c3ef6742`. `tools/govkit/govkit.py` `write_gate_legs` builds `row = {"name", "argv"}`,
adds `subject` when `check_target_reads_subject` passes its floor `SUBJECT_FLOOR_RUN_GATES = (1, 1)`,
and adds the resolved guards that match a tracked target path, dropping the rest. Selfcheck 7h
compares each descriptor leg's `subject` with gov's manifest row and fails on a disagreement or a
manifest row with none. The descriptors spell repo paths with `{memory_root}` and `{kit}`.

### Files touched (estimate)

- `tools/govkit/govkit.py`
- `tools/govkit/selftest.py`

### Alternatives rejected

- **Drop the unresolved elements, as guards are dropped.** A guard that loses an element runs less
  often only when the rest also miss, and is caught at the next full bar; a `doc_reads` list that
  loses one SKIPS on exactly the doc push that touches the lost path. Omitting the key keeps the leg on.
- **Emit regardless of the target's runner.** Its canary pins the key set, so an install would red a
  bar the target did not change.

## 5. Production-readiness checklist

- perf / scale — one token resolution per element, at install time only.
- security — no new input: the values are gov's descriptors, resolved with the existing tokens.
- error / empty / loading states — any unresolved element omits the key, which runs the leg.
- observability — an omission prints a `doc_reads omitted` line naming the leg and the element.
- testing — the govkit selftest's fixture targets, each arm RED against base first.
- migration — an adopter's next `apply` writes the key; until then their legs run as today.
- user docs — the runbook, in `TOOL-dThriftyLanding-6`.
- risks — none beyond S1's: an adopter whose memory root resolves elsewhere gets resolved paths.

## 6. Acceptance criteria

- **AC1** — When `derive_doc_reads` is handed a leg declaring `{memory_root}/builds/` against a target
  tracking a file under memory/builds/, it returns `["memory/builds/"]`; a declared empty list returns
  `[]`; and the writer routes every leg through it at the doc-reads floor.
  Red when: the base module has no such helper and the writer emits no `doc_reads`.
- **AC2** — When one element names a path the target does not track, or carries an unresolved token,
  the helper returns no list and a reason, which the writer prints as `doc_reads omitted`.
  Red when: a narrowed list is returned.
- **AC3** — When the target's runner declares 1.24, `check_target_reads_subject` at the doc-reads floor
  answers no, while the same target still answers yes for `subject`.
  Red when: the key reaches a runner whose canary refuses it.
- **AC4** — When gov's manifest row and its descriptor disagree on `doc_reads`, selfcheck fails
  naming the leg; when they agree, it passes.
  Red when: the two spellings drift with selfcheck green.
- **AC5** — When the selftest's policy predicate reads `GATE_DOC_PATHS="memory/"`, it matches, and
  `POLICY_KEYS` names the key.
  Red when: a kit could ship gov's doc class.

## 7. Gates

`govkit selftest` · `govkit selfcheck` · `govkit acceptance matrix` · `govkit refusal join` · `recall floor arms` · `kit epoch (shipped bytes move, the version moves)` · `spec tokens (a spec's own names resolve)`

New arm: tools/govkit/selftest.py · a descriptor leg declaring `doc_reads`, installed by the base writer · none

## 8. Open questions

none

## 9. Revision log

- rev-1 · 2026-10-05 · initial draft, from `write_gate_legs` and selfcheck 7h at base.
- rev-2 · 2026-10-05 · S1 names the helper the writer calls, so AC1 to AC3 observe it directly
  rather than through a full fixture install; S4 and AC5 add the doc class to the policy keys.

## 10. Reuse audit

The seams extended are `check_target_reads_subject`, whose floor read is reused at a second floor,
`resolve_tokens`, and selfcheck 7h's descriptor-to-manifest comparison. `python
tools/codebase-map/reuse_lookup.py "carry a leg field from a kit descriptor to a target manifest"`
names the `registry.toml` seam of the govkit dossier. The recall query returned
`TOOL-dUnstalledConvoy-26`, which carried `subject` the same way and states why the floor is read from
the target.

Recall terms used: govkit write_gate_legs gate_leg descriptor subject floor KIT_RUN_GATES_VERSION canary key set adopter manifest resolve_tokens selfcheck 7h
