# TOOL-dWellOiledMachine-76 — a mailbox intake ratifies only on the proof of its own request, never a borrowed one

**Status:** OPEN · rev-1 · 2026-10-27 · node a · Tier-2 · base 0689e7fa · streams tooling · order 42 · advances TOOL-dWellOiledMachine-62

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-27-build-TOOL-dWellOiledMachine-76-deviation-761.md](../build/2026-10-27-build-TOOL-dWellOiledMachine-76-deviation-761.md) | deviation | — |

<!-- /gen:spec-records -->

## 1. Goal

Promoted from the spec audit of this build, round 1
(`memory/builds/dWellOiledMachine/reviews/2026-10-27-review-TOOL-dWellOiledMachine-1-spec-audit.md`),
finding 62, item H13, at HIGH. TOOL-dWellOiledMachine-27 S3 ratifies a mailbox receipt when its
`proof` names any request ref that passes `check_request_proof`, and nothing ties that request to the
receipt's own content; the sender chooses the ref. A non-owner sender can name a published owner
request and ratify its own arbitrary text, so a non-owner proposal becomes a build. This unit binds
the proof to the receipt: a mailbox receipt ratifies only when its proof is the content key of the
very intake record it sits in.

## 2. Scope (IN)

- **S1** — The binding. `check_intake_ratifies(receipt, repo)` (`tools/runtime/intake.py`, 27 S3)
  ratifies a `mailbox` receipt only when its `proof` equals the content key of the intake record the
  receipt belongs to, the `<key>` of `<key>.intake`, and the request ref under that key passes
  `check_request_proof` (TOOL-dWellOiledMachine-57 S6). Both keys are
  `derive_request_content_key` (TOOL-dPlacedRequest-19 S1) of the text, so a mailbox message that
  carries an owner's published request verbatim ratifies, and one that carries other words under that
  request's ref does not. Observed by AC1, AC2.
- **S2** — The refusal named. A mailbox receipt whose `proof` names another key prints
  `intake — <key> · does not ratify · mailbox · proof names <other key>` from `intake.py ratifies`,
  exit 1. Observed by AC1.
- **S3** — The filer keeps the field honest. `intake.py file --origin mailbox --proof <key>` records the
  key as given; S1 judges it at ratification, so a filer cannot pre-judge it. Observed by AC1.

## 3. Non-goals (OUT)

- No change to `check_request_proof` or the request's own chain: 57 S6 stands.
- No change to `hook` receipts, which ratify by the owner binding (27 S3), or to `cadence`, which
  never ratifies.
- No new record field: the binding is between two keys the records already carry.

### Edges

- **consumes-from** `TOOL-dWellOiledMachine-27` — `check_intake_ratifies`, `intake.py ratifies` and its fixture, which this unit binds to the receipt's own key
- **consumes-from** `TOOL-dWellOiledMachine-57` — `check_request_proof` and `--request-check`, the request proof S1 still requires

## 4. Design

### Evidence

- 27 S3 ratifies a mailbox receipt whose `proof` names "a request whose ref passes
  `check_request_proof`" (`spec-27.md:47-52`), and 27 S2 takes `--proof` from whatever ref the
  message names (`spec-27.md:38-45`).
- 57 S6 checks that ref's own chain, identity, sha and proof (`spec-57.md:64-70`) and compares nothing
  with the receipt.
- 27 AC2 plants only a forged proof line (`spec-27.md:168-171`), never a valid proof for another key.

### Files touched (estimate)

- `tools/runtime/intake.py`: S1, S2
- `tools/runtime/intake.py`'s fixture case `borrowed-proof`

### Alternatives rejected

- **Comparing the request's `redacted-sha` with the intake's text.** It needs the request body
  fetched and re-hashed at every ratification, where the two content keys are already on disk and
  derived by one function.

## 5. Production-readiness checklist

- security — a non-owner text can no longer ride an owner's request proof into a build placement.
- perf / scale — one string compare before the existing request check.
- error / empty / loading states — a receipt with `proof=none` does not ratify, as today.
- observability — S2's line names the key the proof pointed at.
- risks — a mailbox message that re-words an owner's request no longer ratifies; it routes to an
  owner breakpoint (27 S4), which is the conservative outcome.
- testing — AC1, AC2 and the arm in §7.
- migration — none.
- user docs — `help/runtime.md`'s intake section names the rule.

## 6. Acceptance criteria

- **AC1** — When `python intake.py fixture --case borrowed-proof` files a mailbox intake whose text
  differs from a published owner request and whose `proof` names that request's valid ref,
  `python intake.py ratifies <key>` prints `does not ratify · mailbox · proof names` and exits 1.
  Red when: the borrowed proof ratifies, as 27 S3 alone lets it.
- **AC2** — When `--case proof` files a mailbox intake carrying the owner's request text verbatim with
  its own key as `proof`, `ratifies` prints `ratifies · mailbox`.
  Red when: a verbatim, proven request is refused.

## 7. Gates

`policy fixtures` · `lexicon naming predicates` · `memory hygiene`

New arm: tools/runtime/selftest.py · covers AC1 AC2 · the borrowed-proof case staged against a ratification that checks only the named ref · none

## 8. Open questions

none

## 9. Revision log

- rev-1 · 2026-10-27 · initial draft, promoted from the spec audit round 1, finding 62 (H13).

## 10. Reuse audit

The seam extended is 27 S3's `check_intake_ratifies`, given one compare between keys that
`derive_request_content_key` (TOOL-dPlacedRequest-19 S1) already derives for both records. The probe
`python tools/codebase-map/reuse_lookup.py "ratify a mailbox intake only with its own request proof"`
ranked `owners_of`, `check_gen_region_only` and `check_lease_only_diff` by name stem, none a proof
check, so no other seam fits.

Recall terms used: `python tools/memory-recall/query.py "which intake receipt ratifies a build
request" --terms "intake ratify mailbox proof request content key check_request_proof owner borrowed"`
