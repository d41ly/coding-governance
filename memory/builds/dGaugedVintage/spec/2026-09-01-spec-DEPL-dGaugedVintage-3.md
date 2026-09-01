# DEPL-dGaugedVintage-3 — a default kit must not report adopted while landing no program

**Status:** OPEN · rev-1 · 2026-09-01 · node d · Tier-2 · base d65da7ab · streams deployer · order 2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-09-01-review-DEPL-dGaugedVintage-1-spec-audit-round1.md](../reviews/2026-09-01-review-DEPL-dGaugedVintage-1-spec-audit-round1.md) | spec-audit | DEPL-dGaugedVintage-1 DEPL-dGaugedVintage-2 DEPL-dGaugedVintage-4 DEPL-dGaugedVintage-5 DEPL-dGaugedVintage-6 DEPL-dGaugedVintage-7 DEPL-dGaugedVintage-8 DEPL-dGaugedVintage-9 DEPL-dGaugedVintage-10 DEPL-dGaugedVintage-11 |

<!-- /gen:spec-records -->

## 1. Goal

`memory-recall` is a registry default whose engine files are `role = "forked"`, which
`LANDABLE_ROLES` excludes, so `apply` writes no query CLI into a fresh target while rendering a Skill
that instructs an agent to run it. Make that state either impossible or loud.

## 2. Scope (IN)

- **S1** — `apply` DETECTS the state: an entry is selected, its rendered artifacts land, and every
  file that would carry its executable behaviour is withheld by a non-landable role. The detection is
  derived from the descriptor, never a list of kit names.
- **S2** — On detection against a target that does NOT already hold those files, `apply` reports the
  entry as INCOMPLETE rather than adopted, naming each withheld path and the role that withheld it.
- **S3** — A `forked` rule gains an explicit declaration of what a fresh target should receive:
  either a seed copy on first install, or a stated refusal with the adopter's own remedy.
- **S4** — A regression gate: `apply` over a scratch target with no pre-existing `memory-recall`
  files must not report that entry adopted while its CLI is absent.

## 3. Non-goals (OUT)

- Changing what `forked` means for a target that ALREADY holds those files. Overwriting an adopter's
  own `query.py` is the destruction `DEPL-dCarriedReceipt-10` introduced the role to prevent, and it
  stays prevented.
- Adding `forked` to `LANDABLE_ROLES`. That is the one-line change that would land the files and also
  reintroduce the overwrite.
- Auditing the other two kits with `forked` rules. This unit fixes the CLASS in `apply`; whether any
  other entry is in the same state is measured by S1, not assumed here.
- Rewriting `SKILL.template.md` so it stops naming the CLI. The Skill is correct; the install is not.

## 4. Design

### Inventory

| Fact | Where | Measured |
|---|---|---|
| `memory-recall` is a registry default | `tools/govkit/registry.toml:36` | yes |
| `query.py`, `extract.py`, `recall-opened.js` are `forked` | `tools/memory-recall/kit.toml:77-79` | yes |
| `forked` is not landable | `tools/govkit/govkit.py:236` | yes |
| `SKILL.template.md` is `rendered` and lands | `tools/memory-recall/kit.toml:28-30` | yes |
| 1 of 4 landable, 3 `forked` + 3 `project-owned` withheld | `aScouredKit` wave-2 review | recorded, as an observation |

The state is already MEASURED in this repo, in a review table, with no row asking for a fix. This
unit is that row.

### Rollout

S2 changes an exit condition an adopter sees, so it ships behind the existing outcome machinery
rather than as a new refusal class: an entry that cannot complete reports INCOMPLETE and the run's
overall verdict already accounts for a non-adopted entry.

### Alternatives rejected

Making the Skill conditional on the CLI's presence was rejected: it hides the defect at the point a
reader would notice it, and leaves the adopter with a kit that silently does nothing.

## 5. Production-readiness checklist

- security — N/A. No new content write path.
- perf / scale — S1 is a descriptor read per selected entry; no filesystem walk beyond existence.
- a11y — N/A.
- i18n — N/A.
- error / empty / loading states — an entry with no `forked` rule must take the unchanged path and
  say nothing new, so the common case gains no noise.
- observability — the INCOMPLETE report is the observable and names paths, not counts.
- risks — S2 could turn a currently-green adopter run red. That is the intent, and the run reports
  which entry and why rather than failing wholesale.
- testing + left-shift gates — S4.
- migration / rollback — none; no stored shape changes.
- user docs — `WIRE-INTO-PROJECT.md` §3c gains the fresh-target note for this kit.

## 6. Acceptance criteria

- **AC1** — When `python tools/govkit/govkit.py apply` runs over a scratch target holding no
  `memory-recall` files, the entry is reported INCOMPLETE and the report names `query.py` and
  `extract.py` with the role that withheld each.
- **AC2** — When the same `apply` runs over a target that ALREADY holds those files, the entry
  reports as it does today and no byte of the target's `query.py` changes, observed by comparing
  `git hash-object` before and after.
- **AC3** — When an entry declares no non-landable rule, its `apply` output is byte-identical to
  today's, observed by diffing the run output over an unaffected kit.
- **AC4** — The S4 gate leg is observed RED before the fix: run it against current `HEAD` with
  `bash tools/run-gates/run-gates.sh` scoped to that leg and confirm it fails.

## 7. Gates

`bash tools/run-gates/run-gates.sh` — `govkit selfcheck`, `govkit acceptance matrix`, and
`memory-recall skill wiring`. This unit ADDS the S4 leg with a declared `ceiling`.

## 8. Open questions

- **F1 — seed-on-first-install versus refuse.** A `seed` role copies once and then the target owns
  the bytes, which is exactly the fresh-target semantics wanted, and `seed` is already landable.
  Refusing instead keeps `apply` honest but leaves the adopter to copy by hand. Recommendation: seed
  on first install, because the role already exists and carries the right ownership semantics.
  Unresolved.
- **F2 — whether INCOMPLETE is a new outcome token or an existing one.** Adding a token touches the
  outcome vocabulary every adopter reads. Recommendation: reuse the existing machinery if a token
  fits, and only add one if none does. Unresolved.

## 9. Revision log

- rev-1 · 2026-09-01 · initial draft.

## 10. Reuse audit

- No existing seam fits the DETECTION, and the evidence is that
  `python tools/codebase-map/reuse_lookup.py "land a file whose declared role the deployer excludes
  from writing"` returns only generic writers — `write`, `write_text`, `tracked_files` — none of
  which knows about roles. The role vocabulary itself is the seam this extends:
  `LANDABLE_ROLES` and `ROLE_KINDS` at `tools/govkit/govkit.py:236` and `:1776`.
- Recall terms used: `forked role landable engine seed apply target fresh install memory-recall
  query extract rendered skill`
