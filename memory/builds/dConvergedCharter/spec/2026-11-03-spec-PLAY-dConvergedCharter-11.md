# PLAY-dConvergedCharter-11 — every kit conf key the retrofit does not convert folded into the policy file, its readers inventoried by value and re-pointed

**Status:** OPEN · rev-1 · 2026-11-03 · node d · Tier-2 · base 0d1c1dda · streams playbook · order 2 · advances PLAY-dConvergedCharter-24

**Carries:** cl-dClosedLoop-0485@43490b62 whole

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-11-03-build-PLAY-dConvergedCharter-1-spec-stage-returns.md](../build/2026-11-03-build-PLAY-dConvergedCharter-1-spec-stage-returns.md) | research | PLAY-dConvergedCharter-1 PLAY-dConvergedCharter-2 PLAY-dConvergedCharter-3 PLAY-dConvergedCharter-4 PLAY-dConvergedCharter-5 PLAY-dConvergedCharter-6 PLAY-dConvergedCharter-7 PLAY-dConvergedCharter-8 PLAY-dConvergedCharter-9 PLAY-dConvergedCharter-10 PLAY-dConvergedCharter-12 PLAY-dConvergedCharter-13 PLAY-dConvergedCharter-14 PLAY-dConvergedCharter-15 PLAY-dConvergedCharter-16 PLAY-dConvergedCharter-17 PLAY-dConvergedCharter-18 PLAY-dConvergedCharter-19 PLAY-dConvergedCharter-20 PLAY-dConvergedCharter-21 PLAY-dConvergedCharter-22 PLAY-dConvergedCharter-23 |
| [2026-11-03-build-PLAY-dConvergedCharter-11-deviation-111.md](../build/2026-11-03-build-PLAY-dConvergedCharter-11-deviation-111.md) | deviation | — |
| [2026-11-03-build-PLAY-dConvergedCharter-11-reuse-scout-c.md](../build/2026-11-03-build-PLAY-dConvergedCharter-11-reuse-scout-c.md) | research | PLAY-dConvergedCharter-12 PLAY-dConvergedCharter-16 PLAY-dConvergedCharter-17 PLAY-dConvergedCharter-20 PLAY-dConvergedCharter-21 PLAY-dConvergedCharter-22 |
| [2026-11-04-build-PLAY-dConvergedCharter-1-agent-ledger.md](../build/2026-11-04-build-PLAY-dConvergedCharter-1-agent-ledger.md) | journal | PLAY-dConvergedCharter-1 PLAY-dConvergedCharter-2 PLAY-dConvergedCharter-3 PLAY-dConvergedCharter-4 PLAY-dConvergedCharter-5 PLAY-dConvergedCharter-6 PLAY-dConvergedCharter-7 PLAY-dConvergedCharter-8 PLAY-dConvergedCharter-9 PLAY-dConvergedCharter-10 PLAY-dConvergedCharter-12 PLAY-dConvergedCharter-13 PLAY-dConvergedCharter-14 PLAY-dConvergedCharter-15 PLAY-dConvergedCharter-16 PLAY-dConvergedCharter-17 PLAY-dConvergedCharter-18 PLAY-dConvergedCharter-19 PLAY-dConvergedCharter-20 PLAY-dConvergedCharter-21 PLAY-dConvergedCharter-22 PLAY-dConvergedCharter-23 |
| [2026-11-03-prompt-PLAY-dConvergedCharter-1-fix-brief.md](../prompts/2026-11-03-prompt-PLAY-dConvergedCharter-1-fix-brief.md) | research | PLAY-dConvergedCharter-2 PLAY-dConvergedCharter-3 PLAY-dConvergedCharter-4 PLAY-dConvergedCharter-6 PLAY-dConvergedCharter-7 PLAY-dConvergedCharter-8 PLAY-dConvergedCharter-12 PLAY-dConvergedCharter-14 PLAY-dConvergedCharter-16 PLAY-dConvergedCharter-17 PLAY-dConvergedCharter-18 PLAY-dConvergedCharter-19 PLAY-dConvergedCharter-21 |
| [2026-11-03-prompt-PLAY-dConvergedCharter-1-spec-brief.md](../prompts/2026-11-03-prompt-PLAY-dConvergedCharter-1-spec-brief.md) | research | PLAY-dConvergedCharter-1 PLAY-dConvergedCharter-2 PLAY-dConvergedCharter-3 PLAY-dConvergedCharter-4 PLAY-dConvergedCharter-5 PLAY-dConvergedCharter-6 PLAY-dConvergedCharter-7 PLAY-dConvergedCharter-8 PLAY-dConvergedCharter-9 PLAY-dConvergedCharter-10 PLAY-dConvergedCharter-12 PLAY-dConvergedCharter-13 PLAY-dConvergedCharter-14 PLAY-dConvergedCharter-15 PLAY-dConvergedCharter-16 PLAY-dConvergedCharter-17 PLAY-dConvergedCharter-18 PLAY-dConvergedCharter-19 PLAY-dConvergedCharter-20 PLAY-dConvergedCharter-21 PLAY-dConvergedCharter-22 PLAY-dConvergedCharter-23 |

