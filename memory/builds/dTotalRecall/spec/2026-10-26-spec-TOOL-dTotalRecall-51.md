# TOOL-dTotalRecall-51 — a non-markdown record's cause line wears its Serves line's comment prefix, the header reader reads it, and a bare one is refused

**Status:** DEFERRED · rev-2 · 2026-10-26 · node d · Tier-2 · base 462d20f3 · streams tooling · order 18 · advances TOOL-dTotalRecall-27

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-26-build-TOOL-dTotalRecall-1-agent-ledger.md](../build/2026-10-26-build-TOOL-dTotalRecall-1-agent-ledger.md) | journal | TOOL-dTotalRecall-1 TOOL-dTotalRecall-2 TOOL-dTotalRecall-3 TOOL-dTotalRecall-4 TOOL-dTotalRecall-5 TOOL-dTotalRecall-6 TOOL-dTotalRecall-7 TOOL-dTotalRecall-8 TOOL-dTotalRecall-9 TOOL-dTotalRecall-10 TOOL-dTotalRecall-11 TOOL-dTotalRecall-12 TOOL-dTotalRecall-13 TOOL-dTotalRecall-14 TOOL-dTotalRecall-15 TOOL-dTotalRecall-16 TOOL-dTotalRecall-17 TOOL-dTotalRecall-18 TOOL-dTotalRecall-19 TOOL-dTotalRecall-20 TOOL-dTotalRecall-21 TOOL-dTotalRecall-22 TOOL-dTotalRecall-23 TOOL-dTotalRecall-24 TOOL-dTotalRecall-25 TOOL-dTotalRecall-26 TOOL-dTotalRecall-36 TOOL-dTotalRecall-37 TOOL-dTotalRecall-38 TOOL-dTotalRecall-39 TOOL-dTotalRecall-40 TOOL-dTotalRecall-41 TOOL-dTotalRecall-42 TOOL-dTotalRecall-43 TOOL-dTotalRecall-44 TOOL-dTotalRecall-45 TOOL-dTotalRecall-46 TOOL-dTotalRecall-47 TOOL-dTotalRecall-48 TOOL-dTotalRecall-49 TOOL-dTotalRecall-50 TOOL-dTotalRecall-52 TOOL-dTotalRecall-53 TOOL-dTotalRecall-54 TOOL-dTotalRecall-55 TOOL-dTotalRecall-56 TOOL-dTotalRecall-57 TOOL-dTotalRecall-58 TOOL-dTotalRecall-59 TOOL-dTotalRecall-60 TOOL-dTotalRecall-61 TOOL-dTotalRecall-62 TOOL-dTotalRecall-63 TOOL-dTotalRecall-64 TOOL-dTotalRecall-65 TOOL-dTotalRecall-66 TOOL-dTotalRecall-67 TOOL-dTotalRecall-68 TOOL-dTotalRecall-69 TOOL-dTotalRecall-70 TOOL-dTotalRecall-71 TOOL-dTotalRecall-72 TOOL-dTotalRecall-73 TOOL-dTotalRecall-74 TOOL-dTotalRecall-75 TOOL-dTotalRecall-76 TOOL-dTotalRecall-77 TOOL-dTotalRecall-78 TOOL-dTotalRecall-79 TOOL-dTotalRecall-80 TOOL-dTotalRecall-81 TOOL-dTotalRecall-82 TOOL-dTotalRecall-83 TOOL-dTotalRecall-84 TOOL-dTotalRecall-85 TOOL-dTotalRecall-86 TOOL-dTotalRecall-87 TOOL-dTotalRecall-88 TOOL-dTotalRecall-89 TOOL-dTotalRecall-90 TOOL-dTotalRecall-91 TOOL-dTotalRecall-92 TOOL-dTotalRecall-93 TOOL-dTotalRecall-94 TOOL-dTotalRecall-95 TOOL-dTotalRecall-96 TOOL-dTotalRecall-97 TOOL-dTotalRecall-98 TOOL-dTotalRecall-99 TOOL-dTotalRecall-100 |
| [2026-10-26-review-TOOL-dTotalRecall-44-spec-audit-round1.md](../reviews/2026-10-26-review-TOOL-dTotalRecall-44-spec-audit-round1.md) | spec-audit | TOOL-dTotalRecall-44 TOOL-dTotalRecall-45 TOOL-dTotalRecall-46 TOOL-dTotalRecall-47 TOOL-dTotalRecall-48 TOOL-dTotalRecall-49 TOOL-dTotalRecall-50 TOOL-dTotalRecall-52 TOOL-dTotalRecall-53 |

<!-- /gen:spec-records -->

## 1. Goal

