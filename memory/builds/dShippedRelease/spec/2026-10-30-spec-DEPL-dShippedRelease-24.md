# DEPL-dShippedRelease-24 — `install.guards`: the core guards in the project's settings, or in managed settings where the operator opts in

**Status:** OPEN · rev-2 · 2026-10-30 · node d · Tier-2 · base f4597719 · streams deployer · order 26 · advances DEPL-dShippedRelease-32

**Carries:** cl-dClosedLoop-0434@f8425815 whole
**Carries:** node:policy-key.install.guards

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-30-build-DEPL-dShippedRelease-1-agent-ledger.md](../build/2026-10-30-build-DEPL-dShippedRelease-1-agent-ledger.md) | journal | DEPL-dShippedRelease-1 DEPL-dShippedRelease-2 DEPL-dShippedRelease-3 DEPL-dShippedRelease-4 DEPL-dShippedRelease-5 DEPL-dShippedRelease-6 DEPL-dShippedRelease-7 DEPL-dShippedRelease-8 DEPL-dShippedRelease-9 DEPL-dShippedRelease-10 DEPL-dShippedRelease-11 DEPL-dShippedRelease-12 DEPL-dShippedRelease-13 DEPL-dShippedRelease-14 DEPL-dShippedRelease-15 DEPL-dShippedRelease-16 DEPL-dShippedRelease-17 DEPL-dShippedRelease-18 DEPL-dShippedRelease-19 DEPL-dShippedRelease-20 DEPL-dShippedRelease-21 DEPL-dShippedRelease-22 DEPL-dShippedRelease-23 DEPL-dShippedRelease-25 DEPL-dShippedRelease-26 DEPL-dShippedRelease-27 DEPL-dShippedRelease-28 DEPL-dShippedRelease-29 DEPL-dShippedRelease-30 DEPL-dShippedRelease-31 DEPL-dShippedRelease-49 DEPL-dShippedRelease-50 DEPL-dShippedRelease-51 DEPL-dShippedRelease-52 DEPL-dShippedRelease-53 DEPL-dShippedRelease-54 DEPL-dShippedRelease-55 DEPL-dShippedRelease-56 DEPL-dShippedRelease-57 DEPL-dShippedRelease-58 DEPL-dShippedRelease-59 DEPL-dShippedRelease-60 DEPL-dShippedRelease-61 DEPL-dShippedRelease-62 DEPL-dShippedRelease-63 DEPL-dShippedRelease-64 DEPL-dShippedRelease-65 DEPL-dShippedRelease-66 DEPL-dShippedRelease-67 DEPL-dShippedRelease-68 DEPL-dShippedRelease-69 DEPL-dShippedRelease-70 DEPL-dShippedRelease-71 DEPL-dShippedRelease-72 DEPL-dShippedRelease-73 DEPL-dShippedRelease-74 DEPL-dShippedRelease-75 DEPL-dShippedRelease-76 DEPL-dShippedRelease-77 DEPL-dShippedRelease-78 |
| [2026-10-30-build-DEPL-dShippedRelease-1-spec-stage-returns.md](../build/2026-10-30-build-DEPL-dShippedRelease-1-spec-stage-returns.md) | research | DEPL-dShippedRelease-1 DEPL-dShippedRelease-2 DEPL-dShippedRelease-3 DEPL-dShippedRelease-4 DEPL-dShippedRelease-5 DEPL-dShippedRelease-6 DEPL-dShippedRelease-7 DEPL-dShippedRelease-8 DEPL-dShippedRelease-9 DEPL-dShippedRelease-10 DEPL-dShippedRelease-11 DEPL-dShippedRelease-12 DEPL-dShippedRelease-13 DEPL-dShippedRelease-14 DEPL-dShippedRelease-15 DEPL-dShippedRelease-16 DEPL-dShippedRelease-17 DEPL-dShippedRelease-18 DEPL-dShippedRelease-19 DEPL-dShippedRelease-20 DEPL-dShippedRelease-21 DEPL-dShippedRelease-22 DEPL-dShippedRelease-23 DEPL-dShippedRelease-25 DEPL-dShippedRelease-26 DEPL-dShippedRelease-27 DEPL-dShippedRelease-28 DEPL-dShippedRelease-29 DEPL-dShippedRelease-30 DEPL-dShippedRelease-31 |
| [2026-10-30-build-DEPL-dShippedRelease-24-deviation-241.md](../build/2026-10-30-build-DEPL-dShippedRelease-24-deviation-241.md) | deviation | — |
| [2026-10-30-build-DEPL-dShippedRelease-9-reuse-scout-e.md](../build/2026-10-30-build-DEPL-dShippedRelease-9-reuse-scout-e.md) | research | DEPL-dShippedRelease-9 DEPL-dShippedRelease-10 DEPL-dShippedRelease-21 DEPL-dShippedRelease-23 |
| [2026-10-30-prompt-DEPL-dShippedRelease-1-spec-brief.md](../prompts/2026-10-30-prompt-DEPL-dShippedRelease-1-spec-brief.md) | research | DEPL-dShippedRelease-1 DEPL-dShippedRelease-2 DEPL-dShippedRelease-3 DEPL-dShippedRelease-4 DEPL-dShippedRelease-5 DEPL-dShippedRelease-6 DEPL-dShippedRelease-7 DEPL-dShippedRelease-8 DEPL-dShippedRelease-9 DEPL-dShippedRelease-10 DEPL-dShippedRelease-11 DEPL-dShippedRelease-12 DEPL-dShippedRelease-13 DEPL-dShippedRelease-14 DEPL-dShippedRelease-15 DEPL-dShippedRelease-16 DEPL-dShippedRelease-17 DEPL-dShippedRelease-18 DEPL-dShippedRelease-19 DEPL-dShippedRelease-20 DEPL-dShippedRelease-21 DEPL-dShippedRelease-22 DEPL-dShippedRelease-23 DEPL-dShippedRelease-25 DEPL-dShippedRelease-26 DEPL-dShippedRelease-27 DEPL-dShippedRelease-28 DEPL-dShippedRelease-29 DEPL-dShippedRelease-30 DEPL-dShippedRelease-31 |
| [2026-10-30-review-DEPL-dShippedRelease-1-spec-audit-round1.md](../reviews/2026-10-30-review-DEPL-dShippedRelease-1-spec-audit-round1.md) | spec-audit | DEPL-dShippedRelease-10 DEPL-dShippedRelease-21 DEPL-dShippedRelease-23 DEPL-dShippedRelease-31 DEPL-dShippedRelease-11 DEPL-dShippedRelease-12 DEPL-dShippedRelease-1 DEPL-dShippedRelease-2 DEPL-dShippedRelease-13 DEPL-dShippedRelease-4 DEPL-dShippedRelease-14 DEPL-dShippedRelease-15 DEPL-dShippedRelease-6 DEPL-dShippedRelease-27 DEPL-dShippedRelease-5 DEPL-dShippedRelease-30 DEPL-dShippedRelease-3 DEPL-dShippedRelease-25 DEPL-dShippedRelease-7 DEPL-dShippedRelease-16 DEPL-dShippedRelease-20 DEPL-dShippedRelease-17 DEPL-dShippedRelease-28 DEPL-dShippedRelease-29 DEPL-dShippedRelease-18 DEPL-dShippedRelease-8 DEPL-dShippedRelease-26 DEPL-dShippedRelease-19 DEPL-dShippedRelease-22 DEPL-dShippedRelease-9 |

