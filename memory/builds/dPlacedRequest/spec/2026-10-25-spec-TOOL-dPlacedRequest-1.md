# TOOL-dPlacedRequest-1 — one lease grammar for builds, units and cadence runs, with an epoch, run claims migrated onto it, and its verbs and four policy keys

**Status:** OPEN · rev-3 · 2026-10-25 · node a · Tier-2 · base c63aabbb · streams tooling · order 3 · advances TOOL-dPlacedRequest-22

**Carries:** cl-dClosedLoop-0120@5d655f07 whole
**Carries:** node:record-kind.lease
**Carries:** node:policy-key.leases
**Carries:** node:policy-key.leases.granularity
**Carries:** node:policy-key.leases.renewal
**Carries:** node:policy-key.leases.overlap
**Carries:** node:policy-key.leases.offline

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-25-build-TOOL-dPlacedRequest-1-fix-return.md](../build/2026-10-25-build-TOOL-dPlacedRequest-1-fix-return.md) | research | TOOL-dPlacedRequest-2 TOOL-dPlacedRequest-3 TOOL-dPlacedRequest-4 TOOL-dPlacedRequest-5 TOOL-dPlacedRequest-6 TOOL-dPlacedRequest-7 TOOL-dPlacedRequest-8 TOOL-dPlacedRequest-9 TOOL-dPlacedRequest-10 TOOL-dPlacedRequest-11 TOOL-dPlacedRequest-12 TOOL-dPlacedRequest-13 TOOL-dPlacedRequest-14 TOOL-dPlacedRequest-15 TOOL-dPlacedRequest-16 TOOL-dPlacedRequest-17 TOOL-dPlacedRequest-18 TOOL-dPlacedRequest-19 TOOL-dPlacedRequest-20 TOOL-dPlacedRequest-21 |
| [2026-10-25-build-TOOL-dPlacedRequest-1-reuse-scout-a.md](../build/2026-10-25-build-TOOL-dPlacedRequest-1-reuse-scout-a.md) | research | TOOL-dPlacedRequest-11 TOOL-dPlacedRequest-12 TOOL-dPlacedRequest-13 TOOL-dPlacedRequest-15 TOOL-dPlacedRequest-16 TOOL-dPlacedRequest-17 TOOL-dPlacedRequest-18 TOOL-dPlacedRequest-20 |
| [2026-10-25-build-TOOL-dPlacedRequest-1-reuse-scout-b.md](../build/2026-10-25-build-TOOL-dPlacedRequest-1-reuse-scout-b.md) | research | TOOL-dPlacedRequest-2 TOOL-dPlacedRequest-3 TOOL-dPlacedRequest-4 TOOL-dPlacedRequest-5 TOOL-dPlacedRequest-9 TOOL-dPlacedRequest-10 TOOL-dPlacedRequest-14 TOOL-dPlacedRequest-19 TOOL-dPlacedRequest-21 |
| [2026-10-25-build-TOOL-dPlacedRequest-1-reuse-scout-c.md](../build/2026-10-25-build-TOOL-dPlacedRequest-1-reuse-scout-c.md) | research | TOOL-dPlacedRequest-6 TOOL-dPlacedRequest-7 TOOL-dPlacedRequest-8 |
| [2026-10-25-build-TOOL-dPlacedRequest-1-spec-stage-returns.md](../build/2026-10-25-build-TOOL-dPlacedRequest-1-spec-stage-returns.md) | research | TOOL-dPlacedRequest-2 TOOL-dPlacedRequest-3 TOOL-dPlacedRequest-4 TOOL-dPlacedRequest-5 TOOL-dPlacedRequest-6 TOOL-dPlacedRequest-7 TOOL-dPlacedRequest-8 TOOL-dPlacedRequest-9 TOOL-dPlacedRequest-10 TOOL-dPlacedRequest-11 TOOL-dPlacedRequest-12 TOOL-dPlacedRequest-13 TOOL-dPlacedRequest-14 TOOL-dPlacedRequest-15 TOOL-dPlacedRequest-16 TOOL-dPlacedRequest-17 TOOL-dPlacedRequest-18 TOOL-dPlacedRequest-19 TOOL-dPlacedRequest-20 TOOL-dPlacedRequest-21 |
| [2026-10-25-prompt-TOOL-dPlacedRequest-1-1-reuse-scout.md](../prompts/2026-10-25-prompt-TOOL-dPlacedRequest-1-1-reuse-scout.md) | journal | — |
| [2026-10-25-prompt-TOOL-dPlacedRequest-1-2-reuse-scout.md](../prompts/2026-10-25-prompt-TOOL-dPlacedRequest-1-2-reuse-scout.md) | journal | — |
| [2026-10-25-prompt-TOOL-dPlacedRequest-1-3-reuse-scout.md](../prompts/2026-10-25-prompt-TOOL-dPlacedRequest-1-3-reuse-scout.md) | journal | — |
| [2026-10-25-prompt-TOOL-dPlacedRequest-1-4-spec-writer.md](../prompts/2026-10-25-prompt-TOOL-dPlacedRequest-1-4-spec-writer.md) | journal | — |
| [2026-10-25-prompt-TOOL-dPlacedRequest-1-5-spec-writer.md](../prompts/2026-10-25-prompt-TOOL-dPlacedRequest-1-5-spec-writer.md) | journal | — |
| [2026-10-25-prompt-TOOL-dPlacedRequest-1-6-spec-writer.md](../prompts/2026-10-25-prompt-TOOL-dPlacedRequest-1-6-spec-writer.md) | journal | — |
| [2026-10-25-prompt-TOOL-dPlacedRequest-1-fix-brief.md](../prompts/2026-10-25-prompt-TOOL-dPlacedRequest-1-fix-brief.md) | research | TOOL-dPlacedRequest-2 TOOL-dPlacedRequest-3 TOOL-dPlacedRequest-4 TOOL-dPlacedRequest-5 TOOL-dPlacedRequest-6 TOOL-dPlacedRequest-7 TOOL-dPlacedRequest-8 TOOL-dPlacedRequest-9 TOOL-dPlacedRequest-10 TOOL-dPlacedRequest-11 TOOL-dPlacedRequest-12 TOOL-dPlacedRequest-13 TOOL-dPlacedRequest-14 TOOL-dPlacedRequest-15 TOOL-dPlacedRequest-16 TOOL-dPlacedRequest-17 TOOL-dPlacedRequest-18 TOOL-dPlacedRequest-19 TOOL-dPlacedRequest-20 TOOL-dPlacedRequest-21 |
| [2026-10-25-prompt-TOOL-dPlacedRequest-1-spec-brief.md](../prompts/2026-10-25-prompt-TOOL-dPlacedRequest-1-spec-brief.md) | research | TOOL-dPlacedRequest-2 TOOL-dPlacedRequest-3 TOOL-dPlacedRequest-4 TOOL-dPlacedRequest-5 TOOL-dPlacedRequest-6 TOOL-dPlacedRequest-7 TOOL-dPlacedRequest-8 TOOL-dPlacedRequest-9 TOOL-dPlacedRequest-10 TOOL-dPlacedRequest-11 TOOL-dPlacedRequest-12 TOOL-dPlacedRequest-13 TOOL-dPlacedRequest-14 TOOL-dPlacedRequest-15 TOOL-dPlacedRequest-16 TOOL-dPlacedRequest-17 TOOL-dPlacedRequest-18 TOOL-dPlacedRequest-19 TOOL-dPlacedRequest-20 TOOL-dPlacedRequest-21 |
| [2026-10-25-review-TOOL-dPlacedRequest-1-spec-audit.md](../reviews/2026-10-25-review-TOOL-dPlacedRequest-1-spec-audit.md) | spec-audit | TOOL-dPlacedRequest-11 TOOL-dPlacedRequest-13 TOOL-dPlacedRequest-17 TOOL-dPlacedRequest-16 TOOL-dPlacedRequest-20 TOOL-dPlacedRequest-18 TOOL-dPlacedRequest-12 TOOL-dPlacedRequest-15 TOOL-dPlacedRequest-19 TOOL-dPlacedRequest-9 TOOL-dPlacedRequest-2 TOOL-dPlacedRequest-8 TOOL-dPlacedRequest-6 TOOL-dPlacedRequest-7 TOOL-dPlacedRequest-4 TOOL-dPlacedRequest-10 TOOL-dPlacedRequest-14 TOOL-dPlacedRequest-5 TOOL-dPlacedRequest-21 TOOL-dPlacedRequest-3 |

