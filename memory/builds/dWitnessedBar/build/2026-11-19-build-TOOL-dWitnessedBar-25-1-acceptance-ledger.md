# TOOL-dWitnessedBar-25 — acceptance ledger

**Serves:** journal TOOL-dWitnessedBar-25

This pass ran no merge bar, no gate leg and no suite. Every criterion below was checked on node d on
2026-11-20 by probing the unit's own code over scratch fixtures under `%TEMP%`: the runner over a
scratch clone and a two-leg fixture manifest, driven from a probe script before the role's
scratch-guard refused a direct runner call (see AC2), `keep_tails.py` run as its CLI over scratch
repositories its own fixture writer planted, `gen_build_index.py --print-bindings` over one of them,
the driver's `write_leg_tails` sourced alone with its resolvers stubbed, and `policy.py lists --write`
and `render_playbook.py --reference`. The close owes every leg of section 7 and the RED-first
observation of both `New arm:` lines: the evidence suite's AC1-AC5 arms and `keep_tails.py --selftest`.

**Evidences:** TOOL-dWitnessedBar-25
- AC1 — `run_id` — a red run over the fixture manifest wrote `run_id 20261120T035511Z-1632` into the run
  record's `verdict`, the id its `header` names. Owed: the evidence arm's RED-first observation.
- AC2 — `cause push:<sha>` — the same run, started with `GATE_CAUSE=push:<HEAD sha>`, wrote
  `cause push:039e0992…` into the verdict and the per-tree verdict; unset, both read `cause attended`;
  with a tab in the value the verdict read `attended` and stderr printed `run-gates: GATE_CAUSE refused —
  $'push:a\tb' is outside [A-Za-z0-9._:@-]+`. Not observed here: the fixture leg's own environment
  showing no `GATE_CAUSE` (the probe read the wrong output index, and the re-run was refused by the
  scratch-guard as a runner call), owed to the evidence arm at the close.
- AC3 — `tail.1` — the leg printing 100 numbered lines and exiting 1 left `tail.1 ad79964f… red` in both
  verdicts, and `<common-dir>/gate-tails/ad79964f…` held 60 lines from `line 42`, its name equal to (DERIVED from the builder's probe)
  `git hash-object --stdin` of its bytes.
- AC4 — `***:***@` — the same tail held the URL masked `***:***@` and no `secret`.
- AC5 — `GATE_RUN_KEEP` — six further red runs with a tail each left five run directories and exactly
  the five tails their verdicts name; the first run's tail was removed with its run.
- AC6 — `**Hash:**` — `keep_tails.py --run fx-1 --build x --unit TOOL-x-1` under `tail-by-hash` over a run
  holding one tail wrote `memory/builds/x/build/2026-11-20-build-TOOL-x-1-leg-tail-1.md`, `- **Hash:**`
  the tail's hash and the tail in one fenced block; with that record staged, a second run printed
  `keep-tails: skipped 65ac10aa… — … holds it` and wrote nothing.
- AC7 — `trace.leg-output is node-local` — the same verb under `node-local` wrote no record, printed
  `keep-tails: trace.leg-output is node-local, so no tail is committed (policy.py get)`, exit 0.
- AC8 — `tail-by-hash` — `policy.py get trace.leg-output` on this tree printed `tail-by-hash`, the
  catalogue default; `grep -cx 'trace.leg-output' tools/policy/unsummarised-keys.txt` printed 0 after
  `lists --write` drained it, and `grep -c '^## .trace\.leg-output.$' help/reference/policy.md` printed 1
  after the reference render. The mirror `.governance/policy.json` renders a committed catalogue only.
- AC9 — `leg-tail` — a tail holding an access-key-shaped value the default table matches was written
  into its `leg-tail` record as `AKIA<redacted:aws-key>`, without the value.
- AC10 — `leg-tail` — with that record and a `.memory-tree.conf` declaring the `TOOL` family committed,
  `gen_build_index.py --print-bindings` printed `S … 2026-11-20-build-TOOL-x-1-leg-tail-1.md leg-tail
  TOOL-x-1` and no `A` row; before the conf declared the family it printed an `A` row naming the file.
