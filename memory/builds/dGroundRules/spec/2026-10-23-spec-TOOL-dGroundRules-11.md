# TOOL-dGroundRules-11 — every loop bound and deadline key declares that raising it is a loosening

**Status:** DEFERRED · rev-1 · 2026-10-23 · node d · Tier-2 · base 3708a705 · streams tooling · order 1 · advances TOOL-dGroundRules-12

**Carries:** cl-dClosedLoop-0017@c5b54ae9 whole

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-23-prompt-TOOL-dGroundRules-1-spec-brief.md](../prompts/2026-10-23-prompt-TOOL-dGroundRules-1-spec-brief.md) | research | TOOL-dGroundRules-1 TOOL-dGroundRules-2 TOOL-dGroundRules-3 TOOL-dGroundRules-4 TOOL-dGroundRules-5 TOOL-dGroundRules-6 TOOL-dGroundRules-7 TOOL-dGroundRules-8 TOOL-dGroundRules-9 TOOL-dGroundRules-10 |
| [2026-10-23-prompt-TOOL-dGroundRules-11-build-brief.md](../prompts/2026-10-23-prompt-TOOL-dGroundRules-11-build-brief.md) | journal | — |
| [2026-10-23-review-TOOL-dGroundRules-1-11-spec-audit-round1.md](../reviews/2026-10-23-review-TOOL-dGroundRules-1-11-spec-audit-round1.md) | spec-audit | TOOL-dGroundRules-1 TOOL-dGroundRules-2 TOOL-dGroundRules-3 TOOL-dGroundRules-4 TOOL-dGroundRules-5 TOOL-dGroundRules-6 TOOL-dGroundRules-7 TOOL-dGroundRules-8 TOOL-dGroundRules-10 TOOL-dGroundRules-9 |
| [2026-10-23-review-TOOL-dGroundRules-1-52-closing-diff-round1.md](../reviews/2026-10-23-review-TOOL-dGroundRules-1-52-closing-diff-round1.md) | diff-review | TOOL-dGroundRules-1 TOOL-dGroundRules-2 TOOL-dGroundRules-3 TOOL-dGroundRules-4 TOOL-dGroundRules-5 TOOL-dGroundRules-6 TOOL-dGroundRules-7 TOOL-dGroundRules-8 TOOL-dGroundRules-9 TOOL-dGroundRules-10 TOOL-dGroundRules-65 TOOL-dGroundRules-14 TOOL-dGroundRules-15 TOOL-dGroundRules-16 TOOL-dGroundRules-17 TOOL-dGroundRules-18 TOOL-dGroundRules-19 TOOL-dGroundRules-20 TOOL-dGroundRules-21 TOOL-dGroundRules-22 TOOL-dGroundRules-23 TOOL-dGroundRules-24 TOOL-dGroundRules-25 TOOL-dGroundRules-26 TOOL-dGroundRules-27 TOOL-dGroundRules-28 TOOL-dGroundRules-29 TOOL-dGroundRules-30 TOOL-dGroundRules-31 TOOL-dGroundRules-32 TOOL-dGroundRules-33 TOOL-dGroundRules-34 TOOL-dGroundRules-35 TOOL-dGroundRules-36 TOOL-dGroundRules-37 TOOL-dGroundRules-38 TOOL-dGroundRules-39 TOOL-dGroundRules-40 TOOL-dGroundRules-41 TOOL-dGroundRules-42 TOOL-dGroundRules-43 TOOL-dGroundRules-44 TOOL-dGroundRules-45 TOOL-dGroundRules-46 TOOL-dGroundRules-47 TOOL-dGroundRules-48 TOOL-dGroundRules-49 TOOL-dGroundRules-50 TOOL-dGroundRules-51 TOOL-dGroundRules-52 |

<!-- /gen:spec-records -->

## 1. Goal

P39 says every loop ends and every wait expires, and a later build's owner-silence rule must
recommend declining "a raised loop bound or deadline" (v2:1230). Nothing today says which keys those
are. This unit gives the catalogue a `direction` field, derives the population of loop bound and
deadline keys from each row's typed range, and has the schema refuse a member of that population
that does not declare `direction = "raise-loosens"`. It is seen red on a planted loop bound with no
declared direction.

## 2. Scope (IN)

