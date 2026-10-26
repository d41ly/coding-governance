# TOOL-dTotalRecall-2 — the one `record` write door, `gov_record.py new <kind>`, grown from the record factory: minting under a claim or lease, idempotent and content-addressed, rendering and refusing

**Status:** OPEN · rev-2 · 2026-10-26 · node d · Tier-2 · base 462d20f3 · streams tooling · order 12 · advances TOOL-dTotalRecall-27

**Carries:** cl-dClosedLoop-0213@bfd195a1 whole

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-25-build-TOOL-dTotalRecall-1-reuse-scout-a.md](../build/2026-10-25-build-TOOL-dTotalRecall-1-reuse-scout-a.md) | research | TOOL-dTotalRecall-1 TOOL-dTotalRecall-3 TOOL-dTotalRecall-4 TOOL-dTotalRecall-7 TOOL-dTotalRecall-16 TOOL-dTotalRecall-18 TOOL-dTotalRecall-19 TOOL-dTotalRecall-20 TOOL-dTotalRecall-22 TOOL-dTotalRecall-25 |
| [2026-10-26-build-TOOL-dTotalRecall-1-agent-ledger.md](../build/2026-10-26-build-TOOL-dTotalRecall-1-agent-ledger.md) | journal | TOOL-dTotalRecall-1 TOOL-dTotalRecall-3 TOOL-dTotalRecall-4 TOOL-dTotalRecall-5 TOOL-dTotalRecall-6 TOOL-dTotalRecall-7 TOOL-dTotalRecall-8 TOOL-dTotalRecall-9 TOOL-dTotalRecall-10 TOOL-dTotalRecall-11 TOOL-dTotalRecall-12 TOOL-dTotalRecall-13 TOOL-dTotalRecall-14 TOOL-dTotalRecall-15 TOOL-dTotalRecall-16 TOOL-dTotalRecall-17 TOOL-dTotalRecall-18 TOOL-dTotalRecall-19 TOOL-dTotalRecall-20 TOOL-dTotalRecall-21 TOOL-dTotalRecall-22 TOOL-dTotalRecall-23 TOOL-dTotalRecall-24 TOOL-dTotalRecall-25 TOOL-dTotalRecall-26 TOOL-dTotalRecall-36 TOOL-dTotalRecall-37 TOOL-dTotalRecall-38 TOOL-dTotalRecall-39 TOOL-dTotalRecall-40 TOOL-dTotalRecall-41 TOOL-dTotalRecall-42 TOOL-dTotalRecall-43 TOOL-dTotalRecall-44 TOOL-dTotalRecall-45 TOOL-dTotalRecall-46 TOOL-dTotalRecall-47 TOOL-dTotalRecall-48 TOOL-dTotalRecall-49 TOOL-dTotalRecall-50 TOOL-dTotalRecall-51 TOOL-dTotalRecall-52 TOOL-dTotalRecall-53 |
| [2026-10-26-build-TOOL-dTotalRecall-1-spec-fix-return.md](../build/2026-10-26-build-TOOL-dTotalRecall-1-spec-fix-return.md) | research | TOOL-dTotalRecall-1 TOOL-dTotalRecall-3 TOOL-dTotalRecall-4 TOOL-dTotalRecall-5 TOOL-dTotalRecall-6 TOOL-dTotalRecall-7 TOOL-dTotalRecall-8 TOOL-dTotalRecall-9 TOOL-dTotalRecall-18 TOOL-dTotalRecall-19 TOOL-dTotalRecall-21 TOOL-dTotalRecall-23 TOOL-dTotalRecall-26 |
| [2026-10-26-build-TOOL-dTotalRecall-1-spec-stage-returns.md](../build/2026-10-26-build-TOOL-dTotalRecall-1-spec-stage-returns.md) | research | TOOL-dTotalRecall-1 TOOL-dTotalRecall-3 TOOL-dTotalRecall-4 TOOL-dTotalRecall-5 TOOL-dTotalRecall-6 TOOL-dTotalRecall-7 TOOL-dTotalRecall-8 TOOL-dTotalRecall-9 TOOL-dTotalRecall-10 TOOL-dTotalRecall-11 TOOL-dTotalRecall-12 TOOL-dTotalRecall-13 TOOL-dTotalRecall-14 TOOL-dTotalRecall-15 TOOL-dTotalRecall-16 TOOL-dTotalRecall-17 TOOL-dTotalRecall-18 TOOL-dTotalRecall-19 TOOL-dTotalRecall-20 TOOL-dTotalRecall-21 TOOL-dTotalRecall-22 TOOL-dTotalRecall-23 TOOL-dTotalRecall-24 TOOL-dTotalRecall-25 TOOL-dTotalRecall-26 |
| [2026-10-26-build-TOOL-dTotalRecall-2-deviation-21.md](../build/2026-10-26-build-TOOL-dTotalRecall-2-deviation-21.md) | deviation | — |
| [2026-10-26-build-TOOL-dTotalRecall-36-round1-fix-return.md](../build/2026-10-26-build-TOOL-dTotalRecall-36-round1-fix-return.md) | research | TOOL-dTotalRecall-36 TOOL-dTotalRecall-8 TOOL-dTotalRecall-23 TOOL-dTotalRecall-37 TOOL-dTotalRecall-38 TOOL-dTotalRecall-39 TOOL-dTotalRecall-40 TOOL-dTotalRecall-41 TOOL-dTotalRecall-42 TOOL-dTotalRecall-43 |
| [2026-10-26-prompt-TOOL-dTotalRecall-1-spec-brief.md](../prompts/2026-10-26-prompt-TOOL-dTotalRecall-1-spec-brief.md) | research | TOOL-dTotalRecall-1 TOOL-dTotalRecall-3 TOOL-dTotalRecall-4 TOOL-dTotalRecall-5 TOOL-dTotalRecall-6 TOOL-dTotalRecall-7 TOOL-dTotalRecall-8 TOOL-dTotalRecall-9 TOOL-dTotalRecall-10 TOOL-dTotalRecall-11 TOOL-dTotalRecall-12 TOOL-dTotalRecall-13 TOOL-dTotalRecall-14 TOOL-dTotalRecall-15 TOOL-dTotalRecall-16 TOOL-dTotalRecall-17 TOOL-dTotalRecall-18 TOOL-dTotalRecall-19 TOOL-dTotalRecall-20 TOOL-dTotalRecall-21 TOOL-dTotalRecall-22 TOOL-dTotalRecall-23 TOOL-dTotalRecall-24 TOOL-dTotalRecall-25 TOOL-dTotalRecall-26 |
| [2026-10-26-prompt-TOOL-dTotalRecall-1-spec-fix-brief.md](../prompts/2026-10-26-prompt-TOOL-dTotalRecall-1-spec-fix-brief.md) | research | TOOL-dTotalRecall-1 TOOL-dTotalRecall-4 TOOL-dTotalRecall-5 TOOL-dTotalRecall-6 TOOL-dTotalRecall-7 TOOL-dTotalRecall-8 TOOL-dTotalRecall-9 TOOL-dTotalRecall-14 TOOL-dTotalRecall-18 TOOL-dTotalRecall-19 TOOL-dTotalRecall-21 TOOL-dTotalRecall-23 TOOL-dTotalRecall-26 |
| [2026-10-26-prompt-TOOL-dTotalRecall-36-round1-fix-brief.md](../prompts/2026-10-26-prompt-TOOL-dTotalRecall-36-round1-fix-brief.md) | research | TOOL-dTotalRecall-8 TOOL-dTotalRecall-23 TOOL-dTotalRecall-36 TOOL-dTotalRecall-37 TOOL-dTotalRecall-38 TOOL-dTotalRecall-39 TOOL-dTotalRecall-40 TOOL-dTotalRecall-41 TOOL-dTotalRecall-42 TOOL-dTotalRecall-43 |
| [2026-10-26-review-TOOL-dTotalRecall-1-spec-audit-round1.md](../reviews/2026-10-26-review-TOOL-dTotalRecall-1-spec-audit-round1.md) | spec-audit | TOOL-dTotalRecall-1 TOOL-dTotalRecall-13 TOOL-dTotalRecall-8 TOOL-dTotalRecall-18 TOOL-dTotalRecall-16 TOOL-dTotalRecall-25 TOOL-dTotalRecall-5 TOOL-dTotalRecall-4 TOOL-dTotalRecall-6 TOOL-dTotalRecall-22 TOOL-dTotalRecall-3 TOOL-dTotalRecall-7 TOOL-dTotalRecall-11 TOOL-dTotalRecall-10 TOOL-dTotalRecall-19 TOOL-dTotalRecall-21 TOOL-dTotalRecall-9 TOOL-dTotalRecall-23 TOOL-dTotalRecall-24 TOOL-dTotalRecall-20 TOOL-dTotalRecall-17 TOOL-dTotalRecall-14 TOOL-dTotalRecall-15 TOOL-dTotalRecall-26 TOOL-dTotalRecall-12 |

