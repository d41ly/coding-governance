# TOOL-aCollapsedScan-13 — the hygiene gate stops spawning a process per file, and per criterion

**Status:** INPROGRESS · rev-2 · 2026-08-26 · node a · Tier-2 · base 3c37a1fb · streams tooling · order 5

<!-- gen:spec-records -->

*No record names this unit.*

<!-- /gen:spec-records -->

## 1. Goal

Take the process-creation cost out of `check-memory-hygiene.sh` without changing what any check
covers or reports. It is the leg that gates every commit in this repo, it is recorded at 499 s, and
a line-level profile puts roughly 91% of that in two regions that spawn external commands where
shell builtins and one prebuilt map would do.

## 2. Scope (IN)

- **S1** — Check 23's per-spec filter (lines 1137–1145) stops forking to decide scope: `${sp##*/}`
  for the basename, a substring expansion for the date, a shell string compare for the cutoff, and
  ONE read of the spec's head for the status header instead of `sed` piped into `grep`.
- **S2** — Check 23's per-criterion lookup (line 1169) stops running `printf` into `grep -m1 -E`
  per (unit, label) pair. `$alledger` is already in memory; it is loaded once into a `declare -A`
  keyed `"<uid> <lab>"` and read by subscript.
- **S3** — Check 10's archive loop (line 712) stops running `head -3 | grep -qF` per archive file.
- **S4** — Check 11's tombstone loop (line 717) gets the same treatment, whatever its profile shows
  its per-iteration spawns to be.
- **S5** — A before/after equivalence proof over the real corpus: the checker's stdout and exit
  status are byte-identical before and after, on a clean tree AND on a staged break per touched
  check. Recorded in the build record.

## 3. Non-goals (OUT)

- Changing what any check COVERS. Every spec still walked, every pair still graded, every archive
  still read. The backlog row's argument is that the cost is the implementation and not the
  coverage, and S5 is what holds this unit to that.
- Scoping check 23 to changed specs. It asserts a PAIRING between a spec and a journal record, and
  that pairing breaks without the spec changing — a record renamed, deleted, or its `**Evidences:**`
  block edited. Walking terminal specs is correct and stays. This is the same refusal
  `TOOL-aCollapsedScan-4` made for check 30, and it costs nothing here because the fix is orthogonal.
- `corpus_ids.py`. It is the slowest single helper at 34.2 s standalone but only 2.5% of the leg,
  and it is Python rather than shell — a different unit if it is ever worth one.
- Declaring a wall-clock ceiling for this leg. `tools/gate-legs.json` has no field for one; that is
  `TOOL-aCollapsedScan-5`.
- Any change to the checks' MESSAGES. S5 compares bytes, so a reworded refusal would fail it.

## 4. Design

### The profile this is built against

`PS4='+ ${EPOCHREALTIME} ${LINENO} ' bash -x`, aggregated per line, node `a`, 2026-08-26. Trace
overhead inflates the absolute span to 2161 s, so these seconds RANK the lines and are not the
leg's cost — `gate-ledger.tsv` records that at 499 s.

| line | seconds | hits | what it is |
|---|---|---|---|
| 1137 | 275.5 | 640 | `case "$(basename "$sp")" in` |
| 1169 | 252.2 | 1323 | `printf … \| grep -m1 -E` per (unit, label) |
| 1168 | 247.3 | 441 | the label loop around it |
| 1138 | 230.9 | 951 | `basename \| cut -c1-10` |
| 1141 | 199.0 | 846 | `printf \| sort -C` |
| 717 | 186.4 | 831 | check 11's tombstone loop |
| 1129 | 139.5 | 287 | `git ls-files` for the spec set |
| 713 | 118.2 | 842 | check 10's archive loop body |
| 712 | 111.8 | 277 | `head -3 \| grep -qF` per archive |
| 1057 | 53.1 | 3 | `corpus_ids.py --check` |

Check 23 is about 69% of the run, checks 10 and 11 about 22%, `corpus_ids.py` 2.5%.

### What the profile corrected

The backlog row attributed the cost to check 23's per-spec FILTER. The filter is real — 705 s across
lines 1137, 1138 and 1141 — but the worst single line is 1169 at **1323 hits**, two processes per
acceptance criterion to search a string already held in a variable. And checks 10 and 11, about a
fifth of the leg, were absent from the row entirely. Building to the row as written would have fixed
69% while believing the job was done.

### Data model

One `declare -A` in check 23, keyed `"<uid> <lab>"` with the row's form word as its value, built by
one pass over `$alledger`. `declare -A` is already used three times in this file, so the bash floor
is unchanged.

### Alternatives rejected

