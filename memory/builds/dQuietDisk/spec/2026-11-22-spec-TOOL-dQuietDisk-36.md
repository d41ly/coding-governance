# TOOL-dQuietDisk-36 — the bash template cache runs git without the inherited git environment, and the turnstile suite grades the spared live repository and the swept orphan

**Status:** CLOSED · rev-1 · 2026-11-22 · node d · Tier-2 · base 1af73288 · streams tooling · order 8

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-11-20-build-TOOL-dQuietDisk-1-agent-ledger.md](../build/2026-11-20-build-TOOL-dQuietDisk-1-agent-ledger.md) | journal | TOOL-dQuietDisk-1 TOOL-dQuietDisk-2 TOOL-dQuietDisk-3 TOOL-dQuietDisk-4 TOOL-dQuietDisk-5 TOOL-dQuietDisk-6 TOOL-dQuietDisk-7 TOOL-dQuietDisk-8 TOOL-dQuietDisk-9 TOOL-dQuietDisk-10 TOOL-dQuietDisk-11 TOOL-dQuietDisk-12 TOOL-dQuietDisk-13 TOOL-dQuietDisk-14 TOOL-dQuietDisk-15 TOOL-dQuietDisk-16 TOOL-dQuietDisk-17 TOOL-dQuietDisk-18 TOOL-dQuietDisk-19 TOOL-dQuietDisk-26 TOOL-dQuietDisk-28 TOOL-dQuietDisk-37 |
| [2026-11-22-build-TOOL-dQuietDisk-36-1-acceptance-ledger.md](../build/2026-11-22-build-TOOL-dQuietDisk-36-1-acceptance-ledger.md) | journal | — |
| [2026-11-22-build-TOOL-dQuietDisk-36-widen-20.md](../build/2026-11-22-build-TOOL-dQuietDisk-36-widen-20.md) | widen | — |
| [2026-11-22-build-TOOL-dQuietDisk-36-widen-21.md](../build/2026-11-22-build-TOOL-dQuietDisk-36-widen-21.md) | widen | — |
| [2026-11-22-prompt-TOOL-dQuietDisk-36-1-spec-writer.md](../prompts/2026-11-22-prompt-TOOL-dQuietDisk-36-1-spec-writer.md) | journal | — |
| [2026-11-22-prompt-TOOL-dQuietDisk-36-build-brief.md](../prompts/2026-11-22-prompt-TOOL-dQuietDisk-36-build-brief.md) | journal | — |
| [2026-11-22-prompt-TOOL-dQuietDisk-36-spec-task.md](../prompts/2026-11-22-prompt-TOOL-dQuietDisk-36-spec-task.md) | research | — |
| [2026-11-22-review-TOOL-dQuietDisk-36-closing-diff-review-round2.md](../reviews/2026-11-22-review-TOOL-dQuietDisk-36-closing-diff-review-round2.md) | diff-review | — |

<!-- /gen:spec-records -->

## 1. Goal

The closing diff review of `b3f5a2bc3..879413160` confirmed two HIGHs, and this unit is that round's
fold. H1: the bash face of the suite template cache runs git and its builder with the caller's
environment, so an exported `GIT_DIR` commits a fixture tree onto the repository it names. The fix
runs each of the three git-running verbs in a subshell that unsets the twelve names the Python face
drops, so both faces answer alike. H2: the turnstile suite's foreign-repository fixture names a
common dir that does not exist, which TOOL-dQuietDisk-9's orphan rule now sweeps. The fix points
that fixture at a directory that exists, and adds the orphan arms the rule never had.

## 2. Scope (IN)

- **S1** — `remove_git_env_leaks`, a new function in the `template_cache_sh` block, unsets the
  twelve names of `GIT_ENV_LEAKS` in the order `tools/lib/git_env_leaks.py` spells them. It runs no
  process. Observed by AC1 and AC5.
- **S2** — `derive_template_key`, `resolve_template` and `build_template_clone` take subshell
  bodies, `name() ( ... )`, whose first line calls `remove_git_env_leaks`. Every git call in them,
  and the builder subshell `resolve_template` runs, then runs without those names. The caller's
  shell keeps its environment. Each body is otherwise unchanged, so its stdout, stderr, exit codes
  and key bytes are today's. Observed by AC1, AC2 and AC3.
