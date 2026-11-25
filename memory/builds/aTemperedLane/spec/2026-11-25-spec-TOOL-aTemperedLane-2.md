# TOOL-aTemperedLane-2 — limit L2 reads the guarded list at the commit's first parent

**Status:** CLOSED · rev-1 · 2026-11-25 · node a · Tier-2 · base 3d6c1702 · streams tooling · order 2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-11-25-build-TOOL-aTemperedLane-1-agent-ledger.md](../build/2026-11-25-build-TOOL-aTemperedLane-1-agent-ledger.md) | journal | TOOL-aTemperedLane-1 TOOL-aTemperedLane-3 |
| [2026-11-25-build-TOOL-aTemperedLane-2-1-acceptance-ledger.md](../build/2026-11-25-build-TOOL-aTemperedLane-2-1-acceptance-ledger.md) | journal | — |
| [2026-11-25-prompt-TOOL-aTemperedLane-1-brief.md](../prompts/2026-11-25-prompt-TOOL-aTemperedLane-1-brief.md) | research | TOOL-aTemperedLane-1 |
| [2026-11-25-review-TOOL-aTemperedLane-1-closing-diff-review-round1.md](../reviews/2026-11-25-review-TOOL-aTemperedLane-1-closing-diff-review-round1.md) | diff-review | TOOL-aTemperedLane-1 |

<!-- /gen:spec-records -->

## 1. Goal

Limit L2 of the Red-fix lane grades every fix commit against the guarded list the working tree holds
today, so a commit made before a line joined the list reds, and a commit that removes a line and
edits that path in itself passes. This unit reads the list in the tree of the commit's first parent,
which is the list that was in force when the commit was made.

## 2. Scope (IN)

- **S1** — In `routed_commits.py#check_red_fix_limits`, L2 grades each fix commit against the policy
  kit's `guarded-paths.txt` in the tree of that commit's first parent, read at the path the list has
  in the working tree. A path equal to a line of it is the finding, worded as today. Observed by AC1
  to AC4 and AC9.
- **S2** — The two fallbacks, in order. Where the first parent holds no list, or the commit has no
  parent, the working tree's list is read, as today. Where the working tree's list does not resolve,
  every path under `.governance/` is refused, as today. Observed by AC5 and AC6.
- **S3** — The parent lists are read in one batched git call per population, pinned and counted as
  every other git call of the leg is. No call is made where the population holds no fix commit,
  where no fix commit has a parent, or where the list has no path inside the repository. The
  read is `read_blob_batch`, which TOOL-aTemperedLane-1 adds. Observed by AC7 and AC8.
- **S4** — The module docstring, `help/red-fix-lane.md` and the `routed_commits.py` row of
  `tools/memory-tree/README.md` state the new L2 rule, what it no longer checks, and the git-call
  figure. Observed by AC10.

## 3. Non-goals (OUT)

- Any exemption for a file under `.claude/agents/`, and any read of the roles renderer. The owner's
  answer of 2026-11-25 replaced that exemption with this rule.
- A line added to or removed from `tools/policy/guarded-paths.txt`.
- L1, L3 and L4, the waiver's reach, the lane's switch, the write gate, the record join and the
  policy kit's own commit-time guard.
- Refusing an edit of the guarded list itself. No list line names the list today, and none is added.
- The wording of an L2 finding, and the `red-fix limits` summary line.
- A policy key, a conf key or a flag for the rule.
- `.governance/instructions.toml`, which is owner-guarded, and the kit version, which the lander's
  mint moves.

### Edges

- **consumes-from** `TOOL-aTemperedLane-1` — `read_blob_batch`, the batched blob read the parent's
  list is read through, and the limits pass's git-call figure, which this read moves. Without that
  function this unit would frame a batch stream of its own.

## 4. Design

### Evidence

- `routed_commits.py#read_guarded_paths` finds the policy kit by `backlog.py#resolve_kit_dir` from
  `KIT` and reads the list's working bytes. It returns None where the kit or the file does not
  resolve.
- `routed_commits.py#check_red_fix_limits` fills the caller's one-slot cache from it and tests each
  path of each commit by equality against that one list, or by the `.governance/` prefix on None.
- Each record of `routed_commits.py#read_routed_commits` carries `parents`, so the first parent
  costs no git call. A merge, which only the verb grades, is read against its first parent already.