<!-- /gen:spec-records -->

## 1. Goal

One lease mechanism serves every holder: a build, a unit of a build, and a cadence run, each a ref
on the remote written by compare-and-swap, each carrying an epoch that rises at every take-over, and
the unattended run claim migrated onto it so one mechanism remains (coordination.md:79-101). Today
only runs are claimed (`refs/gov/runs/<slug>`, `tools/unattended/unattended.sh:2087`); a claim names a
user, not a fleet tag (`:2410`), carries no epoch, covers no unit (gap-conc-01, gap-conc-02); overlap is
a probe that "always returns 0" (`check_cross_run_overlap`, `:3409`); and an unreachable remote is only
announced (`:2141-2149`).

## 2. Scope (IN)

- **S1** — The grammar (I5): `refs/gov/leases/<slug>/build`, `refs/gov/leases/<slug>/unit/<id>` and
  `refs/gov/leases/run/<cadence>/<period>`, built only by `derive_lease_ref <kind> <name> [<sub>]`,
  each segment held by `check_lease_segment` to a legal one-segment ref name. `<cadence>` takes any
  legal segment here; `TOOL-dPlacedRequest-18` narrows it to the tag grammar (I7). Observed by AC1.
- **S2** — The record (I6), `record-kind.lease`: the commit `TOOL-dPlacedRequest-11`'s
  `build_gov_commit` builds, parented on the tip read, its message the header `gov-claim <tail>` (the
  ref after `refs/gov/leases/`), a blank line, today's eight keys (`unattended.sh:2411-2412`) and
  `epoch`, `kind`, `fleet-tag`, `renews`, `witness`, `offer`, `offer-deadline` and `last-fetch`, the
  last three written `-` until `TOOL-dPlacedRequest-16` and `TOOL-dPlacedRequest-20` fill them. The
  reader `read_claims` (`:2118`) stays the one parser: it validates the header against the ref, the
  `slug` key against the tail's first segment, `epoch` as a positive integer and `kind` against the
  ref's shape, and carries the new fields in `CLAIM_ROWS`. Observed by AC1 and AC2.
