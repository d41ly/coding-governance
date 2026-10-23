# PLAY-dOrderedCharter-50 — the rows a new leg, key or retirement owes are written by the pass that creates them, through one owed-rows probe

**Status:** OPEN · rev-1 · 2026-10-24 · node d · Tier-2 · base ce13efbe · streams playbook · order 10 · advances PLAY-dOrderedCharter-38

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-24-build-PLAY-dOrderedCharter-50-deviation-501.md](../build/2026-10-24-build-PLAY-dOrderedCharter-50-deviation-501.md) | deviation | — |
| [2026-10-24-build-PLAY-dOrderedCharter-50-promoted-fix-return.md](../build/2026-10-24-build-PLAY-dOrderedCharter-50-promoted-fix-return.md) | research | PLAY-dOrderedCharter-51 PLAY-dOrderedCharter-52 PLAY-dOrderedCharter-54 PLAY-dOrderedCharter-55 |
| [2026-10-24-prompt-PLAY-dOrderedCharter-50-promoted-fix-brief.md](../prompts/2026-10-24-prompt-PLAY-dOrderedCharter-50-promoted-fix-brief.md) | research | PLAY-dOrderedCharter-49 PLAY-dOrderedCharter-51 PLAY-dOrderedCharter-52 PLAY-dOrderedCharter-54 PLAY-dOrderedCharter-55 |

<!-- /gen:spec-records -->

## 1. Goal

The round-2 spec audit (`memory/builds/dOrderedCharter/reviews/2026-10-24-review-PLAY-dOrderedCharter-39-spec-audit.md`)
confirmed **finding 23 at HIGH**, its item **H1**. `PLAY-dOrderedCharter-49` (order 39) creates, at
its own pass, rows that units from order 9 onward need at theirs: the `enforces` key in the canary's
closed key sets, which unit 7 writes at order 11; the subject-pins, descriptor and dossier rows of the
legs units 26, 25, 7, 13, 12, 20, 15 and 3 add; the size row unit 3 crosses; and the registry rows
naming the directory unit 31 deletes. Units 16, 19 and 28 already list their own rows. Every tree
between order 9 and order 39 therefore reds the canary, `govkit selfcheck` or a registry leg, and a
builder either lands red or improvises unit 49's work early. This unit gives the build one probe that
derives, from a pass's own diff, every row that pass owes; teaches the canary `enforces` before unit 7
lands; writes unit 26's rows; and hands the rule to every later leg-adding or retiring unit, so unit
49's bar-keeping items observe rows rather than create them.

## 2. Scope (IN)

- **S1** — The key. Both closed key sets of `tools/run-gates/run-gates.test.sh`, the arm's `KNOWN`
  (`:244`) and `keyset_probe`'s copy (`:580`), gain `enforces`, with a control pair in the shape of
  `signature`'s (`:589-597`): a row carrying `enforces` passes, a near-miss spelling of it reds. It
  lands at order 10, before unit 7 S2 writes the key at order 11. This supersedes
  `PLAY-dOrderedCharter-49` S2 as the act that creates the key; 49's AC2 observes it. Observed by AC1.
