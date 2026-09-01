# DEPL-dGaugedVintage-3 — a default kit must not report adopted while landing no program

**Status:** OPEN · rev-2 · 2026-09-01 · node d · Tier-2 · base d65da7ab · streams deployer · order 2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-09-01-review-DEPL-dGaugedVintage-1-spec-audit-round1.md](../reviews/2026-09-01-review-DEPL-dGaugedVintage-1-spec-audit-round1.md) | spec-audit | DEPL-dGaugedVintage-1 DEPL-dGaugedVintage-2 DEPL-dGaugedVintage-4 DEPL-dGaugedVintage-5 DEPL-dGaugedVintage-6 DEPL-dGaugedVintage-7 DEPL-dGaugedVintage-8 DEPL-dGaugedVintage-9 DEPL-dGaugedVintage-10 DEPL-dGaugedVintage-11 |

<!-- /gen:spec-records -->

## 1. Goal

`memory-recall` is a registry default whose engine files are `role = "forked"`, which
`LANDABLE_ROLES` excludes, so `apply` writes no query CLI into a fresh target while rendering a Skill
that instructs an agent to run it. Make that state loud.

## 2. Scope (IN)

- **S1** — `apply` DETECTS the state: an entry is selected, its rendered artifacts land, and every
  file that would carry its executable behaviour is withheld by a non-landable role. The detection
  reads `resolve_entry`'s `unlanded` return, never a list of kit names.
- **S2** — On detection against a target that does NOT already hold those files, `apply` reports the
  entry as INCOMPLETE rather than adopted, naming each withheld path and, from `UNLANDED_REASON`, the
  sentence for the role that withheld it.
- **S3** — The operator is told what to do about it. The remedy is the adopter's own copy step, NOT a
  seed — see §3 and F1 — and S3 is graded by AC5.
- **S4** — A regression gate over the CLASS, not the instance: `apply` over a scratch target with no
  pre-existing files must not report an entry adopted while its executable files are absent. The
  fixture carries a SECOND, synthetic entry in the same state, because one live instance ships today.

## 3. Non-goals (OUT)

- **Seeding a `forked` file on first install.** This is SUPERSEDED, not open.
  `memory/builds/dCarriedReceipt/spec/2026-08-24-spec-DEPL-dCarriedReceipt-10.md:74-76` ruled it out
  verbatim — "**Not** teaching `apply` to install a forked file at first install either. A fork's
  whole claim is that gov's bytes are wrong for the target, and that claim does not weaken because
  the target's copy is absent" — and `tools/govkit/govkit.py:247-252` carries the same ruling in
  code. Reversing it needs an owner ratification under a new id, which F1 asks for explicitly rather
  than assuming.
- Changing what `forked` means for a target that ALREADY holds those files. Same ratification.
- Adding `forked` to the landable set. That set is DERIVED at `tools/govkit/govkit.py:1776` from
  `ROLE_KINDS` at `:1749`; the edit site is the table, and see §4 on the shadowed duplicate.
- Rewriting `SKILL.template.md` so it stops naming the CLI. The Skill is correct; the install is not.

## 4. Design

### Inventory

| Fact | Where | Measured |
|---|---|---|
| `memory-recall` is a registry default | `tools/govkit/registry.toml:36` | yes |
| `query.py`, `extract.py`, `recall-opened.js` are `forked` | `tools/memory-recall/kit.toml:77-79` | yes |
| `ROLE_KINDS["forked"]` is not `"write"`, so the derived `LANDABLE_ROLES` excludes it | `:1749`, `:1776` | yes |
| `SKILL.template.md` is `rendered` and lands | `tools/memory-recall/kit.toml:28-30` | yes |
| `forked` rules shipping today | `git grep 'role = "forked"' -- '*.toml'` → 1 hit | one, `memory-recall` |
| 1 of 4 landable, 3 `forked` + 3 `project-owned` withheld | `aScouredKit` wave-2 review | recorded as an observation |

**The edit site is `ROLE_KINDS`, not `:236`.** `LANDABLE_ROLES` is bound twice at module level: a
hand-written `("engine", "seed")` at `tools/govkit/govkit.py:236`, and the derived binding at `:1776`
that shadows it. The literal at `:236` is dead and must not be edited or cited as the mechanism.

**One live instance is why S4 carries a synthetic second.** Gating the single shipping case would
certify coverage this unit does not have.

### Rollout

S2 changes an exit condition an adopter sees, so it ships behind the existing outcome machinery: an
entry that cannot complete reports INCOMPLETE and the run's verdict already accounts for a
non-adopted entry.

### Alternatives rejected

