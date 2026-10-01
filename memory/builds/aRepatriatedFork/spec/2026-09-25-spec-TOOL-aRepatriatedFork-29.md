# TOOL-aRepatriatedFork-29 — gov's own gates and declarations derive the prefix they name

**Status:** CLOSED · rev-6 · 2026-10-01 · node a · Tier-2 · base 2143b6d6 · streams tooling · order 13

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-09-25-build-TOOL-aRepatriatedFork-23-prefix-census.md](../build/2026-09-25-build-TOOL-aRepatriatedFork-23-prefix-census.md) | research | TOOL-aRepatriatedFork-23 TOOL-aRepatriatedFork-24 TOOL-aRepatriatedFork-25 TOOL-aRepatriatedFork-26 TOOL-aRepatriatedFork-27 TOOL-aRepatriatedFork-28 TOOL-aRepatriatedFork-30 |
| [2026-09-29-build-TOOL-aRepatriatedFork-29-1-acceptance-ledger.md](../build/2026-09-29-build-TOOL-aRepatriatedFork-29-1-acceptance-ledger.md) | journal | — |
| [2026-09-30-build-TOOL-aRepatriatedFork-23-closing-fold-round1.md](../build/2026-09-30-build-TOOL-aRepatriatedFork-23-closing-fold-round1.md) | journal | TOOL-aRepatriatedFork-23 TOOL-aRepatriatedFork-24 TOOL-aRepatriatedFork-30 TOOL-aRepatriatedFork-46 |
| [2026-09-29-prompt-TOOL-aRepatriatedFork-29-build-brief.md](../prompts/2026-09-29-prompt-TOOL-aRepatriatedFork-29-build-brief.md) | journal | — |
| [2026-09-30-review-TOOL-aRepatriatedFork-23-closing-diff-round1.md](../reviews/2026-09-30-review-TOOL-aRepatriatedFork-23-closing-diff-round1.md) | diff-review | TOOL-aRepatriatedFork-23 TOOL-aRepatriatedFork-24 TOOL-aRepatriatedFork-25 TOOL-aRepatriatedFork-26 TOOL-aRepatriatedFork-27 TOOL-aRepatriatedFork-28 TOOL-aRepatriatedFork-30 TOOL-aRepatriatedFork-44 TOOL-aRepatriatedFork-45 TOOL-aRepatriatedFork-46 TOOL-aRepatriatedFork-47 |
| [2026-09-30-review-TOOL-aRepatriatedFork-23-closing-diff-round2.md](../reviews/2026-09-30-review-TOOL-aRepatriatedFork-23-closing-diff-round2.md) | diff-review | TOOL-aRepatriatedFork-23 TOOL-aRepatriatedFork-24 TOOL-aRepatriatedFork-30 TOOL-aRepatriatedFork-46 |

<!-- /gen:spec-records -->

## 1. Goal

Gov's own registries, leg manifest, version gate, sidecars and gov-internal libraries spell `tools/`
740 times. The census called these correct as literals, because they name gov's checkout. The
owner ruled on 2026-09-25 that they are drained too: a declaration stays a declaration, but it
names its members kit-relatively, and the prefix they sit under is derived. This unit does that for
every gov-side file, so gov itself runs at any kit root.

## 2. Scope (IN)

- **S1** — `tools/govkit/registry.toml` and every kit descriptor name their members relative to the
  tool root. The tool root is derived from the registry's own location, one directory above
  govkit's. A descriptor's `home` key is spelled as §8 F2 resolves. `govkit.py` resolves every such
  name through that one root, and its own 35 literals go through it too. Observed by AC1, AC2.
- **S2** — Gov's leg manifest `tools/gate-legs.json` names no prefix in an argv; each leg resolves as
  §8 F1 resolves. Observed by AC3.
- **S3** — Gov's own gates derive where their subjects sit. `check-kit-versions.sh` keeps its
  declared carrier population, spelled kit-relatively and joined to a root derived from its own
  location. `check-install-prefix.sh`'s kit-source test derives the registry and resolver paths
  from `SELF_PREFIX`. The same holds for `check-dead-paths.sh`, `check-spec-tokens.py`,
  `check-playbook-parity.sh`, `check-hook-destinations.sh`, `check-template-size.sh` and
  `check-kit-placeholders.py`. Observed by AC4.
