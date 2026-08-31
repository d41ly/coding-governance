# TOOL-aGradedMandate-2 — `specs-audited`, an eleventh core Definition-of-Done item

**Status:** CLOSED · rev-3 · 2026-08-31 · node a · Tier-2 · base 396cd9db · streams tooling · order 2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-08-31-build-TOOL-aGradedMandate-1-acceptance-ledger.md](../build/2026-08-31-build-TOOL-aGradedMandate-1-acceptance-ledger.md) | journal | TOOL-aGradedMandate-1 TOOL-aGradedMandate-3 TOOL-aGradedMandate-4 TOOL-aGradedMandate-5 TOOL-aGradedMandate-6 TOOL-aGradedMandate-7 TOOL-aGradedMandate-8 TOOL-aGradedMandate-9 TOOL-aGradedMandate-10 TOOL-aGradedMandate-11 |
| [2026-08-31-build-TOOL-aGradedMandate-1-kit-quality-review.md](../build/2026-08-31-build-TOOL-aGradedMandate-1-kit-quality-review.md) | research | TOOL-aGradedMandate-1 TOOL-aGradedMandate-3 TOOL-aGradedMandate-4 TOOL-aGradedMandate-5 TOOL-aGradedMandate-6 TOOL-aGradedMandate-7 TOOL-aGradedMandate-8 TOOL-aGradedMandate-9 |
| [2026-08-31-review-TOOL-aGradedMandate-1-closing-diff-review-round1.md](../reviews/2026-08-31-review-TOOL-aGradedMandate-1-closing-diff-review-round1.md) | diff-review | TOOL-aGradedMandate-1 TOOL-aGradedMandate-3 TOOL-aGradedMandate-4 TOOL-aGradedMandate-5 TOOL-aGradedMandate-6 TOOL-aGradedMandate-7 TOOL-aGradedMandate-8 TOOL-aGradedMandate-9 TOOL-aGradedMandate-10 TOOL-aGradedMandate-11 |
| [2026-08-31-review-TOOL-aGradedMandate-1-spec-audit-round1.md](../reviews/2026-08-31-review-TOOL-aGradedMandate-1-spec-audit-round1.md) | spec-audit | TOOL-aGradedMandate-1 TOOL-aGradedMandate-3 TOOL-aGradedMandate-4 TOOL-aGradedMandate-5 TOOL-aGradedMandate-6 TOOL-aGradedMandate-7 TOOL-aGradedMandate-8 TOOL-aGradedMandate-9 |
| [2026-08-31-review-TOOL-aGradedMandate-1-spec-audit-round2.md](../reviews/2026-08-31-review-TOOL-aGradedMandate-1-spec-audit-round2.md) | spec-audit | TOOL-aGradedMandate-1 TOOL-aGradedMandate-4 TOOL-aGradedMandate-5 TOOL-aGradedMandate-6 TOOL-aGradedMandate-7 TOOL-aGradedMandate-8 TOOL-aGradedMandate-9 |

<!-- /gen:spec-records -->

## 1. Goal

The spec audit binds every unattended run through the `all`-scoped directive `specs-reviewed`, and
no machine anywhere observes it — while `gen_build_index.py` renders the exact gap into every build
README and the run commits that line as part of its own work. This unit adds the Definition-of-Done
item that reads it, so a CLOSED unit no spec audit ever named blocks the close.

## 2. Scope (IN)

- **S1** — Append `specs-audited:machine` to `DOD_CORE` in `tools/unattended/unattended.sh`.
- **S2** — Add its arm to `dod_met`. For every id in the build README's `gen:build-units` region at
  HEAD whose status is `CLOSED`, require a TRACKED record under `<MEMORY_ROOT>/builds/<slug>/` whose
  first twelve unfenced lines carry a `**Serves:**` line of kind `spec-audit` naming that id.
- **S2a** — The id join is WHOLE-TOKEN and EXPANDS the range form. `memory/HYGIENE.md`'s binding
  grammar admits a trailing `@rev-N` and a contiguous run written `N..M`, and 18 of the 123 tracked
  `spec-audit` binding lines use the range form. A substring join is wrong in both directions: it
  blocks a unit that WAS audited under `TOOL-x-1..5`, and it satisfies `TOOL-x-1` from a line naming
  `TOOL-x-19`. `id_in` in `tools/unattended/lib-unattended.sh` gives the whole-token half; the range
  expansion has no seam in this kit and is written here, because the kit copy-installs without
  `gen_build_index.py`, which is the only existing expander.