- **S3** — The block changes in `tools/lib/template-cache.sh`, the canonical, and byte-identically
  in its two inline copies, `tools/lib/lib-selftest.sh` and `.githooks/pre-push.test.sh`. The
  existing `template_cache_sh` row of `PARITY_ROWS` grades all three, unchanged. The canonical's
  header gains one sentence naming the scrub and the two verbs outside it. Observed by AC4.
- **S4** — The H1 arms in `tools/lib/lib-selftest.test.sh`: under an exported `GIT_DIR` naming a
  scratch SHA-256 repository with one commit and an `origin` remote, a builder that commits its own
  tree leaves that repository's `HEAD` and remotes unmoved. The clone holds the builder's tree and
  no remote, and the key equals the key derived with `GIT_DIR` unset. The harness body calls the
  three verbs directly, as the existing `tkey` and `trace` bodies do. It exports `GIT_DIR` only
  after the harness is sourced, and unsets it for its own reads of the clone. Three assertions, and
  `FLOOR_ASSERTIONS` moves from 31 to 34 [DERIVED, counted off the new block]. Observed by AC2.
- **S5** — One arm in `tools/lib/resolve-python.test.sh` holds the names `remove_git_env_leaks`
  unsets, in `tools/lib/template-cache.sh`, equal member for member and in order to the tuple in
  `tools/lib/git_env_leaks.py`. It also reds an empty list on either side. Observed by AC5.
- **S6** — The H2 fixture in `tools/run-gates/run-gates.turnstile.test.sh` arm 22. The foreign
  owner names `$tmp/other22/.git`, which the arm creates before the first bar starts, under pid
  999998. Its survival arm keeps its text, and the arm adds no assertion for it. Observed by AC6
  and AC7.
