# DEPL-dSealedTally-5 — the govkit self-test grades the tree, not the commit's ref-reachability

**Status:** SPECCED · rev-3 · 2026-09-04 · node d · Tier-2 · base 0f19429a · streams deployer · order 5

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-09-04-prompt-DEPL-dSealedTally-1-0-run-mandate.md](../prompts/2026-09-04-prompt-DEPL-dSealedTally-1-0-run-mandate.md) | journal | DEPL-dSealedTally-1 DEPL-dSealedTally-2 DEPL-dSealedTally-3 DEPL-dSealedTally-4 TOOL-dSealedTally-1 |
| [2026-09-04-review-DEPL-dSealedTally-1-spec-audit-round1.md](../reviews/2026-09-04-review-DEPL-dSealedTally-1-spec-audit-round1.md) | spec-audit | DEPL-dSealedTally-1 DEPL-dSealedTally-2 DEPL-dSealedTally-3 DEPL-dSealedTally-4 TOOL-dSealedTally-1 |
| [2026-09-04-review-DEPL-dSealedTally-1-spec-audit-round2.md](../reviews/2026-09-04-review-DEPL-dSealedTally-1-spec-audit-round2.md) | spec-audit | DEPL-dSealedTally-1 TOOL-dSealedTally-1 |

<!-- /gen:spec-records -->

## 1. Goal

`python tools/govkit/selftest.py` red 46 arms on a `--no-ff` merge commit made on a detached head,
and passed all 1074 over the byte-identical tree on a branch. The suite's real-root `update`
invocations default to `--to HEAD`, and `demand_published_vintage` refuses a commit no ref
contains. Pin those invocations to a ref-reachable commit carrying the SAME TREE, so the suite's
verdict is a function of the tree it grades.

## 2. Scope (IN)

- **S1** A pin is derived once and threaded into the real-root invocations: the `run(*args)` helper
  at `tools/govkit/selftest.py:69`, AND the direct `subprocess.Popen` at 2627, which runs
  `update --write` against the real checkout without going through `run()` and would otherwise stay
  unpinned — leaving AC1 unreachable by S1’s own mechanism.
- **S2** The pin is a ref-reachable commit whose `rev-parse <pin>^{tree}` EQUALS
  `rev-parse HEAD^{tree}`. Tree identity is the acceptance condition, not mere ref-reachability: an
  ancestor that is ref-reachable but carries a different tree grades the wrong tree, which is the
  same defect one level over.
- **S3** When no such commit exists, the suite prints a NAMED refusal and exits non-zero rather than
  falling back to `HEAD`.
- **S4** The fixtures that `apply` at gov HEAD have their receipt’s `gov_commit` REWRITTEN to the
  pin by the fixture itself, immediately after `apply` returns, so `demand_forward_vintage` holds
  reflexively. `apply` is NOT given a vintage argument: `_cmd_apply` hardcodes
  `git rev-parse HEAD` at `tools/govkit/govkit.py:4199` and `main` dispatches it with no `TO_REV`,
  so pinning it would add a public surface to a product verb — M3 veto 2, which is an owner turn
  this run cannot take. The fixture edit is test-only and keeps §4 Files touched honest.
- **S5** A liveness arm asserting BOTH conditions of the pin — that its tree equals the working
  tree's, and that some ref contains it. Either alone is satisfied by a silently-defaulted `HEAD`.
- **S6** Neither `demand_published_vintage` nor `demand_forward_vintage` is changed. Both are
  correct guards; the bug is the argument the suite hands them.

## 3. Non-goals (OUT)

- Not touching the scratch-gov invocations. 27 scratch repositories are built by
  `git init -q -b main` plus one commit, and a sha from the real checkout does not exist in their
  object databases at all — threading the pin there would convert a 46-arm failure into a near-total
  one.
- Not touching any invocation that already carries its own `--to`. 32 of the 74 do, several taking a
  deliberate per-fixture vintage from a scratch repo's own history, and a blanket pin would clobber
  what those arms grade.
- Not relaxing either vintage guard. Refusing a vintage no ref names is what stops a branch nobody
  shipped becoming an adopter's baseline; refusing a downgrade is what stops a rewind being recorded
  as an update.
- Not making the `govkit selftest` leg skip on a detached head. A skip that looks like a pass is the
  class this repo gates against; the suite should RUN and grade the tree.

