# TOOL-dFurnishedOrders-32 — a reviewer's subject read from the roster present at the pass: the merged reviewer's subject is the first slot of a `subject-reads` group its work order hands, so its criterion stays non-exempt

**Status:** DEFERRED · rev-2 · 2026-10-27 · node d · Tier-2 · base 8c395e3c · streams tooling · order 13 · advances TOOL-dFurnishedOrders-21

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-27-review-TOOL-dFurnishedOrders-31-spec-audit-round1.md](../reviews/2026-10-27-review-TOOL-dFurnishedOrders-31-spec-audit-round1.md) | spec-audit | TOOL-dFurnishedOrders-35 TOOL-dFurnishedOrders-36 TOOL-dFurnishedOrders-31 TOOL-dFurnishedOrders-33 TOOL-dFurnishedOrders-34 TOOL-dFurnishedOrders-37 |

<!-- /gen:spec-records -->

## 1. Goal

The spec audit of the round-1 promotions
(`memory/builds/dFurnishedOrders/reviews/2026-10-26-review-TOOL-dFurnishedOrders-22-spec-audit-round1.md`)
confirmed finding **id 2 at HIGH**, report item **H2**. No other id shares it.

`TOOL-dFurnishedOrders-22` §4 plans for `gov-reviewer`, TOOL-dBoundRoles-1's merged reviewer, "if
present at the pass", with `subject-reads` `input:spec` and `input:diff`. Its AC1, and
`TOOL-dFurnishedOrders-23` AC1 and AC2, hard-code `gov-spec-reviewer` and `gov-diff-reviewer`, which
TOOL-dBoundRoles-1 S3 removes; dBoundRoles is this build's parent (README front matter `parents:
dBoundRoles`). Once the merge lands those criteria name roles that do not exist. And with both slots
in a flat `subject-reads`, a merged reviewer's re-read of the spec handed to a diff review as its
criterion is exempt, which re-opens what unit 22 F2 and unit 6 F6 settled against.

This unit makes a reviewer's subject a function of the slots its work order hands: a `subject-reads`
group `input:diff|input:spec` names one subject, the first member the order carries. It writes the
criteria against the roster present at the pass. It repairs `TOOL-dFurnishedOrders-22` and builds one
step after it (order 13), after `TOOL-dFurnishedOrders-23`, which shares unit 22's order.

## 2. Scope (IN)

- **S1** — The group entry. A `subject-reads` entry may be a group, two or more `input:` slot keys
  joined by `|`. R3 in `tools/roles/check_roles.py` (`TOOL-dFurnishedOrders-22` S2) checks each
  member as it checks a plain entry, and a group of one member, or a member named twice in one role's
  value, is an `R3` defect naming the role and the entry. Observed by AC2.
- **S2** — The index keeps the group. `render_roles_index` (`tools/roles/render_agents.py:207-216`,
  `TOOL-dFurnishedOrders-22` S3) writes a group as one string, `input:diff|input:spec`, so the hook
  reads the group as the role file spells it. Observed by AC1.
- **S3** — The hook resolves a group. In `checkAnsweredCall` (`tools/roles/answered-calls.js`,
  `TOOL-dFurnishedOrders-23` S1), a group's subject is the first member whose `### <slot>` block the
  work order carries; a read under that block runs unrecorded, and a read under any other member's
  block takes the policy as any answered call does. A plain entry is unchanged. Observed by AC3.
- **S4** — The merged reviewer's value. Where `tools/roles/agents/gov-reviewer.agent.md` is present at
  the pass, it carries `subject-reads: input:diff|input:spec`: a diff review, handed both slots, has
  its diff as subject and its spec as criterion; a spec review, handed the spec alone, has its spec
  as subject. Where the two reviewers are present instead, unit 22's values stand. Observed by AC1.
- **S5** — The criteria read the roster. The arm `TOOL-dFurnishedOrders-23` S3 draws from
  `.claude/roles.json` plants, for each group entry, a work order handing every member and one handing
  each later member alone, so the group's cases are drawn from the index as the plain ones are. Units
  22 and 23 answer their AC1 and AC2 in the AMENDED form in their ledgers, naming this unit's AC1 and
  AC3. Observed by AC1 and AC3.
- **S6** — The docs. `tools/roles/README.md`'s field row and `help/roles.md`'s "What each agent line
  tells you" say a group names one subject, the first slot the work order hands. Observed by AC4.

## 3. Non-goals (OUT)

- The merge itself, its role file and its rename step: TOOL-dBoundRoles-1 S3 and TOOL-dBoundRoles-18.
  This unit writes `gov-reviewer`'s `subject-reads` line only where that file is present.
- The field, the plain-entry check and the index entry: `TOOL-dFurnishedOrders-22`'s, unchanged. The
  exemption on a plain entry: `TOOL-dFurnishedOrders-23`'s, unchanged.