- **S7** — The H2 orphan arms in the same arm 22. Beside `gate-work.deadmine`, after the first bar
  has swept, the arm plants two more dead owners. `gate-work.orphan` names `$tmp/gone22/.git`, an
  absolute common dir that is never created, under pid 999997, and the second bar must sweep it and
  announce it. `gate-work.relative` names `relative/.git` under pid 999996, and it must survive. The
  health-line arm then expects exactly two `scratch-swept` lines, naming pids 999999 and 999997. The
  never-established branch gains two `skipped` lines, and `FLOOR_ASSERTIONS` moves from 145 to 147
  [DERIVED, counted off arm 22's two new assertions]. Observed by AC6 and AC7.
- **S8** — The shell-line ledger. Each of the six shell files this unit edits has a row in
  `memory/project/shell-role.txt`. The rows grow only through
  `python tools/memory-tree/ratchet.py widen shell-role`, which the main loop runs after the pass,
  never by hand. Observed by AC8.
- **S9** — The adopters. The push-main kit ships `.githooks/pre-push.test.sh`, and the run-gates kit
  ships `tools/run-gates/run-gates.turnstile.test.sh` as project-owned. Each kit's version moves at
  the mint, never by hand, and reaches nc, ic and swydee only through `govkit update`. Observed by
  AC9.

## 3. Non-goals (OUT)

- No change to `scan_dead_work` or its orphan rule. The review judged the rule right and the fixture
  wrong (finding 5, judged SOUND), so `tools/lib/owned-scratch.sh` and its runner copies stay as
  they are.
- No scrub in `read_template_mode`. It runs no git itself, and the `policy.py get` child it starts
  drops `GIT_ENV_LEAKS` for each of its own git calls (`tools/policy/policy.py#run_git`,
  `tools/policy/policy.py#read_blob_at`). `resolve_template_root` runs no process.
- No change to the Python face. Its own git calls already drop the names
  (`tools/lib/template_cache.py@63ffe62be6ee:130`). Its `build` callable runs in the caller's
  process, and its one builder, `tools/govkit/fixture_target.py#run_git`, drops the eight location
  names itself.
- No lint over every bash face whose Python twin drops `GIT_ENV_LEAKS`, and no must-run row for a
  change under `scan_dead_work`. Those are the review's two left-shift gates, each a separate
  mechanism, promoted at the loop's exit with the round's MEDIUM and LOW items.
- No change to the hooks' own eight-name scrub (`.githooks/pre-commit`, `.githooks/pre-push`).
- No kit version bump by hand. `govkit.py mint` writes every owed bump at the lander.

### Edges

- **consumes-from** external — the `template_cache_sh` block, its parity row and its arms as
  TOOL-dQuietDisk-7 built them, and the orphan rule as TOOL-dQuietDisk-9 S9 built it, both landed at
  the base. Both specs are CLOSED and frozen, so they carry no edge back, and this unit changes
  their code and arms in place
- **hands-off** external — the round's MEDIUM and LOW items and both left-shift gates, which the
  loop promotes at its exit

## 4. Design

### Where the code was read

Every citation is at `1af73288`, this run's `HEAD`. The review cites the same blobs:
`tools/lib/template-cache.sh@14b641eb0144`, `tools/lib/lib-selftest.sh@192087e22c69`,
`tools/run-gates/run-gates.turnstile.test.sh@01d29320c246` and
`tools/run-gates/run-gates.sh@d35d666e1720`.

### H1, what leaks today

`resolve_template` runs the builder as `( cd "$_tc_s/repo" && "$@" )`
(`tools/lib/template-cache.sh@14b641eb0144:53`). It then runs `git -C <stage>/repo` for `init`,
`add -A`, `commit`, `rev-parse`, `diff --cached` and `config --local --list`
(`tools/lib/template-cache.sh@14b641eb0144:56-63`). `build_template_clone` runs `clone` and
`git -C <dest> remote remove origin` (`tools/lib/template-cache.sh@14b641eb0144:87-88`).
`derive_template_key` runs two `git hash-object` processes
(`tools/lib/template-cache.sh@14b641eb0144:42-43`). All of them inherit the caller's environment.
The Python face drops `GIT_ENV_LEAKS` for every `run_git`
(`tools/lib/template_cache.py@63ffe62be6ee:130`).

Measured on 2026-11-22 in a scratch directory, with git 2.54.0.windows.1 and bash 5.3.9 [PINNED].
The probe exported `GIT_DIR` at a scratch repository with one commit and an `origin` remote. It
ran a builder that runs `git init` and commits its own tree, then `resolve_template` and
`build_template_clone`, against the base block and against variants of the S2 block.

| Block | Scratch `HEAD` | Scratch `origin` | Key | Clone |
|---|---|---|---|---|
| base | moved: commits `self` and `base` | kept | 64 hex under a SHA-256 `GIT_DIR` | exit 128, the template has no `.git` |
| S2 | unmoved | kept | equals the unexported key, 40 hex | builder's file, no remote |
| S2 less the call in `derive_template_key` | unmoved | kept | 64 hex | builder's file |
| S2 less the call in `resolve_template` | moved | kept | equal | exit 128 |
| S2 less the call in `build_template_clone` | unmoved | removed | equal | builder's file, `origin` removed from the scratch |

Each verb's scrub is therefore seen by one observation, and the S4 arms and AC1 hold all three. A
`GIT_DIR` naming no directory changes no key: `git hash-object` answers the same there, measured in
the same probe. A SHA-256 repository is what makes the key's leak visible.

### The scrub

```bash
remove_git_env_leaks() { # unsets, in the calling subshell, the names GIT_ENV_LEAKS drops
  unset GIT_DIR GIT_WORK_TREE GIT_INDEX_FILE GIT_OBJECT_DIRECTORY GIT_ALTERNATE_OBJECT_DIRECTORIES \
    GIT_COMMON_DIR GIT_NAMESPACE GIT_PREFIX GIT_LITERAL_PATHSPECS GIT_GLOB_PATHSPECS \
    GIT_NOGLOB_PATHSPECS GIT_ICASE_PATHSPECS
}
derive_template_key() ( # <builder> [<input file>...] -> ...   (comment unchanged)
  remove_git_env_leaks
  ...                                   # today's body, unchanged
)
```

`resolve_template` and `build_template_clone` take the same two-line change. A subshell body makes
the scrub hold for every line of the verb, so a git call added to a verb later is scrubbed with no
edit. It also holds for the builder, which runs inside `resolve_template`'s body. `return`, `local`,
`local -` with `set -o pipefail`, and `$BASHPID` all keep their meaning in a subshell body. That was
measured in the same probe, and `tools/run-gates/run-gates.gov.test.sh#check_cr_reached` already
uses the form. Every caller reads `resolve_template` and `derive_template_key` through their stdout,
and none of the three verbs sets a variable its caller reads, so no caller moves.

The bash shell's own scoping cannot do this without a subshell. A function-local `local GIT_DIR`,
and `local GIT_DIR=v; export -n GIT_DIR`, both still hand the exported value to a child process.
That was measured on 2026-11-22 with bash 5.3.9 under its default `localvar_inherit` and
`localvar_unset` [PINNED].

### What it costs

One bash fork per verb call, and no git process. The probe counted `GIT_TRACE2_EVENT` files for
one key, one template build and eight clones, at 30 for the base block and 30 for the S2 block
[PINNED, measured 2026-11-22]. The keys are the same bytes before and after, because the key reads
the builder's `declare -f` and never the verb's own definition.

### The two lists of names

The Python list is canonical in `tools/lib/git_env_leaks.py@819a23826c2f:13-26`, which
`template_cache.py` carries inline under the `git_env_leaks_py` row. The bash list is new, and no
bash canonical of the twelve names exists. `git grep` at the base finds only the hooks' eight
location names (`.githooks/pre-commit`, `.githooks/pre-push`) and four pathspec names in
`tools/check-playbook-parity.sh`. A list in two languages with nothing comparing them is two facts,
so S5's arm compares them. It reads the canonical `git_env_leaks_py` block with the parity table's
`blk` (`tools/lib/resolve-python.test.sh#blk`), takes each quoted `GIT_` name, and compares them in
order with the `GIT_` names in `remove_git_env_leaks`'s body in `tools/lib/template-cache.sh`. The
parity row then carries the bash list to both inline copies.

### H2, the fixture and the four owners

At the base, arm 22 plants `999999\t/nowhere/else/.git\t0` before the first bar starts
(`tools/run-gates/run-gates.turnstile.test.sh@01d29320c246:1184-1185`). `scan_dead_work` now passes
over another repository's owner only where the common dir is relative or names a directory
(`tools/run-gates/run-gates.sh@d35d666e1720:2446-2454`). So the first bar sweeps that owner, the
foreign arm at line 1233 fails, and the health-line arm at lines 1226-1229 counts two lines.

| Owner dir | Pid | Common dir | Planted | Expected |
|---|---|---|---|---|
| `gate-work.foreign` | 999998 | `$tmp/other22/.git`, created by the arm | before the first bar | survives both bars |
| `gate-work.deadmine` | 999999 | this repository's, read from the live owner | after the first bar swept | swept by the second bar, announced |
| `gate-work.orphan` | 999997 | `$tmp/gone22/.git`, never created | after the first bar swept | swept by the second bar, announced |
| `gate-work.relative` | 999996 | `relative/.git` | after the first bar swept | survives |

Distinct pids let the announcement lines and the health lines name which owners were swept. The
two new arms are an orphan arm, which asserts `gate-work.orphan` is gone and the second bar's
output names pid 999997, and a relative arm, which asserts `gate-work.relative/owner` exists and
no output names pid 999996. The health-line arm asserts exactly two `scratch-swept` lines, whose
fourth fields, sorted, are `dead bar pid 999997` and `dead bar pid 999999`. The arms read the same
health log the base arm reads, `$R22/.git/health.log`.

The predicate was checked against the four owners on 2026-11-22. The `owned_work_sh` block of
`tools/lib/owned-scratch.sh@f487e07d735e` was sourced with `ts_alive` and `add_health_event`
stubbed, and it swept this repository's owner and the orphan and kept the other two. The base
fixture's owner naming /nowhere/else/.git was swept, which is H2 reproduced. AC6 repeats this.

`$tmp` is the suite's `mktemp -d` (`tools/run-gates/run-gates.turnstile.test.sh@01d29320c246:286`),
an absolute MSYS path, so the runner's `case "$common" in /*` reads both planted paths as
absolute. A Windows drive spelling would match the rule's `[A-Za-z]:[/\\]*` arm too.

`[class]`: the fixture population is every tracked suite that plants a `gate-work.*/owner`.
`git grep` at the base finds arm 22's two plants and one `owner` file in
`tools/lib/lib-selftest.test.sh` that names no common dir, which `scan_dead_work` never reads there.
So arm 22 is the whole population.

### Wall-clock ceilings

No ceiling moves. S4 adds one template build and one clone to a suite whose ceiling is
370 s [DERIVED from `tools/gate-legs.json@db79c2db62ea:3816`]. S7 adds no bar run to a suite whose
ceiling is 8210 s [DERIVED from `tools/gate-legs.json`].

### Inventory

| Minted identifier | Kind | Naming cell | Graded by |
|---|---|---|---|
| `remove_git_env_leaks` | bash function | `sh.function`, lexicon `--suggest` OK | the S4 arms through each verb, and the S5 arm |
| `gate-work.orphan`, `gate-work.relative` | fixture directory names | none: fixture names are not declared | arm 22 |

`python tools/lexicon/lexicon.py --suggest remove_git_env_leaks --as sh.function` prints `OK`, run
2026-11-22.

### Files touched (estimate)

`tools/lib/template-cache.sh` · `tools/lib/lib-selftest.sh` · `.githooks/pre-push.test.sh` ·
`tools/lib/lib-selftest.test.sh` · `tools/lib/resolve-python.test.sh` ·
`tools/run-gates/run-gates.turnstile.test.sh` · `memory/project/shell-role.txt` ·
`memory/map/generated/symbols.json` ·
`memory/builds/dQuietDisk/build/<date>-build-TOOL-dQuietDisk-36-widen-<n>.md`

The six shell files each have a row in `memory/project/shell-role.txt`, which the widen moves. The
widen record's number is one past the highest in the build folder, which holds widen 19 [DERIVED,
listed 2026-11-22], so `20` unless another unit widens first. `remove_git_env_leaks` joins the
codebase map's symbol index in each of the three files that carry the block. That index, and any
other generated map file it moves, is re-rendered by `gen_map.py --write`, never by hand. No path
here is on the kickoff manifest's `watch:` line.