<!-- /gen:spec-records -->

## 1. Goal

The core guards install only into `.claude/settings.json`, a file the project can edit, and managed
settings are not designed (`gap-deploy-14`). This unit names the core guards, gives the key
`install.guards` its reader, and adds the operator's act that installs them into a settings file the
project cannot edit, on the one machine where that operator opts in.

## 2. Scope (IN)

The policy reader `python tools/policy/policy.py get` is landed. No parent surface is needed to build
this unit, and the catalogue row exists at `tools/policy/catalogue.toml:1058`.

- **S1** — The list. The core guards are the six hooks that can refuse an act: agent-cap, scratch-guard
  on both its events, gate-guard, stop-guard and format-guard. A fragment file declares membership with
  the optional key `guard`, a boolean, default false, which `load_fragment` refuses when it is not a
  boolean. It is `true` on `tools/hooks/scratch-guard.fragment.json`,
  `tools/hooks/scratch-guard-subagent.fragment.json`, `tools/hooks/format-guard.fragment.json`,
  `tools/unattended/gate-guard.fragment.json` and `tools/unattended/stop-guard.fragment.json`.
  Agent-cap ships no fragment (`tools/settings-merge.py:231`), so its built-in row is a member through
  one constant, `AGENT_CAP_GUARD = True`, beside `AGENT_CAP`. Observed by AC1.
