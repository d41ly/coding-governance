# TOOL-dIndexedDesign-16 — design coverage by policy: the carries join read at each Design exit and each spec revision, `UNCARRIED`, and the coverage lens

**Status:** DEFERRED · rev-4 · 2026-10-28 · node d · Tier-2 · base 57bc3b91 · streams tooling · order 3 · advances TOOL-dIndexedDesign-17 · closes TOOL-dIndexedDesign-18

**Carries:** cl-dClosedLoop-0398@f6f6546a whole
**Carries:** node:policy-key.design.coverage
**Carries:** node:policy-key.design.coverage.semantic

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-28-build-TOOL-dIndexedDesign-1-agent-ledger.md](../build/2026-10-28-build-TOOL-dIndexedDesign-1-agent-ledger.md) | journal | TOOL-dIndexedDesign-1 TOOL-dIndexedDesign-2 TOOL-dIndexedDesign-3 TOOL-dIndexedDesign-4 TOOL-dIndexedDesign-5 TOOL-dIndexedDesign-6 TOOL-dIndexedDesign-7 TOOL-dIndexedDesign-8 TOOL-dIndexedDesign-9 TOOL-dIndexedDesign-10 TOOL-dIndexedDesign-11 TOOL-dIndexedDesign-12 TOOL-dIndexedDesign-13 TOOL-dIndexedDesign-14 TOOL-dIndexedDesign-15 TOOL-dIndexedDesign-20 TOOL-dIndexedDesign-31 TOOL-dIndexedDesign-32 TOOL-dIndexedDesign-33 TOOL-dIndexedDesign-34 TOOL-dIndexedDesign-35 TOOL-dIndexedDesign-36 TOOL-dIndexedDesign-37 TOOL-dIndexedDesign-38 TOOL-dIndexedDesign-39 TOOL-dIndexedDesign-40 TOOL-dIndexedDesign-41 TOOL-dIndexedDesign-42 TOOL-dIndexedDesign-43 TOOL-dIndexedDesign-44 TOOL-dIndexedDesign-45 TOOL-dIndexedDesign-46 TOOL-dIndexedDesign-47 TOOL-dIndexedDesign-48 TOOL-dIndexedDesign-49 TOOL-dIndexedDesign-50 TOOL-dIndexedDesign-51 TOOL-dIndexedDesign-52 TOOL-dIndexedDesign-53 |
| [2026-10-28-build-TOOL-dIndexedDesign-1-fix-return.md](../build/2026-10-28-build-TOOL-dIndexedDesign-1-fix-return.md) | research | TOOL-dIndexedDesign-1 TOOL-dIndexedDesign-2 TOOL-dIndexedDesign-3 TOOL-dIndexedDesign-8 TOOL-dIndexedDesign-9 TOOL-dIndexedDesign-11 TOOL-dIndexedDesign-12 TOOL-dIndexedDesign-13 TOOL-dIndexedDesign-15 TOOL-dIndexedDesign-20 |
| [2026-10-28-build-TOOL-dIndexedDesign-1-reuse-scout-a.md](../build/2026-10-28-build-TOOL-dIndexedDesign-1-reuse-scout-a.md) | research | TOOL-dIndexedDesign-1 TOOL-dIndexedDesign-2 TOOL-dIndexedDesign-3 TOOL-dIndexedDesign-6 |
| [2026-10-28-build-TOOL-dIndexedDesign-1-spec-stage-returns.md](../build/2026-10-28-build-TOOL-dIndexedDesign-1-spec-stage-returns.md) | research | TOOL-dIndexedDesign-1 TOOL-dIndexedDesign-2 TOOL-dIndexedDesign-3 TOOL-dIndexedDesign-4 TOOL-dIndexedDesign-5 TOOL-dIndexedDesign-6 TOOL-dIndexedDesign-7 TOOL-dIndexedDesign-8 TOOL-dIndexedDesign-9 TOOL-dIndexedDesign-10 TOOL-dIndexedDesign-11 TOOL-dIndexedDesign-12 TOOL-dIndexedDesign-13 TOOL-dIndexedDesign-14 TOOL-dIndexedDesign-15 |
| [2026-10-28-prompt-TOOL-dIndexedDesign-1-fix-brief.md](../prompts/2026-10-28-prompt-TOOL-dIndexedDesign-1-fix-brief.md) | research | TOOL-dIndexedDesign-1 TOOL-dIndexedDesign-2 TOOL-dIndexedDesign-3 TOOL-dIndexedDesign-8 TOOL-dIndexedDesign-9 TOOL-dIndexedDesign-11 TOOL-dIndexedDesign-12 TOOL-dIndexedDesign-13 TOOL-dIndexedDesign-15 TOOL-dIndexedDesign-20 |
| [2026-10-28-prompt-TOOL-dIndexedDesign-1-spec-brief.md](../prompts/2026-10-28-prompt-TOOL-dIndexedDesign-1-spec-brief.md) | research | TOOL-dIndexedDesign-1 TOOL-dIndexedDesign-2 TOOL-dIndexedDesign-3 TOOL-dIndexedDesign-4 TOOL-dIndexedDesign-5 TOOL-dIndexedDesign-6 TOOL-dIndexedDesign-7 TOOL-dIndexedDesign-8 TOOL-dIndexedDesign-9 TOOL-dIndexedDesign-10 TOOL-dIndexedDesign-11 TOOL-dIndexedDesign-12 TOOL-dIndexedDesign-13 TOOL-dIndexedDesign-14 TOOL-dIndexedDesign-15 |
| [2026-10-28-review-TOOL-dIndexedDesign-9-spec-audit-round1.md](../reviews/2026-10-28-review-TOOL-dIndexedDesign-9-spec-audit-round1.md) | spec-audit | TOOL-dIndexedDesign-9 TOOL-dIndexedDesign-12 TOOL-dIndexedDesign-1 TOOL-dIndexedDesign-7 TOOL-dIndexedDesign-2 TOOL-dIndexedDesign-6 TOOL-dIndexedDesign-8 TOOL-dIndexedDesign-13 TOOL-dIndexedDesign-20 TOOL-dIndexedDesign-5 TOOL-dIndexedDesign-4 TOOL-dIndexedDesign-14 TOOL-dIndexedDesign-10 TOOL-dIndexedDesign-11 TOOL-dIndexedDesign-15 TOOL-dIndexedDesign-3 |

