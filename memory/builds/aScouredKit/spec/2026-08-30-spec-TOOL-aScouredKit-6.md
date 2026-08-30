# TOOL-aScouredKit-6 — three per-file grep loops on the bar batch, at byte-identical output

**Status:** OPEN · rev-3 · 2026-08-30 · node a · Tier-1 · base 093730e4 · streams tooling

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-08-30-review-TOOL-aScouredKit-1-closing-round1.md](../reviews/2026-08-30-review-TOOL-aScouredKit-1-closing-round1.md) | diff-review | TOOL-aScouredKit-1 TOOL-aScouredKit-2 TOOL-aScouredKit-3 TOOL-aScouredKit-4 TOOL-aScouredKit-5 TOOL-aScouredKit-7 TOOL-aScouredKit-8 TOOL-aScouredKit-9 TOOL-aScouredKit-11 TOOL-aScouredKit-12 TOOL-aScouredKit-13 TOOL-aScouredKit-14 TOOL-aScouredKit-15 |

<!-- /gen:spec-records -->

## 1. Goal

Replace the one-process-spawn-per-file discovery loops in three shipped gate scripts with a single
batched invocation each, removing about a minute from every bar and removing a cost that scales with
an ADOPTER's whole repository rather than with the kit.

## 2. Scope (IN)

- S1. `tools/memory-tree/check-method-carriers.sh` — one `grep -lF` spawn per tracked file becomes
  one batched call. Measured 22.45 s to 0.69 s here, identical output.
- S2. `tools/unattended/check-playbook.sh` — 941 `grep -q` spawns to discover a population of one
  become one batched call. Measured 44.1 s to 1.17 s, same single result.
- S3. `tools/check-install-prefix.sh` — both per-file loops batched. The double
  `carried_population()` call on the `--check` path was ALSO in this scope and was NOT built: the
  measurement it rested on did not reproduce. The finders priced it at 2.11 s a call; re-measured
  on node `a` the whole leg runs in about 4 s and a call is nearer 1 s, so the hoist buys about a
  second against a real risk of changing which arm observes a dead population — and this leg's
  liveness assertion is the reason it reads the population twice. Dropped rather than deferred,
  and said here rather than left as a scope item nobody closed.
- S4. Every changed arm proves output equivalence by comparing the batched result against the
  unbatched one on THIS tree, byte for byte, and the comparison is recorded in §9.

## 3. Non-goals (OUT)

- Any change to what the three gates DECIDE. This is discovery cost only; a single differing byte
  of output fails S4 and the change is reverted rather than argued.
- The other legs on the bar. Three instances of one class are what this unit fixes; a repo-wide
  sweep for the class is a separate unit and is reported as a backlog row.
- Adding a guard to any of the three. Whether these legs should be repo-scoped is a separate
  question and holding them would hide the cost rather than remove it.

## 4. Design

All three share one shape: a `while read` loop over a file list with a `grep` spawn inside the body.
Process creation dominates — the class is already catalogued as
`memory/gotchas/process-creation-is-the-suite-cost.md`, and these three are fresh instances
authored after it was recorded, which is the argument that a memory note is not a control.

All three are `subject=repo` with `guard=[]`, so they run on EVERY bar in every adopting tree, and
`check-method-carriers.sh` iterates the adopter's tracked file count rather than the kit's.

### Inventory

| Script | Spawns | Before | After | Ships to adopters |
|---|---|---|---|---|
| `tools/memory-tree/check-method-carriers.sh:59` | 1156 | 22.45 s | 0.69 s | yes |
| `tools/unattended/check-playbook.sh:162` | 941 | 44.1 s | 1.17 s | yes, `kit.toml:96` |
| `tools/check-install-prefix.sh:67` and `:183` | 354 | 10.74 s + 19.24 s | 0.30 s + 0.28 s | yes |

The corrected arithmetic on the third: the post-fix leg is about 4.7 s rather than 0.63 s, because
the loop is not the whole leg. The 15 s saving holds; a 96 % figure would not.

### Alternatives rejected

Guarding the legs so they run less often. That hides the cost behind a scope rather than removing
it, and two of the three exist precisely to grade the whole repo.

