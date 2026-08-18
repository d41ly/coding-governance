# TOOL-aFusedCharter-2 — the micro-format definitions become machine-gradeable against their own grammar

**Status:** OPEN · rev-1 · 2026-08-18 · node a · Tier-2 · base 497d25d0 · streams tooling

## 1. Goal

Parse the micro-format block out of the converged ruleset and assert that every definition line
satisfies the grammar stated above it, so the block stays a compilable definition set rather than
drifting back into shapes nobody can parse.

## 2. Scope (IN)

**S1 — A parser over the block, not over the file.** The gate locates the definition list by the
same anchor a reader uses — the grammar paragraph's heading and the list that follows it — and grades
only those lines. A whole-file scan for shape-like text would match every emission quoted in a
record and every example in a runbook, which is the absence-assertion-over-whole-file-text class
this repo has on record.

**S2 — One predicate per grammar clause, each able to red separately.** The clauses are
`PLAY-aFusedCharter-2` S1's, and the gate implements them as distinct failures because a single
"malformed shape" verdict tells an author nothing about which rule they broke:

- the head is one keyword from the closed set, with its declared case;
- the joiner appears exactly once;
- tail fields are separated only by the declared separator;
- no parentheses outside markdown-link syntax;
- no colon acting as a joiner or a label;
- only the five pinned glyphs appear as structure;
- placeholders are lowercase angle-bracket names, alternation written with the declared glyph.

**S3 — Derive the closed keyword set from the block, never from a list in the gate.** The set is
whatever the definition lines lead with. A hand-typed copy inside the gate would be a mirror of the
subject it grades, which this repo's own gate-discipline rules forbid by name. The anti-vacuity arm
is a frozen SENTINEL: the derived set must contain a named shape and must be non-empty, so a broken
extraction reds as broken rather than certifying an empty set.

**S4 — Byte-level reading.** The pinned glyph set is non-ASCII, so the gate reads bytes with an
explicit encoding and never a platform default. This repo ships `tools/gate-lint/` because a
platform default decoded an em dash into a parse error, and this gate's whole subject is glyphs.

**S5 — A sibling self-test that observes each failure.** One arm per S2 predicate plus the two S3
anti-vacuity arms, each feeding a fixture block that violates exactly one clause and asserting the
gate names THAT clause. A gate is not landed until its failing case has been observed, and a gate
with seven predicates needs seven observations, not one.

**S6 — Wire it as a leg, and print an assertion count.** One row in `tools/gate-legs.json` with a
guard naming the gate and its test. The self-test prints its executed assertion count in the agreed
shape, because `tools/check-testsuite-counts.sh` derives its population from that manifest and a new
suite printing no count reds it.

## 3. Non-goals (OUT)

**No emission checking.** The gate grades DEFINITIONS. Whether a given final message carried the
required pair is not observable from the repository, and the owner resolved at kickoff that a
Stop-hook validator is a follow-up.

**No parity between carriers.** `AGENTS.md` receives the block through the render, and
`bash tools/playbook/adopt-playbook.sh --check` already asserts the region matches its source. A
second comparison here would be two answers to one question.

**No semantic checking.** The gate holds SYNTAX. Whether a shape's fields are the right fields is a
design question, and the gate's own header says so — a structural check reads as a semantic one to
everybody who did not write it.

**No new configuration key.** The grammar is stated in the document and derived from it.

## 4. Design

### Data model

The gate's input is the block. Its output is zero or more offender lines, each naming the definition
line, the clause it violated, and the offending substring. Its exit codes follow this repo's gate
convention: 0 clean, 1 an offender, 2 could-not-run — and could-not-run is a NAMED failure rather
than a silent zero, because a gate that cannot find its block would otherwise report a clean set.

The `could not find the block` case is the one most likely to go wrong in practice, since it fires
when someone renames a heading, and it must be loud. It is one of S5's arms.

### Migration

None. The gate lands after `PLAY-aFusedCharter-2` has already brought every shape into compliance,
so its first real run is green — which is exactly why S5's fixtures are the evidence it works, not
that run.

### Alternatives rejected

**Put it in the hygiene gate as a new check.** A new check inside `check-memory-hygiene.sh` is
cheaper than a new leg, and this repo's own charter says so. Rejected anyway: the hygiene gate's
subject is `memory/`, and the block lives in a shipped product file at the repo root. A check
grading a root product file from inside the memory-tree kit would ship in that kit to every adopter
that has no playbook. Upstream inCMS made the opposite choice and it was right there, because its
hygiene script is invoked by a CI job the gate runner is not — that reasoning does not transfer.

