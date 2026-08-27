# TOOL-aThawedCorpus-1 — hygiene check 21 stops spawning a process per record

**Status:** OPEN · rev-1 · 2026-08-27 · node a · Tier-1 · base f5dff6ae · streams tooling · order 1

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-08-27-build-TOOL-aThawedCorpus-1-per-check-timing.md](../build/2026-08-27-build-TOOL-aThawedCorpus-1-per-check-timing.md) | research | — |
| [2026-08-27-prompt-TOOL-aThawedCorpus-1-1.md](../prompts/2026-08-27-prompt-TOOL-aThawedCorpus-1-1.md) | research | — |

<!-- /gen:spec-records -->

## 1. Goal

Check 21 of `tools/memory-tree/check-memory-hygiene.sh` costs 365.6 s of a 470 s full run on node
`a`, and its filename-projection loop spawns four to six processes for each of 310 records. Collapse
that loop to one `awk` pass so the leg's dominant term stops being process creation this repo
controls.

## 2. Scope (IN)

- **S1** — Replace the `proj21` `while` loop in `check-memory-hygiene.sh` with a single `awk` pass
  over the same `S` rows of `gen_build_index.py --print-bindings`, preserving its four outcomes:
  a name with no date prefix, a bound record with no family-qualified id, a name claiming an id its
  own `Serves` line does not list, and a conformant record that prints nothing.
- **S2** — Keep the four `fail 21` branches in the shell, where `check-arms.py` can discover them.
  The `awk` pass replaces the projection, never the reporting.
- **S3** — Prove the output byte-identical: the full-corpus stdout of the changed checker equals the
  unchanged checker's, and both fixture classes of `check-memory-hygiene.test.sh` still red.
- **S4** — Record the before and after wall clock for the leg in this build's own folder, measured
  the same way on the same node.

## 3. Non-goals (OUT)

- **N1** — No skip, cache, freeze or scoping mechanism. That is `TOOL-aThawedCorpus-2` and
  `TOOL-aThawedCorpus-3`, and buying a policy change to fix a performance bug is the wrong purchase
  in the wrong order. The precedent is `TOOL-aCollapsedScan-1`, which parked exactly that.
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

- **AC1** — When the changed checker runs over the full corpus and its stdout is diffed against the
  unchanged checker's, `diff` reports no difference.
- **AC2** — When `bash tools/memory-tree/check-memory-hygiene.test.sh` runs, it exits 0 and its red
  fixtures still red.
- **AC3** — When the instrumented per-check timing is re-taken on node `a` the same way, check 21's
  own span is under 30 s, against the 365.6 s recorded in this build's measurement record.
- **AC4** — When `python tools/memory-tree/check-arms.py --check` runs, it is green with
  `ARMS_FLOORS` for `tools/memory-tree/check-memory-hygiene.sh` unchanged at `20:20`.
- **AC5** — When the four projection outcomes are staged one at a time into a scratch corpus, each
  still produces its own `fail 21` text — a break observed RED, not asserted.

## 7. Gates

`memory hygiene` · `memory-hygiene self-test` · `harness arms (fail branches armed or pinned)` ·
`check-arms selftest` · `build README slot contract`. Adds no new gate; unit 3 owns the ceiling that
would have been this unit's left-shift.

## 8. Open questions

- **FACT-QUESTION · F1 — is the 365.6 s the projection loop, or the one `gen_build_index.py
  --print-bindings` invocation inside the same check?** The whole unit rests on the answer, and both
  are inside the tick boundary that measured 365.6 s. PROBE: time
  `python tools/memory-tree/gen_build_index.py --print-bindings > /dev/null` alone on node `a`, and
  time the `proj21` loop alone over its saved output. OBSERVATION THAT DECIDES IT: if the python
  invocation is the larger half, this unit is wrong and is re-specced against `--print-bindings`
  instead. LIVENESS: the probe can produce a negative — a python run over 310 records and every
  spec is capable of taking minutes on this node, and `TOOL-aMeteredTurnstile-6` records
  `python -c pass` at 103.7 ms to 1297 ms here, so a slow python half is a live possibility rather
  than a straw one.

- **F2 — does the `awk` pass need `FAM_ALT` interpolated, or passed with `-v`?** Recommendation:
  `-v`, matching check 12's driver, so the family alternation is data rather than program text.
  Immaterial to the verdict either way; recorded so the reviewer does not have to ask.

## 9. Revision log

- rev-1 · 2026-08-27 · initial draft, from the instrumented per-check measurement on node `a`.

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
