# TOOL-aTrimmedWait-2 acceptance ledger

**Serves:** journal TOOL-aTrimmedWait-2

No merge bar and no self-test suite ran in this pass. Every observation below was made on node a,
one command at a time with nothing else running, from the worktree root over the pass's tree, the
spec at rev-4. The pass probe is the spec's fenced `u2.sh` block, copied verbatim into the run's
scratch directory; its fixture repository was `$TEMP/u2`. The verdict-unchanged fixture ran four
argvs over that same fixture after the probe: the full run, `--only 12`, `--offenders`, and
`--staged` with the untracked red spec and a tracked red spec staged. Run with the parent's script
and with this pass's, its eight stdout and stderr files compared byte-identical under `cmp`, each
argv exiting 1 at both: the same refusals, reds and greens. The self-test's new scope arms and its
raised `FLOOR_ASSERTIONS` were not run here; their fixture was built by a scratch probe that drove
this pass's script over the same tree and read every expected exit and line. The suite, its floor
and the new arm's RED-first observation are owed to the close.

**Evidences:** TOOL-aTrimmedWait-2
- AC1 — `bash "$SCRATCH/u2.sh"` — printed `full A 1 B 1 C 1 N 0`,
  `spec-a rc 1 A 1 B 0 C 0 N 0 same yes live 1`, `spec-c rc 1 A 0 B 0 C 1 N 0 same yes live 1` and
  `spec-k rc 0 A 0 B 0 C 0 N 0 same yes live 1`. At the parent the same probe printed
  `full A 1 B 1 C 1 N 0`, and every scoped line read `rc 2` and `live 0`, the `--only` parse refusing.
- AC2 — `bash "$SCRATCH/u2.sh"` — the same run printed `spec-n rc 1 A 0 B 0 C 0 N 1 same yes live 1`
  and `build rc 1 A 1 B 0 C 1 N 1 same yes live 1`.
- AC3 — `bash "$SCRATCH/u2.sh"` — the same run printed `no-only rc 2 said 1`, `other rc 2 said 1`,
  `extra rc 2 said 1`, `not-spec rc 2 said 1`, `absent rc 2 said 1`, `old rc 2 said 1` and
  `no-build rc 2 said 1`. At the parent `no-only` read `rc 1 said 0`, the flag ignored.
- AC4 — `time bash tools/memory-tree/check-memory-hygiene.sh --only 12 --spec memory/builds/aTrimmedWait/spec/2026-11-14-spec-TOOL-aTrimmedWait-2.md`
  — at the parent it refused with `--only takes one comma list and no other argument`, exit 2,
  `real` 0m0.098s, measured over the script blob `f064ddabb88e` the parent holds. <!-- PINNED 2026-11-14 -->
  At this pass it printed `HYGIENE --only 12 ran checks 12 25 over 1 spec(s) of memory/builds/aTrimmedWait/spec/2026-11-14-spec-TOOL-aTrimmedWait-2.md`,
  exit 0, `real` 0m6.204s, under the 60 s budget. <!-- PINNED 2026-11-14 -->
  `time bash tools/memory-tree/check-memory-hygiene.sh --only 12` ended on
  `HYGIENE --only 12 ran checks 12 25` at both, exit 0 at both, `real` 5m23.730s at the parent's
  script blob and 5m12.201s at this pass. <!-- PINNED 2026-11-14 -->
  Its output, timings aside, compared identical line for line between the two runs.
- AC5 — `python tools/roles/render_agents.py --check` — exited 0 after `--write`;
  `grep -c -- '--only 12 --spec <path>' .claude/agents/gov-spec-writer.md` printed 1;
  `grep -cE '[a-z-]+/check-memory-hygiene[.]sh' tools/roles/agents/gov-spec-writer.agent.md`
  printed 0; `grep -c -- '--only 12 --spec <path> | --build <slug>' tools/memory-tree/check-memory-hygiene.sh`
  printed 1.
- Fix (brief `2026-11-14-prompt-TOOL-aTrimmedWait-2-fix`) — the `--build` arm's loop reads `FILES`
  through `done < <(printf '%s\n' "$FILES")`, not `<<<`. `grep -c '<<<' tools/memory-tree/check-memory-hygiene.sh`
  printed 28 at the parent `6d4b20d9a` and 27 after, the loop site alone leaving. <!-- PINNED 2026-11-14 -->
  `bash "$SCRATCH/u2.sh"` printed its AC1 to AC3 lines byte-identical under `cmp` to its run over
  the script at `91e91ed35`, which the parent holds unchanged. The same command,
  `time bash tools/memory-tree/check-memory-hygiene.sh --only 12 --build aTrimmedWait`, timed one
  at a time on node a, ran `real` 0m6.878s before and 0m6.236s after, exit 0 at both, its output <!-- PINNED 2026-11-14 -->
  byte-identical under `cmp` and ending on `HYGIENE --only 12 ran checks 12 25 over 7 spec(s) of aTrimmedWait`. <!-- PINNED 2026-11-14 -->
