# TOOL-aGraftedHelix-6 — a decision row or gotcha whose normalized text another record already holds reds

**Status:** SPECCED · rev-2 · 2026-10-04 · node a · Tier-2 · base 5266d22e · streams tooling · order 6 · ratified 2026-10-04

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-04-prompt-TOOL-aGraftedHelix-1-1-spec-brief.md](../prompts/2026-10-04-prompt-TOOL-aGraftedHelix-1-1-spec-brief.md) | journal | TOOL-aGraftedHelix-1 TOOL-aGraftedHelix-2 TOOL-aGraftedHelix-3 TOOL-aGraftedHelix-4 TOOL-aGraftedHelix-5 TOOL-aGraftedHelix-7 TOOL-aGraftedHelix-8 TOOL-aGraftedHelix-9 |
| [2026-10-04-prompt-TOOL-aGraftedHelix-1-2-build-brief.md](../prompts/2026-10-04-prompt-TOOL-aGraftedHelix-1-2-build-brief.md) | journal | TOOL-aGraftedHelix-1 TOOL-aGraftedHelix-2 TOOL-aGraftedHelix-3 TOOL-aGraftedHelix-4 TOOL-aGraftedHelix-5 TOOL-aGraftedHelix-7 TOOL-aGraftedHelix-8 TOOL-aGraftedHelix-9 TOOL-aGraftedHelix-10 TOOL-aGraftedHelix-11 TOOL-aGraftedHelix-12 TOOL-aGraftedHelix-13 TOOL-aGraftedHelix-14 TOOL-aGraftedHelix-15 |
| [2026-10-04-review-TOOL-aGraftedHelix-1-spec-audit-round1.md](../reviews/2026-10-04-review-TOOL-aGraftedHelix-1-spec-audit-round1.md) | spec-audit | TOOL-aGraftedHelix-1 TOOL-aGraftedHelix-2 TOOL-aGraftedHelix-3 TOOL-aGraftedHelix-4 TOOL-aGraftedHelix-5 TOOL-aGraftedHelix-7 TOOL-aGraftedHelix-8 TOOL-aGraftedHelix-9 |

<!-- /gen:spec-records -->

## 1. Goal

Hygiene check 20 reds an id held twice inside one row document, and nothing reds the same CONTENT
held twice: two nodes that record one decision under two ids, or one gotcha under two file names,
pass every leg and leave the corpus with two answers to one question. This unit adds hygiene check
28 to the memory-tree kit: one normalized content key per decision row and per gotcha body, and a
red when a record added since the mainline merge-base holds a key a record of another identity
also holds. It is the exact half of helixir's
write-time duplicate check; the near half is `TOOL-aGraftedHelix-9`.

## 2. Scope (IN)

- **S1** — `tools/memory-tree/tree_lib.py` gains `derive_content_key(text)`, the five-step
  normalization §4 "The key" pins, so the kit holds one spelling of it. Observed by AC1 and AC2.
- **S2** — The record enumeration `scan_records` that `TOOL-aGraftedHelix-9` adds to
  `tools/memory-tree/row_grammar.py` gains a `body` field on each gotcha record: the file's text after
  the block the shared `FM_RE` matches. A row's keyed text is its existing `summary`, which already
  stands after the row's own id. Observed by AC1 and AC5.
- **S3** — A new mode, `row_grammar.py --check-content [<base>]`, whose base defaults as
  `--check-relations` derives one. It derives every record's key and reds each
  key held by records of two or more distinct identities when at least one holder was ADDED since
  the mainline merge-base, one finding per key naming every holder's location. The base and the
  added set are `TOOL-aGraftedHelix-9`'s `derive_relation_base` and identity-presence test, read
  the same way. A key whose every holder is present at the base is LANDED: it is counted and not
  reported, because nobody may edit a landed append-only row or take it out. With no resolvable
  base every key is graded, and the summary line says so. A key held twice under ONE identity is not
  this check's: check 20 owns an id twice in one document, check 24 owns one across a `cut`
  rotation, and a `snapshot` carry-forward is that by design, across documents included. An empty
  key is not graded and is counted. Every run prints a summary line, a graded count of 0 included.
  Observed by AC1, AC2, AC3, AC4, AC5, AC10 and AC11.
