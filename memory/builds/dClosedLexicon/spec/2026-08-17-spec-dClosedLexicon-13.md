# TOOL-dClosedLexicon-13 — govkit's preview promises writes `apply` will not perform

**Status:** SPECCED · rev-1 · 2026-08-17 · node d · Tier-2 · base b4f0cf1c · streams tooling

## 1. Goal

`plan` and `apply` classify a file rule with two different predicates. `planned_writes`
(`govkit.py:864`) emits `{"kind": "write"}` for every rule that is not `scope = "machine"` and not a
link, whatever its role. `cmd_apply` (`govkit.py:881`) then writes only `role in LANDABLE_ROLES`,
which is `("engine", "seed")`. The four other declared roles — `rendered` (8 rules),
`project-owned` (4), `merged` (3), `generated` (1) — are previewed as writes and never written.

Measured on this tree at `b4f0cf1c`, over the `playbook` entry, which is in the DEFAULT selection:

```
govkit plan  — 2 write(s), 0 side-effect(s), 1 order(s). NOTHING was written.
  write  [project-owned] docs/governance.md   <- playbook
  write  [project-owned] docs/parallel-coding-governance.domain-rules.md   <- playbook
govkit apply — landed 0 file(s)
                                                                      rc=0
```

So the deployer's headline artifact is previewed as a two-file install, and `apply` lands nothing and
exits 0. The backlog row said `apply` "reports it SKIPPED" — measured, it does not: the loop
`continue`s and only an aggregate count is printed, so the skip is invisible on both sides.

The existing plan/apply parity arm (`selftest.py:393`) already knows about this and works around it,
restricting its comparison to `("engine", "seed")` with a comment naming this row. Closing this unit
is what lets that arm quantify over every role, which is the only version of it that would have
caught the defect it was written for.

## 2. Scope (IN)

- **S1** — `plan` classifies with the SAME predicate `apply` writes with. A rule whose role is not in
  `LANDABLE_ROLES` is never `kind: "write"`. It is emitted as `side-effect` when something else in
  the install produces it (`rendered`, `generated` — the kit's adopter runs during `apply`'s CONFIGURE
  step), and as `order` when the target is expected to supply it (`project-owned`).
- **S2** — a `merged` rule is previewed as `BLOCKED`, matching what `apply` actually does with one:
  it refuses the whole install before writing anything (`govkit.py:857`). Today `plan` previews it as
  a write and `apply` refuses, which is the same divergence in the other direction.
- **S3** — `apply` NAMES every rule it skips and why, one line per rule, instead of `continue`-ing
  silently. A verb that declines to do declared work has to say so; the aggregate count cannot.
- **S4** — the parity arm at `selftest.py:393` drops its LANDABLE-role restriction and compares
  plan's `write` set against apply's receipt over EVERY role, on the `**` kit it already uses and on
  the default selection. Its comment loses the workaround and gains the fact that the two predicates
  are now one.
- **S5** — the role→kind mapping is ONE table in the engine, read by both verbs, so a sixth role
  cannot be added on one side only.

## 3. Non-goals (OUT)

- Making any of the four roles landable. Whether `project-owned` is the right role for the playbook's
  two files is a REAL question and it is F1 below, deliberately not answered here: this unit makes the
  preview tell the truth about the roles as declared, and changing what a role MEANS is a descriptor
  and doctrine change with a different blast radius.
- `check`'s behaviour. Grounding this row surfaced a separate and worse defect in the same
  neighbourhood — `govkit check` reported `playbook: landed-but-inert` and exited 0 over a target
  where the playbook was never installed, because the entry's placeholder hole greps two absent files
  and `! grep …` turns grep's rc 2 into success. It is filed as its own row with the measurement
  attached (M3: two designs, two units). This unit does not touch `cmd_check`.
- The `.gitattributes` and gate-runner emitters `apply` already reports as SKIPPED. Those are
  declared-absent, printed, and honest.

## 4. Design

### One predicate, named once

The bug is not that `plan` is wrong about `rendered`. It is that two functions independently decide
what `apply` will do, which is the class this repo keeps a record about — the same file's
`resolve_dests` docstring says it in as many words, and the `**` divergence this arm was written for
was the same shape one level down.

So the fix is a single module-level mapping from role to plan-kind, with `LANDABLE_ROLES` derived
FROM it rather than declared beside it:

```
ROLE_KINDS = {"engine": "write", "seed": "write", "rendered": "side-effect",
              "generated": "side-effect", "project-owned": "order", "merged": "blocked"}
LANDABLE_ROLES = tuple(k for k, v in ROLE_KINDS.items() if v == "write")
```

