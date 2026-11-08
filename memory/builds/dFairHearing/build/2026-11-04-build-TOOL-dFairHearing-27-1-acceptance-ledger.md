# Acceptance ledger — TOOL-dFairHearing-27

**Serves:** journal TOOL-dFairHearing-27

Built against spec rev-4 in pass commit `e3bd1ad45`, whose parent is `b6115ab64`. The first dispatch wrote nothing, because the write set paired `memory/gotchas/INDEX.md` with its generator. The main loop drafted this ledger at the close from the second builder return, whose heading says each criterion in its checks list was observed failing before the change where that applied and passing after. Where a line gives no figure, the return records none. No suite, gate or bar ran in the pass: the spec's gate legs and the first-failure observations of its five `New arm:` lines are owed to the close. A line that says "not recorded" names a half of its criterion no record on disk shows.

The close observed this unit's `New arm:` lines on 2026-11-08 at `4896589bc`: each row, RED or UNSEEN with its log line, is in `2026-11-08-build-TOOL-dFairHearing-1-arm-observations.md`, and every suite holding them exits 0 at that tip.

**Evidences:** TOOL-dFairHearing-27
- AC1 — `python render_lenses.py --markers "$SCRATCH/h.js"` — the gate ran over scratch files and held the zero-row opt-in literal outside the count
- AC2 — `grep -c "never .git clone --branch" tools/workflows/README.md` — the return records this grep and its absence pair among the greps that passed
- AC3 — `grep -c FOREIGN_PREFIX_PROBE spec-audit-optin.test.sh` — the return records this grep and the foreign-prefix row's grep among the greps that passed. The leg itself is owed to the close
- AC4 — `extract_tag_ref('x.md:AC3')` — a direct probe of the scorer's functions passed. The first builder return records `x.md:AC3` giving 6, `x.md:S5 scope` giving 2 and `x.md:prose` giving None, each equal to `extract_section_ref`
- AC5 — `python replay_scorer.py --experiment` — the real held-out file read with backslashed and absolute paths printed `frozen at b6c828a92`, and a scratch copy whose `rev-parse` fails exited 2 naming the call
- AC6 — `check_ungated` — a probe over 9 bodies passed. Not recorded: the selftest arm "a leg-name guard under a blank LEG_MANIFEST is announced and exits 0", since no suite ran
- AC7 — `%TEMP%/fhk` — apply plus update into the scratch target printed `scope: review-harness moves with agent-cap`. The spec's two-kit apply is refused by govkit's dependency check, so the target was installed with kickoff-manifest, settings-merge, policy, memory-tree and drift-audit as well. That fixture is superseded, see below
- AC8 — `grep -n "pack AC1" tools/hooks/agent-cap.test.sh` — a hook probe over a scratch layout passed, and the `pack AC1` arm now expects `apply`
- AC9 — `check-verifier-fanout.js` — the return records both counts among the greps that passed
- AC10 — `git merge-base HEAD main` — the return records this grep among the greps that passed. The criterion is superseded, see below
- AC11 — `lens-array bound` — the pair's two `sed` extractions both read 5. Not recorded: the `git grep -n MAX_LENSES` output
- AC12 — `spec-audit opt-in pack self-test` — the return records this grep among the greps that passed, and a probe found `tools/govkit/subject-pins.tsv` equal to what `selfcheck --write` renders
- AC13 — `gateManifest` — the return records both greps among the greps that passed
- AC14 — `python replay_scorer.py --selftest` — at the tip `948e4141b` it exits 0. A scratch copy with `ARMS_DECLARED` at 28 exited 1 printing `29 arm(s) ran against 28 declared`
- AC15 — `$SCRATCH/p/.governance/install.json` — a hook probe over a scratch layout passed. The third case is superseded, see below
- AC16 — `tools/gate-legs.json` — the guard half passed. Not recorded: the stamp half over `memory/guides/SESSION-KICKOFF.md`, which the return owes to a read of this commit's diff
- AC17 — `git show-ref refs/replay/fhr` — the recipe ran four times. A run at `HEAD` while the `3708a705` clone stood exited 2, a fresh run's clone `HEAD` equalled the repository's, a forced bundle failure exited 128, and `git show-ref refs/replay/fhr` printed nothing after every run
- AC18 — `the marker predicate did not run` — gate copies in fixture repositories, one with stubbed python launchers, passed
- AC19 — `walk` — a prelude probe refused run 2's slot-3 slice of 210 cells, and run 1 proceeded
- AC20 — `the walk table has [0-9]+ gap` — the `tier2-review.test.sh` baseline at the tip `948e4141b` read both `FH27 AC20` arms ok: the complete walk's synthesis prompt carries no such line, and the gapped walk's carries one
- AC21 — `grep -n "roundState" tools/workflows/tier2-review.js` — the return and the commit message record S26, which this criterion observes, as already holding on the tree. Not recorded: the sentence the grep printed
- AC22 — `TOOL-dFairHearing-2 AC4` — the return records this probe among the awk reads that passed
- AC23 — `git grep -n "Windows path limit" -- tools` — the return records this grep among the greps that passed. The criterion is superseded, see below
- AC24 — `git grep -n "Hand a reviewer the classes" <unit> -- tools/memory-tree/gotchas.py` — the generator half passed at this commit. The records commit is `03ed40f98`, whose parent is `e3bd1ad45` and which carries `memory/gotchas/INDEX.md`. Not recorded: the index-side grep there, and the `gotchas.py --write` re-render
- AC25 — `scan_pairing_sites` — a direct probe of the scorer's functions passed
- AC26 — `LENS_SLOTS` — a node probe over the blanked view passed

## Supersessions

Each one is named by the hands-off bullets in this unit's spec, and by the later unit's own scope item.

- `TOOL-dFairHearing-27` S15 and AC10 — S15's base sentence and AC10 are answered by `TOOL-dFairHearing-31` S1 to S3 and AC1 to AC3. S15's version rule stands
- `TOOL-dFairHearing-27` S20 and AC15 — the deny on a missing-path row and AC15's third case are superseded by `TOOL-dFairHearing-32` S25
- `TOOL-dFairHearing-27` AC7 — the two-kit fixture is superseded by `TOOL-dFairHearing-32` S30
- `TOOL-dFairHearing-27` AC9 and AC11 — the whole-text `.js` halves are superseded by `TOOL-dFairHearing-32` S22
- `TOOL-dFairHearing-27` AC23 — superseded by `TOOL-dFairHearing-32` S23's criterion
- `TOOL-dFairHearing-27` S7 — the empty-output case as the only one handled is superseded by `TOOL-dFairHearing-32` S31
- `TOOL-dFairHearing-27` S11 — the sentence-end rule is superseded by `TOOL-dFairHearing-32` S32