### Alternatives rejected

| Alternative | Why it loses |
|---|---|
| Wrap each git call in its own `( unset ...; git ... )` | Seven call sites and the builder, each a fork, and a git call added later is unscrubbed unless its author remembers. |
| `env -u GIT_DIR ...` per call | One `env` process per git call, and the builder is a shell function `env` cannot run. |
| Function-local `local GIT_DIR` | Measured not to hide an exported value from a child (section 4). |
| Keep the foreign owner on a missing path and change the rule | The rule is the review's SOUND design, and a missing absolute common dir is the orphan case the rule exists to sweep. |
| A separate ambient and a third bar for the orphan arms | One more fixture bar run, where planting beside `gate-work.deadmine` lets the second bar grade all four owners. |

## 5. Production-readiness checklist

- security: closes a path where a suite run under an exported `GIT_DIR` commits into, and removes a
  remote from, the repository that variable names. Deny by default: every git-running verb of the
  face drops the names, and no caller opts in.
- perf / scale: no git process added, measured at 30 and 30 [PINNED]. One bash fork per verb call.
- error / empty / loading states: unchanged. Each verb's exit codes and refusal lines are today's.
- observability: unchanged. The `template: <key8> built|reused` lines are today's.
- risks: a caller that meant its `GIT_DIR` to reach the builder. No caller in the tree does: every
  builder at the base works in the stage's own directory. The gotcha class
  `inherited-git-dir-pins-the-work-tree-to-the-cwd` is the review's class for H1, and S2 is its
  class-level cure.
