# TOOL-dWitnessedBar-45 — the leg factory runs in a tree with no govkit: its generated row stays gov's, and its adopter verbs import no govkit

**Status:** DEFERRED · rev-4 · 2026-11-19 · node d · Tier-2 · base cdfbd1cf · streams tooling · order 9 · advances TOOL-dWitnessedBar-31

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-25-build-TOOL-dWitnessedBar-1-agent-ledger.md](../build/2026-10-25-build-TOOL-dWitnessedBar-1-agent-ledger.md) | journal | TOOL-dWitnessedBar-1 TOOL-dWitnessedBar-2 TOOL-dWitnessedBar-3 TOOL-dWitnessedBar-4 TOOL-dWitnessedBar-5 TOOL-dWitnessedBar-6 TOOL-dWitnessedBar-7 TOOL-dWitnessedBar-8 TOOL-dWitnessedBar-9 TOOL-dWitnessedBar-10 TOOL-dWitnessedBar-11 TOOL-dWitnessedBar-12 TOOL-dWitnessedBar-13 TOOL-dWitnessedBar-14 TOOL-dWitnessedBar-15 TOOL-dWitnessedBar-16 TOOL-dWitnessedBar-17 TOOL-dWitnessedBar-18 TOOL-dWitnessedBar-19 TOOL-dWitnessedBar-20 TOOL-dWitnessedBar-21 TOOL-dWitnessedBar-22 TOOL-dWitnessedBar-23 TOOL-dWitnessedBar-24 TOOL-dWitnessedBar-25 TOOL-dWitnessedBar-26 TOOL-dWitnessedBar-27 TOOL-dWitnessedBar-28 TOOL-dWitnessedBar-29 TOOL-dWitnessedBar-30 TOOL-dWitnessedBar-40 TOOL-dWitnessedBar-41 TOOL-dWitnessedBar-42 TOOL-dWitnessedBar-43 TOOL-dWitnessedBar-44 TOOL-dWitnessedBar-46 TOOL-dWitnessedBar-47 TOOL-dWitnessedBar-48 TOOL-dWitnessedBar-49 TOOL-dWitnessedBar-50 TOOL-dWitnessedBar-51 TOOL-dWitnessedBar-52 TOOL-dWitnessedBar-53 TOOL-dWitnessedBar-54 TOOL-dWitnessedBar-55 TOOL-dWitnessedBar-56 TOOL-dWitnessedBar-57 TOOL-dWitnessedBar-58 TOOL-dWitnessedBar-59 TOOL-dWitnessedBar-60 TOOL-dWitnessedBar-61 TOOL-dWitnessedBar-62 TOOL-dWitnessedBar-63 TOOL-dWitnessedBar-64 TOOL-dWitnessedBar-65 TOOL-dWitnessedBar-66 TOOL-dWitnessedBar-67 TOOL-dWitnessedBar-68 TOOL-dWitnessedBar-69 TOOL-dWitnessedBar-70 TOOL-dWitnessedBar-71 TOOL-dWitnessedBar-72 TOOL-dWitnessedBar-73 TOOL-dWitnessedBar-74 TOOL-dWitnessedBar-75 TOOL-dWitnessedBar-76 TOOL-dWitnessedBar-77 TOOL-dWitnessedBar-78 TOOL-dWitnessedBar-79 TOOL-dWitnessedBar-80 TOOL-dWitnessedBar-81 TOOL-dWitnessedBar-82 TOOL-dWitnessedBar-83 TOOL-dWitnessedBar-84 TOOL-dWitnessedBar-85 TOOL-dWitnessedBar-86 TOOL-dWitnessedBar-87 TOOL-dWitnessedBar-88 TOOL-dWitnessedBar-89 TOOL-dWitnessedBar-90 TOOL-dWitnessedBar-91 TOOL-dWitnessedBar-92 TOOL-dWitnessedBar-93 TOOL-dWitnessedBar-94 TOOL-dWitnessedBar-95 TOOL-dWitnessedBar-96 TOOL-dWitnessedBar-97 |
| [2026-10-25-build-TOOL-dWitnessedBar-45-deviation-451.md](../build/2026-10-25-build-TOOL-dWitnessedBar-45-deviation-451.md) | deviation | — |
| [2026-11-19-prompt-TOOL-dWitnessedBar-14-reground-3-brief.md](../prompts/2026-11-19-prompt-TOOL-dWitnessedBar-14-reground-3-brief.md) | journal | TOOL-dWitnessedBar-14 TOOL-dWitnessedBar-54 |
| [2026-11-19-prompt-TOOL-dWitnessedBar-14-reground-brief.md](../prompts/2026-11-19-prompt-TOOL-dWitnessedBar-14-reground-brief.md) | journal | TOOL-dWitnessedBar-14 |
| [2026-10-25-review-TOOL-dWitnessedBar-40-spec-audit-round1.md](../reviews/2026-10-25-review-TOOL-dWitnessedBar-40-spec-audit-round1.md) | spec-audit | TOOL-dWitnessedBar-48 TOOL-dWitnessedBar-49 TOOL-dWitnessedBar-50 TOOL-dWitnessedBar-47 TOOL-dWitnessedBar-46 TOOL-dWitnessedBar-40 TOOL-dWitnessedBar-42 TOOL-dWitnessedBar-44 TOOL-dWitnessedBar-41 TOOL-dWitnessedBar-43 TOOL-dWitnessedBar-51 |