- A step-keyed subject read from the work order's step (§8 F1).
- The report's left-shift gate, a spec-lint joining role names in criteria to the parent's renames: no
  clause of this build names it.

### Edges

- **consumes-from** `TOOL-dFurnishedOrders-22` — `subject-reads`, its R3 check and its index entry, which S1 and S2 extend with the group form, and AC1 whose reviewer rows S5 re-reads from the roster (id 2)
- **consumes-from** `TOOL-dFurnishedOrders-23` — `checkAnsweredCall`'s subject comparison and the index-drawn arm, which S3 and S5 extend to a group, and AC1 and AC2 whose reviewer rows S5 re-reads from the roster (id 2)
- **hands-off** `TOOL-dFurnishedOrders-37` — the group entry, whose members unit 37 S27 checks for `?` (id 43)
- **hands-off** `TOOL-dFurnishedOrders-42` — S1's duplicate-member case and AC2's fixture, which unit 42 S9 and S10 settle (ids 6, 25 of the third audit)

## 4. Design

### The values by roster

| Roster at the pass | Role | `reads` | `subject-reads` |
|---|---|---|---|
| merged (TOOL-dBoundRoles-1 landed) | `gov-reviewer` | its `input:` slots, `input:spec` and `input:diff` among them | `input:diff\|input:spec` |
| unmerged | `gov-spec-reviewer` | `input:spec`, … | `input:spec` (unit 22) |
| unmerged | `gov-diff-reviewer` | `input:diff`, `input:spec?` | `input:diff` (unit 22) |
| either | `gov-skeptic` | `input:diff?`, `input:spec?` | `input:diff`, `input:spec` (unit 22) |

The skeptic keeps two plain entries: each slot carries a source a finding cites, so both are subject
(unit 22 F2). The merged reviewer gets one group, because one of its two slots is a criterion
whenever both are handed.

### The decision after this unit

```
read under ### <slot>, role = index.roles[agent_type]
  for entry in role['subject-reads']:
    plain entry  == <slot>                                   -> run, unrecorded
    group entry  first member the order hands == <slot>      -> run, unrecorded
  else                                                       -> readPolicy('roles.answered-calls')
```

The hook already finds the `### input:` block a read was handed under (unit 6 S4), so the handed set
is the order's own headings and costs no second read.

### Inventory

Minted: the group form of a `subject-reads` entry and its `|` separator. No function.

### Migration

Additive: a plain entry reads as before, and an index without groups is unchanged.

### Rollout

Live at landing. `KIT_ROLES_VERSION` moves for the kit epoch leg.

### Files touched (estimate)

- `tools/roles/check_roles.py`
- `tools/roles/render_agents.py`
- `tools/roles/answered-calls.js`
- `tools/roles/answered-calls.test.sh`
- `tools/roles/adopt-roles.test.sh`
- `tools/roles/roles_lib.py`
- `tools/roles/agents/`
- `tools/roles/README.md`
- `help/roles.md`
- `.claude/agents/` and `.claude/roles.json` (renders, by `render_agents.py --write`)

### Alternatives rejected

- **Keep the two hard-coded reviewer names.** They fail on the merged roster the parent lands first.
- **A flat `input:spec`, `input:diff` on the merged reviewer.** Its criterion read becomes exempt in
  every diff review, which unit 6 F6 refused.

## 5. Production-readiness checklist

- security — no new write path; a group exempts at most one slot per order, never more than a plain
  entry would.
- perf / scale — one scan of the order's headings per matched read, already made.
- error / empty / loading states — a malformed group is an `R3` defect before the index is written.
- observability — the index shows the group; a refused criterion read names its block, as unit 6
  records it.
- risks — a work order handing the criterion slot before the subject slot still resolves by the
  group's order, not the order's, since the group lists the subject first.
- testing — AC1 to AC4 by probes, fixtures and greps; the arms of §7 at the close.
- migration — none.
- user docs — `help/roles.md`, by S6.

## 6. Acceptance criteria

- **AC1** — When `python tools/roles/render_agents.py --write` runs and `python -c` loads
  `.claude/roles.json`: where the index holds `gov-reviewer`, its `subject-reads` is
  `["input:diff|input:spec"]` and neither `gov-spec-reviewer` nor `gov-diff-reviewer` is an entry;
  otherwise `gov-spec-reviewer` carries `["input:spec"]` and `gov-diff-reviewer` `["input:diff"]`; and
  every member of every entry is an `input:` key the role's `reads` line lists.
  Red when: a criterion names a reviewer the roster no longer holds, or the merged reviewer's value
  exempts both slots.
- **AC2** — When `python tools/roles/check_roles.py` runs over a scratch copy of the kit in which
  `gov-diff-reviewer.agent.md` carries `subject-reads: input:diff|input:claim`, it exits 1 with an
  `R3` defect naming `input:claim`; with `subject-reads: input:diff|` it names a group of one member;
  with `subject-reads: input:diff|input:spec` it prints no `R3` defect.
  Red when: a group member the role never reads is admitted.
  fixture: a scratch copy of `tools/roles/` under `%TEMP%`, built by the pass.
