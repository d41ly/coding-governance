# TOOL-aBatchedTribunal-6 — W4: the four rows the closing review left open

**Status:** CLOSED · rev-2 · 2026-08-09 · node a · Tier-2 · base 58c0a583 · streams tooling

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-08-09-review-TOOL-aBatchedTribunal-1-7.md](../reviews/2026-08-09-review-TOOL-aBatchedTribunal-1-7.md) | diff-review | TOOL-aBatchedTribunal-1 TOOL-aBatchedTribunal-8 |
| [2026-08-08-review-TOOL-aBatchedTribunal-1-3.md](../../aDrainedSluice/reviews/2026-08-08-review-TOOL-aBatchedTribunal-1-3.md) | diff-review | TOOL-aDrainedSluice-1 TOOL-aDrainedSluice-2 TOOL-aDrainedSluice-3 TOOL-aDrainedSluice-4 TOOL-aDrainedSluice-5 TOOL-aDrainedSluice-6 TOOL-aDrainedSluice-7 TOOL-aDrainedSluice-8 TOOL-aDrainedSluice-9 TOOL-aBatchedTribunal-1 TOOL-aBatchedTribunal-8 |

<!-- /gen:spec-records -->

## 1. Goal

Close `TOOL-aBatchedTribunal-2` … `-5` — the four findings the W3 closing review confirmed and this
build deliberately did not fix under time pressure. Each was diagnosed against the tree before a line
was written, and three of the four turned out to be worse than their row said.

## 2. Scope (IN)

- **S1 (row -2)** — memory-recall's `_mid_build`. The row said the predicate was narrower than its
  docstring; measured, it is False for the extraction phase (31% of a build of this corpus), False in
  the window where `_write_set` has unlinked a database and not yet recreated it, and False for the
  ENTIRE build on a filesystem whose mtime granularity puts the rebuild inside the previous
  manifest's tick. A concurrent reproduction killed a sibling's build with `unable to open database
  file`, so this was live data loss, not a documentation defect.
- **S1b** — the fix is a BUILD MARKER written before the first read and removed in a `finally`, with
  a TTL so an abandoned build stops protecting its directory. The mtime test stays verbatim beneath
  it: a cache written by an older kit has no marker, and absence of a marker is not evidence of
  absence of a build.
- **S1c** — `evict_over_budget` RE-CHECKS at the moment of deletion. The plan is a proposal made from
  a snapshot; a sibling can start building between the snapshot and the loop, and a plan is not a
  licence to delete what has become live since it was made.
- **S2 (row -3)** — the parity floor. The floor was not wrong about where to look; the CONSTANT was
  wrong about when. `KIT_MEMORY_TREE_VERSION` goes 1.5 → 1.6 across its three sites, and a new
  merge-bar leg, `check-verdict-epoch.sh`, reds when a non-comment line of the engine moves and the
  constant does not.
- **S2b** — the epoch gate OVER-COUNTS deliberately: a rename or a whitespace refactor demands a bump
  it does not strictly need. That is the safe direction — the cost is three lines and a `--render`,
  and the alternative is deciding from a diff whether a verdict moved, which is the judgement call
  that produced the stale constant.
- **S3 (row -4)** — `corpus_ids.py`'s shape filter was `¬(B ∨ ¬B)`, identically False. Deleted, with
  `KNOWN_EXT`. The comment explaining why directory citations count stays.
- **S3b** — because the deletion is behaviour-preserving by construction, NO input/output arm can
  discriminate. The arm is structural: every `continue` in `walk()` must be reached by a fixture, with
  the population derived from `walk()`'s own AST. It immediately found two MORE unreached branches
  (the append-only skip and the elision/slashless skip), which now have fixtures.
- **S4 (row -5)** — the ban keyed on the retired IDIOM, so a launcher invoked BARE carried nothing to
  match. A second ban keys on the INVOCATION SHAPE. One true positive migrated
  (`check-memory-hygiene.test.sh`, a merge-bar leg), three deliberate literals marked
  `# gov:literal-python — <reason>`.

