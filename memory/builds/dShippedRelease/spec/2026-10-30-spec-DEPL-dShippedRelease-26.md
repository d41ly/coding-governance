# DEPL-dShippedRelease-26 — the platform matrix verified per release: runner rows for `platforms.supported` under `platforms.verify`, generalizing `run-held-wsl.sh`, and a Linux job in emitted CI at the floor

**Status:** OPEN · rev-1 · 2026-10-30 · node d · Tier-2 · base f4597719 · streams deployer · order 28 · advances DEPL-dShippedRelease-32

**Carries:** cl-dClosedLoop-0436@57841d5d whole
**Carries:** node:policy-key.platforms.supported
**Carries:** node:policy-key.platforms.verify

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-30-build-DEPL-dShippedRelease-1-agent-ledger.md](../build/2026-10-30-build-DEPL-dShippedRelease-1-agent-ledger.md) | journal | DEPL-dShippedRelease-1 DEPL-dShippedRelease-2 DEPL-dShippedRelease-3 DEPL-dShippedRelease-4 DEPL-dShippedRelease-5 DEPL-dShippedRelease-6 DEPL-dShippedRelease-7 DEPL-dShippedRelease-8 DEPL-dShippedRelease-9 DEPL-dShippedRelease-10 DEPL-dShippedRelease-11 DEPL-dShippedRelease-12 DEPL-dShippedRelease-13 DEPL-dShippedRelease-14 DEPL-dShippedRelease-15 DEPL-dShippedRelease-16 DEPL-dShippedRelease-17 DEPL-dShippedRelease-18 DEPL-dShippedRelease-19 DEPL-dShippedRelease-20 DEPL-dShippedRelease-21 DEPL-dShippedRelease-22 DEPL-dShippedRelease-23 DEPL-dShippedRelease-24 DEPL-dShippedRelease-25 DEPL-dShippedRelease-27 DEPL-dShippedRelease-28 DEPL-dShippedRelease-29 DEPL-dShippedRelease-30 DEPL-dShippedRelease-31 |
| [2026-10-30-build-DEPL-dShippedRelease-1-spec-stage-returns.md](../build/2026-10-30-build-DEPL-dShippedRelease-1-spec-stage-returns.md) | research | DEPL-dShippedRelease-1 DEPL-dShippedRelease-2 DEPL-dShippedRelease-3 DEPL-dShippedRelease-4 DEPL-dShippedRelease-5 DEPL-dShippedRelease-6 DEPL-dShippedRelease-7 DEPL-dShippedRelease-8 DEPL-dShippedRelease-9 DEPL-dShippedRelease-10 DEPL-dShippedRelease-11 DEPL-dShippedRelease-12 DEPL-dShippedRelease-13 DEPL-dShippedRelease-14 DEPL-dShippedRelease-15 DEPL-dShippedRelease-16 DEPL-dShippedRelease-17 DEPL-dShippedRelease-18 DEPL-dShippedRelease-19 DEPL-dShippedRelease-20 DEPL-dShippedRelease-21 DEPL-dShippedRelease-22 DEPL-dShippedRelease-23 DEPL-dShippedRelease-24 DEPL-dShippedRelease-25 DEPL-dShippedRelease-27 DEPL-dShippedRelease-28 DEPL-dShippedRelease-29 DEPL-dShippedRelease-30 DEPL-dShippedRelease-31 |
| [2026-10-30-build-DEPL-dShippedRelease-3-reuse-scout-c.md](../build/2026-10-30-build-DEPL-dShippedRelease-3-reuse-scout-c.md) | research | DEPL-dShippedRelease-3 DEPL-dShippedRelease-6 DEPL-dShippedRelease-8 DEPL-dShippedRelease-15 DEPL-dShippedRelease-19 DEPL-dShippedRelease-22 |
| [2026-10-30-prompt-DEPL-dShippedRelease-1-spec-brief.md](../prompts/2026-10-30-prompt-DEPL-dShippedRelease-1-spec-brief.md) | research | DEPL-dShippedRelease-1 DEPL-dShippedRelease-2 DEPL-dShippedRelease-3 DEPL-dShippedRelease-4 DEPL-dShippedRelease-5 DEPL-dShippedRelease-6 DEPL-dShippedRelease-7 DEPL-dShippedRelease-8 DEPL-dShippedRelease-9 DEPL-dShippedRelease-10 DEPL-dShippedRelease-11 DEPL-dShippedRelease-12 DEPL-dShippedRelease-13 DEPL-dShippedRelease-14 DEPL-dShippedRelease-15 DEPL-dShippedRelease-16 DEPL-dShippedRelease-17 DEPL-dShippedRelease-18 DEPL-dShippedRelease-19 DEPL-dShippedRelease-20 DEPL-dShippedRelease-21 DEPL-dShippedRelease-22 DEPL-dShippedRelease-23 DEPL-dShippedRelease-24 DEPL-dShippedRelease-25 DEPL-dShippedRelease-27 DEPL-dShippedRelease-28 DEPL-dShippedRelease-29 DEPL-dShippedRelease-30 DEPL-dShippedRelease-31 |