The round-1 spec audit of units 36 to 43
(`memory/builds/dTotalRecall/reviews/2026-10-26-review-TOOL-dTotalRecall-37-spec-audit-round1.md`)
confirmed finding **id 40 at HIGH**, its item **H7**, alone in that item. The record folders hold 138
non-markdown records (51 `.py`, 36 `.sh`, 20 `.tsv`, 13 `.js` and others), whose Serves line is a
comment. `tree_lib.record_paths` (`tools/memory-tree/tree_lib.py:420`) admits any extension, and
`BIND_RE` (`:406-410`) reads a Serves line behind `#`, `//` or `;`. `TOOL-dTotalRecall-19` S1 reads
only a column-0 `**Caused-by:**`, `TOOL-dTotalRecall-36` S5 states no form for a comment-headed record,
and its S6 inserts a bare markdown line after the Serves line whatever the extension. A script record
written after the seed then has no valid cause form, and the backfill would break one. This unit gives
the cause line the Serves line's own prefix, teaches the header reader to read it, refuses a bare one,
and repairs any record unit 36's backfill broke. It repairs `TOOL-dTotalRecall-36`.

## 2. Scope (IN)

- **S1** — The reader. `read_header_edges` in `tools/memory-tree/tree_lib.py` reads an untyped record's
  `**Made-by:**` and `**Caused-by:**` lines behind the same optional prefix `BIND_RE` admits, within the
  first `BIND_HEAD_LINES` lines. Observed by AC1.
- **S2** — The refusal. For a record whose Serves line carries a comment prefix, a cause or made-by
  line whose prefix differs from it is a refusal naming both lines, as `TOOL-dTotalRecall-19` S1
  refuses a second line of one key; a `.md` record keeps the bare column-0 form. Observed by AC2.
- **S3** — The repair. Every tracked non-markdown record the legacy population lacks gains, or has
  rewritten, its cause line as `<the Serves line's prefix>**Caused-by:** <first Serves id>`; the pass
  commits each with the parse check of its language. These are the records `TOOL-dTotalRecall-36` S6
  wrote into and those written since without a cause, which `TOOL-dTotalRecall-47`'s verb leaves to
  this unit. Observed by AC3.
- **S4** — The rule a hand-writer reads. The "Record bindings" section of
  `tools/memory-tree/HYGIENE.template.md` gains one sentence: a non-markdown record writes its cause
  line behind the comment prefix its Serves line uses. The render reaches `memory/HYGIENE.md` through
  `adopt-memory-tree.sh --render`. NOT OBSERVED by a criterion: a prose rule, held equal to its render
  by the `kit/dogfood doc parity` leg at the close.

## 3. Non-goals (OUT)

- The typed factory's `- **Key:**` form: unchanged, its records are markdown.
- The causes check's rules: `TOOL-dTotalRecall-19`'s; this unit changes what its reader admits.
- The markdown backfill: `TOOL-dTotalRecall-47`'s verb.
- A `.tsv` record's comment convention beyond the `#` prefix `BIND_RE` already reads.

### Edges

- **consumes-from** `TOOL-dTotalRecall-19` — `read_header_edges` in `tree_lib.py`, whose untyped form
  this unit widens to the prefixed line and whose refusal it extends
- **consumes-from** `TOOL-dTotalRecall-36` — S5's Record bindings sentence and S6's backfill, whose
  non-markdown records this unit gives their prefixed form
- **hands-off** `TOOL-dTotalRecall-53` — the comment-prefixed cause form, which that unit's worksheet writer emits (id 41)
- **hands-off** `TOOL-dTotalRecall-60` — the comment-prefixed cause form, which that unit's backfill verb writes, and §1's citations (the round-1 audit of units 44 to 53, ids 23 and 26)

## 4. Design

### The form

```text
.md   **Serves:** journal TOOL-x-1        .sh / .py   # **Serves:** journal TOOL-x-1
      **Caused-by:** TOOL-x-1                         # **Caused-by:** TOOL-x-1
.js   // **Serves:** research TOOL-x-1
      // **Caused-by:** TOOL-x-1
```

The reader's pattern is `BIND_RE`'s with the key set `Made-by|Caused-by`, one regex built beside it so
the two prefixes cannot drift. The prefix compare in S2 is on the captured prefix text, whitespace
squeezed.

### Inventory

Minted: `HEAD_EDGE_RE` in `tools/memory-tree/tree_lib.py`, beside `BIND_RE`. Naming cell: none, the
lexicon declaring no constant cell.

### Files touched (estimate)

