# TOOL-aTrimmedWait-10 — close-bar repair: the commit-render switch becomes the policy key `memory.staged-render`, and the fork sites the shell-hygiene leg names are converted

**Status:** INPROGRESS · rev-2 · 2026-11-15 · node a · Tier-2 · base 846d51d3 · streams tooling · order 9

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-11-15-prompt-TOOL-aTrimmedWait-10-1-spec-writer.md](../prompts/2026-11-15-prompt-TOOL-aTrimmedWait-10-1-spec-writer.md) | journal | — |
| [2026-11-15-prompt-TOOL-aTrimmedWait-10-2-spec-writer.md](../prompts/2026-11-15-prompt-TOOL-aTrimmedWait-10-2-spec-writer.md) | journal | — |
| [2026-11-15-prompt-TOOL-aTrimmedWait-10-promotion.md](../prompts/2026-11-15-prompt-TOOL-aTrimmedWait-10-promotion.md) | research | — |
| [2026-11-15-prompt-TOOL-aTrimmedWait-10-revision.md](../prompts/2026-11-15-prompt-TOOL-aTrimmedWait-10-revision.md) | research | — |

<!-- /gen:spec-records -->

## 1. Goal

The close bar at `078eb5c58` read `policy check` and `shell hygiene (a fork spent on builtin work)`
RED, each on this build's own change. This unit turns both legs green and moves no other verdict.
The commit-render switch unit 3 added to `.memory-tree.conf` moves to one policy catalogue key,
which the owner ruled on 2026-11-15. The seven fork sites this build added are each converted to
their no-fork form.

## 2. Scope (IN)

- **S1** — A catalogue row `memory.staged-render` in `tools/policy/catalogue.toml`: allowed `on`
  and `off`, default `off`, a `summary`, a `usage` and owner `aTrimmedWait`. It sits after the
  `pass.fast-legs` row, under its own comment naming this unit. Observed by AC4.
- **S2** — `check_staged_write` in `tools/memory-tree/gen_build_index.py` reads the switch through
  `read_policy_value("memory.staged-render", root)`, imported from `tree_lib` in the module's
  existing import block. `on` goes on to the index check. Every other answer declines, as §4 "The
  read" tabulates. Observed by AC1, AC2, AC3.
- **S3** — `STAGED_RENDER` is retired: its line and comment leave `.memory-tree.conf` and
  `tools/memory-tree/.memory-tree.conf.example`, and every other spelling outside `memory/` is
  rewritten to name the key, but one. The one kept spelling is the fixture line of
  `test_staged_write` in `tools/memory-tree/gen_build_index.py` that plants `STAGED_RENDER="1"` in
  the AC2 off arm's conf (§4 "The fixtures of `test_staged_write`"): the arm proves a stale conf line
  no longer turns the render on, so it spells the line it plants. Observed by AC5.
  **Readers:**
  by name: `tools/memory-tree/gen_build_index.py` (`check_staged_write` and the arms of
  `test_staged_write`), `.githooks/pre-commit` (the comment above the hygiene branch),
  `.memory-tree.conf`, `tools/memory-tree/.memory-tree.conf.example`,
  `tools/memory-tree/README.md`, `help/commit-render.md` and `help/README.md`, by a git grep
  outside `memory/` at the close bar's commit.
  by value: `tools/policy/policy.py#derive_legacy_homes`, which yields one legacy-home row for
  every key a tracked root `.*.conf` assigns, and `check_staged_write`, which compares the value
  with `1`.
- **S4** — `test_staged_write` arms its fixtures through a committed `.governance/policy.toml` read
  at the fixture's own branch, and gains arms for the off, refused and no-kit answers. Observed by
  AC1, AC2, AC3.
- **S5** — The user docs name the key: `help/commit-render.md` with the docs leg's usage anchor,
  `help/README.md`, the consumer list of `help/policy.md`, the rendered `help/reference/policy.md`
  and the `gen_build_index.py` row of `tools/memory-tree/README.md`. Observed by AC6.
- **S6** — `.governance/policy.json` is re-rendered by `policy.py mirror --write` and committed
  alone, after the catalogue commit. Observed by AC7.
- **S7** — The seven fork sites of §4 "The fork sites" are converted, so every count falls back to
  its row in `memory/project/spawn-idiom-sites.txt`, and no row is added or raised. Observed by AC8,
  AC9, AC10, AC11.
