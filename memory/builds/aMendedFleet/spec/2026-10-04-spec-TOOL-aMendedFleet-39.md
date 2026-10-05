# TOOL-aMendedFleet-39 — a harness-hooks inventory, and `git-hooks` holds real hook names only

**Status:** CLOSED · rev-3 · 2026-10-04 · node a · Tier-2 · base 7af5f564 · streams tooling · ratified 2026-10-04 · order 39 · advances TOOL-aProbedToolkit-15

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-04-build-TOOL-aMendedFleet-39-1-acceptance-ledger.md](../build/2026-10-04-build-TOOL-aMendedFleet-39-1-acceptance-ledger.md) | journal | — |

<!-- /gen:spec-records -->

## 1. Goal

The codebase map inventories the git hooks but not the harness hooks, which are the larger half of
the steering surface: `.claude/settings.json` wires ten hook scripts across five events, and a new
one lands with no dossier claiming it and no gate noticing. The `git-hooks` inventory has the
opposite fault: three of its seven keys are helper files that git never runs. This unit adds a
fail-closed `harness-hooks` inventory read from the settings file and restricts `git-hooks` to the
names git actually runs, so both inventories describe what steers a session and nothing else.

## 2. Scope (IN)

- **S1** — `tools/codebase-map/map_extractors.py` gains `_derive_harness_hooks` and an `EXTRACTORS`
  entry `harness-hooks`, read through the existing `json_artifact_inventory` seam over
  `.claude/settings.json`. Each key is the hook event, one space, and the repo-relative script path
  the command runs, with the `${CLAUDE_PROJECT_DIR}/` prefix stripped. Several matchers wiring one
  script on one event yield one key. Observed by AC1 and AC2.
- **S2** — The extractor fails CLOSED. It raises `MapError` naming the event and the command when a
  hook entry is not a `command` hook, when its command names no `${CLAUDE_PROJECT_DIR}/` script or
  more than one, and when the named script is not a file in the tree. Observed by AC3.
- **S3** — `_git_hooks` keys only the files whose name is in a module constant `GIT_HOOK_NAMES`, the
  hook names `githooks(5)` documents. A file with an extension is a helper and is not a key. An
  extension-less file whose name is not in the set raises `MapError` naming it, because git will
  never run it. The `<stem>.test.sh` exclusion, the flat-directory guard and the empty refusal stay.
  Observed by AC1 and AC4.
  **Readers:** by name: `memory/map/FOUNDATION.md`, `memory/map/features/run-gates.md`,
  `memory/map/features/memory-tree-hygiene.md`, `memory/map/generated/inventories.json` and
  `memory/map/generated/MAP.md` spell the three keys that leave the inventory, which are
  `gate-env.sh`, `straggler-guard.sh` and `pre_push_bar_selftest.py`.
  by value: `compute_coverage` in `tools/codebase-map/map_lib.py`, through
  `tools/codebase-map/test_codebase_map.py`, which reds a claim naming a key the inventory dropped
  until S4 deletes those claims.
- **S4** — The three dossier claims on the helper keys are deleted: `FOUNDATION.md` drops its
  `git-hooks` claim and the prose naming the key; the `run-gates` and `memory-tree-hygiene` dossiers
  drop theirs. Each helper stays reachable through its dossier's path globs. Observed by AC5.
  **Readers:** by name: `memory/map/FOUNDATION.md`, `memory/map/features/run-gates.md` and
  `memory/map/features/memory-tree-hygiene.md`.
  by value: `compute_coverage` alone, through the coverage gate.
- **S5** — Every `harness-hooks` key is claimed by a dossier, per the §4 Inventory table, and none is
  added to `memory/map/baseline.toml`. The dossiers whose claims change refresh their prose in the
  same commit, and the generated `inventories.json` and `MAP.md` are re-rendered. Observed by AC5 and
  AC6.
- **S6** — No claim lands by breaching the dossier cap. `agent-cap` and `unattended` sit within two
  bytes of `DOSSIER_CAP_BYTES` at base, so the claims the §4 table adds to them would push each past
  hygiene check 6's cap. The same commit makes room in each by the smallest prose cut that removes
  measured history a record already holds, citing that record's id; the cap never moves. Shrinking
  the whole near-cap band to 90% stays `TOOL-aMendedFleet-89`'s. Observed by AC7.
  **Readers:** by name: NOT A NAME — the cut removes measured-history prose, not a named thing.
  by value: NO VALUE READERS — the record the cut cites keeps the figures, and no tool reads dossier prose.

## 3. Non-goals (OUT)