- **S3** — Raise the Definition-of-Done half of `CORE_FLOOR` in `.unattended.conf` from `10` to
  `11`, with the reason beside the number, since the leg refuses a floor below the kit's own count.
- **S4** — Add the item's row to the §4 table in `tools/unattended/PROTOCOL.template.md` and its
  render `memory/guides/UNATTENDED-PROTOCOL.md`, which two legs byte-compare — AND move the
  count sentence directly above that table from `Ten kit-owned core items.` to `Eleven`. Check 16
  parses that word and fails when it disagrees with `DOD_CORE`, and the byte-identity assertion
  cannot see it: the sentence would be wrong in both copies, which is that arm's own recorded origin.
- **S4a** — Move `CORE_FLOOR` in `tools/unattended/.unattended.conf.example` from `12:10` to
  `12:11` as well. `unattended.test.sh` asserts the example's value equals the driver's two set
  sizes, and the example once shipped a slack floor for the whole life of the file.
- **S5** — The item's own header states what it does NOT check: that the audit found anything, that
  it was performed at the unit's current rev, or that a `WONTDO` unit was ever audited.

## 3. Non-goals (OUT)

- **No new record kind and no new binding grammar.** `spec-audit` is already a member of the closed
  kind set in `memory/HYGIENE.md` under "Record bindings", and `gen_build_index.py --print-bindings`
  is already both the report and the gate's predicate.
- **No leg-side clause.** The join is over a build's own HEAD state at close time; a leg iterating
  every tracked record would grade landed builds this item never bound.
- **No rev-currency term.** The rendered line says "has EVER named", which is a LOWER bound and is
  therefore safe as a refusal condition. Demanding an audit at the unit's current rev is a stricter
  rule nobody has ruled on, and it would red honest folds.

## 4. Design

### Data model

No new fact. The evidence is the `**Serves:** spec-audit <id> …` line already required by
`memory/HYGIENE.md` and already written by the review harness.

### Inventory

| Site | Change |
|---|---|
| `unattended.sh:343` `DOD_CORE` | one entry appended |
| `unattended.sh` `dod_met` | the `specs-audited` arm |
| `.unattended.conf` `CORE_FLOOR` | `12:10` → `12:11` |
| `tools/unattended/.unattended.conf.example` `CORE_FLOOR` | `12:10` → `12:11`, or `unattended.test.sh` reds |
| `PROTOCOL.template.md` §4 · `memory/guides/UNATTENDED-PROTOCOL.md` §4 | one table row AND the count sentence above it, byte-identical |
| `unattended.test.sh` | the refusal arm, the pass arm, and a `WONTDO`-only roster arm |

The walk reuses the `closing-review-recorded` arm's shape: `GIT ls-files` over the build folder,
`GIT grep --cached` for the binding line, so an untracked record is excluded by construction and the
object-substitution lever stays inert through `GIT()`.

### Migration

The item binds only at `--close`, so no landed record changes and the merge bar is untouched. This
build is its own first subject and must satisfy it.

### Alternatives rejected

Reading the rendered `Ids no \`spec-audit\` record has ever named:` line out of the README. Rejected:
that line is generated by the memory-tree kit, and this kit copy-installs standalone without it, so
an adopter would get an item keyed on a line nothing in their tree writes.

## 5. Production-readiness checklist

- security — N/A. Reads tracked bytes the run authored; §9's reduction is unchanged.
- perf / scale — one `ls-files` and one `grep --cached` per build, at close only.
- a11y — N/A. No user surface.
- i18n — N/A. No user surface.
- error / empty / loading states — a build whose units region is empty is already refused by
  `build-complete`; this arm reports "no CLOSED unit to audit" as MET and says so, rather than
  passing silently over an empty selection.
- observability — the refusal lists the unaudited ids by name.
- risks — the item is OVERRIDABLE by design, so a genuinely thin Tier-1 unit becomes a recorded
  decision rather than an invisible skip. It is deliberately not in `DOD_NO_OVERRIDE`.
