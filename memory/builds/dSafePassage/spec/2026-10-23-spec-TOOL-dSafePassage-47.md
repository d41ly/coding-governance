# TOOL-dSafePassage-47 — the submodule walk lists a repository by git's own directory shape, and refuses one whose config git cannot read

**Status:** DEFERRED · rev-2 · 2026-10-23 · node d · Tier-2 · base 3708a705 · streams tooling · order 12 · advances TOOL-dSafePassage-14

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-23-build-TOOL-dSafePassage-47-deviation-93.md](../build/2026-10-23-build-TOOL-dSafePassage-47-deviation-93.md) | deviation | — |
| [2026-10-25-build-TOOL-dSafePassage-1-agent-ledger.md](../build/2026-10-25-build-TOOL-dSafePassage-1-agent-ledger.md) | journal | TOOL-dSafePassage-1 TOOL-dSafePassage-2 TOOL-dSafePassage-3 TOOL-dSafePassage-4 TOOL-dSafePassage-5 TOOL-dSafePassage-6 TOOL-dSafePassage-7 TOOL-dSafePassage-8 TOOL-dSafePassage-9 TOOL-dSafePassage-10 TOOL-dSafePassage-11 TOOL-dSafePassage-12 TOOL-dSafePassage-13 TOOL-dSafePassage-15 TOOL-dSafePassage-16 TOOL-dSafePassage-17 TOOL-dSafePassage-18 TOOL-dSafePassage-19 TOOL-dSafePassage-20 TOOL-dSafePassage-21 TOOL-dSafePassage-22 TOOL-dSafePassage-23 TOOL-dSafePassage-24 TOOL-dSafePassage-25 TOOL-dSafePassage-26 TOOL-dSafePassage-27 TOOL-dSafePassage-28 TOOL-dSafePassage-29 TOOL-dSafePassage-30 TOOL-dSafePassage-31 TOOL-dSafePassage-32 TOOL-dSafePassage-33 TOOL-dSafePassage-34 TOOL-dSafePassage-35 TOOL-dSafePassage-36 TOOL-dSafePassage-37 TOOL-dSafePassage-38 TOOL-dSafePassage-39 TOOL-dSafePassage-40 TOOL-dSafePassage-41 TOOL-dSafePassage-42 TOOL-dSafePassage-43 TOOL-dSafePassage-44 TOOL-dSafePassage-45 TOOL-dSafePassage-46 TOOL-dSafePassage-48 TOOL-dSafePassage-49 TOOL-dSafePassage-50 TOOL-dSafePassage-51 TOOL-dSafePassage-52 TOOL-dSafePassage-53 TOOL-dSafePassage-54 TOOL-dSafePassage-55 TOOL-dSafePassage-56 TOOL-dSafePassage-57 TOOL-dSafePassage-58 TOOL-dSafePassage-59 |
| [2026-10-23-review-TOOL-dSafePassage-47-48-49-50-spec-audit-round1.md](../reviews/2026-10-23-review-TOOL-dSafePassage-47-48-49-50-spec-audit-round1.md) | spec-audit | TOOL-dSafePassage-48 TOOL-dSafePassage-50 TOOL-dSafePassage-49 |

<!-- /gen:spec-records -->

## 1. Goal

The spec audit of units 43 to 46
(`memory/builds/dSafePassage/reviews/2026-10-23-review-TOOL-dSafePassage-43-44-45-46-spec-audit-round1.md`)
confirmed finding **id 9** at HIGH, its item **D-1**. The same defect was found at MEDIUM as id 26,
item D-7. That id is batched by its own id in `TOOL-dSafePassage-49`, which adds the second cause it
found.

TOOL-dSafePassage-45 S12 and its §4 "The walk's repository test" list a directory under
`<git_dir>/modules/` as a repository only when `git --git-dir=<d> rev-parse --git-dir` exits 0. Every
other directory goes down the name-segment branch. This unit's probe ran on node d, git
2.54.0.windows.1, 2026-10-23, in a scratch superproject under `%TEMP%`, with the system and global
scopes off. In that superproject `.git/modules/sub` exited 0. After `[core` was appended to its
`config`, both `rev-parse --git-dir` and `config --list` exited 128 with
`fatal: bad config line 15 in file .git/modules/sub/config`. So the repository is never listed, the
read that S12 makes a refusal never runs on it, and the walk descends into its `objects/` and `refs/`.
TOOL-dSafePassage-45 AC9 requires `--plant submodule-config-malformed` to be refused naming the config
file, which a correct build of S12 cannot reach.

This unit is id 9's promotion, built from the skeptic's corrected fix. A directory is a candidate
repository by its shape alone. Each candidate's config read runs, and a read that fails is a refusal.

## 2. Scope (IN)

- **S1** — The shape test. In `read_target_repositories`'s `modules/` walk (TOOL-dSafePassage-30 S1,
  rooted by TOOL-dSafePassage-36 S1), a directory `c` is a candidate repository when `c/HEAD` is a
  regular file and `c/objects` and `c/refs` are directories. The test reads the filesystem only and
  runs no git command, so a repository git refuses to open is classified exactly as a sound one.
  Observed by AC1 and AC2.
