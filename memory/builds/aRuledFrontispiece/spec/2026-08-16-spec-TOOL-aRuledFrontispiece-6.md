# TOOL-aRuledFrontispiece-6 — the slot contract becomes a leg of its own on the merge bar

**Status:** CLOSED · rev-2 · 2026-08-17 · node a · Tier-2 · base 96141aed · streams tooling

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-08-16-review-TOOL-aRuledFrontispiece-1-1.md](../reviews/2026-08-16-review-TOOL-aRuledFrontispiece-1-1.md) | spec-audit | TOOL-aRuledFrontispiece-1 TOOL-aRuledFrontispiece-2 TOOL-aRuledFrontispiece-3 TOOL-aRuledFrontispiece-4 TOOL-aRuledFrontispiece-5 TOOL-aRuledFrontispiece-7 TOOL-aRuledFrontispiece-8 TOOL-aRuledFrontispiece-9 TOOL-aRuledFrontispiece-10 TOOL-aRuledFrontispiece-11 |
| [2026-08-17-review-TOOL-aRuledFrontispiece-1-2.md](../reviews/2026-08-17-review-TOOL-aRuledFrontispiece-1-2.md) | spec-audit | TOOL-aRuledFrontispiece-1 TOOL-aRuledFrontispiece-2 TOOL-aRuledFrontispiece-3 TOOL-aRuledFrontispiece-4 TOOL-aRuledFrontispiece-5 TOOL-aRuledFrontispiece-7 TOOL-aRuledFrontispiece-8 TOOL-aRuledFrontispiece-9 TOOL-aRuledFrontispiece-10 TOOL-aRuledFrontispiece-11 |
| [2026-08-17-review-TOOL-aRuledFrontispiece-1-3.md](../reviews/2026-08-17-review-TOOL-aRuledFrontispiece-1-3.md) | diff-review | TOOL-aRuledFrontispiece-1 TOOL-aRuledFrontispiece-2 TOOL-aRuledFrontispiece-3 TOOL-aRuledFrontispiece-4 TOOL-aRuledFrontispiece-5 TOOL-aRuledFrontispiece-7 TOOL-aRuledFrontispiece-8 TOOL-aRuledFrontispiece-9 TOOL-aRuledFrontispiece-10 TOOL-aRuledFrontispiece-11 |

<!-- /gen:spec-records -->

## 1. Goal

Put the slot contract on the merge bar as a leg with its own name and its own exit code, so a README
that violates it produces a verdict naming the contract rather than one line inside a twenty-check
aggregate. The predicate belongs to `TOOL-aRuledFrontispiece-1`; this unit makes it binding and pays
the four registry costs a new leg incurs.

## 2. Scope (IN)

- **S1** — a new row in `tools/gate-legs.json` named `build-README slot contract`. The name becomes a
  `gate-legs` inventory key in the codebase map the moment it lands, so it is chosen once here and
  not adjusted later; a rename is the delete-plus-add this build is avoiding.
- **S2** — the row's `argv` is `["python3", "tools/memory-tree/gen_build_index.py", "--check-format"]`.
  A new verb on the engine `TOOL-aRuledFrontispiece-1` already changes, not a new script, so the
  predicate stays single-sourced.
- **S3** — `--check-format` walks every build README, applies the slot predicate, prints one line per
  violation naming the file and the line, and exits 1 when there is one. It renders nothing and
  writes nothing. `--check` and `--write` keep their meanings; the mode tuple at
  `gen_build_index.py:896` and the usage line at `gen_build_index.py:897` both grow the fourth verb.
- **S4** — the verb's own header states what it does NOT do, in the shape
  `tools/check-playbook-parity.sh` uses at its line 15: the leg holds the SLOT CONTRACT — which slot
  opens where, in what order — and never the quality, accuracy or wording of the prose inside a slot.
  A fluent README that is subtly wrong passes, and the header says so rather than implying it away.
- **S5** — the leg carries no `guard`. It is one pass over the same files check 9 already reads, and
  the two pathspecs a guard would need (`memory/builds/` and `tools/memory-tree/`) buy a skip worth
  less than the early signal a too-narrow guard costs.
- **S6** — `tools/memory-tree/gen_build_index.py` is present inside the `## The gate suite` section of
  `AGENTS.md` in the SAME commit as the manifest row, and that section gains a bullet naming the leg.
