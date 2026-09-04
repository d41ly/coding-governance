# DEPL-dSealedTally-5 — the govkit self-test grades the tree, not the commit's ref-reachability

**Status:** CLOSED · rev-4 · 2026-09-04 · node d · Tier-2 · base 0f19429a · streams deployer · order 5

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-09-04-build-DEPL-dSealedTally-5-1-acceptance-ledger.md](../build/2026-09-04-build-DEPL-dSealedTally-5-1-acceptance-ledger.md) | journal | — |
| [2026-09-04-prompt-DEPL-dSealedTally-1-0-run-mandate.md](../prompts/2026-09-04-prompt-DEPL-dSealedTally-1-0-run-mandate.md) | journal | DEPL-dSealedTally-1 DEPL-dSealedTally-2 DEPL-dSealedTally-3 DEPL-dSealedTally-4 TOOL-dSealedTally-1 |
| [2026-09-04-review-DEPL-dSealedTally-1-closing-diff-round1.md](../reviews/2026-09-04-review-DEPL-dSealedTally-1-closing-diff-round1.md) | diff-review | DEPL-dSealedTally-1 DEPL-dSealedTally-2 DEPL-dSealedTally-3 DEPL-dSealedTally-4 TOOL-dSealedTally-1 |
| [2026-09-04-review-DEPL-dSealedTally-1-spec-audit-round1.md](../reviews/2026-09-04-review-DEPL-dSealedTally-1-spec-audit-round1.md) | spec-audit | DEPL-dSealedTally-1 DEPL-dSealedTally-2 DEPL-dSealedTally-3 DEPL-dSealedTally-4 TOOL-dSealedTally-1 |
| [2026-09-04-review-DEPL-dSealedTally-1-spec-audit-round2.md](../reviews/2026-09-04-review-DEPL-dSealedTally-1-spec-audit-round2.md) | spec-audit | DEPL-dSealedTally-1 TOOL-dSealedTally-1 |
| [2026-09-04-review-DEPL-dSealedTally-1-spec-audit-round3.md](../reviews/2026-09-04-review-DEPL-dSealedTally-1-spec-audit-round3.md) | spec-audit | DEPL-dSealedTally-1 |

<!-- /gen:spec-records -->

## 1. Goal

`python tools/govkit/selftest.py` red 46 arms on a `--no-ff` merge commit made on a detached head,
and passed all 1074 over the byte-identical tree on a branch. The suite's real-root `update`
invocations default to `--to HEAD`, and `demand_published_vintage` refuses a commit no ref
contains. Pin those invocations to a ref-reachable commit carrying the SAME TREE, so the suite's
verdict is a function of the tree it grades.

## 2. Scope (IN)

- **S1** A pin is derived once and threaded into the real-root invocations at BOTH sites: the
  `run(*args)` helper at `tools/govkit/selftest.py:69`, and the direct `subprocess.Popen` at 2627,
  which runs `update --write` against the real checkout without going through `run()` and would
  otherwise stay unpinned — leaving AC1 unreachable by S1's own mechanism.
- **S2** The pin is a ref-reachable commit whose `rev-parse <pin>^{tree}` EQUALS
  `rev-parse HEAD^{tree}`. Tree identity is the acceptance condition, not mere ref-reachability: an
  ancestor that is ref-reachable but carries a different tree grades the wrong tree, which is the
  same defect one level over.
- **S3** When no such commit exists, the suite prints a NAMED refusal and exits non-zero rather than
  falling back to `HEAD`.
- **S4** The fixtures that `apply` at gov HEAD have their receipt's `gov_commit` REWRITTEN to the
  pin by the fixture itself, immediately after `apply` returns, so `demand_forward_vintage` holds
  reflexively.
- **S5** Every arm resolving the REAL govroot at `HEAD` is re-pointed at the pin. There are exactly
  three, enumerated in §4, and they are not optional: a pinned `update` writes the PIN's bytes and
  stamps the PIN's sha, so an arm still comparing against `HEAD` reds on a correct fix and
  contradicts AC1.
- **S6** A liveness arm asserting BOTH conditions of the pin — that its tree equals the working
  tree's, and that some ref contains it. Either alone is satisfied by a silently-defaulted `HEAD`.