<!-- /gen:spec-records -->

## 1. Goal

v2 keeps every key in `.governance/policy.toml`, but five kit confs and the gate environment file still
hold about a hundred keys beside it, on the shrink-only list dGroundRules derived (v2:1126-1134,
v2:2006-2008; RC-3, M7). This unit folds every key that list holds, the retrofit's cutoffs and pins
excepted, into the policy file with a catalogue row, gives every reader one way to read a folded home
both before and after the fold, inventories the readers of a folded key by value over the tree, and reds
any reader that still reads its old home (DA-H5, DA-M6). The house file's `[effort]` and `[gates]`
readers are graded by the same inventory, armed when the seed retires (FA-6).

## 2. Scope (IN)

Build-run precondition, specced and unbuilt at base `0d1c1dda`: TOOL-dBoundRoles-21 S1, S6, S7, which put
the `[effort]` readers on `roles.effort.*` through `read_policy_setting` and the `[gates]` readers on each
role definition's `gates` field. S8 is graded on gov's tree only after PLAY-dConvergedCharter-21 retires
the seed. Every other item needs only the policy reader, which is CLOSED (dGroundRules).

- **S1** — The fold's catalogue rows. Each row of `tools/policy/legacy-homes.txt` whose home is a kit
  conf, and each `owner-policy` row of `.githooks/gate-env.sh`, gains a `[[key]]` row in
  `tools/policy/catalogue.toml`: `name` per §4 "The folded names", the new optional field `legacy =
  "<home> <KEY>"`, `owner = "dConvergedCharter"`, an `allowed` matching the value the reader parses, a
  `summary` and a `usage`. A key read through `policy.py get` (S4) carries the reader's own default as
  its `default`, the reader keeping no empty-value branch of its own; every other row carries `default = {
  derived = "<reader path>'s own default" }`, so no default is spelled twice. `legacy` joins `OPTIONAL`
  (`tools/policy/policy.py:104`) and the shape audit refuses a `legacy` naming no legacy home, a `KEY`
  outside `[A-Z][A-Z0-9_]*`, or one `(home, KEY)` on two rows. Observed by AC1.
- **S2** — Gov's values moved. Each folded key's value in gov's home is written to gov's
  `.governance/policy.toml` under its folded name, and its line leaves the home. A home keeps its
  retrofit keys: `.memory-tree.conf`, `.codebase-map.conf`, `.lexicon.conf` and `.unattended.conf`
  their `_CUTOFF` and `_PIN` keys, `.githooks/gate-env.sh` its six `mechanic` keys. Each kit's shipped
  example or template conf drops the folded keys' lines, which become their rows' `usage`, so a fresh
  install seeds no folded key. `.process-monitor.conf` holds no other key, so it is deleted with its
  template `tools/process-monitor/process-monitor.template.conf` and that template's `[[files]]` row.
  `python policy.py lists --write` then drains `legacy-homes.txt` to the mechanic and house rows, never
  by hand. Observed by AC1.
  **Readers:** by name: `tools/process-monitor/reap.py`, `tools/process-monitor/scope.py`,
  `tools/process-monitor/classify.py`, `tools/process-monitor/procmon-hook.js`,
  `tools/process-monitor/adopt-process-monitor.sh`, `tools/process-monitor/kit.toml`,
  `tools/process-monitor/README.md`, `tools/run-gates/run-gates.sh`, `.github/workflows/remote-ci.yml`,
  `.gitattributes`, `WIRE-INTO-PROJECT.md`, each re-pointed by S4 or re-worded. by value: the same
  files' `PROCMON_` reads, which read S3's output for `.process-monitor.conf`, and
  `tools/policy/policy.py`'s `derive_legacy_homes`, whose kit-conf rows drain.
- **S3** — The both-homes reader, `python tools/policy/policy.py legacy <home> [--rev <rev>] [--key
  <KEY>]`, its function `render_folded_lines(repo, rev, home)`. It prints the home's effective
  assignments as `KEY=<value>` lines, each value shell-quoted: for a key whose catalogue row's `legacy`
  names the home, the policy file's value at the revision `get` reads (the landed revision, or `--rev`)
  where that file sets it, and otherwise the home's own last `KEY=` line; for every other key the home
  assigns, the home's line. The home is read at `--rev` when given and from the working tree otherwise,
  as each reader read it before. A key neither sets prints nothing, so each reader's own default stands.
  `--key <KEY>` prints that one value bare. Keyed by commit: at a commit before the fold the home
  answers, at one after it the policy file, the precedent `read_legacy_fanout` and
  `derive_lowered_limit` (`policy.py:767-807`). Observed by AC2.