- **S8** — This repository's `.governance/policy.toml` sets the key `on`, in the owner's terminal
  commit, followed by a second mirror commit. Observed by AC12.

## 3. Non-goals (OUT)

- No edit to `tools/policy/legacy-homes.txt`, `tools/policy/unsummarised-keys.txt`,
  `memory/project/spawn-idiom-sites.txt` or any waiver or registry row.
- No other key of `.memory-tree.conf` moves.
- No verdict change beyond the two legs. The hook's flow, every decline but the switch's, and every
  arm of the five shell files keep their verdicts.
- No edit to the spec of `TOOL-aTrimmedWait-3`. It is CLOSED and frozen; its AC7 grep reads the
  retired key, and this unit is the correction on top.
- No conf fallback. A tree that still carries `STAGED_RENDER` is not read for it.
- No lexicon surface for a policy key. §4 "Inventory" records the lexicon's answer.
- No conversion of a fork site this build did not add. The `pure-fn-subst`, `printf-subst` and
  `var-pipe` drains the registry's reasons name are their own follow-up units.
- No kit version move. The build README moves kit versions once, after the last code move.

### Edges

- **consumes-from** external — the owner's terminal commit of `.governance/policy.toml` (S8). The
  policy guard refuses an agent's commit to that path: `tools/policy/guarded-paths.txt@16afba2735ed:5`
  lists it, and the hook admits it only on `[ -t 2 ]` (`.githooks/pre-commit@14e9c510dcd6:208`).
  Every other scope item builds without it.

## 4. Design

### Evidence

- The leg's red is `arm_legacy_homes` (`tools/policy/check_policy.py@4b35ad98559a:412`). It calls
  `check_legacy_homes` (`tools/policy/policy.py@dabd5085dfdc:1311`), whose derivation reads every
  key a tracked root `.*.conf` assigns (`:1271-1273`). A pair the compare base's list lacks is
  reported as a new legacy home (`:1343-1346`). `python tools/policy/policy.py lists --check` prints
  both findings for `.memory-tree.conf STAGED_RENDER` and exits 1, observed 2026-11-15.
- `tree_lib.read_policy_value` (`tools/memory-tree/tree_lib.py@54a65cd4d0c4:65-80`) runs the policy
  kit's `policy.py get` with every `GIT_*` variable dropped. It raises LookupError where no policy
  kit resolves and ValueError carrying the reader's last line where the reader refuses.
  `read_lane_state` (`tools/memory-tree/routed_commits.py@5e29003bb174:281-296`) is its shape for an
  on/off key.
- `policy.py get` reads the catalogue from the kit's own file and the policy file at the landed
  revision (`tools/policy/policy.py@dabd5085dfdc:768-781`). The landed revision is
  `refs/remotes/<remote>/<branch>`, or `refs/heads/<branch>` with no remote, the branch
  `GOV_DEFAULT_BRANCH` else the remote's HEAD else `main` (`:478-506`). A ref that names no commit is
  a Refusal, exit 2 (`:1392-1420`).
- The switch has one reader, `check_staged_write`
  (`tools/memory-tree/gen_build_index.py@1eda60a27f2e:988-999`). The hook names it only in a comment
  (`.githooks/pre-commit@14e9c510dcd6:233`).
- `_fixture` runs `git init` with no branch name
  (`tools/memory-tree/gen_build_index.py@1eda60a27f2e:4572`), so its branch is the machine's
  `init.defaultBranch`, `master` on node a.
- A catalogue row with no `summary` or `usage` must sit on the shrink-only `unsummarised-keys.txt`
  (`tools/policy/catalogue.toml@9ce5a224c3e6:9-10`). A shaped member of the docs leg must be
  anchored on one page or sit on the shrink-only `memory/project/docs-undocumented.txt`
  (`tools/govkit/docs_leg.py@259afa60a559:19-23`). `help/reference/policy.md` renders one section per
  catalogue row and links the page that anchors it
  (`tools/playbook/render_playbook.py@b81935feb7dd:3629-3660`).
- Reader coverage grades a key whose owner build has landed, by a call passing the key as a string
  literal (`tools/policy/check_policy.py#check_reader_coverage`, through `scan_reader_keys`).
  S2's call is that literal.

### The key