- testing: the probes of section 6, and the new arms in three suites, observed by the main loop.
- migration: N/A — no stored data. A template built before the change has the same key and is
  reused.
- user docs: N/A — no knob, flag or output changes.

## 6. Acceptance criteria

- **AC1** — When a probe makes a SHA-256 repository with `git init --object-format=sha256`, gives it
  one commit and an `origin` remote, exports `GIT_DIR` at its git dir, sources
  `tools/lib/template-cache.sh`, and runs `derive_template_key`, `resolve_template` and
  `build_template_clone` for a builder that runs `git init` and commits its own tree, five things
  hold. The key equals the key derived with `GIT_DIR` unset, 40 hex. The scratch `HEAD` is
  unmoved. The scratch `git remote` still prints `origin`. Read with `GIT_DIR` unset, the clone
  prints no remote and holds the builder's file. The probe shell's `GIT_DIR` is still the value it
  exported.
  Red when: any one verb loses its `remove_git_env_leaks` line, each red seen on its own observation
  as section 4's table states. The pass observes each of the three reds on a scratch copy, then
  green.
  figure: 40 and 64 hex DERIVED from the object format; the table PINNED, measured 2026-11-22.
  fixture: a git that creates SHA-256 repositories, 2.29 or later; this host's is 2.54.0 [PINNED].
