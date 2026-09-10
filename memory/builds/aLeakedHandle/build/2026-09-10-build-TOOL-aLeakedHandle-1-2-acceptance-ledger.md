# TOOL-aLeakedHandle-1 — acceptance ledger

**Serves:** journal TOOL-aLeakedHandle-1

**Evidences:** TOOL-aLeakedHandle-1
- AC1 — `pass_commit` sourced out of `lib-unattended.sh` and called over `eff1b6b1..HEAD` for this unit returned `rc=0` printing `e0780e80913ffdcea4f49429bf21011fd52de24b`, which `git log --reverse` confirms is the FIRST qualifying commit in that window and not the last. With `TMPDIR` pointed at a path that cannot be created, the same call printed `lib-unattended: pass_commit cannot create a scratch file, so it cannot say whether this pass committed` on stderr and returned 2, with empty stdout. The `Red when:` control was run too, on a staged copy of the library with the loop behind a pipe: `rc=1`, sha still printed — which is what rev-4 corrected the criterion to say
- AC2 — the row for `unattended kit gate` in `<git-dir>/gate-ledger.tsv`, read after the bar this unit paid for. The reading is under *The bar that observed AC2 and AC8* below, because a figure typed beside prose that does not own it is the defect this repository keeps re-filing
- AC3 — `grep -c 'PASSCOMMITS'` over `lib-unattended.sh` returns 0, the tree scan names that file in neither its hit list nor its registry, and the failing population fell from 19 heredoc sites in 6 files to 18 in 5 in the same edit
- AC4 — the scan over the tree with the fix applied reports `19 sites in 6 files` as its failing population — 18 loop heredocs plus the one here-string — and names none of the near-miss classes. Three of those near-miss figures did NOT reproduce the spec's rev-3 pins and rev-4 moved them; base `013b1af9` and the failing population are unchanged
- AC5 — `python tools/gate-lint/sh_hygiene.py --selftest` prints `PASS (18 assertions)`. Its fixture carries the failing form and its innocent neighbours in ONE file, so no arm can pass by grading nothing. Its own failing case was observed: with `check_substitution` stubbed to `return False` the same run printed six named FAIL lines and exited 1. That control substitutes a synthetic value for the shipped one, so it proves the ARMS can fail and NOT that the predicate is right; AC7 is the observation that stages the real construct into a real tracked file
- AC6 — both refusals staged into the real registry and observed RED. A row re-keyed to a delimiter the file no longer carries printed `the registry declares 'GONETAG' and the scan no longer finds it`; a row keyed on the line number `97` printed `is not a heredoc tag or '<<<' — the key is the DELIMITER, never a line number`. Both exited 1, and `substitution-fed-loops.txt` was restored to green after each
- AC7 — `done <<PASSCOMMITS` staged into `tools/check-template-size.sh`, a tracked shell file with no registry row. The leg exited 1 naming that file and that delimiter; unstaging and restoring the file returned it to `OK — 18 declared site(s)`. This is the gate's failing case, observed before the unit landed
- AC8 — `GATE_SELFTESTS=1 bash tools/run-gates/run-gates.sh`, the one invocation that lifts the self-test hold. Both new legs appear in the reported set. The verdict and the leg list are under *The bar that observed AC2 and AC8* below
- AC9 — `memory/gotchas/bounded-through-a-pipe-is-unbounded.md` gains a clause naming this leg and the construct its predicate matches, and its existing sentence that nothing sweeps other kits for `out=$(timeout` is intact and now says explicitly that the new leg does not close it either. `check-memory-hygiene.sh` item 18 stays green over the record
- AC10 — `python3 tools/codebase-map/test_codebase_map.py` passes with the dossier in place. The failure was REPRODUCED first: with the two leg rows and no dossier the suite named both leg names under `UNCLAIMED` and reported `inventories.json` stale. The `gate-lint` row left `memory/map/baseline.toml` in the same edit, because a key that is both claimed and baselined fails the ratchet's fourth assert
- AC11 — `bash tools/unattended/check-pass-order.sh` and `bash tools/unattended/check-brief-recorded.sh` both exit 0 with the unit CLOSED and its build commit landed, and neither names `TOOL-aLeakedHandle-1`. Both were RED before the amendment, each naming the SPEC commit `e79cd862` as the build commit. Measured either side of the one-word change: 150 closed units graded by the first both times, both rows in `memory/project/pass-order-waiver.txt` still resolving rather than reporting stale, and no other unit's verdict moved. The second leg's population went 20 to 21 closed units, which is this unit joining it