- **S2** — The key's row. `install.guards` gains `summary` and `usage` on its one catalogue row, and its
  name leaves `tools/policy/unsummarised-keys.txt` by `python tools/policy/policy.py lists --write`.
  Its allowed values `project` and `managed` and its default `project` stay the row's. Observed by AC9.
- **S3** — The resolver. `derive_settings_target(root)` in `tools/settings-merge.py` returns the file
  the guards install into. It asks `read_policy("install.guards")`, a helper that runs the policy kit's
  `policy.py get` as a bounded subprocess, the kit found through the file's inline `resolve_kit_dir`,
  and it treats a missing policy kit or a refused read as `project`, printing one line naming why.
  `project` returns `GOV_SETTINGS_JSON` when declared, else `.claude/settings.json`, as
  `run_fragment_merges` resolves it today. `managed` returns `GOV_SETTINGS_JSON` when declared, else
  `gov-guards.json` in the `managed-settings.d` directory of the platform's managed directory (§8 F1).
  The verb `--resolve-target` prints that path. Observed by AC2, AC3 and AC10.
- **S4** — The operator's act. `python <prefix>/settings-merge.py --install-guards`, run by the operator
  from the repository's root, merges agent-cap's entry and every fragment with `guard` true into the
  target S3 returns. Under `project` it exits 2 naming the key, because that value needs no act. The
  population is the receipt's `.fragment.json` rows, else `git ls-files` of them where no receipt
  exists. A guard whose hook file is absent here is named and skipped, as `run_fragment_merges` skips
  it. A second run changes no byte. Observed by AC4.
- **S5** — No rewrite across repositories. A managed entry is machine-wide, so `merge` run by
  `--install-guards` refuses, exit 2, when the target already holds the guard's marker under a command
  that differs, naming both commands and the file. It never rewrites the entry in place, because that
  would point another repository's guard at a path it does not hold. Observed by AC5.
- **S6** — The reading. `python <prefix>/settings-merge.py --check-guards` prints nothing under
  `project`. Under `managed` it prints one line per guard: `ok` when the target holds its rendered
  command, `note` when the target or its entry is absent on this machine, and `UNWIRED` when the entry's
  command differs. It exits 1 on any `UNWIRED`, else 0. Observed by AC6.
- **S7** — The readers. `tools/check-wiring.sh` calls `--check-guards` once, after its hook arms, prints
  its lines and adds its `UNWIRED` count to `unwired`, so one reader answers both `update` and every
  session. Observed by AC7. `run_fragment_merges` (`tools/govkit/govkit.py:6109`) calls it once after
  its merges and, on any line other than `ok`, prints one line naming the operator's command. It writes
  nothing outside the target. Observed by AC8.
- **S8** — The docs. `help/managed-guards.md`, with its row in `help/README.md`, states the list, the
  two values, what the operator runs, on which machines, and what the managed file does not protect.
  `WIRE-INTO-PROJECT.md` gains the same pointer in its wiring section. Observed by AC11.

