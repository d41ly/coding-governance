# TOOL-aRuledFrontispiece-6 — the slot contract becomes a leg of its own on the merge bar

**Status:** OPEN · rev-1 · 2026-08-16 · node a · Tier-2 · base 96141aed · streams tooling

## 1. Goal

Put the slot contract on the merge bar as a leg with its own name and its own exit code, so a README
that violates it produces a verdict naming the contract rather than one line inside a twenty-check
aggregate. The predicate belongs to `TOOL-aRuledFrontispiece-1`; this unit makes it binding and pays
the three registry costs a new leg incurs.

## 2. Scope (IN)

- **S1** — a new row in `tools/gate-legs.json` named `build-README slot contract`. The name becomes a
  `gate-legs` inventory key in the codebase map the moment it lands, so it is chosen once here and
  not adjusted later; a rename is the delete-plus-add this build is avoiding.
- **S2** — the row's `argv` is `["python3", "tools/memory-tree/gen_build_index.py", "--check-format"]`.
  A new verb on the engine unit 1 already changes, not a new script, so the predicate stays
  single-sourced.
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

## 3. Non-goals (OUT)

- Judging prose. S4 is the boundary: section order and marker placement, never content.
- Defining the slot contract or the refusal messages. Unit 1 owns both; this unit calls them.
- Retrofitting the corpus. Unit 10 owns the re-render and the kit version bump.
- Growing `tools/memory-tree/check-memory-hygiene.sh` by a check. Fork 2 rejected that and §4 prices
  it.
- Shipping the leg to adopters through a `[[gate_leg]]` block in `tools/memory-tree/kit.toml`. An
  adopter's corpus has not been retrofitted, and a kit that installs a gate their tree fails hands
  them a red bar on day one. It is a follow-up once the retrofit is a kit-side migration.
- A `--fix` verb. Moving a marker pair is an authored edit and a renderer must not make it.

## 4. Design

### Inventory

A leg is data in four registries, and three of them fail in a way the leg's own author does not see.

| Registry | What it demands | What a skip costs |
|---|---|---|
| `tools/gate-legs.json` | a non-empty `name`, `argv` of length ≥ 2, `argv[0]` in `bash python python3 node` | `tools/run-gates.test.sh` arm 1 reds |
| `AGENTS.md` `## The gate suite` | the row's argv path present as a substring of that section | `python tools/drift-audit/drift_report.py --check` reds |
| `memory/map/features/` | the row's display NAME claimed by a dossier | `python3 tools/codebase-map/test_codebase_map.py` reds UNCLAIMED |
| `tools/govkit/registry.toml` | nothing — `tools/gate-legs.json` is a declared exemption | — |

The charter requirement is mechanical, not editorial. `_charter_mentions_every_leg` at
`tools/drift-audit/drift_signals.py:104` reads the manifest, takes each leg's argv elements
containing `/`, and asks whether any of them appears inside the section matched by
`^##\s+The gate suite.*?$(.*?)^##\s`. `signal_handkept` at `drift_report.py:392` scores the gap as
`actual - claims` over that one probe, and `--check` exits 1 on `value > pin` with
`PINS["handkept_inventories_disagreeing_with_source"] = 0` at `drift_signals.py:177`. Zero slack: one
leg the charter does not name reds the bar, and that leg is `drift-audit records`, which is on it.

Verified at `base 96141aed`, and stated because it changes what S6 is FOR rather than whether it
holds: the string `tools/memory-tree/gen_build_index.py` is already inside that section, at
`AGENTS.md:121`, in the self-test-legs bullet. So the argv chosen in S2 satisfies the signal without
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

The manifest row is the LAST thing this unit lands, because a leg cannot land red, and the corpus is
not conformant today.

Measured at `base 96141aed` over the 39 folders under `memory/builds/`, counting non-blank lines
after each README's `<!-- /gen:build-index -->`: five carry top-level content there —
`aRuledFrontispiece` (65 lines), `aSiftedPlaybook` (120), `cTracedPromise` (23), `cKeyedLaunchpad`
(11) and `aTimedTurnstile` (10). Under unit 1's S4 each is a violation. Unit 1's Migration section
states that every build README today already has front matter, title, prose and index in the required
order; for those five that claim is false, and unit 1 says the corpus verification belongs to unit 10
rather than to that sentence.

