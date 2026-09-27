# TOOL-dPinnedHandoff-2 — a commit naming a unit touches no path its spec froze

**Status:** SPECCED · rev-1 · 2026-09-22 · node d · Tier-2 · base 9b7e2de6 · streams tooling · order 2

<!-- gen:spec-records -->

*No record names this unit.*

<!-- /gen:spec-records -->

## 1. Goal

A NicoCares handoff brief lists the nearby files that are already correct and must be left alone,
each with its reason. Those are the files an agent most wants to "improve". This repo writes the
same instruction as prose: 23 of 191 tracked pass briefs carry a "do not touch" line, and nothing
reads any of them. This unit gives a spec an optional `### Frozen` sub-head in §3. It also adds a
seventh `tools/check-spec-tokens.py` join, which reds when a commit whose subject names the unit's
id changes a frozen path.

## 2. Scope (IN)

- S1. The spec template gains an optional `### Frozen` sub-head inside `## 3. Non-goals (OUT)`, after
  `### Edges`. Each bullet is one backticked path or directory token followed by ` — ` and the reason.
  A directory token needs two or more segments. The single word `none` is legal. The template source
  is `tools/memory-tree/SPEC-TEMPLATE.template.md`, rendered to `memory/TEMPLATE-SPEC.md`. Its
  guidance says what belongs there: the reference implementation being copied, nearby callers that
  are already correct, and the other half of a pair the unit edits. Frozen is not a list of
  everything else. Observed by AC6.
- S2. `extract_frozen` in `tools/check-spec-tokens.py` reads the sub-head body the way
  `extract_files_touched` reads its own. It closes at the next heading of any depth, keeps path-shaped
  and directory-shaped tokens, and returns one-segment roots apart, because they declare nothing.
  Observed by AC1 and AC4.
- S3. The `frozen` join. For a spec carrying the sub-head, it takes the non-merge commits reachable
  from the window's end and not from the spec header's `base` whose SUBJECT names the spec's unit id
  as a word. It tests every path those commits changed against every frozen token with
  `check_guard_trips`. A hit reads `<unit-id> <path> <- <frozen-token> <sha8>`, and a waiver row
  carrying that whole token clears it, as with every other join. Observed by AC1, AC2 and AC3.
- S4. Each frozen token must resolve. It must be a path tracked at `base` or at the window's end, or
  a directory prefix of one. A token resolving to nothing reds as `freezes nothing`, because a stale
  freeze looks like a guard and guards nothing. Observed by AC4.
- S5. A report line prints on every run: specs carrying the sub-head, tokens, commits attributed,
  paths examined. A spec with tokens and zero attributed commits is counted on that line, not red,
  because attribution by subject is the only link and a spec written before its first commit is
  legitimately at zero. Observed by AC5.
- S6. The dossier `memory/map/features/spec-tokens.md` counts this join in its `title` and in its
  join list. Observed by AC7.
- S7. The dry run. Before the join is wired, the paths every unit's attributed commits changed are
  computed over the whole corpus of CLOSED specs, and the count of units whose commits touched a
  path named in their own brief's "do not touch" line is printed. Observed by AC8.
- S8. The arms of AC1 to AC5 are added to the spec-tokens self-test. NOT OBSERVED as a suite,
  because a suite run is not an acceptance observation from `SPEC_DIRECT_CUTOFF` onward; §7 names the
  suite under `New arm:`.

## 3. Non-goals (OUT)

- Commits whose subject does not name the unit id: merges, `fold(<slug>)` commits, and records-only
  commits naming the slug alone. A slug-only subject cannot say which unit it served, and another
  unit of the same build may own the path legitimately. Measured on `dGatedProse`: 22 of its 32
  commits name a unit id.
- Range-spelled subjects beyond their first id. The history holds 20 subjects spelling
  `<id>..<n>`. The word test credits the first id only. `scan_unit_ids` in `tools/runlog/model.py`
  expands ranges, but importing it would couple this gov-only checker to another tool's model.
