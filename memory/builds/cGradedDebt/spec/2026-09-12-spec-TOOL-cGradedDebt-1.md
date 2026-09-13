# TOOL-cGradedDebt-1 — a curation-debt row earns its listing, and check 8 counts what it graded

**Status:** SPECCED · rev-1 · 2026-09-12 · node c · Tier-2 · base 09a22d2b · streams tooling · order 1

<!-- gen:spec-records -->

*No record names this unit.*

<!-- /gen:spec-records -->

## 1. Goal

`memory/project/curation-debt.txt` drops each listed file out of hygiene checks 6, 7 and 8 and
asserts only that the path is still tracked, so a row whose fault has been fixed or whose cap has
been raised past it stays green forever. Make a listed file that would pass unwaived red as a stale
row, report which of the three checks each row actually earns, and make check 8 announce the number
of backlog rows it graded.

## 2. Scope (IN)

- **S1** The three `in_debt` filters in checks 6, 7 and 8 of
  `tools/memory-tree/check-memory-hygiene.sh` are removed, so a listed file re-enters each check's
  population and produces findings again. `in_scope` filtering is untouched. Observed by AC1.
- **S2** One helper partitions each check's findings by leading path into the unwaived set, which
  fails exactly as today, and the waived set, which is recorded and never fails. The helper assigns
  to a global rather than returning on stdout, because a command substitution or a pipeline would
  run it in a subshell and discard the accumulator it exists to fill. Observed by AC1 and AC2.
- **S3** A new `fail 6` arm names every listed path that produced no finding in check 6, 7 or 8.
  It is held under `--staged`, where the selection is the staged set and an unstaged listed file
  would report as earning nothing. Observed by AC2 and AC5.
- **S4** One `memory-hygiene:` report line per listed path names the checks it earns against the
  three it is waived from, so an over-wide row is visible without failing. Observed by AC3.
- **S5** Check 8's awk emits its graded ROW count and shard count on a sentinel line, summed across
  `xargs` invocations, stripped from the findings, and printed as a `memory-hygiene:` line.
  Observed by AC4.
- **S6** `ARMS_FLOORS` for this gate moves from `26:26` to `27:27` in `.memory-tree.conf`, in the
  same commit as the arm. Observed by AC5.
- **S7** `memory/HYGIENE.md`'s grandfather-ratchet entry for this registry states the stale-entry
  guard, and the registry's own header states that the per-check report now derives what its
  blast-radius paragraphs assert by hand. NOT OBSERVED by a criterion here: both are prose, and no
  criterion in this build grades prose.

## 3. Non-goals (OUT)

- No shrink-only pin for this registry. `tools/drift-audit/drift_signals.py` already declares
  `memory/project/curation-debt.txt` under `SHRINK_ONLY` against a git-history seed, and a second
  assertion in `.memory-tree.conf` would be two answers to one question.
- No per-line and no per-check waiver grammar. A row stays whole-file, and a row whose waiver is
  wider than its fault is REPORTED rather than failed. Failing it would red `memory/backlog/TOOL.md`
  and `memory/builds/cBriefedPilot/README.md` on the day this lands, and the first of those is the
  subject of an open owner call.
- No change to check 8's `nmatch`, which is validated per-row against an upstream corpus. The two
  rows that quote a backticked table predicate are unit 2's, and they are two in the whole corpus
  including archives.
- No drain of any existing row, no split of the `TOOL` shard, and no touch to
  `TOOL-aWeighedCompass-3`.
- No new check number and no new gate leg. The arm hangs off check 6 beside the tracked-path
  stale-line guard that already lives there.

### Edges

- **hands-off** `TOOL-cGradedDebt-2` — this unit makes check 8 grade `memory/backlog/TOOL.md`'s
  rows as waived findings, and unit 2 fixes the six it surfaces. Neither blocks the other, because
  a waived finding never fails.
- **consumes-from** external — `tools/drift-audit/drift_signals.py`'s `SHRINK_ONLY` declaration,
  which is why this unit adds no pin. Without it the registry would carry no shrink assertion at all.

