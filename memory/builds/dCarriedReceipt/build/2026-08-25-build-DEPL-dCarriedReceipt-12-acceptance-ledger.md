# Acceptance ledger — DEPL-dCarriedReceipt-12, write preconditions and a lock

**Serves:** journal DEPL-dCarriedReceipt-12

**Evidences:** DEPL-dCarriedReceipt-12
- AC1 — `tools/govkit/selftest.py` — RED observed first in a live LINKED worktree with `MERGE_HEAD`
  planted at the real `--git-path`: `apply` ran to its receipt step and exited 0, and
  `update --write` exited 0 and re-stamped. `target/.git/MERGE_HEAD` did not exist, which is exactly
  why the old path stat saw nothing. GREEN: both verbs refuse by name, with fixture arms asserting
  `.git` really is a FILE and a negative arm proving the same worktree proceeds once the marker is
  cleared.
- AC2 — `tools/govkit/selftest.py` — RED observed first on a normal repo installed with a kit
  declaring no `lf_pin`: `apply` printed `0 pin(s) declared` and exited 0 with `.git/MERGE_HEAD`
  present, because the probe sat inside `if pins:`. GREEN: refuses for all three markers, with a
  fixture arm asserting the receipt carries NO attributes row so the old probe really was skipped.
- AC3 — `tools/govkit/selftest.py` — RED observed first: `update --write` over a live `UU` took the
  `stale` arm, wrote gov's bytes, ran its own `git add`, and `git ls-files -u` went 3 to 0. GREEN:
  refuses naming the path, and the index still shows three stages.
- AC4 — `tools/govkit/selftest.py` — refuses naming a dirty CLAIMED path and leaves the edit on
  disk; the negative half proceeds at exit 0 with a dirty path OUTSIDE the receipt population, with
  a fixture arm asserting `git diff --name-only` is exactly that outside path first.
- AC5 — `tools/govkit/selftest.py` — two REAL concurrent processes. The harness starts run one with
  `Popen`, WATCHES for the lock file to appear rather than sleeping and hoping, then starts run two,
  which refuses naming the holder's pid. If three attempts never catch the lock held, the arm FAILS
  rather than reporting an unearned green.
- AC6 — `tools/govkit/selftest.py` — in two halves that are not the same claim. After AC3's
  refusal, which is raised BEFORE the lock is taken, and after S7's refusal, which is raised with the
  lock ALREADY HELD. Only the second grades the `finally`.
- AC7 — `tools/govkit/selftest.py` — RED observed first on a scratch gov: with the receipt at B,
  `update --to <A> --write` classified the row `stale`, wrote the OLDER bytes and re-stamped
  `gov_commit` backwards. GREEN: refuses, prints both shas, bytes byte-identical, field unmoved.
  Both negative halves armed — an equal `--to` and a descendant `--to` both proceed.
- AC8 — `tools/govkit/selftest.py` — RED observed first: a sha on a deleted branch landed and
  re-stamped the receipt at a commit no ref reaches. GREEN: refuses naming the sha; the negative
  half creates a branch containing that same sha and it then proceeds.
- AC9 — `tools/govkit/selftest.py` — both sides of S4's first carve-out. A `git rm` staged and not
  committed refuses; the same path once committed is not dirty, proceeds, and reaches the `missing`
  cell. A further arm covers S4's SECOND carve-out, which no criterion names.

## Every arm was seen to fail

Twelve breaks were staged and restored byte-identical, each red-ing a named subset: B1 the path-stat
form, B2 the apply-side call, B3 and B12 the index-stage refusal, B4 the dirty predicate, B5 the
`O_EXCL`, B6 the lock release, B8 the ref-reachability refusal, B9 and B10 the two carve-outs, B11
the AC5 watcher itself. B11 is the liveness proof: it shows the concurrency arm CAN fail, which a
timing-dependent arm otherwise cannot claim.

## What this ledger does not claim

The `lexicon naming predicates` leg is RED and it is PRE-EXISTING — 402 offenders across 890 graded
definitions, and `tools/govkit/govkit.py` contributes zero because it is not in the lexicon's armed
population. `tools/govkit/check_runbook_parity.py` also exits 1 standalone and has no caller and no
row in the leg manifest; that is TOOL-dScaffoldedMirror-15's subject, not this unit's.

## The consequence no criterion states

S4's definition of dirty, implemented exactly, makes "commit before you re-run a writing verb" a
hard precondition of BOTH verbs. `apply` stages everything it lands, so after a successful apply
every claimed path differs index-versus-HEAD. A second `apply`, an `apply --resume`, and an
`update --write` straight after `apply` all refuse. This is PARKED for the owner in the run record
rather than resolved here: narrowing S4 to `update` alone is a one-sentence spec change, and the
unit is titled "on both writing verbs" while S7 and S8 say "update" where they mean it, so the spec
distinguishes the two deliberately.
