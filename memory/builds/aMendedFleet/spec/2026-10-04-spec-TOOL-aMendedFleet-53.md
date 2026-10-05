# TOOL-aMendedFleet-53 — the dangling-pointer signal reads the declared auto-memory directory and checks its backticked paths against the tracked tree

**Status:** CLOSED · rev-2 · 2026-10-04 · node a · Tier-1 · base 7af5f564 · streams tooling · ratified 2026-10-04 · order 53 · advances TOOL-aUnmannedHelm-2

<!-- gen:spec-records -->

*No record names this unit.*

<!-- /gen:spec-records -->

## 1. Goal

`dangling_pointers_in_own_ledger` reads `memory/project/in-flight/<node tag>.md`, a ledger shard
that retired with the authored session ledger, so it has printed `DEAD PROBE` on every run since.
The node-local record that does exist, and that nothing audits, is the agent's auto-memory: on node
`a` it holds 75 notes, and one of them still names two files that commit `e3d2cda9b` deleted. This
unit points the signal at an auto-memory directory the project layer declares, and checks every
backticked repo path in those notes against `git ls-files`, so a note that outlived the file it
describes is reported instead of being re-read as true.

## 2. Scope (IN)

- **S1** — THE DECLARATION. The project layer gains `AUTO_MEMORY_DIR`, a string. `~` expands to the
  user's home and the token `{checkout}` expands to the primary checkout's absolute path with every
  character outside `[A-Za-z0-9-]` turned into `-`, which is how Claude Code keys a project's
  auto-memory. The primary checkout is the parent of the absolute path
  `git rev-parse --path-format=absolute --git-common-dir` prints, so every worktree of one clone
  reads the same directory. A new helper `resolve_auto_memory_dir` in
  `tools/drift-audit/drift_report.py` does the expansion. This repo's
  `tools/drift-audit/drift_signals.py` declares `"~/.claude/projects/{checkout}/memory"`; the
  shipped `tools/drift-audit/drift_signals.template.py` declares it blank with a comment saying what
  the two expansions are. Observed by AC1, AC3.
- **S2** — THE PROBE. `signal_dangling_pointers` reads every `*.md` file directly in the resolved
  directory and judges each backticked span that carries a `/`, no whitespace and none of the
  characters `< > { } * ? $ | " ' \`, after a trailing `:<digits>` and a trailing `/` are stripped,
  and whose first `/`-segment is a top-level entry of `git ls-files`. Such a token resolves when it
  equals a tracked file or a directory prefix of one. The record's `value` is the count of distinct
  (note, path) pairs that do not resolve, its `of` the count judged, and each detail row names the
  note's filename and the path. Observed by AC1, AC2.
- **S3** — THE STATES. `AUTO_MEMORY_DIR` blank or absent returns the `_build_not_asked` record.
  Declared but naming no existing directory, or a directory whose notes yield no judged token,
  returns `live` false with a note naming the resolved path, so the human table prints `DEAD PROBE`
  and never a clean 0. The record stays `gateable` false: node-local data reports and never gates,
  and its `tolerance` is the pinless form unit 51 introduces. Observed by AC3.
- **S4** — The node-tag lookup goes, because this signal was its only reader: `Ctx` stops setting
  `node_tag` and the method `_resolve_node_tag` is deleted. The template's `CHARTER` comment, which
  says the charter is read for this signal's node tag, is corrected to name what still reads it.
  Observed by AC4.
  **Readers:** by name: `tools/drift-audit/drift_report.py` defines `_resolve_node_tag`, calls it in
  the `Ctx` constructor and reads `ctx.node_tag` in `signal_dangling_pointers`;
  `tools/drift-audit/drift_signals.template.py` names the signal in its `CHARTER` comment.
  by value: `signal_dangling_pointers` is the only reader of the tag's value, and S2 stops reading it.
- **S5** — The `dangling_pointers_in_own_ledger` row of the `## The signals` table in
  `tools/drift-audit/README.md` asks whether this node's auto-memory notes name repo paths that still
  exist, and the README's layout table lists `AUTO_MEMORY_DIR` among the project-layer names.
  Observed by AC4.
- **S6** — Self-test arms in `tools/drift-audit/selftest.py` over a fixture directory: a note naming
  one tracked path and one untracked path under a tracked top-level directory reads value 1 of 2; a
  blank declaration reads not asked; a missing directory reads not live. NOT OBSERVED by a criterion
  here: the suite runs once at the close, and the arms are declared under `New arm:` in §7.
