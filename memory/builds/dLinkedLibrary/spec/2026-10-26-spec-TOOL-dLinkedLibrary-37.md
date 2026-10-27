# TOOL-dLinkedLibrary-37 — a `reconstructed` or `imported` origin graded on its provenance, so the adopt program's own records read green

**Status:** OPEN · rev-1 · 2026-10-26 · node d · Tier-2 · base 5fede642 · streams tooling · order 22 · advances TOOL-dLinkedLibrary-26

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-26-build-TOOL-dLinkedLibrary-1-agent-ledger.md](../build/2026-10-26-build-TOOL-dLinkedLibrary-1-agent-ledger.md) | journal | TOOL-dLinkedLibrary-1 TOOL-dLinkedLibrary-2 TOOL-dLinkedLibrary-3 TOOL-dLinkedLibrary-4 TOOL-dLinkedLibrary-5 TOOL-dLinkedLibrary-6 TOOL-dLinkedLibrary-7 TOOL-dLinkedLibrary-8 TOOL-dLinkedLibrary-9 TOOL-dLinkedLibrary-10 TOOL-dLinkedLibrary-11 TOOL-dLinkedLibrary-12 TOOL-dLinkedLibrary-13 TOOL-dLinkedLibrary-14 TOOL-dLinkedLibrary-15 TOOL-dLinkedLibrary-16 TOOL-dLinkedLibrary-17 TOOL-dLinkedLibrary-18 TOOL-dLinkedLibrary-19 TOOL-dLinkedLibrary-20 TOOL-dLinkedLibrary-21 TOOL-dLinkedLibrary-22 TOOL-dLinkedLibrary-23 TOOL-dLinkedLibrary-24 TOOL-dLinkedLibrary-25 TOOL-dLinkedLibrary-38 TOOL-dLinkedLibrary-39 TOOL-dLinkedLibrary-40 TOOL-dLinkedLibrary-41 TOOL-dLinkedLibrary-42 TOOL-dLinkedLibrary-43 TOOL-dLinkedLibrary-44 TOOL-dLinkedLibrary-45 TOOL-dLinkedLibrary-46 TOOL-dLinkedLibrary-47 TOOL-dLinkedLibrary-48 TOOL-dLinkedLibrary-49 TOOL-dLinkedLibrary-50 TOOL-dLinkedLibrary-51 TOOL-dLinkedLibrary-52 TOOL-dLinkedLibrary-53 TOOL-dLinkedLibrary-54 TOOL-dLinkedLibrary-55 TOOL-dLinkedLibrary-56 TOOL-dLinkedLibrary-57 TOOL-dLinkedLibrary-58 TOOL-dLinkedLibrary-59 TOOL-dLinkedLibrary-60 TOOL-dLinkedLibrary-61 TOOL-dLinkedLibrary-62 TOOL-dLinkedLibrary-63 TOOL-dLinkedLibrary-64 TOOL-dLinkedLibrary-65 TOOL-dLinkedLibrary-66 TOOL-dLinkedLibrary-67 TOOL-dLinkedLibrary-68 TOOL-dLinkedLibrary-69 TOOL-dLinkedLibrary-70 TOOL-dLinkedLibrary-71 TOOL-dLinkedLibrary-72 TOOL-dLinkedLibrary-73 TOOL-dLinkedLibrary-74 TOOL-dLinkedLibrary-75 TOOL-dLinkedLibrary-76 TOOL-dLinkedLibrary-77 TOOL-dLinkedLibrary-78 TOOL-dLinkedLibrary-79 TOOL-dLinkedLibrary-80 TOOL-dLinkedLibrary-81 TOOL-dLinkedLibrary-82 TOOL-dLinkedLibrary-83 TOOL-dLinkedLibrary-84 TOOL-dLinkedLibrary-85 TOOL-dLinkedLibrary-86 TOOL-dLinkedLibrary-87 TOOL-dLinkedLibrary-88 TOOL-dLinkedLibrary-89 TOOL-dLinkedLibrary-90 TOOL-dLinkedLibrary-91 TOOL-dLinkedLibrary-92 TOOL-dLinkedLibrary-93 TOOL-dLinkedLibrary-94 TOOL-dLinkedLibrary-95 TOOL-dLinkedLibrary-96 |
| [2026-10-26-build-TOOL-dLinkedLibrary-37-deviation-371.md](../build/2026-10-26-build-TOOL-dLinkedLibrary-37-deviation-371.md) | deviation | — |
| [2026-10-27-review-TOOL-dLinkedLibrary-37-spec-audit.md](../reviews/2026-10-27-review-TOOL-dLinkedLibrary-37-spec-audit.md) | spec-audit | TOOL-dLinkedLibrary-43 TOOL-dLinkedLibrary-45 TOOL-dLinkedLibrary-48 TOOL-dLinkedLibrary-49 TOOL-dLinkedLibrary-38 TOOL-dLinkedLibrary-50 TOOL-dLinkedLibrary-39 TOOL-dLinkedLibrary-44 TOOL-dLinkedLibrary-41 TOOL-dLinkedLibrary-46 TOOL-dLinkedLibrary-47 TOOL-dLinkedLibrary-51 TOOL-dLinkedLibrary-42 TOOL-dLinkedLibrary-40 TOOL-dLinkedLibrary-52 TOOL-dLinkedLibrary-53 |

