# TOOL-dFairHearing-1 — the known set: the runtime design's 59 reviewed defects and its 6 escapes

**Serves:** research TOOL-dFairHearing-1

**Population:** 65 · reviewed 59 · escaped 6 · high 8

The file `review_replay.py --known-set` reads (`parse_known_set`, TOOL-dFairHearing-1 S1, S2). Each row
is one known defect of the runtime record at blob `767187aa4073f6e64cb2b2ef6b798f0a538347fd`; its
`address` is that record's path and one section tag, the form `extract_tag_ref` reads.

- **The 59 reviewed rows** are the `[map]` rows of
  `memory/builds/dClosedLoop/build/2026-10-15-build-PLAY-dClosedLoop-1-runtime-reviews-compared.md`
  holding a confirmed finding, in `[map]` order: every row but `prose-ceilings` and `slug-shape`.
  A row's source is the lowest-numbered confirmed finding `[map]` places on it, run A's before run
  B's, and its tag the first `[tag]` of the source's ref that at least one confirmed finding of every
  round that found the defect also cites (spec §8 F6). That moves two rows off the source's own first
  tag, both to `[supervise]`: `executor-map` (A5 opens `[extend]`) and `inflight-count` (A8 opens
  `[invariants]`). `codex-events` takes `[policies]`, because A22's `[\harness]` is not a tag
  `TAG_REF` reads. `grade` is `high` for the eight defects `[numbers]` grades high and `medium`
  otherwise. The rows were derived by the probe the calibration record carries
  (`2026-11-03-build-TOOL-dFairHearing-1-calibration`).
- **The 6 escaped rows** are the four defects the fold found (`[neither]`) and the two the floor probe
  found (`2026-10-15-build-PLAY-dClosedLoop-1-research-review-lenses.md`, `[escapes]`), each at the
  section of the record at blob `767187aa` holding the claim it corrects, graded `ungraded`:
  `act-ceiling` at `[supervise]`, where `--max-turns` is the driver's only bound; `dirty-worktree` at
  `[isolate]`, which allocates each unit's worktree; `kit-confs` at `[policies]`, the key table that
  never places the kit confs; `spawn-backend` at `[spawn]`, which names the Workflow harness as the
  one way an agent spawns; `docs-floor` at `[enforce]`, which declares `runtime.cli-floor`; and
  `allow-bypass` at `[enforce]`, the one enforcement surface the allow rule bypasses.

