# TOOL-aThawedCorpus-4 — hygiene check 23 stops spawning a process per spec and per record

**Status:** OPEN · rev-2 · 2026-08-27 · node a · Tier-1 · base 4f406bf7 · streams tooling · order 1

<!-- gen:spec-records -->

*No record names this unit.*

<!-- /gen:spec-records -->

## 1. Goal

Check 23, the acceptance-ledger check, is 962.0 s of a 1398 s full hygiene run on a quiet node `a` —
68.8% of the leg, measured directly. It spawns one `awk` per record over 310 records, then roughly eleven
processes per spec over ~250 specs, then one more `grep` per acceptance criterion. Collapse all three
loops to `awk` passes so the leg's largest term stops being process creation this repo controls.

## 2. Scope (IN)

- **S1** — Replace the `alledger` loop, `for r in $(git ls-files …); do awk … "$r"; done`, with ONE
  `awk` invocation taking every record path as an argument and emitting the same
  `<unit> <label> <form>` triples.
- **S2** — Replace the per-spec `for sp in $alspecs` prologue — the two `basename` spawns, the `cut`,
  the `sort -C` date comparison, the `sed | grep` header read, the `grep -qE` heading probe and the
  `sed | head` id read — with ONE `awk` pass that emits, per spec, only the specs that survive every
  filter, together with their unit id and their acceptance labels.
- **S3** — Replace the inner `for lab in $labs` membership loop, which runs a `grep` per criterion,
  with a lookup against a map built once in the same `awk` pass.
- **S4** — Preserve every one of the four outcomes and their exact `fail 23` texts: `algap`,
  `albad`, `alnolab`, and the `alpop = 0` liveness line that announces a check that measured nothing.
- **S5** — Preserve `ACCEPTANCE_LEDGER_GRANDFATHER` membership and `ACCEPTANCE_LEDGER_CUTOFF`
  comparison semantics exactly, including that the cutoff is compared as a string date and that the
  grandfather list is matched by whole id and never by pattern.
- **S6** — Record the before and after wall clock for the leg, measured the same way on the same node
  with the foreign-process count reported at both ends.

## 3. Non-goals (OUT)

- **N1** — No skip, cache or freeze. That is `TOOL-aThawedCorpus-2` and `TOOL-aThawedCorpus-3`, and
  it is deliberately sequenced after this unit so it is priced against the collapsed baseline rather
  than the current one.
- **N2** — No change to what check 23 MEANS. The ledger grammar, the two legal forms, the cutoff, the
  grandfather registry and the vacuity arm are untouched.
- **N3** — No change to `.memory-tree.conf`. `ACCEPTANCE_LEDGER_CUTOFF` and
  `ACCEPTANCE_LEDGER_GRANDFATHER` keep their values; a performance unit that moved a ratchet would be
  changing the verdict under cover of changing the cost.
- **N4** — No merging with `TOOL-aThawedCorpus-1`. Both units collapse a spawn loop, but they are two
  checks with two grammars, and one spec covering both would leave the closing diff unable to say
  which half a finding lands on.

## 4. Design

### Data model

Three passes become two `awk` invocations and one shell join.

The RECORD pass takes every tracked record under the two record roots as arguments and emits
`<unit> <label> <form>` exactly as the current per-file `awk` program does, with `FNR == 1` resetting
the `j` and `u` state that the current spelling gets for free from a fresh process per file. That
reset is the whole risk of S1 and it is what AC5 stages a break against.

The SPEC pass takes every tracked spec as arguments and emits, per surviving spec, one `SPEC` line
carrying the unit id followed by one `LAB` line per acceptance label. It reproduces the prologue's
filters in order: filename date at or after the cutoff, a status header in the first six unfenced
lines, `CLOSED`, `Tier-2`, an acceptance-criteria heading, and an `H1` id. A spec failing any filter
emits nothing, which is what `continue` does today.

The join stays in the shell, because the four `fail 23` branches must remain discoverable by
`check-arms.py`, which reads tracked shell and cannot see an `awk` `exit`.

### Migration

None. The checker is not a stored artifact.

### Files touched (estimate)

`tools/memory-tree/check-memory-hygiene.sh` — one block replaced, roughly 60 lines to 70.
`memory/builds/aThawedCorpus/build/` — the before/after measurement.

### Alternatives rejected

- **Move check 23 into `gen_build_index.py`.** Rejected on the same ground the checker's own header
  records for check 21: the `fail` branches would become Python raises that the arms gate cannot
  discover, and this repo pins that file at `20:20` in `ARMS_FLOORS`.
- **Pass paths on stdin instead of as arguments.** Rejected: `FILENAME` and `FNR` are what make the
  per-file state reset expressible, and a stdin stream has neither.
- **Skip specs that cannot reach the label loop, in the shell, before the `awk`.** Rejected as
  self-defeating — the prologue filters ARE the spawns, so filtering before the pass pays exactly the
  cost the pass exists to remove.

## 5. Production-readiness checklist

