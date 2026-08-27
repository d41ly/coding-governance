# TOOL-aThawedCorpus-5 — check 23 gets the `--staged` guard its four siblings already have

**Status:** CLOSED · rev-3 · 2026-08-27 · node a · Tier-1 · base f1be0b49 · streams tooling · order 1

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-08-27-review-TOOL-aThawedCorpus-5-spec-audit.md](../reviews/2026-08-27-review-TOOL-aThawedCorpus-5-spec-audit.md) | spec-audit | TOOL-aThawedCorpus-4 TOOL-aThawedCorpus-1 TOOL-aThawedCorpus-2 TOOL-aThawedCorpus-3 |

<!-- /gen:spec-records -->

## 1. Goal

`check-memory-hygiene.sh:1114` opens check 23 with `if [ -n "$alcut" ]; then` — the cutoff only,
never `$STAGED`. Its four structural siblings all guard on `[ "$STAGED" = 0 ]`. So the one delegating
corpus-walker that never got the guard walks every spec and every record on every commit, whatever is
staged. Give it the guard. One line, and the largest single win in this build.

## 2. Scope (IN)

- **S1** — Change `:1114` to `if [ "$STAGED" = 0 ] && [ -n "$alcut" ]; then`, matching the shape at
  `:1051`, `:1066` and `:1076` exactly.
- **S2** — Record the before and after `--staged` wall clock on a VERIFIED-clean box, with the live
  `bash` process count reported at both ends of each run.
- **S3** — Write the compensating control into the checker's own header beside the change: what the
  pre-commit leg no longer covers, and which boundary covers it instead.

## 3. Non-goals (OUT)

- **N1** — No change to the FULL run. `bash tools/memory-tree/check-memory-hygiene.sh` with no
  arguments still executes check 23 over the whole corpus, and `TOOL-aThawedCorpus-4` is what makes
  that cheap. This unit only stops the pre-commit leg doing it.
- **N2** — Check 9's near-vacuous disjunct at `:599` is NOT fixed here. It reads
  `[ "$STAGED" = 0 ] || <memory/ staged>`, and `.githooks/pre-commit:48` only invokes the gate when
  `memory/**` is staged, so the right disjunct is true by construction and `gen_build_index.py
  --check` re-renders the whole index on every commit. It is a second mechanism and gets its own row,
  not a widening of this one.
- **N3** — No new conf key, no new flag, no change to what check 23 MEANS.

## 4. Design

### Data model

None. One conditional gains a conjunct.

### Rollout

First unit of the build, ahead of the two collapses, because it is one line and it is what the
per-pass commit discipline actually pays for. Every later pass in this run benefits from it.

### Files touched (estimate)

`tools/memory-tree/check-memory-hygiene.sh` — one line, plus a header paragraph for S3.

### Inventory

The two populations check 23 walks, DERIVED rather than typed, because a count written beside the
thing it counts is wrong on the next commit — this build has already watched all three of its
figures drift inside a day:

```bash
git ls-files 'memory/builds/*/spec/*.md' | wc -l                                  # the per-spec loop
git ls-files 'memory/builds/*/build/*.md' 'memory/builds/*/reviews/*.md' | wc -l   # the ledger pass
```

Check 21's population is a THIRD set, `build|prompts|reviews`, and is not check 23's. Conflating the
two is the error this section exists to stop.

### Alternatives rejected

- **Leave it and rely on `TOOL-aThawedCorpus-4`.** Rejected: the collapse makes check 23 cheap, but
  "cheap" over 317 specs and 307 records is still work the pre-commit leg has no reason to do. The
  two units compose — the guard removes the work, the collapse removes the cost of the work that
  remains.
- **Guard on the staged set rather than on `$STAGED`.** Rejected: check 23's verdict joins specs
  against records across the whole corpus, so a staged-scoped run of it would answer a different
  question. Off or whole, and the siblings already chose.

## 5. Production-readiness checklist

- security — N/A.
- perf / scale — the subject.
- a11y — N/A.
- i18n — N/A.
- error / empty / loading states — the `alpop = 0` liveness line is inside the guarded block, so
  under `--staged` check 23 now prints nothing at all. That is the same silence the four siblings
  already produce and is what S3 documents.
