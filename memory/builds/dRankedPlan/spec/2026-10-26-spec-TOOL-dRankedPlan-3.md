# TOOL-dRankedPlan-3 — triage as `plan.triage` says: declared rules, the planner judging the rest

**Status:** OPEN · rev-2 · 2026-10-27 · node a · Tier-2 · base 0689e7fa · streams tooling · order 10 · advances TOOL-dRankedPlan-17

**Carries:** cl-dClosedLoop-0371@3ec4f25f whole
**Carries:** node:policy-key.plan.triage
**Carries:** node:item.plan.triage-rule
**Carries:** node:item.plan.triage-judge
**Carries:** node:record-kind.triage
**Carries:** node:record-kind.dupes

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-26-build-TOOL-dRankedPlan-1-reuse-scout-b.md](../build/2026-10-26-build-TOOL-dRankedPlan-1-reuse-scout-b.md) | research | TOOL-dRankedPlan-1 TOOL-dRankedPlan-2 TOOL-dRankedPlan-4 TOOL-dRankedPlan-5 TOOL-dRankedPlan-6 TOOL-dRankedPlan-9 TOOL-dRankedPlan-10 TOOL-dRankedPlan-15 |
| [2026-10-26-build-TOOL-dRankedPlan-1-spec-stage-returns.md](../build/2026-10-26-build-TOOL-dRankedPlan-1-spec-stage-returns.md) | research | TOOL-dRankedPlan-1 TOOL-dRankedPlan-2 TOOL-dRankedPlan-4 TOOL-dRankedPlan-5 TOOL-dRankedPlan-6 TOOL-dRankedPlan-7 TOOL-dRankedPlan-8 TOOL-dRankedPlan-9 TOOL-dRankedPlan-10 TOOL-dRankedPlan-11 TOOL-dRankedPlan-12 TOOL-dRankedPlan-13 TOOL-dRankedPlan-14 TOOL-dRankedPlan-15 TOOL-dRankedPlan-16 |
| [2026-10-26-prompt-TOOL-dRankedPlan-1-spec-brief.md](../prompts/2026-10-26-prompt-TOOL-dRankedPlan-1-spec-brief.md) | research | TOOL-dRankedPlan-1 TOOL-dRankedPlan-2 TOOL-dRankedPlan-4 TOOL-dRankedPlan-5 TOOL-dRankedPlan-6 TOOL-dRankedPlan-7 TOOL-dRankedPlan-8 TOOL-dRankedPlan-9 TOOL-dRankedPlan-10 TOOL-dRankedPlan-11 TOOL-dRankedPlan-12 TOOL-dRankedPlan-13 TOOL-dRankedPlan-14 TOOL-dRankedPlan-15 TOOL-dRankedPlan-16 |
| [2026-10-26-review-TOOL-dRankedPlan-1-spec-audit.md](../reviews/2026-10-26-review-TOOL-dRankedPlan-1-spec-audit.md) | spec-audit | TOOL-dRankedPlan-16 TOOL-dRankedPlan-1 TOOL-dRankedPlan-9 TOOL-dRankedPlan-10 TOOL-dRankedPlan-2 TOOL-dRankedPlan-14 TOOL-dRankedPlan-13 TOOL-dRankedPlan-11 TOOL-dRankedPlan-12 TOOL-dRankedPlan-4 TOOL-dRankedPlan-5 TOOL-dRankedPlan-15 TOOL-dRankedPlan-6 TOOL-dRankedPlan-8 TOOL-dRankedPlan-7 |

<!-- /gen:spec-records -->

## 1. Goal

Triage is never drained: at base, 434 of the 623 live asks carry no severity and 297 of those sit
DEFERRED onto one owner-triage ask, `TOOL-aMendedFleet-106`, open since 2026-10-05, and no role owns
triage (gap-plan-02; gap-plan-06 adds that most OPEN asks are not ready to build). This unit makes
triage a command that runs as `plan.triage` says: under `rules`, by `plan.triage-rule`'s declared
rules, the planner judging what no rule decides; under `owner-batches`, the same drafts held for the
owner to ratify in batches at an owner breakpoint; under `archive-legacy`, the legacy backlog
archived and only new asks triaged. Every label names the rule that set it, so a wrong rule is found
by its labels (walkthrough:380-383).

## 2. Scope (IN)

