# TOOL-aShardedFloor-4 — the dispatch hint reads a repository-wide store

**Status:** BLOCKED · rev-2 · 2026-08-21 · node a · Tier-2 · base 36d0ad3b · streams tooling

## 1. Goal

The dispatch hint is stored per-worktree and was renamed without migrating, so a fresh worktree
dispatches in manifest order and starts its floor leg ~158 s late. Read the hint from a
repository-wide store, keep the reuse KEY per-worktree, and SAY when the hint is missing.
Discharges `TOOL-aScannedThrottle-8`.

**BLOCKED, and this is the unit's most important line.** It must not land alone. See §8.

## 2. Scope (IN)

- **S1** — split the one file by its two jobs at the line that already fused them. The HINT reads an
  ordered candidate list — per-worktree ledger, common-dir ledger, then both legacy filenames —
  merged first-wins per leg name so coverage is strictly ≥ either single source. The reuse KEY keeps
  reading the per-worktree ledger and nothing else, forever.
- **S2** — the manifest parser takes a LIST of caches, with a PER-FILE try. A corrupt
  low-precedence file must not blank a good high-precedence one.
- **S3** — the write stays per-worktree and keyed. When a common dir resolves AND differs, publish a
  duration-only projection with the key column forced to a dash, applying the SAME carry-forward
  merge and the same atomic rename as the existing write.
- **S4** — say it: a source token on the profile line over a CLOSED five-word vocabulary, and a
  coverage count on its OWN output row.
- **S5** — two header keys recording the resolved source and the coverage.
- **S6** — fold in the fix to the nested-run population line this unit's own proof leans on: it
  selects one leg where seven qualify, which is a near-vacuous arm holding up a load-bearing claim.
- **S7** — **spell the vocabulary and the keys.** The five source tokens are `worktree`, `common`,
  `both`, `legacy` and `NONE`; the two header keys are `dispatch_source` and `dispatch_known`,
  joining `dispatch`. A closed vocabulary written as English descriptions cannot be armed.
- **S8** — **re-word `TOOL-aScannedThrottle-8` at discharge.** That row prescribes the OPPOSITE
  precedence to S1 — common dir first with a per-worktree fallback, against S1's per-worktree first,
  merged first-wins. They are not equivalent: under S1 a stale local row shadows a fresher shared
  one, which is exactly what the coverage count exists to expose. Fixing the spec and leaving the
  row is the two-answers-to-one-question class this repo already tracks.
- **S9** — the four `FLOOR_ASSERTIONS` raises this unit's arms require, each stated as an ABSOLUTE
  value. `run-gates.turnstile.test.sh` is raised by `TOOL-aShardedFloor-1` too, so whichever lands
  second states the number it expects.

## 3. Non-goals (OUT)

No change to the reuse key's derivation. No `--path-format=absolute`: this runner's idiom is one
resolution chain and its own header states the rule that path strings are never compared across
flavours. No edit to `profile_bar.py` — the per-worktree keyed write is preserved precisely so that
tool needs none. No migrate-and-delete of the legacy file, which would put a write on the read path.

## 4. Design

§"Unit C" of [the research record](../build/2026-08-21-build-TOOL-aShardedFloor-1-design-brief.md), with every
line number, every gate pin, and four staged breaks. Three constraints bind hardest:

**The coverage count goes on its OWN row and never on the dispatch-order line.** Manifest line 1 is
consumed as the dispatch order and indexed directly; a non-numeric token there resolves an unset name
to index 0, so leg 0 dispatches twice and one leg reports "no result", which is a FAIL. **That is a
verdict change**, and the runner's own header says a hint may never cause one.

**The vocabulary needs five tokens, not three.** The candidate list creates *per-worktree only*,
*common only*, *both*, and *legacy*, plus `NONE`. A three-token vocabulary cannot name two of the
states it creates.

**The primary tree's git dir IS the common dir.** Every dedupe and equality test must handle that, or
the primary tree merges its ledger with itself and strips its own keys.

## 5. Production-readiness checklist

- security — N/A: advisory scheduling data, key column forced to a dash on the shared copy.
- perf / scale — 16 % of span on any cold worktree, and see the risk below, which is the whole story.
- a11y · i18n — N/A.
- error / empty / loading states — `NONE` and `0/<n>` when nothing is found; a per-file try so one
  corrupt candidate cannot blank the rest.
