# TOOL-aHoistedPass-7 — a brief on disk before the code that cites it

**Status:** SPECCED · rev-1 · 2026-09-04 · node a · Tier-2 · base c4fcf5ad · streams tooling · order 7

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-09-04-build-aHoistedPass-1-design-pass.md](../build/2026-09-04-build-aHoistedPass-1-design-pass.md) | research | TOOL-aHoistedPass-1 TOOL-aHoistedPass-2 TOOL-aHoistedPass-3 TOOL-aHoistedPass-4 TOOL-aHoistedPass-5 TOOL-aHoistedPass-6 TOOL-aHoistedPass-8 TOOL-aHoistedPass-9 DEPL-aHoistedPass-1 |

<!-- /gen:spec-records -->

## 1. Goal

A build unit that closes without a recorded brief leaves no evidence of what the agent that built it
was handed, and nothing on the merge bar notices. This unit adds one leg, `brief-recorded`, that
asserts for every unit a build README carries as CLOSED after a dated cutoff that the build commit
itself carries a `brief · item <id>` row whose hash still joins to a tracked file at that commit.

## 2. Scope (IN)

- **S1** — `tools/unattended/check-brief-recorded.sh`, the leg. Same skeleton as
  `tools/unattended/check-pass-order.sh`: the `GIT_GRAFT_FILE=/dev/null` pin (`:34`), the pinned `GIT`
  wrapper from `lib-unattended.sh:27` at every sha dereference, the subshell conf import (`:59-102`)
  with its own key allow-list, the dated cutoff (`:132-145`), the four-count liveness line plus the
  printed exclusion set (`:245-263`), and exit 0 clean / 1 violation / 2 misconfigured.
- **S2** — `build_commit()` in `tools/unattended/lib-unattended.sh`: the build-commit selection
  currently inlined at `check-pass-order.sh:172-215`, moved whole with its exclusion-set rationale
  comment, taking `base · unit-id · build-dir · generated-indexes · shared-records` and printing the
  sha or returning 1.
- **S3** — `check-pass-order.sh` calls `build_commit` instead of its inlined copy. Behaviour
  unchanged; `tools/unattended/check-pass-order.test.sh` is the regression check and stays green
  without an edit to a single arm.
- **S4** — the two terms of §4, existential over rows with the LAST row winning.
- **S5** — `BRIEF_RECORDED_CUTOFF` in `.unattended.conf`, dated at the landing, and
  `BRIEF_RECORDED_CUTOFF=""` in `tools/unattended/.unattended.conf.example` beside
  `PASS_ORDER_CUTOFF=""` at `:218`. Blank turns the leg off and the leg announces that it is off.
- **S6** — a grammar liveness assertion: the leg refuses with `DEAD PROBE` when the driver no longer
  spells the row shape it matches.
- **S7** — `tools/unattended/check-brief-recorded.test.sh`, carrying the arms of §6, and its two
  rows in `tools/unattended/run-unattended-gates.sh` beside `pass-order history` at `:197` and
  `pass-order selftest` at `:204`.
- **S8** — the five-declaration act of §4's Inventory, plus the kit version bump 1.17 → 1.18 that a
  new shipped script and three moved files owe, and the fourth entry in `check-kit-versions.sh:169`'s
  script list.
- **S9** — `tools/install-prefix-carried.txt` rows for both new files if either spells a `tools/`
  literal, in the shape of `:104-105`.

## 3. Non-goals (OUT)

- **Ordering inside the commit.** Nothing proves the brief preceded the code when both land in one
  commit. Recovering it needs `--brief` to commit its own row, which breaks the one-commit-per-pass
  discipline `stage_or_fail` (`unattended.sh:4226`) exists to keep. Rejected here and not revisited.
- **Grading the brief's CONTENT.** The leg reads a path and a hash. Whether the brief said anything
  useful is outside it, and the header says so.
- **A `harness-used` DoD item.** An agent boundary leaves no artifact inside this repo's reach:
  `dRetiredFork` ran without the harness and wrote 28 `brief` rows byte-identical to what a
  harnessed run writes. A leg claiming to see the harness would reproduce `passes-harnessed`'s exact
  failure one layer down.
- **Anything about a unit that is not CLOSED**, about a build with no pinned run BASE, or about a
  build opened before the cutoff. Those three are COUNTED and announced, never silently skipped.
- **A waiver registry.** The five units that would red under a back-dated cutoff are handled by the
  cutoff, not by an exemption list.
