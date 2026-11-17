# TOOL-dDeclaredLoop-115 — the push arm reads the policy file as added only where no parent holds it, so a merge whose first parent lacks it is graded

**Status:** CLOSED · rev-1 · 2026-11-17 · node a · Tier-2 · base a4256373 · streams tooling · order 52

**Derived:** TOOL-dDeclaredLoop-44

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-24-build-TOOL-dDeclaredLoop-1-agent-ledger.md](../build/2026-10-24-build-TOOL-dDeclaredLoop-1-agent-ledger.md) | journal | TOOL-dDeclaredLoop-1 TOOL-dDeclaredLoop-2 TOOL-dDeclaredLoop-3 TOOL-dDeclaredLoop-4 TOOL-dDeclaredLoop-5 TOOL-dDeclaredLoop-6 TOOL-dDeclaredLoop-7 TOOL-dDeclaredLoop-8 TOOL-dDeclaredLoop-9 TOOL-dDeclaredLoop-10 TOOL-dDeclaredLoop-11 TOOL-dDeclaredLoop-12 TOOL-dDeclaredLoop-13 TOOL-dDeclaredLoop-14 TOOL-dDeclaredLoop-15 TOOL-dDeclaredLoop-16 TOOL-dDeclaredLoop-17 TOOL-dDeclaredLoop-18 TOOL-dDeclaredLoop-19 TOOL-dDeclaredLoop-20 TOOL-dDeclaredLoop-21 TOOL-dDeclaredLoop-22 TOOL-dDeclaredLoop-23 TOOL-dDeclaredLoop-24 TOOL-dDeclaredLoop-25 TOOL-dDeclaredLoop-26 TOOL-dDeclaredLoop-27 TOOL-dDeclaredLoop-28 TOOL-dDeclaredLoop-29 TOOL-dDeclaredLoop-30 TOOL-dDeclaredLoop-31 TOOL-dDeclaredLoop-32 TOOL-dDeclaredLoop-33 TOOL-dDeclaredLoop-34 TOOL-dDeclaredLoop-36 TOOL-dDeclaredLoop-37 TOOL-dDeclaredLoop-38 TOOL-dDeclaredLoop-39 TOOL-dDeclaredLoop-40 TOOL-dDeclaredLoop-41 TOOL-dDeclaredLoop-42 TOOL-dDeclaredLoop-43 TOOL-dDeclaredLoop-44 TOOL-dDeclaredLoop-45 TOOL-dDeclaredLoop-46 TOOL-dDeclaredLoop-47 TOOL-dDeclaredLoop-48 TOOL-dDeclaredLoop-49 TOOL-dDeclaredLoop-50 TOOL-dDeclaredLoop-51 TOOL-dDeclaredLoop-52 TOOL-dDeclaredLoop-53 TOOL-dDeclaredLoop-54 TOOL-dDeclaredLoop-55 TOOL-dDeclaredLoop-56 TOOL-dDeclaredLoop-57 TOOL-dDeclaredLoop-58 TOOL-dDeclaredLoop-59 TOOL-dDeclaredLoop-60 TOOL-dDeclaredLoop-61 TOOL-dDeclaredLoop-62 TOOL-dDeclaredLoop-63 TOOL-dDeclaredLoop-64 TOOL-dDeclaredLoop-65 TOOL-dDeclaredLoop-66 TOOL-dDeclaredLoop-67 TOOL-dDeclaredLoop-68 TOOL-dDeclaredLoop-69 TOOL-dDeclaredLoop-70 TOOL-dDeclaredLoop-71 TOOL-dDeclaredLoop-72 TOOL-dDeclaredLoop-73 TOOL-dDeclaredLoop-74 TOOL-dDeclaredLoop-75 TOOL-dDeclaredLoop-76 TOOL-dDeclaredLoop-77 TOOL-dDeclaredLoop-78 TOOL-dDeclaredLoop-79 TOOL-dDeclaredLoop-80 TOOL-dDeclaredLoop-81 TOOL-dDeclaredLoop-82 TOOL-dDeclaredLoop-83 TOOL-dDeclaredLoop-84 TOOL-dDeclaredLoop-85 TOOL-dDeclaredLoop-86 TOOL-dDeclaredLoop-87 TOOL-dDeclaredLoop-88 TOOL-dDeclaredLoop-89 TOOL-dDeclaredLoop-90 TOOL-dDeclaredLoop-91 TOOL-dDeclaredLoop-92 TOOL-dDeclaredLoop-93 TOOL-dDeclaredLoop-94 TOOL-dDeclaredLoop-95 TOOL-dDeclaredLoop-96 TOOL-dDeclaredLoop-97 TOOL-dDeclaredLoop-98 TOOL-dDeclaredLoop-99 TOOL-dDeclaredLoop-100 TOOL-dDeclaredLoop-112 TOOL-dDeclaredLoop-116 TOOL-dDeclaredLoop-117 |
| [2026-11-17-build-TOOL-dDeclaredLoop-115-1-acceptance-ledger.md](../build/2026-11-17-build-TOOL-dDeclaredLoop-115-1-acceptance-ledger.md) | journal | — |
| [2026-11-17-build-TOOL-dDeclaredLoop-115-deviation-1151.md](../build/2026-11-17-build-TOOL-dDeclaredLoop-115-deviation-1151.md) | deviation | — |
| [2026-11-17-prompt-TOOL-dDeclaredLoop-115-1-spec-writer.md](../prompts/2026-11-17-prompt-TOOL-dDeclaredLoop-115-1-spec-writer.md) | journal | — |
| [2026-11-17-prompt-TOOL-dDeclaredLoop-115-build-brief.md](../prompts/2026-11-17-prompt-TOOL-dDeclaredLoop-115-build-brief.md) | journal | — |
| [2026-11-17-prompt-TOOL-dDeclaredLoop-115-spec-brief.md](../prompts/2026-11-17-prompt-TOOL-dDeclaredLoop-115-spec-brief.md) | research | — |