## 3. Non-goals (OUT)

- Automation writing the managed file. No gov program writes outside a repository's tree here: `update`
  and every hook only report (§8 F3).
- Taking a guard out of the project's settings under `managed` (§8 F2).
- `allowManagedHooksOnly`, `disableAllHooks` or any other managed key. This unit writes hook entries and
  nothing else, so an adopter's own project hooks keep running.
- Protecting a hook's bytes. The managed entry protects the wiring. `receipt sync` grades the bytes.
- Managed policy for any harness but Claude Code. Codex install targets are DEPL-dShippedRelease-27's,
  and NP-20 asked about one harness.
- A preset setting the key. v2's never-touch list holds `install.guards`, and its reader is the preset
  composition's (KICK-dKeptSession). This unit reads the key's value and does not grade its source.
- The MDM and server-managed policy channels (§5 risks).

### Edges

- **consumes-from** external — the harness's managed settings path and its `managed-settings.d` merge, read from Claude Code 2.1.292 on 2026-10-30 (§8 F1); a later harness that moves them makes the target a file nothing reads, which `--check-guards` cannot see
- **hands-off** `DEPL-dShippedRelease-78` — the managed target's pricing and its descriptor, which the minors batch repairs (review ids 66, 108)

## 4. Design

### The list, and how it was named

v2:1310 and night-pass:380, :540 name no members (scout E disagreement 15). The predicate is mechanical:
a core guard is a hook that can refuse an act, by a `PreToolUse` deny or a `Stop` block. Read at
`f4597719`, the twelve shipped fragments and the built-in row split as follows.

| Hook | Event | Refuses | Guard |
|---|---|---|---|
| agent-cap (built-in row) | `PreToolUse` | a fan-out over the limit | yes |
| scratch-guard | `PreToolUse` | a write or a gate outside a role's bounds | yes |
| scratch-guard-subagent | `SubagentStart` | nothing itself: it is scratch-guard's other half, and half a guard is not wired | yes |
| gate-guard | `PreToolUse` | the flagged bar before VERIFYING | yes |
| stop-guard | `Stop` | a turn end on a bound run | yes |
| format-guard | `Stop` | a turn end breaking the charter's formats | yes |
| check-wiring, the two orientation cards, recall-opened, the two procmon hooks, stall-recorder | various | nothing: each observes | no |

### The managed target

Read from the harness binary (§8 F1): the managed directory is `C:\Program Files\ClaudeCode` on Windows,
`/Library/Application Support/ClaudeCode` on macOS and `/etc/claude-code` otherwise, and the harness
merges `managed-settings.json` with each `.json` file in `managed-settings.d`, sorted by name. A
drop-in file lets gov's entries sit beside a machine's own policy without touching it, and
`settings-merge.py` writes it through its existing `run`, whose `.bak` sibling the harness's `.json`
filter does not read.

The rendered command is the project's, byte for byte: `node "${CLAUDE_PROJECT_DIR}/<path>"`, which
settings-merge's docstring says varies for nobody. The harness keys hook dedup on the root and the
command, so a guard present in both tiers fires once.

### Why the project's entries stay

`install.guards` is a committed value and managed settings are per-machine. A node whose operator has
not opted in has no managed file. If `managed` took the entries out of `.claude/settings.json`, that
node would run with no guard at all, which `tools/hooks/README.md` calls the one failure mode a wiring
move must avoid. So `managed` adds a tier the project cannot edit, and the project's entries stay as
the floor (§8 F2 and the deviation record).

### What the operator sees

Under `managed`, a machine with no managed file reads `note`, never `UNWIRED`: the guards fire from
the project's settings, so a fresh CI clone must not go red. An entry that differs reads `UNWIRED`,
because it fires a wrong or dead path on every call.

### Inventory

