# DEPL-aRepatriatedFork-21 — apply never lands gov's bytes on a file the target owns

**Status:** CLOSED · rev-2 · 2026-09-24 · node a · Tier-2 · base 7308f088 · streams deployer · order 3

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-09-24-build-DEPL-aRepatriatedFork-21-1-acceptance-ledger.md](../build/2026-09-24-build-DEPL-aRepatriatedFork-21-1-acceptance-ledger.md) | journal | — |
| [2026-09-24-prompt-DEPL-aRepatriatedFork-21-build-brief.md](../prompts/2026-09-24-prompt-DEPL-aRepatriatedFork-21-build-brief.md) | journal | — |

<!-- /gen:spec-records -->

## 1. Goal

`DEPL-aRepatriatedFork-13` gave a target a declared `adopter-owned` role through `[[own]]` rows in its
`.governance/deploy.toml`, and taught `adopt`, `update` and `check` to honour it. `apply` was out of
that unit's scope and reads no `[[own]]` row: its builder reported that an `apply --resume` over an
owning target resolves the owned source as an ordinary `engine` write and lands gov's bytes on the
adopter's program. That is the file the declaration exists to protect, and a hole in a mechanism this
build introduced. This unit makes `apply` honour the declaration exactly as `update` does.

## 2. Scope (IN)

- **S1** — `apply` reads the target's `[[own]]` rows through `resolve_owned_rows`, the one grader
  `adopt` already calls, before it computes a write, so a malformed declaration refuses there
  exactly as it refuses in `adopt`. Observed by AC3.
- **S2** — An owned `path` that is one of the destinations `resolve_owned_rows` returns under
  `dests` is removed from `apply`'s write set. A `dests` member that is NOT the owned path is gov's
  own copy of a stood-in source, and it keeps landing per `DEPL-aRepatriatedFork-13` §8 F2. It
  prints one line per skipped destination naming the path and the `[[own]]` row, and its receipt
  keeps the row `adopter-owned` rather than re-recording it `engine`: carried verbatim from the
  receipt where that row is already `adopter-owned`, else built in `adopt`'s shape from the
  declaration. Observed by AC1, AC2.
  **Readers:** by name: `_cmd_apply`'s own write loop is the only reader of the write set it
  filters. by value: `update` and `check` read the receipt row's role, which S2 leaves
  `adopter-owned` exactly as `adopt` wrote it.
- **S3** — A target with no `[[own]]` rows is unchanged: the same writes, the same receipt and the
  same output bytes. Observed by AC4.

## 3. Non-goals (OUT)

- `update`, `adopt` and `check`, which `DEPL-aRepatriatedFork-13` already made honour the role.
- Withdrawing gov's own copy of a stood-in source at a different path, which that unit's §8 F2
  resolved as "keep landing it".
- A first `apply` on a target with no receipt that declares `[[own]]` rows. `apply` still lands
  nothing on an owned path there, because S1 reads `deploy.toml` and not the receipt.

### Edges

- **consumes-from** `DEPL-aRepatriatedFork-13` — `resolve_owned_rows` and the `adopter-owned` role.
  Without it there is no declaration to honour and no single grader to call.

## 4. Design

### Evidence

Reported by `DEPL-aRepatriatedFork-13`'s builder at `7308f088`, by reading: `_cmd_apply` loads the
deploy descriptor and resolves the selection, and no line in it names `own` or
`resolve_owned_rows`. `resolve_owned_rows` has one caller, in `adopt`. AC2 is the measurement: it
observes the overwrite on `7308f088`'s bytes before anything is changed.

### Inventory

No new function. `_cmd_apply` gains one call to `resolve_owned_rows` and a filter over its write
set, both in `tools/govkit/govkit.py`.

### Rollout

Additive. A target with no `[[own]]` rows never reaches the new branch, which AC4 observes.

### Files touched (estimate)

`tools/govkit/govkit.py` · `tools/govkit/selftest.py`

### Alternatives rejected

- Refusing `apply` outright on an owning target. The operator re-running an install on such a
  target has done nothing wrong, and the other rows still need landing.
- Reading the owned set from the receipt. A receipt can be stale; the declaration is the owner's
  standing decision, which is the split `DEPL-aRepatriatedFork-13` §8 F1 ruled.

## 5. Production-readiness checklist

- security — the change narrows a write surface: `apply` writes strictly fewer files, and every
  owned path has passed the strict path class and the containment guard in `resolve_owned_rows`.
- perf / scale — one call per `apply`, over a table as long as the target's `[[own]]` rows.
- error / empty / loading states — a malformed `[[own]]` row refuses before any write, with
  `adopt`'s refusal text.
- observability — one skip line per owned destination.
- risks — an owned row whose `dests` resolves differently in `apply` than in `adopt` would skip the
  wrong file. Both call the same function over the same descriptor context, which AC1 observes.
- testing — `govkit selftest` arms for S1 to S3, the AC2 control run on the old bytes.
- migration — none; the receipt shape is unchanged.
- user docs — `WIRE-INTO-PROJECT.md`'s `[[own]]` paragraph says `apply` honours it too.

## 6. Acceptance criteria

- **AC1** — When `python tools/govkit/govkit.py apply --target <fixture> --resume --write` runs on a
  fixture whose deploy descriptor declares one `[[own]]` row over an installed engine file, the owned
  file's bytes are unchanged, the output names it as skipped, and its receipt row still reads
  `adopter-owned`.
  Red when: the owned file's bytes change, or its row reads `engine`.
- **AC2** — Red-first control: the AC1 fixture on `7308f088`'s `govkit.py` overwrites the owned
  file, recorded in the acceptance ledger.
  Red when: the control does not overwrite, so AC1 proves nothing.
- **AC3** — When the fixture's `[[own]]` row names a path with a `..` segment, `apply` exits 1 with
  `resolve_owned_rows`'s refusal and writes nothing.
  Red when: `apply` writes before it grades the declaration.
- **AC4** — When `apply --resume --write` runs on a fixture with no `[[own]]` rows, its output and
  its receipt are byte-identical to `7308f088`'s.
  Red when: the new branch changes behaviour for a target that never declared ownership.

## 7. Gates

`govkit selfcheck` · `govkit selftest` · `govkit refusal join` · `govkit acceptance matrix` · `recall floor arms` · `lexicon naming predicates`

New arm: `tools/govkit/selftest.py` · an owning fixture for AC1 and AC3, a non-owning one for AC4 · none

## 8. Open questions

none

## 9. Revision log

- rev-1 · 2026-09-24 · §2 opened as a discovery adopted under the mandate (protocol §11): the gap
  `DEPL-aRepatriatedFork-13`'s builder reported in `apply`.
- rev-2 · 2026-09-24 · S2 narrowed at build time: `dests` is gov's destinations for the owned
  source, so for a stand-in at another path it names gov's own copy, and skipping every member
  would stop landing the copy §3's second non-goal keeps. Only the owned path is skipped. S2 also
  states where the kept row comes from. AC1-AC4 unchanged.

## 10. Reuse audit

`python tools/codebase-map/reuse_lookup.py "apply skips a file the target declares it owns"` ranked
`skip`, `corpus_files` and `owners_of`, none of which reads a deploy declaration. The seam is
`resolve_owned_rows` in `tools/govkit/govkit.py`, reused rather than copied: `adopt` already grades
the declaration through it, and a second grader in `apply` would be two answers to one question.

Recall terms used: `adopter-owned own deploy apply resume receipt engine overwrite govkit
declaration`.
