# TOOL-dLinkedLibrary-8 — retrofit's record kinds, the `origin` field, and the `adopt` program the core's own command runs

**Status:** OPEN · rev-2 · 2026-10-26 · node d · Tier-2 · base 5fede642 · streams tooling · order 20 · advances TOOL-dLinkedLibrary-26

**Carries:** cl-dClosedLoop-0245@2d7af537 whole
**Carries:** node:record-kind.baseline
**Carries:** node:record-kind.census
**Carries:** node:record-kind.ruling
**Carries:** node:policy-key.retrofit.decisions
**Carries:** node:policy-key.retrofit.practice-pending
**Carries:** node:policy-key.retrofit.reconstruct
**Carries:** node:item.adopt.census
**Carries:** node:item.adopt.practices
**Carries:** node:item.adopt.decisions
**Carries:** node:item.adopt.decisions-ratify
**Carries:** node:item.adopt.reconstruct

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-26-build-TOOL-dLinkedLibrary-1-agent-ledger.md](../build/2026-10-26-build-TOOL-dLinkedLibrary-1-agent-ledger.md) | journal | TOOL-dLinkedLibrary-1 TOOL-dLinkedLibrary-2 TOOL-dLinkedLibrary-3 TOOL-dLinkedLibrary-4 TOOL-dLinkedLibrary-5 TOOL-dLinkedLibrary-6 TOOL-dLinkedLibrary-7 TOOL-dLinkedLibrary-9 TOOL-dLinkedLibrary-10 TOOL-dLinkedLibrary-11 TOOL-dLinkedLibrary-12 TOOL-dLinkedLibrary-13 TOOL-dLinkedLibrary-14 TOOL-dLinkedLibrary-15 TOOL-dLinkedLibrary-16 TOOL-dLinkedLibrary-17 TOOL-dLinkedLibrary-18 TOOL-dLinkedLibrary-19 TOOL-dLinkedLibrary-20 TOOL-dLinkedLibrary-21 TOOL-dLinkedLibrary-22 TOOL-dLinkedLibrary-23 TOOL-dLinkedLibrary-24 TOOL-dLinkedLibrary-25 TOOL-dLinkedLibrary-37 TOOL-dLinkedLibrary-38 TOOL-dLinkedLibrary-39 TOOL-dLinkedLibrary-40 TOOL-dLinkedLibrary-41 TOOL-dLinkedLibrary-42 TOOL-dLinkedLibrary-43 TOOL-dLinkedLibrary-44 TOOL-dLinkedLibrary-45 TOOL-dLinkedLibrary-46 TOOL-dLinkedLibrary-47 TOOL-dLinkedLibrary-48 TOOL-dLinkedLibrary-49 TOOL-dLinkedLibrary-50 TOOL-dLinkedLibrary-51 TOOL-dLinkedLibrary-52 TOOL-dLinkedLibrary-53 TOOL-dLinkedLibrary-54 TOOL-dLinkedLibrary-55 TOOL-dLinkedLibrary-56 TOOL-dLinkedLibrary-57 TOOL-dLinkedLibrary-58 TOOL-dLinkedLibrary-59 TOOL-dLinkedLibrary-60 TOOL-dLinkedLibrary-61 TOOL-dLinkedLibrary-62 TOOL-dLinkedLibrary-63 TOOL-dLinkedLibrary-64 TOOL-dLinkedLibrary-65 TOOL-dLinkedLibrary-66 TOOL-dLinkedLibrary-67 TOOL-dLinkedLibrary-68 TOOL-dLinkedLibrary-69 TOOL-dLinkedLibrary-70 TOOL-dLinkedLibrary-71 TOOL-dLinkedLibrary-72 TOOL-dLinkedLibrary-73 TOOL-dLinkedLibrary-74 TOOL-dLinkedLibrary-75 TOOL-dLinkedLibrary-76 TOOL-dLinkedLibrary-77 TOOL-dLinkedLibrary-78 TOOL-dLinkedLibrary-79 TOOL-dLinkedLibrary-80 |
| [2026-10-26-build-TOOL-dLinkedLibrary-1-reuse-scout-d.md](../build/2026-10-26-build-TOOL-dLinkedLibrary-1-reuse-scout-d.md) | research | TOOL-dLinkedLibrary-9 TOOL-dLinkedLibrary-10 TOOL-dLinkedLibrary-23 TOOL-dLinkedLibrary-1 |
| [2026-10-26-build-TOOL-dLinkedLibrary-1-spec-stage-returns.md](../build/2026-10-26-build-TOOL-dLinkedLibrary-1-spec-stage-returns.md) | research | TOOL-dLinkedLibrary-1 TOOL-dLinkedLibrary-2 TOOL-dLinkedLibrary-3 TOOL-dLinkedLibrary-4 TOOL-dLinkedLibrary-5 TOOL-dLinkedLibrary-6 TOOL-dLinkedLibrary-7 TOOL-dLinkedLibrary-9 TOOL-dLinkedLibrary-10 TOOL-dLinkedLibrary-11 TOOL-dLinkedLibrary-12 TOOL-dLinkedLibrary-13 TOOL-dLinkedLibrary-14 TOOL-dLinkedLibrary-15 TOOL-dLinkedLibrary-16 TOOL-dLinkedLibrary-17 TOOL-dLinkedLibrary-18 TOOL-dLinkedLibrary-19 TOOL-dLinkedLibrary-20 TOOL-dLinkedLibrary-21 TOOL-dLinkedLibrary-22 TOOL-dLinkedLibrary-23 TOOL-dLinkedLibrary-24 TOOL-dLinkedLibrary-25 |
| [2026-10-26-prompt-TOOL-dLinkedLibrary-1-spec-brief.md](../prompts/2026-10-26-prompt-TOOL-dLinkedLibrary-1-spec-brief.md) | research | TOOL-dLinkedLibrary-1 TOOL-dLinkedLibrary-2 TOOL-dLinkedLibrary-3 TOOL-dLinkedLibrary-4 TOOL-dLinkedLibrary-5 TOOL-dLinkedLibrary-6 TOOL-dLinkedLibrary-7 TOOL-dLinkedLibrary-9 TOOL-dLinkedLibrary-10 TOOL-dLinkedLibrary-11 TOOL-dLinkedLibrary-12 TOOL-dLinkedLibrary-13 TOOL-dLinkedLibrary-14 TOOL-dLinkedLibrary-15 TOOL-dLinkedLibrary-16 TOOL-dLinkedLibrary-17 TOOL-dLinkedLibrary-18 TOOL-dLinkedLibrary-19 TOOL-dLinkedLibrary-20 TOOL-dLinkedLibrary-21 TOOL-dLinkedLibrary-22 TOOL-dLinkedLibrary-23 TOOL-dLinkedLibrary-24 TOOL-dLinkedLibrary-25 |
| [2026-10-26-review-TOOL-dLinkedLibrary-1-spec-audit.md](../reviews/2026-10-26-review-TOOL-dLinkedLibrary-1-spec-audit.md) | spec-audit | TOOL-dLinkedLibrary-1 TOOL-dLinkedLibrary-10 TOOL-dLinkedLibrary-11 TOOL-dLinkedLibrary-12 TOOL-dLinkedLibrary-13 TOOL-dLinkedLibrary-14 TOOL-dLinkedLibrary-15 TOOL-dLinkedLibrary-16 TOOL-dLinkedLibrary-17 TOOL-dLinkedLibrary-18 TOOL-dLinkedLibrary-19 TOOL-dLinkedLibrary-2 TOOL-dLinkedLibrary-20 TOOL-dLinkedLibrary-21 TOOL-dLinkedLibrary-22 TOOL-dLinkedLibrary-23 TOOL-dLinkedLibrary-24 TOOL-dLinkedLibrary-25 TOOL-dLinkedLibrary-3 TOOL-dLinkedLibrary-4 TOOL-dLinkedLibrary-5 TOOL-dLinkedLibrary-6 TOOL-dLinkedLibrary-7 TOOL-dLinkedLibrary-9 |

