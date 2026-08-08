# TOOL-aFoldedQuarry-6 — U4: the bug-class corpus and its per-diff checklist

**Status:** CLOSED · rev-3 · 2026-08-08 · node a · Tier-2 · base 42c3f4dc · streams tooling · ratified 2026-08-08

## 1. Goal

Give the kit a catalogue of recurring bug classes that a reviewer is HANDED rather than pointed at:
one authored record per class, a generated index, and a `--for-diff` mode whose stdout is the
checklist for the diff in front of them. A checklist nobody can finish is not a checklist.

## 2. Scope (IN)

- **S1** — `tools/memory-tree/gotchas.py` reads one authored record per class from
  `<MEMORY_ROOT>/gotchas/*.md` and renders the generated region of
  `<MEMORY_ROOT>/gotchas/INDEX.md`. `--check` byte-compares, `--write` renders, `--selftest` runs
  fixtures.
- **S2** — front matter is `name` and `description`, plus optional `kind` (default `class`) and
  `universal`, all at COLUMN 0. A key indented under a parent is silently dropped by any simple
  parser, so an indented key is a NAMED error rather than a quiet omission.
- **S3** — anchors are DERIVED, not declared: the backtick-quoted path-like tokens in the record
  body. A hand-written anchor list is a second copy of what the body already says. Derivation
  over-selects rather than under-selects, and that trade is stated in the module rather than
  discovered.
- **S4** — three harvest defects are carried, and each ARM IS A DELIVERABLE, not a nice-to-have:
  a token containing `::` inside backticks harvests to nothing; a directory anchor written with a
  trailing slash harvests to nothing; and an anchor's BASENAME matches tree-wide however much path
  precedes it. Documented behaviour that no test pins is indistinguishable from a bug nobody has
  noticed, and the point of carrying them is that the next reader does not re-derive them the
  expensive way. A future change that "fixes" one must fail loudly and be made deliberately.
- **S4b** — a record's anchors NEVER select inside `<MEMORY_ROOT>/gotchas/`. Every record cites paths
  under the catalogue when describing its own class, and selection matches on basename, so without
  this exclusion a diff that touches the catalogue emits most of the catalogue — noise that trains
  reviewers to skip the checklist.
- **S5** — check 17: `INDEX.md` freshness. Check 18: every `kind: class` record DECLARES its
  resolution — it names a gate or says in as many words that it has none. Check 19: the INERT-ANCHOR
  arm — a `kind: class` record whose anchors resolve ONLY into the append-only tree is reachable on
  paper and dead in practice.
- **S6** — `--declares` is the ONE copy of the "names a gate or says it has none" predicate. No
  consumer re-types the alternation; the check calls the same function.
- **S7** — the `universal` set is BUDGETED explicitly: `UNIVERSAL_BUDGET` in `.memory-tree.conf`,
  MEASURED against this corpus and recorded in the build journal, with `--report` printing the count
  and a blank value turning the check off — the same convention as every other pin in this kit.
  Upstream designed for 10 and measured 40, and 40 of a 68-entry checklist are the always-emitted
  core, so an unmeasured budget is a number somebody guesses later.
- **S7b** — check 19's fixture CONTAINS a populated append-only area and a record whose only anchor
  points into it. The arm fires only when every path a record reaches is append-only, so on a tree
  with an empty append-only area it can never fire and the rule ships green forever.
- **S8** — the corpus starts from THIS repo's own failure history — the classes this build paid for,
  each citing the measurement that produced it. inCMS's 178 records are not ported: they are its
  history, and here they would be anchors that match nothing.

## 3. Non-goals (OUT)

- Porting inCMS's records. S8 covers why.
- An authored `anchors:` field. S3 covers why.
- Running the checklist automatically inside the review harness. `--for-diff` prints; wiring it into
  a prompt is a separate, deliberate change.
- A severity or priority field. A class is either worth a record or it is not.

## 4. Design

### Data model

```
---
name: vacuous-selector-empty-population
description: a path selector that matches nothing prints nothing, and nothing is what a pass prints
kind: class            # class (default) | note | superseded
universal: false       # true = applies to any diff; costs a slot in UNIVERSAL_BUDGET
---
```

`kind` other than `class` keeps the record in the index, labelled, and takes it out of `--for-diff`
and out of every count. Without it, a record that names no path has to claim `universal: true` to
clear the reachability arm — which puts a policy note on every reviewer's checklist.

### Inventory

| Artifact | Owner |
|---|---|
| `<MEMORY_ROOT>/gotchas/<name>.md` | authored, one per class |
| `<MEMORY_ROOT>/gotchas/INDEX.md` generated region | `gotchas.py` |
| checks 17-19 | `gotchas.py`, delegated from the hygiene gate |
| the append-only ERE | `check-memory-hygiene.sh`, asked for — not retyped |