| Field | Value |
|---|---|
| `name` | `memory.staged-render` |
| `allowed` | `["on", "off"]` |
| `default` | `"off"` |
| `summary` | `Whether the pre-commit hook renders and stages the build index when check 9 refuses a commit: on, or off, the commit then refused as before.` |
| `usage` | `memory.staged-render = "on"` |
| `owner` | `aTrimmedWait` |

The name is derived, not chosen: the `memory.` segment is the family of the memory-tree kit's other
keys, and `staged-render` is the retired conf key's words in the catalogue's lower-case hyphenated
spelling. `on` and `off` are the pair `bar.inline-red-fixes` and `pass.fast-legs` carry. The row
needs no `direction`: it is no loop bound and no deadline. The comment above it reads:
`# TOOL-aTrimmedWait-10: the commit-render switch, default off. It is no row of the design's [policies] table, so the header's order does not place it.`

### The read

`check_staged_write`'s first lines become one `try` over the reader. Each answer and its decline
line, printed after `build-index: render NOT staged — `:

| The reader answers | `check_staged_write` returns |
|---|---|
| `on` | goes on to the index check, as before |
| any other value | `memory.staged-render reads <value>, so the hook does not render` |
| LookupError | `no policy kit resolves beside this kit, so memory.staged-render reads off` |
| ValueError | the reader's own line, `memory.staged-render did not read: <line>` |

A decline exits 1 and writes nothing, so the hook refuses as before. The unit-3 Problem on a value
other than blank or `1` is gone with the key: the catalogue's `allowed` refuses such a value in the
policy file, and `policy-file.on-invalid` decides what the reader then answers.

The switch is still read first, before the index and the unstaged check. It now costs one Python
spawn, 0.44 s on node a for a `policy.py get` (PINNED 2026-11-15), paid only after check 9 refused.

### The fixtures of `test_staged_write`

Both fixtures, `t` and `d`, drop `STAGED_RENDER="1"` from their conf text and write
`.governance/policy.toml` as `[memory]` then `staged-render = "on"` before the `rendered` commit.
`run_write_staged` adds `GOV_DEFAULT_BRANCH`, the tree's `git symbolic-ref --short HEAD`, and
`GOV_REMOTE=""` to its environment, so the landed revision is the fixture's own branch on any
machine; an `extra` entry overrides either. The unit-3 arms keep their names and verdicts, but the
two arms of the loop over `STAGED_RENDER` values, whose names spell the retired key. Those two
change their staged condition and are renamed to name the key, and one arm is added:

| Arm | Staged by | Wants |
|---|---|---|
| AC2 off (was the blank key), named `TOOL-aTrimmedWait-10 AC2 — memory.staged-render reads off at the landed revision, a stale conf line moves nothing, and no status changes` | a branch `policy-absent` whose tip deletes the policy file, read through `GOV_DEFAULT_BRANCH`, with `STAGED_RENDER="1"` in the conf | exit 1, `memory.staged-render reads off`, porcelain unchanged |
| AC2 refused (was the value `yes`), named `TOOL-aTrimmedWait-10 AC3 — memory.staged-render at a missing branch does not read, and no status changes` | `GOV_DEFAULT_BRANCH=no-such-branch` | exit 1, `memory.staged-render did not read`, porcelain unchanged |
| AC3 no kit | `check_staged_write(t, conf)` in-process, `read_policy_value` stubbed in module globals to raise LookupError, restored in a `finally` | `(False, <the no-kit line>)` |

The AC2 off arm's conf text is the fixture's conf plus the one line `STAGED_RENDER="1"`, written by
one source line, the kept spelling of S3. The no-kit arm stubs the reader, as `routed_commits.py`'s selftest stubs it
(`tools/memory-tree/routed_commits.py@5e29003bb174:946-966`). It proves the LookupError branch of
`check_staged_write`, not `resolve_kit_dir`'s miss, which the kit's resolver tests own.

### The fork sites

Each site is a line this build added, by `git diff 846d51d39 078eb5c58` over the five files. Each
conversion is the form the class's label in `tools/gate-lint/sh_hygiene.py@448d62cbd57b:615-627`
names.

