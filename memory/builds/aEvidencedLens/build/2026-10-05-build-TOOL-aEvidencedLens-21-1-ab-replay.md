# TOOL-aEvidencedLens-21 — the A/B replay of the round-1 spec audit

**Serves:** journal TOOL-aEvidencedLens-21

The mandate's replay half, which the closing diff review's M4 found unrecorded. The round-1 spec
audit of this build's eleven specs (`reviews/2026-10-05-review-TOOL-aEvidencedLens-1-spec-audit-round1.md`,
four lenses, the harness as it stood at the run's BASE) is compared with a replay of the same audit by
the improved harness this build made (five lenses, read-only probes, the rewritten skeptic).

## Provenance

The replay ran the improved harness over the same eleven round-1 spec blobs, the ones the round-1
record pins, in a frozen clone at `4d0d64688`, the commit the spec stage authored them at. That is
the main loop's account, carried by spec 21 §2 S4; this pass did not re-run the replay. Its report,
`ab-replay-report.md`, stayed in the session scratch directory and is NOT copied under `reviews/`:
its first line is `**Serves:** spec-audit` over all eleven ids, so a copy there would read as a
second audit of specs no second audit was owed. The scorer is `tools/workflows/review_replay.py` as
unit 10 built it, run both ways by this pass at base `f86bf4826`.

## The ceiling the scorer states

A spec-mode match is the same file and the same SECTION: the window is forced to 0. One candidate in
a spec's §2 therefore matches every known finding in that §2, and a MATCHED pair is not shown to be
the same defect. Both recall figures below are UPPER BOUNDS at section granularity, and the two HIGH
items discussed under liveness matched only that way.

## Forward run — the round-1 record as known, the replay as candidate

`python tools/workflows/review_replay.py --known memory/builds/aEvidencedLens/reviews/2026-10-05-review-TOOL-aEvidencedLens-1-spec-audit-round1.md --candidate <scratch>/ab-replay-report.md`, exit 0, pasted whole:

```text
replay: known memory/builds/aEvidencedLens/reviews/2026-10-05-review-TOOL-aEvidencedLens-1-spec-audit-round1.md · kind spec-audit · unit raw-finding · subjects memory/builds/aEvidencedLens/spec/2026-10-05-spec-TOOL-aEvidencedLens-1.md@de140c3ea4acd5571eb7ee42f9cf4ebbb669e34c, memory/builds/aEvidencedLens/spec/2026-10-05-spec-TOOL-aEvidencedLens-2.md@1ea5a3a513b452f2072c8ab8825d2ba371e8c87e, memory/builds/aEvidencedLens/spec/2026-10-05-spec-TOOL-aEvidencedLens-3.md@075af74ddcb7603efee1e08d2eb2cbb5955616f9, memory/builds/aEvidencedLens/spec/2026-10-05-spec-TOOL-aEvidencedLens-4.md@099033058fe14bfe3407d038ddd4efaf0af34895, memory/builds/aEvidencedLens/spec/2026-10-05-spec-TOOL-aEvidencedLens-6.md@3f4fafd20ffdec3b119b9f4ab319f51e654717e0, memory/builds/aEvidencedLens/spec/2026-10-05-spec-TOOL-aEvidencedLens-10.md@88b6a0f1477ab70a89d33b09b05cf89c824a9b66, memory/builds/aEvidencedLens/spec/2026-10-05-spec-TOOL-aEvidencedLens-5.md@6d1c0773338495d741eccfa96cb18b2573507948, memory/builds/aEvidencedLens/spec/2026-10-05-spec-TOOL-aEvidencedLens-7.md@7d4dce07d8899d54bfff2a1e1515aa297b090950, memory/builds/aEvidencedLens/spec/2026-10-05-spec-TOOL-aEvidencedLens-9.md@9e4e4704eaa6dd5ea1795bcce1019ac1ea03e28a, memory/builds/aEvidencedLens/spec/2026-10-05-spec-TOOL-aEvidencedLens-8.md@629cc42227ce6bb803160f25f74a9ce1fc3db2c4, memory/builds/aEvidencedLens/spec/2026-10-05-spec-TOOL-aEvidencedLens-11.md@69275b8ac283e870a83a368db20a8222fa0263fc · items 46 · scorable 45 · unscorable 1
replay: candidate C:/Users/DAILY-~1/AppData/Local/Temp/claude/C--projects-coding-governance--claude-worktrees-spec-review-improvements-f59dad/6b5d9f56-af37-4095-82f4-be050a2179ba/scratchpad/ab-replay-report.md · confirmed 39 · unscorable 1 · address section
MATCHED         memory/builds/aEvidencedLens/spec/2026-10-05-spec-TOOL-aEvidencedLens-6.md:§6  <-  memory/builds/aEvidencedLens/spec/2026-10-05-spec-TOOL-aEvidencedLens-6.md:section 6 AC7  [coherence]
MATCHED         memory/builds/aEvidencedLens/spec/2026-10-05-spec-TOOL-aEvidencedLens-4.md:§2  <-  memory/builds/aEvidencedLens/spec/2026-10-05-spec-TOOL-aEvidencedLens-4.md:section 2 S5  [coherence]
MATCHED         memory/builds/aEvidencedLens/spec/2026-10-05-spec-TOOL-aEvidencedLens-4.md:§2  <-  memory/builds/aEvidencedLens/spec/2026-10-05-spec-TOOL-aEvidencedLens-4.md:section 2 S5  [coherence]
MATCHED         memory/builds/aEvidencedLens/spec/2026-10-05-spec-TOOL-aEvidencedLens-4.md:§2  <-  memory/builds/aEvidencedLens/spec/2026-10-05-spec-TOOL-aEvidencedLens-4.md:section 2 S5  [coherence]
MATCHED         memory/builds/aEvidencedLens/spec/2026-10-05-spec-TOOL-aEvidencedLens-2.md:§2  <-  memory/builds/aEvidencedLens/spec/2026-10-05-spec-TOOL-aEvidencedLens-2.md:section 2 S3  [failure-envelope]
MATCHED         memory/builds/aEvidencedLens/spec/2026-10-05-spec-TOOL-aEvidencedLens-2.md:§2  <-  memory/builds/aEvidencedLens/spec/2026-10-05-spec-TOOL-aEvidencedLens-2.md:section 2 S3  [failure-envelope]
MATCHED         memory/builds/aEvidencedLens/spec/2026-10-05-spec-TOOL-aEvidencedLens-3.md:§2  <-  memory/builds/aEvidencedLens/spec/2026-10-05-spec-TOOL-aEvidencedLens-3.md:section 2 S3  [failure-envelope]
MATCHED         memory/builds/aEvidencedLens/spec/2026-10-05-spec-TOOL-aEvidencedLens-3.md:§2  <-  memory/builds/aEvidencedLens/spec/2026-10-05-spec-TOOL-aEvidencedLens-3.md:section 2 S3  [failure-envelope]
MATCHED         memory/builds/aEvidencedLens/spec/2026-10-05-spec-TOOL-aEvidencedLens-6.md:§2  <-  memory/builds/aEvidencedLens/spec/2026-10-05-spec-TOOL-aEvidencedLens-6.md:section 2 S3, section 4 Inventory, section 10  [reuse]
MATCHED         memory/builds/aEvidencedLens/spec/2026-10-05-spec-TOOL-aEvidencedLens-6.md:§2  <-  memory/builds/aEvidencedLens/spec/2026-10-05-spec-TOOL-aEvidencedLens-6.md:section 2 S3, section 4 Inventory, section 10  [reuse]
MATCHED         memory/builds/aEvidencedLens/spec/2026-10-05-spec-TOOL-aEvidencedLens-9.md:§2  <-  memory/builds/aEvidencedLens/spec/2026-10-05-spec-TOOL-aEvidencedLens-9.md:section 2 S3  [coherence]
MATCHED         memory/builds/aEvidencedLens/spec/2026-10-05-spec-TOOL-aEvidencedLens-9.md:§2  <-  memory/builds/aEvidencedLens/spec/2026-10-05-spec-TOOL-aEvidencedLens-9.md:section 2 S3  [coherence]
MATCHED         memory/builds/aEvidencedLens/spec/2026-10-05-spec-TOOL-aEvidencedLens-9.md:§2  <-  memory/builds/aEvidencedLens/spec/2026-10-05-spec-TOOL-aEvidencedLens-9.md:section 2 S3  [coherence]
MATCHED         memory/builds/aEvidencedLens/spec/2026-10-05-spec-TOOL-aEvidencedLens-10.md:§2  <-  memory/builds/aEvidencedLens/spec/2026-10-05-spec-TOOL-aEvidencedLens-10.md:section 2 S5  [coherence]
MATCHED         memory/builds/aEvidencedLens/spec/2026-10-05-spec-TOOL-aEvidencedLens-10.md:§2  <-  memory/builds/aEvidencedLens/spec/2026-10-05-spec-TOOL-aEvidencedLens-10.md:section 2 S5  [coherence]
MATCHED         memory/builds/aEvidencedLens/spec/2026-10-05-spec-TOOL-aEvidencedLens-5.md:§2  <-  memory/builds/aEvidencedLens/spec/2026-10-05-spec-TOOL-aEvidencedLens-5.md:section 2 S2  [failure-envelope]
MATCHED         memory/builds/aEvidencedLens/spec/2026-10-05-spec-TOOL-aEvidencedLens-6.md:§6  <-  memory/builds/aEvidencedLens/spec/2026-10-05-spec-TOOL-aEvidencedLens-6.md:section 6 AC7  [coherence]
MATCHED         memory/builds/aEvidencedLens/spec/2026-10-05-spec-TOOL-aEvidencedLens-2.md:§6  <-  memory/builds/aEvidencedLens/spec/2026-10-05-spec-TOOL-aEvidencedLens-2.md:section 6 AC8  [coherence]
MATCHED         memory/builds/aEvidencedLens/spec/2026-10-05-spec-TOOL-aEvidencedLens-10.md:§2  <-  memory/builds/aEvidencedLens/spec/2026-10-05-spec-TOOL-aEvidencedLens-10.md:section 2 S5  [coherence]
MATCHED         memory/builds/aEvidencedLens/spec/2026-10-05-spec-TOOL-aEvidencedLens-3.md:§4  <-  memory/builds/aEvidencedLens/spec/2026-10-05-spec-TOOL-aEvidencedLens-3.md:section 4 Evidence / section 2 S3  [grounding]
MATCHED         memory/builds/aEvidencedLens/spec/2026-10-05-spec-TOOL-aEvidencedLens-5.md:§2  <-  memory/builds/aEvidencedLens/spec/2026-10-05-spec-TOOL-aEvidencedLens-5.md:section 2 S2  [failure-envelope]
MATCHED         memory/builds/aEvidencedLens/spec/2026-10-05-spec-TOOL-aEvidencedLens-6.md:§2  <-  memory/builds/aEvidencedLens/spec/2026-10-05-spec-TOOL-aEvidencedLens-6.md:section 2 S3, section 4 Inventory, section 10  [reuse]
MATCHED         memory/builds/aEvidencedLens/spec/2026-10-05-spec-TOOL-aEvidencedLens-3.md:§2  <-  memory/builds/aEvidencedLens/spec/2026-10-05-spec-TOOL-aEvidencedLens-3.md:section 2 S3  [failure-envelope]
MATCHED         memory/builds/aEvidencedLens/spec/2026-10-05-spec-TOOL-aEvidencedLens-9.md:§2  <-  memory/builds/aEvidencedLens/spec/2026-10-05-spec-TOOL-aEvidencedLens-9.md:section 2 S3  [coherence]
MATCHED         memory/builds/aEvidencedLens/spec/2026-10-05-spec-TOOL-aEvidencedLens-5.md:§2  <-  memory/builds/aEvidencedLens/spec/2026-10-05-spec-TOOL-aEvidencedLens-5.md:section 2 S2  [failure-envelope]
MATCHED         memory/builds/aEvidencedLens/spec/2026-10-05-spec-TOOL-aEvidencedLens-5.md:§2  <-  memory/builds/aEvidencedLens/spec/2026-10-05-spec-TOOL-aEvidencedLens-5.md:section 2 S2  [failure-envelope]
MATCHED         memory/builds/aEvidencedLens/spec/2026-10-05-spec-TOOL-aEvidencedLens-5.md:§2  <-  memory/builds/aEvidencedLens/spec/2026-10-05-spec-TOOL-aEvidencedLens-5.md:section 2 S2  [failure-envelope]
MATCHED         memory/builds/aEvidencedLens/spec/2026-10-05-spec-TOOL-aEvidencedLens-9.md:§2  <-  memory/builds/aEvidencedLens/spec/2026-10-05-spec-TOOL-aEvidencedLens-9.md:section 2 S3  [coherence]
MATCHED         memory/builds/aEvidencedLens/spec/2026-10-05-spec-TOOL-aEvidencedLens-5.md:§2  <-  memory/builds/aEvidencedLens/spec/2026-10-05-spec-TOOL-aEvidencedLens-5.md:section 2 S2  [failure-envelope]
MATCHED         memory/builds/aEvidencedLens/spec/2026-10-05-spec-TOOL-aEvidencedLens-4.md:§2  <-  memory/builds/aEvidencedLens/spec/2026-10-05-spec-TOOL-aEvidencedLens-4.md:section 2 S5  [coherence]
MATCHED         memory/builds/aEvidencedLens/spec/2026-10-05-spec-TOOL-aEvidencedLens-9.md:§5  <-  memory/builds/aEvidencedLens/spec/2026-10-05-spec-TOOL-aEvidencedLens-9.md:section 5 user docs  [blast-radius]
MISSED          memory/builds/aEvidencedLens/spec/2026-10-05-spec-TOOL-aEvidencedLens-1.md:§2  5
MISSED          memory/builds/aEvidencedLens/spec/2026-10-05-spec-TOOL-aEvidencedLens-1.md:§6  6
MISSED          memory/builds/aEvidencedLens/spec/2026-10-05-spec-TOOL-aEvidencedLens-7.md:§2  13
MISSED          memory/builds/aEvidencedLens/spec/2026-10-05-spec-TOOL-aEvidencedLens-8.md:§2  14
MISSED          memory/builds/aEvidencedLens/spec/2026-10-05-spec-TOOL-aEvidencedLens-8.md:§2  16
MISSED          memory/builds/aEvidencedLens/spec/2026-10-05-spec-TOOL-aEvidencedLens-11.md:§2  22
MISSED          memory/builds/aEvidencedLens/spec/2026-10-05-spec-TOOL-aEvidencedLens-11.md:§2  23
MISSED          memory/builds/aEvidencedLens/spec/2026-10-05-spec-TOOL-aEvidencedLens-11.md:§2  29
MISSED          memory/builds/aEvidencedLens/spec/2026-10-05-spec-TOOL-aEvidencedLens-6.md:§7  30
MISSED          memory/builds/aEvidencedLens/spec/2026-10-05-spec-TOOL-aEvidencedLens-5.md:§6  33
MISSED          memory/builds/aEvidencedLens/spec/2026-10-05-spec-TOOL-aEvidencedLens-8.md:§5  45
MISSED          memory/builds/aEvidencedLens/spec/2026-10-05-spec-TOOL-aEvidencedLens-7.md:§2  46
MISSED          memory/builds/aEvidencedLens/spec/2026-10-05-spec-TOOL-aEvidencedLens-1.md:§10  48
MISSED          memory/builds/aEvidencedLens/spec/2026-10-05-spec-TOOL-aEvidencedLens-6.md:§10  49
UNSCORABLE      34
CANDIDATE-ONLY  memory/builds/aEvidencedLens/spec/2026-10-05-spec-TOOL-aEvidencedLens-11.md:section 6 AC6  [coherence]
CANDIDATE-ONLY  memory/builds/aEvidencedLens/spec/2026-10-05-spec-TOOL-aEvidencedLens-3.md:status header  [coherence]
CANDIDATE-ONLY  memory/builds/aEvidencedLens/spec/2026-10-05-spec-TOOL-aEvidencedLens-10.md:section 4 Evidence / section 2 S5  [grounding]
CANDIDATE-ONLY  memory/builds/aEvidencedLens/spec/2026-10-05-spec-TOOL-aEvidencedLens-7.md:section 7 Gates  [grounding]
CANDIDATE-ONLY  memory/builds/aEvidencedLens/spec/2026-10-05-spec-TOOL-aEvidencedLens-8.md:section 10  [grounding]
CANDIDATE-ONLY  memory/builds/aEvidencedLens/spec/2026-10-05-spec-TOOL-aEvidencedLens-7.md:section 4 Evidence (Suite readers)  [grounding]
CANDIDATE-ONLY  memory/builds/aEvidencedLens/spec/2026-10-05-spec-TOOL-aEvidencedLens-1.md:section 4 Self-test re-keying  [blast-radius]
CANDIDATE-ONLY  memory/builds/aEvidencedLens/spec/2026-10-05-spec-TOOL-aEvidencedLens-6.md:section 4 Files touched (estimate) and section 7  [blast-radius]
CANDIDATE-ONLY  memory/builds/aEvidencedLens/spec/2026-10-05-spec-TOOL-aEvidencedLens-10.md:section 4 Files touched (estimate) and section 7  [blast-radius]
CANDIDATE-ONLY  memory/builds/aEvidencedLens/spec/2026-10-05-spec-TOOL-aEvidencedLens-11.md:section 4 Files touched (estimate) and section 7  [blast-radius]
CANDIDATE-ONLY  memory/builds/aEvidencedLens/spec/2026-10-05-spec-TOOL-aEvidencedLens-7.md:section 7 and section 2 S10  [blast-radius]
CANDIDATE-ONLY  memory/builds/aEvidencedLens/spec/2026-10-05-spec-TOOL-aEvidencedLens-9.md:section 4 Files touched (estimate)  [blast-radius]
CANDIDATE-ONLY  memory/builds/aEvidencedLens/spec/2026-10-05-spec-TOOL-aEvidencedLens-2.md:section 4 The policy  [failure-envelope]
CANDIDATE-ONLY  memory/builds/aEvidencedLens/spec/2026-10-05-spec-TOOL-aEvidencedLens-2.md:section 4 The argument  [failure-envelope]
per-lens: blast-radius confirmed 10 matched 4 · coherence confirmed 8 matched 6 · failure-envelope confirmed 10 matched 8 · grounding confirmed 7 matched 3 · reuse confirmed 4 matched 4
per-lens known: contradiction confirmed 10 matched 6 · prior-art confirmed 5 matched 1 · underspecification confirmed 23 matched 16 · unstated-assumption confirmed 8 matched 8
replay: recall 31/45 = 0.69
```

