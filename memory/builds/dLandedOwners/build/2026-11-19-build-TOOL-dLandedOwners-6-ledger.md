# TOOL-dLandedOwners-6 — acceptance ledger

**Serves:** journal TOOL-dLandedOwners-6

No merge bar, gate or self-test suite ran in this pass. Each criterion was observed by the spec's own
command, from the worktree root, with `PY` from `tools/lib/resolve-python.sh`. The pass's base is
`22788ec02`. Every red was observed either at the base, before the first edit, or as a staged break
made inside the probe's own process: `drift_signals.EVIDENCE_GLOBS` rebound on the imported module
before `drift_report` imported it, so no tracked file was edited to observe it. No fixture repository
was made and the real repository's refs were never written.

**Evidences:** TOOL-dLandedOwners-6
- AC1 — `"$PY" -B tools/run-gates/py_reads.py --guards "policy fixtures"` printed
  `py-reads: closure · policy fixtures · tools/memory-tree/commit_trailers.py`, no line holding
  `RED guard`, and exited 0. Red: at the base it printed the same closure line and
  `py-reads: RED guard · policy fixtures · tools/memory-tree/commit_trailers.py is imported and outside its guard`,
  and exited 1.
- AC2 — the spec's `--legs-for` count printed `1`. Red: at the base it printed `0`.
- AC3 — the spec's command printed `444 none` (PINNED, this pass). Red: at the base it printed
  `445 tools/policy/unscanned-readers.txt`; and with the new entry rebound in-process to
  `:(exclude)unscanned-readers.txt`, the spelling without its leading `*/`, it printed the same
  `445 tools/policy/unscanned-readers.txt`. The two figures are the spec's pins, reproduced at this pass.
- AC4 — `"$PY" -B tools/drift-audit/drift_report.py --offenders` printed nothing and exited 0. Red:
  with the new entry dropped from `EVIDENCE_GLOBS` in-process and `drift_report.main(['--offenders'])`
  called, it printed the one line `non_terminal_specs_cited_by_product_source` with id
  `PLAY-dClosedLoop-1`, status `INPROGRESS`, cited in `tools/policy/unscanned-readers.txt` alone, and
  returned 1.
- AC5 — `git diff fcbd7efe -- memory/guides/SESSION-KICKOFF.md | grep -c "^+last-audit: "` printed
  `1`. Red: `git diff fcbd7efe HEAD` at the base, before the stamp, printed `0`.

Before the edit, `git grep` over every spec found `tools/memory-tree/commit_trailers.py` in no
OPEN, SPECCED, INPROGRESS or BLOCKED spec other than this unit's own, which this commit closes. The
one other non-terminal spec naming it, `TOOL-dLinkedLibrary-22`, is DEFERRED.

Owed to the close (M8): the legs of the spec's section 7. The spec declares no new arm.