## 4. Design

### Data model

`DEBT_EARNED` is an associative array keyed by registry path whose value is the space-separated list
of check numbers that path produced a finding in. It is declared beside `DEBT_SET` and filled by the
partition helper during checks 6, 7 and 8.

The partition key is the finding's leading path. All three finding formats begin with the path
followed by a space or a colon, so stripping at the first of either extracts it. A path containing a
space would extract short and match no registry key, which leaves the finding in the UNWAIVED set
and fails loudly. The failure direction is safe by construction rather than by this corpus happening
to hold no such path.

### Inventory

| Identifier | Kind | Where | Cell |
|---|---|---|---|
| `DEBT_EARNED` | associative array | `check-memory-hygiene.sh` | shell global, screaming snake like `DEBT_SET` |
| `_UNWAIVED` | string global | `check-memory-hygiene.sh` | shell scratch global, underscore-prefixed like `_c7env` |
| `split_debt` | function | `check-memory-hygiene.sh` | shell function, verb-first like `in_debt` and `pop_guard` |

### Migration

None. The registry file's bytes do not change, `.memory-tree.conf` gains one digit pair in
`ARMS_FLOORS`, and every current row earns at least one check, so the gate's verdict on today's
tree is unchanged.

### Rollout

Measured at `09a22d2b` with the waiver lifted, so the arm is green on landing and the report is
non-empty on day one:

| Listed path | earns 6 | earns 7 | earns 8 |
|---|---|---|---|
| `memory/builds/aBoundedVerdict/README.md` | yes, 39988 B over 25600 | yes, 5 lines | n/a |
| `memory/builds/cBriefedPilot/README.md` | yes, 27895 B over 25600 | no | n/a |
| `memory/builds/aUnmannedHelm/README.md` | no, 12896 B under 25600 | yes, 1 line | n/a |
| `memory/backlog/TOOL.md` | yes, 359423 B over 61440 | yes, 314 lines | yes, 6 rows |

Two rows are already over-wide and the report says so without failing them. The third column reads
`n/a` for a build README because check 8's population is the backlog shards alone.

### Files touched (estimate)

| Path | Change |
|---|---|
| `tools/memory-tree/check-memory-hygiene.sh` | the helper, three filter removals, three partitions, the arm, two report sites |
| `tools/memory-tree/check-memory-hygiene.test.sh` | the arm's staged break and the report assertions |
| `.memory-tree.conf` | `ARMS_FLOORS` for this gate |
| `memory/HYGIENE.md` | the registry's ratchet entry |
| `memory/project/curation-debt.txt` | header sentence on what the report now derives |
| `memory/map/features/memory-tree-hygiene.md` | dossier refresh on touch |

### Alternatives rejected

**Re-run the three predicates over the debt set alone, after the checks.** It needs a second
spelling of each predicate, which is the two-answers-to-one-question class this engine has already
been bitten by at check 7's exclusion expression.

**A per-check stale guard that fails.** It reds `memory/builds/cBriefedPilot/README.md` on check 7
and `memory/builds/aUnmannedHelm/README.md` on check 6 immediately, and neither has a remedy short
of the per-line waiver grammar this unit rejects.

**A pin for this registry in `.memory-tree.conf`.** Rejected under §3, because the drift audit
already owns the shrink assertion.

## 5. Production-readiness checklist

- security — N/A. No new input, no new path read, no privilege.
- perf / scale — four files re-enter the scanned population. Check 7 gains a 359 KB file and check 8
  gains 438 rows, both inside a single existing awk pass. Measured on the closing bar against the
  `memory hygiene` leg's own recorded seconds.
- error / empty / loading states — an empty registry leaves the accumulator empty and the arm
  silent, which is the registry's declared fully-strict state. A row naming an untracked path is
  already the sibling guard's refusal and is unchanged.
- observability — the two report lines are the whole point of the unit, and they follow the
  engine's existing report convention at check 23.