<!-- /gen:spec-records -->

## 1. Goal

No platform matrix is declared: only Windows with Git-Bash is tested (`gap-tool-11`), and
`run-held-wsl.sh` refuses to start outside Windows. This unit declares the runners as rows, generalizes
the held split so a Linux host runs its own half, reports one verdict per supported platform at each
release under `platforms.verify`, and adds the Linux job to emitted CI, with Python set up at the floor
read from its one declaration.

## 2. Scope (IN)

Build-run preconditions, specced and DEFERRED at base `f4597719`: TOOL-dSafePassage-11's
`tools/lib/python-floor.txt`, TOOL-dSafePassage-12, TOOL-dWellOiledMachine-20's
`tools/runtime/points.toml` with `read_points`, TOOL-dWitnessedBar-6's `read_remote_verdict`, and
TOOL-dWitnessedBar-11's `leg_factory.py`. Every node runs Python 3.15 (AP-31); node d ran 3.14.5 at this
draft. Nothing here is a stand-in.

- **S1** — The point, I21. `tools/runtime/points.toml` gains a `[[point]]` row `point.flow.platform-runners`
  and two `[[adapter]]` rows, `windows-gitbash` and `linux`, each with TOOL-dWellOiledMachine-20 S4's
  fields, `grant` anonymous, and four fields this unit declares and grades: `half`, the partition's half
  name; `uname`, the `uname -s` prefixes of a host that runs it natively; `runs-on`, its emitted CI
  runner; and `launch`, the argv that reaches it from another host, empty where none exists.
  `read_platform_runners(root)` and `check_platform_runners(rows)` in
  `tools/run-gates/platform_matrix.py` read and grade them, the rows found through the inline
  `resolve_kit_dir`, with `RUNNER_DEFAULTS` read where the runtime kit is absent and held equal to the
  rows by an arm. Observed by AC1.
- **S2** — The partition generalized. `HOSTS` in `tools/run-gates/held_halves.py:61` is read from those
  rows' `half` fields, and `--half`'s choices at `:427` follow it. The two half names keep their
  spelling, so the record files, the parity file and `windows-only-legs.txt` keep their bytes. A row
  whose `half` the partition has no rule for is refused by name. Observed by AC2.
- **S3** — `run-held-wsl.sh` generalized. The Windows-side refusal at `:172-175` stays for the three
  public modes it guards, and a new mode, `--native`, runs on a host a row's `uname` names: it takes
  HEAD as the SHA and the worktree as the tree, and runs that row's half through the existing
  `run_half`. It refuses a dirty tree, as `run` does. A new mode, `--bar`, reached only through the
  `linux` row's `launch`, runs the plain bar in the WSL mirror at the SHA with a partition that leaves
  out the `platform matrix` leg. Observed by AC3.
- **S4** — The per-platform record. `held_halves.py --record --half <h> --dir <half dir> --root <root>`
  reads one half through `load_half` and writes `<git-common-dir>/platform-verdict/<sha>/<platform>`
  with `verdict`, `run_id`, `manifest_blob` and `kind`. `run-held-wsl.sh` calls it for each half after
  it combines, and `--native` and `--bar` call it for theirs. A red half is recorded too. Observed by
  AC3 and AC4.
- **S5** — The reading, `python platform_matrix.py verify --sha <sha> [--ci-rows <file>]`, with
  `derive_platform_rows(root, sha)`. It reads `read_policy("platforms.supported")` and
  `read_policy("platforms.verify")` and prints one line per supported platform,
  `platform — <name> · <verified|red|unverified|off> · <how>`, and it exits as §4 "The four values"
  states. A supported platform with no runner row reads `unverified · no runner registered`. Observed
  by AC4, AC5, AC6, AC7 and AC8.