## Reverse run — the replay as known, the round-1 record as candidate

`python tools/workflows/review_replay.py --known <scratch>/ab-replay-report.md --candidate memory/builds/aEvidencedLens/reviews/2026-10-05-review-TOOL-aEvidencedLens-1-spec-audit-round1.md`, exit 0, pasted whole:

```text
replay: known C:/Users/DAILY-~1/AppData/Local/Temp/claude/C--projects-coding-governance--claude-worktrees-spec-review-improvements-f59dad/6b5d9f56-af37-4095-82f4-be050a2179ba/scratchpad/ab-replay-report.md · kind spec-audit · unit raw-finding · subjects memory/builds/aEvidencedLens/spec/2026-10-05-spec-TOOL-aEvidencedLens-1.md@de140c3ea4acd5571eb7ee42f9cf4ebbb669e34c, memory/builds/aEvidencedLens/spec/2026-10-05-spec-TOOL-aEvidencedLens-2.md@1ea5a3a513b452f2072c8ab8825d2ba371e8c87e, memory/builds/aEvidencedLens/spec/2026-10-05-spec-TOOL-aEvidencedLens-3.md@075af74ddcb7603efee1e08d2eb2cbb5955616f9, memory/builds/aEvidencedLens/spec/2026-10-05-spec-TOOL-aEvidencedLens-4.md@099033058fe14bfe3407d038ddd4efaf0af34895, memory/builds/aEvidencedLens/spec/2026-10-05-spec-TOOL-aEvidencedLens-6.md@3f4fafd20ffdec3b119b9f4ab319f51e654717e0, memory/builds/aEvidencedLens/spec/2026-10-05-spec-TOOL-aEvidencedLens-10.md@88b6a0f1477ab70a89d33b09b05cf89c824a9b66, memory/builds/aEvidencedLens/spec/2026-10-05-spec-TOOL-aEvidencedLens-5.md@6d1c0773338495d741eccfa96cb18b2573507948, memory/builds/aEvidencedLens/spec/2026-10-05-spec-TOOL-aEvidencedLens-7.md@7d4dce07d8899d54bfff2a1e1515aa297b090950, memory/builds/aEvidencedLens/spec/2026-10-05-spec-TOOL-aEvidencedLens-9.md@9e4e4704eaa6dd5ea1795bcce1019ac1ea03e28a, memory/builds/aEvidencedLens/spec/2026-10-05-spec-TOOL-aEvidencedLens-8.md@629cc42227ce6bb803160f25f74a9ce1fc3db2c4, memory/builds/aEvidencedLens/spec/2026-10-05-spec-TOOL-aEvidencedLens-11.md@69275b8ac283e870a83a368db20a8222fa0263fc · items 39 · scorable 38 · unscorable 1
replay: candidate memory/builds/aEvidencedLens/reviews/2026-10-05-review-TOOL-aEvidencedLens-1-spec-audit-round1.md · confirmed 46 · unscorable 1 · address section
MATCHED         memory/builds/aEvidencedLens/spec/2026-10-05-spec-TOOL-aEvidencedLens-4.md:§2  <-  memory/builds/aEvidencedLens/spec/2026-10-05-spec-TOOL-aEvidencedLens-4.md:section 2 S4 / section 6 AC4  [underspecification]
MATCHED         memory/builds/aEvidencedLens/spec/2026-10-05-spec-TOOL-aEvidencedLens-9.md:§2  <-  memory/builds/aEvidencedLens/spec/2026-10-05-spec-TOOL-aEvidencedLens-9.md:section 2 S1 / section 6 AC1  [underspecification]
MATCHED         memory/builds/aEvidencedLens/spec/2026-10-05-spec-TOOL-aEvidencedLens-6.md:§6  <-  memory/builds/aEvidencedLens/spec/2026-10-05-spec-TOOL-aEvidencedLens-6.md:section 6 AC7  [underspecification]
MATCHED         memory/builds/aEvidencedLens/spec/2026-10-05-spec-TOOL-aEvidencedLens-2.md:§6  <-  memory/builds/aEvidencedLens/spec/2026-10-05-spec-TOOL-aEvidencedLens-2.md:section 6 AC1 against unit 3 section 2 S5 / AC3  [contradiction]
MATCHED         memory/builds/aEvidencedLens/spec/2026-10-05-spec-TOOL-aEvidencedLens-4.md:§2  <-  memory/builds/aEvidencedLens/spec/2026-10-05-spec-TOOL-aEvidencedLens-4.md:section 2 S4 / section 6 AC4  [underspecification]
MATCHED         memory/builds/aEvidencedLens/spec/2026-10-05-spec-TOOL-aEvidencedLens-10.md:§2  <-  memory/builds/aEvidencedLens/spec/2026-10-05-spec-TOOL-aEvidencedLens-10.md:section 2 S7 / section 6 AC1  [underspecification]
MATCHED         memory/builds/aEvidencedLens/spec/2026-10-05-spec-TOOL-aEvidencedLens-9.md:§2  <-  memory/builds/aEvidencedLens/spec/2026-10-05-spec-TOOL-aEvidencedLens-9.md:section 2 S1 / section 6 AC1  [underspecification]
MATCHED         memory/builds/aEvidencedLens/spec/2026-10-05-spec-TOOL-aEvidencedLens-3.md:§4  <-  memory/builds/aEvidencedLens/spec/2026-10-05-spec-TOOL-aEvidencedLens-3.md:section 4 The sentence (last line) / section 2 S3 against section 3 (uncertain default)  [contradiction]
MATCHED         memory/builds/aEvidencedLens/spec/2026-10-05-spec-TOOL-aEvidencedLens-2.md:§6  <-  memory/builds/aEvidencedLens/spec/2026-10-05-spec-TOOL-aEvidencedLens-2.md:section 6 AC1 against unit 3 section 2 S5 / AC3  [contradiction]
MATCHED         memory/builds/aEvidencedLens/spec/2026-10-05-spec-TOOL-aEvidencedLens-9.md:§2  <-  memory/builds/aEvidencedLens/spec/2026-10-05-spec-TOOL-aEvidencedLens-9.md:section 2 S1 / section 6 AC1  [underspecification]
MATCHED         memory/builds/aEvidencedLens/spec/2026-10-05-spec-TOOL-aEvidencedLens-6.md:§2  <-  memory/builds/aEvidencedLens/spec/2026-10-05-spec-TOOL-aEvidencedLens-6.md:section 2 S5 / section 6 AC4, AC5  [underspecification]
MATCHED         memory/builds/aEvidencedLens/spec/2026-10-05-spec-TOOL-aEvidencedLens-6.md:§2  <-  memory/builds/aEvidencedLens/spec/2026-10-05-spec-TOOL-aEvidencedLens-6.md:section 2 S5 / section 6 AC4, AC5  [underspecification]
MATCHED         memory/builds/aEvidencedLens/spec/2026-10-05-spec-TOOL-aEvidencedLens-10.md:§2  <-  memory/builds/aEvidencedLens/spec/2026-10-05-spec-TOOL-aEvidencedLens-10.md:section 2 S7 / section 6 AC1  [underspecification]
MATCHED         memory/builds/aEvidencedLens/spec/2026-10-05-spec-TOOL-aEvidencedLens-9.md:§2  <-  memory/builds/aEvidencedLens/spec/2026-10-05-spec-TOOL-aEvidencedLens-9.md:section 2 S1 / section 6 AC1  [underspecification]
MATCHED         memory/builds/aEvidencedLens/spec/2026-10-05-spec-TOOL-aEvidencedLens-9.md:§2  <-  memory/builds/aEvidencedLens/spec/2026-10-05-spec-TOOL-aEvidencedLens-9.md:section 2 S1 / section 6 AC1  [underspecification]
MATCHED         memory/builds/aEvidencedLens/spec/2026-10-05-spec-TOOL-aEvidencedLens-9.md:§5  <-  memory/builds/aEvidencedLens/spec/2026-10-05-spec-TOOL-aEvidencedLens-9.md:section 5 user docs (and unit 11 section 2 S5 / section 6 AC5)  [prior-art]
MATCHED         memory/builds/aEvidencedLens/spec/2026-10-05-spec-TOOL-aEvidencedLens-9.md:§2  <-  memory/builds/aEvidencedLens/spec/2026-10-05-spec-TOOL-aEvidencedLens-9.md:section 2 S1 / section 6 AC1  [underspecification]
MATCHED         memory/builds/aEvidencedLens/spec/2026-10-05-spec-TOOL-aEvidencedLens-4.md:§2  <-  memory/builds/aEvidencedLens/spec/2026-10-05-spec-TOOL-aEvidencedLens-4.md:section 2 S4 / section 6 AC4  [underspecification]
MATCHED         memory/builds/aEvidencedLens/spec/2026-10-05-spec-TOOL-aEvidencedLens-9.md:§2  <-  memory/builds/aEvidencedLens/spec/2026-10-05-spec-TOOL-aEvidencedLens-9.md:section 2 S1 / section 6 AC1  [underspecification]
MATCHED         memory/builds/aEvidencedLens/spec/2026-10-05-spec-TOOL-aEvidencedLens-9.md:§5  <-  memory/builds/aEvidencedLens/spec/2026-10-05-spec-TOOL-aEvidencedLens-9.md:section 5 user docs (and unit 11 section 2 S5 / section 6 AC5)  [prior-art]
MATCHED         memory/builds/aEvidencedLens/spec/2026-10-05-spec-TOOL-aEvidencedLens-5.md:§2  <-  memory/builds/aEvidencedLens/spec/2026-10-05-spec-TOOL-aEvidencedLens-5.md:section 2 S8, S9 / section 6 AC5, AC8  [underspecification]
MATCHED         memory/builds/aEvidencedLens/spec/2026-10-05-spec-TOOL-aEvidencedLens-5.md:§2  <-  memory/builds/aEvidencedLens/spec/2026-10-05-spec-TOOL-aEvidencedLens-5.md:section 2 S8, S9 / section 6 AC5, AC8  [underspecification]
MATCHED         memory/builds/aEvidencedLens/spec/2026-10-05-spec-TOOL-aEvidencedLens-3.md:§2  <-  memory/builds/aEvidencedLens/spec/2026-10-05-spec-TOOL-aEvidencedLens-3.md:section 2 S6 / section 6 AC4, AC5  [underspecification]
MATCHED         memory/builds/aEvidencedLens/spec/2026-10-05-spec-TOOL-aEvidencedLens-3.md:§2  <-  memory/builds/aEvidencedLens/spec/2026-10-05-spec-TOOL-aEvidencedLens-3.md:section 2 S6 / section 6 AC4, AC5  [underspecification]
MATCHED         memory/builds/aEvidencedLens/spec/2026-10-05-spec-TOOL-aEvidencedLens-2.md:§2  <-  memory/builds/aEvidencedLens/spec/2026-10-05-spec-TOOL-aEvidencedLens-2.md:section 2 S7 / section 6 AC8  [underspecification]
MISSED          memory/builds/aEvidencedLens/spec/2026-10-05-spec-TOOL-aEvidencedLens-11.md:§6  3
MISSED          memory/builds/aEvidencedLens/spec/2026-10-05-spec-TOOL-aEvidencedLens-10.md:§4  12
MISSED          memory/builds/aEvidencedLens/spec/2026-10-05-spec-TOOL-aEvidencedLens-7.md:§7  14
MISSED          memory/builds/aEvidencedLens/spec/2026-10-05-spec-TOOL-aEvidencedLens-8.md:§10  16
MISSED          memory/builds/aEvidencedLens/spec/2026-10-05-spec-TOOL-aEvidencedLens-7.md:§4  17
MISSED          memory/builds/aEvidencedLens/spec/2026-10-05-spec-TOOL-aEvidencedLens-1.md:§4  23
MISSED          memory/builds/aEvidencedLens/spec/2026-10-05-spec-TOOL-aEvidencedLens-6.md:§4  24
MISSED          memory/builds/aEvidencedLens/spec/2026-10-05-spec-TOOL-aEvidencedLens-10.md:§4  25
MISSED          memory/builds/aEvidencedLens/spec/2026-10-05-spec-TOOL-aEvidencedLens-11.md:§4  26
MISSED          memory/builds/aEvidencedLens/spec/2026-10-05-spec-TOOL-aEvidencedLens-7.md:§7  28
MISSED          memory/builds/aEvidencedLens/spec/2026-10-05-spec-TOOL-aEvidencedLens-9.md:§4  31
MISSED          memory/builds/aEvidencedLens/spec/2026-10-05-spec-TOOL-aEvidencedLens-2.md:§4  37
MISSED          memory/builds/aEvidencedLens/spec/2026-10-05-spec-TOOL-aEvidencedLens-2.md:§4  38
UNSCORABLE      8
CANDIDATE-ONLY  memory/builds/aEvidencedLens/spec/2026-10-05-spec-TOOL-aEvidencedLens-1.md:section 2 S6 / section 6 AC8  [underspecification]
CANDIDATE-ONLY  memory/builds/aEvidencedLens/spec/2026-10-05-spec-TOOL-aEvidencedLens-1.md:section 6 AC8  [underspecification]
CANDIDATE-ONLY  memory/builds/aEvidencedLens/spec/2026-10-05-spec-TOOL-aEvidencedLens-7.md:section 2 S6 / section 6 AC7  [underspecification]
CANDIDATE-ONLY  memory/builds/aEvidencedLens/spec/2026-10-05-spec-TOOL-aEvidencedLens-8.md:section 2 S1 / section 6 AC1  [underspecification]
CANDIDATE-ONLY  memory/builds/aEvidencedLens/spec/2026-10-05-spec-TOOL-aEvidencedLens-8.md:section 2 S8 / section 6 AC9  [underspecification]
CANDIDATE-ONLY  memory/builds/aEvidencedLens/spec/2026-10-05-spec-TOOL-aEvidencedLens-11.md:section 2 S1 / section 6 AC1, AC2  [underspecification]
CANDIDATE-ONLY  memory/builds/aEvidencedLens/spec/2026-10-05-spec-TOOL-aEvidencedLens-11.md:section 2 S3, S4 / section 6 AC4, AC6  [underspecification]
CANDIDATE-ONLY  memory/builds/aEvidencedLens/spec/2026-10-05-spec-TOOL-aEvidencedLens-11.md:section 2 S3 (counts paragraph) against unit 8 section 2 S5/S6  [contradiction]
CANDIDATE-ONLY  memory/builds/aEvidencedLens/spec/2026-10-05-spec-TOOL-aEvidencedLens-6.md:section 7 New arm lines (also unit 5 and unit 8 section 7) against units 1-4 section 7  [contradiction]
CANDIDATE-ONLY  memory/builds/aEvidencedLens/spec/2026-10-05-spec-TOOL-aEvidencedLens-5.md:section 6 AC7 against section 2 S8  [contradiction]
CANDIDATE-ONLY  memory/builds/aEvidencedLens/spec/2026-10-05-spec-TOOL-aEvidencedLens-3.md:status header (also unit 4 status header)  [contradiction]
CANDIDATE-ONLY  memory/builds/aEvidencedLens/spec/2026-10-05-spec-TOOL-aEvidencedLens-8.md:section 5 perf / scale (and section 3, section 10)  [prior-art]
CANDIDATE-ONLY  memory/builds/aEvidencedLens/spec/2026-10-05-spec-TOOL-aEvidencedLens-7.md:section 2 S8, and section 3 'A cutoff for old rows'  [prior-art]
CANDIDATE-ONLY  memory/builds/aEvidencedLens/spec/2026-10-05-spec-TOOL-aEvidencedLens-1.md:section 10 Reuse audit  [prior-art]
CANDIDATE-ONLY  memory/builds/aEvidencedLens/spec/2026-10-05-spec-TOOL-aEvidencedLens-6.md:section 10 Reuse audit  [prior-art]
per-lens: contradiction confirmed 10 matched 6 · prior-art confirmed 5 matched 1 · underspecification confirmed 23 matched 16 · unstated-assumption confirmed 8 matched 8
per-lens known: blast-radius confirmed 10 matched 4 · coherence confirmed 8 matched 6 · failure-envelope confirmed 10 matched 8 · grounding confirmed 7 matched 3 · reuse confirmed 4 matched 4
replay: recall 25/38 = 0.66
```

