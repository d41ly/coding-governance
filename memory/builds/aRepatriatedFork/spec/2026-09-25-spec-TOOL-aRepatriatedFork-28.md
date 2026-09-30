# TOOL-aRepatriatedFork-28 — every suite builds its fixtures at a prefix it derives

**Status:** CLOSED · rev-4 · 2026-10-01 · node a · Tier-2 · base 2143b6d6 · streams tooling · order 14

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-09-25-build-TOOL-aRepatriatedFork-23-prefix-census.md](../build/2026-09-25-build-TOOL-aRepatriatedFork-23-prefix-census.md) | research | TOOL-aRepatriatedFork-23 TOOL-aRepatriatedFork-24 TOOL-aRepatriatedFork-25 TOOL-aRepatriatedFork-26 TOOL-aRepatriatedFork-27 TOOL-aRepatriatedFork-29 TOOL-aRepatriatedFork-30 |
| [2026-09-29-build-TOOL-aRepatriatedFork-28-1-acceptance-ledger.md](../build/2026-09-29-build-TOOL-aRepatriatedFork-28-1-acceptance-ledger.md) | journal | — |
| [2026-09-29-prompt-TOOL-aRepatriatedFork-28-build-brief.md](../prompts/2026-09-29-prompt-TOOL-aRepatriatedFork-28-build-brief.md) | journal | — |
| [2026-09-30-review-TOOL-aRepatriatedFork-23-closing-diff-round1.md](../reviews/2026-09-30-review-TOOL-aRepatriatedFork-23-closing-diff-round1.md) | diff-review | TOOL-aRepatriatedFork-23 TOOL-aRepatriatedFork-24 TOOL-aRepatriatedFork-25 TOOL-aRepatriatedFork-26 TOOL-aRepatriatedFork-27 TOOL-aRepatriatedFork-29 TOOL-aRepatriatedFork-30 TOOL-aRepatriatedFork-44 TOOL-aRepatriatedFork-45 TOOL-aRepatriatedFork-46 TOOL-aRepatriatedFork-47 |

<!-- /gen:spec-records -->

## 1. Goal

Test suites and embedded self-tests hold more than half of the drain: 1253 literals in 69 files. A
fixture that builds its scratch tree at a literal `tools/` is correct only at gov's prefix. Run
from an install at `scripts/`, it builds a layout its own checker was not installed into, which is
why `TOOL-aRepatriatedFork-18`'s execution leg was held. This unit makes every suite build its
fixtures at a prefix variable derived from the kit's own location, and read host-tree files the
same way. The same suite then runs correctly at any install prefix.

## 2. Scope (IN)

- **S1** — Every suite and every embedded self-test derives one prefix variable from its own
  location, using the `derive_self_rel` block `tools/lib/kit-rel.sh` carries for shell and
  `kit_rel()` for Python. Every scratch path it builds is spelled through that variable. This
  covers `*.test.sh`, every `*selftest.py`, and the self-tests embedded in `check-arms.py`,
  `gotchas.py` and `corpus_ids.py`. Observed by AC1, AC3.
- **S2** — A fixture that models a ROOT install on purpose, which today carries a `gov:root-fixture`
  marker, builds it through the same variable set to the empty prefix. Its marker is then empty of
  purpose, and it is struck. Observed by AC2.
- **S3** — A suite that reads a real file of the host tree, such as the leg manifest or a kit
  descriptor, finds it by the same derivation as its checker, never at `$ROOT/tools/…`. Census §2
  counts 45 such lines in withheld suites. Observed by AC1.
- **S4** — Recorded-data fixtures are handled as §8 F1 resolves. The inCMS receipt fixture under
  `tools/govkit/fixtures/` holds 126 literals. Observed by AC4.
- **S5** — Usage headers and comments inside test files follow the spelling rules of
  `TOOL-aRepatriatedFork-25` and `TOOL-aRepatriatedFork-27`. This unit owns those lines because it
  owns the file. Observed by AC1.
