# TOOL-aRepatriatedFork-24 — no line that executes strands an adopter at another prefix

**Status:** CLOSED · rev-5 · 2026-09-30 · node a · Tier-2 · base 2143b6d6 · streams tooling · order 9

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-09-25-build-TOOL-aRepatriatedFork-23-prefix-census.md](../build/2026-09-25-build-TOOL-aRepatriatedFork-23-prefix-census.md) | research | TOOL-aRepatriatedFork-23 TOOL-aRepatriatedFork-25 TOOL-aRepatriatedFork-26 TOOL-aRepatriatedFork-27 TOOL-aRepatriatedFork-28 TOOL-aRepatriatedFork-29 TOOL-aRepatriatedFork-30 |
| [2026-09-29-build-TOOL-aRepatriatedFork-24-1-acceptance-ledger.md](../build/2026-09-29-build-TOOL-aRepatriatedFork-24-1-acceptance-ledger.md) | journal | — |
| [2026-09-30-build-TOOL-aRepatriatedFork-23-closing-fold-round1.md](../build/2026-09-30-build-TOOL-aRepatriatedFork-23-closing-fold-round1.md) | journal | TOOL-aRepatriatedFork-23 TOOL-aRepatriatedFork-29 TOOL-aRepatriatedFork-30 TOOL-aRepatriatedFork-46 |
| [2026-09-29-prompt-TOOL-aRepatriatedFork-24-build-brief.md](../prompts/2026-09-29-prompt-TOOL-aRepatriatedFork-24-build-brief.md) | journal | — |
| [2026-09-30-review-TOOL-aRepatriatedFork-23-closing-diff-round1.md](../reviews/2026-09-30-review-TOOL-aRepatriatedFork-23-closing-diff-round1.md) | diff-review | TOOL-aRepatriatedFork-23 TOOL-aRepatriatedFork-25 TOOL-aRepatriatedFork-26 TOOL-aRepatriatedFork-27 TOOL-aRepatriatedFork-28 TOOL-aRepatriatedFork-29 TOOL-aRepatriatedFork-30 TOOL-aRepatriatedFork-44 TOOL-aRepatriatedFork-45 TOOL-aRepatriatedFork-46 TOOL-aRepatriatedFork-47 |
| [2026-09-30-review-TOOL-aRepatriatedFork-23-closing-diff-round2.md](../reviews/2026-09-30-review-TOOL-aRepatriatedFork-23-closing-diff-round2.md) | diff-review | TOOL-aRepatriatedFork-29 TOOL-aRepatriatedFork-30 TOOL-aRepatriatedFork-46 |

<!-- /gen:spec-records -->

## 1. Goal

The census found 12 sites where a kit path gov spells is EXECUTED or probed, and where an install at
any prefix but `tools/` silently skips a leg, runs nothing or cannot detect a foreign kit. It found
six more where a literal fallback rung follows a derived one. These are the only literals in the
tree that change behaviour, so they go first. Every one derives its kit root at run time or is
stamped at adopt time; none keeps a `tools`, `scripts` or root candidate list.

## 2. Scope (IN)

- **S1** — `.githooks/pre-commit`'s three `gate_at` calls (the hygiene leg at `:48`, the kickoff
  manifest leg at `:54`, the template-size leg at `:59`) take their kit root from one ladder:
  the target's receipt, then `resolve_kit_dir`'s rung, then a `GOV_KITROOT` declared in
  `.githooks/gate-env.sh`. Their fixed candidate lists go, `scripts/manifest-check.sh` included.
  An underivable root is handled as §8 F1 resolves. Observed by AC1, AC2.
  - **S1a (rev-3)** — The ladder is one function, `kit_gate <kit dir> <file> [home]`. Rung 1 is the
    receipt row whose `source` ends in `<kit>/<file>`, the join `check-wiring.sh` already makes.
    Rung 2 is `resolve_kit_dir`'s probe taken from the repo root: `<home>/<file>`, then
    `<kit>/<file>` for a root install. `home` defaults to the kit dir. The kickoff leg names its
    source home `skills/session-kickoff`, the rung `check-wiring.sh`'s card arm already takes,
    because gov keeps no receipt and homes that kit outside any tool root. Rung 3 is
    `<GOV_KITROOT>/<kit>/<file>`. `pre-commit` PARSES the one assignment out of `gate-env.sh`
    rather than sourcing the file, since it does not vet that file the way `pre-push` does. Gov
    declares `GOV_KITROOT=tools` there.
  - **S1b (rev-3)** — The F1 skip is announced when the leg's own trigger holds: a staged
    `memory/` path for hygiene, the staged template for template size. The kickoff leg has no
    trigger in the hook, since its gate decides for itself, so its skip is announced on every
    miss.