- **Widening `--dispatch`, the order gate, or `pass-order history`.** Those are other units and
  other backlog rows.

## 4. Design

### The anchor, measured

`--brief` STAGES its row rather than committing it: `park` at `unattended.sh:4225` appends the line
and `stage_or_fail` at `:4226` stages it, so the row lands in the same commit as the pass. The
sibling leg anchors on the build commit's FIRST PARENT (`check-pass-order.sh:217-221`), which is
correct for a spec — the build method requires a run to author a missing spec, so the spec must
predate the code — and wrong for a brief, which the same pass writes.

Reproduced at `c4fcf5ad` over the three tracked builds that carry brief rows, using
`check-pass-order.sh`'s own build-commit selection and its own conf values:

| build | CLOSED units | with a build commit in range | rows at that commit | rows at its first parent |
|---|---|---|---|---|
| `dBriefedPass` | 5 | 5 | 2 units | 1 unit |
| `dRatifiedSeam` | 2 | 2 | 2 units | 0 units |
| `dRetiredFork` | 29 | 24 | 22 units | 0 units |

Twenty-six units carry at least one row at their build commit. One of those twenty-six also carries
one at the first parent. **A first-parent anchor therefore reds 25 of the 26 conforming units**, and
the unit that BUILT the verb is among them: `TOOL-dBriefedPass-2`'s build commit `b9fb4fb0` carries
three rows and its first parent `ac4875fb` carries zero. The anchor is the build commit itself.

### Data model

The row is `park()`'s grammar and nothing else (`unattended.sh:3830`, and the header at `:4167-4171`
says why): `<ISO-Z> brief · item <unit> · reason <hash12> <tracked-path>`, written at `:4217`. The
hash is `git hash-object` over the tracked path (`:4203`), truncated to twelve hex at `:4204`, so it
is the index blob id on every platform.

Two terms, both evaluated at the build commit:

1. the run-state blob at that commit carries at least one line matching ` brief · item <id> · reason `;
2. the LAST such line for that unit names a path tracked at that commit whose blob id begins with the
   line's twelve hex characters.

### The quantifier — last row wins

A unit can be re-briefed and the corpus does it. Measured at `c4fcf5ad`: `TOOL-dBriefedPass-2`
carries three rows, `TOOL-dBriefedPass-3` two and `DEPL-dRetiredFork-8` two, each set naming ONE path
with different hashes. A universal reading over rows reds all three, because the earlier hashes no
longer describe the file. A bare existential lets a stale row satisfy term 2 forever after an edit.

The LAST row wins, and the writer is why it can: `verb_brief`'s exact-line compare at `:4218-4224`
returns without writing when the whole row is unchanged, so a new row exists only when the hash
CHANGED. The last row is therefore the newest hash, which is the file the builder was handed.

### The liveness line and the dead probe

Four counts and the exclusion set, copied from `check-pass-order.sh:262-263`:

```
brief-recorded: graded N closed unit(s) · X build(s) skipped by the <date> cutoff · Y with no pinned run BASE · Z unit(s) unbuilt-in-range
brief-recorded: the record surface excluded from build-commit selection was: <build folder> <GENERATED_INDEXES> <SHARED_RECORDS>
```

`graded` increments BEFORE the build-commit selection, exactly as the sibling's does at `:173`, so a
unit graded by nothing still counts as graded. That is copied deliberately and it is a hole: the
count that proves term 1 actually ran is `graded − unbuilt`, not `graded`, and the leg's own header
says so in those words. AC4 asserts on the difference and not on `graded`.

The exclusion set is printed for the sibling's reason (`:255-261`): it is composed from two conf keys
the graded run can commit, so widening `GENERATED_INDEXES` turns a real violation green and the only
other trace is a count a reader has been taught to ignore. Printing it buys a trace, not a guard.

The sibling's DEAD PROBE (`:120-130`) guards a classifier sliced out of the driver by line span. This
leg slices nothing, so that probe has no counterpart — what it has instead is a GRAMMAR coupling.
The row shape this leg matches is written by one function in one file. If the driver stops spelling
it, every unit reds with "no brief row", which is a wrong verdict wearing a finding's clothes. So
before grading anything the leg asserts the driver still spells ` brief · item ` and, when it does
not, prints `DEAD PROBE` and exits 2. That is the whole probe: one grep, and it converts a corpus of
false accusations into one honest refusal.

### The cutoff

