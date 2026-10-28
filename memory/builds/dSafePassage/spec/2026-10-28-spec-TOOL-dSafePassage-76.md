# TOOL-dSafePassage-76 — the closing review's nine engine-side minors, from a before-image restoring into the git directory to a walk refusal blamed on the config

**Status:** DEFERRED · rev-3 · 2026-10-28 · node d · Tier-2 · base 83817478 · streams tooling · order 16 · advances TOOL-dSafePassage-14 · ratified 2026-10-28

**Derived:** TOOL-dSafePassage-1

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-28-prompt-TOOL-dSafePassage-76-1-spec-writer.md](../prompts/2026-10-28-prompt-TOOL-dSafePassage-76-1-spec-writer.md) | journal | — |
| [2026-10-28-prompt-TOOL-dSafePassage-76-spec-brief.md](../prompts/2026-10-28-prompt-TOOL-dSafePassage-76-spec-brief.md) | research | TOOL-dSafePassage-77 |

<!-- /gen:spec-records -->

## 1. Goal

The closing diff review of this build confirmed ten mediums and five lows. This unit is the batch of
the nine that sit in the engine (BUILD-METHOD M4): M1 (id 3), M3 (id 6), M4 (id 7), M5 (id 10),
M9 (id 19), L1 (id 11), L2 (id 12), L3 (id 13) and L5 (id 21). Each is closed at the fix the review's
skeptic judged sound, and for M1 and L2 at the skeptic's corrected fix. The walk leg's five are
TOOL-dSafePassage-77's, and the review's line numbers, taken at `83817478f`, were re-read at that
commit for every citation here.

## 2. Scope (IN)