- The working tree and the index. Only commits are read, so an uncommitted edit is invisible until
  it is committed.
- A build-level freeze in the README. The freeze is per unit, because a sibling may own the path.
- Shipping the join to adopters. `tools/check-spec-tokens.py` is exempt from shipping in
  `tools/govkit/registry.toml`, so an adopter receives the template paragraph only. Whether the
  checker ships is its own decision.
- A pre-commit arm. The bar grades; the tracked pre-commit fast leg is not widened.

### Edges

- **consumes-from** external — the build method's rule that every pass commit names its unit id in
  the subject. Check 23 of `tools/unattended/check-unattended.sh` already joins on it, and its header
  says why. If false: a build's commits turn out not to name unit ids reliably; ship the resolver
  and the report line, and park the verdict half for the owner. Do not attribute by build slug or by
  date window instead: either one charges a sibling unit's legitimate edits to this unit.
- **hands-off** `TOOL-dPinnedHandoff-3` — `derive_closing_commit`, which that unit's close arm reuses
  to find the commit that closed a unit. This unit mints it whichever way F1 resolves; F1 decides
  only whether the frozen join uses it too.
- **hands-off** external — the unattended driver quoting a unit's `### Frozen` list into its pass
  brief, so the brief stops restating it as prose. That is filed as a `memory/backlog/TOOL.md` row at
  landing.

### Frozen

- `tools/unattended/check-unattended.sh` — check 23 is the attribution rule this join reuses as a
  RULE, not as code. Editing it to share a helper would couple a shipped kit to a gov-only checker.
- `tools/runlog/model.py` — `scan_unit_ids` is the tempting import; §3 says why it is not taken.

## 4. Design

### Data model

```text
### Frozen

- `<path or dir/>` — <why this unit must leave it alone>
```

A token is path-shaped, meaning a slash and an extension or an exact tracked path, or
directory-shaped, meaning two or more segments and a trailing slash. `check_path_shaped` and
`check_dir_shaped` already decide both. A one-segment root such as `tools/` declares nothing, exactly
as under `### Files touched (estimate)`. It is returned apart so `--list` can name the skip.

### The window

The unit id comes from the spec's H1, `# <uid> — <title>`. `base` comes from the status header and
is resolved with `git rev-parse --verify <base>^{commit}`. An unresolvable base is skipped and
counted, not red: hygiene's `BASE_RESOLVE_CUTOFF` arm already reds a live spec whose base names
nothing, and a second verdict on the same fact would be two answers to one question.

The window's end is `HEAD` for a live spec. For a terminal spec, `derive_closing_commit` returns the
oldest commit in `base..HEAD` whose diff adds a terminal status line to that spec's file. A late
commit that cites an old unit id therefore never reopens a landed unit. That end is immutable, so a
terminal spec's verdict does not change as history grows. Whether terminal specs are graded at all
is fork F1.

`scan_frozen_commits` runs one `git log --no-merges --format=%x00%H%x09%s --name-only
<base>..<end>` per spec. It keeps the commits whose subject matches `\b<escaped uid>\b`, so
`TOOL-x-1` never matches `TOOL-x-10`. It returns `(sha, path)` pairs. That is one process per graded
spec, which matters because process creation is this node's suite cost.

### Inventory

| identifier | kind | cell |
|---|---|---|
| `FROZEN_HEAD` | module constant, the sub-head regex | none; constants are not graded |
| `extract_frozen` | function | `py.function`, checked OK by `tools/lexicon/lexicon.py --suggest` |
| `scan_frozen_commits` | function | `py.function`, checked OK |
| `derive_closing_commit` | function | `py.function`, checked OK |

### Migration

None. No spec carries the sub-head at `9b7e2de6`, so the join's population is empty on landing and
the join is opt-in by construction. No cutoff key is needed.