- **S2** — `.githooks/pre-push:367-368` sets `GOV_KITROOT` from the same ladder. The `tools` default
  and the `scripts` fallback go, and so does the marker whose reason promised a derivation the code
  never did (census §5). Observed by AC3.
  - **S2a (rev-3)** — The ladder runs AFTER `gate-env.sh` is sourced, with any inherited
    `GOV_KITROOT` unset first, so only the vetted file can declare it. Rung 1 takes the receipt row
    for the runner and uses its grandparent. Rung 2 finds a root install by the leg manifest or the
    runner directory at the root. Every `$GOV_KITROOT/` join becomes `${KP}`, so a root install
    resolves too.
  - **S2b (rev-3)** — F1's refusal fires where a miss strands: the DEFAULT bar on a
    default-branch push. It is `bar-refused`, and it comes after the bar class is recorded as
    `default`. A declared `GOV_GATE_CMD` does not need the kit root to find its bar. A leg manifest
    tracked where the ladder does not reach keeps the existing manifest refusal, which now also
    covers a miss. The hook's own fixtures that lay kits at `scripts/` declare that root in a
    committed `gate-env.sh`, and the one that tracks a manifest at `tools/` moves it to the root.
  - **S2c (rev-4)** — The closing review's B1. The receipt rung made the default bar whatever
    runner an untracked or modified `.governance/install.json` named, and nothing vetted that
    runner either. On a default-branch push the hook now vets the receipt with the predicate it
    already applies to `gate-env.sh`: tracked at the pushed sha, working copy hashing to that
    blob. The default bar's resolved runner takes the same predicate. One function carries it for
    all three files, and a failure is `bar-refused` before any forcing predicate reads the kit
    root. A row under `.git/` names a path git cannot track, so it falls to the same refusal.
- **S3** — `adopt-unattended.sh` stamps `LANDER`, `GATE_CMD`, `WIRING_CHECK` and
  `GENERATED_INDEXES` in the seeded `.unattended.conf` with the adopt-time kit root. This is the
  `MAP_DIFF_CMD` mechanism `adopt-codebase-map.sh:116-131` already uses. The example's four values
  become the tokens that stamping replaces. Observed by AC4.
  - **S3a (rev-3)** — The tokens are `{{TOOL_ROOT}}` in `LANDER`, `GATE_CMD` and `WIRING_CHECK`,
    and `{{MEMORY_TREE_DIR}}` for the generator in `GENERATED_INDEXES`. The adopter already probes
    that directory, because an adopter may install the memory-tree kit flat in its tool root. The
    adopter stamps a conf the operator copied that still carries a token, in render mode, and reads
    the result back. `--check` refuses a conf that still carries one. It does not seed an absent
    conf: that would change the `no-project-layer` outcome the descriptor declares, and the
    example's own header already says to copy it.
- **S4** — `unattended.sh`'s condition-3 overlap key compares a `GENERATED_INDEXES` generator by the
  path it resolves to, so a seeded value from an earlier adopt still keys, as §8 F2 resolves.
  Observed by AC5.
  - **S4a (rev-3)** — A generator keys by BOTH its declared spelling and, when that names no file,
    the one tracked file whose path ends in the declared `<dir>/<file>`. Keeping the declared key
    means no refusal that fires today can stop firing.
- **S5** — The three received suites that name their gate as `$ROOT/tools/…`
  (`check-microformats.test.sh:11`, `check-placeholders.test.sh:14`) or probe the memory-tree
  README at two fixed prefixes (`check-wiring.test.sh:823`) derive the path from `$HERE`.
  Observed by AC6.
- **S6** — `tools/codebase-map/selftest.py:1613` finds the lexicon as a sibling of `map_lib.kit_dir()`,
  not at `repo_root() / "tools" / "lexicon"`. This closes backlog `TOOL-aProbedToolkit-3`, whose
  first site `check-verdict-epoch.sh` is already derived (census §5), and with it
  `TOOL-dPolishedVitrine-6`, which names that same first site. Observed by AC7.
