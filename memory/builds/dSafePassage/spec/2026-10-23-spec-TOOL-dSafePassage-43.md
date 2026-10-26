# TOOL-dSafePassage-43 — the step row's one writer admits a stopped down's failure on an `applied` row, by one declared prefix set, and refuses every other

**Status:** DEFERRED · rev-2 · 2026-10-23 · node d · Tier-2 · base 3708a705 · streams tooling · order 2 · advances TOOL-dSafePassage-14

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-23-build-TOOL-dSafePassage-43-deviation-89.md](../build/2026-10-23-build-TOOL-dSafePassage-43-deviation-89.md) | deviation | — |
| [2026-10-25-build-TOOL-dSafePassage-1-agent-ledger.md](../build/2026-10-25-build-TOOL-dSafePassage-1-agent-ledger.md) | journal | TOOL-dSafePassage-1 TOOL-dSafePassage-2 TOOL-dSafePassage-3 TOOL-dSafePassage-4 TOOL-dSafePassage-5 TOOL-dSafePassage-6 TOOL-dSafePassage-7 TOOL-dSafePassage-8 TOOL-dSafePassage-9 TOOL-dSafePassage-10 TOOL-dSafePassage-11 TOOL-dSafePassage-12 TOOL-dSafePassage-13 TOOL-dSafePassage-15 TOOL-dSafePassage-16 TOOL-dSafePassage-17 TOOL-dSafePassage-18 TOOL-dSafePassage-19 TOOL-dSafePassage-20 TOOL-dSafePassage-21 TOOL-dSafePassage-22 TOOL-dSafePassage-23 TOOL-dSafePassage-24 TOOL-dSafePassage-25 TOOL-dSafePassage-26 TOOL-dSafePassage-27 TOOL-dSafePassage-28 TOOL-dSafePassage-29 TOOL-dSafePassage-30 TOOL-dSafePassage-31 TOOL-dSafePassage-32 TOOL-dSafePassage-33 TOOL-dSafePassage-34 TOOL-dSafePassage-35 TOOL-dSafePassage-36 TOOL-dSafePassage-37 TOOL-dSafePassage-38 TOOL-dSafePassage-39 TOOL-dSafePassage-40 TOOL-dSafePassage-41 TOOL-dSafePassage-42 TOOL-dSafePassage-44 TOOL-dSafePassage-45 TOOL-dSafePassage-46 TOOL-dSafePassage-47 TOOL-dSafePassage-48 TOOL-dSafePassage-49 TOOL-dSafePassage-50 TOOL-dSafePassage-51 TOOL-dSafePassage-52 TOOL-dSafePassage-53 TOOL-dSafePassage-54 TOOL-dSafePassage-55 TOOL-dSafePassage-56 TOOL-dSafePassage-57 TOOL-dSafePassage-58 TOOL-dSafePassage-59 |
| [2026-10-26-prompt-TOOL-dSafePassage-43-build-brief.md](../prompts/2026-10-26-prompt-TOOL-dSafePassage-43-build-brief.md) | journal | — |
| [2026-10-23-review-TOOL-dSafePassage-43-44-45-46-spec-audit-round1.md](../reviews/2026-10-23-review-TOOL-dSafePassage-43-44-45-46-spec-audit-round1.md) | spec-audit | TOOL-dSafePassage-44 TOOL-dSafePassage-45 TOOL-dSafePassage-46 |

<!-- /gen:spec-records -->

## 1. Goal

