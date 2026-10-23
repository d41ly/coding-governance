# PLAY-dOrderedCharter-43 — the card import written and checked by the one renderer's entry-files scope, never by a second writer

**Status:** OPEN · rev-1 · 2026-10-24 · node d · Tier-2 · base ce13efbe · streams playbook · order 27 · advances PLAY-dOrderedCharter-38

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-24-build-PLAY-dOrderedCharter-39-promoted-fix-return.md](../build/2026-10-24-build-PLAY-dOrderedCharter-39-promoted-fix-return.md) | research | PLAY-dOrderedCharter-39 PLAY-dOrderedCharter-40 PLAY-dOrderedCharter-41 PLAY-dOrderedCharter-42 PLAY-dOrderedCharter-44 PLAY-dOrderedCharter-45 PLAY-dOrderedCharter-46 PLAY-dOrderedCharter-47 PLAY-dOrderedCharter-48 PLAY-dOrderedCharter-49 |
| [2026-10-24-build-PLAY-dOrderedCharter-43-deviation-431.md](../build/2026-10-24-build-PLAY-dOrderedCharter-43-deviation-431.md) | deviation | — |
| [2026-10-24-prompt-PLAY-dOrderedCharter-39-promoted-fix-brief.md](../prompts/2026-10-24-prompt-PLAY-dOrderedCharter-39-promoted-fix-brief.md) | research | PLAY-dOrderedCharter-39 PLAY-dOrderedCharter-40 PLAY-dOrderedCharter-41 PLAY-dOrderedCharter-42 PLAY-dOrderedCharter-44 PLAY-dOrderedCharter-45 PLAY-dOrderedCharter-46 PLAY-dOrderedCharter-47 PLAY-dOrderedCharter-48 PLAY-dOrderedCharter-49 |

<!-- /gen:spec-records -->

## 1. Goal

The round-1 spec audit (`memory/builds/dOrderedCharter/reviews/2026-10-23-review-PLAY-dOrderedCharter-1-spec-audit.md`)
confirmed **finding 49 at HIGH**, which shares item **H1** with finding 1. `PLAY-dOrderedCharter-8`
(order 26) adds `--card` to `_wire_pointer_or_copy` in `tools/agent-instructions/adopt-agent-instructions.sh`
(its S4) and to the `agent-instructions wiring` leg's argv (its S5). But `PLAY-dOrderedCharter-20`
(order 15) has already moved that pointer and copy logic into `render_playbook.py`'s `entry-files`
scope, and its S5 says no second renderer writes an absorbed file. Unit 8 would either edit logic that
has moved or give `CLAUDE.md` a second writer, and gov's two-line `CLAUDE.md` would then red
`--check-render` or be dropped by the next re-render. This unit puts the card import where the entry
files are rendered: a `--card` option of the renderer's `entry-files` scope, its check inside
`--check-render`, and the adopter script passing the switch through with no card logic of its own.
It repairs unit 8 and is built right after it. Finding 1, the same item's other half, is
`PLAY-dOrderedCharter-39`: the import surviving the agent-instructions kit's retirement.

## 2. Scope (IN)

- **S1** — The write. `python tools/playbook/render_playbook.py --render-scope entry-files --card`
  writes, in pointer mode, `CLAUDE.md` as the line `@AGENTS.md` followed by the line
  `@.claude/orientation-card.md`, and lists both files in a new `.gemini/settings.json`'s `fileName`;
  copy-mode aliases and Codex print `card — not delivered: <alias> ...` as unit 8 §4 "The wiring
  stand-in" tabulates. Without `--card` every byte is what the scope writes today. This supersedes
  unit 8 S4's home for the behaviour, `_wire_pointer_or_copy` in the adopter script. Observed by AC1
  and AC2.
- **S2** — The check. `check_card_import` lives in `tools/playbook/render_playbook.py` and runs under
  `--check-render` whenever `--card` is given, scoped to `entry-files` or unscoped: a native-pointer
  alias lacking the import line, or a Gemini `fileName` list lacking the card, fails naming the file.
  Observed by AC3.
- **S3** — No second writer. `tools/agent-instructions/adopt-agent-instructions.sh --card` passes the
  switch to the renderer it already calls for its render and its `--check` (unit 20 S5) and holds no
  card logic: no function, string or branch of the script names the card file. Where unit 8 landed
  card logic in the script, this unit takes it out of the script.
  **Readers:** by name: READER NOT IN TREE — the card logic in the script is unit 8's, which lands at
  order 26, after this spec's base `ce13efbe` · by value: NO VALUE READERS — the script's card branch
  writes the file the renderer now writes, and no other tool reads that branch. Observed by AC4.