- **S4** — Hygiene check 28 is wired: the module constant `CONTENT_CHECK = 28`, a full-run dispatch
  block in `tools/memory-tree/check-memory-hygiene.sh` that prints the mode's output on a green run
  too and keys offenders under 28, its catalog entry in `tools/memory-tree/HYGIENE.template.md`
  re-rendered into `memory/HYGIENE.md`, and the kit README's check count moved to 28. Observed by
  AC7 and AC8.
- **S5** — The module header states what check 28 does NOT check, and each new branch has a
  `--selftest` arm whose fixture makes it fire. Observed by AC1 to AC4, AC9, AC10 and AC11.
- **S6** — The memory-tree kit version moves once, after the last move, in every carrier
  `tools/check-kit-versions.sh` pairs, and the row-grammar dossier's prose names the new mode. One
  of those carriers is line 1 of `memory/guides/BUILD-METHOD.md`, which the re-render moves and
  nothing else in that file, under `TOOL-aGraftedHelix-3`'s §8 F1 ruling (§8 F1 here). Observed by
  AC12; the kit-versions, verdict-epoch and codebase-map legs grade the rest at the close (§7).

## 3. Non-goals (OUT)

- Near matches, paraphrases and contradictions. Those are `TOOL-aGraftedHelix-9`'s check 27.
- An id held twice. Check 20 and check 24 already grade it, and grading it here would be a second
  answer to their question.
- Any record kind other than decision rows and gotchas, including backlog asks under the `shards`
  layout: `scan_records` takes only the decision index and its archives from the row documents.
- A shrink-only pin, a waiver registry or a conf key. An adopter's landed duplicates are LANDED keys,
  counted and never reported, so a kit update cannot red a corpus nobody may edit (§8 F2). A new
  duplicate cannot land unnoticed: a push carries both sides of any merge, so the push boundary's
  bar grades the added holder while it is still a record its author can change. The bypass that
  skips that bar skips every other leg too.
- The pre-commit `--staged` path. Check 28 runs on full runs only, as checks 13 to 20 and 24 do.
- Front matter. Two gotchas with one body and different `description` lines are one record twice.

### Edges

- **consumes-from** `TOOL-aGraftedHelix-9` — the record enumeration `scan_records` in
  `tools/memory-tree/row_grammar.py` and the shared `FM_RE` in `tree_lib.py`, both built in that
  unit's pass; without them this unit would walk the decision index and the catalogue a second time.
  Also `derive_relation_base` and the identity-presence test that splits ADDED records from those
  present at the base, which decide which keys this check reports.
- **hands-off** `TOOL-aGraftedHelix-13` — the hygiene engine's dispatch block for check 28, which
  calls `--check-content` and keys offenders under `CONTENT_CHECK`. AC7 here proves the block is
  present; that unit observes it red the leg and print its summary on a green run (round-1 audit
  finding 20).

## 4. Design

### Evidence

- Check 20, in `row_grammar.py`, is per-file id uniqueness across the decision index and its
  archives, pinned shrink-only by `ROW_DUPLICATE_PIN`. Its three pinned survivors are ids held twice,
  each with different text, so none of them is a content duplicate and none moves this check.
- Measured at base `5266d22e`, 2026-10-04, node `a`, with a read-only probe over the same population
  `scan_records` will return: 354 records, 260 rows and 94 gotchas. Under the §4 key, 0 keys are
  held by two identities and 0 keys are empty; the shortest key is 150 characters. Under a looser
  variant that also strips every punctuation mark, still 0. No two records share even the first 80
  characters of that loosest key. So there is no live duplicate to repair and nothing to pin.
- Why emphasis is stripped. `memory/DECISIONS.md` carries two row shapes, `- <id> · <text>` and
  `- **<id>** — **<text>**`, so the same decision re-minted in the other shape differs from the first
  only in emphasis and separator, and a key that kept either would let it through.
- Placement follows check 24, which rides `row_grammar.py` as a second mode, `--check-rotation`,
  because the module owns the row grammar; `TOOL-cSpliceWarden-6` is the ruling that a check grading
  rows delegates to that owner.

### The key

`derive_content_key(text)`, applied to a row's `summary` or a gotcha's `body`, in this order:

1. Every markdown link becomes its text: `\[([^\]]*)\]\([^)]*\)` is replaced by `\1`.
2. Every ISO date, `\b\d{4}-\d{2}-\d{2}\b`, is replaced by nothing.
3. Every asterisk, underscore and backtick is replaced by nothing.
4. The text is lowercased, every whitespace run collapses to one space, and both ends are stripped.
5. A leading run of `·`, `—`, `:`, `-` and spaces is stripped, which is the row separator.

The row's own id is already outside `summary`, and the front matter outside `body`. Ids cited
inside the text stay in the key, so two rows that differ only in which record they cite are two keys.
The measurement ran steps 1 to 4; step 5 strips a class the looser punctuation-free variant also
strips, and that variant measured 0 as well.

### Output

A finding, one line per duplicated key, holders in scan order:

```
check 28: 2 records hold one content key — memory/DECISIONS.md:140 (TOOL-x-12), memory/archive/DECISIONS.2026-08-10.md:31 (TOOL-y-3) — key "a check that grades a declared mode delegates to wh…"
```

Every run, red or green, prints one summary line:

```
row-grammar: check 28 graded <n> record(s) in <base8>..HEAD — <r> row(s), <g> gotcha(s), <e> with an empty key, <d> key(s) held twice, <l> landed key(s) held twice and not reported
```

With no resolvable base, `in <base8>..HEAD` reads `with no mainline base, every key graded`.

### Inventory

| identifier | kind | cell |
|---|---|---|
| `derive_content_key` | function, in `tree_lib.py` | `py.function` |
| `check_content` | function | `py.function` |
| `cmd_check_content` | function | `py.function` |
| `CONTENT_CHECK` | module constant | none graded |
| `body` | a `scan_records` field on a gotcha | none graded |
| `--check-content` | CLI flag | none graded |

Every function name was answered `OK` by `lexicon.py --suggest <name> --as py.function`.

### Rollout

The check lands red with no pin, because the tree holds no duplicate, and in every adopter, because
landed duplicates are counted rather than reported. Every decision row and gotcha this build adds is
graded by it at the close. A hit there always includes a record that has not landed, and the remedy
is to reword or drop THAT record; a landed row is never edited or removed.

### Files touched (estimate)

- `tools/memory-tree/tree_lib.py`
- `tools/memory-tree/row_grammar.py`
- `tools/memory-tree/check-memory-hygiene.sh`
- `tools/memory-tree/HYGIENE.template.md`
- `tools/memory-tree/README.md`
- `memory/HYGIENE.md`
- `memory/map/features/row-grammar.md`
- `memory/guides/BUILD-METHOD.md`, line 1 only, the kit version marker the re-render moves
- the memory-tree kit's version carriers

### Alternatives rejected

- Extending check 20. It is per FILE and counts ids, and its pins are id counts; this check is
  corpus-wide over two record kinds, and a gotcha is not a row document.
- Hosting it in `gotchas.py --check`. That module reads no row document, and `row_grammar.py` takes
  its shared helpers from `tree_lib.py`, never from a sibling engine.
- Hashing the key. Equality is the same, and the finding could no longer print the key's start,
  which is how a reader recognises the record.
- Keying gotchas on the `description` line. The brief pins bodies, and two records with one body
  are one record whatever their one-line summaries say.

## 5. Production-readiness checklist

- security — Read-only over tracked files; it writes nothing.
- perf / scale — One pass over the records `scan_records` already reads and one dict, 354 records
  today; no index. The base costs unit 9's spawns, one merge-base, two tree listings and one
  `git show` per row document, which a run that also grades check 27 pays once if the two share it.
- error / empty / loading states — An empty population prints a graded count of 0; an empty key is
  counted, not compared; an unreadable record surfaces through the enumeration's existing refusal.
- observability — The summary line prints on every run, and the hygiene dispatch block shows it on
  a green run.
- risks — Two records that legitimately carry one text would red. None exists today, and the remedy
  is one rewording in a record that has not landed.
- testing — `row_grammar.py --selftest` arms for every branch (AC1 to AC4), a staged break over the
  real corpus (AC6), and the clean real tree (AC5).