| File and line at `078eb5c58` | Class, row | Today | Becomes |
|---|---|---|---|
| `.githooks/pre-commit@14e9c510dcd6:239` | `var-pipe`, 4 | `printf '%s\n' "$hy_out" \| grep -q '^HYGIENE check 9 FAILED'` | `[[ $'\n'$hy_out == *$'\n''HYGIENE check 9 FAILED'* ]]` |
| `.githooks/pre-commit.test.sh@6afa5a00ae82:325` | `cat-file`, none | `$(cat .hy-runs)` | `$(<.hy-runs)` |
| `tools/memory-tree/check-memory-hygiene.sh@e3771865393b:3772` | `var-pipe`, 25 | `$(printf '%s\n' "$c12_sel" \| grep -c $'^P\t')` | `$_c12_p`, below |
| `tools/roles/adopt-roles.test.sh@98423a10fd38:1053` and `:1079` | `pure-fn-subst`, none | `"$(check_cold23 && … && echo 1 \|\| echo 0)"` | `_w23=0; check_cold23 && … && _w23=1`, then `"$_w23"` |
| `tools/workflows/unattended-build.test.sh@bd21cb92788c:3759` and `:3766` | `printf-subst`, 74 | `"$(printf "$TW1_SPEC" <arg>)"` | `printf -v tw1_in "$TW1_SPEC" <arg>`, then `"$tw1_in"` |

The hygiene count, two lines above the `echo`, counts the `P` rows by length difference:

```bash
_c12_t=$'\n'$c12_sel; _c12_u=${_c12_t//$'\n'P$'\t'/}; _c12_p=$(( (${#_c12_t} - ${#_c12_u}) / 3 ))
```

Each `P` row opens with the three characters newline, `P` and tab, after the prefixed newline, and
no row holds a newline. The count equals `grep -c $'^P\t'` over the same text, an empty text
included. The `.hy-runs` line runs in the stand-in's working directory, where both forms read the
same file and both print bash's own error for a missing one. `$TW1_SPEC` ends in `}`, so the
trailing-newline strip that `$( )` performs and `printf -v` does not changes no byte.

### What it does not check

- The key is read at the landed revision, so a branch cannot flip its own switch. In this
  repository the hook declines until the owner's line of S8 reaches `origin/main`, and an adopter's
  hook declines until its own landed policy sets the key.
- The leg grades spelling. That each conversion keeps its line's meaning is observed by the arms
  that already exercise each line: unit 3's AC5 and AC6 arms of `.githooks/pre-commit.test.sh`, the
  scoped liveness arms of `tools/memory-tree/check-memory-hygiene.test.sh@f74795972254:1330-1346`,
  arm 23 of `tools/roles/adopt-roles.test.sh` and the TW1 arms of
  `tools/workflows/unattended-build.test.sh`.
- Between the builder's commit and the mirror commit, `policy check`'s mirror arm reads red.

### Rollout

1. The builder's commit: every path under "Files touched" but the two `.governance` files.
   `help/commit-render.md`'s anchor takes the fingerprint `python tools/govkit/docs_leg.py --fingerprints`
   prints for `policy:memory.staged-render`, and `python tools/playbook/render_playbook.py --reference`
   writes `help/reference/policy.md`.
2. `python tools/policy/policy.py mirror --write`, and `.governance/policy.json` committed alone. The
   guard admits a mirror equal to its render at HEAD (`tools/policy/guard.py@a5d4f9583a5a:9-11`).
3. The owner commits `.governance/policy.toml` from a terminal, then step 2 runs again.

Once `check_staged_write` reads the key, `--write-staged` declines in this repository until the
owner's line of S8 reaches `origin/main`, as "What it does not check" states, so the hook no longer
clears a check 9 refusal. A check 9 refusal in the pass is cleared by
`python tools/memory-tree/gen_build_index.py --write` and staging the rendered files by hand.

### Inventory

| Minted | Kind | Graded by |
|---|---|---|
| `memory.staged-render` | policy catalogue key | `tools/policy/check_policy.py#arm_shape`. The lexicon declares no key surface: `python tools/lexicon/lexicon.py --suggest memory.staged-render --as toml.key` answered `unknown surface 'key'`, exit 2, on 2026-11-15, as it answered `TOOL-aNimbleMend-1` for `pass.fast-legs` |
| `policy-absent` | fixture branch name | none |
| `_c12_t`, `_c12_u`, `_c12_p` | shell variables | none: the lexicon declares no shell variable cell |
| `_w23`, `tw1_in` | suite shell variables | none, as above |

### Files touched (estimate)

