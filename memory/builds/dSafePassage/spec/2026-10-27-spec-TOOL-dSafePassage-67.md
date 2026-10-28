# TOOL-dSafePassage-67 — the fixture factory pins commit signing and hooks in every repository it builds, and refuses a git command that fails

**Status:** CLOSED · rev-1 · 2026-10-27 · node d · Tier-2 · base 60d90cb7 · streams tooling · order 6 · advances TOOL-dSafePassage-14

**Derived:** TOOL-dSafePassage-26

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-26-build-TOOL-dSafePassage-67-ledger.md](../build/2026-10-26-build-TOOL-dSafePassage-67-ledger.md) | journal | — |
| [2026-10-27-prompt-TOOL-dSafePassage-67-1-spec-writer.md](../prompts/2026-10-27-prompt-TOOL-dSafePassage-67-1-spec-writer.md) | research | — |
| [2026-10-27-prompt-TOOL-dSafePassage-67-2-spec-writer.md](../prompts/2026-10-27-prompt-TOOL-dSafePassage-67-2-spec-writer.md) | journal | — |
| [2026-10-27-prompt-TOOL-dSafePassage-67-build-brief.md](../prompts/2026-10-27-prompt-TOOL-dSafePassage-67-build-brief.md) | journal | — |
| [2026-10-28-prompt-TOOL-dSafePassage-37-close-arms-c-brief.md](../prompts/2026-10-28-prompt-TOOL-dSafePassage-37-close-arms-c-brief.md) | research | TOOL-dSafePassage-37 TOOL-dSafePassage-38 TOOL-dSafePassage-39 TOOL-dSafePassage-40 TOOL-dSafePassage-42 TOOL-dSafePassage-43 TOOL-dSafePassage-44 TOOL-dSafePassage-45 TOOL-dSafePassage-47 TOOL-dSafePassage-48 TOOL-dSafePassage-49 TOOL-dSafePassage-5 TOOL-dSafePassage-51 TOOL-dSafePassage-53 TOOL-dSafePassage-54 TOOL-dSafePassage-56 TOOL-dSafePassage-59 TOOL-dSafePassage-62 TOOL-dSafePassage-63 TOOL-dSafePassage-64 TOOL-dSafePassage-65 TOOL-dSafePassage-66 TOOL-dSafePassage-68 TOOL-dSafePassage-69 TOOL-dSafePassage-70 TOOL-dSafePassage-71 |
| [2026-10-28-review-TOOL-dSafePassage-1-71-closing-diff-round1.md](../reviews/2026-10-28-review-TOOL-dSafePassage-1-71-closing-diff-round1.md) | diff-review | TOOL-dSafePassage-1 TOOL-dSafePassage-2 TOOL-dSafePassage-3 TOOL-dSafePassage-4 TOOL-dSafePassage-5 TOOL-dSafePassage-6 TOOL-dSafePassage-7 TOOL-dSafePassage-8 TOOL-dSafePassage-9 TOOL-dSafePassage-10 TOOL-dSafePassage-11 TOOL-dSafePassage-12 TOOL-dSafePassage-13 TOOL-dSafePassage-15 TOOL-dSafePassage-16 TOOL-dSafePassage-17 TOOL-dSafePassage-18 TOOL-dSafePassage-19 TOOL-dSafePassage-20 TOOL-dSafePassage-21 TOOL-dSafePassage-22 TOOL-dSafePassage-23 TOOL-dSafePassage-24 TOOL-dSafePassage-25 TOOL-dSafePassage-26 TOOL-dSafePassage-27 TOOL-dSafePassage-28 TOOL-dSafePassage-29 TOOL-dSafePassage-30 TOOL-dSafePassage-31 TOOL-dSafePassage-32 TOOL-dSafePassage-33 TOOL-dSafePassage-34 TOOL-dSafePassage-35 TOOL-dSafePassage-36 TOOL-dSafePassage-37 TOOL-dSafePassage-38 TOOL-dSafePassage-39 TOOL-dSafePassage-40 TOOL-dSafePassage-41 TOOL-dSafePassage-42 TOOL-dSafePassage-43 TOOL-dSafePassage-44 TOOL-dSafePassage-45 TOOL-dSafePassage-46 TOOL-dSafePassage-47 TOOL-dSafePassage-48 TOOL-dSafePassage-49 TOOL-dSafePassage-50 TOOL-dSafePassage-51 TOOL-dSafePassage-52 TOOL-dSafePassage-53 TOOL-dSafePassage-54 TOOL-dSafePassage-55 TOOL-dSafePassage-56 TOOL-dSafePassage-57 TOOL-dSafePassage-58 TOOL-dSafePassage-59 TOOL-dSafePassage-61 TOOL-dSafePassage-62 TOOL-dSafePassage-63 TOOL-dSafePassage-64 TOOL-dSafePassage-65 TOOL-dSafePassage-66 TOOL-dSafePassage-68 TOOL-dSafePassage-69 TOOL-dSafePassage-70 TOOL-dSafePassage-71 |