- **S1** — M1, a before-image never writes into the git directory. `check_contained`
  (`tools/govkit/upgrade_steps.py:1040-1045`), as TOOL-dSafePassage-72 leaves it, refuses a `rel`
  whose normalised form (72's `derive_contained_rel`) has any segment equal to `.git` once
  case-folded and stripped of trailing dots and spaces. It also refuses a `rel` whose
  `(target / rel).resolve()` lies at or under the resolved git directory of the target, read once per
  resolved target by `read_git_dir`: `git -C <target> rev-parse --absolute-git-dir`, run under
  `build_step_env` as `read_target_repositories` runs it (`:1496`). `resolve()` expands the
  existing prefix, so a short name such as `GIT~1` is judged by the directory it names. A target git
  names no git directory for has none to compare, so the lexical arm alone applies there. Every
  caller inherits both refusals: `write_before_image` (`:1089`), `read_image_changes` (`:1111`),
  `write_from_before_image` (`:1129`), `read_image_paths` (`:1918`), and `derive_image_path`, which
  72 routes through it. The skeptic left out the receipt-sha check, and so does this unit. Observed by AC1.
- **S2** — M3, the forward walk's kill recovery stages. In `run_step_walk`'s move 1
  (`:1986-1994`), a row whose witness holds and whose before-image exists at
  `derive_image_path(target, row.id)` is staged by
  `write_step_staged(target, row.id, read_image_paths(target, row.id), ...)` before
  `persist(row, "applied", ...)`, with the `then` text move 5 passes (`:2008-2009`). A row with no
  image stages nothing, as today. Observed by AC2.
- **S3** — M3, the reverse walk's kill recovery stages. In `run_reverse_walk`, the paths staged after
  a down that took effect (`:2164`) are `paths`, read before the down (`:2128`), or where that is
  empty, the paths of the image the index holds, read by `read_image_paths` from
  `git show :<image path>` when the working tree has no image. `derive_down_verdict`'s
  `image_present` and move 3's `via` test keep reading the working tree. The source is §8 F1's
  recommendation. Observed by AC3.
- **S4** — M4, a rollback over a receipt that records a step id gov has since retired.
  `derive_reverse_steps` (`:2041-2056`) takes out of `gone` (`:2049`) each id a `[[retired]]` row of
  gov's HEAD names, read by `read_retired(gov_root, "HEAD", None)`, as `check_gov_first` does
  (`:2027-2029`). Each such id the receipt records `applied` or `failed` has its introducing commit
  derived by `derive_introduced`, over the files `read_steps` walks at HEAD (`:861-862`). One
  introduced at an ancestor of `to_commit` owes no down and passes. One that does not, or has no
  derivable commit, is refused before any down, naming the id, the retiring row, and that its down is
  owed and no row declares one. The successor is not read, per §8 F2's recommendation.
  **Readers:** this item takes no name out of use; it reads ids a retirement row names.
  by name: `derive_reverse_steps` and `check_gov_first`, the two readers that compare a receipt's
  step ids with the declared rows.
  by value: `read_retired`'s rows, compared by `id` against the receipt's `steps`.
  Observed by AC4.
- **S5** — M5, the floor down's `<to>` outside gov. `python_floor.py`'s `down` verb
  (`tools/lib/python_floor.py:407-412`) defaults `<to>` to the target's `HEAD` only where the resolved
  target is gov, the repository holding the module, found by the reading `read_down_population`
  makes (`:299-300`), moved into one helper `derive_gov_root` both call. Elsewhere a missing `<to>`
  exits 2 with `python-floor down: <to> is required outside gov's own tree: the target's HEAD is a
  commit gov's repository never holds`. The usage lines of `python_floor.py` (`:5`) and
  `tools/lib/python-floor.sh` (`:6`, `:45`) say `[<to>, required outside gov]`. Observed by AC5.
- **S6** — M9, a failing clean-hash proves nothing. `check_render_edited`
  (`tools/govkit/govkit.py:9271-9273`) returns True where `git hash-object --path` exits non-zero or
  prints nothing, so the row reads `render-edited`, its kit is held and the row ordered
  (`:10362-10364`). The fixture `tools/govkit/fixtures/retired_edits.py` gains the plant
  `render-filter-broken`. Observed by AC6.
- **S7** — L2, `run_step_walk` (`tools/govkit/upgrade_steps.py:1937-2034`) takes five parameters:
  the unread `to_commit` is removed from its signature and from every caller's sixth argument.
  **Readers:**
  by name: `tools/govkit/govkit.py` at `:9454-9455` and `:11726-11727`, the FIXTURE child in
  `tools/govkit/upgrade_steps.py` at `:3407`, and `tools/govkit/selftest.py` at `:4448`, the four
  call sites a grep for the call lists; the docstring of `run_step_walk` never named it.
  by value: NO VALUE READERS — the body never reads the parameter, which is the finding.
  Observed by AC7.
- **S8** — L5, a walk refusal is not blamed on the config. `check_target_local_config`
  (`:1678-1680`) raises `Refusal` carrying `render_redacted_config` of the walk's reason where
  `read_target_local_config` returns a string, and returns found keys only. `run_step_isolated`
  (`:1703-1707`) wraps that refusal as `<id> <phase>: the repositories a step could enter from the
  target could not be cleared: <reason>, so nothing was spawned`, and keeps the executor and
  credential wording for found keys. The isolation plants' expectation for each unkeyed kind
  (`:3285-3295`) asserts the refusal begins with `<id> up: the repositories a step could enter from
  the target could not be cleared: ` and holds the kind's reason. Observed by AC8.
- **S9** — The pages. `help/upgrade-steps.md`, `help/python-floor.md` and `help/update-edits.md`
  carry the sentences §4 "The pages" lists: L1's correction of the rollback's "What runs" bullet
  (`help/upgrade-steps.md:275-283`), L3's no-walk line beside the `--kits` bullet (`:218-223`),
  one sentence each for S1, S2 with S3, S4, S5, S6 and S8, and the schema step's paragraph
  (`:184`), whose "Until the deployer runs steps itself, run the step by hand" predates
  TOOL-dSafePassage-2's walk. Observed by AC9.

## 3. Non-goals (OUT)

- The walk leg's five items, M6, M7, M8, M10 and L4. They are TOOL-dSafePassage-77's.
- The HIGH items, H1 to H5. TOOL-dSafePassage-72 to -75 close them, and S1 builds on H1's
  `check_contained`.
- Re-downing a step already recorded `rolled-back` (L1's other option). TOOL-dSafePassage-4 S3 and
  TOOL-dSafePassage-49 S5 skip such a row by design, so the page is what is wrong.
- A receipt-sha check on a before-image (M1), and the read-set and `test_step_row` widening it would
  need. The skeptic left it out.
- Following a retired id's successor (M4), held to §8 F2.
- Amending TOOL-dSafePassage-2 S2's signature (L2). That spec is CLOSED and frozen; this spec is the
  record of the five-parameter signature.
- Any other "recommended as its own unit" hand-off in the build's CLOSED specs. The review's checklist
  row for them is not one of this brief's items.

### Edges

none

Read and closed, so named here rather than joined: TOOL-dSafePassage-1's before-image and
`check_contained`; TOOL-dSafePassage-2's `run_step_walk`, `write_step_staged` and staging journal;
TOOL-dSafePassage-4's `derive_reverse_steps` and `run_reverse_walk`; TOOL-dSafePassage-9's
`check_render_edited` and the `retired_edits.py` fixture; TOOL-dSafePassage-11's and
TOOL-dSafePassage-26's floor down; TOOL-dSafePassage-24, -30, -56 and -59's config check and
repository walk; TOOL-dSafePassage-33 and -40's `via` rule; and TOOL-dSafePassage-70's `held` guard.
The edge join counts CLOSED specs, and a CLOSED spec cannot take the matching `hands-off` line.
TOOL-dSafePassage-72 is not an edge either: S1 builds on its `check_contained` by order of dispatch,
as the brief rules.

## 4. Design

### S1: two refusals, lexical then resolved

```
check_contained(target, rel):
    ... TOOL-dSafePassage-72's normalisation, climb, rooted and link refusals ...
    if any(seg.casefold().rstrip(". ") == ".git" for seg in norm.split("/")):
        refuse "'<rel>' is inside the repository's git directory, so no step may write it"
    gd = read_git_dir(<resolved target>)      # cached per target; None where git names none
    if gd and (target / norm).resolve().is_relative_to(gd):
        refuse the same, naming <gd>
    return pathlib.Path(target) / norm
```

The lexical arm catches `.git`, `.GIT` and `.git.` on any platform. The resolved arm catches what
the lexical one cannot spell: a short name on a volume that keeps them, and a git directory that is
not called `.git`, as `git init --separate-git-dir` makes. `derive_image_path` asks
`check_contained` on every image read once 72 lands, so the git directory is read once per resolved
target and process, `functools.lru_cache` on `read_git_dir`:
`# ponytail: a target whose git directory moves mid-process reads the old one; no step moves it`.
A target outside any repository, as the `[dSP-1 S3]` image row's scratch directory
(`tools/govkit/selftest.py:3097-3104`), keeps today's answers.

### S2 and S3: the kill windows

| Kill | Receipt after the kill | Re-run at HEAD | After this unit |
|---|---|---|---|
| forward, after the second witness, before `write_step_staged` | `failed`, `interrupted:` | move 1 records `applied`, stages nothing | move 1 stages the image's paths and the image, then records `applied` |
| reverse, after the down restored, before staging | `applied` or `failed`, `down interrupted:` | `paths` is `[]`, nothing staged, `rolled-back` | the index's copy of the image names the paths; each is staged, the image's deletion included |

The image is staged and committed with its step's up (TOOL-dSafePassage-2 S11), so the index holds it
until a staging of its deletion. That is why the index can answer for a working-tree image the down
took away. Where the index holds none, the list is `[]`, which is today's behaviour.

### S4: which retired ids may stand in a receipt

| Recorded id | Declared at HEAD | Named by a `[[retired]]` row at HEAD | Introduced at an ancestor of `--to` | Verdict |
|---|---|---|---|---|
| any | yes | no | any | as today |
| any | no | no | any | refused, as today |
| `rolled-back` | no | yes | any | passes, nothing owed |
| `applied` or `failed` | no | yes | yes | passes, no down owed |
| `applied` or `failed` | no | yes | no, or not derivable | refused: its down is owed, no row declares it |

### S5: the gov test

`read_down_population` already decides "is the target gov" by resolving both paths (`:299-300`,
`:308`). `derive_gov_root()` returns that resolved gov, and `main` asks it before defaulting `<to>`.
The step row always passes `{to}` (`tools/govkit/steps.toml`), so the walk is unaffected. Defaulting
to the receipt's `gov_commit` was the review's other option, and it is wrong here: the down grades
the bytes the rollback restores, at `<to>`, and `gov_commit` names the vintage being left.

### S6: why True and not a finding

A failed hash cannot tell edited from clean. True holds the kit and orders the row, which keeps the
adopter's bytes, and the review's left-shift gate asks for exactly `render-edited` and `HELD BACK`.
The order then names an edit that may not exist, and the adopter who opens it sees a broken filter.
That costs one read; a re-render over a real edit costs the edit.

### S8: one prefix per cause

| Cause | Refusal at HEAD | After this unit |
|---|---|---|
| a refused key in a repository's config | `<id> <phase>: the target's own git config declares what git runs as a program or sends as a credential, <key> in <file>, so nothing was spawned: ...` | the same |
| the walk refused (a link, an unreadable `.gitmodules` or config, a repository git will not open, a git call failing) | the same executor prefix, then the walk's reason | `<id> <phase>: the repositories a step could enter from the target could not be cleared: <reason>, so nothing was spawned` |

### The pages

| Page | Where | Sentence |
|---|---|---|
| `help/upgrade-steps.md` | "What runs, in what order" (`:275-283`) | "A step recorded nowhere runs its witness first and is skipped where the witness does not hold: `step <id> · skipped (nothing applied)`. A step the receipt already records `rolled-back` when the run starts is not downed again." |
| `help/upgrade-steps.md` | after the `--kits` bullet (`:218-220`) | "A write run that already has a finding walks none either, and prints `steps: not walked — this run already has <n> finding(s) · <n> pending` in place of the count line." |
| `help/upgrade-steps.md` | "A step that runs" (`:203-210`) | "A path a before-image lists inside your repository's git directory, `.git` in any case or wherever `git rev-parse --absolute-git-dir` points, is refused, so no up or down writes there. A run after a kill stages the writes and the before-image a killed step left unstaged, and a rollback run again after a kill stages what the killed down restored." |
| `help/upgrade-steps.md` | "When" (`:271-274`) | "A receipt recording a step id a `[[retired]]` row names is refused only where that step was introduced after `<rev>`, since its down is owed and no row declares one." |
| `help/upgrade-steps.md` | the config check (`:54-82`) | "A refusal by the walk itself, a link, a `.gitmodules` or a config that does not read, or a repository git will not open, reads `the repositories a step could enter from the target could not be cleared: <reason>`; only a refused key reads that your config declares it." |
| `help/upgrade-steps.md` | the schema step's paragraph (`:184`), its three usage markers kept | "`update --write` walks this step like any other; to run it by hand outside a walk:" in place of "Until the deployer runs steps itself, run the step by hand:" |
| `help/python-floor.md` | "The upgrade step" (`:75-76`) | "`<to>` is required in an adopter, whose `HEAD` gov's repository never holds; left out on gov's own tree, it defaults to gov's `HEAD`." |
| `help/update-edits.md` | "A rendered file you edited" (`:37-45`) | "A rendered file git cannot hash through its own filters, a required clean filter that fails say, cannot be proven unedited, so it reads `render-edited` too." |

### Inventory

Minted: the functions `derive_gov_root` in `tools/lib/python_floor.py` and `read_git_dir` in
`tools/govkit/upgrade_steps.py` (`python tools/lexicon/lexicon.py --suggest <name> --as py.function`
answers OK for each on 2026-10-28); the `retired_edits.py` plant `render-filter-broken`; the `fixture walk` plant
`kill-before-stage`; the `fixture rollback` plant `kill-after-down-stage` and its
`FIXTURE_WALK_STEP` switch `<slug>.down-block-after`, which blocks after `write_from_before_image`;
and the `fixture rollback-update` plant `retired-step`. Plant names and switches are not lexicon
surfaces. No conf key, gate leg, policy key or receipt field is minted.

Refusal branches added: S1's two in `check_contained`, S4's one in `derive_reverse_steps`, and
S8's one in `check_target_local_config`, its wrap in `run_step_isolated` taking the place of the
branch there. The build measures the matcher's count over `tools/govkit/` at its base and on the tree
it leaves and moves `BRANCH_PIN` (`tools/govkit/refusal_join.py:41`) by that delta, named beside it
as the comment there records each move. Each new branch is reached by its arm in §7.

### Migration

None. No recorded value changes shape. A receipt naming a retired step id passed nowhere before and
passes S4's rows now.

### Rollout

Live at landing, at order 16. Every HIGH unit, TOOL-dSafePassage-72 to -75, writes
`tools/govkit/upgrade_steps.py`, so M6 sequences this unit after them by order of dispatch; S1 also
reads 72's `check_contained`. TOOL-dSafePassage-77 writes only the walk leg, and §8 F2 of that spec
names its one page sentence.

### Files touched (estimate)

- `tools/govkit/upgrade_steps.py`
- `tools/govkit/govkit.py`
- `tools/govkit/selftest.py`
- `tools/govkit/refusal_join.py`
- `tools/govkit/fixtures/retired_edits.py`
- `tools/lib/python_floor.py`
- `tools/lib/python-floor.sh`
- `tools/lib/resolve-python.test.sh`
- `help/upgrade-steps.md`
- `help/python-floor.md`
- `help/update-edits.md`

### Alternatives rejected

- **S1 by a call to `demand_contained_dest`** (`tools/govkit/govkit.py:1244`). It answers the climb,
  not the git directory; TOOL-dSafePassage-72 owns that seam.
- **S3 by a sidecar journal or a field on the `down interrupted` record.** §8 F1 sets both beside the
  index read.
- **S6 as a finding naming git's stderr.** It stops the run where a hold already keeps the bytes, and
  the review's gate asks for the hold.
- **S8 by matching the reason's text in `run_step_isolated`.** The type already tells the two apart
  at `read_target_local_config`'s return; a text match would break on the next reason.

## 5. Production-readiness checklist

- security: S1 narrows the before-image's write surface to the worktree outside the git directory,
  which closes M1's hook plant. S1's `rev-parse` runs under `build_step_env`, reads no index and
  spawns no target program. No grant widens.
- perf / scale: one `rev-parse` per target and process (S1); one `git show` per reverse row that
  lost its image (S3).
- error / empty / loading states: a target git names no git directory for is graded by the
  lexical arm alone (S1); an
  index holding no image stages nothing (S3); a retired id with no derivable commit refuses (S4).
- observability: S8's prefix names the real cause; S5's exit-2 line says why `<to>` is required.
- risks: S1 refuses a step whose up names a `.git` path; no shipped step does
  (`tools/govkit/steps.toml`). S6 can order an unedited render behind a broken filter, which §4 S6
  weighs.
- testing: the arms of §7, each staged red against today's code.
- migration: none.
- user docs: S9's sentences in three pages.

## 6. Acceptance criteria

- **AC1** — When a `python -c` probe imports `tools/govkit/upgrade_steps.py` and calls
  `check_contained` over a scratch `git init` target, it prints `refused` for
  `.git/hooks/post-checkout`, `.GIT/config`, `.git./x` and `.git /x`, each naming the path, and `ok`
  for a plain path such as docs/a.md. Over a second target made by
  `git init --separate-git-dir=<target>/gd <target>`, it prints `refused` for `gd/config`, naming
  the git directory. Where `<target>/GIT~1` exists and resolves to `.git`, `GIT~1/hooks/x` prints
  `refused`; the probe prints which.
  Red when: the lexical arm reads segments without case-folding or trailing-dot stripping, or the
  resolved arm is absent, so `gd/config` passes.
  fixture: the short-name row is observable only on a volume with 8.3 names enabled; the probe says
  so rather than counting it.
- **AC2** — When `python3 "tools/govkit/upgrade_steps.py" fixture walk --plant kill-before-stage`
  runs, it exits 0 with no `walk: FAILED` line. Its walk is killed while `fx/s1`'s second witness
  blocks, then run again, and it prints that `git diff --cached --name-only` in the target lists
  `s1.txt` and the step's before-image, s1.before.json under the target's steps directory, and that
  `fx/s1` reads `applied`.
  Red when: move 1 records `applied` without staging, so the index lists neither path.
- **AC3** — When `python3 "tools/govkit/upgrade_steps.py" fixture rollback --plant kill-after-down-stage`
  runs, it exits 0 with no `rollback: FAILED` line. Its rollback is killed after `fx/s1`'s down
  restored, then run again, and it prints that `git diff --cached --name-status` lists `D s1.txt` and a
  `D` line for the step's before-image, and that `fx/s1` reads `rolled-back`.
  Red when: the re-run stages `paths` alone, `[]`, so the index still holds both files.
- **AC4** — When `python3 "tools/govkit/upgrade_steps.py" fixture rollback-update --plant retired-step`
  runs, it exits 0 with no `rollback-update: FAILED` line. Its scratch gov lands `fx/s2` at B and
  names it in a `[[retired]]` row at C, and a target updated to C records `fx/s2` `applied`. The
  plant prints that `update --rollback --to B --write` exits 0, and that
  `update --rollback --to A --write` exits 2 naming `fx/s2`, its `[[retired]]` row and that its down
  is owed.
  Red when: `gone` keeps retired ids, so the rollback to B is refused; or a retired id owing a down
  passes, so the rollback to A runs.
- **AC5** — When `python tools/lib/python_floor.py down 3.12 <scratch>` runs with no `<to>` over a
  scratch `git init` repository, it exits 2 with a stderr line holding
  `<to> is required outside gov's own tree`. When the same verb runs with no `<to>` over a scratch
  gov, a repository holding a copy of `tools/lib/python_floor.py` and `python-floor.txt` under
  `tools/lib/`, from that copy, it exits 0 or 1, never 2.
  Red when: `<to>` still defaults to the target's `HEAD` in an adopter, so the first run exits 2
  naming `names no commit`; or the default is lost on gov's own tree.
- **AC6** — When `python tools/govkit/fixtures/retired_edits.py --plant render-filter-broken` runs,
  it exits 0 with no `MISS` line, its observations reading the verdict
  `render-edited`, the `HELD BACK` line, one render-edited order for the path and the edited bytes
  kept, over a target whose `.gitattributes` maps the render to a required clean filter that fails.
  Red when: `check_render_edited` reads a failed hash as clean, so the verdict is `re-rendered` and
  the edit is overwritten.
- **AC7** — When `python -c "import sys, inspect; sys.path.insert(0, 'tools/govkit'); import upgrade_steps as u; print(list(inspect.signature(u.run_step_walk).parameters))"`
  runs, it prints the five names `gov_root`, `target`, `receipt_path`, `receipt` and `rows`. And
  `git grep -n "run_step_walk(" -- tools/` shows no call passing a sixth argument.
  Red when: the parameter stays, or a caller still passes it and raises `TypeError`.
- **AC8** — When `python3 "tools/govkit/upgrade_steps.py" fixture isolation --plant submodule-config-malformed`
  runs, it exits 1, as at HEAD, with no `isolation: FAILED` line, and its `refused` line holds
  `up: the repositories a step could enter from the target could not be cleared: ` and
  `.git/modules/sub/config or a file it includes does not read`, and not
  `declares what git runs as a program`.
  Red when: `check_target_local_config` still returns the walk's reason as a found key, so the
  executor prefix leads the line.
- **AC9** — When `git grep -n -F -e "is not downed again" -e "this run already has" -e "inside your repository's git directory" -e "left unstaged" -e "since its down is owed" -e "could not be cleared" -e "to run it by hand outside a walk" -- help/upgrade-steps.md`
  runs, it prints one line per phrase, and
  `git grep -n -F -e "is required in an adopter" -- help/python-floor.md` and
  `git grep -n -F -e "cannot be proven unedited" -- help/update-edits.md` each print one line. And
  `git grep -n -F "One recorded \`rolled-back\` whose witness holds is downed again" -- help/upgrade-steps.md`
  and `git grep -n -F "Until the deployer runs steps itself" -- help/upgrade-steps.md` print nothing.
  Red when: a page still documents the unreachable re-down or a deployer that does not walk steps,
  or lacks a sentence §4 "The pages" lists.

## 7. Gates

`govkit selftest` · `govkit refusal join` · `govkit acceptance matrix` · `recall floor arms` · `policy fixtures` · `python resolver (behaviour + inline parity + idiom ban)` · `upgrade-walk` · `step-rows-frozen` · `step-gate` · `docs` · `encoding posture (text IO names its encoding)` · `lexicon naming predicates` · `memory hygiene` · `spec tokens (a spec's own names resolve)`

New arm: tools/govkit/selftest.py · covers AC1 · `[dSP-76]` rows beside the `[dSP-1 S3]` containment check (`tools/govkit/selftest.py:3093-3094`) feeding `check_contained` AC1's paths over scratch targets, their failing case staged by a working copy whose `check_contained` lacks the `.git` refusals · `BRANCH_PIN` by the measured delta
New arm: tools/govkit/selftest.py · covers AC2 AC3 · `check_step_walk` and `check_step_rollback` rows running the plants `kill-before-stage` and `kill-after-down-stage`, tagged `dSP-76`, staged red by today's move 1 and today's `paths`-only staging · none
New arm: tools/govkit/selftest.py · covers AC4 · a `check_step_rollback` row running the `rollback-update` plant `retired-step`, tagged `dSP-76`, staged red by today's `gone` · none
New arm: tools/lib/resolve-python.test.sh · covers AC5 · arm 1e gains the down over `$FT` with no `<to>`, which must exit 2 naming the requirement, and over `$FD` with no `<to>`, which must not exit 2, staged red by today's `HEAD` default · none
New arm: tools/govkit/selftest.py · covers AC6 · a `_rte_cases` row for `render-filter-broken` labelled `[dSafePassage-76]`, staged red by today's `check_render_edited` · none
New arm: tools/govkit/upgrade_steps.py · covers AC8 · the isolation fixture's unkeyed-kind expectation (`:3283-3295`) asserts the full prefix, staged red by today's executor prefix · none

AC7 and AC9 are greps and a signature read; no arm is added for them.

## 8. Open questions

- **F1 — Where does a rollback re-run find the paths of an image the killed down took away (S3)?**
  (a) A journal: the reverse walk writes the image's path list to a file beside the image before the
  down, and the re-run reads and clears it. A new file with its own kill window and cleanup.
  (b) The `down interrupted` record: the paths ride on the receipt row. It widens the row's key set,
  `read_step_states` and `test_step_row`, which the skeptic warned off in M1, and puts adopter paths
  into the receipt.
  (c) The index: the image was staged with its up, so `git show :<image path>` still holds it until
  a staging of its deletion. No new state; where the index holds none, nothing is staged, as today.
  Recommendation: (c). It closes the window with no new file or field, and it reads exactly what
  the first run would have staged. The review's two options are (a) and (b); (c) is offered beside
  them because it needs neither.
  RESOLVED (agent, 2026-10-28, delegated): (c), the paths read from the before-image's index copy.
- **F2 — What does "follow the successor" mean for a retired id in a receipt (S4)?**
  (a) Nothing is read from the successor: a retired id owing no down passes, and one owing a down is
  refused, as an undeclared id is today.
  (b) A retired id owing a down is downed by its successor row's `down` argv.
  (c) The retired id's record is carried onto its successor when the successor has none, so move 1
  judges the successor as recorded.
  Recommendation: (a). No step has retired yet (`tools/govkit/registry.toml:190-195`), a successor's
  down was written for the successor's up rather than the retired one's, and a carry writes a record
  no up made. (a) closes the reported defect, a refusal of a `--to` that owes no down, and fails
  closed on the rest.
  RESOLVED (agent, 2026-10-28, delegated): (a), only a retired id that owes a down is refused, and
  nothing is read from the successor.

## 9. Revision log

- rev-1 · 2026-10-28 · initial draft: the engine-side batch of the closing diff review,
  `memory/builds/dSafePassage/reviews/2026-10-28-review-TOOL-dSafePassage-1-71-closing-diff-round1.md`,
  items M1, M3, M4, M5, M9, L1, L2, L3 and L5 (ids 3, 6, 7, 10, 19, 11, 12, 13 and 21), by
  `memory/builds/dSafePassage/prompts/2026-10-28-prompt-TOOL-dSafePassage-76-1-spec-writer.md`.
  Lines re-read at `83817478f`: the review's `python_floor.py:417-418` is `:411-412` there, its
  `help/python-floor.md:74-75` is `:75-76`, and its `govkit.py:10942` order writer is `:10943`.
- rev-2 · 2026-10-28 · S9 · §4 · AC9 · §8 · S9 gains the schema step's paragraph
  (`help/upgrade-steps.md:184`), whose "Until the deployer runs steps itself" predates
  TOOL-dSafePassage-2's walk, handed off by
  `memory/builds/dSafePassage/prompts/2026-10-28-prompt-TOOL-dSafePassage-78-1-spec-writer.md`, with
  its §4 row and AC9 grep; §8 F1 resolved to (c) and F2 to (a), delegated by the coordinator.
- rev-3 · 2026-10-28 · AC1 · AC2 · AC3 · the scratch-fixture paths the spec-token checker read as
  untracked repo paths are spelled out of backticks; no observation changes.

## 10. Reuse audit

Each item extends the function the review names, so no new seam is built. S1 extends
`check_contained` (`tools/govkit/upgrade_steps.py:1040`) and reuses `build_step_env` and the
`rev-parse --absolute-git-dir` call of `read_target_repositories` (`:1496`). S2 and S3 reuse
`write_step_staged` (`:1922`) and `read_image_paths` (`:1909`). S4 reuses `read_retired` (`:868`)
and `derive_introduced` (`:911`), as `check_gov_first` and `read_steps` call them. S5 moves
`read_down_population`'s gov test into one helper both callers share. S6 changes one return of
`check_render_edited`; its plant extends `run_plant`'s `render-edited` branch
(`tools/govkit/fixtures/retired_edits.py:323-381`). S8 reuses `render_redacted_config`. The plants
extend the `walk`, `rollback` and `rollback-update` families and `FIXTURE_WALK_STEP`'s switches
(`:3346-3396`). `python tools/codebase-map/reuse_lookup.py "refuse a restore path inside the repository git directory and stage a killed step's writes on the re-run"`
ranked `git`, `run`, `write`, `run_git`, `read_steps` and `read_step_states`, name-token matches;
`run_git` and the two step readers are this path's and are reused above, and none is a git-directory
test, so no existing seam fits beyond the functions named. The recall probe ranked
TOOL-dSafePassage-62, -70, -33 and -40 and the review record first; 33 and 40 are the `via` rule S2
leaves as it is.

Recall terms used: `python tools/memory-recall/query.py "how does a rollback treat a before-image path, a retired step id, and a killed walk's unstaged writes" --terms "before-image check_contained rollback retired step id derive_reverse_steps staging write_step_staged kill re-run witness skip"`