- **S7** Neither `demand_published_vintage` nor `demand_forward_vintage` is changed. Both are
  correct guards; the bug is the argument the suite hands them.

## 3. Non-goals (OUT)

- Not touching the scratch-gov invocations. 27 scratch repositories are built by
  `git init -q -b main` plus one commit, and a sha from the real checkout does not exist in their
  object databases at all — threading the pin there would convert a 46-arm failure into a near-total
  one.
- Not re-pointing any of the 13 `"--to"` argument tokens the suite already passes. Four are in
  real-root `run()` calls and nine are elsewhere, several taking a deliberate per-fixture vintage
  from a scratch repo's own history; the §4 Inventory row is the count, and this bullet does not
  restate it.
- Not relaxing either vintage guard. Refusing a vintage no ref names is what stops a branch nobody
  shipped becoming an adopter's baseline; refusing a downgrade is what stops a rewind being recorded
  as an update.
- Not giving `apply` a vintage argument. `_cmd_apply` hardcodes `git rev-parse HEAD` at
  `tools/govkit/govkit.py:4199` and `main` dispatches it with no `TO_REV`, so pinning it would add a
  public surface to a product verb — M3 veto 2, an owner turn this run cannot take.
- Not making the `govkit selftest` leg skip on a detached head. A skip that looks like a pass is the
  class this repo gates against; the suite should RUN and grade the tree.

## 4. Design

### Data model

One module-level value in `tools/govkit/selftest.py`, resolved before any arm runs, and threaded at
the two sites S1 names: the `run(*args)` helper at 69 and the direct `Popen` at 2627. Two, not one —
stating "one place" would be the same overstatement this spec has already made twice about
populations.

### Inventory

Three populations, each measured with a command rather than asserted. Rev-2 said "every `update`
invocation" and rev-3 said "9", and both were wrong in the same way: a substring count.

| Population | Count | Command | Pin applies |
|---|---|---|---|
| `"update"` argument tokens | 74 | `grep -o '"update"' … \| wc -l` | — |
| `"--to"` argument tokens | 13 | `grep -o '"--to"' … \| wc -l` | no, untouched |
| — of which in a strict `run()` call | 4 | `grep -cE '(^\|[^_[:alnum:]])run\(.*"--to"' …` | no, untouched |
| — of which in `gov_run()` | 5 | `grep -c 'gov_run(.*"--to"' …` | no, out of scope |
| scratch gov repositories | 27 | `grep -c 'git init -q -b main' …` | no, the sha is absent there |
| real-root arms resolving `HEAD` | 3 | lines 386, 579, 586 | YES — S5 re-points them |

