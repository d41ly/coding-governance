# TOOL-dLinkedLibrary-9 — the origin check: each record's `origin` re-derived from history, shown in every slice and ranked in the reuse digest

**Status:** OPEN · rev-2 · 2026-10-26 · node d · Tier-2 · base 5fede642 · streams tooling · order 21 · advances TOOL-dLinkedLibrary-26

**Carries:** cl-dClosedLoop-0246@96afa172 whole

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-26-build-TOOL-dLinkedLibrary-1-agent-ledger.md](../build/2026-10-26-build-TOOL-dLinkedLibrary-1-agent-ledger.md) | journal | TOOL-dLinkedLibrary-1 TOOL-dLinkedLibrary-2 TOOL-dLinkedLibrary-3 TOOL-dLinkedLibrary-4 TOOL-dLinkedLibrary-5 TOOL-dLinkedLibrary-6 TOOL-dLinkedLibrary-7 TOOL-dLinkedLibrary-8 TOOL-dLinkedLibrary-10 TOOL-dLinkedLibrary-11 TOOL-dLinkedLibrary-12 TOOL-dLinkedLibrary-13 TOOL-dLinkedLibrary-14 TOOL-dLinkedLibrary-15 TOOL-dLinkedLibrary-16 TOOL-dLinkedLibrary-17 TOOL-dLinkedLibrary-18 TOOL-dLinkedLibrary-19 TOOL-dLinkedLibrary-20 TOOL-dLinkedLibrary-21 TOOL-dLinkedLibrary-22 TOOL-dLinkedLibrary-23 TOOL-dLinkedLibrary-24 TOOL-dLinkedLibrary-25 TOOL-dLinkedLibrary-37 TOOL-dLinkedLibrary-38 TOOL-dLinkedLibrary-39 TOOL-dLinkedLibrary-40 TOOL-dLinkedLibrary-41 TOOL-dLinkedLibrary-42 TOOL-dLinkedLibrary-43 TOOL-dLinkedLibrary-44 TOOL-dLinkedLibrary-45 TOOL-dLinkedLibrary-46 TOOL-dLinkedLibrary-47 TOOL-dLinkedLibrary-48 TOOL-dLinkedLibrary-49 TOOL-dLinkedLibrary-50 TOOL-dLinkedLibrary-51 TOOL-dLinkedLibrary-52 TOOL-dLinkedLibrary-53 TOOL-dLinkedLibrary-54 TOOL-dLinkedLibrary-55 TOOL-dLinkedLibrary-56 TOOL-dLinkedLibrary-57 TOOL-dLinkedLibrary-58 TOOL-dLinkedLibrary-59 TOOL-dLinkedLibrary-60 TOOL-dLinkedLibrary-61 TOOL-dLinkedLibrary-62 TOOL-dLinkedLibrary-63 TOOL-dLinkedLibrary-64 TOOL-dLinkedLibrary-65 TOOL-dLinkedLibrary-66 TOOL-dLinkedLibrary-67 TOOL-dLinkedLibrary-68 TOOL-dLinkedLibrary-69 TOOL-dLinkedLibrary-70 TOOL-dLinkedLibrary-71 TOOL-dLinkedLibrary-72 TOOL-dLinkedLibrary-73 TOOL-dLinkedLibrary-74 TOOL-dLinkedLibrary-75 TOOL-dLinkedLibrary-76 TOOL-dLinkedLibrary-77 TOOL-dLinkedLibrary-78 TOOL-dLinkedLibrary-79 TOOL-dLinkedLibrary-80 |
| [2026-10-26-build-TOOL-dLinkedLibrary-1-reuse-scout-d.md](../build/2026-10-26-build-TOOL-dLinkedLibrary-1-reuse-scout-d.md) | research | TOOL-dLinkedLibrary-8 TOOL-dLinkedLibrary-10 TOOL-dLinkedLibrary-23 TOOL-dLinkedLibrary-1 |
| [2026-10-26-build-TOOL-dLinkedLibrary-1-spec-stage-returns.md](../build/2026-10-26-build-TOOL-dLinkedLibrary-1-spec-stage-returns.md) | research | TOOL-dLinkedLibrary-1 TOOL-dLinkedLibrary-2 TOOL-dLinkedLibrary-3 TOOL-dLinkedLibrary-4 TOOL-dLinkedLibrary-5 TOOL-dLinkedLibrary-6 TOOL-dLinkedLibrary-7 TOOL-dLinkedLibrary-8 TOOL-dLinkedLibrary-10 TOOL-dLinkedLibrary-11 TOOL-dLinkedLibrary-12 TOOL-dLinkedLibrary-13 TOOL-dLinkedLibrary-14 TOOL-dLinkedLibrary-15 TOOL-dLinkedLibrary-16 TOOL-dLinkedLibrary-17 TOOL-dLinkedLibrary-18 TOOL-dLinkedLibrary-19 TOOL-dLinkedLibrary-20 TOOL-dLinkedLibrary-21 TOOL-dLinkedLibrary-22 TOOL-dLinkedLibrary-23 TOOL-dLinkedLibrary-24 TOOL-dLinkedLibrary-25 |
| [2026-10-26-prompt-TOOL-dLinkedLibrary-1-spec-brief.md](../prompts/2026-10-26-prompt-TOOL-dLinkedLibrary-1-spec-brief.md) | research | TOOL-dLinkedLibrary-1 TOOL-dLinkedLibrary-2 TOOL-dLinkedLibrary-3 TOOL-dLinkedLibrary-4 TOOL-dLinkedLibrary-5 TOOL-dLinkedLibrary-6 TOOL-dLinkedLibrary-7 TOOL-dLinkedLibrary-8 TOOL-dLinkedLibrary-10 TOOL-dLinkedLibrary-11 TOOL-dLinkedLibrary-12 TOOL-dLinkedLibrary-13 TOOL-dLinkedLibrary-14 TOOL-dLinkedLibrary-15 TOOL-dLinkedLibrary-16 TOOL-dLinkedLibrary-17 TOOL-dLinkedLibrary-18 TOOL-dLinkedLibrary-19 TOOL-dLinkedLibrary-20 TOOL-dLinkedLibrary-21 TOOL-dLinkedLibrary-22 TOOL-dLinkedLibrary-23 TOOL-dLinkedLibrary-24 TOOL-dLinkedLibrary-25 |
| [2026-10-26-review-TOOL-dLinkedLibrary-1-spec-audit.md](../reviews/2026-10-26-review-TOOL-dLinkedLibrary-1-spec-audit.md) | spec-audit | TOOL-dLinkedLibrary-1 TOOL-dLinkedLibrary-10 TOOL-dLinkedLibrary-11 TOOL-dLinkedLibrary-12 TOOL-dLinkedLibrary-13 TOOL-dLinkedLibrary-14 TOOL-dLinkedLibrary-15 TOOL-dLinkedLibrary-16 TOOL-dLinkedLibrary-17 TOOL-dLinkedLibrary-18 TOOL-dLinkedLibrary-19 TOOL-dLinkedLibrary-2 TOOL-dLinkedLibrary-20 TOOL-dLinkedLibrary-21 TOOL-dLinkedLibrary-22 TOOL-dLinkedLibrary-23 TOOL-dLinkedLibrary-24 TOOL-dLinkedLibrary-25 TOOL-dLinkedLibrary-3 TOOL-dLinkedLibrary-4 TOOL-dLinkedLibrary-5 TOOL-dLinkedLibrary-6 TOOL-dLinkedLibrary-7 TOOL-dLinkedLibrary-8 |

