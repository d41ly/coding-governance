# TOOL-aThawedCorpus-1 — hygiene check 21 stops spawning a process per record

**Status:** CLOSED · rev-5 · 2026-08-27 · node a · Tier-1 · base f1be0b49 · streams tooling · order 3

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-08-27-build-TOOL-aThawedCorpus-1-per-check-timing.md](../build/2026-08-27-build-TOOL-aThawedCorpus-1-per-check-timing.md) | research | — |
| [2026-08-27-prompt-TOOL-aThawedCorpus-1-1.md](../prompts/2026-08-27-prompt-TOOL-aThawedCorpus-1-1.md) | research | — |
| [2026-08-27-review-TOOL-aThawedCorpus-5-spec-audit.md](../reviews/2026-08-27-review-TOOL-aThawedCorpus-5-spec-audit.md) | spec-audit | TOOL-aThawedCorpus-5 TOOL-aThawedCorpus-4 TOOL-aThawedCorpus-2 TOOL-aThawedCorpus-3 |

<!-- /gen:spec-records -->

## 1. Goal

Check 21 of `tools/memory-tree/check-memory-hygiene.sh` costs 338.9 s of a 1398 s full run on a
QUIET node `a` — the second-largest term, after check 23 — and its filename-projection loop spawns
four to six processes for each of 310 records. Collapse that loop to one `awk` pass so this term
stops being process creation this repo controls.

## 2. Scope (IN)

- **S1** — Replace the `proj21` `while` loop in `check-memory-hygiene.sh` with a single `awk` pass
  over the same `S` rows of `gen_build_index.py --print-bindings`, preserving its four outcomes:
  a name with no date prefix, a bound record with no family-qualified id, a name claiming an id its
  own `Serves` line does not list, and a conformant record that prints nothing.
- **S2** — Keep every `fail 21` branch in the shell, where `check-arms.py` can discover it. There
  are FIVE call sites — `:670`, `:673`, `:680`, `:683`, `:704` — and only `:704` belongs to the
  projection this unit touches; the other four are check 21's other branches and are not in scope.
  The `awk` pass replaces the projection, never the reporting.
- **S3** — Prove the output byte-identical: the full-corpus stdout of the changed checker equals the
  unchanged checker's, and both fixture classes of `check-memory-hygiene.test.sh` still red.
- **S4** — Record the before and after wall clock for the leg in this build's own folder, measured
  the same way on the same node.

## 3. Non-goals (OUT)

- **N1** — No skip, cache, freeze or scoping mechanism. `TOOL-aThawedCorpus-2` was to have declared
  one and is RETIRED (WONTDO): the freeze already exists as `run-gates.sh`'s `input_key` plus
  `GATE_REUSE`, guard-skip preempts it, and guarding this leg would break `TOOL-aThawedCorpus-5`'s
  compensating control. The precedent for deferring rather than bundling is `TOOL-aCollapsedScan-1`,
  which parked exactly that decision for exactly that reason.
- **N1b** — No overlap with `TOOL-aThawedCorpus-4`, which collapses check 23's loops. Two checks,
  two grammars, two units.
- **N2** — No change to what check 21 MEANS. The projection rule, the pin, the unbound escape and
  the four branch texts are untouched.
- **N3** — No change to `gen_build_index.py --print-bindings`, whose one invocation is not the term
  under attack. If the probe in §8 shows otherwise, this unit does not silently widen — it is
  re-specced.
- **N4** — No sweep of sibling shell tools. `check-method-carriers.sh` carries the same shape over a
  six-element population and is immaterial; it is named here so the next reader does not re-derive
  that it was considered.

## 4. Design

### Data model

`--print-bindings` emits tab-separated rows. The `S` row is
`S<TAB><path><TAB><ignored><TAB><space-separated ids>`. The projection reads the path's basename,
strips the eleven-byte ISO date prefix, drops the first `-`-delimited token, and looks for a leading
`(FAM_ALT)-<slug>-<seq>` — then asserts that id is a member of the row's own id list.

Every one of those operations is native `awk` string work. The current shell spelling pays a
command substitution plus a `grep` exec for `claimed`, and a subshell plus `tr` and `grep` execs for
the membership test, on every one of 310 rows.

### Migration

None. The checker is not a stored artifact and has no consumers other than its own callers.

### Files touched (estimate)

`tools/memory-tree/check-memory-hygiene.sh` — one block replaced, roughly 18 lines to 20.
`memory/builds/aThawedCorpus/build/` — the before/after measurement record.

### Alternatives rejected

- **Scope check 21 to touched builds.** Rejected HERE and deferred to unit 3: check 21's verdict
  depends on an id set defined by other files, so it is not per-file keyable, and scoping it needs
  the input-digest primitive unit 2 builds. Cutting spawns is the term this unit owns.
- **Move the whole projection into `gen_build_index.py`.** Rejected: the four `fail` branches would
  become Python raises, which `check-arms.py` discovers from tracked shell and cannot see. The
  checker's own header records that split as deliberate.

## 5. Production-readiness checklist

- security — N/A. No new input, no new write path; the same bytes are read by a different parser.
- perf / scale — this IS the subject. The measurement in §6 is the observable.
- a11y — N/A. A shell gate has no user interface.
- i18n — N/A, with one caveat carried into the design: the `awk` pass does byte comparison and
  ASCII class matching only, exactly as the shell spelling did, so no locale collation is
  introduced.
- error / empty / loading states — an empty `S` set prints nothing and the enclosing
  `printf | grep -q .` guard already handles a corpus with no records.