`BRIEF_RECORDED_CUTOFF`, an ISO date, read from `.unattended.conf` through the subshell import and
compared against each build README's `opened:` with `sort -C`, the idiom `PASS_ORDER_CUTOFF`,
`SPEC_THIN_CUTOFF`, `UNITS_REGION_CUTOFF`, `LANDED_ANCHOR_CUTOFF` and `DISPOSITION_CUTOFF` already
share. A malformed value exits 2, because a cutoff nothing can compare grades every build or none.

Its value is the LANDING date and the consequence is stated rather than buried: **the leg grades
zero units on the day it lands.** All three builds that carry brief rows opened on 2026-09-01,
2026-09-02 and 2026-09-03, and five units among them carry no row at all
(`TOOL-dBriefedPass-1`, `-4`, `-5`, `DEPL-dRetiredFork-5`, `TOOL-dRetiredFork-6`), so any cutoff old
enough to grade the conforming ones is old enough to make the leg unlandable. A per-build cutoff
cannot admit one unit without its siblings. This is why §6's green arm is a back-dated run in a
scratch clone and why AC10 asserts the day-one population is empty on purpose.

### Inventory

The five-declaration act, with a `[[gate_leg]]` because this leg is a script the kit SHIPS:

| # | Where | What |
|---|---|---|
| 1 | `tools/gate-legs.json` | `{"name": "brief-recorded", "argv": ["bash", "tools/unattended/check-brief-recorded.sh"], "chunk": "declarations", "subject": "repo", "guard": [], "ceiling": 900}` |
| 2 | `tools/unattended/kit.toml` | a `[[gate_leg]]` with `subject = "repo"`, `argv = ["bash", "{kit}/check-brief-recorded.sh"]`, `guard = []`, `red_after_land = true`, beside the four at `:107-133` |
| 3 | `tools/govkit/subject-pins.tsv` | one `<name>\t<subject>\t<chunk>` row, written by `python tools/govkit/govkit.py selfcheck --write` |
| 4 | `memory/map/features/unattended.md` | the leg name added to the `gate-legs` claim, which today holds three |
| 5 | the map artifacts | regenerated in the same commit |

**No guard, and that is a correction to the design.** `pass-order history` carries `guard = []`
(`tools/unattended/kit.toml:126-129`, `tools/gate-legs.json:713-722`) for the reason the playbook
leg's comment at `:115-117` states: a leg whose subject is the REPOSITORY's records goes stale with
nobody editing the kit, and a guard scoped to the kit dir would skip it on exactly the commits that
add a brief row — a build commit that touches no kit file at all. Ceiling 900 copies the sibling.

### Cost

Measured on node `a`, 2026-09-04, both at `c4fcf5ad`. `bash tools/unattended/check-pass-order.sh`
costs **658 s** wall and reports `graded 45 · 83 skipped by the 2026-09-01 cutoff · 5 with no pinned
run BASE · 5 unbuilt-in-range`; the back-dated walk this unit's probe ran over the three
brief-carrying builds, 36 unit iterations, cost 430 s. Under a landing-dated cutoff every build is
dropped by the `sort -C` compare before any `rev-list` runs, so this leg's day-one cost is the
README scan alone.

The declared ceiling is 900, copied from the sibling, and the headroom is stated rather than assumed:
the sibling is already at 73% of it, and this leg's walk is that walk plus one blob read per graded
unit and one `rev-parse <commit>:<path>` per unit carrying a row. When the graded population reaches
the sibling's, the ceiling is the next thing that reds, and re-declaring it with a reason is the
right answer at that point rather than now.

### Files touched (estimate)

`tools/unattended/check-brief-recorded.sh` (new) · `tools/unattended/check-brief-recorded.test.sh`
(new) · `tools/unattended/lib-unattended.sh` · `tools/unattended/check-pass-order.sh` ·
`tools/unattended/unattended.sh` · `tools/unattended/check-unattended.sh` ·
`tools/unattended/.unattended.conf.example` · `.unattended.conf` ·
`tools/unattended/run-unattended-gates.sh` · `tools/unattended/kit.toml` · the five tracked
`tools/unattended/*.template.md` markers · `tools/check-kit-versions.sh` · `tools/gate-legs.json` ·
`tools/govkit/subject-pins.tsv` · `tools/install-prefix-carried.txt` ·
`memory/map/features/unattended.md` and the regenerated map artifacts.

