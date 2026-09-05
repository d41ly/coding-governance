# TOOL-aTunedCompass-8 — the map log records what a probe returned, not only that it ran

**Status:** BLOCKED · rev-4 · 2026-09-05 · node a · Tier-2 · base c4fcf5ad · streams tooling · order 3 · ratified 2026-09-05

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-09-05-review-TOOL-aTunedCompass-1-spec-audit-round1.md](../reviews/2026-09-05-review-TOOL-aTunedCompass-1-spec-audit-round1.md) | spec-audit | TOOL-aTunedCompass-1 TOOL-aTunedCompass-2 TOOL-aTunedCompass-3 TOOL-aTunedCompass-4 TOOL-aTunedCompass-5 TOOL-aTunedCompass-6 TOOL-aTunedCompass-7 TOOL-aTunedCompass-9 TOOL-aTunedCompass-10 TOOL-aTunedCompass-11 |

<!-- /gen:spec-records -->

## 1. Goal

Give the map half of the reuse obligation the evidence its recall half already has. The row
`tools/codebase-map/reuse_lookup.py` writes proves a probe RAN; it cannot show whether the probe
helped, because it never records what came back. Adding the returned paths makes the map half
measurable by the same method the parent build used on the recall half.

## 2. Scope (IN)

- **S1** — the log row gains `shown_paths`: the deduped, file-backed paths the answer told the reader
  to open, repo-relative and forward-slashed, in shortlist order.
- **S2** — the row gains `n_sources`: the count of those paths BEFORE the cap, so a truncated list is
  visible as truncated. `n_shown` keeps the meaning it has today, which is the ranked-candidate count
  and not a path count, and the field is not redefined.
- **S3** — one module constant caps the logged list, and `write_lookup`'s docstring states the cap,
  what it bounds, and the measured row sizes behind the number. §4 recommends 40 with its evidence.
- **S4** — the paths come from ONE derivation, shared with the renderer. A small pure helper returns
  the file-backed sources; the existing `_sources` labels them for the human, and `main` hands the
  same list to the writer. Nothing parses rendered output for paths.
- **S5** — the write stays NEVER FATAL. The new fields are computed and serialised inside the
  existing guard, so a lookup that cannot log still prints its answer and still exits 0.
- **S6** — a self-test arm in `tools/codebase-map/selftest.py` asserting the two new fields, the cap
  behaviour, and that a write failure does not change the exit code. The arm runs against a SCRATCH
  repository with the map root redirected by environment variable — a working-directory change is
  NOT sufficient, because the kit resolves its root from the kit directory, and an arm that writes
  into this tree's own log manufactures the very evidence a reader of that log would count.
- **S7** — the kit version marker moves, because this is an engine change, and
  `memory/map/features/codebase-map.md` is refreshed to describe the row this kit now writes.
- **S8** — nothing in the change names another kit by literal. The row grammar this kit already
  borrowed stays borrowed by SHAPE, and no sibling path is read, written or spelled.

## 3. Non-goals (OUT)

- **No attributed-open analogue for the map, and this is the largest deliberate cut.** Recall's
  attribution is written by a hook, `tools/memory-recall/recall-opened.js`, so a map equivalent is a
  hooks-kit change plus a second attribution convention, not a field on an existing row. It is also
  aimed at a signal that is itself under repair: the parent report measured that signal as one row
  per query, first read only, inside a 30-minute window and flagged `inferred` by its own author at
  `tools/memory-recall/recall-opened.js` (`:25`), and concluded its numbers are a hint rather than a
  miss rate. Building a map analogue on that shape means building it twice. The backlog already
  carries the enrichment of the recall signal; the map analogue follows it, not this unit.
- Not a reader. This unit writes the field. Whether anything reads the log, and where, is F1.
- Not a change to what the probe returns or how it ranks. The neighbour pool truncated before
  ranking at `tools/codebase-map/reuse_lookup.py` (`:243`) is `TOOL-aTunedCompass-6`, and the
  private-symbol exclusion is a backlog row that needs its own measurement first. If both landed in
  one pass, no later analysis could tell a ranking change from a logging change. That is why this
  unit carries `order 3` against that unit's `order 1`: they are two passes, not one parallel group.
- Not logging the rendered answer, its byte count, or its snippet text. The parent measured a mean
  of 10782 bytes of output per probe; storing that is a corpus, not a telemetry row.
- Not tracking the log, moving it out of the git common directory, or rotating it.

## 4. Design

### What the row carries today, measured at writing time

