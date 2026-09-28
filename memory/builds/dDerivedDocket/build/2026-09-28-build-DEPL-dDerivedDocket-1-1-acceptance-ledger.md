**Serves:** journal DEPL-dDerivedDocket-1

# DEPL-dDerivedDocket-1 — acceptance ledger

One commit carries the unit: the runbook's §2, §3 and new §3a-asks edits, the scaffold's shard
header, the spec at rev-10 with its CLOSED header, this ledger, and the regenerated build index. The
spec moved to rev-10 before the runbook was written, for the two reasons its section 9 line gives:
the carried-prefix list is a ban this pass may not raise, so the section spells its commands through
the `<kit>` token instead of raising the row, and the planner takes each signed record as
`--signed <kind>=<path>`, which rev-9's proposed spelling did not.

NO MERGE BAR, NO GATE LEG AND NO SUITE FILE RAN IN THIS PASS. The direct checks were the memory-tree
kit's own programs, run inside scratch fixture repositories built under this run's scratch root, and
plain `grep`, `awk` and `git check-attr` reads. Each fixture was a fresh `git init` holding a copy of
the tracked `tools/memory-tree`, `tools/memory-recall` and `tools/lib` files at this pass and a
`.memory-tree.conf` copied from the kit's example, committed before anything ran.

## What this ledger does NOT evidence, and why

AC7 carries a `permission:` line and gets no line here; the orchestrator writes it after the
post-build bar, whose `install-prefix (shipped surface)` leg makes the observation. The in-pass half
that line gives the pass was read and is recorded here as prose, not as an answer: the leg's own
carried-literal predicate, the regex and the loose-file existence filter of `scan_carried_hits`,
counted 53 literals in `WIRE-INTO-PROJECT.md` at the parent, `66f99c96`, which reproduces the row's
recorded 53, and 53 at this commit with the same multiset of literals. No added line of the runbook
carries a `tools/` literal, the root-install predicate of arm 1 hits no added line in either touched
file, and the row in `tools/install-prefix-carried.txt` is unedited.

Two fixture notes, neither a finding against this unit. The fixture's switch build needed a build
README with a declared `status:` before the index generator would render, which an adopter's own
deployer build already has. And the scaffold rewrote the kit's `build-readme-slot-limits.txt` without
staging it, which is the scaffolder's existing behaviour for that file and untouched here.

**Evidences:** DEPL-dDerivedDocket-1
- AC1 — `git check-attr merge` — in an empty scratch repository holding the three attribute lines §3 step 4 now carries, `memory/backlog/TOOL.md`, `memory/builds/aSwitch/BACKLOG.md` and `memory/DECISIONS.md` each printed `merge: rows`. RED staged in the same repository with the builds line replacing the backlog line: `memory/backlog/TOOL.md` printed `merge: unspecified` while the builds path still printed `rows`.
- AC2 — `### 3a-asks` — the awk pass that sets a flag at `<!-- govkit:entry memory-tree -->`, clears it at `<!-- govkit:entry drift-audit -->` and prints it at each `### 3a-asks` heading printed `1` exactly once; the heading sits at line 249 and the drift-audit anchor at line 324.
- AC3 — `gen_build_index.py --check` — a derived pass over the section graded all 23 flag uses in its 10 `python <kit>/` commands and its 8 standalone flags against the usage text of `migrate_backlog.py`, `gen_build_index.py`, the `--check` branch of `main()` in `merge-rows.py` and `check-wiring.sh`, with 0 misses, including `--record-as` beside `--record` and `--as`, `same-id=` and `triage=` on `--write`; its 6 repository paths, the three `.githooks/` references and the switch-over spec among them, are all in `git ls-files`; each of the 6 numbered steps names a command, and step 4 names `memory-recall` before its first command. In the scaffolded fixture with `<kit>` read as `tools/memory-tree`, one legacy row appended to the scaffolded `DEPL` shard and one rotated archive `memory/archive/DEPL.2026-08-01.md` committed beside it: step 1 as spelled wrote the census and the same-id, triage and status worksheets under `memory/builds/aSwitch/build`; with two hand-signed records carrying the header cells the kit README's signed-records row states, step 3's preview exited 0 and step 4's `--write` exited 0, migrated both rows into `memory/builds/aFoo/BACKLOG.md` and printed `ASK_CUTOFF=2026-09-29`; with the archive deleted, `BACKLOG_MODE="builds"`, the cutoff and the three attribute lines set and `--write` rendered, `gen_build_index.py --check` exited 0 and `python tools/memory-tree/merge-rows.py --check` exited 0 printing `merge-rows: check · 5 governed path(s) resolve merge=rows · mode builds · view refusal armed`. RED staged three ways: the archive restored made `--check` exit 1 on V19; rev-9's spelling `--signed <path> <path>` refused with "--signed takes <kind>=<path>"; and with `tools/memory-recall` removed, the hygiene engine's check 26 printed that it cannot run because the `memory-recall` kit is not installed.
- AC4 — `grep -n 'BACKLOG_MODE' WIRE-INTO-PROJECT.md` — printed lines 251 and 291, both inside §3a-asks (249 to 323); line 251 states that the key absent or blank runs the tree in `shards` mode, and §3 step 2 carries the pointer to §3a-asks at line 204.
- AC5 — `grep -n 'kit:unattended' WIRE-INTO-PROJECT.md` — printed line 127, §2's unattended bullet, which names the ONE substitute, the pointer to the protocol's landing rule and the protocol contract and states no count of blocks; `grep -n 'kit:kickoff-manifest' WIRE-INTO-PROJECT.md` printed line 125, one bullet in §2's kit list saying that keeping the kit keeps §1's merge exception. RED at the parent: the second grep printed nothing.
- AC6 — `grep -c '^- '` — `bash tools/memory-tree/adopt-memory-tree.sh --scaffold` in the fixture exited 0 and wrote three shards, `ARCH`, `DEPL` and `DES`, each quoting `- <ID> · <STATUS> · <text>` with the id before the status token on its `>` line, and the count printed 0 for every shard; `bash tools/memory-tree/check-memory-hygiene.sh` over the scaffolded tree exited 0 and reported 0 graded rows across 3 shards. RED staged in a second fixture whose scaffold copy wrote the example row on its own line: the count printed 1 for each of the three shards.