<!-- /gen:spec-records -->

## 1. Goal

Nothing takes a census of a repository's own practices (gap-mem-24), and records carry no origin,
so a reconstructed record reads as written (gap-mem-25). This unit lands retrofit's `baseline` and
`census` record kinds with the `ruling` kind the owner's practice rulings need, the `origin` field
the record door derives on every record it writes, and the `adopt` program the core's own command
runs where distribution is absent: `adopt.census`; `adopt.practices`, the owner's one ruling per
practice through `retrofit.practice-pending`; `adopt.decisions`, two raters by the author's rubric
through `retrofit.decisions`, a candidate the raters split on kept `reconstructed` and not major and
ratified by the owner only under `docs-owner-ratifies` or `docs-and-trailers` (the owner's FK-4-6);
and `adopt.reconstruct`, which `retrofit.reconstruct` governs. A decision the owner declines is kept
`rejected`.

## 2. Scope (IN)

Build-run preconditions this unit calls and does not build, each specced and DEFERRED at base
`5fede642`: the kind registry and its factory `record_kinds.py new` (TOOL-dTotalRecall-1 S1, S3, S9)
with the `home`, `lifecycle`, `readers` and `layer` columns (TOOL-dTotalRecall-18 S1); the record
door `gov_record.py new <kind>` over `write_new_record` in `tools/memory-tree/build_records.py`
(TOOL-dTotalRecall-2 S1 to S6, PLAY-dOrderedCharter-7 S7); `tools/playbook/core.py` and its owner
proof (PLAY-dOrderedCharter-7 S6, S9; PLAY-dOrderedCharter-15); the item schema in
`tools/loop/loop.toml` and `check_program` (TOOL-dDeclaredLoop-12 S1, S3); the ledger factory and
`test.seed` (TOOL-dWitnessedBar-13 S1, S2, S10; TOOL-dWitnessedBar-15 S1); the one trailer reader
`commit_trailers.decided(commit)` (TOOL-dDeclaredLoop-23 S3); and TOOL-dLinkedLibrary-1's rubric
module `tools/memory-tree/decision_rubric.py` with `CLASSES`, `RUBRIC`, its labels-file form and
`derive_kappa` (its S5). dGroundRules' `resolve` (`tools/policy/policy.py:752`) is landed.

- **S1** — The kinds, each a `[[record-kind]]` row of `tools/memory-tree/record-kinds.toml` written
  by `record_kinds.py new` (shared interface I3, node `record-kind.<name>`, tag `record.<name>`):
  `census` and `ruling`, form `fields`, writer `gov_record.py new <kind>`, check `memory hygiene`,
  their fields §4 "The kinds" lists; and `baseline`, form `rows`, writer `legacy_ledger.py seed`
  (`test.seed`), whose `home` and `check` are the sentinel `ledger`: each `[[ledger]]`
  registration's own `home` and `leg`, read by `read_registrations`. `check_record_kinds` admits the
  sentinel and grades it as it grades a literal, every registered `home` tracked or recorded
  unarmed and every registered `leg` a leg of `tools/gate-legs.json`. Observed by AC9.
- **S2** — The `origin` field (shared interface I20): every record the door writes carries one
  `- **Origin:** <value>` line after its `**Serves:**` line, its value `written`,
  `reconstructed@<sha8> <sources>` or `imported:<path>`, derived by the door and never typed. The door
  writes `written` unless its caller passes `--reconstructed-from <sha> --source <path>…`, from which
  it derives `reconstructed@<sha8> <sources>` after checking that the sha resolves and each source
  exists at it, or `--imported-from <path>`, which it derives as `imported:<path>` after checking the
  path is tracked and outside the memory root. A `--field Origin=<value>` is refused, exit 2.
  `write_new_record` takes the same two arguments by keyword. Observed by AC8.
- **S3** — The program, `python tools/playbook/core.py adopt <verb> --build <slug> --unit <id>`
  (shared interface I21), `<verb>` one of `census`, `practices`, `decisions` and `reconstruct`, with
  `instructions` reserved for TOOL-dLinkedLibrary-23. `core.py` dispatches each of these four verbs as
  a subprocess to `tools/memory-tree/adopt_program.py`, found by `resolve_kit_dir("memory-tree",
  "adopt_program.py", here)`, so no kit imports a sibling. `--build` and `--unit` name the build the
  owner opened for the adoption and its unit, under whose claim the door mints every record; without
  them the program refuses. Never `govkit adopt`, which writes the install receipt
  (`tools/govkit/govkit.py:12611`). Observed by AC1.
- **S4** — `adopt census`: a read-only scan of the tree at HEAD by `scan_practices(root, sha)` over
  the classes of §4 "The census", each CI job its own practice and a job whose steps deploy, publish
  or push marked `refused`. It writes one `census` record per practice, ranked by instances, largest
  first; the heat ranking of keys times reads is dTendedCadence's, and the census prints
  `heat — not installed` until it lands. A re-run at the same SHA writes nothing new. Observed by AC1.
- **S5** — `adopt practices`: with no flag, it prints each practice no `ruling` names, in rank
  order, with the four practice rulings of §4 "The kinds" and the recommendation and unruled reading
  `retrofit.practice-pending` gives, per §4 "The pending practice". `--rule <census record> <ruling>
  --reason <text>` writes one `ruling` record through the door's owner path, under
  PLAY-dOrderedCharter-15's owner proof; it refuses a second ruling for one practice, an `import` of
  a `refused` CI job, and a caller that is not the owner. Observed by AC2.
- **S6** — `adopt decisions`: `--candidates` prints one `<candidate id> TAB <text>` line per candidate,
  the shape `decision_rubric.py rows` prints, with `RUBRIC` and `CLASSES`, for two raters; the
  candidates are the `decision-doc` practices' documents, one per document section headed as a
  decision, and, under `docs-and-trailers` only, each `Decided:` value
  `commit_trailers.decided(commit)` returns; a candidate id is the first 8 hex digits of the SHA-1 of
  its source and anchor, and a source a `declined` ruling names is never a candidate again.
  `--rate <labels-a> <labels-b>` reads the two raters' labels files in TOOL-dLinkedLibrary-1's form
  and computes the agreement with `derive_kappa`. Below 0.8 no candidate moves: the verb exits 3
  naming the agreement, and the rubric is revised and the candidates rated again, at most
  `flow.route-backs` times. At or above it, the verb writes the adoption's routing record (§4 "The
  decisions"), every candidate a row with its two labels, its settled class or `split`, its origin
  `reconstructed@<sha8> <source>` and its lifecycle `reconstructed`; a split candidate is never
  major (FK-4-6). Observed by AC3, AC4 and AC6.
- **S7** — `adopt.decisions-ratify`, through `retrofit.decisions`: under `author-rubric` (the
  default) no reconstructed decision waits on the owner; under `docs-owner-ratifies` and
  `docs-and-trailers`, `adopt decisions --ratify` lists each candidate settled `major` and each
  `split` one, and `--ratify <candidate id> ratified|declined --reason <text>` writes a `ruling`
  through the owner path, its `Subject` `<routing record>#<candidate id>`. A decision's lifecycle is
  derived, never rewritten into the landed routing record: `read_decision_lifecycle(root, build)`
  answers `rejected` for a candidate a `declined` ruling names and `reconstructed` otherwise, and the
  program's listings omit `rejected` ones. Observed by AC3 and AC5.
- **S8** — `adopt reconstruct`, through `retrofit.reconstruct`: under `on-touch` (the default) it
  prints `reconstruct — not run: retrofit.reconstruct is on-touch` and exits 0, `build.unit-pass`
  reconstructing on first touch; under `at-adoption` it runs once, after a census exists, and a second
  run refuses naming the first; under `on-ask` the owner's call is the ask and it runs each time.
  A run prints a brief for an agent naming each code path no dossier claims, per kit, where the
  codebase map is installed, and lands each dossier the agent returns with a column-0 `**Origin:**
  reconstructed@<sha8> <sources>` line under its H1; with the map absent it prints `reconstruct —
  nothing: the codebase map is not installed`. Observed by AC7.
- **S9** — The items: five `[[item]]` rows in `tools/loop/loop.toml` in TOOL-dDeclaredLoop-12's
  schema, tags `item.adopt.census`, `item.adopt.practices`, `item.adopt.decisions`,
  `item.adopt.decisions-ratify` and `item.adopt.reconstruct`, transcribed from flow-steps' `[adopt]`
  rows (flow-steps.md:712-717) per §4 "The items", each naming `program = "adopt"` in place of
  `step` (§8 F2's ask). `item.test.seed`'s `needs` gains `item.adopt.census`. Observed by AC10.
- **S10** — The keys: `retrofit.decisions`, `retrofit.practice-pending` and `retrofit.reconstruct`,
  each read once per verb through `resolve`; their catalogue rows (`tools/policy/catalogue.toml:1524`,
  `:1530`, `:1536`, owner dLinkedLibrary) gain `summary` and `usage`, their names leave
  `tools/policy/unsummarised-keys.txt` through `policy.py lists --write`, and `.governance/policy.json`
  is regenerated by `policy.py mirror --write`. Observed by AC11.
- **S11** — The fixture, `python adopt_program.py --fixture --plant <case>`: a scratch repository with
  a remote, an adoption build and unit, a committed `.governance/policy.toml` per plant, and the
  practices of §4 "The census"; rater route files and an owner-proof stub as the plants need. The
  plants are §6's. Observed by AC1 to AC8.
- **S12** — The docs: `help/adopt.md`, the program's verbs in order, each policy value, the census
  classes, and what `origin` means on a record, linked from `help/README.md`; the `origin` field and
  the three kinds named in `tools/memory-tree/HYGIENE.template.md`, rendered into `memory/HYGIENE.md`
  by `adopt-memory-tree.sh --render`. Observed by AC12.

## 3. Non-goals (OUT)

- `test.seed` and the ledger files themselves: dWitnessedBar's; `baseline` declares them as records
  and writes no rows.
- The origin check, `origin` in every slice and the digest's ranking: TOOL-dLinkedLibrary-9 and -2.
- `adopt.instructions` and the `instruction-file` practice's migration: TOOL-dLinkedLibrary-23.
- Importing a CI job as a leg, and the install and update hooks that call `adopt`: dShippedRelease's.
- The `decision` kind, the rubric, the routing of gov's own log rows and `derive_kappa`:
  TOOL-dLinkedLibrary-1's; an adopter's reconstructed decisions live in its routing record and add
  no log row.
- Heat ranking and the period's sweep: dTendedCadence's `maintain.retrofit-heat`.

### Edges

- **consumes-from** `TOOL-dLinkedLibrary-1` — `derive_kappa`, the one two-rater agreement S6 computes, with `CLASSES`, `RUBRIC` and the labels-file form the raters answer in
- **hands-off** `TOOL-dLinkedLibrary-9` — `origin`, the field and its three values the door writes, which that unit re-derives from history, renders and ranks
- **hands-off** `TOOL-dLinkedLibrary-10` — `baseline`, the kind whose records are the ledger's population files, whose progress the cell reports
- **hands-off** `TOOL-dLinkedLibrary-23` — `origin`, the `imported:<path>` value its paragraph proposals carry, beside the `adopt` dispatcher whose `instructions` verb it adds and the census class `instruction-file`
- **consumes-from** external — TOOL-dTotalRecall-1, -2 and -18, PLAY-dOrderedCharter-7 and -15, TOOL-dDeclaredLoop-12 and -23, TOOL-dWitnessedBar-13 and -15, DEFERRED at base and built before this unit's pass
- **hands-off** `TOOL-dLinkedLibrary-37` — `adopt_program.py decisions --rate` and the door's `--imported-from`, through which unit 37 mints its two planted records (id 58)
- **hands-off** `TOOL-dLinkedLibrary-47` — `adopt program selftest`, the leg unit 47 adds to run this unit's plants; this unit's ledger names it for the arm line (id 50)
- **hands-off** `TOOL-dLinkedLibrary-51` — `CI_REFUSE_PATTERNS` and the `ci-job` class, which unit 51 widens (id 67)
- **hands-off** `TOOL-dLinkedLibrary-52` — `adopt_program.py`'s `split` plant, which unit 52 resizes so AC3 can pass; this unit's ledger answers AC3 AMENDED (ids 5, 24, 38)

## 4. Design

### Evidence

- No practice census exists: `tools/govkit/census.py:1-26` answers whether an adopter's blob is in
  gov's history (IN-SYNC, DRIFT, FORK), a different question; it shows the read-only shape S4 keeps.
- `govkit adopt` is taken: `cmd_adopt` at `tools/govkit/govkit.py:12611` writes the install receipt.
- The three keys are declared, owner dLinkedLibrary, at `tools/policy/catalogue.toml:1524-1539`, and
  each name is on `tools/policy/unsummarised-keys.txt` (lines 173, 176, 177), verified at base.
- `flow.route-backs` is declared at `tools/policy/catalogue.toml:754`, default 3, owner dDeclaredLoop.
- No kappa or two-rater code exists: `git grep -i kappa -- tools` finds only a Greek-letter word list
  in `tools/govkit/selftest.py:9640` at base.

### The kinds

| Kind | Form | Fields, in order | Writer |
|---|---|---|---|
| `census` | `fields` | `Class`, `Practice`, `Instances`, `Paths`, `Rank`, `State`, `Taken at` | `gov_record.py new census` |
| `ruling` | `fields` | `Subject`, `Ruling`, `Ruled by`, `Reason` | `gov_record.py new ruling` |
| `baseline` | `rows` | none: each ledger file's header, graded by the factory | `legacy_ledger.py seed` |

`State` is `importable` or `refused: <why>`. `Ruling` is closed by its subject: `import`, `translate`,
`alongside` or `retire` for a census record; `ratified` or `declined` for a routing record's
candidate; `unit`, `amend <tag>` or `drop` for an instruction paragraph (TOOL-dLinkedLibrary-23 S7).
`Ruled by` is `owner`. Records are named
`<date>-build-<unit id>-<kind>-<n>.md` in the adoption build's `build/` folder, the factory's grammar.

### The pending practice

| `retrofit.practice-pending` | Recommended ruling | An unruled practice reads |
|---|---|---|
| `alongside` (the default, RF-4) | `alongside` | alongside, kept as it is |
| `propose-retire` | `retire` | `retire proposed`, kept as it is until the owner rules |

No value ends a practice without a ruling: retrofit's `[never]` forbids retiring a practice the
owner has not ruled on.

### The census

| Class | Found by |
|---|---|
| `lint-config` | a tracked `.eslintrc*`, `.prettierrc*`, `.editorconfig`, `.flake8`, `.pylintrc`, `.shellcheckrc`, `.golangci.yml`, or a `[tool.<linter>]` table of `pyproject.toml`, one practice per tool |
| `ci-job` | each job of `.github/workflows/*.yml`, `.gitlab-ci.yml` and `azure-pipelines.yml`, read by indentation without a YAML library; `refused` when a step's `run` or `uses` matches `CI_REFUSE_PATTERNS` (`git push`, `npm publish`, `twine upload`, `docker push`, `gh release`, `deploy`) |
| `decision-doc` | files under a directory named `adr` or `decisions`, and a tracked `DECISIONS.md` outside the memory root |
| `codeowners` | `CODEOWNERS`, `.github/CODEOWNERS` or `docs/CODEOWNERS` |
| `comment-convention` | `TODO(`, `FIXME` and `XXX` markers in tracked code, one practice per marker, counted by `git grep -c` |
| `instruction-file` | `CLAUDE.md`, `GEMINI.md`, `.github/copilot-instructions.md`, `.cursorrules` |

The memory root and gov's own installed kit paths are outside every class. `Instances` is the count
of files, jobs or markers; `Paths` names at most five, then `+<n>`.

### The decisions

The routing record is `<date>-build-<unit id>-decision-routing.md` in the adoption build's `build/`
folder, `**Serves:** research <unit id>`, its column-0 `**Origin:** reconstructed@<sha8> <sources>`
line naming the candidates' source documents, its first line under the H1 `kappa <k> over <n>
candidates · round <r>`, then one table row per candidate:

| Labels A and B | Settled | Major | Lifecycle at write | Listed for ratifying, under the two non-default values |
|---|---|---|---|---|
| both `major` | `major` | yes | `reconstructed` | yes |
| both one other class | that class | no | `reconstructed` | no |
| two different classes | `split` | no | `reconstructed` | yes |

Each row carries the candidate id, its source `path#anchor` or `commit:<sha8>` for a trailer, its
labels, its settled class and its origin `reconstructed@<sha8> <source>`.

### The items

| Tag | Actor | Needs | Returns | Outcomes and routes |
|---|---|---|---|---|
| `item.adopt.census` | `command:adopt.census` | none | `record-kind.census` | `taken` to `item.test.seed` |
| `item.adopt.practices` | `owner` | census | `record-kind.ruling` | `ruled` to done; `pending` to itself |
| `item.adopt.decisions` | `role:reviewer`, two raters | census | `record-kind.research` | `routed` to ratify; `below-floor` to itself, within `flow.route-backs` |
| `item.adopt.decisions-ratify` | `owner` | decisions | `record-kind.ruling` | `ratified`, `declined` to done |
| `item.adopt.reconstruct` | `command:adopt.reconstruct` | census | `record-kind.dossier` | `done`; `skipped` under `on-touch` |

Each row's `owner` is `dLinkedLibrary`, its `witness` the record its `returns` names.

### Inventory

Minted: `tools/memory-tree/adopt_program.py` with `scan_practices`, `rank_practices`,
`route_candidates`, `read_decision_lifecycle`, `CI_REFUSE_PATTERNS`; the routing record; the `adopt` subcommand of `core.py`;
the door flags `--reconstructed-from`, `--source` and `--imported-from`; the kinds `census`,
`ruling`, `baseline`; the home sentinel `ledger`; the five item rows; `help/adopt.md`. Naming cells:
each function asked of the lexicon's `--suggest` under `--as py.function` at the pass.

### Migration

None for existing records: a record with no `**Origin:**` line reads as unrecorded
(TOOL-dLinkedLibrary-9 S3), and nothing is backfilled.

### Rollout

The program runs only when called. Every default is the passive one: no owner wait under
`author-rubric`, alongside for an unruled practice, no reconstruction under `on-touch`.

### Files touched (estimate)

- `tools/memory-tree/adopt_program.py` (new)
- `tools/playbook/core.py`: the `adopt` dispatcher
- `tools/playbook/render_playbook.py`: `KIT_PLAYBOOK_RENDER_VERSION` moved
- `tools/memory-tree/gov_record.py` and `tools/memory-tree/build_records.py`: S2
- `tools/memory-tree/record_kinds.py`: the `ledger` sentinel
- `tools/memory-tree/record-kinds.toml`: the three rows
- `tools/memory-tree/check-memory-hygiene.sh`: `KIT_MEMORY_TREE_VERSION` moved
- `tools/memory-tree/HYGIENE.template.md` (the source) and `memory/HYGIENE.md` (its render)
- `tools/loop/loop.toml`: the five items and `item.test.seed`'s need
- `tools/policy/catalogue.toml`, `tools/policy/unsummarised-keys.txt`, `tools/policy/policy.py` (`KIT_POLICY_VERSION`)
- `.governance/policy.json`: regenerated, in its own commit
- `tools/memory-tree/README.md`
- `help/adopt.md` (new)
- `help/README.md`

### Alternatives rejected

- **The program inside `govkit`.** Its `adopt` verb writes the receipt, and the clause names the
  core's own command.
- **Hand-written census and ruling records.** The door is the one writer and derives `origin`; a
  hand-written record would type it.
- **A new top-level memory directory for adoption records.** The adoption build's folder is already a
  sanctioned home the door mints into.

## 5. Production-readiness checklist

- security — the census reads and never executes: CI files are parsed as text, a deploy, publish or
  push job is refused at the census, and nothing in the adopter's tree runs. Owner rulings pass the
  owner proof. The door validates every field and every origin fact at the write boundary.
- perf / scale — one `git ls-files` and one `git grep -c` per marker class; decisions scale with the
  candidates, each rated once per round.
- error / empty / loading states — a repository with no practices writes no census record and says
  so; an agreement below 0.8 moves nothing; a missing build or unit refuses.
- observability — every verb prints what it wrote, each refusal names its rule, and the routes
  instrument keeps both raters' answers so the agreement can be re-derived.
- risks — a practice class the census does not know stays uncounted; the classes are a table this
  unit owns and extends.
- testing — the plants of S11.
- migration — none.
- user docs — `help/adopt.md`, S12.

## 6. Acceptance criteria

- **AC1** — When `python adopt_program.py --fixture --plant census` runs `core.py adopt census` over a
  repository holding `.eslintrc.json`, a workflow with jobs `test` and `release` (`npm publish`),
  an ADR file in an `adr` directory, `CODEOWNERS`, `CLAUDE.md` and three `TODO(` markers, it writes one
  `census` record per practice, `release` with `State` `refused: npm publish`, ranked by instances;
  `git status --porcelain` lists only the new records; a second run writes nothing; with `--build`
  absent it exits 2.
  Red when: two CI jobs share a record, a deploy job reads importable, or the scan changes a file.
- **AC2** — When the plant `practices` runs `adopt practices`, each unruled practice is listed with
  the recommendation `alongside`; with `retrofit.practice-pending = "propose-retire"` committed, the
  recommendation is `retire` and the practice reads `retire proposed`; `--rule <record> import` on
  `release` exits 2, a second ruling of one practice exits 2, and a ruling from a caller failing the
  owner proof exits 2.
  Red when: an unruled practice reads retired, or an automated caller writes a ruling.
- **AC3** — When the plant `split` rates four candidates, both raters `major` on one, both `minor` on
  one, `waiver` and `process-rule` on one and `major` and `minor` on another, at an agreement of 0.8
  or more, the routing record holds four rows with lifecycle `reconstructed` and an origin
  `reconstructed@<sha8> <source>`, the two split ones settled `split` with `Major` `no`; under
  `author-rubric` `--ratify` lists none; under `docs-owner-ratifies` it lists the major one and the
  two split ones.
  Red when: the planted split candidate is settled major, or is listed for ratifying under
  `author-rubric`.
- **AC4** — When the plant `floor` rates route files whose `derive_kappa` agreement is below 0.8, the
  verb exits 3 naming the agreement and writes no routing record; with `flow.route-backs = 1`
  committed, a second below-floor round exits 3 naming the exhausted bound.
  Red when: a candidate moves below the floor, or rounds run past the bound.
- **AC5** — When the plant `decline` runs `--ratify <candidate id> declined` under
  `docs-owner-ratifies`, `read_decision_lifecycle` answers `rejected` for it, the routing record's
  bytes are unchanged, and a following `--candidates` run omits its source.
  Red when: a declined decision is proposed again, or a landed record is rewritten.
- **AC6** — When the plant `trailers` commits a `Decided:` trailer, `--candidates` lists it under
  `retrofit.decisions = "docs-and-trailers"` and omits it under `docs-owner-ratifies`.
  Red when: trailers are read under a value that excludes them.
- **AC7** — When the plant `reconstruct` runs `adopt reconstruct`, under the default it prints
  `reconstruct — not run` and writes nothing; under `at-adoption` it prints a brief naming the
  unclaimed paths and a second run exits 2 naming the first; under `on-ask` a second run is admitted.
  Red when: reconstruction runs under `on-touch`, or twice under `at-adoption`.
- **AC8** — When `python gov_record.py new census … --field Origin=written` runs, it exits 2; a record
  written with no origin flag carries `- **Origin:** written`; one written with
  `--reconstructed-from <sha> --source <path>` carries `reconstructed@<sha8> <path>`, and one naming
  a source absent at that sha exits 2.
  Red when: an origin value is accepted as typed, or an unverifiable source is recorded.
- **AC9** — When `python record_kinds.py --check` reads the registry with the three rows, it exits 0;
  with a planted `[[ledger]]` registration whose `leg` names no leg of the manifest, it exits 1 naming
  `baseline` and that leg.
  Red when: the `ledger` sentinel is read as a literal home or passes an unknown leg.
- **AC10** — When `python loop_lib.py --check` runs at the pass tip, its population holds the five
  `item.adopt.*` rows and `item.test.seed` needing `item.adopt.census`; with a planted need naming an
  undeclared item, it exits 1 naming it.
  Red when: an adopt item is outside the program check.
  fixture: needs §8 F2's ask landed in dDeclaredLoop; until then the rows are a stand-in the check
  names.
- **AC11** — When `python policy.py get retrofit.reconstruct` runs with no value set it prints
  `on-touch`, and after `policy.py lists --write` the summary list names none of the three keys.
  Red when: a row is missing or still unsummarised.
- **AC12** — When `grep -n "docs-and-trailers" adopt.md` runs over the help page, it finds the
  decisions section naming the three values of `retrofit.decisions` and the split rule.
  Red when: the page omits a verb or a policy value.

## 7. Gates

`memory hygiene` · `spec tokens (a spec's own names resolve)` · `lexicon naming predicates` · `kit epoch (shipped bytes move, the version moves)` · `kit/dogfood doc parity` · `recall floor` · `recall floor arms` · `govkit acceptance matrix` · `playbook render selftest` · `policy fixtures`

New arm: tools/memory-tree/adopt_program.py · covers AC1 AC2 AC3 AC4 AC5 AC6 AC7 AC8 · `adopt_program.py --selftest` runs every plant under the `record-kinds` leg, its failing case staged by a router that writes a split candidate major · none

## 8. Open questions

- **F1 — Where do the program's records live, when `adopt` runs before any build?** Options: (a) a
  build the owner opens for the adoption, named by `--build` and `--unit`, its `build/` folder the
  home the door mints into under that build's claim; (b) a new sanctioned directory under the memory
  root, a change to hygiene check 3; (c) registries under `memory/project/`. (b) changes a governance
  carrier; (c) has no `**Serves:**` binding for a ruling. RESOLVED (agent, 2026-10-26, delegated):
  (a), rung 3, every write through the door's existing minting rule. widens: none · relaxes: none
- **F2 — How is an adopt item declared, when the item schema names one of five steps?**
  TOOL-dDeclaredLoop-12 §3 keeps every adopt item out of the five steps, and TOOL-dWitnessedBar-15 §8
  F4 recommends the same ask for `item.test.seed`. Options: (a) ask dDeclaredLoop that an `[[item]]`
  row may name `program = "adopt"` in place of `step`; (b) declare the rows under `step.test`; (c)
  keep the items outside `loop.toml`. (b) misplaces them and (c) leaves the item join blind.
  RESOLVED (agent, 2026-10-26, delegated): (a), rung 3. The ask, for the main loop to file once:
  target dDeclaredLoop's `BACKLOG.md`, "AN ADOPT-PROGRAM ITEM HAS NO STEP. TOOL-dLinkedLibrary-8 and
  TOOL-dWitnessedBar-15 each declare `item.adopt.*` and `item.test.seed`, rows of flow-steps'
  `[adopt]` table, and TOOL-dDeclaredLoop-12's schema requires a step", accept "an `[[item]]` row
  naming `program = "adopt"` in place of `step` is held by `check_program`'s need, outcome, route and
  layer rules and not its step-exit rule, seen on a planted adopt row with an undeclared need".
  widens: none · relaxes: none
- **F3 — How does the `baseline` kind name its home, when each population's home differs?**
  Options: (a) a sentinel `ledger` meaning each registration's own `home` and `leg`, resolved by
  `read_registrations`; (b) the comma list of every registered home typed into the row; (c) one glob
  over every kit's directory. (b) types a fact the registrations own; (c) matches files that are not
  ledgers. RESOLVED (agent, 2026-10-26, delegated): (a), rung 3, one fact read where it lives.
  widens: none · relaxes: none
- **F4 — What does `adopt reconstruct` reconstruct?** The design says "records for code no unit
  touched" and names the first-touch dossier as the reconstructed record's other source
  (retrofit.md:455). Options: (a) dossiers for the paths no dossier claims, where the codebase map is
  installed; (b) every record kind a unit pass writes; (c) code purposes. (b) names kinds whose
  first-touch writers are dScopedBuild's and unbuilt; (c) are not records and are
  TOOL-dLinkedLibrary-15's. RESOLVED (agent, 2026-10-26, delegated): (a), rung 3. widens: none ·
  relaxes: none

## 9. Revision log

- rev-1 · 2026-10-26 · initial draft, from the packet's Items 8, retrofit.md `[seed]`, `[origin]`,
  `[practices]` and RF-3, RF-4 (:343-372, :445-470, :471-484, :579-582), flow-steps.md `[adopt]`
  (:702-718), layer-memory.md:463-465, and scout D's row for cl-0245.
- rev-2 · 2026-10-26 · §3 · the Edges block gains the bullets mirroring TOOL-dLinkedLibrary-37, TOOL-dLinkedLibrary-47, TOOL-dLinkedLibrary-51, TOOL-dLinkedLibrary-52, promoted from the round-1 spec audit of the 25 unit specs; nothing else moved.

## 10. Reuse audit

The seams extended: TOOL-dTotalRecall-1's registry and factory for the three kinds, with its
`check_record_kinds` taught the `ledger` sentinel; TOOL-dTotalRecall-2's door, which gains the origin
derivation rather than a second writer; PLAY-dOrderedCharter-7's `core.py` for the dispatcher;
TOOL-dDeclaredLoop-12's item rows; TOOL-dDeclaredLoop-23's `decided` for trailers;
TOOL-dLinkedLibrary-1's `derive_kappa`. `python tools/codebase-map/reuse_lookup.py "census of a
repository's own practices lint configs ci jobs decision documents codeowners"` ranked `census`
(`tools/memory-tree/merge-rows.py`), `CensusRefused` (`tools/process-monitor/census.py`) and
`derive_census_tree` (`tools/policy/policy.py:1043`); each counts something else (merge rows,
processes, an install receipt), so no existing seam fits the practice census, and
`tools/govkit/census.py` is a fork census, read only for its read-only shape. Scout D's lines
agreed with source at base (`govkit.py:12611`, `catalogue.toml:1524-1539`); its proposal to edit
`tree_lib.py:406` is not needed, since door-written kinds join the Serves kinds through
TOOL-dTotalRecall-18 S7. The recall query returned scout D's row, the brief's row and
PLAY-dOrderedCharter-1's spec, and nothing that takes a practice census.

Recall terms used: `python tools/memory-recall/query.py "how does the adopt program take a census of practices and reconstruct decisions with two raters" --terms "adopt census practices ruling retrofit.decisions reconstructed rejected origin baseline two raters kappa FK-4-6"`