<!-- /gen:spec-records -->

## 1. Goal

The push arm decides that a commit adds the policy file from its FIRST parent alone, and an add is
printed and never graded. A merge whose first parent lacks the file, an orphan branch or a side that
deleted it, therefore skips the re-merge grade and the parents grade, and can set any policy value
with no `Gov-Policy:` trailer and no change record (round-1 item 1 of
2026-11-17-review-TOOL-dDeclaredLoop-1-closing-diff-round1, findings 1 and 2, HIGH). This unit reads
the file as added only where NO parent holds it, and routes every other merge into the merge grade
the arm already has, a parent lacking the file read as the empty table, as the parents grade already
reads every later parent. One plant observes both topologies the review names.

## 2. Scope (IN)

- **S1** — `check_push_range` (`tools/loop/guard.py#check_push_range`) reads each parent's policy
  blob once per commit into one list, in parent order. Where no entry of that list holds the file, a
  root commit included, the add rule stands as today: the `adds <policy path>, not graded` line where
  the commit's own blob holds the file and, for a merge, the combined diff lists it, then the next
  commit. Otherwise the commit falls through to the grade, `old` the first parent's blob or None,
  which `tools/loop/guard.py#parse_policy_bytes` reads as `{}`. The merge skip and the two reference
  lists of the `failed` arm and the parents-only arm read the same list instead of re-reading a later
  parent's blob, so each parent's blob is read once. No exit code, printed line shape or re-merge
  state changes. Observed by AC1, AC2, AC3.
- **S2** — One plant, `push-merge-first-parent-lacks-policy`, joins `PLANTS` and `run_guard_plant`
  (`tools/loop/guard.py#run_guard_plant`), with two scenarios over one scratch repository, each
  untrailered and owed exit 1: an orphan first parent lacking the file, whose re-merge fails on
  unrelated histories, and a first parent that deleted the file, whose clean re-merge lacks it. Its
  `run_selftest` owed exit is 1 (`tools/loop/guard.py#run_selftest`). Observed by AC1.
  **Readers:** by name: nothing is retired; the plant name is new and only `PLANTS` and `run_guard_plant` in `tools/loop/guard.py` spell it. by value: NO VALUE READERS, because the item adds a plant and retires no value.
