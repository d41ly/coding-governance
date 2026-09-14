# TOOL-dLoggedFlight-10 — the schema leg: a committed run record outside the closed schema reds the bar

**Status:** CLOSED · rev-7 · 2026-09-14 · node d · Tier-2 · base 9fac2b53 · streams tooling · order 10

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-09-13-build-TOOL-dLoggedFlight-1-design-research.md](../build/2026-09-13-build-TOOL-dLoggedFlight-1-design-research.md) | research | TOOL-dLoggedFlight-1 TOOL-dLoggedFlight-2 TOOL-dLoggedFlight-3 TOOL-dLoggedFlight-4 TOOL-dLoggedFlight-5 TOOL-dLoggedFlight-6 TOOL-dLoggedFlight-7 TOOL-dLoggedFlight-8 TOOL-dLoggedFlight-9 TOOL-dLoggedFlight-11 TOOL-dLoggedFlight-12 TOOL-dLoggedFlight-13 |
| [2026-09-14-build-TOOL-dLoggedFlight-10-1-acceptance-ledger.md](../build/2026-09-14-build-TOOL-dLoggedFlight-10-1-acceptance-ledger.md) | journal | — |
| [2026-09-13-prompt-TOOL-dLoggedFlight-1-1-build-brief.md](../prompts/2026-09-13-prompt-TOOL-dLoggedFlight-1-1-build-brief.md) | journal | TOOL-dLoggedFlight-1 TOOL-dLoggedFlight-2 TOOL-dLoggedFlight-3 TOOL-dLoggedFlight-4 TOOL-dLoggedFlight-5 TOOL-dLoggedFlight-6 TOOL-dLoggedFlight-7 TOOL-dLoggedFlight-8 TOOL-dLoggedFlight-9 TOOL-dLoggedFlight-11 TOOL-dLoggedFlight-12 TOOL-dLoggedFlight-13 |
| [2026-09-13-review-TOOL-dLoggedFlight-1-spec-audit-round1.md](../reviews/2026-09-13-review-TOOL-dLoggedFlight-1-spec-audit-round1.md) | spec-audit | TOOL-dLoggedFlight-1 TOOL-dLoggedFlight-2 TOOL-dLoggedFlight-3 TOOL-dLoggedFlight-4 TOOL-dLoggedFlight-5 TOOL-dLoggedFlight-6 TOOL-dLoggedFlight-7 TOOL-dLoggedFlight-8 TOOL-dLoggedFlight-9 TOOL-dLoggedFlight-11 TOOL-dLoggedFlight-12 TOOL-dLoggedFlight-13 |
| [2026-09-13-review-TOOL-dLoggedFlight-1-spec-audit-round2.md](../reviews/2026-09-13-review-TOOL-dLoggedFlight-1-spec-audit-round2.md) | spec-audit | TOOL-dLoggedFlight-1 TOOL-dLoggedFlight-2 TOOL-dLoggedFlight-3 TOOL-dLoggedFlight-4 TOOL-dLoggedFlight-5 TOOL-dLoggedFlight-6 TOOL-dLoggedFlight-7 TOOL-dLoggedFlight-8 TOOL-dLoggedFlight-9 TOOL-dLoggedFlight-11 TOOL-dLoggedFlight-12 TOOL-dLoggedFlight-13 |
| [2026-09-13-review-TOOL-dLoggedFlight-1-spec-audit-round3.md](../reviews/2026-09-13-review-TOOL-dLoggedFlight-1-spec-audit-round3.md) | spec-audit | TOOL-dLoggedFlight-1 TOOL-dLoggedFlight-2 TOOL-dLoggedFlight-3 TOOL-dLoggedFlight-4 TOOL-dLoggedFlight-5 TOOL-dLoggedFlight-6 TOOL-dLoggedFlight-7 TOOL-dLoggedFlight-8 TOOL-dLoggedFlight-9 TOOL-dLoggedFlight-11 TOOL-dLoggedFlight-12 TOOL-dLoggedFlight-13 |
| [2026-09-14-review-TOOL-dLoggedFlight-1-closing-diff-review-round1.md](../reviews/2026-09-14-review-TOOL-dLoggedFlight-1-closing-diff-review-round1.md) | diff-review | TOOL-dLoggedFlight-1 TOOL-dLoggedFlight-2 TOOL-dLoggedFlight-3 TOOL-dLoggedFlight-4 TOOL-dLoggedFlight-5 TOOL-dLoggedFlight-6 TOOL-dLoggedFlight-7 TOOL-dLoggedFlight-8 TOOL-dLoggedFlight-9 TOOL-dLoggedFlight-11 TOOL-dLoggedFlight-12 TOOL-dLoggedFlight-13 |