<!-- /gen:spec-records -->

## 1. Goal

dTrueNorth's carries join already finds every arm v2 names, a dropped, unbound, stale or stopped
carrier and an uncarried clause (`tools/check-spec-tokens.py:931-1046`), but it is gated by a conf date
alone, read at no Design exit, and check 29 grades only INPROGRESS specs, which the harness never
holds (`gen_build_index.py:2958-2962`; ask PLAY-dClosedLoop-20). This unit reads that join as
`design.coverage` says (`refuse`, `warn`, `off`) at each spec revision and at each Design exit, gives
`design.ready` an `UNCARRIED` state, counts an `implements=` edge with a clause target as a carrier,
renders the policy in the coverage region, and adds the lens that reads each carried clause against
the sections it rests on, run as `design.coverage.semantic` says (`every-exit`, `with-spec-audit`,
`off`) (v2:1290-1291, P41; flow-steps:246; the owner's FQ-2). It closes ask TOOL-dIndexedDesign-18: the
exit reads clause text through the as-built view.

## 2. Scope (IN)

Build-run preconditions: the memory-tree policy adapter `tools/memory-tree/policy_value.py`,
`read_policy_value(key, root, rev=None)` (TOOL-dTotalRecall-8 S10, to PLAY-dOrderedCharter-7 §4 "The
policy reads"), built by the parent dTotalRecall; `read_spec_edge_lines` (`TOOL-dIndexedDesign-12` S1,
order 2). `SPEC_CARRIES_CUTOFF` stays the arming key: blank, everything below is off and says so, as
today; set, `design.coverage` decides.

- **S1** — The policy reader, shared interface I3: `read_design_policy(key, root)` in
  `tools/memory-tree/design_lib.py` returns the value of one of the seven `design.*` keys of
  `tools/policy/catalogue.toml` (:919-948, and `design.forks`, `design.reentry` at :41, :47), a list for
  `design.reentry` and a string otherwise, through `read_policy_value(key, root)`: no second
  subprocess reader. A key outside the seven, a `PolicyRefused` and an absent policy kit each raise
  `DesignRefusal` naming the key. Every caller passes the key as a string literal first, the shape
  `check_policy.py`'s reader arm counts (:425-433). Shell callers spell
  `"$PY" "<policy kit>/policy.py" get design.<key>` literally. Observed by AC1.
- **S2** — The per-spec verdict, shared interface I4's Python half: each build entry
  `derive_carries_coverage` returns (`check-spec-tokens.py:1049-1101`) gains `by_spec`,
  `{spec path: [(arm, ref)]}`, every per-spec finding plus each per-clause finding (`ambiguous`,
  `parts`, `token`) on every carrier of that clause; the exit-only arms (`uncarried`, `node`) stay
  build-level. The value also gains `policy`, `{"design.coverage": v, "design.coverage.semantic": v}`,
  read once through S1 when armed. Observed by AC4 and AC6.
- **S3** — At each spec revision, the spec-tokens checker's carries join (`check-spec-tokens.py:1685-1700`,
  its line at :1803-1809) reads `design.coverage`: `refuse` keeps today's hits; `warn` lists each
  finding as `NEAR` and adds no hit; `off` reads no join and its line says `design.coverage off`.
  Check 29, `cmd_check_coverage` (`gen_build_index.py:2911-2964`), does the same: `refuse` as today,
  `warn` one `build-index: coverage WARN —` line per finding and exit 0, `off` the line
  `build-index: coverage off — design.coverage is off` and exit 0. Observed by AC2 and AC3.
- **S4** — `implements=` with a clause target is a carrier: `scan_carries` reads each spec's
  `implements` edges through `read_spec_edge_lines`, and a `pinned-id` target whose id is a clause id
  joins as a whole carrier at its hash, beside the `**Carries:**` lines. One spec names a clause once:
  a `**Carries:**` line and an `implements=` edge at one hash are one carrier, at two hashes two pins,
  which `ambiguous` reds. The `stopped` arm's revisions read both. An edge line the adapter refuses is
  the spec's `malformed` finding. Observed by AC8.
