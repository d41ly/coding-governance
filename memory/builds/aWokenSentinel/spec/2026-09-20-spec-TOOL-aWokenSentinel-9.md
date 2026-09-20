# TOOL-aWokenSentinel-9 — the stop-guard listing as a FIELD on `--status`'s one line, and the one-line promise made an arm

**Status:** SPECCED · rev-1 · 2026-09-20 · node a · Tier-2 · base 12b3701d · streams tooling · order 14

<!-- gen:spec-records -->

*No record names this unit.*

<!-- /gen:spec-records -->

## 1. Goal

Close audit finding H1 (round 1, raw ids 1, 21, 30 and 44): `TOOL-aWokenSentinel-7` S4 had
`verb_status` print an unconditional second stdout line, which survives the suite's whole-output
reader `sed 's/.*· next //'` at `tools/unattended/unattended.test.sh:1874` and reds that arm on
every fixture, and contradicts both the driver header's `--status <slug>  # one line` at
`tools/unattended/unattended.sh:8` and `TOOL-aWokenSentinel-5` F1, which measured the same arm and
chose a field. This unit takes spec 5's shape: the recorded keepalive id and what the newest
stop-guard line says about it become one FIELD on the existing status line, omitted when nothing
was recorded, and the header's one-line promise becomes an arm so the next unit that grows a
second line reds instead of drifting.

## 2. Scope (IN)