<!-- /gen:spec-records -->

## 1. Goal

One write command, `record`, standing as `python gov_record.py new <kind>` the way `gov_tag.py` stands
in for `gov tag`, is the door of every record kind the registry names it the writer of: it mints the
record's id under the build's claim or lease, is idempotent and content-addressed, renders the kind's
template from its schema, and refuses an invalid value at the write boundary (`layer-memory.md:316-346`,
P30). Today three scaffolds write records (`gen_build_index.py --new-build` and `--new-spec`, runlog's
`write_record`), none generic, nothing mints a `<seq>`, and nothing makes a replayed write a no-op.

## 2. Scope (IN)

- **S1** — The CLI `tools/memory-tree/gov_record.py`, verb `new <kind>` with `--build <slug>`,
  `--unit <id>`, `--title <text>` and repeated `--field <Name>=<value>`, a thin adapter over one function,
  `write_new_record(root, kind, build, unit, fields)`, in PLAY-dOrderedCharter-7 S7's factory
  `tools/memory-tree/build_records.py`. The factory's own stand-in verb `build_records.py new <kind>`
  (PLAY-dOrderedCharter-7 S8) calls the same function, so there is one door and no third writer. The
  verbs `find` and `show` are TOOL-dTotalRecall-9's. Observed by AC1.