- **S3** — The epoch: a create writes 1; a take or an announced take of a foreign lease writes the
  read epoch plus one; every other write keeps it. A record with no `epoch` reads 0. Observed by AC2.
- **S4** — The migration of run claims (I24): the driver's claim is the build lease
  `refs/gov/leases/<slug>/build`. `read_claims` fetches `refs/gov/leases/*` and the legacy
  `refs/gov/runs/*` in one bounded fetch; for a slug with both, the lease row wins and the legacy row
  is not printed. The first write to a slug holding only a legacy claim parents the lease's first
  commit on the legacy tip at epoch 1, so the history carries over, and the legacy ref is left in
  place. `RUN_CLAIMS` (`:671-676`) stays the dark-landing switch for every lease read and write.
  Observed by AC3.
- **S5** — The verbs: `unattended.sh --lease acquire|renew|release|take-over <kind> <name> [<sub>]`,
  with `--witness <sha>` on `renew` and `--as landed|aborted|withdrawn` on `release`. Each reads the
  remote's leases, derives its row through `check_claim_writable`'s table, which gains a `lease` mode
  (S6), writes through `write_gov_ref`, and prints one line: `lease — <tail> · <act> · epoch <n>`, or
  `lease refused — <cause> · <tail> · <holder>` with one cause word of I9 and exit 1, or `lease not
  written — <why>` with exit 2. `withdrawn` joins `landed` and `aborted` as a terminal status. Observed
  by AC1, AC2, AC9 and AC10.
- **S6** — The `lease` mode, a column of `CLAIM_MODES` (`:2220`): a lease is `mine` when its
  `fleet-tag` and `session` equal this node's tag and this harness's session; `acquire` creates on
  none, renews on mine, and refuses `live-holder` on foreign live or held, `live-holder` naming
  `take-over` on foreign stale, and `tombstone` on foreign terminal; `take-over` takes foreign stale
  with an announced line and health event and refuses every other foreign row as `acquire` does. A
  compare-and-swap lost between read and write is `epoch-fence`. Observed by AC2 and AC9.
- **S7** — `leases.granularity` (`build-and-unit`, `build`, `unit`; default `build-and-unit`): `build`
  refuses `--lease acquire unit` and `unit` refuses `--lease acquire build`, each with exit 2 naming the
  key and its value; the driver's run claim is a build lease under every value. Observed by AC5.
- **S8** — `leases.renewal` (`progress`, `activity`, `fixed`, `none`; default `progress`) sets each
  write's `renews` and `witness`. Under `progress`, a write renews only when it carries a witness: a
  commit that resolves, carries a `Gov-Transition` trailer (TOOL-dDeclaredLoop-3 S1) naming this
  build, and differs from the record's `witness`; any other write, a beat included, writes
  `renews: no`. `activity` renews on every write, `fixed` only at acquisition, and `none` writes
  `renews: -`, which `TOOL-dPlacedRequest-17` reads as a lease that never expires. Until
  dWellOiledMachine's progress ledger lands, the transition record is the only witness. Observed by AC4.
- **S9** — `leases.overlap` (`kit-dirs`, `files`, `builds`; default `kit-dirs`) and `leases` (`warn`,
  `refuse`; default `warn`) replace the probe's constant 0. `check_cross_run_overlap` reduces each
  path before its join, to its kit directory under `kit-dirs` and unchanged under `files`, and under
  `builds` prints one finding per other branch instead of one per path. It runs at `--lease acquire`
  and where the driver calls it today (`:7492`); under `warn` it prints and returns 0, under `refuse` it
  returns 1 and the acquisition is refused `overlap`. Observed by AC6.
- **S10** — `leases.offline` (`warn`, `refuse`, `follow-leases`; default `warn`) when the read cannot
  reach the remote: `warn` builds the lease commit on the cached tip, records it in
  `<git-common-dir>/gov-queue.log` and prints `queued`; `refuse` refuses `offline`; `follow-leases`
  lets a renew of a lease this node holds print `follow-leases` and write nothing, and refuses every
  acquisition and take-over `offline`. `--lease flush` and every later successful read push each queued
  commit by compare-and-swap on its recorded tip; a lost one prints `yield`, appends a `lease-yielded`
  health event and leaves the queue. No value creates a ref, local or remote, while offline. Observed by
  AC7.