- **S7** — the leg's NAME is claimed by a dossier under `memory/map/features/` in the same commit.
  `memory/map/baseline.toml` is not touched.
- **S8** — `memory/guides/SESSION-KICKOFF.md`'s `last-audit` stamp is re-stamped in the same commit as
  the manifest row, per the stamp rule at `memory/guides/SESSION-KICKOFF.md:22` — sha `HEAD` on `main`,
  else `git merge-base origin/main HEAD`, datetime always advancing — with a delta line in the commit
  message. This unit is LAST in the build order, so this is the build's closing re-stamp and it
  discharges every watched path the build moved, not just this unit's own.

## 3. Non-goals (OUT)

- Judging prose. S4 is the boundary: section order and marker placement, never content.
- Defining the slot contract or the refusal messages. Unit 1 owns both; this unit calls them.
- Retrofitting the corpus. `TOOL-aRuledFrontispiece-11`, at position 9 of the build order, owns every
  authored relocation — the prose moves and the `roster:units` insertions — and
  `TOOL-aRuledFrontispiece-10`, at position 10, owns the re-render and the kit version bump. This unit
  is position 11 and moves no authored byte in any README.
- Growing `tools/memory-tree/check-memory-hygiene.sh` by a check. Fork 2 rejected that and §4 prices
  it.
- Shipping the leg to adopters through a `[[gate_leg]]` block in `tools/memory-tree/kit.toml`. An
  adopter's corpus has not been retrofitted, and a kit that installs a gate their tree fails hands
  them a red bar on day one. It is a follow-up once the retrofit is a kit-side migration.
- A `--fix` verb. Moving a marker pair is an authored edit and a renderer must not make it.

## 4. Design

### Inventory

A leg is data in five registries, and four of them fail in a way the leg's own author does not see.

| Registry | What it demands | What a skip costs |
|---|---|---|
| `tools/gate-legs.json` | a non-empty `name`, `argv` of length ≥ 2, `argv[0]` in `bash python python3 node` | `tools/run-gates.test.sh` arm 1 reds |
| `AGENTS.md` `## The gate suite` | the row's argv path present as a substring of that section | `python tools/drift-audit/drift_report.py --check` reds |
| `memory/map/features/` | the row's display NAME claimed by a dossier | `python3 tools/codebase-map/test_codebase_map.py` reds UNCLAIMED |
| `memory/guides/SESSION-KICKOFF.md` | a `last-audit` re-stamp at or after any commit touching a `watch:` path | `bash skills/session-kickoff/manifest-check.sh` reds C5 |
| `tools/govkit/registry.toml` | nothing — `tools/gate-legs.json` is a declared exemption | — |

The ratchet row is this unit's because of WHERE it sits, not because of what it edits.
`tools/gate-legs.json` is a `watch:` path at `memory/guides/SESSION-KICKOFF.md:6`, so S1 puts this
unit inside C5's population on its own. C5 at `skills/session-kickoff/manifest-check.sh:285-311`
requires the newest watch-touching commit since the last stamp to be an ancestor of the newest commit
that CHANGED the stamp value; `TOOL-aRuledFrontispiece-9` re-stamps at position 8, and both
`TOOL-aRuledFrontispiece-10` at position 10 (the hygiene engine) and this unit at position 11
(`tools/gate-legs.json`) touch watched paths after it. The newest such commit is therefore this
unit's, so only this unit can carry the stamp that satisfies C5 at the build tip — and
`.githooks/pre-push` runs the full bar, so an unstamped tip blocks the landing push rather than
merely warning. No §B claim goes stale alongside it: the gate-commands block at
`memory/guides/SESSION-KICKOFF.md:72` points a reader at `tools/gate-legs.json` for the list instead
of restating it, which is exactly why a new leg costs a topological stamp and no prose edit.

The charter requirement is mechanical, not editorial. `_charter_mentions_every_leg` at
`tools/drift-audit/drift_signals.py:104` reads the manifest, takes each leg's argv elements
containing `/`, and asks whether any of them appears inside the section matched by
`^##\s+The gate suite.*?$(.*?)^##\s`. `signal_handkept` at `drift_report.py:392` scores the gap as
`actual - claims` over that one probe, and `--check` exits 1 on `value > pin` with
`PINS["handkept_inventories_disagreeing_with_source"] = 0` at `drift_signals.py:177`. Zero slack: one
leg the charter does not name reds the bar, and that leg is `drift-audit records`, which is on it.

