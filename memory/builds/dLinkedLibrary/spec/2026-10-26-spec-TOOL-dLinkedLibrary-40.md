# TOOL-dLinkedLibrary-40 — `gov:legacy` registered as a `[[marker]]` row of the marker registry the markers arm reads

**Status:** OPEN · rev-2 · 2026-10-27 · node d · Tier-2 · base 5fede642 · streams tooling · order 26 · advances TOOL-dLinkedLibrary-26

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-26-build-TOOL-dLinkedLibrary-1-agent-ledger.md](../build/2026-10-26-build-TOOL-dLinkedLibrary-1-agent-ledger.md) | journal | TOOL-dLinkedLibrary-1 TOOL-dLinkedLibrary-2 TOOL-dLinkedLibrary-3 TOOL-dLinkedLibrary-4 TOOL-dLinkedLibrary-5 TOOL-dLinkedLibrary-6 TOOL-dLinkedLibrary-7 TOOL-dLinkedLibrary-8 TOOL-dLinkedLibrary-9 TOOL-dLinkedLibrary-10 TOOL-dLinkedLibrary-11 TOOL-dLinkedLibrary-12 TOOL-dLinkedLibrary-13 TOOL-dLinkedLibrary-14 TOOL-dLinkedLibrary-15 TOOL-dLinkedLibrary-16 TOOL-dLinkedLibrary-17 TOOL-dLinkedLibrary-18 TOOL-dLinkedLibrary-19 TOOL-dLinkedLibrary-20 TOOL-dLinkedLibrary-21 TOOL-dLinkedLibrary-22 TOOL-dLinkedLibrary-23 TOOL-dLinkedLibrary-24 TOOL-dLinkedLibrary-25 TOOL-dLinkedLibrary-37 TOOL-dLinkedLibrary-38 TOOL-dLinkedLibrary-39 TOOL-dLinkedLibrary-41 TOOL-dLinkedLibrary-42 TOOL-dLinkedLibrary-43 TOOL-dLinkedLibrary-44 TOOL-dLinkedLibrary-45 TOOL-dLinkedLibrary-46 TOOL-dLinkedLibrary-47 TOOL-dLinkedLibrary-48 TOOL-dLinkedLibrary-49 TOOL-dLinkedLibrary-50 TOOL-dLinkedLibrary-51 TOOL-dLinkedLibrary-52 TOOL-dLinkedLibrary-53 TOOL-dLinkedLibrary-54 TOOL-dLinkedLibrary-55 TOOL-dLinkedLibrary-56 TOOL-dLinkedLibrary-57 TOOL-dLinkedLibrary-58 TOOL-dLinkedLibrary-59 TOOL-dLinkedLibrary-60 TOOL-dLinkedLibrary-61 TOOL-dLinkedLibrary-62 TOOL-dLinkedLibrary-63 TOOL-dLinkedLibrary-64 TOOL-dLinkedLibrary-65 TOOL-dLinkedLibrary-66 TOOL-dLinkedLibrary-67 TOOL-dLinkedLibrary-68 TOOL-dLinkedLibrary-69 TOOL-dLinkedLibrary-70 TOOL-dLinkedLibrary-71 TOOL-dLinkedLibrary-72 TOOL-dLinkedLibrary-73 TOOL-dLinkedLibrary-74 |
| [2026-10-26-build-TOOL-dLinkedLibrary-40-deviation-401.md](../build/2026-10-26-build-TOOL-dLinkedLibrary-40-deviation-401.md) | deviation | — |
| [2026-10-27-review-TOOL-dLinkedLibrary-37-spec-audit.md](../reviews/2026-10-27-review-TOOL-dLinkedLibrary-37-spec-audit.md) | spec-audit | TOOL-dLinkedLibrary-43 TOOL-dLinkedLibrary-45 TOOL-dLinkedLibrary-48 TOOL-dLinkedLibrary-49 TOOL-dLinkedLibrary-38 TOOL-dLinkedLibrary-50 TOOL-dLinkedLibrary-39 TOOL-dLinkedLibrary-44 TOOL-dLinkedLibrary-41 TOOL-dLinkedLibrary-46 TOOL-dLinkedLibrary-47 TOOL-dLinkedLibrary-51 TOOL-dLinkedLibrary-37 TOOL-dLinkedLibrary-42 TOOL-dLinkedLibrary-52 TOOL-dLinkedLibrary-53 |

