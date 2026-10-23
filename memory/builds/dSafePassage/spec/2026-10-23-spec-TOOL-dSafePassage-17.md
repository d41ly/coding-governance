# TOOL-dSafePassage-17 — a down is judged by its row's declared `reverted` rule, and a down with no before-image by its exit

**Status:** OPEN · rev-1 · 2026-10-23 · node d · Tier-2 · base 3708a705 · streams tooling · order 4 · advances TOOL-dSafePassage-14

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-23-build-TOOL-dSafePassage-17-deviation-63.md](../build/2026-10-23-build-TOOL-dSafePassage-17-deviation-63.md) | deviation | — |

<!-- /gen:spec-records -->

## 1. Goal

The round-1 spec audit of this build
(`memory/builds/dSafePassage/reviews/2026-10-23-review-TOOL-dSafePassage-1-2-3-4-5-6-7-8-9-10-11-12-13-spec-audit-round1.md`)
confirmed finding **id 51** at BLOCKER, its item **D-2**. TOOL-dSafePassage-4's reverse walk stops
with `witness still holds after down` whenever a witness exits 0 after a down (its spec, S4 move 5,
line 58, and the §4 table, line 128). Three of this build's witnesses no down can falsify:
`lib/python-floor-3.15`'s witness is the node's preflight (TOOL-dSafePassage-11 §4, lines 130-134), and
the two legacy-home steps' witnesses are "the file is absent" (TOOL-dSafePassage-1 §4, lines 226 and
233), which holds on any adopter that never had the file, where the forward walk records the row
`applied` by witness alone and no before-image exists. So no rollback past those steps completes. This
unit is id 51's promotion, built from the skeptic's corrected fix: an optional per-row `reverted` rule
in TOOL-dSafePassage-1's grammar, the floor row declaring that its down's own exit decides, and a no-image
rule for the downs TOOL-dSafePassage-1's helper runs.

## 2. Scope (IN)

- **S1** — The key. `read_steps` admits an optional `reverted` on an `[[upgrade]]` row: an argv list
  under the row-argv rules of TOOL-dSafePassage-1's §4 table, whose exit 0 means the down took effect,
  or the string `"down-exit"`, meaning the down's own exit 0 decides. Absent means "the witness does
  not hold after the down". Any other value exits 2 naming the file, the row and the key, as every
  refused key does. Observed by AC1.
- **S2** — The verdict. `derive_down_verdict(row, image_present, down_rc)` in
  `tools/govkit/upgrade_steps.py` decides move 5 of `run_reverse_walk`, `image_present` read before
  the down's spawn, where TOOL-dSafePassage-4 already reads the image's paths:
  - `reverted = "down-exit"`: reverted when the down exited 0, the witness not run;
  - `reverted` an argv: reverted when that argv exits 0 under `run_step_isolated`;
  - no `reverted` and an image present: reverted when the witness does not hold, as today;
  - no `reverted` and no image: reverted when the down exited 0, the no-image rule.
  Not reverted records `failure` `witness still holds after down` in the default case and
  `reverted check exits <rc>` for an argv. Observed by AC2, AC3 and AC4.
- **S3** — The no-image down. `write_from_before_image`, TOOL-dSafePassage-1's restore helper, exits 0
  and writes nothing when no image exists for the step at
  `.governance/steps/<entry>/<slug>.before.json`, so the two legacy-home downs on a target that never
  held the file succeed and leave it as it was. Observed by AC5.
- **S4** — The floor row. `lib/python-floor-3.15` in `tools/govkit/steps.toml` gains
  `reverted = "down-exit"`, so its down's `check_down_floor` refusal still stops a rollback and its
  exit 0 records `rolled-back` whatever the node's interpreter. Observed by AC6.
- **S5** — Frozen. `check_frozen` treats `reverted` as it treats `down`: an edited `reverted` on a
  landed row reds. Observed by AC7.
- **S6** — The docs. The "Rolling back" section of `help/upgrade-steps.md` says how a down is judged
  and when a row declares `reverted`. Observed by AC8.

## 3. Non-goals (OUT)

- The reverse walk's records below schema 4 and the rollback's stamp: `TOOL-dSafePassage-18` and
  `TOOL-dSafePassage-19`.
- A lint that decides from a witness's text whether it reads node state. The report's left-shift
  names one; no grammar exists to read a witness's meaning, so the fixture arm of AC2 and AC3 is the
  class's observation instead.