- `tools/memory-tree/gen_build_index.py`
- `tools/memory-tree/.memory-tree.conf.example`
- `tools/memory-tree/README.md`
- `tools/memory-tree/check-memory-hygiene.sh`
- `.memory-tree.conf`
- `tools/policy/catalogue.toml`
- `.governance/policy.json`
- `.governance/policy.toml`
- `help/commit-render.md`
- `help/README.md`
- `help/policy.md`
- `help/reference/policy.md`
- `.githooks/pre-commit`
- `.githooks/pre-commit.test.sh`
- `tools/roles/adopt-roles.test.sh`
- `tools/workflows/unattended-build.test.sh`
- `memory/guides/SESSION-KICKOFF.md`, whose `last-audit` the builder's commit re-stamps: it stages
  `tools/memory-tree/check-memory-hygiene.sh` and `.memory-tree.conf`, both on the manifest's
  `watch:` line (`memory/guides/SESSION-KICKOFF.md@1e3ccd1af015:7`), and C5 of
  `skills/session-kickoff/manifest-check.sh@4d3d63c0fad1:1835-1844` reds a watch-touching commit
  that no `last-audit` stamp follows

### Alternatives rejected

- **Drop the switch.** The owner ruled for the key on 2026-11-15.
- **Add the pair to the legacy-home list.** It is shrink-only, and §3 rules out the edit.
- **Read the key through govkit's or the playbook kit's reader.** A kit imports no sibling, and
  `tree_lib.read_policy_value` is this kit's one policy read (TOOL-aNimbleMend-8 S7).
- **Keep the conf as a fallback.** One fact would have two homes, and the conf line is the legacy
  home the leg refuses.
- **Raise a Problem on a refused read.** It exits 1 as a decline does, under a second shape;
  `read_lane_state` treats a refused read as off with the reader's line.
- **Count the `P` rows with a `while read` loop over `<<<"$c12_sel"`.** `c12_sel` is assigned from a
  command substitution, so the loop is `loop-var-sub` on the leg `shell hygiene (a loop fed by a
  command substitution)`, whose `<<<` row for this file stands at 8.
- **Move `check_cold23` later in the substitution.** The substitution would still fork; only its
  first word would change.

## 5. Production-readiness checklist

- security — No new write path. The switch moves from a conf any committer edits to a guarded,
  owner-only file read at the landed revision, so an agent's branch cannot turn the hook's staging
  on. Every answer but `on` declines, the absent kit included.
- perf / scale — One `policy.py get` per `--write-staged` run, 0.44 s (PINNED 2026-11-15, §4), only
  after check 9 refused. `test_staged_write` holds 14 `run_write_staged(` calls today
  <!-- DERIVED from tools/memory-tree/gen_build_index.py@1eda60a27f2e by grep -c 'run_write_staged(' less its definition -->
  and gains no generator run: the off and refused arms take the two runs of the loop they replace,
  and the no-kit arm calls `check_staged_write` in-process. The leg's worst reading stays 88 s
  against its 140 s row in `tools/run-gates/selftest-budgets.txt`. <!-- PINNED 2026-11-15, selftest-budgets.txt:54 -->
  The three converted counts each remove one fork per run.
- error / empty / loading states — Four answers, four lines, §4 "The read". Each declines and
  exits 1, and the hook refuses as before.
- observability — The decline lines name the key and, on a refused read, the reader's line.
- risks — Dogfood is off until S8 lands at `origin/main`. A pass between the builder's commit and
  the mirror commit reads `policy check` red.
- testing — AC1 to AC3 are generator runs and one in-process call over fixtures. AC4 to AC10 are
  probes and greps. AC11 and AC12 are the main loop's and the owner's.
- migration — None. No release carried `STAGED_RENDER`: the build is not on `origin/main` at
  `a76c6afe7`, and no kit version moved in it.
- user docs — S5.

## 6. Acceptance criteria

`<f>` is unit 3's §6 fixture under `%TEMP%/<short-name>`, with no `STAGED_RENDER` line in its conf
and `.governance/policy.toml` holding `[memory]` and `staged-render = "on"` in its `rendered`
commit. `<gbi>` is `tools/memory-tree/gen_build_index.py` in this worktree, run in `<f>` with
`GOV_DEFAULT_BRANCH` set to `<f>`'s branch and `GOV_REMOTE` empty. "Unchanged" means
`git status --porcelain` prints the same bytes before and after.