- **S1** — `verb_status` appends, beside the `parked`, `noted` and `resume-tick` fields and on
  their omit-at-nothing rule, ` · keepalive <kid> <present|absent> in the harness listing at
  <utc>` when `read_stop_listing` (unit 7's helper) prints a line for the slug AND the record's
  `keepalive` fact is non-empty; nothing is appended otherwise. `present` and `absent` come from
  the same `grep -qF` unit 7's `--landed` uses. `--status` reads the newest line whatever its
  phase, because it reports and does not judge. Observed by AC1 and AC2.
- **S2** — The one-line promise is an arm: `run --status tRun | wc -l` prints `1` on a fixture
  whose sidecar, resume log and parked region are all populated, so every field that can print
  prints on the same line. Observed by AC3.
- **S3** — The `--status` entry of `tools/unattended/VERBS.template.md` names the field, and its
  render `memory/guides/UNATTENDED-VERBS.md` is re-made in the same commit. Observed by AC4.
- **S4** — The arms: the three fixtures of unit 7's AC1, AC3 and AC4 read through `--status` for
  `present`, `absent` and the omitted field, plus the fourth fixture — a stop line present and the
  record's `keepalive` line deleted — for the omitted field, which is the `none` arm the audit's
  L6 (raw 15) asked for in field form; each observed RED first against a driver copy with the
  field's line removed. Observed by AC1, AC2 and AC3.

## 3. Non-goals (OUT)

- **No change to `--landed`.** Unit 7's read, refusals and helper are consumed, never edited.
- **No change to the existing fields.** `parked`, `noted`, `STALE briefs` and unit 5's
  `resume-tick` field keep their spelling and order; this field is appended after them.
- **No `--resume` change.** `--resume` prints through `verb_status`, so it inherits the field, and
  the status-and-resume agreement arm at `unattended.test.sh:1028` keeps holding by construction.
- **No second line, ever.** The arm of S2 is the rule; a future field joins the line or does not
  print.

### Edges

- **consumes-from** `TOOL-aWokenSentinel-7` — `read_stop_listing` and its three fields, and the
  `grep -qF` id match. Without the helper this unit has nothing to print; unit 7 S4 is retired at
  its rev-2 and prints no line.
- **consumes-from** `TOOL-aWokenSentinel-5` — the field rule at `verb_status`: appended to
  `parked`, omitted at nothing, and the `resume-tick` field that precedes this one.
- **consumes-from** `TOOL-aWokenSentinel-3` — the sidecar line whose `session_crons` value and
  `utc` the field reports.
- **hands-off** external — nothing.

## 4. Design

### The field

In `verb_status`, after unit 5's `resume-tick` clause and before the line prints:

```
if listing=$(read_stop_listing "$slug") && [ -n "$kid" ]; then
  # utc · phase · session_crons — the helper's three fields, the listing last
  ...; parked="$parked · keepalive $kid $presence in the harness listing at $utc"
fi
```

where `kid=$(fact "$rel" keepalive)` is read once and `presence` is `present` when the listing
contains `$kid` under `grep -qF`, else `absent`. An empty `kid` or a helper that prints nothing
appends nothing, which is the `none` arm: a status line with nothing recorded is byte-identical to
what it printed before this unit, exactly as unit 5's field promises for the resume log.

The word order — id first, presence second, the utc last — reads as a sentence on the line
(`keepalive k1 absent in the harness listing at 2026-09-16T12:00:00Z`) and keeps ` · ` as the only
field separator, so the suite's `sed 's/.*· next //'` reader and the `grep -c 'next '` reader at
`:1859` are untouched: the `next` field stays last and this field sits before it, on the same
line, as `parked` and `noted` do.

### The one-line arm

One arm in region two of the driver suite, on a fixture where every optional field is populated —
a parked row, a resume log of one line, a stop line naming the id — asserts
`$(run --status tRun | wc -l)` is `1`. It is the header's comment at `unattended.sh:8` turned into
a check; a second stdout line from any future unit reds it by name.

### The carriers

| carrier | edit | render, same commit |
|---|---|---|
| `tools/unattended/VERBS.template.md`, the `--status` entry | the field, its omission rule, and that the line stays one line | `memory/guides/UNATTENDED-VERBS.md` |
| `tools/unattended/unattended.sh:8` header line | unchanged — `# one line` is now true and armed | none |

Unit 7's carrier table at its rev-2 names the `--landed` entry only; the `--status` entry is this
unit's, so no entry is edited twice.

### Inventory

| identifier | kind | cell |
|---|---|---|
| ` · keepalive <kid> <present\|absent> in the harness listing at <utc>` | status field | no cell; grammar above |

No function, key, verb or file is minted; the helper is unit 7's.

### Files touched (estimate)

| file | change |
|---|---|
| `tools/unattended/unattended.sh` | the field clause in `verb_status` |
| `tools/unattended/unattended.test.sh` | the four field fixtures and the one-line arm, region two |
| `tools/unattended/VERBS.template.md` · `memory/guides/UNATTENDED-VERBS.md` | the `--status` entry |

### Alternatives rejected

- **Keep unit 7's second line and re-point the `:1874` arm at `head -1`.** It edits a control arm
  to admit the defect it was measuring, breaks the header's promise, and leaves every future
  whole-output reader to learn the exception.
- **Print the field when `kid` is empty as `keepalive none`.** A field that prints on every run
  grows every existing status line, which is the byte-change unit 5 F1 refused for its own field.

## 5. Production-readiness checklist

- security — N/A; the verb reads a sidecar line and a fact and prints.
- perf / scale — one helper call per `--status` and per `--resume`; nothing measurable.
- error / empty / loading states — no sidecar, an empty sidecar or no `keepalive` fact print
  nothing; an unreadable phase does not matter here, because `--status` reports the listing and
  not the phase.
- observability — the line names the id, the presence and the utc; the operator sees the reap's
  state without opening the sidecar.
- risks — a status line that grows past a reader's expectation is the class this unit's arm now
  guards; the `next` field stays last, which is the only position any reader keys on.
- testing — §6; four fixtures and the one-line arm, each against the driver over the suite's
  scratch fixture.
- migration — none; a record with no stop line and an old record with no `keepalive` fact print
  exactly what they printed before.
- user docs — the `--status` VERBS entry and its render.

## 6. Acceptance criteria

The fixture is unit 7's §6 fixture: the suite's `tRun` build at its `--landed` success shape, a
stop log written by `printf` under the fixture's git dir, removed with `rm -f` before and after.
Each criterion is observed by running the driver over that fixture in a scratch clone; the staged
break is a driver copy with the field clause removed.

- **AC1** — When the newest stop line reads phase `LANDING` and its `session_crons` contains `k1`,
  `bash tools/unattended/unattended.sh --status tRun` prints one line carrying ` · keepalive k1
  present in the harness listing at 2026-09-16T12:00:00Z`; when the listing is `[]`, the same
  line carries ` · keepalive k1 absent in the harness listing at 2026-09-16T12:00:00Z`; and the
  line still ends with the `next` field the `:1874` reader extracts.
  Red when: `present` and `absent` swap, or the field prints after `next`, which moves the one
  position every reader keys on.
- **AC2** — When no stop log exists for the slug, the status line is byte-identical to what the
  driver at this unit's base prints, compared with `cmp` over the two outputs; when a stop line
  exists and the record's `keepalive` line is deleted with `sed -i '/^keepalive: /d'`, the line
  carries no `keepalive` field.
  Red when: the field prints at nothing, which grows every existing status line; or a listing with
  no id to compare prints a presence.
- **AC3** — When the fixture holds a parked row, a two-line `resume.tRun.log` and a stop line
  naming `k1`, `bash tools/unattended/unattended.sh --status tRun | wc -l` prints `1`, and the same
  count over `--resume tRun`'s output minus its resume lines is `1` for the status portion,
  observed by the existing status-and-resume agreement arm still holding.
  Red when: any field arrives on a second line, which is the H1 defect re-introduced by any unit.
- **AC4** — When `grep -c 'in the harness listing' tools/unattended/VERBS.template.md` and the
  same over `memory/guides/UNATTENDED-VERBS.md` run, both print 1 and 0 at this unit's base, and
  `bash tools/unattended/adopt-unattended.sh --check` exits 0 printing `in sync`.
  Red when: the template moved and the render did not, which check 10 reds at the close.
- **AC5** — When `grep -c 'run --status' tools/unattended/unattended.test.sh` is compared between
  this unit's base and tip, the difference equals the arms this unit adds, and the arm at `:1874`
  — `--status selects the same first row through the extracted helper` — is unchanged in bytes.
  Red when: a control arm was edited to admit a second line, which is the resolution this unit
  rejects.

## 7. Gates

`unattended kit gate` · `unattended skill wiring` · `harness arms (fail branches armed or pinned)` · `memory hygiene` · `spec tokens (a spec's own names resolve)` · `lexicon naming predicates`

These are `--close`'s. The pass runs none of them: it verifies with the driver invocations of AC1 to
AC3 over the fixture and the greps of AC4 and AC5. Under `unattended kit gate`, check 10's
parity of the VERBS pair is the join this unit moves.

New arm: `tools/unattended/unattended.test.sh` · the four field fixtures of AC1 and AC2 and the one-line arm of AC3, each observed red against a driver copy with the field clause removed · `FLOOR_ASSERTIONS` and `FLOOR_SHARD_2` rise by the executed count; `FLOOR_SHARD_1` does not move

## 8. Open questions

none

## 9. Revision log

- rev-1 · 2026-09-20 · initial draft, authored at the M4 disposal of spec-audit round 1 as the
  promotion of H1 (raw ids 1, 21, 30, 44); carries the `none` arm of L6 (raw id 15) in field form,
  which unit 7's rev-2 routes here.

## 10. Reuse audit

`python tools/codebase-map/reuse_lookup.py "print the stop-guard listing as a field on the status
line and assert the status output is one line"` returned no seam and `unscanned layers: .sh`, so
the driver is invisible to it. The seam, read at source: the `parked`/`noted` field rule in
`verb_status` at `tools/unattended/unattended.sh:2890` onward — `parked=" · parked $nparked"` when
non-zero, `parked="$parked · noted $nnoted"` — which unit 5 S8 already extends for its resume
field and this unit extends once more; `read_stop_listing`, unit 7's helper; and the suite's
thirty-two `run --status` readers, of which the `:1874` `sed` and the `:1859` `grep -c` read the
output whole and are why the field, not a line. The recall probe's hits were unit 5's own F1
(the field decision, `spec/2026-09-16-spec-TOOL-aWokenSentinel-5.md:469`), `TOOL-dHonouredPark-4`
(`--status` and `--plan` take their `next` from one generated region, which is the field this
unit must stay before), and a `dScriptedRepeat` ledger row on the byte-equality `same` helper.

Recall terms used: `status one line sed next unit same byte equality parked noted field omitted header promise`