- **S5** — The exit reading, `python tools/memory-tree/gen_build_index.py --design-exit <slug> [--unit
  <id>]`, beside `--check-coverage`, through `read_carries_coverage` (:1967) so the region, check 29
  and the exit read one value. It prints a head line naming the build, both policy values and the
  counts; one `design-exit: spec <path> · <arm> <ref>` line per `by_spec` finding; one
  `design-exit: build · <arm> <ref>` line per exit-only finding; and one
  `design-exit: lens <id>@rev-<N> · <none|past <M>|blocked>` line per unit S8's reading is owed and
  missing. With `--unit`, only that unit's spec and lens lines. Exit 1 when `design.coverage` is
  `refuse` and any line is printed, 0 otherwise, 2 on a refusal. Observed by AC4, AC5 and AC11.
- **S6** — `derive_ready_state <spec> <cutoff> [<exit-lines>]`, shared interface I4's shell half, in
  `tools/unattended/unattended.sh` beside `plan_state` (:4458): it prints `plan_state`'s token, unless
  that token is `READY`, `design.coverage` is `refuse` and S5's lines name the spec, when it prints
  `UNCARRIED`. The third argument is a file holding S5's output, read when given so a caller grading
  every unit runs S5 once; absent, it runs `--design-exit <slug> --unit <id>` itself. `plan_state` and its
  one-token contract stay byte-identical. Observed by AC6.
- **S7** — The Design exit, shared interface I5: `check_design_exit <slug> [<unit>]` in `unattended.sh`,
  called from `verb_phase` (:6135) when the move enters `BUILDING` and from `verb_dispatch` (:13624)
  after its THIN case (:13654-13656), with the dispatched unit. It runs S5 once, prints its lines, then
  for each roster unit of the build, or the one unit, takes the state from S6 with those lines; that
  per-unit step is where `TOOL-dIndexedDesign-1` adds its `design.handoff` arms. It refuses when S5
  exits 1, with fail 49 at `--dispatch` and `verb_phase`'s own refusal at `--phase`, each naming
  the slug, the first finding and `design.coverage`; under `warn` it admits after printing each line
  with `WARN` and the ask to file; under `off` it prints `design-exit: coverage off`. Observed by AC7.
- **S8** — The lens, shared interface I17: a `coverage` entry in `SPEC_LENSES`
  (`tools/workflows/tier2-review.template.js:810`) whose brief reads each clause a subject spec carries,
  by `**Carries:**` or `implements=`, through `design_lib.py --design --build <slug>`, with the sections
  it rests on (Scope, Design, Acceptance criteria, by `design_lib.py --section`), and reports a carrier
  that keeps the clause's tokens and contradicts it as a blocker. A new argument `coverage`, `with`,
  `only` or `skip`, default `skip`, is checked like `intensity` (:210-217): `skip` leaves the lens out
  inside the Find thunk as `LIGHT_LENSES` does; `only` runs the lens alone and `renderAuditBinding`
  (:318-328) writes `**Serves:** coverage-lens <id>@rev-<N> …`; the review-shape line gains
  `coverage=<value>`. `unattended-build.template.js` takes `coverageSemantic` (`every-exit`,
  `with-spec-audit` or `off`; absent, announced and taken as `off`) and passes `with` to its audit under
  `every-exit` or `with-spec-audit`, and under `every-exit` with no `specAudit` runs one `only` review
  before the hand-out. The driver's preflight line naming `spec-audit` also prints
  `design.coverage.semantic <value>`, read by the literal `policy.py get design.coverage.semantic`.
  Renders `tier2-review.js` and `unattended-build.js`. Observed by AC9 and AC10.
- **S9** — The lens reading at the exit: `coverage-lens` joins `RECORD_KIND_TOKENS`
  (`tools/memory-tree/tree_lib.py:406`), its pins graded as a `spec-audit` record's are under
  `SPEC_AUDIT_PIN_CUTOFF` (`gen_build_index.py:730`). S5 owes a reading under `every-exit` for every
  unit, and under `with-spec-audit` only where the build declares a spec audit: a `coverage-lens`
  record, or a `spec-audit` record whose review-shape line says `coverage=with`, pinning the unit's
  header revision. A reading missing (`none`), below the revision (`past <M>`), or whose record's
  verdict is `BLOCKED` (`blocked`) is a lens line. Under `off` nothing is owed. No audit counter reads a
  `coverage-lens` record. Observed by AC11.
- **S10** — The index renders coverage under the policy: `render_coverage` (`gen_build_index.py:1796`)
  heads its region with `design.coverage <value>` and adds the bullet `uncarried units: <ids or none>`,
  each from S2's value. Observed by AC12.