- **AC1** — When `python <gbi> --write-staged` runs in `<f>`, it exits 0 and prints a
  `build-index: staged` line naming the build README of `<f>`.
  Red when: the switch is still read from the conf, so the run declines with
  `STAGED_RENDER is blank`. That is base behaviour.
- **AC2** — When `GOV_DEFAULT_BRANCH` names a branch of `<f>` whose tip deletes the policy file,
  and `<f>`'s conf carries `STAGED_RENDER="1"`, the run exits 1, prints
  `render NOT staged — memory.staged-render reads off`, and the tree is unchanged.
  Red when: the conf line still turns the render on, as at base, or the catalogue default is `on`.
- **AC3** — When `GOV_DEFAULT_BRANCH=no-such-branch`, the run exits 1, prints
  `render NOT staged — memory.staged-render did not read:`, and the tree is unchanged. When
  `check_staged_write` runs in-process with `read_policy_value` raising LookupError, it returns
  `(False, 'no policy kit resolves beside this kit, so memory.staged-render reads off')`.
  Red when: a refused read or an absent kit raises past the decline, or proceeds to stage.
- **AC4** — When `python tools/policy/policy.py get memory.staged-render` runs in this worktree, it
  prints `off` and exits 0. At base it exits 2 naming `is not a catalogue key`, observed 2026-11-15.
  `grep -c 'read_policy_value("memory.staged-render", root)' tools/memory-tree/gen_build_index.py`
  prints 1, and the row of `tools/policy/catalogue.toml` carries every field of §4 "The key".
  Red when: the row is absent or ships `on`, or the call passes the key through a variable, which
  reader coverage cannot see once this build lands.
- **AC5** — When `python tools/policy/policy.py lists --check` runs, it exits 0 and prints no line
  naming `STAGED_RENDER`. At base it prints `RED · 2 finding(s)`, observed 2026-11-15.
  `git grep -c STAGED_RENDER -- ':!memory/'` prints the one row
  `tools/memory-tree/gen_build_index.py:1`, and that line, by `git grep -n`, lies inside
  `test_staged_write`: the AC2 off arm's planted conf line of S3.
  Red when: a conf still assigns the key, or a doc, comment, code line or arm name still spells it,
  which adds a row or raises the count; or the planted line is gone, which drops the row.
- **AC6** — When `grep -c '<!-- usage: policy:memory.staged-render ' help/commit-render.md` runs, it
  prints 1. `grep -c 'memory.staged-render' help/README.md help/policy.md tools/memory-tree/README.md`
  prints at least 1 for each file. `grep -A1 '^## .memory.staged-render.$' help/reference/policy.md`
  prints, under the heading, the `Documented on` line whose link names `help/commit-render.md`.
  Red when: the key is unanchored, which the docs leg reds as an undocumented member, or the
  reference page was not re-rendered.
- **AC7** — When `python tools/policy/policy.py mirror --check` runs after step 2 of §4 "Rollout",
  it exits 0, and `grep -c '"memory.staged-render"' .governance/policy.json` prints 1.
  Red when: the mirror was not re-rendered, so its catalogue blob is the old one.
- **AC8** — When `grep -n 'hy_out' .githooks/pre-commit` runs, no line it prints holds `| grep`, and
  the line holding `HYGIENE check 9 FAILED` outside a comment opens `if [[`.
  `grep -c 'RUNS=$(cat .hy-runs)' .githooks/pre-commit.test.sh` prints 0.
  Red when: either site keeps its fork.
- **AC9** — When `bash tools/memory-tree/check-memory-hygiene.sh --only 12 --build aTrimmedWait`
  runs, its liveness line ends `over <N> spec(s) of aTrimmedWait`, and `--only 12 --spec` over this
  spec ends `over 1 spec(s) of` this spec's path. `grep -c 'c12_sel" | grep -c' tools/memory-tree/check-memory-hygiene.sh`
  prints 0.
  Red when: the length arithmetic miscounts, so `<N>` differs from the build's spec count.
  figure: `<N>` is DERIVED as the count of `memory/builds/aTrimmedWait/spec/*.md`, all dated after
  `SPEC_FORMAT_CUTOFF`.