- **S4** — Gov's switch, still dark until unit 8's AC1 is green (unit 8 §8 F1). Every gov leg whose
  check covers the `entry-files` scope carries `--card` in gov's `tools/gate-legs.json`: the
  `agent-instructions wiring` leg (unit 20 S6) and the `instruction render (one renderer of record)`
  leg (unit 20 S10), which checks every scope. Gov's `CLAUDE.md` gains the second line by a render of
  the scope, never by an edit. This supersedes unit 8 S5's single-leg argv. Observed by AC5.

## 3. Non-goals (OUT)

- The card file, its writer, its ignore line, the subagent and brief slices and the compaction
  fixture: unit 8's S1 to S3 and S6 to S9.
- The `entry-files` scope itself and the absorbed legs: unit 20's.
- Which leg holds the card check after the agent-instructions kit leaves the tree, and the kit's
  retirement inventory: `PLAY-dOrderedCharter-39`.
- A per-repository config key for the switch: rejected in §4.

### Edges

- **consumes-from** `PLAY-dOrderedCharter-8` — the card file's path, the delivery table of its §4 wiring stand-in and its dark switch, which S1 to S4 move into the renderer
- **consumes-from** `PLAY-dOrderedCharter-20` — the entry-files scope, the render and check verbs and the two legs S4 names; without them there is no renderer to carry the import
- **hands-off** `PLAY-dOrderedCharter-39` — the card option and its check in the renderer, which that unit carries through the retirement of the agent-instructions kit

## 4. Design

### Evidence

Read at `ce13efbe`. The pointer and copy logic is `_wire_pointer_or_copy`
(`tools/agent-instructions/adopt-agent-instructions.sh:142`), reached from the mode `case` at `:137`
and `:139`; `is_import` (`:62`) greps any matching line, and `gemini_configured` (`:61`) reads
`.gemini/settings.json`. The leg is `agent-instructions wiring` (`tools/gate-legs.json:293`), argv
`adopt-agent-instructions.sh --check --aliases claude`, claimed by the kit's `[[gate_leg]]` row
(`tools/agent-instructions/kit.toml:51-55`). `CLAUDE.md` is one line, `@AGENTS.md`. Unit 20 S5 moves
the pointer and copy writes into the renderer's `entry-files` scope with the script calling it, and
S8 makes `--check-render` with no scope check every scope; unit 8's spec names neither unit 20 nor
unit 31 in its Edges.

### Why a flag and not a config key

An argv flag is the surface unit 8 already priced, moved and not widened. A deploy-file key would be a
new adopter-facing surface (veto 2), and deriving the switch from the file being checked would make
the check pass on whatever it reads. The cost of the flag is that every gov leg covering the scope
carries it, which S4 names.

### Inventory

Moved, not minted: the flag `--card`, `check_card_import` and the `card —` line prefix, from unit 8's
script home to `tools/playbook/render_playbook.py`. Naming cells: `lexicon naming predicates` grades
the Python names.

### Files touched (estimate)