- **S6** — The `bar` value's leg. `python platform_matrix.py bar`, a `[[gate_leg]]` row `platform matrix`
  of `tools/run-gates/kit.toml` made by `leg_factory.py new`, prints one skip line and exits 0 under any
  other value. Under `bar` it runs each supported platform's `launch` from this host and exits 1 on a
  red, or on a platform this host cannot reach. Observed by AC6.
- **S7** — Per release. `cmd_cut` (DEPL-dShippedRelease-3 S5) runs `verify` on the SHA it is about to
  tag, after `read_gov_first`, refuses as `verify` exits, and appends its lines to the notes as a
  `platforms` section after `derive_release_notes` returns, because those lines depend on the node and
  that text does not. So each release records what was verified. Observed by AC9.
- **S8** — Emitted CI. `gov-bar.template.yml` (DEPL-dShippedRelease-8) gains the job block per supported
  platform with a row, each named `bar-<platform>`, `runs-on` from the row, a `{{ACTION_SETUP_PYTHON}}`
  step and `python-version: '{{PYTHON_FLOOR}}'`. `ci_emit.py render` reads `platforms.supported` by a
  literal call, and the floor from the target receipt's `python_floor`, else from `read_python_floor`
  in gov's own tree, and refuses when neither answers. So the default set emits the Linux job. Observed
  by AC10.
- **S9** — The floor's record. The floor is read from its one declaration through the kit factory's
  `read_python_floor`, and the receipt's `python_floor` is DEPL-dShippedRelease-25's write. This unit
  writes neither, and adds no floor of its own. Observed by AC11.
- **S10** — The key rows. `platforms.supported` and `platforms.verify` gain `summary` and `usage` on their
  one catalogue row each (`tools/policy/catalogue.toml:1615`, `:1622`), and both names leave
  `tools/policy/unsummarised-keys.txt` by `policy.py lists --write`. Allowed values and defaults stay the
  rows'. Observed by AC12.
- **S11** — The docs. `help/platforms.md`, with its row in `help/README.md`, states the four values, what
  a release records and how a Linux node runs its half. `tools/run-gates/README.md` gains the same, and
  the header of `tools/run-gates/run-held-wsl.sh` names the new modes. Observed by AC13.

## 3. Non-goals (OUT)

- `platforms.provision`: TOOL-dSafePassage-11's and its build's.
- A Linux job in `.github/workflows/remote-ci.yml` (§8 F3).
- Making any leg green on Linux. `gap-tool-11` closes when the matrix is declared and read. The WSL
  failures it cites are what the report then shows, and `held` keeps them from stopping a release until
  the owner moves the key (§8 F2).
- The macOS and pwsh-launch runners. v2's `[planned]` holds both behind triggers, so each reads
  `unverified · no runner registered` here.
- Per-kit floors (§8 F6), the receipt field and `read_python_floor`.
- `held-green`'s semantics and the paired-run parity record, which stay as they are.
- The action pins and the template's other lines: DEPL-dShippedRelease-8's.

### Edges

- **consumes-from** `DEPL-dShippedRelease-10` — `kit-schema.toml` and `read_python_floor`, the floor the factory reads; without them emitted CI has no floor in gov's tree
- **consumes-from** `DEPL-dShippedRelease-25` — `python_floor`, the receipt's record of the floor, which `ci_emit.py render` reads in an adopter; without it an adopter's render refuses
- **consumes-from** `DEPL-dShippedRelease-8` — `action-pins.toml`, `ci_emit.py` and `gov-bar.template.yml`; without them S8 has no emitter, into which this unit adds the floor, `actions/setup-python` and the Linux job
- **consumes-from** `DEPL-dShippedRelease-3` — `govkit.py cut` and its notes, where S7 reports the matrix; without it nothing is verified per release
- **consumes-from** external — TOOL-dWellOiledMachine-20's `tools/runtime/points.toml`, TOOL-dWitnessedBar-6's `read_remote_verdict`, and a WSL distro or a native Linux node the operator provides; with no such node the `linux` row reads unverified

## 4. Design

### The four values

`platforms.verify` says who runs the matrix and whether a miss stops a release. "Behind" below means the
newest record at or within `PLATFORM_WALK` first-parent commits behind the SHA, because a held run or a
bar runs at a tip that is rarely the tag's own commit.