- Claiming `pre-commit` and `pre-push`, which stay in the baseline as the backfill they are, and
  moving the `skill-engines` claim between dossiers. Both are claim housekeeping the synthesis lists
  beside this point; neither changes what an inventory enumerates.
- The charter half of `TOOL-aProbedToolkit-15`, where the template oversells what the map guarantees.
  That is a governance-carrier edit and a separate mechanism; §8 F1 hands it to
  `TOOL-aMendedFleet-85`.
- The coverage-number half of `TOOL-aProbedToolkit-8`, in the `map_diff.py` digest. §8 F1 hands it to
  `TOOL-aMendedFleet-86`.
- A `kit-entrypoints` inventory, which the synthesis says not to build yet.
- Validating what a hook DOES. `tools/check-wiring.sh` owns whether a hook is wired, and each hook's
  own suite owns its behaviour.
- A second inventory for the `.githooks/` helper files. No reader asked for one, and each helper is
  already under its dossier's path globs.

### Edges

- **hands-off** `TOOL-aMendedFleet-85` — the template's overclaim, the other half of
  `TOOL-aProbedToolkit-15`, which F1 moves there.
- **hands-off** `TOOL-aMendedFleet-86` — the digest's coverage figure, the half of
  `TOOL-aProbedToolkit-8` F1 moves there.
- **consumes-from** external — `json_artifact_inventory` in the codebase-map kit, already landed.

## 4. Design

### Evidence

Read at base `7af5f564`, whose bytes for every file below equal HEAD's at `fee9f62ba`.

- `_git_hooks` lists every non-test file in `.githooks/`: `commit-msg`, `gate-env.sh`, `pre-commit`,
  `pre-push`, `pre-rebase`, `pre_push_bar_selftest.py` and `straggler-guard.sh`. Three are helpers:
  the report's "3 of its 7 keys are not hooks" holds unchanged.
- `.claude/settings.json` carries five events and twelve command hooks, which collapse to ten
  distinct event and script pairs: `manifest-check.sh` is wired twice on `SessionStart`.
- `json_artifact_inventory` in `tools/codebase-map/map_lib.py` reads a JSON file, raises `MapError`
  on a missing file, malformed JSON or an empty key list, and sorts the keys. It does not de-duplicate,
  so the extract function returns a set.

### Inventory

| Name | Kind | Cell |
|---|---|---|
| `_derive_harness_hooks` | function in `map_extractors.py` | `py.function`; `--suggest` answered OK |
| `GIT_HOOK_NAMES` | module constant, a frozenset | none; constants are not a declared cell |
| `harness-hooks` | inventory id | none |

The claim table, which S5 writes. A key carries a space, so the claims-join refusal for path-shaped
objects does not apply to it.

| Key | Claiming dossier | Why that one |
|---|---|---|
| `PreToolUse tools/hooks/agent-cap.js` | `agent-cap` | its path globs cover the script |
| `PreToolUse tools/hooks/scratch-guard.js` | `agent-cap` | its path globs cover the script |
| `PreToolUse tools/unattended/gate-guard.js` | `unattended` | its path globs cover the script |
| `Stop tools/unattended/stop-guard.js` | `unattended` | its path globs cover the script |
| `StopFailure tools/unattended/stall-recorder.js` | `unattended` | its path globs cover the script |
| `SessionStart tools/process-monitor/procmon-hook.js` | `process-monitor` | its path globs cover the script |
| `PostToolUse tools/process-monitor/procmon-hook.js` | `process-monitor` | its path globs cover the script |
| `PostToolUse tools/memory-recall/recall-opened.js` | `memory-recall` | its path globs cover the script |
| `SessionStart skills/session-kickoff/manifest-check.sh` | `session-kickoff` | no glob covers it; the script is that skill's engine |
| `SessionStart tools/check-wiring.sh` | `FOUNDATION.md` | no glob covers it; it wires every kit |

A key the settings file gains before the pass is claimed by the same rule: the dossier whose path
globs cover the script, else the dossier whose feature the script belongs to, else `FOUNDATION.md`.

### Data model

`GIT_HOOK_NAMES` holds the names `githooks(5)` documents at writing: `applypatch-msg`,
`pre-applypatch`, `post-applypatch`, `pre-commit`, `pre-merge-commit`, `prepare-commit-msg`,
`commit-msg`, `post-commit`, `pre-rebase`, `post-checkout`, `post-merge`, `pre-push`, `pre-receive`,
`update`, `proc-receive`, `post-receive`, `post-update`, `reference-transaction`, `push-to-checkout`,
`pre-auto-gc`, `post-rewrite`, `sendemail-validate`, `fsmonitor-watchman`, `p4-changelist`,
`p4-prepare-changelist`, `p4-post-changelist`, `p4-pre-submit` and `post-index-change`. Its comment
cites the manual page. A hook git adds later fails loudly here as an unknown extension-less name,
and the remedy the error prints is to add the name to the constant.