Deriving `LANDABLE_ROLES` is what makes S5 mechanical rather than a rule someone remembers: a role
added to the table with any kind other than `write` is automatically not landable, and a role added
as `write` is automatically landed, in both verbs, from one edit.

`scope = "machine"` and `link` keep their existing precedence — they are `order` regardless of role,
because they describe an act on the machine rather than on the tree.

### An unknown role must not default to `write`

A rule whose role is absent defaults to `engine` today (`rule.get("role", "engine")`), which is a
write. A role SPELLED but not in the table is the dangerous case: falling back to `write` would
reintroduce exactly this bug for the next role someone adds. It refuses — `selfcheck` and `plan`
both fail naming the unknown role and the entry it came from.

### Data model

No descriptor change. The six roles already in the tree are the table's keys; `selfcheck` asserts
the declared population is a subset of it, which is how a seventh role gets caught at authoring time
rather than at install time.

### Files touched (estimate)

`tools/govkit/govkit.py`, `tools/govkit/selftest.py`. No descriptor edits, no registry edit.

## 5. Production-readiness checklist

- security — narrows what `plan` promises; it cannot cause a write that did not happen before, and
  `apply`'s write condition is derived from the same table so it cannot widen either.
- perf / scale — a dict lookup per rule.
- a11y / i18n — N/A.
- error / empty / loading states — an unknown role refuses rather than defaulting; an absent role
  still defaults to `engine`, which is the documented existing behaviour and is asserted.
- observability — this unit IS observability: S3 makes every skip visible, and the plan marks
  distinguish four outcomes where there was one.
- risks — the real one is mis-mapping a role, which would make the preview confidently wrong in a new
  way. Each of the six mappings is asserted against the behaviour `apply` actually exhibits for that
  role, not against the table itself, so a wrong entry reds.
- testing + left-shift gates — S4, on `python tools/govkit/selftest.py`, already a leg.
- migration / rollback — none. No on-disk format changes; a receipt written before this unit is
  unchanged in shape.
- user docs — the plan legend in `USAGE`, and `tools/govkit/README.md`'s role vocabulary.

## 6. Acceptance criteria

- **AC1** — When `plan` runs over the `playbook` entry, neither `project-owned` row is counted as a
  write, and the summary line reports 0 write(s).
- **AC2** — When `plan` runs over an entry carrying a `merged` rule, that row is marked BLOCKED, and
  `apply` over the same entry refuses — the two agree.
- **AC3** — When `apply` skips a rule, its role, its destination and the reason appear on stdout.
- **AC4** — When plan's write set is compared against the `files` list in
  `.governance/install.json` over the default selection with NO role filter, the two sets are equal.
- **AC5** — When a descriptor declares a role absent from `ROLE_KINDS`, `plan` and `selfcheck` both
  refuse and name the role and the entry.
- **AC6** — When `LANDABLE_ROLES` is derived, it still equals `("engine", "seed")` — asserted against
  a literal, so a table edit that silently changes what lands reds.
- **AC7** — When `bash tools/run-gates.sh` runs on the landing commit, it is green.

## 7. Gates

`python tools/govkit/selftest.py` and `python tools/govkit/govkit.py selfcheck`, both already legs.
No new leg.

## 8. Open questions

- **F1 — is `project-owned` the right role for the playbook's two files?** The entry's own
  `why_no_adopter` says "installation is a copy to an owner-chosen path", which describes a `seed`,
  not a file the target already owns. If that comment is right, govkit installs no playbook today and
  the honest preview this unit ships will say so out loud. OWNER-FACING; filed to the backlog rather
  than decided here, because it changes what the default install DOES rather than what it claims.
  This unit is correct under either answer.

## 9. Revision log

- rev-1 · 2026-08-17 · initial draft. Written from a measured plan/apply pair over the `playbook`
  entry rather than from the backlog row, which named only `rendered` and credited `apply` with a
  SKIPPED report it does not print.

## 10. Reuse audit

`resolve_dests` and `resolve_rule_pool` (`govkit.py:690`, added by `TOOL-dClosedLexicon-4`) are the
precedent and the shape to copy: one function both verbs call, so the preview and the action cannot
disagree. This unit applies the same move one level up, to the classification rather than the path
set — `python tools/codebase-map/reuse_lookup.py "one predicate, two callers"` surfaces that pair and
nothing else with this shape. `ROLE_KINDS` deliberately does NOT reuse the `SYMBOL_KINDS` frozen-
vocabulary idiom from `map_lib.py`: that one rejects unknown members at render time, and this one has
to map rather than merely admit.
