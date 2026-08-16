# TOOL-dClosedLexicon-13 — govkit's preview promises writes `apply` will not perform

**Status:** CLOSED · rev-2 · 2026-08-17 · node d · Tier-2 · base b4f0cf1c · streams tooling

## 1. Goal

`plan` and `apply` classify a file rule with two different predicates. `planned_writes`
(`govkit.py:531`, emit at `:564`) stamps `{"kind": "write"}` on every rule that is not
`scope = "machine"` and not a link, whatever its role. `cmd_apply` (`govkit.py:881`) then writes only
`role in LANDABLE_ROLES`, which is the hand-written `("engine", "seed")` at `:688`. The four other
declared roles — `rendered` (8 rules), `project-owned` (4), `merged` (3), `generated` (1) — are
previewed as writes and never written.

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

- **S1** — `plan` classifies with the same predicate `apply` acts with. A rule whose role is not in
  `LANDABLE_ROLES` is never `kind: "write"`. The classification is keyed on THREE facts, not on the
  role alone, because the role alone is measurably not enough (§4):
  - **`write`** — role in `LANDABLE_ROLES`.
  - **`blocked`** — role `merged`. `apply` refuses the whole install on one (`govkit.py:857`), so a
    preview calling it a write is the same divergence in the other direction.
  - **`side-effect`** — role `rendered`/`generated` AND the entry declares a producer that `apply`
    actually runs: a non-empty `adopt.argv` with no `blocks_adopt` hole, or a `side_effects` entry
    covering the destination.
  - **`order`** — everything else that is not written: `project-owned`, and any `rendered`/`generated`
    rule whose entry declares no producer. Something outside `apply` must supply it.
  - **`covered`** — a `project-owned` rule whose DESTINATION another rule in the same selection
    writes. Measured, this is not hypothetical: 2 of the 4 `project-owned` rules pair with a sibling
    `seed` rule at the same path.
- **S2** — `apply` NAMES every rule it skips, its role, its destination and why, one line per rule,
  instead of `continue`-ing silently. A verb that declines declared work has to say so; the aggregate
  count cannot.
- **S3** — the mapping is ONE table in the engine, read by both verbs, with `LANDABLE_ROLES` DERIVED
  from it rather than declared beside it, so a role added on one side cannot be missing on the other.
- **S4** — the parity arm at `selftest.py:393` drops its LANDABLE-role restriction and compares plan's
  `write` set against apply's receipt over EVERY role, on the `**` kit it already uses AND on the
  default selection. Its comment loses the workaround and gains the fact that the two predicates are
  now one.
- **S5** — the three documents that STATE plan's promise are corrected together, because leaving one
  is how the promise survives: `cmd_plan`'s mark legend (`govkit.py:590-598`), `planned_writes`'
  docstring (`govkit.py:534`, whose "Machine-scoped rules produce an ORDER" exception list goes stale
  the moment four roles map to non-write kinds), and `skills/deploy-governance/SKILL.md:40-42` — "Lists
  every file `apply` would write, with its role and the source commit its bytes would come from",
  which this build's own `reviews/2026-08-16-review-dClosedLexicon-8.md:96-98` already listed as a
  carrier of the false promise.

## 3. Non-goals (OUT)

- Making any of the four roles landable. Whether `project-owned` is the right role for the playbook's
  two files is a REAL question and it is F1 below, deliberately not answered here: this unit makes the
  preview tell the truth about the roles as declared, and changing what a role MEANS is a descriptor
  and doctrine change with a different blast radius.
- `check`'s behaviour. Grounding this row surfaced a separate and worse defect in the same
  neighbourhood — `govkit check` reported `playbook: landed-but-inert` and exited 0 over a target
  where the playbook was never installed, because the entry's placeholder hole greps two absent files
  and `! grep …` turns grep's rc 2 into success. It is filed as `TOOL-dClosedLexicon-14` with the
  measurement attached (M3: two designs, two units). This unit does not touch `cmd_check`.
