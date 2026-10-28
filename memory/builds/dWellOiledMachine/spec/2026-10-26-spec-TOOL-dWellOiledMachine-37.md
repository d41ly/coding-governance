# TOOL-dWellOiledMachine-37 — the launch preflight: no hook- or permission-skipping launch, trusted hooks by hash, an allowlisted environment, the credential order, and relative worktree pointers

**Status:** DEFERRED · rev-2 · 2026-10-27 · node a · Tier-2 · base 0689e7fa · streams tooling · order 29 · advances TOOL-dWellOiledMachine-62

**Carries:** cl-dClosedLoop-0315@b5839378 whole
**Carries:** node:policy-key.runtime.secret-home

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-26-build-TOOL-dWellOiledMachine-1-reuse-scout-a.md](../build/2026-10-26-build-TOOL-dWellOiledMachine-1-reuse-scout-a.md) | research | TOOL-dWellOiledMachine-1 TOOL-dWellOiledMachine-6 TOOL-dWellOiledMachine-7 TOOL-dWellOiledMachine-8 TOOL-dWellOiledMachine-9 TOOL-dWellOiledMachine-19 TOOL-dWellOiledMachine-25 TOOL-dWellOiledMachine-30 TOOL-dWellOiledMachine-32 TOOL-dWellOiledMachine-36 TOOL-dWellOiledMachine-39 TOOL-dWellOiledMachine-43 TOOL-dWellOiledMachine-45 TOOL-dWellOiledMachine-46 TOOL-dWellOiledMachine-47 TOOL-dWellOiledMachine-49 TOOL-dWellOiledMachine-53 TOOL-dWellOiledMachine-56 |
| [2026-10-26-build-TOOL-dWellOiledMachine-1-spec-stage-returns.md](../build/2026-10-26-build-TOOL-dWellOiledMachine-1-spec-stage-returns.md) | journal | TOOL-dWellOiledMachine-1 TOOL-dWellOiledMachine-2 TOOL-dWellOiledMachine-6 TOOL-dWellOiledMachine-10 TOOL-dWellOiledMachine-11 TOOL-dWellOiledMachine-12 TOOL-dWellOiledMachine-13 TOOL-dWellOiledMachine-14 TOOL-dWellOiledMachine-15 TOOL-dWellOiledMachine-16 TOOL-dWellOiledMachine-17 TOOL-dWellOiledMachine-20 TOOL-dWellOiledMachine-21 TOOL-dWellOiledMachine-22 TOOL-dWellOiledMachine-23 TOOL-dWellOiledMachine-31 TOOL-dWellOiledMachine-32 TOOL-dWellOiledMachine-33 TOOL-dWellOiledMachine-35 TOOL-dWellOiledMachine-36 TOOL-dWellOiledMachine-38 TOOL-dWellOiledMachine-39 TOOL-dWellOiledMachine-40 TOOL-dWellOiledMachine-55 TOOL-dWellOiledMachine-56 TOOL-dWellOiledMachine-57 TOOL-dWellOiledMachine-58 TOOL-dWellOiledMachine-60 TOOL-dWellOiledMachine-61 |
| [2026-10-27-build-TOOL-dWellOiledMachine-1-agent-ledger.md](../build/2026-10-27-build-TOOL-dWellOiledMachine-1-agent-ledger.md) | journal | TOOL-dWellOiledMachine-1 TOOL-dWellOiledMachine-2 TOOL-dWellOiledMachine-3 TOOL-dWellOiledMachine-4 TOOL-dWellOiledMachine-5 TOOL-dWellOiledMachine-6 TOOL-dWellOiledMachine-7 TOOL-dWellOiledMachine-8 TOOL-dWellOiledMachine-9 TOOL-dWellOiledMachine-10 TOOL-dWellOiledMachine-11 TOOL-dWellOiledMachine-12 TOOL-dWellOiledMachine-13 TOOL-dWellOiledMachine-14 TOOL-dWellOiledMachine-15 TOOL-dWellOiledMachine-16 TOOL-dWellOiledMachine-17 TOOL-dWellOiledMachine-18 TOOL-dWellOiledMachine-19 TOOL-dWellOiledMachine-20 TOOL-dWellOiledMachine-21 TOOL-dWellOiledMachine-22 TOOL-dWellOiledMachine-23 TOOL-dWellOiledMachine-24 TOOL-dWellOiledMachine-25 TOOL-dWellOiledMachine-26 TOOL-dWellOiledMachine-27 TOOL-dWellOiledMachine-28 TOOL-dWellOiledMachine-29 TOOL-dWellOiledMachine-30 TOOL-dWellOiledMachine-31 TOOL-dWellOiledMachine-32 TOOL-dWellOiledMachine-33 TOOL-dWellOiledMachine-34 TOOL-dWellOiledMachine-35 TOOL-dWellOiledMachine-36 TOOL-dWellOiledMachine-38 TOOL-dWellOiledMachine-39 TOOL-dWellOiledMachine-40 TOOL-dWellOiledMachine-41 TOOL-dWellOiledMachine-42 TOOL-dWellOiledMachine-43 TOOL-dWellOiledMachine-44 TOOL-dWellOiledMachine-45 TOOL-dWellOiledMachine-46 TOOL-dWellOiledMachine-47 TOOL-dWellOiledMachine-48 TOOL-dWellOiledMachine-49 TOOL-dWellOiledMachine-50 TOOL-dWellOiledMachine-51 TOOL-dWellOiledMachine-52 TOOL-dWellOiledMachine-53 TOOL-dWellOiledMachine-54 TOOL-dWellOiledMachine-55 TOOL-dWellOiledMachine-56 TOOL-dWellOiledMachine-57 TOOL-dWellOiledMachine-58 TOOL-dWellOiledMachine-59 TOOL-dWellOiledMachine-60 TOOL-dWellOiledMachine-61 TOOL-dWellOiledMachine-63 TOOL-dWellOiledMachine-64 TOOL-dWellOiledMachine-65 TOOL-dWellOiledMachine-66 TOOL-dWellOiledMachine-67 TOOL-dWellOiledMachine-68 TOOL-dWellOiledMachine-69 TOOL-dWellOiledMachine-70 TOOL-dWellOiledMachine-71 TOOL-dWellOiledMachine-72 TOOL-dWellOiledMachine-73 TOOL-dWellOiledMachine-74 TOOL-dWellOiledMachine-75 TOOL-dWellOiledMachine-76 TOOL-dWellOiledMachine-77 TOOL-dWellOiledMachine-78 TOOL-dWellOiledMachine-79 TOOL-dWellOiledMachine-80 TOOL-dWellOiledMachine-81 TOOL-dWellOiledMachine-82 TOOL-dWellOiledMachine-83 TOOL-dWellOiledMachine-84 TOOL-dWellOiledMachine-85 TOOL-dWellOiledMachine-86 TOOL-dWellOiledMachine-87 TOOL-dWellOiledMachine-88 TOOL-dWellOiledMachine-89 TOOL-dWellOiledMachine-90 TOOL-dWellOiledMachine-91 TOOL-dWellOiledMachine-92 TOOL-dWellOiledMachine-93 TOOL-dWellOiledMachine-94 TOOL-dWellOiledMachine-95 TOOL-dWellOiledMachine-96 TOOL-dWellOiledMachine-97 TOOL-dWellOiledMachine-98 TOOL-dWellOiledMachine-99 TOOL-dWellOiledMachine-100 TOOL-dWellOiledMachine-101 TOOL-dWellOiledMachine-102 TOOL-dWellOiledMachine-103 TOOL-dWellOiledMachine-104 TOOL-dWellOiledMachine-105 TOOL-dWellOiledMachine-106 TOOL-dWellOiledMachine-107 TOOL-dWellOiledMachine-108 TOOL-dWellOiledMachine-109 TOOL-dWellOiledMachine-110 TOOL-dWellOiledMachine-111 TOOL-dWellOiledMachine-112 TOOL-dWellOiledMachine-113 TOOL-dWellOiledMachine-114 TOOL-dWellOiledMachine-115 TOOL-dWellOiledMachine-116 TOOL-dWellOiledMachine-117 TOOL-dWellOiledMachine-118 TOOL-dWellOiledMachine-119 TOOL-dWellOiledMachine-120 TOOL-dWellOiledMachine-121 TOOL-dWellOiledMachine-122 TOOL-dWellOiledMachine-123 TOOL-dWellOiledMachine-124 TOOL-dWellOiledMachine-125 TOOL-dWellOiledMachine-126 TOOL-dWellOiledMachine-127 |
| [2026-10-27-build-TOOL-dWellOiledMachine-37-deviation-371.md](../build/2026-10-27-build-TOOL-dWellOiledMachine-37-deviation-371.md) | deviation | — |
| [2026-10-26-prompt-TOOL-dWellOiledMachine-1-spec-brief.md](../prompts/2026-10-26-prompt-TOOL-dWellOiledMachine-1-spec-brief.md) | research | TOOL-dWellOiledMachine-1 TOOL-dWellOiledMachine-2 TOOL-dWellOiledMachine-3 TOOL-dWellOiledMachine-4 TOOL-dWellOiledMachine-5 TOOL-dWellOiledMachine-6 TOOL-dWellOiledMachine-7 TOOL-dWellOiledMachine-8 TOOL-dWellOiledMachine-9 TOOL-dWellOiledMachine-10 TOOL-dWellOiledMachine-11 TOOL-dWellOiledMachine-12 TOOL-dWellOiledMachine-13 TOOL-dWellOiledMachine-14 TOOL-dWellOiledMachine-15 TOOL-dWellOiledMachine-16 TOOL-dWellOiledMachine-17 TOOL-dWellOiledMachine-18 TOOL-dWellOiledMachine-19 TOOL-dWellOiledMachine-20 TOOL-dWellOiledMachine-21 TOOL-dWellOiledMachine-22 TOOL-dWellOiledMachine-23 TOOL-dWellOiledMachine-24 TOOL-dWellOiledMachine-25 TOOL-dWellOiledMachine-26 TOOL-dWellOiledMachine-27 TOOL-dWellOiledMachine-28 TOOL-dWellOiledMachine-29 TOOL-dWellOiledMachine-30 TOOL-dWellOiledMachine-31 TOOL-dWellOiledMachine-32 TOOL-dWellOiledMachine-33 TOOL-dWellOiledMachine-34 TOOL-dWellOiledMachine-35 TOOL-dWellOiledMachine-36 TOOL-dWellOiledMachine-38 TOOL-dWellOiledMachine-39 TOOL-dWellOiledMachine-40 TOOL-dWellOiledMachine-41 TOOL-dWellOiledMachine-42 TOOL-dWellOiledMachine-43 TOOL-dWellOiledMachine-44 TOOL-dWellOiledMachine-45 TOOL-dWellOiledMachine-46 TOOL-dWellOiledMachine-47 TOOL-dWellOiledMachine-48 TOOL-dWellOiledMachine-49 TOOL-dWellOiledMachine-50 TOOL-dWellOiledMachine-51 TOOL-dWellOiledMachine-52 TOOL-dWellOiledMachine-53 TOOL-dWellOiledMachine-54 TOOL-dWellOiledMachine-55 TOOL-dWellOiledMachine-56 TOOL-dWellOiledMachine-57 TOOL-dWellOiledMachine-58 TOOL-dWellOiledMachine-59 TOOL-dWellOiledMachine-60 TOOL-dWellOiledMachine-61 |
| [2026-10-27-review-TOOL-dWellOiledMachine-1-spec-audit.md](../reviews/2026-10-27-review-TOOL-dWellOiledMachine-1-spec-audit.md) | spec-audit | TOOL-dWellOiledMachine-1 TOOL-dWellOiledMachine-10 TOOL-dWellOiledMachine-11 TOOL-dWellOiledMachine-12 TOOL-dWellOiledMachine-13 TOOL-dWellOiledMachine-14 TOOL-dWellOiledMachine-15 TOOL-dWellOiledMachine-16 TOOL-dWellOiledMachine-17 TOOL-dWellOiledMachine-18 TOOL-dWellOiledMachine-19 TOOL-dWellOiledMachine-2 TOOL-dWellOiledMachine-20 TOOL-dWellOiledMachine-21 TOOL-dWellOiledMachine-22 TOOL-dWellOiledMachine-23 TOOL-dWellOiledMachine-24 TOOL-dWellOiledMachine-25 TOOL-dWellOiledMachine-26 TOOL-dWellOiledMachine-27 TOOL-dWellOiledMachine-28 TOOL-dWellOiledMachine-29 TOOL-dWellOiledMachine-3 TOOL-dWellOiledMachine-30 TOOL-dWellOiledMachine-31 TOOL-dWellOiledMachine-32 TOOL-dWellOiledMachine-33 TOOL-dWellOiledMachine-34 TOOL-dWellOiledMachine-35 TOOL-dWellOiledMachine-36 TOOL-dWellOiledMachine-38 TOOL-dWellOiledMachine-39 TOOL-dWellOiledMachine-4 TOOL-dWellOiledMachine-40 TOOL-dWellOiledMachine-41 TOOL-dWellOiledMachine-42 TOOL-dWellOiledMachine-43 TOOL-dWellOiledMachine-44 TOOL-dWellOiledMachine-45 TOOL-dWellOiledMachine-46 TOOL-dWellOiledMachine-47 TOOL-dWellOiledMachine-48 TOOL-dWellOiledMachine-49 TOOL-dWellOiledMachine-5 TOOL-dWellOiledMachine-50 TOOL-dWellOiledMachine-51 TOOL-dWellOiledMachine-52 TOOL-dWellOiledMachine-53 TOOL-dWellOiledMachine-54 TOOL-dWellOiledMachine-55 TOOL-dWellOiledMachine-56 TOOL-dWellOiledMachine-57 TOOL-dWellOiledMachine-58 TOOL-dWellOiledMachine-59 TOOL-dWellOiledMachine-6 TOOL-dWellOiledMachine-60 TOOL-dWellOiledMachine-61 TOOL-dWellOiledMachine-7 TOOL-dWellOiledMachine-8 TOOL-dWellOiledMachine-9 |

