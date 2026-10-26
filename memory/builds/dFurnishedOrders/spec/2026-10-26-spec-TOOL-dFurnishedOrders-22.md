# TOOL-dFurnishedOrders-22 — a verifier's subject declared as the input slots it reads, `subject-reads`, checked against `reads` and `verifies` and written into the role index

**Status:** OPEN · rev-1 · 2026-10-26 · node d · Tier-2 · base 5ff43572 · streams tooling · order 12 · advances TOOL-dFurnishedOrders-21

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-26-build-TOOL-dFurnishedOrders-22-round1-fix-return.md](../build/2026-10-26-build-TOOL-dFurnishedOrders-22-round1-fix-return.md) | research | TOOL-dFurnishedOrders-29 TOOL-dFurnishedOrders-30 |
| [2026-10-26-prompt-TOOL-dFurnishedOrders-22-round1-fix-brief.md](../prompts/2026-10-26-prompt-TOOL-dFurnishedOrders-22-round1-fix-brief.md) | research | TOOL-dFurnishedOrders-29 TOOL-dFurnishedOrders-30 |

<!-- /gen:spec-records -->

## 1. Goal

The round-1 spec audit of the 20 unit specs
(`memory/builds/dFurnishedOrders/reviews/2026-10-26-review-TOOL-dFurnishedOrders-1-spec-audit-round1.md`)
confirmed finding **id 1 at BLOCKER**, report item **B1**. Id 48 shares that item and takes
`TOOL-dFurnishedOrders-23`.

`TOOL-dFurnishedOrders-6` S4 exempts a matched read only when it sits under a `### input:<name>` block
whose `<name>` the role's `verifies` names, and `TOOL-dFurnishedOrders-5` S1 fixes `verifies` to the
class words `subject`, `claim` and `verdict`. A work order's input blocks are named after the slots a
role reads: the only `input:` slots any `reads:` line under `tools/roles/agents/` names are `input:spec`, `input:diff`,
`input:question` and `input:prompt` (`gov-builder.agent.md:7`, `gov-diff-reviewer.agent.md:7`,
`gov-orienter.agent.md:8`, `gov-skeptic.agent.md:7`, `gov-spec-reviewer.agent.md:7`, read at base
`5ff43572`). No block a real work order carries can match a class word, so under the default `refuse`
a reviewer is refused the spec or diff it reviews. Nothing declares which slot is a verifier's subject.

This unit declares it: a role field `subject-reads` naming the `input:` slots whose read is the role's
verification, checked both ways against the role's `reads` and `verifies`, and written into
`.claude/roles.json` for the hook. It repairs `TOOL-dFurnishedOrders-6` and builds one step after it
(order 12); `TOOL-dFurnishedOrders-23` re-keys the hook's exemption on the field.

## 2. Scope (IN)

- **S1** — The field. One `[[field]]` row in `tools/roles/role-schema.toml`, in TOOL-dBoundRoles-2
  S1's grammar as `TOOL-dFurnishedOrders-5` S1 writes `verifies`: `key = "subject-reads"`,
  `owner = "gov"`, `shape = "list"`, `required = "every"`. Its value is `none` or a list of `input:`
  slot keys. Every role file present at the pass carries it, per §4 "The values". Observed by AC1.
- **S2** — The check, both ways, in `tools/roles/check_roles.py` beside R3's `reads` checks
  (`check_roles.py:200-210`): a role whose `verifies` is not `none` and whose `subject-reads` is
  `none` is a defect; a role whose `verifies` is `none` and whose `subject-reads` names a slot is a
  defect; an entry that is not an `input:` key, or that the same role's `reads` does not list (with
  or without its `?`), or that is named twice, is a defect. Each defect is `R3`, naming the role and
  the entry. Observed by AC2.
- **S3** — The index. `render_roles_index` (`tools/roles/render_agents.py:207-216`) writes each role's
  `subject-reads` list into its `.claude/roles.json` entry beside `verifies`, `[]` for `none`, the key
  spelled as the field is, so the hook reads one spelling. `render_agents.py --write` re-renders the
  index and `.claude/agents/`. Observed by AC1.
- **S4** — The docs. `tools/roles/README.md`'s field table and `help/roles.md`'s "What each agent line
  tells you" name `subject-reads`: the slots a verifier re-checks, and the only reads the answered-call
  hook never refuses it. Observed by AC3.

## 3. Non-goals (OUT)

- The hook's exemption reading the field, and the arms that certify it on the shipped roles:
  `TOOL-dFurnishedOrders-23`, for id 48.
- The `verifies` field, its class words and the `## Trust` block that renders them:
  `TOOL-dFurnishedOrders-5`'s, unchanged. The class says what a verifier does; this field says where
  its subject arrives.
- Rewording `TOOL-dFurnishedOrders-6`'s spec text. Its ledger answers AC2 in the AMENDED form, naming
  units 22 and 23.
- The report's left-shift gate, a spec-lint over planted block names: no clause of this build names it.

### Edges