The spec audit of units 36 to 42
(`memory/builds/dSafePassage/reviews/2026-10-23-review-TOOL-dSafePassage-36-37-38-39-40-41-42-spec-audit-round1.md`)
confirmed finding **id 2** at HIGH, its item **D-1**. TOOL-dSafePassage-3 §4 "Data model" has
`set_step_state` raise `Refusal` on "a `failure` on a state other than `failed`", and its AC7
(`2026-10-23-spec-TOOL-dSafePassage-3.md:259-262`) observes the refusal of "a `failure` on an
`applied` row". TOOL-dSafePassage-4 S4 (`2026-10-23-spec-TOOL-dSafePassage-4.md:55-59`) and its §4
table (`:131-134`) write exactly that row: move 3 keeps the state and sets `down interrupted: …`
before every down, move 4 sets `down exit <rc>: …`, and move 5 sets
`witness still holds after down`. TOOL-dSafePassage-17 S2 (`2026-10-23-spec-TOOL-dSafePassage-17.md:45-46`)
adds `reverted check exits <rc>`, and TOOL-dSafePassage-33 S3 (`2026-10-23-spec-TOOL-dSafePassage-33.md:47-48`)
writes `witness still holds after down; before-image <path> absent`. TOOL-dSafePassage-39 AC1
(`2026-10-23-spec-TOOL-dSafePassage-39.md:128-131`) needs the row to read `applied` with the
`down interrupted:` failure, and its second non-goal (`:53-55`) leaves the disagreement to "the
units that own it", which no spec names; this unit read each cited line on 2026-10-23. Built as
written, a correct TOOL-dSafePassage-3 writer refuses the row TOOL-dSafePassage-4's pass must write
at order 2. This unit is id 2's promotion: one declared prefix set names a stopped down's failure,
and the one writer admits a `failure` on an `applied` row only when it begins with one of them.

## 2. Scope (IN)

- **S1** — The prefix set. `DOWN_STOP_PREFIXES` in `tools/govkit/upgrade_steps.py`, beside
  `set_step_state`, holds the four openings §4 "Data model" lists. Every failure text the reverse walk
  writes on a row it keeps `applied` or `failed` starts with one of them, built from the constant in
  code rather than retyped. Observed by AC1 and AC3.
- **S2** — The writer's rule. `set_step_state` admits a `failure` on an `applied` row only when the
  text starts with an entry of `DOWN_STOP_PREFIXES`, and raises `Refusal` naming the step and the text
  on any other. A `failed` row still needs a `failure` of any text, and a `rolled-back` row takes none.
  Observed by AC1.
- **S3** — The reader inherits it. `read_step_states` raises on a row the writer would refuse, as
  TOOL-dSafePassage-3 §4 says, so an `applied` row carrying a down stop parses, and `govkit.py check`
  counts a problem on an `applied` row whose failure is not a down stop. Observed by AC2.
- **S4** — The criterion restated. TOOL-dSafePassage-3's AC7 is read as: the probe refuses `state`
  `done`, a `failed` row with no `failure`, a `failure` on a `rolled-back` row, and a `failure` on an
  `applied` row that begins with no entry of `DOWN_STOP_PREFIXES`; it admits
  `down interrupted: started <utc>, no exit recorded` on an `applied` row. Its S2 is read with "an
  `applied` row a down stopped on carries that stop's `failure`". TOOL-dSafePassage-3's §3 hands-off
  bullet to this unit names the reading. Observed by AC1.
- **S5** — The non-goal owned. TOOL-dSafePassage-39's second non-goal, whether an `applied` row may
  carry a `failure`, is answered by S2; its §3 consumes-from bullet on this unit names the owner, and
  its AC1 and AC3 rows are the rows S2 admits. Observed by AC3.

## 3. Non-goals (OUT)

- What the forward walk does with an `applied` row that carries a down stop. The step is still
  applied, as TOOL-dSafePassage-2 S1 reads a row that is `applied`, and this unit changes no walk.
- The `via` mark and its carry: `TOOL-dSafePassage-39`.
- A second record of a stopped down beside the receipt's row, the alternative §4 rejects.

### Edges