<!-- /gen:spec-records -->

## 1. Goal

No preflight refuses a launch that skips hooks or permissions (`--bare`, `--safe-mode`, the skip flag),
an act session inherits its parent's messaging token, entrypoint and session variables, nothing orders
the act's credentials, and a worktree's pointer holds a Windows path WSL's git cannot open (gap-rt-28,
gap-rt-30, gap-rt-43, gap-tool-16). This unit puts one preflight between the launcher and every act
session: it refuses a skipping launch and a Codex launch whose wired hooks are not all trusted, scrubs
the launch environment to an allowlist, tries the act's credential in `runtime.act-auth`'s order with
`runtime.secret-home: env-injected` honoured on a headless node, refuses a credential list that is
empty or puts api-key first, and writes the workspace's worktree pointers relative.

## 2. Scope (IN)

- **S1** — The preflight, `check_launch_preflight(argv, env, harness, workspace)` in
  `tools/runtime/preflight.py`, called by `launch_act` (TOOL-dWellOiledMachine-1 S2) on the argv and
  environment it built, before it returns them; a refusal raises `LaunchRefused`, printed as
  `launch — refused · <rule> · <detail>`, and nothing starts. Observed by AC1 to AC5.
- **S2** — The skipping launch refused, rule `skip`: an argv carrying `--bare`, `--safe-mode`,
  `--dangerously-skip-permissions`, `--allow-dangerously-skip-permissions` or `--permission-mode
  bypassPermissions`, or a `--setting-sources` list lacking `project`; an environment carrying a
  non-empty `CLAUDE_CODE_SIMPLE` or `CLAUDE_CODE_SAFE_MODE`; and any settings source the act session
  loads, the managed, user, project and local settings files and each enabled plugin's hook file,
  holding `disableAllHooks: true`, `permissions.defaultMode` `bypassPermissions`, an `allow` rule on a
  gated tool (`Bash`, `PowerShell`, `Write`, `Edit`, `MultiEdit`, `NotebookEdit`, `Agent`, `Workflow`),
  or a `PermissionRequest` hook other than the dispatcher's (TOOL-dWellOiledMachine-10 S2, S9). Each
  refusal names the flag, variable or file and key. Observed by AC1.