- **S2** — The read and its refusal. Each candidate gets TOOL-dSafePassage-30 S2's read,
  `git --git-dir=<c> config --list --show-scope --show-origin --includes -z`. Exit 0 lists the
  candidate, and its rows are graded as every listed repository's are. Any other exit is a refusal
  naming `<c>/config` and the exit code, whatever its stderr says, and stderr is never parsed. The
  refusal uses TOOL-dSafePassage-24's one `raise Refusal` site. Observed by AC2.
- **S3** — The descent. The walk descends into a directory that is not a candidate, which is a
  segment of a submodule name holding `/`. Inside a candidate it descends into that candidate's own
  `modules/` only. So no candidate's `objects/`, `refs/` or `logs/` tree is walked, and a ref named
  `config` is never reached. Observed by AC1 and AC3.
- **S4** — The plants. `submodule-config-malformed`, which TOOL-dSafePassage-45 mints, is a
  superproject whose absorbed submodule's `.git/modules/<name>/config` ends with the unterminated
  section `[core`. The `isolation` family of `python3 "tools/govkit/upgrade_steps.py" fixture` gains
  `submodule-name-slashed`: a submodule named `lib/x`, so its repository sits at
  `.git/modules/lib/x/`, whose config sets `filter.canary.clean`. Observed by AC2 and AC3.
- **S5** — The reading. TOOL-dSafePassage-45 S12 and its §4 "The walk's repository test" are read
  with S1 to S3 in place of the `rev-parse --git-dir` test, and TOOL-dSafePassage-36's hands-off
  bullet to TOOL-dSafePassage-45 is read the same way. TOOL-dSafePassage-45 AC9 stands as written,
  and AC1 and AC2 here are its two halves under this design. The §3 hands-off bullets of
  TOOL-dSafePassage-45 and TOOL-dSafePassage-36 to this unit name the reading, so whichever pass first
  builds the walk's test builds this one. Observed by AC1 and AC2.
- **S6** — The docs. The "What a step can reach" section of `help/upgrade-steps.md` says that a
  submodule repository whose config git cannot read refuses the step, naming that config file.
  Observed by AC4.

## 3. Non-goals (OUT)

- A repository git refuses to open for a reason other than its config, such as an unknown
  `core.repositoryformatversion`: finding 26, item D-7, batched in `TOOL-dSafePassage-49`.
- The `.gitmodules` read and its exits, which TOOL-dSafePassage-45 S13 states.
- Parsing git's stderr to tell one failure from another. S2 refuses every non-zero exit alike.

### Edges

- **consumes-from** `TOOL-dSafePassage-45` — S12's walk, its plants `submodule-ref-named-config` and `submodule-config-malformed`, and AC9, whose repository test this unit replaces; without them there is no walk test to correct
- **consumes-from** `TOOL-dSafePassage-36` — the `modules/` walk rooted at the target's own git directory, whose classification and descent this unit states
- **hands-off** `TOOL-dSafePassage-49` — the candidate's `rev-parse --git-dir` exit added to S2's refusal, and the `submodule-format-unknown` plant, finding 26 of the spec audit of units 43 to 46
- **hands-off** `TOOL-dSafePassage-51` — the walk never following a symlink or junction, a link or an unlistable directory under `modules/` refused naming its path, with the `submodule-modules-link-loop` plant; S2's refusal naming `<c>/config` "or a file it includes"; S2's read placed before `TOOL-dSafePassage-49`'s `rev-parse`; and AC4 read through that unit's one section probe, findings 22, 23, 2, 9 and 8 of the spec audit of units 47 to 50

## 4. Design

### The walk

```
walk(d):                                        # d starts at <git_dir>/modules/
  for c in subdirectories of d:
    if isfile(c/HEAD) and isdir(c/objects) and isdir(c/refs):      # S1, a candidate
      rc = git --git-dir=c config --list --show-scope --show-origin --includes -z
      if rc != 0:  refuse "<c>/config", rc                         # S2
      else:        list c; walk(c/modules)                         # S3
    else:
      walk(c)                                   # S3, a name segment
```

| Directory under `modules/` | Shape | Outcome |
|---|---|---|
| a sound submodule repository | candidate | listed, its rows graded |
| a repository whose `config` does not parse | candidate | refused, naming `<c>/config` |
| `lib/` of a submodule named `lib/x` | not a candidate | descended as a name segment |
| `refs/heads/config` inside a repository | never reached | not walked |

This unit's probes on node d, 2026-10-23, both under `%TEMP%`. A directory holding only a `HEAD`
file and empty `objects/` and `refs/` directories exited 0 under `git --git-dir=<d> rev-parse
--git-dir`, and the same shape without `refs/` exited 128. So the shape S1 tests is one git itself
opens. `.git/refs/heads` exited 128.

### Inventory

Minted in `tools/govkit/upgrade_steps.py`: the plant `submodule-name-slashed`. No function, conf
key, gate leg or policy key. S2's refusal is TOOL-dSafePassage-24's one `raise Refusal` site, so
`tools/govkit/refusal_join.py`'s `BRANCH_PIN` does not move.