- **consumes-from** `TOOL-dSafePassage-3` — `set_step_state`, `read_step_states` and AC7, whose refusal this unit narrows to the failures no stopped down writes; without them there is no writer to carry the rule
- **hands-off** `TOOL-dSafePassage-4` — moves 3, 4 and 5 of the reverse walk, which build their failure texts from `DOWN_STOP_PREFIXES` and write them through the writer this unit's rule admits
- **hands-off** `TOOL-dSafePassage-17` — the `reverted check exits <rc>` failure of S2, built from `DOWN_STOP_PREFIXES` and admitted on an `applied` row
- **hands-off** `TOOL-dSafePassage-39` — the second non-goal's owner: an `applied` row may carry a down stop's failure, so AC1 and AC3 write and read the rows this unit admits
- **hands-off** `TOOL-dSafePassage-33` — S3's `witness still holds after down; before-image <path> absent` built from `DOWN_STOP_PREFIXES` and admitted on an `applied` row, findings 7 and 20 of the spec audit of units 43 to 46
- **hands-off** `TOOL-dSafePassage-49` — AC3 and the rollback-plant half of the arm observed at TOOL-dSafePassage-4's pass, so this unit's arm covers AC1; the row rule as one predicate `test_step_row` that the writer and the reader both call, admitting a `failure` only when absent, null or a non-empty string; move 3 recording a `rolled-back` row `applied`; no stop-text literal outside `DOWN_STOP_PREFIXES`; and a second staged break admitting any failure on an `applied` row, findings 1, 18, 29, 15, 2, 20 and 33 of the spec audit of units 43 to 46

## 4. Design

### Data model

```
DOWN_STOP_PREFIXES = ("down interrupted:", "down exit ", "witness still holds after down",
                      "reverted check exits ")
```

| State | `failure` | Writer |
|---|---|---|
| `applied` | none | admitted |
| `applied` | starts with an entry of `DOWN_STOP_PREFIXES` | admitted |
| `applied` | any other text | `Refusal` naming the step and the text |
| `failed` | any text | admitted |
| `failed` | none | `Refusal` |
| `rolled-back` | any | `Refusal` when a `failure` is given |

The texts each prefix opens, by the spec that writes them:

| Prefix | Full text | Writer's spec |
|---|---|---|
| `down interrupted:` | `down interrupted: started <utc>, no exit recorded` | TOOL-dSafePassage-4 S4 move 3 |
| `down exit ` | `down exit <rc>: <the last stderr line>` | TOOL-dSafePassage-4 S4 move 4 |
| `witness still holds after down` | the bare text, or `…; before-image <path> absent` | TOOL-dSafePassage-4 S4 move 5, TOOL-dSafePassage-33 S3 |
| `reverted check exits ` | `reverted check exits <rc>` | TOOL-dSafePassage-17 S2 |

The forward walk's `interrupted: started <utc>, no exit recorded` (TOOL-dSafePassage-2 S2 move 3)
opens with no entry, so on an `applied` row it is refused: that text belongs on a `failed` row only.

### Inventory

Minted: the constant `DOWN_STOP_PREFIXES` in `tools/govkit/upgrade_steps.py`. No function, conf key,
gate leg, plant or policy key. The refusal is `set_step_state`'s own `raise Refusal`, which
TOOL-dSafePassage-3 adds, so `tools/govkit/refusal_join.py`'s `BRANCH_PIN` does not move.

### Migration

Additive: no receipt at the base records a step.

### Rollout

Live at landing. It builds at order 2, one above TOOL-dSafePassage-3 (order 1), whose writer rule it
repairs. TOOL-dSafePassage-4, also at order 2, writes its moves through this rule, so M6 clause 2
makes the two passes non-parallel: the run sequences this pass before TOOL-dSafePassage-4's, as it
sequences the other order-2 units that share `tools/govkit/upgrade_steps.py`.

### Files touched (estimate)

- `tools/govkit/upgrade_steps.py`
- `tools/govkit/selftest.py`

### Alternatives rejected

- **Recording the interruption outside the row, and dropping AC1's failure clause.** Moves 4 and 5,
  TOOL-dSafePassage-17 and TOOL-dSafePassage-33 write the same shape, so every one of them would need a
  second record, and TOOL-dSafePassage-39 §3 already rejects a second record beside the row.
- **Admitting any `failure` on an `applied` row.** A forward-walk bug that left `interrupted:` on an
  applied row would then pass the writer, and the row would read as completed with a stale failure.
- **Typing the prefix list in the writer and the texts in each caller.** A new down text would drift
  from the list unseen; with one constant, a text built outside it is refused at its own fixture.

