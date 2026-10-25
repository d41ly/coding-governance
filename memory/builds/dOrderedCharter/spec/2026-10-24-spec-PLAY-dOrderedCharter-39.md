# PLAY-dOrderedCharter-39 — the card import survives the agent-instructions kit's retirement, with the wiring leg kept by name

**Status:** DEFERRED · rev-2 · 2026-10-24 · node d · Tier-2 · base ce13efbe · streams playbook · order 37 · advances PLAY-dOrderedCharter-38

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-24-build-PLAY-dOrderedCharter-39-deviation-391.md](../build/2026-10-24-build-PLAY-dOrderedCharter-39-deviation-391.md) | deviation | — |
| [2026-10-24-build-PLAY-dOrderedCharter-39-promoted-fix-return.md](../build/2026-10-24-build-PLAY-dOrderedCharter-39-promoted-fix-return.md) | research | PLAY-dOrderedCharter-40 PLAY-dOrderedCharter-41 PLAY-dOrderedCharter-42 PLAY-dOrderedCharter-43 PLAY-dOrderedCharter-44 PLAY-dOrderedCharter-45 PLAY-dOrderedCharter-46 PLAY-dOrderedCharter-47 PLAY-dOrderedCharter-48 PLAY-dOrderedCharter-49 |
| [2026-10-25-build-PLAY-dOrderedCharter-1-agent-ledger.md](../build/2026-10-25-build-PLAY-dOrderedCharter-1-agent-ledger.md) | journal | PLAY-dOrderedCharter-1 PLAY-dOrderedCharter-2 PLAY-dOrderedCharter-3 PLAY-dOrderedCharter-4 PLAY-dOrderedCharter-5 PLAY-dOrderedCharter-6 PLAY-dOrderedCharter-7 PLAY-dOrderedCharter-8 PLAY-dOrderedCharter-9 PLAY-dOrderedCharter-10 PLAY-dOrderedCharter-11 PLAY-dOrderedCharter-12 PLAY-dOrderedCharter-13 PLAY-dOrderedCharter-14 PLAY-dOrderedCharter-15 PLAY-dOrderedCharter-16 PLAY-dOrderedCharter-17 PLAY-dOrderedCharter-18 PLAY-dOrderedCharter-19 PLAY-dOrderedCharter-20 PLAY-dOrderedCharter-21 PLAY-dOrderedCharter-22 PLAY-dOrderedCharter-23 PLAY-dOrderedCharter-24 PLAY-dOrderedCharter-25 PLAY-dOrderedCharter-26 PLAY-dOrderedCharter-27 PLAY-dOrderedCharter-28 PLAY-dOrderedCharter-29 PLAY-dOrderedCharter-30 PLAY-dOrderedCharter-31 PLAY-dOrderedCharter-32 PLAY-dOrderedCharter-33 PLAY-dOrderedCharter-34 PLAY-dOrderedCharter-35 PLAY-dOrderedCharter-36 PLAY-dOrderedCharter-37 PLAY-dOrderedCharter-40 PLAY-dOrderedCharter-41 PLAY-dOrderedCharter-42 PLAY-dOrderedCharter-43 PLAY-dOrderedCharter-44 PLAY-dOrderedCharter-45 PLAY-dOrderedCharter-46 PLAY-dOrderedCharter-47 PLAY-dOrderedCharter-48 PLAY-dOrderedCharter-49 PLAY-dOrderedCharter-50 PLAY-dOrderedCharter-51 PLAY-dOrderedCharter-52 PLAY-dOrderedCharter-53 PLAY-dOrderedCharter-54 PLAY-dOrderedCharter-55 |
| [2026-10-24-prompt-PLAY-dOrderedCharter-39-promoted-fix-brief.md](../prompts/2026-10-24-prompt-PLAY-dOrderedCharter-39-promoted-fix-brief.md) | research | PLAY-dOrderedCharter-40 PLAY-dOrderedCharter-41 PLAY-dOrderedCharter-42 PLAY-dOrderedCharter-43 PLAY-dOrderedCharter-44 PLAY-dOrderedCharter-45 PLAY-dOrderedCharter-46 PLAY-dOrderedCharter-47 PLAY-dOrderedCharter-48 PLAY-dOrderedCharter-49 |
| [2026-10-24-review-PLAY-dOrderedCharter-39-spec-audit.md](../reviews/2026-10-24-review-PLAY-dOrderedCharter-39-spec-audit.md) | spec-audit | PLAY-dOrderedCharter-44 PLAY-dOrderedCharter-47 PLAY-dOrderedCharter-48 PLAY-dOrderedCharter-42 PLAY-dOrderedCharter-45 PLAY-dOrderedCharter-41 PLAY-dOrderedCharter-43 PLAY-dOrderedCharter-46 PLAY-dOrderedCharter-40 PLAY-dOrderedCharter-49 |