## 5. Production-readiness checklist

- security — N/A.
- perf / scale — this IS the perf unit; the saving scales with the adopter's repo, not the kit's.
- a11y — N/A. i18n — N/A.
- error / empty / loading states — an empty file list must produce an empty result, not a `grep`
  reading stdin. Each batched form is exercised against an empty list.
- observability — each script's own output is the comparison subject.
- risks — a batched `grep` changes the exit-code contract: no-match exits 1 and fails a `&&` chain,
  which is a named class in the charter. Every changed site terminates its probe explicitly.
- testing + left-shift gates — the three legs themselves, plus `bash tools/check-install-prefix.sh`
  and `bash tools/unattended/run-unattended-gates.sh` on demand.
- migration / rollback — N/A, in-place edits to three scripts.
- user docs — N/A.

## 6. Acceptance criteria

- **AC1** — When each changed script runs before and after the change on this tree, the two outputs
  are byte-identical, proven by `diff` on captured stdout and recorded in §9.
- **AC2** — When `bash tools/memory-tree/check-method-carriers.sh` runs, it completes in under 5 s
  on node `a`, against 22.45 s at the base sha.
- **AC3** — When each changed arm is run against an EMPTY file list, it produces an empty result and
  does not block reading stdin — proven by driving each script with `git ls-files -- nosuchpath` as
  its population and observing a prompt-free exit.
- **AC4** — When `bash tools/run-gates/run-gates.sh` runs, it is green.

## 7. Gates

`method carriers` · `install prefix` · `playbook records` · the full bar at the push boundary.

## 8. Open questions

none

## 9. Revision log

- rev-1 · 2026-08-30 · initial draft, authored by the run under the standing mandate.
- rev-2 · 2026-08-30 · built, with AC1's byte-comparison recorded. Each leg was run from its
  committed bytes, then from the batched bytes, on node `a`, and the two stdouts diffed:
  `check-method-carriers.sh` 7652 ms to 2349 ms; `check-playbook.sh` 33467 ms to 6147 ms;
  `check-install-prefix.sh` 18399 ms to 3816 ms, with `--check` AND `--list` compared separately.
  All five comparisons byte-identical. 47.2 s off the leg-sum on this node. The lens's own
  figures (22.45 s, 44.1 s, 10.74+19.24 s) are not reproduced here and are not contradicted:
  they were taken on a differently-loaded machine, and what AC2 binds is the AFTER figure.
  S3's hoist is DROPPED, not deferred - see section 2; the closing review caught this spec still
  claiming it. TWO REGRESSIONS the closing review caught in the code, both mine and both in this
  file: a BARE `xargs` on both arms, where a path holding a quote aborts the invocation and one
  holding a space is split, with stderr eaten by `2>/dev/null` and the status by `|| true` - so
  the gate would print clean over files it never read, and the two siblings batched in the same
  commit used `-0` for exactly that reason. And a missing `-H`: `grep` omits the `<file>:` prefix
  when handed exactly ONE file, which both pipelines assume, so a single-file population fed the
  LINE NUMBER to `cut` as the path. Verified directly rather than argued. Both fixed at rev-3;
  output re-compared against the pre-change bytes and still byte-identical on both modes.
  ONE FIRST CUT WAS WRONG AND IS RECORDED RATHER THAN QUIETLY FIXED: the playbook change first
  round-tripped a NUL-delimited list through `$(...)`, which strips NUL bytes, so `xargs -0` got
  one mangled argument and the leg reported a population of 0 against a tree holding 1 - it
  REFUSED rather than passing, which is the direction that saves you. The list is piped straight
  through now, and the second predicate was deliberately left per-file so its `^```toml` anchor
  is unchanged; a batched `-F` pass would have widened the predicate rather than sped it up.

## 10. Reuse audit

The seam is `tools/check-agent-cap-restatement.sh`, the sibling gate that already carries a
"batching rejected" note explaining when the per-file form is REQUIRED — read first, and its reason
does not apply to these three, which is why they batch and it does not. No shared helper is
extracted: three bash scripts in three kits cannot import one, and the copy-installed kit model is
why. The build's reuse probe is recorded in `TOOL-aScouredKit-1` §10.