<!-- /gen:spec-records -->

## 1. Goal

Every repository `tools/govkit/fixture_target.py` builds stops inheriting the machine's global git
config for commit signing and hooks, as it already does not for `core.autocrlf`. Its `run_git` stops
ignoring a git command that fails. A fixture can then not pass, fail or hang because of a developer's
`commit.gpgsign`, `core.hooksPath` or `init.templateDir`, and a target that lost its `base` commit
is a loud error rather than an empty repository. TOOL-dSafePassage-26's build pass (`dfcef45a7`)
found the gap and could not fix it, its unit being CLOSED.

Every line cited below was read at the run branch's HEAD `2b6e6d1d`. The factory is not on the
default branch yet, so the header's `base` is the run's merge base, as on TOOL-dSafePassage-62 to -66.

## 2. Scope (IN)

- **S1** — The pins. `build_scratch_gov` (`tools/govkit/fixture_target.py:27-34`) runs its `init`
  with `--template=`, and its config loop (`:31-32`) gains `commit.gpgsign false` and
  `core.hooksPath .git/hooks` beside `core.autocrlf false`. Both factories get them, since
  `build_target` builds through `build_scratch_gov` (`:42`). The function's docstring names the
  pins, and the `core.autocrlf` comment in `build_target` (`:43-49`) moves up to the loop it
  describes. Observed by AC1.
- **S2** — The refusal. `run_git` (`:21-24`) raises `OSError` naming the argv, the directory and
  git's stderr when git exits non-zero. It still returns `None`. Observed by AC1.
- **S3** — The self-check. `python -I tools/govkit/fixture_target.py --selftest` plants a global
  config in a temporary directory, proves the plant is live on an unpinned control repository, and
  then builds a target through `build_target` under it (§4). It prints one line per observation and
  exits 0 when all hold, or 1 naming each one that does not. Observed by AC1.
- **S4** — The arm. `tools/govkit/selftest.py` gains `check_fixture_target`. It runs S3's command
  and checks the exit code and the pass line, and `main` calls it beside `check_step_gate_fixture`
  (`tools/govkit/selftest.py:4475`). Observed by AC1, which it re-observes.

## 3. Non-goals (OUT)

- Other global keys a fixture can inherit, such as `core.excludesFile` (a developer's global ignore
  file drops files from `add -A`) or `tag.gpgSign`. No factory repository is tagged today: the one
  tag read is on the upgrade walk's gov clone (`tools/govkit/upgrade_walk.py:473`).
- Repositories the factory does not build. The upgrade walk's gov clone commits with an identity
  and nothing else (`tools/govkit/upgrade_walk.py:212`). `shims.py` builds its own scratch, which
  already pins `commit.gpgsign` (`tools/govkit/shims.py:392-397`).
- Removing the per-command `-c core.hooksPath=/dev/null` pins callers already pass
  (`tools/govkit/fixtures/retired_edits.py:105`, `tools/govkit/shims.py:404`). They are redundant on
  a factory repository and harmless, and taking them out is a separate edit.
- A system-config pin. A global key outranks a system one, so the global file is the one this unit
  plants against.

### Edges

- **consumes-from** `TOOL-dSafePassage-5` — `fixture_target.py`, `build_target` and the upgrade walk's release-0 target built through it (S12); without the factory there is no seam to pin
- **consumes-from** `TOOL-dSafePassage-26` — `build_scratch_gov`, lifted into the factory by its S19, and the callers it routed through it; without them the pins reach the targets alone and not the synthetic govs

## 4. Design

### What was measured

A probe was PINNED on 2026-10-27 on node `d`, with `git version 2.54.0.windows.1`. It used a global
file through `GIT_CONFIG_GLOBAL` setting `commit.gpgsign = true`, `gpg.program = false` and
`core.hooksPath` at a directory whose `pre-commit` writes a canary. Under it,
`build_target(tmp, None)` returned a target where `git rev-parse --verify -q HEAD` exits 1, and the
canary was written. The same build with `commit.gpgsign false` and `core.hooksPath .git/hooks` set
after `build_scratch_gov` held `base` at HEAD, wrote no canary, and a later plain `git commit` in the
target, run by no factory code, was also clean. A second global file setting `init.templateDir`
made a plain `git init` copy the template's `hooks/pre-commit`. `git init --template=` copied no
`hooks` directory at all.

### Where the pin goes: the repository's own config, not `-c`

A per-command `-c` reaches only the factory's own three git calls. The repositories it builds are
then committed by their callers through their own helpers, and none of them pins signing:

| Caller | Commit | Pins |
|---|---|---|
| `write_gov17` | `tools/govkit/selftest.py:1709-1710`, in a gov `build_scratch_gov` made (`:1720`) | none |
| `write_commit` | `tools/govkit/upgrade_walk.py:70-73`, in the release-0 target (`:182-183`) | identity only |
| `write_commit` | `tools/govkit/fixtures/retired_edits.py:103-107` | `core.hooksPath` only |

Local config outranks global for every process that later runs git in the repository, so the
config loop is the one place that covers the factory's commit and every caller's. Pinning both ways
adds nothing the loop does not already cover.

### Why these values

- **`commit.gpgsign false`.** It removes signing and, with it, a `pinentry` prompt that could hang.
  The isolation fixture's `local-gpg` plant appends `commit.gpgsign = true` to the same
  `.git/config` (`tools/govkit/upgrade_steps.py:2267`, `:2275-2277`). For a single-valued key the
  last line wins, so that plant stays armed.
- **`core.hooksPath .git/hooks`.** A relative value resolves from the work-tree root, so it names
  git's own default directory. Every reader that resolves hooks then reads the directory it reads on
  a machine with no global key: `write_target_plants` takes `--local core.hooksPath` first
  (`tools/govkit/upgrade_steps.py:1147-1152`), and `hook_probe` asks `--git-path hooks/pre-commit`
  (`tools/govkit/govkit.py:6589-6591`). The key is in `STEP_UNREFUSED_KEYS`
  (`tools/govkit/upgrade_steps.py:238`), and no `STEP_REFUSED_KEYS` row (`:194-234`) matches either
  pin, so a step over a factory target is not refused.
- **`init --template=`.** A pinned `.git/hooks` would still run hooks a global `init.templateDir`
  copied there, so the template is not copied at all. That also drops a template's `info/exclude`
  and `description`. Nothing in `tools/govkit/` reads those, and the policy snapshot copies an
  exclude only when one is present (`tools/policy/check_policy.py:1005-1008`).

### Why `run_git` refuses

Its callers are the factory's own three calls and no other: `init` and the config loop (`:31-33`),
`add` and `commit` (`:58-59`). Every importer takes `build_scratch_gov` and `build_target` only
(`tools/govkit/selftest.py:680`, `tools/govkit/fixtures/retired_edits.py:30`,
`tools/govkit/upgrade_walk.py:182`), and `upgrade_steps.py` reads those two names off
`load_fixture_target()` (`:2097`, `:2643`, `:2686`, `:3144`, `:3151`). Each call is a step of the
contract the docstring states, "committed once as `base`", so no caller can want one to fail
silently. A target that returns with no commit is the `fixture-passes-by-finding-nothing` class:
every arm then grades an empty history.

`OSError` follows the factory's sibling, `write_commit` in `tools/govkit/fixtures/retired_edits.py:106-107`.
It is not a govkit `Refusal`, which `fixture_target.py` does not import and which
`tools/govkit/refusal_join.py` counts by name (`:259-264`), so `BRANCH_PIN` does not move.

### The self-check

```
--selftest, in a TemporaryDirectory d:
  plant   d/hooks/pre-commit  -> writes d/canary/hooks-path
          d/tpl/hooks/pre-commit -> writes d/canary/template
          d/global: commit.gpgsign=true, gpg.program=false, core.hooksPath=d/hooks, init.templateDir=d/tpl
          os.environ["GIT_CONFIG_GLOBAL"] = d/global          # run_git copies os.environ
  live    plain git, outside run_git, in d/control with an identity on the command line:
            init copies d/control/.git/hooks/pre-commit                     else LIVENESS miss
            commit exits non-zero, and d/canary/hooks-path is written       else LIVENESS miss
            commit with -c commit.gpgsign=false exits 0                     else LIVENESS miss
          then clear d/canary
  probe   t = build_target(d, None)
            git rev-parse HEAD^{commit} holds the subject "base"
            no file in d/canary; no t/.git/hooks/pre-commit
            run_git(t, "-c", "commit.gpgsign=true", "commit", "--allow-empty", "-qm", "signed")
              raises OSError whose text names `commit`
  print   one line per observation; exit 0 when all hold, else 1
```

The hooks are written with `encoding="utf-8"` and `newline="\n"` and made executable, and the
liveness half is what keeps a plant that stopped biting from reading as a pass.

### Inventory

Minted: the flag `--selftest` of `tools/govkit/fixture_target.py`, its function `check_inherited_config`,
and the selftest arm `check_fixture_target`. No conf key, gate leg, receipt field or policy key.

### Migration

None. Scratch repositories are built fresh on every run.

### Rollout

Live at landing, in order 6 beside TOOL-dSafePassage-26.

### Files touched (estimate)

- `tools/govkit/fixture_target.py`
- `tools/govkit/selftest.py`