<!-- /gen:spec-records -->

## 1. Goal

The run record is public, and its safety rests on a closed schema. A renderer that honours the schema
proves nothing about a record edited afterwards by hand, by a merge, or by a later renderer with a bug.
Add a merge-bar leg that reads every committed run record's BYTES and refuses anything outside the
schema, independently of the renderer.

## 2. Scope (IN)

- **S1** `runlog.py check-records`, run as a new repo-subject leg `runlog record schema`. It reads every
  tracked `<memory-root>/builds/*/build/*-runlog-*.md` from the index, not the working tree, with the
  root from `resolve_memory_root` of `TOOL-dLoggedFlight-1`, and validates each against
  `RECORD_SCHEMA` from `TOOL-dLoggedFlight-9`. Observed by AC1.
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

  Each refusal carries one rule id from a closed list, `RECORD_RULES`: `headings`, `first-cell`, `cell`,
  `absolute-path`, `uuid`, `data`, `size` and `serves` are the eight above. Three more follow from a
  closed grammar, and each is a refusal S2's list implies without naming. `line` is any line outside
  the record grammar, such as free text, a CR byte, or a fact after a table. `name` is a file the glob
  admits whose name the renderer would never write. `unreadable` is a record that is not UTF-8, not a
  regular file, or unmerged in the index. A fact line is a cell: its label must be declared for its
  section, at most once and in the declared order, and its value must match one of the label's
  templates. `-` is admissible in every class, because it is what the renderer writes for an absent or
  withheld value, and it is refused only as a first cell. The size rule reads `RECORD_SCHEMA`'s own
  `cap_bytes`.
- **S3** Liveness. The leg prints the population it graded. An empty population is reported as
  `0 records (none committed yet)` and exits 0, because a repo with no run records yet is a legitimate
  state. The leg asserts the tracked glob it reads is the one the renderer writes, and that the
  declared root holds tracked files, so a renamed pattern or a wrong root cannot empty the population in
  silence. The glob is asserted at run time against the renderer's own code: the path
  `derive_record_relpath` builds for a probe run must be one the glob admits, or the leg reds with the
  rule `glob`. The root assertion reds with the rule `root`. Exit 0 is a graded population with no
  refusal, 1 is any refusal or failed assertion, and 2 is a leg that could not run. Observed by AC3.
- **S4** Cost: the leg reads the whole population in a constant number of git calls, one `ls-files`
  and one `cat-file --batch`, and declares a 60 s ceiling. Observed by AC4.
- **S5** A render-then-grade arm. The clean fixture the leg is tested against is produced by
  `render_record` from a model fixture that populates every section with one value of each closed
  class. So a renderer and a leg that disagree fail the self-test. Observed by AC1.

  The absolute-path and UUID shapes are DATA in `RECORD_SCHEMA`, under `forbidden`, and the renderer
  withholds any value one of them finds. Building this found the disagreement S5 exists for: the
  `label` class admits a lowercase UUID, so without that the renderer would write a record the leg
  refuses.