- migration — None. No conf key, no pin.
- user docs — Check 28's catalog entry in `memory/HYGIENE.md`, rendered from the kit template, and
  the kit README's row for the mode.

## 6. Acceptance criteria

- **AC1** — When a `--selftest` fixture holds two gotchas whose bodies differ only in letter case,
  whitespace runs, a date, a link target and emphasis, `row_grammar.py --check-content` exits 1 with
  one `check 28:` line naming both paths. Observed by
  `python tools/memory-tree/row_grammar.py --selftest`.
  Red when: any one of those five differences keeps the two keys apart.
- **AC2** — When a fixture decision index holds one row as `- <id> · <text>` and a second, under a
  new id, as `- **<id>** — **<text>**`, the mode exits 1 naming both locations. Observed by
  `python tools/memory-tree/row_grammar.py --selftest`.
  Red when: the shape difference lets the re-mint through.
- **AC3** — When a fixture under `ROTATION_MODE=snapshot` holds one id with one text in its
  decision index and again in a rotated archive, and separately two gotchas with different bodies,
  the mode prints no `check 28:` line for either and exits 0. Observed by
  `python tools/memory-tree/row_grammar.py --selftest`.
  Red when: a same-identity pair across two documents, which a build keyed on path and id reports,
  or two distinct bodies is reported.
- **AC4** — When a fixture holds no decision index and no gotcha, the mode exits 0 and prints its
  summary line with a graded count of 0. Observed by
  `python tools/memory-tree/row_grammar.py --selftest`.
  Red when: the empty population prints nothing.
- **AC5** — When `python tools/memory-tree/row_grammar.py --check-content` runs on this tree at the
  unit's build commit, it exits 0 and its summary line's graded count equals the number of records
  `scan_records` returns.
  Red when: it reds on this tree, or its graded count is 0.
  figure: DERIVED at observation; it read 354 at base `5266d22e` and grows with every record.
- **AC6** — When a scratch clone of this tree copies `memory/gotchas/two-answers-to-one-question.md`
  to a second name in the same folder and commits the copy, `row_grammar.py --check-content` there
  exits 1 naming both paths, the copy being the added holder.
  Red when: the copy passes.
  fixture: the clone goes under a short `%TEMP%` directory, never inside the worktree.
- **AC7** — When `grep -n 'CONTENT_CHECK = 28' tools/memory-tree/row_grammar.py` and
  `grep -n 'check-content' tools/memory-tree/check-memory-hygiene.sh` run, each prints one line.
  Red when: the constant or the dispatch block is absent.
- **AC8** — When `grep -c '^28\. ' memory/HYGIENE.md` runs, it prints 1, and the kit README's row for
  `check-memory-hygiene.sh` reads `28 checks`.
  Red when: the catalog or the README count disagrees with the module constant.
- **AC9** — When the header of `tools/memory-tree/row_grammar.py` is read, it states that check 28
  does NOT check a paraphrase, an id held twice, a record outside the two kinds, front matter, or a
  duplicate whose every holder had landed at the base.
  Red when: any of the five is unstated.
- **AC10** — When a `--selftest` fixture commits two decision rows with one text under two ids at
  its base, and `row_grammar.py --check-content <base>` runs with nothing added, it exits 0 and its
  summary line counts 1 landed key. When a third row restating them is then added under a new id,
  it exits 1 naming all three holders. Observed by
  `python tools/memory-tree/row_grammar.py --selftest`.
  Red when: a landed pair reds, which no author can repair, or an added restatement of it passes.
- **AC11** — When a `--selftest` fixture holds two records whose keys normalize to empty, the mode
  prints no `check 28:` line and its summary counts 2 with an empty key; when three records hold
  one key, the finding names all three. Observed by
  `python tools/memory-tree/row_grammar.py --selftest`.
  Red when: two empty-bodied records red each other, or a three-holder finding names two.
- **AC12** — When `git diff <the pass's parent sha> -- memory/guides/BUILD-METHOD.md` runs at the
  pass's commit, it changes line 1 only.
  Red when: the method's content moved, which shared invariant 10 forbids.

## 7. Gates