## The bar that observed AC2 and AC8

`GATE_SELFTESTS=1 bash tools/run-gates/run-gates.sh` on node `a`, 2026-09-10, over the working tree
this unit commits. 69 legs ran, 37 were skipped by their own guards, 1 failed.

**AC2.** `unattended kit gate` — status `ok`, **708.037 s**, against its declared ceiling of 16040.
The same leg burned 4168 s on the killed run of 2026-09-10 before an operator stopped it, so the
reading is 5.9x lower and it is a VERDICT rather than a kill. The third `Red when:` clause does not
apply: the wall guard fired on nothing, and the row's timestamp is this run's.

**AC8.** Both new legs are in the reported set and both are green — `shell hygiene (a loop fed by a
command substitution)` at 1.013 s and `shell-hygiene selftest` at 0.562 s, each against a declared
ceiling of 300. Every leg §7 names ran and every one is `ok`, the two run-gates canaries included:
`unattended kit gate`, `pass-order history`, `brief-recorded`, `memory hygiene`, `spec tokens`,
`govkit selfcheck`, `lexicon naming predicates`, `harness arms`, `every held leg is budgeted`,
`testsuite counts`, `install-prefix`, `line length`, `codebase-map coverage + freshness`,
`run-gates canary`, `run-gates gov canary`.

**THE ONE RED, and it is this criterion's own bookkeeping rather than a defect.** `drift-audit
records` failed on `closed_specs_with_no_product_commit = 2` against a pin of 1: the spec's status
header reads CLOSED in the tree the bar graded, and the commit carrying the code did not exist yet.
The signal is measured against `HEAD`, so it cannot go green until the commit it is complaining
about is made. Re-run after the commit and recorded below.

**Four edits landed AFTER that bar and before the commit, and each names what re-ran for it.** They
are stated rather than folded into the green line, because a bar's verdict covers the bytes it read.
`tools/gate-lint/sh_hygiene.py` gained `FLOOR_ASSERTIONS` (AC5's `Red when:` names a stranded arm and
nothing could see one), a refusal for a `git ls-files` that FAILS as distinct from a tree with no
shell in it, and the one-line-one-form blind spot in its own header. `tools/gate-lint/README.md`
said the kit had no gate legs of its own, which these two legs made false.
`memory/builds/aLeakedHandle/README.md`'s authored roster still called this unit MISSING.
Re-run for them: the scanner and its self-test directly, plus `line length`, `install-prefix`,
`lexicon naming predicates`, `testsuite counts`, `kit version markers`, `govkit selfcheck`,
`memory hygiene`, `spec tokens`, `codebase-map coverage + freshness` and the build-index pair.


## What the ledger does not evidence

A green `unattended kit gate` does not by itself prove the deadlock is gone — the hang was
intermittent and that leg passed on other runs with the defect present. AC3 is the criterion that
proves it, by ABSENCE of the construct, and AC7 is what stops it coming back. The distinction is
worth keeping because the tempting reading of a green ledger row is the wrong one.

Nothing here measures whether the nineteen carried sites are SAFE. They are known, counted and
unable to grow; §8 fork B is where draining them is decided, and the registry's own header says so.

## The three figures that did not reproduce, and why that is the honest outcome

The spec pinned six population counts at base `013b1af9`, measured by a prototype of the predicate
this unit ships. Running the SHIPPED predicate at the same base reproduced the failing population
exactly — 19 loop heredocs in 6 files, 1 here-string in 1 file, the seven-file split named in §3 —
and disagreed with three of the four near-miss counts: the substitution-free loop heredocs sit in 13
files rather than 17, the non-loop heredocs holding a substitution are 3 rather than 2, and the
process-substitution loops are 27 rather than 21.

Three of those are the numbers that decide nothing, which is exactly why they were the ones to
drift: no criterion reds on them. The repair is not to make the prototype's figures true. It is that
the scan DERIVES and PRINTS every count on every run, so the source that owns them is the only place
they exist, and rev-4 moved the prose to agree with it.
