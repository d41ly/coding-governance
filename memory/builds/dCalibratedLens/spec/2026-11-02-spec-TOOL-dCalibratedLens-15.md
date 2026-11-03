# TOOL-dCalibratedLens-15 — each size breach priced by its bytes and its reads, and a persisting or grown breach raised to the owner

**Status:** DEFERRED · rev-2 · 2026-11-02 · node a · Tier-2 · base 8bec4cef · streams tooling · order 6 · advances TOOL-dCalibratedLens-18

**Carries:** cl-dClosedLoop-0472@bf8d8ee5 whole

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-11-02-build-TOOL-dCalibratedLens-15-deviation-152.md](../build/2026-11-02-build-TOOL-dCalibratedLens-15-deviation-152.md) | deviation | — |
| [2026-11-02-prompt-TOOL-dCalibratedLens-1-edge-fix-brief.md](../prompts/2026-11-02-prompt-TOOL-dCalibratedLens-1-edge-fix-brief.md) | research | TOOL-dCalibratedLens-1 TOOL-dCalibratedLens-2 TOOL-dCalibratedLens-3 |
| [2026-11-02-prompt-TOOL-dCalibratedLens-1-spec-brief.md](../prompts/2026-11-02-prompt-TOOL-dCalibratedLens-1-spec-brief.md) | research | TOOL-dCalibratedLens-1 TOOL-dCalibratedLens-2 TOOL-dCalibratedLens-3 TOOL-dCalibratedLens-4 TOOL-dCalibratedLens-5 TOOL-dCalibratedLens-6 TOOL-dCalibratedLens-7 TOOL-dCalibratedLens-8 TOOL-dCalibratedLens-9 TOOL-dCalibratedLens-10 TOOL-dCalibratedLens-11 TOOL-dCalibratedLens-12 TOOL-dCalibratedLens-13 TOOL-dCalibratedLens-14 TOOL-dCalibratedLens-16 TOOL-dCalibratedLens-17 |
| [2026-11-03-prompt-TOOL-dCalibratedLens-1-departures-brief.md](../prompts/2026-11-03-prompt-TOOL-dCalibratedLens-1-departures-brief.md) | research | TOOL-dCalibratedLens-1 TOOL-dCalibratedLens-2 TOOL-dCalibratedLens-3 TOOL-dCalibratedLens-4 TOOL-dCalibratedLens-5 TOOL-dCalibratedLens-6 TOOL-dCalibratedLens-7 TOOL-dCalibratedLens-8 TOOL-dCalibratedLens-9 TOOL-dCalibratedLens-10 TOOL-dCalibratedLens-11 TOOL-dCalibratedLens-12 TOOL-dCalibratedLens-13 TOOL-dCalibratedLens-14 TOOL-dCalibratedLens-16 TOOL-dCalibratedLens-17 TOOL-dCalibratedLens-21 TOOL-dCalibratedLens-23 TOOL-dCalibratedLens-25 TOOL-dCalibratedLens-29 |
| [2026-11-02-review-TOOL-dCalibratedLens-1-spec-audit.md](../reviews/2026-11-02-review-TOOL-dCalibratedLens-1-spec-audit.md) | spec-audit | TOOL-dCalibratedLens-2 TOOL-dCalibratedLens-3 TOOL-dCalibratedLens-7 TOOL-dCalibratedLens-9 TOOL-dCalibratedLens-12 TOOL-dCalibratedLens-4 TOOL-dCalibratedLens-6 TOOL-dCalibratedLens-16 TOOL-dCalibratedLens-17 TOOL-dCalibratedLens-5 TOOL-dCalibratedLens-10 TOOL-dCalibratedLens-11 TOOL-dCalibratedLens-8 TOOL-dCalibratedLens-13 TOOL-dCalibratedLens-1 TOOL-dCalibratedLens-14 |

<!-- /gen:spec-records -->

## 1. Goal

Caps are advisory under `budgets.enforce` (dGroundRules), and a warning nobody acts on is no brake:
"a cap's breach is priced nowhere and trended nowhere" (gap-review-19). The owner's NT-23, "Shown,
priced, trended", splits the brake in four (night pass two, point 5, part 4): dWitnessedBar shows each
size warning in the runner's summary and verdict record, attributed to the unit that grew the file
(TOOL-dWitnessedBar-29); this unit prices each breach in the value ledger as its bytes times its reads
(research-caps, pick B), and makes the Loop Review raise an owner item for a breach that persists or
grows across reviews, counting only new or grown breaches, so the warnings never turn into noise.

