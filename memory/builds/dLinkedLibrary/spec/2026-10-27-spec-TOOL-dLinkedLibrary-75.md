# TOOL-dLinkedLibrary-75 — the reuse-tag sweep reads a hyphenated feature name, and shows its red on a planted tag

**Status:** OPEN · rev-2 · 2026-10-27 · node d · Tier-2 · base 5fede642 · streams tooling · order 31 · advances TOOL-dLinkedLibrary-26

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-26-build-TOOL-dLinkedLibrary-1-agent-ledger.md](../build/2026-10-26-build-TOOL-dLinkedLibrary-1-agent-ledger.md) | journal | TOOL-dLinkedLibrary-1 TOOL-dLinkedLibrary-2 TOOL-dLinkedLibrary-3 TOOL-dLinkedLibrary-4 TOOL-dLinkedLibrary-5 TOOL-dLinkedLibrary-6 TOOL-dLinkedLibrary-7 TOOL-dLinkedLibrary-8 TOOL-dLinkedLibrary-9 TOOL-dLinkedLibrary-10 TOOL-dLinkedLibrary-11 TOOL-dLinkedLibrary-12 TOOL-dLinkedLibrary-13 TOOL-dLinkedLibrary-14 TOOL-dLinkedLibrary-15 TOOL-dLinkedLibrary-16 TOOL-dLinkedLibrary-17 TOOL-dLinkedLibrary-18 TOOL-dLinkedLibrary-19 TOOL-dLinkedLibrary-20 TOOL-dLinkedLibrary-21 TOOL-dLinkedLibrary-22 TOOL-dLinkedLibrary-23 TOOL-dLinkedLibrary-24 TOOL-dLinkedLibrary-25 TOOL-dLinkedLibrary-37 TOOL-dLinkedLibrary-38 TOOL-dLinkedLibrary-39 TOOL-dLinkedLibrary-40 TOOL-dLinkedLibrary-41 TOOL-dLinkedLibrary-42 TOOL-dLinkedLibrary-43 TOOL-dLinkedLibrary-44 TOOL-dLinkedLibrary-45 TOOL-dLinkedLibrary-46 TOOL-dLinkedLibrary-47 TOOL-dLinkedLibrary-48 TOOL-dLinkedLibrary-49 TOOL-dLinkedLibrary-50 TOOL-dLinkedLibrary-51 TOOL-dLinkedLibrary-52 TOOL-dLinkedLibrary-53 TOOL-dLinkedLibrary-54 TOOL-dLinkedLibrary-55 TOOL-dLinkedLibrary-56 TOOL-dLinkedLibrary-57 TOOL-dLinkedLibrary-58 TOOL-dLinkedLibrary-59 TOOL-dLinkedLibrary-60 TOOL-dLinkedLibrary-61 TOOL-dLinkedLibrary-62 TOOL-dLinkedLibrary-63 TOOL-dLinkedLibrary-64 TOOL-dLinkedLibrary-65 TOOL-dLinkedLibrary-66 TOOL-dLinkedLibrary-67 TOOL-dLinkedLibrary-68 TOOL-dLinkedLibrary-69 TOOL-dLinkedLibrary-70 TOOL-dLinkedLibrary-71 TOOL-dLinkedLibrary-72 TOOL-dLinkedLibrary-73 TOOL-dLinkedLibrary-74 TOOL-dLinkedLibrary-76 TOOL-dLinkedLibrary-77 TOOL-dLinkedLibrary-78 TOOL-dLinkedLibrary-79 TOOL-dLinkedLibrary-80 TOOL-dLinkedLibrary-81 TOOL-dLinkedLibrary-82 TOOL-dLinkedLibrary-83 TOOL-dLinkedLibrary-84 TOOL-dLinkedLibrary-85 TOOL-dLinkedLibrary-86 |
| [2026-10-27-build-TOOL-dLinkedLibrary-75-deviation-751.md](../build/2026-10-27-build-TOOL-dLinkedLibrary-75-deviation-751.md) | deviation | — |
| [2026-10-27-review-TOOL-dLinkedLibrary-75-spec-audit.md](../reviews/2026-10-27-review-TOOL-dLinkedLibrary-75-spec-audit.md) | spec-audit | TOOL-dLinkedLibrary-76 TOOL-dLinkedLibrary-77 TOOL-dLinkedLibrary-78 TOOL-dLinkedLibrary-79 TOOL-dLinkedLibrary-80 |

<!-- /gen:spec-records -->

## 1. Goal

The spec audit of units 65 to 74
(`memory/builds/dLinkedLibrary/reviews/2026-10-27-review-TOOL-dLinkedLibrary-65-spec-audit.md`) confirmed
finding **id 25 at HIGH**, report item **H1**. Ids 12 and 41 bind the same defect at MEDIUM, item M3,
and are items of the minors batch `TOOL-dLinkedLibrary-80`.

