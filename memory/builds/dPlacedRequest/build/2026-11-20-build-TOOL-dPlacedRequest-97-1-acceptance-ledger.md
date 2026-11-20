# TOOL-dPlacedRequest-97 — acceptance ledger

**Serves:** journal TOOL-dPlacedRequest-97

The unit was built from its spec at rev-2 on base `a0fe07954`. Built: S1, a second `mine` row in the
`lease` mode of `tools/unattended/unattended.sh#check_claim_writable`, below the session row and above
the `same` row, matching where a run-state file is handed, either session is `absent`, the record's
fleet tag is this node's, and its `keepalive` is present, not `absent`, and equal to that file's
`keepalive` fact; `tools/unattended/unattended.sh#write_fence_beat` hands the slug's run-state file,
read by `tools/unattended/unattended.sh#runmd_of`, as the sixth argument; the column's header comment
names the fence as the one `lease` caller handing a keepalive. The arm is the TOOL-dPlacedRequest-97
block of `tools/unattended/unattended.test.sh`, a region-eight seam of its own after the fence read's
block, over that block's lease fixture and its helpers `seed_lease_at`, `run_offer_arm` and
`run_lease_arm`; `FLOOR_ASSERTIONS` and `FLOOR_SHARD_8` are raised by its assertion count. No gate,
suite or bar ran in this pass.

THE AC1 PROBE, the reading the lines below cite as "the probe": a scratch script under the run's
scratch directory builds a bare origin and one clone under a short temp path, the clone's conf from the
suite's own `mkconf` with `RUN_CLAIMS="on"`, plants on the origin a `tKa/build` lease of fleet tag `a`
(the fleet registry's tag for `daily-agent`), `session: absent`, `keepalive: K`, status `live`, and
writes the clone's `memory/builds/tKa/RUN.md` with `keepalive: K` under `## Run facts`; then it runs,
as `daily-agent`, `env -u CLAUDE_CODE_SESSION_ID bash <driver> --lease fence build tKa`, then
`CLAUDE_CODE_SESSION_ID=s2 ... --lease acquire build tKa`, then rewrites the fact to `keepalive: K2`
and fences again, then removes the run-state file and fences a last time.

**Evidences:** TOOL-dPlacedRequest-97
- AC1 — `fence — refs/gov/leases/tKa/build` — the probe over the driver at this pass: the id-less fence exited 0 printing one line `fence — refs/gov/leases/tKa/build <the planted tip> <a beat sha>`, the tip the one the probe planted. (DERIVED)
- AC1 — `keepalive: K2` — the probe then rewrote the run-state fact to `keepalive: K2` and the same fence exited 1 printing `lease refused — live-holder · tKa/build · node a · session absent · … · status live · verdict live`. (DERIVED)
- AC1 — `lease refused — live-holder` — between the two fences, the acquire under `CLAUDE_CODE_SESSION_ID=s2`, the run-state file still holding `keepalive: K`, exited 1 printing `lease refused — live-holder · tKa/build · node a · session absent · …`, the origin's tip unmoved: the `--lease` verbs hand no run-state file and gain no identity. (DERIVED)
- AC1 — `95c3103ad` — the RED reading: the same probe through a scratch clone of this repository checked out at that commit, its driver blob `0e8038fd5`, printed the first id-less fence exit 1 `lease refused — live-holder · tKa/build · node a · session absent · … · verdict live`, the acquire and the `K2` fence exit 1 with the same line. (DERIVED)

## Readings beside the criteria

- The probe's last fence, with the run-state file removed, exited 1 printing `lease refused — live-holder`: `fact` on a missing file answers nothing and the new row cannot match. (DERIVED)
- A first RED attempt ran the commit's `tools/` from a `git archive` with no repository around it; the driver could not resolve its fleet tag there and exited 2 `lease not written`, a fixture failure and no reading, so the RED above was re-taken from a clone. (DERIVED)
- The block's assertions counted off its lines: five `same` and one `hit`, six in all, each moving the executed count by one, no loop over an assertion and no skip branch. (DERIVED)
- The floors as written: `FLOOR_ASSERTIONS` from 4056 to 4062. (DERIVED)
- `FLOOR_SHARD_8` from 1275 to 1281. (DERIVED)
- `bash -n` over both edited files exited 0. (DERIVED)
- The arm `DPR32 AC4`, which calls the column in the `lease` mode with no sixth argument over a lease of session and keepalive `absent`, still reads `foreign-live`: the new row needs a run-state file and a keepalive other than `absent`. (DERIVED)
- The unattended kit's version carrier was not moved by hand: the kit-epoch rule has the lander mint it at the push boundary, as this build's earlier driver moves did. (DERIVED)

## Items diverged

None.

## Owed at the close

- `New arm:` `tools/unattended/unattended.test.sh`, the TOOL-dPlacedRequest-97 block, six rows, the floors raised; its RED-first observation against the lease column at `95c3103ad` and its GREEN reading inside the suite are the close's, its clean reading owed with PLAY-dClosedLoop-14 under README rule 8. (DERIVED)
- The legs the spec's Gates section names, run once by the main loop.