- **S4** — Data sidecars that name gov paths as rows name them relative to the tool root, and their
  readers join the derived root. They are `selftest-budgets.txt`, `ceiling-evidence.txt`,
  `dead-path-waivers.txt`, `subject-pins.tsv`, `template-size-limits.txt`, `line-length-limits.txt`,
  `playbook-kit-waivers.txt`, `recall-fixture.json` and the rank harness's `scen-adversarial.json`.
  Observed by AC5.
- **S5** — `render_playbook.py` derives `gov_root`'s descriptor and registry fallbacks from its own
  location (`:384-385`). Its bar-command heuristic at `:204` probes candidates under the target's
  derived kit root rather than a fixed `tools`/`scripts` list. Observed by AC6.
- **S6** — The withheld engine files, which are `map_extractors.py`, `drift_signals.py`, the runlog
  and run-gates sidecars, and gov-internal `tools/lib/` scripts (`pyrun.sh`, `extract-arms.sh`,
  `lib-selftest.sh`, `resolve_kit_dir.py`), derive from their own location. Gov's four renders of
  shipped workflow templates are handled as §8 F3 resolves. Observed by AC7.
- **S7** — The ledger rows for these files are lowered, and every kit moved takes its version bump in
  every carrier. Observed by AC8.
- **S8 (rev-4)** — The closing review's round-1 fold of four readers S1 and S2's `{prefix}`
  spelling left unmigrated.
  - **S8a** — H2. The run-gates canary's arm 1b resolves each guard through the inlined
    `resolve_prefix_token` block against the kit's parent before the tracked-path test. Observed by
    AC9.
  - **S8b** — M2. Its arm 2 resolves each leg path the same way before grepping the runner, and a
    new assertion requires every path in that population to name a tracked path, so an arm whose
    needles name nothing reds instead of reporting ok. The suite floor rises by one. Observed by
    AC10.
  - **S8c** — M1. `derive_gate_runner` reads the TOP-LEVEL `prefix` from the target's
    `.governance/deploy.toml` when `[answers]` carries none, which is where `govkit intake` writes
    it, so the flat `run-gates.sh` and `gate.sh` rungs are reachable again. Observed by AC11.
  - **S8d** — L2. `make_adopter_receipt.py`'s `resolve_kit_homes` resolves each descriptor's token
    against the revision's own tool root, joins a tokened descriptor's kit-relative home to it
    unless the descriptor declares `home_root_relative`, and refuses a descriptor that reads empty.
    Observed by AC12.

## 3. Non-goals (OUT)

- Test files and fixtures anywhere, govkit's own self-test and its receipt fixture included.
  `TOOL-aRepatriatedFork-28` owns them.
- The waiver registry `install-prefix-waivers.txt`, which `TOOL-aRepatriatedFork-30` deletes.
- Kit-relative member names. They stay literal, which is what keeps a declaration a declaration.

### Edges

- **consumes-from** `TOOL-aRepatriatedFork-23` — the epoch-5 ledger, whose population is the first
  to include the 57 files no descriptor resolves.
- **hands-off** `TOOL-aRepatriatedFork-28` — the registry, descriptor and leg-manifest shape that
  govkit's self-test fixtures and the run-gates suites read. They are re-derived against this
  unit's output, which is why 28 follows 29.
- **hands-off** `TOOL-aRepatriatedFork-30` — the pure ban's population rule for gov's own renders,
  if §8 F3 resolves to (a).

## 4. Design

### Evidence

From the 2026-09-25 prefix census at `2143b6d6` (session scratchpad, not committed). PINNED,
measured 2026-09-25.

- Census §4 lists 362 class-F literals over 16 files: `scen-adversarial.json` 201,
  `govkit/registry.toml` 74, `check-kit-versions.sh` 33, `selftest-budgets.txt` 27, and 27 more
  across twelve files.
- Census §1 found 57 tracked files no descriptor resolves, holding 562 literals under the arm-2
  predicate (the census record). 51 are covered by a registry exemption.