- **S4** — The named readers re-pointed, each in this unit:
  - the four copies of `read_policy_key` (`.githooks/pre-push:1426`, `tools/push-main.sh:404`,
    `tools/run-gates/post-merge.sh:171`, `tools/unattended/unattended.sh:9684`) are deleted with their
    byte-identity comments (`pre-push:1416-1421`, `post-merge.sh:170`, `push-main.sh:401-402`) and
    their parity arms (`tools/push-main.test.sh:1007-1011`, `.githooks/pre-push.test.sh:1560`,
    `tools/unattended/unattended.test.sh:15431`, `:15551`); each caller reads a folded key through
    `policy.py get <key> --rev <sha>` and an unfolded `mechanic` key through `policy.py legacy
    .githooks/gate-env.sh --rev <sha> --key <KEY>`, both under the inline `resolve_kit_dir`
    `pre-push:806-830` already carries for `platforms.provision` (shared interface I4);
  - `transition_audit.read_modes` (`tools/memory-tree/transition_audit.py:421`) reads both homes keyed by
    commit: one `cat-file --batch-check` per home over the commits, the policy file's
    `memory-tree.backlog-mode` winning where a commit's policy blob sets it, else `read_mode` over the
    conf blob, as today;
  - `tools/run-gates/held_halves.py` reads `GATE_WSL_PARITY_RUNS` as `gate.wsl-parity-runs` through
    `policy.py get` (`:212-216`), and `GATE_WSL_MIRROR_DEFAULT`, a `mechanic`, through `legacy --key`;
  - govkit's conf-key gap check `read_conf_key_gaps` (`tools/govkit/govkit.py:4943`) reads a kit's
    assignments from `policy.py legacy <[config].file>` in place of the file, so a kit's `*_keys` lists
    in `tools/{codebase-map,memory-tree,roles,runlog,unattended}/kit.toml` name the keys that output
    yields;
  - the kit-placeholders leg's second arm (`tools/check-kit-placeholders.py`) adds to a kit's key set
    every `KEY` a catalogue row's `legacy` names for that kit's `[config].file`, so a template spelling a
    folded key's value still reds once the key leaves the shipped example;
  - every other reader `derive_readers` returns by path for a folded home (§4 "The readers") replaces
    its source or read of the home with S3's output, `eval "$(… policy.py legacy <home>)"` in shell and
    the printed text through its own parser in Python.
  **Readers:** by name: `.githooks/pre-push`, `tools/push-main.sh`, `tools/run-gates/post-merge.sh`,
  `tools/unattended/unattended.sh`, `tools/push-main.test.sh`, `.githooks/pre-push.test.sh`,
  `tools/unattended/unattended.test.sh`, `tools/policy/README.md`. by value: `tools/policy/policy.py`
  (`POLICY_KEY_READ`, `scan_gate_readers`, `:1137-1196`), whose gate-file rows are re-derived by `lists`
  from the keys the home still assigns. Observed by AC4, AC5, AC6, AC9, AC10, AC11.
- **S5** — The red arm, `arm_folded_homes` in `tools/policy/check_policy.py`, one more entry of `ARMS`
  (`:740`): over `CODE_PATHSPECS` (`:313`), outside the memory root, a file that spells a folded row's
  `KEY` as a token and its home's path, and spells neither `policy.py legacy`, `render_folded_lines`
  nor the policy file's path, reds naming the file, the `KEY` and the home. The policy kit's own
  `policy.py` is not graded, as `scan_reader_keys` skips its own module. `READER_SHAPES` (`:425-437`)
  gains the adapter's two call shapes, `policy.py legacy <home>` in shell and `"legacy", "<home>"` in a
  Python argv, and `scan_reader_keys` expands a matched home to every key whose `legacy` names it, so the
  reader-coverage arm counts a folded key as read. Observed by AC4.
- **S6** — The reader inventory (shared interface I1), `derive_readers(repo, needle, kind)` beside
  `scan_reader_keys` (`check_policy.py:481`): every tracked text file outside the memory root, tests,
  help pages and comment lines included, in which `needle` occurs, as a path (`kind = "path"`, at a
  path boundary) or as a token (`kind = "value"`, no `[A-Za-z0-9_]` on its left and none of
  `[A-Za-z0-9_/-]` on its right), returned as sorted `path:line` pairs. Its CLI, `python check_policy.py
  --readers <needle> --kind path|value [--except <path>]…`, prints the readers clause the retiring
  specs write, its by-name and by-value halves (TOOL-dWellOiledMachine-28 S1, S4, S7), and exits 1 while any
  reader outside the `--except` paths survives: the red on a surviving reader every retirement of this
  build observes. Observed by AC6.
