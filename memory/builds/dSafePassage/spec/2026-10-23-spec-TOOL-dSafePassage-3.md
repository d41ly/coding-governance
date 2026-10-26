# TOOL-dSafePassage-3 — the receipt's schema 4: the `steps` field, its one writer, and the step that ships it

**Status:** CLOSED · rev-6 · 2026-10-26 · node d · Tier-2 · base 3708a705 · streams tooling · order 1 · advances TOOL-dSafePassage-14

**Carries:** cl-dClosedLoop-0020@42c7d579 whole

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-23-build-TOOL-dSafePassage-3-deviation-122.md](../build/2026-10-23-build-TOOL-dSafePassage-3-deviation-122.md) | deviation | — |
| [2026-10-23-build-TOOL-dSafePassage-3-deviation-123.md](../build/2026-10-23-build-TOOL-dSafePassage-3-deviation-123.md) | deviation | — |
| [2026-10-23-build-TOOL-dSafePassage-3-deviation-124.md](../build/2026-10-23-build-TOOL-dSafePassage-3-deviation-124.md) | deviation | — |
| [2026-10-23-build-TOOL-dSafePassage-3-deviation-125.md](../build/2026-10-23-build-TOOL-dSafePassage-3-deviation-125.md) | deviation | — |
| [2026-10-25-build-TOOL-dSafePassage-1-agent-ledger.md](../build/2026-10-25-build-TOOL-dSafePassage-1-agent-ledger.md) | journal | TOOL-dSafePassage-1 TOOL-dSafePassage-2 TOOL-dSafePassage-4 TOOL-dSafePassage-5 TOOL-dSafePassage-6 TOOL-dSafePassage-7 TOOL-dSafePassage-8 TOOL-dSafePassage-9 TOOL-dSafePassage-10 TOOL-dSafePassage-11 TOOL-dSafePassage-12 TOOL-dSafePassage-13 TOOL-dSafePassage-15 TOOL-dSafePassage-16 TOOL-dSafePassage-17 TOOL-dSafePassage-18 TOOL-dSafePassage-19 TOOL-dSafePassage-20 TOOL-dSafePassage-21 TOOL-dSafePassage-22 TOOL-dSafePassage-23 TOOL-dSafePassage-24 TOOL-dSafePassage-25 TOOL-dSafePassage-26 TOOL-dSafePassage-27 TOOL-dSafePassage-28 TOOL-dSafePassage-29 TOOL-dSafePassage-30 TOOL-dSafePassage-31 TOOL-dSafePassage-32 TOOL-dSafePassage-33 TOOL-dSafePassage-34 TOOL-dSafePassage-35 TOOL-dSafePassage-36 TOOL-dSafePassage-37 TOOL-dSafePassage-38 TOOL-dSafePassage-39 TOOL-dSafePassage-40 TOOL-dSafePassage-41 TOOL-dSafePassage-42 TOOL-dSafePassage-43 TOOL-dSafePassage-44 TOOL-dSafePassage-45 TOOL-dSafePassage-46 TOOL-dSafePassage-47 TOOL-dSafePassage-48 TOOL-dSafePassage-49 TOOL-dSafePassage-50 TOOL-dSafePassage-51 TOOL-dSafePassage-52 TOOL-dSafePassage-53 TOOL-dSafePassage-54 TOOL-dSafePassage-55 TOOL-dSafePassage-56 TOOL-dSafePassage-57 TOOL-dSafePassage-58 TOOL-dSafePassage-59 |
| [2026-10-26-build-TOOL-dSafePassage-3-deviation-165.md](../build/2026-10-26-build-TOOL-dSafePassage-3-deviation-165.md) | deviation | — |
| [2026-10-26-build-TOOL-dSafePassage-3-ledger.md](../build/2026-10-26-build-TOOL-dSafePassage-3-ledger.md) | journal | — |
| [2026-10-23-prompt-TOOL-dSafePassage-1-spec-brief.md](../prompts/2026-10-23-prompt-TOOL-dSafePassage-1-spec-brief.md) | research | TOOL-dSafePassage-1 TOOL-dSafePassage-2 TOOL-dSafePassage-4 TOOL-dSafePassage-5 TOOL-dSafePassage-6 TOOL-dSafePassage-7 TOOL-dSafePassage-8 TOOL-dSafePassage-9 TOOL-dSafePassage-10 TOOL-dSafePassage-11 TOOL-dSafePassage-12 TOOL-dSafePassage-13 |
| [2026-10-26-prompt-TOOL-dSafePassage-3-1-spec-writer.md](../prompts/2026-10-26-prompt-TOOL-dSafePassage-3-1-spec-writer.md) | research | — |
| [2026-10-26-prompt-TOOL-dSafePassage-3-2-spec-writer.md](../prompts/2026-10-26-prompt-TOOL-dSafePassage-3-2-spec-writer.md) | journal | — |
| [2026-10-26-prompt-TOOL-dSafePassage-3-build-brief.md](../prompts/2026-10-26-prompt-TOOL-dSafePassage-3-build-brief.md) | journal | — |
| [2026-10-23-review-TOOL-dSafePassage-1-2-3-4-5-6-7-8-9-10-11-12-13-spec-audit-round1.md](../reviews/2026-10-23-review-TOOL-dSafePassage-1-2-3-4-5-6-7-8-9-10-11-12-13-spec-audit-round1.md) | spec-audit | TOOL-dSafePassage-1 TOOL-dSafePassage-2 TOOL-dSafePassage-4 TOOL-dSafePassage-7 TOOL-dSafePassage-11 TOOL-dSafePassage-12 TOOL-dSafePassage-8 TOOL-dSafePassage-6 TOOL-dSafePassage-9 TOOL-dSafePassage-10 TOOL-dSafePassage-13 TOOL-dSafePassage-5 |