- **S2** — The probe, `python tools/run-gates/owed_rows.py --base <rev>`. It derives five populations
  from `<rev>` against the working tree and prints one `owed — <file> <- <row>` line per row missing,
  exit 1 when any is owed, 0 with a one-line count when none is, 2 on a refusal (a `<rev>` that does
  not resolve, or two `KNOWN` copies that disagree). Observed by AC2 and AC3.

  | Population | Derived as | Owed |
  |---|---|---|
  | leg added | names in `tools/gate-legs.json` absent at `<rev>` | a `tools/govkit/subject-pins.tsv` row; a descriptor `[[gate_leg]]` row or a `tools/govkit/registry.toml` `[[exempt_leg]]` row; a claim in a dossier under `memory/map/features/` |
  | leg removed | names at `<rev>` absent now | no row of `subject-pins.tsv`, `memory/map/baseline.toml` or `tools/run-gates/selftest-budgets.txt` naming it |
  | key | every key of every row of `tools/gate-legs.json` | membership in each `KNOWN` copy of `run-gates.test.sh` |
  | path deleted | `git diff --name-only --diff-filter=D <rev>` | no row of `memory/project/spawn-idiom-sites.txt`, `memory/project/testsuite-count-waivers.txt` or `memory/project/unarmed-branches.txt` naming it |
  | size | each path changed since `<rev>` holding a `tools/template-size-limits.txt` row | its CR-stripped bytes within the row, else the row's raise on that file's own terms or a trim |

  A leg added also owes a `tools/run-gates/ceiling-evidence.txt` row, which only a measured bar run
  writes (`derive-ceilings.py --write`, that file's header). The probe prints it as a `deferred —` line
  that leaves the exit unchanged; the main loop's close writes it.
  **Readers:** by name: none — this item retires nothing; a leg removed and a path deleted are
  populations the probe derives from a pass's diff, and only the probe reads them. by value:
  NO VALUE READERS — the probe reports presence and changes no value any reader holds.
- **S3** — Its readers are the existing ones. Pins are read by the pin file's first column as
  `selfcheck` reads it (`tools/govkit/govkit.py:3005-3014`); claimed legs through `read_descriptors`
  (`:13238`) and the registry's `[[exempt_leg]]` rows; dossier claims through the codebase-map kit's
  claim reader (`claimant_index`, `tools/codebase-map/map_lib.py:1613`), reached through
  `resolve_kit_dir`; size rows by the two-sidecar grammar `read_size_ceilings` documents
  (`tools/check-spec-tokens.py:1248`). The probe mints no predicate a leg already owns: it reports
  presence, and each leg still grades its own row. Observed by AC2.
- **S4** — `--selftest`: a scratch repository plants each population's failing case, a leg added with
  no pin row, a leg removed whose budget row stays, a key outside `KNOWN`, a deleted script named by
  `unarmed-branches.txt`, a file grown past its size row, and a tree owing nothing, and asserts the
  exit and the named row of each. Observed by AC3.
  **Readers:** by name: none — this item retires nothing; the removed leg and the deleted script are
  failing cases planted in a scratch repository. by value: NO VALUE READERS — the plants live and end
  with the scratch repository.
- **S5** — Unit 26's rows. `tags positional selftest`, the leg `PLAY-dOrderedCharter-26` S7 adds at
  order 9, gets its subject-pins row, the descriptor row that claims it beside unit 19's `tags`
  legs, and its dossier claim in `memory/map/features/playbook.md`, at this pass. Observed by AC4.
- **S6** — The rule, handed off. Each unit this spec's §3 hands off to runs
  `python tools/run-gates/owed_rows.py --base HEAD` as the last probe of its pass, before its commit,
  and writes every owed row in that commit. A subject-pins row is regenerated by
  `python tools/govkit/govkit.py selfcheck --write`, the writer the pin failure names
  (`tools/govkit/govkit.py:3019-3022`); where the pass's role refuses that command, the pass returns
  the row to the main loop, which writes it before the next dispatch. Observed by AC5.
- **S7** — Unit 49's bar-keeping items observe. `PLAY-dOrderedCharter-49` S2 to S5, S30, S31 and S49
  find their rows written by the passes that needed them; 49's pass creates none, and its AC2, AC3,
  AC23 and AC40 read the tree as they are written. Observed by AC5 and AC6.

## 3. Non-goals (OUT)

- The legs, keys and deletions themselves: each is its own unit's.
- `ceiling-evidence.txt` rows: a measured run writes them, at the close.
- One source for the canary's key set: the two literal copies are a shipped schema arm's, and the
  probe refuses when they disagree rather than re-homing them.
- Units 16, 19 and 28, whose specs already list their rows.

### Edges

- **consumes-from** `PLAY-dOrderedCharter-26` — the `tags positional selftest` leg, whose pin, descriptor and dossier rows S5 writes; without it S5 has no leg to keep
- **hands-off** `PLAY-dOrderedCharter-25` — its pass runs the probe and writes the rows of `tags bundle selftest` (S6)
- **hands-off** `PLAY-dOrderedCharter-7` — its pass finds `enforces` already in both key sets and writes its new legs' rows (S1, S6)
- **hands-off** `PLAY-dOrderedCharter-13` — its pass writes the rows of its ladder leg (S6)
- **hands-off** `PLAY-dOrderedCharter-12` — its pass writes the rows of its grammar leg (S6)
- **hands-off** `PLAY-dOrderedCharter-20` — its pass writes the rows of its render legs (S6)
- **hands-off** `PLAY-dOrderedCharter-15` — its pass writes the rows of its manifest-checks leg (S6)
- **hands-off** `PLAY-dOrderedCharter-3` — its pass writes the rows of its envelope leg and the size rows its envelopes cross (S6)
- **hands-off** `PLAY-dOrderedCharter-31` — its pass removes every registry row naming the directory it deletes and every row of the legs it retires (S6)
- **hands-off** `PLAY-dOrderedCharter-49` — S2 to S5, S30, S31 and S49 observe rows the earlier passes wrote and create none (S7)
- **hands-off** `PLAY-dOrderedCharter-55` — the round-2 minors that run the probe: the kept wiring leg's rows and `edge_checks.py`'s deletion (ids 1, 6)

## 4. Design

### Evidence

Read at `ce13efbe`. The canary's arm holds `KNOWN` as a closed literal at
`tools/run-gates/run-gates.test.sh:244` and sends every other key to `stray`, and `keyset_probe`
repeats it at `:580`. `selfcheck` reds "a NEW leg" with no pin row (`tools/govkit/govkit.py:3019-3022`)
and a leg "claimed by no descriptor and carried by no [[exempt_leg]]" (`:2944-2946`, check 7h).
`tools/run-gates/ceiling-evidence.txt`'s header says it is generated from run records and never typed.
`.claude/skills/unattended/SKILL.md` has its 10240-byte row at `tools/template-size-limits.txt:151`.
The map's baseline is shrink-only (`tools/codebase-map/test_codebase_map.py:155`), so a new leg is
claimed by a dossier, never baselined. Of the leg-adding specs, 16, 19, 28, 29, 31 and 39 list
`subject-pins.tsv` under Files touched; 26, 25, 7, 13, 12, 20, 15 and 3 do not.

### Order

Order 10. The unit this repairs first is `PLAY-dOrderedCharter-26` at order 9, the earliest unit in
build order whose pass adds a leg without its rows; S5 writes them one step later. Order 10 is also
the last order before unit 7 writes `enforces` at 11, so S1 lands first, and every unit S6 hands off
to sits at order 10 or later, which check 12's edge-order arm requires of a hands-off.
`PLAY-dOrderedCharter-25` shares order 10 and consumes from this unit, so the dispatch runs this unit
first.

### Inventory

Minted: `tools/run-gates/owed_rows.py`, its `--base` and `--selftest` flags, the line prefixes
`owed —` and `deferred —`, and the canary's `enforces` control pair. Naming cells: `lexicon naming
predicates` grades the Python names.

### Files touched (estimate)

- `tools/run-gates/owed_rows.py` (new)
- `tools/run-gates/run-gates.test.sh`
- `tools/govkit/subject-pins.tsv`
- `tools/govkit/registry.toml`
- `tools/playbook/kit.toml`
- `memory/map/features/playbook.md`

### Rollout

Live at landing, order 10, after unit 26 at order 9. A probe, not a leg: no bar runs it, and no
adopter receives it.

### Alternatives rejected

- **Unit 49 creating the rows at order 39**, the current design: the finding.
- **A build-order replay of the bar after each pass**: it runs the bar inside a pass, which BUILD-METHOD
  M6 forbids, and it reports a red rather than naming the row.
- **Folding each row into its unit's spec**: the exit disposes a finding by promotion and never by a
  fold (BUILD-METHOD M4).

## 5. Production-readiness checklist

- security: read-only probe; S5 writes three tracked rows.
- perf / scale: two reads of `tools/gate-legs.json`, one `git diff`, and one parse of each registry.
- error / empty / loading states: an unresolvable `--base` or disagreeing `KNOWN` copies exit 2 naming
  which; an absent registry file is a refusal, never an empty population.
- observability: every owed row is one line naming the file and the row; deferred rows are listed
  apart.
- risks: the probe reports presence only, so a pin row with a wrong subject passes it and still reds
  `govkit selfcheck`; the leg remains the grader. The canary suite's arm count grows by two, against
  its budget row in `tools/run-gates/selftest-budgets.txt`, measured at the close.
- testing: AC1 to AC6; S4's fixtures are the probe's own.
- migration: none.
- user docs: none; the probe's docstring names the five populations.

## 6. Acceptance criteria

- **AC1** — When `git grep -n '"enforces"' -- tools/run-gates/run-gates.test.sh` runs after this pass,
  both `KNOWN` lines carry it, and the control pair passes a row carrying `enforces` and fails
  `enforce`.
  Red when: a leg row carrying `enforces` reds the canary at unit 7's pass.
- **AC2** — When `python owed_rows.py --base ce13efbe` runs from `tools/run-gates/` over this
  build's tree after this pass, it exits 0 with only `deferred —` lines, each naming a leg added since
  the base.
  Red when: a leg added since the base lacks a pin, claim or dossier row and the probe exits 0.
- **AC3** — When `python owed_rows.py --selftest` runs, each of S4's six fixtures gives its stated exit
  and names its row, and the owing-nothing tree exits 0.
  Red when: a population's failing case exits 0, or the control tree exits 1.
- **AC4** — When `git grep -n "tags positional selftest" -- tools/govkit/subject-pins.tsv tools/playbook/kit.toml memory/map/features/playbook.md`
  runs after this pass, each file names the leg.
  Red when: unit 26's leg is still unpinned, unclaimed or undocumented.
- **AC5** — When `git grep -n -E "consumes-from.*PLAY-dOrderedCharter-50" -- memory/builds/dOrderedCharter/spec/`
  runs, it prints one line in each of the ten specs this unit hands off to.
  Red when: a handed-off unit's spec does not carry the rule.
- **AC6** — When the probe runs with `--base` at the parent of each handed-off unit's pass commit,
  replayed after the last of them lands, each run exits 0.
  Red when: a unit landed a leg, key or deletion without its rows.
  cost: one probe per handed-off commit, seconds each.

## 7. Gates

`run-gates canary` · `govkit selfcheck` · `govkit selftest` · `govkit acceptance matrix` · `govkit refusal join` · `codebase-map coverage + freshness` · `recall floor` · `recall floor arms` · `playbook render selftest` · `lexicon naming predicates` · `spec tokens (a spec's own names resolve)`

New arm: tools/run-gates/run-gates.test.sh · covers AC1 AC3 · the `enforces` control pair, staged by removing the key from one `KNOWN` copy, and `owed_rows.py --selftest`, staged by planting a leg with no pin row · none

## 8. Open questions

- **F1 — Which binding line does a unit the spec audit promoted carry?** Options: (a) `**Derived:**`
  naming `PLAY-dClosedLoop-2`, as the tree's promoted specs do; (b) none; (c) parts of the repaired
  units' clauses. (b) reds unbound and (c) splits clauses this unit does not carry. RESOLVED (agent,
  2026-10-24, delegated): (a), rung 3. widens: none · relaxes: none
- **F2 — Where the bar-keeping rows are written.** Options: (a) by the pass that creates the need, one
  probe deriving them and a hand-off edge carrying the rule; (b) by unit 49 at order 39, as written;
  (c) by a replay of the bar after each pass. (b) is the finding and (c) runs the bar in a pass.
  RESOLVED (agent, 2026-10-24, delegated): (a), rung 3. widens: none · relaxes: none

## 9. Revision log

- rev-1 · 2026-10-24 · initial draft, promoted from the round-2 spec audit's finding 23 (HIGH, item H1).

## 10. Reuse audit

The seams extended are the canary's key-set arm (`tools/run-gates/run-gates.test.sh:244`, `:580`),
`selfcheck`'s pin read and writer (`tools/govkit/govkit.py:3005-3022`), `read_descriptors` (`:13238`),
the map's `claimant_index` (`tools/codebase-map/map_lib.py:1613`) and the size sidecars' grammar
(`tools/check-spec-tokens.py:1248`); the probe composes their reads and mints no rule. `python
tools/codebase-map/reuse_lookup.py "list the registry rows a newly added gate leg still owes"` ranked
`rows`, `row`, `legs` and `leg` by name stem, test-suite helpers with no owed-row logic, so no
existing seam fits the derivation itself and it is new code over the readers above. The recall query
returned DEPL-aBenchedProbe-1, TOOL-dUnstalledConvoy-26 and TOOL-aWokenSentinel-27 on how a new leg
earns its pin and descriptor rows.

Recall terms used: `python tools/memory-recall/query.py "how does a new gate leg get its subject pin, descriptor claim and dossier line" --terms "subject-pins selfcheck write exempt_leg gate_leg descriptor dossier new leg reds canary KNOWN"`