- `routed_commits.py#resolve_leg_manifest` is the precedent for turning a sibling kit's file into a
  path relative to the graded repository, and for answering the empty string where the file is
  outside it.
- The spec of TOOL-aTemperedLane-1 gives `read_blob_batch(repo, names)`: one entry per name, the
  body's bytes or None where the answer is not a blob, through the module's pinned, counted
  `run_git`, and a Refusal on a stream that ends early.
- `tools/policy/guard.py#read_guarded_paths` reads the list at HEAD, which at commit time is the
  first parent of the commit being made. This unit gives the history grader the same list.
- `tools/policy/guarded-paths.txt@16afba27:5` opens its four lines, all under `.governance/`. Main
  guards no agent file, and `be10c468` is inside all four limits on main today.
- The run branch's list gained `.claude/agents/gov-skeptic.md` in `9e14a5ca4`, committed
  2026-11-22 18:49. `be10c468` was committed 08:04 that day, and its first parent's list holds no
  agent line.
- Measured 2026-11-25, PINNED: of 259 non-merge fix commits reachable from HEAD and 255 from
  `branch/unattended-dboundroles-62c3df`, every first parent holds a list, and neither the
  working-tree reading nor the parent reading finds one under L2 with main's list on disk. So no
  landed commit changes verdict and no waived sha turns stale.

### The rule

| First parent | Working tree's list | L2 refuses |
|---|---|---|
| holds a list | resolves inside the repository | a path equal to a line of the parent's list |
| holds no list, or there is no parent | resolves | a path equal to a line of the working tree's list |
| not read | resolves outside the repository | a path equal to a line of the working tree's list |
| not read | does not resolve | every path under `.governance/` |

A list that is present and holds no line guards nothing, as it does today. "Holds a list" means the
tree answers a blob that decodes as UTF-8 at that path.

### Mechanism

1. The line filter at the end of `read_guarded_paths` becomes `parse_guarded_paths(text)`, so both
   readings drop the same comments and blank lines.
2. `resolve_guarded_path(repo)` answers the list's path relative to `repo`, by the same
   `resolve_kit_dir` call, and the empty string where it does not resolve or lies outside `repo`.
   Both sides are resolved before the compare, as `resolve_leg_manifest` does.
3. `read_parent_lists(repo, fixes)` answers `{sha: lines}`, holding only the commits whose first
   parent holds a list. It asks `read_blob_batch` for one `<first parent>:<path>` name per commit
   that has a parent, and makes no call where there is none. A None entry, and a body that is not
   UTF-8, is no list.
4. `check_red_fix_limits` reads the parent lists once, beside its one log. For each commit its list
   is that commit's entry, or the cached working list where it has none.

`read_blob_batch` answers one entry per name, so a missing one cannot shift its neighbour's. The
cache slot and the signature of `check_red_fix_limits` stay, so neither caller changes. No code from a
graded commit runs: the parent's list is read as text and compared by equality.

### The git-call figure

A population holding no fix commit costs no call. Any other costs the one log, plus one call where a
fix commit has a parent and the list lies inside the repository, plus the spec blob read of
TOOL-aTemperedLane-1 where it is owed. So the pass makes three calls at most, whatever the count of
fix commits. The docstring and the README row state that figure. A self-test fixture whose `KIT` lies
outside it makes no list read, so the counts TOOL-aTemperedLane-1 pins over its fixture stand.

### What L2 no longer checks

- A path the list gained after the commit, or in it. A commit made on an older parent is graded by
  that parent's list, whenever it lands.
- A path an earlier commit took off the list. The shortening commit is graded by the longer list,
  and the commit after it by the shorter one. An edit of the list alone is still no L2 finding, since
  the list does not name itself.
- A list that has moved. It is looked for at the working tree's path, and a parent holding none
  there is graded by the working tree's list, which the graded run controls.
- The list's file mode. A symbolic link at the list's path is read as its target text.

What it gains: a line the fix commit itself removes, and a line any later commit removes, are still
in force for that fix commit.

### Inventory

| Minted | Where | Graded by |
|---|---|---|
| function `parse_guarded_paths` | `routed_commits.py` | `py.function`, the `lexicon naming predicates` leg |
| function `resolve_guarded_path` | `routed_commits.py` | `py.function`, the `lexicon naming predicates` leg |
| function `read_parent_lists` | `routed_commits.py` | `py.function`, the `lexicon naming predicates` leg |