<!-- /gen:spec-records -->

## 1. Goal

A reconstructed record reads as written today, because no record carries an origin (gap-mem-25,
`memory/builds/dClosedLoop/build/2026-10-14-build-PLAY-dClosedLoop-1-gap-register.md:208`).
TOOL-dLinkedLibrary-8 gives every record kind the `origin` field, written by the record door and
never typed (I20). This unit makes that field trustworthy and visible: a check re-derives each
record's origin from history, independently of the write path, and reds a stored value that
disagrees; `record find` and `record show` render the origin in every row and slice; and one
ranking function orders `written` above `imported` above `reconstructed`, which the reuse digest of
TOOL-dLinkedLibrary-2 sorts by (retrofit.md `[origin]`,
`memory/builds/dClosedLoop/build/2026-10-17-build-PLAY-dClosedLoop-1-retrofit.md:445-470`).

## 2. Scope (IN)

Build-run preconditions this unit calls and does not build, each specced and DEFERRED at base: the
record door `gov_record.py new <kind>` and its `write_new_record` (TOOL-dTotalRecall-2 S1 to S5); the
one header reader `read_header_edges` in `tools/memory-tree/tree_lib.py` (TOOL-dTotalRecall-19 S1);
`record find` and `record show` in `tools/memory-tree/record_find.py` (TOOL-dTotalRecall-9 S3, S5);
and the `origin` field with its three values, written by the door (TOOL-dLinkedLibrary-8, I20).