## 3. Non-goals (OUT)

- Shipping the bare-launcher ban to adopters. `tools/lib/` is gov-repo-internal, so this protects the
  kits before they ship and not an adopter's fork. Making the ban travel means putting it inside a
  kit, which is a bigger change than this row and gets its own row if anyone wants it.
- Widening the ban past `*.sh`. Measured: .githooks/, `*.json` and `*.md` add 46 hits across 15 files,
  every one operator prose. A 46-entry allowlist on day one is a second source of truth, not a gate.
- A lock file for the recall cache. Two builders writing one cache directory is already survivable —
  last writer wins, the manifest is atomic — so a mutual-exclusion protocol with a stale-lock recovery
  story buys nothing this marker does not.
- Bumping `CACHE_VERSION`. The marker is not a manifest field, so no adopter's warm cache is
  invalidated.

## 4. Design

### Data model

```
BUILD_MARKER  : `building`, written before the first read, removed in a finally
BUILD_TTL_S   : 900 — ~7700x the 0.117 s measured for this corpus, so a slow live build cannot expire
verdict epoch : KIT_MEMORY_TREE_VERSION; must differ across any diff that moves a non-comment
                line of check-memory-hygiene.sh
bare launcher : an invocation of python3/python/py NOT through a resolved variable, outside the
                resolver block and outside a `gov:literal-python` line
```

### Inventory

| File | Change |
|---|---|
| `tools/memory-recall/query.py` | build marker + TTL, `build_cache` split so the marker wraps the whole build, re-check before delete |
| `tools/memory-recall/selftest.py` | `_sib(marker_age=, db_absent=)`; three new arms (state table, TTL, race) |
| `tools/memory-tree/check-verdict-epoch.sh` + `.test.sh` | new gate + 10 arms |
| `tools/memory-tree/check-memory-hygiene.sh` · `HYGIENE.template.md` · `memory/HYGIENE.md` | 1.5 → 1.6 |
| `tools/memory-tree/hygiene-parity.test.sh` | header: why the floor was wrong, and the gap after a bump |
| `tools/memory-tree/corpus_ids.py` | the tautology and `KNOWN_EXT` deleted; reachability arm + 4 fixtures |
| `tools/lib/resolve-python.test.sh` | §3b, the invocation-shape ban, 9 arms |
| `tools/memory-tree/check-memory-hygiene.test.sh` | the inline resolver; the bare `python3` migrated |
| `tools/memory-recall/adopt-memory-recall.sh` · `tools/check-wiring.sh` · `tools/hooks/agent-cap.test.sh` | `gov:literal-python` markers |

### Alternatives rejected

- **`built_at` vs db mtimes** for mid-build. Rejected: `built_at` is stamped AFTER both databases are
  written, so during extraction the old databases still match the old `built_at` and the longest
  unprotected phase survives untouched. It also compares a process wall clock against a filesystem
  clock, which diverge on a network mount.
- **mtime vs process start.** Rejected: says nothing about a sibling that started before this process
  did, which is the only case that matters.