- observability — the source token and the coverage count ARE the observability, and the coverage
  count is what discharges a present-but-stale hint that would otherwise print a reassuring source.
- risks — see §8; the sequencing risk is this unit's defining property, not a footnote.
- testing + left-shift gates — four staged breaks, including a fixture no existing harness builds: a
  linked worktree of a scratch repo.
- migration / rollback — additive; removing the candidate list restores today's behaviour exactly.
- user docs — the charter sentence naming the dead filename as the live cache, which this unit makes
  wrong in a NEW way. That edit is a governance carrier and is the owner's.

## 6. Acceptance criteria

- **AC1** — a first-ever bar in a linked worktree of a scratch repo whose primary has run once writes
  a dispatch order that is not manifest order and whose leading index is the longest leg. The
  DURABLE negative direction is the same fixture with every candidate removed writing manifest
  order; "the same fixture at HEAD" stops being true the moment this lands and is kept only as the
  pre-landing RED observation. Witness: the `dispatch` key of `<git-dir>/gate-run/<id>/header`.
- **AC2** — with only a legacy file present and no ledger anywhere, the order is not manifest order
  and the source token names `legacy`. The coverage count is load-bearing here because it separates
  78.4 % from 100 % — measured on this node, not asserted.
- **AC3** — with no candidate present: `0/<n>` with `<n>` derived at emission, `NONE` in the profile
  tail and in the source header key.
- **AC4** — a green keyed row present ONLY in `<common>/gate-ledger.tsv`, with `GATE_REUSE=1`,
  yields an executed leg and never a reused one — carrying its control on the SAME run, where a row
  in `<git-dir>/gate-ledger.tsv` does yield a reuse.
- **AC5** — the per-worktree ledger keeps its exact five-field shape, and `profile_bar.py --width N`
  run from inside a linked worktree of a scratch repo does not report that the ledger did not move.
  `--report` cannot exercise that refusal in any tree, which is why the criterion names `--width`.
- **AC6** — a guard-scoped run in a linked worktree does not remove a skipped leg's row from
  `<common>/gate-ledger.tsv`, with the staged-break RED observed.
- **AC7** — in the primary tree exactly ONE `gate-ledger.tsv` is written, it still carries real
  keys, and no self-merge occurs — asserted by content plus an exactly-one-file check, never by inode
  and never by absence of an error.
- **AC8** — every leg driving a nested runner resolves a `git rev-parse --git-common-dir` different
  from the real repo's, asserted over a population derived from `tools/gate-legs.json` that selects
  every such leg.
- **AC9** — stdout of a warm-hint run, filtered of `^gate (profile|dispatch): `, is byte-identical
  to the same tree with every hint removed, with the companion presence check that a filter without
  one makes any regression in the filtered line invisible.
- **AC10** — no leg's scratch repo shares the real repo's `--git-common-dir`, asserted as a PROPERTY
  over the widened population using the git-identity idiom, never by banning a spelling and never by
  path comparison.
- **AC11** — the win observed in both directions in the `dispatch` key of
  `<git-dir>/gate-run/<id>/header`: a cold linked worktree's floor leg moves from a late dispatch
  rank to rank 1 with the hint present, and back to manifest order with it removed.
- **AC12** — `GATE_FULL=1 bash tools/run-gates/run-gates.sh` green.

## 7. Gates

As the sibling units, plus `run-gates evidence` and `profile-bar selftest`.

## 8. Open questions

**Three, and the first is why this spec's status is BLOCKED rather than OPEN.**

**0. PREREQUISITE, not a question:** this unit lands AFTER `TOOL-aShardedFloor-2` and
`TOOL-aShardedFloor-3`. The mechanism, not just the sequence: the dispatch sort keys an unknown leg
name at 0.0 and every known leg at a negative, so a NEW shard name sorts dead last on a warm
ledger — and this unit's whole job is warming every worktree's ledger. Landing it first makes the
shard rename penalty worse, not better.

