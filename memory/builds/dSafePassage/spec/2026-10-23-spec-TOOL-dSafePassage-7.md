# TOOL-dSafePassage-7 — the step kind's isolation contract, and the check of its needs-target field

**Status:** OPEN · rev-1 · 2026-10-23 · node d · Tier-2 · base 3708a705 · streams tooling · order 2 · advances TOOL-dSafePassage-14

**Carries:** cl-dClosedLoop-0024@7817c7d0 whole

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-23-build-TOOL-dSafePassage-7-deviation-21.md](../build/2026-10-23-build-TOOL-dSafePassage-7-deviation-21.md) | deviation | — |
| [2026-10-23-prompt-TOOL-dSafePassage-1-deviation-after-fix.md](../prompts/2026-10-23-prompt-TOOL-dSafePassage-1-deviation-after-fix.md) | research | TOOL-dSafePassage-1 TOOL-dSafePassage-11 TOOL-dSafePassage-13 |
| [2026-10-23-prompt-TOOL-dSafePassage-1-spec-brief.md](../prompts/2026-10-23-prompt-TOOL-dSafePassage-1-spec-brief.md) | research | TOOL-dSafePassage-1 TOOL-dSafePassage-2 TOOL-dSafePassage-3 TOOL-dSafePassage-4 TOOL-dSafePassage-5 TOOL-dSafePassage-6 TOOL-dSafePassage-8 TOOL-dSafePassage-9 TOOL-dSafePassage-10 TOOL-dSafePassage-11 TOOL-dSafePassage-12 TOOL-dSafePassage-13 |

<!-- /gen:spec-records -->

## 1. Goal

An upgrade step is code gov wrote, run over a tree gov does not own. Today nothing bounds what it
reaches: govkit's target-side spawns run with the target as working directory and the node's whole
environment (`tools/govkit/govkit.py:1218-1230`), so a step's `git mv` would fire the adopter's
hooks, its `python` would import from the adopter's tree, and both would hold the node's ambient
credential (`memory/gotchas/foreign-code-runs-on-the-ambient-credential.md`, the shape audit's M28
and M32). This unit puts one isolation contract in the step kind, so every caller inherits it: a
declared working directory, an environment built from an allowlist, Python's `-I`,
`core.hooksPath` pointed at an empty directory through `GIT_CONFIG_COUNT`, and no ambient
credential. It also checks each step's `needs-target` field by running the step under that contract
beside a planted target hook and a planted target module, so a step that needs target code fails
there and is marked attended. It closes no packet gap of its own; it is the execution half of
`gap-deploy-16` (no upgrade-step kind) that the step row of TOOL-dSafePassage-1 leaves open.

## 2. Scope (IN)