| Value | Who runs a platform | What `verify` reads | `verify` exits |
|---|---|---|---|
| `held` | the held tier, `run-held-wsl.sh` or `--native`, on a node that has the host | the record at or behind the SHA | 0 always, the lines stating what holds |
| `bar` | the leg `platform matrix` at each bar, the plain bar on each reachable platform | the record at or behind the SHA | 1 on `red` or `unverified` |
| `ci` | the emitted job `bar-<platform>` | that job's conclusion at the SHA | 1 on `red` or `unverified` |
| `off` | nobody | nothing | 0, each line `off` |

A record is a claim by the node that wrote it, kept under its git common dir, so a node with no record
reads `unverified`, never green.

### Reading `ci`

`derive_platform_rows` calls `read_remote_verdict` with the workflow `.github/workflows/gov-bar.yml` and
the job `bar-<platform>`, and maps `GREEN` to `verified`, `RED` to `red`, and `NONE`, `HELD` and
`DEAD PROBE` to `unverified`. That function reads one declared job today, so the build adds a `job`
keyword defaulting to `bar`, and no caller changes. `--ci-rows <file>` reads saved rows of the same
shape in place of the network, which is what a fixture plants.

### The generalization

`run_half` already takes a host, a tree, a directory and a half, and the `--half` branch is host-agnostic
but for its `/mnt/` refusal and its `PATH` scrub, which only matter under WSL. So `--native` is a small
branch reaching the same function, and the two half names stay partition rules: `windows` runs the
declared Windows-only legs, and `wsl` runs every other held leg, on WSL or on a native Linux host alike.

```toml
# tools/runtime/points.toml
[[adapter]]
point = "point.flow.platform-runners"
name = "linux"
tenancy = "local"
retention = "none"
region = "local"
grant = { service = "local", scopes = [], secret = "anonymous" }
half = "wsl"
uname = ["Linux"]
runs-on = "ubuntu-latest"
launch = ["bash", "{kit}/run-held-wsl.sh", "--bar"]
```

### The policy reads

`read_policy(key)` in `platform_matrix.py` and in `ci_emit.py` runs `policy.py get <key> --json` as a
bounded subprocess, the policy kit found through the inline `resolve_kit_dir`, because a kit imports no
sibling kit. With no policy kit it reads the catalogue's defaults from `PLATFORM_DEFAULTS` and prints one
line, the copy held to the catalogue by an arm. The calls are literal, which the reader-coverage arm's
first `READER_SHAPES` row counts (`tools/policy/check_policy.py:424`).

### Inventory

| Minted | Kind | Home |
|---|---|---|
| `point.flow.platform-runners` | point, rows `windows-gitbash`, `linux` | `tools/runtime/points.toml` |
| `half`, `uname`, `runs-on`, `launch` | adapter fields | the point's rows |
| `platform_matrix.py`, `verify`, `bar`, `rows` | module and verbs | `tools/run-gates/` |
| `read_platform_runners`, `check_platform_runners`, `derive_platform_rows`, `read_policy` | functions | `platform_matrix.py` |
| `RUNNER_DEFAULTS`, `PLATFORM_DEFAULTS`, `PLATFORM_WALK` | constants | `platform_matrix.py` |
| `--native`, `--bar` | modes | `run-held-wsl.sh` |
| `--record` | mode | `held_halves.py` |
| `platform-verdict/<sha>/<platform>` | node-local record | the git common dir |
| `platform matrix` | gate leg | `tools/run-gates/kit.toml` |
| `{{PYTHON_FLOOR}}`, `{{ACTION_SETUP_PYTHON}}` | template tokens | `gov-bar.template.yml` |

`lexicon.py --suggest <name> --as py.function` printed OK for `read_platform_runners`,
`check_platform_runners`, `derive_platform_rows` and `read_policy` on 2026-10-30. `PLATFORM_WALK` is 64
commits, PINNED here as a design choice.

### Migration

Additive. `HOSTS` keeps its two values at gov's rows, so a held run keeps its bytes. No receipt field is
written here.

### Rollout

`held` is the default and gov's value, so the first release's notes state which platforms a held run
reached, and nothing refuses. The leg prints its skip line on gov.

### Files touched (estimate)

