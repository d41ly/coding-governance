# DEPL-cMendedVintage-11 — `cmd_check` grades the attributes row's block

**Status:** SPECCED · rev-2 · 2026-09-16 · node c · Tier-2 · base 859daa67 · streams deployer · order 20

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-09-16-prompt-DEPL-cMendedVintage-1-1-spec-briefs.md](../prompts/2026-09-16-prompt-DEPL-cMendedVintage-1-1-spec-briefs.md) | journal | DEPL-cMendedVintage-1 DEPL-cMendedVintage-2 DEPL-cMendedVintage-3 DEPL-cMendedVintage-4 DEPL-cMendedVintage-5 DEPL-cMendedVintage-6 DEPL-cMendedVintage-7 DEPL-cMendedVintage-8 DEPL-cMendedVintage-9 DEPL-cMendedVintage-10 DEPL-cMendedVintage-12 DEPL-cMendedVintage-13 DEPL-cMendedVintage-14 TOOL-cMendedVintage-1 TOOL-cMendedVintage-2 TOOL-cMendedVintage-3 TOOL-cMendedVintage-4 TOOL-cMendedVintage-5 TOOL-cMendedVintage-6 TOOL-cMendedVintage-7 TOOL-cMendedVintage-8 TOOL-cMendedVintage-9 |
| [2026-09-16-review-DEPL-cMendedVintage-1-spec-audit-round1.md](../reviews/2026-09-16-review-DEPL-cMendedVintage-1-spec-audit-round1.md) | spec-audit | TOOL-cMendedVintage-1 TOOL-cMendedVintage-2 TOOL-cMendedVintage-3 TOOL-cMendedVintage-4 TOOL-cMendedVintage-5 TOOL-cMendedVintage-6 TOOL-cMendedVintage-7 TOOL-cMendedVintage-8 TOOL-cMendedVintage-9 DEPL-cMendedVintage-1 DEPL-cMendedVintage-2 DEPL-cMendedVintage-3 DEPL-cMendedVintage-4 DEPL-cMendedVintage-5 DEPL-cMendedVintage-6 DEPL-cMendedVintage-7 DEPL-cMendedVintage-8 DEPL-cMendedVintage-9 DEPL-cMendedVintage-10 DEPL-cMendedVintage-12 DEPL-cMendedVintage-13 DEPL-cMendedVintage-14 |

<!-- /gen:spec-records -->

## 1. Goal

`cmd_check`'s block-drift loop opens by skipping every row whose role is not `merged`, so the
`attributes` row — which carries `block_id`, `marker_style` and `block_sha256` exactly as a merged
row does — is graded by nothing. A target can delete or edit gov's LF-pin block and `check` reports
a clean install. Admit that role to the loop the receipt already equips it for.

## 2. Scope (IN)

- **S1** The role gate at `tools/govkit/govkit.py:3164` admits `attributes` alongside `merged`. The
  `json-pointer` exclusion beside it is unchanged; the `attributes` row's `marker_style` is
  `hash-comment`, which is the only style `marker_pair` synthesizes. Observed by AC1 and AC2.
- **S2** The loop counts the two roles SEPARATELY and prints the existing `merged blocks:` note
  unchanged plus one new note for the pin block. The existing string is asserted verbatim by two
  shipped arms, and a target with one merged row and one attributes row would otherwise read
  `merged blocks: 2/2 intact`, which is a false sentence and a red arm in the same edit. Observed by
  AC4.
- **S3** A row admitted by S1 that carries no `block_sha256` is REPORTED as ungradeable and named,
  never failed. Comparing a digest against `None` prints `expected None` and reads as drift.
  Observed by AC3.
- **S4** The messages name the role. `gov block 'govkit:lf-pins' has been REMOVED from
  .gitattributes` is the pin case and reads correctly as written; the DRIFT message gains the role
  so an operator can tell which of the two loops spoke. Observed by AC2.

## 3. Non-goals (OUT)

- No grading of whether the PATTERNS still match what the claimed kits declare. That is a vintage
  question and it belongs to `update`'s `pins` arm at `tools/govkit/govkit.py:6386`, which recomputes
  from the descriptors at the requested commit. This loop asks a drift question: are gov's bytes
  still gov's bytes. The two are deliberately separate and neither is moved here.
- No repair. `check` reports; `DEPL-cMendedVintage-10` is what writes the block back.
- No change to the merged loop's CR handling, its `find_block` refusal catch or its extraction.
  They are reused unmodified, and reusing them is the unit.
- No new receipt field and no floor. Every field this reads has been written by `apply` since the
  `attributes` row existed.