- **S7** — `tools/policy/README.md:212-219`'s sentence that the shell parser and its copies "stay as
  they are for the legacy homes" is rewritten: no copy remains, the folded keys are read through `get`
  and a home's other keys through `legacy`. Observed by AC10.
- **S8** — The house-file arm, `arm_house_readers`, the red on the house-file fallback of
  `roles_lib.load_policy`, which leaves with the seed: once `tools/roles/house/policy.toml` is absent from
  the tree, a file other than `tools/roles/roles_lib.py` that calls `load_policy(` or spells
  `house/policy.toml` reds; while the seed is present it prints `house-file arm: unarmed — the seed is
  present (PLAY-dConvergedCharter-21)` and grades nothing, and the line is the arm's
  verdict, never a pass. The re-points of `check_roles.py:367`, `handoff.py:480` and
  `render_agents.py:140` are TOOL-dBoundRoles-21 S7's (deviation 111). Observed by AC7.

## 3. Non-goals (OUT)

- The retrofit's conversions: the `_CUTOFF` and `_PIN` keys stay in `.memory-tree.conf`
  (`RETROFIT_KEY`, `policy.py:1139`), as v2:1133 keeps them.
- The six `mechanic` keys of `.githooks/gate-env.sh`: they stay, read through S3 (§8 F3).
- The house file's retirement, its fallback's removal and gov's defaults in the role definitions:
  PLAY-dConvergedCharter-21. `[effort]` readers on `roles.effort.*`: TOOL-dBoundRoles-21.
- Shipping the fold to adopters as an upgrade step: PLAY-dConvergedCharter-20.
- Removing the unattended kit, which still reads its folded keys through S3 until it goes:
  PLAY-dConvergedCharter-12.
- Running the unattended kit's suites: waived for this build's landing (README rule 8).

### Edges

- **consumes-from** `PLAY-dConvergedCharter-22` — `settings_census.py`, whose run conf and gate environment population this unit re-points from `legacy-homes.txt` rows to the catalogue's `legacy` field, a folded key reading `moved by the fold`
- **hands-off** `PLAY-dConvergedCharter-17` — `derive_readers`, the inventory by value whose `--readers` CLI reds a surviving reader of `/build`
- **hands-off** `PLAY-dConvergedCharter-12` — `derive_readers`, the inventory by path and by value whose `--readers` CLI reds a surviving reader of `tools/unattended/` on the scratch clone
- **hands-off** `PLAY-dConvergedCharter-16` — `derive_readers`, the inventory over `skills/session-kickoff/` and `/session-kickoff`
- **hands-off** `PLAY-dConvergedCharter-21` — `derive_readers`, whose house-file arm `arm_house_readers` arms when the seed retires, and the house file's two `legacy-homes.txt` rows the seed's retirement drains
- **hands-off** `PLAY-dConvergedCharter-3` — `derive_readers`, the inventory by value each record-kind merge lists its readers through
- **hands-off** `PLAY-dConvergedCharter-9` — `derive_readers`, the inventory by path and by value each Skill rename re-points its readers from
- **hands-off** `PLAY-dConvergedCharter-20` — `legacy-homes.txt`, the folded rows and their catalogue `legacy` field, which the upgrade step reads to move an adopter's conf values into its policy file
- **consumes-from** external — TOOL-dBoundRoles-21, the `[effort]` and `[gates]` re-points S8 grades

## 4. Design

### Evidence

Read at `d8a12f046`; no product file differs from base `0d1c1dda`.

- `legacy-homes.txt` holds 115 rows: `.codebase-map.conf` 6, `.lexicon.conf` 2, `.memory-tree.conf` 35,
  `.process-monitor.conf` 6, `.unattended.conf` 53, `.githooks/gate-env.sh` 11 (5 `owner-policy`, 6
  `mechanic`), the house file 2. The fold takes 102 + 5 = 107 rows, PINNED at `d8a12f046`; S1's
  `lists --write` re-derives the remainder.
- No catalogue row names any of the 107 keys (a `grep` of each over `catalogue.toml` finds none), and
  v2's `[policies]` table names only `PROCMON_REAP_MODE`, `RESUME_ATTEMPTS` and `RESUME_TURNS`, as keys
  that stay in their confs until this fold (v2:1127-1128).