- **S11** — The keys' rows: `design.coverage` and `design.coverage.semantic` gain `summary` and `usage`
  in `catalogue.toml`, values and defaults as written, and `python tools/policy/policy.py lists --write`
  drains both from `tools/policy/unsummarised-keys.txt` (:52-53). The literal readers are S3's and S5's
  `read_design_policy("design.coverage", root)` and S8's shell read. Observed by AC13.
- **S12** — The surfaces: `tools/unattended/kit.toml` `requires` gains `policy` (§8 F3); `help/policy.md`
  names both keys and their consumers; `tools/unattended/VERBS.template.md`, rendered to
  `memory/guides/UNATTENDED-VERBS.md`, names the coverage refusal at `--phase BUILDING` and
  `--dispatch`; `tools/memory-tree/HYGIENE.template.md`, rendered to `memory/HYGIENE.md`, names the
  `coverage-lens` kind (:627-630). Observed by AC14.

## 3. Non-goals (OUT)

- The `design.handoff` arms in `check_design_exit`: `TOOL-dIndexedDesign-1`'s. This unit lands the
  function, its call sites, its unit population and its coverage reading.
- Extending check 29's trigger past INPROGRESS: the owner's ruling, ask PLAY-dClosedLoop-20. The exit
  reading is how a harness-run build is graded instead (§4 "What check 29 misses").