**Grade the block with a regex per shape.** Rejected: that is a hand-kept second copy of the
definitions, one file over from the definitions.

### Files touched (estimate)

New: `tools/check-microformats.sh` and `tools/check-microformats.test.sh`.
Edited: `tools/gate-legs.json`, the govkit descriptor that must claim the two new files, and a map
dossier claim.

## 5. Production-readiness checklist

- security — N/A; a read-only scanner.
- perf / scale — one file, one pass.
- a11y — N/A.
- i18n — S4 is the i18n concern and it is load-bearing.
- error / empty / loading states — the empty case is S3's anti-vacuity arm and the could-not-run
  case is in the Data model.
- observability — offender lines name the clause, not just the line.
- risks — a gate whose vocabulary mirrors its subject is the failure mode this gate is most likely
  to commit; S3 is the mitigation and the sentinel is what makes it checkable.
- testing + left-shift gates — S5, one arm per predicate.
- migration / rollback — a new leg; removing the row disables it.
- user docs — the gate's own header states what it does not check.

## 6. Acceptance criteria

- **AC1** — When `bash tools/check-microformats.sh` runs against the landed ruleset it exits 0 and
  prints the number of definition lines it graded, derived rather than declared.
- **AC2** — When a definition line is given a second joiner, `bash tools/check-microformats.sh`
  exits 1 and its message names the joiner clause and that line.
- **AC3** — When a definition line is given a parenthetical outside a markdown link,
  `bash tools/check-microformats.sh` exits 1 naming the parenthesis clause; when a line carries a
  markdown link, it does not.
- **AC4** — When a definition line uses a colon as a label, `bash tools/check-microformats.sh`
  exits 1; when a line carries a colon glued to a port value such as `:3200`, it does not.
- **AC5** — When the block's heading is renamed so the anchor misses,
  `bash tools/check-microformats.sh` exits 2 with a message naming the missing block — not 0.
- **AC6** — When the extraction is broken so the derived keyword set is empty,
  `bash tools/check-microformats.sh` reds naming the frozen sentinel rather than grading cleanly.
- **AC7** — When `bash tools/check-microformats.test.sh` runs it exits 0 and prints an executed
  assertion count in the shape `tools/check-testsuite-counts.sh` accepts, with one arm per S2
  predicate and both S3 arms.
- **AC8** — When `bash tools/run-gates.test.sh` and `python tools/govkit/govkit.py selfcheck` run,
  both exit 0 with the new leg declared and its files claimed.

## 7. Gates

`run-gates canary` · `testsuite counts` · `govkit selfcheck` · `codebase-map coverage + freshness` ·
`install-prefix (shipped surface)` · `harness arms` · the new leg itself · the full bar. Adding a leg
trips a growing set of meta-gates, so the full bar is the instrument.

## 8. Open questions

none — the fork below is RESOLVED.

- **F1 — a new leg, or a check inside an existing gate?** RESOLVED (agent, 2026-08-18, delegated by
  the build's stated order): a new leg, on the grounds in `§4`'s Alternatives rejected. The cheaper
  option would ship a root-product check inside a kit that adopters install without the product.

## 9. Revision log

- rev-1 · 2026-08-18 · initial draft.

## 10. Reuse audit

`python tools/codebase-map/reuse_lookup.py "grade a document block against a stated grammar"`
returns no existing seam: every structural gate in this tree grades code, a conf or a filename, and
none parses prose against a grammar the prose itself states. The closest relatives are
`tools/memory-tree/row_grammar.py`, which parses record rows and carries its arms in a selftest
mode, and `tools/check-placeholders.sh`, which grades marker lines in the same product files — this
gate follows the second one's file placement and the first one's arms-with-the-engine discipline.
The anti-vacuity sentinel is lifted from `tools/check-playbook-parity.sh`, which froze a kit name for
exactly this reason.

Recall terms used: `micro-format grammar definition block parser gate vocabulary derived sentinel
anti-vacuity glyph encoding arms selftest`. The binding prior record is `TOOL-aSiftedPlaybook-3`,
whose anti-vacuity constraint is the design this gate copies, and `PLAY-cDerivedGlossary-1`, which
ported the rule that a gate's own hardcoded vocabulary drifts silently — the rule S3 exists to obey.