- `tools/run-gates/platform_matrix.py`
- `tools/run-gates/held_halves.py`
- `tools/run-gates/run-held-wsl.sh`
- `tools/run-gates/kit.toml`
- `tools/run-gates/README.md`
- `tools/runtime/points.toml`
- `tools/integrations/ci/ci_emit.py`
- `tools/integrations/ci/gov-bar.template.yml`
- `tools/govkit/govkit.py`
- `tools/govkit/selftest.py`
- `tools/policy/catalogue.toml`
- `tools/policy/unsummarised-keys.txt`
- `tools/gate-legs.json`, rendered from the kit's `[[gate_leg]]` rows by `leg_factory.py --write`
- `help/platforms.md`
- `help/README.md`

### Alternatives rejected

- **A new runner script beside `run-held-wsl.sh`.** The test: `run_half`, the record copy and the partition
  are the bulk of the work and already host-agnostic, so a second script copies them (`[reuse]`).
- **Renaming the halves to the platform names.** The test: `windows` and `wsl` are written into each half's
  `meta`, the parity file and the selftest's arms, and the partition rule is what they name, so a rename
  moves bytes and buys nothing a row's `half` field does not.
- **Runner rows in a file of the run-gates kit.** The test: I21 and TOOL-dWellOiledMachine-20 S4 make a point
  and its adapters the registry's, and the `resolves` check reads `point.*` tokens against it.
- **Verifying at every landing.** The test: the clause says "per release", and `gap-tool-11`'s Linux half is
  not green, so a landing refusal would stop every build (§8 F2).

## 5. Production-readiness checklist

- security: `launch` is a descriptor argv in a kit file, run by a leg under `bar` only, with the same trust
  as a `[[gate_leg]]` argv. `--ci-rows` reads a file and runs nothing. `ci` reads anonymously through the
  bounded GET TOOL-dWitnessedBar-6 specifies.
- perf / scale: `verify` is one policy read, a walk of at most `PLATFORM_WALK` commits and a file read per
  platform. `bar` adds a whole bar per reachable platform, so the leg's ceiling is its own and the value is
  opt-in.
- error / empty / loading states: a refused read exits 2. An unknown `half` is refused. An empty
  `platforms.supported` is refused by the catalogue's `empty = "never"`. No record reads `unverified`.
- observability: one line per platform at the cut and in the notes, naming how each was read and how far
  behind the SHA.
- risks: `held` reports and never refuses, so a red Linux half can ship with the notes saying so. That is
  v2:1402's stated posture until the owner moves the key. A record is node-local, so a node that never ran
  a half cuts with `unverified` lines. The floor in an emitted workflow is frozen at render, and the next
  update's `[[regenerate]]` moves it.
- testing: the probes of §6 and the arms of §7.
- migration: §4 "### Migration".
- user docs: `help/platforms.md`, S11.

## 6. Acceptance criteria

- **AC1** — When `python platform_matrix.py rows` runs on the tree, it prints the two rows with `half`,
  `uname`, `runs-on` and `launch`, and `check_platform_runners` finds nothing. With a planted row whose
  `half` is `macos`, it exits 2 naming the row.
  Red when: a row with no partition rule passes, or `RUNNER_DEFAULTS` differs from the rows.
- **AC2** — When `python tools/run-gates/held_halves.py --partition --half wsl --out <file>` runs on gov's
  manifest, its output equals the base's, and `--half windows` likewise.
  Red when: reading `HOSTS` from rows moves a leg between halves.
  fixture: the output at `f4597719`, taken by the pass before its edit.
- **AC3** — When `bash tools/run-gates/run-held-wsl.sh --native` runs in a fixture clone with a stub `uname`
  printing `Linux` and a one-leg manifest, it exits 0 and `<git-common-dir>/platform-verdict/<sha>/linux`
  holds `verdict GREEN`. With the stub printing `Darwin` it exits 2 naming the rows.
  Red when: the script still refuses a Linux host, or runs on a host no row names.
  fixture: a scratch clone under `%TEMP%` and a stub on `PATH`.
- **AC4** — When `python platform_matrix.py verify --sha <sha>` runs in a fixture whose landed
  `.governance/policy.toml` sets `verify = "held"` under `[platforms]`, with a planted `RED` record for
  `linux` and none for `windows-gitbash`, it prints `red` and `unverified` and exits 0.
  Red when: `held` refuses a release, or reads a missing record as `verified`.