- **S6** A real-population arm for runs. The leg derives, through the population form of
  `derive_run_starts`, the start commit of every tracked run-state file under the declared root, and
  refuses a build in which two runs share one. The tracked set comes from the leg's own `ls-files`
  rather than the working tree. Through `derive_run_eras` it also computes each run's window from git
  alone, as a fresh clone must, and refuses one that ends before its start or overlaps another window
  of its build. The window is the model's own derivation, not a copy. `derive_record_commits` and
  `derive_window` are moved out of `build_run_model` into functions both callers read, with no change
  to what the model computes. That costs one `git log` for the whole population, plus one log and one
  batch read over the run-state paths, whatever the number of builds. On this tree it grades six
  rotated builds and prints each one's start commits. The leg ends a non-terminal window one second
  past the run's last record commit. The model's end also reads the run's own commits and the journal
  lines of the trees it holds (`TOOL-dLoggedFlight-8` S2), which the leg does not read, so the model's
  end is at or after the leg's. Neither refusal turns on the difference. A preflight rotates only a
  terminal record, so a non-terminal run is the last of its build and its end meets no later window,
  and a later end cannot put a window's end before its start. When the shared start is one
  `derive_run_starts` marks `joint_add`, the shape and its causes being `TOOL-dLoggedFlight-8` S1's,
  the `run-start` refusal names that shape, and the leg follows no path back past it. It stays a
  refusal, because one log cannot tell a move from a squash and AC5 requires the squash to red. No
  waiver clears it; the unit's acceptance ledger parks that question. Observed by AC4 and AC5.

## 3. Non-goals (OUT)

- Grading content truth. The leg proves a record carries only permitted SHAPES, never that its counts
  are right, which the leg's own header states as charter §7 requires.
- Records in other folders, and records not named `-runlog-`.

### Edges

- **consumes-from** `TOOL-dLoggedFlight-9` — the closed schema, the record naming and the renderer the
  clean fixture comes from, with the run starts it reads from the model.
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
| `derive_record_relpath` | the renderer's path builder, which the leg's glob assertion calls | `py.function` |
| `derive_record_commits`, `derive_window` | moved out of `build_run_model`, read by both | `py.function` |
| `RECORD_RULES`, `RECORD_GLOB`, `RECORD_SCHEMA["forbidden"]` | data | constants |
| `cmd_check_records` | CLI subcommand | reserved `cmd` |
| `runlog record schema` | leg, `repo` / `declarations`, ceiling 60, unguarded | manifest |

The leg ships. It is a `[[gate_leg]]` in the runlog descriptor with `history_depth = "full"`, because a
shallow clone's boundary commit adds every run-state path at once and would give every run one start.

### Files touched (estimate)

`tools/runlog/{record.py,runlog.py,model.py,selftest.py,kit.toml,README.md}`, `tools/gate-legs.json`,
`tools/govkit/subject-pins.tsv`, `memory/guides/SESSION-KICKOFF.md`'s stamp,
`memory/map/features/runlog.md` and the regenerated map.

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
  pointed at a pattern the renderer does not write, the self-test fails. With `MEMORY_ROOT=docs/mem`,
  the leg grades records under `docs/mem/builds/`, and with the declared root holding no tracked file
  it reds rather than reporting zero.
  Red when: an empty population reads as a green grade with no announcement, or a wrong root does.
- **AC4** — When `check-records` runs over fixture indexes of 1 and of 100 records, and of 1 and of 50
  builds carrying run-state files, it makes the same number of git subprocess calls for each pair, and
  `tools/gate-legs.json` declares its ceiling. When a
  staged record violates S2 while its working copy is clean, the leg reds, and in the reverse case it
  stays green.
  Red when: the leg reads git per record or per build, or grades the working tree instead of the
  index.
