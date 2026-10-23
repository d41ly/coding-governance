# TOOL-dSafePassage-24 — a step is refused when the target's own git config declares an executor or a credential

**Status:** DEFERRED · rev-3 · 2026-10-23 · node d · Tier-2 · base 3708a705 · streams tooling · order 3 · advances TOOL-dSafePassage-14

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-23-build-TOOL-dSafePassage-24-deviation-119.md](../build/2026-10-23-build-TOOL-dSafePassage-24-deviation-119.md) | deviation | — |
| [2026-10-23-build-TOOL-dSafePassage-24-deviation-70.md](../build/2026-10-23-build-TOOL-dSafePassage-24-deviation-70.md) | deviation | — |
| [2026-10-23-prompt-TOOL-dSafePassage-26-hygiene-fix.md](../prompts/2026-10-23-prompt-TOOL-dSafePassage-26-hygiene-fix.md) | research | TOOL-dSafePassage-25 TOOL-dSafePassage-26 |
| [2026-10-23-review-TOOL-dSafePassage-15-16-17-18-19-20-21-22-23-24-25-26-spec-audit-round1.md](../reviews/2026-10-23-review-TOOL-dSafePassage-15-16-17-18-19-20-21-22-23-24-25-26-spec-audit-round1.md) | spec-audit | TOOL-dSafePassage-16 TOOL-dSafePassage-20 TOOL-dSafePassage-15 TOOL-dSafePassage-18 TOOL-dSafePassage-19 TOOL-dSafePassage-22 TOOL-dSafePassage-17 TOOL-dSafePassage-23 TOOL-dSafePassage-25 TOOL-dSafePassage-21 TOOL-dSafePassage-26 |

<!-- /gen:spec-records -->

## 1. Goal