- **Scoping the walk to changed specs.** §3 states why: the assertion is about a pairing, not about
  a spec, and it breaks without the spec changing.
- **Moving check 23 into `row_grammar.py` or a new Python helper.** It would remove the spawns by
  moving the work, at the cost of a second reader of the acceptance-ledger grammar that
  `HYGIENE.md` documents once. Two answers to one question, for a cost the builtins already remove.

### Files touched (estimate)

`tools/memory-tree/check-memory-hygiene.sh` only, plus the memory-tree kit version marker.

## 5. Production-readiness checklist

- security — N/A. No new input, write path or network call.
- perf / scale — the subject. Measured before and after per AC3.
- a11y / i18n — N/A.
- error / empty / loading states — the empty-`$labs` arm, the absent-index arm in check 10 and the
  unconfigured-`TOOMBSTONE_ROOTS` arm in check 11 all keep their current behaviour; S5's byte
  comparison is what proves it rather than reading the diff.
- observability — refusal text is unchanged by construction, since S5 compares bytes.
- risks — THE risk is silently weakening a merge-bar gate. A refactor that makes a check stop
  finding things looks exactly like a faster check. AC2 is the whole answer: each touched check is
  staged RED before and after and the messages compared.
- testing + left-shift gates — the hygiene kit's own self-test suite plus AC2's staged breaks.
- migration / rollback — a single-file revert.
- user docs — none owed.

## 6. Acceptance criteria

- **AC1** — When `bash tools/memory-tree/check-memory-hygiene.sh` runs on the clean tree before and
  after, its stdout and exit status are byte-identical, proven by `diff` of the two captures.
- **AC2** — When a break is staged for EACH touched check (23, 10, 11) and `bash tools/memory-tree/check-memory-hygiene.sh` runs, the post-change checker
  reports it with a message byte-identical to the pre-change checker's, and both exit 1. A check
  whose break cannot be staged is named as unproven rather than assumed.
- **AC3** — When the leg is timed on the same node before and after UNDER THE SAME MACHINE LOAD,
  taken back to back, the after figure is at most half the before figure. The ratio is the claim and
  the absolute seconds are not: another session has been running `GATE_SELFTESTS=1` on this box for
  hours, and an idle reading is not available to this run. Both figures and the contention are
  recorded in the build record, so a later idle re-measurement can supersede them.
- **AC4** — When `bash tools/memory-tree/check-memory-hygiene.sh` is re-profiled with the same
  `PS4` trace, no line in the top ten is one this unit claimed to fix.
- **AC5** — When `bash tools/run-gates/run-gates.sh` runs, the bar is green.

## 7. Gates

`memory hygiene` — which is the subject, so its own green is necessary and not sufficient; AC2 is
what makes it meaningful. Plus the memory-tree kit's self-tests and the full bar.

## 8. Open questions

- **F1 — refactor in shell, or move the hot checks into Python?** RESOLVED (agent, 2026-08-26,
  delegated): shell. §4 records the reason — a Python check 23 would be a second reader of the
  acceptance-ledger grammar, and the builtins remove the cost without that.
- **F2 — is a `declare -A` acceptable here?** RESOLVED (agent, 2026-08-26, delegated): yes. This
  file already uses three, so the bash floor does not move.
- **F3 — should the leg gain a declared ceiling so the cost cannot silently return?** RESOLVED
  (agent, 2026-08-26, delegated): not here. No leg in `tools/gate-legs.json` can carry one, which is
  `TOOL-aCollapsedScan-5`, and inventing a mechanism for one leg is how a manifest grows a second
  grammar. AC4's re-profile is this unit's own guard against regression.

## 9. Revision log

- rev-1 · 2026-08-26 · initial draft, written against the line-level profile rather than against the
  backlog row, which had the region right and the hottest line wrong.
- rev-2 · 2026-08-26 · AC3 rewritten before any code, because as drafted it demanded an idle box and
  this one is not idle: a concurrent `GATE_SELFTESTS=1` bar has been running for hours. An acceptance
  criterion I already know cannot be met is not a criterion, so it now claims a RATIO under stated
  identical load rather than an absolute figure.

## 10. Reuse audit

The seam is `check-memory-hygiene.sh` itself; this unit changes how three of its checks reach their
data and adds no new reader. The prior art it copies is `TOOL-aCollapsedScan-1` in this same build —
one pass over the corpus into a map, then lookups — and `TOOL-dNarrowedAnchor-1`, which cut the same
class from the unattended gate self-test and whose measurement of per-spawn cost on a node with an
on-access scanner is what makes these numbers legible. No probe was needed to find the seam: the
profile names the lines.