- observability — the leg's own row in `<git-dir>/gate-ledger.tsv` carries the duration.
- risks — the single real risk is a projection that differs from the shell's on some record. S3's
  byte-identity diff over the whole corpus is the control, not an argument.
- testing + left-shift gates — `check-memory-hygiene.test.sh` and the `harness arms` leg both stay
  green; `ARMS_FLOORS` for this file stays at `20:20`, since no `fail` branch is added or removed.
- migration / rollback — one commit, revertable; nothing generated changes.
- user docs — N/A. No user-facing surface.

## 6. Acceptance criteria

- **AC1** — When the changed checker runs over the full corpus AND over a scratch corpus seeded
  with one instance of each projection outcome, its stdout is diffed against the unchanged
  checker's on both and `diff` reports no difference. The real corpus alone is a ONE-SIDED oracle:
  check 21 emits nothing today, so a diff over it catches added output and can never catch a
  dropped finding.
- **AC2** — When `bash tools/memory-tree/check-memory-hygiene.test.sh` runs, it exits 0 and its red
  fixtures still red.
- **AC3** — When the instrumented per-check timing is re-taken on a quiet node `a` the same way,
  check 21's own span is under 30 s, against the 338.9 s recorded in this build's measurement
  record, with the foreign-process count reported at both ends of the run.
- **AC4** — When `python tools/memory-tree/check-arms.py --check` runs, it is green with
  `ARMS_FLOORS` for `tools/memory-tree/check-memory-hygiene.sh` unchanged at `20:20`.
- **AC5** — When the three reportable projection outcomes are staged one at a time into a scratch
  corpus, each still appears inside the single `fail 21` body at `:704`, and a conformant record
  still contributes no line — the fourth outcome prints nothing by construction, which is why it is
  not gradeable as its own message.

## 7. Gates

`memory hygiene` · `memory-hygiene self-test` · `harness arms (fail branches armed or pinned)` ·
`check-arms selftest` · `build README slot contract`. Adds no new gate; unit 3 owns the ceiling that
would have been this unit's left-shift.

## 8. Open questions

- **FACT-QUESTION · F1 — is the span the projection loop, or the one `gen_build_index.py
  --print-bindings` invocation inside the same check?** RESOLVED (agent, 2026-08-27, delegated): the
  LOOP. Measured on a quiet node `a`, `--print-bindings` alone is **1.416 s** producing 301 `S` rows,
  against check 21's directly measured body span of **338.9 s** — 0.4% and 99.6%. The probe could
  have produced a negative and nearly did on the prior contaminated pass, where the same command
  measured 10.1 s; on a quiet box it does not. This unit's design stands unchanged and N3 holds.

- **F2 — does the `awk` pass need `FAM_ALT` interpolated, or passed with `-v`?** RESOLVED (agent,
  2026-08-27, delegated): `-v`, matching check 12's driver, so the family alternation is data rather
  than program text. Interpolating it would put shell-expanded bytes inside an `awk` program, which
  is the class this corpus records as `heredoc-escape-reaches-the-regex`.

## 9. Revision log

- rev-1 · 2026-08-27 · initial draft, from the instrumented per-check measurement on node `a`.
- rev-2 · 2026-08-27 · re-based on the QUIET-box re-measurement, which withdrew the contaminated
  figures and reordered this unit behind `TOOL-aThawedCorpus-4`. F1 and F2 both resolved, F1 by its
  stated probe.
- rev-3 · 2026-08-27 · folded the M4 spec audit. `base` re-pinned after regrounding 39 commits.
  Corrected the `fail 21` surface from four branches to five call sites of which one is in scope.
  AC5 restated against what the projection can actually emit, and AC1 given a seeded scratch corpus
  because a byte-diff over a silent corpus is one-sided.
- rev-4 · 2026-08-27 · N1 re-pointed after `TOOL-aThawedCorpus-2` was retired. Caught by
  `gotchas.py --for-diff` selecting `amendment-leaves-its-other-half-standing`, which is precisely
  a retirement leaving a forward reference describing it as merely sequenced later.

- rev-5 · 2026-08-27 · CLOSED. Built and measured: full leg 226 s -> 34 s, stdout AND stderr
  identical. AC1's seeded half satisfied by a differential feeding both implementations crafted S
  rows over all four outcomes plus empty ids, short rows and non-S rows — identical on every one.
## 10. Reuse audit

The seam is `tools/memory-tree/check-memory-hygiene.sh`'s own check 12 driver, which already builds
a tagged path stream in the shell and hands it to one `awk` with `-v` bindings. `TOOL-aBatchedLintel-1`
built that shape for checks 12 and 7, porting `PERF-aSlothfulCapstan-1`; `TOOL-aCollapsedScan-1` built
the same collapse for `unattended.sh --plan` on 2026-08-26 and its README carries the spawn cost
measured on a node with an on-access scanner. This unit extends that seam rather than inventing one.

`python tools/codebase-map/reuse_lookup.py "skip re-checking a memory build folder whose content has
not changed since it was last verified"` returned `checks` at `tools/memory-tree/corpus_ids.py` and
`cmd_check` at `tools/memory-tree/row_grammar.py` as the nearest seams, plus `build_cache` at
`tools/memory-recall/query.py` — the last of which is unit 2's business, not this unit's.

Recall terms used, because M7 re-runs the query: `cache freeze closed build corpus walk hygiene gate
fingerprint incremental stale mtime tree-hash rescan`. The query surfaced `TOOL-aQuarriedLantern-1`'s
review finding F1, which is the record that establishes this corpus's existing cache freshness key is
mtime-based — evidence for unit 2 and not for this one.