- **S1** — The reader. `read_header_edges(path, text)` (TOOL-dTotalRecall-19 S1) returns a fourth
  key, `origin`: the value of the record's origin line in the spelling I20 gives, read where that
  function reads `Made-by` (a column-0 `**Origin:**` line within `BIND_HEAD_LINES`,
  `tools/memory-tree/tree_lib.py:401`, for an untyped record; the `- **Origin:**` field for a typed
  one), or `None` when the record carries none. A second origin line is a refusal naming both lines,
  as a second `Made-by` is. Observed by AC1 and AC5.
- **S2** — The derivation, `derive_origin(root, record, landing, history)` in a new
  `tools/memory-tree/record_origin.py`, per §4 "The derivation": from the record's landing commit and
  its subject's last-changing commit before it, it answers `written` or `not-written`; for a stored
  `reconstructed@<sha8> <sources>` it checks that `<sha8>` names an ancestor of the landing commit
  holding each source; for a stored `imported:<path>` it checks that `<path>` existed at the landing
  commit's first parent and lies outside the memory root. It reads history and never the door's
  write path. Observed by AC1, AC2 and AC3.
- **S3** — The check, `check_origin(root)` and `python record_origin.py --check`: over every tracked
  record whose S1 reader returns an origin, red (exit 1) on each record whose stored value S2 does not
  derive, one line per record naming the path, the stored value, the derived answer and the commit
  and build that decided it. Records with no origin line are counted and named as `unrecorded`, never
  red and never green: with none graded the check prints `origin — unarmed: 0 of <n> records carry an
  origin line` and exits 0. Exit 2 on a refusal (a shallow clone, a failed git call). Observed by AC1
  to AC5.
- **S4** — The leg `record origin (stored origin against history)` in `tools/gate-legs.json`, argv
  `python {prefix}/memory-tree/record_origin.py --check`, its `reads.history` naming the commit
  graph, and the leg `record origin selftest`, argv `python {prefix}/memory-tree/record_origin.py
  --selftest`, guard `{prefix}/memory-tree/`, which runs every `--fixture --plant` case of §4 red and
  green. Observed by AC1 to AC4 and AC6.
- **S5** — The slices. `record find` rows (TOOL-dTotalRecall-9 S3, `key · kind · build · bytes ·
  path:line`) become `key · kind · build · origin · bytes · path:line`, and every `record show` slice
  (TOOL-dTotalRecall-9 S5) opens with one line `origin <value>`; the value is the stored origin, or
  `unrecorded` for a record that carries none. `reconstructed` records therefore render labelled
  wherever a slice is shown, a work order included. Observed by AC7 and AC8.
