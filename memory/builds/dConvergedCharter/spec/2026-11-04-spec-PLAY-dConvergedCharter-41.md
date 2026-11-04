# PLAY-dConvergedCharter-41 — the folded homes' named readers re-pointed: the four `read_policy_key` copies, `read_modes`, `held_halves.py`, govkit's conf-key gap check and the placeholder arm, with the house-file arm

**Status:** DEFERRED · rev-1 · 2026-11-04 · node d · Tier-2 · base 923954b6 · streams playbook · order 3 · advances PLAY-dConvergedCharter-24

**Carries:** cl-dClosedLoop-0485@43490b62 part 2/2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-11-04-build-PLAY-dConvergedCharter-1-agent-ledger.md](../build/2026-11-04-build-PLAY-dConvergedCharter-1-agent-ledger.md) | journal | PLAY-dConvergedCharter-1 PLAY-dConvergedCharter-2 PLAY-dConvergedCharter-3 PLAY-dConvergedCharter-4 PLAY-dConvergedCharter-5 PLAY-dConvergedCharter-6 PLAY-dConvergedCharter-7 PLAY-dConvergedCharter-8 PLAY-dConvergedCharter-9 PLAY-dConvergedCharter-10 PLAY-dConvergedCharter-11 PLAY-dConvergedCharter-12 PLAY-dConvergedCharter-13 PLAY-dConvergedCharter-14 PLAY-dConvergedCharter-15 PLAY-dConvergedCharter-16 PLAY-dConvergedCharter-17 PLAY-dConvergedCharter-18 PLAY-dConvergedCharter-19 PLAY-dConvergedCharter-20 PLAY-dConvergedCharter-21 PLAY-dConvergedCharter-22 PLAY-dConvergedCharter-23 PLAY-dConvergedCharter-38 PLAY-dConvergedCharter-39 PLAY-dConvergedCharter-40 |
| [2026-11-04-build-PLAY-dConvergedCharter-41-deviation-411.md](../build/2026-11-04-build-PLAY-dConvergedCharter-41-deviation-411.md) | deviation | — |
| [2026-11-04-build-PLAY-dConvergedCharter-41-deviation-412.md](../build/2026-11-04-build-PLAY-dConvergedCharter-41-deviation-412.md) | deviation | — |
| [2026-11-04-prompt-PLAY-dConvergedCharter-41-split-brief.md](../prompts/2026-11-04-prompt-PLAY-dConvergedCharter-41-split-brief.md) | research | PLAY-dConvergedCharter-11 |

<!-- /gen:spec-records -->

## 1. Goal

PLAY-dConvergedCharter-11 folds every kit conf key the retrofit does not convert into
`.governance/policy.toml`, gives every reader one both-homes verb, `policy.py legacy`, and re-points
the readers its inventory derives. The owner split that unit on 2026-11-04
(`memory/builds/dConvergedCharter/prompts/2026-11-04-prompt-PLAY-dConvergedCharter-1-owner-decisions.md`,
"fold vs re-points"): this unit, built after it, re-points the readers the clause NAMES, each a parser
of its own rather than a `source` of the home: the four `read_policy_key` copies with their callers,
comments and parity arms, `transition_audit.read_modes`, `tools/run-gates/held_halves.py`, govkit's
conf-key gap check with kit.toml's `*_keys`, and the kit-placeholders leg. It moves the folded values
those readers read, which unit 11 holds in their homes until here (§8 F2), and it carries the
house-file arm: `roles_lib.load_policy`'s fallback to the house file is red once the seed retires
(DA-H5, DA-M6, FA-6).

## 2. Scope (IN)