### Alternatives rejected

- **`-c` on the factory's own commands.** It leaves every caller's later commit inheriting (the
  table above).
- **`GIT_CONFIG_GLOBAL` set to the null device in `run_git`'s environment**, as `build_tree_git_env`
  does (`tools/govkit/upgrade_steps.py:1129-1134`). It reaches the factory's own calls and no caller's,
  for the same reason.
- **`core.hooksPath` at a fresh empty directory.** It would also disarm a template's hooks, but
  every hooks reader would then resolve a path no machine resolves by default, and the template's
  other files would still be copied.

## 5. Production-readiness checklist

- security: no new write path. The pins remove two ways a developer's machine runs code inside a
  fixture repository: a global hook and a signing program.
- perf / scale: two more `git config` calls per factory repository, and one self-check of a few
  git calls.
- error / empty / loading states: a failed git call in the factory now raises `OSError` naming
  itself, where it used to return a repository with no commit.
- observability: the `OSError` text carries git's stderr; the self-check prints one line per
  observation.
- risks: an arm that called the factory twice on one path with no change would now raise on
  `nothing to commit`. None was found among the call sites read, and the arm of §7 runs the whole
  suite at the close. The target's own `check-wiring.sh` reads `core.hooksPath` as set rather than
  unset, and no arm over a factory target reads its hooks line (`tools/govkit/selftest.py:2813-2816`
  and `:2845-2848` filter `roles` lines).
- testing: `fixture_target.py --selftest`, and the arm of §7.
- migration: none.
- user docs: N/A — fixture infrastructure, with no page under `help/`.

## 6. Acceptance criteria

- **AC1** — When `python -I tools/govkit/fixture_target.py --selftest` runs, it exits 0. Its lines
  show the liveness half first: the unpinned control's commit refused, its `hooks-path` canary
  written, and the template's `pre-commit` copied. Then they show the factory's target: `base` at
  HEAD, no canary, no `.git/hooks/pre-commit`, and the signed commit through `run_git` raising
  `OSError` naming `commit`.
  Red when: the config loop drops `commit.gpgsign` (the base commit is refused and `run_git` raises
  out of `build_target`), drops `core.hooksPath` (the `hooks-path` canary is written), `init` drops
  `--template=` (the template's `pre-commit` is copied), or `run_git` returns on a non-zero exit
  (the signed commit raises nothing).
  fixture: planted by the flag under a temporary directory through `GIT_CONFIG_GLOBAL`; the tree
  holds none today.

## 7. Gates

`govkit selftest` · `govkit refusal join` · `govkit acceptance matrix` · `recall floor arms` · `policy fixtures` · `upgrade-walk` · `encoding posture (text IO names its encoding)` · `lexicon naming predicates` · `memory hygiene` · `spec tokens (a spec's own names resolve)`

New arm: tools/govkit/selftest.py · covers AC1 · `check_fixture_target` runs `fixture_target.py --selftest` beside `check_step_gate_fixture`, its failing case staged by a working copy whose config loop drops `commit.gpgsign` · none

## 8. Open questions

none

## 9. Revision log

- rev-1 · 2026-10-27 · initial draft, from TOOL-dSafePassage-26's build-pass finding that the
  factory's base commit inherits the machine's `commit.gpgsign` and `core.hooksPath` while `run_git`
  ignores a failed command, by `2026-10-27-prompt-TOOL-dSafePassage-67-2-spec-writer.md`.

## 10. Reuse audit

The seam extended is `build_scratch_gov` in `tools/govkit/fixture_target.py:27-34`. Its config loop
already pins `user.email`, `user.name` and `core.autocrlf` for every repository both factories build,
and `run_git` (`:21-24`) is the one git call under it. `python tools/codebase-map/reuse_lookup.py
"pin a scratch fixture repository's git config so commit signing and hooks are not inherited from
the machine's global config"` ranked `git`, `run_git`, `write_commit`, `build_git_env` and
`build_scratch_gov`. `build_scratch_gov` is the seam this unit extends. `build_git_env`
(`tools/memory-tree/tree_lib.py:232-243`) and `build_tree_git_env` pin a process environment, which
§4 rejects, and each `run_git` and `write_commit` is a caller's helper for its own repositories. The
recall probe found TOOL-aWokenSentinel-14's measurement of the same signing failure on a developer's
node and `memory/gotchas/fixture-inherits-ambient-machine-state.md`, the class this unit closes for
the factory.

Recall terms used: `python tools/memory-recall/query.py "fixture scratch repository inherits global git config commit signing gpgsign hooksPath" --terms "gpgsign hooksPath GIT_CONFIG_GLOBAL autocrlf fixture-inherits-ambient-machine-state build_scratch_gov fixture_target run_git check=False base commit fixture-passes-by-finding-nothing"`