<!-- /gen:spec-records -->

## 1. Goal

The round-1 spec audit (`memory/builds/dWitnessedBar/reviews/2026-10-25-review-TOOL-dWitnessedBar-1-spec-audit-round1.md`)
confirmed finding **id 33 at HIGH**, its item **H6**, alone in that item. `TOOL-dWitnessedBar-11` S2 puts
the factory's `[[generated]]` row in `tools/run-gates/kit.toml`, which ships (`include = "**"`,
`tools/run-gates/kit.toml@4d1909b97cfa:23`), and `regen.py --check` reads every tracked descriptor and runs before the
first leg. `leg_factory.py` imports govkit's `read_descriptors` and `resolve_tokens`, and govkit never
reaches an adopter. Once run-gates updates, every adopter's bar fails at stage 1, and
`TOOL-dWitnessedBar-28` S8's `leg sources` leg (`leg_factory.py --sources`) hits the same import failure.
This unit takes the skeptic's corrected fix. It repairs `TOOL-dWitnessedBar-11`.

## 2. Scope (IN)

- **S1** — A gov-only row. `regen.py`'s `when` gains a second form, `exists:<path>`, its tokens resolved
  as a row's argv tokens are, holding when that path exists in the tree. The factory's `[[generated]]`
  row carries `when = "exists:{prefix}/govkit/govkit.py"`, so in a tree with no govkit regen skips it
  and lists it skipped. Today `tools/run-gates/regen.py#build_items` passes over a `[[generated]]` row
  whose `when` does not hold without adding it to `skipped`, and `tools/run-gates/regen.py#print_items`
  prints every skipped entry as one that carries no stage. So a row a `when` skips joins `skipped`, and
  each entry carries its own reason, printed `its when <when> does not hold` for such a row. Observed
  by AC1.
- **S2** — No import at load. `leg_factory.py` imports at module level only the standard library and
  two shipped run-gates siblings: `regen`, and `pass_legs`, whose rule and render unit 11 §4 step 5
  sets `pass_leg` through. Each of the two imports only the standard library (§4 Evidence). govkit
  is loaded inside the verbs that need it, through one function `load_govkit(root)`. It finds govkit
  through the inline `resolve_kit_dir` copy unit 11 §10 carries, as
  `tools/run-gates/owed_rows.py#load_readers` does. Where govkit is absent it exits 2 with that
  lookup's `LookupError` line, which names the places looked. Observed by AC2.