- The four `read_policy_key` copies' callers read `INHERITED_RED`, `INHERITED_RED_MAX_AGE`,
  `GATE_POST_MERGE`, `GATE_DOC_PATHS` (`pre-push:1453-1454,1744-1745`), `GATE_POST_MERGE`
  (`push-main.sh:431`), `GOV_GATE_CMD`, `GOV_PYTHON`, `GATE_SELFTESTS` (`post-merge.sh:222,231-232`),
  and `GATE_POST_MERGE`, `GATE_POLICY_FILE`, `INHERITED_RED`, `INHERITED_RED_MAX_AGE`,
  `HELD_CI_WORKFLOW` (`unattended.sh:9718-9743,10360`). Post-merge's three are `mechanic`, so they
  re-point through `legacy --key`, which is what lets the fourth copy go too.
- The confs are sourced or parsed whole: `. "$CONF"` (`unattended.sh:746`), `. "$ROOT/.memory-tree.conf"`
  (`check-memory-hygiene.sh:188`), `tree_lib.parse_conf(text, defaults)` with per-reader defaults
  (`tree_lib.py:135-146`). 72 tracked code files outside the memory root spell `.memory-tree.conf`, 31
  `.unattended.conf` and 15 `gate-env.sh`, PINNED by `git grep -l` at `d8a12f046`.
- `policy.py get` takes `--rev` (`:1346-1355`); `policy-shim.sh get` does not (`:236-239`).
- The `--decide` mode reads `INHERITED_RED` at the remote tip R through `read_policy_at`
  (`pre-push:1443-1466`) and announces `inherited-red policy at <sha8> reads <policy>` (`:1804`); gov's
  value is `land` (`.githooks/gate-env.sh:103`).

### The folded names

| Home | Namespace | Prefix dropped |
|---|---|---|
| `.codebase-map.conf` | `codebase-map` | none |
| `.lexicon.conf` | `lexicon` | none |
| `.memory-tree.conf` | `memory-tree` | none |
| `.process-monitor.conf` | `process-monitor` | `PROCMON_` |
| `.unattended.conf` | `unattended` | none |
| `.githooks/gate-env.sh` | `gate` | `GATE_` |

A key's name is `<namespace>.<KEY>` with the dropped prefix taken off, lower-cased and `_` read as `-`:
`BACKLOG_MODE` is `memory-tree.backlog-mode`, `INHERITED_RED` `gate.inherited-red`, `GATE_DOC_PATHS`
`gate.doc-paths`, `PROCMON_REAP_MODE` `process-monitor.reap-mode`. None collides with a row at base:
the catalogue's `lexicon.*` rows are `pin`, `forced`, `at-commit`, `drift` and `packs`. The `legacy`
field, not the name, is what every reader joins on (shared interface I5).

### The readers

The re-point population is derived, never typed: for each folded home, `derive_readers(repo, <home>,
"path")` over `CODE_PATHSPECS`, less the policy kit's own files. Each hit takes one of three re-points:
a shell reader that sources the home evals S3's output in its place; a Python reader passes S3's output
to its existing parser (`parse_conf`, `parse_conf_assignment`, `held_halves.parse_conf`) in place of the
file's text; a reader of one gate key at a revision calls `get` or `legacy --key`. A reader that also
reads the policy file keyed by commit, as `read_modes` does, reads both homes itself. A file that only
names a home in prose (a comment, a README, a help page) is re-worded where it states where a folded
value lives, and is not graded by S5, which reads code.

### Inventory

Minted: the catalogue field `legacy`; the 107 folded key names; `render_folded_lines`, the verb
`legacy` with `--key`; `derive_readers` and the CLI `--readers`, `--kind`, `--except`;
`arm_folded_homes`, `arm_house_readers`. Naming cell `py.function`: each `OK` by `python
tools/lexicon/lexicon.py --suggest <name> --as py.function` at `d8a12f046`.

### Migration

Gov's tree only, in one pass: S1's rows, then S2's values and `lists --write`, then S4's re-points, then
S5's arm. A tree that still holds its homes, an adopter before PLAY-dConvergedCharter-20's step or a
fixture that plants a conf, reads exactly what it read before, because S3 falls back to the home for any
key the policy file does not set.

### Files touched (estimate)

- `tools/policy/policy.py`, `tools/policy/check_policy.py`, `tools/policy/catalogue.toml`,
  `tools/policy/legacy-homes.txt` (regenerated), `tools/policy/README.md`, `tools/policy/kit.toml`
- `.governance/policy.toml`, `.governance/policy.json` (the mirror, regenerated)
- `.codebase-map.conf`, `.lexicon.conf`, `.unattended.conf`, `.memory-tree.conf`,
  `.githooks/gate-env.sh`, `.process-monitor.conf` (deleted)