- **S7** — `memory/map/generated/symbols.json` is regenerated for the new definition. NOT OBSERVED
  by a criterion here: `python tools/codebase-map/gen_map.py --check` at the close is its check, and
  §7 names the legs that read it.

## 3. Non-goals (OUT)

- Editing any auto-memory note. The notes are node-local and outside this repository; draining the
  two deleted install-prefix paths is the note owner's act, and the signal is what tells them.
- The `ledger_rows_contradicting_git` signal and `Ctx.ledger_dir`, which it still reads. That
  signal stays empty by declaration; the rest of `TOOL-aUnmannedHelm-2` is its own question.
- Renaming the signal. The name keeps its readers, among them the history rows unit 48 writes.
- A pin. The value is a property of one machine's notes, so a committed number would be another
  node's wrong answer.
- The drift-audit kit version bump, owed once at the close.

### Edges

- **consumes-from** `TOOL-aMendedFleet-51` — the pinless `tolerance` form S3 uses; without it the
  record would print `over pin 0` on every node with a stale note.
- **hands-off** external — the two stale paths in node `a`'s install-prefix note, for the note's
  owner to correct.
- **hands-off** external — the drift-audit kit version bump, owed once at the close.

## 4. Design

### Evidence

Read at worktree HEAD `725b1449`, whose `tools/` bytes equal base `7af5f564`'s.

- `python tools/drift-audit/drift_report.py` prints `dangling_pointers_in_own_ledger -1 0 DEAD
  PROBE`; the detail note is `no ledger file for node a`. The ledger directory it reads does not
  exist in the tree.
- A scratch probe applying S1 and S2 from this worktree resolved the primary checkout to
  `C:\projects\coding-governance`, the key `C--projects-coding-governance`, and a directory holding
  75 notes. It judged 54 (note, path) pairs and found 3 that do not resolve: the install-prefix note
  names `tools/install-prefix-carried.txt` and `tools/install-prefix-waivers.txt`, both deleted by
  `e3d2cda9b`, and the suite-slicing note names a scratch script it tells the reader to create and
  delete, which is a true report of a path the tree does not carry. PINNED, measured 2026-10-04 on
  node `a`.
- `node_tag` has one reader, `signal_dangling_pointers`; `git grep` over `tools/` finds no other.

### Inventory

- `resolve_auto_memory_dir` — cell `py.function`; answered OK by
  `python tools/lexicon/lexicon.py --suggest resolve_auto_memory_dir --as py.function`.
- `AUTO_MEMORY_DIR` — a project-layer attribute read with `getattr` and a blank default, so an older
  adopter's layer keeps importing.

### Files touched (estimate)

- `tools/drift-audit/drift_report.py`
- `tools/drift-audit/drift_signals.py`
- `tools/drift-audit/drift_signals.template.py`
- `tools/drift-audit/selftest.py`
- `tools/drift-audit/README.md`
- `memory/map/generated/symbols.json`

### Alternatives rejected

- **A literal absolute directory in the project layer.** It is right on one machine and names a
  missing directory on every other, which is the DEAD state on purpose rather than by accident.
- **Re-deriving the old ledger shard.** It retired; the directory the probe would read is banned by
  hygiene check 3, which is the disagreement `TOOL-aUnmannedHelm-2` records.
- **Checking existence on disk instead of `git ls-files`.** An untracked leftover file would make a
  stale note read as true, and the brief names the tracked set as the oracle.

## 5. Production-readiness checklist

- security — reads files under the user's own profile and prints repo-relative paths and note
  filenames only; no note text reaches the output.
- perf / scale — one `git ls-files` and one `git rev-parse`; 75 small files read at writing.
- error / empty / loading states — S3's three states; an unreadable note is skipped and counted in
  the record's `unjudgeable`.
- observability — each detail row names the note and the path to correct.
- risks — a note quoting a path as an example of what NOT to create reads as stale; report-only, so
  the cost is one line a reader dismisses.
- testing — AC1 to AC4 here; the arms in S6.
- migration — N/A: nothing stored changes.
- user docs — S5.

## 6. Acceptance criteria