- **S1** — The environment. `build_step_env(scratch)` in `tools/govkit/upgrade_steps.py` returns a
  new dict built from `STEP_ENV_KEEP`, an allowlist of the names process creation needs (§4 "Data
  model"), copied from the parent only when present. It never starts from a copy of the parent's
  environment, so a name the list does not hold cannot survive, whatever it is called. It redirects
  the home and temp names into a fresh per-run scratch directory, and sets git's isolation names:
  `GIT_CONFIG_NOSYSTEM=1`, `GIT_CONFIG_GLOBAL` to the null device, `GIT_TERMINAL_PROMPT=0`, and
  `GIT_CONFIG_COUNT=2` carrying `core.hooksPath` = an empty directory in the scratch and
  `credential.helper` = the empty value. Observed by AC1, AC2, AC3 and AC4.
- **S2** — The argv. `resolve_step_argv(argv, ctx)` resolves a step argv for the contract. A leading
  `python`, one of the two interpreters TOOL-dSafePassage-1's grammar admits, becomes govkit's own
  interpreter followed by `-I`. A leading `bash`, the other, goes through `resolve_shell_argv`
  (`tools/govkit/govkit.py:1200-1215`). The grammar's three placeholders resolve through
  `resolve_tokens` (`tools/govkit/govkit.py:1233`): `{gov}`, gov's tool root, absolute; `{target}`,
  the target's checkout root, absolute; and `{prefix}`, the target's install prefix as
  `target_context` validates it (`tools/govkit/govkit.py:1436`). An argv left holding a token the
  context does not answer is a refusal naming the step id and the token. Observed by AC1, AC3 and
  AC7.
- **S3** — The runner. `run_step_isolated(row, phase, target, gov_root)` runs one phase of one step
  row, `up`, `down`, `witness` or `resume`, from the declared working directory, which is gov's
  checkout root (the step row's "run from gov's checkout", TOOL-dSafePassage-1's S1 grammar), with
  S1's environment and S2's argv. Output is captured and decoded as `run_target_argv` decodes it.
  The scratch directory is made fresh for the call and cleared after it. It returns a result whose
  `verdict` is `ok`, `failed` or `attended`, with the exit code and the last 20 lines of stderr. A
  row whose `needs-target` is true returns `attended` without a spawn, through `derive_step_mode`.
  This function is the one place a step row's argv is spawned, so the walk, the reverse walk, gov
  first and the leg inherit the contract by calling it. Observed by AC1, AC5 and AC6.
- **S4** — The plants. `write_target_plants(tree, canary_dir)` plants, in a scratch copy of a
  target tree, a hook script under every client-side hook name in the tree's effective hooks
  directory (its own `core.hooksPath` when set, else the directory `git rev-parse --git-path hooks`
  names), and two modules at the tree's root: `sitecustomize.py`, which any interpreter whose path
  holds the tree runs at start-up, and `json.py`, which shadows the standard module a step imports.
  Each writes a canary file naming itself when it runs. `read_plant_canaries(canary_dir)` lists the
  canaries present. The fixture also plants a parent-side credential: a global gitconfig whose
  `credential.helper` writes a canary, and a token variable. Observed by AC2, AC3, AC4 and AC5.
- **S5** — The check. `check_needs_target(row, tree, gov_root)` runs the row's `up`, then its
  `witness`, under the contract beside S4's plants, and returns one of four verdicts, each printed
  with the step id. `isolated`: both phases exit 0 and no canary ran. `breach`: a canary ran, named
  by the line, so the step reached target code the contract should have kept from it. `needs-target`:
  a phase failed and no canary ran, so the step needs target code; the line names the remedy,
  `needs-target = true`, under which the step is attended. `attended`: the row already declares
  `needs-target = true`, and nothing is spawned. Observed by AC5.
- **S6** — The fixture. `python3 "tools/govkit/upgrade_steps.py" fixture isolation [--plant <case>]`
  builds a scratch gov directory holding three synthetic step scripts and a scratch target
  repository, and observes S1 to S5 over them. Every plant is listed in §4 "Inventory". A
  `-stub` plant replaces one half of the contract inside the fixture process only, so the red each
  criterion names is observed without a switch in shipped code. Observed by AC1 to AC7.
- **S7** — The callers probe. `fixture isolation --plant callers` reads `upgrade_steps.py` and
  `govkit.py` with `ast` and lists each call of `subprocess.run`, `subprocess.Popen` or
  `run_target_argv` whose argv expression reads a step row's `up`, `down`, `witness` or `resume`
  key. It passes when the only such site is inside `run_step_isolated`. Observed by AC6.
- **S8** — The docs. `help/upgrade-steps.md`, the page TOOL-dSafePassage-1 opens and lists in
  `help/README.md`, gains a section "What a step can reach" stating the contract and what the
  `needs-target` field means. TOOL-dSafePassage-2 and TOOL-dSafePassage-4 add their sections to the
  same page. Observed by AC8.

## 3. Non-goals (OUT)

- The step row's grammar, its reader and the `needs-target` key itself: TOOL-dSafePassage-1. This
  unit reads the row through that reader.
- The walk that calls the runner, the receipt rows it writes, and what an `attended` verdict does to
  a walk: TOOL-dSafePassage-2. The reverse walk: TOOL-dSafePassage-4.
- Running every release-0 step under the contract. The release-0 tree and the walk over it are
  TOOL-dSafePassage-5's (`upgrade-walk`), at order 5; this unit ships the check and observes it on
  its own fixture, recorded as `2026-10-23-build-TOOL-dSafePassage-7-deviation-21.md` (§8 F2).
- A sandbox beyond the contract: no container, job object, filesystem jail or network block. A step
  that deliberately opens a path into the target, or reads a secret file by absolute path, is not
  stopped by an environment; S5's `breach` verdict is what catches the first.
- A timeout on a step phase. The clause asks none, and `update` is an attended verb today.
- Interpreters a shell step starts for itself. `-I` reaches the argv's own leading Python; a nested
  interpreter inherits S1's environment, which holds no `PYTHONPATH`, and nothing else.
- `kits.offer`'s mode and the `install.steps` policy, which decide when an unattended caller may
  run a step: dShippedRelease (research F6).
- Any policy key. This unit reads none.

### Edges

- **consumes-from** `TOOL-dSafePassage-1` — the step row reader `read_steps`, its `needs-target`, `up`, `down`, `witness` and `resume` keys and its three placeholders, the help page this unit adds a section to, and `tools/govkit/upgrade_steps.py` itself with its import seam from `govkit.py`; without them there is no row to run
- **hands-off** `TOOL-dSafePassage-2` — `run_step_isolated` and its `attended` verdict, the only spawn of a step argv the walk may use
- **hands-off** `TOOL-dSafePassage-4` — `run_step_isolated` for each `down`, and `attended` for a down that needs target code
- **hands-off** `TOOL-dSafePassage-11` — the runner the floor step's argv runs under, which hands that step the target root through its placeholder
- **hands-off** `TOOL-dSafePassage-5` — running this unit's needs-target check over the release-0 tree for every declared step, on a scratch clone of that tree because the plants change its bytes

## 4. Design

### Data model

The environment `build_step_env` returns:

| Name | Value |
|---|---|
| each of `STEP_ENV_KEEP` present in the parent | the parent's value |
| `HOME`, `USERPROFILE`, `APPDATA`, `LOCALAPPDATA`, `XDG_CONFIG_HOME` | `<scratch>/home` |
| `TMP`, `TEMP`, `TMPDIR` | `<scratch>/tmp` |
| `GIT_CONFIG_NOSYSTEM` | `1` |
| `GIT_CONFIG_GLOBAL` | `os.devnull` |
| `GIT_TERMINAL_PROMPT` | `0` |
| `GCM_INTERACTIVE` | `never` |
| `GIT_CONFIG_COUNT` | `2` |
| `GIT_CONFIG_KEY_0`, `GIT_CONFIG_VALUE_0` | `core.hooksPath`, `<scratch>/hooks`, an empty directory |
| `GIT_CONFIG_KEY_1`, `GIT_CONFIG_VALUE_1` | `credential.helper`, the empty string |

`STEP_ENV_KEEP` is `PATH`, `PATHEXT`, `SYSTEMROOT`, `SYSTEMDRIVE`, `WINDIR`, `COMSPEC`, `OS`,
`PROCESSOR_ARCHITECTURE`, `NUMBER_OF_PROCESSORS`, `LANG`, `LC_ALL` and `TZ`. The Windows names are
what process creation and Python's start-up need there; none carries a credential. Every name
`tools/memory-tree/tree_lib.py:262` lists in `GIT_ENV_LEAKS`, and every token variable, falls out
because nothing copies it in.

Measured on node d, 2026-10-23, git 2.54.0.windows.1, in a throwaway repository under `%TEMP%`: a
`post-index-change` hook under the repository's own `core.hooksPath` ran on a plain `git add` and
did not run with `GIT_CONFIG_COUNT` naming `core.hooksPath` = an empty directory, so the environment
pair outranks repository config. `git config --get-all credential.helper` read `manager` from
`C:/Program Files/Git/etc/gitconfig` plainly, and only the empty value under `GIT_CONFIG_NOSYSTEM=1`,
`GIT_CONFIG_GLOBAL=/dev/null` and the empty `credential.helper` pair; `git credential fill` then
exited 128 with terminal prompts disabled. PINNED at that date; the fixture re-observes all three.

The result of `run_step_isolated`:

```
{"verdict": "ok" | "failed" | "attended", "rc": int | None, "tail": str}
```

`ok` is exit 0. `failed` is any other exit or a spawn error, `rc` None for the latter, `tail` naming
it. `attended` spawns nothing and carries `rc` None.

### The flow

1. `derive_step_mode(row)` reads `needs-target` through TOOL-dSafePassage-1's reader. True returns
   `attended` before any directory is made.
2. A `tempfile.TemporaryDirectory(prefix="gk-step-")` holds `home/`, `tmp/` and the empty
   `hooks/`. The short prefix keeps a git call under it inside Windows' path limit.
3. `resolve_step_argv` resolves the phase's argv with `{"gov": <gov's tool root, absolute>,
   "target": <the target root, absolute>, "prefix": <the target's install prefix>}`.
4. One `subprocess.run` with `cwd=gov_root`, `env=build_step_env(scratch)`, captured, UTF-8 with
   `errors="replace"`.

The working directory is gov's checkout and never the target, so a shell step's relative path
names gov's file. Under `-I` Python adds neither the script's directory nor the working directory
to `sys.path`, and ignores every `PYTHON*` variable, so a target module is reachable only through a
path a step opens on purpose, which S5 reads as `breach`. When the target is gov's own checkout, as
in TOOL-dSafePassage-8, the target's code is gov's and the contract still applies whole.

### The check's fixture steps

`fixture isolation` writes three step scripts into the scratch gov directory: `clean.py`, which
writes one file into `{target}`, dumps its environment, `sys.flags.isolated` and its working
directory to a report file in the canary directory, and runs `git -C {target} add` over that file;
`reaches.py`, which imports `adopter_only`, a module only the target root holds; and `opens.py`,
which inserts `{target}` into `sys.path` and imports `adopter_only`. Each row's `witness` is a
`python -c` that tests the file `clean.py` writes.

### Inventory

Minted in `tools/govkit/upgrade_steps.py`: `build_step_env`, `resolve_step_argv`,
`run_step_isolated`, `derive_step_mode`, `write_target_plants`, `read_plant_canaries` and
`check_needs_target`; the constant `STEP_ENV_KEEP`; the fixture family `isolation`, its plants
`hook`, `hook-stub`, `module`, `module-stub`, `credential`, `credential-stub`, `needs-target`,
`breach`, `token` and `callers`; and the four verdict words of S5. Each function name passes the
`py.function` cell (`python3 tools/lexicon/lexicon.py --suggest <name> --as py.function`, OK for all
seven, 2026-10-23). The section "What a step can reach". No conf key, no gate leg, no policy key.

### Migration

None. No step row exists before TOOL-dSafePassage-1 and TOOL-dSafePassage-3 land theirs, and no
caller spawns one until TOOL-dSafePassage-2 wires the walk.

### Rollout

Live at landing, with no caller. Within order 2 this unit builds first, then TOOL-dSafePassage-2,
then TOOL-dSafePassage-4: the three write `tools/govkit/upgrade_steps.py`, so they are not disjoint
(BUILD-METHOD M6) and the build run sequences them in that order.

### Files touched (estimate)

- `tools/govkit/upgrade_steps.py`
- `tools/govkit/selftest.py`
- `help/upgrade-steps.md`
- `memory/builds/dSafePassage/build/2026-10-23-build-TOOL-dSafePassage-7-deviation-21.md` (new, at the spec commit)

### Alternatives rejected

- **A subtractive scrub**, the parent's environment minus a list, as `derive_scrub_set`
  (`tools/run-gates/measure_legs.py:402-418`) and `GIT_ENV_LEAKS` do for their own callers. A list
  of what to strip misses every credential nobody named, and `GH_TOKEN` is the fixture's case.
- **`GIT_CONFIG_PARAMETERS`**, which the shape audit's M32 offers beside `GIT_CONFIG_COUNT`. Its
  quoting is internal to git; the clause names `GIT_CONFIG_COUNT`, the documented form.
- **An empty scratch working directory**, as `run_probe_in_empty_dir` runs gov's own probes
  (`tools/govkit/govkit.py:5225-5235`). The step row's argvs run from gov's checkout (§8 F1).
- **A container or OS sandbox.** A new external dependency, which M3's veto 2 refuses.

## 5. Production-readiness checklist

- security: the whole unit. Deny by default: the environment is an allowlist, git's system and
  global config and its helper are unreachable, hooks point at an empty directory and Python runs
  `-I`. What it does not cover is §3's fifth bullet, and S5's `breach` verdict is the probe of it.
- perf / scale: one temporary directory and one spawn per phase; the check doubles that per step.
  No figure is pinned.
- error / empty / loading states: a spawn error is `failed` with `rc` None and its message in
  `tail`; an unresolved token is a refusal before any spawn; an `attended` row spawns nothing.
- observability: each verdict prints with the step id, and a `breach` names the canary that ran.
- risks: a shell step that needs a name outside `STEP_ENV_KEEP` fails under the contract and reads
  `needs-target`, which is the honest reading; the list grows by a reviewed edit with its reason. A
  hook name git adds later is unplanted until `write_target_plants` lists it.
- testing: `fixture isolation` with every plant; the arm joins `tools/govkit/selftest.py` (§7),
  and each new refusal branch is reached there, as `govkit refusal join` requires.
- migration: none; §4 "Migration".
- user docs: `help/upgrade-steps.md`, S8.

## 6. Acceptance criteria

The fixture builds its scratch repositories under `%TEMP%`, never in the worktree. A `-stub` plant
exits 1 by design: it is the criterion's red case, observed.

- **AC1** — When `python3 "tools/govkit/upgrade_steps.py" fixture isolation` runs, it exits 0
  and prints `clean` as `ok`, its report naming only `STEP_ENV_KEEP` names and the contract's own,
  `GIT_CONFIG_COUNT` = 2 with `core.hooksPath` naming an empty directory, `sys.flags.isolated` = 1
  and the scratch gov root as its working directory.
  Red when: the environment starts from a copy of the parent's, or the leading `python` runs without
  `-I`.
- **AC2** — When `python3 "tools/govkit/upgrade_steps.py" fixture isolation --plant hook` runs,
  `clean`'s `git add` meets a planted `post-index-change` and `pre-commit` under the target's own
  `core.hooksPath`, and the run exits 0 printing `hook canary: absent`; `--plant hook-stub`, which
  leaves the `core.hooksPath` pair out of the environment, exits 1 naming the hook's canary.
  Red when: the pair is not set through `GIT_CONFIG_COUNT`, or the target's own `core.hooksPath`
  outranks it.
- **AC3** — When `python3 "tools/govkit/upgrade_steps.py" fixture isolation --plant module` runs,
  with `sitecustomize.py` and `json.py` planted at the target root and `PYTHONPATH` naming the target
  in the parent's environment, it exits 0 printing `module canary: absent`; `--plant module-stub`,
  which passes the parent's environment and omits `-I`, exits 1 naming the `sitecustomize.py`
  canary.
  Red when: `PYTHONPATH` reaches the step, or the argv carries no `-I`.
- **AC4** — When `python3 "tools/govkit/upgrade_steps.py" fixture isolation --plant credential`
  runs, with `GIT_CONFIG_GLOBAL` naming a planted gitconfig whose `credential.helper` writes a
  canary and `GH_TOKEN` set in the parent, a step running `git credential fill` for an https URL
  on the reserved `.invalid` domain exits non-zero without a prompt, the helper's canary is absent,
  `GH_TOKEN` is absent from its report and `git config --get-all credential.helper` prints only the
  empty value; the run exits 0. `--plant credential-stub`, which passes the parent's
  `GIT_CONFIG_GLOBAL` and `GH_TOKEN` through in place of the contract's values, exits 1 naming the
  helper's canary and the token.
  Red when: a parent credential variable or git helper reaches the step.
- **AC5** — When `python3 "tools/govkit/upgrade_steps.py" fixture isolation --plant needs-target`
  runs, `check_needs_target` prints `needs-target` for `reaches` with the remedy
  `needs-target = true` and `attended` for a copy of `reaches` declaring it, whose script's own
  canary is absent, and exits 1; `--plant breach` prints `breach` for `opens`, naming the
  `adopter_only` canary, and exits 1; the base run prints `isolated` for `clean`.
  Red when: a step that fails under the contract reads `isolated`, or an `attended` row spawns.
- **AC6** — When `python3 "tools/govkit/upgrade_steps.py" fixture isolation --plant callers`
  runs over the shipped `upgrade_steps.py` and `govkit.py`, it lists exactly one spawn site of a
  step row's argv, inside `run_step_isolated`, and exits 0; with a planted module text that spawns
  `row["up"]` directly, it exits 1 naming that call's line.
  Red when: a second spawn site of a step argv exists, or the probe finds zero sites and passes.
- **AC7** — When `python3 "tools/govkit/upgrade_steps.py" fixture isolation --plant token` runs,
  a row whose `up` holds `{unknown}` is refused before any spawn, the refusal naming the row's id
  and `{unknown}`, and the run exits 1.
  Red when: the argv spawns with a literal brace token in it.
- **AC8** — When `git grep -n -e "core.hooksPath" -e "GIT_CONFIG_COUNT" -e "needs-target" -- "help/upgrade-steps.md"`
  runs, the page's "What a step can reach" section names all three.
  Red when: the section is missing, or names the contract without the field.

## 7. Gates

`govkit selftest` · `govkit refusal join` · `govkit acceptance matrix` · `govkit selfcheck` · `recall floor` · `recall floor arms` · `memory hygiene` · `encoding posture (text IO names its encoding)` · `lexicon naming predicates` · `spec tokens (a spec's own names resolve)`

New arm: tools/govkit/selftest.py · covers AC1 AC2 AC3 AC4 AC5 AC6 AC7 · the self-test calls `upgrade_steps.py fixture isolation` with every plant and asserts each exit and named line, each failing case staged by its `-stub` plant or its planted module text · none

## 8. Open questions

- **F1 — The declared working directory.** Options: gov's checkout root; a fresh empty directory, as
  `run_probe_in_empty_dir` runs gov's probes; the target. The target is the clause's hazard, and
  veto 1 discards it. RESOLVED (agent, 2026-10-23, delegated): gov's checkout root, on rung 1 — the
  step row of `cl-dClosedLoop-0018` says its up and down argvs run "from gov's checkout", so a
  relative path in a step argv names gov's file; under `-I` the working directory reaches no import
  either way. widens: none · relaxes: none
- **F2 — Where the release-0 half of the needs-target check runs.** The clause checks the field "by
  running each release-0 step under that contract". The release-0 tree is TOOL-dSafePassage-5's, at
  order 5, and the floor step it walks is TOOL-dSafePassage-11's, at order 3. Options: this unit
  builds its own release-0 tree, a second copy of unit 5's generator; this unit ships the check and
  observes it on its own fixture steps, and unit 5's leg runs it over release-0 for every step.
  RESOLVED (agent, 2026-10-23, delegated): the second, on rung 3 — the first is two generators of one
  fixture, which [reuse] refuses. The clause text stands and the build observes it whole; the
  departure in who observes the release-0 half is
  `2026-10-23-build-TOOL-dSafePassage-7-deviation-21.md`. widens: none · relaxes: none
- **F3 — What "marked attended" persists as.** Options: a fourth receipt state `attended`; the
  `install.steps` policy key; the row's own `needs-target = true`, read by `derive_step_mode` so the
  runner returns `attended`, the check's `needs-target` verdict naming that remedy and the walk
  stopping on it (TOOL-dSafePassage-2). S4 of the brief fixes three receipt states, owned by
  TOOL-dSafePassage-3, and `install.steps` is dShippedRelease's (research F6), so veto 1 discards the
  first two. RESOLVED (agent, 2026-10-23, delegated): the row's field, on rung 1. widens: none ·
  relaxes: none
- **F4 — The parent, dGroundRules, is unbuilt.** RESOLVED (agent, 2026-10-23, delegated): this unit
  reads no key of `.governance/policy.toml` and calls no policy reader, so `cl-dClosedLoop-0007` and
  `cl-dClosedLoop-0008` bind nothing here; the build run re-grounds against the landed parent before
  its first pass, and an interface the parent lands that this unit should read is an M2 amendment.
  widens: none · relaxes: none
- **F5 — Names spelled by a sibling.** The row reader and its key spellings are TOOL-dSafePassage-1's,
  written concurrently. RESOLVED (agent, 2026-10-23, delegated): this spec spells them as the brief's
  S1 and S3 fix them; the M2 cross-read before the first code pass binds any difference, fixed in
  whichever document is wrong with a rev bump. widens: none · relaxes: none

## 9. Revision log

- rev-1 · 2026-10-23 · initial draft.

## 10. Reuse audit

The seam extended is govkit's target-side spawn: `resolve_shell_argv` and `run_target_argv`
(`tools/govkit/govkit.py:1200-1230`), whose decode rule the runner keeps, and `resolve_tokens`
(`tools/govkit/govkit.py:1233`), which resolves the argv's tokens. `run_probe_in_empty_dir`
(`tools/govkit/govkit.py:5225-5235`) is the precedent for a spawn kept apart from a target; F1 says
why its empty directory is not taken. `reuse_lookup.py "run a subprocess with a scrubbed
environment, no git hooks and no credential helper"` ranked `git` and `run` by fan-in, `run_git`,
`GIT` (`lib-unattended.sh`) and `build_git_env` (`tools/memory-tree/tree_lib.py:232-243`). None
isolates a spawn: `build_git_env` copies the whole environment and adds one pin, and the two scrubs
the map does not rank, `GIT_ENV_LEAKS` and `derive_scrub_set`, subtract named lists, which §4
"Alternatives rejected" refuses. The hits agree with source; the map ranks no allowlist builder
because none exists, so this one is new.

Recall terms used: `python tools/memory-recall/query.py "how is target-side code kept from running on the node credential when a step or probe runs in an adopter tree" --terms "isolation scrubbed environment hooksPath credential helper sandbox target code needs-target canary plant"`