`memory hygiene` · `row-grammar selftest` · `kit/dogfood doc parity` · `memory-hygiene self-test` · `lexicon naming predicates` · `codebase-map coverage + freshness` · `recall floor` · `recall floor arms` · `kit version markers` · `verdict epoch (kit version dates the engine)` · `kit epoch (shipped bytes move, the version moves)`

A pass runs `python tools/memory-tree/row_grammar.py --selftest` as its direct check, each new arm
observed red on a staged break first; the close runs the legs listed above. The two recall legs are
owed by the memory root's guard, which `memory/HYGIENE.md` reaches, and the last three grade S6's
kit version bump.

New arm: `tools/memory-tree/row_grammar.py --selftest` · fixture trees holding a gotcha body twice under five surface differences, a row re-minted in the other shape, a same-id pair across a snapshot rotation, distinct bodies, an empty population, a landed pair with and without an added restatement, two empty keys and three holders · the module's arm count rises by the new arms

## 8. Open questions

- **F1 — Does the memory-tree bump's re-render of line 1 of `memory/guides/BUILD-METHOD.md` breach
  shared invariant 10, which says no unit edits that file?** `TOOL-aGraftedHelix-3` §8 F1 decided
  this for the kit's version marker: the line is a derived carrier `check-kit-versions.sh` pairs
  with the engine constant, and the invariant protects the method's content, which the render
  leaves byte-identical below line 1. RESOLVED (agent, 2026-10-04, delegated): as unit 3's Option
  A, the file listed under Files touched as line 1 only, and AC12 observes that only line 1 moved.
- **F2 — How does check 28 treat an adopter's landed duplicates?** (a) Grade only keys an added
  record holds, as check 27 grades only added records; (b) a shrink-only content-duplicate pin with
  an emit verb, as check 20 carries; (c) ship the check dark in the example conf. Landed rows may
  never be edited or removed, so (b) pins a count nobody may lower, the old "fold the two" remedy
  asks for an edit nobody may make, and (c) leaves every adopter ungraded. (a) grades every new duplicate in every adopter and reuses the
  base unit 9 already derives. RESOLVED (agent, 2026-10-04, delegated): (a).

## 9. Revision log

- rev-1 · 2026-10-04 · initial draft from the aGraftedHelix spec brief, with the duplicate census
  measured on node `a` at base `5266d22e`.
- rev-2 · 2026-10-04 · §1 §3 §4 §5 §6 §7 §8 · S3 S5 S6 · AC3 AC6 AC9 AC10 AC11 AC12 · folded the
  round-1 spec audit's findings on this unit: 48 (landed duplicates are counted and never reported,
  §1, S3, §3, §4 Rollout, §8 F2, AC10, and AC6's copy committed so it is the added holder); 21 (AC3's same-id pair sits across a snapshot rotation); 22 (AC11, the
  empty-key branch and three holders); 36 (§7 states that the pass runs the module's `--selftest` as
  its direct check); and 37 (`memory/guides/BUILD-METHOD.md` line 1 listed, §8 F1 citing unit 3's
  ruling, AC12). §3 Edges extends the consumes-from to unit 9's base and gains the hands-off to the
  unit promoted from finding 20.

## 10. Reuse audit

The seams extended, each verified against source at base `5266d22e`: the record enumeration
`scan_records` and the shared `FM_RE` that `TOOL-aGraftedHelix-9` builds, so this unit adds a key
and a mode and no second walk; `tree_lib.py` as the kit's home for helpers two modules share; and
check 24's `--check-rotation` as the precedent for a second mode on `row_grammar.py` with its own
dispatch block. `reuse_lookup.py` with "red when two records carry the same normalized text"
ranked `read_text` and `write_text` in `gen_build_index.py` first, which are byte IO and not a
normalization, then `records` in `gotchas.py`, which the enumeration above supersedes for this
purpose without importing an engine. Its `unscanned layers: .sh` line means the hygiene engine's
dispatch was read by hand. No existing seam computes a content key: the recall query's hits were
check 20's per-file id uniqueness and its `ROW_DUPLICATE_PIN`, `TOOL-aCollapsedScan-10` confirming
that check 20 grades ids on the bar, and this build's own brief. No hit disagreed with the code.

Recall terms used: `duplicate content row document check 20 ROW_DUPLICATE_PIN re-mint byte-identical gotcha body decision index uniqueness`