- **S1** — The declared rules, I12. `.governance/triage-rules.toml` holds `[[triage-rule]]` rows,
  read by `read_triage_rules(root)` in `tools/memory-tree/triage.py`. Each row carries `id`, a
  bool `enabled`, a `when` table, a `verdict`, a `level` and a `why`, with an optional `accept`; §4
  "The rule grammar" states the closed key sets. A row with an unknown key, an unknown condition, a
  verdict outside the four flow-steps.md:182 names, or no `level` where its verdict keeps the ask
  live is refused, exit 2, naming the row's `id` and the key. An absent file declares no rule.
  Observed by AC1, AC6.
- **S2** — `plan.triage-rule`, the command item `item.plan.triage-rule`. `python
  tools/memory-tree/triage.py pass [--ask <id>…]` reads `plan.triage` once, through `python
  tools/policy/policy.py get plan.triage` (I14), a refused read taking the catalogue default `rules`
  with one `NOTE:` line. It reads every live ask the generator's fold reads (`OPEN`, `BLOCKED`,
  `DEFERRED`) that carries no `SEV` row, or only the asks `--ask` names. For each, the first enabled
  rule in file order whose every condition holds decides it, and the pass renders that ask's rows
  through `tools/memory-tree/backlog.py`'s renderers (§4 "Rows"). An ask no rule decides goes to S3.
  Inside a build, `triage.py pass --build <slug>` triages the build's one input: the ask it was
  selected from, by the rules, or, for an input that is an owner's request rather than an ask,
  `select` under the fixed rule `request`, since that request is the plan's ratification under
  `plan.ratification: request` (FR-1, flow-roles.md:189-199) and no declared rule may refuse it. It
  prints its outcome, one of the four verdicts of §4 "Rows" or `no-rule`. `--dry-run` prints the rows
  and a count per rule and writes nothing. Observed by AC1, AC5, AC8, AC11.