`TOOL-dLinkedLibrary-74` S20 rewrites every hyphenated reuse-entry tag `unit.reuse.<feature>-<n>` to the
dotted `unit.reuse.<feature>.<n>`, and its AC16 certifies the sweep with `git grep -nE
'unit\.reuse\.[A-Za-z0-9_]+-[0-9]+'`. That feature class holds no hyphen, so the tag of any hyphenated
feature never matches: `unit.reuse.memory-tree-hygiene-1` survives while AC16 reads green. 25 of the 32
dossiers under `memory/map/features/` carry a hyphenated name (PINNED, `ls memory/map/features/*.md`,
2026-10-27). The same grep prints nothing at base, so AC16 is also green before 74 is built.

This unit runs the sweep with a predicate that reads every feature name the dossiers spell, rewrites what
it finds, shows the predicate's red on a planted hyphenated tag, and gives the reuse-entry check a
durable plant drawn from the same hardest member. It repairs `TOOL-dLinkedLibrary-74` and builds one step
after it (order 31).

## 2. Scope (IN)

- **S1** — The predicate. The sweep's population is `tools` and `memory/map`, and its predicate is
  `git grep -nE 'unit\.reuse\.[A-Za-z0-9_-]+-[0-9]+([^0-9A-Za-z_]|$)' -- tools memory/map`: the feature
  class admits a hyphen, and the part number ends at a character that is not a word character or at the
  end of the line. It matches `unit.reuse.memory-tree-hygiene-1` and `unit.reuse.playbook-1`, and never
  the dotted `unit.reuse.run-gates.2` or the bare `unit.reuse.media-picker`. Observed by AC1 and AC3.
- **S2** — The rewrite. Each tag S1 prints at this pass's tip is rewritten to `unit.reuse.<feature>.<n>`,
  `<feature>` being the longest dossier stem under `memory/map/features/` that the tag's name opens with
  followed by a hyphen, so `unit.reuse.run-gates-turnstile-1` reads `run-gates-turnstile` and part 1. A tag
  that no stem opens is not guessed: it is named in this unit's acceptance ledger and AC2 stays red until
  it is resolved. Observed by AC2.