- **S2** — The kind's row: the door reads `<kind>`'s `[[record-kind]]` row from
  `tools/memory-tree/record-kinds.toml` (I1) and refuses, exit 2, a kind with no row and a kind whose
  `writer` names another door, naming that door, since each kind has one door and the registry names
  it. Observed by AC1.
- **S3** — Rendering: the record's text is TOOL-dTotalRecall-1's generated template for the row,
  `render_template` (the `record_kinds.py --template <kind>` skeleton: the `**Serves:** <kind> <ids>`
  line and one `- **<Key>:** ` line per field in the row's order), each field line filled with the
  caller's value, under an H1 the caller's `--title` gives. A row whose `schema.form` is not `fields`
  is written only by a kind verb of S7. Observed by AC8.
- **S4** — Refusal at the write boundary: the rendered bytes are parsed back, before anything is
  written, by the predicates that grade the kind: TOOL-dTotalRecall-1's generated field check for a
  `fields` row (its S4), and for a factory kind the factory's `read_record` refusals
  (`tools/memory-tree/deviation_join.py:212`, moved by PLAY-dOrderedCharter-7 S7). Any finding exits 2
  naming the field and the reason, and nothing is written. The door adds no validator of its own.
  Observed by AC2.
- **S5** — Content-addressed and idempotent: `derive_content_key(kind, fields)`, the shape of
  `derive_section_sha` (`tools/roles/handoff.py:307`: the first 12 hex digits of the SHA-256 of the
  LF-folded text), over the kind name and the field values in schema order. A record of the kind whose
  re-derived key matches is the same write: the door prints `exists <path>` and exits 0. A different
  value under an existing id is refused, naming the record. Observed by AC3 and AC4.
- **S6** — Minting under the build's claim or lease, by the row's `id-rule`, per §4 "Minting".
  Observed by AC5 and AC6.
- **S7** — The two existing scaffolds become kinds of the door: `new build-readme <slug> --asks <IDLIST>`
  runs `cmd_new_build`'s path (`gen_build_index.py:4050`) and `new spec <id> --tier 1|2 [--order <n>]
  [--base <sha>]` runs `cmd_new_spec`'s (`:8586`), each imported, never copied. Each takes every flag
  `--new-build` and `--new-spec` take today (`NEW_BUILD_USAGE` at `:3887`, `NEW_SPEC_USAGE` at
  `:8488`), parsed by their own `read_new_build_args` and `read_new_spec_args`, so a forward passes
  them through unchanged. The `writer` cells of the
  `build-readme` and `spec` rows become `gov_record.py new build-readme` and `gov_record.py new spec`.
  Forwarding `--new-build` and `--new-spec` to the door is TOOL-dTotalRecall-20's. Observed by AC7.
- **S9** — Each registry row whose `writer` is `hand` and whose `schema.form` is `fields` (unit 1's
  `journal`, `research`, `deviation` and `design-record` rows, and any other the pass finds) takes
  `writer = "gov_record.py new <kind>"`, since the door now writes it; a `hand` row of another form
  keeps `hand`, and the pass commit's `Decided:` trailer names the unit or kit owning its door
  (`backlog-row`: TOOL-dTotalRecall-7's ask door; `dossier`: the codebase-map kit). Observed by AC9.
- **S8** — The written file is staged with `git add`, as `cmd_new_build` stages its README; the door
  commits nothing, and prints `wrote <path>` with the content key. Observed by AC3.

## 3. Non-goals (OUT)

- The header lines `**Made-by:**` and `**Caused-by:**` and the section `**Edges:**` lines, and the
  causes and orphan checks: TOOL-dTotalRecall-19's, written through this door.
- The ask kind's acceptance at filing: TOOL-dTotalRecall-7's; the shape-run kind: TOOL-dTotalRecall-11's.
- Appending a landed record write to the change feed: TOOL-dTotalRecall-24's.
- The claim and counter refs and their writer: TOOL-dTotalRecall-3's; the slug grammar:
  TOOL-dTotalRecall-5's; the README schema: TOOL-dTotalRecall-4's.
- runlog's run record: its door is runlog's own `write_record` (`tools/runlog/record.py:1179`), in a
  kit that does not require memory-tree, and the registry names that door, so `new run` refuses
  naming it (S2).
- Editing or versioning a record in place: `new` writes a new record or replays one; a kind whose
  lifecycle is current-state is edited by its own verb.
- Generated kinds (a view, the index, symbols): written by their generators, which the registry names.

### Edges

- **consumes-from** `TOOL-dTotalRecall-1` — `record-kinds.toml` and `--template`, the rows naming each
  kind's schema, id rule, writer and check, and the template the door fills
- **consumes-from** `TOOL-dTotalRecall-5` — `slug_grammar`, whose `mint_re` and `record` the
  `build-readme` kind writes against
- **consumes-from** `TOOL-dTotalRecall-4` — `FRONT_MATTER_KEYS`, which the `build-readme` kind's front
  matter is validated against
- **consumes-from** `TOOL-dTotalRecall-3` — `refs/gov/claims/`, the slug claim and the ask-family
  counter the door mints under through `gov-claim.sh`
- **hands-off** `TOOL-dTotalRecall-9` — `gov_record.py`, the door CLI that gains the `find` and `show`
  verbs
- **hands-off** `TOOL-dTotalRecall-7` — `gov_record.py`, whose `new ask` refuses an ask without its
  acceptance under `asks.acceptance`
- **hands-off** `TOOL-dTotalRecall-11` — `gov_record.py`, through which the shape-run kind's records
  are written
- **hands-off** `TOOL-dTotalRecall-19` — `gov_record.py`, which gains the header lines and the
  section edge lines, spelled `**Edges:** type=target[,target]` one per type, and the missing-cause
  refusal
- **hands-off** `TOOL-dTotalRecall-24` — `gov_record.py`, whose writes, once landed, unit 24's lander
  hook appends to the change feed through `add_feed_event`; the door appends nothing itself
- **hands-off** `TOOL-dTotalRecall-20` — `gov_record.py`, to which the `--new-build` and `--new-spec`
  shims forward, every flag passed through unchanged
- **consumes-from** `TOOL-dTotalRecall-8` — `policy_value.py`, the memory-tree kit's `read_policy_value`
  adapter the door reads `leases.offline` through
- **consumes-from** external — PLAY-dOrderedCharter-7 S7/S8's `tools/memory-tree/build_records.py`,
  its renderer, `read_record` and `new` verb; TOOL-dPlacedRequest-1's build lease
  `refs/gov/leases/<slug>/build` and its `--claims` reader
- **hands-off** `TOOL-dTotalRecall-43` — `gov_record.py`, its writer refusal, its hand-row rewrite, its value refusal and its mint, which that unit changes for the round-1 audit's ids 5, 8, 9, 50 and 60

## 4. Design

### The command

```
python gov_record.py new <kind> [--build <slug>] [--unit <id>] [--title <text>] [--field <Name>=<value>]...
python gov_record.py new build-readme <slug> --asks <IDLIST>
python gov_record.py new spec <id> --tier 1|2 [--order <n>] [--base <sha>]
```

| Exit | stdout | Meaning |
|---|---|---|
| 0 | `wrote <path> key <content key>` | written and staged |
| 0 | `exists <path> key <content key>` | the same write, a no-op |
| 2 | `refused <kind>: <why>` | no row, another door, an invalid value, a different value under an existing id, or no authority to mint |

A `--field` value is taken verbatim; the door never reads a value from the environment or a file the
caller did not name.

A kind whose input is not a field list takes a handler of its own inside `gov_record.py`, keyed by
the kind name in one table `KIND_HANDLERS`, with its own flags, and every handler ends in
`write_new_record`'s mint, idempotence and refusal path. This unit adds two, `build-readme` and
`spec`; later units add theirs (TOOL-dTotalRecall-7's `ask`, TOOL-dTotalRecall-11's `shape-run`).

### Minting

The row's `id-rule` is the record's name grammar (TOOL-dTotalRecall-1's data model), and the door
mints each placeholder it holds; a grammar holding none names a given id.

| Placeholder | Minted as | Authority checked first |
|---|---|---|
| `<n>` | the next free `<n>` in the home folder, the factory's collision rule | the build's lease or claim |
| `<seq>` of an ask id | `gov-claim.sh ask <FAMILY> <slug> --claimant <content key>` | the counter ref itself |
| `<slug>` of a build | `gov-claim.sh slug <slug> --claimant <content key>`, after `mint_re` | the slug claim itself |
| `<date>` | today, as an ISO date | none |
| `<unit id>` | the caller's `--unit`, an id the tree defines | none |
| none (a given id, such as a spec's) | the caller's id, minted by its session | the build's lease or claim |

The build's authority, in order: the lease `refs/gov/leases/<slug>/build` held by this session, read
through `unattended.sh --claims` (TOOL-dPlacedRequest-1); else the slug claim `refs/gov/claims/<slug>`
whose `claimant:` is this session's; a lease or claim held by another refuses, naming the holder. A
build with neither, every build opened before TOOL-dTotalRecall-3, mints under the charter's
per-session rule and prints `minted under the session rule: no claim or lease for <slug>`. The
offline value passed to `gov-claim.sh` is `read_policy_value("leases.offline", root)` (I8), through
memory-tree's adapter `tools/memory-tree/policy_value.py`, which TOOL-dTotalRecall-8 creates (its S10)
and this unit reads.

The content key is the claimant a counter or slug mint passes, so a replayed `new` returns the id the
first call minted (TOOL-dTotalRecall-3 S4).

### Idempotence

Before minting, the door lists the kind's home (tracked and staged files matching the row's `home`),
parses each with the kind's check, and re-derives its content key. An equal key is `exists`; a record
holding the requested `given` id with a different key is a refusal; otherwise the door mints. The key
is derived from the record's fields, never stored in it, so it is one fact in one place.

### Inventory

Minted: `tools/memory-tree/gov_record.py` with the verb `new`, its flag `--title` and the table
`KIND_HANDLERS`;
`write_new_record`, `derive_content_key` and `check_mint_authority` in `build_records.py`. Naming cells: the three functions are asked of the lexicon's
`--suggest` under `--as py.function` at the pass. The module is never named `record.py`, which would
collide with `tools/runlog/record.py`.

### Migration

None. Every record already written keeps its form; the door writes new ones. The rows of kinds the
door writes at this pass are read from the registry and named in the pass commit's `Decided:` trailer.

### Files touched (estimate)

- `tools/memory-tree/gov_record.py` (new)
- `tools/memory-tree/build_records.py`
- `tools/memory-tree/record-kinds.toml` (the `writer` cells of `build-readme` and `spec`)
- `tools/memory-tree/kit.toml` (the new file in the kit's `[[files]]`)
- `tools/memory-tree/README.md` (the door's usage)

### Alternatives rejected

- **A new module beside the factory.** The factory is the record writer's second instance; a third
  writer is a copy (scout A, Shared 2).
- **Validate values with a schema validator of the door's own.** The kind's check already refuses a
  bad record; a second validator can disagree with it. Round-tripping through the check makes the
  write boundary and the gate one predicate.
- **Store the content key in the record.** A stored key is typed beside the fields it describes and
  can go stale under a hand edit; the door re-derives it.
- **Import `derive_section_sha` from the roles kit.** memory-tree requires no kit; the door uses the
  same formula over its own input, named `derive_content_key`.

## 5. Production-readiness checklist

- security — the door is the write boundary for authored record structure: every value is checked by
  the kind's own check before a byte is written, a kind's door is enforced from the registry, minting
  checks the build's lease or claim and refuses another holder, and the door commits nothing.
- perf / scale — one listing of the kind's home per call; a build's `build/` folder holds at most a
  few hundred records.
- error / empty / loading states — every refusal names the kind and the cause, and writes nothing; a
  missing registry refuses naming `record-kinds.toml`.
- observability — every call prints the path and the content key.
- risks — a legacy build mints under the session rule, which is today's rule; the named line says so.
- testing — AC1 to AC9 by a pass; the arms of §7 at the close.
- migration — none, as §4 says.
- user docs — the kit README names the door; no page under `help/` describes record writing.

## 6. Acceptance criteria

- **AC1** — When `python gov_record.py new nosuch` runs in a scratch clone, it exits 2 naming
  `record-kinds.toml`; when the clone's registry row for a planted kind `planted` names
  `writer = "runlog"`, `gov_record.py new planted` exits 2 naming `runlog`.
  Red when: an unregistered kind, or a kind with another door, is written.
- **AC2** — When `gov_record.py new deviation --build dTotalRecall --unit TOOL-dTotalRecall-2` runs
  in a scratch clone with `--field Risk=bogus` and the other required fields, it exits 2 naming `Risk`,
  and `git status --porcelain` is empty.
  Red when: the value reaches disk, or a validator other than the kind's check decides.
- **AC3** — When the same complete `gov_record.py new deviation` call runs twice in a scratch clone,
  the first prints `wrote` and stages one file, and the second prints `exists` with the same path and
  key, and the clone holds one new file.
  Red when: a replay writes a second record.
- **AC4** — When the call runs a third time with one field changed, it writes a second record whose
  `<n>` is one higher; and when `gov_record.py new spec TOOL-dTotalRecall-2` runs at the pass tip, it
  exits 2 naming the existing spec.
  Red when: a different value overwrites a record, or an existing id is re-written.
- **AC5** — When a fixture clone holds a local lease ref `refs/gov/leases/xA/build` held by another
  session, `gov_record.py new deviation --build xA …` exits 2 naming the holder; with the claim ref
  `refs/gov/claims/xA` carrying this session's claimant it writes; with neither it writes and prints
  `minted under the session rule`.
  Red when: the door mints without reading the build's authority.
- **AC6** — When a fixture registry row `planted-ask` whose `id-rule` is `<FAMILY>-<slug>-<seq>` is written
  twice with equal fields through `gov_record.py new` against a bare fixture remote under
  `%TEMP%/<short>`, both calls print the same id and the counter ref's tip moves once.
  Red when: the content key is not passed as the claimant, so a replay mints twice.
- **AC7** — When `gov_record.py new spec TOOL-xNew-1` runs in a fixture clone holding build `xNew`, the
  written file is byte-equal to what `gen_build_index.py --new-spec TOOL-xNew-1` writes in a twin
  clone; and `gov_record.py new build-readme dLoop --asks <IDLIST>` against a fixture remote writes the
  README with its `slug-grammar:` line and creates `refs/gov/claims/dLoop`.
  Red when: the door copies a scaffold instead of calling it, or skips the claim.
- **AC8** — When a probe reads the record AC3 wrote back with the factory's `read_record`, it reports
  no finding and the record's first binding line is `**Serves:** deviation TOOL-dTotalRecall-2`.
  Red when: the template the door renders fails its own kind's check.
- **AC9** — When a probe reads `record-kinds.toml` with `tomllib` at the pass tip, no row whose
  `schema.form` is `fields` has `writer = "hand"`, and the `deviation` row's writer is
  `gov_record.py new deviation`.
  Red when: a kind the door can write is still registered as hand-written.

## 7. Gates

`memory hygiene` · `build-index selftest` · `verdict epoch (kit version dates the engine)` · `verdict-epoch self-test` · `routed-commits selftest`

New arm: tools/memory-tree/build_records.py · covers AC1 AC2 AC3 AC4 AC5 AC6 AC8 AC9 · its self-test gains the door's refusals, the replay, the changed-field record, the authority ladder and the counter replay, staged by dropping the key comparison · none
New arm: tools/memory-tree/gen_build_index.py · covers AC7 · its `--selftest` gains the byte-equality of the two spec writers, staged by a copied skeleton in the door · none

## 8. Open questions

- **F1 — Is `record` a new module or the factory grown?** Options: (a) `gov_record.py` as a thin CLI
  over a function in PLAY-dOrderedCharter-7 S7's `build_records.py`, its `new` verb calling the same
  function; (b) a new writer module. (b) is a third writer. RESOLVED (agent, 2026-10-26, delegated):
  (a), rung 1, the layer's "It extends the writers that exist" (`layer-memory.md:343-346`) and the
  brief's I2. widens: none · relaxes: none
- **F2 — What validates a value?** Options: (a) the kind's own check over the rendered bytes; (b) a
  schema validator in the door. (b) can disagree with the check that grades the same record later.
  RESOLVED (agent, 2026-10-26, delegated): (a), rung 3, the most feature-rich: one predicate at write
  and at the gate. widens: none · relaxes: none
- **F3 — A build opened before claims exist has no claim and no lease.** Options: (a) mint under the
  per-session rule with a named line; (b) refuse. (b) makes the door unusable for every build in the
  tree today, this one included. RESOLVED (agent, 2026-10-26, delegated): (a), rung 3; the per-session
  rule is the charter's `[ids]` rule these builds were minted under; the departure from the clause's
  "under the build's claim or lease" is recorded beside this spec as deviation 21
  (`2026-10-26-build-TOOL-dTotalRecall-2-deviation-21.md`). widens: none · relaxes: none
- **F4 — Does the door write runlog's run record?** Options: (a) no: the registry names runlog's
  `write_record` as that kind's door, and `new run` refuses naming it; (b) yes, by importing runlog.
  (b) makes memory-tree depend on a kit it does not require. RESOLVED (agent, 2026-10-26, delegated):
  (a), rung 1, the layer's "Each kind has one door, and the registry names it" (`layer-memory.md:348`).
  widens: none · relaxes: none
- **F5 — The parents are specced and not built.** PLAY-dOrderedCharter-7's factory and the lease
  reader are DEFERRED at `462d20f3`. RESOLVED (agent, 2026-10-26, delegated): this spec calls them as
  their specs name them, and the build run re-grounds on the landed code, rung 1 (the brief's chain
  rule). widens: none · relaxes: none

## 9. Revision log

- rev-1 · 2026-10-26 · initial draft, from the packet's Items 2, the brief's shared interfaces I1 to
  I4 and I8, scout A's row for cl-0213, and the scaffolds read at `fb872a37e`.
- rev-2 · 2026-10-26 · §3 · the Edges block gains the hands-off bullets mirroring the consumes-from
  edges of TOOL-dTotalRecall-43, written by the round-1 spec audit's disposal; nothing else moved. The Carries pin re-pinned from `09982ca6` to `bfd195a1`, the hash the as-built view gives cl-dClosedLoop-0213 once deviation 21 states its whole clause as After.

## 10. Reuse audit

The seam extended is PLAY-dOrderedCharter-7 S7's record factory `tools/memory-tree/build_records.py`,
itself extracted from `tools/memory-tree/deviation_join.py` (`FIELD` and `REQUIRED` at `:145-147`,
`read_record` at `:212`), with the two scaffolds `cmd_new_build` and `cmd_new_spec`
(`tools/memory-tree/gen_build_index.py:4050`, `:8586`) called as kinds and the content-key formula of
`derive_section_sha` (`tools/roles/handoff.py:307`). The lookup,
`python tools/codebase-map/reuse_lookup.py "write a typed record from a schema idempotently and refuse invalid field values"`,
listed `write_record`, `render_record` and `check_records` (`tools/runlog/record.py:1179`, `:1154`)
and `read_records` (`deviation_join.py`); runlog's writer stays its own kind's door (§8 F4). The recall
probe returned scout A's row, the layer's `[contract]` and the brief's I2; scout A's lines held at
`fb872a37e`.

Recall terms used: `python tools/memory-recall/query.py "which command writes typed memory records idempotently from a schema" --terms "record door build_records new kind content key derive_section_sha idempotent template schema refuse mint"`