- **S3** — Trusted hooks, rule `untrusted-hook`, for a Codex launch only: the SHA-256 of every hook
  file the workspace's Codex hook configuration wires must appear in the trusted set the store
  `read_capability("codex", "hook-trust-store")` names (TOOL-dWellOiledMachine-14 S3), a capability
  name this unit adds to `CAPABILITY_NAMES`. An unmeasured row, an unreadable store or a missing hash
  refuses, naming the hook. Observed by AC2.
- **S4** — The launch-environment allowlist, `derive_launch_env(parent_env)` in `preflight.py`, the one
  filter `launch_act` builds its environment from: it keeps only the names in `LAUNCH_ENV_ALLOW`, the
  operating system's own variables (`PATH`, `HOME`, `USERPROFILE`, `APPDATA`, `LOCALAPPDATA`,
  `SYSTEMROOT`, `SystemDrive`, `COMSPEC`, `PATHEXT`, `TEMP`, `TMP`, `TMPDIR`, `LANG`, `LC_ALL`,
  `TERM`, `USER`, `USERNAME`, `LOGNAME`, `SHELL`), so `CLAUDE_CODE_MESSAGING_TOKEN`,
  `CLAUDE_CODE_ENTRYPOINT`, `CLAUDE_CODE_SESSION_ID`, `CLAUDECODE`, every other `CLAUDE_*` variable,
  `ANTHROPIC_API_KEY` and every `GOV_SECRET_*` never reach an act; `launch_act` adds its own keys after
  the filter. Observed by AC3.