## 4. Design

### Data model

One module-level value in `tools/govkit/selftest.py`, resolved before any arm runs, and threaded
through the `run(*args)` helper alone.

### Inventory

The population, counted rather than asserted — rev-1 said "every `update` invocation" and that was
false of all three groups:


| Group | Count | Pin applies |
|---|---|---|
| `update` invocations in the suite | 74 | — |
| carrying an explicit `"--to"` ARGUMENT | 13 | no, untouched |
| — of which inline in a `run()` call | 9 | the quantity AC5 counts |
| against a scratch gov repo | 27 repos | no, the sha does not exist there |
| real-root, via `run()` at line 69 plus the direct `Popen` at 2627 | the remainder | YES |

Rev-2 said "32 of the 74" and that was a LINE count — lines mentioning `--to` anywhere, prose and
comments included — wrong by about 2.5x. The argument count is 13, measured with
`grep -o '"--to"' tools/govkit/selftest.py | wc -l`, and 9 of those are inline in a `run()` call.
AC5 counts the 9, because that is the quantity its arm can compute from the file.

### Migration

The derivation, spelled as one runnable sequence rather than two candidates neither of which ran:

```bash
T=$(git rev-parse HEAD^{tree})
if [ -n "$(git for-each-ref --contains HEAD --count=1)" ]; then
  PIN=$(git rev-parse HEAD)                 # ordinary case: HEAD is ref-reachable
else
  PIN=""
  for p in $(git rev-parse HEAD^@); do      # every parent, not just the first
    [ "$(git rev-parse "$p^{tree}")" = "$T" ] || continue
    [ -n "$(git for-each-ref --contains "$p" --count=1)" ] || continue
    PIN=$p; break
  done
fi
```

Measured on a scratch repository holding a detached `--no-ff` merge: HEAD tree `02573c73`,
parent^1 `0aa8969` tree `3be22be7` (ref-reachable but the WRONG tree), parent^2 `741af85` tree
`02573c73` (ref-reachable and the right one). `HEAD^` would have picked parent^1, which is why
rev-1's `^` spelling was wrong and why the loop tests every parent.

`PIN` empty is S3's refusal. It is NOT a fallback to `HEAD`: falling back is what makes a broken
derivation indistinguishable from a working one.

### Rollout

The pin is threaded at one helper, so a future edit widening it is visible in one place.

### Files touched (estimate)

`tools/govkit/selftest.py` (~70 lines: the resolution, its refusal, the `--to` threading through
`run(*args)`, the apply-at-pin change for S4, and the liveness arm).

### Alternatives rejected

Creating a temporary ref pointing at `HEAD` for the duration of the suite. Rejected: it mutates the
repository the suite is grading, and a crashed run leaves the ref behind.

Deriving the pin as `HEAD^` or "the nearest described ancestor", which is what rev-1 said. Rejected
on measurement, above: for a merge, `^` is the pre-merge base and its tree is not the tree under
test.

## 5. Production-readiness checklist

- security — N/A — a test harness change; neither guard it stops tripping is touched.
- perf / scale — one `for-each-ref` and at most a handful of `rev-parse` calls per suite run, not
  per arm.
- a11y — N/A.
- i18n — N/A.
- error / empty / loading states — a repository with no ref-reachable same-tree commit is S3's
  named refusal, which is the empty case and is not a fallback.
- observability — the suite prints the pin it resolved and which branch it took, so a reader can
  tell a pinned run from a defaulted one without reading the code.
- risks — the derivation picking a ref-reachable commit with a DIFFERENT tree would grade the wrong
  tree silently. S2 makes tree identity the acceptance condition and S5's arm asserts both halves,
  which is the mitigation actually covering the risk — rev-1 named a mitigation that did not.
- testing + left-shift gates — S5's liveness arm, plus an arm counting explicitly-pinned `update`
  invocations against a declared number, so a future edit widening the pin reds rather than quietly
  re-pointing fixtures.
- migration / rollback — reverting the commit is the rollback.
- user docs — N/A.

## 6. Acceptance criteria

- **AC1** — When `python tools/govkit/selftest.py` runs on a detached `--no-ff` merge commit whose
  tree matches a branch tip, it exits 0, where at base `0f19429a` it exits 1 with 46 failing arms.
