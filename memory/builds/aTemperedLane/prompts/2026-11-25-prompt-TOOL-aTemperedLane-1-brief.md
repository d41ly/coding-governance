# Brief — aTemperedLane: the Red-fix lane's L3 reads past a generated region, and its L2 reads the list at the commit's parent

**Serves:** research TOOL-aTemperedLane-1 TOOL-aTemperedLane-2
**Caused-by:** TOOL-aTemperedLane-1

## The prompt

> Background (from the session that started this one):
> The unattended build run dBoundRoles has finished its units, and its closing session reports that the push boundary refuses nine pushed `Red-fix:` commits: eight for a one-line record row a generator wrote into a spec (L3), one for a rendered agent file that moved with its source (L2). The RANGE half of `routed_commits.py` reads no waiver. The owner was offered: fix the gate on main first, hold the run, change the gate inside the run, or rewrite the branch. The owner answered "Fix gate on main". Changing it inside the run was set aside because a bar whose diff edited its own grader blocks every red; rewriting because built work is never rewritten in place and records cite the shas. After this lands, the run merges main once more and lands. The cases are real but the exemptions loosen a merge gate, so keep them as narrow as the cases and say what the gate no longer checks. The asking session read the diff of `dbc7bb6a` and `be10c468` only; for the other seven it saw one added spec line by numstat and nothing more.
>
> Task:
> In coding-governance, teach the Red-fix lane limits in `tools/memory-tree/routed_commits.py` two narrow exemptions, and land them on main. Attended build: read `AGENTS.md`, run `/session-kickoff`, then `/build`; fetch and base on `origin/main`. Work only in your own worktree, never in the primary tree.
>
> The two exemptions, and nothing wider:
> 1. L3 (spec edit): a change to a spec file that is confined to a generated region (such as `gen:spec-records`) is not a spec edit. Decide it by comparing the file at the commit and at its parent with the generated regions blanked: everything outside must be byte-identical and the region markers unchanged. A moved, added or removed marker, a new file, a delete or a rename stays a finding.
> 2. L2 (guarded file): a rendered agent file under `.claude/agents/` that moves in the same commit as its source under `tools/roles/agents/` is not a guarded edit, only when the rendered bytes are what the renderer emits from that commit's tree, or the closest check the leg can afford. A hand edit of the rendered file stays a finding.
>
> STOP and ask the owner before landing if the second exemption cannot be held that tight, or if it would in effect let a Red-fix commit change what an agent is told without L2 noticing: bring narrower options with it. The owner was told that it loosens a merge gate, not that detail.
>
> The commits it must admit, all on the pushed branch `branch/unattended-dboundroles-62c3df`: `dbc7bb6a 3fa017d5 918ffb5b 69a05280 b9a6d520 0b026d5c e6196f84 f40a0e58` (L3, each adds one record row in a spec) and `be10c468` (L2, `.claude/agents/gov-skeptic.md` with its source). Verify each against the new predicate by `python tools/memory-tree/routed_commits.py --red-fix-limits <sha>`; read them from git, and never write to that branch or its worktree `C:/projects/coding-governance/.claude/worktrees/unattended-dboundroles-62c3df`, which another session is driving. If any is still refused for another reason, report it and do not widen the predicate.
>
> Done means: spec first, each new self-test arm seen red on its break and green after, including arms for a hand edit outside a region, a marker tamper and a hand-edited rendered file; one adversarial Tier-2 review; the docstring and any doc naming L2/L3 updated; the bar green; landed by `bash tools/push-main.sh` (the owner's "Fix gate on main" is the ask for this landing, for these two exemptions only). Never `--no-verify`, never set `GATE_SELFTESTS=1` without asking the owner. Commits end with `Co-Authored-By: Claude Opus 5 <noreply@anthropic.com>`. Report the landed sha, the nine verdicts and any red as it is.

## The brief

### Goal
Two changes to the Red-fix lane's limits in `tools/memory-tree/routed_commits.py`: L3 stops
reading a change confined to a spec's `gen:spec-records` region as a spec edit, and L2 reads the
guarded list as it stood at the commit's first parent.

### Items
1. `TOOL-aTemperedLane-1`, L3. A spec path is exempt when its status in the commit is a plain
   modification with the mode unchanged, each side holds exactly one
   `<!-- gen:spec-records -->` … `<!-- /gen:spec-records -->` pair as whole marker lines in that
   order, and every byte outside the region, the two marker lines included, is identical. A moved,
   added or removed marker, a new file, a delete, a rename and a root commit stay findings. No
   other generated region is exempt: the cases are `gen:spec-records` alone.
2. `TOOL-aTemperedLane-2`, L2. The guarded list is the policy kit's `guarded-paths.txt` in the tree
   of the commit's first parent, read at the path that list has in the working tree. Where the
   parent holds no list, the working tree's list is read as today, and where that does not resolve
   either, every path under `.governance/` is refused as today. There is no agent-file exemption:
   the task's exemption 2 is replaced by this rule on the owner's answer below.
3. The docstring, `help/red-fix-lane.md`, `help/README.md` where it names a changed limit, and the
   `routed_commits.py` row of `tools/memory-tree/README.md` say the new rules and what each limit
   no longer checks.

### Acceptance
- Each of `dbc7bb6a 3fa017d5 918ffb5b 69a05280 b9a6d520 0b026d5c e6196f84 f40a0e58 be10c468` exits 0
  under `python tools/memory-tree/routed_commits.py --red-fix-limits <sha>`, and `be10c468` also
  with the run branch's guarded list as the working tree's list.
- New self-test arms, each seen red on its staged break: a records row inside the region admitted;
  a hand edit outside the region refused; a marker moved, removed, duplicated or altered refused; a
  new spec, a deleted spec and a mode change refused; a path the parent's list names refused though
  the working list no longer names it; a path only the working list names admitted; a commit that
  removes a line of the list and edits that path in itself refused; a hand-edited rendered agent
  file refused where the parent's list names it.
- The git spawn count stays constant whatever the fix-commit count, and zero where no fix commit
  exists, and the arms and the docstring say the new figure.

### Gates
`routed commits name a specced unit` · `routed-commits selftest` · `policy fixtures` ·
`lexicon naming predicates` · `python reads (a name never bound, an import outside its guard)` ·
`docs` · `memory hygiene` · `spec tokens (a spec's own names resolve)`

### Non-goals
- Any exemption for a file under `.claude/agents/`, and any other generated region.
- L1, L4, the waiver's reach, the lane's switch, the write gate and the record join.
- `.governance/instructions.toml`: its pocket naming L3 is owner-guarded, so it is reported.
- A kit version bump: the lander's mint moves it.

### Limitations
- The owner took the L2 rule with one gap named, and every statement of the rule (spec, docstring,
  help page, kit README row) states it: a path unlisted in one commit, fixed in the next and
  relisted later passes.
- Work only in this worktree; never write to `branch/unattended-dboundroles-62c3df`.
- `routed_commits.py` runs no repository code from a graded commit and stays stdlib and git.
- The predicate is not widened to admit a commit that is refused for another reason.
- Never `--no-verify`, never `GATE_SELFTESTS=1` without the owner.

### Reuse
Seam: `routed_commits.py#check_red_fix_limits` and its one `git log --raw`, whose raw lines carry
both blob ids under `--no-abbrev`; the batched `cat-file --batch` read in `check_routed_commits`;
`gen_build_index.py#SPEC_RECORDS_OPEN`, `#SPEC_RECORDS_CLOSE` and the `check_marker_line` contract
its own `apply_region` uses; the self-test's `limits` fixture. Records: TOOL-aNimbleMend-10 set the
four limits; TOOL-dGroundRules-6 reads the list at HEAD, which is the parent at commit time.

## Drawn from the session

> Main does not guard agent files: `be10c468` is inside all four limits on main today. The agent
> lines of `tools/policy/guarded-paths.txt` exist only on the run's branch, added by `9e14a5ca4`.
> `be10c468` was committed 2026-11-22 08:04. `9e14a5ca4` is 18:49 the same day and descends from it.
> As worded, exemption 2 lets a Red-fix commit change what an agent is told.
> Measured under A: main 261 Red-fix commits, 0 L2 findings; branch 257, 0.
— agent, 2026-11-25, `redfix-lane-l2-question.md` in the session family's notes folder

> A: L2 reads the guarded list as it stood at the commit's first parent; working-tree list where the
> parent has none. What A stops checking: a path the list gained after the commit, or in it.
— agent, 2026-11-25, the option the owner chose

> Owner's answer on which L2 rule lands: "A, list at parent (Recommended)". As I put it to the owner:
> "Grade each commit by the guarded list as it stood at its first parent. No agent-file exemption.
> Gap: a path unlisted in one commit, fixed in the next and relisted later would pass." The owner
> took it with that gap named; state the gap where the rule is stated.
— agent, 2026-11-25, the starting session

## Owner confirmation

Asked: Which L2 rule should land?
Answer: A: list at parent