- The `.gitattributes` and gate-runner emitters `apply` already reports as SKIPPED. Those are
  declared-absent, printed, and honest.

## 4. Design

### One predicate, named once

The bug is not that `plan` is wrong about `rendered`. It is that two functions independently decide
what `apply` will do — this repo's `two-answers-to-one-question` gotcha class, which
`reuse_lookup.py` surfaces by name. `resolve_dests`' own docstring says it one level down, and the
`**` divergence that arm was written for was the same shape.

So: a single module-level mapping, with `LANDABLE_ROLES` derived FROM it. A role added to the table
with any kind other than `write` is automatically not landable, and a role added as `write` is
automatically landed, in both verbs, from one edit.

`scope = "machine"` and `link` keep their existing precedence — they are `order` regardless of role,
because they describe an act on the machine rather than on the tree.

### Why the role alone is not enough, measured twice

rev-1 mapped `rendered`/`generated` to `side-effect` on the reasoning that "the kit's adopter runs
during `apply`'s CONFIGURE step". CONFIGURE is `argv = d.get("adopt", {}).get("argv") or []` /
`if not argv: continue` (`govkit.py:932-934`), so an entry with an empty adopter runs nothing. Two
entries carrying exactly that declare it in writing:

| entry | rule | `adopt.argv` | its own words |
|---|---|---|---|
| `review-harness` | `REVIEW-PROTOCOL.template.md` → `{memory_root}/guides/REVIEW-PROTOCOL.md` | `[]` | "the render is performed by the parity gate's own `--render` mode rather than by a separate adopter" |
| `check-install-prefix` | `install-prefix-waivers.txt` (the tree's ONLY `generated` rule) | `[]` | "this is seeded empty rather than copied" |

Counted across every descriptor: 9 `rendered`/`generated` rules, 7 with a producer and 2 without.
Mapping on the role alone would have previewed those 2 under a promise no step keeps — the same
over-promise this unit exists to delete, moved one mark over. Hence the producer test in S1.

The `blocks_adopt` half of that test is armed by a FIXTURE, not by the shipped tree: no descriptor
here declares a `blocks_adopt` hole today, so the condition is correct and unexercised, and saying so
is the difference between a guard and a claim.

rev-1's `project-owned` → `order` had the mirror problem. In 2 of the 4 `project-owned` rules a
sibling `seed` rule in the SAME descriptor lands that exact destination during the same `apply` —
`tools/codebase-map/kit.toml:13-20` pairs `map_extractors.py` (no `to`, so `resolve_dests` defaults it
to `{kit}/map_extractors.py`) with `map_extractors.template.py` (`seed`, `to` = that same path), and
`tools/drift-audit/kit.toml` carries the identical pair for `drift_signals.py`. MEASURED,
`plan --kits codebase-map` prints both rows at one path:

```
write  [project-owned] tools/codebase-map/map_extractors.py   <- codebase-map
write  [seed         ] tools/codebase-map/map_extractors.py   <- codebase-map
```

`codebase-map` is in the DEFAULT selection. Under a role-only mapping the first becomes ORDER while
the second stays a write, and the preview prints two contradictory verbs for one path. Hence
`covered`: the row stays visible (a rule that vanishes from the preview is its own defect) and names
the rule that writes it, so the operator reads one answer to "what will be at this path".

### An unknown role must not default to `write`

A rule whose role is absent defaults to `engine` (`rule.get("role", "engine")`), which is a write. A
role SPELLED but not in the table is the dangerous case: falling back to `write` reintroduces exactly
this bug for the next role someone adds. It refuses — `selfcheck` and `plan` both fail naming the
unknown role and the entry it came from.

### Data model

No descriptor change. The six roles already in the tree are the table's keys; `selfcheck` asserts the
declared population is a subset of it, which catches a seventh role at authoring time.

### Files touched (estimate)

`tools/govkit/govkit.py`, `tools/govkit/selftest.py`, `skills/deploy-governance/SKILL.md`. No
descriptor edits, no registry edit. There is no `tools/govkit/README.md` — `git ls-files tools/govkit/`
returns only `entries/*.kit.toml`, `govkit.py`, `registry.toml`, `selftest.py` — which is why rev-1's
§5 sent the builder to a file that does not exist.

## 5. Production-readiness checklist

- security — narrows what `plan` promises; it cannot cause a write that did not happen before, and
  `apply`'s write condition is derived from the same table so it cannot widen either.
- perf / scale — a dict lookup plus a destination set per rule.
- a11y / i18n — N/A.
- error / empty / loading states — an unknown role refuses rather than defaulting; an absent role
  still defaults to `engine`, which is the documented existing behaviour and is asserted.
- observability — this unit IS observability: S2 makes every skip visible, and the plan marks
  distinguish five outcomes where there was one.
- risks — the real one is mis-mapping a rule, which would make the preview confidently wrong in a new
  way. rev-1 claimed each mapping is "asserted against the behaviour `apply` actually exhibits for
  that role"; it CANNOT be, because `govkit.py:881` is one condition and apply's observable behaviour
  is identical for `rendered`, `generated` and `project-owned`. What is assertable, and what AC3 and
  AC4 assert, is the mark each named rule receives over a named selection — pinned positively, per
  role, against a measured expectation rather than against the table itself.
- testing + left-shift gates — S4 plus AC3/AC4/AC5, on `python tools/govkit/selftest.py`, already a
  leg.
- migration / rollback — none. No on-disk format changes; a receipt written before this unit is
  unchanged in shape.
- user docs — the three carriers in S5, corrected together.

## 6. Acceptance criteria

- **AC1** — When `plan` runs over the `playbook` entry, neither `project-owned` row is counted as a
  write, and the summary line reports 0 write(s).
- **AC2** — When `plan` runs over an entry carrying a `merged` rule (`--kits push-main`), that row is
  marked BLOCKED, and `apply` over the same entry refuses — the two agree.
- **AC3** — When `plan` runs over the DEFAULT selection, the non-write rows counted by
  `MARK|role` PAIR are exactly `SIDE|rendered` **4** (memory-tree 3, memory-recall 1),
  `ORDER|project-owned` **2** (playbook) and `COVER|project-owned` **1** (codebase-map's
  `map_extractors.py`, covered by its sibling seed), with no `write|project-owned` row at all — so an
  implementation emitting all seven under one mark fails. Keyed on the PAIR because a mark-only tally
  is not stable: `ORDER` also covers the holes and the machine-scoped link rule, so its total moves
  with which answers a descriptor supplies.
- **AC4** — When `plan` runs over `--kits review-harness` and over `--kits check-install-prefix`, the
  `rendered` and `generated` rows are marked ORDER and not SIDE, because neither entry declares an
  adopter; and a fixture descriptor with a `blocks_adopt` hole is marked ORDER too.
- **AC5** — When `apply` skips a rule, its role, its destination and the reason appear on stdout, one
  line per rule.
- **AC6** — When plan's write set is compared against the `files` list in `.governance/install.json`
  with NO role filter, the two sets are equal over BOTH operands: the `**` kit (`--kits drift-audit`)
  and the default selection.
- **AC7** — When a descriptor declares a role absent from the table, `plan` and `selfcheck` both
  refuse and name the role and the entry.
- **AC8** — When `LANDABLE_ROLES` is derived, it still equals `("engine", "seed")` — asserted against
  a literal, so a table edit that silently changes what lands reds.
- **AC9** — When `skills/deploy-governance/SKILL.md` is checked, it no longer says `plan` lists every
  file `apply` would write; `planned_writes`' docstring no longer carries the machine-scope-only
  exception list; and `cmd_plan`'s legend spells all five marks.
- **AC10** — When `bash tools/run-gates.sh` runs on the landing commit, it is green.

## 7. Gates

`python tools/govkit/selftest.py` and `python tools/govkit/govkit.py selfcheck`, both already legs.
No new leg.

## 8. Open questions

- **F1 — is `project-owned` the right role for the playbook's two files?** RESOLVED (agent,
  2026-08-17): OUT of this unit and filed as `TOOL-dClosedLexicon-15`. The entry's own
  `why_no_adopter` says "installation is a copy to an owner-chosen path", which describes a `seed`,
  not a file the target already owns. If that comment is right, govkit installs no playbook today —
  and the honest preview this unit ships now says so out loud, in the two `ORDER [project-owned]`
  rows AC1 pins. That is a change to what the default install DOES rather than to what it claims, so
  it is owner-facing and not a resolver call. This unit is correct under either answer, and its
  output is what makes the question visible.