### Files touched (estimate)

- `tools/codebase-map/map_extractors.py`
- `memory/map/FOUNDATION.md`
- `memory/map/features/agent-cap.md`
- `memory/map/features/unattended.md`
- `memory/map/features/process-monitor.md`
- `memory/map/features/memory-recall.md`
- `memory/map/features/session-kickoff.md`
- `memory/map/features/run-gates.md`
- `memory/map/features/memory-tree-hygiene.md`
- every other dossier under `memory/map/features/`, each gaining an empty `harness-hooks = []` line:
  `parse_dossier` in `tools/codebase-map/map_lib.py` refuses a `[claims]` table that does not carry
  exactly the inventory ids, so a new inventory is a line in every dossier
- `memory/map/generated/inventories.json`
- `memory/map/generated/MAP.md`

### Alternatives rejected

- **Keying a hook by its script path alone.** `procmon-hook.js` runs on two events, and which event
  fires a script is the fact a reader of the steering surface needs.
- **Keying by event, matcher and script.** A matcher edit is not a new moving part, and keying on it
  would churn a claim for every matcher widening.
- **Treating every extension-less file as a hook, with no name set.** It derives without a constant,
  but a misspelt hook would be inventoried as live while git never runs it, which is the fiction the
  inventory exists to refuse.
- **Baselining the new keys.** The baseline is the backfill and only shrinks; unit 40 makes that a
  gate, and claiming ten keys in the dossiers that own their scripts is the remedy the gate prints.

## 5. Production-readiness checklist

- security — N/A — a read of a tracked settings file into a generated inventory; nothing executes it.
- perf / scale — one JSON read and one directory listing, inside a gate that already runs both kinds.
- error / empty / loading states — a missing or malformed settings file, a non-command hook, a command
  with no script and a dangling script each raise `MapError` naming the entry; no settings hook at
  all raises the seam's existing empty-inventory refusal.
- observability — `MAP.md` prints the `harness-hooks` count and its claimants on every render.
- risks — a hook wired by an adopter tool into this tree's settings file now reds the coverage gate
  until a dossier claims it, which is the intended effect.
- testing — AC3 and AC4 stage each refusal in a scratch clone; the real-tree gate runs the extractor
  on every bar after landing.
- migration — N/A — the inventory is derived; the three claim deletions are S4.
- user docs — the touched dossiers, per S5. The kit README lists no project inventory.

## 6. Acceptance criteria

- **AC1** — When `python tools/codebase-map/gen_map.py --check` runs after the unit's commit, it exits
  0, and the `git-hooks` array in `memory/map/generated/inventories.json` holds exactly `commit-msg`,
  `pre-commit`, `pre-push` and `pre-rebase`.
  Red when: a helper file is still a key, or the committed artifact is stale.
- **AC2** — When `grep -o "harness-hooks: [0-9]*" memory/map/generated/MAP.md` runs after the unit's
  commit, it prints the number of distinct event and script pairs in `.claude/settings.json`.
  Red when: the inventory is absent, or a doubly wired script is counted twice.
  figure: DERIVED at the pass by reading the settings file; ten at writing.
- **AC3** — When a scratch clone under the TEMP root has one hook command in `.claude/settings.json`
  rewritten to `node -e 1`, `python tools/codebase-map/gen_map.py --check` in it exits non-zero with
  `harness-hooks` and the event name in its error; and when instead one command names a script path
  that does not exist, the error names that path.
  Red when: the extractor returns keys for either entry.
- **AC4** — When the same scratch clone's hooks directory gains an empty extension-less file named
  `pre-comit`, `python tools/codebase-map/gen_map.py --check` exits non-zero naming it; and when it
  gains an empty file named `helper.sh` instead, the `git-hooks` array is unchanged.
  Red when: the misspelt hook is inventoried, or the helper becomes a key.
- **AC5** — When `python tools/codebase-map/test_codebase_map.py` runs after the unit's commit, it
  exits 0, and `git grep -n -E "^git-hooks = .*(straggler-guard|pre_push_bar_selftest|gate-env)" --
  memory/map` prints nothing.
  Red when: a claim names a key the inventory dropped, or a harness key is unclaimed.