- **S3** — `plan.triage-judge`, the planner's item `item.plan.triage-judge`. `triage.py judge
  --request` prints one JSON object per undecided ask (`id`, `text`, `status`, `ready`, `missing`,
  `filed`); the planner, slot `gov-planner` (I10), returns one JSON object per ask with `id`,
  `verdict`, `level` and `why`. `triage.py judge --return <path>` schema-checks the return before
  anything is written: each `id` is one the request named, each `verdict` one of the four, each
  `level` one of `SEVERITIES` (`tools/memory-tree/backlog.py:84`) where the verdict keeps the ask live.
  A failing return exits 2 naming the object and the field, and writes nothing. A passing one renders
  rows as S2 does, the why naming `judge`. Observed by AC2.
- **S4** — The three values of `plan.triage`, read by S2 and S3 alike (§4 "The three values"). Under
  `rules` the rows are written into each ask's home `BACKLOG.md`. Under `owner-batches` nothing is
  written to a backlog; S5's record holds the batch. Under `archive-legacy` every live ask filed
  before `ASK_CUTOFF` (`.memory-tree.conf:742`) with no `SEV` row is archived by one `WONTDO` row
  whose why names `archive-legacy`, and only asks filed on or after it are triaged by S2 and S3.
  Observed by AC1, AC3, AC4.
- **S5** — The triage record, `record-kind.triage`, I12. Registered by `python
  tools/memory-tree/record_kinds.py new triage` (TOOL-dTotalRecall-1 S9) with the fields `Value`,
  `Rules`, `Asks`, `Rows`, `Judged`, `Batch` and `Ratified`, and written through `gov_record.py new
  triage` (TOOL-dTotalRecall-2), one record per pass per home build that the pass decided an ask in.
  `Rows` is `<n> rows · <key>`, the key `derive_section_sha` (`tools/roles/handoff.py:307`) over the
  rendered rows joined by LF. Observed by AC3, AC7.
- **S6** — The batch ratification, the owner breakpoint of `owner-batches`. `triage.py ratify
  <record>` calls `read_plan_ratification(<home>)` (TOOL-dRankedPlan-9, I6), the home being the build
  whose folder holds the record. With no witness it exits 1, `triage — <home> batch held: <why>`, the
  predicate's own reason, and writes nothing. With one it
  re-derives the batch's rows at HEAD from the record's `Rules` blob and `Judged` field, refuses with
  exit 1 when their key differs from `Rows` (`triage — batch moved; run pass again`), and otherwise
  writes the rows and a second triage record of the same home with `Batch` `ratified` and `Ratified`
  the value and witness. Observed by AC3.
- **S7** — The dupes record, `record-kind.dupes`. Registered by `python
  tools/memory-tree/record_kinds.py new dupes` with the fields `Input`, `Matched`, `Finding` and
  `Overlap`, its writer `gov_record.py new dupes`. `python tools/loop/plan_items.py dedupe --build
  <slug> --record` writes one from TOOL-dRankedPlan-2's `check_plan_dupes` finding: `Input` the
  claim's content key, `Matched` `none` or each `<build|ask> <id>` matched, `Finding` `none` or
  `duplicate`, and `Overlap` `unmeasured` until dIndexedDesign's design index lands. Observed by AC7,
  AC12.
- **S8** — The seed rules. This repository's `.governance/triage-rules.toml` ships the four rows of
  §4 "The seed", each conservative: none of them closes an ask. Observed by AC8.
- **S9** — `plan.triage`'s catalogue row in `tools/policy/catalogue.toml` gains its `summary` and
  `usage`, and `python tools/policy/policy.py lists --write` takes it off
  `tools/policy/unsummarised-keys.txt`. Observed by AC9.
- **S10** — The docs: `help/plan.md` (TOOL-dRankedPlan-16 S9) gains a section "Triage" on running the
  pass, the judge exchange, each value of `plan.triage` and the rule grammar; `tools/memory-tree/README.md`
  names `triage.py`. Observed by AC10.
- **S11** — The three items armed, as TOOL-dDeclaredLoop-13 §4 "The stand-ins" says an owning build
  arms its items: `read_plan_item_witness` in `tools/loop/plan_items.py` (TOOL-dRankedPlan-2 S5)
  gains the witness readers of `item.plan.dedupe`, `item.plan.triage-rule` and
  `item.plan.triage-judge` by §4 "The witnesses", and the three `[[stand-in]]` rows naming those items
  are deleted from `tools/loop/loop.toml` in the same pass.
  **Readers:** by name: READER NOT IN TREE — the loop kit is absent at base 0689e7fa; the rows'
  reader is TOOL-dDeclaredLoop-13's stand-in reader in its `loop_table.py`, specced and unbuilt ·
  by value: the `[[stand-in]]` list TOOL-dDeclaredLoop-13 S8 grades and TOOL-dDeclaredLoop-7's
  `derive_position`, which reads an item's witness through the armed reader from this pass.
  Observed by AC12.

## 3. Non-goals (OUT)

- The planner role and the Plan workflow: TOOL-dRankedPlan-2's. The `item.plan.*` rows themselves:
  TOOL-dDeclaredLoop-12 S2 declares all eleven; this unit adds no row and arms three by S11.
- The dedupe check and what counts as a duplicate: `check_plan_dupes`, TOOL-dRankedPlan-2's. S7
  records its finding.
- Opening a build for a selected ask: `entry.claim` (dPlacedRequest) and `plan.record`. A `select`
  verdict labels the ask and prints it; it opens nothing.
- The ratification predicate and its intake stand-in: TOOL-dRankedPlan-9's, called by S6.
- The backlog grammar, the fold and the view: `tools/memory-tree/backlog.py` is read and its
  renderers called, never changed. No new status verb.
- Running the pass over this repository's real backlog. That is an operational act under the owner's
  value of `plan.triage`, and the shrink-only pin on drift's `backlog_asks_unlabelled` moves when it
  happens, not in this unit.
- Plan Review over a triage result (TOOL-dRankedPlan-6, dCalibratedLens) and the rule lenses of
  walkthrough:354.

### Edges

- **consumes-from** `TOOL-dRankedPlan-9` — `read_plan_ratification`, the witness S6 requires before a held `owner-batches` batch is written
- **consumes-from** `TOOL-dRankedPlan-2` — `gov-planner`, the slot whose return S3 schema-checks as `plan.triage-judge`
- **consumes-from** `TOOL-dRankedPlan-2` — `check_plan_dupes`, the dedupe finding S7 records as the dupes record, and `read_plan_item_witness` in `tools/loop/plan_items.py`, which S11 extends to arm `item.plan.dedupe`, `item.plan.triage-rule` and `item.plan.triage-judge`
- **consumes-from** external — dDeclaredLoop: the eleven Plan item rows (TOOL-dDeclaredLoop-12 S2) and the `[[stand-in]]` rule (TOOL-dDeclaredLoop-13 §4, S8) S11 follows
- **consumes-from** external — dTotalRecall, built before this build run: `record_kinds.py new` (TOOL-dTotalRecall-1 S9) and `gov_record.py new` with `write_new_record` (TOOL-dTotalRecall-2 S1)
- **consumes-from** external — dGroundRules, landed: `policy.py get` and `policy.py lists --write`
- **hands-off** `TOOL-dRankedPlan-28` — the `triage` and `dupes` rows of `record-kinds.toml`, which that unit registers in the binding reader, the factory table and the HYGIENE kind list (round-1 spec audit, id 28)
- **hands-off** `TOOL-dRankedPlan-29` — `triage.py`'s policy read and its row writer, which that unit's S6 to S8 and S17 correct (round-1 spec audit, ids 9, 17, 20, 44)

## 4. Design

### Evidence

- The row grammar and its renderers are at base: `render_sev_row` (`tools/memory-tree/backlog.py:1538`),
  `render_status_row` (:1532), `render_scope_row` (:1528), `SEVERITIES` (:84). No production code
  writes a `SEV` row: every `render_sev_row` call at base sits in the module's own arms.
- The fold folds several `SEV` rows to the most severe (`derive_statuses`, :993-995), so a label is
  never softened by a later row, and a `WONTDO` row is undone by `REOPEN · <id> · of <slug>`
  (`derive_evidence`, :836-845), the slug being the folder of the file the `WONTDO` row sits in.
- The grade the rules read is the one `--asks` prints: `build_grade_row`
  (`tools/memory-tree/gen_build_index.py:3599`) over `derive_ready` (`backlog.py:1386`), whose six
  rules R1 to R6 are `READY_RULES` (:1311).
- The legacy boundary is declared: `ASK_CUTOFF="2026-10-01"` (`.memory-tree.conf:742`), read by
  `check_filed_before_cutoff` (`backlog.py:1463`), the grandfathering rule `legacy` grades by.
- A `BACKLOG.md` is capped by `INDEX_CAP_BYTES` (61440, `.memory-tree.conf:483`): 434 rows of about
  150 bytes in one file would breach it, so rows go into each ask's own home file.
- `policy.py get plan.triage` prints `rules` at base (catalogue row `tools/policy/catalogue.toml:907-911`).

### The rule grammar

```toml
# .governance/triage-rules.toml
[[triage-rule]]
id = "unlocated"                     # [a-z0-9-]+, unique
enabled = true                       # the owner's switch
when = { ready = ["no"], missing = ["R4"] }
verdict = "defer"                    # select | defer | retire | refuse
level = "LOW"                        # BLOCKER | HIGH | MED | LOW; required for select and defer
why = "cites no path the tree holds"
accept = ""                          # optional: written as an `accept` clause on an ask lacking one
```

| `when` key | Holds when the ask's |
|---|---|
| `status` | status is a member of the list |
| `home` | filing home slug is a member of the list |
| `ready` | grade (`yes`, `legacy`, `no`) is a member of the list |
| `missing` | failing READY rules include every listed rule id |
| `older-than-days` | `filed` date is more than N days before the pass's HEAD commit date |
| `text` | summary text matches the Python regex |
| `cites` | locators include a path under the listed prefix |

Conditions are joined by AND. A rule with an empty `when` matches every ask, which is legal and
the author's to choose. The pass reads HEAD's commit date, never the clock, so a re-run at the same
commit renders the same rows.

### Rows

| Verdict | Rows written for ask `<id>` |
|---|---|
| `select` | `SEV · <id> · <level> · triage rule <rule id>: <why>`, and `select — <id>` printed for the planner |
| `defer` | the same `SEV` row; the ask stays OPEN, filed with its acceptance |
| `retire` | `WONTDO · <id> · retired by triage rule <rule id>: <why>` |
| `refuse` | `WONTDO · <id> · refused by triage rule <rule id>: out of scope, <why>` |

A rule's `accept`, where the ask's merged clauses carry none, adds `SCOPE · <id> · accept <text>`.
A judged ask's why reads `triage judge gov-planner: <why>`. Each row is appended under
`## Dispositions` of the ask's home `BACKLOG.md` by `append_disposition_rows(path, rows)`, which
creates the section when the file lacks it, and the pass then runs `gen_build_index.py --write` so the
views those rows feed are not left stale. The `select` and `defer` verdicts differ in what Plan does
next, not in the rows.