### Edges

- **consumes-from** `DEPL-cMendedVintage-10` — the remedy for a red this unit raises. On its own
  this reds every adopter whose pins moved and leaves them only `govkit apply`, which overwrites
  engine bytes unconditionally. It ships in the same release as that unit and never before.
- **hands-off** external — an adopter's own bar gains a real verdict on gov's pin block; nothing in
  this build consumes it.

- **consumes-from** `DEPL-cMendedVintage-17` — that unit drops the receipt row and the region together, so a row it withdraws does not read here as a missing block.
## 4. Design

### Data model

No new fields. The join is over the row `apply` synthesizes at `tools/govkit/govkit.py:4627`:

| field | value | read by |
|---|---|---|
| `role` | `attributes` | the admitted gate at `:3164` |
| `block_id` | `govkit:lf-pins` (`GA_BLOCK_ID`) | `marker_pair` |
| `marker_style` | `hash-comment` | `marker_pair`, the only style it synthesizes |
| `block_sha256` | sha256 of `lf_pin_block`'s marker-inclusive text | the comparison |

The hashes already agree, and it is worth stating because it is the reason this is a one-line gate
and not a new comparator. `lf_pin_block` returns marker-inclusive text, hashed by `apply` before the
file is written. The extractor in this loop slices the same marker-inclusive span out of the file
and hashes it after `.replace(CR, "")`. So a target whose `.gitattributes` is checked out CRLF —
which is the normal state on a Windows clone with no `text` attribute on the file itself — grades
green against a digest taken over LF bytes, without a second normalization being written anywhere.

### Inventory

| identifier | kind | where |
|---|---|---|
| `n_pins_blocks` / `n_pins_ok` | local counters in `cmd_check` | `tools/govkit/govkit.py`, beside `n_blocks` |
| the ungradeable-row `r.note` text | report line | one new call site |

The DRIFT and REMOVED refusal texts are edited, not added, so `tools/govkit/refusal_join.py`'s
anchor set gains nothing from S4; S3 adds a note, which is not a refusal channel. The anchor count
is DERIVED by that engine and is not written here.

### Rollout

Red on arrival at any adopter whose block was edited or removed, which is the point and is also why
the edge to `DEPL-cMendedVintage-10` is a hard ordering rather than a preference. The two land in
one release: the verdict and the verb that clears it.

### Alternatives rejected

- **Rename the note to cover both roles.** One string, two populations, and the string is asserted
  verbatim at `tools/govkit/selftest.py:1477`. Renaming it flips a shipped arm to buy a shorter
  diff, and the sentence it would produce is less true than the two it replaces.
- **A second loop for the attributes row.** It would spell `marker_pair`, `find_block`, the CR
  strip and the digest compare a second time, which is this repo's named defect class. The existing
  loop is role-blind below its gate for exactly this reason.
- **Fail on a missing `block_sha256`.** A receipt row minted before a field existed is an artefact
  of vintage, not of tampering. UNVERIFIED whether such an `attributes` row exists in the wild; the
  guard costs one branch and the failure it prevents is a false accusation.

### Files touched (estimate)

| Path | Change |
|---|---|
| `tools/govkit/govkit.py` | the role gate, two counters, one note, the role in two messages |
| `tools/govkit/selftest.py` | the arms §7 names |

## 5. Production-readiness checklist

- security — read-only. The loop opens one target-owned file whose path is a receipt row, which
  every other arm of this verb already does.
- perf / scale — one extra `read_text` of `.gitattributes` per run, on a file the pins arm already
  reads.
- error / empty / loading states — an absent file takes the existing GONE branch; an absent block
  takes the existing REMOVED branch; a `find_block` refusal is caught by the existing `except`.
- observability — the new note prints on every run including the clean one, so a zero is
  distinguishable from a loop that did not execute.
- risks — this reds targets. The mitigation is the release ordering in §3, not a flag: a verdict
  that ships behind an opt-in grades the installs that were already careful.
- testing — AC1 through AC4, each on a scratch fixture target; gov keeps no receipt of its own, so
  none of them is observable against this repo.
- migration — none. No schema change, no floor, no re-adoption.
- user docs — `WIRE-INTO-PROJECT.md`'s description of what `check` grades gains the pin block.

## 6. Acceptance criteria

- **AC1** — When a scratch fixture target installed with a kit declaring an `[[lf_pin]]` is left
  untouched and `python tools/govkit/govkit.py check --target <fixture>` runs, it exits 0 and its
  new note reports the pin block intact.
  Red when: the role gate admits the row but the extractor is handed the file's whole text rather
  than the marked span, so every target reads as drifted and the arm passes by failing.
  fixture: a scratch fixture target under the run's scratch root, built with `intake` then `apply`.
  This repo does not dogfood govkit and carries no receipt, so no criterion here is observable
  against it.