- `reverted` on any row but the floor row. The two legacy-home rows are covered by the no-image rule
  and keep the default.

### Edges

- **consumes-from** `TOOL-dSafePassage-1` — the row grammar and `read_steps`, `check_frozen`, and the before-image helpers whose restore gains the no-image rule; without them there is no key to add and no down to judge
- **consumes-from** `TOOL-dSafePassage-4` — `run_reverse_walk` and its move 5, whose verdict this unit replaces, and the `rollback` fixture family; without them there is no reverse walk to change
- **consumes-from** `TOOL-dSafePassage-11` — the floor row in the steps file and its down; without it S4 has no row to declare on
- **hands-off** `TOOL-dSafePassage-5` — the rollback of the release-0 tree past the floor step and the two legacy-home steps, back to release-0's digest

## 4. Design

### Data model

The key, beside TOOL-dSafePassage-1's §4 table:

| Key | Type | Rule |
|---|---|---|
| `reverted` | optional | `"down-exit"`, or an argv list under the `up`, `down` and `witness` rules. Absent means the witness must not hold after the down, or, with no before-image at the down's spawn, the down's exit 0. |

The floor row after this unit:

```toml
[[upgrade]]
id = "lib/python-floor-3.15"
up = ["bash", "{gov}/lib/python-floor.sh", "preflight"]
down = ["bash", "{gov}/lib/python-floor.sh", "down", "3.11", "{target}"]
witness = ["bash", "{gov}/lib/python-floor.sh", "preflight"]
reverted = "down-exit"
surfaces = []
needs-target = false
resume = "atomic"
```

The reverse walk's table, TOOL-dSafePassage-4 §4 "Data model", with move 5 read through S2:

| Row | Image at spawn | Down | Judged by | Row after |
|---|---|---|---|---|
| `reverted = "down-exit"` | either | exit 0 | the down | `rolled-back` |
| `reverted` an argv | either | exit 0 | that argv | `rolled-back` on its exit 0 |
| no `reverted` | present | exit 0 | the witness | `rolled-back` when it does not hold |
| no `reverted` | absent | exit 0 | the down | `rolled-back` |

A non-zero down is `down exit <rc>: …` and stops, as TOOL-dSafePassage-4 S4 move 4 says.

### Inventory

Minted: the row key `reverted` and its value `down-exit`; `derive_down_verdict` in
`tools/govkit/upgrade_steps.py` (cell `py.function`, verb `derive`, OK by
`python tools/lexicon/lexicon.py --suggest derive_down_verdict --as py.function` on 2026-10-23); the
failure text `reverted check exits <rc>`; the `rollback` plants `witness-only`, `node-witness` and
`node-witness-refuses`. No conf key, no gate leg, no policy key.

### Migration

Additive: the key is optional, and no landed row exists at the base, so the frozen check grades no
row that predates it.

### Rollout

Live at landing. It builds at order 4, after TOOL-dSafePassage-11 (order 3), the last of the three
units whose code it amends, and before TOOL-dSafePassage-5 (order 5), whose `down` case it unblocks.

### Files touched (estimate)

- `tools/govkit/upgrade_steps.py`
- `tools/govkit/steps.toml`
- `tools/govkit/selftest.py`
- `help/upgrade-steps.md`

### Alternatives rejected

- **The witness decides every down**, today's rule: three shipped rows can never roll back.
- **The no-image rule alone, with no key.** It covers today's three rows, but a later row whose up
  writes an image and whose witness reads node state would stop every rollback again; the key lets
  that row say so, and the floor row is its first user.
- **Removing the floor step's witness.** The forward walk's skip needs it (TOOL-dSafePassage-2 S2
  move 1).

## 5. Production-readiness checklist

- security: the argv form runs under `run_step_isolated`, the one spawn site, and the reader refuses
  it under the same rules as every argv.
- perf / scale: at most one extra spawn per down, for the argv form only.
- error / empty / loading states: a malformed `reverted` exits 2 at read time; a down with no image
  exits 0 and writes nothing.
- observability: the failure text names which rule judged the down.
- risks: a row with no image whose down exits 0 without undoing anything reads `rolled-back`; such a
  down wrote nothing on the up side either, which is what "no image" records.
- testing: the `rollback` plants of S2 and the probes of §6.
- migration: additive.
- user docs: the "Rolling back" section of `help/upgrade-steps.md`, S6.

