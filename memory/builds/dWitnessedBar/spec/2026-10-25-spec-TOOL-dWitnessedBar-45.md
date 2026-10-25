# TOOL-dWitnessedBar-45 — the leg factory runs in a tree with no govkit: its generated row stays gov's, and its adopter verbs import no govkit

**Status:** OPEN · rev-2 · 2026-10-25 · node d · Tier-2 · base cdfbd1cf · streams tooling · order 9 · advances TOOL-dWitnessedBar-31

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-25-build-TOOL-dWitnessedBar-1-agent-ledger.md](../build/2026-10-25-build-TOOL-dWitnessedBar-1-agent-ledger.md) | journal | TOOL-dWitnessedBar-1 TOOL-dWitnessedBar-2 TOOL-dWitnessedBar-3 TOOL-dWitnessedBar-4 TOOL-dWitnessedBar-5 TOOL-dWitnessedBar-6 TOOL-dWitnessedBar-7 TOOL-dWitnessedBar-8 TOOL-dWitnessedBar-9 TOOL-dWitnessedBar-10 TOOL-dWitnessedBar-11 TOOL-dWitnessedBar-12 TOOL-dWitnessedBar-13 TOOL-dWitnessedBar-14 TOOL-dWitnessedBar-15 TOOL-dWitnessedBar-16 TOOL-dWitnessedBar-17 TOOL-dWitnessedBar-18 TOOL-dWitnessedBar-19 TOOL-dWitnessedBar-20 TOOL-dWitnessedBar-21 TOOL-dWitnessedBar-22 TOOL-dWitnessedBar-23 TOOL-dWitnessedBar-24 TOOL-dWitnessedBar-25 TOOL-dWitnessedBar-26 TOOL-dWitnessedBar-27 TOOL-dWitnessedBar-28 TOOL-dWitnessedBar-29 TOOL-dWitnessedBar-30 TOOL-dWitnessedBar-40 TOOL-dWitnessedBar-41 TOOL-dWitnessedBar-42 TOOL-dWitnessedBar-43 TOOL-dWitnessedBar-44 TOOL-dWitnessedBar-46 TOOL-dWitnessedBar-47 TOOL-dWitnessedBar-48 TOOL-dWitnessedBar-49 TOOL-dWitnessedBar-50 TOOL-dWitnessedBar-51 TOOL-dWitnessedBar-52 TOOL-dWitnessedBar-53 TOOL-dWitnessedBar-54 TOOL-dWitnessedBar-55 TOOL-dWitnessedBar-56 TOOL-dWitnessedBar-57 TOOL-dWitnessedBar-58 TOOL-dWitnessedBar-59 TOOL-dWitnessedBar-60 TOOL-dWitnessedBar-61 TOOL-dWitnessedBar-62 |
| [2026-10-25-review-TOOL-dWitnessedBar-40-spec-audit-round1.md](../reviews/2026-10-25-review-TOOL-dWitnessedBar-40-spec-audit-round1.md) | spec-audit | TOOL-dWitnessedBar-48 TOOL-dWitnessedBar-49 TOOL-dWitnessedBar-50 TOOL-dWitnessedBar-47 TOOL-dWitnessedBar-46 TOOL-dWitnessedBar-40 TOOL-dWitnessedBar-42 TOOL-dWitnessedBar-44 TOOL-dWitnessedBar-41 TOOL-dWitnessedBar-43 TOOL-dWitnessedBar-51 |

<!-- /gen:spec-records -->

## 1. Goal

The round-1 spec audit (`memory/builds/dWitnessedBar/reviews/2026-10-25-review-TOOL-dWitnessedBar-1-spec-audit-round1.md`)
confirmed finding **id 33 at HIGH**, its item **H6**, alone in that item. `TOOL-dWitnessedBar-11` S2 puts
the factory's `[[generated]]` row in `tools/run-gates/kit.toml`, which ships (`include = "**"`,
`tools/run-gates/kit.toml:18`), and `regen.py --check` reads every tracked descriptor and runs before the
first leg. `leg_factory.py` imports govkit's `read_descriptors` and `resolve_tokens`, and govkit never
reaches an adopter. Once run-gates updates, every adopter's bar fails at stage 1, and
`TOOL-dWitnessedBar-28` S8's `leg sources` leg (`leg_factory.py --sources`) hits the same import failure.
This unit takes the skeptic's corrected fix. It repairs `TOOL-dWitnessedBar-11`.

## 2. Scope (IN)

- **S1** — A gov-only row. `regen.py`'s `when` gains a second form, `exists:<path>`, its tokens resolved
  as a row's argv tokens are, holding when that path exists in the tree. The factory's `[[generated]]`
  row carries `when = "exists:{prefix}/govkit/govkit.py"`, so in a tree with no govkit regen skips it
  and lists it skipped. Observed by AC1.
