# TOOL-dGroundRules-42 — the criterion bug class gains the input respelled to pass a join, and is handed to every spec commit

**Status:** DEFERRED · rev-2 · 2026-10-23 · node d · Tier-1 · base 3708a705 · streams tooling · order 13 · advances TOOL-dGroundRules-12

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-23-build-TOOL-dGroundRules-42-deviation-30.md](../build/2026-10-23-build-TOOL-dGroundRules-42-deviation-30.md) | deviation | — |
| [2026-10-23-prompt-TOOL-dGroundRules-42-build-brief.md](../prompts/2026-10-23-prompt-TOOL-dGroundRules-42-build-brief.md) | journal | — |
| [2026-10-23-review-TOOL-dGroundRules-1-52-closing-diff-round1.md](../reviews/2026-10-23-review-TOOL-dGroundRules-1-52-closing-diff-round1.md) | diff-review | TOOL-dGroundRules-1 TOOL-dGroundRules-2 TOOL-dGroundRules-3 TOOL-dGroundRules-4 TOOL-dGroundRules-5 TOOL-dGroundRules-6 TOOL-dGroundRules-7 TOOL-dGroundRules-8 TOOL-dGroundRules-9 TOOL-dGroundRules-10 TOOL-dGroundRules-11 TOOL-dGroundRules-65 TOOL-dGroundRules-14 TOOL-dGroundRules-15 TOOL-dGroundRules-16 TOOL-dGroundRules-17 TOOL-dGroundRules-18 TOOL-dGroundRules-19 TOOL-dGroundRules-20 TOOL-dGroundRules-21 TOOL-dGroundRules-22 TOOL-dGroundRules-23 TOOL-dGroundRules-24 TOOL-dGroundRules-25 TOOL-dGroundRules-26 TOOL-dGroundRules-27 TOOL-dGroundRules-28 TOOL-dGroundRules-29 TOOL-dGroundRules-30 TOOL-dGroundRules-31 TOOL-dGroundRules-32 TOOL-dGroundRules-33 TOOL-dGroundRules-34 TOOL-dGroundRules-35 TOOL-dGroundRules-36 TOOL-dGroundRules-37 TOOL-dGroundRules-38 TOOL-dGroundRules-39 TOOL-dGroundRules-40 TOOL-dGroundRules-41 TOOL-dGroundRules-43 TOOL-dGroundRules-44 TOOL-dGroundRules-45 TOOL-dGroundRules-46 TOOL-dGroundRules-47 TOOL-dGroundRules-48 TOOL-dGroundRules-49 TOOL-dGroundRules-50 TOOL-dGroundRules-51 TOOL-dGroundRules-52 |
| [2026-10-23-review-TOOL-dGroundRules-35-43-spec-audit-round1.md](../reviews/2026-10-23-review-TOOL-dGroundRules-35-43-spec-audit-round1.md) | spec-audit | TOOL-dGroundRules-35 TOOL-dGroundRules-36 TOOL-dGroundRules-37 TOOL-dGroundRules-38 TOOL-dGroundRules-39 TOOL-dGroundRules-40 TOOL-dGroundRules-41 TOOL-dGroundRules-43 |

<!-- /gen:spec-records -->

## 1. Goal

The round-1 spec audit of units 33 and 34
(`memory/builds/dGroundRules/reviews/2026-10-23-review-TOOL-dGroundRules-33-34-spec-audit-round1.md`)
exited CONVERGED with finding **id 25 at HIGH**, which shares item **H3** with ids 2
(`TOOL-dGroundRules-39`), 17 (`TOOL-dGroundRules-40`) and 21 (`TOOL-dGroundRules-41`). Id 25 is H3
seen from the failure envelope: `TOOL-dGroundRules-34` AC11, AC12, AC15, AC16 and AC32 can never
pass, and the unit carrying them is the one whose S14 closes the same corruption from the round
before. The cause is recorded in the spec commit's own trailer: fourteen criterion paths were
respelled as basenames before the first commit, because the spec-tokens paths join reds a backticked
path `git ls-files` cannot resolve. This unit is id 25's promotion and the item's left-shift, which
BUILD-METHOD M8 requires of every confirmed finding: the bug-class record
`criterion-asserts-what-its-own-command-cannot-show` gains the respelled input as a fifth form, with
the fix that makes a respelling unnecessary, and is anchored so `gotchas.py --for-diff` hands it to
every spec commit. It repairs `TOOL-dGroundRules-34`, which sits at order 12, so it builds at order 13.

## 2. Scope (IN)

- **S1** — The symptom. The record's front-matter `description` and its Symptom list gain a fifth
  form: a criterion's literal argument, a fixture path, a Python literal or a sourced file, was
  shortened so a join would pass, and the shortened literal no longer probes what its scope item
  names. Observed by AC2.
- **S2** — Where it bit. A paragraph names this audit's H3, `TOOL-dGroundRules-34`'s criteria after
  the respelling the commit `b9f7b5c4e` records, finding 37 of the round before, and the open ask
  `TOOL-aKeyedAnnotation-9` on the join itself. Observed by AC2.
