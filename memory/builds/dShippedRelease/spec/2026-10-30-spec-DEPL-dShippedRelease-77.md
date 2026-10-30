# DEPL-dShippedRelease-77 — the engine answers an empty environment, a named service and a failed restart

**Status:** OPEN · rev-1 · 2026-10-30 · node d · Tier-2 · base f4597719 · streams deployer · order 14 · advances DEPL-dShippedRelease-32

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-30-build-DEPL-dShippedRelease-1-agent-ledger.md](../build/2026-10-30-build-DEPL-dShippedRelease-1-agent-ledger.md) | journal | DEPL-dShippedRelease-1 DEPL-dShippedRelease-2 DEPL-dShippedRelease-3 DEPL-dShippedRelease-4 DEPL-dShippedRelease-5 DEPL-dShippedRelease-6 DEPL-dShippedRelease-7 DEPL-dShippedRelease-8 DEPL-dShippedRelease-9 DEPL-dShippedRelease-10 DEPL-dShippedRelease-11 DEPL-dShippedRelease-12 DEPL-dShippedRelease-13 DEPL-dShippedRelease-14 DEPL-dShippedRelease-15 DEPL-dShippedRelease-16 DEPL-dShippedRelease-17 DEPL-dShippedRelease-18 DEPL-dShippedRelease-19 DEPL-dShippedRelease-20 DEPL-dShippedRelease-21 DEPL-dShippedRelease-22 DEPL-dShippedRelease-23 DEPL-dShippedRelease-24 DEPL-dShippedRelease-25 DEPL-dShippedRelease-26 DEPL-dShippedRelease-27 DEPL-dShippedRelease-28 DEPL-dShippedRelease-29 DEPL-dShippedRelease-30 DEPL-dShippedRelease-31 DEPL-dShippedRelease-49 DEPL-dShippedRelease-50 DEPL-dShippedRelease-51 DEPL-dShippedRelease-52 DEPL-dShippedRelease-53 DEPL-dShippedRelease-54 DEPL-dShippedRelease-55 DEPL-dShippedRelease-56 DEPL-dShippedRelease-57 DEPL-dShippedRelease-58 DEPL-dShippedRelease-59 DEPL-dShippedRelease-60 DEPL-dShippedRelease-61 DEPL-dShippedRelease-62 DEPL-dShippedRelease-63 DEPL-dShippedRelease-64 DEPL-dShippedRelease-65 DEPL-dShippedRelease-66 DEPL-dShippedRelease-67 DEPL-dShippedRelease-68 DEPL-dShippedRelease-69 DEPL-dShippedRelease-70 DEPL-dShippedRelease-71 DEPL-dShippedRelease-72 DEPL-dShippedRelease-73 DEPL-dShippedRelease-74 DEPL-dShippedRelease-75 DEPL-dShippedRelease-76 DEPL-dShippedRelease-78 |

<!-- /gen:spec-records -->

## 1. Goal

