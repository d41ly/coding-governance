# TOOL-dTendedCadence-14 — reading bands: log, diagnose read-only or act, by a reading's deviation from its pin

**Status:** OPEN · rev-1 · 2026-11-01 · node a · Tier-2 · base f4597719 · streams tooling · order 5 · advances TOOL-dTendedCadence-19

**Carries:** cl-dClosedLoop-0455@238dcec0 whole
**Carries:** node:policy-key.maintain.tiers

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-11-01-build-TOOL-dTendedCadence-1-agent-ledger.md](../build/2026-11-01-build-TOOL-dTendedCadence-1-agent-ledger.md) | journal | TOOL-dTendedCadence-1 TOOL-dTendedCadence-2 TOOL-dTendedCadence-3 TOOL-dTendedCadence-4 TOOL-dTendedCadence-5 TOOL-dTendedCadence-6 TOOL-dTendedCadence-7 TOOL-dTendedCadence-8 TOOL-dTendedCadence-9 TOOL-dTendedCadence-10 TOOL-dTendedCadence-11 TOOL-dTendedCadence-12 TOOL-dTendedCadence-13 TOOL-dTendedCadence-15 TOOL-dTendedCadence-16 TOOL-dTendedCadence-17 TOOL-dTendedCadence-18 TOOL-dTendedCadence-35 TOOL-dTendedCadence-36 TOOL-dTendedCadence-37 TOOL-dTendedCadence-38 TOOL-dTendedCadence-39 TOOL-dTendedCadence-40 TOOL-dTendedCadence-41 TOOL-dTendedCadence-42 TOOL-dTendedCadence-43 TOOL-dTendedCadence-44 TOOL-dTendedCadence-45 TOOL-dTendedCadence-46 TOOL-dTendedCadence-47 TOOL-dTendedCadence-48 TOOL-dTendedCadence-49 TOOL-dTendedCadence-50 TOOL-dTendedCadence-51 TOOL-dTendedCadence-52 TOOL-dTendedCadence-53 TOOL-dTendedCadence-54 TOOL-dTendedCadence-55 TOOL-dTendedCadence-56 TOOL-dTendedCadence-57 TOOL-dTendedCadence-58 TOOL-dTendedCadence-59 |
| [2026-11-01-build-TOOL-dTendedCadence-1-spec-stage-returns.md](../build/2026-11-01-build-TOOL-dTendedCadence-1-spec-stage-returns.md) | research | TOOL-dTendedCadence-1 TOOL-dTendedCadence-2 TOOL-dTendedCadence-3 TOOL-dTendedCadence-4 TOOL-dTendedCadence-5 TOOL-dTendedCadence-6 TOOL-dTendedCadence-7 TOOL-dTendedCadence-8 TOOL-dTendedCadence-9 TOOL-dTendedCadence-10 TOOL-dTendedCadence-11 TOOL-dTendedCadence-12 TOOL-dTendedCadence-13 TOOL-dTendedCadence-15 TOOL-dTendedCadence-16 TOOL-dTendedCadence-17 TOOL-dTendedCadence-18 |
| [2026-11-01-build-TOOL-dTendedCadence-4-reuse-scout-b.md](../build/2026-11-01-build-TOOL-dTendedCadence-4-reuse-scout-b.md) | research | TOOL-dTendedCadence-4 TOOL-dTendedCadence-15 TOOL-dTendedCadence-16 |
| [2026-11-01-prompt-TOOL-dTendedCadence-1-fix-brief.md](../prompts/2026-11-01-prompt-TOOL-dTendedCadence-1-fix-brief.md) | research | TOOL-dTendedCadence-1 TOOL-dTendedCadence-2 TOOL-dTendedCadence-3 TOOL-dTendedCadence-4 TOOL-dTendedCadence-5 TOOL-dTendedCadence-6 TOOL-dTendedCadence-7 TOOL-dTendedCadence-8 TOOL-dTendedCadence-9 TOOL-dTendedCadence-10 TOOL-dTendedCadence-11 TOOL-dTendedCadence-12 TOOL-dTendedCadence-13 TOOL-dTendedCadence-15 TOOL-dTendedCadence-16 TOOL-dTendedCadence-17 TOOL-dTendedCadence-18 |
| [2026-11-01-prompt-TOOL-dTendedCadence-1-spec-brief.md](../prompts/2026-11-01-prompt-TOOL-dTendedCadence-1-spec-brief.md) | research | TOOL-dTendedCadence-1 TOOL-dTendedCadence-2 TOOL-dTendedCadence-3 TOOL-dTendedCadence-4 TOOL-dTendedCadence-5 TOOL-dTendedCadence-6 TOOL-dTendedCadence-7 TOOL-dTendedCadence-8 TOOL-dTendedCadence-9 TOOL-dTendedCadence-10 TOOL-dTendedCadence-11 TOOL-dTendedCadence-12 TOOL-dTendedCadence-13 TOOL-dTendedCadence-15 TOOL-dTendedCadence-16 TOOL-dTendedCadence-17 TOOL-dTendedCadence-18 |
| [2026-11-01-review-TOOL-dTendedCadence-1-to-18-spec-audit-round1.md](../reviews/2026-11-01-review-TOOL-dTendedCadence-1-to-18-spec-audit-round1.md) | spec-audit | TOOL-dTendedCadence-1 TOOL-dTendedCadence-10 TOOL-dTendedCadence-11 TOOL-dTendedCadence-12 TOOL-dTendedCadence-13 TOOL-dTendedCadence-15 TOOL-dTendedCadence-16 TOOL-dTendedCadence-17 TOOL-dTendedCadence-18 TOOL-dTendedCadence-2 TOOL-dTendedCadence-3 TOOL-dTendedCadence-4 TOOL-dTendedCadence-5 TOOL-dTendedCadence-6 TOOL-dTendedCadence-7 TOOL-dTendedCadence-8 TOOL-dTendedCadence-9 |