- **S3** — The adopter verbs. Every verb a tree with no govkit runs reads descriptors through
  `regen.read_descriptors` and resolves tokens through `regen.resolve_argv`, and never calls
  `load_govkit`: `--sources` and `--legacy-rows` (`TOOL-dWitnessedBar-28`), and `--conform`, which
  unit 28 S3 makes a fixed row of an adopter's composition. Under no govkit, `--conform` runs its other
  field arms over the `[[gate_leg]]` rows of the target's descriptors. It prints
  `fresh: not graded here — no govkit`, since the render the `fresh` arm compares is gov's, and
  `enforces: not graded here — no govkit` (§8 F4). What it does not read there: the registry's
  `[[exempt_leg]]` rows, which live in `tools/govkit/registry.toml` and never reach an adopter; and
  the flat entries' descriptors, which the playbook kit lands as `{prefix}/playbook/<entry>.kit.toml`
  (`tools/playbook/kit.toml`, its flat-entry `[[files]]` rules). `regen.read_descriptors` reads only
  `*/kit.toml` one directory below the tool root, so it reads none of those descriptors. Observed by
  AC2 and AC3.
- **S4** — The gov verbs refuse plainly. `--write`, `--check`, `--list` and `new` call `load_govkit` and,
  in a tree with no govkit, exit 2 with its message, never an import traceback. Observed by AC2.

## 3. Non-goals (OUT)

- The factory, its render, its gate and its declarations: `TOOL-dWitnessedBar-11`'s.
- The `--sources`, `--legacy-rows` and composition verbs themselves: `TOOL-dWitnessedBar-28`'s, which
  this unit only binds to the govkit-free path.
- Whether `gate-leg conformance` and `leg-factory selftest` are `[[gate_leg]]` or `[[exempt_leg]]` rows,
  and unit 11's AC3 restated for them: the minors batch's id 6 item (`TOOL-dWitnessedBar-51`).
- An inline copy of govkit's descriptor reader under a parity row: `regen.read_descriptors` already
  ships in the same kit, so a third reader is not written.

### Edges

- **consumes-from** `TOOL-dWitnessedBar-11` — `leg_factory.py`, its `[[generated]]` row and its verbs, which this unit makes runnable where govkit is absent
- **hands-off** `TOOL-dWitnessedBar-28` — the govkit-free path of S3, on which the `--sources`, `--legacy-rows` and composition verbs unit 28 adds must stay
- **hands-off** `TOOL-dWitnessedBar-54` — the `exists:` form and the factory row carrying it, whose two unmigrated readers unit 54 migrates (id 42)
- **hands-off** `TOOL-dWitnessedBar-56` — its arm in `adopt-run-gates.test.sh`, whose floor the verdict-boundary minors batch raises (id 37)
- **hands-off** `TOOL-dWitnessedBar-57` — the factory row's `exists:` `when`, under which the resolver and ledger minors batch observes `govkit selfcheck` (id 30)

## 4. Design

### Evidence

- `regen.py` reads every tracked `tools/*/kit.toml` (`tools/run-gates/regen.py#read_descriptors`),
  honours a row's `when = "<conf>:<KEY>=<value>"` (`tools/run-gates/regen.py#check_when`) and skips
  the row when it does not hold (`tools/run-gates/regen.py#build_items`), listing it nowhere.
- `regen.resolve_argv` (`tools/run-gates/regen.py#resolve_argv`) resolves the four tokens of
  `tools/run-gates/regen.py#TOKENS`, `{kit}`, `{prefix}`, `{memory_root}` and `{map_root}`, the
  tokens unit 11 §4 step 3 resolves.
- `regen.py` imports only the standard library at module level and runs `main` only under
  `__main__`, so a sibling may import it; it loads `profile_bar.py` only inside
  `tools/run-gates/regen.py#resolve_bash`. `pass_legs.py` imports only the standard library too, and
  ships: the run-gates descriptor withholds only its evidence file, `pass-leg-evidence.txt`.
- The inline `resolve_kit_dir` (`tools/run-gates/owed_rows.py#resolve_kit_dir`, the canonical copy
  in `tools/lib/resolve_kit_dir.py`) raises `LookupError` naming the receipt and the two probe paths
  it looked in, never a guessed prefix.