**This unit is OWNER-GATED and the coupling is why.** The kit's version comes from
`unattended.sh`'s constant (`tools/unattended/kit.toml:6`, today 1.17). A new shipped script plus
moved bytes in three shipped files owes 1.17 → 1.18, and `check-kit-versions.sh:179-192` requires the
matching `gov:kit unattended@` marker in every tracked `tools/unattended/*.template.md` — including
`SKILL.template.md`, which ruling D1 of 2026-09-04 put on the veto-2 list. The bump is what makes
this an owner turn, not a prose edit anyone intended.

### Alternatives rejected

- **Copy the build-commit selection into the new leg.** Rejected. It is instance #2 of one predicate,
  and the sibling's own header (`check-pass-order.sh:106-108`) forbids exactly this: *"a second copy
  here would be two answers to one question"*. The selection is also the half that has already been
  wrong twice — `:179-196` records an exclusion set that made a CONFORMING run unlandable, twice over
  — so a second copy is a second chance to get the same thing wrong, in a file whose test suite runs
  on no bar. Extracting it leaves ONE answer and the sibling's 19-arm suite as the regression check.
- **Anchor on the first parent, as the sibling does.** Rejected by measurement: 25 of 26 conforming
  units red.
- **Assert the brief preceded the code.** Rejected under §3; the record is one commit.
- **A fifth printed count for units that reached term 1.** Rejected. `graded − unbuilt` is already
  derivable from the printed line, so the arithmetic costs a reader one subtraction and costs the
  leg nothing, and the sibling's four-count shape stays byte-comparable with this one.

## 5. Production-readiness checklist

- security — the conf is IMPORTED in a subshell and never sourced into the leg's shell, with a
  NUL-delimited stream and a sentinel, copied from `check-pass-order.sh:59-102`; the key allow-list
  is this leg's own declared four and nothing else, because the sibling's blanket assignment was
  itself a reproduced takeover of its `DRIVER` variable.
- perf / scale — zero builds walked on day one; the sibling leg over the same commit ranges measures
  658 s against its 900 s ceiling, so the ceiling this row copies has 27% of headroom and is the
  first thing that reds once the graded population catches up.
- a11y — N/A, a shell leg with no interface.
- i18n — N/A.
- error / empty / loading states — blank cutoff announces OFF and exits 0; malformed cutoff exits 2;
  missing conf, missing driver and a dead grammar each exit 2 with their own sentence.
- observability — the four-count line plus the printed exclusion set on every run, clean or not; the
  bar persists it under `<git-dir>/gate-logs/` like every other leg.
- risks — the leg grades zero on day one and can only be exercised by the staged arms; the extraction
  moves code inside a landed leg whose suite is on no bar; a widened `GENERATED_INDEXES` turns a real
  violation green, traced by the printed exclusion set and by nothing else.
- testing + left-shift gates — six arms in `check-brief-recorded.test.sh`, three of them staged
  failures observed RED before the leg lands; the sibling suite re-run unchanged for the extraction.
- migration / rollback — additive. Reverting is deleting the manifest row and the two files; no data
  shape changes and no run-state byte is rewritten.
- user docs — `tools/unattended/README.md`'s leg list gains the row; `memory/guides/UNATTENDED-PROTOCOL.md`
  is NOT edited by this unit, because the protocol pair is `TOOL-aHoistedPass-2`'s carrier.

## 6. Acceptance criteria

- **AC1** — When a fixture repo's closed unit has its `brief · item` row dropped from the build
  commit and `bash tools/unattended/check-brief-recorded.sh` runs, the leg exits 1 and names that
  unit id and the short sha of its build commit.
- **AC2** — When the leg runs in a scratch clone of this repo with `BRIEF_RECORDED_CUTOFF` back-dated
  to `2026-09-01`, `TOOL-dBriefedPass-2` is absent from the printed violations and
  `TOOL-dBriefedPass-1` is present in them. The exit code of that run is 1 and no arm asserts on it,
  because asserting on the exit would have discarded the leg.
- **AC3** — When a closed unit's brief file is edited inside its build commit with no matching
  re-brief row and the leg runs, it exits 1 naming both the row's twelve hex and the blob's. This arm
  is staged because no unit in real history exercises it: measured at `c4fcf5ad`, all 26 rows join.
- **AC4** — When the leg runs under the back-dated cutoff of AC2, the printed liveness line's
  `graded` minus its `unbuilt-in-range` is at least 1, and on the live tree at landing the same line
  prints `graded 0` with all four counts present and never the word `clean`.