<!-- /gen:spec-records -->

## 1. Goal

The round-1 spec audit (`memory/builds/dOrderedCharter/reviews/2026-10-23-review-PLAY-dOrderedCharter-1-spec-audit.md`)
confirmed **finding 1 at HIGH**, which shares item **H1** with finding 49. `PLAY-dOrderedCharter-31`
(order 36) deletes `tools/agent-instructions/` and both its legs and names only `CODEX_MAX` as moving,
so at the close the card import's switch and check would leave with the script, and the level-1 card
delivery and unit 8's AC7 would not survive. Unit 20's F2 and Alternatives keep the
`agent-instructions wiring` leg by name, because the name is the join key of every file keyed by leg
name, and unit 31 S1 deletes it: the two specs disagree. This unit reconciles them in favour of unit
20's ruling, names the card import as moving beside `CODEX_MAX`, and makes the retirement prove that
every option of the retired adopter is either an option of its successor or named retired. It repairs
unit 31 and is built right after it. Finding 49, the same item's other half, is
`PLAY-dOrderedCharter-43`, which moved the import into the renderer at order 27.

## 2. Scope (IN)

- **S1** — The leg keeps its name. `agent-instructions wiring` stays in `tools/gate-legs.json` with its
  argv the renderer's `--check-render --scope entry-files`, carrying `--card` in gov's manifest as
  `PLAY-dOrderedCharter-43` S4 sets it. Its descriptor claim moves from the retired kit's `[[gate_leg]]`
  row (`tools/agent-instructions/kit.toml:51-55`) to a `[[gate_leg]]` row of the `playbook-render` entry's
  descriptor, `tools/playbook/kit.toml`, with no `--card` there, the adopter default. Its rows in
  `tools/govkit/subject-pins.tsv:17` and `tools/run-gates/ceiling-evidence.txt:33` stay, re-derived where
  their generator re-derives them. Only `agent-instructions self-test` leaves, with its rows at
  `tools/govkit/registry.toml:522-524`, `tools/govkit/subject-pins.tsv:16`,
  `tools/run-gates/ceiling-evidence.txt:32` and `tools/run-gates/selftest-budgets.txt:52`. This
  supersedes unit 31 S1's "its two legs leave `tools/gate-legs.json` (`:293`, `:382`)".
  **Readers:** by name: `tools/gate-legs.json`, `tools/govkit/registry.toml`,
  `tools/govkit/subject-pins.tsv`, `tools/run-gates/ceiling-evidence.txt` and
  `tools/run-gates/selftest-budgets.txt`, each spelling the self-test leg's name at the base · by value:
  NO VALUE READERS — the self-test leg's verdict feeds no other check, and each row above is keyed by
  the name alone. Observed by AC1 and AC2.
- **S2** — The card import moves by name. Unit 31's retirement names, beside `CODEX_MAX`, the
  `--card` option, `check_card_import` and the `card —` line prefix as moved into
  `tools/playbook/render_playbook.py`, and the pass commit's `Decided:` trailer lists them with
  `CODEX_MAX`. This extends unit 31 S1's "`CODEX_MAX` moves into the module unit 20 absorbed the wiring
  into". Observed by AC3.