- **S6** — Suite by suite, each suite's executed assertion count is unchanged and its floor
  (`SELFTEST_FLOOR` or `FLOOR_ASSERTIONS`) is unchanged. Observed by AC5. Rev-3: one suite's count
  moves by construction. `resolve-python.test.sh` runs one parity arm per inline `derive_self_rel`
  copy, so it gains one arm for each suite that now carries the block.
- **S7** — The ledger rows for these files are lowered, and every kit moved takes its version bump in
  every carrier. Observed by AC6.

## 3. Non-goals (OUT)

- The canonical-copy marker line in a test file, which `TOOL-aRepatriatedFork-27` rewords with its
  lockstep, and the four stranding sites `TOOL-aRepatriatedFork-24` fixed in test files.
- Running any suite at a foreign prefix. `TOOL-aRepatriatedFork-30` is that proof.
- Arming a branch, or raising a floor.

### Edges

- **consumes-from** `TOOL-aRepatriatedFork-23` — the epoch-5 ledger. Epoch 4 counts 179 of these
  literals and misses the 721 fixture loose names, `/`-led host reads and `"tools"` joins.
- **consumes-from** `TOOL-aRepatriatedFork-24` — the four test-file stranding sites, fixed first so
  this unit's derivation lands on lines that already work.
- **consumes-from** `TOOL-aRepatriatedFork-29` — the registry, descriptor and leg-manifest shape
  that govkit's self-test fixtures and the run-gates suites read.
- **hands-off** `TOOL-aRepatriatedFork-30` — suites whose fixtures derive their prefix, which its
  execution proof runs at `scripts/` and a second prefix.

## 4. Design

### Evidence

From the 2026-09-25 prefix census at `2143b6d6` (session scratchpad, not committed). PINNED,
measured 2026-09-25.

- Census §4 lists 179 class-D literals over 27 files. The largest are `unattended/gate-guard.test.sh`
  62, `check-line-length.test.sh` 25 and `lexicon/selftest.py` 22.
- Census §1 counts 154 invisible literals in received tests, and the withheld tests hold most of the
  514 invisible withheld literals. Epoch 2's existence filter drops fixture loose names such as
  `tools/gate-a.sh` (census §1, "What the gate cannot see").