Rev-3's "9" came from `grep -c 'run(.*"--to"'`, which matches `gov_run(` as a substring: 4 + 5 = 9.
The anchored pattern in the table is what excludes it, and AC5 counts 4 by that pattern.

The three real-root `HEAD` sites, which S5 re-points:

| Line | What it does |
|---|---|
| 386 | `idx_of` reads `HEAD:<path>` blobs from the real govroot |
| 579 | `head_bytes` reads `HEAD:tools/check-wiring.sh` and is compared to what `update` wrote |
| 586 | asserts a receipt's `gov_commit` equals `rev-parse HEAD` of the real govroot |

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

The pin is threaded at TWO sites, both named in the Data model, so a future edit widening it has two
places to look rather than one. Two is the floor, not a compromise: the direct `Popen` at 2627 does
not go through `run()` and cannot be reached by threading `run()` alone.

### Files touched (estimate)

`tools/govkit/selftest.py` (~110 lines): the pin resolution and its named refusal; the conditional
`--to` threading in `run(*args)` at 69; the same threading at the direct `Popen` at 2627; the
post-`apply` `gov_commit` rewrite for S4; the three `HEAD` re-points at 386, 579 and 586 for S5; the
liveness arm; and the pinned-invocation count arm for AC5.

### Alternatives rejected

Creating a temporary ref pointing at `HEAD` for the duration of the suite. Rejected: it mutates the
repository the suite is grading, and a crashed run leaves the ref behind.

Deriving the pin as `HEAD^` or "the nearest described ancestor", which is what rev-1 said. Rejected
on measurement, above: for a merge, `^` is the pre-merge base and its tree is not the tree under
test.

Giving `apply` a `--to`, which is what rev-2 said. Rejected under M3 veto 2, per §3.

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
  tree silently. S2 makes tree identity the acceptance condition and S6's arm asserts both halves.
  The second risk is S5's: a pinned write compared against `HEAD` bytes reds on a correct fix, which
  is why the three sites are enumerated rather than described.
- testing + left-shift gates — S6's liveness arm, plus AC5's count arm, so a future edit widening
  the pin reds rather than quietly re-pointing fixtures.
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
- **AC5** — When the suite runs, the number of strict `run()` invocations carrying their own inline
  `"--to"` is 4, unchanged from base `0f19429a`, asserted in `tools/govkit/selftest.py` by the
  anchored pattern `(^|[^_[:alnum:]])run\(.*"--to"` — the unanchored form counts `gov_run` and
  returns 9, which is the miscount rev-3 shipped.
- **AC6** — When a fixture's receipt has its `gov_commit` rewritten to the pin after `apply` and is
  then updated to the pin, `demand_forward_vintage` does not refuse it, proved by an arm in
  `tools/govkit/selftest.py` exercising the apply-rewrite-update path on a detached head.
- **AC7** — When the suite runs on a detached head where the pin differs from `HEAD`, the three arms
  at `tools/govkit/selftest.py` lines 386, 579 and 586 compare against the PIN and pass; reverting
  any one of them to `HEAD` makes it FAIL, recorded as an observed staged break.
- **AC8** — When `python tools/govkit/selftest.py` runs, its arm count is at least 4 greater than
  the count observed at the head of `order 4`, captured in §9 when this unit's pass opens.

## 7. Gates

`govkit selftest` · `bash tools/run-gates/run-gates.sh` with `GATE_FULL=1 GATE_SELFTESTS=1`, run
once from a detached merge commit as AC1's own observation.

## 8. Open questions

none

## 9. Revision log

- rev-1 · 2026-09-04 · initial draft. The 92/93 and 1074/1074 figures are from `dRatifiedSeam`'s
  own landing, recorded in its closing diff review.
- rev-2 · 2026-09-04 · folded B3, B5, H4, H12 and M2, and raised the tier from 1 to 2. B3: the
  population is three groups, not one. B5: `demand_forward_vintage` refuses an ancestor pin as a
  downgrade. H4 and H12: the derivation requires TREE IDENTITY. M2: one runnable sequence.
- rev-3 · 2026-09-04 · folded round 2's B2, H2 and H3. B2: `apply` has no vintage parameter, so S4
  rewrites the fixture's `gov_commit` instead. H2: the "32 of 74" row was a line count. H3: a
  real-root `update` runs outside `run()` at 2627.
- rev-4 · 2026-09-04 · folded round 3, which returned MORE blockers than round 2, so the subject is
  NON-CONVERGENT and this is the disposal fold — the loop stops here and every standing blocker is
  folded, per the build method. B3 added S5: a pinned `update` writes the pin's bytes and stamps the
  pin's sha, so the three arms still resolving the real govroot at `HEAD` would red on a correct
  fix; they are enumerated at 386, 579 and 586 and graded by AC7. B4: rev-3's "9" was a SUBSTRING
  count — `grep 'run(.*"--to"'` matches `gov_run(`, and 4 + 5 = 9; the strict figure is 4, the
  Inventory now spells every measuring command, and AC5 names the anchored pattern. H5 rewrote the
  §3 bullet to the measured split. H6 corrected the Data model, Rollout and Files touched, which had
  all still described a single threading site after rev-3 added a second.

## 10. Reuse audit

No existing seam fits — `tools/govkit/selftest.py` has no vintage-resolution layer today, which is
the coupling being removed; `python tools/codebase-map/reuse_lookup.py "resolve a ref-reachable
commit for a working tree"` returned no candidate in the suite's harness layer, and both vintage
guards are things this unit satisfies rather than seams it extends.

`memory/backlog/DEPL.md` carries `DEPL-dRatifiedSeam-6` as the row this unit closes; no other OPEN
DEPL row names `tools/govkit/selftest.py`'s vintage handling.

Recall terms used: `govkit update receipt rollback verify snapshot touched_kits landing unclaimed
sources liveness dead probe index_read topology`