- **S7** — govkit's `foreign_kit_present` (`tools/govkit/govkit.py:5415`) probes the intake's own
  prefix instead of the pair `("tools", "")`. The `sentinel =` lines it reads become kit-relative:
  two kit descriptors and five `tools/govkit/entries/` descriptors. Observed by AC8.
  - **S7b (rev-4)** — The closing review's M5. S7a dropped the old pair's `tools` probe, so a
    hand-copied kit at gov's canonical prefix was not detected under an intake that declares
    another prefix, and `apply` installed a second copy. The probe takes the union: the target's own
    ctx, gov's canonical ctx from `canonical_ctx`, and the root.
  - **S7a (rev-3)** — Each entry is probed at its own `target_context`: the intake's prefix, with
    any per-entry override, and then at the root, which the old pair also covered. A `sentinel` is
    relative to the entry's home, meaning the kit dir, or the prefix for a flat entry.
- **S8** — The literal fallback rungs after a derived rung, at `tools/check-wiring.sh:496, 547, 770,
  780` and `skills/session-kickoff/manifest-check.sh:426`, give way to an announced skip when the
  derived rung misses. Their four waiver rows are struck in the same commit, because a stale row
  reds the arm. Observed by AC9.
  - **S8a (rev-3)** — `manifest-check.sh`'s rung becomes the one tracked `corpus_ids.py`. No probe
    reaches gov's copy: gov homes the checker under `skills/`, homes the reader under its tool root
    and keeps no receipt. A miss is the checker's existing "id citations unchecked" note.
    `check-wiring.test.sh` lays its recall fixture at the checker's own prefix. AC12 derives the
    root-layout command from a copy of the checker installed at the root, because the mixed layout
    the bare rungs served is now a named skip. The `.githooks/pre-commit:48` waiver row goes too,
    since S1 removes its literal, so five rows go and not four.
  **Readers:** by name: `check-install-prefix.sh` is the one reader of the waiver rows, and
  `check-wiring.test.sh`'s recall arm and its AC12 are the only fixtures laid in the mixed layout
  the bare rungs served. by value: NO VALUE READERS — a waiver row and a probe rung carry no value
  another program consumes; the checker's own skip line is the only output that moves.
- **S9** — The ledger rows for these files are lowered by `--write-ratchet`, and every kit moved
  takes its version bump in every carrier. Observed by AC10.

## 3. Non-goals (OUT)

- Any other literal in the files S1 to S8 touch. The fixture literals in `check-wiring.test.sh` and
  `codebase-map/selftest.py` belong to `TOOL-aRepatriatedFork-28`, and the comments in
  `.unattended.conf.example` to `TOOL-aRepatriatedFork-27`.
- `render_playbook.py:204`, the sixth fallback rung in the census. Its candidates name adopter-owned
  gate scripts rather than kit files, and `TOOL-aRepatriatedFork-29` owns that file.
- Re-stamping a `.unattended.conf` an adopter already seeded. It is adopter-owned after the first
  write; S4 makes an old value still work instead.

### Edges

- **consumes-from** `TOOL-aRepatriatedFork-23` — the epoch-5 ledger rows for `pre-commit:54`, the
  three suite lines and the `"tools"` join. Epoch 4 cannot see them, so without it this unit's
  lowering has nothing to lower.
- **hands-off** `TOOL-aRepatriatedFork-28` — the remaining fixture literals in the two test files
  S5 and S6 edit.
- **hands-off** `TOOL-aRepatriatedFork-30` — a waiver registry four rows shorter.
- **hands-off** `TOOL-aRepatriatedFork-49` — the default bar's remaining selection inputs: the leg
  manifest its vetted runner reads, and the environment knobs that choose that manifest and its python.

## 4. Design

### Evidence

From the 2026-09-25 prefix census at `2143b6d6` (session scratchpad, not committed), census §2
unless stated. PINNED, measured 2026-09-25.

- `pre-commit:48` probes only gov's prefix and the root, so at `scripts/` or `vendor/gov/` the
  staged hygiene leg is skipped and the hook exits 0. `:54` has the same shape with a fixed list,
  and the epoch-2 existence filter hides it from the ledger.
- `pre-push:367` can only set `GOV_KITROOT` to `tools` or `scripts`, so at a root or `vendor/gov/`
  install `GATE_RUNNER` names a runner that does not exist.