The remedy is mechanical and small: relocate the generated region's marker pair to the end of the
file. The rendered bytes do not change, so `--check` stays clean across the move. This unit performs
those five moves in the commit that adds the manifest row, on the ground that the build README's
build-level rules declare unit 10's retrofit commit a PURE re-render reviewable as `--check` output,
and moving an authored marker pair is not a re-render. If the build's ordering section would rather
give those five files to unit 10, then the manifest row moves with them and this unit ships the verb,
its arms, the charter bullet and the dossier claim alone. Either split works; what does not work is
adding the row while five READMEs fail the predicate.

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
`.memory-tree.conf`. The script would then shell out to the engine anyway, because unit 1 puts the
predicate in Python. That is three new files and a ratchet row to reach a predicate one argv element
already reaches.

### Files touched (estimate)

`tools/gate-legs.json` · `tools/memory-tree/gen_build_index.py` (the fourth verb, the mode tuple and
the usage line) · its `--selftest` arms · `AGENTS.md` `## The gate suite` · one dossier under
`memory/map/features/` · `memory/map/generated/` re-rendered by the map's own regen command · the
five build READMEs named in Rollout.

## 5. Production-readiness checklist

- security — N/A. The verb reads tracked files the render already reads and writes nothing.
- perf / scale — one read pass over 39 build READMEs, the same set `--check` already opens.
- a11y — N/A. No user-facing surface.
- i18n — N/A. The markers are ASCII literals.
- error / empty / loading states — a repo with no folder under `memory/builds/` must exit 0, not fail
  on an empty population; a young tree is a legitimate empty and not a disarmed gate.
- observability — the leg's whole output is persisted at `<git-dir>/gate-logs/` by the runner and a
  RED run's durable summary carries a `log:` pointer at it.
- risks — the leg overlaps check 9 wherever unit 1's refusals also fire inside `--check`, so a
  violation can red two legs at once; that is duplicated reporting, never a duplicated predicate.
  The larger risk is the Rollout ordering: a manifest row added before the five READMEs are moved
  lands a red leg on the default branch.
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

## 7. Gates

`bash tools/run-gates.test.sh` · `python tools/drift-audit/drift_report.py --check` ·
`python3 tools/codebase-map/test_codebase_map.py` · `python3 tools/memory-tree/gen_build_index.py --selftest` ·
`python tools/memory-tree/check-arms.py --check` · `bash tools/memory-tree/check-memory-hygiene.sh` ·
`bash tools/memory-tree/check-verdict-epoch.sh`, which this unit does not discharge — the verb moves a
behaviour-bearing line of a scanned delegate, and unit 10 carries the one bump the whole build gets.

## 8. Open questions

none — fork 2 fixed where this check rides, and the two questions this unit would otherwise put are
recorded as measured facts instead: §4 Rollout names the five build READMEs that must be conformant
before the manifest row may land and states which split this unit takes, and §4 Inventory records
that the charter requirement is already satisfied by the argv chosen in S2.

## 9. Revision log

- rev-1 · 2026-08-16 · initial draft.

## 10. Reuse audit

Recall terms used, recorded so a resumed session re-runs the same query: `gate leg manifest run-gates
coverage key charter handkept pin inventory dossier baseline shrink-only guard`. The
`tools/codebase-map/reuse_lookup.py` pass over that query returned `compute_coverage` in
`map_lib.py`, the `gate-legs` inventory keys themselves, and the affordance seams of the playbook and
govkit dossiers. It returned no seam for "check a markdown file's section order", which is consistent
with unit 1 being the first place such a predicate exists in this corpus.

| Behaviour needed | Existing seam | Decision |
|---|---|---|
| run a predicate as a bar leg | a row in `tools/gate-legs.json`, iterated by `tools/run-gates.sh` | REUSE unchanged — the runner is a thin iterator and a leg is data |
| the slot predicate itself | the parameterised `apply_region` and slot walk unit 1 adds to `gen_build_index.py` | REUSE — a fourth verb over the same predicate, never a second copy |
| declare a gate structural rather than semantic | the header of `tools/check-playbook-parity.sh` at line 15 | REUSE THE SHAPE — the verb's header states the same boundary in the same place |
| persist a failing leg's own output | `leg_log` and `runleg` in `tools/run-gates.sh` | REUSE unchanged — every leg gets this for free |
| claim a new inventory key | a `[claims]` block in a dossier under `memory/map/features/` | REUSE unchanged — the same shape `build-method.md` uses for its two gate-leg keys |