- testing + left-shift gates — three arms, each observed RED first.
- migration / rollback — removing the entry from `DOD_CORE` and lowering `CORE_FLOOR` reverts it.
- user docs — the Skill's Definition-of-Done prose is not enumerated there, so no change is owed;
  `TOOL-aGradedMandate-8` carries the carrier corrections that are.

## 6. Acceptance criteria

- **AC1** — When a build's units region carries a `CLOSED` id that no tracked record names with a
  `spec-audit` binding line, `--close` blocks on `specs-audited` and the message lists that id,
  verified by an arm in `unattended.test.sh`.
- **AC2** — When every `CLOSED` id is named by such a record, the item is MET.
- **AC3** — When a record naming the id exists on disk but is UNTRACKED, `--close` reports the item
  unmet and the message says the join reads the index, since it walks `GIT ls-files`.
- **AC4** — `bash tools/unattended/check-unattended.sh` stays green with `CORE_FLOOR="12:11"` in
  BOTH `.unattended.conf` and `tools/unattended/.unattended.conf.example`, and reds with `12:10`
  against the new core count, proving the floor pin moved for a reason.
- **AC4a** — AMENDED at rev-4. It named `bash tools/unattended/run-unattended-gates.sh --selftests`,
  which the owner instructed this run to skip mid-build. What is observed instead: the driver suite
  `bash tools/unattended/unattended.test.sh` is GREEN, and it is the suite that reads the example
  conf's `CORE_FLOOR` against the driver's two set sizes — the `--selftests` wrapper only invokes it.
  The wrapper's other four suites are unexercised and the run-state record says so.
- **AC4b** — Check 16 is green: the protocol's count sentence reads `Eleven` and agrees with
  `DOD_CORE`, verified by `bash tools/unattended/check-unattended.sh` reporting no count
  disagreement.
- **AC4c** — A record binding `TOOL-x-1..5` satisfies unit `TOOL-x-5`, and a record binding
  `TOOL-x-19` does NOT satisfy unit `TOOL-x-1`, both verified by arms in `unattended.test.sh`.
- **AC5** — `bash tools/unattended/run-unattended-gates.sh --checks` reports the protocol pair
  byte-identical after the §4 row lands in both copies.

## 7. Gates

`unattended kit gate` · `memory hygiene` · `bash tools/run-gates/run-gates.sh` ·
`bash tools/unattended/run-unattended-gates.sh --selftests`.

## 8. Open questions

none

## 9. Revision log

- rev-1 · 2026-08-31 · authored from finding F3 of
  `build/2026-08-31-build-TOOL-aGradedMandate-1-kit-quality-review.md`.

- rev-2 · 2026-08-31 · round-1 fold of F4, F6 and F8: the id join becomes whole-token with range expansion (S2a), the protocol's spelled-out count sentence joins S4 because check 16 parses it, and the kit example conf's CORE_FLOOR joins the Inventory because unattended.test.sh asserts it.

- rev-3 · 2026-08-31 · the acceptance criterion naming `run-unattended-gates.sh --selftests` is AMENDED: the owner instructed this run to skip that suite mid-build, and the criterion now names what WAS observed instead. The acceptance ledger's AMENDED form exists for exactly this case, so the divergence is visible rather than written untruly.

## 10. Reuse audit

The SET-level probes are recorded in `TOOL-aGradedMandate-1` §10 and are not re-run per spec.

The seam is the `closing-review-recorded` arm's own record walk at
`tools/unattended/unattended.sh:3128` — `GIT ls-files -- "$M/builds/$slug/reviews/*.md"` plus a
`GIT grep --cached -qE '^\*\*Serves:\*\*.*diff-review'`. This unit extends that walk to the
`spec-audit` kind rather than writing a second one, and inherits its stated reasons for reading the
index and for using a local grep instead of the memory-tree parser.

`unit_ids_of` and `unit_rows` at `unattended.sh:1685` and `:1822` already project ids and statuses
out of the generated units region; both are reused. No existing seam covers the CLOSED-status filter,
which is three characters of `grep` inside `unit_rows`'s existing output.