- **S11** — Fleet identity and uniqueness: `resolve_fleet_tag` asks the playbook kit's one fleet
  reader, `read_fleet` (`tools/playbook/render_playbook.py:347`), through a new `--fleet-tag --user
  <u> --host <h>` flag, for the row matching this node; a node with none is refused with exit 2 naming
  `fleet.toml` before any write. The `--claims` row's node column prints the fleet tag. A build lease
  create is the remote uniqueness check of a slug: two nodes creating one lease see one win and one
  `epoch-fence`. Observed by AC8 and AC9.
- **S12** — The four keys and `leases` are read through dGroundRules-2 S6's `resolve(key)`, as
  `python <prefix>/policy/policy.py get <key>`, once per process each, by `read_lease_policy`; until
  dGroundRules' reader resolves an unset key, a refusal reads as the catalogue default above and prints
  one NOTE naming the key. Their catalogue rows are dGroundRules-1 S3's. Observed by AC4 and AC5.
- **S13** — The stops guide's section 7 (`tools/unattended/STOPS.template.md:187-245`, rendered to
  `memory/guides/UNATTENDED-STOPS.md`) states the grammar, the record, the epoch, the `lease` column,
  the verbs, the four keys and the refusal causes `[rules]` routes. Observed by AC10.

## 3. Non-goals (OUT)

- No expiry by a declared clock: the verdict's age stays the reader's clock against `beat-utc`
  (`:2177-2186`) until `TOOL-dPlacedRequest-17`.
- No hand-over status, tombstone rule, queued-claim age or prune: `released`, `last-fetch` and the
  terminal refusals' draw exception are `TOOL-dPlacedRequest-16`'s.
- No offer: `offer` and `offer-deadline` are written `-` here and filled by `TOOL-dPlacedRequest-20`.
- No step-checklist caller: `plan.lease`, `build.unit-lease` and `deploy.unlease` are later builds'
  items that call S5's verbs; `entry.claim`'s lease is `TOOL-dPlacedRequest-21`'s.
- No mailbox notice of an overlap or a take-over: dKeptSession's mailbox posts them.
- No record-kind factory: the `record kind` kind's factory is dConvergedCharter's, which registers
  `record-kind.lease` from the grammar S2 states.
- No ask-id mint: the offline queue (S10) carries lease writes; other compare-and-swap mints apply
  `leases.offline` through the same queue functions when they land.

### Edges

- **consumes-from** `TOOL-dPlacedRequest-11` — `write_gov_ref` and `build_gov_commit`, through which every lease write lands parented on the tip read
- **hands-off** `TOOL-dPlacedRequest-17` — `refs/gov/leases/<slug>/build` and the `renews` and `witness` fields, whose expiry the observer clock judges
- **hands-off** `TOOL-dPlacedRequest-16` — `refs/gov/leases/<slug>/build`, the `epoch` and the `last-fetch` field, which the hand-over, the tombstone and the queued-claim age rule extend
- **hands-off** `TOOL-dPlacedRequest-20` — `refs/gov/leases/<slug>/build`, the `epoch` and the `offer` fields, which acquisition with an offer extends
- **hands-off** `TOOL-dPlacedRequest-18` — `refs/gov/leases/<slug>/build` and `derive_lease_ref`, whose cadence segment that unit narrows to the tag grammar
- **hands-off** `TOOL-dPlacedRequest-15` — `refs/gov/leases/<slug>/build`, the lease tip the fenced effect push carries a beat on
- **hands-off** `TOOL-dPlacedRequest-19` — `refs/gov/leases/<slug>/build`, the grammar a request record's lease is acquired by, and the offline queue it applies
- **hands-off** `TOOL-dPlacedRequest-21` — `refs/gov/leases/<slug>/build` and the refusal causes, which `entry.claim` routes, and the offline queue it applies
- **hands-off** `TOOL-dPlacedRequest-4` — `refs/gov/leases/<slug>/build`, the lease `placement.check` reads for `continue` and `amend`
- **hands-off** external — dKeptSession's presets cannot set `leases` beside a `leases.*` key in one TOML file (TOOL-dGroundRules-1 §8 F5), and its mailbox posts overlaps and take-overs
- **hands-off** `TOOL-dPlacedRequest-23` — `run_lease_verb` and `leases.offline`'s offline branch, which that unit keeps out of every strict claim read
- **hands-off** `TOOL-dPlacedRequest-24` — `add_gov_queue`, `write_gov_queue` and `gov-queue.log`, which that unit puts under a node lock and makes idempotent
- **hands-off** `TOOL-dPlacedRequest-25` — the lease writer's `renews` decision, which that unit derives so a write opening a tenure renews
- **hands-off** `TOOL-dPlacedRequest-26` — the record's `epoch` and `renews` keys, which mark the tenure that unit's walk stops at
- **hands-off** `TOOL-dPlacedRequest-29` — the record's `epoch`, `fleet-tag` and `session` and the `lease` mode, which decide that unit's same-holder re-fence
- **hands-off** `TOOL-dPlacedRequest-32` — the `lease` mode's `mine` test and the `--lease` verbs, which that unit closes to an absent session
- **hands-off** `TOOL-dPlacedRequest-34` — the round-1 spec audit's minors this unit's code carries, which that unit amends in place as its §2 names