- **S5** — The credential order, `run_with_credentials(start, classes, refs)` in `preflight.py`:
  `classes` is `runtime.act-auth` read through `resolve` (`tools/policy/policy.py:752`), default
  `setup-token, oauth-shared`. Each class in order: `setup-token` and `api-key` read their value
  through `read_secret_ref` (TOOL-dWellOiledMachine-17 S4), which honours `runtime.secret-home`: under
  `os-keychain` Credential Manager on Windows or libsecret on a Linux desktop, under `env-injected` the
  variable the service manager hands the supervisor on a headless Linux node; the value enters only
  the act session's environment, as `CLAUDE_CODE_OAUTH_TOKEN` or `ANTHROPIC_API_KEY`, never a file or
  an argument. `oauth-shared` passes no credential: the harness reads its own login from its own store.
  An absent value, or a start failure classified `expired` or `rejected` by `AUTH_FAILURE_CLASSES`,
  moves to the next class; a failure classified `transient` relaunches on the same class up to
  `AUTH_TRANSIENT_ATTEMPTS` (2) times, counted apart from `RESUME_ATTEMPTS`, then moves on. Each step
  prints `credential — <class> · <outcome>`; no class left prints `launch — refused · no-credential`.
  gov reads and copies no credential file. Observed by AC4.