<!-- /gen:spec-records -->

## 1. Goal

Raise the install receipt to schema 4, which gains `steps`, the per-step progress the walk and gov
first record, without laundering a corrupt schema-3 receipt past the integrity preamble (the shape
audit's H1, SA-3): the `gov_oid` back-fill is pinned to schemas below 3, the change ships as the
upgrade step `govkit/receipt-schema-4` whose down restores schema 3, and every reader of the
receipt's schema is inventoried by value.

## 2. Scope (IN)

- **S1** — `RECEIPT_SCHEMA = 4` at `tools/govkit/govkit.py:50`, its comment saying readers accept 1
  to 4 and that schema 4 is reached by the step `govkit/receipt-schema-4` or by a first install's
  `apply` or `adopt`. Observed by AC3 and AC4.
- **S2** — The field. `steps` is a list of objects `{"id", "introduced", "state"}`, `state` one of
  `applied`, `failed` or `rolled-back`, a `failed` row adding `"failure"`, and the list's last
  `applied` row naming the last completed step. `introduced` is the commit unit 1's reader derives,
  or `null` for a step run before it landed, filled by the next write that sees it landed. A receipt
  below schema 4 carries no `steps`. Observed by AC7 and AC8.
- **S3** — One writer and one reader, in `tools/govkit/upgrade_steps.py`: `set_step_state` is the
  only code that mutates `steps`, and `read_step_states` the only code that parses it. The walk,
  the reverse walk and gov first write through the first (the brief's S4). `govkit check` reads
  through the second, on the receipt it loads at `tools/govkit/govkit.py:5449`, and counts a
  malformed field as a problem. Observed by AC7 and AC8.
- **S4** — The back-fill pinned. The `gov_oid` back-fill at `tools/govkit/govkit.py:9387` runs under
  `schema < 3`, never `schema < RECEIPT_SCHEMA`, so a schema-3 receipt is never back-filled, and its
  comment at :9375-9386 says why. The integrity message at :9441-9445 spells schema 3 where it
  interpolates `RECEIPT_SCHEMA` today, with `below schema 3` on one source line, and `apply`'s
  comment at :7712 names the schema S5 gives. Observed by AC1, AC2 and AC3.
- **S5** — Who moves the number, and what a re-run keeps. One function, `derive_receipt_schema` in
  `tools/govkit/govkit.py`, gives the `schema` and `steps` keys of every receipt `apply` and `adopt`
  write, from the receipt the run rewrites (§4 Data model):
  - a first install, with no prior receipt, is born at schema 4 with `"steps": []` (first install);
  - over a prior receipt whose `schema` is an `int` of 4 or more, its `schema` and, where it holds
    one, its `steps` are carried verbatim. `steps` records EVENTS, so D2's rule
    (`tools/govkit/govkit.py:13100-13113`) holds for it: a re-run never re-measures it, and every
    `applied`, `failed` and `rolled-back` row survives a re-apply and a re-adopt;
  - over any other prior receipt (below schema 4, without a `schema`, or one `--re-adopt` could not
    parse) the write is schema 3 with no `steps` key: the lift to 3 a schema-1 or schema-2 receipt
    gets from `apply` today, and never 4.
  `apply` asks it of the receipt it reads at :7570 and builds its doc at :8014-8025 with `schema` in
  place and `steps` its last key; its rewrites at :8330 and :8436 carry both unchanged. `adopt` asks
  it of the receipt `--re-adopt` rewrites (:13114-13136), or of none, and sets both in the envelope
  it opens at :13098, `steps` after D2's five carried keys at :13130, which stay as they are, so
  `steps` is the envelope's last key. Each verb's
  receipt line (:8441, :13142) prints the schema it wrote. `update`'s re-stamp at :12475 never raises
  a receipt past 3 by itself (`max(schema, 3)`, §4); schema 4 on an existing receipt is the step's
  alone. Observed by AC4, AC9 and AC14.
- **S6** — The step `govkit/receipt-schema-4`, the FIRST row of `tools/govkit/steps.toml`, whose
  program is `tools/govkit/steps/receipt_schema_4.py`. Its up takes a schema-3 receipt to schema 4
  with an empty `steps`, in one atomic write; its down restores schema 3, the field gone, in
  govkit's own serialization; its witness exits 0 at schema 4 or above with `steps` a list.
  Observed by AC5, AC6 and AC10.
  **Readers:** by name: READER NOT IN TREE — the field's one parser, `read_step_states`, is built by
  this unit; the down takes the field out of a receipt and retires no name · by value: `govkit check`'s
  call of `read_step_states`, and the walk's use of the last `applied` row.
- **S7** — The receipt's readers, inventoried by value (§4 Inventory), each disposed: the govkit
  sites, matrix's schema fixtures (`build_role_pair` in `tools/govkit/matrix.py`, which takes a
  `steps` field out of a receipt it forces below schema 4), the selftest's schema assertions, and
  `tools/run-gates/check-receipt.py`, which reads the schema only to print it and writes a schema-3
  fixture, both left as they are. Observed by AC11 and AC12.
  **Readers:** by name: `tools/govkit/govkit.py`, `tools/govkit/matrix.py`,
  `tools/govkit/selftest.py`, `tools/run-gates/check-receipt.py`,
  `tools/govkit/fixtures/make_adopter_receipt.py` · by value: `RECEIPT_SCHEMA` at every comparison §4
  Inventory lists, and `build_role_pair`'s `schema` argument.
- **S8** — The help page `help/upgrade-steps.md` gains a section on what the receipt records: the
  schema, `steps` and its three states, and that a first install is born at schema 4 while an
  existing receipt keeps its schema and its `steps` across a re-apply or a re-adopt, reaching 4 only
  by the step. Observed by AC13.

## 3. Non-goals (OUT)

- The grammar, the reader, the steps file and the before-image helpers, which are
  `TOOL-dSafePassage-1`'s. This unit adds one row and one program under them.
- Running steps and advancing the receipt per completed step (`TOOL-dSafePassage-2`), the reverse
  walk and the recorded rollback (`TOOL-dSafePassage-4`), and gov's own source-mode receipt
  (`TOOL-dSafePassage-8`).
- The research's other schema-4 fields, `superseded`, `deprecations` and `prior_commit`, which v2
  leaves to dShippedRelease.
- `TOOL-dRetiredFork-38`: a `--kits`-scoped update back-fills only its scoped rows and re-stamps the
  whole receipt. The pin narrows the population that back-fill reaches and fixes nothing else.
- Moving the schema-1 and schema-2 migration paths, which stay in `update`'s preamble.

### Edges

- **consumes-from** `TOOL-dSafePassage-1` — the step-row grammar, the steps file, `read_steps` and the
  derived introducing commit this unit's row and field rely on; without them the row has no reader.
- **hands-off** `TOOL-dSafePassage-2` — writing each step's state through the one writer, and
  re-reading the receipt from disk after each step, since this step's up rewrites it.
- **hands-off** `TOOL-dSafePassage-4` — running this step's down last in a rollback, after every other
  applied step's down, since the down refuses while another step reads applied.
- **hands-off** `TOOL-dSafePassage-8` — recording gov's own steps through the one writer, a step run
  before it landed recorded with a null introducing commit.
- **hands-off** `TOOL-dSafePassage-11` — the floor step's row, placed second in the steps file, after
  this unit's.
- **hands-off** `TOOL-dSafePassage-16` — the writer's below-schema-4 precondition exported as one predicate, and the bootstrap rule stated, the repair of finding 50
- **hands-off** `TOOL-dSafePassage-20` — the reader's unlanded value taken as null at the writer's boundary, the repair of finding 3
- **hands-off** `TOOL-dSafePassage-26` — the minors batch of the round-1 spec audit, which repairs the findings that land on this unit after every unit is built
- **hands-off** `TOOL-dSafePassage-33` — the optional mark on an applied step row saying the forward walk applied it by witness alone, accepted and refused at the one writer and reader, the repair of finding 40 of the round-1 audit of units 15 to 26
- **hands-off** `TOOL-dSafePassage-39` — `set_step_state` carrying `via` across a rewrite that keeps a row `applied`, the repair of finding 23 of the spec audit of units 27 to 35
- **hands-off** `TOOL-dSafePassage-43` — the writer admitting a `failure` on an `applied` row only when it opens with an entry of `DOWN_STOP_PREFIXES`, so AC7 is read with that refusal narrowed, the repair of finding 2 of the spec audit of units 36 to 42

## 4. Design

### Data model

```json
{
  "schema": 4,
  "gov_source": "...",
  "gov_commit": "...",
  "kits": ["..."],
  "files": ["..."],
  "steps": [
    {"id": "govkit/receipt-schema-4", "introduced": "<sha or null>", "state": "applied"},
    {"id": "lib/python-floor-3.15", "introduced": null, "state": "failed", "failure": "<text>"}
  ]
}
```

`set_step_state(receipt, step_id, introduced, state, failure=None)` raises `Refusal` on a receipt
below schema 4, an id that is not a string, a state outside the three, a `failure` on a state other
than `failed` or none on `failed`, and an `introduced` that is neither a 40-hex string nor `None`. It
moves any existing row for the id to the end, so the last `applied` row stays the last completed
step, and keeps a known `introduced` where the new value is `None`. It mutates the dictionary and
persists nothing; the caller writes the receipt.

`read_step_states(receipt)` returns the rows, raising `Refusal` on a `steps` field below schema 4,
a schema-4 receipt without the field, or any row the writer would refuse.

`derive_receipt_schema(prior)` takes the parsed receipt a run rewrites, or `None` when there is none,
and returns the dictionary of the two keys that run writes:

| `prior` | Returned |
|---|---|
| `None`, a first install | `{"schema": RECEIPT_SCHEMA, "steps": []}`, the first install's shape |
| `schema` an `int` of 4 or more | its `schema`, and its `steps` verbatim where the key is present |
| anything else: below 4, no `schema`, a non-`int`, or `{}` for an unparsed `--re-adopt` prior | `{"schema": 3}` |

It reads `prior` and writes nothing. A carried `steps` is never checked here: a malformed one, or a
schema-4 prior without the key, is written back as it was and `check` counts it through
`read_step_states` (S3), so a corrupt record is reported where it is read and never repaired by a
re-run. A first install's empty list records no event; it is the field schema 4 requires, which is
why a first `adopt` writes it while D2 has a first `adopt` omit the five install-record keys.

The step row:

```toml
# tools/govkit/steps.toml, its first row
[[upgrade]]
id = "govkit/receipt-schema-4"
up = ["python", "{gov}/govkit/steps/receipt_schema_4.py", "up", "{target}"]
down = ["python", "{gov}/govkit/steps/receipt_schema_4.py", "down", "{target}"]
witness = ["python", "{gov}/govkit/steps/receipt_schema_4.py", "witness", "{target}"]
resume = "atomic"
surfaces = []
needs-target = false
```

The program reads `<target>/.governance/install.json`. Its up exits 0 at schema 4 or above with
`steps` a list; exits 1 naming the schema, writing nothing, below schema 3 (§8 F4); and otherwise
sets `schema` to 4 in place and appends an empty `steps` list as the last key, written to a temporary file
and renamed over the receipt, so a kill leaves either receipt and never half of one. Its down exits 0
at schema 3 without the field; exits 1, writing nothing, while `steps` holds an `applied` row for any
other step; and otherwise sets `schema` to 3 and takes the field out, by the same atomic write. A
schema-4 receipt without the field, or a schema-3 one with it, the two shapes a foreign writer could
leave, are normalised to schema 3 without the field. Both write `json.dumps(receipt, indent=2) +
"\n"`, govkit's own serialization (`tools/govkit/govkit.py:12468-12511`), so the down's output equals
the up's input for every receipt `apply`, `adopt` or `update` wrote.

`update`'s re-stamp at `tools/govkit/govkit.py:12475` becomes `max(<the receipt's schema>, 3)`: the
preamble still lifts a schema-1 or schema-2 receipt to 3 and back-fills it, and nothing but the
step lifts it to 4.

### Inventory

Minted: `set_step_state`, `read_step_states` (`tools/govkit/upgrade_steps.py`, cell `py.function`
snake, verbs set and read); `derive_receipt_schema` (`tools/govkit/govkit.py`, cell `py.function`,
verb derive: `python tools/lexicon/lexicon.py --suggest derive_receipt_schema --as py.function`
printed OK on 2026-10-26); `cmd_up`, `cmd_down`, `cmd_witness`, `main`
(`tools/govkit/steps/receipt_schema_4.py`); the step id `govkit/receipt-schema-4`.

The receipt's readers by value, from
`git grep -n -E 'RECEIPT_SCHEMA|"schema"|get\("schema"' -- tools skills .githooks` at the base, each
line re-read at HEAD `2ac1c347`, the lines cited here. The other readers
`git grep -l install.json -- tools skills .githooks` lists read `files`, `kits` or `gov_commit`, and
none compares the key set, so an added key reaches none of them.

| Reader | What it does with the value | Disposition |
|---|---|---|
| `tools/govkit/govkit.py:50` | the constant | 4, comment re-worded (S1) |
| `tools/govkit/govkit.py:5449` | `check` loads the receipt | reads `steps` through `read_step_states` (S3) |
| `tools/govkit/govkit.py:5560-5565` | `check`'s comment on a receipt below schema 3 | unchanged: already spells 3 |
| `tools/govkit/govkit.py:7712` | comment, "the receipt, schema 3" | names the schema S5 gives |
| `tools/govkit/govkit.py:7570`, `:8014-8025`, `:8330`, `:8436` | `apply` reads the prior receipt, rebuilds the doc at `RECEIPT_SCHEMA` carrying only `orders`, `after` and `gate_runner` from it, and writes it three times | `schema` and `steps` from `derive_receipt_schema(receipt)`, `steps` last; both rewrites keep them (S5) |
| `tools/govkit/govkit.py:13098`, `:13114-13136` | `adopt`'s envelope writes `RECEIPT_SCHEMA`, and `--re-adopt` carries D2's five install-record keys from the prior receipt | `schema` and `steps` from `derive_receipt_schema` of that prior, or of none; D2's five keys unchanged (S5) |
| `tools/govkit/govkit.py:8441`, `:13142` | `apply` and `adopt` print `RECEIPT_SCHEMA` as the schema written | print the schema written (S5) |
| `tools/govkit/govkit.py:9540` | `update` prints the receipt's schema | unchanged |
| `tools/govkit/govkit.py:9209` | `update` reads the receipt's schema | unchanged |
| `tools/govkit/govkit.py:9375-9387` | the back-fill under `schema < RECEIPT_SCHEMA` | `schema < 3` (S4) |
| `tools/govkit/govkit.py:9441-9445` | the integrity message interpolates `RECEIPT_SCHEMA` | spells 3 (S4) |
| `tools/govkit/govkit.py:9753`, `:9777` | the schema-1 and schema-2 role arms | unchanged |
| `tools/govkit/govkit.py:12475` | the re-stamp writes `RECEIPT_SCHEMA` | `max(schema, 3)` (S5) |
| `tools/govkit/matrix.py:484-486` | `build_role_pair` forces a schema onto an `apply`-written receipt | forcing below 4 also takes `steps` out (S7) |
| `tools/govkit/selftest.py:3546` | a first `apply` receipt equals `RECEIPT_SCHEMA` | unchanged: a first `apply` writes 4 |
| `tools/govkit/selftest.py:8677-8678` | an `update --write` re-stamps at `RECEIPT_SCHEMA` | asserts the receipt keeps its schema, now that the re-stamp caps at 3 |
| `tools/govkit/selftest.py:8878-8880` | "at the CURRENT schema, so no migration fills them in" | asserts schema 3 or above, the pin's real condition |
| `tools/govkit/selftest.py:9794-9795` | `schema == 3 == GK9.RECEIPT_SCHEMA` | `schema == 3` |
| `tools/govkit/selftest.py:12970-12972` | a first `adopt` carries none of D2's five install-record keys | unchanged: its tuple names the five, and a first `adopt`'s empty `steps` records no event |
| `tools/run-gates/check-receipt.py:198`, `:437` | writes a schema-3 fixture; prints the schema | unchanged |
| `tools/govkit/fixtures/make_adopter_receipt.py:302`, the `ic` fixture | a real adopter's schema-3 vintage | unchanged: it is a schema-3 receipt |

Each new `raise Refusal` site in `tools/govkit/upgrade_steps.py` and `tools/govkit/govkit.py` is an
anchor of `tools/govkit/refusal_join.py`, armed by a `tools/govkit/selftest.py` arm, and its
`BRANCH_PIN` floor moves by the measured count.

### Migration

A receipt at schema 1, 2 or 3 keeps working with no step run: every reader the inventory lists
accepts it, and the field it lacks is one `read_step_states` refuses only at schema 4. An old govkit
reading a schema-4 receipt finds one unknown key and no refusal (`tools/govkit/govkit.py:9209` reads
the number; no branch refuses a schema above its own).

### Rollout

The step is live when `TOOL-dSafePassage-2`'s walk runs it; until then a first install writes schema
4 and an existing receipt stays at 3 through every `apply`, `adopt --re-adopt` and `update`, which
every reader accepts.

### Files touched (estimate)

- `tools/govkit/govkit.py`
- `tools/govkit/upgrade_steps.py`
- `tools/govkit/steps.toml`
- `tools/govkit/steps/receipt_schema_4.py`
- `tools/govkit/selftest.py`
- `tools/govkit/matrix.py`
- `tools/govkit/refusal_join.py`
- `help/upgrade-steps.md`

### Alternatives rejected

- Bumping the constant with the back-fill left under `schema < RECEIPT_SCHEMA`: SA-3's laundering.
- A before-image for the receipt (§8 F5).
- The re-stamp writing schema 4 (§8 F2).
- `apply` and `adopt` writing schema 4 with an empty `steps` on every run (§8 F3 (c)).
- Two copies of the rule, one in `apply` and one in `adopt`: the second instance of one decision,
  which `derive_receipt_schema` holds once.

## 5. Production-readiness checklist

- security — the pin is the security change: a text-merged schema-3 row with `commit` and no
  `gov_oid` still refuses the whole run before any write. The writer refuses every malformed state.
- perf / scale — one JSON read and one atomic write per step run.
- error / empty / loading states — an empty `steps` is legal and means no step has run; a malformed
  field refuses with the receipt's path and the row, and a re-run carries it as it was, for `check`
  to report.
- observability — `check` names a malformed field; the step's up and down print the schema they read
  and the one they wrote.
- risks — a receipt not in govkit's serialization (the `ic` fixture uses a one-space indent) does not
  round-trip byte-identical through up and down; every receipt govkit writes does.
- testing — `tools/govkit/selftest.py` arms on scratch targets, one per criterion.
- migration — §4 Migration.
- user docs — the receipt section of `help/upgrade-steps.md` (S8).

## 6. Acceptance criteria

- **AC1** — When a scratch target's receipt is set to schema 3 and one engine row keeps `commit`
  with its `gov_oid` taken out, `govkit.py update --target <t>` exits 2 and its stderr names
  `commit` and no `gov_oid` for that row's path, with `RECEIPT_SCHEMA` at 4.
  Red when: the back-fill is staged back to `schema < RECEIPT_SCHEMA`, fills the row, and the run
  exits 0.
- **AC2** — When the same receipt is set to schema 2 instead, `govkit.py update --target <t>` fills
  the row's `gov_oid` from gov's blob at its `commit` and classifies it without a refusal.
  Red when: the pin is staged to `schema < 2`, and the schema-2 row refuses.
- **AC3** — When `grep -n -E 'RECEIPT_SCHEMA = 4|below schema 3' tools/govkit/govkit.py` runs, it
  prints the constant with its comment naming readers 1 to 4, and the integrity message's
  "A receipt below schema 3".
  Red when: the message still interpolates `RECEIPT_SCHEMA` and would print 4.
- **AC4** — When `govkit.py apply --target <t>` makes a first install on a scratch target with no
  receipt, its `.governance/install.json` reads `"schema": 4` and, a first install, `"steps": []`
  as its last key; when `govkit.py adopt --target <t> --write` makes a first install on a scratch
  target with no receipt, its receipt reads the same.
  Red when: either first receipt carries no `steps`, or reads a schema other than 4.
- **AC5** — When the step's `witness` argv runs on a schema-3 receipt `apply` wrote and was forced
  back to 3, it exits 1; after the `up` argv it exits 0 and the receipt reads schema 4 with an
  empty `steps` list; after the `down` argv the receipt's bytes equal the schema-3 bytes before the up.
  Red when: a byte differs after the down.
- **AC6** — When the `up` argv runs on a schema-2 receipt, it exits 1 and the file is unchanged;
  when the `down` argv runs while `steps` holds an `applied` row for `lib/python-floor-3.15`, it exits
  1 and the file is unchanged; when it runs on a schema-4 receipt with no `steps`, it leaves schema 3.
  Red when: either refusal writes the file.
- **AC7** — When a `python -c` probe imports `tools/govkit/upgrade_steps.py` and calls
  `set_step_state` on a schema-3 receipt, it raises `Refusal`; on a schema-4 receipt it appends
  `{"id", "introduced", "state"}`; it refuses `state` `done`, a `failed` row with no `failure`, and a
  `failure` on an `applied` row; a second call for the same id moves the row to the end; and a call
  with `introduced` `None` keeps a known commit.
  Red when: a schema-3 receipt gains `steps`.
- **AC8** — When `govkit.py check --target <t>` reads a receipt whose `steps` holds a row with state
  `done`, it counts a problem naming the row; on a receipt whose `steps` is valid, it counts none for
  the field.
  Red when: the malformed row passes.
- **AC9** — When a clean `govkit.py update --target <t> --write` runs on a schema-3 receipt with no
  walk, the receipt stays at schema 3; on a schema-4 receipt it stays at 4.
  Red when: the re-stamp writes 4 onto a receipt with no `steps`.
- **AC10** — When `python tools/govkit/upgrade_steps.py list` runs on gov's tree after the build, its
  first row is `govkit/receipt-schema-4`.
  Red when: another row precedes it.
- **AC11** — When a `python -c` probe calls matrix's `build_role_pair` with `schema=3`, the receipt
  it leaves reads schema 3 and carries no `steps` key.
  Red when: the forced schema-3 receipt keeps `steps`, the shape `read_step_states` refuses.
- **AC12** — When `grep -n -F '3 == GK9.RECEIPT_SCHEMA' tools/govkit/selftest.py` runs, it prints
  nothing, and `tools/run-gates/check-receipt.py` is byte-identical to the base by
  `git diff --quiet <base> -- tools/run-gates/check-receipt.py`.
  Red when: the stale equality is still there, or `check-receipt.py` moved.
- **AC13** — When `grep -n -E 'steps|rolled-back|first install' help/upgrade-steps.md` runs, it
  prints the receipt section naming `steps`, its three states, and the sentence saying a first
  install is born at schema 4 and an existing receipt reaches 4 only by the step.
  Red when: the page names neither the states nor the first install.
- **AC14** — Four scratch targets, each first installed by `govkit.py apply --target <t>`: on two,
  the receipt is planted at schema 4 with `steps` holding the one row
  `{"id": "govkit/receipt-schema-4", "introduced": null, "state": "applied"}`; on the other two, it
  is forced to schema 3 with `steps` taken out. When `govkit.py apply --target <t>` re-runs on one
  target of each plant and `govkit.py adopt --target <t> --re-adopt --write` runs on the other, the
  planted schema-4 receipt reads schema 4 with that one row, byte-equal to the planted `steps`, after
  both commands, and the planted schema-3 receipt reads schema 3 with no `steps` key after both; each
  command's receipt line prints the schema it wrote.
  Red when: a re-run writes an empty `steps` over the planted row, or a planted schema-3 receipt
  reads 4 after either command.

## 7. Gates

`govkit selftest` · `govkit refusal join` · `govkit acceptance matrix` · `recall floor arms` · `govkit selfcheck` · `govkit runbook parity` · `receipt sync (installed files match the receipt)` · `memory hygiene` · `spec tokens (a spec's own names resolve)`

New arm: tools/govkit/selftest.py · covers AC1 AC2 AC4 AC5 AC6 AC7 AC8 AC9 AC14 · each case staged by its own scratch target, one forced schema, one taken-out field or one planted state per arm · `tools/govkit/refusal_join.py` `BRANCH_PIN`, by the measured count

What these arms do not check: a receipt in a serialization govkit never writes, and whether a caller
persists the receipt after `set_step_state`, which is the walk's.

## 8. Open questions

- **F1 — Where do the field's writer and reader live?** (a) `tools/govkit/upgrade_steps.py`, beside
  the walk that calls them. (b) `tools/govkit/govkit.py`. The walk lives in the step module (the
  brief's S3), and govkit imports that module, so (b) would make the step module import govkit back.
  Recommendation (a). Rung 1, the brief's S3 and S4. RESOLVED (agent, 2026-10-23, delegated): (a).
- **F2 — Does `update`'s re-stamp still write `RECEIPT_SCHEMA`?** (a) No: it writes
  `max(schema, 3)`, and only the step lifts a receipt to 4. (b) Yes. Under (b) every clean update
  stamps 4 on a receipt with no `steps`, which `read_step_states` refuses, and the step's witness
  holds on a receipt it never migrated. (b) fails AC8 and AC9. Recommendation (a). Rung 3.
  RESOLVED (agent, 2026-10-23, delegated): (a).
- **F3 — What schema and `steps` do `apply` and `adopt` write?** (a) A first install writes 4 and
  `"steps": []` (first install); a re-run keeps a prior schema of 4 or more with its `steps` verbatim,
  and writes any other prior as schema 3 with no `steps` (S5). (b) 3 on a first install too, left for
  the step. (c) 4 with an empty `steps` on every run. Under (b) every first install owes a migration
  for a field it could have been born with, and the walk's first act on it is a write. Under (c) a
  re-run over schema 4 discards every row the walk reads, `TOOL-dSafePassage-2`'s pending set being
  the step record (its §8 F1), so a rolled-back step is applied again; and over schema 3 it lifts an
  existing receipt to 4 without the step, which F2's reasoning forbids. Recommendation (a). Rung 3.
  RESOLVED (agent, 2026-10-26, delegated): (a), the re-run half from the 2026-10-26 build brief's
  direction; the first-install half as resolved on 2026-10-23.
- **F4 — What does the up do with a receipt below schema 3?** (a) Exit 1 and write nothing: the
  preamble lifts it to 3 first. (b) Lift it straight to 4. Under (b) the schema-1 or schema-2 rows
  would reach 4 without their `gov_oid` back-fill, which the pin then never runs, so S9 refuses that
  receipt forever. (b) fails AC1's guarantee on every older adopter. Recommendation (a). Rung 3.
  RESOLVED (agent, 2026-10-23, delegated): (a).
- **F5 — How is the down byte-identical?** (a) A semantic inverse in govkit's own serialization.
  (b) `TOOL-dSafePassage-1`'s before-image. The receipt changes after this step by design, as each
  later step's state row and the re-stamp land, so (b)'s after-hash never matches at rollback and its
  down would refuse every real rollback. (a) is exact for every receipt govkit wrote, and §5 states
  the one it is not. Recommendation (a). Rung 3. RESOLVED (agent, 2026-10-23, delegated): (a).
- **F6 — Does the down refuse while another step reads applied?** (a) Yes. (b) No, leaving order to
  the reverse walk. Under (b) a down run out of order deletes every other step's record, which the
  reverse walk then cannot read. (a) guards the record at its one writer. Recommendation (a). Rung 3.
  RESOLVED (agent, 2026-10-23, delegated): (a).
- **F7 — What `introduced` does a step run before it landed record?** (a) `null`, filled by the next
  write that sees the id landed. (b) The commit it ran at. A commit on a branch is not the commit that
  lands the row after the merge, so (b) records a value unit 1's reader never derives (its deviation
  11). Recommendation (a). Rung 3. RESOLVED (agent, 2026-10-23, delegated): (a).
- **F8 — Does `check` grade the field?** (a) Yes, through `read_step_states`. (b) No. The field is
  written by four units and read by the walk, so a malformed row found only by the walk stops an
  update mid-way; (a) reports it where nothing is written. Recommendation (a), charter
  `[security]`. Rung 3. RESOLVED (agent, 2026-10-23, delegated): (a).
- **F9 — Does the walk's copy of the receipt see this step's write?** The step rewrites the receipt
  on disk while `update` holds it in memory (`tools/govkit/govkit.py:9208`). (a) The walk re-reads
  the receipt from disk after every step, handed off to `TOOL-dSafePassage-2`. (b) This step is run
  in process. (b) breaks the brief's S1, which makes every step an argv. Recommendation (a). Rung 1,
  the brief's S1. RESOLVED (agent, 2026-10-23, delegated): (a).

## 9. Revision log

- rev-1 · 2026-10-23 · initial draft, from the spec brief
  `memory/builds/dSafePassage/prompts/2026-10-23-prompt-TOOL-dSafePassage-1-spec-brief.md` and the
  packet's Items 3.
- rev-2 · 2026-10-23 · §3 · the Edges gain the ends this unit owes the promotions of the round-1 spec audit's findings, written by the disposal stage: `TOOL-dSafePassage-16`, `TOOL-dSafePassage-20`, `TOOL-dSafePassage-26`; no other section moved.
- rev-3 · 2026-10-23 · §3 · the Edges gain the ends this unit owes the promotions of the round-1 audit of units 15 to 26, written by the disposal stage: `TOOL-dSafePassage-33`; no other section moved.
- rev-4 · 2026-10-23 · §3 · the Edges gain the ends this unit owes the promotions of the spec audit of units 27 to 35, written by the disposal stage: `TOOL-dSafePassage-39`; no other section moved.
- rev-5 · 2026-10-23 · §3 · the Edges gain the ends this unit owes the promotions of the spec audit of units 36 to 42, written by the disposal stage: `TOOL-dSafePassage-43`; no other section moved.
- rev-6 · 2026-10-26 · S1 S3 S4 S5 S8 · §4 · AC4 AC5 AC13 AC14 · §7 · §8 F3 F9 · §10 · from the
  spec-writer brief `memory/builds/dSafePassage/prompts/2026-10-26-prompt-TOOL-dSafePassage-3-2-spec-writer.md`:
  S5 said `apply` and `adopt` write a fresh schema-4 receipt with an empty `steps`, and also that
  schema 4 on an existing receipt is the step's alone, while at HEAD `2ac1c347` `apply` rebuilds over
  the prior receipt and `adopt --re-adopt` carries D2's five keys from it. S5 now states the
  first-install and re-run cases through one function, `derive_receipt_schema`; the §4 Inventory rows
  for `apply` and `adopt` name the re-run at their lines; F3 gains option (c); AC14 observes both
  plants under both commands, and the selftest `New arm:` line covers it; AC4 adds a first `adopt`;
  every `tools/govkit/govkit.py`, `tools/govkit/selftest.py` and `tools/govkit/matrix.py` line the
  spec cites is re-read at HEAD `2ac1c347`. Cross-read against TOOL-dSafePassage-2, -4, -15, -16,
  -19 and -20, which agree and are not changed.

## 10. Reuse audit

The seams extended, found with `python tools/codebase-map/reuse_lookup.py "migrate the install
receipt to a new schema version and record per-step progress"` and by reading the hits: the
preamble's back-fill and S9 integrity arms (`tools/govkit/govkit.py:9375-9446`), narrowed rather than
copied; govkit's receipt serialization (`tools/govkit/govkit.py:12468-12511`), whose bytes the step
writes; `write_atomic`'s temporary-and-rename pattern (`tools/govkit/govkit.py:4224`), which the step
program repeats because it runs isolated and cannot import govkit; `adopt`'s D2 carry
(`tools/govkit/govkit.py:13100-13136`), whose verbatim-carry rule `derive_receipt_schema` applies to
`steps` for both verbs, beside its five keys rather than inside its tuple, because the first-install
case writes the field D2 would omit; matrix's `build_role_pair` (`tools/govkit/matrix.py:422`), the
one place a fixture forces a schema; and unit 1's step row and reader. No existing seam records
per-step progress: the lookup's `record` hits are run-log records (`tools/runlog/record.py`), another
kit's, so the field's writer is new. Where a hit disagreed with source: the shape audit cites the
messages at `govkit.py:5278` and `:9007-9011`, which are at `:5560-5565` and `:9436-9446` at HEAD
`2ac1c347`, and the first already spells schema 3. The recall probe surfaced `TOOL-dRetiredFork-38`,
named in §3.

Recall terms used: `python tools/memory-recall/query.py "how was the receipt schema bumped before and
which readers compare the schema number" --terms "receipt schema RECEIPT_SCHEMA gov_oid back-fill
install.json S9 integrity migration readers"`
