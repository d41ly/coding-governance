# TOOL-dTrueNorth-2 — acceptance ledger

**Serves:** journal TOOL-dTrueNorth-2

No merge bar, no self-test suite and no gate leg but the naming lexicon ran in this pass. Every
criterion was observed by a probe of the new join, each a scratch script under the run's scratchpad:
the parity probe section 4 Fixtures describes, which loads `tools/check-spec-tokens.py` and the
bootstrap instrument by path, builds the design with `read_design` over the tree's keys and hands
the instrument's own `fixture()` to `scan_carries` with `exit_mode=True`, the instrument's own
`join` run beside it over the same input; a probe calling `derive_carries_coverage` over this
worktree; a scratch clone of the branch under the user temp directory, short-named, with the
uncommitted checker copied in and its `main()` run there through a `python -c` loader; and an
independent Python construction of the fixture repository the new suite arm builds, the same plants
staged and restored, the checker run over it the same way. The probes stand in for the
`spec tokens (a spec's own names resolve)` leg over scratch trees; that leg over the real tree, the
`spec-tokens self-test` suite with its 36 new arms and their RED-first observation, and
`memory hygiene` are owed to the close.

**Evidences:** TOOL-dTrueNorth-2
- AC1 — `ghost` — the parity probe handed `scan_carries` the `ghost` plant and it returned one
  `ghost` finding naming `cl-dClosedLoop-9999`, as the instrument's `join` returned one over the
  same input; the clean set returned none.
- AC2 — `unbound` — the `unbound` plant returned one `unbound` finding naming
  `fixture/dTrueNorth/spec/unit-3.md`, over 3 specs measured.
- AC3 — `@deadbeef` — the `stale` plant returned one `stale` finding reading `pins
  cl-dClosedLoop-0001@deadbeef, and the clause's text in the view hashes 83b6b117`.
- AC4 — `ambiguous` — the `ambiguous` plant returned one `ambiguous` finding, `carried whole by 2
  spec(s)`, naming unit-1 and unit-2. The probe's edit pinning the third clause's `part 2/2`
  carrier to `@deadbeef` returned `ambiguous` reading `pinned to 2 hashes (d2811290, deadbeef)`,
  beside that carrier's `stale` finding.
- AC5 — `typo` — the `dropped` plant returned a `stopped` finding for `cl-dClosedLoop-0001`, beside
  the plant's own `ambiguous` and exit-only `uncarried`, three findings as the instrument's `join`
  returns three; the `typo` plant returned one `stopped` finding, `1 of the 2 revision(s) read
  carried`, the drop sitting in the earlier revision.
- AC6 — `token` — the `token` plant returned one `token` finding naming the name the plant strips
  from the prose of `cl-dClosedLoop-0001`'s carrier, its binding lines left whole, read from the
  carrier's text.
- AC7 — `unmeasured` — the `unmeasured` plant's measured set was `{}`. In the scratch clone with
  every dTrueNorth spec removed by `git rm`, `main()` exited 1 printing `spec-tokens: REFUSING — the
  carries join measured no chain spec at/after SPEC_CARRIES_CUTOFF 2026-10-21, so it read nothing
  and is never green`.
- AC8 — `crossbuild` — the `crossbuild` plant returned one `crossbuild` finding naming
  `cl-dClosedLoop-0007`, `a clause of dGroundRules, and no **Moved:** line names it to dTrueNorth`.
- AC9 — `moved-token` — the `moved` plant returned no finding over 4 specs in two builds; the
  `moved-token` plant returned one `token` finding for `cl-dClosedLoop-0007`, its token
  `.governance/policy.toml`, naming the carrier `fixture/dTrueNorth/spec/unit-2.md` in the receiving
  build's folder.
- AC10 — `exit_mode=False` — with `exit_mode=True` the `uncarried` plant returned an `uncarried`
  finding and the `node` plant a `node` finding naming `record-kind.deviation`; with
  `exit_mode=False` neither returned an exit arm, and neither did any other plant.
- AC11 — `WONTDO` — one edit of the clean set holding `part 1/3` and `part 3/3`, a carry of
  `cl-dClosedLoop-0999` with that id added to a copy of the design's `retired` set, a third spec
  whose `**Carries:**` line has no hash, and a fourth at `WONTDO` carrying the first clause whole
  returned exactly `malformed`, `parts` and `withdrawn`, no `unbound` and no `ambiguous`. The same
  fourth spec at `OPEN` returned `ambiguous` naming it, so the status is what set it apart.
- AC12 — `scan_carries` — the clean set, `fixture(builds, nodes, "dTrueNorth", None)`, returned no
  finding over 2 specs measured; for the clean set and each of the thirteen plants the finding
  count equalled the instrument's `join` over the same input.
- AC13 — `carries.py --report dTrueNorth` — at 102352eaa with this pass's checker,
  `derive_carries_coverage`'s `dTrueNorth` entry read 6 clauses and 1 owned node over 20 specs:
  whole 6, split none, released none, uncarried none, stale none, ambiguous none, unnamed none, 14
  derived specs each `PLAY-dClosedLoop-2`, blind `cl-dClosedLoop-0002`. The instrument's
  `--report dTrueNorth` printed `over 20 specs`, `carried whole: 6; carried in parts: 0 (none)`,
  `moved, retired or deferred: none`, `uncarried: none; stale: none; ambiguous: none`, `owned nodes
  no spec names: none`, the same 14 derived specs, and `clauses the token arm cannot see:
  cl-dClosedLoop-0002`. The values are derived at observation.
- AC14 — `SPEC_CARRIES_CUTOFF 2026-10-21` — in the scratch clone `main()` exited 0 printing
  `spec-tokens: carries join · 20 chain spec(s) measured in 1 build(s), every status but WONTDO,
  not only live spec(s) · 509 clause(s) · 0 withdrawn · 524 owned node(s) · 0 finding(s), 0 at the
  Design exit only · SPEC_CARRIES_CUTOFF 2026-10-21`; 20 is the figure derived from the build's
  roster at observation, where the criterion's text wrote 7. With unit 3's pin changed to
  `@deadbeef` it exited 1 printing the hit `carries <- stale:cl-dClosedLoop-0003` on that spec.
- AC15 — `SPEC_CARRIES_CUTOFF blank (arm off)` — in the clone, the stale pin still planted and the
  key set to `SPEC_CARRIES_CUTOFF=""`, `main()` exited 0 printing the carries line with `0 chain
  spec(s) measured in 0 build(s)` and `SPEC_CARRIES_CUTOFF blank (arm off)`, and no `[carries]`
  hit. Set to `2026-10-2`, it exited 1 printing `REFUSING — SPEC_CARRIES_CUTOFF 2026-10-2 is not an
  ISO date (YYYY-MM-DD)`.
- AC16 — `--list` — in the clone, a waiver row keyed `carries <- stale:cl-dClosedLoop-0003` made
  the plain run exit 0, and `--list` printed `WAIVED [carries]` for that token; a row keyed on the
  bare spec path instead left the run at exit 1 with the stale hit printed.
- AC17 — `grep -n 'carries' tools/check-spec-tokens.py` — over the module header it printed line
  37, the ninth join named with its own population, and the entry from line 117, its matched lines
  naming the carries population, `the carries key SPEC_CARRIES_CUTOFF`, `THE SEMANTIC BLIND SIDE`
  at line 132 and `THE RENAME` at line 135.