- **AC5** — When `BRIEF_RECORDED_CUTOFF` is set to the empty string, the leg exits 0 having printed
  the sentence naming `BRIEF_RECORDED_CUTOFF` and saying the term is off; when it is set to a
  non-ISO value the leg exits 2 naming the value.
- **AC6** — When the fixture's `unattended.sh` no longer spells the row grammar, the leg exits 2 with
  a line carrying `DEAD PROBE`, and it does so before printing any violation.
- **AC7** — When `bash tools/unattended/check-pass-order.test.sh` runs after `build_commit` is
  extracted into `tools/unattended/lib-unattended.sh`, it exits 0 with every arm unchanged, and
  `bash tools/unattended/check-pass-order.sh` on the live tree prints a liveness line whose four
  counts are identical to the pre-extraction run.
- **AC8** — When `python tools/govkit/govkit.py selfcheck` runs, it exits 0, which is what proves the
  `[[gate_leg]]` row and the `memory/map/features/unattended.md` claim are both present, since
  `govkit.py:1602-1604` reds without the second and the leg is claimed by no other descriptor.
- **AC9** — When `bash tools/check-kit-versions.sh` runs after the bump, it exits 0 with
  `tools/unattended/check-brief-recorded.sh` in the script list it walks, and it exits non-zero when
  that script's `KIT_UNATTENDED_VERSION` is staged back to `1.17`.
- **AC10** — When `bash tools/unattended/check-brief-recorded.sh` runs on the landing tree, every
  tracked `memory/builds/*/README.md` whose `opened:` date is on or after `BRIEF_RECORDED_CUTOFF` is
  zero, so the leg reports `graded 0` — asserted as the intended day-one population, with the
  cutoff's value strictly later than every tracked `opened:` date.
- **AC11** — When `bash tools/unattended/run-unattended-gates.sh --all` runs, `brief-recorded` and
  its selftest each appear as their own named row, and `bash tools/run-gates/run-gates.sh` reports
  `brief-recorded` among the legs it ran.

## 7. Gates

The new leg, `brief-recorded`, chunk `declarations`, subject `repo`, unguarded, ceiling 900.

Standing legs this unit must keep green: `unattended kit gate` — the new script joins `KIT_SH`
(`check-unattended.sh:2321-2325`) with no edit, so check 28c's bare-git ban applies to it from the
first commit, which is why every dereference goes through the `GIT` wrapper. `pass-order history`,
which the S2 extraction moves under. `kit version markers`. `govkit selfcheck`. `codebase-map
coverage + freshness`. `install-prefix (shipped surface)`. `memory hygiene`, for this spec and the
records that land with it.

**The arms are on NO bar, and that is the standing exemption, not an oversight.**
`tools/unattended/check-brief-recorded.test.sh` is registered in `run-unattended-gates.sh` as a
selftest, and by the owner ruling of 2026-08-23 no boundary runs this kit's self-tests, not even
`GATE_FULL=1`. The compensating check is a person invoking
`bash tools/unattended/run-unattended-gates.sh`, and the DoD for any later work touching this leg is
that invocation. This mirrors the sibling exactly.

**It does NOT owe an arm under `harness arms (fail branches armed or pinned)`, correcting the
design.** That leg's population is discovered, not named: a tracked `*.sh` that DEFINES `fail() {`
and has `fail <n> "` call sites, with its sibling `<stem>.test.sh` as the arm source
(`tools/memory-tree/check-arms.py:9-11`). `check-pass-order.sh` defines no such helper — measured, it
has zero `fail() {` and zero `fail <n> "` sites — and `check-arms.py --report` lists ten gates, none
of them this one. A leg built as its twin is invisible to that checker by construction.

## 8. Open questions

- **F1 — the day-one population is empty, and nothing on the bar can fail because of it.** Option (a),
  RECOMMENDED: date `BRIEF_RECORDED_CUTOFF` at the landing, accept `graded 0`, and carry the whole
  evidential weight in AC1, AC3 and AC6, which are staged failures observed RED before the leg lands.
  Option (b): back-date to `2026-09-01` and add a waiver registry for the five units that carry no
  row. Rejected as the recommendation because it invents an exemption surface for five historical
  units, and an exemption is not coverage — the leg would then be green over a list rather than over
  a fact. The cost of (a) is stated plainly: this leg's first real verdict arrives with the first
  unattended run that lands after the cutoff, and until then it is an assertion the arms proved and
  the bar cannot.