<!-- /gen:spec-records -->

## 1. Goal

The round-1 spec audit of the 25 unit specs
(`memory/builds/dLinkedLibrary/reviews/2026-10-26-review-TOOL-dLinkedLibrary-1-spec-audit.md`) confirmed
finding **id 58 at BLOCKER**, report item **R1**. No other id shares the item.

`TOOL-dLinkedLibrary-9` §4 "The derivation" takes the landing build from a record's folder (step 2) and
the subject build from its served unit (step 4), and its table greens `reconstructed@<sha8> <sources>`
and `imported:<path>` only when step 5 answers `not-written`. The adopt program writes every routing
record (`TOOL-dLinkedLibrary-8` §4 "The decisions") and every instruction ruling
(`TOOL-dLinkedLibrary-23` S7, through the door's `--imported-from`) into the adoption build's own
`build/` folder, serving the adoption unit. Both steps land on that build, step 5 answers `written`, and
the unguarded `record origin` leg reds every such record in every adopter. The `reconstructed-but-written`
plant pins the red as correct.

This unit grounds both values on provenance alone, rewrites that plant, and plants one record of each
kind minted through the real program in the adoption build's own folder. It repairs
`TOOL-dLinkedLibrary-9` and builds one step after it (order 22).

## 2. Scope (IN)

- **S1** — The grounds. In `derive_origin` (`tools/memory-tree/record_origin.py`, `TOOL-dLinkedLibrary-9`
  S2), a stored `reconstructed@<sha8> <sources>` is green when `<sha8>` resolves to the landing commit
  `L` or an ancestor of it and every source is a blob at `<sha8>`; a stored `imported:<path>` is green
  when `<path>` is a blob at `L^` and lies outside the memory root. Neither reads step 5's answer, so
  both hold whatever build folder the record sits in. A stored `written` is graded by step 5 as before.
  Observed by AC1 and AC2.
- **S2** — The plant that pinned the red. The `reconstructed-but-written` case of `record_origin.py
  --fixture` is renamed `reconstructed-in-landing-build` and expects exit 0, and a sibling
  `imported-in-landing-build` stores `imported:adr-1.md` on a record whose subject last changed in its
  own build, also exit 0. Observed by AC1.
- **S3** — The program's own records, planted. `adopt-routing` builds the scratch adoption build
  `dAdopt` with unit `TOOL-dAdopt-1`, a decision document under `adr/`, and two raters' labels files that
  agree on every candidate; it runs `adopt_program.py decisions --rate` there (`TOOL-dLinkedLibrary-8`
  S6), which writes the routing record into `memory/builds/dAdopt/build/`, commits it under a subject
  naming `TOOL-dAdopt-1`, and runs `--check`. `adopt-ruling` runs `gov_record.py new ruling
  --imported-from CLAUDE.md --build dAdopt --unit TOOL-dAdopt-1` over a tracked `CLAUDE.md`, the call
  `TOOL-dLinkedLibrary-23` S7 makes, commits it the same way, and runs `--check`. Each expects exit 0.
  Observed by AC3.
- **S4** — Provenance still bites. A `reconstructed@` record whose source is absent at its `<sha8>`, and
  an `imported:` record naming a path under the memory root, each still red, so S1 widens no value to
  "anything goes". Observed by AC2.
- **S5** — The page. `help/record-origin.md` (`TOOL-dLinkedLibrary-9` S7) says that `reconstructed` and
  `imported` are graded on their provenance in any build folder, and that the check does not ask
  whether a record typed `reconstructed` could have been `written`. Observed by AC4.

## 3. Non-goals (OUT)

- The `written` direction and its derivation: `TOOL-dLinkedLibrary-9`'s steps 1 to 5, unchanged.
- The door, the adopt program and the ruling verb: `TOOL-dLinkedLibrary-8`'s and
  `TOOL-dLinkedLibrary-23`'s; the plants call them and change neither.
- Judging a `reconstructed` record that could have been written: a writer that under-claims ranks its
  record lower (`origin_rank`), which harms nothing, and the check reads provenance, never intent.
- The report's left-shift gate, a cross-spec probe in the spec audit: a harness change outside this
  build.

### Edges

- **consumes-from** `TOOL-dLinkedLibrary-9` — `derive_origin`, its table and its `--fixture` plants, whose two provenance rows S1 rewrites and whose `reconstructed-but-written` plant S2 renames (id 58)
- **consumes-from** `TOOL-dLinkedLibrary-8` — `adopt_program.py decisions --rate`, the routing record it writes, and the door's `--imported-from`, through which S3 mints the two planted records (id 58)
- **hands-off** `TOOL-dLinkedLibrary-23` — `imported:<path>`, graded on provenance from this unit on, so each ruling record its `--rule` writes in the adoption build's own folder reads green (id 58)
- **consumes-from** external — dTotalRecall's door `gov_record.py new` (TOOL-dTotalRecall-2), which S3's ruling plant calls

## 4. Design

### Evidence

- `TOOL-dLinkedLibrary-9` §4's table requires step 5's `not-written` for both values, and its plant
  `reconstructed-but-written` expects exit 1 for a `reconstructed@` record whose subject last changed
  in its own build.
- `TOOL-dLinkedLibrary-8` §4 "The decisions" names the routing record
  `<date>-build-<unit id>-decision-routing.md` in the adoption build's `build/` folder,
  `**Serves:** research <unit id>`, with a column-0 `**Origin:** reconstructed@<sha8> <sources>` line.
- `TOOL-dLinkedLibrary-23` S7 writes each ruling through `gov_record.py new ruling --imported-from <src>`
  under the build and unit of `core.py adopt instructions --build <slug> --unit <id>`.
- `TOOL-dLinkedLibrary-8` S2 has the door check, at write time, that `--reconstructed-from` resolves with
  each source present at it and that `--imported-from` is tracked and outside the memory root: the
  provenance S1 re-derives from history, independently of that write path.

### The table after S1

| Stored | Green when |
|---|---|
| `written` | step 5 answers `written` |
| `reconstructed@<sha8> <sources>` | `<sha8>` is `L` or an ancestor of `L`, and each source is a blob at `<sha8>` |
| `imported:<path>` | `<path>` is a blob at `L^`, outside the memory root |
| anything else | never |

### Files touched (estimate)

- `tools/memory-tree/record_origin.py`: S1, and the plants of S2 to S4
- `help/record-origin.md`: S5

### Alternatives rejected

- **Exempting the adoption build from step 5.** It needs a list of adoption builds, a typed fact beside
  the routing record's own binding, and a record written under any other build would still red.
- **Writing the adopt program's records into a build other than the adoption build.** The door mints
  under the claim of the build the owner opened (`TOOL-dLinkedLibrary-8` S3); moving them breaks that
  claim to satisfy a check.
- **Retiring the `reconstructed-but-written` plant without a replacement.** The rename keeps its fixture
  as a green case, so the provenance-only reading is itself observed.

## 5. Production-readiness checklist

- security — read-only, as `TOOL-dLinkedLibrary-9` §5: blobs are read by name through git, never from
  the working tree.
- perf / scale — the same three history reads per run; S1 drops step 5 from two rows, so it adds none.
- error / empty / loading states — unchanged: exit 2 on a shallow clone or failed git call.
- observability — a red line still names the stored value and the commit or path that failed it.
- risks — a writer typing `reconstructed` for a record it wrote passes; it under-claims and ranks last.
- testing — the plants of S2 to S4 under `record_origin.py --selftest`.
- migration — none: no record carries an origin line before `TOOL-dLinkedLibrary-8`'s door.
- user docs — `help/record-origin.md`, S5.

## 6. Acceptance criteria

- **AC1** — When `python record_origin.py --fixture --plant reconstructed-in-landing-build` and
  `--plant imported-in-landing-build` run, each exits 0.
  Red when: either value is graded by step 5, so a record in its subject's own build reds.
- **AC2** — When `--plant reconstructed-unresolved`, a planted `reconstructed-source-absent` and
  `--plant imported-memory` run, each exits 1 naming the `<sha8>`, the absent source or `memory/DECISIONS.md`.
  Red when: S1 greens a value whose provenance does not hold.
- **AC3** — When `python record_origin.py --fixture --plant adopt-routing` and `--plant adopt-ruling`
  run, each prints the record it minted under `memory/builds/dAdopt/build/` and exits 0.
  Red when: a routing record or ruling the real program writes in its adoption build reads red, as it
  does with `derive_origin` staged back to the rev-1 table.
  fixture: a scratch repository under `%TEMP%/ro-<case>`, built by the plant, with the memory-tree kit's
  `adopt_program.py` and the door installed from this tree.
- **AC4** — When `grep -n "provenance" record-origin.md` runs over the help page, it finds the sentence
  naming both values and the question the check does not ask.
  Red when: the page still says either value requires a record not written in its subject's build.

## 7. Gates

`memory hygiene` · `spec tokens (a spec's own names resolve)` · `lexicon naming predicates`

New arm: tools/memory-tree/record_origin.py --selftest (the `record origin selftest` leg `TOOL-dLinkedLibrary-9` adds) · covers AC1 AC2 AC3 · the renamed plant, `reconstructed-source-absent` and the two adopt plants, the failing case staged by restoring step 5's `not-written` to the two provenance rows · none

## 8. Open questions

- **F1 — Which binding line does a unit the spec audit promoted carry?** Options: (a) `**Derived:**`
  naming `PLAY-dClosedLoop-2`; (b) a `part k/n` carry of the repaired unit's clause. (b) splits a clause
  unit 9 carries whole; veto 1 discards it. RESOLVED (agent, 2026-10-26, delegated): (a), rung 3, the
  precedent `TOOL-dTotalRecall-40` set for this chain. widens: none · relaxes: none

## 9. Revision log

- rev-1 · 2026-10-26 · initial draft, promoted from the round-1 spec audit of the 25 unit specs, id 58
  (BLOCKER, item R1), on the skeptic's corrected fix.

## 10. Reuse audit

The seam extended is `derive_origin` and its table in `TOOL-dLinkedLibrary-9`'s `record_origin.py`, with
its `--fixture` plants; the history readers it already calls (`read_adding_commits` and `read_blobs_at`,
`tools/memory-tree/tree_lib.py:302`, :328) answer S1 with no new reader. `python
tools/codebase-map/reuse_lookup.py "check a record's stored provenance against the commit history"`
ranked `check`, `records`, `checks` and `build_commit`, none a provenance grader, so no existing seam
fits beyond the module being repaired.

Recall terms used: `python tools/memory-recall/query.py "how is a promoted spec-audit finding repaired by a unit placed after the unit it repairs" --terms "spec-audit promoted finding repairs order rescope add batch minors disjoint write set"`
