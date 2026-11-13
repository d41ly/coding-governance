**Serves:** journal TOOL-dNarrowedAnchor-1

# TOOL-dNarrowedAnchor-1 — the acceptance record, written at the close

Node `d`, 2026-11-13. The unit landed on `main` at `baa2857e4` on 2026-08-25, and its spec stayed
INPROGRESS for eleven weeks. This record is written at the close, so the evidence comes from two
places, and each line says which one:

- **At the landing.** The feature commit `473ce2b9a` and the merge `baa2857e4` record the arms
  watched red against the code they guard, in an isolated worktree at the branch tip.
- **At this close.** These checks were re-run on `main` at `2ba17e9d6`.

The kit self-test suites were not re-run at this close. The owner's standing instruction holds them
(`memory/guides/SESSION-KICKOFF.md`, dated corrections, 2026-08-23).

**Evidences:** TOOL-dNarrowedAnchor-1

- **AC1** — `tools/unattended/unattended.test.sh` — the `hit` arm at line 6165 asserts the `fail 50`
  refusal text for a `slug` README resolved through the second anchor. That text is at
  `tools/unattended/unattended.sh@ecf49fdf:4275` on `main`. The arm was watched red at the landing, as
  `473ce2b9a` records.
- **AC2** — `tools/unattended/unattended.test.sh` — arm 50c, the `miss` at line 6183, passes a `recipe`
  README through the second anchor without the refusal. The `prompt` direction is armed on the leg side,
  by the `miss` at `tools/unattended/check-unattended.test.sh@42c65ff8:3494`. At this close I found no
  driver-side `prompt` arm for `fail 50`, so the driver half of AC2's `prompt` case rests on the landing
  record alone. `baa2857e4` records that the `miss` arms stayed green while `fail 50` was deleted.
- **AC3** — `tools/unattended/unattended.test.sh` — arm 50d, the `miss` at line 6191, resolves a `slug`
  README at the first anchor with `published` declared, and asserts `preflight OK`. It was observed at
  the landing and not re-run here.
- **AC4** — `tools/unattended/check-unattended.test.sh` — the `hit` arm at line 3483 asserts the
  `fail 29` text, which is at `tools/unattended/check-unattended.sh@a12efbde:2847` on `main`. It was observed
  at the landing.
- **AC5** — `tools/unattended/check-unattended.test.sh` — the `miss` at line 3505 runs with no remote,
  so no default-branch tip is advertised, and `fail 29` stays silent. `473ce2b9a` records it armed. It
  was observed at the landing and not re-run here.
- **AC6** — `baa2857e4` — the merge message records the deletion test. Deleting `fail 50` took the
  driver suite from 3 failures to 6, and deleting `fail 29` added exactly 1. Both were restored
  afterwards.
- **AC7** — `python tools/memory-tree/check-arms.py --check` — re-run at this close on `2ba17e9d6`:
  rc 0, reporting 36 armed and 174 waived sites.
- **AC8** — `bash tools/unattended/adopt-unattended.sh --check` — re-run at this close: rc 0, "in sync".
  `bash tools/unattended/check-unattended.sh` was also re-run at this close: rc 0, with the
  `fail 29` check live against the real remote. `tools/unattended/run-unattended-gates.sh` runs the
  held self-test suites and was not re-run.