`tools/codebase-map/reuse_lookup.py` (`:417`) writes `{type, at, query, worktree, n_shown}` to the
kit's own file under the git common directory, and `main` (`:478`) passes `len(shortlist.ranked)` as
`n_shown`. So the count in the row is the RANKED CANDIDATE count, which is not the number of paths a
reader was pointed at. Measured over the live log today: 472 rows, 120234 bytes, mean row 254.7
bytes, longest row 308. Excluding this worktree's own 416 research probes, the 56 rows other sessions
wrote carry `n_shown` at mean 70.8, median 69, maximum 188, minimum 18. The row count differs from
the parent report's 399 for the reason that report declared about its own perturbation: this research
appends to the log it measures.

The comparator is the recall query log, whose rows carry a `results` array of set, id, path and line
per slot. Measured the same way today: 248 rows, mean row 2150.6 bytes, median 2980.5, maximum 4113.
That is the shape section 1 of the parent report derives from, and the map row cannot answer any of
those questions.

### What `shown_paths` is, precisely

The population is the file-backed sources `_sources` (`:356`) already computes: a symbol candidate
contributes its definition file, a dossier candidate contributes its dossier, and an inventory key
with no file contributes nothing. Deduped, in shortlist order, which is the order the reader sees.

That set is a superset of the parent report's grading population, which counted product paths only
and measured mean 17.3 and 17.4 per probe against its two independent ground truths. Dossier paths
are kept rather than filtered, because a reader can filter by prefix and a writer that pre-filters
has thrown the evidence away. The precision figure the same report gives — 0.056, about one useful
path in eighteen — is exactly the quantity this field makes computable per probe rather than only in
a research harness.

### The size bound, in three parts

1. **The list is the deduped SOURCE set, not the ranked candidates.** Measured above, that is a mean
   of about 17 paths against a mean of about 71 ranked entries — roughly a quarter of the naive
   choice.
2. **A module constant caps it.** Recommended value 40: comfortably above the measured mean, below
   the 188-candidate outlier, and cheap to raise because `n_sources` records what was cut.
3. **The result stays well under the comparator.** At a nominal 40 bytes per path, 17 paths add about
   700 bytes to today's 255-byte row, and a capped worst case adds about 1.6 KB. The recall log
   already runs at a 2150-byte mean row and nobody has called it expensive.

### Where it is written

Inside the existing guarded block, after the answer is rendered, exactly as the row is written today.
The ordering is deliberate in the current code and it survives: a row means a lookup that ANSWERED,
so a crash in the renderer leaves no evidence of a probe whose result nobody saw.

**Which path the log resolves to, stated because AC4 turns on it.** `_resolve_git_dir`
(`tools/codebase-map/reuse_lookup.py` `:392`-`:404`) is pure path math over `root/.git` plus the
`commondir` file, with an explicit "NO child process" docstring, and `root` is `m.repo_root()`, which
reads `CODEBASE_MAP_ROOT` alone (`tools/codebase-map/map_lib.py` `:113`-`:119`). `GIT_DIR` appears
nowhere under `tools/codebase-map/`. So the only lever that moves the log's location is
`CODEBASE_MAP_ROOT`, and an arm that tried to disable the writer through the git environment would
leave the writer pointed at the real common directory and APPEND to the live corpus it was written to
protect.

### Data model

| Field | Kind | Meaning |
|---|---|---|
| `type` | string | unchanged, the row discriminator a reader filters on first |
| `at` · `query` · `worktree` | unchanged | unchanged |
| `n_shown` | int | unchanged — the RANKED candidate count, not a path count |
| `n_sources` | int | the deduped file-backed source count, before the cap |
| `shown_paths` | list of strings | those paths, in shortlist order, truncated at the cap |

Old rows carry neither new field. A reader treats their absence as UNKNOWN and never as zero, and the
dossier says so, because a zero would read as "the probe pointed at nothing".

### Files touched (estimate)

`tools/codebase-map/reuse_lookup.py`, `tools/codebase-map/map_lib.py` for the version marker,
`tools/codebase-map/selftest.py`, and `memory/map/features/codebase-map.md`. Four files.

### Alternatives rejected

- **Logging the ranked candidate names instead of the source paths.** The unit of every analysis this
  field exists to enable is the PATH — both of the parent's ground truths are path sets — and the
  ranked list is about four times larger for an answer that still needs a second join to a file.
- **Parsing the rendered output for paths.** Two readers of one value, and the render is formatted
  for a human console whose layout is free to change.
- **Writing into the recall kit's log.** Already rejected by the unit that landed this logger,
  because it makes this kit depend on a convention neither kit's descriptor declares.
- **A shared telemetry module under the tools library.** Rejected by that same unit: every
  copy-installed kit carries library contents inline, so a shared module becomes two copies plus a
  parity gate — three mechanisms where two small appenders are one.
- **Redefining `n_shown` to mean the path count.** It would silently change the meaning of 472
  existing rows, and a field whose meaning changed mid-log is worse than a field that was never
  there.

## 5. Production-readiness checklist