### Rollout

The join lands live. Its first graded spec is the first one written with the sub-head after landing.
This spec's own `### Frozen` is the dogfood: it becomes graded the moment the join exists, over
this unit's own commits.

### Files touched (estimate)

| path | change |
|---|---|
| `tools/check-spec-tokens.py` | the three functions, the join, the report line, the docstring's join rows and its cannot-see list |
| `tools/check-spec-tokens.test.sh` | the arms of AC1 to AC5, each staged red first, and the floor raise |
| `tools/memory-tree/SPEC-TEMPLATE.template.md` | the `### Frozen` rule and its place in the skeleton |
| `memory/TEMPLATE-SPEC.md` | REGENERATED from the template; never hand-edited |
| `memory/map/features/spec-tokens.md` | the join count in `title`, one join row, one Gaps bullet naming the cannot-see list |
| `memory/backlog/TOOL.md` | at landing, the hand-off row §3 Edges names |

### Alternatives rejected

- **Compare the Files-touched estimate against the diff instead.** An estimate is written to be
  exceeded, and redding every file a unit touched but did not predict would make the join fire on
  ordinary work. A freeze is written to be binding, so its breach is always a finding.
- **Attribute by build slug.** A fold commit legitimately edits files that belong to several units,
  and a sibling unit may own a path this unit froze.
- **Grade the pass brief's prose.** 23 briefs carry the line in free prose with no fixed shape. The
  measured sentences disagree on verb, object and scope, and a spec sub-head is where the brief
  should have read it from.

## 5. Production-readiness checklist

- security: N/A — reads tracked text and git history; no write path, no egress.
- perf / scale: one `git log` per spec carrying the sub-head. The population is new specs only,
  which bounds the cost by authoring, not by corpus size.
- error / empty / loading states: no sub-head means not graded. `none` means graded and empty. An
  unresolvable base is skipped and counted. Zero attributed commits is counted. Each of these has a
  different remedy, and the report line keeps them apart.
- observability: the report line prints every run, and `--list` names each hit and each skipped
  root.
- risks: a commit that spells the unit id in its subject for an unrelated reason is charged to the
  unit. The window's end bounds that for terminal specs, and a waiver row clears a false one.
- testing: every self-test arm is observed red on a staged break before it is kept.
- migration: none; the population starts empty.
- user docs: the rendered template is the doc. This repo has no `help/`.

## 6. Acceptance criteria

- **AC1** — When `tools/check-spec-tokens.py` runs over a scratch repository whose live spec freezes
  one file, and whose later commit subject names the spec's unit id and edits that file, it prints a
  hit naming the unit id, the file and that commit's sha8.
  Red when: no hit is printed, or the hit names a different commit.
  fixture: a `mktemp -d` repository the self-test builds, with the spec, a base commit and the
  offending commit. The fixture paths are not backticked here, because the paths join would read
  them against this tree.
- **AC2** — When the offending commit's subject instead names `TOOL-x-10` for a spec whose id is
  `TOOL-x-1`, or names only the build slug, or the commit is a merge, `tools/check-spec-tokens.py`
  prints no hit.
  Red when: any of the three is charged to the unit.
- **AC3** — When the spec freezes a two-segment directory and the commit edits a file under it,
  `tools/check-spec-tokens.py` prints a hit. When the spec freezes a one-segment root alone, `--list`
  names the root as declaring nothing, and no hit is printed.
  Red when: the directory freeze misses the file, or the one-segment root is enforced.
- **AC4** — When a frozen token names a path tracked neither at `base` nor at the window's end,
  `tools/check-spec-tokens.py` prints `freezes nothing` beside the token.
  Red when: the dead token passes silently.
- **AC5** — When the join runs over a tree whose only spec with the sub-head has no attributed
  commit, `tools/check-spec-tokens.py` prints the report line with a commits-attributed count of zero
  and exits 0.
  Red when: the line is absent, or the zero reds.
  figure: DERIVED — every count on the line comes from the run.