- `tools/process-monitor/process-monitor.template.conf` (deleted), `tools/process-monitor/kit.toml`,
  `tools/process-monitor/reap.py`, `tools/process-monitor/scope.py`, `tools/process-monitor/classify.py`,
  `tools/process-monitor/procmon-hook.js`, `tools/process-monitor/adopt-process-monitor.sh`
- `tools/codebase-map/.codebase-map.conf.example`, `tools/memory-tree/.memory-tree.conf.example`,
  `tools/lexicon/kit.toml`, `tools/unattended/.unattended.conf.example`
- `.githooks/pre-push`, `.githooks/pre-push.test.sh`, `tools/push-main.sh`, `tools/push-main.test.sh`
- `tools/run-gates/post-merge.sh`, `tools/run-gates/held_halves.py`
- `tools/unattended/unattended.sh`, `tools/unattended/unattended.test.sh`
- `tools/memory-tree/transition_audit.py`, `tools/memory-tree/tree_lib.py`,
  `tools/memory-tree/check-memory-hygiene.sh`
- `tools/govkit/govkit.py`, `tools/check-kit-placeholders.py`
- `tools/codebase-map/kit.toml`, `tools/memory-tree/kit.toml`, `tools/roles/kit.toml`,
  `tools/runlog/kit.toml`, `tools/unattended/kit.toml`
- every further reader §4 "The readers" derives, named in the build run's `--dispatch --writes`
- `help/policy.md`: the folded keys, the `legacy` verb, and where a kit conf's value now lives

### Alternatives rejected

- **Each reader calling `get` once per key.** The hygiene engine alone reads 35 keys from one conf, and
  `get` is one interpreter start per call; S3 reads a home's keys in one call and keeps each reader's
  parser and defaults.
- **The conf kept as a render of the policy file.** It leaves every reader on the old home, which is
  the red the clause asks for.
- **`policy-shim.sh get` for the shell reads.** It takes no `--rev` (`:236`), and the hook reads at R.
- **Catalogue defaults copied from each reader.** `parse_conf` keeps defaults per reader on purpose
  (`tree_lib.py:138-141`), so one catalogue default would change readers that disagree; §8 F2.
- **Folding the six `mechanic` gate keys.** v2:1130 folds the owner-policy keys only; §8 F3.

## 5. Production-readiness checklist