### The three values

| `plan.triage` | Population triaged | Rows | Record `Batch` |
|---|---|---|---|
| `rules` | every live unlabelled ask | written at once | `applied` |
| `owner-batches` | every live unlabelled ask | held; written by `ratify` | `held`, then `ratified` |
| `archive-legacy` | live unlabelled asks filed on or after `ASK_CUTOFF` | written at once | `applied` |

Under `archive-legacy` the asks filed before `ASK_CUTOFF` take `WONTDO · <id> · archived: plan.triage
archive-legacy, filed before ASK_CUTOFF <date>` and no rule is applied to them. A legacy ask that
already carries a `SEV` row was triaged once and is left as it is. An archived ask is restored by one
`REOPEN` row of its home slug, which the help page states.

### The triage record

```markdown
**Serves:** triage TOOL-aFoo-3
- **Value:** owner-batches
- **Rules:** 3f9c2a71
- **Asks:** TOOL-aFoo-3 TOOL-aFoo-7
- **Rows:** 3 rows · 9b1e04c2d7aa
- **Judged:** TOOL-aFoo-7 defer MED
- **Batch:** held
- **Ratified:** pending
```

`Rules` is the first eight hex digits of the rules file's blob at the pass's HEAD, or `none`.
`Asks` lists the ids the record decided, or `intake <key>` for an owner's request triaged inside its
build. `Judged` lists `<id> <verdict> <level>` for each ask the planner decided, joined by `; `,
`pending <ids>` for asks awaiting the judge, or `none`; the judge's why is carried by its row.
`Ratified` is `not-owed` under `rules` and `archive-legacy`, `pending` on a held batch, and `<value>
<witness>` on the record `ratify` writes. The record's `--unit` is the home's lowest decided ask id,
so hygiene check 21's filename join holds; inside a build it is the build's anchor id, the lowest unit
id a spec H1 under it defines (TOOL-dDeclaredLoop-3 S2), and the record sits in that build's folder.