## 4. Design

### The record

```
gov-claim dExample/unit/TOOL-dExample-3

slug: dExample
node: daily-agent
host: COMPEETO-AGENT
session: 5f0c…
keepalive: absent
status: live
lease-utc: 2026-10-25T09:00:00Z
beat-utc: 2026-10-25T09:40:12Z
epoch: 3
kind: unit
fleet-tag: a
renews: yes
witness: 3f9c2a71…
offer: -
offer-deadline: -
last-fetch: -
```

A lease taken by a step checklist outside a run has no keepalive and writes `absent`. A run claim
keeps its keepalive, session and host rules from the run-state file, unchanged (`:2405-2410`).

### The rows

`CLAIM_ROWS` grows from eleven TAB fields to eighteen: the eleven `:2113-2114` lists, with field 1 the
lease's name (`<slug>` for a build lease, so every slug-keyed caller keeps working, `<slug>/unit/<id>`,
or `run/<cadence>/<period>`) and field 2 the fleet tag, then `epoch`, `kind`, `renews`, `witness`,
`offer`, `offer-deadline` and `last-fetch`. `print_claims` still prints fields 1 to 5 (`:2204`), so the
`--claims` row shape TOOL-dDeclaredLoop-8 S7 extends is unchanged. `check_claim_writable` reads the
eighteen fields.

### The table, extended

| claim read | `lease` acquire | `lease` take-over | `lease` renew | `lease` release |
|---|---|---|---|---|
| none | create, epoch 1 | create, epoch 1 | not written, exit 2 | not written, exit 2 |
| mine | renew | renew | renew | write the status |
| same session | rewrite | take, epoch +1 | rewrite | write the status |
| foreign `live` or `held` | refused `live-holder` | refused `live-holder` | refused `live-holder` | refused `live-holder` |
| foreign `stale` | refused `live-holder`, naming `take-over` | take, announced, epoch +1 | refused `live-holder` | refused `live-holder` |
| foreign `terminal` | refused `tombstone` | refused `tombstone` | refused `tombstone` | refused `tombstone` |
| `unknown` | refused `live-holder` | refused `live-holder` | refused `live-holder` | refused `live-holder` |

The run columns of section 7 keep every cell; their takes now bump the epoch. `CLAIM_READS` gains no
class here.

### The policy reads

| Key | Values | Default | Read where |
|---|---|---|---|
| `leases` | warn, refuse | warn | the overlap's verdict (S9) |
| `leases.granularity` | build-and-unit, build, unit | build-and-unit | `--lease acquire` (S7) |
| `leases.renewal` | progress, activity, fixed, none | progress | every lease write (S8) |
| `leases.overlap` | kit-dirs, files, builds | kit-dirs | the overlap's reduction (S9) |
| `leases.offline` | warn, refuse, follow-leases | warn | an unanswered read (S10) |

Defaults from v2:1157-1162. A policy file cannot hold `leases` and a `leases.*` key together
(TOOL-dGroundRules-1 §8 F5); a project setting one reads the other at its default.

### The witness under `progress`

`--witness <sha>` must name a commit the clone holds whose `Gov-Transition` trailer names this build,
read with one `git log -1 --format='%(trailers:key=Gov-Transition,valueonly)'`; a sha that does not
resolve or carries none exits 2. A beat (`--beat`, `write_claim_beat`, `:2469`) and every holder write
the driver makes without a new witness write `renews: no`; they still move `beat-utc`, which the
liveness verdict reads until `TOOL-dPlacedRequest-17` replaces it. The driver passes the newest
`Gov-Transition` commit on the run's branch as its witness when one exists. Until dWellOiledMachine's
executor writes transitions at item boundaries, a run lease therefore renews only when a transition is
recorded by hand, and this is the interim v2:1159 journals.

### The overlap reduction

`kit-dirs` reduces `tools/<kit>/…` and `skills/<skill>/…` to that directory and any other path to its
first segment, so two builds editing different files of one kit overlap. `files` is today's join, a path
or a directory the other sits under. `builds` keeps that join and prints one finding per other branch,
naming the shared count. The probe's population stays every unmerged remote branch within
`OVERLAP_AGE_DAYS`: a lease names no branch (I6), so its branches are a subset of that population.

### The offline queue

`<git-common-dir>/gov-queue.log`, one TAB line per queued write: `ref`, the cached tip, the commit,
`queued-utc`. `write_gov_queue` reads it after every read that reached the remote and pushes each line
through `write_gov_ref`, oldest first; rc 0 removes the line, rc 1 removes it with `yield`, rc 2 keeps
it. `add_gov_queue` and `write_gov_queue` are the functions every later compare-and-swap writer of this
build calls when its read fails.

### Inventory