- **AC2** — When `python tools/govkit/selftest.py` runs on that same tree checked out as a branch,
  it still exits 0, so the fix does not trade one head shape for another.
- **AC3** — When the pin is resolved, an arm in `tools/govkit/selftest.py` asserts BOTH that
  `rev-parse <pin>^{tree}` equals `rev-parse HEAD^{tree}` AND that some ref contains the pin — the
  liveness assertion, failing if the resolution silently returned an unpinned `HEAD`.
- **AC4** — When no ref-reachable same-tree commit exists, `tools/govkit/selftest.py` prints a named
  refusal and exits non-zero, proved by an arm driving the resolution against a fixture repository
  with no refs.
- **AC5** — When the suite runs, the number of `run()` invocations carrying their own inline
  `"--to"` is 9, unchanged from base `0f19429a`, asserted by an arm in `tools/govkit/selftest.py`
  so a future edit widening the pin reds rather than quietly re-pointing fixtures.
- **AC6** — When a fixture’s receipt has its `gov_commit` rewritten to the pin after `apply` and
  is then updated to the pin, `demand_forward_vintage` does not refuse it, proved by an arm in
  `tools/govkit/selftest.py` exercising the apply-rewrite-update path on a detached head.
- **AC7** — When `python tools/govkit/selftest.py` runs, its arm count is at least 4 greater than
  the count observed at the head of `order 4`, captured in §9 when this unit's pass opens.

## 7. Gates

`govkit selftest` · `bash tools/run-gates/run-gates.sh` with `GATE_FULL=1 GATE_SELFTESTS=1`, run
once from a detached merge commit as AC1's own observation.

## 8. Open questions

none

## 9. Revision log

- rev-1 · 2026-09-04 · initial draft. The 92/93 and 1074/1074 figures are from `dRatifiedSeam`'s
  own landing, recorded in its closing diff review.
- rev-2 · 2026-09-04 · folded the spec audit's B3, B5, H4, H12 and M2, and raised the tier from 1 to
  2 because the unit turned out to touch a guarded argument's whole path. B3: rev-1 said "every
  `update` invocation" and the population is three groups, not one — 74 total, 32 already pinned, 27
  scratch repositories whose object databases do not hold a real-root sha; §3 and the Inventory now
  count them. B5: `demand_forward_vintage` at `tools/govkit/govkit.py:4129` runs first and refuses
  an ancestor pin as a downgrade, which made rev-1's AC1 unsatisfiable by any implementation; S4 and
  AC6 close it by applying fixtures at the pin. H4 and H12: the derivation now requires TREE
  IDENTITY, measured against a real detached merge where `^` picks the wrong-tree parent. M2:
  the derivation is one runnable sequence with its empty case named, replacing two candidates
  neither of which ran. Order moved 3 to 5 per M1.
- rev-3 · 2026-09-04 · folded round 2’s B2, H2 and H3. B2: rev-2’s S4 pinned `apply` to a vintage
  `apply` has no parameter for — `_cmd_apply` hardcodes `rev-parse HEAD` at 4199 — so the fix as
  written needed a product-surface change §4 never budgeted; S4 now rewrites the fixture’s
  `gov_commit` instead, keeping the unit test-only because adding `apply --to` trips M3 veto 2.
  H2: the "32 of 74" row was a LINE count, wrong by 2.5x; the argument count is 13 and AC5 now
  counts the 9 it can actually compute. H3: a real-root `update --write` runs outside `run()` at
  `tools/govkit/selftest.py:2627` and would have stayed unpinned, making AC1 unreachable.

## 10. Reuse audit

No existing seam fits — `tools/govkit/selftest.py` has no vintage-resolution layer today, which is
the coupling being removed; `python tools/codebase-map/reuse_lookup.py "resolve a ref-reachable
commit for a working tree"` returned no candidate in the suite's harness layer, and both vintage
guards are things this unit satisfies rather than seams it extends.

`memory/backlog/DEPL.md` carries `DEPL-dRatifiedSeam-6` as the row this unit closes; no other OPEN
DEPL row names `tools/govkit/selftest.py`'s vintage handling.

Recall terms used: `govkit update receipt rollback verify snapshot touched_kits landing unclaimed
sources liveness dead probe index_read topology`