| Minted | Kind | Home |
|---|---|---|
| `guard` | fragment key, optional boolean | `tools/settings-merge.py` `load_fragment` |
| `AGENT_CAP_GUARD` | constant | `tools/settings-merge.py` |
| `derive_settings_target`, `read_policy` | functions | `tools/settings-merge.py` |
| `--resolve-target`, `--install-guards`, `--check-guards` | CLI verbs | `tools/settings-merge.py` |

`lexicon.py --suggest derive_settings_target --as py.function` and `--suggest read_policy --as
py.function` printed OK on 2026-10-30. No gate leg is minted.

### Migration

Additive. Every value of the key keeps today's bytes under the default `project`. No receipt field moves.

### Rollout

`managed` is opt-in and dark. Nothing changes on a machine until its operator runs `--install-guards`.

### Files touched (estimate)

- `tools/settings-merge.py`
- `tools/check-wiring.sh`
- `tools/govkit/govkit.py`
- `tools/govkit/selftest.py`
- `tools/hooks/scratch-guard.fragment.json`
- `tools/hooks/scratch-guard-subagent.fragment.json`
- `tools/hooks/format-guard.fragment.json`
- `tools/hooks/README.md`
- `tools/unattended/gate-guard.fragment.json`
- `tools/unattended/stop-guard.fragment.json`
- `tools/policy/catalogue.toml`
- `tools/policy/unsummarised-keys.txt`
- `help/managed-guards.md`
- `help/README.md`
- `WIRE-INTO-PROJECT.md`

### Alternatives rejected

- **`update` writes the managed file.** The test: the directory is administrator-owned on every
  platform the probe read, so `update` in a session either fails or proves the file is writable by the
  session, which is the state that protects nothing (§8 F3).
- **Merging into `managed-settings.json`.** The test: the harness reads a sorted drop-in directory, so a
  separate file touches nothing a machine's administrator owns.
- **A list of hook names typed in `settings-merge.py`.** It states membership a second time, away from
  the fragment. The test: a new guard fragment would need two edits, and only one is graded.
- **A wrapper hook that exits 0 where the project holds no copy.** It would quiet a non-gov repository
  on an opted-in machine, and it changes the command, so dedup fails and every guard fires twice.

## 5. Production-readiness checklist

- security: this adds a write outside the repository, made only by an operator's explicit verb and
  bounded to one file name. Hook paths still pass `resolve_hook_path` and `_SAFE_ARG`. No automation
  gains a write. A managed file a session can write protects nothing, and this unit does not detect that
  state: the help page says to install it as an administrator.
- perf / scale: `--check-guards` costs one `policy.py get` and one JSON read per session, inside
  check-wiring's existing python use.
- error / empty / loading states: a refused policy read is `project` with a line. An unwritable target
  exits 2 through `run`'s existing `write failed`. A missing fragment file is named and skipped.
- observability: the `ok`, `note` and `UNWIRED` lines in every session, and `update`'s one line.
- risks: the entries fire in every project on that machine, and `node` exits non-zero on each call where
  the path is absent, a non-blocking error the harness prints. So the opt-in suits a machine serving
  repositories with one prefix, and S5 refuses the rest. Under the harness's default `first-wins`, a
  machine with MDM or server-managed policy reads that source alone, so a file here is ignored and
  `--check-guards` cannot tell. The drop-in path is a harness fact pinned at one version.
- testing: the probes of §6 and arms in `tools/settings-merge.py` and `tools/check-wiring.test.sh`.
- migration: §4 "### Migration".
- user docs: `help/managed-guards.md`, S8.

## 6. Acceptance criteria

- **AC1** — When `git grep -l '"guard": true' -- '*.fragment.json'` runs, it prints exactly the five
  paths of S1, and `python tools/settings-merge.py --check-guards` under `managed` in a fixture prints
  one line per guard, six with agent-cap.
  Red when: a guard loses the key, a non-guard gains it, or agent-cap's built-in row is left out.
  figure: five and six are PINNED, read at `f4597719`.
