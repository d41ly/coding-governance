# TOOL-dWellOiledMachine-84 — the record door matches a namespace entry exactly or by prefix, so the single attendance ref sits behind its session rule

**Status:** DEFERRED · rev-2 · 2026-10-27 · node a · Tier-2 · base 0689e7fa · streams tooling · order 64 · advances TOOL-dWellOiledMachine-62

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-27-build-TOOL-dWellOiledMachine-84-deviation-841.md](../build/2026-10-27-build-TOOL-dWellOiledMachine-84-deviation-841.md) | deviation | — |
| [2026-10-27-review-TOOL-dWellOiledMachine-80-spec-audit.md](../reviews/2026-10-27-review-TOOL-dWellOiledMachine-80-spec-audit.md) | spec-audit | TOOL-dWellOiledMachine-86 TOOL-dWellOiledMachine-88 TOOL-dWellOiledMachine-82 TOOL-dWellOiledMachine-87 TOOL-dWellOiledMachine-80 TOOL-dWellOiledMachine-83 TOOL-dWellOiledMachine-89 TOOL-dWellOiledMachine-81 TOOL-dWellOiledMachine-85 TOOL-dWellOiledMachine-90 |

<!-- /gen:spec-records -->

## 1. Goal

Promoted from the spec audit of the round-1 promotions
(`memory/builds/dWellOiledMachine/reviews/2026-10-27-review-TOOL-dWellOiledMachine-63-spec-audit.md`),
finding 39, item H5, at HIGH. TOOL-dWellOiledMachine-79 S47 extends TOOL-dWellOiledMachine-58's
session rule to `refs/gov/attendance/`, but TOOL-dWellOiledMachine-3 writes the single ref
`refs/gov/attendance`, with no trailing slash, and 58 S2 runs the door when a ref "sits under" a
namespace spelled with one. The rule never applies: every attendance override write passes the door
with no session check, so an unbound or foreign session can flip a build between attended and
unattended, while 79 S47 and its §5 say every `refs/gov/` write is behind the door. This unit gives
the door's namespace list two entry kinds, a prefix and an exact ref, spells the attendance entry as
the exact ref, and proves a foreign session's attendance write is refused.

## 2. Scope (IN)

- **S1** — Two entry kinds. In the namespace list `write_gov_ref` consults before it runs the door
  (58 S2, as 79 S47 extends it) and in the rule table of `check_writer_binding`
  (`tools/memory-tree/gov_record.py`), an entry ending in `/` matches every ref under it, and an
  entry with no trailing `/` matches that ref exactly. The block stays byte-identical in its three
  carriers, `tools/lib/gov-ref.sh`, `tools/unattended/unattended.sh` and
  `tools/run-gates/post-merge.sh`. Observed by AC1, AC2.
- **S2** — The attendance entry spelled exactly. 79 S47's `refs/gov/attendance/` becomes
  `refs/gov/attendance` in both places, so TOOL-dWellOiledMachine-3 S6's override write runs the door
  and meets the session rule. Observed by AC1, AC3.
  **Readers:** by name: READER NOT IN TREE — the namespace list in `write_gov_ref`'s three carriers and
  `check_writer_binding` in `gov_record.py` are TOOL-dPlacedRequest-11's and TOOL-dWellOiledMachine-58's,
  unbuilt at HEAD, both edited here. by value: NO VALUE READERS — the entry decides whether the door runs, and no other code reads it.
- **S3** — The coverage case. `door_fixture.py --case namespace-coverage` reads every ref
  `refs/gov/<…>` that `git grep -ohE "refs/gov/[a-z-]+/?" -- tools` names under `tools/runtime/`,
  `tools/unattended/` and `tools/memory-tree/`, and prints each one no door entry matches; the exempt
  list names `refs/gov/bar-red` with 58 S2's reason. Observed by AC4.

## 3. Non-goals (OUT)

- No change to which rule a write meets once inside the door: 58 S3 to S5 and 79 S47 stand.
- The fleet-tag and scan-population halves of 79 S47 are findings 6 and 66, carried by the minors
  batch TOOL-dWellOiledMachine-90.

### Edges

- **consumes-from** `TOOL-dWellOiledMachine-79` — S47's extension of the door's session rule to the attendance namespace, whose spelling this unit corrects
- **consumes-from** `TOOL-dWellOiledMachine-58` — `write_gov_ref`'s namespace list, `check_writer_binding` and `door_fixture.py`, which this unit gives the exact-entry kind and its cases
- **hands-off** `TOOL-dWellOiledMachine-94` — S3's population and exempt list, and §7's parity leg (findings 6, 28, 35, 36)