- **S6** — The schema refusal: the `allowed` table of `runtime.act-auth` (`tools/policy/catalogue.toml:1607-1611`)
  gains `last = ["api-key"]`, and `check_value` (`tools/policy/policy.py:143`) gains the arm for a
  `set` or `list` row: a member named in `last` followed by any other member is refused,
  `"api-key" must be last`. The empty list is already refused by `empty = "never"`. The policy kit's
  README states the `last` field. Observed by AC5.
- **S7** — Relative worktree pointers, rule `worktree-pointer`: `check_worktree_pointers(workspace)`
  reads the workspace's `.git` file and the `gitdir` file it points back from; an absolute path in
  either runs `git -C <workspace> worktree repair --relative-paths` and reads both again, and a pointer
  still absolute, or a git without `--relative-paths`, refuses the launch naming the file. Observed by
  AC6.
- **S8** — The fixture, `python preflight.py --fixture --plant <case>`: a scratch repository and worktree
  under `%TEMP%` with short names, a stub harness on `PATH` that prints a planted start failure, a
  planted secret store answering through `read_secret_ref`'s `env-injected` reading, and a planted
  Codex trusted-hook store. The live arm, `python preflight.py --live`, runs one launch per class whose
  credential the real store on this node holds and records each outcome, never a value. Observed by
  AC1 to AC7.
- **S9** — `help/runtime.md` gains the preflight's rules, the allowlist, the credential order and the
  two `runtime.secret-home` values. Observed by AC7.

## 3. Non-goals (OUT)

- Resolving the harness and the credential classes per role: TOOL-dWellOiledMachine-56, which passes
  `run_with_credentials` a role's classes and references.
- The secret store reader itself: TOOL-dWellOiledMachine-17's `read_secret_ref`.
- Measuring Codex's trusted-hook store: TOOL-dWellOiledMachine-36's fixture writes the
  `hook-trust-store` row it measures; until then S3 refuses every Codex launch.