## Per lens

Each lens's raw, confirmed and refuted findings, counted off each report's `## Appendix — every
finding` by its `lens` and `verdict` columns; precision is confirmed over confirmed plus refuted. No
row of either appendix is uncertain or unverified.

Round 1, four lenses:

| lens | raw | confirmed | refuted | precision |
|---|---|---|---|---|
| contradiction | 11 | 10 | 1 | 0.91 |
| underspecification | 24 | 23 | 1 | 0.96 |
| unstated-assumption | 9 | 8 | 1 | 0.89 |
| prior-art | 5 | 5 | 0 | 1.00 |
| total | 49 | 46 | 3 | 0.94 |

The replay, five lenses, which agree with the replay report's own lens-yield table:

| lens | raw | confirmed | refuted | precision |
|---|---|---|---|---|
| coherence | 8 | 8 | 0 | 1.00 |
| grounding | 9 | 7 | 2 | 0.78 |
| reuse | 4 | 4 | 0 | 1.00 |
| blast-radius | 10 | 10 | 0 | 1.00 |
| failure-envelope | 11 | 10 | 1 | 0.91 |
| total | 42 | 39 | 3 | 0.93 |

## Old against new

Items and raw findings by severity are each report's own adjudicated tally: the round-1 record's
`## Review shape` and the replay report's severity table.