- The ownership rule (the census record's section 7) gives this unit 740 literals over 61 files: 368 counted
  today, 100 invisible and 272 in unresolved files. The largest are `scen-adversarial.json` 202,
  `gate-legs.json` 137, `registry.toml` 100, `check-kit-versions.sh` 41, `govkit.py` 35,
  `selftest-budgets.txt` 27, `check-install-prefix.sh` 13 and `map_extractors.py` 13.
- Arm 3 marks five class-F lines: `check-install-prefix.sh:100, 102, 155` and
  `render_playbook.py:384, 385` (census §1, arm-3 table).
- `render_playbook.py:204` is the census's invisible fallback rung. Its candidates name
  adopter-owned gate scripts (census §2).
- Descriptors already render adopter legs from `{kit}` tokens, as in `tools/memory-tree/kit.toml`'s
  `[[gate_leg]]` rows. Gov's own `tools/gate-legs.json` holds no token.

### Ownership rule

This unit owns every literal in a gov-side file: a withheld file that is not a test, a file no
descriptor resolves that is not a test, a kit descriptor, and the registry. A `sentinel =` line is
`TOOL-aRepatriatedFork-24`'s. The rule is `TOOL-aRepatriatedFork-23` §8 F3's.

### Rev-3 decisions, made by the unit pass before code

Measured at `e3d91e32` with the gate's epoch-5 counter, run per line, because five drain units moved
the tree after the census.

- **The registry and the descriptors spell a gov-side path through the `{prefix}` token.** That
  covers an entry's `descriptor`, an exemption's `path`, a surface glob, a gov-only pin's `pattern`,
  a `root_relative` include and a `claims` row. S1 said "relative to the tool root", but the ban
  counts a bare `<kit>/<file>` wherever it sits, so the kit-relative spelling is itself a literal.
  The token is the one the descriptors already use for a destination. A `home` stays kit-relative,
  as §8 F2 resolves, and a flat entry's home is `.`, the tool root itself.
- **One home sits outside the tool root.** The kickoff entry's engine lives under `skills/`, which
  machine-junction discovery fixes, so that descriptor carries `home_root_relative = true` and its
  home keeps its repo-root spelling.
- **govkit joins these paths once, at load.** `load_registry` and `resolve_descriptor_paths` join
  every token and home to the root `derive_tool_root` derives, so each reader downstream keeps the
  repo-relative spelling it always had. The tool root is govkit's grandparent, and the checkout root
  is the first directory above it holding a `.git` entry.
- **§8 F1 reaches every reader of the manifest's argv and guards, not the runner alone.** These are
  `run-gates.sh`, `run-selftests.sh` with its budget and pooled-evidence sidecars,
  `check-testsuite-counts.sh`, `check-spec-tokens.py` and govkit's guard-class arm. The runbook's
  harness-migration program reads the registry and descriptors raw, so its reader learns the new
  shape too. The literal registry path on its read line is `TOOL-aRepatriatedFork-46`'s.
- **§8 F3's population rule is `TOOL-aRepatriatedFork-30`'s to build**, as the Edges hand-off says.
  AC7's render clause is observed there, and the rows for `unattended-build.js` and
  `drift-audit-state.js` stay until then.
- **Lines left to their owners.** Three executing lines join a literal kit segment under a derived
  base, and they belong to `TOOL-aRepatriatedFork-46`: govkit's runner probe, and the workflows and
  lexicon joins in `map_extractors.py`. Four text cells in `dead-path-waivers.txt` must match lines of
  the frozen adopter-receipt fixture byte for byte, so they drain only with that fixture, which is
  `TOOL-aRepatriatedFork-28`'s. The same unit owns the selftest fixture strings in
  `render_playbook.py` and the whole of `govkit/matrix.py`, the acceptance-matrix harness.
- **The install-prefix gate's own predicate still reads gov's literal prefix**, in arm 3 and in the
  counter. That is the definition of the class it bans, which is `TOOL-aRepatriatedFork-30`'s to
  change. Only the kit-source test moved to `SELF_PREFIX`, as S3 says.

### Files touched (estimate)

`tools/govkit/registry.toml` · `tools/govkit/govkit.py` · `tools/gate-legs.json` ·
`tools/run-gates/run-gates.sh` · `tools/check-kit-versions.sh` · `tools/check-install-prefix.sh` ·
`tools/check-dead-paths.sh` · `tools/check-spec-tokens.py` · `tools/check-playbook-parity.sh` ·
`tools/check-hook-destinations.sh` · `tools/check-template-size.sh` ·
`tools/check-kit-placeholders.py` · `tools/playbook/render_playbook.py` ·
`tools/codebase-map/map_extractors.py` · `tools/codebase-map/scen-adversarial.json` ·
`tools/drift-audit/drift_signals.py` · `tools/run-gates/selftest-budgets.txt` ·
`tools/lib/pyrun.sh` · `tools/lib/extract-arms.sh` · every `kit.toml` descriptor under `tools/` ·
`tools/install-prefix-carried.txt` · (rev-3) `tools/run-gates/run-selftests.sh` ·
`tools/run-gates/selftest-pooled-evidence.txt` · `tools/run-gates/derive-ceilings.py` ·
`tools/run-gates/ceiling-evidence.txt` · `tools/check-testsuite-counts.sh` ·
`tools/codebase-map/rank_harness.py` · `tools/govkit/check_runbook_parity.py` ·
`tools/govkit/refusal_join.py` · `tools/govkit/subject-pins.tsv` · `tools/dead-path-waivers.txt` ·
`WIRE-INTO-PROJECT.md` · every carrier of the thirteen kit versions this unit moves

### Alternatives rejected

- Keeping gov-side literals under a per-file exemption, which census §6 recommended. The owner
  ruled it out on 2026-09-25.
- Deriving a declaration's members by globbing. `check-kit-versions.sh`'s ledger reason already
  says why: a carrier that forgets its constant then vanishes from its own check.

## 5. Production-readiness checklist

- security — `govkit.py` resolves every destination through its containment guard; S1 changes the
  root it joins, not the guard, and AC2 observes a `..` member still refused.
- perf / scale — one root derivation per process.
- error / empty / loading states — an underivable tool root refuses, as `check-install-prefix.sh`
  already does for its own sidecars.
- observability — each gate prints the root it derived where it already prints its population.
- risks — this is a shared-contract change: every descriptor and every govkit verb reads S1's form.
  The govkit acceptance matrix and refusal join are its gates.
- testing — govkit's self-test runs at `scripts/` in a scratch clone (AC1). The main loop runs the
  suites after `TOOL-aRepatriatedFork-28` has re-derived their fixtures.
- migration — an adopter's receipt names destinations, not gov's `home` keys, so no receipt
  migrates. AC2 observes an update over an existing receipt.
- user docs — `WIRE-INTO-PROJECT.md`'s descriptor section, `TOOL-aRepatriatedFork-26`'s file.

## 6. Acceptance criteria

- **AC1** — When gov's tree is cloned and its `tools/` renamed to `scripts/`, govkit's `selfcheck`
  verb, run from the renamed directory, exits 0 in the clone.
  Red when: any govkit verb resolves a member at `tools/`.
  cost: a scratch clone; seconds.
- **AC2** — When `govkit.py update` runs from that clone against a fixture adopter whose receipt was
  written from `2143b6d6`, it reports no row as moved by this change, and a descriptor member
  spelled with `..` is still refused.
  Red when: a receipt row reads as moved, or the containment guard admits the member.
- **AC3** — When the runner's argv resolution is applied in that clone to every leg of
  `tools/gate-legs.json`, each argv names an existing file under `scripts/`.
  Red when: an argv names `tools/`.
- **AC4** — When `check-kit-versions.sh` runs from the renamed directory in that clone, it exits 0
  and reports the same carrier count as at gov's prefix.
  Red when: a carrier is missed at the new root, or the count changes.
- **AC5** — Red-first control: `check-kit-versions.sh` in the same clone at `2143b6d6` exits non-zero
  naming a `tools/` carrier. Recorded in the acceptance ledger.
  Red when: the old gate already passes at `scripts/`, so AC4 proves nothing.
- **AC6** — When `render_playbook.py` renders a fixture target whose bar sits under
  `vendor/gov/run-gates/`, the rendered bar command names that path.
  Red when: it names a `tools/` or `scripts/` candidate.
- **AC7** — When `bash tools/check-install-prefix.sh --list` runs, no ledger row remains for any file
  this unit owns, the four renders included once §8 F3 is applied.
  Red when: an owned file keeps a row.
  figure: DERIVED at observation time.
- **AC8** — `bash tools/check-kit-versions.sh` exits 0, and `python tools/govkit/govkit.py epoch
  --base 2143b6d6` names no kit this unit moved.
  Red when: a moved kit's carrier was missed.
- **AC9** — rev-4. A slice of `tools/run-gates/run-gates.test.sh` over arm 1b passes on the real
  manifest, and fails naming the guard when a manifest copy passed as `GATE_LEGS` adds a guard
  under the `{prefix}` token that names no tracked path.
  Red when: the arm reports 114 bad guards on the real manifest, the `7de665e5` behaviour.
- **AC10** — rev-4. The same slice over arm 2 passes, fails when a copy of `run-gates.sh` carrying a
  resolved leg path is graded, and fails its new liveness assertion when the resolution is removed.
  Red when: the arm stays green over unresolved `{prefix}/…` needles.
- **AC11** — rev-4. A `render_playbook.py --selftest` arm renders `bash scripts/gate.sh`,
  `bash scripts/run-gates.sh` and `bash tools/run-gates.sh` for targets whose `deploy.toml`
  declares the prefix at its top level.
  Red when: any renders empty, which `7de665e5` does for all three.
- **AC12** — rev-4. A `tools/govkit/selftest.py` arm asserts `resolve_kit_homes` yields a home for
  every registry entry at the pinned revision, each a directory that revision tracks files under.
  Red when: the map is empty, as it is at `7de665e5`.

## 7. Gates

`install-prefix (shipped surface)` · `install-prefix self-test` · `kit version markers` · `kit epoch (shipped bytes move, the version moves)` · `govkit selfcheck` · `govkit selftest` · `govkit refusal join` · `govkit acceptance matrix` · `govkit runbook parity` · `run-gates canary` · `run-gates gov canary` · `every held leg is budgeted, every budget row resolves` · `leg ceilings clear their evidenced maximum` · `dead-path carriers (deleted files still named)` · `spec tokens (a spec's own names resolve)` · `playbook parity` · `hook destinations (every declared hook path ships)` · `template size <=48KiB` · `kit placeholders (a declared token its adopter substitutes)` · `playbook render selftest` · `lexicon naming predicates` · `playbook parity selftest` · `codebase-map kit selftest` · `codebase-map gate coverage` · `codebase-map adopter e2e` · `recall floor arms` · `drift-audit selftest` · `hook destinations self-test` · `extract-arms self-test` · `run-selftests self-test`

New arm: `tools/govkit/selftest.py` · a registry and descriptors at a `scripts/` root, which the
`2143b6d6` resolver misreads · none

New arm: `tools/run-gates/run-gates.test.sh` · rev-4: arm 2's population must name tracked paths · the floor rises by one

New arm: `tools/playbook/render_playbook.py` · rev-4: flat runners under a top-level deploy prefix · none

New arm: `tools/govkit/selftest.py` · rev-4: the fixture regenerator derives a tracked home for every registry entry · none

## 8. Open questions

- **F1 — how does a leg in gov's own manifest name its program?** Option (a): each argv carries a
  `{prefix}` token that the runner resolves against the kit root it already derives, the way
  descriptors carry `{kit}`. Option (b): gov renders its manifest from the descriptors'
  `[[gate_leg]]` rows with the adopter renderer, plus a gov-side source for gov-only legs. That is
  a generated artifact and a parity gate. Option (c): each argv is relative to the manifest's own
  directory, and the runner sets that directory as the working directory. That breaks every leg
  that expects the repo root. Recommendation: (a). It is one resolution rule in one runner, and it
  matches the token grammar the descriptors already use.
  RESOLVED (owner, 2026-09-25): (a), the recommendation.
- **F2 — what does a descriptor's `home` key hold?** Option (a): a kit-relative name, resolved
  against the derived tool root. This works for kit descriptors and for the flat entries under
  `tools/govkit/entries/`, whose `home` is the tool root itself. Option (b): no `home` key for a kit
  descriptor, whose home is derived from its own directory, and a kit-relative `home` for flat
  entries only. Recommendation: (a). One rule for both kinds of entry, and the declaration stays
  explicit.
  RESOLVED (owner, 2026-09-25): (a), the recommendation.
- **F3 — what about gov's own renders of shipped templates?** The four `tools/workflows/*.js` files
  gov runs are renders of `{{TOOL_ROOT}}` templates at gov's prefix, so they must carry a concrete
  path. Option (a): the pure ban's population leaves out a tracked file that re-renders
  byte-identically from its declared template. That rule is structural and is checked by
  re-rendering, not declared by a marker. Option (b): gov stops tracking the renders and renders them
  at run time. Every Workflow caller of those paths then needs a render step first. Option (c): the
  renders carry a relative path from the repo root that the Workflow runtime resolves; it does not
  resolve one today. Recommendation: (a). A render at gov's prefix is the "rendered at deploy
  time" form the owner's ruling allows, and re-rendering proves it is one.
  RESOLVED (owner, 2026-09-25): (a), the recommendation.

## 9. Revision log

- rev-1 · 2026-09-25 · initial draft. Owner rulings of 2026-09-25: drain every hard-coded kit
  prefix, gov-side files included, before `TOOL-aRepatriatedFork-18`'s held leg. A declaration stays
  a declaration: derive the prefix and keep the kit-relative member names. The proposed split
  listed the `corpus_ids.py` and `gotchas.py` fixtures here; census §1 classes them D, and they
  moved to `TOOL-aRepatriatedFork-28`, whose mechanism drains them.
- rev-2 · 2026-09-25 · §8 resolved by the owner: every fork takes its recommendation.
- rev-3 · 2026-09-29 · the unit pass, before code. §4 gains the decisions the build met: the
  `{prefix}` spelling for every gov-side registry and descriptor path, since a kit-relative
  `<kit>/<file>` is itself a counted literal; the one repo-root home and its declaring key; the load
  seam; every argv and guard reader §8 F1 reaches; F3's rule left to `TOOL-aRepatriatedFork-30`;
  and the lines left to other owners. The Files touched list gains what they reach.
- rev-4 · 2026-09-30 · closing review round 1 fold: H2 — the canary's guard arm resolves the
  `{prefix}` token before its tracked-path test (S8a, AC9). closing review round 1 fold: M2 — its
  hardcoded-path arm resolves before grepping and asserts its needles are real paths (S8b, AC10).
  closing review round 1 fold: M1 — the bar deriver reads the deploy prefix where intake writes it
  (S8c, AC11). closing review round 1 fold: L2 — the fixture regenerator reads tokened
  descriptors and joins kit-relative homes (S8d, AC12).
- rev-5 · 2026-10-01 · gate repair at VERIFYING, legs `govkit selftest` and `run-gates run-log line`.
  S1 moved the registry and descriptors to `{prefix}`-tokened, kit-relative spellings, and four
  readers in govkit's selftest still read them raw. The `[gate_runner_seed]` arm joined an
  unresolved `{prefix}` and crashed the suite, leaving every later arm unrun. The `[dBF]` and
  integrity-count arms loaded check-wiring's descriptor without `resolve_descriptor_paths`, so every
  source read `./<file>`. Arm 7e staged its break against the old one-line `default`, matched
  nothing and staged nothing; it now asserts that its edit took. The leg-name arm pinned the
  `tools/gate-legs.json` text the message no longer prints, and takes the new text. run-gates.sh's
  manifest-parse line gained the kit-dir argument, and the run-log suite's EXITS table still named
  the old line; its row takes the new text.
- rev-6 · 2026-10-01 · S3: gate repair at VERIFYING, leg `foreign-prefix parity (every self-test at
  three prefixes)`, row `kit-placeholders self-test`, red at `vendor/gov/`. For a fixture tree handed
  in by `--root`, `check-kit-placeholders.py` searched for `kit.toml` one segment below a single
  root only, so every fixture built at a two-segment prefix was refused as declaring nothing. It
  searches one or two segments deep.

## 10. Reuse audit

`python tools/codebase-map/reuse_lookup.py "registry declares kit homes and exempt paths"` ranked
`kit_rel`, `load_affordance_exempt` and `kit_dir` in `tools/codebase-map/map_lib.py`. `kit_rel` is
the derive-from-own-location seam in Python and S3 and S6 reuse its shape. The shell side reuses
`check-install-prefix.sh`'s `SELF_PREFIX` derivation, which `git -C` makes junction-safe, rather
than writing a new one.

Recall terms used: `registry descriptor home kit-relative gate-legs argv prefix token derive
selfcheck check-kit-versions carrier gov-side`.