- **AC5** — When `check-records` runs on this tree, it reports the start commits of the six rotated
  builds as pairwise distinct and their windows as ending at or after their starts and disjoint. On a
  fixture build whose two records share a start commit, and on one whose live window would end at its
  predecessor's terminal write, it exits 1 naming the build.
  The first fixture is a squashed history, one commit adding an archive and `RUN.md`, and a rotated
  build graded under the naive key, each archive keyed on its own creation commit. The second is a
  LANDED-after-LANDED build rotated the way the driver rotates. It is green under the era-bounded
  derivation, and red once the eras are staged to span the path's whole history, which is the reading
  round-3 H2 named. A third is a build rotated the way the driver rotates whose memory root then
  moves in one commit, as `git mv` records it, with the conf naming the new root. The leg exits 1
  naming that build under `run-start`, and that refusal, like the squashed history's, names the
  shape it saw, while the rotation graded before the move names none.
  Red when: the key derivation collapses an archive into its successor, or a window ends before its
  start, and the leg stays green, or a moved root's refusal does not name the shape.

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
- rev-3 · 2026-09-13 · S6 · AC4 AC5 · folded round-2 spec audit L2 (an index-versus-working-tree arm) and
  B1's left-shift (the leg asserts every build's run keys are distinct over the real population).
- rev-4 · 2026-09-13 · S1 S3 S6 · AC3 AC4 AC5 · folded round-3 spec audit M12 (the declared memory root,
  with a two-segment fixture and a wrong-root refusal), L3 (the cost criterion varies the build count)
  and H2's left-shift (every run's window is graded over the real population).
- rev-5 · 2026-09-14 · S2 S3 S5 S6 · §4 · AC5 · the build pass, before its code. S2 names each rule's id
  and adds the three a closed grammar implies, `line`, `name` and `unreadable`. It says a fact line is
  graded as a cell, and that `-` is admissible everywhere but a first cell. S3 says how the glob and
  root assertions run and fixes the exit codes. S5 moves the absolute-path and UUID shapes into
  `RECORD_SCHEMA` as data the renderer also withholds by: its `label` class admits a lowercase UUID,
  which is the renderer-leg disagreement S5 exists to catch. S6 reads the tracked set from the leg's
  own `ls-files`, and it reads the window through two functions moved out of `build_run_model`, so the
  leg and the model share one derivation. §4 lists the added names and why the leg ships with full
  history, and Files touched gains `model.py`, the README and the manifest stamp. AC5 names its
  fixtures: the H2 window needs a staged derivation to go red, because the era-bounded one cannot end
  a window before its start.
- rev-6 · 2026-09-14 · S6 · the closing diff review's round-1 M5, folded into `TOOL-dLoggedFlight-8`
  S2. The model's non-terminal end now reads the run's own commits and the lines of the trees it
  holds, and the leg reads neither: own commits need a range per run, and the leg's git cost is
  constant over the population. S6 says the two ends differ, which is the larger, and why no refusal
  of the leg turns on it. Before this line, "the model's own derivation" read as the same window.
- rev-7 · 2026-09-14 · S6 · AC5 · folded the closing diff review's round-1 L3. A memory root or a
  build folder moved in one commit ADDS every record it moves, with renames off, so a rotated
  build's archive and live record both started at the move. The leg then refused `run-start` on
  every bar, `verify` looked up the pre-move key and raised, and `record --write` wrote a second
  file. The kit README expects a root to move, and its list of what the leg does not check did not
  name this. The refusal now names the shape, and that list names the limit. The review's first
  option, following the pre-move path, was not taken: the model keys every read on a path under the
  current root, so following the starts alone would leave its windows quietly wrong. Its waiver
  route is parked in the unit's acceptance ledger, since a waiver registry is a new surface an
  adopter authors, which is the owner's turn.

## 10. Reuse audit

`tools/codebase-map/reuse_lookup.py "check committed records against a schema"` pointed at the
hygiene gate's check 21 and the build-index record reader, both of which grade BINDING, not content.
No existing seam grades a record's cell values. The leg shape follows `recall floor` and
`codebase-map gate coverage`, both repo-subject declarations legs with small ceilings.

Recall terms used: run-state RUN.md parked rows driver verb witness phase transcript session keepalive gate-ledger wrap-up telemetry