- **S1** — The catalogue field `direction`, optional on every row of `tools/policy/catalogue.toml`,
  with one allowed value, `raise-loosens`. Any other value on any row is refused. Observed by AC4.
- **S2** — The population rule, `derive_bounds(rows)` in `tools/policy/policy.py`: a row is a
  loop bound when its `allowed` is a typed range whose `type` is in `LOOP_BOUND_TYPES`, which is
  `retry-count`, `round-count` and `route-back-count`. It is a deadline when that `type` is in
  `DEADLINE_TYPES`, which is `hours`, `days` and `seconds`. The two tuples are the rule; no row is
  named. Observed by AC1 and AC5.
- **S3** — `check_direction(rows)` in `tools/policy/policy.py`, and the arm `arm_direction` in
  `tools/policy/check_policy.py`, registered in `ARMS`. The arm prints the population's size and
  reds on each member with no `direction`, on any row with a value other than `raise-loosens`, and on
  an empty population. Observed by AC1, AC2, AC3 and AC4.
- **S4** — Each row the rule selects carries `direction = "raise-loosens"` in the catalogue.
  Observed by AC1.
- **S5** — Three cases in `CASES`: `direction-missing`, `direction-new-bound` and
  `direction-wrong-value`. Observed by AC2, AC3 and AC4.
- **S6** — The rule documented in `tools/policy/README.md` and `help/policy.md`. Observed by AC6.

## 3. Non-goals (OUT)

- Any consumer of the field: the owner-silence rule that recommends declining a raise
  (`run.on-owner-silence`), the flow change that waits for the owner, and the update report that
  names a raise as a widening are later builds' readers.
- Enforcing a raise itself, at a write or at a landing. This unit declares and checks the
  declaration; it refuses no policy write.
- A direction for keys outside the population, such as `runtime.agents-in-flight` or a cap under
  `budgets.*`. Raising either loosens too, but neither is a loop bound or a deadline, and the clause
  names only those.
- The catalogue's rows, its typed-range nouns and the shape audit's field set, which are
  TOOL-dGroundRules-1's.

### Edges

- **consumes-from** `TOOL-dGroundRules-1` — the catalogue, its typed ranges with v2's nouns, the module `policy.py`, the arms' home and its `--fixture` mode; without them there is no row to declare on and no arm to run
- **hands-off** external — the readers of the declaration: dWellOiledMachine's owner-silence rule and dDeclaredLoop's flow change and update report

## 4. Design

### Evidence

- v2's `[policies]` table states its loop bounds and deadlines by noun in the Allowed cell: "a
  retry count", "a round count", "a route-back count", and the durations "hours", "days" and
  "seconds". A probe over that table on 2026-10-23 found 19 rows whose cell opens with one of those
  six nouns. That figure is PINNED as of that reading; AC1 and AC5 re-derive it.
- TOOL-dGroundRules-1 §8 F3 keeps those nouns as the catalogue's `type` values for exactly this rule.
- v2's Source cells do not mark the population: `leases.expiry-hours`, a deadline, cites P40 and not
  P39, while `leases.renewal`, an enum that cannot be raised, cites P39.

### Data model

```toml
[[key]]
name = "flow.wait-ceiling"
allowed = { type = "hours", min = 0 }
default = 72
owner = "dDeclaredLoop"
direction = "raise-loosens"       # required here: `hours` is in DEADLINE_TYPES
```

The population at the 2026-10-23 reading, for the builder to check against the derivation and never
to type into code:

| Noun | Rows |
|---|---|
| `retry-count` | `roles.retries`, `runtime.no-progress`, `runtime.refusal-repeats`, `runtime.restarts` |
| `round-count` | `review.design.round-count`, `review.max-rounds` |
| `route-back-count` | `flow.route-backs`, `flow.rework-budget` |
| `hours` | `leases.expiry-hours`, `runtime.act-ceiling`, `runtime.hold-ceiling`, `run.owner-deadline`, `flow.wait-ceiling`, `build.release-ceiling` |
| `days` | `leases.queued-claim-days`, `runtime.journal`, `review.loop.window-days` |
| `seconds` | `leases.offer-seconds`, `mailbox.fetch-seconds` |

### Inventory — what the unit mints