1. **Does this unit wait for a reserved short-leg slot, or ship with a measured 131× regression in
   time-to-first-signal?** Not resolvable here. Measured: 669.1 s to first verdict on a warm ledger
   against 5.1 s on a cold one, a swing decided solely by ledger warmth. The worktree population is
   RE-DERIVED at write time with `git worktree list`, never quoted from the report: it was 24 of 26
   when measured and the cleanup at `49aea26` took it to six the same night, which is in this
   branch's history. What does not move is the PROPERTY — every worktree with no hint is
   accidentally protected, and this unit removes that protection everywhere at once. So
   a real 16 % span win reads as a large regression to the person who filed the complaint that
   started `aScannedThrottle`, and the complaint was about PERCEIVED latency. The fix is
   `TOOL-aMeteredTurnstile-5` — dispatch longest-first into width-1 workers while one worker pulls
   shortest-first, which leaves makespan unchanged because the floor leg still starts at t=0. Nobody
   has designed it. **This is a scope fork: the options differ in what gets built, and scope is not
   delegated.** The new coverage line explains the silence; it does not remove it.
2. **The `input_key` hole.** The key hashes the tree and never the commit sha, so legs whose verdict
   reads git HISTORY can differ at an equal key. Two worktrees cut from the same upstream with the
   same tree and different shas share a key. **This unit does not create the hole — it exists today
   inside one worktree — but it raises the hit rate from rare to routine.** Widening the key
   invalidates every cached key at once, so it is its own unit and its own landing. Recorded here so
   the next reader does not rediscover it.
3. **Does the legacy filename fallback EXPIRE?** A permanent fallback keeps a dead filename alive
   forever; a migrate-then-delete needs a write on the READ path, which S1 otherwise avoids
   entirely. Measured today at 78.4 % coverage, so the fallback is worth something now and worth
   nothing once every worktree has run a bar. Owner's, with the sequencing question.

## 9. Revision log

- rev-1 · 2026-08-21 · initial, from the design pass at
  [`build/2026-08-21-build-TOOL-aShardedFloor-1-design-brief.md`](../build/2026-08-21-build-TOOL-aShardedFloor-1-design-brief.md).
  Opened at BLOCKED deliberately: §8's first question is a scope fork, and a spec that reads OPEN
  while its landing waits on a unit nobody has designed misrepresents what is ready. Skeptic
  corrections folded before first writing: the coverage count must not ride the dispatch line (it
  would change a verdict), the vocabulary needs five tokens rather than three, the write stays
  per-worktree so `profile_bar.py` needs no edit, and the nested-run arm this design leans on selects
  one leg where seven qualify.
- rev-2 · 2026-08-21 · M4 spec audit folded, record [`reviews/2026-08-21-review-TOOL-aShardedFloor-1.md`](../reviews/2026-08-21-review-TOOL-aShardedFloor-1.md), verdict BLOCKED, 40 confirmed of
  65. This unit was already correctly BLOCKED; the audit added what it was missing rather than
  changing its disposition. Folded: the 2-and-3 prerequisite and its MECHANISM are now stated (F9);
  the backlog row's opposite read precedence is superseded in the row itself, not only in this spec
  (F17); the five source tokens and both header key names are spelled (F18); the worktree count is
  re-derived rather than quoted from a night it expired (F19); the four floor raises are named
  (F13); and the legacy-fallback-expiry fork joins §8 (F12's sibling).

## 10. Reuse audit

**The seam is the line that already fused the two jobs** — `TIMINGS="$LEDGER"` in
`tools/run-gates/run-gates.sh`, whose own comment names both jobs in the sentence above it. Two
secondary seams are already parameterised and need widening rather than inventing: the manifest
parser takes its cache as an argument, and the common dir is already resolved once for the turnstile.

**Probe result recorded as an answer, not a failure.**
`python tools/codebase-map/reuse_lookup.py "read a scheduling cache shared across every worktree of one repository"`
returns no seam that reads a git-dir-rooted cache from anywhere but the current worktree, and the map
again declares bash unextractable. The nearest existing thing is `profile_bar.py`, which reads the
per-worktree ledger and refuses when it did not move — which is exactly why S3 keeps the
per-worktree write intact rather than redirecting it.

**Recall terms used:**
`python tools/memory-recall/query.py "why is the gate timing cache stored per worktree and what decided the rename to a ledger" --terms "gate-timings gate-ledger dispatch hint per-worktree common dir reuse input key carry-forward eviction manifest longest-first cache"`