### The witnesses

| Item | Witness `read_plan_item_witness` reads | Outcome |
|---|---|---|
| `item.plan.dedupe` | the build's dupes record | `none` when `Finding` is `none`; a finding routes to `entry.place` |
| `item.plan.triage-rule` | a triage record whose `Asks` names the build's input, `Batch` `applied` or `ratified` | the input's verdict, or `no-rule` when `Judged` reads `pending` for it |
| `item.plan.triage-judge` | a triage record whose `Judged` names the input with a verdict | that verdict |

A held `owner-batches` record witnesses nothing until `ratify` writes its `ratified` successor, so a
build in Plan waits at the owner breakpoint exactly as a backlog batch does.

### The seed

| `id` | `when` | `verdict` | `level` |
|---|---|---|---|
| `ready` | `ready = ["yes"]` | `select` | `MED` |
| `legacy-graded` | `ready = ["legacy"]` | `defer` | `LOW` |
| `unlocated` | `ready = ["no"]`, `missing = ["R4"]` | `defer` | `LOW` |
| `unacceptable` | `ready = ["no"]`, `missing = ["R5"]` | `defer` | `LOW` |

None is `retire` or `refuse`: a rule that ends an ask is the owner's to add.

### Inventory

| Minted | Kind | Lexicon cell |
|---|---|---|
| `tools/memory-tree/triage.py` | module and CLI | none |
| `read_triage_rules`, `match_triage_rule`, `render_triage_rows`, `append_disposition_rows`, `check_judge_return`, `read_batch_rows` | functions, `triage.py` | `py.function`, asked at the pass |
| `pass`, `judge --request`, `judge --return`, `ratify`, `--fixture --plant` | verbs of `triage.py` | none |
| `.governance/triage-rules.toml`, `[[triage-rule]]` | declared-rules file and table | none |
| `triage`, `dupes` | `[[record-kind]]` rows | none |
| `--record` | flag of `plan_items.py dedupe` | none |
| the plants `rules`, `judge`, `owner-batches`, `archive-legacy`, `default`, `bad-rule`, `kinds`, `intake` | fixture cases of `triage.py` | none |
| the plant `triage-witness` | fixture case of `plan_items.py` | none |

### Rollout

`plan.triage` is read at every pass and defaults to `rules`. Nothing runs the pass on its own: the
`item.plan.triage-rule` row runs it inside a build, and an owner or a cadence run runs it over the
backlog. Its fixture arms run inside the `build-index selftest` leg: `gen_build_index.py`'s
`cmd_selftest` imports `triage` beside `backlog` and runs its arms.

### Files touched (estimate)

- `tools/memory-tree/triage.py`: S1 to S6, the arms
- `tools/memory-tree/gen_build_index.py`: `cmd_selftest` runs the triage arms
- `tools/memory-tree/record-kinds.toml`: the `triage` and `dupes` rows, through `record_kinds.py new`
- `tools/loop/plan_items.py`: S7's `--record`, S11's three witness readers, the `triage-witness` plant
- `tools/loop/loop.toml`: three `[[stand-in]]` rows deleted (S11)
- `.governance/triage-rules.toml`: S8's seed
- `tools/policy/catalogue.toml`: `plan.triage`'s `summary` and `usage`
- `tools/policy/unsummarised-keys.txt`: re-rendered by `lists --write`
- `tools/memory-tree/README.md`: names `triage.py`
- `help/plan.md`: S10's section