## 4. Design

### Evidence

- Spec 3 writes `refs/gov/attendance` (`spec-3.md:93`) and lists it as a namespace with no trailing
  slash (`spec-3.md:177`).
- 58 S2 runs the door when `<ref>` "sits under" `refs/gov/leases/`, `refs/gov/mail/`,
  `refs/gov/requests/` or `refs/gov/runs/` (`spec-58.md:48-50`).
- 79 S47 extends the session rule to `refs/gov/life/` and `refs/gov/attendance/`
  (`spec-79.md:224-229`), and AC47 tests only `refs/gov/life` (`spec-79.md:481-482`).
- `git grep -n "write_gov_ref()" -- tools` prints nothing at this base: the carriers are
  TOOL-dPlacedRequest-11's, and 58 and 79 edit them before this unit.

### Inventory

| Minted | Kind | Lexicon cell |
|---|---|---|
| `attendance-foreign`, `attendance-owner`, `namespace-coverage` | `door_fixture.py` cases | none |

### Files touched (estimate)

- `tools/lib/gov-ref.sh`, `tools/unattended/unattended.sh`, `tools/run-gates/post-merge.sh`: S1's
  namespace match
- `tools/memory-tree/gov_record.py`: S1, S2
- `tools/memory-tree/door_fixture.py`: the three cases

### Alternatives rejected

- **Spelling the entry both ways.** Two entries for one ref is two answers to one question; the
  exact kind states the single ref once.
- **Moving attendance under `refs/gov/attendance/<slug>`.** It changes TOOL-dWellOiledMachine-3's
  record grammar and its readers to fix a match rule.

## 5. Production-readiness checklist

- security — deny by default kept: an attendance write now meets the session rule; S3 finds the next
  ref a namespace list misses.
- perf / scale — one string compare per entry.
- error / empty / loading states — a ref no entry matches runs no door, as today, and S3 lists it.
- observability — a refusal prints `door — refused · refs/gov/attendance · cross-session`.
- risks — an owner session whose binding is missing can no longer flip attendance; that is the rule.
- testing — AC1 to AC4 and the arm in §7.
- migration — none: no record moves.
- user docs — none: no verb or key a user types changes.

## 6. Acceptance criteria

- **AC1** — When `python door_fixture.py --case attendance-foreign` writes `refs/gov/attendance` from a
  session that is not the build owner's, the verb exits 2 printing `door — refused ·
  refs/gov/attendance · cross-session` and the ref is unchanged.
  Red when: the write is pushed with no session check, as a trailing-slash entry lets it.
- **AC2** — When `--case attendance-owner` writes the same ref from the owner's bound session, the
  write lands.
  Red when: the exact entry refuses its rightful writer.
- **AC3** — When `grep -rn "refs/gov/attendance/" gov_record.py gov-ref.sh`
  runs, it prints nothing.
  Red when: the trailing-slash spelling remains.
- **AC4** — When `--case namespace-coverage` runs, it prints no unmatched ref outside the exempt list.
  Red when: a `refs/gov/` ref the tools write is matched by no entry.

## 7. Gates

`unattended kit gate` · `run-gates canary` · `run-gates gov canary` · `memory hygiene` · `spec tokens (a spec's own names resolve)` · `lexicon naming predicates`

The unattended kit's self-test suites are waived for this build's landing (README rule 8); the door
fixture is this unit's observation.

New arm: tools/memory-tree/door_fixture.py · covers AC1 AC2 AC4 · the attendance cases staged against a namespace list matching by prefix only · none

## 8. Open questions

none

## 9. Revision log

- rev-1 · 2026-10-27 · initial draft, promoted from the spec audit of the round-1 promotions, finding
  39 (H5).
- rev-2 · 2026-10-27 · §3 · Edges: the reciprocal of each edge the spec audit of the round-2
  promotions' promoted units declare on this unit, mirrored from TOOL-dWellOiledMachine-94.

## 10. Reuse audit

The seam extended is TOOL-dWellOiledMachine-58's door and its namespace list in `write_gov_ref`, the
one gate on a `refs/gov/` write. The probe `python tools/codebase-map/reuse_lookup.py "match a ref
against a door namespace exactly"` ranked `match_expr`, `matchers_of` and `resolve_base_ref` by name
stem, none a ref matcher; the recall query below ranked scout C's row on TOOL-dWellOiledMachine-58,
the door this unit extends.

Recall terms used: `python tools/memory-recall/query.py "which refs does the record door gate" --terms
"record door namespace refs gov attendance prefix exact session rule write_gov_ref GOVREF_DOOR"`