- `carries.py` and the packet's Gates line: instruments under `memory/builds/dClosedLoop/build/`, never
  edited (the packet's Non-goals). Retiring the instrument from the exit is the execution plan's
  `[phase-1]` table's act once this lands.
- Running the coverage lens from the driver: the driver cannot spawn an agent; it reads the record.
- The design index's overlap region: `TOOL-dIndexedDesign-2`'s.
- Audit opt-in by `review.design`: `TOOL-dIndexedDesign-3`'s; S9's `with-spec-audit` reads today's
  declaration, which that unit re-points.

### Edges

- **consumes-from** `TOOL-dIndexedDesign-12` — `read_spec_edge_lines`, whose `implements=` pinned clause targets S4 counts; without it S4 has no edges to read
- **hands-off** `TOOL-dIndexedDesign-1` — `check_design_exit`, I5, with `derive_ready_state`, I4, the per-unit step its `design.handoff` arms sit in; a `coverage-lens` record is no audit for `ready-plus-audit`
- **hands-off** `TOOL-dIndexedDesign-1` — `read_design_policy`, I3, the reader its `design.handoff` read follows
- **hands-off** `TOOL-dIndexedDesign-2` — `read_design_policy`, I3, for `design.overlap`
- **hands-off** `TOOL-dIndexedDesign-8` — `read_design_policy`, I3, for `design.forks`
- **hands-off** `TOOL-dIndexedDesign-20` — `read_design_policy`, I3, for `design.reentry`, the one key of the seven it returns as a list
- **hands-off** `TOOL-dIndexedDesign-15` — `read_design_policy`, I3, for `design.streams-when`
- **hands-off** `TOOL-dIndexedDesign-3` — `read_design_policy`, I3, and S9's `with-spec-audit` test, which reads the audit declaration it re-points
- **consumes-from** external — dTotalRecall's `policy_value.read_policy_value` (TOOL-dTotalRecall-8 S10), DEFERRED at base, built before this build run; dGroundRules' `policy.py get` and `lists --write`, landed
- **hands-off** `TOOL-dIndexedDesign-35` — S8's coverage lens, which that unit runs as its own one-agent stage so `SPEC_LENSES` stays at five (report id 28, HIGH)
- **hands-off** `TOOL-dIndexedDesign-36` — the dispatch refusals this unit adds, which that unit names in BUILD-METHOD M6 (report id 33, HIGH)
- **hands-off** `TOOL-dIndexedDesign-38` — the round-1 spec audit's minors that land on this spec, report ids 1, 2, 3, 9, 12, 13, 18, 24, 29 and 40, each a scope item of that batch unit
- **hands-off** `TOOL-dIndexedDesign-39` — this unit's pass commit also carries unit 35's S1 to S4, as that unit's S1 requires, so S8's brief goes straight to `COVERAGE_BRIEF` and `SPEC_LENSES` never holds six entries; that unit's own pass observes every commit (id 1)
- **hands-off** `TOOL-dIndexedDesign-41` — S7's refusals, which that unit's S1 composes in this unit's pass commit: `check_design_exit` holds no `fail` site, `--dispatch` refuses through the THIN site and the two `fail 31` sites fold into one, so the census stays at or under 323 (id 3)
- **hands-off** `TOOL-dIndexedDesign-44` — S8's `coverage` argument and `coverage-lens` binding, whose coverage agent that unit counts as a finder (id 26)
- **hands-off** `TOOL-dIndexedDesign-48` — S7's `--dispatch` refusal, whose composed THIN site that unit's S1 writes in this unit's pass commit with its own literal run, `--dispatch refuses a build pass for a unit not ready to build`, and whose THIN arm its S2 re-pins (id 10)
- **hands-off** `TOOL-dIndexedDesign-49` — S7's design-exit refusal at `--dispatch`, whose arm, declared in this unit's §7, asserts the clause `_dx_msg` holds and not the composed site's literal run, as that unit's S1 requires in this unit's pass commit (id 19)
- **hands-off** `TOOL-dIndexedDesign-50` — this unit's pass commit also carries `TOOL-dIndexedDesign-44`'s S1 to S4, the coverage stage's finder counts, dead label, findings join and durable file, as that unit's S1 requires (id 3)

## 4. Design

### One value, four readers

```
read_carries_coverage (gen_build_index.py:1967) -> derive_carries_coverage (check-spec-tokens.py:1049)
   value: builds[b] = {..., findings, by_spec}, policy = {design.coverage, design.coverage.semantic}
   ├─ spec-tokens carries join   at commit and inside --dispatch     (each spec revision)
   ├─ check 29 --check-coverage  per staged spec, INPROGRESS          (each spec revision, attended)
   ├─ --design-exit              check_design_exit, derive_ready_state (each Design exit)
   └─ render_coverage            the README coverage region           (the owner's report)
```

| `design.coverage` | spec revision | Design exit | `design.ready` |
|---|---|---|---|
| `refuse` | a hit, exit 1 | refused naming the finding | `UNCARRIED` where the spec has a finding |
| `warn` | `NEAR`, exit 0 | admitted, each finding printed with the ask to file | `plan_state`'s token |
| `off` | not read, said | not read, said | `plan_state`'s token |

`UNCARRIED` follows `FORKED` in M2's first-match order: a THIN or FORKED spec keeps its token.

### What check 29 misses, and what reads it instead

The harness takes each spec OPEN to CLOSED in its build commit, so check 29's INPROGRESS population is
empty on every harness-run build. `check_design_exit` reads the same findings, every arm, at the two
moments that matter there: the move into `BUILDING`, the moment check 29 assumes, and every
`--dispatch` after it, so a spec revised past the exit is graded before its unit builds. A revision
after the last dispatch meets the spec-tokens join at its commit.

### Ask TOOL-dIndexedDesign-18

`read_design` builds each clause's text and hash from the as-built view, where a deviation's `amends`
row replaces the text (`design_lib.py:682-701`, `VIEW_ROW` at :125). The exit reads that value, never
`carries.py`, so a spec pinned to an amended clause's view hash is carried, and one pinned to the
baseline hash of that clause is `stale`. AC5 plants both.

### The lens

The join sees a dropped clause; it cannot see a carrier that keeps every token and says the opposite.
The lens reads the clause text from the design view, never from the spec, and the spec's Scope, Design
and Acceptance criteria, and reports each contradiction with the clause line and the spec line. Its
reading is a record S9 can find, so `every-exit` is graded at the exit rather than claimed.

```
review-shape kind=spec-audit round=1 intensity=full coverage=only at=synth raw=2 … agents=4 out-tokens=…
**Serves:** coverage-lens TOOL-dFix-3@rev-2 TOOL-dFix-4@rev-1
```

### Inventory

| Minted | Kind | Lexicon cell |
|---|---|---|
| `read_design_policy` | Python function, `design_lib.py` | `py.function` |
| `by_spec`, `policy` | keys of the coverage value | none |
| `--design-exit`, `--unit` | flags of `gen_build_index.py` | none |
| `derive_ready_state`, `check_design_exit` | shell functions, `unattended.sh` | `sh.function` |
| `UNCARRIED` | `design.ready` state token | none |
| `coverage` lens, `coverage` argument | `tier2-review.js` | none |
| `coverageSemantic` | `unattended-build.js` argument | none |
| `coverage-lens` | record kind token, `tree_lib.py` | none |

### Migration

None forced. Under a blank `SPEC_CARRIES_CUTOFF`, an adopter's state, nothing reads policy. This repo's
chain builds read `refuse` and `every-exit`, the catalogue defaults; a build run entering `BUILDING`
after this lands needs a lens reading pinned to its specs' revisions, which its spec run's audit or one
`only` review gives.

### Rollout

The reader and the value first, then the revision readers, then `--design-exit` and the driver, then the
lens and its record kind, then the region and the docs. Each step is green because the exit reads
nothing until S7 lands.

### Files touched (estimate)

- `tools/memory-tree/design_lib.py`: S1
- `tools/check-spec-tokens.py`: S2, S3, S4
- `tools/check-spec-tokens.test.sh`: arms of §7
- `tools/memory-tree/gen_build_index.py`: S3, S5, S9, S10
- `tools/memory-tree/tree_lib.py`: S9
- `tools/memory-tree/check-memory-hygiene.sh`: check 29's comment block and `KIT_MEMORY_TREE_VERSION`
- `tools/unattended/unattended.sh`: S6, S7, S8's preflight line, `KIT_UNATTENDED_VERSION`
- `tools/unattended/unattended.test.sh`: S6, S7 arms
- `tools/unattended/kit.toml`: S12
- `tools/workflows/tier2-review.template.js`, `tools/workflows/unattended-build.template.js`: S8;
  `tools/workflows/tier2-review.js`, `tools/workflows/unattended-build.js` their renders
- `tools/workflows/tier2-review.test.sh`, `tools/workflows/unattended-build.test.sh`: S8 arms
- `tools/policy/catalogue.toml`, `tools/policy/unsummarised-keys.txt`: S11
- `help/policy.md`: S12
- `tools/unattended/VERBS.template.md`, and `memory/guides/UNATTENDED-VERBS.md` its render: S12
- `tools/memory-tree/HYGIENE.template.md`, and `memory/HYGIENE.md` its render: S12

### Alternatives rejected

- **A sixth token inside `plan_state`'s awk.** Lost to its one-token contract, which two harnesses
  slice (`unattended.sh:4485-4490`); `derive_ready_state` wraps it and AC6 checks the slice is
  unchanged.
- **The exit reading `carries.py`.** Lost to ask -18 itself: the instrument hashes v2 alone, so a spec
  following its own amendment reads stale (dFairHearing's two pins).
- **A second subprocess policy reader in `design_lib`, as the brief's I3 first proposed.** Lost to
  [reuse]: TOOL-dTotalRecall-8 S10's adapter is the memory-tree kit's one caller of `policy.py get`, and
  five other specs already read through it.
- **The lens as an always-on sixth spec-audit lens.** Lost to `off`: every audit would run it, and
  `every-exit` with no audit declared would run nothing.

## 5. Production-readiness checklist

- security — no new write path; the lens is read-only like every spec lens; policy is read at the
  landed revision, never the working tree.
- perf / scale — one join and two policy reads per exit or per run; `derive_ready_state` reuses S5's
  output inside `check_design_exit`; the lens is one agent stage, at most once per exit.
- error / empty / loading states — a policy refusal or an absent kit refuses the exit by name, never
  defaults; an empty roster prints its zero count; an armed join measuring nothing refuses, as today.
- observability — the head line names both values; every finding is one line; the review-shape line
  names `coverage=`.
- risks — the exit now refuses where it admitted; `warn` is the owner's escape, by the policy file.
- testing — AC1 to AC14 by a pass; the arms of §7 and AC10's live run at the close.
- migration — §4 Migration.
- user docs — `help/policy.md` (S12).

## 6. Acceptance criteria

- **AC1** — When `python -c "import design_lib; print(design_lib.read_design_policy('design.coverage', r))"`
  runs from `tools/memory-tree/` over a scratch repository whose committed `.governance/policy.toml`
  sets `design.coverage = "warn"`, it prints `warn`; with the key unset, `refuse`; asked for
  `design.nope`, it raises naming the key.
  Red when: the working tree is read, or an unknown key is answered.
- **AC2** — When `python tools/check-spec-tokens.py` runs from a scratch chain repository built by
  `design_lib.write_design_fixture` holding one spec with a stale pin, with `design.coverage` planted as
  `refuse`, `warn` and `off` in turn, it exits 1 naming `stale`, then 0 listing it `NEAR`, then 0 with
  the join line saying `design.coverage off`.
  Red when: any value grades as another does.
- **AC3** — When `gen_build_index.py --check-coverage` runs over the AC2 repository with that spec
  `INPROGRESS`, it exits 1 under `refuse`, 0 with a `coverage WARN` line under `warn`, and 0 with
  `design.coverage is off` under `off`.
  Red when: check 29 ignores the key.
- **AC4** — When `gen_build_index.py --design-exit tFixA` runs over the AC2 repository with one clause
  dropped from every spec, the clause's first seen-red case, it prints `design-exit: build · uncarried`
  naming the clause and exits 1 under `refuse`; with the clause carried and a current lens reading, it
  exits 0.
  Red when: a dropped clause passes the exit under `refuse`.
- **AC5** — When the AC2 repository's view row amends a clause, `since` naming a deviation, and one spec
  pins the amended text's hash, `--design-exit` prints no finding for it; pinned instead to the clause's
  baseline hash, it prints `stale` and exits 1: ask TOOL-dIndexedDesign-18's accept line.
  Red when: the baseline hash is carried, or the amended one is stale.
- **AC6** — When `derive_ready_state` runs over a READY spec S5 names, it prints `UNCARRIED` under
  `refuse` and `READY` under `warn` and `off`; over a FORKED spec S5 names, `FORKED`; and
  `sed -n '/^plan_state()/,/^}/p'` over `unattended.sh` prints the same bytes at HEAD and at base.
  Red when: `UNCARRIED` outranks FORKED, prints under `warn`, or `plan_state` changed.
- **AC7** — When `bash tools/unattended/unattended.sh --phase tFixA BUILDING <sha>` runs on a fixture
  run whose build has an uncarried clause, it refuses naming the clause and
  `design.coverage refuse`; `--dispatch` of a unit whose spec has a stale pin refuses with fail 49;
  under `warn` both admit printing `WARN`.
  Red when: either verb admits under `refuse` or refuses under `warn`.
- **AC8** — When `--design-exit` runs over a scratch spec carrying its clause only through
  `**Edges:** implements=<cl>@<hash8>`, the clause reads carried whole; with a `**Carries:**` line at
  the same hash beside it, one carrier and no `ambiguous`; at another hash, `ambiguous`.
  Red when: the edge is not counted, or one spec counts twice.
- **AC9** — When `tier2-review.js` is evaluated under `node` with a stub `Workflow` that records the
  agents it is handed, `coverage: 'only'` hands the `coverage` lens alone and writes a
  `**Serves:** coverage-lens` line and `coverage=only` on the shape line, `'skip'` hands no `coverage`
  lens, and `coverage: 'all'` is refused naming the three values; and `unattended-build.js`, evaluated
  the same way with `coverageSemantic: 'every-exit'` and no `specAudit`, schedules one `only` review.
  Red when: the lens runs under `skip`, or the record kind is `spec-audit` for an `only` run.
- **AC10** — When a `Workflow` run of `tier2-review.js` with `coverage: 'only'` reviews a planted
  carrier that keeps every token of its clause and states the clause's opposite in its Scope, the
  clause's second seen-red case, its record's verdict is `BLOCKED` naming the clause; its faithful twin
  reads `CLEAN`.
  cost: one lens and its verifier, a few minutes of agent time.
  permission: an agent run; the main loop observes it at the close, as `New arm:` declares.
  Red when: the contradiction passes, which only the lens can see.
- **AC11** — When `--design-exit` runs under `every-exit` over the AC2 repository, it prints
  `lens <id>@rev-<N> · none` for a unit no reading pins and exits 1; a `coverage-lens` record pinning
  the revision clears it; the same record with `## Verdict: BLOCKED` prints `blocked`; under
  `with-spec-audit` with no `spec-audit:` declared, and under `off`, no lens line prints.
  Red when: a missing, stale or blocked reading passes under `every-exit`.
- **AC12** — When `gen_build_index.py --write` runs over the AC2 repository, the build's
  `gen:build-coverage` region heads with `design.coverage refuse` and lists `uncarried units:` with the
  stale spec's unit.
  Red when: the region omits the policy or the units.
- **AC13** — When `python tools/policy/policy.py lists --check` runs at the pass tip it exits 0, and
  `grep -c "design.coverage" tools/policy/unsummarised-keys.txt` prints 0; `git grep -n
  "read_design_policy(\"design.coverage" -- tools` finds S3's and S5's literal reads.
  Red when: a row lacks its summary, or a key has no literal reader.
- **AC14** — When `grep -n "design.coverage" help/policy.md memory/guides/UNATTENDED-VERBS.md` and
  `grep -n "coverage-lens" memory/HYGIENE.md` run, each names its key, refusal or kind, and each render
  matches its template.
  Red when: a surface is undocumented.

## 7. Gates

`spec tokens (a spec's own names resolve)` · `spec-tokens self-test` · `build-index selftest` · `memory hygiene` · `memory-hygiene self-test` · `marker contracts` · `tier2-review self-test` · `unattended-build self-test` · `workflow script syntax` · `unattended kit gate` · `pass-order history` · `policy check` · `policy fixtures` · `kit/dogfood doc parity` · `recall floor` · `recall floor arms` · `verifier fan-out self-test` · `review-join self-test`

New arm: tools/check-spec-tokens.test.sh · covers AC1 AC2 AC5 AC8 · the fixture chain repository with a stale pin, an amended clause and an `implements=` carrier under each `design.coverage` value, staged by the join ignoring the key · none

New arm: tools/memory-tree/gen_build_index.py · covers AC3 AC4 AC11 AC12 · `--check-coverage` and `--design-exit` over the same fixture, staged by a dropped clause passing under `refuse` · none

New arm: tools/unattended/unattended.test.sh · covers AC6 AC7 · `--phase BUILDING` and `--dispatch` over a fixture run with an uncarried clause, staged by `check_design_exit` admitting under `refuse` · none

New arm: tools/workflows/tier2-review.test.sh · covers AC9 · the `coverage` argument's three values and the `coverage-lens` binding, staged by the lens running under `skip` · none

New arm: tools/workflows/unattended-build.test.sh · covers AC9 · `coverageSemantic` under each value, staged by `every-exit` with no `specAudit` scheduling no `only` review · none

New arm: tools/workflows/tier2-review.js · covers AC10 · a live `coverage: 'only'` run over the planted contradicting carrier and its twin, staged by the twin pair itself · none

## 8. Open questions

- **F1 — Does `warn` print `UNCARRIED` from `design.ready`?** Options: (a) only under `refuse`; (b) under
  `refuse` and `warn`. v2:1290 answers it: under `warn` a stale or dropped carrier "warns with an ask"
  rather than refusing the exit, and flow-steps:246 counts `UNCARRIED` as not ready "under
  `design.coverage`", so (b) would refuse at the hand-off what the key says to admit. Rung 1. RESOLVED
  (agent, 2026-10-28, delegated): (a). widens: none · relaxes: none
- **F2 — How is the lens's run at a Design exit recorded, and does the exit refuse without it?** Options:
  (a) a `coverage-lens` record for an `only` run and `coverage=with` on an audit's shape line, read by
  the exit under the key's disposition; (b) the lens's findings only, folded through M4's disposal,
  the exit reading nothing; (c) an `only` run written as a `spec-audit` record. (b) leaves `every-exit`
  a claim no gate can see, the gate rule's case; (c) makes a one-lens reading count as an audit for
  `ready-plus-audit` and the audited-ids region. (a) is the only one whose absence is observable
  (AC11). Rung 3, the most feature-rich survivor. RESOLVED (agent, 2026-10-28, delegated): (a). widens:
  none · relaxes: none
- **F3 — The surfaces are governance carriers and a kit edge.** `UNATTENDED-VERBS.md`, `HYGIENE.md` and a
  new record kind are carriers (BUILD-METHOD M11), and `requires = [... "policy"]` changes what the
  unattended kit installs. Options: (a) make them under the README's grant, the clause naming the policy
  read at each Design exit and the lens's reading; (b) read no policy in the driver and leave the
  refusals undocumented. (b) fails AC7 and AC14. Rung 3 with veto 2 lifted by the grant. RESOLVED
  (agent, 2026-10-28, delegated): (a). grants: PLAY-dClosedLoop-3 the `coverage-lens` record kind, the
  coverage refusal in the verbs guide, and the unattended kit's `policy` requirement. widens: none ·
  relaxes: none
- **FACT-QUESTION · F4 — Is the shared reader's proposed subprocess form a second copy of an adapter a
  parent already specs?** Probe: `git grep -n "memory-tree/policy_value.py" -- memory/builds/*/spec`.
  Observation that decides: a parent spec creating the adapter. Liveness: the probe prints nothing where
  no spec names the path. Run at writing: TOOL-dTotalRecall-8 S10 creates it, and five dLinkedLibrary and
  dTotalRecall specs read through it. RESOLVED (agent, 2026-10-28, delegated): `read_design_policy`
  delegates to it (S1), the I3 spelling kept so the six consuming specs agree. widens: none · relaxes:
  none

## 9. Revision log

- rev-1 · 2026-10-28 · initial draft, from the packet's Items 16, ask TOOL-dIndexedDesign-18, the
  brief's I3, I4, I5 and I17, scout A row 16 and interfaces 1-4, v2:1290-1291 and flow-steps:246, each
  site re-read at base `57bc3b91`.
- rev-2 · 2026-10-28 · §3 · the Edges block gains the hands-off bullets mirroring the consumes-from edges of TOOL-dIndexedDesign-35, TOOL-dIndexedDesign-36, TOOL-dIndexedDesign-38,
  promoted by the round-1 spec audit of this build; nothing else moved.
- rev-3 · 2026-10-28 · §3 · the Edges block gains the hands-off bullets mirroring the consumes-from
  edges of TOOL-dIndexedDesign-39, TOOL-dIndexedDesign-41 and TOOL-dIndexedDesign-44, promoted by
  the round-1 spec audit of units 31 to 38; nothing else moved.
- rev-4 · 2026-10-28 · §3 · the Edges block gains the hands-off bullets mirroring the consumes-from
  edges of TOOL-dIndexedDesign-48, TOOL-dIndexedDesign-49 and TOOL-dIndexedDesign-50, promoted by the
  round-1 spec audit of units 39 to 46; nothing else moved.

## 10. Reuse audit

The seams extended are the carries join, `scan_carries` and `derive_carries_coverage`
(`tools/check-spec-tokens.py:931`, :1049), read once through `read_carries_coverage`
(`tools/memory-tree/gen_build_index.py:1967`) by every reader here; check 29's `cmd_check_coverage`
(:2911); `render_coverage` (:1796); the driver's `--dispatch` floor (`unattended.sh:13645-13656`) and
`verb_phase` (:6135); `SPEC_LENSES` and the `intensity` check (`tier2-review.template.js:810`, :210-217);
`renderAuditBinding` (:318); `RECORD_KIND_TOKENS` (`tree_lib.py:406`); and TOOL-dTotalRecall-8 S10's
`policy_value.read_policy_value`, so no second policy reader is written. `python
tools/codebase-map/reuse_lookup.py "refuse a build phase move while a clause is carried by no spec"`
ranked `phases` (`unattended.sh`, fan-in 15, the phase vocabulary `verb_phase` checks),
`derive_clause_hash`, `read_chain_clauses` and `read_spec_revisions`; none reads coverage at a phase
move, so `check_design_exit` is new at the seam `verb_phase` and `verb_dispatch` already are. Where
records and source disagree: scout A proposed `read_design_policy` as a subprocess reader with its own
`requires_if` row, and source records a specced memory-tree adapter (F4); scout A's I4 named
`derive_unit_coverage`, which this spec folds into the value as `by_spec` so the region, check 29 and the
exit read one value; check 29's docstring calls INPROGRESS "past the Design exit", which the harness
falsifies (`gen_build_index.py:2958-2962`), as the scout says. The recall query returned scout A's row 16,
TOOL-dTrueNorth-3's exit reading of every arm, and ask PLAY-dClosedLoop-30, the instrument-side twin of
ask -18 in dClosedLoop's backlog, which this unit does not close.

Recall terms used: `python tools/memory-recall/query.py "what refuses the Design exit when a clause is uncarried or a carrier pin is stale" --terms "carries join derive_carries_coverage scan_carries check 29 Design exit uncarried stale as-built view amends lens"`