- **AC2** — When the main loop runs the selftest harness suite, its three new lines print `ok`, the
  suite passes at `FLOOR_ASSERTIONS=34`, and every base line prints as before. With `remove_git_env_leaks` removed from `resolve_template` in the `lib-selftest.sh`
  copy, the `HEAD` line prints `nope`.
  Red when: a scrub is missing from a verb, or an existing template arm moves.
  permission: a role pass runs no suite. This is the `New arm:` line's RED and GREEN observation,
  owed to the main loop. The pass's proxy is AC1.
- **AC3** — When a probe sets `GIT_TRACE2_EVENT` to an empty directory and runs one
  `derive_template_key`, one `resolve_template` and eight `build_template_clone` calls, the
  directory holds 30 files [PINNED, measured 2026-11-22] for the base block and the same count for
  the S2 block. `derive_template_key` for one builder, with no input and with one input file, prints
  the same keys under both blocks.
  Red when: the change adds a git process, or a key moves.
  figure: 30 PINNED for the base block; the S2 count DERIVED at observation and equal to it.
- **AC4** — When the `template_cache_sh` block is extracted with the parity table's own `blk` awk
  from `tools/lib/template-cache.sh`, `tools/lib/lib-selftest.sh` and the push-main kit's pre-push
  suite, the three compare equal, and each holds `remove_git_env_leaks` and three `name() (` openers
  for the three verbs.
  Red when: a copy drifts by one byte, which the `template_cache_sh` row then reports.
- **AC5** — When a probe extracts the quoted `GIT_` names from the `git_env_leaks_py` block of
  `tools/lib/git_env_leaks.py` and the `GIT_` names from `remove_git_env_leaks` in
  `tools/lib/template-cache.sh`, both lists hold twelve names in the same order. With a thirteenth
  name appended to a scratch copy of either side, the lists differ. When the main loop runs the
  python resolver suite, the new arm prints nothing, and with a name dropped from the bash list it
  prints one `FAIL` naming both files.
  Red when: the comparison is skipped, or an empty list passes.
  figure: twelve DERIVED from `tools/lib/git_env_leaks.py`.
  permission: the suite half is the main loop's, as AC2.
- **AC6** — When a probe sources the `owned_work_sh` block of `tools/lib/owned-scratch.sh` with
  `ts_alive` and `add_health_event` stubbed, plants section 4's four owners plus one naming the base
  fixture's missing path, each under a dead pid, and calls `scan_dead_work`, it removes exactly the
  owner naming this repository, `gate-work.orphan` and the base fixture's owner. It keeps
  `gate-work.foreign` and `gate-work.relative`, and appends one health line per removal.
  Red when: the fixture design does not match the rule, for instance the foreign owner's common dir
  is not created.
- **AC7** — When the main loop runs the turnstile suite at the base, arm 22's foreign line and its
  health line print `FAIL`, which is H2. At this unit's commit, every arm 22 line prints `ok`, the
  orphan and relative lines included, and the suite passes at `FLOOR_ASSERTIONS=147`. With the
  orphan branch of `scan_dead_work` replaced by today's `continue` in the fixture's copy of the
  runner, the orphan line prints `FAIL`. With the relative `case` arm dropped there, the relative
  line prints `FAIL`.
  Red when: the foreign fixture still names a missing directory, or an orphan arm cannot fail.
  permission: a role pass runs no suite. The RED at the base and the GREEN at the commit are the
  main loop's.
  cost: one run of the suite each way, minutes.