### Alternatives rejected

- **A new `ARCHIVED` status verb.** It would separate an archive from a decline, and every fold
  reader (`derive_statuses`, the family view, `migrate_backlog.py`) would have to learn it; a
  `WONTDO` row whose why names `archive-legacy`, undone by `REOPEN`, carries the same fact in the
  grammar every reader already holds.
- **Rows into one file.** Writing every row into one build's `BACKLOG.md`, as TOOL-aMendedFleet-14
  did for its 297 rows, breaches `INDEX_CAP_BYTES` at this population.
- **Writing draft rows into the backlog under a hold.** The fold reads every `SEV` row at once and
  keeps the most severe, so a draft label would bind before the owner ratified it.

## 5. Production-readiness checklist

- security — the rules file is read with `tomllib` and never executed; `text` is compiled as a
  regex with a refusal on error; the judge's return is untrusted input, schema-checked before any
  write (S3). A rule can only render the four row shapes, each undone by a later row.
- perf / scale — one fold per pass, about 620 asks at base; rows are appended once per home file.
- error / empty / loading states — an absent rules file sends every ask to the judge; an empty
  population prints `triage — nothing to triage` and writes no record.
- observability — the pass prints one `triage — <id> · <verdict> · <rule|judge>` line per ask and a
  count per rule.
- risks — a loose rule labels many asks at once. Under `rules` the owner reads the result by its
  labels (`--asks` with the rule named in each why), and every row is reversible. A rule that ends
  asks is never seeded. The ratification predicate answers for a build's plan, so a backlog batch is
  ratified as its home build would be: under `hook-keyword` by the owner typing `ratify <home>`, under
  `terminal-command` by the owner's terminal disposition record in that folder, and under `request`
  only in a session that typed the home's own request; a home with no claim stays held under
  `request`, which the help section states.
- testing — the eight `triage.py` plants and the `plan_items.py` plant, red and green.
- migration — none: no row is rewritten, and an ask labelled before this unit is not re-triaged.
- user docs — `help/plan.md`, S10.

## 6. Acceptance criteria

- **AC1** — When `python triage.py --fixture --plant rules` runs over a fixture whose policy file
  sets `plan.triage = "rules"`, one ask matching the rule `unlocated` gains `SEV · <id> · LOW ·
  triage rule unlocated: …` in its own home `BACKLOG.md`, an ask matching no rule gains no row and is
  printed by `judge --request`, and the written record reads `Batch: applied`.
  Red when: an ask no rule matches is labelled, or a label's why does not name its rule.
- **AC2** — When the plant `judge` feeds `triage.py judge --return` a return choosing `retire` for
  the undecided ask, its home file gains `WONTDO · <id> · retired by …` naming `judge`; a return
  naming an id the request did not, or a verdict `close`, exits 2 naming the object and the field,
  and no file changes.
  Red when: an out-of-request id or an unknown verdict reaches a backlog file.
- **AC3** — When the plant `owner-batches` sets `plan.triage = "owner-batches"`, `pass` changes no
  `BACKLOG.md` and writes a record reading `Batch: held`; `ratify` against a stub predicate giving no
  witness exits 1 naming the home and writes nothing; against one giving `request k1` it writes the
  drafted rows and a record reading `Ratified: request k1`; and after a planted extra ask moves the
  population, `ratify` exits 1 with `batch moved`.
  Red when: a held batch's row reaches a backlog before ratification, or a moved batch is written.
- **AC4** — When the plant `archive-legacy` sets `plan.triage = "archive-legacy"` with `ASK_CUTOFF`
  at 2026-10-01, an unlabelled ask filed 2026-09-20 gains `WONTDO · <id> · archived: …`, an
  unlabelled ask filed 2026-10-05 is triaged by its rule, and a labelled ask filed 2026-09-20 gains
  no row; a planted `REOPEN` row returns the archived ask to `OPEN` in `gen_build_index.py --asks`.
  Red when: a new ask is archived, a legacy ask is triaged, or the archive is irreversible.
- **AC5** — When the plant `default` runs with no policy file, `pass` prints one `NOTE:` naming
  `plan.triage` and its default and triages as AC1 does.
  Red when: a refused read stops the pass or takes another value.
- **AC6** — When the plant `bad-rule` gives a row `verdict = "close"`, and another a `select` with no
  `level`, `pass` exits 2 naming `id` and key for each, before any file is written.
  Red when: a malformed rule is skipped silently or applied.