- **S3** — Every behaviour of the deleted kit accounted for. Before the directory leaves, a probe reads
  each option the adopter's argument `case` accepts at the base and finds it among the options
  `render_playbook.py --help` prints; an option it does not find is named retired in the pass
  commit's `Decided:` trailer with its reason, and the pass is refused while one is neither. Observed by
  AC3.
- **S4** — Gov's card import after the close. Gov's `CLAUDE.md` still carries the
  `@.claude/orientation-card.md` line when unit 8's AC1 was green, and the kept leg checks it.
  Observed by AC4.

## 3. Non-goals (OUT)

- The `[[retired]]` row, the step kind and the other steps of unit 31: unit 31's.
- Moving the card import into the renderer: `PLAY-dOrderedCharter-43`.
- Renaming any leg: a leg keeps its name (unit 20 F2).

### Edges

- **consumes-from** `PLAY-dOrderedCharter-31` — the retirement of the agent-instructions kit, its registry rows and its inventory query, which S1 and S2 amend; without it there is nothing to carry the import through
- **consumes-from** `PLAY-dOrderedCharter-43` — the card option and its check in the renderer, which S2 names as moved and S1's kept leg runs
- **hands-off** `PLAY-dOrderedCharter-55` — round-2 ids 1, 10, 11, 22, 26 and 29: S3's probe read at the deleting commit's parent and keyed on behaviour, the map baseline and generated map, the moved leg's adopter population, and the renderer-of-record leg

## 4. Design

### Evidence

Read at `ce13efbe`. `agent-instructions wiring` is `tools/gate-legs.json:293`, `agent-instructions
self-test` `:382`. The wiring leg's `[[gate_leg]]` row is `tools/agent-instructions/kit.toml:51-55`;
the self-test's `[[exempt_leg]]` row is `tools/govkit/registry.toml:522-524`. The leg-keyed rows are
`tools/govkit/subject-pins.tsv:16-17`, `tools/run-gates/ceiling-evidence.txt:32-33` and
`tools/run-gates/selftest-budgets.txt:52` (the wiring leg has no budget row). The `playbook-render`
entry's descriptor is `tools/playbook/kit.toml` (`tools/govkit/registry.toml:66-67`). The adopter's
options are its `case "$1"` arms, `--source`, `--aliases`, `--mode`, `--check` and `--force`
(`tools/agent-instructions/adopt-agent-instructions.sh:34-42`), to which unit 8 adds `--card`. Unit 20
F2 keeps an absorbed leg's name, citing the systems record's "A leg keeps its name"
(`memory/builds/dClosedLoop/build/2026-10-16-build-PLAY-dClosedLoop-1-systems.md:262`); unit 31 S1
deletes both legs and names `CODEX_MAX` alone as moving.

### Inventory

No identifier is minted. The `[[gate_leg]]` row `agent-instructions wiring` moves descriptor.

### Files touched (estimate)

- `tools/playbook/kit.toml`
- `tools/gate-legs.json`
- `tools/govkit/registry.toml`
- `tools/govkit/subject-pins.tsv`
- `tools/run-gates/ceiling-evidence.txt`
- `tools/run-gates/selftest-budgets.txt`

### Rollout

Live at landing, order 37, after unit 31 at order 36. Unit 37 shares order 37 and writes none of these
files.

### Alternatives rejected

- **Both legs leave and the `instruction render (one renderer of record)` leg holds the card check**:
  it checks every scope, so the import is still checked, but the leg-keyed files lose a name the
  systems record says a leg keeps, and the scoped, cheap check of the entry files goes.
- **Keeping the self-test leg too**: its suite lives in the deleted directory and grades a script that
  no longer exists.

## 5. Production-readiness checklist

- security: no new surface; a leg changes its argv and its claiming descriptor.
- perf / scale: the kept leg runs one scope of the renderer, measured against its existing ceiling row.
- error / empty / loading states: S3's probe refuses the pass naming an unaccounted option.
- observability: the `Decided:` trailer lists every moved and retired option.
- risks: an adopter whose bar holds `agent-instructions wiring` keeps it, now claimed by the
  `playbook-render` entry; one without that entry loses the leg, as the retired kit's row says.