- **S2** — No import at load. `leg_factory.py` imports only the standard library and its sibling
  `regen` at module level. govkit is loaded inside the verbs that need it, through one function
  `load_govkit(root)`, which exits 2 naming the path it looked for when govkit is absent. Observed by AC2.
- **S3** — The adopter verbs. Every verb a tree with no govkit runs reads descriptors through
  `regen.read_descriptors` and resolves tokens through `regen.resolve_argv`, and never calls
  `load_govkit`: `--sources` and `--legacy-rows` (`TOOL-dWitnessedBar-28`), and `--conform`, which
  unit 28 S3 makes a fixed row of an adopter's composition. Under no govkit, `--conform` runs its field
  arms over the target's descriptors and prints `fresh: not graded here — no govkit`, since the render
  the `fresh` arm compares is gov's. Observed by AC2 and AC3.
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

- `regen.py` reads every tracked `tools/*/kit.toml` (`read_descriptors`, `tools/run-gates/regen.py:108-122`),
  honours a row's `when = "<conf>:<KEY>=<value>"` (`check_when`, `:140-146`) and skips the row when it
  does not hold (`build_items`, `:186-187`).
- `regen.resolve_argv` resolves `{kit}`, `{prefix}`, `{memory_root}` and `{map_root}` (`:125-138`), the
  tokens unit 11 §4 step 3 resolves.
- `run-gates adopter e2e` runs `tools/run-gates/adopt-run-gates.test.sh`, the kit's own adopter suite.
- govkit is an `[[exempt]]` home and never installed at an adopter (`tools/govkit/registry.toml`).

### The `when` grammar

```
when = "<conf file>:<KEY>=<value>"     # today: holds when the conf's key reads value
when = "exists:<path>"                 # new: holds when the token-resolved path exists in the tree
```

A `when` naming neither form is a refusal, as a malformed one is today. Neither form runs a command.

### Inventory

Minted: the `exists:` form of `when`; `load_govkit`; the `fresh: not graded here — no govkit` line.
Naming cells: `load_govkit` is asked of `python tools/lexicon/lexicon.py --suggest load_govkit --as
py.function` at the pass.

### Migration

None for gov: govkit exists, so the row holds and every verb runs as unit 11 states.

### Rollout

Live at landing, before any adopter updates past unit 11.

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
- error / empty / loading states — a gov verb without govkit exits 2 naming the path; `--conform` names
  the arm it did not grade.
- observability — `regen.py --list` names the skipped row.
- risks — `--conform` at an adopter grades fields only; the line says so.
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
  exits 0, and `python leg_factory.py --write` there exits 2 naming the govkit path it looked for; once
  `TOOL-dWitnessedBar-28` has added `--sources`, the same suite runs it there with no traceback.
  Red when: the module imports govkit at load, so every verb fails with `ModuleNotFoundError`.
- **AC3** — When `python leg_factory.py --conform` runs in the same scratch tree, it prints
  `fresh: not graded here — no govkit` and exits 0 over the target's untouched descriptors; in gov's
  tree it grades `fresh` as unit 11 states.
  Red when: `--conform` refuses or crashes where govkit is absent, so the fixed row reds every adopter.

## 7. Gates

`run-gates adopter e2e` · `run-gates wiring` · `run-gates canary` · `measure-legs selftest` · `memory hygiene`

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

## 9. Revision log

- rev-1 · 2026-10-25 · initial draft, promoted from the round-1 spec audit's id 33 (HIGH, item H6).
- rev-2 · 2026-10-25 · §3 · the Edges block gains the hands-off bullets mirroring the consumes-from
  edges of TOOL-dWitnessedBar-54, TOOL-dWitnessedBar-56, TOOL-dWitnessedBar-57, promoted by the
  round-1 spec audit of units 40 to 51; nothing else moved.

## 10. Reuse audit

The seams extended are `regen.py`'s row condition `check_when` and its shipped reader
`read_descriptors` with `resolve_argv`, which the factory reuses instead of importing govkit's.
`python tools/codebase-map/reuse_lookup.py "skip a generated row when a gov-only tool is absent"`
ranked `rows`, `row`, `absent`, `skip`, `extract_row` and `resolve_generated_indexes`; the last is the
unattended kit's reader of `GENERATED_INDEXES`, rejected in §4, and none of the others conditions a row.

Recall terms used: `python tools/memory-recall/query.py "how does a kit row stay out of an adopter that has no govkit" --terms "generated row regen.py when govkit adopter leg_factory read_descriptors import exempt gov-only stage"`