- **AC5** — When `python platform_matrix.py verify --sha <sha>` runs with `verify = "off"` planted, it
  prints `off` for each supported platform, reads no record and exits 0.
  Red when: `off` is read as a missing policy file, or a line claims a verification.
- **AC6** — When `python platform_matrix.py bar` runs with `verify = "bar"` planted and a row's `launch` a
  stub exiting 1, it exits 1 naming the platform; with the stub exiting 0 it exits 0; and with a platform
  no `launch` reaches it exits 1 naming `unverified`. Under `held` it prints its skip line and exits 0.
  `verify --sha` then exits 1 on a planted `RED` record under `bar`.
  Red when: the leg runs under any other value, or an unreachable platform passes.
- **AC7** — When `python platform_matrix.py verify --sha <sha> --ci-rows <file>` runs with `verify = "ci"`
  planted, it exits 0 on rows `GREEN` for both jobs, and exits 1 on one `RED`, on one `NONE` and on one
  `DEAD PROBE`.
  Red when: a dead probe reads green, or a job absent from the workflow does.
- **AC8** — When `python platform_matrix.py verify --sha <sha>` runs with `supported` planted as `["linux"]`,
  it prints one line and never names `windows-gitbash`. With `["linux", "macos", "pwsh-launch"]` it prints
  `unverified · no runner registered` for the last two. With `[]` it exits 2.
  Red when: a planned platform reads verified, or the empty set is read as nothing to verify.
- **AC9** — When `python tools/govkit/govkit.py cut` runs in a fixture under `verify = "ci"` with a planted
  `RED` row it exits 1 and tags nothing. Under `held` it tags, and the tag's notes hold a `platforms`
  section naming each supported platform.
  Red when: a release records nothing about its platforms.
  fixture: a scratch clone and a bare remote under `%TEMP%`, after DEPL-dShippedRelease-3 is built.
- **AC10** — When `python ci_emit.py render --target <fixture>` runs with `[gate_runner.ci]` declared and a
  receipt holding `"python_floor": "3.15"`, the emitted file holds a job `bar-linux` with
  `runs-on: ubuntu-latest`, and `python-version: '3.15'`, and `python ci_emit.py check` exits 0 over it.
  With the receipt lacking the field it exits 2.
  Red when: the Linux job is absent, the floor is typed in the template, or a `uses:` line escapes its pin.
- **AC11** — When `python -c` calls `read_python_floor` on the tree and the fixture of AC10 is rendered from
  gov's own tree with no receipt, the emitted `python-version` equals the value it returns.
  Red when: a second declaration of the floor exists.
- **AC12** — When `grep -cxE 'platforms\.(supported|verify)' tools/policy/unsummarised-keys.txt` runs it
  prints `0`, `python tools/policy/policy.py lists --check` exits 0, and a grep of `platform_matrix.py` for
  `read_policy("platforms` prints both literal calls.
  Red when: a key has no literal reader, which the policy kit's reader-coverage arm reds once this build
  is terminal.
- **AC13** — When `grep -n 'platforms.md' help/README.md` runs it prints the row, and a grep for `--native`
  over `tools/run-gates/run-held-wsl.sh` and `tools/run-gates/README.md` prints each file's statement.
  Red when: a Linux node's operator has no page, or the script's header omits a mode.

## 7. Gates

`govkit selftest` · `govkit refusal join` · `govkit acceptance matrix` · `policy fixtures` · `recall floor arms` · `measure-legs selftest` · `run-gates canary` · `run-gates gov canary` · `memory hygiene` · `spec tokens (a spec's own names resolve)`

New arm: tools/run-gates/platform_matrix.py · covers AC1 AC4 AC5 AC6 AC7 AC8 · each value of both keys planted, a planted `half`, a stub `launch`, saved rows naming each verdict state · none
New arm: tools/run-gates/held_halves.py · covers AC2 AC3 · the partition compared with its base shape, and a one-half record · none
New arm: tools/integrations/ci/ci_emit.py · covers AC10 AC11 · a fixture receipt with and without `python_floor` · none
New arm: tools/govkit/selftest.py · covers AC9 · a fixture cut under `ci` with a planted red row · none

The leg `platform matrix` is new, so it sits on the `New arm:` line and not the leg line above. What these do
not check: that a Linux green means what a Windows green means, which the paired runs own;
that a real Linux node passes; or that a recorded verdict was truly earned, since a record is node-local.

## 8. Open questions

