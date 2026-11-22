# TOOL-aFlattenedSeed-2 — sh_hygiene's home-graded note rides stderr

**Status:** CLOSED · rev-1 · 2026-11-23 · node a · Tier-1 · base 87c8a917 · streams tooling

<!-- gen:spec-records -->

*No record names this unit.*

<!-- /gen:spec-records -->

## 1. Goal

On an adopter whose receipt lists engine files, `sh_hygiene.py` prints its home-graded note to stdout.
Under `--measure`, stdout is a ledger seed's rows, so the seeds of `shell-role`, `quoting-sites` and
`path-literal-sites` read the note as a malformed row and leave the population unarmed. This unit
moves the note to stderr. TOOL-aFlattenedSeed-1's flat-install fix made these seeds runnable on
inCMS, which is how this defect surfaced.

## 2. Scope (IN)

- **S1** — `tools/gate-lint/sh_hygiene.py#remove_home_graded` prints its note to stderr, and the
  note's truncated last clause now ends "an edited one is graded". Observed by AC1.

## 3. Non-goals (OUT)

- The other kits' home-graded notes, such as the lexicon's: none of them feeds a seed's stdout today.

### Edges

- **consumes-from** `TOOL-aFlattenedSeed-1` — the flat-install seed resolution that exposed this

## 4. Design

### Mechanism

`print(..., file=sys.stderr)`. Every grading run already captures both streams, so its finding lines
are unchanged.

### Files touched (estimate)

- `tools/gate-lint/sh_hygiene.py`

## 5. Acceptance criteria

- **AC1** — When `--selftest` runs a `--shell-role --measure` scan over a tree whose receipt homes one
  file, stdout holds only the other file's row and stderr carries the note. Red when: the note is on
  stdout. Observed red against the base copy on 2026-11-23: the note was stdout's first line.

## 6. Gates

`shell-hygiene selftest` · `portability (shell lines only shrink)` · `memory hygiene` · `line length` · `spec tokens (a spec's own names resolve)`

New arm: tools/gate-lint/sh_hygiene.py · covers AC1 · `--selftest` splits a `--measure` run's streams over a home-graded tree; staged red against the base copy · none

## 7. Open questions

none

## 8. Revision log

- rev-1 · 2026-11-23 · initial draft.
