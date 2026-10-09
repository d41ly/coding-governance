# TOOL-aQuotedBrief-5 — preflight and term 7 recognise a prompt record by one predicate

**Status:** SPECCED · rev-1 · 2026-10-09 · node a · Tier-2 · base 6473ae38 · streams tooling · order 4

<!-- gen:spec-records -->

*No record names this unit.*

<!-- /gen:spec-records -->

## 1. Goal

`check_prompt_brief` normalises headings with `sub(/^## +/)`, so a record headed `##  The prompt` is
graded and joined at preflight. Term 7 gates with `grep -qE '^## The prompt[[:space:]]*\r?$'`, which
needs exactly one space, so it skips that record and meets green with no item graded. A DoD term then
certifies what it did not check. This unit gives both one predicate, the exact spelling
`read_audit_ask_record` already uses, so all three readers of a prompt record answer the same. It
closes closing-review round 1 H2 (id 7).

## 2. Scope (IN)

- **S1** — `check_prompt_heading` in `tools/unattended/unattended.sh` returns 0 when its stdin holds a
  line that is `## The prompt`, with only trailing whitespace or a CR after it, and 1 otherwise.
  Observed by AC1 and AC2.
- **S2** — `check_prompt_brief` decides "is this a prompt record" with `check_prompt_heading` before
  its structural awk, instead of from the awk's normalised `seen` table. A `##  The prompt` record is
  then not a prompt record, so a build holding only such a record refuses at check 113. Observed by
  AC1.
- **S3** — `check_brief_items` uses the same function. Observed by AC2.
- **S4** — `read_audit_ask_record` is unchanged; its anchor already is that spelling. Observed by AC3.

## 3. Non-goals (OUT)

- Widening the spelling to admit `##  The prompt`. The audit reader would then admit more records as
  the owner's words, which widens the one surface a run must not author; narrowing preflight to the
  reader that already exists widens nothing.
- The `## The brief` and `###` sub-head normalisation, which preflight and `read_brief_items` already
  do the same way.

### Edges

- **hands-off** `TOOL-aQuotedBrief-6` — the heading predicate, beside which that unit fixes the listings.

## 4. Design

### Evidence

Read at `5e2187386` on 2026-10-09.

- `check_prompt_brief`'s awk sets `seen[h2]` after `sub(/^## +/, "", h2)` and treats a record as a
  prompt record when `seen["The prompt"]` is set.
- `check_brief_items` skips a record unless `grep -qE '^## The prompt[[:space:]]*\r?$'` matches.
- `read_audit_ask_record` opens its section on `/^## The prompt[[:space:]]*\r?$/`.

### Inventory

| Identifier | Kind | Cell |
|---|---|---|
| `check_prompt_heading` | function | `sh.function`; `python tools/lexicon/lexicon.py --suggest check_prompt_heading --as sh.function` answered OK |

### Files touched (estimate)

`tools/unattended/unattended.sh` · `tools/unattended/unattended.test.sh` · `memory/map/generated/symbols.json`

### Alternatives rejected

- **Teaching term 7 the preflight awk's normalisation.** It agrees two readers by widening them, and
  leaves the third, the audit reader, answering differently.

## 5. Production-readiness checklist

- security — narrows what preflight treats as the owner's prompt to what the audit reader already
  treats as it.
- perf / scale — one `grep` per record.
- error / empty / loading states — a build whose only record is mis-headed refuses at check 113, which
  names the empty population.
- observability — unchanged messages.
- risks — a record written with a doubled space now refuses at preflight instead of passing; no
  tracked record carries one.
- testing — arms in `tools/unattended/unattended.test.sh`, run once at VERIFYING.
- migration — none.
- user docs — none: the verbs file already spells the heading exactly.

## 6. Acceptance criteria

- **AC1** — When a prompt-mode build's only record is headed `##  The prompt`, `--preflight` refuses at
  check 113.
  Red when: preflight grades a record term 7 would skip.
- **AC2** — When `--close` runs over a fixture whose record is headed `##  The prompt` and carries an
  unbuilt `planned` item, term 7 and preflight agree, by the slice of both arms.
  Red when: one reader grades the record and the other skips it.
- **AC3** — When `git diff 6473ae38 -- tools/unattended/unattended.sh` is read for
  `read_audit_ask_record`, the function is unchanged.
  Red when: the audit reader's anchor moved.

## 7. Gates

`unattended kit gate` · `harness arms (fail branches armed or pinned)` · `lexicon naming predicates` · `codebase-map coverage + freshness` · `spec tokens (a spec's own names resolve)` · `recall floor` · `recall floor arms`

New arm: tools/unattended/unattended.test.sh · covers AC1 AC2 · the pre-unit driver, which grades a doubled-space record at preflight · none

## 8. Open questions

none

## 9. Revision log

- rev-1 · 2026-10-09 · initial draft, promoted from closing review round 1 H2.

## 10. Reuse audit

`reuse_lookup.py "record a self-contained brief of an unattended prompt-mode run, quoting session
context, and refuse unrelated commits on the run branch"` found no heading predicate. The extended
seam is the anchor `read_audit_ask_record` in `tools/unattended/unattended.sh` already spells, which
this unit names once and calls from the two new readers.

Recall terms used: `prompt record verbatim authorized-by prompt published anchor branch tip
self-authorization orientation AskUserQuestion owner turn build folder roster` — the build's query.