- security — no reader sources a home any more: S3 prints shell-quoted `KEY=<value>` lines for keys
  matching `[A-Z][A-Z0-9_]*`, and the policy file is read as committed, at the landed revision or R,
  never from the working tree (dGroundRules's reader contract).
- perf / scale — one interpreter start per reader per home in place of a `source`; `read_modes` stays two
  batch processes per home over the whole history.
- error / empty / loading states — an absent home with no policy value prints nothing and each reader's
  default stands, as an absent conf did; a malformed policy file reads as `policy-file.on-invalid` says.
- observability — `policy.py get --explain` names the source of a folded key; `legacy` prints nothing
  it did not read.
- risks — a reader that read its home from the working tree now reads the policy file as committed, so
  an uncommitted policy edit takes effect at its commit; the home's own lines still read from the
  working tree.
- testing — the fixtures of §6 and the arms of §7.
- migration — §4 Migration; adopters: PLAY-dConvergedCharter-20.
- user docs — `help/policy.md`.

## 6. Acceptance criteria

The fixture is `python check_policy.py --fixture <case> <dir>`, which writes a scratch repository under
`%TEMP%` with a short name holding the policy kit and the case's files, committed.

- **AC1** — When `python policy.py lists --write` runs after S2, `grep -vc '^#' legacy-homes.txt` prints
  8, every remaining row is a `mechanic` row of `.githooks/gate-env.sh` or a house row, and
  `python policy.py check` exits 0 over gov's policy file holding the folded values.
  Red when: a folded key is left in its home, or a catalogue row lacks its `legacy` field.
  figure: PINNED at `d8a12f046`, 6 mechanic rows and 2 house rows.
- **AC2** — When `python policy.py legacy .memory-tree.conf --rev <sha>` runs over the `both-homes`
  fixture, whose first commit holds `BACKLOG_MODE=shards` in the conf and no policy value and whose
  second sets `memory-tree.backlog-mode = "builds"` and drops the line, it prints `BACKLOG_MODE=shards`
  at the first and `BACKLOG_MODE=builds` at the second, a `_CUTOFF` key of the conf at both, and nothing
  for a key neither sets; `read_modes` over the two commits returns `shards` then `builds`.
  Red when: the policy file is read without its revision, or the home is not read before the fold.
- **AC3** — When `python policy.py check` runs over the `bad-legacy` fixture, whose catalogue carries a
  row with `legacy = ".memory-tree.conf backlog_mode"`, it exits 2 naming the row.
  Red when: the shape audit admits a `legacy` value outside its grammar.
- **AC4** — When `python check_policy.py` runs over the `old-home` fixture, which plants a shell
  file spelling `BACKLOG_MODE` that sources `.memory-tree.conf`, `arm_folded_homes` reds naming the file,
  the key and the home; over `adapter`, the same file evaling `policy.py legacy .memory-tree.conf`, it is
  green and the reader-coverage arm counts `memory-tree.backlog-mode` as read.
  Red when: a reader of a folded key reads its old home and the arm stays silent.
- **AC5** — When a scratch clone of gov at this unit's parent commits `gate.inherited-red = "park"` in
  `.governance/policy.toml` on its remote tip, `INHERITED_RED=park` folded there in place of
  `.githooks/gate-env.sh:103`'s `land`, and runs `.githooks/pre-push --decide <tip> <remote-sha>`,
  the combined output names `inherited-red policy` reading `land` before the re-point and `park` after.
  Red when: the hook still reads `.githooks/gate-env.sh` at R after the re-point.
  fixture: built under `%TEMP%` with a short name; the clone's remote is a second local clone.
- **AC6** — When `python check_policy.py --readers read_policy_key --kind value` runs over gov's tree
  after S4, it exits 0 and prints no reader outside the memory root; over a scratch copy that keeps one
  copy in `tools/push-main.sh`, it exits 1 naming that file and line.
  Red when: a surviving reader is not named, or a reader under the memory root is.
- **AC7** — When `python check_policy.py` runs over the `house-reader` fixture, a tree with no
  house file and a planted Python file calling `load_policy(`, `arm_house_readers` reds naming
  it; over `house-seed`, the same tree with the seed present, it prints `house-file arm: unarmed`.
  Red when: a reader of the house file passes once the seed is gone.
- **AC8** — When `python policy.py legacy .githooks/gate-env.sh --key GOV_PYTHON --rev HEAD` runs over
  gov's tree it prints the mechanic's value, and `--key INHERITED_RED` prints nothing once it is folded.
  Red when: a mechanic key needs a parser outside the policy kit.
- **AC9** — When `python held_halves.py` resolves its parity count over the `parity` fixture, which sets
  `gate.wsl-parity-runs = 5` in the policy file and `GATE_WSL_PARITY_RUNS=3` in the gate file, it reads 5.
  Red when: the working tree's gate file still wins.
- **AC10** — When `grep -n 'stay as they are' README.md` runs over the policy kit's README it prints
  nothing, and `grep -c 'policy.py legacy' README.md` prints at least 1.
  Red when: the README still says the shell copies stay.
- **AC11** — When `python check-kit-placeholders.py --root <dir>` runs over the `template-leak` fixture,
  a rendered template spelling `BACKLOG_MODE=500` while the example no longer assigns it, it exits 1
  naming the template and the key.
  Red when: the folded key leaves the arm's key set with the example.

## 7. Gates

`policy fixtures` · `kit placeholders (a declared token its adopter substitutes)` · `kit-placeholders self-test` · `govkit selftest` · `govkit refusal join` · `govkit acceptance matrix` · `transition-audit arms` · `straggler-guard arms` · `kit/dogfood doc parity` · `recall floor` · `recall floor arms` · `codebase-map kit selftest` · `codebase-map gate coverage` · `codebase-map adopter e2e` · `process-monitor adopter selftest` · `measure-legs selftest` · `runlog selftest` · `pre-push run-log line` · `run-gates run-log line` · `lexicon selftest` · `lexicon naming predicates` · `unattended kit gate` · `memory hygiene` · `spec tokens (a spec's own names resolve)`

The unattended kit's suites are waived for this build's landing (README rule 8); the parity arms S4
deletes there are named for the close. The arms below are declared for the main loop's close.

New arm: tools/policy/check_policy.py · covers AC2 AC3 AC4 AC6 AC7 · each fixture case run with `arm_folded_homes` matching nothing, `render_folded_lines` skipping the home fallback, the `legacy` shape check removed, and `arm_house_readers` grading while the seed is present · none
New arm: .githooks/pre-push.test.sh · covers AC5 · the inherited-red read staged against the gate file at R in place of `policy.py get` · none
New arm: tools/push-main.test.sh · covers none · the `pm9` parity arm deleted with the copy it compared · none

## 8. Open questions

- **F1 — How does a reader read a folded home?** (a) One verb, `policy.py legacy <home>`, printing the
  home's effective assignments from the policy file and the home keyed by revision, which a reader
  evals or parses in place of its file; (b) every reader calling `get` once per key; (c) the conf kept
  as a render of the policy file. (b) costs one interpreter start per key and drops each reader's own
  default; (c) leaves every reader on its old home, the red the clause names. Rung 3, the most capable
  option. RESOLVED (agent, 2026-11-03, delegated): (a). widens: none · relaxes: none
- **F2 — What is a folded key's catalogue default?** (a) `{ derived = "<reader>'s own default" }`, the
  reader's literal default kept where it is, except for a key read through `get`, whose default moves to
  the catalogue and whose empty branch is deleted; (b) every reader's default copied into the catalogue.
  (b) spells each default twice, and `parse_conf`'s readers disagree on some on purpose
  (`tree_lib.py:138-141`). Rung 3, fewer open names. RESOLVED (agent, 2026-11-03, delegated): (a).
  widens: none · relaxes: none
- **F3 — The `mechanic` gate keys and post-merge's copy.** (a) The six `mechanic` keys stay in the gate
  file and are read through `legacy --key`, so all four copies are deleted; (b) the mechanics folded
  too; (c) post-merge's copy kept, its keys being mechanic. v2:1130 folds "`.githooks/gate-env.sh`'s
  owner-policy keys" only, which removes (b); (c) fails the clause's "four copies … each re-pointed".
  Rung 1, v2 and the clause answer it. RESOLVED (agent, 2026-11-03, delegated): (a). widens: none ·
  relaxes: none
- **F4 — The folded names.** (a) `<namespace>.<key>`, the namespace from the home and the home's own
  prefix dropped where every key of the home carries it (`PROCMON_`, and `GATE_` on the gate file's
  keys that carry it), lower-kebab; (b) the full key kebabed with no prefix dropped. (b) prints
  `gate.gate-doc-paths`. Rung 3, the catalogue's own form (I5). RESOLVED (agent, 2026-11-03,
  delegated): (a). widens: none · relaxes: none