- **AC2** — When `python tools/settings-merge.py --resolve-target` runs in a fixture repository whose
  landed `.governance/policy.toml` sets `guards = "project"` under `[install]`, it prints
  `.claude/settings.json`. With the key unset it prints the same.
  Red when: the default moves a repository off its project settings.
- **AC3** — When `python tools/settings-merge.py --resolve-target` runs in a fixture whose landed policy
  sets `guards = "managed"` under `[install]`, it prints a path ending
  `gov-guards.json` under the platform's directory of §8 F1.
  Red when: the `managed` value reads as `project`, or the path is not the harness's.
- **AC4** — When `python tools/settings-merge.py --install-guards` runs in AC3's fixture with
  `GOV_SETTINGS_JSON` naming a scratch file, that file gains every guard's entry, `.claude/settings.json`
  keeps its bytes, and a second run changes no byte. In AC2's fixture it exits 2 and writes nothing.
  Red when: the verb writes under `project`, removes a project entry, or appends a second entry.
- **AC5** — When `--install-guards` of `settings-merge.py` runs with the scratch file already holding
  agent-cap's marker under `node "${CLAUDE_PROJECT_DIR}/scripts/hooks/agent-cap.js"`, it exits 2, names
  both commands, and the file keeps its bytes.
  Red when: the entry is rewritten in place, which turns another repository's guard off.
- **AC6** — When `python tools/settings-merge.py --check-guards` runs in AC3's fixture, it prints `note`
  for each guard with the file absent, `ok` after AC4, and `UNWIRED` with exit 1 after one entry's
  command is changed. Under AC2's fixture it prints nothing and exits 0.
  Red when: an absent file reds a fresh clone, or a differing entry reads `ok`.
- **AC7** — When `bash tools/check-wiring.sh --check` runs in AC3's fixture with one entry's command
  changed, it prints that guard's `UNWIRED` line and exits 1. With the file absent it exits as it does
  under `project`.
  Red when: the arm counts a `note` as unwired, or check-wiring carries a second reader of the key.
- **AC8** — When `python tools/govkit/govkit.py update --target <fixture> --write` runs under AC3's
  fixture with the file absent, it prints one line naming `--install-guards`, and no path outside the
  fixture is written.
  Red when: `update` writes the managed target, or stays silent on a machine that has not opted in.
- **AC9** — When `grep -cx 'install.guards' tools/policy/unsummarised-keys.txt` runs it prints `0`, and
  `python tools/policy/policy.py lists --check` exits 0.
  Red when: the row lacks `summary` or `usage`, or a second row was added.
- **AC10** — When `git grep -n 'read_policy("install.guards"' -- tools/settings-merge.py` runs, it prints
  the literal call the policy kit's reader-coverage arm needs.
  Red when: the key is read through a variable, so the arm reds it once this build is terminal.
- **AC11** — When `grep -n 'managed-guards.md' help/README.md WIRE-INTO-PROJECT.md` runs, each file
  prints its pointer.
  Red when: the operator's act has no page.

## 7. Gates

`settings-merge selftest` · `check-wiring self-test` · `govkit selftest` · `govkit refusal join` · `govkit acceptance matrix` · `policy fixtures` · `recall floor arms` · `straggler-guard arms` · `transition-audit arms` · `agent-cap self-test` · `scratch-guard self-test` · `hook destinations self-test` · `verifier fan-out self-test` · `review-join self-test` · `memory hygiene` · `spec tokens (a spec's own names resolve)`

New arm: tools/settings-merge.py · covers AC2 AC3 AC4 AC5 AC6 · a fixture repository with each value of the key landed, a differing managed entry, and a guard whose hook is absent · none
New arm: tools/check-wiring.test.sh · covers AC7 · a fixture whose managed file holds one differing command · none
New arm: tools/govkit/selftest.py · covers AC8 · a fixture update under `managed` with no managed file · none

What these do not check: that a real harness reads the file, which only a machine with an administrator
can show; that the file is out of a session's reach; or that no MDM policy shadows it.

## 8. Open questions