Verified at `base 96141aed`, and stated because it changes what S6 is FOR rather than whether it
holds: the string `tools/memory-tree/gen_build_index.py` is already inside that section, at
`AGENTS.md:195`, in the self-test-legs bullet, which is inside the `## The gate suite` section
spanning lines 75 to 214. So the argv chosen in S2 satisfies the signal without
any charter edit at all. S6 is still binding for two reasons. The bullet is what a reader needs, and
the signal grades presence of a path, not description of a leg. And the moment this leg is moved to a
script of its own — the alternative §4 rejects below — the pin bites immediately with no warning.

The map requirement is keyed the other way. `_gate_legs` in `tools/codebase-map/map_extractors.py:71`
builds the `gate-legs` inventory from each leg's display NAME, so S1's string is the key, not the
argv. `memory/map/baseline.toml` is not an option for it: its own header declares the file
shrink-only and reserved for the initial backfill, and
`test_every_inventory_key_is_claimed_or_baselined` in `tools/codebase-map/test_codebase_map.py:79`
reports an unclaimed key under UNCLAIMED regardless.

### Rollout

This unit is position 11 of the build order — LAST — and that position is what makes the manifest row
addable at all. A leg cannot land red, and the corpus is not conformant at `base 96141aed`.

This unit performs NO relocation. `TOOL-aRuledFrontispiece-11`, at position 9, owns every authored
move in the corpus: the prose that sits where a generated region must go, and the `roster:units`
insertions. This unit ships the verb, its arms, the manifest row, the charter bullet, the dossier
claim and the closing ratchet stamp, and nothing else.

Measured at `base 96141aed` over the 39 folders under `memory/builds/`, counting non-blank lines
after each README's `<!-- /gen:build-index -->`: five carry top-level content there —
`aRuledFrontispiece` (134 lines), `aSiftedPlaybook` (120), `cTracedPromise` (23), `cKeyedLaunchpad`
(11) and `aTimedTurnstile` (10). That is the trailing-content class alone. The plan-before-prose class
— an authored heading between the authored plan and the generated open — is a second population that
`TOOL-aRuledFrontispiece-1`'s S4 also refuses, and this unit does not restate its size, because it
moves with every relocation `TOOL-aRuledFrontispiece-11` lands and a figure quoted here would be a
second answer to a question that unit owns. AC6 is this unit's whole interest in the number: the
predicate reports nothing over any folder under `memory/builds/` at this unit's tip.

The commit order inside this unit is therefore: the verb and its arms first, then the manifest row,
the charter bullet, the dossier claim and the `last-audit` re-stamp together. The row is added only
once `--check-format` is already clean over the corpus, which is a fact this unit OBSERVES rather than
one it creates.

### Alternatives rejected

**A twenty-first check inside `check-memory-hygiene.sh`.** This is fork 2's rejected option and its
cost is measurable rather than stylistic. The `gate-legs` inventory key for that leg is its display
name, `memory hygiene (20 checks)`, and that exact string is a row of `memory/map/baseline.toml`.
Adding a check renames it, and a rename through a shrink-only file is a delete plus an add: the
coverage gate reports the old key under STALE BASELINE and the new one under UNCLAIMED in the same
run. The only precedent is recorded in that file's own header — the ceiling raise under
`TOOL-aSiftedPlaybook-1`, taken deliberately, resolved by the owner, and written into the header so a
reader meeting the shrink-only rule also meets its one exception. Nothing enforces the rule
mechanically, which is exactly why the option was available and exactly why it is not taken twice on
an agent's own authority.

**A new `tools/memory-tree/check-build-readme.sh`.** This is still a standalone leg, so it is a
choice inside fork 2 rather than a re-opening of it, and it is rejected on cost. `check-arms.py`
DISCOVERS its population as any tracked `*.sh` that defines `fail() {` and has `fail <n> "` call
sites, so a new shell gate would demand a sibling `check-build-readme.test.sh` carrying a positive
assertion per branch naming that branch's own failure text, plus a per-gate row in `ARMS_FLOORS` in
`.memory-tree.conf`. The script would then shell out to the engine anyway, because
`TOOL-aRuledFrontispiece-1` puts the predicate in Python. That is three new files and a ratchet row
to reach a predicate one argv element already reaches.

### Files touched (estimate)