| Minted | Kind | Lexicon cell |
|---|---|---|
| `derive_lease_ref` | shell function | `derive`, OK |
| `check_lease_segment` | shell function | `check`, OK |
| `resolve_fleet_tag` | shell function | `resolve`, OK |
| `read_lease_policy` | shell function | `read`, OK |
| `run_lease_verb`, the verb's body, `write_lease` being the run-state lease's (`:7979`) | shell function | `run`, OK |
| `add_gov_queue`, `write_gov_queue` | shell functions | `add` and `write`, OK |
| `--lease`, `--lease flush` | driver verbs | none |
| `--fleet-tag` | render_playbook.py flag | none |
| `gov-queue.log` | node-local file | none |
| `lease-yielded` | health event | none |
| `lease` | `CLAIM_MODES` member | graded by leg check 52 |
| `withdrawn` | claim status value | none |

### Migration

Lazy and additive (§8 F3): the reader reads both namespaces and the first write moves a slug onto its
lease, parented on the legacy tip. No ref is deleted. The suite's `refs/gov/runs` fixtures move to the
lease ref with the tests that assert a write's position.

### Rollout

Dark behind `RUN_CLAIMS`, as today. This repository's conf has it `on` (`.unattended.conf:162`), so
its runs move onto build leases at their next claim write; an adopter's stay untouched until it opts in.

### Files touched (estimate)

- `tools/unattended/unattended.sh`: the grammar, the reader's two namespaces and new fields, the
  epoch, the `lease` mode, the verbs, the four keys' reads, the overlap reduction, the offline queue,
  the fleet tag, `KIT_UNATTENDED_VERSION` moved
- `tools/unattended/lib-unattended.sh`: `resolve_fleet_tag` beside `resolve_index_generator` (`:188`),
  through the same `resolve_kit_dir` call
- `tools/unattended/unattended.test.sh`: the lease arms, and the claim fixtures moved to the lease ref
- `tools/unattended/STOPS.template.md`: section 7
- `memory/guides/UNATTENDED-STOPS.md`: its render
- `tools/playbook/render_playbook.py`: the `--fleet-tag` flag over `read_fleet`
- `skills/session-kickoff/manifest-check.sh`: the `claims —` cell (`:630-655`) reads a lease name in
  field 1, unchanged in shape
- `tools/govkit/subject-pins.tsv`, regenerated by `python tools/govkit/govkit.py selfcheck --write`

### Alternatives rejected

- **A `[[upgrade]]` step that copies every run claim at once** (dSafePassage-1 S1). A step's `down`
  would have to delete leases, which `TOOL-dPlacedRequest-16` forbids, and the lazy read needs none.
- **The fleet tag parsed from `fleet.toml` in shell.** `read_fleet` is the file's one reader and
  grades every row; a second parser is a second grammar.
- **A `writes` key in the record for the overlap.** I6 fixes the keys, and the probe already derives
  each branch's write set from its specs' Files touched (`:3458`).

## 5. Production-readiness checklist

- security — every write is a compare-and-swap on the tip read, so no stale reader overwrites; the
  record names a fleet tag and a session, never a credential; a node outside the fleet writes nothing.
- perf / scale — one bounded fetch of two namespaces and one `awk` pass per read, as today; one
  `policy.py get` per key per process.
- error / empty / loading states — a refusal names one cause and the holder; an unanswered read
  follows `leases.offline`; an unreadable key prints a NOTE and its default.
- observability — every verb prints one line naming the tail, the act and the epoch; a take-over and a
  yield each append a health event.
- risks — under `progress`, a run lease renews only on a recorded transition, and nothing records one
  automatically until dWellOiledMachine lands; once `TOOL-dPlacedRequest-17` judges expiry, a run past
  `leases.expiry-hours` with no transition reads stale (§8 F5).
- testing — the probes of §6, and the suite arms of §7.
- migration — lazy, per slug, at its next write.
- user docs — `memory/guides/UNATTENDED-STOPS.md` section 7; no `help/` page covers the unattended kit.

## 6. Acceptance criteria

- **AC1** — When `bash unattended.sh --lease acquire build tFix`, `--lease acquire unit tFix
  TOOL-tFix-2` and `--lease acquire run maintain 2026-10` run in a fixture clone, the origin holds
  `refs/gov/leases/tFix/build`, `refs/gov/leases/tFix/unit/TOOL-tFix-2` and
  `refs/gov/leases/run/maintain/2026-10`, each message opening `gov-claim <tail>` with `epoch: 1`, its
  `kind` and `fleet-tag: a`; `--lease acquire build 'a b'` exits 2 and writes nothing.
  Red when: a ref is built outside `derive_lease_ref`, or an illegal segment reaches a push.
  fixture: a scratch clone with a bare origin whose `HEAD` is set, the kit's example conf with
  `RUN_CLAIMS=on`, and `USERNAME=daily-agent`.
- **AC2** — When session `s2` runs `--lease take-over build tFix` over a planted stale lease, the origin's
  lease reads `epoch: 2` and its parent is the planted tip; `--lease acquire build tFix` by `s3` then
  exits 1 printing `lease refused — live-holder`.
  Red when: a take-over keeps the epoch, or a live lease is acquired.