| Name | Kind | Where |
|---|---|---|
| `LOOP_BOUND_TYPES`, `DEADLINE_TYPES` | module tuples, the population rule | `tools/policy/policy.py` |
| `derive_bounds(rows)` | function, the selected rows in file order | `tools/policy/policy.py` |
| `check_direction(rows)` | function, `(key, why)` pairs | `tools/policy/policy.py` |
| `arm_direction` | arm function, registered in `ARMS` | `tools/policy/check_policy.py` |
| `direction-missing`, `direction-new-bound`, `direction-wrong-value` | fixture cases in `CASES` | `tools/policy/check_policy.py` |

### The arm and its cases

`arm_direction` prints `policy-check: direction · <n> finding(s) · <m> loop bound and deadline
row(s)`. A finding names the key and one reason: "a loop bound or deadline declares no direction",
or "direction must be raise-loosens". An `m` of zero is itself a finding, so the arm cannot pass by
selecting nothing.

| Case | Plant | Expected |
|---|---|---|
| `direction-missing` | the first row `derive_bounds` selects in the shipped catalogue loses its `direction` | RED naming that row |
| `direction-new-bound` | a new row `zz.loop`, `allowed = { type = "retry-count", min = 1 }`, `default = 3`, no `direction` | RED naming `zz.loop` |
| `direction-wrong-value` | the same first selected row gets `direction = "raise-tightens"` | RED naming that row |

`direction-missing` edits a shipped row, so it proves the rule on the shipped value. Each case runs
the arm again on the unplanted copy, which must be green.

TOOL-dGroundRules-1's unknown-field rule already admits `direction`, so this unit adds no field to
the shape audit's set.

### Rollout

This unit shares order 1 with TOOL-dGroundRules-1, and every file it writes is one that unit writes
too, so the two write sets intersect and the build runs this unit after that one, never beside it
(M6, clause 1).
Once TOOL-dGroundRules-1 lands, its `policy fixtures` leg guards `{prefix}/policy/` and the guards
join owes that leg on §7's line. The build pass adds it there as a revision before dispatch, since
the name resolves to nothing in the manifest today.

### Files touched (estimate)

- `tools/policy/catalogue.toml`
- `tools/policy/policy.py`
- `tools/policy/check_policy.py`
- `tools/policy/README.md`
- `help/policy.md`
- `memory/map/generated/symbols.json`

### Alternatives rejected

- **The population from v2's P39 citations.** The probe in Evidence shows it misses a deadline and
  admits an enum, and the catalogue carries no Source column to read.
- **A typed list of key names.** The brief forbids it, and a new loop bound added without its name
  on the list would pass unseen.
- **The rule inside `check_shape`.** It would fold this unit's red into TOOL-dGroundRules-1's arm,
  and the population's size would print nowhere.

## 5. Production-readiness checklist

- security — none: a declaration in a catalogue the kit ships; no write path changes.
- perf / scale — one pass over about 270 rows; three more fixture repositories.
- error / empty / loading states — an empty population is a finding, never a pass.
- observability — the arm prints its population size on every run.
- risks — a durations row that bounds no loop is in the population; §8 F2 accepts that on the
  safe side.
- testing — the three cases, each red as planted and green without, with AC1 to AC6.
- migration — none: the field is additive and optional outside the population.
- user docs — `help/policy.md` and `tools/policy/README.md` gain the rule.

## 6. Acceptance criteria

The kit's paths are quoted inside each command below, because none is tracked until
TOOL-dGroundRules-1 lands.

- **AC1** — When `python "tools/policy/check_policy.py"` runs on the built tree, its `direction`
  line reports 0 findings over a population of at least one row.
  Red when: a selected row lacks `direction`, or the population reads zero.
  figure: the population is DERIVED by `derive_bounds` at observation; 19 at writing.
- **AC2** — When `python "tools/policy/check_policy.py" --fixture` reaches `direction-missing`, it is
  RED as planted, naming the shipped row it edited, and green unplanted.
  Red when: `check_direction` stays silent on a selected row with no `direction`.
- **AC3** — When the same `--fixture` run reaches `direction-new-bound`, it is RED as planted, naming
  `zz.loop`, and green unplanted.
  Red when: a planted loop bound with no declared direction passes `arm_direction`.
- **AC4** — When the same `--fixture` run reaches `direction-wrong-value`, it is RED as planted and
  green unplanted.
  Red when: a `direction` other than `raise-loosens` passes.