- **AC3** — When `node answered-calls.js` reads a `Read` payload of the role whose index entry holds
  the group, its work order handing `### input:diff` and `### input:spec`, a read under
  `### input:diff` exits 0 with no record and a read under `### input:spec` exits 2 recording
  `refused`; with an order handing `### input:spec` alone, the read under it exits 0 with no record.
  Red when: a diff review's criterion read is exempt, or a spec review is refused its subject.
  fixture: the AC2 scratch kit's rendered index copied into a scratch repository under `%TEMP%`; once
  TOOL-dBoundRoles-1 has landed, the shipped `gov-reviewer` entry instead.
- **AC4** — When `grep -n "first slot the work order hands"` runs over `help/roles.md` and
  `tools/roles/README.md`, each prints a line.
  Red when: a user cannot learn which of a merged reviewer's slots is its subject.

## 7. Gates

`roles catalogue` · `roles render wiring` · `roles render selftest` · `roles adopter self-test` · `check-wiring self-test` · `policy fixtures` · `kit epoch (shipped bytes move, the version moves)` · `lexicon naming predicates` · `memory hygiene` · `spec tokens (a spec's own names resolve)`

The leg `answered-calls self-test` is `TOOL-dFurnishedOrders-6`'s, not in the manifest at base, so it
is named here in prose; this unit's hook arm runs under it.

New arm: tools/roles/answered-calls.test.sh · covers AC3 · the index-drawn plants of a group entry, staged by exempting every member of a group · none
New arm: tools/roles/adopt-roles.test.sh · covers AC1 AC2 · the roster-read reviewer rows and three planted group values, staged by asserting the two unmerged names on a merged index · none

## 8. Open questions

- **F1 — How does a merged reviewer's criterion slot stay non-exempt?** Options: (a) a `subject-reads`
  group whose subject is the first member the work order hands; (b) a subject keyed by the workflow
  step, read from the work order; (c) a subject per lens. (b) needs the work order to carry its step
  in a shape the hook reads, which no spec of this build states; (c) moves the subject out of the role
  file into dCalibratedLens's lens data, which TOOL-dBoundRoles-1 §3 leaves to that build. RESOLVED
  (agent, 2026-10-26, delegated): (a), rung 3, the most feature-rich survivor: it reads only the
  blocks the hook already reads and keeps one field. widens: none · relaxes: none
- **F2 — Which binding line does a unit the spec audit promoted carry?** RESOLVED (agent, 2026-10-26,
  delegated): `**Derived:**` naming `PLAY-dClosedLoop-2`, rung 3, the precedent `TOOL-dBoundRoles-39`
  §8 F1 records. widens: none · relaxes: none
- **F3 — The units this one extends are unbuilt.** `TOOL-dFurnishedOrders-6`, `-22` and `-23`, and
  TOOL-dBoundRoles-1, are specced and unbuilt at `8c395e3c`. RESOLVED (agent, 2026-10-26, delegated):
  the build run re-grounds on each at the pass and stops this unit if a named section of units 22 or
  23 is still absent then; TOOL-dBoundRoles-1's absence selects the unmerged rows of §4, rung 1, the
  brief's rule for unbuilt parents. widens: none · relaxes: none

## 9. Revision log

- rev-1 · 2026-10-26 · initial draft, promoted from the spec audit of the round-1 promotions, id 2
  (HIGH, item H2).
- rev-2 · 2026-10-27 · §3 · the Edges block gains the **hands-off** bullet(s) mirroring TOOL-dFurnishedOrders-42, promoted from the spec audit of the round-2 promotions (`memory/builds/dFurnishedOrders/reviews/2026-10-27-review-TOOL-dFurnishedOrders-31-spec-audit-round1.md`); nothing else moved.

## 10. Reuse audit

The seams extended: R3's entry check and `render_roles_index` (`tools/roles/check_roles.py:200-210`,
`tools/roles/render_agents.py:207-216`) as `TOOL-dFurnishedOrders-22` extends them, and
`checkAnsweredCall`'s subject comparison as `TOOL-dFurnishedOrders-23` S1 builds it. `python
tools/codebase-map/reuse_lookup.py "a role field declaring which input slots a verifier re-checks,
written into the role index"` ranked name stems (`check`, `field`, `build_index`), none a subject
declaration, so no existing seam fits beyond the ones named. The recall probe returned
TOOL-dBoundRoles-1 S3's merge and the audit's H2 text, neither disagreeing with source.

Recall terms used: `python tools/memory-recall/query.py "which input slot is a merged reviewer's
subject" --terms "gov-reviewer merged reviewer subject-reads input:spec input:diff criterion exemption
answered-calls roster"`