- risks — the partition key. Covered by the fail-safe direction above, and by AC1, which observes a
  waived finding landing in the waived set rather than merely not failing.
- testing — one new arm in `check-memory-hygiene.test.sh`, staged RED before it is wired.
- migration — none.
- user docs — `memory/HYGIENE.md` only. This is gate-internal.

## 6. Acceptance criteria

- **AC1** — When a compliant file is added to the fixture's `curation-debt.txt` and
  `check-memory-hygiene.test.sh` runs, the gate names that path as a row that hides nothing, and the
  run's other verdicts are unchanged.
  Red when: the filters are removed but the partition sends a waived finding to the unwaived set,
  which turns every listed file into a hard failure instead.
  fixture: the tree `check-memory-hygiene.test.sh` builds. No conf cutoff arms this arm.
- **AC2** — When `bash tools/memory-tree/check-memory-hygiene.sh` runs over this repo at the landing
  commit, it exits 0 and names no stale row, because all four listed paths earn a check.
  Red when: `memory/builds/aUnmannedHelm/README.md` stops producing its one over-cap line, which is
  the only check it earns.
  figure: DERIVED — the table in §4 Rollout re-derives from the same run.
- **AC3** — When that same run's stdout is read, one `memory-hygiene:` line per listed path names
  the checks it earns, and the lines for `memory/builds/cBriefedPilot/README.md` and
  `memory/builds/aUnmannedHelm/README.md` each name fewer than the three they are waived from.
  Red when: the report prints the waived set rather than the earned set, which would name three for
  every row and tell a reader nothing.
- **AC4** — When that same run's stdout is read, a `memory-hygiene:` line states how many backlog
  rows check 8 graded, and the number is 499 rather than the 61 it grades today.
  Red when: the sentinel line reaches the findings variable instead of being stripped, which turns
  the count into a finding and fails check 8 on every run.
  figure: DERIVED — 499 is this corpus's row count at `09a22d2b`, and the criterion re-derives it.
- **AC5** — When `python tools/memory-tree/check-arms.py --check` runs it passes with this gate's
  `ARMS_FLOORS` entry at `27:27`, and the new arm is absent from
  `memory/project/unarmed-branches.txt`.
  Red when: the arm is added without its self-test assertion, which is the unarmed state this floor
  exists to catch.

## 7. Gates

`memory hygiene` · `memory-hygiene self-test` · `harness arms (fail branches armed or pinned)` · `drift-audit records` · `codebase-map coverage + freshness` · `shell hygiene (a loop fed by a command substitution)`

New arm: `tools/memory-tree/check-memory-hygiene.test.sh` · a compliant fixture file listed in the fixture's curation-debt registry · this gate's `ARMS_FLOORS` entry

The full bar is owed with `GATE_SELFTESTS=1`, because this is kit work and the memory-tree
self-tests are held by default.

## 8. Open questions

none

## 9. Revision log

- rev-1 · 2026-09-12 · initial draft.

## 10. Reuse audit

The seam is `tools/check-testsuite-counts.sh`, which already spells this exact shape for a different
registry: compute the verdict for every member, then branch on waivedness, so that a complying
member which is waived fails as a stale row while a non-complying member which is not waived fails
as a real finding. This unit applies that branch to checks 6, 7 and 8 rather than inventing one. The
second seam is the arm's HOME — `check-memory-hygiene.sh` already carries a `fail 6` stale-line
guard for this same registry, so the new arm sits beside it and no new check number, gate leg or
`tools/gate-legs.json` row is minted. `tools/memory-tree/corpus_ids.py` is the model for the message
wording, being check 14's waiver plus pin plus stale guard.
`python tools/codebase-map/reuse_lookup.py` was run and returned no shell seam at all, because its
scan-coverage line reports the shell layer as unscanned. The two seams above were found by reading
the sibling registries instead, and that is recorded here rather than dressed up as a probe hit.

Recall terms used: `curation-debt waiver registry shrink-only pin stale-entry guard hygiene check 8 status vocabulary WONTDO backlog shard population pop_guard grandfather`