- `tools/memory-tree/tree_lib.py`
- `tools/memory-tree/record_causes.py` (the two fixture plants only)
- `tools/memory-tree/HYGIENE.template.md`
- `memory/HYGIENE.md` (the render)
- `memory/builds/dTotalRecall/build/` (S3's non-markdown records only)
- `memory/builds/dTotalRecall/prompts/` (S3's non-markdown records only)

`TOOL-dTotalRecall-47` writes the markdown records of the same folders at order 18, disjoint by file.
It, `TOOL-dTotalRecall-49` and `TOOL-dTotalRecall-50` also write `record_causes.py`, so BUILD-METHOD M6
sequences this pass with theirs.

### Alternatives rejected

- **Exempt non-markdown records from the causes check.** It lets every probe script and worksheet
  written after the seed sit outside the rule this build lands.
- **Accept a bare cause line in any record.** A bare `**Caused-by:**` line in a `.sh` or `.py` record is
  a syntax error, so the reader would admit a line that breaks the record it describes.

## 5. Production-readiness checklist

- security — no new surface; S3 writes one comment line into records already tracked.
- perf / scale — one regex per head line, as `BIND_RE` costs.
- error / empty / loading states — a prefix mismatch is a refusal naming both lines.
- observability — the refusal names the record and its two lines.
- risks — an extension with no line-comment syntax (`.json`, `.svg`, `.html` and others, 18 records at
  base, PINNED 2026-10-26 by `git ls-files` over the record folders) has no prefixed form; S3 names any
  such record it cannot repair and writes nothing into it.
- testing — AC1 to AC3 by the pass; the arm of §7 at the close.
- migration — S3's repair of this run's non-markdown records.
- user docs — none under `help/`; `memory/HYGIENE.md` carries S4.

## 6. Acceptance criteria

- **AC1** — When `read_header_edges` from `tree_lib.py` reads a fixture `.py` record headed
  `# **Serves:** journal TOOL-x-1` then `# **Caused-by:** TOOL-x-1`, it returns `caused-by` `TOOL-x-1`,
  and `python record_causes.py --check` over the fixture passes it.
  Red when: a prefixed cause line reads as absent and the record reds as causeless.
- **AC2** — When the same reader reads a fixture `.sh` record whose Serves line is `# `-prefixed and
  whose cause line is bare, it refuses naming both lines.
  Red when: the bare line in a script record is read as its cause.
- **AC3** — When `bash -n` runs over each `.sh` record and `python -m py_compile` over each `.py`
  record S3 wrote, every one passes, and `python record_causes.py --check` at the pass tip names no
  non-markdown record.
  Red when: a repaired record no longer parses, or one is left causeless.

## 7. Gates

`memory hygiene` · `kit/dogfood doc parity` · `recall floor` · `recall floor arms` · `lexicon naming predicates`

New arm: tools/memory-tree/record_causes.py · covers AC1 AC2 · the plants `script-cause-prefixed` and `script-cause-bare`, staged by reading the column-0 form only · none

## 8. Open questions

- **F1 — Which binding line does a unit the spec audit promoted carry?** The carries join reds a chain
  spec carrying nothing and derived from nothing. Options: (a) `**Derived:**` naming
  `PLAY-dClosedLoop-2`, the ruling that a chain spec run carries the units it adds; (b) a `part k/n`
  carry of `TOOL-dTotalRecall-19`'s clause, which would split a clause that unit carries whole. (b)
  reds the parts join; veto 1 discards it. RESOLVED (agent, 2026-10-26, delegated): (a), rung 3, the
  precedent `TOOL-dDeclaredLoop-36` §8 F1 set. widens: none · relaxes: none
- **F2 — May this unit add a sentence to `HYGIENE.template.md`, a governance carrier?** Options: (a) yes,
  under the grant `TOOL-dTotalRecall-36` §8 F2 used for the same section, the comment form being part
  of cl-dClosedLoop-0230's "each record's header (Serves, Made-by, Caused-by)"; (b) no, leaving a
  script record's writer to learn the form from the refusal. (b) leaves every hand-written script record
  of the next build refused with no instruction that prevents it. RESOLVED (agent, 2026-10-26,
  delegated): (a), rung 5, the grant the README's `may:` line names. grants: PLAY-dClosedLoop-3
  HYGIENE.template.md's Record bindings section states the comment-prefixed cause line · widens: none
  · relaxes: none

## 9. Revision log

- rev-1 · 2026-10-26 · initial draft, promoted from the round-1 spec audit of units 36 to 43, id 40
  (HIGH, item H7).
- rev-2 · 2026-10-26 · §3 · the Edges block gains the mirror of TOOL-dTotalRecall-60, each the other end of an edge a unit the round-1 spec audit of units 44 to 53 promoted wrote; nothing else moved.

## 10. Reuse audit

The seam extended is `BIND_RE` (`tools/memory-tree/tree_lib.py:408-410`), whose optional prefix the
cause reader copies by construction, and `read_header_edges` (`TOOL-dTotalRecall-19` S1), the one header
reader. `python tools/codebase-map/reuse_lookup.py "insert a cause line into a record head after its
binding line"` ranked `parse_conf_line` and `check_line`, readers of other lines, and no comment-aware
head reader beside `BIND_RE`.

Recall terms used: `python tools/memory-recall/query.py "how is a record written by a pinned instrument given its cause and kept green by the causes check" --terms "Caused-by causes legacy-records backfill instrument pinned repin departures record_causes census kept"`