Making the Skill conditional on the CLI's presence: it hides the defect where a reader would notice
it, and leaves the adopter with a kit that silently does nothing.

## 5. Production-readiness checklist

- security — N/A. No new content write path.
- perf / scale — S1 reads a return `resolve_entry` already computes; no extra walk.
- a11y — N/A.
- i18n — N/A.
- error / empty / loading states — an entry with no non-landable rule takes the unchanged path and
  says nothing new, so the common case gains no noise.
- observability — the INCOMPLETE report names paths and role sentences, not counts.
- risks — S2 turns a currently-green adopter run red. That is the intent, and it names which entry.
- testing + left-shift gates — S4, with the synthetic second entry.
- migration / rollback — none; no stored shape changes.
- user docs — `WIRE-INTO-PROJECT.md` §3c gains the fresh-target note for this kit.

## 6. Acceptance criteria

- **AC1** — When `python tools/govkit/govkit.py apply` runs over a scratch target holding no
  `memory-recall` files, the entry is reported INCOMPLETE and the report names `query.py` and
  `extract.py` with each one's `UNLANDED_REASON` sentence.
- **AC2** — When the same `apply` runs over a target that ALREADY holds those files, the entry
  reports as it does today and no byte of the target's `query.py` changes, observed by comparing
  `git hash-object` before and after.
- **AC3** — When an entry declares no non-landable rule, its `apply` output is byte-identical to
  today's, observed by diffing the run output over an unaffected kit.
- **AC4** — The S4 gate is observed RED before the fix: run it against current `HEAD` with
  `bash tools/run-gates/run-gates.sh` scoped to that leg and confirm it fails.
- **AC5** — S3's remedy is observable: the INCOMPLETE report names the copy step an adopter runs, and
  `bash tools/check-install-prefix.sh` stays green over the message, so the remedy is not spelled at
  a prefix an adopter does not use.
- **AC6** — S4 exercises the class: the fixture's SYNTHETIC second entry, in the same state and not
  shipping today, is reported INCOMPLETE by the same arm that reports `memory-recall`.

## 7. Gates

`bash tools/run-gates/run-gates.sh` — `govkit selfcheck`, `govkit acceptance matrix`, and
`memory-recall skill wiring`. This unit ADDS the S4 leg with a declared `ceiling`.

## 8. Open questions

- **F1 — refuse, or ask the owner to reverse a ratified non-goal.** §3 records that seeding a
  `forked` file at first install was ruled out by `DEPL-dCarriedReceipt-10` §3 and is carried in code
  at `tools/govkit/govkit.py:247-252`. So the branch this unit can build unilaterally is the REFUSAL:
  report INCOMPLETE and name the adopter's own copy step. The seed branch is available only if the
  owner ratifies the reversal under a new id. Recommendation: build the refusal branch.
  `prior:` `DEPL-dCarriedReceipt-10` §3 says gov's bytes are wrong for a forked target whether or not
  the target's copy is absent. Unresolved — it is the owner's.
- **F2 — whether INCOMPLETE is a new outcome token or an existing one.** Adding a token touches the
  outcome vocabulary every adopter reads. Recommendation: reuse the existing machinery if a token
  fits. `prior:` no prior ruling found. Unresolved.

## 9. Revision log

- rev-1 · 2026-09-01 · initial draft.
- rev-2 · 2026-09-01 · folded round-1 spec audit B4, H5, H9, M3, M4. F1 no longer recommends seeding
  a `forked` file: `DEPL-dCarriedReceipt-10` ratified against it and rev-1 cited nothing, so building
  the recommendation would have reversed a decision by silence. The seed option moved to §3 as
  superseded. §4 and §10 repointed off the shadowed dead `LANDABLE_ROLES:236` onto `ROLE_KINDS:1749`.
  S3 gained AC5 and S4 gained AC6 with a synthetic second entry, since exactly one `forked` rule
  ships. §10 rewritten: two seams existed and rev-1 said none did.

## 10. Reuse audit

- The seam exists and rev-1 missed it. `resolve_entry` (`tools/govkit/govkit.py:282`) already returns
  `unlanded` rows carrying rule index, source, destination and role, and `UNLANDED_REASON`
  (`:242-252`) already holds the per-role sentence explaining why each was withheld. S1 and S2 filter
  and report over that return; they add no walk. `python tools/codebase-map/reuse_lookup.py "land a
  file whose declared role the deployer excludes from writing"` returned only generic writers —
  `write`, `write_text`, `tracked_files` — because the query asked about LANDING BYTES rather than
  about the resolver's return, which is the query's defect and not evidence of absence.
- Recall terms used: `forked role landable engine seed apply target fresh install memory-recall
  query extract rendered skill`