- **F1 — What does each `platforms.verify` value do?** v2:1402, the away pass's AP-18 and research-compatibility
  F4 name the values, and no record defines them. Options: the table of §4; or `bar` as the held tier run
  inside the bar, which a bar's wall cannot hold. RESOLVED (agent, 2026-10-30, delegated): §4's table, rung 3,
  each value the plainest reading of its word: the held tier, the bar, CI, nothing. widens: none · relaxes: none
- **F2 — Does a red or unverified platform stop a release under `held`?** Options: (a) report and never refuse;
  (b) refuse. AP-18 reads "held, until the Linux half is green, then ci", so `held` is the state before green,
  and (b) stops the first `kits.cut` on `gap-tool-11`'s own reds, against `gap-deploy-11`. RESOLVED (agent,
  2026-10-30, delegated): (a), rung 1, and `bar` and `ci` refuse. widens: none · relaxes: none
- **F3 — Does gov gain a Linux job for `platforms.verify: ci` (scout C F11)?** Options: (a) a job in
  `.github/workflows/remote-ci.yml`; (b) none, gov stays `held`, and under `ci` a supported platform with no
  job reads `unverified`. The clause adds Linux to emitted CI only, `remote-ci.yml:19-21` argues against it
  ("a Linux runner's first reds would measure the host rather than the tree"), and gov's key is `held`.
  RESOLVED (agent, 2026-10-30, delegated): (b), rung 1. The strict preset's `ci` meets the emitted job in an
  adopter, and a preset run on gov would read `unverified` and refuse, by name. widens: none · relaxes: none
- **F4 — How is `run-held-wsl.sh` generalized?** Options: (a) rows name the runners, `HOSTS` reads them, and a
  `--native` mode reaches `run_half`; (b) a new script per platform. RESOLVED (agent, 2026-10-30, delegated):
  (a), rung 3, the seam the clause names. widens: none · relaxes: none
- **F5 — Who owns the runner adapters?** TOOL-dWitnessedBar-24:99 assigns them to its unit 9, whose
  `[[test_runner]]` is test-level, and v2:1873 and :1879 put the macOS and pwsh adapters on dWitnessedBar.
  RESOLVED (agent, 2026-10-30, delegated): this unit, rung 1, since the clause says "platform runner adapters"
  and the planned two wait for their triggers. widens: none · relaxes: none
- **F6 — One floor, or a floor per kit?** research-compatibility:146 says per kit, and P37 and this clause say
  one declaration. RESOLVED (agent, 2026-10-30, delegated): one, rung 1, the later word. widens: none · relaxes: none
- **F7 — How does a Linux node's verdict reach a release?** Options: (a) a node-local record the cut reads, with
  `unverified` where absent; (b) a ref a second node can read. (b) adds a remote write for a report `held` never
  acts on, and `ci` already reads the host. RESOLVED (agent, 2026-10-30, delegated): (a), rung 3, and
  `held-green` stays unread by any boundary, as `run-held-wsl.sh:31` states. widens: none · relaxes: none

## 9. Revision log

- rev-1 · 2026-10-30 · initial draft.

## 10. Reuse audit

The seams extended are `run_half` in `tools/run-gates/run-held-wsl.sh:135`, `HOSTS` at
`tools/run-gates/held_halves.py:61`, `--half` at `:427` and `load_half` at `:147`, plus
DEPL-dShippedRelease-8's emitter and the `GATE_LEGS` seam for the `--bar` partition.
`reuse_lookup.py "split the held self-test tier across platform hosts and combine verdicts"` ranked
`build_self_chain`, `read_host_name` and `parse_verdicts`, each a name-stem neighbour and none a seam here,
and the source disagrees by holding the exact seam at the two files above. Scout C's rows held at `f4597719`,
its `:157` and `:172-175` citations read true, and its disagreement 12 stands: the Windows-side refusal is at
`:174`. Disagreement 13 is §8 F3, and disagreement 11 is why `python_floor` is DEPL-dShippedRelease-25's. The
recall probe found the scout's row, the brief, and research-compatibility's F3 and F4, which this spec
follows. Candidates rejected and their tests are under §4 "### Alternatives rejected".

Recall terms used: `python tools/memory-recall/query.py "how are the platforms verified per release and how does the held tier split" --terms "platforms.verify platforms.supported run-held-wsl held_halves Linux half parity interpreter floor runner adapter"`
