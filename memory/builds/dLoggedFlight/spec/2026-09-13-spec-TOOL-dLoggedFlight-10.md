# TOOL-dLoggedFlight-10 — the schema leg: a committed run record outside the closed schema reds the bar

**Status:** SPECCED · rev-2 · 2026-09-13 · node d · Tier-2 · base 9fac2b53 · streams tooling · order 10

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-09-13-build-TOOL-dLoggedFlight-1-design-research.md](../build/2026-09-13-build-TOOL-dLoggedFlight-1-design-research.md) | research | TOOL-dLoggedFlight-1 TOOL-dLoggedFlight-2 TOOL-dLoggedFlight-3 TOOL-dLoggedFlight-4 TOOL-dLoggedFlight-5 TOOL-dLoggedFlight-6 TOOL-dLoggedFlight-7 TOOL-dLoggedFlight-8 TOOL-dLoggedFlight-9 TOOL-dLoggedFlight-11 TOOL-dLoggedFlight-12 TOOL-dLoggedFlight-13 |
| [2026-09-13-review-TOOL-dLoggedFlight-1-spec-audit-round1.md](../reviews/2026-09-13-review-TOOL-dLoggedFlight-1-spec-audit-round1.md) | spec-audit | TOOL-dLoggedFlight-1 TOOL-dLoggedFlight-2 TOOL-dLoggedFlight-3 TOOL-dLoggedFlight-4 TOOL-dLoggedFlight-5 TOOL-dLoggedFlight-6 TOOL-dLoggedFlight-7 TOOL-dLoggedFlight-8 TOOL-dLoggedFlight-9 TOOL-dLoggedFlight-11 TOOL-dLoggedFlight-12 TOOL-dLoggedFlight-13 |

<!-- /gen:spec-records -->

## 1. Goal

The run record is public, and its safety rests on a closed schema. A renderer that honours the schema
proves nothing about a record edited afterwards by hand, by a merge, or by a later renderer with a bug.
Add a merge-bar leg that reads every committed run record's BYTES and refuses anything outside the
schema, independently of the renderer.

## 2. Scope (IN)

- **S1** `runlog.py check-records`, run as a new repo-subject leg `runlog record schema`. It reads every
  tracked `memory/builds/*/build/*-runlog-*.md` from the index, not the working tree, and validates
  each against `RECORD_SCHEMA` from `TOOL-dLoggedFlight-9`. Observed by AC1.
- **S2** The refusals, each naming the record, the line and the rule. Observed by AC2. A record is
  refused for:
  - a heading set or order other than S3's;
  - a table row whose first cell is not a timestamp, sha or ordinal;
  - a cell outside the allow-list;
  - an absolute path (a drive letter, a `/Users/` or `/home/` root, or a UNC prefix);
  - a UUID;
  - a `Data` block that is not valid JSON or carries a key outside the schema;
  - more than 24 KB;
  - a `Serves:` line naming an id outside the record's own build.
- **S3** Liveness. The leg prints the population it graded. An empty population is reported as
  `0 records (none committed yet)` and exits 0, because a repo with no run records yet is a legitimate
  state. The leg asserts the tracked glob it reads is the one the renderer writes, so a renamed
  pattern cannot empty the population in silence. Observed by AC3.
- **S4** Cost: the leg reads the whole population in a constant number of git calls, one `ls-files`
  and one `cat-file --batch`, and declares a 60 s ceiling. Observed by AC4.
- **S5** A render-then-grade arm. The clean fixture the leg is tested against is produced by
  `render_record` from a model fixture that populates every section with one value of each closed
  class. So a renderer and a leg that disagree fail the self-test. Observed by AC1.

## 3. Non-goals (OUT)

- Grading content truth. The leg proves a record carries only permitted SHAPES, never that its counts
  are right, which the leg's own header states as charter §7 requires.
- Records in other folders, and records not named `-runlog-`.

### Edges

- **consumes-from** `TOOL-dLoggedFlight-9` — the closed schema, the record naming and the renderer the
  clean fixture comes from.
- **hands-off** `TOOL-dLoggedFlight-11` — the leg that grades this run's own record before its landing.