`tools/gate-legs.json` · `tools/memory-tree/gen_build_index.py` (the fourth verb, the mode tuple and
the usage line) · its `--selftest` arms · `AGENTS.md` `## The gate suite` · one dossier under
`memory/map/features/` · `memory/map/generated/` re-rendered by the map's own regen command · the
`last-audit` stamp in `memory/guides/SESSION-KICKOFF.md`. No file under `memory/builds/` is edited.

## 5. Production-readiness checklist

- security — N/A. The verb reads tracked files the render already reads and writes nothing.
- perf / scale — one read pass over 39 build READMEs, the same set `--check` already opens.
- a11y — N/A. No user-facing surface.
- i18n — N/A. The markers are ASCII literals.
- error / empty / loading states — a repo with no folder under `memory/builds/` must exit 0, not fail
  on an empty population; a young tree is a legitimate empty and not a disarmed gate.
- observability — the leg's whole output is persisted at `<git-dir>/gate-logs/` by the runner and a
  RED run's durable summary carries a `log:` pointer at it.
- risks — the leg overlaps check 9 wherever `TOOL-aRuledFrontispiece-1`'s refusals also fire inside
  `--check`, so a violation can red two legs at once; that is duplicated reporting, never a
  duplicated predicate.
  The larger risk is inherited rather than owned: this unit's row goes red the moment
  `TOOL-aRuledFrontispiece-11` leaves one README unconformed, and this unit cannot repair it without
  taking a relocation that belongs to another unit. AC6 is the tripwire and the remedy is to hold the
  row, not to move a marker here.
- testing + left-shift gates — the fixture arms live in the engine's `--selftest`, which is already a
  leg; this unit adds the arm that `--check-format` exits non-zero on a violating fixture and 0 on a
  conformant one.
- migration / rollback — rollback is deleting the manifest row; the verb is inert without it.
- user docs — the `AGENTS.md` bullet and the dossier under `memory/map/features/`.

## 6. Acceptance criteria

- **AC1** — When `bash tools/run-gates.sh` runs at this unit's tip, a leg named
  `build-README slot contract` reports `GATE ok` and the manifest holds one more leg than at
  `base 96141aed`.
- **AC2** — When a build README carries top-level content after its `<!-- /gen:build-index -->`
  marker, `python3 tools/memory-tree/gen_build_index.py --check-format` exits 1 and prints that file
  with the line number of the offending content.
- **AC3** — When `bash tools/run-gates.test.sh` runs, it passes: the new row's `argv[0]` is `python3`,
  its `argv` length is 3, and no leg script path is hardcoded in `tools/run-gates.sh`.
- **AC4** — When `python tools/drift-audit/drift_report.py --check` runs, the signal
  `handkept_inventories_disagreeing_with_source` reports 0 against its pin of 0.
- **AC5** — When `python3 tools/codebase-map/test_codebase_map.py` runs,
  `test_every_inventory_key_is_claimed_or_baselined` passes and `git diff --stat memory/map/baseline.toml`
  prints nothing.
- **AC6** — When `python3 tools/memory-tree/gen_build_index.py --check-format` runs over the corpus at
  this unit's tip, it exits 0 over every folder under `memory/builds/`.
- **AC7** — When `python tools/memory-tree/check-arms.py --check` runs, it passes with no new row in
  `memory/project/unarmed-branches.txt`, because this unit adds no shell gate defining `fail()`.
- **AC8** — When `bash skills/session-kickoff/manifest-check.sh` runs at this unit's tip it exits 0,
  and its C5 check finds no watched file changed since `last-audit` without a re-stamp at or after the
  change — the observation being that the stamp in `memory/guides/SESSION-KICKOFF.md` names a sha at
  or after this unit's own `tools/gate-legs.json` commit.
- **AC9** — When this unit's own commits are diffed against their parent — never against a base
  figure quoted in prose — `git diff --name-only <parent>..HEAD -- memory/builds/` prints nothing
  outside `memory/builds/aRuledFrontispiece/`, whose own spec header and rendered region this unit
  moves. No other build's README is touched, which is the observable form of "this unit relocates
  nothing".

## 7. Gates

