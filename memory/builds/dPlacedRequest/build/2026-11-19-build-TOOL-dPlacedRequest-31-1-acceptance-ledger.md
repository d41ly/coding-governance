# TOOL-dPlacedRequest-31 — acceptance ledger

**Serves:** journal TOOL-dPlacedRequest-31

The unit was built from its spec at rev-4 (PINNED) on base `3100d2abd`. `tools/unattended/unattended.sh#write_request_record`
now appends `<session><TAB><blob>` to `<git-common-dir>/requests/<key>.typed`, the blob `GIT hash-object --
<file>` of the bytes this session submitted, once per session and blob; a hash that does not answer, or
answers other than an object id, is refused through the append's own `this session could not be added to`
line, so no line without a blob is written and no new refusal site was added (S1).
`tools/unattended/unattended.sh#check_request_consent` hashes `<git-common-dir>/requests/<key>.md` as it reads
now and returns 0 only on an exact line `<this session><TAB><that blob>`; a missing copy, a line naming other
bytes and a line of any other shape read as no consent, printing `TOOL-dPlacedRequest-19` S5's `relayed` line
(S2). The verbs guide's `--request` row says consent is bound to the stored words, rendered byte for byte into
`memory/guides/UNATTENDED-VERBS.md` (S3), and the request paragraph of `help/loop.md` says so too, its usage
anchor unmoved because the usage line is.

No gate, suite or bar ran in this pass. Each criterion was observed by a probe script in the run's scratch
directory that ran the region-8 `TOOL-dPlacedRequest-19` block of `tools/unattended/unattended.test.sh`, its
`TOOL-dPlacedRequest-30` and `TOOL-dPlacedRequest-31` arms included, read out by `sed` with the suite's
`mkconf`, `write_lease_fixture` and `read_lease_field`, under stub `same` and `hit` printers: a bare origin and
two clones under the node's short temp path, `core.autocrlf` false as the fixture sets it.

**Evidences:** TOOL-dPlacedRequest-31
- AC1 — after session `qA` ran `--request req.md` on clone c1, `check_request_consent` in `qA` returned 0
  (PINNED); with `<git-common-dir>/requests/<key>.md` overwritten by `date.md`, the same words one day later and
  the same key, it returned 1 (PINNED) printing `request — <key> · relayed: data with provenance, never
  consent`. The base driver returned 0 on the replaced copy.
- AC2 — a line `qD<TAB><blob of date.md>` planted in `<git-common-dir>/requests/<key>.typed` beside req.md's
  stored copy left `qD` at 1 (PINNED) and `relayed`; a second line naming the stored copy's blob turned it to 0
  (PINNED), so the 1 is the blob's and not a predicate that refuses every line. A session-only line planted
  for `qE` read 1 (PINNED); the base driver read it 0.
- AC3 — `awk -F'\t' 'NF != 2 || $2 !~ /^[0-9a-f]{40}$/'` over the non-empty `.typed` file after the requests
  printed nothing; under the base driver it printed `qA`.
- AC4 — `grep -n 'consent' tools/unattended/VERBS.template.md` prints the `--request` row's lines saying
  `consent is bound to the stored words`; `cmp` of the template and `memory/guides/UNATTENDED-VERBS.md` reads
  identical. A further probe in a scratch repository observed a missing stored copy read as no consent, 1
  (PINNED), and the same line with the copy present 0 (PINNED).

**Owed at the close.** The `New arm:` line of section 7: the `TOOL-dPlacedRequest-31` arm at the end of the
region-8 `TOOL-dPlacedRequest-19` block, 8 assertions (DERIVED: 7 `same` and 1 `hit`), beside the block's
`DPR19 AC2` assertion, whose `.typed` reading now carries the blob. Its RED-first observation is the close's,
staged against the session-only `.typed` line and its predicate. The probe above ran all 51 (DERIVED) of the
block's assertions green on this driver; under the base driver 5 (DERIVED) failed: `DPR19 AC2`, `DPR31 AC3`,
the replaced-copy `DPR31 AC1`, the stored-blob `DPR31 AC2` and `DPR31 S2`. That probe is no suite reading.
The suite is waived for this build's landing by README rule 8. The floors rose by the same 8 (DERIVED):
`FLOOR_ASSERTIONS` and `FLOOR_SHARD_8`.