- **FACT-QUESTION · F1 — Where does Claude Code read managed settings, and may gov's entries sit beside a
  machine's own?** Probe: `grep -ao` over the installed harness binary, `claude.exe` 2.1.292 on node d,
  for `managed-settings.json`, `managed-settings.d` and `allowManagedHooksOnly`. Observation: one function
  returns `/Library/Application Support/ClaudeCode` on macOS, `C:\Program Files\ClaudeCode` on Windows and
  `/etc/claude-code` otherwise; the loader reads `managed-settings.json`, then each non-dot `.json` of
  `managed-settings.d` in sorted order, into one policy tier; a project's `disableAllHooks` leaves managed
  hooks running. Liveness: the same grep for `managed-settingz.json` counts 0, so the probe can return a
  negative. RESOLVED (agent, 2026-10-30, delegated): the drop-in file `managed-settings.d/gov-guards.json`
  under that directory, PINNED at 2.1.292 and re-read at the build pass. Rung 2. widens: none · relaxes: none
- **F2 — How does a committed key express a per-machine setting (scout E F12)?** Options: (a) the committed
  value names the posture, each machine's operator acts on it, and the project's entries stay as the
  floor; (b) a per-machine untracked declaration, a new install location (veto 2) the clause does not
  name; (c) `managed` moves the entries out of the project's settings, which leaves any node with no
  opt-in unguarded (veto 3). RESOLVED (agent, 2026-10-30, delegated): (a), rung 3, with the clause's "or"
  read as where the core guards are held against the project, recorded in deviation 241.
  widens: none · relaxes: none
- **F3 — Who writes the managed file?** Options: (a) an operator's explicit verb; (b) `update` and
  `apply`, through `run_fragment_merges`. The clause says "where the operator opts in", and v2's reason is
  that the install location is the operator's. (b) adds an automation write outside the repository (veto
  3). RESOLVED (agent, 2026-10-30, delegated): (a), rung 1, from the clause's own words.
  widens: none · relaxes: none
- **F4 — Which hooks are the core guards?** Options: (a) every hook that can refuse an act, S1's six; (b)
  agent-cap and scratch-guard alone, the two in the `hooks` kit; (c) every shipped hook. (b) leaves a
  refusing hook where the project can unwire it, and (c) makes an observer machine-wide for no
  protection. RESOLVED (agent, 2026-10-30, delegated): (a), rung 3, the only predicate that needs no
  judgement per hook. widens: none · relaxes: none

## 9. Revision log

- rev-1 · 2026-10-30 · initial draft.
- rev-2 · 2026-10-30 · §3 · the Edges gain the mirror of each edge the round-1 spec audit's promoted units declare toward this unit (units 78); no scope, design or criterion moved.

## 10. Reuse audit

The seam extended is `run` in `tools/settings-merge.py:510`, whose first argument is already the
settings file, with `merge` at `:428` and `load_fragment` at `:252`, plus `run_fragment_merges` at
`tools/govkit/govkit.py:6109` and `settings_json` in `tools/check-wiring.sh`, around `:99`.
`reuse_lookup.py "merge a hook into a settings file outside the repository"` ranked `merge` in
`tools/memory-tree/merge-rows.py` and `tools/settings-merge.py` first; the second path is the seam and
the first is a name-stem neighbour. Scout E's seam row held. It cited `settings-merge.py:510` and
`govkit.py:6132`, `:6187`, and each read true at `f4597719`. Scout E's F12 said managed paths could not be
confirmed from this repository, and the harness binary answered that (§8 F1). The recall probe found no
managed-settings design beyond NP-20 and v2's two rows: `git grep managed-settings` over the tree names
nothing, so the path facts are new here. Candidates rejected and their tests are under §4 "### Alternatives
rejected".

Recall terms used: `python tools/memory-recall/query.py "where do the core guards install, the project settings or managed settings" --terms "install.guards managed settings guard hooks agent-cap scratch-guard settings-merge check-wiring operator opts"`