- **AC2** — When one line INSIDE the marker pair of that fixture's pin block is edited and
  `python tools/govkit/govkit.py check --target <fixture>` runs, it fails naming `govkit:lf-pins`
  and the file; when the block is deleted entirely, the same command fails with the REMOVED wording
  instead.
  Red when: the tamper is appended after the close marker, in which case the block is byte-identical,
  `current` is the correct verdict and the arm proves nothing — the shape already measured on this
  file's sibling arm.
- **AC3** — When the fixture's receipt has `block_sha256` removed from its `attributes` row and
  `python tools/govkit/govkit.py check --target <fixture>` runs, the row is reported as ungradeable
  by name and the run does not fail on it.
  Red when: the guard tests the row's truthiness rather than the key's presence, which also swallows
  a legitimately empty digest and silently drops a real row from the graded population.
- **AC4** — When a fixture carrying both a `merged` row and an `attributes` row is checked with
  `python tools/govkit/govkit.py check --target <fixture>`, stdout carries `merged blocks: 1/1
  intact` unchanged alongside the separate pin-block note.
  Red when: the two roles share one counter, which makes the existing string report 2/2 and flips
  the shipped arms that assert it verbatim.
  figure: DERIVED — the counts come from the run's own output; `1/1` is the fixture's shape, not a
  claim about any other tree.

## 7. Gates

`govkit selftest` · `govkit selfcheck` · `govkit acceptance matrix`

New arm: `tools/govkit/selftest.py` · a fixture whose pin block is edited inside the markers,
asserted to fail `check`, beside an untouched fixture asserted to pass and a receipt with the digest
field removed asserted to report rather than fail · no assertion floor to move.

## 8. Open questions

- **Q1 — FACT-QUESTION · does the existing extractor grade this row unmodified, or does the
  attributes row need its own comparator?**
  RESOLVED (agent, 2026-09-16, delegated): unmodified. The probe is reading the four fields
  `apply` writes at `tools/govkit/govkit.py:4627` against what the loop at
  `tools/govkit/govkit.py:3164` consumes, and `marker_pair`'s refusal for any style but
  `hash-comment`. The probe can produce a negative — a row carrying a style `marker_pair` refuses,
  or a digest taken over marker-exclusive text, would each have forced a comparator — and neither
  is the case.
- **Q2 — should a drifted pin block fail the verb or merely report?**
  RESOLVED (agent, 2026-09-16, delegated): fail, as the merged loop does. A gov-owned region a
  target edited is the exact condition `check`'s drift arm exists to raise, and demoting this one
  role to a note would mean the only block gov synthesizes rather than ships is the only one nobody
  has to fix.

## 9. Revision log

- rev-1 · 2026-09-16 · initial draft.
- rev-2 · 2026-09-17 · §3 · RECIPROCAL EDGE, no scope or criterion changed. The spec-audit disposal authored DEPL-cMendedVintage-17 naming this unit, and the edge was never written back — hygiene check 12 reds on a handoff one author declared and the other never saw. The edge is a fact about this build that became true when the promotion was created, so recording it completes the record rather than changing the design.

## 10. Reuse audit

The seam this unit extends is the merged-block drift loop at `tools/govkit/govkit.py:3160`, read
from source: it already synthesizes the marker pair through the one synthesizer, already catches
`find_block`'s refusal, and already strips CR before hashing. Admitting a second role to it is the
whole change. `python tools/codebase-map/reuse_lookup.py "write the govkit-owned gitattributes pin
block and renormalize the pinned population"` returned only name-token neighbours and no seam — its
top rows are `write` in `tools/memory-tree/gotchas.py` and `write_text` in
`tools/memory-tree/gen_build_index.py`, neither reachable from this verb — and
`memory/map/features/govkit.md` states the negative directly: nothing in this repo writes or grades
a `.gitattributes` block outside govkit itself. The recall probe supplied the constraint that fixes
this unit's order: `DEPL-dCarriedReceipt-2` ratified that the `pins` disposition reports and never
writes, which is why the remedy for a red raised here did not exist until
`DEPL-cMendedVintage-10`.

Recall terms used: `--terms "govkit update apply gitattributes lf_pin attributes receipt
renormalize outbox order pins-moved rollback snapshot"`, with the question "why does govkit update
report the gitattributes pin block as an order instead of writing it, and what owns the
renormalize".