- **S6** — The ranking, `origin_rank(value)` in `record_origin.py`, the one ordering of the three
  values: `written` and `unrecorded` rank 0, `imported:<path>` 1, `reconstructed@<sha8> …` 2, any
  other value refused. The CLI `python record_origin.py --rank <value>…` prints the values in rank
  order, and `python record_origin.py --of <path>…` prints one `<path> TAB <origin> TAB <rank>` line
  per path, the origin read by S1 or `unrecorded`, so a caller in another kit ranks records with one
  subprocess call. TOOL-dLinkedLibrary-2's digest sorts by it and never re-spells the order.
  Observed by AC6.
- **S7** — The docs: a new page `help/record-origin.md` saying what each value means, where a slice
  shows it, how the check derives it and what it does not check, with its line in `help/README.md`;
  and a section of `tools/memory-tree/README.md` naming the module, the leg and the rank. Observed by
  AC9.

## 3. Non-goals (OUT)

- Writing the field. The door derives and writes `origin` at write time (TOOL-dLinkedLibrary-8,
  through TOOL-dTotalRecall-2); this unit only reads and checks it.
- A backfill of `origin` over the records landed before the door: a typed value over 4,000 records
  is exactly what "derived once, never typed" forbids, and `unrecorded` says what is true of them
  (§8 F3).
- The reuse digest itself and where it sorts: TOOL-dLinkedLibrary-2's; S6 is the order it calls.
- The work-order render: dBoundRoles shows a slice's lines, so S5's head line needs no change there
  (retrofit.md:467-469).
- Judging whether a `reconstructed` record's sources actually support its text: the check reads
  provenance, never content.

### Edges

- **consumes-from** `TOOL-dLinkedLibrary-8` — `origin`, the field and its three values (I20) the door writes on every record kind; without it the check has no stored value to compare and stays unarmed
- **hands-off** `TOOL-dLinkedLibrary-2` — `reconstructed`, ranked last by `origin_rank`, the order the reuse digest sorts its records and entries by
- **consumes-from** external — dTotalRecall, built before this build run: `read_header_edges` (TOOL-dTotalRecall-19 S1), the record door (TOOL-dTotalRecall-2 S1 to S5), and `record find` and `record show` (TOOL-dTotalRecall-9 S3, S5)
- **hands-off** `TOOL-dLinkedLibrary-37` — `derive_origin` and its table, whose provenance rows unit 37 rewrites, and the `reconstructed-but-written` plant it renames (id 58)
- **hands-off** `TOOL-dLinkedLibrary-52` — the two legs, which unit 52 declares through `leg_factory.py new` with their meta rows (ids 37, 45)

## 4. Design

### Evidence

- No origin field, value or check exists at base: `git grep -n "Origin:"` over `tools/` finds none,
  and `memory/HYGIENE.md` never names one (scout D row 9).
- `read_adding_commits(root, pathspec, wanted)` (`tools/memory-tree/tree_lib.py:302`) is the one
  reader of the commit that added each record, oldest add kept, from ONE `git log` call.
- `read_blobs_at(root, requests)` (`tools/memory-tree/tree_lib.py:328`) reads `<rev>:<path>` bytes in
  one `git cat-file --batch`.
