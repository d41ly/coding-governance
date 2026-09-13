# TOOL-cSpliceWarden-6 — hygiene check 24 grades the declared rotation mode

**Status:** SPECCED · rev-1 · 2026-09-13 · node c · Tier-2 · base 2aff637e · streams tooling · order 6

<!-- gen:spec-records -->

*No record names this unit.*

<!-- /gen:spec-records -->

## 1. Goal

`ROTATION_MODE` has been validated against its closed set since `TOOL-cSpliceWarden-1` and read by no
check since. Grade it: under `cut`, assert the two things `cut` means, so the archive that build
repaired cannot re-form.

## 2. Scope (IN)

- **S1** — under `cut`, a rotated archive of a STATUS-BEARING shard holds terminal rows only.
  Observed by **AC1**.
- **S2** — under `cut`, no id sits in both an archive and the live index it was cut from. Observed by
  **AC2**.
- **S3** — the assertion DELEGATES to `row_grammar.py` rather than spelling a second row predicate,
  and reuses the enumeration and resolution check 10 already owns. Observed by **AC3**.
- **S4** — `snapshot` and an UNDECLARED mode ANNOUNCE that they are ungraded, with the count they
  leave ungraded. Observed by **AC4**.
- **S5** — `cut` over a tree with no rotated archive says it graded nothing. Observed by **AC5**.

## 3. Non-goals (OUT)

- Grading `snapshot`. Its assertion inverts to "an archived row is never edited after the rotation",
  whose baseline is the commit that ADDED the archive, and that baseline is not resolvable here. §4
  carries the measurement. The mode announces instead.
- Grading any archive's CONTENT. Check 24 grades the partition, never whether the rows are the right
  rows or their status true.
- A DECISIONS archive's terminal half. A decision row carries no lifecycle token, so "terminal only"
  is vacuously true there and asserting it is a category error. The exclusivity half still applies.
- Cross-file uniqueness in general. Check 20 stays per-file; this unit asserts one specific pair
  relationship, not corpus-wide uniqueness, which the row-grammar dossier records as refused on
  measurement.

### Edges

- **consumes-from** `TOOL-cSpliceWarden-1` — that unit declared the key this one reads.
- **consumes-from** `TOOL-cSpliceWarden-2` — the enumeration contract and the basename resolution.
- **hands-off** external — nothing. The three rows this build filed are closed by it.

## 4. Design

### Data model

Check 24, delegated from `check-memory-hygiene.sh` to `row_grammar.py --check-rotation`, in the shape
checks 13-20 already use. Three modes, three behaviours:

| `ROTATION_MODE` | behaviour |
|---|---|
| `cut` | graded: terminal-only over status-bearing shards, plus exclusivity over all |
| `snapshot` | ANNOUNCED as ungraded, with the archive count it leaves ungraded |
| blank | ANNOUNCED as undeclared, with the same count |

### Why it delegates

The first cut spelled its own row predicate in shell: `^- <ID> · <STATUS> · `. That is a third
spelling of "what is a row" in a kit that already owns one, and it was broken six ways in a scratch
copy — five of six evasions passed SILENTLY. Two spaces after the middot, a `*` bullet, a row with no
status token, a row whose status is the final field, and a BOLD-WRAPPED id. The last is the one that
matters: `memory/DECISIONS.md` carries fifteen bold-wrapped ids, so the EXCLUSIVITY arm — the arm
that would have caught the 2026-08-17 archive — was blind to fifteen live rows on the day it was
written. Delegating to `row_grammar.scan`'s grammar closes all six and comes with `unfenced_lines`,
so the check no longer grades inside fenced blocks either.

### Why `snapshot` is announced and not graded

Measured 2026-09-13 on this repo, not assumed:

```
git log --diff-filter=A               -- memory/archive/DECISIONS.2026-08-10.md   -> EMPTY
git log --full-history --diff-filter=A   (same file)                              -> EMPTY
git log -m --diff-filter=A               (same file)                              -> b8e33b18
git log --diff-filter=A               -- memory/archive/TOOL.2026-08-14.md        -> 581433ff
git log --full-history --diff-filter=A   (same file)                              -> d84d2d58
```