## 5. Production-readiness checklist

- security: no new write path; the receipt's one writer gains one admitted shape and keeps refusing
  the rest.
- perf / scale: one `str.startswith` over a four-entry tuple per write.
- error / empty / loading states: a refused text names the step and the text, so a caller that
  builds its failure outside the constant fails at its own fixture.
- observability: the receipt row shows the stopped down's text beside `applied`.
- risks: a down text minted later without the constant is refused, which stops that down's walk
  rather than recording it wrong.
- testing: the writer probe of AC1 and the rollback plants of AC3, through §7.
- migration: additive.
- user docs: N/A — `help/upgrade-steps.md`'s receipt section, written by TOOL-dSafePassage-3 and
  TOOL-dSafePassage-4, names the stop texts already; this unit changes which state may carry them in
  the writer, not what an operator reads.

## 6. Acceptance criteria

- **AC1** — When a `python -c` probe imports `tools/govkit/upgrade_steps.py` by path and calls
  `set_step_state` on a schema-4 receipt, state `applied` with each full text of §4's table is
  admitted; `applied` with `interrupted: started 2026-10-23T00:00:00Z, no exit recorded` and with
  `exit 1: x` each raises `Refusal` naming the text; `rolled-back` with any `failure` raises; and
  `failed` with none raises.
  Red when: a stopped down's text is refused on an `applied` row, or a forward-walk text passes there.
- **AC2** — When `govkit.py check --target <t>` reads a receipt whose `steps` holds an `applied` row
  with `down exit 1: boom`, it counts no problem for the field; with the row's failure set to
  `exit 1: boom` it counts one problem naming the row.
  Red when: the reader refuses a row the writer admits, or admits one it refuses.
- **AC3** — When `python3 "tools/govkit/upgrade_steps.py" fixture rollback --plant down-fails` runs,
  `s3` reads `applied` with a failure starting `down exit 1` and no `Refusal` traceback is printed;
  `--plant witness-stays` leaves `s2` `applied` with `witness still holds after down`; and a
  `python -c` probe reading `DOWN_STOP_PREFIXES` finds each text the two plants left starting with
  one of its entries.
  Red when: the reverse walk's own stop is refused by the writer, or its text opens with no entry.

## 7. Gates

`govkit selftest` · `govkit refusal join` · `govkit acceptance matrix` · `govkit selfcheck` · `recall floor arms` · `encoding posture (text IO names its encoding)` · `spec tokens (a spec's own names resolve)`

New arm: tools/govkit/selftest.py · covers AC1 AC3 · the self-test runs the writer probe over the six rows of §4 and the two rollback plants, its failing case staged by a writer copy that refuses every `failure` on an `applied` row · none

What the check does not cover: a down text whose opening is one of the four but whose rest is wrong;
the writer grades the opening only.

## 8. Open questions

none

## 9. Revision log

- rev-1 · 2026-10-23 · initial draft, the promotion of the spec audit of units 36 to 42's id 2 (HIGH,
  item D-1).
- rev-2 · 2026-10-23 · §3 · the Edges gain the ends this unit owes the promotions of the spec audit of units 43 to 46, written by the disposal stage: `TOOL-dSafePassage-33`, `TOOL-dSafePassage-49`; no other section moved.

## 10. Reuse audit

The seams extended are TOOL-dSafePassage-3's `set_step_state` and `read_step_states`, and the stop
texts of TOOL-dSafePassage-4, TOOL-dSafePassage-17 and TOOL-dSafePassage-33, all specced and unbuilt at
the base. `python tools/codebase-map/reuse_lookup.py "admit a failure text on a row only when it names
a stopped down"` ranked `rows`, `row`, `read_text` and `write_text`, name-token matches in test and
generator files, so no existing seam fits beyond those specs. The prefix table was derived by
`git grep` over this build's specs for each stop text, not from a record.

Recall terms used: `python tools/memory-recall/query.py "how a spec audit's minor findings are batched and their readings carried to the faulted unit" --terms "spec audit minors batch promoted reading hands-off consumes-from order disposal rescope severity"`
