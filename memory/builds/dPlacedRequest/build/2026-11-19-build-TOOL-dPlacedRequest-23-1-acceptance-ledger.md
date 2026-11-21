# TOOL-dPlacedRequest-23 — acceptance ledger

**Serves:** journal TOOL-dPlacedRequest-23

The unit was built from its spec at rev-3 on base `0d877e288`. The driver already held the split the
spec states: `tools/unattended/unattended.sh#read_claims` refuses a failed `strict` read with check
109 and returns before any policy read, and `leases.offline` is read only inside
`tools/unattended/unattended.sh#run_lease_verb`, so no driver line changed. The pass adds the stops
guide's sentence (S3) and the suite block the spec's §7 declares. Each criterion below was observed
by a probe: the driver's `--preflight tOff` run in a scratch clone with a bare origin under the node's
short temp path, `RUN_CLAIMS` on, `USERNAME=daily-agent`, the origin renamed away, and the new suite
block evaluated alone over the helpers it calls. The red copy is a scratch copy of the driver whose
preflight claim first reads the claims `quiet` and, on a failed read under `warn`, appends a line
through `add_gov_queue`; beside it no policy kit resolves, so it reads the catalogue default `warn`.
No gate, suite or bar ran in this pass; the arm the spec's §7 declares and its RED-first observation
are owed at the close.

**Evidences:** TOOL-dPlacedRequest-23
- AC1 — under the default `leases.offline`, `--preflight tOff` exited 1 printing `UNATTENDED check
  109 FAILED`, `<git-common-dir>/gov-queue.log` absent, and `for-each-ref refs/gov/` listed 0 refs in
  the clone and 0 on the origin (DERIVED). The red copy printed the same check 109 and left a queue of
  1 line (DERIVED).
- AC2 — with `leases.offline` planted `warn`, `refuse` and `follow-leases` in turn, committed and
  pushed, `policy.py get leases.offline` answered each value and `--preflight tOff` exited 1 printing
  check 109 under all 3, no queue and 0 refs each time (DERIVED); `--lease acquire build tOff` under
  `warn` exited 0 printing `queued` with 1 queue line (DERIVED).
- AC3 — an `awk` over `tools/unattended/unattended.sh` printing each function whose body spells both
  `read_claims strict` and `add_gov_queue` printed nothing; its population, the functions spelling
  `read_claims strict`, is 4 (DERIVED): `print_claims`, `verb_preflight`, `run_takeover` and
  `verb_close`. Over a scratch copy whose `verb_close` calls `add_gov_queue` after its strict read it
  printed `verb_close` (DERIVED).
- AC4 — `grep -n 'check 109' tools/unattended/STOPS.template.md` printed 1 line naming
  `leases.offline` (DERIVED), the key table's `leases.offline` row inside section 7 "The lease", which
  names `--preflight`, a take-over and `--close`; the base guide printed 0 such lines (DERIVED).
  `memory/guides/UNATTENDED-STOPS.md` is its byte copy, `cmp` silent.
- The suite block `TOOL-dPlacedRequest-23 — A STRICT CLAIM READ STAYS STRICT`, evaluated alone over
  `mkconf`, `readme`, `write_lease_fixture`, `run_lease_arm` and `write_lease_policy`, ran 10
  assertions, all green (DERIVED); against the red copy as the driver it ran the same 10 with 6
  failing (DERIVED): the staged-line count, the three planted preflights, which queued, the lease
  verb's queue line and the red copy's own count. The floors move by those 10: `FLOOR_ASSERTIONS`
  3552 to 3562 and `FLOOR_SHARD_8` 786 to 796 (DERIVED).