Two of four archives were added INSIDE merge commits, which is how a rotation lands here, and only
`-m` sees them. The three spellings disagree on a third file. And `git log ""..HEAD -- <path>` exits
0 printing nothing, so an unresolved baseline reports a clean archive. An arm that cannot find its
own starting point and says so by staying silent is the reassuring zero this repo refuses; shipping
it would be worse than the gap. The gap is named on every run instead.

### Files touched (estimate)

`tools/memory-tree/row_grammar.py` · `tools/memory-tree/check-memory-hygiene.sh` ·
`tools/memory-tree/HYGIENE.template.md` and its render · the kit version markers.

### Alternatives rejected

- **Keep the shell implementation and harden its regex.** Rejected: it is the third spelling either
  way, and hardening it against six known evasions leaves the seventh.
- **Grade `snapshot` on the git-history property.** Rejected on the measurement above.

## 5. Production-readiness checklist

- security — N/A — a read-only scan of tracked text.
- perf / scale — one extra pass over the row documents, measured at 0.26 s including the `git
  ls-files` fork.
- error / empty / loading states — all three are named: an unresolvable stem reports that the
  exclusivity half was not graded, a row with no readable status reports that it could not be graded
  either way, and an empty archive population says it graded nothing.
- observability — every finding names the archive, the id, the status and the line.
- risks — §4's delegation is the mitigation for the one real risk, which is a second row grammar.
- testing — AC1-AC5, eight arms in `row_grammar.py --selftest`.
- migration — none. An adopter declaring nothing sees an announcement, not a red.
- user docs — the numbered catalogue entry in `HYGIENE.md`, item 24.

## 6. Acceptance criteria

- **AC1** — When a fixture archive carries `- ARCH-tStay-1 · OPEN · …`, `row_grammar.py --check-rotation`
  names it with its id, status and line.
  Red when: the row is counted terminal, or the arm reports clean.
- **AC2** — When a fixture's archive and its live shard both carry `ARCH-tBoth-1`,
  `--check-rotation` reports that the pair does not partition the family and names the id.
  Red when: the overlap passes, which is the 2026-08-17 defect itself.
- **AC3** — When a fixture archive carries `- **ARCH-tBold-1** · SPECCED · …`, it is still graded.
  Red when: the bold wrapper hides the row — the evasion the shell version passed silently, with
  fifteen live instances in `memory/DECISIONS.md`.
- **AC4** — When `ROTATION_MODE` is `snapshot` or blank, `--check-rotation` exits 0 and its output
  says the mode is not graded and how many archives that leaves.
  Red when: either mode passes silently, which is a skip wearing a pass's clothes.
- **AC5** — When `cut` is declared over a tree with no rotated archive, the output says it graded
  NOTHING.
  Red when: it reports clean, which is a green over a population of zero.

## 7. Gates

`memory hygiene` · `row-grammar selftest` · `memory-hygiene self-test` · `harness arms (fail branches armed or pinned)` · `kit version markers` · `verdict epoch (kit version dates the engine)` · `kit/dogfood doc parity`

New arm: `tools/memory-tree/row_grammar.py --selftest` · eight arms covering every branch of check 24, including both ungraded modes and the empty population · no assertion floor moves, because the delegation adds no `fail` branch to any `*.sh`.

## 8. Open questions

none.

## 9. Revision log

- rev-1 · 2026-09-13 · the first draft. AUTHORING ORDER, recorded rather than implied by the commit
  graph: a shell implementation of this check was written first, a design lens broke it six ways,
  and this spec was authored as the delegation replaced it. The commits were then ORDERED
  spec-first before landing, at the owner's direction, so `pass-order history` passes. The graph
  says spec-then-code; this line says what actually happened, and the two are meant to be read
  together.

## 10. Reuse audit

`python tools/codebase-map/reuse_lookup.py "rotation mode archive terminal exclusivity"` returns the
seam this unit extends: `row_docs` and `id_pattern` in `row_grammar.py`, the module that already owns
which documents carry rows and what a row looks like. No new enumeration and no new grammar were
written — the one new thing is the assertion, and it sits beside the grammar it reads rather than
beside the shell that used to spell a rival copy of it. The status vocabulary is imported from
`gen_build_index.STATUS_TOKENS` rather than retyped, which is what stopped the first cut reading the
prose words `ONE` and `CORRECTS` as status tokens in a decision archive.
Recall terms used: `rotation archive terminal exclusivity partition shard cut snapshot declared mode check delegate grammar`
