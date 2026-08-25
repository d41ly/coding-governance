# TOOL-aFoldedQuarry-1 — fold the upstream ledger + trove builds into the memory-tree kit

**Status:** CLOSED · rev-3 · 2026-08-08 · node a · Tier-2 · base 42c3f4dc · streams tooling · ratified 2026-08-08

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-08-08-review-TOOL-aFoldedQuarry-1-1.md](../reviews/2026-08-08-review-TOOL-aFoldedQuarry-1-1.md) | spec-audit | TOOL-aFoldedQuarry-2 |
| [2026-08-08-review-TOOL-aFoldedQuarry-1-7.md](../reviews/2026-08-08-review-TOOL-aFoldedQuarry-1-7.md) | diff-review | TOOL-aFoldedQuarry-2 TOOL-aFoldedQuarry-3 TOOL-aFoldedQuarry-4 TOOL-aFoldedQuarry-5 TOOL-aFoldedQuarry-6 TOOL-aFoldedQuarry-7 |

<!-- /gen:spec-records -->

## 1. Goal

Fold two upstream inCMS builds (`ARCH-dQuarriedLedger-1`, `ARCH-dWinnowedTrove-2`) into this repo's
parameterised `tools/memory-tree/` kit, and re-dogfood every change on this repo's own `memory/`.
The upstream work doubled the hygiene gate's reach; porting the mechanism rather than the scripts is
what lets any adopting repo get that reach without inheriting inCMS's corpus measurements.

## 2. Scope (IN)

- **S1** — U6: replace the ref-echo verdict join in `tools/workflows/tier2-review.js` with an
  orchestrator-assigned integer index keyed on a `Map`, keeping the kit's existing unverified and
  PARTIAL reporting. Add the source-level gate that no `.ref`-keyed verdict join survives in any
  JavaScript file under `tools/`, and the syntax gate that a workflow script still parses in the
  dialect its runtime evaluates.
- **S2** — U1: retire the discipline DIRECTORY axis from the kit and from this repo's tree. Build
  folders become `<MEMORY_ROOT>/builds/<slug>/`. The per-discipline decision logs become one
  append-only `<MEMORY_ROOT>/DECISIONS.md`. Backlogs stay sharded, one mutable file per FAMILY under
  `<MEMORY_ROOT>/backlog/`. The discipline survives as a CLOSED enum in the spec status header,
  validated by the spec-format check and date-gated by `STREAMS_CUTOFF`.
- **S3** — U2: delete `gen-memory-tree.sh` and the authored tree file it generates; replace with
  `tools/memory-tree/gen_build_index.py`, which renders each build README's generated region,
  `<MEMORY_ROOT>/LIVE.md`, and `<MEMORY_ROOT>/ledger/` month shards from README front matter plus
  the `**Status:**` headers under that build's `spec/`.
- **S4** — U3: add `tools/memory-tree/corpus_ids.py` — one id grammar, one walk, every consumer —
  carrying the dead-path registry, the orphan-id waiver, and read-path accounting.
- **S5** — U4: add `tools/memory-tree/gotchas.py` plus the authored bug-class corpus under
  `<MEMORY_ROOT>/gotchas/`, its generated index, and the `--for-diff` reviewer checklist.
- **S6** — U5: apply the harness disciplines to `check-memory-hygiene.test.sh` — derived pins keyed
  on the call site, pinned in both directions, an unarmed-branch pin keyed on the `fail` branch, and
  batched fixtures.
- **S7** — every PIN, FLOOR, CEILING and CUTOFF this build introduces is MEASURED against this
  repo's corpus at adoption time and written by `adopt-memory-tree.sh`, never inherited from inCMS.
- **S8** — `hygiene-parity.test.sh` stays green across every unit: the kit's built-in defaults and
  this repo's `.memory-tree.conf` must not diverge.

## 3. Non-goals (OUT)

- inCMS's 178 gotcha records. The MECHANISM ports; the corpus is this repo's own failure history and
  starts from the records this build can evidence. Porting the records ships anchors matching nothing.
- `tier2-review-indexed.js` as a file. Only its join ports; the kit's reporting is richer than the
  file inCMS deleted, so the kit harness keeps its identity and filename.
- inCMS's node registry rows, worktree paths, remote names, and `curation-debt.txt` contents.
- `drift_report.py`. It is a reporting convenience, not a gate, and nothing in S1–S8 depends on it.
  Follow-up row if a consumer appears.
- Renumbering or rewriting ratified ids. Frozen id eras are cited unchanged; a citation that stops
  resolving is registered as a dead path (S4), never rewritten.
