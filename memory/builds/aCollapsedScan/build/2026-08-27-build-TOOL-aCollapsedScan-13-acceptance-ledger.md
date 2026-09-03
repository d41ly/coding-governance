# Acceptance ledger — TOOL-aCollapsedScan-13

**Serves:** journal TOOL-aCollapsedScan-13

Node `a` · branch `branch/acollapsedscan-followups` · base `3c37a1fb`. One line per numbered
criterion, naming the observation that answered it.

**Evidences:** TOOL-aCollapsedScan-13

- AC1 — `bash tools/memory-tree/check-memory-hygiene.sh` — MET, and re-verified AFTER the round-3
  fold, because a byte-identity proof taken before the last three changes proves nothing about what
  lands. Clean tree, both checkers: exit 0, zero bytes of output, `diff` identical. Post-fold run
  297 s.
- AC2 — `bash tools/memory-tree/check-memory-hygiene.sh` — MET, with its scope stated. Two breaks
  were staged, one per touched check: an `AC99` on a CLOSED Tier-2 spec with no ledger row, and a
  record renamed so its filename claims an id its `Serves:` line omits. Pre-fold, the pre-change and
  post-change checkers produced byte-identical output over that tree, both exit 1, old 1121 s
  against new 167 s. Post-fold the comparison was re-run and the two staged-break lines are again
  byte-identical. The first post-fold attempt read DIFFERS, and the difference was TREE drift rather
  than code drift - this unit had become CLOSED with unevidenced criteria, so check 23 correctly
  reported those too. Rather than explain that away, the comparison was re-run with this ledger in
  place, over a tree matching the original capture in everything check 23 reads: IDENTICAL, whole.
  Separately, every
  check-21 and check-23 failure template is byte-identical between the two scripts — only line
  numbers moved — each still interpolating `$algap`, `$albad`, `$alnolab`, `$proj21`.
- AC3 — `bash tools/memory-tree/check-memory-hygiene.sh` — MET and exceeded. 1908 s before, 249 s
  after, taken back to back on the same tree under the same load: **7.7×**, where the criterion asked
  for 2×. The ratio is the claim; the absolute figures are a loaded box and are superseded by any
  later idle reading.
- AC4 — `EPOCHREALTIME` checkpoint probe — MET. Re-profiled after the fix, the largest region is
  check 20 at 150.5 s; check 23 is 74.8 s and check 21 is 16.6 s, so neither is the largest. Against
  the pre-fix profile that is 1035.9 s to 74.8 s for check 23 (13.8x) and 149.6 s to 16.6 s for
  check 21 (9.0x). The criterion exists because a 7.7x overall cut is equally consistent with having
  MOVED the cost, and only a re-profile tells the two apart.
- AC5 — `bash tools/run-gates/run-gates.sh` — MET. `gates GREEN — 41/41 legs passed (5 skipped)
  (39 held: kit self-tests)`, 1605 s. Two earlier runs redded and both were this unit's own debt:
  `verdict epoch` for the kit version I had argued was unnecessary, and `kit version markers` for
  two carriers the first refusal's list did not name. THE BAR'S OWN WALL CLOCK is the unit's least
  arguable evidence: 3162 s on the run before the fix landed against 1605 s after, on the same node
  and the same 41 legs.

## The equivalence evidence that is not an acceptance criterion

`memory/builds/aCollapsedScan/build/2026-08-26-build-TOOL-aCollapsedScan-13-equivalence-harness.sh`
runs the pre-change `grep` predicate and the post-change builtin predicate side by side: **560
inputs, 0 divergences**, including every class the closing review named and the hyphenated-`FAMILY`
adopter case the pre-fold code got wrong. It is committed as a record rather than a test because it
grades a predicate that no longer exists in one of its two forms — but the next change to that
extraction has something to run instead of a diff to read.

That matters because the diff was read carefully twice before the closing review and all three
defects survived both readings.

## Superseded at landing — read AC3 and AC4 as history, not as the shipped cost

This unit's implementation did NOT land. Between this build's close and its merge to `main`,
`TOOL-aThawedCorpus-1` and `TOOL-aThawedCorpus-4` rewrote the same three regions of
`check-memory-hygiene.sh` independently and further: where this unit replaced per-record forks with
shell builtins and kept the enclosing loops, those units replaced the loops themselves with one
`awk` pass each. The merge kept theirs. Every criterion above was MET against a predicate that is no
longer in the file.

What that changes for a reader:

- **AC3's 1908 s -> 249 s and AC4's re-profile describe the retired implementation.** The direction
  of the claim survives — the shipped `awk` version is the same or faster in the same regions — but
  these particular figures measure code that is not in the tree. Re-measure before citing them.
- **The equivalence harness beside this file grades a predicate neither side now ships.** It was
  already committed as a record rather than a test; it is now a differential record of a fork that
  closed the other way. It is in no leg of `tools/gate-legs.json` and asserts nothing about the bar.
- **The two defects this unit's guards existed to fix are unreachable in the shipped code, not
  unfixed.** `TOOL-aThawedCorpus-1` retained the `^(FAM_ALT)-[A-Za-z0-9]+-[0-9]+` regex, and POSIX
  ERE leftmost-longest alternation makes the hyphenated-`FAMILY` case resolve correctly while the
  mandatory second hyphen makes the two-segment `TOOL-1` phantom impossible. Verified by execution
  against gawk 5.4.0 at merge, not by reading.

What DID land from this build: the `BUDGET_kit_gate` 120 -> 240 re-declaration
(`TOOL-aCollapsedScan-4`), the `repo_root()` repository-boundary walk and its linked-worktree
regression case 47 (`TOOL-aCollapsedScan-7`), the `tools/memory-recall/` guard that makes case 47
actually run, and every spec and review record in this folder.