- security — N/A. Same bytes, same tracked population, no new input and no write path.
- perf / scale — this IS the subject; §6 carries the observable.
- a11y — N/A. A shell gate has no user interface.
- i18n — the passes use byte comparison and ASCII classes only, as the shell spelling did. The
  `sort -C` date comparison becomes a string compare on a fixed-width ISO date, which is the same
  relation without a locale in it.
- error / empty / loading states — a corpus with no surviving spec must still print the `alpop = 0`
  liveness line rather than nothing, which is what AC4 asserts.
- observability — the leg's own row in `<git-dir>/gate-ledger.tsv`.
- risks — an `awk` reading many files in one process carries state across file boundaries where a
  fresh process did not. That is the single real defect class here and AC5 stages it.
- testing + left-shift gates — `check-memory-hygiene.test.sh` stays green; `ARMS_FLOORS` for this
  file stays `20:20`, no `fail` branch added or removed. The recurring class itself is left-shifted by
  `TOOL-aThawedCorpus-3`, not here.
- migration / rollback — one commit, revertable.
- user docs — N/A.

## 6. Acceptance criteria

- **AC1** — When the changed checker runs over the full corpus and its stdout is diffed against the
  unchanged checker's, `diff` reports no difference.
- **AC2** — When `bash tools/memory-tree/check-memory-hygiene.test.sh` runs, it exits 0 and its red
  fixtures still red.
- **AC3** — When the instrumented per-check timing is re-taken on a quiet node `a`, check 23's own
  span is under 60 s, against the 962.0 s this build's measurement record carries, with the
  foreign-process count reported at both ends of the run.
- **AC4** — When every tracked spec is temporarily moved below `ACCEPTANCE_LEDGER_CUTOFF` in a
  scratch corpus, the checker still prints the `check 23 measured NO unit` liveness line.
- **AC5** — When two records are staged into a scratch corpus such that the first carries an
  `**Evidences:**` block and the second carries none, the changed `awk` attributes no triple from the
  first to the second — the per-file state reset observed RED before the `FNR == 1` guard is added,
  and green after.
- **AC6** — When `python tools/memory-tree/check-arms.py --check` runs it is green, with
  `ARMS_FLOORS` for `tools/memory-tree/check-memory-hygiene.sh` unchanged at `20:20`.

## 7. Gates

`memory hygiene` · `memory-hygiene self-test` · `harness arms (fail branches armed or pinned)` ·
`check-arms selftest`. Adds no new gate.

## 8. Open questions

- **FACT-QUESTION · F1 — is check 23's span really ~900 s, or is the remainder hiding a third term?**
  RESOLVED (agent, 2026-08-27, delegated): no third term. Measured DIRECTLY at **962.0 s**, from a
  tick on check 23's own `alcut=` line to process end, on a quiet node `a` with the foreign-process
  count zero at both ends. The subtraction this spec was drafted against said ~900 s, so the two
  agree to 6.9% and the §1 figure is now the span rather than the remainder. Checks 21 and 23
  together are 1300.9 s of 1398 s, 93.1%.

- **F2 — should the RECORD pass and the SPEC pass be one `awk` or two?** One would read both
  populations in a single process and save a spawn; two keep the two grammars separate and each
  readable on its own. Recommendation: TWO, because the populations are selected by different
  `git ls-files` patterns and a single pass would need a discriminator that the file lists already
  express. The saving is one process against several thousand.

## 9. Revision log

- rev-1 · 2026-08-27 · initial draft, from the quiet-box per-check measurement on node `a`.
- rev-2 · 2026-08-27 · F1 resolved by direct span (962.0 s) and §1 re-based on it; F2 resolved.

## 10. Reuse audit

The seam is this checker's own check 12 driver, which builds a tagged path stream in the shell and
hands it to one `awk` with `-v` bindings — the exact shape both this unit and `TOOL-aThawedCorpus-1`
extend. `TOOL-aBatchedLintel-1` built it for checks 12 and 7, porting `PERF-aSlothfulCapstan-1`;
`TOOL-aCollapsedScan-1` built the same collapse for `unattended.sh --plan` on 2026-08-26 and its
README carries the per-spawn cost measured on a node with an on-access scanner. No new seam is
invented here.

`python tools/codebase-map/reuse_lookup.py "skip re-checking a memory build folder whose content has
not changed since it was last verified"` returned `checks` at `tools/memory-tree/corpus_ids.py`,
`cmd_check` at `tools/memory-tree/row_grammar.py` and `build_cache` at
`tools/memory-recall/query.py`. The last is `TOOL-aThawedCorpus-2`'s business, not this unit's.

Recall terms used, because M7 re-runs the query: `cache freeze closed build corpus walk hygiene gate
fingerprint incremental stale mtime tree-hash rescan`. It surfaced `TOOL-aQuarriedLantern-1`'s review
finding F1, which establishes that this corpus's existing cache freshness key is mtime-based, and
`TOOL-aCollapsedScan-1`'s parked decision, which is the closest prior art to this whole build.