- Check 26's positive-path population (inCMS's `help/` + `infra/`). The kit gets the configured
  positive path list with an empty default; this repo configures nothing.

## 4. Design

### Data model

The tree loses one axis and gains one field. Before, a build's discipline was encoded in its PATH
(`<MEMORY_ROOT>/<discipline>/builds/<date>-<FAMILY>-<slug>/`) and nowhere else. After, it is encoded
in the spec status header as a `streams` field over a CLOSED enum whose legal values are
`.memory-tree.conf`'s `DISCIPLINES`, and the path is `<MEMORY_ROOT>/builds/<slug>/`.

| Concern | Before | After |
|---|---|---|
| build folder | `<MEMORY_ROOT>/<disc>/builds/<date>-<FAMILY>-<slug>/` | `<MEMORY_ROOT>/builds/<slug>/` |
| decision log | one per discipline | one append-only `<MEMORY_ROOT>/DECISIONS.md` |
| backlog | one per discipline | one per FAMILY under `<MEMORY_ROOT>/backlog/` |
| discipline signal | the directory name | the status-header `streams` enum |
| tree index | authored-then-generated tree file | generated build index plus month shards |

### Inventory

| Kit file | Unit | Change |
|---|---|---|
| `tools/workflows/tier2-review.js` | U6 | join replaced, reporting kept |
| `tools/gate-legs.json` | U6, U2, U3, U4 | new legs |
| `tools/memory-tree/check-memory-hygiene.sh` | U1–U4 | new and retargeted checks |
| `tools/memory-tree/check-memory-hygiene.test.sh` | U5 | pins, arms, batched fixtures |
| `tools/memory-tree/hygiene-parity.test.sh` | U1 | parity over the new conf keys |
| `tools/memory-tree/adopt-memory-tree.sh` | U1, S7 | scaffolds the flat shape, measures the pins |
| `tools/memory-tree/gen-memory-tree.sh` | U2 | deleted |
| `tools/memory-tree/gen_build_index.py` | U2 | new |
| `tools/memory-tree/corpus_ids.py` | U3 | new |
| `tools/memory-tree/gotchas.py` | U4 | new |
| `tools/memory-tree/HYGIENE.template.md` | U1–U4 | the rule text the checks mechanise |
| `tools/memory-tree/SPEC-TEMPLATE.template.md` | U1 | the `streams` field |
| `.memory-tree.conf` | U1, S7 | `DISCIPLINES` becomes enum values, new measured knobs |

### Migration

This repo's tree migrates in the same commit as the kit change that demands it, so the merge bar is
never red between the two. `git mv` preserves history for every moved recording file. The five
per-discipline decision logs concatenate into one append-only file in id order, with each source
file's rows kept verbatim — an append-only log is not rewritten, only relocated.

### Rollout

Unit by unit, each its own commit, each closing with the full bar green. U6 lands first because
every later unit's adversarial review runs on that harness.

### Files touched (estimate)

Roughly 15 kit files, the four discipline subtrees of `memory/` (about 60 tracked files moved), and
the three live pointer documents at the repo root.

### Alternatives rejected

- **Copy the inCMS scripts in and parameterise later.** Rejected: the numbers are corpus
  measurements, and a copied PIN is either vacuous or permanently red on a 162-file repo.
- **Keep the discipline directories and add the enum.** Rejected: two encodings of one fact drift,
  and the directory axis is what forces a build touching two disciplines to pick one.
- **Delete the kit's review harness and adopt the upstream replacement wholesale.** Rejected: the
  kit's harness already fixes the unverified-versus-refuted conflation the replacement had to add
  back, and deleting it would lose that.

## 5. Production-readiness checklist

- security — N/A for the kit's own surface. `gotchas.py --for-diff` reads a diff and writes stdout;
  it executes nothing from the corpus.
- perf / scale — the hygiene gate is already batched to one awk pass per population; every new check
  follows that shape rather than forking per file.
- a11y — N/A — no user interface.
- i18n — N/A — the corpus is English-only by construction.
- error / empty / loading states — a generator whose input README is absent must fail with a named
  error, not a traceback; an empty corpus must be a clean pass, not a crash.
- observability — every `fail` branch names the offending path and the rule it broke.
- risks — the migration moves tracked files; a half-applied move leaves the gate red, which is the
  intended failure mode. No data loss path: `git mv` only.
- testing + left-shift gates — each unit adds its own gate leg and its own armed test branch.
- migration / rollback — one commit per unit; rollback is a revert of that commit plus its migration.
- user docs — `HYGIENE.template.md` and `WIRE-INTO-PROJECT.md` carry the adopter-facing rules.