Build-run preconditions: PLAY-dConvergedCharter-11 has landed S1 (the catalogue rows and their
`legacy` field), S2 (the fold, with the held keys left in their homes), S3 (`policy.py legacy`,
`render_folded_lines`), S5 (`arm_folded_homes`, `FOLDED_HOME_EXEMPT` with its transitional rows) and
S6 (`derive_readers`, I1). For S3 here: TOOL-dBoundRoles-21 S1, S6 and S7, specced and unbuilt, which
put the `[effort]` readers `check_roles.py`, `handoff.py` and `render_agents.py` on the `roles.effort.*`
keys through `read_policy_setting` and the `[gates]` readers on each role definition's `gates` field;
S3 grades gov's tree only once PLAY-dConvergedCharter-21 retires the seed.

- **S1** — The named readers re-pointed, each through PLAY-dConvergedCharter-11's interfaces:
  - the four copies of `read_policy_key` (`.githooks/pre-push:1426`, `tools/push-main.sh:404`,
    `tools/run-gates/post-merge.sh:171`, `tools/unattended/unattended.sh:9684`) are deleted with their
    byte-identity comments (`pre-push:1416-1421`, `post-merge.sh:170`, `push-main.sh:401-402`) and
    their parity arms (`tools/push-main.test.sh:1007-1011`, `.githooks/pre-push.test.sh:1560`,
    `tools/unattended/unattended.test.sh:15431`, `:15551`); each caller reads a folded key through
    `policy.py get <key> --rev <sha>` and an unfolded `mechanic` key through `policy.py legacy
    .githooks/gate-env.sh --rev <sha> --key <KEY>`, both under the inline `resolve_kit_dir`
    `pre-push:777-814` already carries for `platforms.provision` (`:825`, shared interface I4);
    `tools/run-gates/post-merge.sh` carries no resolver today ("sources no kit", `:170`), so it gains
    the inlined `resolve_python` and `resolve_kit_dir` blocks, each a new row of `PARITY_ROWS`
    (`tools/lib/resolve-python.test.sh:351`). Its `GOV_PYTHON` is the interpreter, so it is never read
    through itself: post-merge first resolves a python with `resolve_python` and no override, reads
    `legacy .githooks/gate-env.sh --rev <sha> --key GOV_PYTHON` through it, and where that prints a
    value resolves again with it as the override and exports it. Where no python resolves without the
    override, post-merge refuses through `write_refusal`, naming `GOV_PYTHON` and that exporting it in
    the hook's environment answers it, never running the bar on a default;
  - `tools/policy/policy.py`'s gate-file reader shape, `POLICY_KEY_READ` (`:1138`) and its use in
    `scan_gate_readers` (`:1197-1208`), reads the re-pointed call shape `legacy .githooks/gate-env.sh
    … --key <KEY>` in place of `read_policy_key "<expr>" KEY`, so a gate key read only by a hook keeps
    its `legacy-homes.txt` row after the copies go; the regex, its docstring, the module docstring's
    sentence (`:25`) and `tools/policy/README.md` (`:155`, and the copies' sentence PLAY-dConvergedCharter-11
    S7 leaves naming them) stop spelling `read_policy_key`;
  - `transition_audit.read_modes` (`tools/memory-tree/transition_audit.py:421`) reads both homes keyed
    by commit: one `cat-file --batch-check` per home over the commits, the policy file's
    `memory-tree.backlog-mode` winning where a commit's policy blob sets it, else `read_mode` over the
    conf blob, as today; its second caller, `migrate_backlog.py:1325`, takes the result unchanged;
  - `tools/run-gates/held_halves.py` reads `GATE_WSL_PARITY_RUNS` as `gate.wsl-parity-runs` through
    `policy.py get` (`resolve_wsl_host`, `:212-216`), and `GATE_WSL_MIRROR_DEFAULT`, a `mechanic`,
    through `legacy --key`;
  - govkit's conf-key gap check `read_conf_key_gaps` (`tools/govkit/govkit.py:4943`, called by `check`
    at `:5484` and `update` at `:11897`) reads a kit's assignments from `policy.py legacy
    <[config].file>` in place of the file, so a kit's `*_keys` lists in
    `tools/{codebase-map,memory-tree,roles,runlog,unattended}/kit.toml` name the keys that output yields;
  - the kit-placeholders leg's second arm (`extract_conf_keys`, `tools/check-kit-placeholders.py:194`)
    adds to a kit's key set every `KEY` a catalogue row's `legacy` names for that kit's
    `[config].file`, so a template spelling a folded key's value still reds once the key leaves the
    shipped example.
  Each re-pointed shell caller captures the read and tests its exit before binding, the shape
  PLAY-dConvergedCharter-11 S4 states, so a missing python or kit refuses naming the reader.
  Observed by AC1, AC2, AC3, AC4, AC5, AC6 and AC7.
  **Readers:** by name: `.githooks/pre-push`, `tools/push-main.sh`, `tools/run-gates/post-merge.sh`,
  `tools/unattended/unattended.sh`, `tools/push-main.test.sh`, `.githooks/pre-push.test.sh`,
  `tools/unattended/unattended.test.sh`, `tools/lib/resolve-python.test.sh`, `tools/policy/README.md`,
  `tools/policy/policy.py` (`:25`, `:1138`, `scan_gate_readers`), `tools/memory-tree/transition_audit.py`,
  `tools/memory-tree/migrate_backlog.py`, `tools/run-gates/held_halves.py`, `tools/govkit/govkit.py`,
  `tools/check-kit-placeholders.py`. by value: every hit at the pass's base of
  `python check_policy.py --readers read_policy_key --kind value`, and `tools/policy/policy.py`'s
  `derive_legacy_homes`, whose gate-file rows `lists` re-derives from the re-pointed calls.
- **S2** — The held keys moved. PLAY-dConvergedCharter-11 S2 leaves in its home, and in its kit's
  shipped example, every folded key a reader of S1 reads from a home's own text in the tree at hand
  (§8 F2). In the commit that re-points that reader, each such key's value is written to gov's
  `.governance/policy.toml` under its folded name, its line leaves gov's home and the shipped example,
  becoming its row's `usage`, `python policy.py mirror --write` and `python policy.py lists --write`
  are re-run, and the gate file's documentation line `#   GATE_WSL_PARITY_RUNS=`
  (`.githooks/gate-env.sh:82`) is reworded to name `gate.wsl-parity-runs` in the policy file, as unit
  11 S2 rewords the others. At base the held set reads `BACKLOG_MODE` (`read_modes`; a blob assigning
  none reads `shards`, `transition_audit.py:208-223`, where gov's is `builds`, `.memory-tree.conf:734`),
  `GATE_WSL_PARITY_RUNS` (`held_halves.py:234-236` refuses a blank count) and every key a
  `required_keys_gate` or `required_keys_render` list names for a folded home and no `[config].defaults`
  holds (`read_conf_key_gaps` reads such a key `absent`): `tools/codebase-map/kit.toml:72-73`,
  `tools/memory-tree/kit.toml:82-83`, `tools/memory-recall/kit.toml:69`, `tools/drift-audit/kit.toml:60`
  and `tools/unattended/kit.toml:172-173`; DERIVED again at unit 11's pass. The four copies' keys are not
  held: each copy reads at R (`pre-push:1449`, `:1743`, `unattended.sh:9718`, `:10359`) or at the landed
  tip (`push-main.sh:430`), which on the run branch is the remote's unfolded tree until the landing
  that carries this unit too. Each `FOLDED_HOME_EXEMPT` row unit 11 S5 adds for a reader of S1 is
  deleted in the commit that re-points that reader, so the table ends holding its one permanent row,
  `read_modes`, which reads a home's history by revision. Observed by AC7 and AC8.
  **Readers:** by name: the readers of S1, `tools/policy/legacy-homes.txt`, and
  `tools/policy/policy.py`, whose lists verb alone drains it. by value: `FOLDED_HOME_EXEMPT` in
  `tools/policy/check_policy.py`, whose transitional rows leave, and the folded readers
  PLAY-dConvergedCharter-11 S4 re-pointed, which read each held key from the policy file once it moves,
  through `policy.py legacy`.
- **S3** — The house-file arm, `arm_house_readers`, the red on the house-file fallback of
  `roles_lib.load_policy`, which leaves with the seed. It is one more row of `ARMS`
  (`tools/policy/check_policy.py:740`) over the existing scanner, never a scanner of its own:
  `arm_single_reader` (`:631`) gains an optional `exempt` set of file paths it does not grade, and its
  `reader_dir` may name the one reader FILE, in which case only that file is skipped rather than its
  directory. The row reads `arm_single_reader(repo, "<tool-root>/roles/house/policy.toml",
  <roles_lib.py>, const="load_policy", exempt=HOUSE_MIGRATORS)`, `roles_lib.py` found through the
  inlined `resolve_kit_dir("roles", "roles_lib.py", here)`. So a code line, never a comment, a docstring
  or a self-test's data, in any file but `roles_lib.py` and the migrators that reads the house file or
  names `load_policy` reds. `HOUSE_MIGRATORS` is declared once, in `check_policy.py`, and is the set the
  migration needs after the seed leaves: `tools/govkit/steps/house_seed.py` (PLAY-dConvergedCharter-21
  S1) and `tools/playbook/adopt_declarations.py` (`derive_house_proposals`, DEPL-dShippedRelease-28 S2),
  each required to spell `house/policy.toml` literally so `derive_readers` still lists it; their plants
  sit in `tools/govkit/selftest.py`, which `derive_code_files` already skips as a self-test.
  PLAY-dConvergedCharter-21 AC6 passes the same set as `--except` paths. The row is armed only once
  `tools/roles/house/policy.toml` is absent from the tree; while the seed is present it prints
  `house-file arm: unarmed — the seed is present (PLAY-dConvergedCharter-21)` and grades nothing, and
  the line is the arm's verdict, never a pass. The re-points of `check_roles.py:367`, `handoff.py:480`
  and `render_agents.py:140`, each a `load_policy` call at base (`roles_lib.py:398`), are
  TOOL-dBoundRoles-21 S7's (deviation 412). Observed by AC9.

## 3. Non-goals (OUT)

- The fold itself, the both-homes verb, the derived re-points, the folded-home arm and the inventory:
  PLAY-dConvergedCharter-11.
- The `mechanic` gate keys: they stay in the gate file, read through `legacy --key`
  (PLAY-dConvergedCharter-11 §8 F3, which also rules that all four copies go).
- The house file's retirement and its fallback's removal: PLAY-dConvergedCharter-21. The `[effort]`
  readers on `roles.effort.*`: TOOL-dBoundRoles-21.
- Removing the unattended kit, whose copy this unit re-points first: PLAY-dConvergedCharter-12.
- Shipping the re-points to adopters: PLAY-dConvergedCharter-20.
- Running the unattended kit's suites: waived for this build's landing (README rule 8).

### Edges

- **consumes-from** `PLAY-dConvergedCharter-11` — `render_folded_lines` behind `policy.py legacy`, the folded key names with each catalogue row's `legacy` field, `derive_readers` with its `--readers` CLI, and `FOLDED_HOME_EXEMPT` with the transitional rows S2 drains and the held keys S2 moves; without it there is no verb to re-point to and no key to read
- **hands-off** `PLAY-dConvergedCharter-12` — `read_policy_key`, the copy in `tools/unattended/unattended.sh` S1 deletes and re-points before that unit removes the kit, so its P3 probe reads no copy
- **hands-off** `PLAY-dConvergedCharter-20` — `read_conf_key_gaps`, re-pointed to `policy.py legacy`, and the pre-push hook's `gate.doc-paths` and `gate.post-merge` reads through `policy.py get`, which that unit's gate-file step relies on at an adopter
- **hands-off** `PLAY-dConvergedCharter-21` — `arm_house_readers`, armed when the seed retires, and `HOUSE_MIGRATORS`, the exempt paths that unit's AC6 passes as `--except`
- **consumes-from** external — TOOL-dBoundRoles-21 S1, S6 and S7, the `[effort]` and `[gates]` re-points S3 grades, specced and unbuilt

## 4. Design

### Evidence

Read at `923954b6`.

- The four copies' callers read `INHERITED_RED`, `INHERITED_RED_MAX_AGE`, `GATE_POST_MERGE`,
  `GATE_DOC_PATHS` (`pre-push:1453-1454,1744-1745`), `GATE_POST_MERGE` (`push-main.sh:431`),
  `GOV_GATE_CMD`, `GOV_PYTHON`, `GATE_SELFTESTS` (`post-merge.sh:222,231-232`), and `GATE_POST_MERGE`,
  `GATE_POLICY_FILE`, `INHERITED_RED`, `INHERITED_RED_MAX_AGE`, `HELD_CI_WORKFLOW`
  (`unattended.sh:9718-9743,10360`). Post-merge's three are `mechanic`, so they re-point through
  `legacy --key`, which is what lets the fourth copy go too.
- The `--decide` mode reads `INHERITED_RED` at the remote tip R through `read_policy_at`
  (`pre-push:1443-1466`), where an absent or blank value reads `land`, and announces `inherited-red
  policy at <sha8> reads <policy>`; gov's value is `land` (`.githooks/gate-env.sh:103`).
- `policy.py get` takes `--rev`; `policy-shim.sh get` does not.
- `read_conf_key_gaps` parses the conf file's text line by line with `parse_conf_assignment`, a key in
  `[config].defaults` never absent; `held_halves.parse_conf` parses the gate file's text strictly.

### The order

One pass, after PLAY-dConvergedCharter-11 and before PLAY-dConvergedCharter-12: each reader of S1 is
re-pointed, its held keys moved and its transitional `FOLDED_HOME_EXEMPT` row deleted in one commit,
then S3's row. Every re-point reads the same values before and after its held keys move, because
`legacy` falls back to the home for a key the policy file does not set (unit 11 S3).

### Inventory

Minted: `arm_house_readers`, `HOUSE_MIGRATORS` and the `exempt` parameter of `arm_single_reader`,
each `OK` at `d8a12f046` by `python tools/lexicon/lexicon.py --suggest <name> --as py.function`, as
PLAY-dConvergedCharter-11 §4 recorded them before the split. Nothing else is named here.

### Files touched (estimate)

- `.githooks/pre-push`, `.githooks/pre-push.test.sh`, `tools/push-main.sh`, `tools/push-main.test.sh`
- `tools/run-gates/post-merge.sh`, `tools/run-gates/held_halves.py`, `tools/lib/resolve-python.test.sh`
- `tools/unattended/unattended.sh`, `tools/unattended/unattended.test.sh`
- `tools/policy/policy.py`, `tools/policy/check_policy.py`, `tools/policy/README.md`,
  `tools/policy/legacy-homes.txt` (regenerated)
- `.governance/policy.toml`, `.governance/policy.json` (the mirror, regenerated)
- `.memory-tree.conf`, `.codebase-map.conf`, `.unattended.conf`, `.githooks/gate-env.sh` (the held lines)
- `tools/codebase-map/.codebase-map.conf.example`, `tools/memory-tree/.memory-tree.conf.example`,
  `tools/unattended/.unattended.conf.example` (the held lines)
- `tools/memory-tree/transition_audit.py`, `tools/govkit/govkit.py`, `tools/check-kit-placeholders.py`
- `tools/codebase-map/kit.toml`, `tools/memory-tree/kit.toml`, `tools/roles/kit.toml`,
  `tools/runlog/kit.toml`, `tools/unattended/kit.toml`

### Alternatives rejected

- **`policy-shim.sh get` for the shell reads.** It takes no `--rev`, and the hook reads at R.
- **Post-merge reading `GOV_PYTHON` through a pure-shell copy of the old parser.** The clause re-points
  all four copies (PLAY-dConvergedCharter-11 §8 F3); post-merge resolves an interpreter first and reads
  the key through it, and refuses naming the remedy on the one host where only the gate file's value
  names a working python.
- **The held keys moved by PLAY-dConvergedCharter-11 with the rest.** Between the two passes
  `read_modes` would read gov's `builds` as `shards`, `held_halves.py` would refuse its parity count and
  `read_conf_key_gaps` would read a required key `absent` (§8 F2).
- **A scanner of its own for the house file.** `arm_single_reader` already reads one path's readers
  with comment and docstring skipping; S3 adds an `exempt` set to it.

## 5. Production-readiness checklist

- security — no reader parses a policy home in shell any more: each reads through the policy kit's
  reader, as committed at `--rev`, at R or at the landed tip.
- perf / scale — one interpreter start per read in each hook; `read_modes` stays two batch processes
  per home over the whole history.
- error / empty / loading states — a reader whose `get` or `legacy` call fails refuses naming the
  reader, exit 2 (unit 11 S4's capture shape); an absent key prints nothing and each caller's own
  default stands, as an absent line did.
- observability — the `--decide` line names the reading it took; the house-file arm prints `unarmed`
  while the seed is present.
- risks — post-merge on a host where only the gate file's `GOV_PYTHON` names a working python now
  refuses, naming `GOV_PYTHON` and the remedy, where it used to run (S1). Between unit 11's pass and
  this one the placeholder arm's key set misses the keys unit 11 dropped from the examples; nothing
  lands between them, the build landing once at its close.
- testing — the fixtures of §6 and the arms of §7.
- migration — gov's tree only; adopters: PLAY-dConvergedCharter-20.
- user docs — `help/policy.md` is PLAY-dConvergedCharter-11's; this unit changes no reading it states.

## 6. Acceptance criteria

The fixture verb is PLAY-dConvergedCharter-11's, `python check_policy.py --fixture <case> <dir>`, which
writes a scratch repository under `%TEMP%` with a short name.

- **AC1** — When a scratch clone of gov at this unit's parent commits `gate.inherited-red = "park"` in
  `.governance/policy.toml` on its remote tip, `INHERITED_RED=park` folded there in place of
  `.githooks/gate-env.sh:103`'s `land`, and runs `.githooks/pre-push --decide` with `<tip>
  <remote-sha>`, the combined output names `inherited-red policy` reading `land` before the re-point
  and `park` after.
  Red when: the hook still reads `.githooks/gate-env.sh` at R after the re-point.
  fixture: built under `%TEMP%` with a short name; the clone's remote is a second local clone.
- **AC2** — When `python check_policy.py --readers read_policy_key --kind value` runs over gov's tree
  after S1, it exits 0 and prints no reader outside the memory root, `tools/policy/policy.py` and
  `tools/policy/README.md` among the files it no longer names; over a scratch copy that keeps one copy
  in `tools/push-main.sh`, it exits 1 naming that file and line.
  Red when: a copy, a comment naming it or a parity arm comparing it survives the re-point.
- **AC3** — When `read_modes` runs over the `both-homes` fixture, whose first commit holds
  `BACKLOG_MODE=shards` in the conf and no policy value and whose second sets
  `memory-tree.backlog-mode = "builds"` and drops the line, it returns `shards` then `builds`.
  Red when: a commit whose policy blob sets the mode reads the conf blob's absence as `shards`.
- **AC4** — When `python held_halves.py` resolves its parity count over the `parity` fixture, which
  sets `gate.wsl-parity-runs = 5` in the policy file and `GATE_WSL_PARITY_RUNS=3` in the gate file, it
  reads 5.
  Red when: the working tree's gate file still wins.
- **AC5** — When `python check-kit-placeholders.py --root <dir>` runs over the `template-leak` fixture,
  a rendered template spelling `BACKLOG_MODE=500` while the example no longer assigns it, it exits 1
  naming the template and the key.
  Red when: the folded key leaves the arm's key set with the example.
- **AC6** — When `grep -c "post-merge.sh" tools/lib/resolve-python.test.sh` runs after S1 it prints at
  least 2, one row per inlined block, and `grep -c "read_policy_key" tools/run-gates/post-merge.sh`
  prints 0; over a scratch clone whose `PATH` holds no python and whose gate file sets `GOV_PYTHON`,
  `post-merge.sh` writes a refusal naming `GOV_PYTHON` and runs no bar.
  Red when: post-merge reads the interpreter's key through the interpreter it names, or runs the bar on
  a default python.
- **AC7** — When `python govkit.py check --target <dir>` runs over a scratch target holding the
  memory-tree kit whose `.memory-tree.conf` assigns no `MEMORY_ROOT` and whose policy
  file sets `memory-tree.memory-root`, it prints no `required key MEMORY_ROOT is ABSENT` line
  (`govkit.py:5488`); with the policy value removed too, it prints that line.
  Red when: the gap check reads the conf file's text alone, so a folded required key reads absent.
  fixture: the target under `%TEMP%` with a short name, the kit installed by `govkit.py apply`.
- **AC8** — When `python policy.py lists --write` runs over gov's tree after S2, `grep -vc '^#'
  legacy-homes.txt` prints 14, every row a `mechanic` row of `.githooks/gate-env.sh`, one of the six
  `.unattended.conf` extension rows or a house row; `grep -cE '^#\s+GATE_WSL_PARITY_RUNS='
  .githooks/gate-env.sh` prints 0; and `python check_policy.py` prints exactly one exempt row of
  `arm_folded_homes`, `tools/memory-tree/transition_audit.py` `read_modes`, and no finding.
  Red when: a held key stays in its home, or a transitional exempt row outlives its reader's re-point.
  figure: PINNED at `d8a12f046`, 6 mechanic rows, 6 extension rows and 2 house rows.
- **AC9** — When `python check_policy.py` runs over the `house-reader` fixture, a tree with no house
  file and a planted Python file calling `load_policy(`, `arm_house_readers` reds naming it; over
  `house-seed`, the same tree with the seed present, it prints `house-file arm: unarmed`; over
  `house-migrators`, the seedless tree holding the two `HOUSE_MIGRATORS` planted, `house_seed.py` and
  `adopt_declarations.py`, that each read `tools/roles/house/policy.toml`, it is green, and the same
  read planted in `tools/roles/check_roles.py` reds naming that file.
  Red when: a reader of the house file passes once the seed is gone, or a migrator in
  `HOUSE_MIGRATORS` reds.

## 7. Gates

`policy fixtures` · `transition-audit arms` · `pre-push self-test` · `pre-push bar self-test` · `push-main self-test` · `held-halves selftest` · `python resolver (behaviour + inline parity + idiom ban)` · `govkit selftest` · `govkit refusal join` · `govkit acceptance matrix` · `kit placeholders (a declared token its adopter substitutes)` · `kit-placeholders self-test` · `codebase-map kit selftest` · `codebase-map gate coverage` · `codebase-map adopter e2e` · `measure-legs selftest` · `recall floor` · `recall floor arms` · `lexicon selftest` · `runlog selftest` · `unattended kit gate` · `memory hygiene` · `spec tokens (a spec's own names resolve)` · `kit/dogfood doc parity` · `pre-push run-log line` · `run-gates run-log line`

The unattended kit's suites are waived for this build's landing (README rule 8); the parity arms S1
deletes there are named for the close. The arms below are declared for the main loop's close.

New arm: tools/policy/check_policy.py · covers AC2 AC3 AC8 AC9 · the `both-homes` and house fixture cases and gov's tree run with `read_modes` reading the conf blob alone, a transitional exempt row left standing, and `arm_house_readers` grading while the seed is present or exempting nothing · none
New arm: tools/lib/resolve-python.test.sh · covers AC6 · post-merge's two inlined blocks as `PARITY_ROWS` rows, staged red by one byte changed in a copy · none
New arm: .githooks/pre-push.test.sh · covers AC1 · the inherited-red read staged against the gate file at R in place of `policy.py get` · none
New arm: tools/push-main.test.sh · covers none · the `pm9` parity arm deleted with the copy it compared · none

## 8. Open questions

- **F1 — When does the house-file arm grade gov's tree?** (a) Once the seed file is absent, printing
  `unarmed` before; (b) at this unit's landing. Under (b) the arm reds on `render_agents.py:330`, the
  seed's writer, which PLAY-dConvergedCharter-21 removes, and on the readers TOOL-dBoundRoles-21 has
  not re-pointed at HEAD; the clause retires the fallback "with the seed". The departure from the
  clause's "already on" is deviation 412, carried over from PLAY-dConvergedCharter-11's deviation 111
  when the arm moved here, number 411 being reserved for the main loop's design-to-spec record of this
  unit. Rung 1, the clause answers it. RESOLVED (agent, 2026-11-03, delegated): (a). widens: none · relaxes: none
- **F2 — How do PLAY-dConvergedCharter-11's fold and this unit's re-points stand between the two
  passes?** (a) Unit 11 S2 holds back every folded key a reader of S1 reads from a home's or a shipped
  example's own text, and S2 here moves each in the commit that re-points its reader, unit 11's arm
  exempting those readers by named, printed `FOLDED_HOME_EXEMPT` rows S2 deletes; (b) the two units
  built in one pass; (c) this unit built before unit 11's value move. Unheld, the tree at unit 11's tip
  reads gov's `builds` as `shards` in `read_modes`, refuses the parity count in `held_halves.py` and
  reads a required key `absent` in `read_conf_key_gaps`, so veto 1 removes the unheld split; (c)
  reverses the order the owner ruled on 2026-11-04, and (b) leaves no pass that tells the two halves
  apart, which the split exists for (M2). Rung 1, unit 11 S2's own rule that no reader reads a home
  whose line has left before it reads the policy file answers it. RESOLVED (agent, 2026-11-04, delegated): (a). widens: none · relaxes: none

## 9. Revision log

- rev-1 · 2026-11-04 · initial draft: S1 and S3 moved from PLAY-dConvergedCharter-11 S4 and S8 by the
  owner's split ruling,
  `memory/builds/dConvergedCharter/prompts/2026-11-04-prompt-PLAY-dConvergedCharter-1-owner-decisions.md`
  ("fold vs re-points"), with that unit's AC5, AC7, AC9, AC11 and AC15 as AC1, AC9, AC4, AC5 and AC6,
  the `read_modes` half of its AC2 as AC3, the after-S4 half of its AC6 as AC2 and its AC1's figure as
  AC8; S2, AC7 and §8 F2 new, the held keys the split owes (F2); F1 is that unit's F5.

## 10. Reuse audit

The seams extended: PLAY-dConvergedCharter-11's `policy.py legacy` and `policy.py get --rev`, the one
reader every re-point calls; the inline `resolve_kit_dir` the hook already carries (`pre-push:777-814`,
`:825`) and the `PARITY_ROWS` table (`tools/lib/resolve-python.test.sh:351`) post-merge's blocks join;
`read_legacy_fanout` and `derive_lowered_limit` (`tools/policy/policy.py:767-807`), the keyed-by-commit
precedent `read_modes` follows; `arm_single_reader` (`tools/policy/check_policy.py:631`), which S3
extends with an `exempt` set. `python tools/codebase-map/reuse_lookup.py "read a kit conf key from the
policy file with a fallback to its legacy home keyed by commit"` ranked `load_conf` and `parse_conf`
(`tree_lib.py:135`, `held_halves.py`, SEAM), the parsers the re-points keep, and `resolve_kit_dir`
(SEAM). Scout C's rows hold at `923954b6` with one disagreement: PLAY-dConvergedCharter-11 rev-4 cited
the hook's resolver at `pre-push:806-830`; it sits at `:777-814`, with the `platforms.provision` read
at `:825`.

Recall terms used: `python tools/memory-recall/query.py "how are the named readers of a folded conf
re-pointed to the policy file" --terms "read_policy_key copies pre-push push-main post-merge held_halves
read_modes read_conf_key_gaps house file load_policy arm DA-H5"`