### Migration

None: no step row spawns before this build's walk lands.

### Rollout

Live at landing. It builds at order 12, one above TOOL-dSafePassage-45 (order 11), whose walk test
it repairs. It shares `tools/govkit/upgrade_steps.py` and `tools/govkit/selftest.py` with
`TOOL-dSafePassage-48` at order 12, so the build run sequences the two passes by M6's first clause.
`TOOL-dSafePassage-50`, also at order 12, writes none of this unit's files.

### Files touched (estimate)

- `tools/govkit/upgrade_steps.py`
- `tools/govkit/selftest.py`
- `help/upgrade-steps.md`

### Alternatives rejected

- **Keep `rev-parse --git-dir` and read its stderr.** The finder's fix, rejected by the skeptic. The
  stderr text is git's to change, and a message parse would sort a new failure into the
  name-segment branch, which is the silent skip this unit closes.
- **List a directory because it holds a `config` file.** TOOL-dSafePassage-45 S12 rejects it: a ref
  named `config` becomes a population row.
- **Skip a candidate whose read fails.** The read fails exactly where git cannot tell what the
  config holds, so a skip passes a config nobody graded.

## 5. Production-readiness checklist

- security: a submodule repository with an unreadable config now refuses the step, where before it
  passed ungraded.
- perf / scale: three filesystem tests per directory under `modules/`, in place of one `rev-parse`
  spawn; one config read per candidate, as before.
- error / empty / loading states: a failed read is a refusal naming the file and the exit, never a
  skip; a target with no `modules/` directory yields no candidate.
- observability: the refusal names `<c>/config` and the exit code.
- risks: a directory under `modules/` that has the shape and is not a repository refuses the step;
  git writes nothing of that shape there except a submodule's git directory.
- testing: the three plants of §6, through §7's arm.
- migration: none.
- user docs: `help/upgrade-steps.md`, S6.

## 6. Acceptance criteria

- **AC1** — When `python3 "tools/govkit/upgrade_steps.py" fixture isolation --plant submodule-ref-named-config`
  runs, its population holds one row per real repository, none under `refs/`, `objects/` or `logs/`,
  and the run exits 0.
  Red when: a ref named `config` becomes a row, or the walk descends into a candidate's `refs/`.
- **AC2** — When the same family runs with `--plant submodule-config-malformed`, the step is refused
  before any spawn, the refusal names `.git/modules/<name>/config`, and the run exits 1.
  Red when: the malformed repository goes down the name-segment branch and the run exits 0.
- **AC3** — When the same family runs with `--plant submodule-name-slashed`, the step is refused
  naming `filter.canary.clean` and `.git/modules/lib/x/config`, and the run exits 1.
  Red when: the walk does not descend through the `lib/` name segment, so the key passes ungraded.
- **AC4** — When `awk '/^#+ What a step can reach/{f=1;next} /^#+ /{f=0} f' help/upgrade-steps.md`
  runs, its output holds a line naming a submodule config git cannot read as refused.
  Red when: the section says nothing of a submodule config that does not parse.

## 7. Gates

`govkit selftest` · `govkit refusal join` · `govkit acceptance matrix` · `govkit selfcheck` · `recall floor arms` · `encoding posture (text IO names its encoding)` · `lexicon naming predicates` · `spec tokens (a spec's own names resolve)`

New arm: tools/govkit/selftest.py · covers AC1 AC2 AC3 · the self-test runs the three plants through the walk, its failing cases staged by a walk copy that classifies by the `rev-parse --git-dir` exit, which skips the malformed repository, and by a walk copy that never descends a non-candidate, which misses `lib/x` · none

What the check does not cover: a directory of the shape under `modules/` that git did not write, and
a repository git refuses for a reason its config read does not hit, which `TOOL-dSafePassage-49`
takes.

## 8. Open questions

none

## 9. Revision log

- rev-1 · 2026-10-23 · initial draft, the promotion of the spec audit of units 43 to 46's id 9 (HIGH,
  item D-1), from the skeptic's corrected fix.
- rev-2 · 2026-10-23 · §3 · the Edges gain the end this unit owes the promotion `TOOL-dSafePassage-51` of the spec audit of units 47 to 50, written by the disposal stage; no other section moved.

## 10. Reuse audit

The seams extended are TOOL-dSafePassage-30's `read_target_repositories` and its config read,
TOOL-dSafePassage-36's walk root and TOOL-dSafePassage-24's refusal, all specced and unbuilt at the
base. `python tools/codebase-map/reuse_lookup.py "classify a directory as a git repository by its layout"`
ranked `git`, `run_git`, `classify` and `read_git_output`, name-token matches; none tests a
directory's layout, so no existing seam fits beyond those specs. The shape was measured against git
itself on node d, not taken from a record.

Recall terms used: `python tools/memory-recall/query.py "how a spec audit finding on a submodule walk or a refused executor key is promoted and its reading carried to the faulted unit" --terms "spec audit promoted reading hands-off submodule walk repository shape refused executor sendemail identity"`