### The fixture

One scratch repository from `routed_commits.py#build_fixture`, with the module's `KIT` stubbed to
`kits/memory-tree` inside it, as the `lanebeside` arm does. The list is at
`kits/policy/guarded-paths.txt`. The disk copy, written by hand, names `src/a.txt` alone. Every fix
commit names `TOOL-tFix-1` and carries `Red-fix: leg one`, so the routing half is green.

| Commit | Holds | L2 |
|---|---|---|
| g1, plain, before the cutoff | `src/a.txt`, `src/b.txt`, the agent file, the policy file, the unit's spec, no list | not graded |
| g2, fix | edits `src/a.txt` | finding, by the working list: the parent holds none |
| g3, plain | adds the list, naming `src/b.txt` and `.claude/agents/gov-x.md` | not graded |
| g4, fix | edits `src/a.txt` | none: only the working list names it |
| g5, fix | edits `src/b.txt` | finding: the working list no longer names it |
| g6, fix | hand edit of `.claude/agents/gov-x.md` | finding |
| g7, fix | removes the `src/b.txt` line and edits `src/b.txt` | finding |
| g8, fix | edits `src/b.txt` | none: the parent's list no longer names it |
| g9, fix | adds a `src/a.txt` line to the list and edits `src/a.txt` | none |
| g10, fix | edits `.governance/policy.toml` | none while the disk list is there, a finding once it is removed |

### Files touched (estimate)

- `tools/memory-tree/routed_commits.py`
- `tools/memory-tree/README.md`
- `help/red-fix-lane.md`

### Alternatives rejected

- **An exemption for a rendered agent file that moves with its source.** Where the list names the
  agent files it lets a fix commit change what an agent is told, so the owner chose this rule.
- **The union of the parent's list and the working tree's.** It keeps refusing `be10c468`, whose
  path only the later list names.
- **The list in the commit's own tree.** A commit that removes a line would be graded by the list it
  shortened, which is the gap this unit closes.
- **`tree_lib.read_blobs_at`.** Its runner does not pin replace refs, so a `git replace` ref in the
  clone would substitute the parent's list, and the call would be outside the spawn count.
- **One call for both reads.** It saves one process per run and ties L2's read to L3's, where each
  unit's read is now made only when its own limit needs it.

## 5. Production-readiness checklist

- security — the rule moves which list is in force and loosens L2 only as §4, "What L2 no longer
  checks", states. Deny by default stands where no list resolves. The read is pinned against
  replace refs, and no code from a graded commit runs.
- perf / scale — at most one git call more per population holding a fix commit. The read holds one
  copy of a short text file per fix commit, 259 of them in this tree by the measurement in §4.
- error / empty / loading states — an absent, non-blob or undecodable parent list takes the working
  list. A failed git call or a torn stream is the leg's exit 2.
- observability — the finding line and the summary line are unchanged.
- risks — a landed commit whose parent's list named a path that today's does not would red in WHOLE
  from this commit on. §4 measured none.
- testing — the fixture above, by a scratch probe in the pass and by the self-test arms at the close.
- migration — none. An adopter whose parent trees hold no list reads the working list as today.
- user docs — `help/red-fix-lane.md`. `help/README.md` counts the limits and describes none, so it
  does not move.

## 6. Acceptance criteria

- **AC1** — When `python tools/memory-tree/routed_commits.py --red-fix-limits be10c468` runs, it
  exits 0; and when a scratch probe calls `main` with that same argument and `read_guarded_paths`
  replaced by the lines of the run branch's list, read from git, it exits 0 too.
  Red when: L2 still reads the working tree's list, so the second form names `L2` and
  `.claude/agents/gov-skeptic.md`.
  fixture: the run branch's objects, which this clone holds; the probe only reads them.
- **AC2** — When `--red-fix-limits` runs in the fixture for g5 and for g6, each exits 1 naming `L2`
  and the one path.
  Red when: the working list alone is read, so a line it dropped guards nothing, or an agent file
  named by the parent's list is exempt.
- **AC3** — When `--red-fix-limits` runs in the fixture for g4, g8 and g9, each exits 0.
  Red when: the working list is read beside the parent's, or the commit's own tree is read in its
  place.
- **AC4** — When `--red-fix-limits` runs in the fixture for g7, it exits 1 naming `L2` and
  the path whose line it removed.
  Red when: the list is read at the commit, where the line is already gone.