- **S3** — The module docstring of `tools/loop/guard.py`, THE PUSH ARM paragraph, replaces its
  sentence on a first parent lacking the file with: "A commit or merge no parent of which holds the
  file, a root commit included, is printed where it adds the file and is not graded; a merge any
  parent of which holds it is graded as above, a parent lacking it, the first included, read as the
  empty table (TOOL-dDeclaredLoop-115)." Its WHAT THIS DOES NOT CHECK clause on a commit adding the
  policy file reads "a commit or merge adding the policy file that no parent holds". The parents-only
  arm's comment reads a lacking parent, the first included, as `{}`. Observed by AC4.
- **S4** — `help/policy.md`, the paragraph opening **The push check.** under `## Who may change the
  policy file`, replaces its sentence on an adding commit with: "A commit that adds the policy file, as
  an adopter's scaffold does, is printed and not graded, and so is a merge none of whose parents holds
  the file. A merge any of whose parents holds the file is graded as below, a parent lacking it read as
  setting no key, so a merge whose first parent is an orphan branch or deleted the file is graded too."
  Observed by AC4.
  **Readers:** by name: no reader spells the replaced sentence; its twin is the module docstring S3 rewrites. by value: NO VALUE READERS, because the sentence is prose no code reads.
- **S5** — The `loop guard fixtures` row of `tools/run-gates/selftest-budgets.txt` is re-priced for
  the plant, as every unit that added a guard plant re-priced it. Observed by AC5.

## 3. Non-goals (OUT)

- No change to the re-merge's five states, to `read_remerge_policy`, to the `failed` arm's rule that
  every key apart from some parent is owed, or to the parents-only arm's exemption for a key set back
  to one parent's value. A merge reaches those arms unchanged; only which merges reach them moves.