- **AC7** — When `python record_kinds.py --template triage` and `--template dupes` run in the
  fixture's kit, they print the `**Serves:**` line and one `- **<Key>:**` line for each field of S5
  and S7, in that order.
  Red when: a field is missing or the kind is not registered.
- **AC8** — When `python triage.py pass --dry-run` runs at the build run's tip, it prints a count per
  seed rule and exits 0, and `grep -c 'verdict = "retire"' triage-rules.toml` over the seed prints 0.
  Red when: the seed fails to parse or carries a rule that ends an ask.
  figure: the per-rule counts are DERIVED at the run and not pinned here.
- **AC9** — When `python policy.py get plan.triage --explain` runs at the tip, it prints `rules`, and
  `grep -c '^plan.triage$' unsummarised-keys.txt` prints 0.
  Red when: the row is still unsummarised.
- **AC10** — When `grep -n "archive-legacy" plan.md` runs over the help page, it finds the Triage
  section's paragraph on that value naming the `REOPEN` row that restores an ask.
  Red when: the section is absent or omits how an archived ask is restored.
- **AC11** — When the plant `intake` runs `triage.py pass --build tFix` on a build whose input is an
  owner's request, it prints `select` under rule `request` and writes a record whose `Asks` reads
  `intake <key>`, though the planted rules carry an empty-`when` `refuse` rule; on a build selected
  from an ask matching no rule it prints `no-rule` and the record's `Judged` reads `pending <id>`.
  Red when: a declared rule refuses an owner's request, or an undecided input reads as decided.
- **AC12** — When `python plan_items.py --fixture --plant triage-witness` runs, `dedupe --build tFix
  --record` writes a dupes record reading `Finding: none` and `Overlap: unmeasured`, and
  `read_plan_item_witness` answers `item.plan.dedupe` with `none`, `item.plan.triage-rule` with the
  input's verdict, and `item.plan.triage-judge` with the judged verdict; with the triage record
  reading `Batch: held` the triage-rule witness does not hold; and `grep -c "item.plan.triage-rule"`
  over the fixture's `[[stand-in]]` rows prints 0.
  Red when: a held batch witnesses the item, or a stand-in row survives beside its armed reader.

## 7. Gates

`build-index selftest` · `memory hygiene` · `policy fixtures` · `policy check` · `tier2-review self-test` · `lexicon naming predicates` · `spec tokens (a spec's own names resolve)`

New arm: tools/memory-tree/triage.py · covers AC1 AC2 AC3 AC4 AC5 AC6 AC7 AC11 · the eight plants, run inside the build-index selftest leg through gen_build_index.py's cmd_selftest, the failing case a label written without its rule · none

New arm: tools/loop/plan_items.py · covers AC12 · the `triage-witness` plant beside TOOL-dRankedPlan-2's plants, the failing case a held batch read as a witness · none

## 8. Open questions

- **F1 — Where do the declared rules live?** Options: (a) `.governance/triage-rules.toml`, the
  repository's own governance directory beside its policy file; (b) a data file in the memory-tree
  kit; (c) a table in `.governance/policy.toml` read through the policy reader; (d) (a) with the path
  added to `tools/policy/guarded-paths.txt`. (b) is copy-installed and overwritten at an adopter's
  kit update, so an adopter's own rules would not survive one. (c) needs a table type the policy
  reader does not hold, a dGroundRules surface. (d) refuses every agent commit to the file, so the
  build run could not land S8's seed and AC8 fails. RESOLVED (agent, 2026-10-26, delegated): (a),
  rung 3, the most feature-rich survivor: per repository, owner-switchable by each row's `enabled`,
  and reviewed like any commit. grants: PLAY-dClosedLoop-3 the declared-rules file
  `.governance/triage-rules.toml`, the surface clause 0371 names as `plan.triage-rule`'s declared
  rules. widens: none · relaxes: none
- **FACT-QUESTION · F2 — What is the legacy backlog `archive-legacy` archives?** Probe: join
  `gen_build_index.py --asks --all --tsv` at `0689e7fa1` with each ask row's `filed` date, counting
  live unlabelled asks by `filed` against `ASK_CUTOFF` and by `decided_by`. Observation: 434 live
  unlabelled asks, every one filed before 2026-10-01, 297 of them decided by
  `TOOL-aMendedFleet-106`, and 185 live asks filed after the cutoff, every one labelled. Liveness: the
  same join prints a nonzero `after unlabelled` count on any ask filed after the cutoff with no `SEV`
  row, which verdict V12 (`tools/memory-tree/backlog.py:1174-1186`) refuses today. RESOLVED (agent, 2026-10-26,
  delegated): the legacy backlog is the live asks filed before `ASK_CUTOFF` with no `SEV` row, rung 2,
  the declared boundary the `legacy` grade already uses, so no second cutoff is typed. widens: none ·
  relaxes: none