- **AC8** — When `grep -n -E` for the six shell files runs over `memory/project/shell-role.txt`
  after the widen, it prints six rows, each ending `widened:<stem>` for one record stem. That stem
  names a file under `memory/builds/dQuietDisk/build/` whose Keys field lists exactly those six
  paths and whose Caused-by is `TOOL-dQuietDisk-36`. Then
  `git diff --stat -- memory/project/shell-role.txt` shows those rows and no other.
  Red when: a row is edited by hand, or a row for a file this unit does not touch moves.
- **AC9** — When `python tools/govkit/govkit.py shipped` runs, it lists the pre-push suite under
  `push-main` and the turnstile suite under `run-gates`. When
  `python tools/govkit/govkit.py check --target C:/projects/incms/main`, and the same with
  `C:/projects/nicocares/main`, run read-only from gov before and after the unit, each prints the
  same bytes and exit code.
  Red when: a copy is not claimed by its kit, or a check reads differently.
  permission: read-only against the adopters' main checkouts, never their `gov-upgrade` worktrees.
  fixture: the adopters reach the change only after a minted version and their own `govkit update`;
  `tools/govkit/fixtures/release-0/deploy.toml` names `push-main` for an adopter-side install.

This unit moves no verdict a passing suite gave at the base. The turnstile suite's arm 22 goes from
red to green, and every other arm keeps its line.

## 7. Gates

`selftest harness self-test` · `extract-arms self-test` · `python resolver (behaviour + inline parity + idiom ban)` · `run-gates turnstile` · `pre-push self-test` · `pre-push bar self-test` · `pre-push run-log line` · `kit epoch (shipped bytes move, the version moves)` · `portability (shell lines only shrink)` · `ratchet (never gains)` · `codebase-map coverage + freshness` · `lexicon naming predicates` · `recall floor` · `recall floor arms` · `line length` · `memory hygiene` · `spec tokens (a spec's own names resolve)`

New arm: tools/lib/lib-selftest.test.sh · covers AC2 · the three H1 lines under an exported GIT_DIR naming a scratch SHA-256 repository; its failing case is staged by removing remove_git_env_leaks from one verb in the lib-selftest.sh copy · FLOOR_ASSERTIONS 31 to 34
New arm: tools/lib/resolve-python.test.sh · covers AC5 · the bash scrub's names against git_env_leaks.py's tuple; its failing case is staged by dropping one name from the bash list · none
New arm: tools/run-gates/run-gates.turnstile.test.sh · covers AC7 · arm 22's orphan and relative lines and its two-line health count; the failing cases are staged by restoring today's continue for another repository's owner, or dropping the relative case arm, in the fixture's runner copy · FLOOR_ASSERTIONS 145 to 147

The bar runs once at the close. The new arms' RED and GREEN observation is the main loop's. No
criterion has the pass run a suite, a gate leg or the bar.

## 8. Open questions

none

## 9. Revision log

- rev-1 · 2026-11-22 · initial draft, under `2026-11-22-prompt-TOOL-dQuietDisk-36-spec-task`, from
  the round-1 closing review's H1 and H2. Order 8: it follows TOOL-dQuietDisk-19 at order 7, and its
  write set meets no live unit.

## 10. Reuse audit

The seam extended is the `template_cache_sh` block itself, with its existing parity row in
`tools/lib/resolve-python.test.sh`, and arm 22 of the turnstile suite. No existing bash seam drops
the git environment. `python tools/codebase-map/reuse_lookup.py "unset the inherited git environment variables GIT_DIR GIT_WORK_TREE before running git in a bash helper"`
ranked `run_git`, `run_fixture_git`, `read_git` and `GIT`. The first three are Python runners, and
`GIT` in `tools/unattended/lib-unattended.sh` pins two `-c` options and drops nothing. A `git grep`
for the pathspec names in shell files found one partial `unset` in
`tools/check-playbook-parity.sh`, and the hooks unset eight names inline. So no existing seam fits
a bash scrub of the twelve names, and the face gains one function that the S5 arm holds to the
Python canonical, `tools/lib/git_env_leaks.py`.

Owning chain build: dWitnessedBar (Test: gate health), whose suites these are. No dWitnessedBar spec
defines the template cache or the dead-scratch sweep.

Recall terms used: template cache bash face GIT_DIR GIT_ENV_LEAKS scrub subshell builder resolve_template build_template_clone orphan sweep scan_dead_work turnstile foreign owner