Close finding id 94 of `reviews/2026-10-30-review-DEPL-dShippedRelease-1-spec-audit-round1.md`,
HIGH, item H21. Unit 6 S1 requires `read-current` to print a running digest and unit 15 S6 needs
that id for `--expect`; neither defines an E with no container, or a systemd unit with no
`GOV_IMAGE` yet. S3's `docker inspect of the project's containers` names no service, and §4's exit
table has no row for a restart that fails after the override is written. The first promote into any
new environment has no id, so no adopter can start, and a failed unit cannot be rolled back when it
most needs it.

## 2. Scope (IN)

- **S1** — `none`. `read-current <E>` prints `none`, exit 0, for an E with no container or no
  `GOV_IMAGE`. `--expect none` compares equal only to an empty live digest, inside the lock.
  Observed by AC1.
- **S2** — The service. An eighth value, `release.env.<environment>.service`, a catalogue row with
  the seven of unit 6 S5: the compose service whose image is the deployment id. Empty is legal with
  one service; empty with two or more exits 2 naming the key. Observed by AC2.
- **S3** — A failed restart. A swap whose override is written and whose restart fails exits 2
  printing `swap written · restart failed`, and leaves the override. `read-current` then prints the
  configured digest, so `rollback --expect <that digest>` compares and proceeds. Observed by AC3.
- **S4** — `already there` requires `ActiveState=active`: a failed unit whose configured digest
  equals the target re-runs the swap. Observed by AC3.

## 3. Non-goals (OUT)

- The pick and its floor: DEPL-dShippedRelease-55.
- An engine exit outside the table: review id 95, in the minors batch.

### Edges

- **consumes-from** `DEPL-dShippedRelease-6` — the verbs, the host script and the seven rows
- **consumes-from** `DEPL-dShippedRelease-15` — `run_engine_verb` and the pick's stored id, through which `none` reaches `--expect`

## 4. Design

### Evidence

- Unit 6 §4 "The verbs and their exits" lists exits 0, 3, 2 and 4, and no row after the override is written.
- Unit 6 S3 reads systemd's digest "with `ActiveState=active`", so a failed unit prints none.
- A `<word>` segment matches one segment (`tools/policy/README.md:50-53`, cited by unit 6), so `service` is one more row of the same pattern.

### Files touched (estimate)

- `tools/integrations/engines/compose_systemd.py`: S1, S2, S3, S4
- `tools/integrations/engines/compose-systemd-host.sh`: S1, S3, S4
- `tools/policy/catalogue.toml`: the eighth row
- `tools/policy/unsummarised-keys.txt`: drained by `policy.py lists --write`
- `help/release.md`: the first deploy and `service`

## 5. Production-readiness checklist

- security — `service` reaches the host as a quoted positional argument, its row's pattern admitting
  no shell metacharacter, as unit 6 §4 states of the seven.
- perf / scale — N/A — a read or a compare on a path that already runs once per landing.
- error / empty / loading states — the three cases of §6 are this unit's whole purpose.
- observability — each state prints the line §2 names, on green and red.
- risks — the stated repair is the unit's only change; a wrong reading reds at its own fixture.
- testing — the criteria of §6 and the arm of §7.
- migration — N/A — the code it changes lands in this same build, so no installed state moves.
- user docs — `help/release.md` states the first deployment and the `service` value.

## 6. Acceptance criteria

- **AC1** — When `python compose_systemd.py --fixture --case first-deploy` runs with no container,
  `read-current` prints `none`, and `promote <E> <sha> --expect none` swaps and exits 0.
  Red when: no adopter can make a first deployment.
- **AC2** — When `--case two-services` runs with `service` empty it exits 2 naming the key, and with
  it set the digest read is that service's.
  Red when: a multi-service compare reads an arbitrary container.
- **AC3** — When `--case restart-fails` plants a restart that exits 1, `promote` exits 2 printing
  `restart failed`, `read-current` prints the configured digest, and
  `rollback <E> <sha> --expect <that digest>` exits 0.
  Red when: a failed unit has no id, so E cannot be rolled back.

## 7. Gates

`policy fixtures` · `spec tokens (a spec's own names resolve)` · `memory hygiene`

New arm: tools/integrations/engines/compose_systemd.py · covers AC1 AC2 AC3 · the three cases, their failing case `read-current` on an empty E exiting non-zero · none

## 8. Open questions

none

## 9. Revision log

- rev-1 · 2026-10-30 · initial draft, promoted from review id 94 (HIGH, item H21) of the round-1 spec audit.

## 10. Reuse audit

The seam extended is unit 6's `run_host_script`, one code path for `promote` and `rollback`.
`python tools/codebase-map/reuse_lookup.py "pick the newest verified release for an environment without going below the running one"`
ranked no engine helper, since the adapter is specced and unbuilt, so no existing seam fits outside
it. The recall probe surfaced scout C's row and report item H21, which agree with this reading.

Recall terms used:
`python tools/memory-recall/query.py "how does promotion avoid a downgrade and what does an environment with no deployment read" --terms "release pick superseded environment rollback expect compare-and-swap first deploy engine verify"`