- **AC1** — When `python tools/drift-audit/drift_report.py --json` runs on node `a`, the
  `dangling_pointers_in_own_ledger` record has `live` true, `gateable` false and `of` above 0, and
  every detail row carries a note filename and a repo path.
  Red when: the probe still reads the ledger shard, or reports DEAD with the directory present.
  fixture: node `a`'s auto-memory directory, present today with 75 notes.
  figure: DERIVED at observation time; 3 of 54 at writing.
- **AC2** — When `AUTO_MEMORY_DIR` in `tools/drift-audit/drift_signals.py` is pointed, in the
  working tree, at a scratch directory holding one note whose backticks name
  `tools/drift-audit/drift_report.py` and a second path in that same directory that no file
  carries, and `python tools/drift-audit/drift_report.py --json` runs, the record reads `value` 1 and
  `of` 2 and its one detail row names the second path; restoring the declaration restores AC1.
  Red when: an untracked path resolves, or a tracked one is reported.
- **AC3** — When the declaration is staged blank and `python tools/drift-audit/drift_report.py` runs,
  the signal's row prints the not-asked status; when it names a directory that does not exist, the
  row prints `DEAD PROBE` and the `--json` detail names the resolved path.
  Red when: either state prints a value with an `ok` status.
- **AC4** — When `grep -c "node_tag" tools/drift-audit/drift_report.py` runs it reports 0, and
  `grep -n "AUTO_MEMORY_DIR" tools/drift-audit/drift_signals.template.py tools/drift-audit/README.md`
  reports at least one hit in each file.
  Red when: the dead lookup survives, or a carrier omits the new name.

## 7. Gates

`drift-audit selftest` · `drift-audit records` · `drift-audit wiring` · `encoding posture (text IO names its encoding)` · `codebase-map coverage + freshness` · `recall floor` · `recall floor arms` · `lexicon naming predicates` · `kit epoch (shipped bytes move, the version moves)` · `spec tokens (a spec's own names resolve)`

New arm: `tools/drift-audit/selftest.py` · a fixture auto-memory directory with one note naming a tracked and an untracked path, then a blank declaration, then a missing directory · `CHECK_FLOOR` moves by the checks the arm adds

## 8. Open questions

- **F1** — How is a per-machine directory declared in a committed file?
  Options: a literal absolute path; an environment variable the operator sets; a template with `~`
  and `{checkout}` expanded at run time. The literal is wrong on every other node, and an environment
  variable unset on a fresh machine makes the signal silently not asked where the directory exists.
  RESOLVED (agent, 2026-10-04, delegated): the template, per S1; its key derivation was measured to
  resolve node `a`'s directory from a linked worktree.

## 9. Revision log

- rev-1 · 2026-10-04 · initial draft, from the synthesis's item [#56] and a scratch probe of node
  `a`'s auto-memory against `git ls-files` at base.
- rev-2 · 2026-10-04 · S7 · §4 · §7 · M2 cross-read: the new definition owes `symbols.json`, which
  units 57, 59 and 90 regenerate for theirs and this spec omitted.

## 10. Reuse audit

The seam extended is `signal_dangling_pointers` in `tools/drift-audit/drift_report.py`, whose record
shape, DEAD reporting and `gateable` false this unit keeps, with `_build_not_asked` for the blank
declaration. `python tools/codebase-map/reuse_lookup.py "check backticked paths in a markdown note
against git ls-files"` returned name-stem neighbours only: `tracked_files` in the lexicon kit,
`corpus_files` in the recall kit and `attribute_paths` in the map kit, each another kit's file
lister that a kit file may not import, and none judging a note's backticked paths; no existing seam
fits, so the judging lives in the signal. The projects-root lookup in `tools/runlog/extract.py`,
`resolve_projects_root`, finds Claude Code's transcripts and not a project key, and is another kit's.
The scan names `.sh` as unscanned; no shell file is involved. Recall returned
`TOOL-aUnmannedHelm-2`, the open ask this advances, the aScouredKit wave-1 and statewave records
that found the probe permanently dead, and `TOOL-aMendedLedger-3`, the rule that a drained probe
goes to `DECLARED_EMPTY`; this probe is re-pointed rather than declared empty because a population
exists for it. Where the report and the tree disagree: nowhere; the two deleted paths reproduce.

Recall terms used: `python tools/memory-recall/query.py "why is the dangling pointer drift probe
dead and where should it read node-local memory" --terms "dangling_pointers_in_own_ledger ledger_dir
in-flight node tag DEAD PROBE auto-memory MEMORY.md node-local ledger retired drift-audit"`