- `tools/playbook/render_playbook.py`
- `tools/playbook/renderers.toml` (the `CLAUDE.md` row's note that the scope may import the card)
- `tools/agent-instructions/adopt-agent-instructions.sh`
- `tools/agent-instructions/README.md`
- `tools/gate-legs.json` (S4, after unit 8's AC1)
- `CLAUDE.md` (S4, by render)
- `WIRE-INTO-PROJECT.md`

### Rollout

Dark, as unit 8 is: S1 to S3 land at order 27, after unit 8 at order 26; S4 lands only once the main
loop has recorded unit 8's AC1 green.

### Alternatives rejected

- **Leaving the import in the adopter script**, unit 8's S4: a second writer of `CLAUDE.md` beside the
  renderer of record, which unit 20 S5 forbids, and a script `PLAY-dOrderedCharter-31` deletes.
- **A `deploy.toml` key for the switch**: §4 above.

## 5. Production-readiness checklist

- security: no new surface; the flag moves from one tool to its successor.
- perf / scale: none; one more line compared per check.
- error / empty / loading states: a missing import line fails naming the file; with no `--card`
  nothing is compared.
- observability: the `card — not delivered:` lines name each alias left out.
- risks: a gov leg covering the scope without `--card` would red gov's two-line `CLAUDE.md`; S4 names
  both legs and AC5 reads them.
- testing: AC1 to AC5 by fixture and probe; the render selftest gains the arm §7 names.
- migration: none for adopters; the flag is off by default.
- user docs: `tools/agent-instructions/README.md` and `WIRE-INTO-PROJECT.md` name the flag on the
  renderer.

## 6. Acceptance criteria

- **AC1** — When `python tools/playbook/render_playbook.py --render-scope entry-files --card` runs in a
  fixture with aliases `claude gemini copilot`, `CLAUDE.md` is exactly `@AGENTS.md` and
  S1's card import line, the new Gemini `settings.json` lists both files, and the output
  carries `card — not delivered: copilot has no native import`.
  Red when: a pointer alias lacks the import.
- **AC2** — When the same render runs without `--card`, `CLAUDE.md` is the single line `@AGENTS.md`,
  byte-identical to the scope's output before this unit.
  Red when: the default moves.
- **AC3** — When `--check-render --scope entry-files --card` and unscoped `--check-render --card` run
  over AC1's fixture, each exits 0; after the second line of `CLAUDE.md` is deleted, each exits 1
  naming `CLAUDE.md`.
  Red when: the check passes without the import, or only the scoped check carries it.
- **AC4** — When `git grep -n -e "orientation-card" -- tools/agent-instructions/` runs after the pass,
  it prints nothing, and `adopt-agent-instructions.sh --card` in AC1's fixture writes the same bytes as
  the renderer.
  Red when: the script holds card logic of its own.
- **AC5** — When a probe reads `tools/gate-legs.json` at the commit that lands S4, both
  `agent-instructions wiring` and `instruction render (one renderer of record)` carry `--card` in their
  argv, and the acceptance ledger records unit 8's AC1 green before that commit.
  Red when: S4 lands with unit 8's AC1 red, or one leg covering the scope lacks the flag.

## 7. Gates

`playbook render selftest` · `playbook render wiring` · `agent-instructions wiring` · `agent-instructions self-test` · `govkit acceptance matrix` · `run-gates canary` · `run-gates gov canary` · `measure-legs selftest` · `lexicon naming predicates` · `spec tokens (a spec's own names resolve)`

New arm: tools/playbook/render_playbook.py · covers AC1 AC2 AC3 · the selftest renders and checks the entry-files scope with and without `--card` over a fixture, its failing case staged by deleting the import line · none

## 8. Open questions

- **F1 — Which binding line does a unit the spec audit promoted carry?** Options: (a) `**Derived:**`
  naming `PLAY-dClosedLoop-2`, as the tree's promoted specs do; (b) none; (c) a part of unit 8's
  clause. (b) reds unbound and (c) splits a clause this unit does not carry. RESOLVED (agent,
  2026-10-24, delegated): (a), rung 3. widens: none · relaxes: none
- **F2 — How the renderer knows the switch is on.** Options: (a) the `--card` flag on the render and
  check verbs, carried by every gov leg covering the scope; (b) a key in `.governance/deploy.toml`;
  (c) derived from the checked file. (b) is a new adopter-facing surface, which veto 2 sends to the
  owner, and (c) makes the check pass on what it reads. RESOLVED (agent, 2026-10-24, delegated): (a),
  rung 3, the surface unit 8 already priced. widens: none · relaxes: none

## 9. Revision log

- rev-1 · 2026-10-24 · initial draft, promoted from the round-1 spec audit's finding 49 (HIGH, item H1).

## 10. Reuse audit

The seam is unit 20's `entry-files` scope in `tools/playbook/render_playbook.py` (its S5), which
absorbs the pointer and copy logic of `_wire_pointer_or_copy`
(`tools/agent-instructions/adopt-agent-instructions.sh:142`) and is the one renderer of `CLAUDE.md`;
the card import is one more line that scope writes. `python tools/codebase-map/reuse_lookup.py "write
the entry file that imports the charter and a second instruction file"` ranked `write`
(`tools/memory-tree/gotchas.py`), `write_text` and `corpus_files` by name stem and not the renderer;
the probe disagrees with source, where unit 20 S5 names the scope that writes `CLAUDE.md`. The recall query returned unit 20's S5,
unit 31's brief row and the review's H1 text.

Recall terms used: `python tools/memory-recall/query.py "how does the agent-instructions wiring move into the one renderer and what happens to its legs" --terms "agent-instructions wiring entry-files render_playbook absorbed leg retired kit successor CLAUDE.md pointer"`