- The ownership rule (the census record's section 7) gives this unit 1253 literals over 69 files: 256 counted
  today, 721 invisible and 276 in files no descriptor resolves. The largest are
  `run-gates/run-selftests.test.sh` 150, the inCMS receipt fixture 126, `run-gates/run-gates.test.sh`
  71, `govkit/selftest.py` 68, `memory-tree/check-arms.py` 66, `unattended/gate-guard.test.sh` 63,
  `runlog/selftest.py` 59, `check-install-prefix.test.sh` 55, `unattended/check-playbook.test.sh` 53
  and `lexicon/selftest.py` 51.
- Arm 1 carries 31 class-D lines under `gov:root-fixture` markers and two waived fixture lines in
  `corpus_ids.py`. Arm 3 marks seven class-D lines in `corpus_ids.py` and `gotchas.py` (census §1).
- The census's closing section cites the ledger reason for `check-pass-order.test.sh`: a sweep that
  rewrote fixture values broke 14 of 19 arms. S1 derives the PREFIX and keeps each fixture's
  kit-relative layout, which is the difference between a repath and a rewrite.

### Ownership rule

This unit owns every literal in a test or self-test file, in a fixture file or fixture record, and in
the three engine files whose self-test is embedded, except the marker lines and stranding sites §3
names. The rule is `TOOL-aRepatriatedFork-23` §8 F3's.

### Rollout

Suite by suite, one commit per kit, in the order the build's runbook lists the kits. Each commit
records the suite's assertion count before and after in the acceptance ledger. A suite whose count
moves is red and is fixed before the next kit starts.

### Files touched (estimate)

The 69 files the census record's section 7 lists for this unit, under `tools/run-gates/`, `tools/govkit/`,
`tools/memory-tree/`, `tools/unattended/`, `tools/runlog/`, `tools/lexicon/`, `tools/workflows/`,
`tools/codebase-map/`, `tools/hooks/`, `tools/memory-recall/`, `tools/drift-audit/`,
`tools/process-monitor/`, `tools/pytest-parallel-guardrails/`, `tools/lib/`,
`skills/session-kickoff/` and `.githooks/`, plus the loose suites under `tools/` ·
`tools/install-prefix-waivers.txt` · `tools/install-prefix-carried.txt`

### The spelling (rev-3)

- **One variable, `PFX`, carrying its trailing slash and empty at a root install.** A shell suite
  derives it through the inline `derive_self_rel` block: a kit suite takes the parent of its
  `KIT_REL`, a loose suite takes `KIT_REL` itself. A Python self-test carries an inline
  `derive_install_prefix()`; an engine whose self-test is embedded binds it inside that self-test
  only, so the engine's import never walks for a `.git`. A suite whose `KIT_REL` already meant the
  tool root keeps that meaning, now derived. A quoted heredoc takes a `{PFX}` placeholder and one
  `sed` after it, because a quoted heredoc cannot expand a variable, which is how the earlier sweep
  of `check-pass-order.test.sh` broke 14 arms.
- **The two `.githooks` suites read `GOV_KITROOT` from `.githooks/gate-env.sh`**, the value the
  hooks under test read, since nothing about a hook's location says where the kits are. The
  session-kickoff suite's `tools/` was never a prefix: it is a fixture adopter's watched directory,
  renamed to `vendor/`.
- **A root-install fixture spells its paths through a prefix variable set empty** (`ROOTPFX`,
  `root_pfx`, `ROOT_PFX`), per S2. Each marker is struck, and the two `corpus_ids.py` waiver rows go
  with them.
- **govkit's scratch-gov fixtures move to `TOOL-aRepatriatedFork-29`'s spelling**: `{prefix}`
  registry paths and kit-relative homes. The old `home = "tools/demo"` loaded as
  `tools/tools/demo` after that unit, which redded both of `check_shipped_verb`'s arms and five of
  `check_epoch_verb`'s. A fixture target's own `prefix = …` follows `PFX` too, so a target's
  declaration and the paths asserted in it cannot disagree. The two intake arms that assert the
  ENGINE's default keep the engine's value.
- **F1 is `{prefix}`**, substituted by the reading arm on load. The generator derives the recorded
  revision's tool root from that revision's own tree, since a recorded layout does not move with
  this checkout, and emits the token.

### Returned (rev-3)

Classes this unit's mechanism cannot drain, each named for its owner:

- A literal kit segment joined under an already-derived base (`$KIT_REL/hooks/…`,
  `root / PFX / "lexicon"`): `TOOL-aRepatriatedFork-46`.
- A fixture that models an adopter at a FOREIGN literal prefix on purpose (`scripts/`, `kit/`,
  `vendor/gov/`): spelled through the derived prefix it would stop being foreign.
  `TOOL-aRepatriatedFork-30`'s population rule.
- A kit id used as an argv or list value that the epoch-5 counter reads as a join
  (`"--kits", "memory-tree"`): `TOOL-aRepatriatedFork-30`.
- The unattended kit's rendered fixture playbook and piece records. `adopt-unattended.sh` renders
  them and `check-playbook.sh` reads their paths literally, so draining them is a leg change:
  `TOOL-aRepatriatedFork-30`.
- `check-install-prefix.test.sh`'s `"tools"`-join red fixtures, which exercise the ban's own literal
  predicate: `TOOL-aRepatriatedFork-30` rewrites that predicate.

### Alternatives rejected

- Exempting fixture-internal literals as correct at every prefix, which census §6 recommended. The
  owner ruled it out on 2026-09-25, and a fixture built at a literal prefix is exactly what cannot
  run at another one.

## 5. Production-readiness checklist

- security — none; test code.
- perf / scale — none per suite. The main loop's re-observation of every suite costs hours; the
  unattended suites alone are about 2.5 h pooled on node a, so they run once, early, on a frozen
  clone.
- error / empty / loading states — an underivable prefix refuses in the suite's prologue rather than
  building at the root by accident.
- observability — none added (rev-3). A printed prefix line was planned beside each suite's count,
  but that count line is parsed by the testsuite-counts leg and the arm extractor, so a new line in
  sixty suites is an output-contract change for no gain at gov's prefix.
- risks — a fixture whose layout silently changes, passing arms that no longer exercise their
  subject. S6's unchanged count is the guard, and AC3's control is the check on it.
- testing — this unit is testing.
- migration — none.
- user docs — none.

## 6. Acceptance criteria

- **AC1** — When `git grep -nE '(^|[^<{A-Za-z0-9_.-])tools/' -- '*.test.sh' '*selftest.py'` runs,
  together with the same pattern over this unit's other owned files, it finds no line outside
  fixture data that §8 F1 keeps. Rev-3: the unattended kit's rendered fixture playbook and its two
  rendered piece records are not owned files here (§4, "Returned").
  Red when: a literal prefix survives in an owned file.
- **AC2** — When `git grep -l 'gov:root-fixture' -- tools skills .githooks` runs, it lists only the
  install-prefix gate and its own suite, which grade the marker until `TOOL-aRepatriatedFork-30`
  deletes it. Each root-install arm builds its fixture with the prefix variable empty.
  Red when: a marker remains, or a root-install arm stops building a root layout.
- **AC3** — Red-first control: in one suite chosen per kit, the variable `derive_self_rel` sets is pinned
  to a wrong prefix in a scratch clone, and that suite reds rather than passing on a layout it never built.
  Staged, recorded and discarded.
  Red when: the suite passes with a wrong prefix, so the derivation is decorative.
- **AC4** — When the receipt fixture is loaded by govkit's self-test in a clone whose kits sit at
  `scripts/`, the arms reading it see destinations under `scripts/`.
  Red when: a loaded row names `tools/`.
- **AC5** — When `git diff 2143b6d6 -G '^(SELFTEST_FLOOR|FLOOR_ASSERTIONS)=' -- tools skills
  .githooks` runs, it shows no floor lowered, and the acceptance ledger records every suite's
  executed count at `2143b6d6` and after, equal.
  Red when: a floor falls, or a count differs.
  permission: a unit pass runs no suite; the main loop runs each suite at gov's prefix and records
  its count.
  figure: PINNED per suite at `2143b6d6`, DERIVED after.
- **AC6** — `bash tools/check-kit-versions.sh` exits 0, and `python tools/govkit/govkit.py epoch
  --base 2143b6d6` names no kit this unit moved.
  Red when: a moved kit's carrier was missed.

## 7. Gates

`install-prefix (shipped surface)` · `install-prefix self-test` · `testsuite counts (every bar self-test prints one)` · `harness arms (fail branches armed or pinned)` · `kit version markers` · `kit epoch (shipped bytes move, the version moves)` · `govkit selfcheck` · `govkit selftest` · `lexicon naming predicates` · `manifest-check self-test` · `agent-cap self-test` · `scratch-guard self-test` · `row-keyed merge driver replay` · `pre-push run-log line` · `verifier fan-out self-test` · `tier2-review self-test` · `unattended-build self-test` · `review-join self-test` · `pytest-guardrails self-test` · `codebase-map kit selftest` · `codebase-map gate coverage` · `codebase-map adopter e2e` · `memory-recall kit selftest` · `recall floor` · `recall floor arms` · `drift-audit selftest` · `process-monitor census selftest` · `process-monitor adopter selftest` · `runlog selftest` · `run-gates run-log line` · `hook destinations self-test` · `lexicon selftest` · `govkit refusal join` · `govkit acceptance matrix` · `selftest harness self-test` · `extract-arms self-test` · `run-selftests self-test`

New arm: every suite this unit edits · its own arms, now built at a derived prefix · each floor
unchanged

## 8. Open questions

- **F1 — what happens to recorded real-world fixtures?** The inCMS receipt fixture is a real
  adopter's receipt, committed so arms grade a population nobody authored. Option (a): regenerate it
  from `make_incms_receipt.py` at test time with the derived prefix. That needs the inCMS tree it
  was cut from, so it is not reproducible here. Option (b): keep the recorded bytes, and have the
  reading arms translate gov's recorded prefix to the derived one on load, through one declared
  mapping. Option (c): re-record the fixture once with a prefix token in place of gov's prefix, and
  substitute the token on load. Recommendation: (c). The data stays real, the fixture carries no
  literal, and (b) keeps a literal in the tree.
  RESOLVED (owner, 2026-09-25): (c), the recommendation.

## 9. Revision log

- rev-1 · 2026-09-25 · initial draft. Owner rulings of 2026-09-25: "Drain everything, fixtures too",
  before `TOOL-aRepatriatedFork-18`'s held leg. Every suite's fixture builds its scratch tree at a
  prefix variable derived from the kit's own location. The proposed split listed the `corpus_ids.py`
  and `gotchas.py` fixtures under `TOOL-aRepatriatedFork-29`; census §1 classes them D, and this
  unit's mechanism drains them.
- rev-2 · 2026-09-25 · §8 resolved by the owner: every fork takes its recommendation.
- rev-3 · 2026-09-30 · before code, from the unit pass. §4 gains "The spelling" and "Returned":
  the `PFX` variable and where each file class takes it, the empty-prefix spelling S2 names, the
  move of govkit's fixtures to `TOOL-aRepatriatedFork-29`'s spelling that unit's change made
  necessary, and five classes this mechanism cannot drain, each named for its owner. AC1 no longer
  counts the unattended kit's rendered fixture files. S6 names the one suite whose count moves by
  construction. §5 drops the printed-prefix line.
- rev-4 · 2026-10-01 · gate repair at VERIFYING, legs `scratch-guard self-test`, `codebase-map kit
  selftest` and `govkit selftest`, and the foreign-prefix calibrate's `unattended gate-guard
  selftest` row. Three defects of this unit's derivation. The meta-arms of `scratch-guard.test.sh`
  and `gate-guard.test.sh` copy the suite to `$TMP`, where `derive_self_rel` finds no repository
  and the copy exits before the liveness guard can fire; the copy's `HERE` is pinned to the suite's
  own. codebase-map's `derive_install_prefix` spelled `Path(__file__).resolve()`, which the kit's
  own B2 arm bans; it takes `os.path.abspath`. govkit's pre-fix arms (`-14` AC8, `-24` AC5, `-26`
  AC1 and AC4) run an engine read out of git inside a copy of a fixture gov this unit moved to the
  `{prefix}` spelling. That engine predates the token and refused every entry as a missing
  descriptor, so the arms graded a refusal. The pre-fix copy is re-spelled the way that engine
  reads, by `write_pre_fix_spelling`; every expectation stays.

## 10. Reuse audit

`python tools/codebase-map/reuse_lookup.py "fixture builds a scratch tree at a prefix"` ranked
`tree` in `tools/memory-recall/selftest.py` and `build_reference_index`, neither of which derives a
prefix. The seams reused are `derive_self_rel` in `tools/lib/kit-rel.sh`, which
`TOOL-aRepatriatedFork-18` S2 made the canonical inline block for exactly this, and `kit_rel()` in
`tools/codebase-map/map_lib.py` and `tools/memory-tree/tree_lib.py`.

Recall terms used: `fixture prefix derive_self_rel KIT_REL root-fixture scratch tree suite floor
assertion count withheld repath`.