- **AC3** — When the fixture origin holds only a legacy `refs/gov/runs/tFix` claim and `--claims` runs,
  it prints one row for `tFix` of five fields; after the run's next holder write, the origin holds
  `refs/gov/leases/tFix/build` at `epoch: 1` whose parent is the legacy tip, the legacy ref is
  unchanged, and `--claims` still prints one row.
  Red when: both rows print, the legacy ref moves, or the lease starts a new chain.
- **AC4** — When no policy file exists and `--lease renew build tFix` runs without `--witness`, the new
  record reads `renews: no`; with `--witness` naming a commit carrying `Gov-Transition: … build=tFix`,
  it reads `renews: yes` and that `witness`; the same witness again reads `renews: no`; a witness with
  no trailer exits 2. With `leases.renewal` planted `activity`, `fixed` and `none`, a renew without a
  witness reads `yes`, `no` and `-`.
  Red when: a beat alone renews under the default `progress`, or a planted value is not read.
- **AC5** — When `leases.granularity` is planted `build`, `--lease acquire unit tFix TOOL-tFix-2` exits
  2 naming `leases.granularity`; planted `unit`, `--lease acquire build tFix` exits 2; under the default
  both write.
  Red when: a planted value admits the level it excludes.
- **AC6** — When the fixture origin holds a branch whose spec declares one script in a planted kit
  directory under the tools root (the fixture's own scratch kit name, never a tracked kit) and this
  build's spec declares a second script in that same directory, `--lease acquire build tFix` prints
  an `overlap` finding under the default `kit-dirs` and none under planted `files`; with `leases` planted `refuse` it exits 1
  printing `lease refused — overlap`; with the shared path made equal and `builds` planted, it prints
  one finding naming the branch.
  Red when: the probe returns 0 under `refuse`, or a granularity value is not applied.
- **AC7** — When the origin is renamed away and `--lease acquire build tOff` runs, under the default it
  exits 0 printing `queued`, `gov-queue.log` holds one line and `git for-each-ref refs/gov/leases`
  lists nothing new; with the origin restored, `--lease flush` creates the ref and empties the queue;
  with a conflicting write made first, it prints `yield`. Under planted `refuse` the offline acquire
  exits 1 printing `offline`; under `follow-leases`, a renew of a held lease prints `follow-leases`
  and an acquire exits 1 printing `offline`.
  Red when: an offline call writes a ref, or a queued write overwrites a conflicting one.
- **AC8** — When `USERNAME` names no `fleet.toml` row, `--lease acquire build tFix` exits 2 naming
  `fleet.toml` and the origin is unchanged; with `daily-agent`, `--claims` prints `a` in the node column.
  Red when: a node with no tag writes a lease, or the row names a user.
- **AC9** — When two clones whose caches both read no lease run `--lease acquire build tNew` one after
  the other without a fetch between, the first exits 0 and the second exits 1 printing `epoch-fence`.
  Red when: both report a create.
- **AC10** — When `grep -n 'refs/gov/leases/<slug>/build\|--lease\|leases.renewal\|epoch-fence'` runs over
  `STOPS.template.md`, each is found in section 7, and `--claims` in the AC1 fixture prints rows of
  exactly five TAB fields.
  Red when: the guide omits the grammar or the verbs, or the row shape changes.

## 7. Gates

`memory hygiene` · `spec tokens (a spec's own names resolve)` · `unattended kit gate` · `manifest-check self-test` · `scratch-guard self-test` · `playbook render selftest` · `govkit acceptance matrix` · `kit epoch (shipped bytes move, the version moves)` · `govkit selfcheck` · `lexicon naming predicates` · `recall floor` · `recall floor arms` · `routed-commits selftest` · `govkit selftest` · `govkit refusal join`

New arm: tools/unattended/unattended.test.sh · covers AC1 AC2 AC3 AC4 AC5 AC6 AC7 AC8 AC9 AC10 · the lease arms over the suite's bare origin, staged by planting each policy value and by cutting the epoch increment · `FLOOR_ASSERTIONS` and its shard floor rise by the arms' count, counted off the diff
New arm: tools/playbook/render_playbook.py · covers AC8 · the `--fleet-tag` flag's selftest case, staged by a user no row names · none

## 8. Open questions

- **FACT-QUESTION · F1 — The brief gives this spec's status header the token `DRAFT`; is that legal?**
  Probe: `STATUS_TOKENS` at `tools/memory-tree/tree_lib.py:28`. Observation, 2026-10-25: the tuple holds
  `OPEN`, `SPECCED`, `INPROGRESS`, `BLOCKED`, `DEFERRED`, `CLOSED` and `WONTDO`, and not `DRAFT`.
  Liveness: the tuple would show `DRAFT` if the vocabulary held it. RESOLVED (agent, 2026-10-25,
  delegated): `OPEN`, rung 2.
- **F2 — Does the migration retire `RUN_CLAIMS`?** I24 keeps it "until unit 1's migration retires it";
  `leases` has no off value (v2:1157). (a) Keep it as the switch every lease read and write sits
  behind; (b) retire it, leases always on. (b) lands a Tier-2 write surface live in every adopter,
  against the charter's `[small]` rule. RESOLVED (agent, 2026-10-25, delegated): (a), rung 3; retiring
  the switch is an owner's default change after the chain lands. widens: none · relaxes: none
- **F3 — How do run claims migrate?** (a) Lazily, the reader reading both namespaces and the first
  write parenting the lease on the legacy tip; (b) an `[[upgrade]]` step copying every claim. (b)'s
  `down` must delete leases, which clause 0134 forbids, so veto 1 discards it. RESOLVED (agent,
  2026-10-25, delegated): (a), rung 3. widens: none · relaxes: none
- **F4 — Which lease does a run hold under `leases.granularity: unit`?** (a) The build lease always,
  the key governing the checklists' acquisitions; (b) no build lease, so a run holds no claim. (b)
  removes the one exclusive claim section 7 exists for, and v2 names no run without a claim.
  RESOLVED (agent, 2026-10-25, delegated): (a), rung 3. widens: none · relaxes: none
- **F5 — What witnesses progress for a run lease before any caller records a transition?** (a) Only a
  `Gov-Transition` trailer, as clause 0120 and v2:1159 state; (b) also the driver's `Pass:` commits and
  phase moves. (b) renews on a witness the clause does not name, which veto 1 discards. RESOLVED
  (agent, 2026-10-25, delegated): (a), rung 1; the consequence, a long run reading stale once
  `TOOL-dPlacedRequest-17` lands, is listed in §5 and is the interim v2:1159 journals. widens: none · relaxes: none
- **F6 — What do `fixed` and `none` mean, which v2 names without defining?** RESOLVED (agent,
  2026-10-25, delegated): `fixed` renews only at acquisition, so the lease expires `leases.expiry-hours`
  after it is taken; `none` tracks no renewal and the lease never expires, ending only by release or a
  take-over the holder's own session makes; rung 3, the reading of walk C2's value names.
  widens: none · relaxes: none
- **F7 — How do the three `leases.overlap` values reduce a path?** RESOLVED (agent, 2026-10-25,
  delegated): as §4 "The overlap reduction" states, `kit-dirs` coarsest by directory and `builds`
  coarsest in its report; rung 3, from the value names and coordination item 3's "against every live
  lease at `leases.overlap`'s granularity". widens: none · relaxes: none

## 9. Revision log

- rev-1 · 2026-10-25 · initial draft, from the packet's Items 1, scout A row 1 and Shared interfaces 1,
  4 and 8, coordination.md:79-101, v2:1157-1162 and flow-steps:53-60.
- rev-2 · 2026-10-25 · fix brief, the spec stage's gate hits: AC6 describes the overlap fixture's two planted
  scripts in prose, so no untracked path reads as a repository path; §3 gains the hands-off to
  TOOL-dPlacedRequest-4 that unit's consumes-from names.
- rev-3 · 2026-10-25 · §3 · the round-1 spec audit's disposal: hands-off TOOL-dPlacedRequest-23,
  hands-off TOOL-dPlacedRequest-24, hands-off TOOL-dPlacedRequest-25, hands-off
  TOOL-dPlacedRequest-26, hands-off TOOL-dPlacedRequest-29, hands-off TOOL-dPlacedRequest-32,
  hands-off TOOL-dPlacedRequest-34, each the mirror of that promoted unit's own edge.

## 10. Reuse audit

The seam extended is the run-claim block, `tools/unattended/unattended.sh:2070-2462`: `read_claims`
(`:2118`) stays the one reader, `check_claim_writable`'s table (`:2243`, its axes at `:2219-2220`)
gains the `lease` column, and writes go through `TOOL-dPlacedRequest-11`'s `write_gov_ref`. The
overlap is `check_cross_run_overlap` (`:3409`) with its return wired to `leases`; the fleet tag is the
playbook kit's `read_fleet` (`tools/playbook/render_playbook.py:347`) over `tools/playbook/fleet.toml`,
reached through `resolve_kit_dir` as `resolve_index_generator` reaches the memory-tree kit
(`tools/unattended/lib-unattended.sh:188-197`). `python tools/codebase-map/reuse_lookup.py "lease a
build or unit on the remote with an epoch and take over"` ranked `build_commit`, `units`,
`build_fixture` and `resolveLease` (`tools/unattended/run-lease.js`, the run-state lease, which
lives on the run's own branch and is what the claim exists to complement); none writes a remote ref,
so the claim block above is the seam. Scout A's row 1 holds against source, with one correction: the
dispatch line for `--claims` is `:14489`, not `:14490`. `python tools/memory-recall/query.py "how are
run claims written and how would they migrate to leases"` returned scout A's rows 1 and 6, the brief's
unit rows and coordination.md:54; none disagrees with source.

Recall terms used: lease epoch take-over refs/gov/leases run claim migrate fleet tag overlap offline renewal progress