- security — the row records repo-relative paths drawn from this repo's own committed map corpus. No
  new external input, and the log stays untracked inside the git common directory.
- perf / scale — one append per lookup, on a tool a session runs a handful of times. The log has
  grown 120234 bytes across 472 rows; this change roughly quadruples the row and leaves it at about a
  third of the recall log's mean row.
- a11y — N/A. No user-facing surface.
- i18n — N/A. Paths are ASCII repo-relative strings and the writer already forces newline handling.
- error / empty / loading states — an empty shortlist logs an empty list and `n_sources` zero, which
  is distinguishable from an old row that carries neither field. A failure to locate or write the log
  warns on stderr and the answer still prints.
- observability — this unit IS the observability change. What it still cannot see is whether the
  session READ any path it logged; that gap is §3's cut and is named there rather than implied away.
- risks — the log is shared by every worktree of this repo through the common directory, so any
  analysis must filter on `worktree` first. The parent had to exclude 366 of 399 rows on exactly that
  basis. F2 asks whether the row should carry more attribution than that.
- testing + left-shift gates — S6, with the failing case observed before the arm is written, and with
  the scratch-repo redirect that keeps the suite from writing into the log a reader would count.
- migration / rollback — purely additive. Removing the fields later leaves old rows readable, and
  every reader must already tolerate their absence.
- user docs — the kit's own README and `memory/map/features/codebase-map.md`. No `help/` page: this
  is agent-facing telemetry, not a user-facing feature.

## 6. Acceptance criteria

- **AC1** — When `python tools/codebase-map/reuse_lookup.py "<phrase>"` is run, exactly one row is
  appended to the kit's `lookups.jsonl`, and that row carries `shown_paths` and `n_sources` alongside
  the five fields it carries today. Observed by reading the file before and after.
- **AC2** — When a probe whose answer names more sources than the cap is run, the row's
  `shown_paths` length equals the cap constant and `n_sources` is strictly greater than it.
- **AC3** — When the same query's rendered output is compared with its row, every entry in
  `shown_paths` appears in the command's own `## sources to open` block, is repo-relative, and uses
  forward slashes.
- **AC4** — When the command is run with `CODEBASE_MAP_ROOT` pointed at a scratch tree holding no
  `.git` (or whose `.git` file names a missing gitdir), it still prints its candidates and exits 0,
  no row is written anywhere, and this repository's own `lookups.jsonl` is byte-unchanged across the
  run. The environment variable is named deliberately: the resolution is `root/.git` plus
  `commondir`, and `GIT_DIR` reaches none of it — see §4.
- **AC5** — When `python tools/codebase-map/selftest.py` runs, the new arm passes, and the real
  log's hash is unchanged by the suite run — the arm wrote into its scratch repository, not this one.
- **AC6** — When `bash tools/check-install-prefix.sh` runs, it stays green: the diff adds no sibling
  kit path literal to `tools/codebase-map/reuse_lookup.py`.
- **AC7** — When `bash tools/check-kit-versions.sh` runs, it exits 0 with the codebase-map marker in
  `tools/codebase-map/map_lib.py` advanced by this change.
- **AC8** — When `memory/map/features/codebase-map.md` is read, it names both new fields, states that
  their absence on an older row means unknown rather than zero, and
  `python tools/codebase-map/test_codebase_map.py` exits 0.
- **AC9** — When the new helper's name is checked with `python tools/lexicon/lexicon.py --suggest`,
  the name shipped is one the declared verb table admits, and `lexicon naming predicates` stays
  green.

## 7. Gates

`codebase-map kit selftest` · `codebase-map coverage + freshness` · `kit version markers`
`install-prefix (shipped surface)` · `lexicon naming predicates` · `memory hygiene`

The full bar is `bash tools/run-gates/run-gates.sh`. This unit adds no merge-bar leg. S6's arm lands
in a suite whose subject is the KIT, and this repo's standing ruling holds those off the default bar,
so it runs on demand with the self-tests enabled. That is the ruling, not an exemption this unit
invents, and it is stated here so a green bar is not read as having exercised the new arm.

## 8. Open questions


**F1 RESOLVED (owner, 2026-09-05): land the missing run-state reader first.** The owner did not take this
fork's recommendation of shipping the field with no reader. That reader is now
`TOOL-aTunedCompass-11`, a unit of this build, and this unit is BLOCKED on it and sequenced after it.
The field lands against a reader that exists, so the log is never a write-only surface.

**F2 RESOLVED (owner, 2026-09-05): add no extra attribution now, and record the deferral.** The owner chose
to wait until an analysis needs it rather than decline it, so a backlog row is owed rather than
silence. That row carries the cost this fork named: adding a field later is a second migration of a
log that has no schema, and the row exists so that cost is a planned one.