The round-1 spec audit of this build
(`memory/builds/dSafePassage/reviews/2026-10-23-review-TOOL-dSafePassage-1-2-3-4-5-6-7-8-9-10-11-12-13-spec-audit-round1.md`)
confirmed finding **id 53** at HIGH, its item **D-8**. TOOL-dSafePassage-7's contract isolates the
system and global git config, the hooks and the credential helper (its spec, S1 and §4 "Data
model"), and leaves the target's own repository config live. That config can declare
`filter.<x>.clean`, `smudge` or `process`, `core.fsmonitor`, `diff.external` and an
`http.<url>.extraheader`, which actions/checkout persists. The report reproduced it on git
2.54.0.windows.1: under the contract's environment, `git add` ran a local `filter.canary.clean`. A
step that stages in the target, as the contract's own fixture step does, runs adopter code and can
send a persisted auth header while `check_needs_target` certifies the contract `isolated`. This unit
is id 53's promotion, built from the skeptic's corrected fix: before any step spawn, the target's
config is read with includes resolved, and the step is refused when it declares any key git runs as
a program or sends as a credential, the key named.

## 2. Scope (IN)

- **S1** — The read. `read_target_local_config(target)` in `tools/govkit/upgrade_steps.py` runs
  `git -C <target> config --list --show-scope --show-origin --includes -z` under
  `build_step_env`'s environment, so the system and global scopes are already off, and keeps the
  `local` and `worktree` rows, the included files' rows among them. The `command` rows, the
  contract's own pairs, are not kept. Observed by AC1 and AC4.
- **S2** — The refusal. `check_target_local_config(target)` returns each kept key matching the set
  of §4 "Data model", and `run_step_isolated` raises `Refusal` before any spawn when it returns any,
  naming the step id, each key and the file that declares it. Observed by AC1, AC2, AC3 and AC4.
- **S3** — Every phase. The check runs inside `run_step_isolated`, so every phase it spawns, `up`,
  `down`, `witness` and `resume`, is checked, and so is any argv a later unit spawns through it;
  an `attended` row still spawns nothing and is not checked. Observed by AC1.
- **S4** — The plants. The `isolation` family of `python3 "tools/govkit/upgrade_steps.py" fixture`
  gains `local-filter`, `local-process`, `local-fsmonitor` and `local-include`, each with a `-stub`
  that skips the refusal inside the fixture process only, as TOOL-dSafePassage-7's stubs do.
  Observed by AC1 to AC4.
- **S5** — The docs. The "What a step can reach" section of `help/upgrade-steps.md` names the refused
  keys and the one this check does not cover. Observed by AC5.

## 3. Non-goals (OUT)

- Neutralising a key with an environment override, key by key. The skeptic rejected it: a list of
  what to override misses the next executor git adds, and a refusal names what the operator must
  remove.
- `merge.<driver>.driver`. A step does not merge, and gov's own checkout declares
  `merge.rows.driver` and `merge.ours.driver` in its local config (read 2026-10-23 on node d), so
  refusing the key would refuse every gov-first step. It is named in §7 as what the check does not
  cover.
- The line-ending keys the contract drops: id 19, `TOOL-dSafePassage-26`.

### Edges

- **consumes-from** `TOOL-dSafePassage-7` — `run_step_isolated`, `build_step_env`, its refusal before a spawn and the `isolation` fixture family; without them there is no contract to close
- **hands-off** `TOOL-dSafePassage-26` — the line-ending config the contract drops, the other scope finding on the same environment
- **hands-off** `TOOL-dSafePassage-29` — the refused keys as the class git's own config list derives, held to it by an arm, the repair of finding 12 of the round-1 audit of units 15 to 26
- **hands-off** `TOOL-dSafePassage-30` — the config check over every repository git can enter from the target, submodules included, the repair of finding 38 of the round-1 audit of units 15 to 26
- **hands-off** `TOOL-dSafePassage-35` — the minors batch of the round-1 audit of units 15 to 26, which adds the credential-bearing values and reads the inventory's refusal-join sentence
- **hands-off** `TOOL-dSafePassage-38` — every key and file path of the refusal line passed through one redactor, so no refusal prints a credential, the repair of finding 30 of the spec audit of units 27 to 35

## 4. Design

### Data model

The refused keys, matched case-insensitively on the key git prints:

| Key | Why |
|---|---|
| `filter.<x>.clean`, `filter.<x>.smudge`, `filter.<x>.process` | git runs it on `add`, `checkout` and `hash-object --path` |
| `core.fsmonitor`, any value but a git false | git runs it, or starts a daemon, on index refresh |
| `diff.external`, `diff.<x>.textconv`, `diff.<x>.command` | git runs it on `diff` and `log -p` |
| `core.sshcommand`, `core.askpass` | git runs it on a fetch or a push |
| `http.extraheader`, `http.<url>.extraheader` | git sends it as a credential |
| `credential.<anything>` | a helper git runs, or a credential setting |

Gov's own checkout, read on 2026-10-23 with `GIT_CONFIG_NOSYSTEM=1` and `GIT_CONFIG_GLOBAL` the null
device, declares none of these keys, so gov first is not refused.

### Inventory

Minted in `tools/govkit/upgrade_steps.py`: `read_target_local_config` and `check_target_local_config`
(cell `py.function`, verbs `read` and `check`, OK by
`python tools/lexicon/lexicon.py --suggest <name> --as py.function` on 2026-10-23); the plants
`local-filter`, `local-process`, `local-fsmonitor`, `local-include` and their four `-stub` twins. No
conf key, no gate leg, no policy key. The new `raise Refusal` site is an anchor of
`tools/govkit/refusal_join.py`, armed by the §7 arm, and its `BRANCH_PIN` floor moves by one.

### Migration

None: no step row spawns before this build's walk lands.

### Rollout

Live at landing. It builds at order 3, after TOOL-dSafePassage-7 (order 2), and shares
`tools/govkit/upgrade_steps.py` with the other order-3 repairs, so the build run sequences those
passes by M6's disjointness rule.

### Files touched (estimate)

- `tools/govkit/upgrade_steps.py`
- `tools/govkit/selftest.py`
- `tools/govkit/refusal_join.py`
- `help/upgrade-steps.md`

### Alternatives rejected

- **`GIT_CONFIG_NOLOCAL` or an empty local config.** Git has no switch that drops the repository
  scope, and a step that edits the target's repository needs it.
- **Planting the keys in `write_target_plants`.** Every `check_needs_target` over a planted tree would
  then refuse, and the check exists to run the step.

## 5. Production-readiness checklist

- security: the unit closes the repository-scope hole of the contract; deny by default on every key
  git runs or sends.
- perf / scale: one `git config` spawn per step phase.
- error / empty / loading states: a `git config` that fails is a refusal naming it, never an empty
  read.
- observability: the refusal names the step, the key and its file.
- risks: an adopter with a legitimate LFS filter has every step refused until an operator runs it
  attended; the refusal names the key, and the help page says so.
- testing: the four plants and their stubs, through the arm of §7.
- migration: none.
- user docs: `help/upgrade-steps.md`, S5.

## 6. Acceptance criteria

- **AC1** — When `python3 "tools/govkit/upgrade_steps.py" fixture isolation --plant local-filter`
  runs, with the scratch target's `.git/config` setting `filter.canary.clean` and its
  `.gitattributes` reading `*.txt filter=canary`, the `clean` step is refused before any spawn,
  naming `filter.canary.clean` and `.git/config`, the filter's canary is absent, and the run exits 1;
  `--plant local-filter-stub` lets the step spawn and exits 1 naming the filter's canary.
  Red when: the step spawns and `git add` runs the target's filter.
- **AC2** — When the same family runs with `--plant local-process`, setting `filter.canary.process`,
  the step is refused naming that key; `local-process-stub` exits 1 naming its canary.
  Red when: a long-running filter process is not refused.
- **AC3** — When the same family runs with `--plant local-fsmonitor`, setting `core.fsmonitor` to a
  canary script, the step is refused naming `core.fsmonitor`; with `core.fsmonitor=false` it is not
  refused.
  Red when: an executable fsmonitor passes, or a false one is refused.
- **AC4** — When the same family runs with `--plant local-include`, its `.git/config` holding only
  `include.path` to a file that sets `filter.canary.clean`, the step is refused naming the key and the
  included file.
  Red when: the read runs without `--includes`, so an included executor passes.
- **AC5** — When `git grep -n -e "filter.<x>.clean" -e "extraheader" -e "merge.<driver>.driver" -- help/upgrade-steps.md`
  runs, the "What a step can reach" section names all three.
  Red when: the page names the contract's scopes but not the repository scope.

## 7. Gates

`govkit selftest` · `govkit refusal join` · `govkit acceptance matrix` · `govkit selfcheck` · `recall floor arms` · `encoding posture (text IO names its encoding)` · `lexicon naming predicates` · `spec tokens (a spec's own names resolve)`

New arm: tools/govkit/selftest.py · covers AC1 AC2 AC3 AC4 · the self-test calls `upgrade_steps.py fixture isolation` with the four plants, each failing case staged by its `-stub` twin · `tools/govkit/refusal_join.py` `BRANCH_PIN`, by one

What the check does not cover: `merge.<driver>.driver` (§3), and a key git adds later as an executor
until this table lists it.

## 8. Open questions

none

## 9. Revision log

- rev-1 · 2026-10-23 · initial draft, the promotion of the round-1 spec audit's id 53 (HIGH, item
  D-8).
- rev-2 · 2026-10-23 · §3 · the Edges gain the ends this unit owes the promotions of the round-1 audit of units 15 to 26, written by the disposal stage: `TOOL-dSafePassage-29`, `TOOL-dSafePassage-30`, `TOOL-dSafePassage-35`; no other section moved.
- rev-3 · 2026-10-23 · §3 · the Edges gain the ends this unit owes the promotions of the spec audit of units 27 to 35, written by the disposal stage: `TOOL-dSafePassage-38`; no other section moved.

## 10. Reuse audit

The seam extended is TOOL-dSafePassage-7's `run_step_isolated` and `build_step_env`, the one spawn
site of a step argv, whose refusal-before-spawn shape S2 copies from its unresolved-token refusal.
`python tools/codebase-map/reuse_lookup.py "read the git config of a repository with includes and
refuse executor keys"` ranked `read`, `git`, `read_text` and `key`, name-token matches; no reader of
repository config exists in the tree, so no existing seam fits beyond the contract's own spec.

Recall terms used: `python tools/memory-recall/query.py "how were spec audit findings promoted into repair units placed beside the unit they repair" --terms "spec audit promoted unit repair blocker high minors batch disposal order edges rescope"`
