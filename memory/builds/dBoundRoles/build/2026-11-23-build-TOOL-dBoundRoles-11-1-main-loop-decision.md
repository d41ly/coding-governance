**Serves:** journal TOOL-dBoundRoles-11

# TOOL-dBoundRoles-11 — the main loop's decision over the first builder's divergence

Run `wf_4e23c012-8e3` read rev-5 against `6b0a1a102` and wrote nothing. It handed back one path outside the
write set and four places where the spec cannot hold as written. Direct spawns of a spec writer are still refused
on this run, because the session's spawn guard predates TOOL-dBoundRoles-17's `item=`. So the main loop settles each
item by M3 as a delegated resolution, and the next builder builds the result under the one deviation record its brief
names. widens: none · relaxes: S2's registry check inside `plan_state` (item 2) and the exit code AC6 names (item 4).

1. **The refusal ceiling rises by one, under a decision the main loop landed.** The driver sits at its ceiling,
   347 of 347 (DERIVED: the builder's read-only `tools/memory-tree/check-arms.py#classify` probe at `6b0a1a102`).
   S6's FORKED case adds one site. Every answer of `run.on-owner-question` and the relay of the reader's own refusal
   go through one shared `fail 49`, so the census rises to 348 and no further. A pass commit cannot write
   `memory/DECISIONS.md`, so the main loop appended the `TOOL-dBoundRoles-11` row there in the records commit that
   carries this decision. The builder raises the driver's `REFUSAL_CEILINGS` token in `.memory-tree.conf` to
   `348:2026-11-23:TOOL-dBoundRoles-11`, a file already in the write set. Retiring a different site to pay for this one
   was not chosen: that is a retirement review, which belongs to dWitnessedBar's wrap-up.
2. **`plan_state` checks the shape of the `admitted-by` tag, not the registry.** The driver reads no playbook kit, and
   F6's four arguments hand it no registry. So `plan_state` grades the tag as `principle.` plus one segment, the reading
   check 12 itself uses when no registry is installed, and the contract rows test that shape. Check 12 keeps the
   registry check. The gap left is one direction only: a well-shaped tag the registry lacks reds check 12 and reads
   READY in `--plan`. It is named in the deviation record and caught at the close by the memory hygiene leg.
3. **AC4 runs over live specs.** `--plan` prints DONE for a terminal spec, and check 12 grades §8 only at a terminal
   one. So AC4's fixture writes the same §8 under `**Status:** INPROGRESS`, the way the contract table already writes
   each case twice, and reads FORKED for the failing records and READY for the passing ones.
4. **AC6 reads "refuses with check 49".** The driver's `fail 49` prints `UNATTENDED check 49 FAILED` and the process
   exits 1 (`tools/unattended/unattended.sh#fail`), so the arm observes the check number and the parked region, never an
   exit code of 49.
5. **The two open choices in S6.** When no roles kit resolves beside the driver, `--dispatch` takes the key's catalogue
   default, `best-effort-recorded` read as `resolve`, and prints one NOTE line naming the absent kit, the way
   `read_lease_policy` does: the reader being absent is no reason to admit a FORKED unit, and `resolve` still refuses
   it. The `park-build` row's item field names the build slug.

`FORK_RECORD_CUTOFF` is set to `2026-11-24` (the builder's plan): the newest tracked spec filename is dated
`2026-11-21`, so no spec of this build is graded, and the run's later dispatches are unaffected.