## 6. Acceptance criteria

- **AC1** — When `tools/workflows/tier2-review.js` runs its verify phase, the verdict map is keyed on
  the orchestrator-assigned integer and two findings sharing one `file:line` receive independent
  verdicts.
- **AC2** — When the ref-keyed-join gate leg runs against `tools/`, it exits non-zero on a
  reintroduced `.ref`-keyed verdict assignment and zero on the shipped tree.
- **AC3** — When the hygiene gate runs after the flatten, no path under `<MEMORY_ROOT>` contains a
  discipline directory segment, and a spec whose header names a discipline outside the enum fails
  the spec-format check with a message naming the illegal value.
- **AC4** — When the build index generator runs with the check flag over an unmodified tree it exits
  zero, and when any generated region is edited by hand it exits non-zero naming that file.
- **AC5** — When a citation in the corpus points at a path that no longer exists, the id check fails
  unless that exact path is registered, and registering a path that DOES resolve also fails.
- **AC6** — When `gotchas.py --for-diff` is given a base and head, its stdout lists every record
  whose derived anchors intersect the diff plus the whole universal set, and nothing else.
- **AC7** — When a `fail` branch is added to the hygiene gate without a matching armed test branch,
  the harness meta-check fails naming that branch's own failure text.
- **AC8** — When `hygiene-parity.test.sh` runs after every unit, it exits zero.

## 7. Gates

`bash tools/run-gates.sh` — the full bar. The legs this build must keep green throughout:
`tools/memory-tree/check-memory-hygiene.sh`, `tools/memory-tree/check-memory-hygiene.test.sh`,
`tools/memory-tree/hygiene-parity.test.sh`, `tools/check-wiring.sh`, and the kickoff-manifest
ratchet. New legs this build adds: the ref-keyed-join ban (U6), the build-index drift check and its
selftest (U2), the id-corpus check (U3), and the gotchas check plus its selftest (U4).

## 8. Open questions

none — both forks below are RESOLVED (owner-ratified 2026-08-08); kept for the record.

- **Fork A — how much of the upstream check set ports.** Options: all 26 upstream checks, or the
  subset whose population this repo actually has. RESOLVED (owner, 2026-08-08): port the mechanism
  behind checks 13–25 and configure the population; leave check 26's positive-path list empty here.
  The handoff's instruction to ratify the most feature-rich decision governs, and a configured-empty
  population is a live check with nothing to say rather than a missing capability.
- **Fork B — the four open upstream backlog rows.** Options: port them as debt, or fix them in the
  kit. RESOLVED (owner, 2026-08-08): fix what the port makes cheap and carry the rest as rows in this
  repo's own backlog. The anchor-line id schema defect and the unarmed-branch count are fixed by
  U4 and U5 respectively as part of building them; the universal-set budget is measured and recorded
  rather than assumed; the unresolving-pointer census is this repo's own number, not inCMS's.

## 9. Revision log

- rev-1 · 2026-08-08 · initial draft.
- rev-2 · 2026-08-08 · folded review 1 finding R4: the ban's population is every JavaScript file
  under `tools/`, matching the U6 sub-spec, and the workflow syntax gate joins S1.
- rev-3 · 2026-08-08 · all six units CLOSED; folded the closing review (review 7) over the whole
  diff. Two scope items landed larger than drafted and are recorded here rather than in a follow-up:
  S3's replacement generator also owns `LIVE.md` and the month shards, and the build gained a
  kit/dogfood document-parity gate that S1-S8 did not anticipate — it was added because the shipped
  spec template had already drifted four days behind the installed one with nothing watching.

## 10. Reuse audit

No `tools/codebase-map/` map exists in this repo (`.codebase-map.conf` is absent), so the reuse pass
is a direct inventory of `tools/`. Every unit wires through an existing seam rather than adding a
parallel one: U6 edits the harness already at `tools/workflows/tier2-review.js` instead of adding the
upstream file beside it; U2, U3 and U4 register as legs in `tools/gate-legs.json`, which
`tools/run-gates.sh` already iterates, instead of adding runners; the new checks live inside
`check-memory-hygiene.sh`'s existing `fail` protocol and batched-awk idiom; the scaffold and the
measured knobs go into `adopt-memory-tree.sh`, which already owns adoption-time writes; and the
parity between the kit's built-in defaults and this repo's conf stays the property of
`hygiene-parity.test.sh`. The one genuinely new seam is `gotchas.py`, whose `--declares` predicate
becomes the single source the shell check shells out to rather than a second copy of the alternation.
