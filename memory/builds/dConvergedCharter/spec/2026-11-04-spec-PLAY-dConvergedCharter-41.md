# PLAY-dConvergedCharter-41 — the folded homes' named readers re-pointed: the four `read_policy_key` copies, `read_modes`, `held_halves.py`, govkit's conf-key gap check and the placeholder arm, with the house-file arm

**Status:** DEFERRED · rev-3 · 2026-11-04 · node d · Tier-2 · base 923954b6 · streams playbook · order 3 · advances PLAY-dConvergedCharter-24

**Carries:** cl-dClosedLoop-0485@43490b62 part 2/2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-11-04-build-PLAY-dConvergedCharter-1-agent-ledger.md](../build/2026-11-04-build-PLAY-dConvergedCharter-1-agent-ledger.md) | journal | PLAY-dConvergedCharter-1 PLAY-dConvergedCharter-2 PLAY-dConvergedCharter-3 PLAY-dConvergedCharter-4 PLAY-dConvergedCharter-5 PLAY-dConvergedCharter-6 PLAY-dConvergedCharter-7 PLAY-dConvergedCharter-8 PLAY-dConvergedCharter-9 PLAY-dConvergedCharter-10 PLAY-dConvergedCharter-11 PLAY-dConvergedCharter-12 PLAY-dConvergedCharter-13 PLAY-dConvergedCharter-14 PLAY-dConvergedCharter-15 PLAY-dConvergedCharter-16 PLAY-dConvergedCharter-17 PLAY-dConvergedCharter-18 PLAY-dConvergedCharter-19 PLAY-dConvergedCharter-20 PLAY-dConvergedCharter-21 PLAY-dConvergedCharter-22 PLAY-dConvergedCharter-23 PLAY-dConvergedCharter-38 PLAY-dConvergedCharter-39 PLAY-dConvergedCharter-40 |
| [2026-11-04-build-PLAY-dConvergedCharter-41-deviation-411.md](../build/2026-11-04-build-PLAY-dConvergedCharter-41-deviation-411.md) | deviation | — |
| [2026-11-04-build-PLAY-dConvergedCharter-41-deviation-412.md](../build/2026-11-04-build-PLAY-dConvergedCharter-41-deviation-412.md) | deviation | — |
| [2026-11-04-prompt-PLAY-dConvergedCharter-11-r4-fold-brief.md](../prompts/2026-11-04-prompt-PLAY-dConvergedCharter-11-r4-fold-brief.md) | research | PLAY-dConvergedCharter-11 PLAY-dConvergedCharter-20 |
| [2026-11-04-prompt-PLAY-dConvergedCharter-41-split-brief.md](../prompts/2026-11-04-prompt-PLAY-dConvergedCharter-41-split-brief.md) | research | PLAY-dConvergedCharter-11 |
| [2026-11-04-review-PLAY-dConvergedCharter-11-chain-spec-audit-round1.md](../reviews/2026-11-04-review-PLAY-dConvergedCharter-11-chain-spec-audit-round1.md) | spec-audit | PLAY-dConvergedCharter-11 PLAY-dConvergedCharter-17 PLAY-dConvergedCharter-38 PLAY-dConvergedCharter-20 PLAY-dConvergedCharter-21 PLAY-dConvergedCharter-13 PLAY-dConvergedCharter-40 PLAY-dConvergedCharter-7 PLAY-dConvergedCharter-9 |
| [2026-11-04-review-PLAY-dConvergedCharter-11-spec-audit-round1.md](../reviews/2026-11-04-review-PLAY-dConvergedCharter-11-spec-audit-round1.md) | spec-audit | PLAY-dConvergedCharter-11 PLAY-dConvergedCharter-12 PLAY-dConvergedCharter-20 PLAY-dConvergedCharter-21 |

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
    `tools/unattended/unattended.test.sh:15431`, `:15551`), and every other line AC2's command prints
    at the pass's base is deleted or re-worded, the list DERIVED there (at `52945ea0d` also the comments
    `unattended.sh:10259`, `:11220` and `unattended.test.sh:5373`, and the `unset -f` at `:15467`);
    each caller reads every gate key, folded
    or `mechanic`, at the revision it reads today through `policy.py legacy .githooks/gate-env.sh
    --rev <sha> --key <KEY>`, and a `.unattended.conf` key at R through `policy.py legacy
    .unattended.conf --rev <sha> --key <KEY>`, under the inline `resolve_kit_dir` `pre-push:777-814`
    already carries for `platforms.provision` (`:825`, shared interface I4). `legacy` prints the
    policy file's value at `<sha>` where that file sets it, else the home's own line at `<sha>`
    (PLAY-dConvergedCharter-11 S3, its AC8), so a remote tip R from before the fold, the remote's tree
    on every first push after an `update` and on gov's own landing push, still reads the values R
    declares; `policy.py get --rev`, which reads only the policy file and else the catalogue default
    (`resolve`, `tools/policy/policy.py:752-757`, `:687-707`), reads no revision another tree may hold
    unfolded. Each caller keeps every arm of the reader it replaces: in `read_policy_at`
    (`pre-push:1443-1466`) an empty or all-zero R reads `park` with its "no tip" line before any read,
    since `legacy --rev` refuses a sha naming no commit; `legacy` printing no `INHERITED_RED` at R,
    the gate file absent or silent and the policy file unset, reads `land` with the line naming the
    kit default; a value outside `park land` reads `park`; and a non-positive or non-numeric
    `INHERITED_RED_MAX_AGE` reads as no bound;
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
    by commit: one `cat-file --batch-check` per home over the commits, then, per DISTINCT pair of
    blobs, `render_folded_lines(repo, <sha>, ".memory-tree.conf")` in-process, the policy kit reached
    by the inlined `resolve_kit_dir`, which takes the policy blob's `memory-tree.backlog-mode` where it
    sets one, else the conf blob's line; its second caller, `migrate_backlog.py:1325`, takes the result
    unchanged;
  - `tools/run-gates/held_halves.py`'s `resolve_wsl_host` (`:210-238`) parses the gate file's
    `GATE_WSL_MIRROR_DEFAULT`, a `mechanic`, and `GATE_WSL_PARITY_RUNS` from one `policy.py legacy
    .githooks/gate-env.sh` read at `HEAD` in place of the file's text, as unit 11 S3 reads a folded key,
    never `get` at the landed revision; a non-zero exit refuses through `print_refusal` (`:69`),
    naming `policy.py legacy` and its exit, and a blank count keeps its refusal (`:234-236`);
  - govkit's conf-key gap check `read_conf_key_gaps` (`tools/govkit/govkit.py:4943`, called by `check`
    at `:5484` and `update` at `:11897`) reads a kit's assignments from `policy.py legacy
    <[config].file>` in place of the file, so the `*_keys` lists of every kit whose `[config].file` is
    a folded home name the keys that output yields: DERIVED at the pass, at base
    `tools/{codebase-map,drift-audit,memory-recall,memory-tree,process-monitor,roles,runlog,unattended}/kit.toml`,
    of which `roles` and `runlog` declare only `optional_keys`;
  - the straggler guard (`.githooks/straggler-guard.sh`), which reads `BACKLOG_MODE` per commit
    (`read_conf_modes`, `:124-146`) and at the default branch's tip (`:215-229`), reads both homes
    keyed by commit by `read_modes`' rule: one `cat-file --batch-check` over each commit's
    `.governance/policy.toml` and `.memory-tree.conf`, then, per DISTINCT pair of blobs, the policy
    blob's `[memory-tree]` table's `backlog-mode` line, read by `read_policy_backlog_mode` beside
    `read_conf_value` (`:105-121`), winning, else the conf blob as today; the tip read the same over
    `$ref`. It stays python-free, as its header rules (`:27`, `:85`), a shell parse of the policy file
    beside `policy.py`, the recorded exception to its one reader (§8 F3, the owner's). A policy file spelling the key in
    another TOML shape reads as unset there, which can only make the layer instruct where it need
    not, the direction its no-conf default already takes (`:129-131`). The guard's suite holds the
    read to `policy.py legacy .memory-tree.conf --rev <sha> --key BACKLOG_MODE` at each commit, and to
    `policy.parse_policy` over one table of policy-file spellings, as `read_conf_value` is held to
    `parse_conf` (`:84-89`);
  - regen's `check_when` (`tools/run-gates/regen.py:140-146`), which reads a descriptor's `when =
    "<conf>:<KEY>=<value>"` (`tools/memory-tree/kit.toml:492`, `:501`) from the conf's text and skips
    the row when it fails (`:186`), reads `<KEY>` through `policy.py legacy <conf> --root <root> --key
    <KEY>`, captured, a failing call refusing naming the row, so the two `{memory_root}/backlog`
    generated rows stay declared once `BACKLOG_MODE` leaves the conf;
  - the kit-placeholders leg's second arm (`extract_conf_keys`, `tools/check-kit-placeholders.py:194`)
    adds to a kit's key set every `KEY` `policy.py legacy <[config].file> --keys` prints
    (PLAY-dConvergedCharter-11 S3), never reading the catalogue's `legacy` field itself, so a template
    spelling a folded key's value still reds once the key leaves the shipped example.
  Each re-pointed shell caller captures the read and tests its exit before binding, the shape
  PLAY-dConvergedCharter-11 S4 states, so a missing python or kit refuses naming the reader. The legs
  `pre-push self-test`, `transition-audit arms` and `straggler-guard arms` add
  `{prefix}/policy/policy.py` to their `guard` in `tools/gate-legs.json`, as unit 11 S4 does for its
  suites. Observed by AC1, AC2, AC3, AC4, AC5, AC6, AC7, AC10, AC11 and AC12.
  **Readers:** by name: `.githooks/pre-push`, `tools/push-main.sh`, `tools/run-gates/post-merge.sh`,
  `tools/unattended/unattended.sh`, `tools/push-main.test.sh`, `.githooks/pre-push.test.sh`,
  `tools/unattended/unattended.test.sh`, `tools/lib/resolve-python.test.sh`, `tools/policy/README.md`,
  `tools/policy/policy.py` (`:25`, `:1138`, `scan_gate_readers`), `tools/memory-tree/transition_audit.py`,
  `tools/memory-tree/migrate_backlog.py`, `tools/run-gates/held_halves.py`, `tools/govkit/govkit.py`,
  `tools/check-kit-placeholders.py`, `.githooks/straggler-guard.sh`, `tools/run-gates/regen.py`,
  `tools/gate-legs.json`, and the
  registries the re-points change by count: `memory/project/spawn-idiom-sites.txt`, whose
  `pure-fn-subst` rows count `.githooks/pre-push` 10, `tools/push-main.sh` 1, `post-merge.sh` 3 and
  `unattended.sh` 41 (`:26`, `:179`, `:196`, `:298`), `substitution-fed-loops.txt` and
  `temp-name-sites.txt`, each re-derived by its scanner in the commit that changes its file. by value:
  every hit at the pass's base of
  `python check_policy.py --readers read_policy_key --kind value`, and `tools/policy/policy.py`'s
  `derive_legacy_homes`, whose gate-file rows `lists` re-derives from the re-pointed calls.
- **S2** — The held keys moved. PLAY-dConvergedCharter-11 S2 leaves in its home, and in its kit's
  shipped example, the keys its HELD RULE names; that unit's S2 states the rule once, and this unit
  cites it and never restates it (§8 F2). At base it names `BACKLOG_MODE`, `GATE_WSL_PARITY_RUNS`, and
  the required keys no `[config].defaults` holds, DERIVED again at unit 11's pass. Each moves in the
  two commits unit 11 S2's commit route gives a policy-file change, since the policy guard admits no
  agent commit of `.governance/policy.toml` (`tools/policy/guard.py:5-12`): commit N, the owner's from
  a terminal, writes the key's value to gov's `.governance/policy.toml` under its folded name, its home
  line still in place, so every reader reads the same value; commit N+1, the agent's, re-points its
  reader, takes its line out of gov's home and the shipped example, the line becoming its row's
  `usage`, re-runs `python policy.py mirror --write` and `python policy.py lists --write`, deletes that
  reader's transitional `FOLDED_HOME_EXEMPT` row, and rewords the gate file's documentation line
  `#   GATE_WSL_PARITY_RUNS=` (`.githooks/gate-env.sh:82`) to name `gate.wsl-parity-runs` in the policy
  file, as unit 11 S2 rewords the others. The held keys of several readers may share one commit N.
  The four copies' keys are not held: each copy reads at R (`pre-push:1449`, `:1743`,
  `unattended.sh:9718`, `:10359`) or at the landed tip (`push-main.sh:430`), which on the run branch is
  the remote's unfolded tree until the landing that carries this unit too, and S1's `legacy --rev`
  reads both homes there. Once every reader of S1 is re-pointed the table holds its two permanent
  rows, `read_modes`, which reads a home's history by revision, and the `.githooks/pre-push` source of
  the gate file, which binds only `mechanic` keys (unit 11 S5). Observed by AC7 and AC8.
  **Readers:** by name: the readers of S1, `tools/policy/legacy-homes.txt`, and
  `tools/policy/policy.py`, whose lists verb alone drains it. by value: `FOLDED_HOME_EXEMPT` in
  `tools/policy/check_policy.py`, whose transitional rows leave, and the folded readers
  PLAY-dConvergedCharter-11 S4 re-pointed, which read each held key from the policy file once it moves,
  through `policy.py legacy`.