- testing: AC1 to AC4 by probe at the pass.
- migration: the claim moves with the `[[retired]]` row's successor, `playbook-render`.
- user docs: unit 31's `help/upgrade-steps.md` section names the kept leg.

## 6. Acceptance criteria

- **AC1** — When a probe reads `tools/gate-legs.json` after the pass, `agent-instructions wiring` is
  present with an argv running `render_playbook.py --check-render --scope entry-files`, and
  `agent-instructions self-test` is absent.
  Red when: the wiring leg is deleted, or the self-test leg survives its directory.
- **AC2** — When `git grep -n "agent-instructions wiring" -- tools/playbook/kit.toml tools/govkit/subject-pins.tsv tools/run-gates/ceiling-evidence.txt`
  runs, each file names the leg once.
  Red when: the leg is left with no descriptor claim or loses a keyed row.
- **AC3** — When S3's probe runs before the directory leaves, every option of the adopter's argument
  `case`, `--card` included, is printed as found in `render_playbook.py --help` or as named retired in
  the pass's trailer, and the trailer names `--card`, `check_card_import` and `CODEX_MAX` as moved.
  Red when: an option leaves with the script and is named nowhere.
- **AC4** — When `git show HEAD:CLAUDE.md` runs after the pass, it holds the card import line where unit
  8's AC1 was recorded green, and `--check-render --scope entry-files --card` exits 0 over the tree.
  Red when: the retirement drops the import or its check.

## 7. Gates

`agent-instructions wiring` · `playbook render selftest` · `playbook render wiring` · `govkit acceptance matrix` · `govkit selfcheck` · `govkit selftest` · `govkit refusal join` · `run-gates canary` · `run-gates gov canary` · `measure-legs selftest` · `recall floor arms` · `spec tokens (a spec's own names resolve)`

## 8. Open questions

- **F1 — Which binding line does a unit the spec audit promoted carry?** Options: (a) `**Derived:**`
  naming `PLAY-dClosedLoop-2`, as the tree's promoted specs do; (b) none; (c) a part of unit 31's
  clause. (b) reds unbound and (c) splits a clause this unit does not carry. RESOLVED (agent,
  2026-10-24, delegated): (a), rung 3. widens: none · relaxes: none
- **F2 — Does `agent-instructions wiring` survive the kit.** Options: (a) it keeps its name, re-homed
  on the renderer and claimed by `playbook-render`; (b) both legs leave and the unscoped render leg
  holds the check. Unit 20 F2 settled (a) at rung 1 from the systems record; unit 31 S1 wrote (b)
  without naming that ruling. RESOLVED (agent, 2026-10-24, delegated): (a), rung 1, the systems record
  `[design-tags]` "A leg keeps its name". widens: none · relaxes: none

## 9. Revision log

- rev-1 · 2026-10-24 · initial draft, promoted from the round-1 spec audit's finding 1 (HIGH, item H1).
- rev-2 · 2026-10-24 · §3 · Edges gain the mirror of each edge the round-2 spec audit's promoted units declare against this unit: PLAY-dOrderedCharter-55.

## 10. Reuse audit

The seams are unit 31's retirement (its S1 and §4 inventory queries) and unit 20's absorbed-leg rule
(its S6 and F2), which this unit makes agree; the claim mechanism is the descriptor `[[gate_leg]]` row
the kit already uses (`tools/agent-instructions/kit.toml:51-55`), moved to the successor's descriptor.
`python tools/codebase-map/reuse_lookup.py "keep a gate leg by name when its kit is retired and its
successor absorbs it"` ranked `legs`, `leg` (two suites' test helpers) and `kit_rel` by name stem;
no existing seam re-homes a leg, so none fits
beyond the descriptor row. The recall query returned unit 31's brief row, unit 20's S5 and the
review's H1 text.

Recall terms used: `python tools/memory-recall/query.py "how does the agent-instructions wiring move into the one renderer and what happens to its legs" --terms "agent-instructions wiring entry-files render_playbook absorbed leg retired kit successor CLAUDE.md pointer"`