- **F5 — When does the house-file arm grade gov's tree?** (a) Once the seed file is absent, printing
  `unarmed` before; (b) at this unit's landing. Under (b) the arm reds on `render_agents.py:330`, the
  seed's writer, which PLAY-dConvergedCharter-21 removes, and on the readers TOOL-dBoundRoles-21 has
  not re-pointed at HEAD (deviation 111); the clause retires the fallback "with the seed". Rung 1, the
  clause answers it. RESOLVED (agent, 2026-11-03, delegated): (a). widens: none · relaxes: none

## 9. Revision log

- rev-1 · 2026-11-03 · initial draft.

## 10. Reuse audit

The seams extended: `derive_legacy_homes` and `lists --write` (`tools/policy/policy.py:1211`, `:1443`),
which already derive and drain the shrink-only list the fold empties; the catalogue's row grammar and
shape audit (`policy.py:103-104`, `check_shape`); `resolve` and `get` (`:752`, `:1346`), the one reader;
`read_legacy_fanout` and `derive_lowered_limit` (`:767-807`), the keyed-by-commit precedent S3 and
`read_modes` follow; `READER_SHAPES` and `scan_reader_keys` (`check_policy.py:425-437`, `:481`), which
gain the adapter's shapes and `derive_readers` beside them; and the inline `resolve_kit_dir` the hook
already carries (`pre-push:806-830`). `python tools/codebase-map/reuse_lookup.py "read a kit conf key
from the policy file with a fallback to its legacy home keyed by commit"` ranked `load_conf` (fan-in
18, SEAM, one per kit: `map_lib.py`, `lexicon_conf.py`, `recall_conf.py`, `corpus_ids.py`,
`gen_build_index.py`, `gotchas.py`, `routed_commits.py`, `row_grammar.py`, `check-arms.py`,
`drift_report.py`, `process-monitor/scope.py`) and `parse_conf` (`tree_lib.py:135`, `held_halves.py`,
`steps/fanout_cap.py`, SEAM). These are the Python re-point sites §4 "The readers" names: each kit's
`load_conf` takes S3's output in place of its file's text and keeps its parser and defaults, so the
re-point is one call per kit and not one per key. `resolve_kit_dir` (installs 103, SEAM) is the inline
resolver every re-pointed shell reader already carries or gains. Scout C's rows hold at `d8a12f046` with one
disagreement: `post-merge.sh`'s copy reads only `mechanic` keys (`:222,231-232`), which no clause
folds, so it re-points through `legacy --key` (§8 F3).

Recall terms used: `python tools/memory-recall/query.py "how are kit conf keys folded into the policy
file and their readers re-pointed" --terms "legacy-homes conf fold policy.toml catalogue read_policy_key
gate-env owner-policy mechanic reader inventory DA-H5"`