- The tracked-settings class check: TOOL-dWellOiledMachine-10 S9 grades tracked settings at the bar;
  S2 reads every source at the launch.
- Creating worktrees: TOOL-dWellOiledMachine-11's allocator; S7 repairs the pointers of the one an act
  launches in.

### Edges

- **consumes-from** `TOOL-dWellOiledMachine-1` — `launch_act`, which calls S1 on the argv and environment it builds and builds its environment from S4
- **consumes-from** `TOOL-dWellOiledMachine-6` — `supervise.py`, whose act launches S5 wraps in the credential order
- **consumes-from** `TOOL-dWellOiledMachine-17` — `read_secret_ref`, the one reader of a setup token or key under `runtime.secret-home`
- **consumes-from** `TOOL-dWellOiledMachine-14` — `[[capability]]`, the table S3 adds `hook-trust-store` to and reads through `read_capability`
- **hands-off** `TOOL-dWellOiledMachine-56` — `run_with_credentials`, which that unit calls with a role's classes and references, and the `last` field it puts on `roles.auth.<role>`
- **consumes-from** external — the harness's own documented flags and settings keys, measured on CLI 2.1.292 by `claude --help`
- **consumes-from** `TOOL-dWellOiledMachine-77` — the launch marker rule: `derive_launch_env` keeps `GOV_SESSION_KIND` and `GOV_ACT` after its filter, so an act launch never binds `owner: yes`
- **hands-off** `TOOL-dWellOiledMachine-79` — `derive_launch_env` and `LAUNCH_ENV_ALLOW` (findings 20, 33, 56), which the spec audit's minors batch repairs

## 4. Design

### Evidence