| measure | round 1 | replay |
|---|---|---|
| raw | 49 | 42 |
| confirmed | 46 | 39 |
| refuted | 3 | 3 |
| precision | 0.94 | 0.93 |
| items BLOCKER / HIGH / MEDIUM / LOW | 0 / 3 / 11 / 9, 23 in all | 0 / 2 / 20 / 10, 32 in all |
| raw confirmed BLOCKER / HIGH / MEDIUM / LOW | 0 / 3 / 26 / 17 | 0 / 4 / 25 / 10 |
| recall of the other side, section level | 25/38 = 0.66 of the replay's | 31/45 = 0.69 of round 1's |

## Liveness at this unit's base

Every replay-only HIGH or MEDIUM finding of the forward run, and the two HIGH items that matched
round 1 only at section level, probed at base `f86bf4826`. A finding not live is recorded and
changes nothing, a §3 non-goal of spec 21.

| replay id | defect | at base | probe |
|---|---|---|---|
| 3 | spec 11's AC6 grep cannot print nothing on a correct build | not live | `git show f86bf4826:memory/builds/aEvidencedLens/spec/2026-10-05-spec-TOOL-aEvidencedLens-11.md`: the status header reads `CLOSED · rev-3`, and AC6 at lines 207-208 runs with `':!memory/gotchas'`, which excludes the two history gotchas the finding named |
| 12 | spec 10's subject pins are read from the opening line, which is the Serves line | not live | `git show f86bf4826:tools/workflows/review_replay.py`: `extract_subject_pins` at line 127 reads every pin after the binding line and before the first `## ` |
| 14 | spec 7's new and reworded `fail 37` sentences carry no arm duty | not live | `python tools/memory-tree/check-arms.py --check` exited 0 |
| 23 | spec 1's re-keying table misses the summed-kind arm `uvp.length` | not live | `git show f86bf4826:tools/workflows/tier2-review.test.sh` line 936 reads `uvp.length === 10` |
| 24 | spec 6 mints top-level functions with no `symbols.json` regeneration | not live | `git show f86bf4826:memory/map/generated/symbols.json` names `deriveLensYield` and `renderLensYield` |
| 25 | spec 10 mints functions with no `symbols.json` regeneration | not live | the same file names `read_record_kind` and `extract_section_ref` |
| 26 | re-rendering BUILD-METHOD owes the kickoff manifest a re-stamp | not live | `bash skills/session-kickoff/manifest-check.sh memory/guides/SESSION-KICKOFF.md` exited 0 |
| 28 | spec 7's §7 omits the harness-arms leg its arm duty trips | not live | `python tools/memory-tree/check-arms.py --check` exited 0 |
| 37 | every probing agent shares one scratch directory | LIVE, fixed by S5 | `git show f86bf4826:tools/workflows/tier2-review.template.js \| grep -c "named for your own role"` printed 0; this unit adds the per-role rule to `PROBE_RULES` |
| 38 | the scratch-under-repo test is textual: a relative `repo`, MSYS spellings and `..` unfolded | LIVE in part, fixed by S1 | AC1's prelude probe over the base render: `repo "."`, `C:/p/x` beside `/c/p/x/t`, `/c/p/x` beside `C:/p/x/t` and `/tmp/r` beside `/tmp/q/../r/x` all proceeded; the prefix-sibling case `/tmp/rs` beside `/tmp/r` was already correct |
| H1 (id 1) | the moved-text read resolves `<path>` outside `repo` | not live | `git show f86bf4826:tools/workflows/tier2-review.template.js` line 892 hands `git -C ${repo} diff <blob> -- <path>` |
| H2 (ids 2, 10, 22) | check 19's terminal walk is keyed on the grant scan alone | not live | `git show f86bf4826:tools/unattended/check-unattended.sh` line 2483 walks on `[ -n "$maywr$mayrw" ]`, unit 14's fix |