- `read_routed_commits(repo, rev_args)` (`tools/memory-tree/routed_commits.py:228`) reads, in one log
  pass, each commit's sha, parents, subject, `Pass:` trailer and paths; `build_id_re` (:113) and
  `extract_unit_ids` (:119) give the unit ids a subject names. Attribution is the union of the
  subject's ids and the trailer's (that module's docstring).
- A unit id carries its build's slug, `<FAMILY>-<slug>-<n>` (`UNIT_RE`, `tools/roles/handoff.py:104`).

### The derivation

For a record `R` at path `P` carrying stored origin `o`:

1. `L`, the landing commit: `read_adding_commits(root, <records glob>, {P})[P]`, one call for every
   graded record.
2. The landing build: the build folder `P` sits in (`<memory root>/builds/<slug>/…`); for a record
   outside any build folder, the slugs of the unit ids `L` attributes.
3. The subject: `R`'s served unit ids, read by `read_bindings` (`tools/memory-tree/tree_lib.py:471`).
4. The subject's last change: the newest commit strictly before `L` on `L`'s first-parent line whose
   attribution names one of the served ids, from one `read_routed_commits` pass over `L^`. Its build
   is that id's slug.
5. The answer: `written` when step 4 finds no commit (the record is its subject's first change) or
   when step 4's build is a landing build; `not-written` otherwise.

| Stored `o` | Green when |
|---|---|
| `written` | step 5 answers `written` |
| `reconstructed@<sha8> <sources>` | step 5 answers `not-written`, `<sha8>` resolves to an ancestor of `L` or `L` itself, and each source path is a blob at `<sha8>` (`read_blobs_at`) |
| `imported:<path>` | step 5 answers `not-written`, `<path>` is a blob at `L^`, and `<path>` is outside the memory root |
| anything else | never: refused as a value I20 does not define |

A record whose served ids are none and whose stored value is `written` is red, `written with no
subject to derive from`, since nothing could make it so.

### The fixture plants

`python record_origin.py --fixture --plant <case>` builds a scratch repository under
`%TEMP%/ro-<case>`, a short path outside the worktree (a clone path under the session scratchpad is
too long on Windows), runs `--check` in it and prints its output and exit. `--selftest` runs every
case and compares each exit with the table.

| Case | Planted | Expected |
|---|---|---|
| `written-predates` | unit `TOOL-dOld-1` changed in a commit naming it; later a record under `memory/builds/dNew/build/` serving `TOOL-dOld-1`, stored `written`, landed by a commit naming `TOOL-dNew-1` | exit 1 naming the record, `stored written`, `derived not-written`, the dOld commit |
| `written-same-build` | the same record serving `TOOL-dNew-1`, last changed by a dNew commit | exit 0 |
| `reconstructed-ok` | stored `reconstructed@<sha8> notes.md`, `<sha8>` an ancestor holding `notes.md` | exit 0 |
| `reconstructed-unresolved` | `<sha8>` naming no commit | exit 1 |
| `imported-ok` | stored `imported:adr-1.md`, present at `L^` | exit 0 |
| `imported-memory` | stored `imported:memory/DECISIONS.md` | exit 1, a gov record is never an import |
| `reconstructed-but-written` | stored `reconstructed@…` on a record whose subject's last change is its own build | exit 1, stored differs |
| `unarmed` | no record carries an origin line | exit 0 and the `unarmed` line |
| `slices` | two records, one `reconstructed@…`, one with no line, then `gov_record.py find` and `show` | the rows carry `reconstructed@…` and `unrecorded`; each slice opens `origin <value>` |

### Inventory

| Minted | Kind | Lexicon cell |
|---|---|---|
| `record_origin.py` | file, `tools/memory-tree/` | none |
| `derive_origin`, `check_origin`, `origin_rank` | functions | `py.function`, asked at the pass |
| `--check`, `--rank`, `--of`, `--fixture --plant`, `--selftest` | flags of `record_origin.py` | `cli.flag`, asked at the pass |
| `record origin (stored origin against history)`, `record origin selftest` | legs | none |
| the `origin` key of `read_header_edges` | return key | none |
| `help/record-origin.md` | help page | none |

### Migration

None. Records landed before the door carry no line and render `unrecorded`; the first record the
door writes with a line arms the check.

### Rollout

Live at landing. The `record origin` leg prints `unarmed` until TOOL-dLinkedLibrary-8's door writes
the first origin line, and the selftest leg holds the red cases meanwhile.

### Files touched (estimate)

- `tools/memory-tree/record_origin.py` (new): S2, S3, S6, the plants
- `tools/memory-tree/tree_lib.py`: S1's `origin` key in `read_header_edges`
- `tools/memory-tree/record_find.py`: S5's row column and slice head line
- `tools/gate-legs.json`: S4's two legs
- `tools/memory-tree/README.md`: S7's section
- `help/record-origin.md` (new) and `help/README.md`: S7

### Alternatives rejected

- **Derive the origin and never store it.** The clause keeps a stored value and a check against it;
  a derived-only origin has nothing to disagree with, so a write path that types a wrong value would
  pass unseen.
- **A hygiene-check arm.** `check-memory-hygiene.sh` grades one tree; this check walks the commit
  graph, which is why it is a leg with `reads.history`, as `routed commits name a specced unit` is.
- **Ranking inside the digest.** A second spelling of the order would drift; S6 is the one order.

## 5. Production-readiness checklist

- security — read-only: git reads with argv lists, paths from `git ls-files` and record lines only;
  an `imported:` or source path is read as a blob name, never opened from the working tree.
- perf / scale — one `read_adding_commits` call, one `read_routed_commits` pass and one
  `read_blobs_at` batch per run, whatever the record count.
- error / empty / loading states — `unarmed` with its counts when no record is graded; exit 2 on a
  shallow clone or a failed git call, naming it; `unrecorded` in a slice for a record with no line.
- observability — one line per red record naming the deciding commit and build.
- risks — a records commit naming no unit id leaves the landing build to the record's folder; a
  record outside every build folder whose landing commit names no id is red as `no landing build`.
- testing — the nine plants, red and green, in the selftest leg.
- migration — none.
- user docs — `help/record-origin.md`, S7.

## 6. Acceptance criteria

- **AC1** — When `python record_origin.py --fixture --plant written-predates` runs, it prints one
  line naming the planted record with `stored written` and `derived not-written` and exits 1; with
  `--plant written-same-build` it exits 0.
  Red when: a record typed `written` whose subject last changed in an earlier build passes.
- **AC2** — When `--plant reconstructed-ok` runs it exits 0, and `--plant reconstructed-unresolved`
  exits 1 naming the unresolved `<sha8>`.
  Red when: a `reconstructed@` value whose commit names nothing passes.
- **AC3** — When `--plant imported-ok` runs it exits 0, and `--plant imported-memory` exits 1 naming
  `memory/DECISIONS.md`.
  Red when: a path under the memory root is accepted as an import.
- **AC4** — When `--plant reconstructed-but-written` runs, it exits 1 naming the stored value.
  Red when: the check reads only the `written` direction.
- **AC5** — When `python record_origin.py --check` runs in this repository before the door writes a
  line, it prints `origin — unarmed: 0 of <n> records carry an origin line` and exits 0, and
  `--plant unarmed` prints the same shape.
  Red when: an empty population prints a green line.
  figure: `<n>` is DERIVED at the run from the tracked records.
- **AC6** — When `python record_origin.py --rank reconstructed@abcdef12 notes.md imported:adr-1.md
  written` runs, it prints `written`, then `imported:adr-1.md`, then the `reconstructed@` value; an
  unknown value exits 2 naming it; and `--plant slices` runs `--of` over its two records, printing
  rank `2` for the `reconstructed@` record and `0` with `unrecorded` for the other.
  Red when: a `reconstructed` value ranks above a `written` one.
- **AC7** — When `--plant slices` runs `python gov_record.py find --build dNew` in its fixture, each
  row carries six fields, the fourth `reconstructed@<sha8> notes.md` or `unrecorded`.
  Red when: a row omits the origin field.
- **AC8** — When `--plant slices` runs `python gov_record.py show <key>` for each record, the first
  line of each slice reads `origin <value>`.
  Red when: a slice renders without its origin.
- **AC9** — When `grep -n "unrecorded" record-origin.md` runs over the help page, it finds the
  section naming the three values and the leg.
  Red when: the page is absent or omits a value.

## 7. Gates

`memory hygiene` · `memory-hygiene self-test` · `routed-commits selftest` · `policy fixtures` · `measure-legs selftest` · `run-gates canary` · `run-gates gov canary` · `spec tokens (a spec's own names resolve)` · `lexicon naming predicates`

The two legs S4 adds are not on the line above, since the leg join resolves a name against the
manifest at base, where neither exists yet; the arm line below declares them.

New arm: tools/memory-tree/record_origin.py --selftest (the `record origin selftest` leg) · covers AC1 AC2 AC3 AC4 AC5 AC6 AC7 AC8 · the nine plants of §4, the failing case a `written-predates` record the check passes, staged by making `derive_origin` answer `written` always · none

## 8. Open questions

- **F1 — What is a record's subject, whose last change the derivation reads?** Options: (a) the
  record's served unit ids, whose last attributed commit gives the build; (b) every product path the
  record cites; (c) a typed `Subject` field. (b) reads prose for paths and cannot tell a subject from
  a mention; (c) is a typed field beside a derived one, which retrofit.md:451 refuses. RESOLVED
  (agent, 2026-10-26, delegated): (a), rung 3, the most feature-rich survivor: it derives from the
  binding every record already carries and the attribution `routed_commits.py` already reads, and it
  decides the clause's planted case. widens: none · relaxes: none
- **F2 — Where does the check run?** Options: (a) its own leg with `reads.history`; (b) an arm of
  hygiene check 21 or another record check; (c) inside `record causes` (TOOL-dTotalRecall-19 S12).
  (b) grades the tree, not the graph; (c) puts two mechanisms behind one verdict. RESOLVED (agent,
  2026-10-26, delegated): (a), rung 3, by the tie-break: one mechanism per leg, shaped as the
  `routed commits name a specced unit` row is. widens: none · relaxes: none
- **F3 — What does a record with no origin line read as?** Options: (a) `unrecorded`, counted and
  shown, never red and ranked with `written`; (b) a dated backfill writing `written` on every landed
  record; (c) red. (b) types a value the clause derives; (c) reds every record landed before the
  door. RESOLVED (agent, 2026-10-26, delegated): (a), rung 3: it leaves no reconstructed record able
  to read as written, since the door writes every reconstructed record's line, and it never prints
  an empty population as green. widens: none · relaxes: none

## 9. Revision log

- rev-1 · 2026-10-26 · initial draft, from the packet's Items 9, retrofit.md `[origin]` :445-470,
  TOOL-dTotalRecall-2, -9 and -19, I20 and scout D's row for this unit.
- rev-2 · 2026-10-26 · §3 · the Edges block gains the bullets mirroring TOOL-dLinkedLibrary-37, TOOL-dLinkedLibrary-52, promoted from the round-1 spec audit of the 25 unit specs; nothing else moved.

## 10. Reuse audit

The seams extended are the one header reader `read_header_edges` (TOOL-dTotalRecall-19 S1), which
gains the `origin` key rather than a second reader of a record's head; the history readers
`read_adding_commits` and `read_blobs_at` (`tools/memory-tree/tree_lib.py:302`, :328) and the one
log pass `read_routed_commits` with `build_id_re` and `extract_unit_ids`
(`tools/memory-tree/routed_commits.py:228`, :113, :119), each verified at base by reading it; and
`record find` and `record show` (TOOL-dTotalRecall-9 S3, S5), whose row and slice gain the field.
`python tools/codebase-map/reuse_lookup.py "re-derive a record's origin from the commit history that
added it and compare with its stored field"` ranked name stems (`records`, `field`, `build_commit`,
`resolve_compare_base`, `read_records`); none derives a record's provenance, so no existing seam fits
the derivation and S2 adds it beside the readers it calls. Scout D's row named `Caused-by`
(TOOL-dTotalRecall-19) as the nearest precedent of a door-written field checked against history;
`record_origin.py` follows that unit's `record_causes.py` shape. The record and the source agree on
every cited line at base.

Recall terms used: `python tools/memory-recall/query.py "how is a record's origin derived from history and checked against its stored value" --terms "origin written reconstructed imported derived history landing build subject last-changing commit record door"`