- **S3** — The house-file arm, `arm_house_readers`, the red on the house-file fallback of
  `roles_lib.load_policy`, which leaves with the seed. It is one more row of `ARMS`
  (`tools/policy/check_policy.py:740`) over the existing scanner, never a scanner of its own:
  `arm_single_reader` (`:631`) gains an optional `exempt` set of file paths it does not grade. Its
  `reader_dir` stays the policy kit, so the policy kit's own directory is skipped as it is for the
  mirror and limits rows (`derive_code_files`, `:617-623`): the row's own `const="load_policy"` and
  every fixture plant `check_policy.py` writes sit where the arm never grades, so it cannot red on its
  own source. The row reads `arm_single_reader(repo, "<tool-root>/roles/house/policy.toml", kit,
  const="load_policy", exempt={<roles_lib.py>} | HOUSE_MIGRATORS)`, `roles_lib.py` found through the
  inlined `resolve_kit_dir("roles", "roles_lib.py", here)`. So a code line, never a comment, a docstring
  or a self-test's data, in any file outside the policy kit but `roles_lib.py` and the migrators that
  reads the house file or names `load_policy` reds. `HOUSE_MIGRATORS` is declared once, in
  `check_policy.py`, and is the set the migration needs after the seed leaves:
  `tools/govkit/steps/house_seed.py` (PLAY-dConvergedCharter-21 S1) and
  `tools/playbook/adopt_declarations.py` (`derive_house_proposals`, DEPL-dShippedRelease-28 S2), each
  required to spell `house/policy.toml` literally so `derive_readers` still lists it under the needle
  `house/policy.toml` (`HOUSE_ANCHOR`, `tools/policy/policy.py:1119`) that PLAY-dConvergedCharter-21 AC6
  runs. This unit's AC9 plants come from `check_policy.py`'s fixture verb, inside the policy kit;
  PLAY-dConvergedCharter-21's plants of the step sit in `tools/govkit/selftest.py`, which
  `derive_code_files` already skips as a self-test.
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
- `drift_report.py`'s `LANGS` history readers, by revision but found by `derive_readers` in code:
  PLAY-dConvergedCharter-11 S4.