- **AC5** — When `--red-fix-limits` runs in the fixture for g2, and in a second fixture for a root
  commit that carries the trailer and adds the path the disk list names, each exits 1
  with an `L2` line naming that path.
  Red when: a parent with no list, or no parent, reads as an empty list.
- **AC6** — When `--red-fix-limits` runs for g10 it exits 0, and after the fixture's disk copy of
  `guarded-paths.txt` is removed it exits 1 naming `L2` and `.governance/policy.toml`.
  Red when: an unresolved list turns L2 off.
- **AC7** — When `check_routed_commits` grades the fixture's history whole, the `L2` lines name
  exactly g2, g5, g6 and g7; and `GIT_SPAWNS` rises over `check_red_fix_limits` by the same amount
  for one fix commit as for 30, by one more than with `KIT` outside the repository, and by 0 for no
  fix commit.
  Red when: an absent answer shifts the next commit's list, or the read makes a call per commit.
  figure: one and 0 are DERIVED from readings of the counter in one probe.
- **AC8** — When the list blob at g5's first parent is replaced through `git replace` by a blob with
  no lines, `--red-fix-limits` for g5 still exits 1 naming `L2`.
  Red when: the read goes through a runner that follows replace refs, as `read_blobs_at` does.
- **AC9** — When a scratch probe passes every non-merge fix commit reachable from HEAD to
  `check_red_fix_limits`, the `L2` findings count 0 over a population that is not empty.
  Red when: a landed commit's parent list names a path it edited, or the probe graded nothing.
  figure: 0 is PINNED, measured 2026-11-25; the probe re-derives it.
- **AC10** — When `grep -n "first parent" help/red-fix-lane.md` runs, the L2 row of the limits table
  and a bullet of "What it does not check" answer; and when `grep -c "itself shortened"` runs over
  that page and over `tools/memory-tree/routed_commits.py`, each prints 0.
  Red when: the page or the docstring still says L2 reads the working tree's list, or still lists a
  self-shortened list as unchecked.

## 7. Gates

`routed commits name a specced unit` · `routed-commits selftest` · `policy fixtures` · `lexicon naming predicates` · `python reads (a name never bound, an import outside its guard)` · `docs` · `memory hygiene` · `spec tokens (a spec's own names resolve)`

The close runs these once. `routed-commits selftest` is in the held tier, so its arms are observed at
the close and the pass uses a scratch probe over the same fixture.

New arm: tools/memory-tree/routed_commits.py · covers AC2 AC3 AC4 · the fixture's g4 to g9, staged red by reading the working list, then the commit's own tree, in place of the parent's · none
New arm: tools/memory-tree/routed_commits.py · covers AC5 AC6 · g2, a root fix commit and g10 with the disk list removed, staged red by reading an absent parent list as empty · none
New arm: tools/memory-tree/routed_commits.py · covers AC7 · the whole-history run and the spawn count over one and 30 fix commits, staged red by a read per commit and by pairing answers with commits by position · none
New arm: tools/memory-tree/routed_commits.py · covers AC8 · a replace ref over the parent's list, staged red by dropping the pinned runner · none

## 8. Open questions

none

## 9. Revision log

- rev-1 · 2026-11-25 · initial draft.

## 10. Reuse audit

`python tools/codebase-map/reuse_lookup.py "grade a Red-fix commit against the guarded paths list as
its parent held it"` ranked `read_routed_commits` of `tools/memory-tree/routed_commits.py`, whose
records already carry the parents. The seam is `check_red_fix_limits` of that file, with
`read_blob_batch` of TOOL-aTemperedLane-1 for the read and `resolve_leg_manifest` as the pattern for
the relative path. Reading the code found one disagreement: `tree_lib.py#read_blobs_at` calls itself
the one `<rev>:<path>` reader, and its runner does not pin replace refs, so it is not used here.
Records: TOOL-aNimbleMend-10 set the four limits and listed a self-shortened list as unchecked;
TOOL-dGroundRules-6 reads the list at HEAD.

Recall terms used: `python tools/memory-recall/query.py "why does L2 of the red-fix lane limits read
the guarded paths list as the working tree holds it" --terms "red-fix lane limits guarded-paths
routed_commits L2 policy guard HEAD first parent working-tree cat-file waiver"`