<!-- /gen:spec-records -->

## 1. Goal

The round-1 spec audit of the 25 unit specs
(`memory/builds/dLinkedLibrary/reviews/2026-10-26-review-TOOL-dLinkedLibrary-1-spec-audit.md`) confirmed
finding **id 3 at HIGH**, report item **R4**. Id 35 describes the same defect at MEDIUM (item R34); the
report keeps the two apart only because their grades differ, and `TOOL-dLinkedLibrary-53`'s item for
id 35 observes this unit's row.

`TOOL-dLinkedLibrary-23` S9 registers `marker.legacy` as a member row in `tools/playbook/namespaces.toml`.
The registry `check_marker_words` reads is `TOOL-dLinkedLibrary-12`'s `tools/memory-tree/marker-words.toml`
`[[marker]]` rows, and that unit rejected a members column on the namespace row (its §4 "Alternatives
rejected"). So `gov:legacy`, which `adopt_instructions.py`, the render gate, the help page and
`WIRE-INTO-PROJECT.md` write, has no registry row, the `markers` arm reds `unregistered gov: word
legacy` on every bar, and `TOOL-dLinkedLibrary-23` AC8 certifies a row the check never reads.

This unit writes the one `[[marker]]` row and leaves the namespace row in the shape
`TOOL-dTotalRecall-9` gives it. It repairs `TOOL-dLinkedLibrary-23` and builds one step after it
(order 26).

## 2. Scope (IN)

- **S1** — The row, appended to `tools/memory-tree/marker-words.toml` in `TOOL-dLinkedLibrary-12` S1's
  schema: `word = "legacy"`, `reader = "tools/playbook/render_playbook.py"`, `reads` naming
  `--check-render`'s legacy half, the pair beside its `instructions-legacy` row, `kind = "pair"`,
  `owner = "TOOL-dLinkedLibrary-23"`, the unit whose lines write the word, as `TOOL-dLinkedLibrary-4`
  S14 owns the rows of the words it writes. Observed by AC1 and AC2.
- **S2** — The namespace row keeps its shape. The `marker` row of `tools/playbook/namespaces.toml`
  holds no member list and no `legacy` entry: where `TOOL-dLinkedLibrary-23`'s pass wrote one, this pass
  restores the row to the bytes `TOOL-dTotalRecall-9` S1 lands. Observed by AC3.
- **S3** — `TOOL-dLinkedLibrary-23` AC8's registry half is answered here: that unit's acceptance ledger
  answers it AMENDED, naming this unit and AC1. Observed by AC4.

## 3. Non-goals (OUT)

- The legacy pair, its renderer and its gate: `TOOL-dLinkedLibrary-23`'s and PLAY-dOrderedCharter-20's.
- How a registry row resolves its reader in an adopter: `TOOL-dLinkedLibrary-48`'s (id 59), which reads
  this row as it reads every other.
- The report's left-shift gate, a spec-tokens arm checking that a spec writes to the registry its owning
  spec names: a checker change outside this build's clauses.

### Edges

- **consumes-from** `TOOL-dLinkedLibrary-23` — `gov:legacy`, the pair its capture writes, and the namespace edit of its S9, which S2 restores (id 3)
- **consumes-from** `TOOL-dLinkedLibrary-12` — `marker-words.toml` and `check_marker_words`, the registry and the check S1's row joins (id 3)
- **hands-off** `TOOL-dLinkedLibrary-53` — the `legacy` row of `marker-words.toml` and the namespace row S2 keeps member-free, which unit 53's item for id 35 observes
- **hands-off** `TOOL-dLinkedLibrary-64` — the `legacy` row of `marker-words.toml`, which unit 64 observes beside the member-free namespace row (id 8 of the spec audit of units 37 to 53)

## 4. Design

### Evidence

- `TOOL-dLinkedLibrary-12` S1 defines `marker-words.toml`'s `[[marker]]` row and S3 reads it in
  `check_marker_words`; its §3 says `TOOL-dLinkedLibrary-23` adds the `legacy` row "with the first line
  that writes the word", and its §3 Edges hand that unit the registry.
- `TOOL-dLinkedLibrary-23` S9 and its Files touched name `tools/playbook/namespaces.toml` for the member
  and never name `marker-words.toml`.
- `TOOL-dLinkedLibrary-4` S14 writes its three rows into `marker-words.toml`, each owned by that unit.

### The row

```toml
[[marker]]
word = "legacy"
reader = "tools/playbook/render_playbook.py"
reads = "--check-render: each legacy pair beside its instructions-legacy row, its paragraph count"
kind = "pair"
owner = "TOOL-dLinkedLibrary-23"
```

### Files touched (estimate)

- `tools/memory-tree/marker-words.toml`: S1
- `tools/playbook/namespaces.toml`: S2, where unit 23's pass wrote a member

### Alternatives rejected

- **A members field on the namespace row.** `TOOL-dLinkedLibrary-12` rejected it: the row is a parent
  build's schema and a word's reader and kind do not fit one cell.
- **`owner` naming this unit.** The row registers a word another unit writes; the owner names the
  mechanism the word belongs to, as unit 4's rows do.

## 5. Production-readiness checklist

- security — a registry row; no write path.
- perf / scale — one row.
- error / empty / loading states — `read_marker_words` refuses a malformed row, naming it, as before.
- observability — the `markers` arm names `legacy` registered, and no longer refuses it.
- risks — none beyond the registry's own.
- testing — AC1 to AC3 by probe; the markers arm at the close.
- migration — none.
- user docs — none under `help/`: `help/adopting-instructions.md` names the pair, not its registry.

## 6. Acceptance criteria

- **AC1** — When `grep -n 'word = "legacy"' marker-words.toml` runs in `tools/memory-tree`, it prints the row,
  and the four lines after it carry `reader`, `reads`, `kind = "pair"` and `owner`.
  Red when: the row is absent, or sits in another registry.
- **AC2** — When `python annotations.py check --only markers` runs over a scratch clone holding one
  captured legacy pair, it names no unregistered word; with the `legacy` row cut from the clone's
  registry it exits 1 naming `legacy`.
  Red when: the word is refused with its row present, or passes without it.
- **AC3** — When `grep -n "legacy" namespaces.toml` runs in `tools/playbook` at this pass's tip, it prints
  no line inside the `marker` row.
  Red when: a member for `legacy` is left on the namespace row.
- **AC4** — When `grep -n "AC8" <unit 23's acceptance ledger>` runs, the answer reads AMENDED and names
  `TOOL-dLinkedLibrary-40`.
  Red when: unit 23's ledger certifies the namespace-row reading.
  fixture: unit 23's acceptance ledger, written at its pass under `memory/builds/dLinkedLibrary/build/`.

## 7. Gates

`govkit acceptance matrix` · `playbook render selftest` · `memory hygiene` · `spec tokens (a spec's own names resolve)`

## 8. Open questions

- **F1 — Which binding line does a unit the spec audit promoted carry?** Options: (a) `**Derived:**`
  naming `PLAY-dClosedLoop-2`; (b) a `part k/n` carry of the repaired unit's clause. (b) splits a clause
  unit 23 carries whole; veto 1 discards it. RESOLVED (agent, 2026-10-26, delegated): (a), rung 3, the
  precedent `TOOL-dTotalRecall-40` set for this chain. widens: none · relaxes: none

## 9. Revision log

- rev-1 · 2026-10-26 · initial draft, promoted from the round-1 spec audit of the 25 unit specs, id 3
  (HIGH, item R4; id 35 shares the defect at MEDIUM, item R34).
- rev-2 · 2026-10-27 · §3 · the Edges block gains the bullets mirroring TOOL-dLinkedLibrary-64, promoted from the spec audit of units 37 to 53; nothing else moved.

## 10. Reuse audit

The seam extended is `TOOL-dLinkedLibrary-12`'s member registry `tools/memory-tree/marker-words.toml`,
read by `read_marker_words` and `check_marker_words`; this unit adds one row in its schema and mints
nothing. `python tools/codebase-map/reuse_lookup.py "find which kit directory an installed file lives
in"` ranked `resolve_kit_dir`, `kit_rel` and `kit_dir`, readers of where a kit sits, none a word
registry, so no existing seam fits beyond the registry this row joins.

Recall terms used: `python tools/memory-recall/query.py "how is a promoted spec-audit finding repaired by a unit placed after the unit it repairs" --terms "spec-audit promoted finding repairs order rescope add batch minors disjoint write set"`