- **F2 — whether the `build_commit` extraction rides this unit or lands as its own.** Option (a),
  RECOMMENDED: this unit, because the alternative is a copy the sibling's own header forbids, and
  because `check-pass-order.test.sh` is a ready-made regression check that costs nothing to re-run.
  Option (b): land the extraction first as a Tier-1 unit so the owner turn this unit already owes is
  not also carrying a refactor of a landed leg. The argument for (b) is blast radius — S2 and S3
  touch a green merge-bar leg whose suite is on no bar — and the argument against is that splitting
  makes two owner turns out of one and leaves an intermediate commit where the helper exists with a
  single caller. Owner call; either resolution changes only sequencing, not the design.

## 9. Revision log

- rev-1 · 2026-09-04 · initial draft, from design rev-8 §6 at `c4fcf5ad`. Four corrections to the
  design, each verified against source in this pass rather than argued.
  **(1)** Design §6.4's closing line says the leg's `fail` branch "owes an arm under `harness arms
  (fail branches armed or pinned)`". False for a leg of this shape: that checker's population is a
  tracked `*.sh` that defines `fail() {` and carries `fail <n> "` sites
  (`tools/memory-tree/check-arms.py:9-11`), `check-pass-order.sh` has zero of each, and
  `check-arms.py --report` enumerates ten gates without it. §7 states the real position — the arms
  live in the sibling test file and no boundary runs it.
  **(2)** Design §7's U6 row calls the leg "guarded on the kit dir with its reason". Corrected to
  unguarded, matching `pass-order history` (`tools/unattended/kit.toml:126-129`,
  `tools/gate-legs.json:713-722`): the subject is the repository's run-state records, and a kit-dir
  guard would skip the leg on exactly the commits that add a brief row.
  **(3)** Design §7's U6 row says the unit moves `check-unattended.sh` for the conf key. It does not:
  that leg's declaration-key binding rule reads `PLAYBOOK-TEMPLATE.template.md`
  (`check-unattended.sh:2315`), not `.unattended.conf.example`, and only ONE key exemption exists
  (`:2415-2418`), for `check-playbook.sh`. `check-unattended.sh` is still touched, but by the version
  bump, not by the key.
  **(4)** Design §6 names no reuse seam. §4 and §10 name it and S2 extracts it, because a second copy
  of the build-commit selection is the class `check-pass-order.sh:106-108` forbids in its own words.
  Two further figures were re-derived rather than carried: the first-parent anchor reds 25 of 26
  conforming units (the design asserted the failure without a count), and all 26 rows join their
  blobs, which is why AC3 is a staged arm.

## 10. Reuse audit

`python tools/codebase-map/reuse_lookup.py "brief row recorded in the run-state file, graded at the
build commit by a merge-bar history leg"` returned no SYMBOL seam this unit can extend, and the
reason is structural rather than a near miss: its ranked candidates are Python functions matched on
the name stems `build`, `run`, `record` and `fil` — `run` in `tools/settings-merge.py`, five
`build_*_index` functions, `tracked_files` in `tools/lexicon/lexicon.py` — over a corpus of 645
symbols with no shell in it, so a bash merge-bar leg cannot rank in it at all. What the same run DID
surface is the right seam, as an affordance-seam row rather than a symbol:
`` `.unattended.conf` [unattended] `` and `` `id_pattern(conf)` [row-grammar] ``. Following those two
rows to source found the reuse target this unit takes: `tools/unattended/lib-unattended.sh`, the
kit's shared-predicate library that
already holds `pass_commit`, `next_anchor`, `pinned_units` and `baseline_units` for precisely this
reason, and `tools/unattended/check-pass-order.sh:172-215`, whose build-commit selection becomes
`build_commit()` in that library with two callers instead of two copies. The conf-import block
(`:59-102`), the cutoff block (`:132-145`) and the liveness line (`:245-263`) are reused as the
sibling reuses them from `check-unattended.sh` — copied deliberately, because each is a per-leg
declaration of ITS OWN keys and counts, and the sibling's comment at `:82-89` records the incident
where sharing that block verbatim let a tracked conf line take over the leg.

Recall terms used: `brief run-state park build-commit first-parent cutoff liveness dead-probe
gate-leg record-surface pass-order hash-object re-brief graft`, passed to
`python tools/memory-recall/query.py "why is a brief row graded at the build commit rather than at
its first parent, and what does a merge-bar history leg over the run-state file owe"`.