- **F1 — does this log need a reader, and if so where?** Three pieces of evidence, and they do not
  all point the same way. First, the recall log accumulated 219 rows over a month before anybody read
  it, and the parent report's entire first section exists because somebody finally did — a log with
  no reader is not obviously worthless, but it is provably not consulted. Second, the "on the bar"
  half already has a recorded answer AGAINST: the unattended run's `reuse-probed` item reads the
  recall log and its own header at `tools/unattended/unattended.sh` (`:3588`) says why it is not a
  merge-bar leg — the evidence lives in the git common directory, is neither tracked nor pushed, and
  a leg could only ever report a dead probe in a fresh clone. Third, and measured at writing time:
  the map log has NO reader anywhere in the product. `git grep MAP_CLI` returns nothing outside the
  build records, and that item's join reads the recall log alone, although the CLOSED unit that
  landed this logger carries a scope item for exactly that reader and an acceptance-ledger line
  claiming a key-table join accepted it.
  Options: ship the field with no reader and treat the log as a substrate for periodic analysis; land
  the missing run-state reader first and gate this field behind it; or ship a small analysis script
  inside the kit that nothing invokes automatically.
  Recommendation: the first, because the reader that was specced belongs to the unit that specced it
  and re-scoping it here would hide a record defect inside an unrelated diff. The record defect
  itself is owed as a backlog row rather than a third document in this build's records unit, whose
  scope is two documents by the build's own rule.
  Left open: whether a write with no reader is acceptable is a standing question about this repo's
  telemetry, not a fact this unit can measure.

- **F2 — should the row carry attribution beyond `worktree`?** An analysis cannot today tell which
  build or unit a probe was run for. The parent had to exclude 366 of 399 rows by worktree, and the
  existing run-state reader states plainly that it cannot tell whether a probe ran for THIS build or
  earlier in the same worktree. Options: add the branch name; add nothing and leave attribution to
  the analysis; wait until an analysis actually needs it.
  Recommendation: add nothing here. It is a second question, a second field and a second privacy
  surface, and the field this unit adds is worth having on its own. Recorded rather than decided,
  because the cost of adding it later is a second migration of a log that has no schema.

## 9. Revision log

- rev-1 · 2026-09-04 · initial draft, authored by the aTunedCompass spec pass.
- rev-2 · 2026-09-05 · M2 cross-read, ordering axis. §3 requires this unit and
  `TOOL-aTunedCompass-6` not to land in one pass, while the header carried `order 1` — the same
  value that unit carries, which `memory/TEMPLATE-SPEC.md` defines as the parallel group. The header
  was the half that disagreed with the body, so the order moves to 2 and §3 says why.
- rev-3 · 2026-09-05 · both forks resolved by the owner. The unit is BLOCKED on the new
  `TOOL-aTunedCompass-11` and moves to order 3; the extra attribution is deferred to a backlog row
  rather than declined.
- rev-4 · 2026-09-05 · round-1 spec audit folded, findings H5 and L1. AC4 named `GIT_DIR`, which
  reaches nothing under this kit: the log path is `CODEBASE_MAP_ROOT` -> `root/.git` -> `commondir`,
  so the criterion could not fail for the reason it gave and running it would have appended a row to
  the live log AC5 exists to protect. AC4 now drives the real lever and asserts the corpus is
  byte-unchanged, and §4 states the resolution. §3 still read `order 2` after rev-3 moved the header
  to 3; the body follows the header.

## 10. Reuse audit

`python tools/codebase-map/reuse_lookup.py "record which paths a reuse probe returned in its own
append-only jsonl log row"` returned 147 candidates and did NOT name the function this unit edits.
`log_event`, the recall kit's writer, came back at position 54; `test_reuse_lookup` in the kit's own
self-test came back at 92; `tools/codebase-map/reuse_lookup.py` itself appears in the sources list
only because two of its dataclasses were pulled in as same-kind neighbours. `write_lookup` was never
returned. So no probe-named seam fits, and the seam this unit extends was found by reading the file:
the writer at `tools/codebase-map/reuse_lookup.py` (`:417`) and the source derivation at (`:356`),
which already computes the exact list S1 wants and today throws it away after rendering. That miss is
itself an instance of the parent report's finding that the probe's precision is about one useful path
in eighteen, and it is why this unit's design was read rather than probed.

Recall terms used: `reuse_lookup lookups.jsonl telemetry row grammar n_shown recall queries.jsonl
opened attributed liveness efficacy codebase-map`. The question was why the map lookup log records
only that a probe ran and not which paths it returned. It returned 40 hits, and the ones that bind
are the backlog row naming this exact gap, the row recording that the map log's own liveness claim
was stale in the opposite direction, and the CLOSED spec that landed the logger — whose rejected
alternatives are quoted in §4 rather than re-derived, and whose scratch-repo requirement for the
self-test is S6.
