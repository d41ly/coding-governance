# TOOL-dDerivedDocket-33 — acceptance ledger

**Serves:** journal TOOL-dDerivedDocket-33

The delegated signing is a build-folder script,
`memory/builds/dDerivedDocket/build/2026-09-22-build-TOOL-dDerivedDocket-33-signer.py`, and its two
records sit beside it. They sign unit 11's worksheet pair, computed at `e21fa86f`: 153 same-id pairs,
66 of them `unit` and 87 `not-unit`, and 334 triage asks, 333 of them KEEP and one excluded under T1.

The spec went to rev-6 before these observations were made. Over the real worksheet, rev-5's T2 and
T3 would have signed 67 closures on evidence that does not declare one. Of those, 46 were bare
citations in commit bodies, at least 11 of them saying the ask stays open; 20 were commits about the
ask's own same-id spec; and one was a mined phrase about another shape. §8 F9 records the fork and §4
the measurement. At rev-6, CLOSED comes only from a spec header's `closes` verb or a commit subject,
and a withdrawal only from a row's status slot or its text's opening word. So this worksheet signs no
closure and no withdrawal, and each of the 67 refused rows is KEEP naming the rule that refused it.

No merge bar, gate leg or `*.test.sh` suite ran in this pass. The observations below come from the
signer itself, from its `--check` over worksheet copies under the run's scratch root, and from the
three direct reads the spec names: `anchor_at`, `corpus_ids.py --check` and the planner's `--plan`.
Some fixtures had to be read at a pinned tree. For those, `git commit-tree` built one fixture commit
with no ref. Its tree is `e21fa86f`'s with eleven synthetic ask rows appended to
`memory/backlog/TOOL.md` from line 533. Its subject names one synthetic ask, and its body cites
another. The synthetic ids live only in the scratch worksheets, so no tracked file cites an id that
nothing defines.

**Evidences:** TOOL-dDerivedDocket-33
- AC1 — `--check` — two signing runs over the pair wrote byte-identical records, 31140 and 41652
  bytes, and `--check` then exited 0 reading "2 of 2 record(s) re-derive byte-identical".
- AC2 — `--check` — with `DEPL-aHoistedPass-2`'s KEEP edited to CLOSED in the tracked triage record,
  `--check` exited 1, printed the one-line diff and "DEPL-aHoistedPass-2 — tracked T6 CLOSED,
  re-derived T6 KEEP". It exited 0 again once the bytes were restored.
- AC3 — `TOOL-dFramedEntrypoint-1` — it and the other three design-named pairs read `U2 not-unit`,
  and all 66 `unit` rows cite `specced-in-place` or `born-in-spec-commit` evidence under rule `all`.
- AC4 — amended rev-6 — `closes`: CLOSED is now read from a spec header's `closes` verb or a commit
  subject, for an ask that is no spec H1. §9 rev-6 and §8 F9 log the change. The tracked record has
  no CLOSED row. Over the synthetic arms, the ask the fixture commit's subject names signed CLOSED
  under T3. An ask proposed CLOSED by `TOOL-dRetiredFork-4` signed CLOSED under T2 while that spec's
  header carried `closes` for it, and KEEP with the header as tracked. The ask the commit names
  only in its body signed KEEP naming T3. The spec file was restored byte-identical, and
  `git diff --quiet` on it exited 0.
- AC5 — `KEEP` — all 333 KEEP rows are T6, and every reason names a rule from T2 to T5. The 67
  rows whose proposal a rule refused each open with that rule's `refused:` clause.
- AC6 — `TOOL-aWeighedCompass-3` — the record carries one line naming it, under `## Exclusions`,
  and that line gives the flip's WONTDO disposal as the reason.
- AC7 — `unlabelled` — it is the only severity value in the record, and the header states the
  census "0 of 590 legacy row(s)" at `e21fa86f`, which the script derived there.
- AC8 — `anchor_at` — over all 528 lines of the two records, `grammar_for(root)` anchored no id, and
  `python tools/memory-tree/corpus_ids.py --check` exited 0 over the staged tree, reporting no
  collision.
- AC9 — `memory/DECISIONS.md` — the TOOL heading gains one row keyed `TOOL-dDerivedDocket-33`, 284
  characters, naming both records by path and pointing at the spec's §4 for the rules.
- AC10 — `--check` — over a triage copy with one synthetic row added, the triage record's diff was
  that one row, the triage-worksheet line with its path and blob, and the counts line. The same-id
  record differed in those two header lines only.
- AC11 — `--check` — an empty same-id worksheet and a triage copy with an 8-cell row each exited 2,
  under the signing run and `--check` alike. The messages named `empty.tsv:1` and
  `bad-triage.tsv:11`, and both default records were left byte-identical.
- AC12 — amended rev-6 — `unit-inserted`: the criterion now uses the planner's option spelling and
  what the planner actually prints. `migrate_backlog.py --plan --signed same-id=… --signed triage=…`,
  run from `tools/memory-tree/`, exited 0 after 3m43s with `unit-inserted: 66`, where unit 11's
  unsigned census reads 0. It ran over the records as first signed. The later re-sign changed one
  prose line of the triage header and no table row or header cell.
- AC13 — `--tail switch` — the pair's triage `#` line named the fixture commit. Its one added row
  cites `memory/backlog/TOOL.md:533`, which holds `TOOL-aDeferredBar-13` in the working tree. At
  the fixture commit, that line holds the added ask's own OPEN row, whose text opens with WITHDRAWN.
  `--tail switch` then `--tail landing` wrote four records whose rows equal the default rows plus
  that one row, signed `T4 WONTDO` from the text read there. Each header names both worksheet paths
  and blobs and the fixture's sha.
  The `-switch` pair was byte-identical after the landing run and the default records were
  unchanged. Once the four were removed, `git status --porcelain` matched its pre-run reading.
- AC14 — `not-unit` — over three synthetic same-id rows, the `specced-in-place` row with the
  low-overlap flag signed `U3 not-unit`. The row naming a missing spec and the row whose spec's H1
  lacks the id each signed `U4 not-unit`.
- AC15 — `KEEP` — at the fixture commit, four rows each signed KEEP: a proposed WONTDO over an OPEN
  slot (T4), a BLOCKED on a target its row does not name (T5), a BLOCKED on `TOOL-dRetiredFork-4`,
  which is not live (T5), and a DEFERRED over an OPEN slot (T5). The WONTDO row's prose says
  "withdrawn" mid-text and was not read as a withdrawal. Three positive controls signed: a BLOCKED
  and a DEFERRED on the live `TOOL-dDerivedDocket-34` whose rows name it, as `T5 BLOCKED` and
  `T5 DEFERRED`, and a row whose status slot reads WITHDRAWN, as `T4 WONTDO`.