- **AC6** — When `grep -n "PreToolUse" memory/map/baseline.toml` runs after the unit's commit, it
  prints nothing.
  Red when: a harness key was baselined instead of claimed.
- **AC7** — When a `python -c` reader reads `DOSSIER_CAP_BYTES` from `.memory-tree.conf` and the byte
  size of every dossier and of `memory/map/FOUNDATION.md` this unit's commit touched, each is at most
  the cap.
  Red when: a claim pushed `agent-cap` or `unattended` past the cap.
  figure: DERIVED at observation; 20,479 and 20,478 bytes at base against 20,480.

## 7. Gates

`codebase-map coverage + freshness` · `codebase-map gate coverage` · `codebase-map kit selftest` · `codebase-map adopter e2e` · `recall floor` · `recall floor arms` · `lexicon naming predicates` · `memory hygiene` · `spec tokens (a spec's own names resolve)`

The extractor has no suite of its own: the real-tree coverage gate runs it on every bar, and AC3 and
AC4 stage its refusals. No arm is added or moved.

## 8. Open questions

- **F1 — The brief cites `TOOL-aProbedToolkit-15` and `TOOL-aProbedToolkit-8` against this point.
  Is either ask one mechanism with this unit?**
  The first carries two findings: the unclaimed steering files, which S1 and S3 answer for the hook
  half, and the template sentence overselling the map, which is a charter edit. The second carries
  the digest's coverage figure, a change to `map_diff.py`, and the baseline's missing shrink assert,
  which is unit 40.
  RESOLVED (agent, 2026-10-04, delegated): split — the template overclaim and the digest's coverage
  figure move to new units the run adds, `TOOL-aMendedFleet-85` and `TOOL-aMendedFleet-86`; this unit
  advances the first ask and closes neither.
- **F2 — What is a git-hooks key?**
  Options: every non-test file, as today; every extension-less file; the names git documents.
  RESOLVED (agent, 2026-10-04, delegated): the documented names, with an unknown extension-less
  name raising. It is the only option under which a misspelt hook cannot read as live, and a new git
  hook name fails loudly rather than silently.

## 9. Revision log

- rev-1 · 2026-10-04 · initial draft, from the synthesis's items [#43] and [#44], `_git_hooks`,
  `json_artifact_inventory` and the settings file at base.
- rev-2 · 2026-10-04 · §3 §8 S6 AC7 · the M2 cross-read: the two split halves named `external` and
  "units the run adds" while `TOOL-aMendedFleet-85` and `TOOL-aMendedFleet-86` exist in this build,
  so the Non-goals, Edges and F1 name them; and the claims this unit adds to `agent-cap` and
  `unattended` would breach the dossier cap that `TOOL-aMendedFleet-89`, ordered after this unit,
  is the first to relieve, so S6 and AC7 make the room in this commit.
- rev-3 · 2026-10-05 · §4 Files touched · the build pass: `parse_dossier` requires every dossier's
  `[claims]` to carry exactly the inventory ids, so every dossier gains an empty `harness-hooks`
  line, not only the claimants the estimate listed; and S4's "stays reachable through its dossier's
  path globs" held only for `straggler-guard.sh`, so the `run-gates` dossier's globs gain
  `.githooks/pre_push_bar_selftest.py` and `FOUNDATION.md`'s gain `.githooks/gate-env.sh`.

## 10. Reuse audit

The seam extended is `json_artifact_inventory` in `tools/codebase-map/map_lib.py`, which the
`gate-legs` inventory already reads its JSON registry through; the new extractor passes it an
extract function, as `_gate_legs` does. `python tools/codebase-map/reuse_lookup.py "enumerate the
hook commands a claude settings file wires"` returned name-stem neighbours, `corpus_files` and
`walk_file_keys` among them, and no reader of the settings file's hook list; the probe printed
`unscanned layers: .sh`, and `tools/check-wiring.sh` is the shell reader it cannot see, which checks
that named hooks are wired and lists none. `tools/settings-merge.py` writes and removes entries and
enumerates none either. The recall probe returned the asks naming the gap, `TOOL-aProbedToolkit-15`
among them, and a spec-audit finding that the extractors walk no fragment files. Where the report and
the tree disagree: nowhere; the seven `git-hooks` keys and their three helpers are unchanged at base.

Recall terms used: `python tools/memory-recall/query.py "which inventory covers the claude harness
hooks in settings.json and why do git-hooks keys include helper files" --terms "harness hooks
settings.json git-hooks inventory extractor map_extractors unclaimed fail-closed codebase-map dossier
claim steering surface"`