- Running the unattended kit's suites: waived for this build's landing (README rule 8).

### Edges

- **consumes-from** `PLAY-dConvergedCharter-11` — `render_folded_lines` behind `policy.py legacy`, the folded key names with each catalogue row's `legacy` field and `legacy --keys`, the one map the placeholder arm reads, `derive_readers` with its `--readers` CLI, `FOLDED_HOME_EXEMPT` with its two permanent rows and the transitional rows S2 drains, the held keys S2 moves by the held rule that unit's S2 states, and its commit route for a policy-file change, the owner's terminal commit then the agent's mirror; without it there is no verb to re-point to and no key to read
- **hands-off** `PLAY-dConvergedCharter-12` — `read_policy_key`, the copy in `tools/unattended/unattended.sh` S1 deletes and re-points before that unit removes the kit, so its P3 probe reads no copy
- **hands-off** `PLAY-dConvergedCharter-20` — `read_conf_key_gaps`, re-pointed to `policy.py legacy`, and the pre-push hook's `GATE_DOC_PATHS` and `GATE_POST_MERGE` reads through `policy.py legacy .githooks/gate-env.sh --rev <sha> --key`, which read `gate.doc-paths` and `gate.post-merge` where the policy file sets them and the gate file's line where it does not, which that unit's gate-file step relies on at an adopter
- **hands-off** `PLAY-dConvergedCharter-21` — `arm_house_readers`, armed when the seed retires, its reach every code file outside the policy kit, which holds the arm's own constant and plants, and `HOUSE_MIGRATORS`, the exempt paths that unit's AC6 passes as `--except` beside `tools/policy/check_policy.py`
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
- `policy.py get` takes `--rev`; `policy-shim.sh get` does not. `get --rev` reads only the policy file
  at that revision, else the catalogue default (`policy.py:752-757`, `:687-707`), and refuses a sha
  naming no commit, exit 2; read at `552333463` for the audit's fold.
