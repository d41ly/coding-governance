**Status:** INPROGRESS · rev-2 · 2026-08-27 · node a · Tier-1 · base f5dff6ae · streams tooling · order 1

# TOOL-aGroundedOrientation-3 — check 23 gets the `--staged` guard its four siblings carry

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-08-27-review-TOOL-aGroundedOrientation-1-spec-audit-round1.md](../reviews/2026-08-27-review-TOOL-aGroundedOrientation-1-spec-audit-round1.md) | spec-audit | TOOL-aGroundedOrientation-1 TOOL-aGroundedOrientation-2 |

<!-- /gen:spec-records -->

## 1. Goal
Give check 23 of `tools/memory-tree/check-memory-hygiene.sh` the `[ "$STAGED" = 0 ]` guard every
other corpus-walking check in that file already has, so the pre-commit leg stops paying a
whole-corpus cost on every commit.

## 2. Scope (IN)
- **S1.** `tools/memory-tree/check-memory-hygiene.sh:1114` — change `if [ -n "$alcut" ]; then` to
  `if [ "$STAGED" = 0 ] && [ -n "$alcut" ]; then`, with a comment naming the measurement and the
  four sibling line numbers.

## 3. Non-goals (OUT)
- **N1.** Check 9 at `:599`. Its guard is `[ "$STAGED" = 0 ] || <memory/ staged>` and
  `.githooks/pre-commit:48` only invokes the gate when `memory/**` is staged, so the right disjunct is
  true by construction and `gen_build_index.py --check` re-renders the whole index every commit. That
  is a second, smaller instance of the same class and it needs its own decision about whether the
  pre-commit leg should verify index freshness at all. Backlog, not this unit.
- **N2.** Batching the per-file spawns inside check 23. The guard removes the cost from the commit
  path; the full-bar cost remains and is a separate optimisation with a separate risk profile.
- **N3.** Renumbering the block. Its header at `:1098` calls itself 22 while all four emissions say
  23, and the real check 22 is at `:604`. Cosmetic, and renumbering a check is how waiver registries
  and arm pins silently unpin. Backlog.
- **N4.** Any wall-clock ceiling machinery. `tools/gate-legs.json` has no field a ceiling could go in
  and all three rows of `tools/run-gates/gate-profiles.txt` set `timeout=0`. That is the charter's
  COST IS A VERDICT rule going unenforced repo-wide, already carried by `TOOL-aCollapsedScan-5`.

## 4. Design
`:1114` opens on the cutoff alone and never consults `$STAGED`. Its four structural siblings all open
`if [ "$STAGED" = 0 ]` — `:667` (check 21), `:1051` (13-16), `:1066` (17-19), `:1076` (20). Check 23 is
the one delegating corpus-walker that never got the guard.

Unguarded it walks all 317 specs and 307 records on every commit: one `awk` per record to flatten the
ledger at `:1117`, roughly five forks per spec at `:1136-1141` paid *before* the date filter rejects
212 of them, and one `printf`+`grep` pair per acceptance label at `:1169` re-scanning the whole
flattened ledger. The file's own `:111-112` records that a fork costs ~50-100 ms under MSYS/Windows
and that this exact class once cost "minutes on a large adopter tree".

### Alternatives rejected
- **Batch the spawns instead of guarding.** Larger diff, same commit-path cost until it is finished,
  and it does not answer why this check runs on a commit at all when its four siblings do not.
- **Raise the commit timeout.** Not a fix; it is what produced four orphaned hook trees today.

## 6. Acceptance criteria
- **AC1.** `grep -c '\[ "$STAGED" = 0 \] && \[ -n "$alcut" \]' tools/memory-tree/check-memory-hygiene.sh`
  returns 1, and that line is the check-23 block's opening condition. Pinned by PREDICATE, never by
  line number: rev-1 pinned `sed -n '1114p'` and the comment S1 itself mandates pushed the guard to
  `:1121`, so the criterion was falsified by the very change it describes.
- **AC2.** `check-memory-hygiene.sh --staged` over the same staged set drops from 963 s to 54 s,
  uncontended, both exit 0. **Observed 2026-08-27 node `a`** — 963 s unguarded untraced, 54 s guarded
  untraced, 890 s unguarded traced. 94% of the leg's wall clock, 17.8x.
- **AC3.** COVERAGE IS NOT LOST: with a break staged that check 23 catches, a FULL-mode run still
  REDs naming `fail 23`, while the `--staged` run over the same tree passes. This is the failing case
  the charter requires observed before a gate change lands, and it is the one that matters here —
  the risk is not a false red, it is a check that silently stops running.
- **AC4.** `.githooks/pre-push:229` runs `tools/run-gates/run-gates.sh`, which invokes this checker
  without `--staged`, so `STAGED=0` and the block executes unchanged at the push boundary. Verified
  by reading the hook.

## 7. Gates
`bash tools/memory-tree/check-memory-hygiene.sh` (full) · `python3 tools/memory-tree/check-arms.py --check` ·
`bash tools/run-gates/run-gates.sh` at the push boundary, which covers the `records`-chunk leg.

**The self-test is NOT covered by that push-boundary run and must be invoked deliberately:**
`bash tools/memory-tree/check-memory-hygiene.test.sh`, or `GATE_SELFTESTS=1 bash tools/run-gates/run-gates.sh`.
`tools/gate-legs.json` puts `memory-hygiene self-test` in chunk `selftests`, which is held by default,
and `.githooks/pre-push:224` exports `GATE_FULL=1` only — `GATE_FULL` does not unlock that chunk. rev-1
claimed the push boundary covered it, which is the "an exemption is not coverage" class named against
a gate this spec is itself changing.

## 8. Open questions
None. AC3 is an obligation, not a fork.

## 9. Revision log
- rev-1 · 2026-08-27 · authored during the run after the owner ruled the fix ahead of the build's own
  two units. Unreviewed by definition (M4).
- rev-2 · 2026-08-27 · round-1 spec-audit fold, three findings, all reproduced against source before
  folding. **F2 (high)** — AC1 pinned `sed -n '1114p'` and the comment S1 mandates moved the guard to
  `:1121`, so the criterion was falsified by its own change; re-pinned on the PREDICATE. **F3 (high)** —
  §7 claimed the push boundary covered `check-memory-hygiene.test.sh`; it does not, because that leg
  is chunk `selftests` and `.githooks/pre-push:224` exports `GATE_FULL=1` only. **F4 (medium)** — §7
  spelled `check-arms.py` with `bash`, disagreeing with both sibling unit 2 and `tools/gate-legs.json`.
  This spec was written and BUILT before any audit ran, under the owner's sequencing ruling; the audit
  therefore graded shipped code, and all three findings were spec defects rather than code defects.

## 10. Reuse audit
**The seam extended.** The four sibling guards in this same file — `:667`, `:1051`, `:1066`, `:1076`.
This unit adds no mechanism; it applies the file's existing one to the block that lacks it. That is
why the diff is one condition and a comment.

**Recall probe.** Terms: `memory hygiene check staged guard pre-commit leg cost fork spawn corpus
walk acceptance ledger cutoff sibling`. Prior art found: `TOOL-aCollapsedScan-5` (OPEN) carries the
repo-wide "no leg declares a wall-clock ceiling" verdict, which is the general form of this
instance and is deliberately NOT closed by this unit — N4 says so.

**Map probe.** `reuse_lookup.py "guard a hygiene check so it does not walk the whole corpus on a
staged run"` returned no symbol-level seam, which is correct: the seam is four sibling conditions in
one shell script, below the granularity the map indexes.

**Staleness.** Every line number above was read from source at writing time, not recalled.
