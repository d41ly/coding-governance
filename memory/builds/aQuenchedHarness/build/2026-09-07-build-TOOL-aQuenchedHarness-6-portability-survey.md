# Which of the costly suites can actually be ported, and what the remainder costs

**Serves:** research TOOL-aQuenchedHarness-6

Node `a`, 2026-09-07. Spec §S3 selects the suites to rebuild in descending recorded seconds until
the selected set carries the declared majority share; §S9 requires every suite NOT ported to be
NAMED with its recorded cost. This is that survey, over the twelve costliest rows of
`tools/run-gates/selftest-budgets.txt` after the first port. Four readers, one per group, each
reading the harness and the already-ported suite first and then reporting from source.

## The verdicts

| leg | recorded | verdict | arms | mappable | effort | extractable |
|---|---|---|---|---|---|---|
| manifest-check self-test | 2547 s | **partial** | 62 | 62 | large | yes |
| run-gates turnstile | 2419 s | **partial** | 65 | 41 | large | yes |
| check-wiring self-test | 2192 s | **partial** | 95 | 40 | large | yes |
| run-gates evidence | 1500 s | **partial** | 51 | 20 | large | yes |
| install-prefix self-test | 783 s | **partial** | 30 | 28 | medium | yes |
| run-gates canary | 2436 s | **no** | 123 | 0 | large | NO |
| row-keyed merge driver replay | 1077 s | **no** | 217 | 0 | large | NO |
| govkit selftest | 1065 s | **no** | 1054 | 0 | large | yes |
| drift-audit selftest | 855 s | **no** | 168 | 0 | large | yes |
| memory-recall kit selftest | 835 s | **no** | 44 | 0 | large | NO |
| memory-hygiene self-test | 808 s | **no** | 289 | 14 | large | NO |
| corpus-ids selftest | 715 s | **no** | 54 | 0 | large | yes |

## What that means for the share

**Not one of the twelve is portable under this unit's own rules without changing them, and the
declared majority share is therefore NOT met.** That is the finding, and it is written here rather
than resolved by lowering the number: §S6 exists because rev-1 paired a criterion with a threshold
it could not fail, and moving a share to fit the result is the same defect wearing the opposite
sign. The share stays at 0.50 in the declaration and this build does not reach it.

Four independent reasons, each fatal on its own:

- **Three are python suites.** `govkit selftest`, `drift-audit selftest` and `corpus-ids selftest`
  drive module internals in-process, mostly with no CLI entrypoint at all. The harness is a bash
  library whose `arm` takes shell strings with an exit code, so a "port" is a rewrite of the suite
  AND of the module surface it grades. `corpus-ids` would also be SLOWER: 54 arms means 54 python
  spawns at ~773 ms, about 42 s of new cost added to a 95 s suite, to parallelise ~127 git spawns.
- **Two have inventories that cannot be recovered.** `run-gates canary` and
  `row-keyed merge driver replay` print no comparable per-arm line, and
  `memory-hygiene self-test` is worse than either: it prints 14 readable lines against 289 executed
  assertions, which the extractor used to return as a confident 14-arm inventory. That defect was
  found here and fixed in the extractor; the suite is still unportable, and now it says so.
- **Four need the arms to share state a pool destroys.** `run-gates turnstile` needs two and three
  runners live against ONE repository at once and grades a peak-occupancy count; `install-prefix`
  has two LIVENESS arms whose LABELS embed a running counter incremented across arms
  (`LIVENESS 11 arm(s) actually engaged the carried-prefix branch`), so a per-arm `cp -a` copy
  makes those two labels unreproducible and the inventory diff non-empty BY CONSTRUCTION —
  which §S5 says is a defect in the port, not a judgement call.
- **The rest need assertions the harness does not have.** A want-substring-ABSENT verb (56
  assertions in memory-hygiene, 8 in install-prefix, all 62 in manifest-check via its
  no-raw-`fatal:` contract), a structural silent-clean predicate, an rc-inequality comparison, and
  slicing a capture per check rather than searching the whole of it.

## The one that is worth a follow-up, and what it needs

`skills/session-kickoff/manifest-check.test.sh` — the single costliest row at 2547 s, 62 of 62
arms mappable, extractable, no backgrounded process, no sleep and no elapsed-time assertion. It
already made the fixture optimisation itself (one template, `cp -r` per scenario, its header
noting it turned 36 git chains into one), so the remaining cost is genuinely the subject: one
`bash manifest-check.sh` per arm, and that checker carries 33 git call sites.

What stops it being MECHANICAL is uniform rather than scattered, which is why it is the follow-up
and not a refusal:

1. `run` asserts a NEGATIVE on all 62 arms — no raw `fatal:` may leak — and the harness compares
   rc plus one POSITIVE substring. Every subject needs a wrapper that folds the negative into an
   exit code.
2. Fifteen arms assert a structural silent-clean property rather than a substring.
3. Setup and subject run under a fresh `bash -c`, so the suite's five fixture functions and its
   fake clock must be exported or re-homed into the snapshot.
4. One scenario needs a file OUTSIDE the repo, so the snapshot has to become a directory
   containing the repo rather than the repo itself.

The harness gained one thing this survey demanded and it is already landed: `build_fixture` now
resets the batch, so a suite needing several base fixtures no longer re-runs the first batch's
arms against the second batch's snapshot. `check-wiring.test.sh` needs about twenty-five of them.

## What this survey does NOT claim

- The seconds in the table are `gate-run` readings taken under the bar, not standalone. The first
  port measured 208 s recorded against 31.9 s standalone — a 6.5x contention factor — and nothing
  here establishes that the factor is uniform across legs. So the ORDER of this table is a
  ranking of recorded cost, which is what §S3 asks for, and not necessarily of the work each
  suite does.
- No suite was run to produce a verdict except `memory-hygiene self-test` and
  `install-prefix self-test`, whose readers ran them to check extractability empirically. The rest
  is read from source, and a reader can be wrong about a 1600-line file.
- "Not portable under this unit's rules" is not "not worth improving". `corpus-ids` names its own
  better lever — drop redundant scratch commits and reuse corpora in-process — and that is a
  different unit, not this one.