- `.githooks/straggler-guard.sh` reads `BACKLOG_MODE` per commit and at the default branch's tip,
  python-free by its header (`:27`, `:85`); regen's `check_when` reads the descriptors' `when` rows
  from the conf's text (`regen.py:140-146`); neither spells a home `derive_readers` can see in code.
- `read_conf_key_gaps` parses the conf file's text line by line with `parse_conf_assignment`, a key in
  `[config].defaults` never absent; `held_halves.parse_conf` parses the gate file's text strictly.

### The order

One pass, after PLAY-dConvergedCharter-11 and before PLAY-dConvergedCharter-12: each reader of S1 is
re-pointed, its held keys moved and its transitional `FOLDED_HOME_EXEMPT` row deleted by S2's two
commits, the owner's terminal commit N of the values and the agent's commit N+1 of the rest, then S3's
row. Every re-point reads the same values before and after its held keys move, because `legacy` falls
back to the home for a key the policy file does not set (unit 11 S3), and commit N leaves each line in
place.

### Inventory

Minted: `arm_house_readers`, `HOUSE_MIGRATORS` and the `exempt` parameter of `arm_single_reader`,
each `OK` at `d8a12f046` by `python tools/lexicon/lexicon.py --suggest <name> --as py.function`, as
PLAY-dConvergedCharter-11 §4 recorded them before the split; `read_policy_backlog_mode`, the straggler
guard's policy-blob read, `OK` at `52945ea0d` by `--suggest read_policy_backlog_mode --as sh.function`,
a name `govkit.read_policy_value` (`tools/govkit/govkit.py:274`), another contract, does not share.
Nothing else is named here.

