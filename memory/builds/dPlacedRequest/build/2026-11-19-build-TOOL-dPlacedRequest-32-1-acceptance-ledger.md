# TOOL-dPlacedRequest-32 — acceptance ledger

**Serves:** journal TOOL-dPlacedRequest-32

The unit was built from its spec at rev-5 (PINNED) on base `67fc0923d`. The session is
`CLAUDE_CODE_SESSION_ID`, read as `${CLAUDE_CODE_SESSION_ID:-absent}` where `TOOL-dPlacedRequest-19` and
`TOOL-dPlacedRequest-1` read it, so unset, empty and the literal `absent` are the one value `absent`, no
session (S1). `tools/unattended/unattended.sh#write_request_record` still writes the remote record with
`session: absent` as provenance but appends no `.typed` line with no session, and
`tools/unattended/unattended.sh#check_request_consent` returns 1 printing `request — <key> · no session: the
harness exposed none, so nothing here is consent` before any read (S2). In
`tools/unattended/unattended.sh#check_claim_writable`, the `lease` mode's `mine` row now needs the session
handed in to be present, neither empty nor `absent`, as well as equal to the record's and under this node's
fleet tag; the column is handed no keepalive, a `--lease` write recording `keepalive: absent`, so with either
session absent no `lease`-mode read is `mine`, while the run columns' keepalive rows are untouched (S3).
`tools/unattended/unattended.sh#run_lease_verb` prints `lease not written — no session:
CLAUDE_CODE_SESSION_ID is unset and no keepalive identifies this holder` and exits 2 right after the
`RUN_CLAIMS` switch, before any read (S4). The stops guide's section 7 states the source, the absent rule
and the refusal, rendered byte for byte into `memory/guides/UNATTENDED-STOPS.md` (S5), and `help/loop.md`'s
request and lease paragraphs say the same, their usage anchors unmoved because no usage line moved.

No gate, suite or bar ran in this pass. The criteria were observed by two probe scripts in the run's scratch
directory over a bare origin and a clone under the node's short temp path, built by the suite's own
`mkconf` and `write_lease_fixture`: one driving the driver's CLI and sourcing it for the two in-process
reads, and one running the lease-fixture half of the new suite block, extracted by `sed`, under stub `same`
and `hit` printers.

**Evidences:** TOOL-dPlacedRequest-32
- AC1 — `--request` with CLAUDE_CODE_SESSION_ID unset exited 0 (PINNED) printing `recorded`; the remote
  record's `session` line read `absent`, `<git-common-dir>/requests/<key>.md` was kept and no
  `<git-common-dir>/requests/<key>.typed` existed. With an `absent<TAB><blob>` line planted there, naming the
  stored copy's blob as the base driver would have written it, `check_request_consent <key>` in that
  environment returned 1 (PINNED) printing the `no session` line.
- AC2 — the same with `CLAUDE_CODE_SESSION_ID=absent`: the same exit 0, `session: absent`, no `.typed` line
  and a refusal of 1 (PINNED) over the planted line. A control request under session `qN` still wrote its
  `.typed` line and consented, 0 (PINNED), so the refusal is the absent session's and not the predicate's.
- AC3 — `--lease acquire build tFix` with the session unset, then `absent`, each exited 2 (PINNED) printing
  the `no session` line; the origin held 0 (DERIVED) refs under `refs/gov` and no
  `<git-common-dir>/gov-last-fetch` was stamped, so nothing was read.
- AC4 — a build lease of fleet tag `a` acquired under session `s9` read `mine` to `s9` in the `lease` mode;
  re-planted with `session: absent`, `keepalive: absent` and the same tag, the sourced
  `check_claim_writable tFix lease a <session> acquire` read `foreign-live` with the session unset,
  `absent` and `s9`. With the row's two session guards cut in process by `sed` over `declare -f`, its one
  site, the same read with the session unset was `mine`: the base row's literal comparison.
- AC5 — over that lease re-planted with `keepalive: k2`, the sourced `check_claim_writable tFix preflight k2
  absent k2` with the session unset returned 0 (PINNED), class `mine`, act `renew`; under keepalive `k3` it
  returned 1 (PINNED), class `foreign-live`. The full `--preflight tFresh` reading is the suite arm's, owed below.
- AC6 — `grep -n 'CLAUDE_CODE_SESSION_ID' tools/unattended/STOPS.template.md` prints the section 7 lines
  naming it as the session source and stating that unset, empty and `absent` are no session; `cmp` of the
  template and `memory/guides/UNATTENDED-STOPS.md` reads identical.

**Owed at the close.** The `New arm:` line of section 7: the `TOOL-dPlacedRequest-32` block of region 8 of
`tools/unattended/unattended.test.sh`, right after the `TOOL-dPlacedRequest-19` block, 11 assertions
(DERIVED: 10 `same` and 1 `hit`). The extracted probe above ran its lease-fixture half, 8 (DERIVED)
assertions, green on this driver; that probe is no suite reading. The claim-fixture half, AC5's two
`--preflight tFresh` passes under keepalives `k2` and `k3`, 3 (DERIVED) assertions, ran in no probe and is the
close's to read. Its RED-first observation is the close's, staged against the `lease` mode's `mine` row with
its two session guards cut, which reads AC4's plant `mine`, and against the base driver's `.typed` append and
predicate, which consent on the planted line. The existing `DPR20 AC9` assertion moved with the behaviour:
an acquire of an offered lease under `absent` or no session now exits 2 `no session` rather than 1
`offered`. The suite is waived for this build's landing by README rule 8. The floors rose by the same 11
(DERIVED): `FLOOR_ASSERTIONS` and `FLOOR_SHARD_8`.