- **Treating a MISSING database as mid-build** (the review's own suggestion). Rejected: it collides
  with `_remove_cache_dir`, which deliberately leaves the manifest in place when it cannot finish, so
  a half-deleted directory would become permanently un-evictable rubble.
- **Keeping the dead shape filter as documentation.** Rejected: that is a comment's job, and the
  comment survives. Executable dead code is plumbing a later edit will trust.
- **A `VERDICT_EPOCH` constant** separate from the kit version. Rejected: it is the bump plus one more
  literal to keep honest, and the kit version is already the declared epoch marker in three places.

## 5. Production-readiness checklist

- security — the marker is a few bytes of pid inside the kit's own cache directory.
- perf / scale — one `write_text` and one `unlink` per build; one extra `stat` per candidate.
- a11y — N/A. i18n — N/A.
- error / empty / loading states — no marker (older kit) falls through to the mtime test; an expired
  marker stops protecting; a missing engine, an unresolvable base and a bogus base are all NAMED in
  the epoch gate.
- observability — a skipped eviction says why (`did NOT evict …: a build started in it after the plan
  was made`); the epoch gate prints the version pair it compared.
- risks — the marker adds a file to the cache directory, counted by `_dir_bytes` as noise against a
  megabyte budget. The epoch gate can demand a bump for a behaviour-preserving refactor.
- migration / rollback — one commit; no schema, no conf key, no `CACHE_VERSION` bump.
- user docs — `AGENTS.md` names the new leg; the parity harness header explains the post-bump gap.

## 6. Acceptance criteria

- **AC1** — When a sibling is mid-extraction or between unlink and recreate, an over-budget run does
  NOT evict it, and the same run evicts something else so the survival is not vacuous.
- **AC2** — When a marker is older than the TTL, that directory is evicted; a fresh marker is not.
  The two fixtures differ only in marker age.
- **AC3** — When a build starts after the plan is made, the deletion loop skips it and says so.
- **AC4** — When the marker disjunct is removed, AC1–AC3 all red. (Verified by removing it.)
- **AC5** — When the engine's non-comment lines move without the constant, the epoch gate fails and
  names all three files to edit; with the bump, it passes and prints the pair.
- **AC6** — When only comments change, no bump is demanded; an INDENTED comment is still a comment
  and an indented statement is not.
- **AC7** — When any `continue` in `walk()` is unreached by a fixture, the corpus-ids selftest names
  its line; the population is derived from the AST, not listed.
- **AC8** — When a shell script invokes a bare launcher, the invocation ban names the file and line;
  the resolver block and a `gov:literal-python` line are exempt, and the SAME line without the marker
  is not.
- **AC9** — When the full bar runs, it is green.

## 7. Gates

`bash tools/run-gates.sh` — 36 legs. New: `verdict epoch` and its self-test.

## 8. Open questions

none.

## 9. Revision log

- rev-2 · 2026-08-09 · folded the closing review of W4: 31 raw, 24 confirmed, 7 refuted, precision
  0.77. One BLOCKER of my own making — the new self-test's `arm()` captured the gate's exit code and
  never asserted it, so the gate could be mutated into a printer with all ten arms green. Four highs,
  all the same family: an arm that names a branch it does not reach. The marker PRODUCER was unarmed
  (every arm planted the file by hand); the deletion-time re-check arm was excluded at the candidate
  filter and so never reached the loop it was written for; the live-tree epoch arm asserted the prefix
  every message carries; and the launcher ban read only column one, so three live bare assignments
  passed — one of them two lines above a site this same commit had marked. Plus: the engine is not one
  file (8 of 19 verdicts delegate to three Python modules), a no-base run exited 0 where run-gates
  cannot tell a skip from a pass, an unreadable old constant failed open, the marker was unlinked
  unconditionally so one builder released another's protection, and two arms held by construction.
  All fixed, each mutation-verified. One narrowing stays OPEN as `TOOL-aBatchedTribunal-7`.

- rev-1 · 2026-08-09 · written after diagnosing all four rows against the tree; three were worse than
  their row said, and one — the mid-build predicate — was live data loss rather than a documentation
  defect.

## 10. Reuse audit

Nothing new is designed. The marker is the same author's-claim-plus-shape-check shape as
`gov:bounded-fanout` and `gov:fixed-verifiers`, one concern over. The epoch gate is a source-level
diff gate in the mould of `check-review-join.sh`, and it delegates its remedy to the existing
three-file bump plus `kit-dogfood-parity.test.sh --render` rather than automating it. The invocation
ban lives in the resolver's existing self-test beside the idiom ban it complements, sharing its
scan-the-tree shape and its empty-population guard. The reachability arm uses `sys.settrace` and the
`ast` module rather than adding a coverage dependency, and its population comes from the function
under test.