### Files touched (estimate)

- `.githooks/pre-push`, `.githooks/pre-push.test.sh`, `tools/push-main.sh`, `tools/push-main.test.sh`
- `tools/run-gates/post-merge.sh`, `tools/run-gates/held_halves.py`, `tools/lib/resolve-python.test.sh`
- `tools/unattended/unattended.sh`, `tools/unattended/unattended.test.sh`
- `tools/policy/policy.py`, `tools/policy/check_policy.py`, `tools/policy/README.md`,
  `tools/policy/legacy-homes.txt` (regenerated)
- `.governance/policy.toml`, `.governance/policy.json` (the mirror, regenerated)
- `.memory-tree.conf`, `.unattended.conf`, `.githooks/gate-env.sh` (the held lines), and any other
  home the held set DERIVED at the pass names
- `tools/memory-tree/.memory-tree.conf.example`, `tools/unattended/.unattended.conf.example` (the held
  lines)
- `tools/memory-tree/transition_audit.py`, `tools/govkit/govkit.py`, `tools/check-kit-placeholders.py`
- `.githooks/straggler-guard.sh`, `.githooks/straggler-guard.test.sh` (the `both-homes` case),
  `tools/run-gates/regen.py`
- `memory/project/spawn-idiom-sites.txt`, `memory/project/substitution-fed-loops.txt`,
  `memory/project/temp-name-sites.txt` (re-derived by their scanners)
- the `kit.toml` of each kit whose `[config].file` is a folded home, DERIVED at the pass:
  `tools/{codebase-map,drift-audit,memory-recall,memory-tree,process-monitor,roles,runlog,unattended}/kit.toml`
  at base

### Alternatives rejected

- **`policy-shim.sh get` for the shell reads.** It takes no `--rev`, and the hook reads at R.
- **`policy.py get --rev` for a folded gate key at R.** It reads R's policy file alone, so a pre-fold
  R's declared `INHERITED_RED=park` reads `land` and a push can land over an inherited red, and it
  refuses a null sha where the old reader read `park`.
- **The straggler guard spawning `policy.py legacy --rev` per blob pair.** Its header rules it
  python-free (`straggler-guard.sh:27`, `:85`); and a read of the mirror blob in shell is a second
  reader of the mirror, which `arm_mirror_readers` reds. The narrow `read_policy_backlog_mode` beside
  the guard's own conf parser, held to `legacy` and `parse_policy` by its suite, is the shape left,
  as the owner ruled (§8 F3).
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

- security — no reader parses a policy home in shell any more but the straggler guard's
  `read_policy_backlog_mode`, one key of committed blobs, parity-held, the owner's recorded exception
  (§8 F3);
  every other reads through the policy kit's reader, as committed at `--rev`, at R or at `HEAD`.
- perf / scale — one interpreter start per read in each hook; `read_modes` stays two batch processes
  per home over the whole history.