- `claude --help` on CLI 2.1.292 (node a, 2026-10-26) documents `--bare` ("skip hooks … Sets
  CLAUDE_CODE_SIMPLE=1 … OAuth and keychain are never read"), `--safe-mode` (hooks disabled, "Sets
  CLAUDE_CODE_SAFE_MODE=1"), `--dangerously-skip-permissions`, `--allow-dangerously-skip-permissions`,
  `--permission-mode` with `bypassPermissions` among its choices, and `--setting-sources` naming
  `user, project, local`.
- This session's own environment carries `CLAUDE_CODE_SIMPLE`, `CLAUDE_CODE_MESSAGING_TOKEN`,
  `CLAUDE_CODE_ENTRYPOINT` and `CLAUDE_CODE_SESSION_ID`, the inheritance the harness research recorded
  (`memory/builds/dClosedLoop/build/2026-10-18-build-PLAY-dClosedLoop-1-research-harness-cli.md:82`).
- The live launcher today filters the environment by a deny list, `SETTINGS_VARS` and
  `CLAUDE_PROJECT_DIR`, and passes `--permission-mode bypassPermissions`
  (`tools/policy/check_policy.py:4289-4296`); scout A records that this preflight would refuse it.
- `check_value` admits `["api-key", "setup-token"]` for `runtime.act-auth` today: its list arm checks
  membership and repeats only (`tools/policy/policy.py:160-173`).
- git 2.54 on this node offers `git worktree repair --relative-paths`, and this worktree's `.git` file
  holds an absolute `gitdir:` path.

### The order, on a planted node

| Class tried | Store answer | Start | Next |
|---|---|---|---|
| `setup-token` | absent | none | `oauth-shared` |
| `setup-token` | a value | `expired` or `rejected` | `oauth-shared` |
| `setup-token` | a value | `transient` | `setup-token` again, at most twice |
| `oauth-shared` | not read by gov | started | done |

### Inventory

| Minted | Kind | Lexicon cell |
|---|---|---|
| `preflight.py`, `check_launch_preflight`, `LaunchRefused` | file, function, exception | `check`, OK |
| `derive_launch_env`, `LAUNCH_ENV_ALLOW` | function, constant | `derive`, OK |
| `run_with_credentials`, `AUTH_FAILURE_CLASSES`, `AUTH_TRANSIENT_ATTEMPTS` (2, PINNED) | function, constants | `run`, OK |
| `check_worktree_pointers` | function | `check`, OK |
| `hook-trust-store` | capability name | none |
| `last` | `allowed` field of the policy catalogue | none |

`AUTH_FAILURE_CLASSES` maps the harness's start-failure text to `expired`, `rejected` or `transient`;
its patterns are UNVERIFIED until S8's live arm records each class's text on a binary, and a text no
pattern matches is `rejected`, which moves on rather than retrying. `AUTH_TRANSIENT_ATTEMPTS` is PINNED
at 2, the contended OAuth refresh the harness research recorded resolving on one retry.

### Files touched (estimate)

- `tools/runtime/preflight.py`
- `tools/runtime/launch.py`: the preflight call and the S4 filter in `launch_act`
- `tools/runtime/harness.py`: `hook-trust-store` in `CAPABILITY_NAMES`
- `tools/runtime/harnesses/codex.toml`: the `hook-trust-store` row, `unmeasured`
- `tools/policy/catalogue.toml`: `last` on `runtime.act-auth`
- `tools/policy/policy.py`: the `last` arm of `check_value`
- `tools/policy/README.md`: the `last` field
- `help/runtime.md`

### Alternatives rejected

- **A deny list of variables.** The parent's next variable would pass; the research names three
  classes, entrypoint, session and messaging, and an allowlist refuses the ones nobody has met yet.
- **Reading the OAuth login from the harness's credential file.** The owner's AP-14: gov reads and
  copies no credential file.
- **Setting `worktree.useRelativePaths` in the repository's config.** It changes every worktree any
  tool adds, outside the act's own; S7 repairs the one the act launches in.

## 5. Production-readiness checklist

- security — deny by default at every rule: an unmeasured trust store, an unreadable settings source,
  an unclassified auth failure and an unrepaired pointer each refuse or move on, never pass; a
  credential value reaches only the act's environment.
- perf / scale — one parse of each settings file and one hash per wired hook per launch.
- error / empty / loading states — an absent store, an absent value and an empty list each answer by
  name; no credential left refuses the launch.
- observability — one `launch — refused` or `credential —` line per decision, naming the rule, class or
  file and never a value.
- risks — a harness that renames a flag or a variable passes the argv rule until the help text is
  re-measured; S8's live arm re-measures per binary.
- testing — the fixture cases under AC1 to AC6, the live arm, and the arms in §7.
- migration — `tools/policy/check_policy.py`'s live launcher passes `bypassPermissions` and is not a
  `launch_act` caller, so S1 does not reach it; a policy file listing api-key first is refused at its
  next read, naming the fix.
- user docs — `help/runtime.md` and the policy kit's README.

## 6. Acceptance criteria

- **AC1** — When `python preflight.py --fixture --plant skip` runs one launch per planted case,
  `--bare`, `--safe-mode`, `--dangerously-skip-permissions`, `--permission-mode bypassPermissions`,
  `--setting-sources user`, `CLAUDE_CODE_SIMPLE=1`, a project settings file holding
  `disableAllHooks: true`, a local file allowing `Bash(git fetch *)` and a user file adding a second
  `PermissionRequest` hook, each prints `launch — refused · skip` naming its flag, variable or file;
  the clean launch passes.
  Red when: any planted case starts the stub.
- **AC2** — When `--plant trust` hashes a Codex workspace's two wired hooks into the planted store and
  launches, it passes; with one hook changed by one byte, it prints `launch — refused · untrusted-hook`
  naming that hook; with the store row `unmeasured`, every Codex launch is refused.
  Red when: the edited hook launches, as a check that hashes nothing shows.
- **AC3** — When `--plant env` launches with a parent environment carrying
  `CLAUDE_CODE_MESSAGING_TOKEN`, `CLAUDE_CODE_ENTRYPOINT`, `CLAUDE_CODE_SESSION_ID` and
  `ANTHROPIC_API_KEY`, the stub's recorded environment holds none of them and holds `PATH`.
  Red when: any parent variable outside `LAUNCH_ENV_ALLOW` reaches the act.
- **AC4** — When `--plant credentials` runs one planted node per class, `setup-token` absent, expired,
  rejected and transient twice then admitted, and the store under `env-injected`, the printed
  `credential —` lines show the move to `oauth-shared` for the first three, two relaunches then a start
  on `setup-token` for the fourth with `RESUME_ATTEMPTS`'s count unchanged, and the value read from
  `GOV_SECRET_<NAME>` under `env-injected`; and `git grep -n ".credentials.json" -- tools`
  finds nothing.
  Red when: a class is skipped out of order, a transient failure moves on before its retries, or the
  retries draw on `RESUME_ATTEMPTS`.
  cost: the live arm launches one short act per class present on the node.
  fixture: the live arm needs the real store holding a setup token; this node's store is not
  inspected by the offline arm.
- **AC5** — When `python policy.py check` reads a planted policy file whose `runtime.act-auth` is
  `["api-key", "setup-token"]`, it refuses with `"api-key" must be last`, and `[]` is refused as
  before; `["setup-token", "api-key"]` is admitted.
  Red when: api-key before another entry is admitted, as the base `check_value` shows.
- **AC6** — When `--plant pointer` launches in a worktree whose `.git` file holds an absolute path,
  the file reads `gitdir: ../` relative afterwards and the launch passes; with `git` stubbed to reject
  `--relative-paths`, the launch prints `launch — refused · worktree-pointer`.
  Red when: an act launches over an absolute pointer.
- **AC7** — When `grep -n "env-injected\|LAUNCH_ENV_ALLOW\|untrusted-hook" runtime.md` runs over the
  help page, each is named.
  Red when: the page omits one.

## 7. Gates

`policy check` · `policy fixtures` · `lexicon naming predicates` · `spec tokens (a spec's own names resolve)` · `memory hygiene`

New arm: tools/runtime/preflight.py · covers AC1 AC2 AC3 AC4 AC6 · each planted case staged against a `launch_act` with the preflight call and the environment filter removed · none
New arm: tools/policy/check_policy.py · covers AC5 · a policy file listing api-key first, staged against `check_value` without the `last` arm · none

## 8. Open questions

- **F1 — Where is Codex's trusted set read from?** (a) A `hook-trust-store` capability row on the
  Codex adapter, measured by TOOL-dWellOiledMachine-36 and refusing every Codex launch while
  unmeasured; (b) a path typed in this unit's code. (b) asserts an unmeasured fact, which the
  capability table forbids (TOOL-dWellOiledMachine-14 S2). Rung 3, deny by default. RESOLVED (agent,
  2026-10-26, delegated): (a). widens: none · relaxes: none
- **F2 — Which side of the launcher runs the preflight?** (a) `launch_act` itself, so every caller is
  covered; (b) each starter, the supervisor and the fixtures. (b) leaves a starter that forgets it
  unguarded. Rung 3, logic in the shared core. RESOLVED (agent, 2026-10-26, delegated): (a). widens:
  none · relaxes: none
- **F3 — Is an unclassified start failure transient or final?** (a) Final, `rejected`, moving to the
  next class; (b) transient, retried. (b) can spend both retries on a credential the harness refused.
  Rung 3. RESOLVED (agent, 2026-10-26, delegated): (a). widens: none · relaxes: none

## 9. Revision log

- rev-1 · 2026-10-26 · initial draft.
- rev-2 · 2026-10-27 · §3 · Edges: the reciprocal of each edge the spec audit round 1's
  promoted units declare on this unit, mirrored from TOOL-dWellOiledMachine-77, TOOL-dWellOiledMachine-79.

## 10. Reuse audit

The seams extended are I2's `launch_act` (TOOL-dWellOiledMachine-1 S2, extracted from
`tools/policy/check_policy.py:4289`, whose dict filter on `os.environ` this unit turns from a deny list
into an allowlist), TOOL-dWellOiledMachine-17's `read_secret_ref` for every stored credential, the
capability table's reader `read_capability` (TOOL-dWellOiledMachine-14 S3), and the policy kit's
`check_value` (`tools/policy/policy.py:143`), which gains one arm. The probe
`python tools/codebase-map/reuse_lookup.py "scrub the environment and refuse a launch flag before
starting a headless session"` ranked `CensusRefused`, `ScopeRefused`, `extract_session` and
`derive_run_starts` by name stem; none filters an environment or reads a launch's argv, and scout A's
row names the same `check_policy.py:4291` precedent, which holds at this base. The unattended
preflight (`tools/unattended/unattended.sh:7341`, `verb_preflight`) checks a run's start, not an act
session's launch, so it is not the seam.

Recall terms used: `python tools/memory-recall/query.py "what must preflight refuse before an act
session launches and which credential does it try" --terms "preflight launch bare safe-mode skip
permissions allowlist messaging token setup-token oauth-shared api-key secret-home"`