- No change to the commit verdict, `check_staged`, or to a non-merge commit: a commit has one parent,
  so it is an add exactly where it was one before (spec 2's §8 F11 stands).
- No edit to the CLOSED specs TOOL-dDeclaredLoop-2 and TOOL-dDeclaredLoop-44, whose texts state the
  first-parent rule; both stay frozen, and this spec is where the narrowing is written.
- No edit to `tools/loop/README.md`: its `guard.py` bullet names the push arm and states no add rule.
- No edit to `.githooks/pre-push`: it maps the arm's exit 1 to `policy-unrecorded` and exit 2 to a
  refusal, and neither mapping moves.
- Nothing in `tools/loop/loop_lib.py`, which TOOL-dDeclaredLoop-116 and TOOL-dDeclaredLoop-117 edit,
  and none of round 1's items 2 to 6 or round 2's items, each another unit's.

### Edges

- **consumes-from** external — the push arm's merge grade, landed CLOSED by TOOL-dDeclaredLoop-44, -59, -69, -78, -81 and -85: the re-merge states, the parents grade and the failed grade this unit routes one more class of merge into, unchanged

## 4. Design

### Evidence

Every code claim below was read at the branch tip a4256373 of
`branch/unattended-declared-loop-d56bf0` through `git show`, `tools/loop/guard.py` at blob 13a73d3e;
this worktree is cut from main, which lacks the loop kit. Both review records were read whole at the
same tip. The probes of §10 ran on this worktree's tree, main at 8eda4a5a0.

### Where the merge escapes

In `check_push_range`, for each commit `read_commits` names, `old` is `read_policy_blob` of
`c["parents"][0]` and nothing else. Where `old` is None the arm prints the add line when the merge's
own blob holds the file and the combined diff lists it, and then continues, for a commit and a merge
alike. That continue sits above the merge skip, above `read_remerge_policy`
(`tools/loop/guard.py#read_remerge_policy`) and above every grade, so a merge whose second parent
holds the file is never compared with anything. The parents-only arm already reads a parent past the
first that lacks the file as `{}`, through `parse_policy_bytes(None)`, and the `failed` arm does the
same; only the first parent is read differently.

### The mechanism

```python
blobs = [read_policy_blob(p, mguard.POLICY) for p in c["parents"]]
old, new = (blobs[0] if blobs else None), read_policy_blob(c["sha"], mguard.POLICY)
if all(b is None for b in blobs):
    # TOOL-dDeclaredLoop-115: an add is a commit or merge no parent of which holds the file, a root
    # commit included; any other merge is graded below, a lacking parent read as {}
    if new is not None and (listed is None or mguard.POLICY in listed):
        print(...)            # the add line, its bytes unchanged
    continue
if kind == "merge":
    if all(b == new for b in blobs):      # the merge skip, read from the same list
        continue
    ...                                   # read_remerge_policy and its arms, unchanged
refs = [parse_policy_bytes(b) for b in blobs]   # in the failed arm and the parents-only arm
```

`a`, the first parent's parsed table, stays `parse_policy_bytes(old)`, so a first parent lacking the
file is `{}` wherever `a` is read. `refs.index(None)` still names a parent whose file does not parse,
because the list keeps parent order.

### Which merges move

| Topology | Before | After |
|---|---|---|
| a non-merge commit adding the file, an adopter's scaffold | add line, not graded | unchanged |
| a root commit holding the file | add line, not graded | unchanged |
| a merge no parent of which holds the file, its result holding it | add line, not graded | unchanged |
| an orphan first parent lacking the file, the other parent holding it, finding 1 | add line, exit 0 | the re-merge fails on unrelated histories, so the failed grade: each key the result sets is owed, since it differs from the orphan's `{}` |
| a first parent that deleted the file, the other unchanged, the result keeping it, finding 2 | add line, exit 0 | the clean re-merge lacks the file, `absent`: each key the result sets is owed |
| the same, the result taking the deletion | continued in silence | `absent` re-merge equal to the result: nothing owed |
| a first parent that never held the file merging a side that added it, the result equal to that side | add line, not graded | `present` re-merge equal to the result: nothing owed, the side's adding commit still printed as an add |

The unrelated-history re-merge's failure is git's: the `push-merge-unrelated-histories` plant asserts
`the clean re-merge failed: 128` against a real git at the tip. The other git outcomes in this table
are UNVERIFIED by a run here; AC1 observes the two the plant builds.

### The plant

`push-merge-first-parent-lacks-policy`, one branch of `run_guard_plant`, over `write_guard_plant`'s
repository, whose policy file sets only the cap:

1. **An orphan first parent.** `tip` is HEAD. `checkout --orphan lacks`, `rm -- <policy path>`,
   commit. Back on `main`, append `FX_REVIEW` to the policy file through `write_staged`, then
   `commit-tree` of `write-tree` with `-p lacks -p main` and `reset --hard` to it, the idiom the
   `push-merge-unparseable-parent` branch writes its octopus with, so the first parent is the
   orphan whatever git's merge would do. Graded `--push-range <tip>..HEAD`: exit 1 naming
   `merge <sha8> · <policy path> · review.max-rounds`, and a second row on the same output naming
   `the clean re-merge failed: 128`. The orphan's root commit is in the range and reads as an add
   whose own blob lacks the file, so it prints nothing.
2. **A first parent that deleted the file.** `reset --hard <tip>`. `checkout -b run`, commit a
   non-policy file, `checkout main`, `rm -- <policy path>` and commit, `deleted` its sha. Then
   `merge --no-ff --no-commit run`, `checkout run -- <policy path>` and commit, the mirror of the
   `push-merge-resurrect-deleted-policy` branch. Graded `--push-range <deleted>..HEAD`: exit 1 naming
   `merge <sha8> · <policy path> · budgets.`, the cap's key.

Its `PLANTS` description names the policy file in words: "an orphan branch lacking the policy file as
a merge's first parent, main's file with review.max-rounds set as its result, then main deleting the
policy file and merging a run branch that keeps it, each untrailered". Two scenarios, because the two
findings reach two different arms, the failed grade and the `absent` re-merge grade, and the class is
the first parent's absence, not one arm.

### Inventory

| Identifier | Kind | Where | Naming |
|---|---|---|---|
| `push-merge-first-parent-lacks-policy` | a `PLANTS` key | `tools/loop/guard.py` | none: a plant id is a string, graded by no lexicon cell |

`blobs` is a local of `check_push_range` and is not a minted name. No function is minted.

### Files touched (estimate)

- `tools/loop/guard.py`: `check_push_range`, `PLANTS`, `run_guard_plant`, `run_selftest`, the module
  docstring
- `help/policy.md`: the paragraph opening **The push check.**
- `tools/run-gates/selftest-budgets.txt`: the `loop guard fixtures` row

### Alternatives rejected

- **Grade a lacking parent out of the references, not as `{}` (§8 F1 (b)).** It is a second reading
  of an absent file beside the parents and failed arms' `{}`, and it exempts a merge whose orphan side
  never held the policy at all.
- **One `any()` over the parents beside the existing reads.** Each later parent's blob would be read
  at the add test, again at the merge skip and again for the references: one fact read three times.
- **A helper for the `commit-tree` merge.** It is two git calls, and the kind this file repeats is
  the plant, whose table and branch this unit extends; the charter's kinds are kits.
- **One scenario, the orphan alone.** The deleted-first-parent merge reaches the `absent` arm, which
  the orphan's failed re-merge never does, so a regression there would stay green.

## 5. Production-readiness checklist

- security — the unit's subject: the push arm is the witness that a policy value changed with its
  trailer and record, and this closes a route around it. Deny by default holds: a merge any parent
  of which holds the file is graded, and only a merge no parent of which holds it keeps the add
  rule's exemption, which spec 2's §8 F11 granted the adopter's scaffold.
- perf / scale — a non-merge commit reads one parent blob, as before. A merge reads each parent's
  blob once, where it read the first, then each later one at the skip and again for the references.
  A merge whose first parent lacks the file now runs one `git merge-tree --write-tree`, the cost the
  docstring of `check_push_range` already prices per graded merge.
- error / empty / loading states — a root commit's empty parent list is an add, as before. A parent
  blob that git cannot read raises `OSError` at the up-front read, as it did at the later reads, and
  the arm prints `cannot judge` and exits 2.
- observability — the add line no longer prints for a merge any parent of which holds the file; the
  merge's grade prints instead, the failed line where the re-merge fails.
- risks — the failed grade owes every key a merge with an orphan first parent sets, since the orphan
  reads `{}`: a deliberate unrelated-history merge onto the default branch needs a trailer and record
  per key, or main as its first parent (§8 F1). The table in §4 marks the git outcomes no run here
  observed.
- testing — AC1 to AC5. The sweep, each reader of what the body changes and what keeps it green:
  - `check_push_range`'s callers, `git grep -n -E "check_push_range|--push-range" -- tools .githooks help`:
    `main` in `tools/loop/guard.py` for `--push-range`; `run_grade_in_process` inside
    `run_guard_plant`; the policy push arm block of `.githooks/pre-push`, which reads only the exit.
    The exit contract does not move.
  - `.githooks/pre-push.test.sh`, its TDL2 AC19 case: it writes a stub `loop/guard.py` that prints
    its argv and exits as told, so no byte of the real arm reaches it.
  - `PLANTS`, 44 keys PINNED at a4256373, 45 after; re-derived by the AST count in AC1's `figure:`.
    Its readers are `main`'s `--plant` choices, `run_fixture` and `run_selftest`, which iterates the
    table and reads its owed map, where the new key is owed 1.
  - the module docstring: `main` passes only its first paragraph, the title line, to the argument
    parser, and that line does not change.
  - `help/policy.md`: the `policy fixtures` leg reads only its `## Install` section
    (`tools/policy/check_policy.py`); the `docs` and `help page commands` legs read usage anchors,
    fenced blocks and inline code spans opening `python`, `python3` or `bash`
    (`tools/govkit/docs_leg.py`), and the edited sentences add none of the three.
  - `tools/run-gates/selftest-budgets.txt`, row `loop guard fixtures`: budget 146 PINNED at
    a4256373 against an r of 97 s PINNED on node d 2026-11-17, x1.5. The builder adds the plant's
    worst of two direct-CLI runs, rounded up, to r, writes the ceiling of 1.5 times the sum, and
    appends the clause and this unit's id as units 75 to 94 did. The leg's hang ceiling, 300 s PINNED
    in `tools/gate-legs.json` at a4256373, stays above it.
  - the lexicon's verb offender pin, 1215 PINNED as `VERB_OFFENDER_PIN` in `.lexicon.conf` at
    a4256373: no function is minted. Re-derive with `python tools/lexicon/lexicon.py --offenders`,
    its rows under `tools/loop/guard.py` equal at the base and at the pass. A helper a builder adds
    goes through `python tools/lexicon/lexicon.py --suggest <name> --as py.function` first.
  - `SHARED_RECORDS` in `.unattended.conf` names `memory/DECISIONS.md` and
    `memory/project/readme-contract.txt`; the pass writes neither, and the decisions file the plant
    writes is the scratch repository's own.
  - refusal ceilings and family sidecars: `REFUSAL_CEILINGS` in `.memory-tree.conf` and
    `tools/unattended/unattended.families.txt` are read by `tools/memory-tree/check-arms.py` over
    tracked shell scripts, whose docstring puts Python refusals outside its population; no shell
    script changes. Re-derive with `python tools/memory-tree/check-arms.py --report`.
  - `memory/map/generated/symbols.json`: its rows carry an id, a kind and a file, and no symbol is
    added or removed, so it does not move.
  - the kickoff manifest's `watch:` line in `memory/guides/SESSION-KICKOFF.md` names neither
    `tools/loop/guard.py` nor `help/policy.md`, so no `last-audit` re-stamp is owed.
  - `tools/govkit/registry.toml`, its `loop guard fixtures` exempt-leg row, describes the leg in prose
    that names no plant, and does not move.
- migration — none: no record, row shape or flag changes.
- user docs — `help/policy.md` (S4). No verb or flag is added, so no usage anchor is owed.

## 6. Acceptance criteria

- **AC1** — When `python tools/loop/guard.py --fixture --plant push-merge-first-parent-lacks-policy`
  runs at this pass, it prints `held` for the orphan first parent naming `review.max-rounds`, `held`
  for its failed-line row naming `the clean re-merge failed: 128`, and `held` for the
  deleted-first-parent merge naming `budgets.`, then `all held`, and exits 1.
  Red when: `check_push_range`'s first-parent read and its continue are restored, so each merge
  prints the add line, `adds <policy path>, not graded`, every row prints `MISSED` and the plant
  exits 3.
  figure: the plant count is DERIVED by
  `python -c "import ast,sys; t=ast.parse(open(sys.argv[1],encoding='utf-8').read()); print([len(n.value.keys) for n in t.body if isinstance(n,ast.Assign) and getattr(n.targets[0],'id','')=='PLANTS'])" tools/loop/guard.py`,
  44 PINNED at a4256373 and 45 at the pass.
- **AC2** — When `python tools/loop/guard.py --fixture --plant push-first-to-empty-remote` runs, its
  rows print `held`, the count row naming
  `push · 2 commit(s) read · 1 changing .governance/policy.toml · 0 finding(s)`.
  Red when: the fixture's root commit, which adds the policy file with no parent, falls through to
  the grade and owes the cap's trailer, so the first scenario exits 1.
- **AC3** — When `python tools/loop/guard.py --fixture --plant <case>` runs for each of
  `push-merge-equal-to-every-parent`, `push-merge-unparseable-parent`,
  `push-merge-tree-fatal-unparseable-parent`, `push-merge-octopus`, `push-merge-both-absent` and
  `push-merge-unrelated-histories`, each prints `all held`.
  Red when: the merge skip reads a list other than the parents' blobs, so
  `push-merge-equal-to-every-parent` prints `merge-tree runs: 1`, or a reference list loses parent
  order, so `refs.index(None)` names another parent than the one whose file does not parse.
- **AC4** — When
  `python -c "import ast,sys; s=' '.join(ast.get_docstring(ast.parse(open(sys.argv[1],encoding='utf-8').read())).split()); print('no parent of which holds the file' in s, 'whose first parent lacks the file' in s)" tools/loop/guard.py`
  runs, it prints `True False`; when
  `python -c "import sys; s=' '.join(open(sys.argv[1],encoding='utf-8').read().split()); print('none of whose parents holds the file' in s, 'a parent lacking it read as setting no key' in s)" help/policy.md`
  runs, it prints `True True`; and `grep -c "a parent past the first lacking" tools/loop/guard.py`
  prints `0`.
  Red when: the docstring, the help paragraph or the parents-only comment still states the
  first-parent rule.
- **AC5** — When `grep -n "^loop guard fixtures" tools/run-gates/selftest-budgets.txt` runs, the row
  names `TOOL-dDeclaredLoop-115` and the plant's reading, and its budget is the ceiling of 1.5 times
  the r it states.
  Red when: the row still reads 146 with no clause for the plant.
  figure: the reading and the budget are PINNED by the builder at the pass.

## 7. Gates

`loop guard fixtures` · `policy fixtures` · `docs` · `help page commands` · `line length` · `lexicon naming predicates` · `codebase-map coverage + freshness` · `positional (the citation check alone)` · `pre-push self-test` · `spec tokens (a spec's own names resolve)` · `memory hygiene`

New arm: tools/loop/guard.py · covers AC1 · the plant push-merge-first-parent-lacks-policy run over the tip's check_push_range, its first-parent continue in place, prints MISSED on every row and exits 3 · the loop guard fixtures row of tools/run-gates/selftest-budgets.txt, re-priced

What the arm does not check, so a green is not read as more. It builds two topologies, each with one
untrailered merge, and grades neither a trailered pass nor the merge that takes the deletion; the
`push-merge-both-absent` and `push-merge-equal-to-every-parent` plants hold the arm's exit 0 on other
shapes, and nothing holds it on these two. It builds no octopus whose first parent lacks the file and
no re-merge that conflicts on the file with a lacking first parent, both of which reach the parents
grade and its stated exemption. It reads the host's git, whose unrelated-history refusal it takes as
the `push-merge-unrelated-histories` plant does. And it grades the arm, not the pre-push hook, whose
suite stubs the arm.

## 8. Open questions

- **F1 — What does a parent lacking the policy file read as, once a merge with such a first parent is
  graded?** (a) The empty table, `{}`, at every parent: the review's fix, judged sound, and the rule
  the parents arm and the failed arm already apply to a later parent through `parse_policy_bytes`.
  A merge with an orphan first parent then owes every key it sets on the failed grade. (b) Only the
  parents holding the file are references: such an orphan merge owes only what differs from the
  holding side, but an absent file then reads two ways in one function, and a later lacking parent
  in the existing arms would have to move with it or disagree. Recommendation (a).
  RESOLVED (agent, 2026-11-17, delegated): (a), rung 3: one reading of an absent file at every parent, the review's sound fix, and deny by default where the re-merge fails
  widens: none · relaxes: none

## 9. Revision log

- rev-1 · 2026-11-17 · initial draft, from round-1 item 1 of
  2026-11-17-review-TOOL-dDeclaredLoop-1-closing-diff-round1, read with its round-2 record
  2026-11-17-review-TOOL-dDeclaredLoop-1-closing-diff-round2, and the writer's handoff
  2026-11-17-prompt-TOOL-dDeclaredLoop-115-1-spec-writer.

## 10. Reuse audit

The seam is the push arm itself: `tools/loop/guard.py#check_push_range`'s per-commit parent read,
which S1 widens from the first parent to every parent, and the parents arm's existing rule that a
lacking parent reads as `{}` through `tools/loop/guard.py#parse_policy_bytes`, which S1 applies to the
first parent too. The plant extends `PLANTS` and `tools/loop/guard.py#run_guard_plant`, reusing the
`commit-tree` idiom of its `push-merge-unparseable-parent` branch and the merge idiom of its
`push-merge-resurrect-deleted-policy` branch. The map probe,
`python tools/codebase-map/reuse_lookup.py "grade a merge whose parent lacks the guarded policy file on the push arm"`,
ran on main's tree, 322 files scanned PINNED 2026-11-17 and the loop kit not among them, and ranked
name-stem neighbours (`merge`, `read_policy_value`, `run_plant_arms`) and no seam in the push arm. The
recall probe found TOOL-dDeclaredLoop-59, TOOL-dDeclaredLoop-78 and TOOL-dDeclaredLoop-81, the arms
this unit routes the merge into, and TOOL-dDeclaredLoop-44, whose S2 wrote the first-parent rule.

Recall terms used: `push arm merge first parent policy.toml adds not graded re-merge parents-only lacking parent empty table Gov-Policy trailer`, against the question "how does the policy push arm grade a merge when a parent lacks the policy file".