<!-- /gen:spec-records -->

## 1. Goal

A reading over its pin gets one response whatever its size: the engine prints `OVER PIN` or
`over pin (report only)` and nothing else (`tools/drift-audit/drift_report.py:4427-4438`), so a reading
one past its pin and one far past it are the same event (gap-maint-13). This unit tiers each reading
under `maintain.tiers: bands` by its deviation from its pin, against band edges the reading declares
beside its pin at registration: the log band a journal line and a count in the maintenance record with
nothing filed, the diagnose band a read-only probe through `probe.trigger` with the reading as its
observation, its record attached to the ask `maintain.file` files, and the act band routed by its fix
within `maintain.fixes`; `pins` keeps one severity per pin (NP-21, the owner's FK-5-5).

## 2. Scope (IN)

Build-run preconditions: TOOL-dTendedCadence-8 (the `[[reading]]` rows, I3, and their `fix` field) and
TOOL-dTendedCadence-4 (`check_reading_admission` and `read_policy_value`, in `drift_report.py`);
TOOL-dPlacedRequest-7 S3 and TOOL-dPlacedRequest-19 S1 for the diagnose band, with this spec's §8 F3
ask of dPlacedRequest (ask TOOL-dTendedCadence-23).

- **S1** — The edges, I8 as this unit settles it (§8 F1): an `edges = [<e1>, <e2>]` field on the
  reading's `[[reading]]` row, two non-negative integers with `e1 <= e2`, beside the row's `pin`. With
  `d` the reading's deviation, `value - pin`, or for a reading bounded by an id set the count of its
  `new` and `stale` ids (`drift_report.py:4339-4343`): `in-pin` for `d <= 0`, `log` for `0 < d <= e1`,
  `diagnose` for `e1 < d <= e2`, `act` for `d > e2`. Observed by AC1, AC2, AC3 and AC4.
- **S2** — The refusal. Under `maintain.tiers: bands`, `check_reading_admission` (TOOL-dTendedCadence-4
  S3) gives a row with no `edges`, or an `edges` that is not two non-negative integers in order, the
  verdict `refused` with the reason `no band edges` or `band edges <value> are not two ordered
  non-negative integers`, whatever `maintain.reading-admission` says, since an edge is not an
  ownership question. Under `pins` the field is neither required nor read. Observed by AC5.
- **S3** — The band, `derive_reading_band(record, edges, tiers)` in `tools/drift-audit/drift_report.py`,
  run in `main` after admission, so every record gains `band` beside `pin`, `owner` and `admission`:
  - under `bands`, S1's band; under `pins`, `act` for a record over its pin and `in-pin` otherwise, the
    one severity per pin as before;
  - a record whose `admission` is not `admitted` takes `log`, so an unowned reading is reported and
    nothing is filed for it (TOOL-dTendedCadence-4 S4);
  - a record not live takes `log`, and one not asked takes `in-pin`; TOOL-dTendedCadence-18 gives a
    record dead past `maintain.dead-after` readings the band `dead`.

  The table's status gains ` · band <band>` for a live record over its pin, and `--json` carries the
  field. `tiers` is read once per run as `read_policy_value("maintain.tiers", root)`. Observed by AC1 to AC6.
- **S4** — The log band, I9 as this unit settles it (§8 F2): its journal line is the reading's
  drift-history row (`HISTORY_COLUMNS`, `drift_report.py:3758`), which already carries the sha, the
  value, the denominator and `key_hash`; the band is derived from that row and the registration and is
  stored nowhere. Its count is the number of `log` records the run read, which the Maintain walk counts
  for the maintenance record's `log-band:` field (TOOL-dTendedCadence-1 S4; I10, TOOL-dTendedCadence-6).
  Nothing is filed for it. Observed by AC1.
- **S5** — The diagnose band, `run_band_probe(record, offender_key, root=".")` in `drift_report.py`,
  called only by the Maintain walk and by no mode of the report. It derives the content key of
  `<reading>\t<offender key>` with `python <loop kit>/request.py key <file>` (TOOL-dPlacedRequest-19
  S1), and runs as a bounded subprocess `python <loop kit>/probe.py trigger --cause observation --asker
  item.maintain.read --subject "<reading> <value> of <of>, pin <pin>, band diagnose" --request <content
  key>` (TOOL-dPlacedRequest-7 S3), the loop kit found through the inline `resolve_kit_dir`. It applies
  no fix and changes no tracked file: the probe is read-only, as the clause says. It returns the content
  key and the record path `probe.py` prints on `probe — opened · <record>` or `probe — joined ·
  <record>`, which the walk hands to `maintain.file` for the ask's `data probe` clause
  (TOOL-dTendedCadence-15 S2); `probe — not opened · <key>: <why>` returns no record and the walk files
  the ask without one. Observed by AC2.
- **S6** — The act band. A record in `act` keeps its route by the row's `fix`, which the Maintain walk
  takes (TOOL-dTendedCadence-1 S4, TOOL-dTendedCadence-3): `maintain.direct` or `maintain.patch` for a
  fix inside `maintain.fixes`, `maintain.file` for none. This unit adds no route. Observed by AC3.
- **S7** — The edges at landing (§8 F4): every `[[reading]]` row in gov's descriptors gains
  `edges = [0, 0]`, so under the default `bands` each reading over its pin acts exactly as today, and
  admission refuses none. Observed by AC7.
- **S8** — The policy read and the row. `read_policy_value("maintain.tiers", root)`, TOOL-dTendedCadence-4
  S6's adapter; its `PolicyRefused` reads `pins`, the behaviour before this unit,
  printed once. The catalogue row `maintain.tiers` (`tools/policy/catalogue.toml:1181-1185`) gains its
  `summary` and `usage`, its values and default unchanged, and `policy.py lists --write` drains its name
  from `tools/policy/unsummarised-keys.txt:123`. Observed by AC8.
- **S9** — The docs: `help/maintain.md` gains a section "Bands" naming both values of the key, the
  `edges` field, the four bands and what each does; the drift-audit README's status vocabulary gains
  the band suffix. Observed by AC9.

## 3. Non-goals (OUT)

- Rolling baselines: NP-21's bands measure deviation from the pin, and rolling baselines "were not
  asked, and stay out" (night-pass-instruments:3440-3441).
- The routes of the act band and the walk that applies them: TOOL-dTendedCadence-1 and
  TOOL-dTendedCadence-3.
- Filing the ask and attaching the probe record: TOOL-dTendedCadence-15 S2.
- The `log-band:` field and the record's writer: TOOL-dTendedCadence-6 (I10).
- The probe program, its pin, design and judge items: TOOL-dPlacedRequest-7.
- Choosing gov's edges per reading: S7 seeds the one value that changes no response; an owner widens a
  row's edges in its own commit.

### Edges

- **consumes-from** `TOOL-dTendedCadence-8` — `[[reading]]`, the row S1 adds `edges` to and whose `fix` the act band keeps
- **consumes-from** `TOOL-dTendedCadence-4` — `check_reading_admission`, which S2 extends with the edgeless refusal, the `unowned` verdict S3 sends down the log band, and `read_policy_value`
- **hands-off** `TOOL-dTendedCadence-15` — `edges`, through which each breach's band is derived; the band and the diagnose band's probe record go to the ask `maintain.file` files
- **hands-off** `TOOL-dTendedCadence-1` — `edges`, the band S3 derives, which the walk routes each reading by, counts for the record's log band and calls the diagnose probe for
- **consumes-from** external — TOOL-dPlacedRequest-7 S3 (`probe.py trigger`) with the §8 F3 ask, and TOOL-dPlacedRequest-19 S1 (`request.py key`), specced and unbuilt at base

## 4. Design

### Evidence

At this base the engine judges a record against its pin once: `OVER PIN <pin> — gateable` or
`over pin <pin> (report only)` (`drift_report.py:4427-4438`), and `--check` reds a gateable record
whose value exceeds its pin (`:4364-4365`). Nothing measures how far. `key_hash`, the offender-set
digest the log line needs, already exists (`:3761-3780`), and the history row it sits in carries the
sha, value and denominator (`:3758`). The design routes `maintain.read` by band and refuses at
admission a reading with no edges under `bands` (layer-expansions:223).

### Bands

```
d = value - pin            (an id-set reading: len(new) + len(stale))
d <= 0         in-pin      nothing
0 < d <= e1    log         the history row; counted for the record; nothing filed
e1 < d <= e2   diagnose    run_band_probe -> probe.py trigger --cause observation; the ask carries its record
d > e2         act         routed by the row's fix, within maintain.fixes
```

Under `pins` the table is two rows: `d <= 0` in-pin, `d > 0` act.

### The two interface refinements

I8 was proposed as a column on the `drift-pins.txt` row. The ledger row grammar carries a positive
integer count (TOOL-dWitnessedBar-13 §4 "The ledger file"), so a reading at pin 0, 14 of the 27 at
this base, has no row to carry edges (TOOL-dTendedCadence-34, the ask of dWitnessedBar); §8 F1 puts them on the `[[reading]]` row, the registration the
clause names, beside the row's `pin`. I9 was proposed as an `ev=reading` journal line. Runlog's journal admits only
`start`, `end` and `once` events (`tools/runlog/runlog_lib.py:34`), Runtime's writer only its closed
`JOURNAL_CLASSES` (TOOL-dWellOiledMachine-16 S3), and adding a column to drift's history makes every
node's existing file unreadable, since its reader refuses a header lacking a column it requires
(`drift_report.py:3842-3843`); §8 F2 takes the history row as it stands.

### Inventory

Names this unit mints, each asked of `lexicon.py --suggest <name> --as py.function` at this base and
answered OK: `derive_reading_band`, `run_band_probe`. Row field: `edges`. Record field: `band`. Band
values: `in-pin`, `log`, `diagnose`, `act`.

### Files touched (estimate)

- `tools/drift-audit/drift_report.py`
- `tools/drift-audit/kit.toml` (S7's `edges` on its `[[reading]]` rows)
- `tools/drift-audit/selftest.py`
- `tools/drift-audit/README.md`
- `tools/policy/catalogue.toml`
- `tools/policy/unsummarised-keys.txt` (rendered by `policy.py lists --write`)
- `help/maintain.md`

### Alternatives rejected

- **Edges on the `drift-pins.txt` row.** Rejected by §8 F1's probe: a pin of 0 has no row.
- **A second dict of edges beside the pins.** Rejected: the spec brief's settled 2 puts the pin on one
  home and nothing beside it, and a dict keyed by signal duplicates the registration's key.
- **A `band` column in drift's history.** Rejected by §8 F2's test: the reader refuses an old header
  missing it, so every node's history would read as absent until hand-migrated.
- **Bands relative to the pin as a percentage.** Rejected: a pin of 0, the common case, has no
  percentage, and the design states edges in the reading's own units.

## 5. Production-readiness checklist

- security — the diagnose probe runs `probe.py trigger` with arguments the engine builds from a record;
  the subject is passed as one argv element, never through a shell, and the probe writes only its own
  record (TOOL-dPlacedRequest-7 S3, S7).
- perf / scale — one comparison per record; one bounded subprocess pair per diagnose-band offender,
  only inside the Maintain walk.
- error / empty / loading states — no edges under `bands`: refused at admission; no policy kit: `pins`;
  no loop kit or a probe that does not open: the ask is filed without a probe record, the line naming
  why.
- observability — the `band` field, the status suffix, the history row and the probe's own record.
- risks — an owner who widens edges stops a reading from filing until it passes `e1`; that is the band's
  purpose, and the log count in the record keeps it visible.
- testing — §7's New arm line; the fixture of §6.
- migration — S7: `edges = [0, 0]` on every gov row, so the landing moves no response.
- user docs — `help/maintain.md` (S9).

## 6. Acceptance criteria

The bands fixture is a clone of this repository at the build commit under `%TEMP%/bnd`, its remote
removed so the policy reader reads the local default branch, with the `[[reading]]` row of
`live_builds_without_activity` carrying `edges = [1, 3]`, the pins carrying
`live_builds_without_activity: 2`, and `memory/LIVE.md` holding a table with an `Activity` column whose
`dormant` rows the reading counts (`drift_report.py:3492-3514`), each case committing its own count on
the default branch. Each command runs with the fixture as its working directory and `tools/drift-audit/`
as the path to the engine.

- **AC1** — When `memory/LIVE.md` holds 3 dormant rows, `python drift_report.py --json` gives the record
  `"band": "log"`, and the history row `python drift_report.py --check` appends for it carries value 3.
  Red when: a reading one past its pin is filed or acts, or carries no band.
  cost: a full report over this repository, under the `drift-audit records` leg's 540 s ceiling
  (PINNED, `tools/gate-legs.json:1067`).
- **AC2** — When it holds 5, the record reads `"band": "diagnose"`, and `run_band_probe` called on its
  first offender key, by a `python -c` probe importing `drift_report` from the fixture's kit, prints
  `probe — opened` from `probe.py trigger` and returns that record's path and its content key, with
  `git status --porcelain` empty afterwards.
  Red when: the diagnose reading opens no probe, or the probe changes a tracked file.
  fixture: needs TOOL-dPlacedRequest-7 and -19 built and §8 F3's ask landed.
- **AC3** — When it holds 6, the record reads `"band": "act"`.
  Red when: a reading past `e2` reads any other band.
- **AC4** — When it holds 2, the record reads `"band": "in-pin"`.
  Red when: a reading at its pin reads a breach band.
- **AC5** — When the row's `edges` is removed, `python drift_report.py --check` exits 1 printing
  `reading admission refused — live_builds_without_activity: no band edges`; with
  `.governance/policy.toml` committed with `maintain.tiers = "pins"`, it is admitted and 3 dormant rows
  read `"band": "act"`.
  Red when: an edgeless reading is admitted under `maintain.tiers: bands`, or refused under `pins`.
- **AC6** — When the row's `kind` names no registry row, `maintain.reading-admission = "report-unowned"`
  is set and the table holds 6, the record reads `"admission": "unowned"` and `"band": "log"`.
  Red when: an unowned reading reads a band that files.
- **AC7** — When `python drift_report.py --check` runs in a clone of the build commit with nothing
  planted, it prints no `no band edges` line, and every `[[reading]]` row of
  `tools/drift-audit/kit.toml` carries an `edges` field.
  Red when: a reading registered at the tip is refused for its edges.
- **AC8** — When `grep -n 'read_policy_value("maintain.tiers"' drift_report.py` runs in
  `tools/drift-audit/`, it finds the reader; `grep -c "^maintain.tiers$" unsummarised-keys.txt` in
  `tools/policy/` prints 0; and with `tools/policy/` removed from the fixture's commit and 3 dormant rows,
  the record reads `"band": "act"` and the report prints `maintain.tiers takes pins` once.
  Red when: the key has no literal reader, its summary is missing, or a kit-less read takes bands.
- **AC9** — When `grep -n "Bands\|maintain.tiers: bands\|edges" maintain.md` runs in `help/`, each
  matches.
  Red when: the page omits the section, the key or the field.

## 7. Gates

`drift-audit records` · `drift-audit selftest` · `policy fixtures` · `memory hygiene`

New arm: tools/drift-audit/selftest.py · covers AC1 AC3 AC4 AC5 AC6 · its bands fixture, one planted reading per band, an edgeless row under each value of `maintain.tiers` and an unowned reading over its edges, staged against an engine that derives no band · none

## 8. Open questions

- **FACT-QUESTION · F1 — Where do a reading's band edges live?** Options: (a) an `edges` field on the
  `[[reading]]` row beside its `pin`; (b) a fifth field on the reading's `drift-pins.txt` row, as I8 was
  proposed. Probe: the ledger row grammar in TOOL-dWitnessedBar-13 §4 "The ledger file" ("then a positive
  integer count") against the readings whose pin is 0 in §4 of TOOL-dTendedCadence-4. Observed: the
  grammar admits no count of 0, and 14 of the 27 readings carry pin 0 at this base, with up to five more
  after that unit's S5, so under (b) they have no row to hold edges and admission would refuse every
  one under the default. Liveness: a grammar admitting 0, or no reading at pin 0, makes (b) feasible. RESOLVED (agent, 2026-11-01, delegated): (a), which is also
  the clause's own "beside its pin at registration". widens: none · relaxes: none
- **FACT-QUESTION · F2 — What is the log band's journal line?** Options: (a) the reading's drift-history
  row as it stands, the band derived; (b) a `band` column added to that row; (c) a Runtime journal line
  through `write_journal_line`. Probe: `read_history_groups` (`drift_report.py:3842-3843`) refuses a
  file whose header lacks any of `HISTORY_COLUMNS`, and TOOL-dWellOiledMachine-16 S3's `JOURNAL_CLASSES`
  holds no class for a reading. Observed: (b) makes every node's existing history unreadable, and (c)
  needs a class that parent does not spec, an ask of dWellOiledMachine for a value (a) already records.
  Liveness: a reader that admitted an optional column, or a reading class in that tuple, would leave (b)
  or (c) standing. RESOLVED (agent, 2026-11-01, delegated): (a). widens: none · relaxes: none
- **F3 — `probe.py trigger` takes `--build <slug>` or `--request <content key>`
  (TOOL-dPlacedRequest-7 S3), and a Maintain run is neither.** This is ask TOOL-dTendedCadence-23, filed by
  the main loop for dPlacedRequest: `probe.py trigger` takes a cadence target, the content key of
  (reading, offender key). Accept line: `probe.py trigger --cause observation --asker item.maintain.read
  --request <content key>` opens a probe for a key no request file names, its records under
  `<git-common-dir>/requests/` as S7's entry-time probe keeps them. Options for this unit: (a) S5 as
  written, against the ask; (b) the diagnose band files the ask with no probe. (b) fails the clause's
  diagnose case. Rung 3, the build-run precondition S5 states. RESOLVED (agent, 2026-11-01, delegated):
  (a), with ask TOOL-dTendedCadence-23. widens: none · relaxes: none
- **F4 — Which edges does every gov reading carry at landing?** (a) `[0, 0]` on every row, which
  routes every reading over its pin to act, as today; (b) edges computed from each pin, a share of it;
  (c) no edges, with gov's policy file setting `pins`. (b) types numbers no measurement backs, and (c)
  turns the key off in the one tree that dogfoods it. Rung 3, the survivor that moves no response at
  landing and leaves no number to justify. RESOLVED (agent, 2026-11-01, delegated): (a).
  widens: none · relaxes: none

## 9. Revision log

- rev-1 · 2026-11-01 · initial draft.

## 10. Reuse audit

The seams extended: the engine's record join, where the pin is derived and TOOL-dTendedCadence-4's
verdict is added (`drift_report.py:4319-4337`); the id-set judgement's `new` and `stale` lists
(`:4339-4343`); the history row and its `key_hash` (`:3758-3780`), taken as the log line unchanged; the
inline `resolve_kit_dir` block (`:55-56`) to reach the loop kit; and the probe verb and content key of
TOOL-dPlacedRequest-7 S3 and -19 S1, called rather than re-specced. The probe `python
tools/codebase-map/reuse_lookup.py "tier a reading's response by how far its value deviates from its
pin"` returned name stems only (`read`, `read_text`, `read_conf`, `read_journal`), none of them a
deviation band, so no existing seam fits the band derivation itself and it is new over the seams above.
Where scout B's record disagrees with source at this base: it places the status lines at `:4404-4417`
(they are `:4427-4438`), and proposes the edges on the pins row and the journal line as `ev=reading`,
which §8 F1 and F2 show source does not admit; its `:3761-3780` and `catalogue.toml:1182` hold.

Recall terms used: `python tools/memory-recall/query.py "how is a reading's breach tiered by its
deviation from its pin into log diagnose and act bands" --terms "maintain.tiers bands pins deviation
edges log diagnose act probe.trigger observation key_hash journal"`
