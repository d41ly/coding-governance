# DEPL-dSealedTally-4 — `index_read` asserts git's exit code instead of reading failure as absence

**Status:** SPECCED · rev-1 · 2026-09-04 · node d · Tier-2 · base 0f19429a · streams deployer · order 1

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-09-04-prompt-DEPL-dSealedTally-1-0-run-mandate.md](../prompts/2026-09-04-prompt-DEPL-dSealedTally-1-0-run-mandate.md) | journal | DEPL-dSealedTally-1 DEPL-dSealedTally-2 DEPL-dSealedTally-3 DEPL-dSealedTally-5 TOOL-dSealedTally-1 |

<!-- /gen:spec-records -->

## 1. Goal

`index_read` batches paths 400 at a time into `git ls-files -s -z` with `check=False` and never
looks at the exit code. A chunk that fails produces empty stdout, so every path in it reads
absent-from-index — a reassuring answer that is indistinguishable from the truth. Make a failed
read say so.

## 2. Scope (IN)

- **S1** `index_read` inspects `out.returncode` for every chunk and raises a `Refusal` naming the
  chunk's first path, the exit code, and git's stderr, rather than returning a silently empty map.
- **S2** The refusal states what the caller would otherwise have concluded — that these paths are
  absent from the index — so the operator reads a diagnosis and not just a failure.
- **S3** A staged-RED arm that forces a chunk to fail and asserts the refusal, plus a negative arm
  proving an ordinary read still returns its map.

## 3. Non-goals (OUT)

- Not changing the 400-path batch size. Whether that number is right is a separate question and
  nothing here depends on it.
- Not adding a retry. A failing `ls-files` is a broken invocation or a broken repository, and
  retrying either produces the same answer more slowly.
- Not auditing the other `check=False` call sites in `tools/govkit/govkit.py`. This unit closes the
  one with a measured dead-probe shape; a sweep is a separate unit if the closing review wants one.

## 4. Design

### Data model

Unchanged. `index_read` keeps returning `(at_stage0, present)`; it simply stops returning them when
it does not know them.

### Migration

None.

### Rollout

A refusal where there was silence. The risk direction is a run that now stops rather than
proceeding on bad data, which is the intended trade: `update` writes into a repository gov does not
own, and proceeding on a false "absent" is how it decides a path is free to write.

### Files touched (estimate)

`tools/govkit/govkit.py` (~15 lines: the returncode check and its refusal text).
`tools/govkit/selftest.py` (~35 lines: the forced-failure arm and its negative).

### Alternatives rejected

Returning a third value meaning "unknown" and letting each caller decide. Rejected: there are
several callers, each would need the same decision, and a caller that forgot would reproduce
exactly the bug being fixed. A refusal at the read is one decision in one place.

## 5. Production-readiness checklist

- security — the bug's consequence is a write decision taken on a false absence, in a foreign
  repository. Closing it narrows that surface.
- perf / scale — one integer comparison per chunk.
- a11y — N/A — a CLI verb with no rendered surface.
- i18n — N/A — operator-facing English.
- error / empty / loading states — an EMPTY path list still returns empty maps without invoking
  git, which the existing `if not chunk` guard already handles and this change must not disturb.
- observability — the refusal names the exit code and stderr, so the operator sees git's own words.
- risks — a run that previously limped now refuses. That is the point, and the refusal names the
  remedy rather than leaving the operator stuck.
- testing + left-shift gates — S3's arms are the left-shift; the positive fails before the change.
- migration / rollback — reverting the commit is the rollback.
- user docs — N/A.

## 6. Acceptance criteria

- **AC1** — When a chunk's `git ls-files` invocation exits non-zero, `index_read` in
  `tools/govkit/govkit.py` raises a `Refusal` rather than returning an empty map, proved by a new
  arm in `tools/govkit/selftest.py`.
- **AC2** — When that refusal is printed, it names the exit code and the first path of the failing
  chunk, asserted by substring in `tools/govkit/selftest.py`.
- **AC3** — When an ordinary read runs over a healthy fixture, `index_read` returns the same two
  maps as at base `0f19429a`, so the check adds no behaviour on the success path.
- **AC4** — When `index_read` is handed an empty path list, it returns empty maps without invoking
  git, proved by an arm asserting no subprocess is spawned in `tools/govkit/selftest.py`.
- **AC5** — When the returncode check is reverted in a scratch copy of `tools/govkit/govkit.py`, the AC1 arm FAILS, recorded as
  an observed staged break rather than asserted.

## 7. Gates

`govkit selftest` · `memory-hygiene` · `bash tools/run-gates/run-gates.sh` with
`GATE_FULL=1 GATE_SELFTESTS=1`.

## 8. Open questions

- **F1 — `Refusal` or a returned error?** `Refusal` is the file's own vocabulary for an operator
  error and is caught at the verb boundary, but `index_read` is also called from the snapshot path
  where a raise aborts a run mid-write. Options: raise always, or raise only on the read-only
  preflight read. Recommendation: raise always, because a snapshot built on a false absence is
  worse than an aborted run — the rollback pass depends on that snapshot being true.
  RESOLVED (agent, 2026-09-04, delegated): raise always, per the recommendation. A snapshot that
  records a path as absent when it is not cannot roll that path back.

## 9. Revision log

- rev-1 · 2026-09-04 · initial draft, grounded against `tools/govkit/govkit.py` lines 3752-3785 at
  `0f19429a`, where no `returncode` read exists in the function body.

## 10. Reuse audit

`python tools/codebase-map/reuse_lookup.py "batched git index read with a liveness assertion"` returned no candidate in this layer, so for a NEW reader no existing seam fits — but none is wanted, because the seam is `index_read` in `tools/govkit/govkit.py`, which is already the single batched index
reader that `DEPL-dCarriedReceipt-7` consolidated — the snapshot path deliberately routes its
extra lookups back through it rather than opening a second call site. That is why one liveness
assertion here covers every caller, and why no new helper is warranted.

Recall terms used: `govkit update receipt rollback verify snapshot touched_kits landing unclaimed
sources liveness dead probe index_read topology`