- **F3 — How is an ask archived?** Options: (a) a `WONTDO` row naming `archive-legacy`; (b) a
  `DEFERRED` row onto one archive ask, as TOOL-aMendedFleet-14 did; (c) a new `ARCHIVED` verb. (b)
  keeps the asks live and in every count, which is the defect gap-plan-02 measures. RESOLVED (agent,
  2026-10-26, delegated): (a), rung 3, by the tie-break of reusing the grammar every reader holds;
  `REOPEN` restores one, so nothing is lost. widens: none · relaxes: none
- **F4 — What is the owner breakpoint of `owner-batches`, when the pass runs outside any build?**
  Options: (a) a held batch per home, released by `read_plan_ratification`'s witness (S6); (b)
  TOOL-dDeclaredLoop-19's owner gate, which holds a build at a step exit, and the pass has no build
  phase to hold (flow-steps.md:164-167); (c) a disposition record, whose value
  `check_disposition_record` grades against the disposed item's outcomes, which hold no
  `ratified`. RESOLVED (agent, 2026-10-26, delegated): (a), rung 3, the one survivor, and it reads
  the predicate every ratification in this build reads. widens: none · relaxes: none
- **F5 — Where do the rows go?** Options: (a) each ask's home `BACKLOG.md`; (b) one file. RESOLVED
  (agent, 2026-10-26, delegated): (a), rung 3: (b) breaches `INDEX_CAP_BYTES` at the measured
  population, and (a) keeps each `REOPEN` naming the ask's own slug. widens: none · relaxes: none

## 9. Revision log

- rev-1 · 2026-10-26 · initial draft, from the packet's Items 3, walkthrough P3 and its revision
  (:350-353, :380-383), flow-steps.md:164-190, TOOL-dDeclaredLoop-15 T4 to T6, scout B's row -3, and
  TOOL-dRankedPlan-2's hand-off of `check_plan_dupes` and the three items to arm (its §8 F7).
- rev-2 · 2026-10-27 · §3 · gains the hands-off edge to `TOOL-dRankedPlan-28`, the hands-off edge to `TOOL-dRankedPlan-29`, each the reciprocal of that promoted unit's own edge (round-1 spec audit, `reviews/2026-10-26-review-TOOL-dRankedPlan-1-spec-audit.md`); no other section moves.

## 10. Reuse audit

The seams extended are the backlog grammar's renderers and fold (`render_sev_row`,
`render_status_row` and `render_scope_row` at `tools/memory-tree/backlog.py:1528-1540`,
`derive_statuses` and `derive_evidence`), the grade `--asks` prints (`build_grade_row` at
`tools/memory-tree/gen_build_index.py:3599`), the declared `ASK_CUTOFF`, the record-kind factory and
door (TOOL-dTotalRecall-1 S9, TOOL-dTotalRecall-2 S1), and `derive_section_sha`
(`tools/roles/handoff.py:307`) for the batch key. `python tools/codebase-map/reuse_lookup.py "apply
declared rules to label backlog asks with a severity and record the rule"` ranked name stems
(`records`, `declares`, `render_ask_row`, `derive_ask_locators`); none applies a rule to an ask, so no
existing seam fits the rule engine and S1 adds it beside the renderers. The driver's
`write_backlog_rows` (`tools/unattended/unattended.sh:9791`) writes an ask row with its `SEV` and
`KEEP` rows in one bash call, so it does not fit a disposition-only append from Python; S2 adds
`append_disposition_rows`. S11 extends TOOL-dRankedPlan-2's `read_plan_item_witness` rather than adding a
second witness reader. Scout B cited `migrate_backlog.py --triage-ask` as the archive seam: it is
the switch-over's one-shot filer of a triage ask, not an archive, and F3 takes the `WONTDO` row
instead. The recall query returned `TOOL-aMendedFleet-106`, TOOL-aMendedFleet-14's bulk deferral and
the dDerivedDocket design line making `ASK_CUTOFF` forward-only for `SEV`; source agrees, as verdict
V12 at `tools/memory-tree/backlog.py:1186`, and F2's probe confirms it on the tree.

Recall terms used: `python tools/memory-recall/query.py "how are backlog asks triaged and labelled with a severity by declared rules" --terms "triage severity SEV row unlabelled asks owner-triage aMendedFleet-106 ASK_CUTOFF legacy declared rules archive"`