## 6. Acceptance criteria

- **AC1** — When `python tools/govkit/upgrade_steps.py list` runs over a scratch gov whose steps file
  plants `reverted = "maybe"` on a row, it exits 2 naming the file, the row and `reverted`; with
  `reverted = "down-exit"` it exits 0.
  Red when: an unknown `reverted` value is read as the default.
- **AC2** — When `python3 "tools/govkit/upgrade_steps.py" fixture rollback --plant witness-only` runs,
  a row whose witness is "the file is absent" is recorded `applied` by witness alone on a target that
  never held the file, and the reverse walk downs it with no image, records it `rolled-back`, and
  exits 0.
  Red when: the reverse walk stops on the row with `witness still holds after down`.
- **AC3** — When `python3 "tools/govkit/upgrade_steps.py" fixture rollback --plant node-witness` runs,
  a row shaped as the floor row, whose up writes nothing, whose witness always exits 0 and which
  declares `reverted = "down-exit"`, is downed and recorded `rolled-back`, and the run exits 0;
  `--plant node-witness-refuses` makes that down exit 1, and the run exits 1 with the row's failure
  naming `down exit 1`.
  Red when: the walk stops on the row whose down exited 0, or passes the one whose down refused.
- **AC4** — When `python3 "tools/govkit/upgrade_steps.py" fixture rollback --plant witness-stays`
  runs, TOOL-dSafePassage-4's plant with an image present, the row keeps `applied` with
  `witness still holds after down`, and the run exits 1.
  Red when: the no-image rule reaches a row whose image was present.
- **AC5** — When `python tools/govkit/steps/fanout_cap.py down <t>` runs on a scratch target with no
  `.agent-cap.conf` and no image under `.governance/steps/agent-cap/`, it exits 0 and
  `git -C <t> status --porcelain` prints nothing.
  Red when: the down refuses for want of an image, or writes a file.
- **AC6** — When `python -c "import sys, tomllib; print([r.get('reverted') for r in tomllib.load(open(sys.argv[1], 'rb'))['upgrade'] if r['id'] == 'lib/python-floor-3.15'])" "tools/govkit/steps.toml"`
  runs, it prints `['down-exit']`.
  Red when: the floor row carries no `reverted`.
- **AC7** — When a branch of a scratch clone edits a landed row's `reverted`,
  `python tools/govkit/upgrade_steps.py frozen --base <main sha>` exits 1 naming the id and
  `reverted`.
  Red when: the edit exits 0.
- **AC8** — When `git grep -n -e "reverted" -e "down-exit" -- help/upgrade-steps.md` runs, the
  "Rolling back" section names both.
  Red when: the page does not say how a down is judged.

## 7. Gates

`govkit selftest` · `govkit refusal join` · `govkit acceptance matrix` · `govkit selfcheck` · `recall floor arms` · `encoding posture (text IO names its encoding)` · `lexicon naming predicates` · `spec tokens (a spec's own names resolve)`

New arm: tools/govkit/selftest.py · covers AC1 AC2 AC3 AC4 AC5 AC7 · the self-test calls `upgrade_steps.py fixture rollback` with the three new plants beside `witness-stays`, the `list` refusal and the frozen edit, its failing case staged by a walk copy whose move 5 reads the witness for every row · none

## 8. Open questions

none

## 9. Revision log

- rev-1 · 2026-10-23 · initial draft, the promotion of the round-1 spec audit's id 51 (BLOCKER, item
  D-2).

## 10. Reuse audit

The seams extended are TOOL-dSafePassage-1's row grammar, `read_steps`, `check_frozen` and
`write_from_before_image`, TOOL-dSafePassage-4's `run_reverse_walk` move 5, and the floor row of
TOOL-dSafePassage-11, all specced and unbuilt at the base. `python tools/codebase-map/reuse_lookup.py
"judge whether a rollback down step took effect when the witness reads node state"` ranked `read`,
`read_text`, `read_conf` and `read_journal`, name-token matches, so no existing seam fits beyond the
three specs; the map cannot rank code no unit has built yet, which is where it and the specs
disagree.

Recall terms used: `python tools/memory-recall/query.py "how were spec audit findings promoted into repair units placed beside the unit they repair" --terms "spec audit promoted unit repair blocker high minors batch disposal order edges rescope"`
