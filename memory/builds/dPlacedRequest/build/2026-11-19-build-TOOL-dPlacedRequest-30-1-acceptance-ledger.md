# TOOL-dPlacedRequest-30 — acceptance ledger

**Serves:** journal TOOL-dPlacedRequest-30

The unit was built from its spec at rev-6 (PINNED) on base `0c2ddd6f8`. `tools/unattended/unattended.sh#write_request_record`
now compares, once the key and the common dir resolve and before the store is made, the stored copy
`<git-common-dir>/requests/<key>.md` with the file, both through the new
`tools/unattended/unattended.sh#derive_request_fold` (a leading BOM dropped, every run of space, tab, CR, LF,
form feed or vertical tab one space, the ends trimmed: one `sed` and `tr` pipeline per text) and `cmp -s` over
the two; a difference prints `request not written — <key> · collision: a different text keys alike, the
stored copy is <path>` and returns 2, so no copy, no `.typed` line, no commit and no push follow (S1). Equal
folds fall through to `TOOL-dPlacedRequest-19`'s S2 and S3 unchanged (S2). The verbs guide's `--request` row
names the collision line and exit 2, rendered byte for byte into `memory/guides/UNATTENDED-VERBS.md` (S3),
and the request paragraph of `help/loop.md` names it too, its usage anchor unmoved because the usage line is.
The refusal is an `echo` and `return 2` like the verb's other outcomes, so no `fail` call site was added.

No gate, suite or bar ran in this pass. Each criterion was observed by a probe script in the run's scratch
directory over a fixture of the suite's own `mkconf` and `write_lease_fixture`, read out of
`tools/unattended/unattended.test.sh` by `sed`: a bare origin and one clone with `RUN_CLAIMS=on` under the
node's short temp path, the driver run as `daily-agent` (node a) under session `qA`.

**Evidences:** TOOL-dPlacedRequest-30
- AC1 — after `--request a.md` recorded key `c69a4b8070b6` (DERIVED), `--request b.md`, the same words with
  the ISO date one day later, exited 2 (PINNED) printing `request not written — c69a4b8070b6 · collision: a
  different text keys alike, the stored copy is <clone>/.git/requests/c69a4b8070b6.md`; the stored copy stayed
  byte-identical to `a.md`, the `.typed` file held 1 line (PINNED) before and after, and
  `refs/gov/requests/c69a4b8070b6` on the origin was unmoved. The base driver, the first-copy rule, exited 0
  (PINNED) `already recorded` on the same pair.
- AC2 — `a.md` again, its CRLF copy, its BOM-and-CRLF copy and a copy re-wrapped at another width each exited
  0 (PINNED) printing `request — c69a4b8070b6 · already recorded refs/gov/requests/c69a4b8070b6`, and after each
  the stored copy was byte-identical to `a.md`.
- AC3 — `grep -n 'collision' tools/unattended/VERBS.template.md` prints the `--request` row's line naming
  `request not written — <key> · collision: ...` and `(exit 2)`; `cmp` of the template and
  `memory/guides/UNATTENDED-VERBS.md` reads identical.

**Owed at the close.** The `New arm:` line of section 7: the `TOOL-dPlacedRequest-30` arm at the end of the
region-8 `TOOL-dPlacedRequest-19` block in `tools/unattended/unattended.test.sh`, 6 assertions (DERIVED: 5
`same`, the AC2 loop's 4 among them, and 1 `hit`). Its RED-first observation is the close's, staged against
the first-copy rule (the compare removed) and a raw `cmp -s` (the two `derive_request_fold` calls replaced by
the two paths). A probe of this pass ran the arm's own lines, read out of the suite by `sed`, under stub
`same` and `hit` printers over the fixture above: all 6 (DERIVED) passed on this driver; under the base
driver the AC1 `same` and its `hit` failed and the AC2 four passed; under the raw-`cmp -s` driver the AC1 pair
and the identical copy passed and the CRLF, BOM and re-wrapped copies failed. That probe is no suite reading.
The suite is waived for this build's landing by README rule 8. The floors rose by the same 6 (DERIVED):
`FLOOR_ASSERTIONS` and `FLOOR_SHARD_8`.

**The checklist, acted on.** The bug-class checklist over the pass commit selected 54 classes (DERIVED: 48
by an anchor, 6 universal). One needed a change. fixture-passes-by-finding-nothing: the AC1 assertion's
`.typed` count could not move under a write the refusal let through, because the block's session `qA` was
already named there and the writer appends a session once; the date-differing request now runs under
session `qC`, so the first-copy rule reads `0 identical 2` against the wanted `2 identical 1` (PINNED), a
probe of the arm's lines observed under the base driver. refusal-branch-with-no-arm: the one branch this
pass adds, the collision, is the arm's AC1. guard-above-a-fold-makes-its-fallback-dead: the compare runs
only where the stored copy exists, so the copy branch below it still runs on an absent one. topology-sweep:
two sessions racing one key between the compare and the copy is `TOOL-dPlacedRequest-43`'s, the hand-off
the spec's edges name. The verbs template and its render are byte-identical, and the codebase map was
regenerated for the new `derive_request_fold`.