- **AC6** — When `memory/TEMPLATE-SPEC.md` is re-rendered from its template, it carries a
  `### Frozen` rule under `## 3. Non-goals` in the skeleton and in the rules above it.
  Red when: the rendered file lacks `### Frozen`, or a fresh render differs from the committed copy.
- **AC7** — When `memory/map/features/spec-tokens.md` is read after landing, its `title` counts seven
  joins and names the frozen join.
  Red when: the title still counts six.
- **AC8** — When the dry run computes, for every CLOSED unit whose pass brief under
  `memory/builds/` carries a "do not touch" line, the paths its attributed commits changed, it prints
  how many of those units touched a path their brief named. The output is recorded in this build
  folder before the join is wired.
  Red when: the run examines zero briefs, which would mean the brief match found nothing.
  cost: minutes; one `git log` per unit.
  figure: DERIVED. The 23 briefs are PINNED at `9b7e2de6` on 2026-09-22 as a sanity bound.

## 7. Gates

`spec tokens (a spec's own names resolve)` · `spec-tokens self-test` · `kit/dogfood doc parity` · `codebase-map coverage + freshness` · `recall floor` · `recall floor arms` · `testsuite counts (every bar self-test prints one)` · `memory hygiene`

`kit/dogfood doc parity` is armed by the template edit. `recall floor` and `recall floor arms` carry
the guard `memory/`. `codebase-map coverage + freshness` grades the dossier edit. `spec-tokens
self-test` is held by default; the post-build run reaches it.

New arm: `tools/check-spec-tokens.test.sh` · AC1's offending commit, AC2's three non-attributed
shapes, AC3's directory and root tokens, AC4's dead token, AC5's zero-attribution tree · the suite's
floor moves by the arms added

## 8. Open questions

- **F1 — are terminal specs graded, over a window that ends at the closing commit?** (a) Yes: the
  window ends where the status first went terminal, so the verdict is immutable and a violation made
  in the same commit that closes the unit is still seen. (b) No: live specs only, matching every
  other join, which leaves a landed record ungraded. Under (b), a unit's last commit can flip it to
  CLOSED and touch a frozen path, and the bar at that HEAD never sees it. Recommendation: (a). A
  hit on a terminal spec is cleared by a waiver row, never by rewriting the landed record. That keeps
  the corpus rule that a landed record is frozen.

## 9. Revision log

- rev-1 · 2026-09-22 · initial draft, from the comparison of the three NicoCares handoff briefs with
  this template; the build README states the source.

## 10. Reuse audit

`python tools/codebase-map/reuse_lookup.py "compare the paths a unit's commits touched against a
declared list of paths"` returned no seam this unit can extend. The closest candidates are
`attribute_paths` and `drop_touched_exemptions` in `tools/codebase-map/map_lib.py`, which attribute
paths to map features, not to units. Then comes `build_unit_id_re` in `tools/runlog/model.py`, whose
word-bounded id pattern this unit copies as a pattern, not an import. The seams this unit extends
are in the checker it joins: `extract_files_touched`, `check_path_shaped`, `check_dir_shaped` and
`check_guard_trips` (`tools/check-spec-tokens.py:322-384`), plus the waiver and report plumbing
every join shares. The attribution rule is check 23's, in `tools/unattended/check-unattended.sh`,
reused as a rule.

Recall terms used: `python tools/memory-recall/query.py "was a halt rule on external edges, a
do-not-touch path list checked against the diff, or a runnable grep invariant as acceptance
considered before, and what decided the Edges block and the acceptance witness shape" --terms "Edges
consumes-from external precondition witness Red-when Files-touched guard join invariant grep frozen
shape-only"` — 40 hits. None proposes a freeze. The nearest is the Files-touched guards join of
`TOOL-aBlindedTrial-8`, whose path-shape rules this unit reuses.