- `.unattended.conf.example:268` holds two literals in `GENERATED_INDEXES`, which is not
  REPLACE-marked. `unattended.sh:5742` uses the generator half as the condition-3 overlap key, so
  at another prefix the refusal cannot fire. `:18`, `:25` and `:71` are REPLACE-marked and strand
  only an adopter who keeps the default.
- `check-microformats.test.sh:11` and `check-placeholders.test.sh:14` name `$ROOT/tools/…`, and at
  another prefix every arm fails to reach its gate. `check-wiring.test.sh:823` makes the AC12
  README arms skip with a false reason at `scripts/`.
- `codebase-map/selftest.py:1613` skips with a false reason at inCMS, whose lexicon is at
  `scripts/lexicon/`.
- `govkit.py:5415` means a foreign install at `scripts/` is not detected.
- The ownership rule this set uses (the census record's section 7) gives this unit 19
  literals over 13 files: 9 counted today, 5 invisible and 5 in files no descriptor resolves. It
  also gives it arm 1's five lines at `pre-commit:48` and `check-wiring.sh`, and arm 3's two at
  `pre-push:367` and `manifest-check.sh:426`.

### Ownership rule

One literal has one writer. A stranding site or fallback rung is this unit's, even inside a test
file, and every other literal in those files is its class owner's. The rule is written in
`TOOL-aRepatriatedFork-23` §8 F3 and applied by the census record's section 7.

### Files touched (estimate)

`.githooks/pre-commit` · `.githooks/pre-push` · `.githooks/gate-env.sh` ·
`tools/unattended/adopt-unattended.sh` · `tools/unattended/.unattended.conf.example` ·
`tools/unattended/unattended.sh` · `tools/check-microformats.test.sh` ·
`tools/check-placeholders.test.sh` · `tools/check-wiring.test.sh` · `tools/check-wiring.sh` ·
`tools/codebase-map/selftest.py` · `tools/govkit/govkit.py` · `tools/govkit/selftest.py` ·
`skills/session-kickoff/manifest-check.sh` · `tools/install-prefix-waivers.txt` ·
`tools/install-prefix-carried.txt` · the seven descriptors carrying a `sentinel =` line ·
rev-3 adds `.githooks/pre-commit.test.sh` · `.githooks/pre-push.test.sh` ·
`.githooks/pre_push_bar_selftest.py` · `tools/unattended/unattended.test.sh` ·
`tools/unattended/adopt-unattended.test.sh`

### Alternatives rejected

- A new conf key naming the kit root. The build-level rule reserves a new key for an adopter's
  decision, and the kit root is its layout.
- Keeping `tools` as the first rung "because gov resolves unchanged". Gov resolves through the
  receipt-free rung like any source, which AC1 observes at gov's own prefix.

## 5. Production-readiness checklist

- security — `pre-push` is a guarded surface (`TOOL-aRepatriatedFork-5`). The bar command's
  tracked-and-unmodified check is unchanged; only where the runner is found moves. AC3 observes the
  refusal path still refuses.
- perf / scale — one receipt read per hook invocation, which `check-wiring.sh` already pays.
- error / empty / loading states — an underivable kit root is §8 F1.
- observability — each announced skip names the rung that missed.
- risks — a hook that derives the wrong root runs the wrong gate. AC1 runs the ladder at three
  prefixes.
- testing — the pre-commit and pre-push self-tests gain a `vendor/gov/` fixture; govkit's self-test
  gains a foreign install at `scripts/`.
- migration — an adopter keeps its seeded `.unattended.conf`; S4 is what makes that safe.
- user docs — `WIRE-INTO-PROJECT.md`'s hook paragraph, which is `TOOL-aRepatriatedFork-26`'s file.

## 6. Acceptance criteria

- **AC1** — When a fixture repo with the hygiene kit at `vendor/gov/memory-tree/` stages a change
  under `memory/`, `.githooks/pre-commit` runs `check-memory-hygiene.sh --staged` from that path.
  The same holds at `scripts/` and at the repo root.
  Red when: the leg is skipped at any of the three prefixes.
- **AC2** — Red-first control: the `vendor/gov/` fixture under `2143b6d6`'s hook skips the leg and
  exits 0. Recorded in the acceptance ledger.
  Red when: the old hook already runs it, so AC1 proves nothing.
- **AC3** — When `.githooks/pre-push` runs in a fixture whose runner sits at
  `vendor/gov/run-gates/`, `GATE_RUNNER` names that path. A modified runner is still refused.
  Red when: `GATE_RUNNER` names `tools/…` or `scripts/…`, or the modified runner passes.
- **AC4** — When `adopt-unattended.sh` installs at `scripts/unattended/`, the seeded conf's four keys
  name `scripts/` paths, and `git grep -n 'tools/'` over the seeded conf's values finds none.
  Red when: any of the four values names gov's prefix.
- **AC5** — When a run declares a `GENERATED_INDEXES` pair whose generator is spelled at gov's old
  prefix in a fixture installed at `scripts/`, the condition-3 refusal still fires on an overlap.
  Red when: the refusal is silent, the `2143b6d6` behaviour.
- **AC6** — When the microformat and placeholder gates and the wiring checker are copied to
  `scripts/` in a fixture, `git grep -nE '\$(ROOT|REPO)/tools/'` over their three suites finds
  nothing, and each suite's gate variable resolves to an existing file.
  cost: the suites themselves run in the main loop, not in this pass.
  Red when: a `$ROOT/tools/` spelling survives, or the variable names a missing file.
- **AC7** — When the codebase-map self-test's lexicon lookup is imported in a fixture whose kit
  sits at `scripts/codebase-map/` and whose lexicon sits at `scripts/lexicon/`, it resolves the
  lexicon through `kit_dir()` and the arm runs instead of skipping.
  Red when: it prints the old "not installed" skip.
  permission: the self-test as a whole runs in the main loop; this pass observes the lookup alone.
- **AC8** — When `python tools/govkit/govkit.py intake` targets a fixture with a foreign kit
  installed at `scripts/`, it refuses with the AC8 refusal of `foreign_kit_present`.
  Red when: the intake proceeds, which is `2143b6d6`'s behaviour.
- **AC9** — When the derived rung of `check-wiring.sh` misses, it prints a skip naming the rung,
  and `bash tools/check-install-prefix.sh` reports no stale waiver row.
  Red when: a literal `tools/` rung still runs, or a waiver row outlives its line.
- **AC10** — `bash tools/check-kit-versions.sh` exits 0, and `python tools/govkit/govkit.py epoch
  --base 2143b6d6` names no kit this unit moved.
  Red when: a moved kit's carrier was missed.
- **AC11** — rev-4. In `.githooks/pre-push.test.sh`, a fixture whose tracked root runner exits 1
  pushes the default bar three ways: with an ignored `.governance/install.json` naming a runner
  under `.git/` beside a planted manifest, with that receipt tracked, and with a tracked receipt
  naming the tracked runner and then modified. The first two and the last are refused as
  `bar-refused` before the planted runner runs. The third reaches the tracked runner and is
  refused as `gate-red`.
  Red when: any push lands, or the planted runner prints. The `7de665e5` hook lands the first two.
- **AC12** — rev-4. A `tools/govkit/selftest.py` arm runs `apply` against a target whose
  `deploy.toml` declares `prefix = "scripts"` and which carries a foreign kit at gov's canonical
  prefix. `foreign_kit_present` names it and `apply` refuses before writing a receipt.
  Red when: the apply exits 0, which is the `7de665e5` behaviour.

## 7. Gates

`install-prefix (shipped surface)` · `install-prefix self-test` · `branch-guard self-test` · `pre-push self-test` · `pre-push bar self-test` · `pre-push run-log line` · `push-main self-test` · `check-wiring self-test` · `micro-format gate selftest` · `placeholder-catalogue self-test` · `codebase-map kit selftest` · `codebase-map gate coverage` · `codebase-map adopter e2e` · `manifest-check self-test` · `scratch-guard self-test` · `recall floor arms` · `govkit selftest` · `govkit selfcheck` · `govkit refusal join` · `govkit acceptance matrix` · `kit version markers` · `kit epoch (shipped bytes move, the version moves)` · `unattended kit gate` · `lexicon naming predicates` · `harness arms (fail branches armed or pinned)`

New arm: `.githooks/pre-commit.test.sh` · a `vendor/gov/` fixture whose staged hygiene leg the
`2143b6d6` hook skips · none

New arm: `tools/govkit/selftest.py` · a foreign kit at `scripts/` the old probe misses · none

New arm: `.githooks/pre-push.test.sh` · a `vendor/gov/` fixture whose default bar names the runner at that prefix, and refuses it modified · none

New arm: `tools/unattended/unattended.test.sh` · a `GENERATED_INDEXES` generator spelled at a prefix the fixture does not have, still refusing its pairing · none

New arm: `tools/unattended/adopt-unattended.test.sh` · a copied example conf stamped at the adopter's own tool root, and `--check` refusing an unstamped one · none

New arm: `.githooks/pre-push.test.sh` · rev-4: an ignored receipt, a tracked receipt naming an untracked runner, and a modified receipt, each refused as bar-refused, beside a tracked-receipt control · none

New arm: `tools/govkit/selftest.py` · rev-4: a foreign kit at gov's canonical prefix under a `scripts` intake · none

## 8. Open questions

- **F1 — what does a hook do when no rung of the ladder yields a kit root?** Option (a): an
  announced skip in both hooks. Option (b): a refusal in both. Option (c): an announced skip in
  `pre-commit`, whose staged legs are an early signal, and a refusal in `pre-push`, whose bar is the
  merge bar. Recommendation: (c). A commit hook that blocks on an absent kit stops ordinary work,
  while a push that cannot find its bar and passes is the silent skip this unit exists to remove.
  RESOLVED (owner, 2026-09-25): (c), the recommendation.
- **F2 — how does an adopter's existing `.unattended.conf` keep keying condition 3?** It was seeded
  with gov's generator path and is adopter-owned after that. Option (a): the driver resolves both
  halves of each pair before comparing, so an old value keys at any prefix. Option (b): stamp at
  adopt only, and let `govkit update` report the stale seed value. Recommendation: (a). It closes
  the defect for adopters who never re-adopt, and (b) leaves the refusal dead until someone reads a
  report.
  RESOLVED (owner, 2026-09-25): (a), the recommendation.

## 9. Revision log

- rev-1 · 2026-09-25 · initial draft. Owner rulings of 2026-09-25: the remaining hard-coded kit
  prefixes are found and drained before `TOOL-aRepatriatedFork-18`'s held leg, and every one is
  drained. This unit takes the stranding sites first, as census §6 recommends.
- rev-2 · 2026-09-25 · §8 resolved by the owner: every fork takes its recommendation.
- rev-3 · 2026-09-29 · the unit pass, before code. Reading the code showed that several rev-2 lines
  would break gov or its own suites, so each got a sub-item. S1a: the kickoff leg keeps its source
  home as rung 2, because gov keeps no receipt. S2a/S2b: `pre-push` resolves after the vetted
  `gate-env.sh`, and refuses only where the default bar is stranded, so a declared bar and the
  hook's fixtures still reach their verdicts. S3a: the generator token is `{{MEMORY_TREE_DIR}}`,
  because the memory-tree kit may sit flat, and the adopter stamps a copied conf rather than seeding
  one. S4a: both keys are kept. S7a: the probe is per entry. S8a: the manifest checker gets a
  tracked-reader rung, and a fifth waiver row goes. Five suites join the files touched.
- rev-4 · 2026-09-30 · closing review round 1 fold: B1 — the default bar follows only a receipt
  and a runner the repository tracks unmodified, vetted as `gate-env.sh` is (S2c, AC11).
  closing review round 1 fold: M5 — the foreign-kit probe keeps gov's canonical prefix beside the
  target's own and the root (S7b, AC12).
- rev-5 · 2026-09-30 · §3 · closing review round 2: H1 is promoted to `TOOL-aRepatriatedFork-49`,
  and §3 gains the hands-off edge that unit consumes. No scope or criterion of this unit moves.

## 10. Reuse audit

`python tools/codebase-map/reuse_lookup.py "derive a kit directory from the receipt or the script
location"` ranked `kit_rel` and `kit_dir` in `tools/codebase-map/map_lib.py`; S6 reuses `kit_dir`.
The probe cannot see shell, so the hook ladder was found by reading: `check-wiring.sh:37-53` already
walks receipt then `KIT_REL`, and `resolve_kit_dir` is the canonical inline block in
`tools/lib/render-doc.sh:77`. S1 and S2 reuse those rungs rather than writing a third. S3 reuses
the `MAP_DIFF_CMD` stamp in `adopt-codebase-map.sh`.

Recall terms used: `install-prefix GOV_KITROOT gate_at resolve_kit_dir KIT_REL receipt stamp
MAP_DIFF_CMD GENERATED_INDEXES foreign_kit_present sentinel`.