- **S3** — The durable plant. `reuse_entries.py --fixture --plant hyphen-tag` writes a scratch tree whose
  `memory/map/features/` holds the dossier `memory-tree-hygiene.md` and the part
  `memory-tree-hygiene.1.reuse.toml` with the tag `unit.reuse.memory-tree-hygiene-1`, and runs
  `check_reuse_entries` (`TOOL-dLinkedLibrary-1` S2, as `TOOL-dLinkedLibrary-38` S1 reads a part's stem):
  the part is reported, naming the tag; a twin tree whose part carries `unit.reuse.memory-tree-hygiene.1`
  reports nothing. Observed by AC3.

## 3. Non-goals (OUT)

- Reuse-entry proposal records under `memory/builds/`: a proposal names its part `<feature>.<n>` by
  `TOOL-dLinkedLibrary-60` S3, and the record is history, not a tag reader's input.
- A spec-audit rule that every population grep carries a planted red: the report's left-shift is a
  review-protocol change, outside this build's write set.
- The re-observation at the batch's tip: `TOOL-dLinkedLibrary-80`'s items for ids 12 and 41.

### Edges

- **consumes-from** `TOOL-dLinkedLibrary-74` — S20's tag sweep and AC16's population, which S1 re-reads with a hyphen-admitting feature class and S2 completes (id 25)
- **hands-off** `TOOL-dLinkedLibrary-80` — S1's predicate and AC3's scratch plant, which unit 80 re-runs at its own tip for ids 12 and 41
- **hands-off** `TOOL-dLinkedLibrary-86` — S2's remainder rule and part-file stem, S3's plant literal, AC2's population count and §10's recall line, which unit 86 corrects (ids 38, 21, 25, 7, 23, 11 of the spec audit of units 75 to 80)

## 4. Design

### Evidence

- `memory/builds/dLinkedLibrary/spec/2026-10-26-spec-TOOL-dLinkedLibrary-19.md:146` writes the seam's
  destination as `unit.reuse.<feature>-<n>`; `TOOL-dLinkedLibrary-60` S1 admits `<feature>-<n>` as a
  `--name` and composes the part `<feature>.<n>`.
- `TOOL-dLinkedLibrary-1` S2 reports a part whose `tag` is not `unit.reuse.<file stem>`, and
  `TOOL-dLinkedLibrary-38` S1 makes a part's stem `<feature>.<n>`, so a hyphenated tag inside a dotted
  part is a finding of the existing check; S3 plants that case.
- The predicate, probed on 2026-10-27 over six lines with `grep -nE`: it printed
  `unit.reuse.memory-tree-hygiene-1"`, `unit.reuse.playbook-1` and `tag unit.reuse.run-gates-2.`, and not
  `unit.reuse.run-gates.2`, `unit.reuse.media-picker` or `unit.reuse.foo-2fa`. Over `tools memory/map` at
  base it printed nothing, rc 1.

### Files touched (estimate)

- `tools/memory-tree/reuse_entries.py`: S3
- `memory/map/features/`: S2, each part S1 prints
- any file under `tools/` S1 prints: S2

### Alternatives rejected

- **The report's trailing class `([^0-9.]|$)`.** It matches `unit.reuse.foo-2fa`, a feature whose name
  holds a hyphen before a digit; excluding word characters keeps that out and still matches a tag ending a
  sentence.
- **Deriving each stem and grepping it alone.** It reads only stems that exist today, so a tag on a
  feature whose dossier was renamed is never seen.
- **A repository-wide tag gate.** The reuse-entry check already reads every part, which is where a tag
  lives; S3 holds that check to the hardest stem.

## 5. Production-readiness checklist

- security — none: the sweep reads tracked text and rewrites tags.
- perf / scale — one `git grep` over two directories.
- error / empty / loading states — an unresolvable tag is named, never guessed (S2).
- observability — the grep prints each surviving tag with its file and line.
- risks — a tag inside a quoted example is rewritten too; the ledger lists every rewrite.
- testing — AC3's scratch plant and the `hyphen-tag` fixture plant.
- migration — S2's rewrite, in this unit's own commit.
- user docs — none under `help/`: no user-facing behaviour moves.

## 6. Acceptance criteria

- **AC1** — When `git grep -nE 'unit\.reuse\.[A-Za-z0-9_-]+-[0-9]+([^0-9A-Za-z_]|$)' -- tools memory/map`
  runs at this pass's tip, it prints nothing. Hyphenated feature names are inside its population.
  Red when: a hyphenated tag of any feature, hyphenated stems included, survives in the tree.
- **AC2** — When `grep -n 'unit\.reuse\.'` runs over this unit's acceptance ledger, every tag S1 printed
  before S2 is listed beside the dotted tag it became, and no tag is listed unresolved.
  Red when: a tag no stem opens is rewritten by guess, or left unnamed.
- **AC3** — When the AC1 predicate runs in a scratch git repository under `%TEMP%/rt75`, holding a copy of
  `tools` and `memory/map` with `unit.reuse.memory-tree-hygiene-1`, `unit.reuse.run-gates-2` and
  `unit.reuse.run-gates.2` planted on three lines, it prints the two hyphenated lines and not the dotted
  one; and `python reuse_entries.py --fixture --plant hyphen-tag` reports the part naming
  `unit.reuse.memory-tree-hygiene-1` and reports nothing for the dotted twin.
  Red when: the predicate misses a hyphenated stem, or the check passes a tag that is not its part's stem.

## 7. Gates

`build-index selftest` · `recall floor` · `recall floor arms` · `memory hygiene` · `spec tokens (a spec's own names resolve)`

New arm: tools/memory-tree/reuse_entries.py · covers AC3 · the `hyphen-tag` plant, the failing case staged by a tag check that compares the tag with the stem's first hyphen-free segment · none

## 8. Open questions

- **F1 — Which binding line does a unit the spec audit promoted carry?** Options: (a) `**Derived:**`
  naming `PLAY-dClosedLoop-2`; (b) a `part k/n` carry of the repaired unit's clause. (b) splits a clause
  the repaired unit carries whole; veto 1 discards it. RESOLVED (agent, 2026-10-27, delegated): (a), rung
  3, the precedent `TOOL-dTotalRecall-40` set for this chain. widens: none · relaxes: none

## 9. Revision log

- rev-1 · 2026-10-27 · initial draft, promoted from the spec audit of units 65 to 74, id 25 (HIGH, item
  H1).
- rev-2 · 2026-10-27 · §3 · the Edges block gains the bullets mirroring TOOL-dLinkedLibrary-86, promoted from the spec
  audit of units 75 to 80; nothing else moved.

## 10. Reuse audit

The seam extended is `TOOL-dLinkedLibrary-74` S20's sweep, read with a wider predicate, and
`TOOL-dLinkedLibrary-1` S2's `check_reuse_entries` with its `--fixture --plant` harness, which gains one
plant. `python tools/codebase-map/reuse_lookup.py "rewrite a reuse entry tag to its dotted part stem"`
ranked `stems` (`tools/codebase-map/map_lib.py`), `resolve_entry`, `read_stem` and `render_dotted`, none a
reuse-tag reader or rewriter, so no existing seam fits beyond the two this unit extends.

Recall terms used: `python tools/memory-recall/query.py "how does a census refuse a ci job whose text or credentials come from a block it does not read" --terms "census ci-job refused opaque step credentials default variables block scalar fold header promoted"`