## 9. Revision log

- rev-1 · 2026-08-17 · initial draft. Written from a measured plan/apply pair over the `playbook`
  entry rather than from the backlog row, which named only `rendered` and credited `apply` with a
  SKIPPED report it does not print.
- rev-2 · 2026-08-17 · folds `review-dClosedLexicon-9`, 7 defects, no blockers; the audit reproduced
  §1's role census exactly and confirmed the diagnosis and the one-table design. Both mapping
  rationales were measurably false — `side-effect` for two entries that declare no adopter (13-1) and
  `order` for two `project-owned` rules a sibling seed writes at the same path (13-2) — so the
  classification is keyed on the producer and the destination, and gains a `covered` mark. AC3/AC4 pin
  the mapping POSITIVELY per role over named selections, which no rev-1 criterion did while §5 claimed
  otherwise (13-3). §5's user docs pointed at a `tools/govkit/README.md` that does not exist and
  missed `skills/deploy-governance/SKILL.md`, the document that actually carries the promise (13-4).
  AC6 names both operands S4 requires (13-6). `planned_writes` re-cited at `:531`/`:564`; rev-1's
  `:864` was a continuation line inside `cmd_apply` (13-7). §10 records what the probe returned
  (13-5, X-1).

## 10. Reuse audit

**Probe 1, `reuse_lookup.py` — RE-RUN, and it MISSES the pair.**
`python tools/codebase-map/reuse_lookup.py "one predicate, two callers"` returns thirteen candidates —
`id_pattern(conf)`, `registry.toml`, `agent-cap.topLevelArgs`,
`assertion-between-two-derived-values.md`, `check-install-prefix.sh`, `check-template-size.sh`,
`kit-dogfood-parity.PAIRS`, "lexicon naming predicates", `lexicon.subtokens`, `manifest-check.sh`,
`merge-rows.skeleton`, `pyrun.sh`, `two-answers-to-one-question.md` — and neither `resolve_dests` nor
`resolve_rule_pool` appears, though `symbols.json` carries both against `tools/govkit/govkit.py`. So
rev-1's "surfaces that pair and nothing else with this shape" was false in both halves. Recorded as an
answer per M5. What it DID surface is the gotcha class this unit closes,
`memory/gotchas/two-answers-to-one-question.md`, which is the better citation.

**Probe 2, `query.py` — terms recorded for M7 (satisfied once for the SET, per M5).**
Question: *how does this repo retire a finished record and start a fresh one without losing the old
bytes, and how does a preview verb stay in step with the verb that acts.*
Terms: `rotation archive retired record terminal phase preflight refusal preview parity plan apply
divergence symbol corpus census`. Relevant hit:
`memory/builds/aSealedCaravan/reviews/2026-08-10-review-aSealedCaravan-1.md:169` — "`plan` … is the
only read-only preview of a write-heavy tool, so it can ship inert with every AC green", the same
mechanism one review earlier and the reason AC3/AC4 pin the mapping positively.

**Reuse, hand-verified.** `resolve_dests` (`govkit.py:691`) and `resolve_rule_pool` (`:715`), added by
`TOOL-dClosedLexicon-4`, are the precedent and the shape to copy: one function both verbs call, so the
preview and the action cannot disagree — their docstrings state that rule verbatim. This unit applies
the same move one level up, to the classification rather than the path set. The table deliberately
does NOT reuse the `SYMBOL_KINDS` frozen-vocabulary idiom from `map_lib.py`: that one rejects unknown
members at render time, and this one has to map rather than merely admit.