- **S3** — The fix. "The fix" gains: a literal argument the join cannot resolve is spelled whole in a
  fenced block of the acceptance section, outside every criterion bullet, and the criterion names
  it; a literal is never shortened to satisfy a join; and the house rule of citing a kit file by
  basename covers prose only, never a command's argument. Observed by AC2.
- **S4** — The anchors. The new paragraphs backtick `memory/builds/` and `tools/check-spec-tokens.py`,
  so a commit touching a spec selects the record. Observed by AC1.
- **S5** — The gate paragraph. "Its gate" gains the measured reason no lint ships for this form: a
  missing-prefix predicate over the live specs, a scope-item path ending in `/` plus a criterion token,
  gave 136 hits across 30 specs on 2026-10-23, nearly all the house basename style, so it cannot
  tell a respelled literal from a kit file named by basename. Observed by AC3.
- **S6** — The index. `memory/gotchas/INDEX.md` is regenerated with
  `python tools/memory-tree/gotchas.py --write`. Observed by AC3.

## 3. Non-goals (OUT)

- A change to the paths join of `tools/check-spec-tokens.py`. That is the open ask
  `TOOL-aKeyedAnnotation-9` of another build, and the predicate measured in S5 shows no clean rule
  for a lint here.
- Rewriting `TOOL-dGroundRules-34`'s criteria. `TOOL-dGroundRules-39`, `TOOL-dGroundRules-40`,
  `TOOL-dGroundRules-41` and `TOOL-dGroundRules-43` observe them whole; nothing is folded.
- A new class record. The respelled input is a fifth way the existing class's criterion cannot pass.

### Edges

- **hands-off** `TOOL-dGroundRules-47` — the record's fix section, which that unit extends with the re-run of a read-only literal from the root (id 1 of the round-1 spec audit of units 35 to 43)

## 4. Design

`tools/memory-tree/gotchas.py:16-20` derives a record's anchors from the backticked path-like tokens
in its body, and `selectable` (`:340-356`) admits a path that holds the anchor as a substring, so a
backticked `memory/builds/` selects every spec under a build. Before this unit,
`python tools/memory-tree/gotchas.py --for-diff b9f7b5c4e~1..b9f7b5c4e`, the commit that carried the
respelling, selected 17 classes by anchor and 6 universal, and none was this record (measured
2026-10-23, PINNED).

The S5 figure came from a scratch script that, for every OPEN, SPECCED, INPROGRESS or BLOCKED spec,
joined each scope item's backticked path tokens to the backticked words of the criteria the item
names, and counted a word that a path ends in after a `/` while the path itself is absent from the
criterion.

### Files touched (estimate)

- `memory/gotchas/criterion-asserts-what-its-own-command-cannot-show.md`
- `memory/gotchas/INDEX.md`

## 5. Acceptance criteria

- **AC1** — When `python tools/memory-tree/gotchas.py --for-diff b9f7b5c4e~1..b9f7b5c4e` runs, its
  output names `criterion-asserts-what-its-own-command-cannot-show`.
  Red when: the spec commit that carried the respelling selects no record of the class.
- **AC2** — When `grep -c "TOOL-aKeyedAnnotation-9" memory/gotchas/criterion-asserts-what-its-own-command-cannot-show.md`
  runs, it prints `1` or more, and the record's fix section carries the words `fenced block`.
  Red when: the record names the form without the join that causes it or the fix that avoids it.
- **AC3** — When `python tools/memory-tree/gotchas.py --check` runs, it exits 0, and
  `grep -n "criterion-asserts" memory/gotchas/INDEX.md` prints a row whose description names the
  respelled input.
  Red when: the index still carries the four-form description only.

## 6. Gates

`gotchas selftest` · `memory hygiene` · `recall floor` · `recall floor arms`

## 7. Open questions

none

## 8. Revision log

- rev-1 · 2026-10-23 · initial draft, promoting finding id 25 (HIGH, item H3) of the round-1 spec
  audit of units 33 and 34 as the item's left-shift, with the record, `gotchas.py`'s anchor rule and
  a prefix-drop predicate over the live specs measured on 2026-10-23.
- rev-2 · 2026-10-23 · §3 · the hands-off edge to `TOOL-dGroundRules-47`, the reciprocal ends the disposal of
  the round-1 spec audit of units 35 to 43 wrote; no scope or criterion moved.

## 9. Reuse audit

The seam extended is the record `memory/gotchas/criterion-asserts-what-its-own-command-cannot-show.md`,
whose class is a criterion that cannot pass and whose "Its gate" already names
`tools/check-spec-tokens.py` as where a partial join would sit.
`python tools/codebase-map/reuse_lookup.py "hold a help page line equal to the line a script prints"`
ranks code seams and none of record shape; the record was found by listing `memory/gotchas/`, so no
new record is written. The recall probe returned `TOOL-aKeyedAnnotation-9`, the open ask on the
paths join, and `TOOL-cMendedVintage-4`, a spec that met the same join with fixture paths; both
agree with widening the record.

Recall terms used: `python tools/memory-recall/query.py "how is a criterion's path respelled to pass
the spec-tokens paths join" --terms "acceptance criterion path stripped prefix paths join basename
respelled spec-tokens literal fixture"`