| tag | address | grade | escaped |
|---|---|---|---|
| relaunch-replay | memory/builds/dClosedLoop/build/2026-10-15-build-PLAY-dClosedLoop-1-layer-runtime.md:[supervise] | high | no |
| driver-schema | memory/builds/dClosedLoop/build/2026-10-15-build-PLAY-dClosedLoop-1-layer-runtime.md:[supervise] | medium | no |
| driver-cwd | memory/builds/dClosedLoop/build/2026-10-15-build-PLAY-dClosedLoop-1-layer-runtime.md:[isolate] | medium | no |
| calls-per-act | memory/builds/dClosedLoop/build/2026-10-15-build-PLAY-dClosedLoop-1-layer-runtime.md:[act] | medium | no |
| merge-back | memory/builds/dClosedLoop/build/2026-10-15-build-PLAY-dClosedLoop-1-layer-runtime.md:[isolate] | high | no |
| chain-overlap | memory/builds/dClosedLoop/build/2026-10-15-build-PLAY-dClosedLoop-1-layer-runtime.md:[build] | high | no |
| return-check-owner | memory/builds/dClosedLoop/build/2026-10-15-build-PLAY-dClosedLoop-1-layer-runtime.md:[build] | medium | no |
| executor-map | memory/builds/dClosedLoop/build/2026-10-15-build-PLAY-dClosedLoop-1-layer-runtime.md:[supervise] | medium | no |
| renewal-keys | memory/builds/dClosedLoop/build/2026-10-15-build-PLAY-dClosedLoop-1-layer-runtime.md:[policies] | medium | no |
| fixture-2-population | memory/builds/dClosedLoop/build/2026-10-15-build-PLAY-dClosedLoop-1-layer-runtime.md:[tests] | high | no |
| hidden-spawns | memory/builds/dClosedLoop/build/2026-10-15-build-PLAY-dClosedLoop-1-layer-runtime.md:[invariants] | medium | no |
| inflight-count | memory/builds/dClosedLoop/build/2026-10-15-build-PLAY-dClosedLoop-1-layer-runtime.md:[supervise] | medium | no |
| unfailing-fixtures | memory/builds/dClosedLoop/build/2026-10-15-build-PLAY-dClosedLoop-1-layer-runtime.md:[tests] | medium | no |
| fail-closed-policy | memory/builds/dClosedLoop/build/2026-10-15-build-PLAY-dClosedLoop-1-layer-runtime.md:[invariants] | medium | no |
| binding-events | memory/builds/dClosedLoop/build/2026-10-15-build-PLAY-dClosedLoop-1-layer-runtime.md:[invariants] | medium | no |
| extension-enums | memory/builds/dClosedLoop/build/2026-10-15-build-PLAY-dClosedLoop-1-layer-runtime.md:[extend] | medium | no |
| compaction-checks | memory/builds/dClosedLoop/build/2026-10-15-build-PLAY-dClosedLoop-1-layer-runtime.md:[sessions] | medium | no |
| invariant-8-fixture | memory/builds/dClosedLoop/build/2026-10-15-build-PLAY-dClosedLoop-1-layer-runtime.md:[invariants] | medium | no |
| invariant-coverage | memory/builds/dClosedLoop/build/2026-10-15-build-PLAY-dClosedLoop-1-layer-runtime.md:[invariants] | medium | no |
| cli-binary | memory/builds/dClosedLoop/build/2026-10-15-build-PLAY-dClosedLoop-1-layer-runtime.md:[enforce] | medium | no |
| cli-floor-decision | memory/builds/dClosedLoop/build/2026-10-15-build-PLAY-dClosedLoop-1-layer-runtime.md:[enforce] | medium | no |
| supervisor-host | memory/builds/dClosedLoop/build/2026-10-15-build-PLAY-dClosedLoop-1-layer-runtime.md:[supervise] | medium | no |
| codex-events | memory/builds/dClosedLoop/build/2026-10-15-build-PLAY-dClosedLoop-1-layer-runtime.md:[policies] | medium | no |
| dispatcher-latency | memory/builds/dClosedLoop/build/2026-10-15-build-PLAY-dClosedLoop-1-layer-runtime.md:[enforce] | medium | no |
| fanout-carrier | memory/builds/dClosedLoop/build/2026-10-15-build-PLAY-dClosedLoop-1-layer-runtime.md:[policies] | medium | no |
| reap-key | memory/builds/dClosedLoop/build/2026-10-15-build-PLAY-dClosedLoop-1-layer-runtime.md:[policies] | medium | no |
| resume-tick-seed | memory/builds/dClosedLoop/build/2026-10-15-build-PLAY-dClosedLoop-1-layer-runtime.md:[supervise] | medium | no |
| hookspath | memory/builds/dClosedLoop/build/2026-10-15-build-PLAY-dClosedLoop-1-layer-runtime.md:[enforce] | medium | no |
| hookspath-readers | memory/builds/dClosedLoop/build/2026-10-15-build-PLAY-dClosedLoop-1-layer-runtime.md:[enforce] | medium | no |
| permission-mode | memory/builds/dClosedLoop/build/2026-10-15-build-PLAY-dClosedLoop-1-layer-runtime.md:[supervise] | medium | no |
| parallel-cleared | memory/builds/dClosedLoop/build/2026-10-15-build-PLAY-dClosedLoop-1-layer-runtime.md:[current] | medium | no |
| core-sweep | memory/builds/dClosedLoop/build/2026-10-15-build-PLAY-dClosedLoop-1-layer-runtime.md:[isolate] | medium | no |
| journal-owner | memory/builds/dClosedLoop/build/2026-10-15-build-PLAY-dClosedLoop-1-layer-runtime.md:[contract] | medium | no |
| hook-fragments | memory/builds/dClosedLoop/build/2026-10-15-build-PLAY-dClosedLoop-1-layer-runtime.md:[enforce] | medium | no |
| resume-tick-consumers | memory/builds/dClosedLoop/build/2026-10-15-build-PLAY-dClosedLoop-1-layer-runtime.md:[supervise] | medium | no |
| next-readers | memory/builds/dClosedLoop/build/2026-10-15-build-PLAY-dClosedLoop-1-layer-runtime.md:[decide] | medium | no |
| catalogue-duplicates | memory/builds/dClosedLoop/build/2026-10-15-build-PLAY-dClosedLoop-1-layer-runtime.md:[policies] | high | no |
| gap-keys | memory/builds/dClosedLoop/build/2026-10-15-build-PLAY-dClosedLoop-1-layer-runtime.md:[gaps-proposed] | medium | no |
| relaunch-cap | memory/builds/dClosedLoop/build/2026-10-15-build-PLAY-dClosedLoop-1-layer-runtime.md:[supervise] | medium | no |
| hold-bound | memory/builds/dClosedLoop/build/2026-10-15-build-PLAY-dClosedLoop-1-layer-runtime.md:[spawn] | medium | no |
| command-idempotence | memory/builds/dClosedLoop/build/2026-10-15-build-PLAY-dClosedLoop-1-layer-runtime.md:[supervise] | medium | no |
| fencing | memory/builds/dClosedLoop/build/2026-10-15-build-PLAY-dClosedLoop-1-layer-runtime.md:[supervise] | high | no |
| reap-predicate | memory/builds/dClosedLoop/build/2026-10-15-build-PLAY-dClosedLoop-1-layer-runtime.md:[isolate] | medium | no |
| deferral-fixtures | memory/builds/dClosedLoop/build/2026-10-15-build-PLAY-dClosedLoop-1-layer-runtime.md:[tests] | medium | no |
| cadence-period | memory/builds/dClosedLoop/build/2026-10-15-build-PLAY-dClosedLoop-1-layer-runtime.md:[schedule] | medium | no |
| next-answers | memory/builds/dClosedLoop/build/2026-10-15-build-PLAY-dClosedLoop-1-layer-runtime.md:[decide] | medium | no |
| bash-improvisation | memory/builds/dClosedLoop/build/2026-10-15-build-PLAY-dClosedLoop-1-layer-runtime.md:[act] | medium | no |
| cycle-spawns | memory/builds/dClosedLoop/build/2026-10-15-build-PLAY-dClosedLoop-1-layer-runtime.md:[act] | high | no |
| instance-witness | memory/builds/dClosedLoop/build/2026-10-15-build-PLAY-dClosedLoop-1-layer-runtime.md:[invariants] | medium | no |
| structured-output | memory/builds/dClosedLoop/build/2026-10-15-build-PLAY-dClosedLoop-1-layer-runtime.md:[spawn] | high | no |
| headless-workflow | memory/builds/dClosedLoop/build/2026-10-15-build-PLAY-dClosedLoop-1-layer-runtime.md:[supervise] | medium | no |
| compact-target | memory/builds/dClosedLoop/build/2026-10-15-build-PLAY-dClosedLoop-1-layer-runtime.md:[sessions] | medium | no |
| user-guards | memory/builds/dClosedLoop/build/2026-10-15-build-PLAY-dClosedLoop-1-layer-runtime.md:[tests] | medium | no |
| stopfailure-packs | memory/builds/dClosedLoop/build/2026-10-15-build-PLAY-dClosedLoop-1-layer-runtime.md:[enforce] | medium | no |
| deferral-seam | memory/builds/dClosedLoop/build/2026-10-15-build-PLAY-dClosedLoop-1-layer-runtime.md:[spawn] | medium | no |
| owner-rulings | memory/builds/dClosedLoop/build/2026-10-15-build-PLAY-dClosedLoop-1-layer-runtime.md:[framing] | medium | no |
| git-witness-readers | memory/builds/dClosedLoop/build/2026-10-15-build-PLAY-dClosedLoop-1-layer-runtime.md:[enforce] | medium | no |
| return-write-path | memory/builds/dClosedLoop/build/2026-10-15-build-PLAY-dClosedLoop-1-layer-runtime.md:[spawn] | medium | no |
| limit-hold | memory/builds/dClosedLoop/build/2026-10-15-build-PLAY-dClosedLoop-1-layer-runtime.md:[spawn] | medium | no |
| act-ceiling | memory/builds/dClosedLoop/build/2026-10-15-build-PLAY-dClosedLoop-1-layer-runtime.md:[supervise] | ungraded | yes |
| dirty-worktree | memory/builds/dClosedLoop/build/2026-10-15-build-PLAY-dClosedLoop-1-layer-runtime.md:[isolate] | ungraded | yes |
| kit-confs | memory/builds/dClosedLoop/build/2026-10-15-build-PLAY-dClosedLoop-1-layer-runtime.md:[policies] | ungraded | yes |
| spawn-backend | memory/builds/dClosedLoop/build/2026-10-15-build-PLAY-dClosedLoop-1-layer-runtime.md:[spawn] | ungraded | yes |
| docs-floor | memory/builds/dClosedLoop/build/2026-10-15-build-PLAY-dClosedLoop-1-layer-runtime.md:[enforce] | ungraded | yes |
| allow-bypass | memory/builds/dClosedLoop/build/2026-10-15-build-PLAY-dClosedLoop-1-layer-runtime.md:[enforce] | ungraded | yes |