- **consumes-from** `TOOL-dFurnishedOrders-5` — `verifies` and the index entry `render_roles_index` writes it into, beside which S3 writes `subject-reads` and against which S2 checks it (id 1)
- **consumes-from** `TOOL-dFurnishedOrders-15` — the re-founded `gov-tester` role file, its `reads` and its `verifies`, which S1 gives a `subject-reads` value (id 1)
- **hands-off** `TOOL-dFurnishedOrders-23` — `subject-reads`, the index key the answered-call hook keys a verifier's exemption on (ids 1 and 48)

## 4. Design

### The values

Item 5 of layer-roles `[trust]`
(`memory/builds/dClosedLoop/build/2026-10-15-build-PLAY-dClosedLoop-1-layer-roles.md:277-285`) names
each verifier's subject: the reviewer the pinned artifact, the skeptic each finding's cited source, the
tester each red of the verdict. The slot each subject arrives in is the role's own `reads` line.

| Role | `reads` at base | `verifies` (unit 5) | `subject-reads` |
|---|---|---|---|
| `gov-spec-reviewer` | `input:spec`, … | `subject` | `input:spec` |
| `gov-diff-reviewer` | `input:diff`, `input:spec?` | `subject` | `input:diff` |
| `gov-skeptic` | `input:diff?`, `input:spec?` | `claim` | `input:diff`, `input:spec` |
| `gov-tester` (unit 15) | `input:spec`, `input:diff?`, `input:question?` | `verdict`, `claim` | `input:diff`, `input:question` |
| `gov-reviewer` (TOOL-dBoundRoles-1's merged reviewer, if present at the pass) | its `input:` slots | `subject` | `input:spec`, `input:diff` |
| every other role | — | `none` | `none` |

The diff reviewer's `input:spec` is its criterion and the tester's `input:spec` its criterion, so
neither is a subject: a verifier re-reading its handed criterion stays an answered call, as unit 6 F6
settled. The skeptic's two optional slots each carry the source a finding cites, so both are subject.
A merged reviewer reviews a spec or a diff, and its subject is whichever it is handed (§8 F2).

### The check

```
verifies none     and subject-reads none       ok
verifies <class>  and subject-reads <slots>    ok when every slot is an input: key the role's reads lists
verifies <class>  and subject-reads none       R3: a verifier with no subject slot
verifies none     and subject-reads <slots>    R3: a subject slot on a role that verifies nothing
```

The check reads only the role file, so it holds in every adopter the roles kit renders, and no hook or
fixture can declare a subject a role does not read.

### Inventory

Minted: the role field `subject-reads` and its index key of the same spelling. No function: S2 is a
branch of `check_roles`, S3 one entry of `render_roles_index`'s dictionary.

### Migration

Additive to the role grammar: every role file the kit ships carries the field from this pass, and an
adopter's house overlay carries no front matter, so nothing of the adopter's is re-keyed. An index
rendered before this unit has no `subject-reads` key; the hook reads an absent key as `[]`
(`TOOL-dFurnishedOrders-23` S2).

### Rollout

Live at landing. `KIT_ROLES_VERSION` in `tools/roles/roles_lib.py` moves for the kit epoch leg.

### Files touched (estimate)

- `tools/roles/role-schema.toml`
- `tools/roles/check_roles.py`
- `tools/roles/render_agents.py`
- `tools/roles/roles_lib.py`
- `tools/roles/agents/`
- `tools/roles/adopt-roles.test.sh`
- `tools/roles/README.md`
- `help/roles.md`
- `.claude/agents/` and `.claude/roles.json` (renders, by `render_agents.py --write`)

### Alternatives rejected

- **Spell `verifies` entries as input keys.** It re-spells `TOOL-dFurnishedOrders-5`'s J2 field, which
  the `## Trust` block renders as the design's class words and unit 15 gives the tester; one field
  would then carry two meanings (§8 F1).
- **A table in `roles_lib.py` mapping each role to its subject slots.** A second place naming the
  roles, typed beside the role files it describes, which the charter's `[one-fact]` rule refuses.
- **Derive the subject as the role's required `input:` slots.** The tester's required slot is
  `input:spec`, its criterion, so the rule names the wrong slot for a shipped verifier.

## 5. Production-readiness checklist

- security — no new write path; the field narrows the hook's exemption to slots a role declares and
  reads, so a fixture or a hand-edited index cannot widen it without a role file the check grades.
- perf / scale — one more key per role in the index; the check is linear in the roles.
- error / empty / loading states — every defect names the role and the entry; `none` is explicit.
- observability — the index carries the field for every role, so `.claude/roles.json` shows each
  verifier's subject.
- risks — a verifier whose subject arrives in a slot this table misses is refused that read; the
  check refuses a verifier with no subject slot, so the gap is a red, never a silent refusal.
- testing — AC1 to AC3 by probe, fixture and grep; the arm of §7 at the close.
- migration — additive, per §4.
- user docs — `help/roles.md`, by S4.

## 6. Acceptance criteria

- **AC1** — When `python tools/roles/render_agents.py --write` runs and `python -c` loads
  `.claude/roles.json`, the entry `gov-spec-reviewer` carries `subject-reads` `["input:spec"]`,
  `gov-diff-reviewer` `["input:diff"]`, `gov-skeptic` `["input:diff", "input:spec"]` and `gov-builder`
  `[]`; and every value of every entry is an `input:` key that the same role's `reads` line lists.
  Red when: the index carries class words or no key, so the hook has no slot to compare a block with.
- **AC2** — When `python tools/roles/check_roles.py` runs over a scratch copy of the kit in which
  `gov-skeptic.agent.md` carries `subject-reads: input:claim`, it exits 1 with an `R3` defect naming
  `gov-skeptic` and `input:claim`; with `subject-reads: none` it names a verifier with no subject slot;
  with `gov-builder.agent.md` carrying `subject-reads: input:spec` it names a subject slot on a role
  that verifies nothing; with the shipped files it prints no `R3` defect.
  Red when: a role declares a subject slot it never reads, which is the synthetic population id 48
  names.
  fixture: a scratch copy of `tools/roles/` under `%TEMP%`, built by the pass.
- **AC3** — When `grep -n "subject-reads"` runs over `help/roles.md` and `tools/roles/README.md`, each
  prints a line saying the field names the slots a verifier re-checks.
  Red when: a user meets a verifier's exempt read with no page naming the field that decides it.

## 7. Gates

`roles catalogue` · `roles render wiring` · `roles render selftest` · `roles adopter self-test` · `check-wiring self-test` · `lexicon naming predicates` · `policy fixtures` · `kit epoch (shipped bytes move, the version moves)` · `memory hygiene` · `spec tokens (a spec's own names resolve)`

New arm: tools/roles/adopt-roles.test.sh · covers AC1 AC2 · the shipped index's four verifier entries and the three planted role-file defects, staged by writing `verifies` into `subject-reads` · none

## 8. Open questions

- **F1 — Where does a verifier's subject slot live?** Options: (a) a role field `subject-reads`,
  checked against `reads` and `verifies`; (b) `verifies` entries spelled as input keys; (c) a table in
  `roles_lib.py`. (b) gives `TOOL-dFurnishedOrders-5`'s field two meanings and changes the `## Trust`
  line unit 5 renders; (c) names the roles a second time, beside their files. RESOLVED (agent,
  2026-10-26, delegated): (a), rung 3, the most feature-rich survivor: it is the only option a check
  can hold both ways in an adopter. widens: none · relaxes: none
- **F2 — Which slots are each shipped verifier's subject?** Options: (a) the table of §4, the
  criterion slot left out for the diff reviewer and the tester; (b) every `input:` slot a verifier
  reads. (b) exempts a verifier re-reading its criterion, which unit 6 F6 settled against. RESOLVED
  (agent, 2026-10-26, delegated): (a), rung 1, layer-roles `[trust]` item 5 and unit 6 F6. widens:
  none · relaxes: none
- **F3 — Which binding line does a unit the spec audit promoted carry?** Options: (a) `**Derived:**`
  naming `PLAY-dClosedLoop-2`; (b) a part carry of `TOOL-dFurnishedOrders-6`'s clause, which that unit
  carries whole. (b) splits a whole carry (veto 1). RESOLVED (agent, 2026-10-26, delegated): (a),
  rung 3, the precedent `TOOL-dBoundRoles-39` §8 F1 records. widens: none · relaxes: none
- **F4 — The units this one extends are unbuilt.** `TOOL-dFurnishedOrders-5`, `-6` and `-15` and
  TOOL-dBoundRoles-2's `role-schema.toml` are specced and unbuilt at `5ff43572`. RESOLVED (agent,
  2026-10-26, delegated): the build run re-grounds on each at the pass and stops this unit if a named
  section is still absent then, rung 1, the brief's rule for unbuilt parents. widens: none ·
  relaxes: none

## 9. Revision log

- rev-1 · 2026-10-26 · initial draft, promoted from the round-1 spec audit of the 20 unit specs, id 1
  (BLOCKER, item B1, shared with id 48).

## 10. Reuse audit

The seams extended: `render_roles_index` (`tools/roles/render_agents.py:207-216`), the one writer of
the role index the hooks read, and R3's `reads` walk in `check_roles` (`tools/roles/check_roles.py:200-210`),
the one reader of a role's slots, which S2 joins to the new field. `python
tools/codebase-map/reuse_lookup.py "a role field declaring which input slots a verifier re-checks,
written into the role index"` ranked name stems (`check`, `field`, `build_index`), none a role field or
a subject declaration, so no existing seam fits beyond the two named. The recall probe returned
`TOOL-dFurnishedOrders-6`, the audit's B1 text and the spec brief's J2 row, none disagreeing with
source.

Recall terms used: `python tools/memory-recall/query.py "which input slot does a verifier role read as
its subject" --terms "verifies subject claim verdict input:spec input:diff reads exemption
answered-calls verifier role index"`