- observability — S3's header paragraph is the record; the leg's ledger row carries the duration.
- risks — this is a COVERAGE REDUCTION at the pre-commit boundary, and calling it anything else
  would be dishonest. The compensating control is `.githooks/pre-push`, which ALWAYS runs
  `run-gates.sh` at `:230`; what it decides at `:222` is only WHICH mode — `GATE_FULL=1` on the
  force branch, `GATE_BASE="$rec_sha"` on the scoped one. Guards are what `GATE_FULL` bypasses, and
  `memory hygiene` DECLARES NO GUARD, so it executes on both branches. The control therefore holds
  today, and it holds BECAUSE that leg is unguarded. `TOOL-aThawedCorpus-2` was retired partly to
  keep it that way: a guard on this leg would let a scoped push skip the very pass that compensates
  for what this unit removes. AC3 asserts the boundary in both directions.
- testing + left-shift gates — `check-memory-hygiene.test.sh` stays green; no `fail` branch moves, so
  `ARMS_FLOORS` stays `20:20`.
- migration / rollback — one line, revertable.
- user docs — the header paragraph. No user-facing surface.

## 6. Acceptance criteria

- **AC1** — When `bash tools/memory-tree/check-memory-hygiene.sh --staged` is timed on a box verified
  at three or fewer live `bash` processes, it completes in under 120 s, against the unguarded reading
  taken the same way.
- **AC2** — When the full `bash tools/memory-tree/check-memory-hygiene.sh` runs with no arguments,
  check 23 still executes and its output is byte-identical to the pre-change run's.
- **AC3** — When a spec is staged whose acceptance ledger is broken, `--staged` passes and the FULL
  run REDS on it — the coverage boundary observed in both directions rather than asserted.
- **AC4** — When `bash tools/memory-tree/check-memory-hygiene.test.sh` runs, it exits 0.
- **AC5** — When `python tools/memory-tree/check-arms.py --check` runs it is green with
  `ARMS_FLOORS` for `tools/memory-tree/check-memory-hygiene.sh` unchanged at `20:20`.

## 7. Gates

`memory hygiene` · `memory-hygiene self-test` · `harness arms (fail branches armed or pinned)` ·
`check-arms selftest`. Adds no new gate.

## 8. Open questions

none — the defect, the fix and the compensating boundary are all read directly from source, and the
measurement exists twice from two independent sessions.

## 9. Revision log

- rev-1 · 2026-08-27 · initial draft. Found late, from a `project` memory note written by another
  session on this node at 10:30 the same day; the defect and the sibling guards were then verified
  against source before this spec was written.
- rev-2 · 2026-08-27 · folded the M4 spec audit. Re-pinned `base` to a real default-branch sha after
  regrounding 39 commits. Corrected §5's compensating control: `.githooks/pre-push` always runs the
  bar and only chooses its MODE, and the control holds because `memory hygiene` is unguarded. Added
  §4 Inventory deriving both populations instead of quoting counts, after all three figures in this
  build drifted within a day.

- rev-3 · 2026-08-27 · CLOSED. Built and measured: `--staged` 683 s -> 20 s on a controlled pair,
  stdout identical, and AC3's coverage boundary observed in both directions with a real criterion
  staged into a live CLOSED Tier-2 spec. AC4 PASS 254 assertions, AC5 green at 20:20.
## 10. Reuse audit

The seam is the checker's OWN four sibling guards — `:667` for check 21, and `:1051`, `:1066`,
`:1076` for the three delegating blocks. This unit copies that shape rather than inventing one, which
is also why it needs no new declaration and moves no pin.

**Provenance, stated because it is not this session's measurement.** A `project` memory note on this
node, `hygiene-staged-leg-costs-16-minutes`, written 2026-08-27T10:30 by session
`6f20e318-fe74-4a21-a18f-37d2093b000a`, measured `--staged` uncontended at **963 s** as shipped and
**54 s** with check 23 guarded — 17.8x, and check 23 at 94% of the pre-commit leg. That note also
names check 9's vacuous disjunct, which N2 defers. Both claims were re-verified against source here;
the figures are cited, not re-derived, and S2 re-takes them on this branch.

`python tools/codebase-map/reuse_lookup.py "skip re-checking a memory build folder whose content has
not changed since it was last verified"` surfaced no seam for this — it is a one-line conjunct, and
the reuse that matters is the sibling shape above.

Recall terms used, because M7 re-runs the query: `cache freeze closed build corpus walk hygiene gate
fingerprint incremental stale mtime tree-hash rescan`.
