# TOOL-dDeclaredLoop-65 — acceptance ledger

**Serves:** journal TOOL-dDeclaredLoop-65

No merge bar and no self-test suite ran in this pass. The criteria were observed on node `d` (win32), at
rev-3 of the spec, over the working tree: each of the three new plants and `stale-remote` run alone by
`--fixture`, with `steps` and `no-remote` run the same way over the changed reading, standing in for the
`loop position fixtures` leg; and the `grep` probes over `help/loop.md`, standing in for the `docs` leg.
The section 5 sweep re-run at the base of this pass held its design claims: `read_remote_claim` has one
caller, `stale-remote` is spelled in `tools/loop/position.py` and `help/loop.md` alone, no reader parses
the tracking ref's `read` entry, the `--plant` usage anchor's fingerprint did not move, the lexicon
offender pin stays 1215 PINNED with `read_fetch_time` graded OK, no shell file is edited, and neither
edited path is on the kickoff watch list; its stale figures, the clone plants' branch and the re-priced
row are deviation 652.

Owed to the close: every leg section 7 names, and the `loop position fixtures` leg whole. Owed RED-first:
the `tools/loop/position.py` arm, `fresh-clone`, `quiet-remote`, `offline-stale` and `stale-remote`,
against the reflog-only reading `TOOL-dDeclaredLoop-56` S36 keeps. A probe in this pass, a reflog-only
reader bound in place of `read_fetch_time` in process, printed `MISSED` for all three new plants; the
`stale-remote` plant's red is the tip's entry naming no source, which that probe does not reach.

**Evidences:** TOOL-dDeclaredLoop-65
- AC1 — `--plant fresh-clone` — it printed `position: fixture · fresh-clone · held`, the answer `act`, and the ref's `read —` line ending `from clone`, its age 0 PINNED seconds, exit 0; with the reflog-only reader it printed `MISSED`.
- AC2 — `--plant quiet-remote` — it printed `position: fixture · quiet-remote · held`, the answer `act`, and the ref's line ending `from FETCH_HEAD`, exit 0; with the reflog-only reader it printed `MISSED`.
- AC3 — `--plant offline-stale` — it printed `position: fixture · offline-stale · held`, the answer `stale-remote`, and the ref's line ending `from FETCH_HEAD`, its age 10800 PINNED seconds, twice the bound, exit 0; with the reflog-only reader it printed `MISSED`.
- AC4 — `grep -c "from clone" loop.md` — it printed 2 PINNED in `help/`, and `grep -c "finds nothing new leaves it stale" loop.md` printed 0 PINNED.
- AC5 — `--plant stale-remote` — it printed `position: fixture · stale-remote · held` and the ref's line ending `from reflog`, exit 0.