- **AC5** — When a probe reads v2's `[policies]` table from `git show 9bf3b4c91952d54f01be759082f7ae3e52cde160`
  and lists the rows whose Allowed cell opens with "a retry count", "a round count", "a route-back
  count", "hours", "days" or "seconds", that list equals the names `derive_bounds` returns over
  `tomllib.load(open( "tools/policy/catalogue.toml" , "rb"))["key"]`.
  Red when: a row typed by another noun is selected, or a row v2 states by one of the six is not.
  figure: both sides are DERIVED; 19 at the 2026-10-23 reading.
- **AC6** — When `grep -c "raise-loosens" "help/policy.md" "tools/policy/README.md"` runs, each file
  counts at least one line, and the README names `LOOP_BOUND_TYPES` and `DEADLINE_TYPES`.
  Red when: either page omits the rule.

## 7. Gates

`recall floor` · `recall floor arms` · `codebase-map coverage + freshness` · `govkit selfcheck`

New arm: tools/policy/check_policy.py · covers AC1 · a selected row's `direction` removed from the live catalogue · none
New arm: tools/policy/check_policy.py --fixture · covers AC2 AC3 AC4 · each `direction-*` case plants its break in a temporary repository · none

## 8. Open questions

- **F1 — How is the population derived?** (a) From each row's typed-range noun: `retry-count`,
  `round-count` and `route-back-count` are loop bounds, `hours`, `days` and `seconds` deadlines.
  (b) From v2's P39 citations, which the probe in §4 Evidence shows miss `leases.expiry-hours` and
  admit `leases.renewal`, an enum; and the catalogue holds no Source column. (c) A typed list of
  names, which the brief forbids. Veto 1 discards (b) and (c). Recommendation (a). Rung 3.
  RESOLVED (agent, 2026-10-23, delegated): (a). widens: none · relaxes: none
- **F2 — Do durations that bound no loop stay in the population?** `runtime.journal`, a retention,
  `review.loop.window-days`, an evidence window, and `mailbox.fetch-seconds`, a staleness bound, are
  typed by duration nouns. (a) Keep them, each declaring `raise-loosens`: over-inclusion fails safe,
  because the declaration's readers decline a raise on owner silence. (b) An exception list, a typed
  list again. (c) A new noun for them, one v2's cells do not state, which types the classification
  into the catalogue. Veto 1 discards (b); (c) passes but adds a vocabulary member nothing asks for,
  so (a) leaves fewer open questions. Recommendation (a). Rung 3.
  RESOLVED (agent, 2026-10-23, delegated): (a). widens: none · relaxes: none
- **F3 — One value or two?** (a) `raise-loosens` alone, the clause's words. (b) `raise-loosens` and
  `raise-tightens`, so a key outside the population could declare either. Nothing reads (b)'s second
  value, which YAGNI refuses. Recommendation (a). Rung 3.
  RESOLVED (agent, 2026-10-23, delegated): (a). widens: none · relaxes: none

## 9. Revision log

- rev-1 · 2026-10-23 · initial draft.

## 10. Reuse audit

The seam is TOOL-dGroundRules-1's catalogue in `tools/policy/catalogue.toml` and its arms' home
`tools/policy/check_policy.py`, both specced in `2026-10-23-spec-TOOL-dGroundRules-1.md` and not yet
in the tree: this unit adds a field, a rule and an arm to them rather than a module. No existing seam
in today's tree classifies a declared field by direction. `python tools/codebase-map/reuse_lookup.py
"classify a declared field by its direction tightening or loosening"` ranked `field` in a run-gates
test, `classify` in `tools/govkit/census.py`, `tools/lexicon/subtokens.py` and
`tools/memory-tree/check-arms.py`, and the unattended kit's `declared_list` and `declared_scalar`.
Each classifies another subject and none reads a policy key. The recall probe surfaced
`TOOL-aDeclaredBound-4`, whose agent cap holds lowering free and raising attributed, the same
direction asymmetry for one key. TOOL-dGroundRules-10 owns that key and this unit leaves it alone.
No hit disagreed with source.

Recall terms used: `python tools/memory-recall/query.py "which policy keys are loop bounds or
deadlines and does raising one loosen the policy" --terms "loop bound deadline raising loosening
direction rework-budget max-rounds wait-ceiling owner-deadline P39 schema"`