## 4. Design

The leg is the second of two enforcement points. The renderer builds the record from the allow-list,
and this leg re-derives every value's class from the committed bytes, so a disagreement between the two
is itself a finding, and S5 makes that disagreement a red. It shares `RECORD_SCHEMA` as data, not the
renderer's code path. That is the repo's rule against a second implementation that merely confirms the
first.

### Inventory

| identifier | kind | cell |
|---|---|---|
| `check_records`, `check_record`, `scan_forbidden` | functions | `py.function`, verb-led |
| `cmd_check_records` | CLI subcommand | reserved `cmd` |
| `runlog record schema` | leg, `repo` / `declarations`, ceiling 60 | manifest |

### Files touched (estimate)

`tools/runlog/{record.py,runlog.py,selftest.py,kit.toml}`, `tools/gate-legs.json`,
`tools/govkit/subject-pins.tsv`, `memory/map/features/runlog.md` and the regenerated map.

### Alternatives rejected

- Folding the check into the hygiene gate: rejected, since the schema is this kit's, and a hygiene
  check naming it would be a cross-kit literal.
- A hand-written clean fixture: rejected, since it would pass the leg while the renderer drifted.

## 5. Production-readiness checklist

- security — this is the enforcement point for the public record's privacy promise.
- perf / scale — a constant number of git calls over any population (AC4). The wall time is printed
  report-only; the ceiling is the cost verdict.
- error / empty / loading states — an empty population is named and legal. An unreadable record is a
  refusal, not a skip.
- observability — the population line on every run.
- risks — a schema too strict to render a real run. Mitigated by S5, and because
  `TOOL-dLoggedFlight-11` renders this run's own record and grades it under this leg before landing.
- testing — one fixture per refusal staged RED, and the rendered clean fixture.
- migration — none; no record exists before this build.
- user docs — the leg's header, which states what it does not check.

## 6. Acceptance criteria

`<kit>` below is `tools/runlog`. Every criterion runs `python <kit>/selftest.py` unless it names another
command.

- **AC1** — When `python <kit>/runlog.py check-records` runs over a fixture index holding one record
  that `render_record` produced from a model fixture populating every closed class, it exits 0 and
  prints `1 record`.
  Red when: the rendered record is refused, so the renderer and the leg disagree.
- **AC2** — When fixtures stage each refusal in S2, `check-records` exits 1 naming that rule and the
  line.
  Red when: any staged violation passes.
- **AC3** — When no record is tracked, the leg prints `0 records` and exits 0. When the glob is
  pointed at a pattern the renderer does not write, the self-test fails.
  Red when: an empty population reads as a green grade with no announcement.
- **AC4** — When `check-records` runs over fixture indexes of 1 and of 100 records, it makes the same
  number of git subprocess calls for both, and `tools/gate-legs.json` declares its ceiling.
  Red when: the leg reads git per record.

## 7. Gates

`govkit selfcheck` · `codebase-map coverage + freshness` · `leg ceilings clear their evidenced maximum` · `lexicon naming predicates` · `memory hygiene`

New arm: `tools/runlog/selftest.py` · each refusal staged RED on a fixture record · floor raised by the arm count

## 8. Open questions

none

## 9. Revision log

- rev-1 · 2026-09-13 · initial draft.
- rev-2 · 2026-09-13 · S4 S5 · AC1 AC4 · folded round-1 spec audit B3 (the clean fixture is rendered by
  `render_record` from a model fixture carrying every closed class, so renderer-leg disagreement reds)
  and H9 (AC4's wall-clock floor becomes a constant git-call count), and L2 (the hand-off to unit 11).

## 10. Reuse audit

`tools/codebase-map/reuse_lookup.py "check committed records against a schema"` pointed at the
hygiene gate's check 21 and the build-index record reader, both of which grade BINDING, not content.
No existing seam grades a record's cell values. The leg shape follows `recall floor` and
`codebase-map gate coverage`, both repo-subject declarations legs with small ceilings.

Recall terms used: run-state RUN.md parked rows driver verb witness phase transcript session keepalive gate-ledger wrap-up telemetry