- **AC10** — When `grep -c '"$(check_cold23' tools/roles/adopt-roles.test.sh` runs, it prints 0.
  `grep -c '$(printf "$TW1_SPEC"' tools/workflows/unattended-build.test.sh` prints 0, and
  `grep -c 'printf -v tw1_in "$TW1_SPEC"' tools/workflows/unattended-build.test.sh` prints 2.
  Red when: a site keeps its substitution.
- **AC11** — When the main loop runs `python tools/policy/check_policy.py` and the leg argv of
  `shell hygiene (a fork spent on builtin work)` in `tools/gate-legs.json`, each exits 0.
  `git diff 078eb5c58 -- memory/project/spawn-idiom-sites.txt tools/policy/legacy-homes.txt tools/policy/unsummarised-keys.txt`
  prints nothing.
  Red when: a count stays above its row, or the fix edited a list instead of the code.
  permission: the main loop's; a role agent runs no gate.
- **AC12** — When the owner's commit of S8 is HEAD's parent, `python tools/policy/policy.py get memory.staged-render --rev HEAD`
  prints `on`, and `python tools/policy/policy.py mirror --check` exits 0.
  Red when: the line sits under another table, so the key reads its default.
  permission: the owner's; the policy guard refuses an agent's commit to the file.

## 7. Gates

`policy check` · `shell hygiene (a fork spent on builtin work)` · `shell hygiene (a loop fed by a command substitution)` · `build-index selftest` · `memory hygiene` · `memory-hygiene self-test` · `branch-guard self-test` · `roles adopter self-test` · `unattended-build self-test` · `docs` · `help reference pages` · `help page commands` · `lexicon naming predicates` · `policy fixtures` · `scratch-guard self-test` · `routed-commits selftest` · `tier2-review self-test` · `verifier fan-out self-test` · `review-join self-test` · `kit/dogfood doc parity` · `recall floor` · `recall floor arms` · `transition-audit arms` · `straggler-guard arms`

The first two are the legs this unit turns green, and the third is the leg §4 rejects a loop for.
The suites re-observe each converted line, and `docs` and the two help legs grade S5. The last ten
are owed by a guard a path of the estimate trips. The main loop runs the merge bar once, at the
close. No leg is added.

New arm: tools/memory-tree/gen_build_index.py · covers AC1 AC2 AC3 · `test_staged_write` with each fixture's switch in its committed policy file, the absent-file branch, the unresolved branch and the stubbed reader; RED with `check_staged_write` reading `conf.get("STAGED_RENDER")` again, where the fixture's key reads blank and AC2's conf line proceeds · none

## 8. Open questions

none

## 9. Revision log

- rev-1 · 2026-11-15 · initial draft.
- rev-2 · 2026-11-15 · the builder's DIVERGENCE before any edit and the owner's ruling to keep the
  stale-conf arm (2026-11-15-prompt-TOOL-aTrimmedWait-10-revision): S3 keeps one fixture spelling of
  the retired key and AC5 counts it; the loop's two AC2 arms are renamed to name the key; §5 keeps
  the generator-run count; "Files touched" adds the manifest's `last-audit` re-stamp; "Rollout"
  states how a check 9 refusal is cleared before S8 lands; §7 adds `recall floor arms`, the leg
  the manifest path's guard owes.

## 10. Reuse audit

The seam is `tree_lib.read_policy_value`, the memory-tree kit's one policy read, called as
`read_lane_state` in `tools/memory-tree/routed_commits.py` calls it, with that function's mapping of
LookupError and ValueError. The row follows the `TOOL-aNimbleMend-1` block of
`tools/policy/catalogue.toml`, and the anchor follows `help/red-fix-lane.md`'s. The no-kit arm
reuses `routed_commits.py`'s module-global stub. The conversions are the forms the leg's own class
labels name. `tools/codebase-map/reuse_lookup.py` for "read an on or off switch from the policy
catalogue in a memory-tree kit tool, off when no policy kit resolves" ranked `read_policy_value` a
SEAM, in `tools/memory-tree/tree_lib.py` beside govkit's and the playbook kit's own; no closer seam.
Recall returned the same refusal met by `TOOL-dFoldedAudit-7` for `.unattended.conf` and by the
`dLinkedLibrary` spec audit for a `.memory-tree.conf` cutoff, each resolved to a catalogue key or no
conf key.

Recall terms used: legacy home shrink-only catalogue key policy.toml read_policy_value memory-tree
conf switch default off mirror