## 2. Scope (IN)

Build-run preconditions, each specced and unbuilt at base `8bec4cef`, re-grounded by the build run,
which stops this unit when one is absent: TOOL-dCalibratedLens-2 (the module, `PROVIDERS`, the row
grammar, `price`), TOOL-dCalibratedLens-3 (`METRICS`, the walk `run_loop_walk`, `run_loop_file` and
its proposal shape, the record and its home, and the window), the `warned` and `warn.<k>` verdict keys
(TOOL-dWitnessedBar-29 S7) and the `tree` key (TOOL-dWitnessedBar-4 S1). The verdict record's
directory, its `ended`, `verdict`, `skipped` and `reused` keys, and runlog's transcript walker are built
at base and cited where used.

- **S1** — (amended, id 22) The breaches read. `read_verdict_warnings(root, window)` in `tools/loop/loop_review.py`
  reads the `verdict` file of every run directory under each git dir of the clone, the common dir's
  `gate-run/` and each `worktrees/<name>/gate-run/` (the runner's `RUNROOT="$gd/gate-run"`,
  `tools/run-gates/run-gates.sh:2721`, `gd` the worktree's `--git-dir`, `:114-116`), and takes the
  newest record whose `ended` lies in the window, whose `verdict` is `GREEN` or `RED`, and whose
  `skipped` and `reused` read `0` (`:5675-5681`): a full run, every leg executed, so every size
  warning was printed. From it, each `warn.<k>` value of class `size`, split on TAB as
  TOOL-dWitnessedBar-29 §4 states, gives a breach: leg, subject and growing unit. With no such record
  it returns the reason, and the review prices no `cap` row and decides no trend (§4 "No full run").
  Observed by AC1 and AC2.
- **S2** — Bytes. Each breach's bytes are `git cat-file -s <tree>:<subject>`, `<tree>` the record's
  `tree` key, else the review's base where the key reads `-` or names no local object. A subject absent
  from that tree is no breach and is dropped with one `ledger — cap · <subject> · absent at <tree8>`
  line. Observed by AC3.
- **S3** — Reads, the producer the brief found missing. `python runlog.py reads --since <epoch>
  [--transcripts <dir>] [--entry <path>]... <subject>...`, a new verb of `tools/runlog/runlog.py`,
  calls `measure_subject_reads(root, repo_key, subjects, since, entry)` in `tools/runlog/extract.py`,
  beside `measure_ready_tree` (`:1204`) and walking the projects root as it does, through
  `build_session_tree` (`:238`) and `read_records` (`:308`). It prints one `<subject>\t<n>` line per
  subject on stdout and one `runlog: reads · <files> transcript file(s) since <iso>` line on stderr,
  per §4 "Reads". Nothing of a transcript is printed but the counts: the subjects are the caller's.
  The loop kit runs it as a bounded subprocess (120 s) through `resolve_kit_dir`; a refused run leaves
  every breach's reads `-`. Observed by AC4 and AC5.
- **S4** — One read per review. `read_cap_breaches(root, window)` runs S1 to S3 once and is cached for
  the process by its arguments (`functools.lru_cache`), so the gather metrics, the provider and the
  raises, which the walk runs in one process (TOOL-dCalibratedLens-3 S2), read the node once.
  Observed by AC6.
- **S5** — The provider, `PROVIDERS`' `cap` entry. `derive_cap_rows(root, window)` reads S4 and
  returns `(rows, events)` in TOOL-dCalibratedLens-2's provider shape, as §4 "The rows" states: one row
  per breached subject, its `cost` `<bytes times reads>B/<reads>` or `-`, its `catches` `-`, and no
  event. Observed by AC6.
- **S6** — (amended, ids 10, 30, 46) The trend. `read_previous_breaches(root, key)` reads the newest committed `loop-review`
  record other than this period's, the record the newest first-parent commit of `HEAD` touching
  `<MEMORY_ROOT>/loop-review/` added, through `git show` and never the working tree, and parses its
  `cap-breaches:` Metrics line; a record whose line reads `searched-none` is skipped back to the newest
  that decided. `derive_cap_trends(breaches, previous)`, a pure function, gives each breach `new` where
  the previous line names no breach of the subject, `grown` where this review's bytes exceed its bytes,
  else `held`; and each subject the previous line names and this review does not, `cleared`. Observed
  by AC7.
- **S7** — The raise, counting only new or grown breaches. `derive_cap_raises(trends, previous)`
  returns every `grown` breach, and every `held` breach whose previous trend was `new`, its first
  persistence. A `held` breach already raised, a `new` one and a `cleared` one raise nothing.
  `run_loop_walk` extends the proposals it hands `run_loop_file` (TOOL-dCalibratedLens-3 S7) with one
  per raise: `{"kind": "cap", "id": <subject>, "action": "raise", "accept": "<subject> back under its
  cap, or the cap moved by the owner through the guarded policy command", "row": <the subject's cap
  row>}`. `run_loop_file`'s key hash of `cap\t<subject>` files the first raise and appends a `seen`
  receipt to the open intake for a later one, so one subject never has two owner items. A raise is
  handed on whatever the retirement policy key holds (§8 F4). Observed by AC8 and AC9.
- **S8** — The metrics. `METRICS` (TOOL-dCalibratedLens-3 S5) gains two entries, each answering
  `(value, source)` from S4, S6 and S7, written as the record's Metrics lines per §4 "The metrics":
  `cap-breaches`, each breach's subject, bytes, reads and trend, and the cleared subjects; and
  `cap-counted`, the new and grown counts. Under "No full run" both answer `searched-none` with the
  reason. Observed by AC2 and AC9.
- **S9** — The docs. `tools/loop/README.md`, `help/loop-review.md` (TOOL-dCalibratedLens-2 S12) and
  `tools/runlog/README.md` (the `reads` verb) each state what is read, how a breach is priced and when
  one is raised, and that the reach is the lease holder's node. NOT OBSERVED by a criterion: prose, read
  by the closing review.

## 3. Non-goals (OUT)

- Showing and attributing the warning: TOOL-dWitnessedBar-29's runner, which this unit reads.
- Any cap's value or mode: `budgets.*` and `budgets.enforce` are dGroundRules', and a cap re-derived
  from evidence is TOOL-dCalibratedLens-4's. A raise asks the owner for a trim or a cap move and writes
  no policy value.
- The view, its grammar, `price`, `run_loop_file`'s keyed filing and the record grammar:
  TOOL-dCalibratedLens-2's and -3's. This unit adds a `PROVIDERS` entry, two `METRICS` entries and the
  raises the walk hands `run_loop_file`.
- Proposing a `cap` row's retirement: the row carries no catch (§8 F3), and a breach leaves the ledger
  by clearing, never by `propose`.
- Breaches and reads on another node. The verdict records live in the git dir and the transcripts
  under the user profile, both node-local, so the review reads the lease holder's node, the reach
  v2:1345 states for the journal; a cross-node breach record is the persistence no build owns.
- Reads by a rule file the harness loads on a path match (`.claude/rules/`), and by a Skill's
  injection: neither is a `Read` call nor an entry import, and both count as no read (`ponytail:`
  ceiling; a load-set read per act is the upgrade once a work order records its loads).

### Edges

- **consumes-from** `TOOL-dCalibratedLens-2` — `PROVIDERS`, which gains the `cap` entry, the provider shape and the `-` catches rule
- **consumes-from** `TOOL-dCalibratedLens-3` — `METRICS`, which gains `cap-breaches` and `cap-counted`; `run_loop_walk` and the proposal shape `run_loop_file` reads; the record's Metrics lines and its home
- **hands-off** `TOOL-dCalibratedLens-4` — the `kind=cap` rows of the value ledger, each breach priced by its bytes and its reads in the `cost` column
- **consumes-from** external — TOOL-dWitnessedBar-29 (the `warn.<k>` verdict keys) and TOOL-dWitnessedBar-4 (the `tree` key), DEFERRED at base and of an ancestor build
- **hands-off** `TOOL-dCalibratedLens-30` — `read_previous_breaches` over `read_loop_records`, which the minors batch's `keep-after-review` arm runs (ids 10, 46)

## 4. Design

### The flow

```
run_loop_walk, one process
  read_cap_breaches (cached)
    read_verdict_warnings  -> newest full run in the window: warn.<k> rows of class size
    bytes                  -> git cat-file -s <tree>:<subject>
    runlog.py reads        -> <subject> TAB <n>, the lease holder's transcripts since the window's start
  loop.gather  METRICS cap-breaches, cap-counted  <- read_previous_breaches, derive_cap_trends
  loop.price   PROVIDERS["cap"] = derive_cap_rows
  loop.file    proposals + derive_cap_raises -> run_loop_file, keyed cap TAB <subject>
```

### The rows

| Column | Value for one breached subject |
|---|---|
| `kind` | `cap` |
| `id` | the subject, a repository-relative path |
| `since` | the date of the oldest record in the run of consecutive decided records naming the subject, read back through `read_previous_breaches`, else this review's date |
| `cost` | `<bytes times reads>B/<reads>`, or `-` where reads is `-` |
| `catches` | `-`, so `derive_ledger_rows` keeps `-` in all three catch columns |

Bytes are the document's whole size, since a reader pays the whole document on each read; the cap is
the owner's affordance and the breach is what makes the cost visible.

### Reads

A read of a subject is one of:

- a `tool_use` block named `Read` or `NotebookRead` whose `file_path` or `notebook_path`, with every
  `\` folded to `/`, equals the subject or ends with `/<subject>`, in a record at or after `--since`;
- for a subject given as `--entry`, one per transcript file, a session's main file or one of its
  `agent-*.jsonl` files, whose first record is at or after `--since`, since the harness injects the
  entry files into each.

The loop kit passes `--entry CLAUDE.md` and one `--entry` per `@<path>` line of `CLAUDE.md` at the
review's base (`CLAUDE.md:1` imports `AGENTS.md` at base). The transcripts walked are those under
`<projects root>/<key>/` whose `<key>` begins with the main checkout's repository key, from
`resolve_projects_root` (`tools/runlog/extract.py:185`) and `resolve_repo_key` (`:230`), so every
worktree of the clone counts (`ponytail:` a sibling repository whose path extends this one's is
counted too; matching the key to `git worktree list` is the upgrade).

### The metrics

```
cap-breaches: memory/guides/BUILD-METHOD.md 29326B 41r grown, AGENTS.md 20912B 212r held, skills/session-kickoff/SKILL.md cleared · gate-run <run id> on <node>
cap-counted: 0 new, 1 grown · gate-run <run id> on <node>
cap-breaches: searched-none · no full run on <node> in 2026-09-03..2026-11-02
```

One Metrics line per entry, the shape TOOL-dCalibratedLens-3 §4 "The record" gives. Each breach is
`<subject> <bytes>B <reads>r <trend>`, `-r` where reads is `-`; a cleared subject is `<subject>
cleared`. A subject carrying a space or a comma is refused at the write boundary, with the line break
the writer already refuses, so the line splits back without quoting. `cap-counted:` is the clause's
count, new and grown breaches only, so a review whose breaches all hold reads `0 new, 0 grown`. The
raises appear in the record's Filed lines, `cap <subject>: filed|seen`, which `run_loop_file` already
writes. The figures in the sample are illustrative and DERIVED at each review.

### No full run

A window whose node ran no full bar, every leg executed, has no complete warning set: a skipped,
held or reused leg prints no marker (TOOL-dWitnessedBar-29 S3), so its breach would read as cleared
and then as new. The review then answers `searched-none` and decides no trend, rather than clearing
what it could not see; the next decided review compares against the last decided one.

### Inventory

Minted: the functions `read_verdict_warnings`, `read_cap_breaches`, `derive_cap_rows`,
`read_previous_breaches`, `derive_cap_trends` and `derive_cap_raises` in `tools/loop/loop_review.py`,
and `measure_subject_reads` in `tools/runlog/extract.py`, each answered OK by `python
tools/lexicon/lexicon.py --suggest <name> --as py.function` at this base (`count_subject_reads` was
refused for `measure`); the `reads` verb of `runlog.py`; the `PROVIDERS` key `cap`; the `METRICS`
entries `cap-breaches` and `cap-counted`; the cost unit `B`; the proposal action `raise`; the trend words
`new`, `grown`, `held` and `cleared`; the output lines `ledger — cap · …`.

### Migration

None: at base no verdict record carries a `warn.<k>` key and no `loop-review` record exists, so the
first decided review reads every breach `new` and raises none.

### Amendments (round-1 spec audit)

The round-1 spec audit
(`reviews/2026-11-02-review-TOOL-dCalibratedLens-1-spec-audit.md`) confirmed the
findings below on this spec, and its disposal amended this text. Each bullet supersedes the text it
names; the unit it names owns the finding and its proof.

- **id 49 · §4 "The metrics" (H9, `TOOL-dCalibratedLens-27`)** — A subject carrying a space or a
  comma is skipped from `cap-breaches` with one
  `ledger — cap · <subject> · skipped · unsplittable subject` line, never refused at the write
  boundary, so one such path cannot stop the period.
- **id 10 · S6, AC7 (M6, `TOOL-dCalibratedLens-30`)** — The previous record is the newest committed
  `*-loop-review-*.md` other than this period's, read through `read_loop_records`
  (TOOL-dCalibratedLens-3 S8 as amended), never the record the newest commit touching the folder
  added, which may have added only a keep or a snapshot. AC7 also plants a keep committed after the
  previous review, and the trend still reads that review.
- **id 46 · S6 (M6, `TOOL-dCalibratedLens-30`)** — The same defect, raised by a second lens: it
  closes with id 10's rule.
- **id 30 · S6 (M14, `TOOL-dCalibratedLens-30`)** — `read_previous_breaches` keeps only its
  `cap-breaches:` line parser over `read_loop_records` and `read_metrics_lines`.
- **id 22 · S1, §4 "No full run" (L7, `TOOL-dCalibratedLens-30`)** — A full run is one where every
  leg of subject `repo` executed: legs are held only when of subject `kit` or chunk `selftests`
  (`run-gates.sh:3249-3251`), and `read_verdict_warnings` answers `unread` when a leg emitting class
  `size` warnings has subject `kit` or chunk `selftests`, so a held size leg can never read as
  cleared.
- **id 34 · §10 (L10, `TOOL-dCalibratedLens-30`)** — §10's precedent for S1's walk is
  `read_git_dirs` (`tools/drift-audit/drift_report.py:3114`, its glob at `:3133-3134`), carried
  inline with the same order, the common dir then the sorted `worktrees/` dirs, and the same empty
  case.
- **id 39 · Files touched (M19, `TOOL-dCalibratedLens-30`)** — Every `loop_review.py` verb or flag
  this unit adds to `help/loop-review.md` gets its `[[usage]]` row in `tools/govkit/usage.toml`, and
  the page's `<!-- usage: … -->` anchor is re-fingerprinted, so
  `python tools/govkit/docs_leg.py --list` names it and the `docs` leg reads no `UNROWED` line.

### Files touched (estimate)

- `tools/loop/loop_review.py` (S1, S2, S4 to S8, and the `--fixture` cases of §7)
- `tools/loop/README.md` (S9)
- `tools/runlog/runlog.py` (S3)
- `tools/runlog/extract.py` (S3)
- `tools/runlog/selftest.py` (the arm in §7)
- `tools/runlog/README.md` (S9)
- `help/loop-review.md` (S9, TOOL-dCalibratedLens-2's page)
- `tools/govkit/usage.toml` — the `[[usage]]` row of each verb or flag added (id 39)

### Alternatives rejected

- **Re-measuring every census cap at the review.** `tools/policy/caps.toml` names each cap's enforcer
  and no subject, so the review would re-run each enforcer's measurement, a second copy of each.
- **The union of every verdict record in the window.** A scoped run omits legs, so the union cannot
  tell a cleared breach from an unmeasured one; the newest full run can.
- **Pricing by the bytes over the cap.** The warn row carries no cap name or value, and a reader pays
  for the whole document.
- **Raising every persisting breach at every review.** Each review would append a `seen` receipt to
  an unchanged breach's owner item, the noise the clause forbids.

## 5. Production-readiness checklist

- security — no new write path: the walk reads the node's verdict files, one `cat-file` per subject
  and the runlog verb's counts, and its output lands through `record` and `run_loop_file`, unit 3's.
  The `reads` verb prints counts for caller-given subjects only, so no transcript text, path or command
  leaves runlog, as `derive_tool_class` keeps nothing of its input (`tools/runlog/extract.py:532`).
- perf / scale — one directory scan of at most `GATE_RUN_KEEP` runs per worktree
  (`tools/run-gates/run-gates.sh:2692`), one `cat-file` per breach, and one transcript walk per
  review, bounded by 120 s and cached across the walk's items.
- error / empty / loading states — no full run answers `searched-none` and decides nothing; a refused
  reads walk prices `-`; an absent subject is dropped and named.
- observability — every `ledger — cap` line names the subject and why it was dropped or unpriced.
- risks — a node that never runs a full bar never prices a breach; its `searched-none` line says so
  every period, which is the signal to run one.
- testing — each criterion is a probe of this unit's functions or a scratch fixture; the arms in §7
  are observed RED then GREEN by the main loop at the close.
- migration — none.
- user docs — S9.

## 6. Acceptance criteria

- **AC1** — When a probe plants, under a scratch repository's git dir, three run directories in the
  window, a full GREEN run with `warn.1` of class `size` for `AGENTS.md`, an older full run, and a
  newer run with `reused` at `4`, `read_verdict_warnings` from `loop_review.py` returns the full
  GREEN run's one breach, its leg, subject and unit.
  Red when: the newer reused run is read, or the older full run wins.
  fixture: a scratch repository under `%TEMP%`, its run directories planted in the warn grammar
  TOOL-dWitnessedBar-29 S7 gives, absent from the runner at `8bec4cef`.
- **AC2** — When the probe plants only scoped runs in the window, `read_verdict_warnings` returns the
  no-full-run reason, the `cap-breaches` metric answers `searched-none` with it, and `derive_cap_rows`
  returns no row.
  Red when: a scoped run's partial set is read as complete.
- **AC3** — When the full run's `tree` names a tree holding `AGENTS.md` at 20912 bytes, the breach's
  bytes read `20912`; when its subject is absent from that tree, the breach is dropped with one
  `ledger — cap · AGENTS.md · absent at` line.
  Red when: bytes are read from the working tree, or an absent subject prices as 0.
- **AC4** — When `python runlog.py reads --since <epoch> --transcripts <dir> --entry AGENTS.md
  AGENTS.md memory/guides/BUILD-METHOD.md` runs over a planted projects dir, one session of a main
  file and one agent file, both started after `<epoch>`, with two `Read` calls of a backslashed
  absolute path ending in the method guide's path and one before `<epoch>`, it prints `AGENTS.md` `2`
  and the guide `2`.
  Red when: a read before `--since` is counted, a backslashed path is missed, or an entry file counts
  once per session rather than once per transcript file.
  fixture: a planted projects dir under `%TEMP%`, the shape `measure_ready_tree`'s own fixtures plant.
- **AC5** — When the same verb runs over a projects dir holding a second repository key that does not
  begin with the checkout's key, its reads of `AGENTS.md` are not counted, and stdout carries nothing
  but the `<subject>\t<n>` lines.
  Red when: another repository's reads are counted, or a transcript path or text reaches stdout.
- **AC6** — When a probe calls `derive_cap_rows` from `loop_review.py` twice in one process over the
  AC1 plant with a breach of 20912 bytes and 212 reads and one with reads `-`, it returns `cost`
  `4433344B/212` and `-`, each with `catches` `-` and no event, and the planted reads stub records one
  call.
  Red when: a `-` read prices as 0, a catch column carries a number, or the node is read twice.
- **AC7** — (amended, ids 10, 46) When a probe calls `derive_cap_trends` with this review's breaches `A` at 120 bytes, `B` at
  90 and `C` at 50 against a previous line naming `A` at 100, `B` at 90 and `D`, it returns `A`
  `grown`, `B` `held`, `C` `new` and `D` `cleared`; and when `read_previous_breaches` reads a scratch
  repository whose newest committed record's line is `searched-none` and whose record before it names
  `A` at 120, `A` reads `held`.
  Red when: a `searched-none` record clears every breach, equal bytes read `grown`, or the working tree
  is read in place of the commit.
- **AC8** — When a probe calls `derive_cap_raises` over trends `A` `grown`, `B` `held` after `new`, `C`
  `held` after `held`, `D` `new` and `E` `cleared`, it returns `A` and `B` alone, each a proposal with
  `action` `raise` and a non-empty `accept`.
  Red when: an unchanged persisting breach is raised again, a new breach is raised at first sight, or
  a raise carries no accept line, which `run_loop_file` refuses.
- **AC9** — When `python loop_review.py --fixture --plant cap-raise` runs from the loop kit directory
  with `review.loop.retire` set to `report` in the scratch repository's policy file, the dry-run walk
  prints a `cap A` and a `cap B` proposal handed to `item.loop.file`, and the record's `cap-counted`
  line reads `1 new, 1 grown`.
  Red when: the counted line counts held breaches, or `report` silences a raise.
  fixture: the `--fixture` frame and the walk are TOOL-dCalibratedLens-2's and -3's, absent at
  `8bec4cef`.

## 7. Gates

`runlog selftest` · `pre-push run-log line` · `run-gates run-log line` · `format-guard self-test` · `policy fixtures` · `memory hygiene` · `spec tokens (a spec's own names resolve)` · `lexicon naming predicates` · `docs` · `recall floor arms` · `govkit selftest` · `govkit refusal join` · `govkit acceptance matrix`

The leg `loop-review selftest` (TOOL-dCalibratedLens-2 S11, argv `loop_review.py --fixture`) is not in
the manifest at base, so it is named here in prose; it grades the loop arm below once that unit lands.

New arm: tools/loop/loop_review.py · covers AC1 AC2 AC3 AC6 AC7 AC8 AC9 · `--fixture` cases planting run directories full, scoped and reused, a tree with and without the subject, committed previous records with each trend and a `searched-none` one, and `report` set; the failing case staged by dropping the `reused 0` test from `read_verdict_warnings` · none
New arm: tools/runlog/selftest.py · covers AC4 AC5 · a planted projects dir of two repository keys, a main and an agent transcript, backslashed and early reads; the failing case staged by counting entry files once per session · none

## 8. Open questions

- **F1 — Nothing persists a breach (the brief's PRIMITIVE GAP: `check_cap`,
  `tools/policy/budgets.py:304`, prints one and returns); where does the review read breaches from?**
  Options: (a) the `warn.<k>` rows of the newest full run's verdict record on the lease holder's node
  (TOOL-dWitnessedBar-29 S7), deciding no trend where no full run exists; (b) re-measuring every census
  cap at the review, which copies each enforcer's measurement; (c) an ask on dWitnessedBar and
  dWellOiledMachine for a committed or journaled breach record, leaving this clause unbuilt until it
  lands. RESOLVED (agent, 2026-11-02, delegated): (a), rung 3, the most feature-rich survivor and a
  reuse of the ancestor's verdict keys; its one-node reach is stated in §3. widens: none · relaxes:
  none
- **F2 — "Reads" has no producer (the brief's PRIMITIVE GAP); what counts a document's reads?**
  Options: (a) a runlog verb over the lease holder's transcripts, counting `Read` calls and entry
  injections and printing counts only (S3); (b) the act count times a declared load set, which no
  record declares per document; (c) an ask on dWellOiledMachine for a slice manifest per work order
  (TOOL-dTotalRecall-12 S9 hands it there, unspecced), pricing reads `-` until then. (b) has no source;
  (c) leaves every row unpriced. RESOLVED (agent, 2026-11-02, delegated): (a), rung 3: runlog already
  walks the projects root for `extract --ready` (`tools/runlog/runlog.py:512`, `extract.py:1204`), and
  counts of caller-given paths widen no data surface. widens: none · relaxes: none
- **F3 — What fills the catch columns of a `cap` row?** RESOLVED (agent, 2026-11-02, delegated): `-`,
  rung 1 of the records: TOOL-dCalibratedLens-2 §4 "The row" keeps `-` in the three catch columns of a
  row its provider returns with `catches` `-`, so a breach, which catches nothing, never reads as a row
  that caught nothing and is not proposed for retirement; a breach leaves the ledger by clearing.
  widens: none · relaxes: none
- **F4 — Does `review.loop.retire` govern a raise?** Options: (a) no: a raise is handed on under every
  value, since it proposes no retirement and the clause's brake is the owner item; (b) yes, so under
  `report` a breach is only recorded. (b) lets a key about retiring silence the one brake an advisory
  cap keeps. RESOLVED (agent, 2026-11-02, delegated): (a), rung 1, the clause: "the Loop Review raising
  an owner item for a breach that persists or grows". widens: none · relaxes: none
- **F5 — How does a raise reach `run_loop_file`, given `propose` (TOOL-dCalibratedLens-5) builds at
  order 11 and this unit at order 6, and the provider shape returns rows and events only?** Options:
  (a) `run_loop_walk` extends the proposals it hands `run_loop_file` with `derive_cap_raises`'s, read
  from the cached S4; (b) a step of `propose`, which leaves the raise unbuilt until order 11; (c) a
  provider that returns proposals, a third member of a shape TOOL-dCalibratedLens-2 fixes at two.
  RESOLVED (agent, 2026-11-02, delegated): (a), rung 3: the proposal shape `{"kind", "id", "action",
  "accept", "row"}` and its keyed filing are TOOL-dCalibratedLens-3 S7's as written, and the walk is
  the one place every item's output meets; the spec audit's cross-read holds the extension on unit 3's
  spec (M2). widens: none · relaxes: none
- **F6 — TOOL-dCalibratedLens-2's `cost` grammar admits the units `s` and `tok`; what unit does a
  breach's bytes times reads take?** Options: (a) a third unit `B`, `<bytes times reads>B/<reads>`, in
  the grammar's `<number><unit>/<runs>` shape; (b) tokens estimated from bytes, a conversion no record
  measures; (c) `-` always, leaving the clause's price unwritten. RESOLVED (agent, 2026-11-02,
  delegated): (a), rung 3: the row's shape holds and the figure is the one research-caps names; the
  added member of unit 2's unit set is an interface the spec audit's cross-read holds on both specs
  (M2). widens: none · relaxes: none

## 9. Revision log

- rev-1 · 2026-11-02 · initial draft, from the packet's Items 15 (`cl-dClosedLoop-0472@bf8d8ee5`),
  gap-review-19, night pass two point 5 and NT-23, research-caps sections 5 and 6, the brief's row for
  this unit and S1, S3 and S4, the sibling specs TOOL-dCalibratedLens-2 and -3 as written this run,
  TOOL-dWitnessedBar-4 and -29, and the runner, the policy kit and runlog at base `8bec4cef`. The status
  token is `OPEN`, the drafting token of TEMPLATE-SPEC; the brief's `DRAFT` is no member of
  `STATUS_TOKENS` (`tools/memory-tree/tree_lib.py:28`).
- rev-2 · 2026-11-02 · §3 §4 §7 §10 S1 S6 AC7 · amended at the disposal of the round-1 spec audit
  `2026-11-02-review-TOOL-dCalibratedLens-1-spec-audit`, §4 "Amendments (round-1 spec
  audit)": ids 49 (`TOOL-dCalibratedLens-27`), and 10, 46, 30, 22, 34 and 39
  (`TOOL-dCalibratedLens-30`); §3 gains the hands-off to unit 30.

## 10. Reuse audit

The seams extended are TOOL-dCalibratedLens-2's `PROVIDERS` and TOOL-dCalibratedLens-3's `METRICS`,
walk and proposal shape; the runner's verdict record and its run directories
(`tools/run-gates/run-gates.sh:2721-2722`, the keys at `:5675-5681`) with TOOL-dWitnessedBar-29's
`warn.<k>` keys read as that spec spells them; runlog's transcript walk, `measure_ready_tree`
(`tools/runlog/extract.py:1204`) beside which `measure_subject_reads` sits, over `build_session_tree`
and `read_records`; and `extract --ready`'s CLI shape (`tools/runlog/runlog.py:512`) for the `reads`
verb. `python tools/codebase-map/reuse_lookup.py "persist a size cap breach and count how often a
document is read"` ranked `read_text`, `read`, `counts`, `read_journal` and `resolve_caps`
(`tools/policy/budgets.py:206`); `resolve_caps` answers a cap's value and mode and `check_cap` (`:304`)
its verdict, neither persists a breach, and no seam counts a document's reads, which is why S3 adds one.
Where record and source disagree: the brief says no journal class or record carries a breach, and
research-caps' pick B says a breach "is journaled automatically, keyed by unit"; neither
TOOL-dWellOiledMachine-16's `JOURNAL_CLASSES` nor TOOL-dWitnessedBar-29 journals one, and its verdict
keys live in the git dir, so the brief is right and §8 F1 settles the source. `caps.toml` names each
cap's enforcer and no subject, which is why re-measuring was rejected.

Recall terms used: `python tools/memory-recall/query.py "how does an advisory size cap breach get priced and trended into an owner item" --terms "size cap breach budgets.enforce warn advisory NT-23 bytes reads value ledger Loop Review owner item curation-debt"`