### Migration

None. `gotchas/` is a new root child, so check 3's sanctioned root set gains it IN THE SAME COMMIT —
otherwise the tree reds between the two edits, which is what the one-commit rollout exists to avoid.

### Rollout

One commit: the module, the corpus, the generated index, the three checks, the conf key, the gate
legs and the documentation.

### Files touched (estimate)

One new module, one new corpus directory, the hygiene gate, the conf, the gate-leg manifest and the
two kit documents.

### Alternatives rejected

- **Author the anchors.** Rejected by S3.
- **Let a record with no anchors pass silently.** Rejected: it is reachable on paper and dead in
  practice, which is the whole failure mode this catalogue is meant to expose in other people's
  gates.

## 5. Production-readiness checklist

- security — N/A. Reads tracked markdown; `--for-diff` runs `git diff --name-only`.
- perf / scale — one read per record, one `git diff` per invocation.
- a11y — N/A. i18n — N/A.
- error / empty / loading states — an empty corpus renders an empty index and is a clean pass. A
  record with no front matter is a named error.
- observability — `--report` prints the counts the budget is measured against.
- risks — none material; the module writes one generated region.
- testing + left-shift gates — `--selftest` with a red and a green arm per rule, including all three
  documented harvest defects.
- migration / rollback — one commit.
- user docs — `HYGIENE.template.md` gains checks 17-19 and the record schema.

## 6. Acceptance criteria

- **AC1** — When a record is added or edited and `INDEX.md` is not re-rendered, check 17 fails naming
  the file.
- **AC2** — When a `kind: class` record neither names a gate nor says it has none, check 18 fails
  naming it; when it says either, it passes.
- **AC3** — When a `kind: class` record's anchors resolve only into the append-only tree, check 19
  fails naming it.
- **AC4** — When `--for-diff <base>..<head>` runs, stdout lists every record whose derived anchors
  intersect the changed paths, plus every `universal` record, and nothing else.
- **AC5** — When a front-matter key is indented under a parent, the parse fails naming the file and
  the key, rather than dropping it.
- **AC6** — When an anchor contains `::`, or a directory anchor carries a trailing slash, it harvests
  to nothing — asserted, not assumed. When an anchor is a bare basename, it selects that file
  wherever it lives.
- **AC7** — When the `universal` count exceeds `UNIVERSAL_BUDGET`, `--check` fails with both numbers.
- **AC8** — When `python tools/memory-tree/gotchas.py --selftest` runs, every arm above has a red and
  a green side and the pass line prints last.

## 7. Gates

`bash tools/run-gates.sh` in full. Checks 17-19 ride `check-memory-hygiene.sh`; a new leg runs
`gotchas.py --selftest`.

## 8. Open questions

none — the two forks below are RESOLVED (owner-ratified 2026-08-08); kept for the record.

- **Fork A — what seeds the corpus.** Options: port upstream's records, or write this repo's own.
  RESOLVED (owner, 2026-08-08): this repo's own, each citing the measurement that produced it. A
  ported record's anchors name files that do not exist here, so it can never fire.
- **Fork B — where `--declares` lives.** Options: a predicate in the module plus a `grep` in the
  shell, or one function every consumer calls. RESOLVED (owner, 2026-08-08): one function. Upstream
  shipped both and they disagreed — the shell grepped the whole file, the module only the body, so a
  `description` carrying the word "gated" satisfied one and not the other.

## 9. Revision log

- rev-1 · 2026-08-08 · initial draft.
- rev-2 · 2026-08-08 · folded review 5: J1 makes the three harvest arms deliverables; J2 adds S4b,
  excluding the catalogue from its own selection; J3 measures the budget and allows a blank to
  disable; J4 adds S7b so check 19's arm can actually fire; J5 pins the sanctioned-set edit to the
  same commit.
- rev-3 · 2026-08-08 · one carried defect turned out NOT to apply: this harvest pattern allows an
  empty tail after the slash, so a trailing-slash directory anchor IS harvested and selects
  everything beneath it, where upstream's dropped it. The arm asserts the DIFFERENCE rather than
  upstream's behaviour, so a future tightening reintroduces the upstream defect loudly.

## 10. Reuse audit

The append-only classification is `check-memory-hygiene.sh`'s, asked for through the print mode U3
added rather than imported a second time. The generated-region mechanics — a marker pair, an exact
slice replacement, a byte-compare `--check` and a `--write` — are `gen_build_index.py`'s, reused in
shape so a reader who understands one understands the other. The checks ride the hygiene gate's
existing delegation seam and the `fail` protocol; the leg registers in `tools/gate-legs.json`. The
budget key follows the measured-pin convention U3 established. The only new thing is the anchor
harvest, and its three known defects are carried as tests rather than as prose.