- An adopter holding the playbook kit receives each flat entry's descriptor beside the engine, as
  `{prefix}/playbook/<entry>.kit.toml` (`tools/playbook/kit.toml`, the rules under its "EVERY FLAT
  ENTRY'S DESCRIPTOR TRAVELS TOO" comment). It does not receive `core-pending.txt`, which the kit
  marks `project-owned` and writes empty at the target. At this spec's rev-1 (`dc75b671c`) the
  playbook kit shipped its own descriptor alone and no flat entry's.
- Unit 11's `enforces` arm reads gov's principle registry, practice catalogue and pending list
  (TOOL-dWitnessedBar-11 §4 "The gate"). The registry's `core meta-check` `[[exempt_leg]]` row keeps
  the leg that grades the same pair at gov, "the principles, legs and pending rows it grades are
  authored here" (`tools/govkit/registry.toml`, that row's `why`).
- `run-gates adopter e2e` runs `tools/run-gates/adopt-run-gates.test.sh`, the kit's own adopter suite.
- govkit is an `[[exempt]]` home and never installed at an adopter (`tools/govkit/registry.toml`, its
  `path = "{prefix}/govkit"` row).
- govkit selfcheck's `[[generated]]` arm (`tools/govkit/govkit.py#selfcheck`, its `_gwbad` test)
  refuses a `when` that does not fullmatch `<conf>:<KEY>=<value>`, so it refuses the `exists:` form
  until TOOL-dWitnessedBar-54 S2 widens it. The leg `govkit selfcheck` carries no `guard` in
  `tools/gate-legs.json`, so it runs on every bar (§8 F3).

### The `when` grammar

```
when = "<conf file>:<KEY>=<value>"     # today: holds when the conf's key reads value
when = "exists:<path>"                 # new: holds when the token-resolved path exists in the tree
```

A `when` naming neither form is a refusal, as a malformed one is today. Neither form runs a command.

### Inventory

Minted: the `exists:` form of `when`; `load_govkit`; the `fresh: not graded here — no govkit` and
`enforces: not graded here — no govkit` lines.
Naming cells: `load_govkit` is asked of `python tools/lexicon/lexicon.py --suggest load_govkit --as
py.function` at the pass.

### Migration

None for gov: govkit exists, so the row holds and every verb runs as unit 11 states.

### Rollout

Live at landing, before any adopter updates past unit 11. This unit and TOOL-dWitnessedBar-54 land
on local main in one merge, this unit's commit first, and the bar runs once over both, since
govkit selfcheck refuses the factory row's `exists:` `when` until unit 54 S2 lands (§8 F3).

### Files touched (estimate)

- `tools/run-gates/regen.py`
- `tools/run-gates/leg_factory.py`
- `tools/run-gates/kit.toml`
- `tools/run-gates/adopt-run-gates.test.sh`
- `tools/run-gates/README.md`

### Alternatives rejected

- **`.unattended.conf`'s `GENERATED_INDEXES`.** It is the unattended kit's key, read by
  `resolve_generated_indexes`, and an adopter of run-gates without that kit never reads it.
- **Withhold `leg_factory.py` from adopters.** Unit 28's `leg sources` leg runs it in every adopter.
- **An inline copy of govkit's reader.** A third descriptor reader where the kit already ships one.

## 5. Production-readiness checklist

- security — no new surface; `exists:` reads a path and runs nothing.
- perf / scale — one stat per row carrying the form.
- error / empty / loading states — a gov verb without govkit exits 2 naming the places it looked;
  `--conform` names each arm it did not grade.
- observability — `regen.py --list` names the skipped row.
- risks — `--conform` at an adopter grades the `[[gate_leg]]` rows of its `*/kit.toml` descriptors
  only, never the flat entries' copies under the playbook kit or the `fresh` and `enforces` arms; the
  lines say which arms.
- testing — AC1 to AC3 by fixture and the adopter suite; the arm of §7 at the close.
- migration — none.
- user docs — `tools/run-gates/README.md`'s regen section names the `exists:` form at the pass.

## 6. Acceptance criteria

- **AC1** — When `python regen.py --list` runs in a scratch tree made by `govkit.py apply --target <scratch>
  --kits run-gates` and committed, since regen reads tracked descriptors only, it names the factory's row skipped, and `python regen.py --check` there
  exits 0.
  Red when: the row has no `when`, so regen runs `leg_factory.py --check` and the adopter's bar refuses at
  stage 1.
  fixture: a scratch target under `%TEMP%/<short-name>`; the tree holds none.
- **AC2** — When `python -c "import leg_factory"` runs in that scratch tree's run-gates kit directory it
  exits 0, and `python leg_factory.py --write` there exits 2 naming the govkit paths it looked in; once
  `TOOL-dWitnessedBar-28` has added `--sources`, the same suite runs it there with no traceback.
  Red when: the module imports govkit at load, so every verb fails with `ModuleNotFoundError`.
- **AC3** — When `python leg_factory.py --conform` runs in the same scratch tree, it prints
  `fresh: not graded here — no govkit` and `enforces: not graded here — no govkit` and exits 0 over
  the target's untouched descriptors; in gov's tree it grades `fresh` and `enforces` as unit 11 states.
  Red when: `--conform` refuses or crashes where govkit is absent, or grades `enforces` against
  registries the target does not hold, so the fixed row reds every adopter.

## 7. Gates

`run-gates adopter e2e` · `run-gates wiring` · `run-gates canary` · `measure-legs selftest` · `govkit selfcheck` · `memory hygiene`

New arm: tools/run-gates/adopt-run-gates.test.sh · covers AC1 AC2 AC3 · a scratch target applied with the run-gates kit alone, running `regen.py --check`, the module import, `--write` and `--conform` there, staged red by removing the row's `when` · none

## 8. Open questions

- **F1 — Which binding line does a unit the spec audit promoted carry?** The carries join reds a chain
  spec carrying nothing and derived from nothing. Options: (a) `**Derived:**` naming
  `PLAY-dClosedLoop-2`; (b) a `part k/n` carry of `TOOL-dWitnessedBar-11`'s clause. (b) reds the parts
  join; veto 1 discards it. RESOLVED (agent, 2026-10-25, delegated): (a), rung 3, the precedent
  `TOOL-dDeclaredLoop-36` §8 F1 set. widens: none · relaxes: none
- **F2 — How does a shipped descriptor carry a gov-only row?** Options: (a) regen's `when` gains an
  `exists:` form naming govkit; (b) a gov-only descriptor home that never ships; (c) the factory's check
  declines with exit 0 where govkit is absent. (b) needs a new descriptor regen and govkit would both
  read; (c) is a check that passes over nothing in every adopter. RESOLVED (agent, 2026-10-25,
  delegated): (a), rung 3, an extension of the condition regen already honours. widens: none ·
  relaxes: none
- **F3 — How does this unit land green while govkit selfcheck refuses the `exists:` form?** The
  re-ground at `5e569d9c9` read `tools/govkit/govkit.py#selfcheck`: its `[[generated]]` arm refuses
  every `when` outside `<conf>:<KEY>=<value>`, and its leg runs on every bar. TOOL-dWitnessedBar-54 S2
  widens that arm, and its S3 parity arm needs this unit's `exists:` reading in `regen.py`, so neither
  unit lands green alone. Options: (a) the two land on local main in one merge, this unit's commit
  first, under one bar; (b) this unit's pass widens the selfcheck arm itself; (c) this unit lands
  alone and the bar reds until unit 54. (b) states unit 54 S2 in two specs, and (c) fails the bar
  every unit passes, veto 1. RESOLVED (agent, 2026-11-19, delegated): (a), rung 3, the one option
  that leaves each spec's scope as written and lands no red. widens: none · relaxes: none
- **F4 — What does `--conform`'s `enforces` arm do in a tree with no govkit?** Unit 11's gate table
  grades an empty `enforces` against gov's `core-pending.txt`, and each tag against gov's principle
  registry and practice catalogue (§4 Evidence). AC1's scratch holds the run-gates kit alone, so none
  of the three is there. An adopter holding the playbook kit has the two registries but an empty
  `core-pending.txt` of its own. Options: (a) the arm is gov's, as `fresh` is: under no govkit
  `--conform` prints `enforces: not graded here — no govkit` and skips it; (b) the arm runs wherever
  the playbook registries resolve and prints a not-graded line where they do not; (c) the arm runs
  unconditionally. (c) fails AC3 in AC1's scratch, which holds no registry, so veto 1 discards it.
  (b) reds an adopter holding the playbook kit on every gov leg unit 11 S6 leaves pending, since that
  adopter's own `core-pending.txt` is empty. That is the failure AC3's Red-when names, so veto 1
  discards (b) too. RESOLVED (agent, 2026-11-19, delegated): (a), the one survivor. Its reason
  matches the one the registry's `core meta-check` row gives for keeping that leg at gov: the pair it
  grades is authored there. widens: none · relaxes: none

## 9. Revision log

- rev-1 · 2026-10-25 · initial draft, promoted from the round-1 spec audit's id 33 (HIGH, item H6).
- rev-2 · 2026-10-25 · §3 · the Edges block gains the hands-off bullets mirroring the consumes-from
  edges of TOOL-dWitnessedBar-54, TOOL-dWitnessedBar-56, TOOL-dWitnessedBar-57, promoted by the
  round-1 spec audit of units 40 to 51; nothing else moved.
- rev-3 · 2026-11-19 · §1 · S1 · §4 Evidence, Rollout · §7 · §8 F3 · re-grounded at `5e569d9c9` per
  brief 2026-11-19-prompt-TOOL-dWitnessedBar-14-reground-brief: line citations become `path#symbol`
  or blob-pinned (the descriptor's `include = "**"` moved to line 23); S1 states that a `when`-skipped
  row joins regen's `skipped` list with its own reason, which `print_items` lacks today; govkit
  selfcheck's `when` arm, which refuses `exists:` until unit 54, joins the evidence and the leg line,
  and F3 lands the two units in one merge.
- rev-4 · 2026-11-19 · S2 · S3 · §4 Evidence, Inventory · §5 · AC2 · AC3 · §8 F4 · §10 · re-grounded at
  `4e5497fb7` per brief 2026-11-19-prompt-TOOL-dWitnessedBar-14-reground-3-brief, against
  TOOL-dWitnessedBar-11 rev-6 as the contract. S2's module-level imports now name `pass_legs`, which
  unit 11 §4 step 5 renders `pass_leg` through. `load_govkit` wraps unit 11's inline
  `resolve_kit_dir` and exits with its `LookupError` line. S3 states what an adopter's `--conform`
  does not read: the registry's exempt rows, and the flat-entry descriptors the playbook kit now
  ships under `{prefix}/playbook/`. Unit 11's `enforces` arm is gov's, as `fresh` is (F4), and AC3
  observes its line. Every other claim was re-read at HEAD and holds.

## 10. Reuse audit

The seams extended are `regen.py`'s row condition `check_when` and its shipped reader
`read_descriptors` with `resolve_argv`, which the factory reuses instead of importing govkit's.
`load_govkit` reuses the inline `resolve_kit_dir` lookup unit 11 already carries
(`tools/run-gates/owed_rows.py#load_readers` is the precedent), rather than a second path probe.
`python tools/codebase-map/reuse_lookup.py "skip a generated row when a gov-only tool is absent"`
ranked `rows`, `row`, `absent`, `skip`, `extract_row` and `resolve_generated_indexes`; the last is the
unattended kit's reader of `GENERATED_INDEXES`, rejected in §4, and none of the others conditions a row.

Recall terms used: `python tools/memory-recall/query.py "how does a kit row stay out of an adopter that has no govkit" --terms "generated row regen.py when govkit adopter leg_factory read_descriptors import exempt gov-only stage"`