- error / empty / loading states — a reader whose `legacy` call fails refuses naming the
  reader, exit 2 (unit 11 S4's capture shape); an absent key prints nothing and each caller's own
  default stands, as an absent line did; a remote with no tip reads `park` before any read, as
  `read_policy_at` did.
- observability — the `--decide` line names the reading it took; the house-file arm prints `unarmed`
  while the seed is present.
- risks — post-merge on a host where only the gate file's `GOV_PYTHON` names a working python now
  refuses, naming `GOV_PYTHON` and the remedy, where it used to run (S1). Between unit 11's pass and
  this one the placeholder arm's key set misses the keys unit 11 dropped from the examples; nothing
  lands between them, the build landing once at its close. Each held key's value needs the owner's
  terminal commit (S2).
- testing — the fixtures of §6 and the arms of §7.
- migration — gov's tree only; adopters: PLAY-dConvergedCharter-20.
- user docs — `help/policy.md` is PLAY-dConvergedCharter-11's; this unit changes no reading it states.

## 6. Acceptance criteria

The fixture verb is PLAY-dConvergedCharter-11's, `python check_policy.py --fixture <case>`
(`check_policy.py:4577`, `--fixture [--strict-from <dir>] [<case>]`), whose runner writes the case's
scratch repository under `%TEMP%` with a short name.

- **AC1** — When a scratch clone of gov at this unit's parent commits `gate.inherited-red = "park"` in
  `.governance/policy.toml` on its remote tip, `INHERITED_RED=park` folded there in place of
  `.githooks/gate-env.sh:103`'s `land`, and runs `.githooks/pre-push --decide` with `<tip>
  <remote-sha>`, the combined output names `inherited-red policy` reading `land` before the re-point
  and `park` after; with `<remote-sha>` all zeros, a remote with no tip, it reads `park` with its "no
  tip" line and no `legacy` refusal; and over a remote tip R from before the fold, whose
  `.githooks/gate-env.sh` declares `INHERITED_RED=park` and whose policy file sets no
  `gate.inherited-red`, it reads `park`, and R's `INHERITED_RED_MAX_AGE=10` is the bound it names.
  Red when: the hook still reads `.githooks/gate-env.sh` at R alone after the re-point, a pre-fold R's
  declared value reads as the catalogue default, or a remote with no tip is refused.
  fixture: built under `%TEMP%` with a short name; the clone's remote is a second local clone.
- **AC2** — When `python check_policy.py --readers read_policy_key --kind value` runs over gov's tree
  after S1, it exits 0 and prints no reader outside the memory root, `tools/policy/policy.py` and
  `tools/policy/README.md` among the files it no longer names; over a scratch copy that keeps one copy
  in `tools/push-main.sh`, it exits 1 naming that file and line. The run passes no `--except`, since
  every fixture plant of the name is assembled at run time (`'read_policy' + '_key'`,
  PLAY-dConvergedCharter-11 AC6), this unit's scratch copy included.
  Red when: a copy, a comment naming it or a parity arm comparing it survives the re-point, or a
  fixture spells the name literally.
- **AC3** — When `read_modes` runs over the `both-homes` fixture, whose first commit holds
  `BACKLOG_MODE=shards` in the conf and no policy value and whose second sets
  `memory-tree.backlog-mode = "builds"` and drops the line, it returns `shards` then `builds`, each
  equal to `policy.py legacy .memory-tree.conf --rev <sha> --key BACKLOG_MODE` at that commit.
  Red when: a commit whose policy blob sets the mode reads the conf blob's absence as `shards`, or
  `read_modes` and `legacy` answer one commit differently.
- **AC4** — When `python held_halves.py` resolves its parity count over the `parity` fixture, which
  commits `gate.wsl-parity-runs = 5` in the policy file and `GATE_WSL_PARITY_RUNS=3` in the gate file,
  it reads 5; on a scratch clone of gov after S2 whose remote's default branch predates the move, it
  reads gov's count from the policy file at `HEAD`; and with `policy.py` replaced by one exiting 3, it
  refuses naming `policy.py legacy` and `exit 3`.
  Red when: the working tree's gate file still wins, the count is read at the landed revision, or a
  failed read is not refused.
  fixture: the clone under `%TEMP%` with a short name; its remote a second local clone.
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
  memory-tree kit whose `.memory-tree.conf` assigns no `FAMILIES`, a key `required_keys_gate` names
  (`tools/memory-tree/kit.toml:82`) and no `[config].defaults` holds, and whose policy file sets
  `memory-tree.families`, it prints no `required key FAMILIES is ABSENT` line (`govkit.py:5488`); with
  the policy value removed too, it prints that line; before S1, with the policy value set, it prints
  that line.
  Red when: the gap check reads the conf file's text alone, so a folded required key reads absent.
  fixture: the target under `%TEMP%` with a short name, the kit installed by `govkit.py apply`.
- **AC8** — When `python policy.py lists --write` runs over gov's tree after S2, `grep -vc '^#'
  legacy-homes.txt` prints 14, every row a `mechanic` row of `.githooks/gate-env.sh`, one of the six
  `.unattended.conf` extension rows or a house row; `grep -cE '^#\s+GATE_WSL_PARITY_RUNS='
  .githooks/gate-env.sh` prints 0; and `python check_policy.py` prints exactly two exempt rows of
  `arm_folded_homes`, `tools/memory-tree/transition_audit.py` `read_modes` and the `.githooks/pre-push`
  source of the gate file, and no finding.
  Red when: a held key stays in its home, or a transitional exempt row outlives its reader's re-point.
  figure: PINNED at `d8a12f046`, 6 mechanic rows, 6 extension rows and 2 house rows.
- **AC9** — When `python check_policy.py` runs over the `house-reader` fixture, a tree with no house
  file and a planted Python file calling `load_policy(`, `arm_house_readers` reds naming it; over
  `house-seed`, the same tree with the seed present, it prints `house-file arm: unarmed`; over
  `house-migrators`, the seedless tree holding the two `HOUSE_MIGRATORS` planted, `house_seed.py` and
  `adopt_declarations.py`, that each read `tools/roles/house/policy.toml`, it is green, and the same
  read planted in `tools/roles/check_roles.py` reds naming that file; and over gov's tree with the seed
  absent from a scratch clone, the arm names no file under `tools/policy/`, its own row's
  `const="load_policy"` and its fixture plants included.
  Red when: a reader of the house file passes once the seed is gone, a migrator in
  `HOUSE_MIGRATORS` reds, or the arm reds on its own source.
- **AC10** — When `read_conf_modes`, sourced from `.githooks/straggler-guard.sh`, runs over a `both-homes`
  scratch repository whose first commit holds `BACKLOG_MODE=builds` in `.memory-tree.conf` and no policy
  value and whose second sets `memory-tree.backlog-mode = "builds"` in `.governance/policy.toml` and
  drops the line, it prints `builds` alone, the tip read at the second reads `builds`, each equal to
  `policy.py legacy .memory-tree.conf --rev <sha> --key BACKLOG_MODE` there, no python starts inside
  the guard, and `read_policy_backlog_mode` and `policy.parse_policy` agree on every row of the
  spelling table.
  Red when: a commit whose policy blob sets the mode reads the conf blob's absence as `shards`, the
  guard spawns python, or a spelling reads differently in the two parsers.
  fixture: the repository under `%TEMP%` with a short name.
- **AC12** — When `python -c` loads `tools/gate-legs.json` after S1, the `guard` of `pre-push
  self-test`, `transition-audit arms` and `straggler-guard arms` each holds `{prefix}/policy/policy.py`.
  Red when: a suite re-pointed through `policy.py legacy` is selected by a guard that misses it.
- **AC11** — When `python tools/run-gates/regen.py --list` runs over a scratch clone of gov after S2,
  whose `.memory-tree.conf` assigns no `BACKLOG_MODE` and whose policy file sets
  `memory-tree.backlog-mode = "builds"`, it lists the two `{memory_root}/backlog` generated rows of
  `tools/memory-tree/kit.toml:492` and `:501`; with the policy value removed it lists neither.
  Red when: a `when` row reads the conf's text alone, so a folded key silently skips its rows.
  fixture: the clone under `%TEMP%` with a short name.

## 7. Gates

`policy fixtures` · `policy check` · `run-gates canary` · `transition-audit arms` · `straggler-guard arms` · `shell hygiene (a fork spent on builtin work)` · `shell hygiene (a loop fed by a command substitution)` · `shell hygiene (a fixed-name temp renamed into place)` · `pre-push self-test` · `pre-push bar self-test` · `push-main self-test` · `held-halves selftest` · `python resolver (behaviour + inline parity + idiom ban)` · `govkit selftest` · `govkit refusal join` · `govkit acceptance matrix` · `kit placeholders (a declared token its adopter substitutes)` · `kit-placeholders self-test` · `codebase-map kit selftest` · `codebase-map gate coverage` · `codebase-map adopter e2e` · `measure-legs selftest` · `recall floor` · `recall floor arms` · `lexicon selftest` · `runlog selftest` · `unattended kit gate` · `memory hygiene` · `spec tokens (a spec's own names resolve)` · `kit/dogfood doc parity` · `pre-push run-log line` · `run-gates run-log line`

The unattended kit's suites are waived for this build's landing (README rule 8); the parity arms S1
deletes there are named for the close. The arms below are declared for the main loop's close.

New arm: tools/policy/check_policy.py · covers AC2 AC3 AC8 AC9 · the `both-homes` and house fixture cases and gov's tree run with `read_modes` reading the conf blob alone, a transitional exempt row left standing, and `arm_house_readers` grading while the seed is present, exempting nothing, or grading the policy kit's own files · none
New arm: tools/lib/resolve-python.test.sh · covers AC6 · post-merge's two inlined blocks as `PARITY_ROWS` rows, staged red by one byte changed in a copy · none
New arm: .githooks/pre-push.test.sh · covers AC1 · the inherited-red read staged against R's policy file alone in place of `policy.py legacy --rev`, and with the null-sha arm removed · none
New arm: .githooks/straggler-guard.test.sh · covers AC10 · the `both-homes` case and the policy-file spelling table, staged red with `read_conf_modes` reading the conf blob alone and with one byte changed in `read_policy_backlog_mode` · none
New arm: tools/run-gates/held_halves.py · covers AC4 · the `parity` case and a failing `legacy` read, staged red with the count read from the gate file's text and with a non-zero exit read as a blank count · none
New arm: tools/run-gates/run-gates.test.sh · covers AC11 · a `--regen-list` case over a folded tree, staged red with `check_when` reading the conf's text alone · none
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
- **F3 — How does the straggler guard read a commit's policy blob?** (a) `read_policy_backlog_mode`, a
  shell parse of the one `[memory-tree]` `backlog-mode` line, held to `policy.parse_policy` over a
  spelling table and to `legacy --rev` at each commit, as `read_conf_value` is held to `parse_conf`;
  an exception to TOOL-dGroundRules-2's one reader of the policy file; (b) one `policy.py legacy
  .memory-tree.conf --rev <sha> --key BACKLOG_MODE` per distinct blob pair holding a policy blob, under
  inlined `resolve_python` and `resolve_kit_dir`, against the guard's python-free header rule
  (`straggler-guard.sh:27`, `:85`). (a) keeps the hook python-free, its failure direction the
  no-conf default's (instruct where it need not); (b) keeps one reader but adds a launcher and two
  `PARITY_ROWS` rows to a git hook.
  RESOLVED (owner, 2026-11-04): (a), the parity table the recorded exception to one reader of the
  policy file, ruled in
  `memory/builds/dConvergedCharter/prompts/2026-11-04-prompt-PLAY-dConvergedCharter-1-owner-decisions.md`,
  "After round 4 of the spec-audit chain".
  widens: none · relaxes: none

## 9. Revision log

- rev-1 · 2026-11-04 · initial draft: S1 and S3 moved from PLAY-dConvergedCharter-11 S4 and S8 by the
  owner's split ruling,
  `memory/builds/dConvergedCharter/prompts/2026-11-04-prompt-PLAY-dConvergedCharter-1-owner-decisions.md`
  ("fold vs re-points"), with that unit's AC5, AC7, AC9, AC11 and AC15 as AC1, AC9, AC4, AC5 and AC6,
  the `read_modes` half of its AC2 as AC3, the after-S4 half of its AC6 as AC2 and its AC1's figure as
  AC8; S2, AC7 and §8 F2 new, the held keys the split owes (F2); F1 is that unit's F5.
- rev-2 · 2026-11-04 · S1 S2 S3 §3 §4 §5 AC1 AC2 AC7 AC8 AC9 AC10 AC11 §7 · folded
  `2026-11-04-review-PLAY-dConvergedCharter-11-spec-audit-round1` findings 11 and 40 (every gate key at
  R read through `policy.py legacy --rev`, never `get --rev`, the null-sha, absent-file and
  outside-the-set arms of `read_policy_at` kept, AC1's no-tip and pre-fold-R cases), 2 (S2 cites unit
  11 S2's held rule, S1's kit list derived from the kits whose conf is a folded home), 10 (each held key
  moves by unit 11 S2's commit route, the owner's terminal commit then the agent's), 17 (two permanent
  exempt rows, AC8), 3 and 30 (the house arm's reach skips the policy kit, which holds its own const
  and plants, AC9; the migrators spell the needle unit 21 AC6 runs, S3's plants sentence corrected), 8
  (AC2 runs with no `--except`, every plant assembled at run time), 12 (AC7 plants `FAMILIES`, a
  required key no default holds), 19 (the fixture verb's grammar), 34 (the spawn-idiom, loop and
  temp-name registries re-derived, their shell-hygiene legs in §7), 35 (`straggler-guard arms` in §7)
  and 45 (the straggler guard and regen's `check_when` re-pointed by revision, AC10, AC11); the
  consumes-from edge to PLAY-dConvergedCharter-11 and the hands-off edges to PLAY-dConvergedCharter-20
  and -21 name what each now carries.
- rev-3 · 2026-11-04 · S1 §3 §4 §5 AC3 AC4 AC10 AC12 §7 §8 · folded
  `2026-11-04-review-PLAY-dConvergedCharter-11-chain-spec-audit-round1` findings 6 (S1's delete-or-reword
  list DERIVED from AC2's command at base), 21 (the straggler guard's read renamed
  `read_policy_backlog_mode`, held to `parse_policy`, §5 corrected, the shell parse put to the owner as
  §8 F3, which the owner resolved (a) on 2026-11-04 in `2026-11-04-prompt-PLAY-dConvergedCharter-1-owner-decisions`,
  "After round 4 of the spec-audit chain"), 22 (`read_modes` reads through `render_folded_lines`, AC3 held equal to `legacy --rev`), 36,
  H1's landed-read class (`held_halves.py` reads `legacy .githooks/gate-env.sh` at `HEAD`, a failed read
  refused, AC4 on a clone whose remote predates the move), 24 (the placeholder arm reads `legacy
  --keys`), 3 (the three legs' guards name `policy.py`, AC12) and 28 (`drift_report.py` named
  unit 11's in §3); AC10 runs the guard's function, not its suite; the consumes-from edge to
  PLAY-dConvergedCharter-11 names `--keys`.

## 10. Reuse audit

The seams extended: PLAY-dConvergedCharter-11's `policy.py legacy`, the one reader every re-point
calls, at `--rev` for each reader keyed by revision; the inline `resolve_kit_dir` the hook already carries (`pre-push:777-814`,
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