`bash tools/run-gates.test.sh` · `python tools/drift-audit/drift_report.py --check` ·
`python3 tools/codebase-map/test_codebase_map.py` · `python3 tools/memory-tree/gen_build_index.py --selftest` ·
`python tools/memory-tree/check-arms.py --check` ·
`bash skills/session-kickoff/manifest-check.sh` — the `kickoff-manifest ratchet` leg, which S8 exists
to keep green and which no earlier unit in this build can discharge, because this unit's own
`tools/gate-legs.json` edit is the newest watch-touching commit at the build tip ·
`bash tools/memory-tree/check-memory-hygiene.sh` ·
`bash tools/memory-tree/check-verdict-epoch.sh`, which this unit does not discharge — the verb moves a
behaviour-bearing line of a scanned delegate, and `TOOL-aRuledFrontispiece-10` at position 10 carries
the one bump the whole build gets.

## 8. Open questions

none — fork 2 fixed where this check rides, and the questions this unit would otherwise put are
recorded as measured facts instead: §4 Rollout states that this unit relocates nothing and that
`TOOL-aRuledFrontispiece-11` at position 9 owns every authored move, and §4 Inventory records that the
charter requirement is already satisfied by the argv chosen in S2 and that the ratchet stamp falls to
this unit by position rather than by content.

The build README's park P3 — one script or two — is RESOLVED (owner, 2026-08-16): reuse
`gen_build_index.py --check-format` rather than adding `tools/memory-tree/check-build-readme.sh`.
"Standalone" in fork 2 binds the LEG, not the file, so S2 is built as written and the rejected
alternative below stands as the cost record rather than as an open option.

## 9. Revision log

- rev-1 · 2026-08-16 · initial draft.
- rev-2 · 2026-08-16 · folded the M4 spec audit (`reviews/2026-08-16-review-aRuledFrontispiece-1.md`).
  BLOCKER "§4 Rollout takes the five prose relocations": the relocation claim and the "either split
  works" escape are deleted, `TOOL-aRuledFrontispiece-11` at position 9 is named as the owner of every
  authored move, the five READMEs leave §4 Files touched, and AC9 makes "relocates nothing"
  observable. HIGH "the kickoff-manifest ratchet reds at the build tip": S8 adds the closing
  `last-audit` re-stamp, §4 Inventory grows a fifth registry row explaining why the stamp falls to
  this unit by POSITION, §7 names the leg and AC8 observes it. LOW "the charter is cited at line 121":
  corrected to `AGENTS.md:195`, with the section bounds stated so the next reader can re-derive it.
  Park P3 marked RESOLVED (owner, 2026-08-16) in §8. One stale figure found while folding and
  corrected: §4 Rollout said `aRuledFrontispiece` carries 65 non-blank lines after its closing marker;
  re-measured at `base 96141aed` it is 134, which is what a count quoted from an earlier pass of a
  file the build itself is growing does.

## 10. Reuse audit

Recall terms used, recorded so a resumed session re-runs the same query: `gate leg manifest run-gates
coverage key charter handkept pin inventory dossier baseline shrink-only guard`. The
`tools/codebase-map/reuse_lookup.py` pass over that query returned `compute_coverage` in
`map_lib.py`, the `gate-legs` inventory keys themselves, and the affordance seams of the playbook and
govkit dossiers. It returned no seam for "check a markdown file's section order", which is consistent
with `TOOL-aRuledFrontispiece-1` being the first place such a predicate exists in this corpus.

| Behaviour needed | Existing seam | Decision |
|---|---|---|
| run a predicate as a bar leg | a row in `tools/gate-legs.json`, iterated by `tools/run-gates.sh` | REUSE unchanged — the runner is a thin iterator and a leg is data |
| the slot predicate itself | the parameterised `apply_region` and slot walk `TOOL-aRuledFrontispiece-1` adds to `gen_build_index.py` | REUSE — a fourth verb over the same predicate, never a second copy |
| declare a gate structural rather than semantic | the header of `tools/check-playbook-parity.sh` at line 15 | REUSE THE SHAPE — the verb's header states the same boundary in the same place |
| persist a failing leg's own output | `leg_log` and `runleg` in `tools/run-gates.sh` | REUSE unchanged — every leg gets this for free |
| claim a new inventory key | a `[claims]` block in a dossier under `memory/map/features/` | REUSE unchanged — the same shape `build-method.md` uses for its two gate-leg keys |
| record that a watched file changed | the `last-audit` stamp in `memory/guides/SESSION-KICKOFF.md`, audited by `skills/session-kickoff/manifest-check.sh` | REUSE unchanged — S8 re-stamps under the existing rule; the ratchet needs no edit to see a new watched change |
