# TOOL-aPrunedIndex-24 — the held-answer rules get a `held-key` plant that `tags bundle selftest` runs

**Status:** CLOSED · rev-2 · 2026-11-26 · node a · Tier-1 · base 3d6c1702 · streams tooling · order 8

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-11-26-build-TOOL-aPrunedIndex-24-1-acceptance-ledger.md](../build/2026-11-26-build-TOOL-aPrunedIndex-24-1-acceptance-ledger.md) | journal | — |
| [2026-11-26-prompt-TOOL-aPrunedIndex-24-1-spec-brief.md](../prompts/2026-11-26-prompt-TOOL-aPrunedIndex-24-1-spec-brief.md) | research | TOOL-aPrunedIndex-17 |
| [2026-11-26-review-TOOL-aPrunedIndex-24-diff-review-round4.md](../reviews/2026-11-26-review-TOOL-aPrunedIndex-24-diff-review-round4.md) | diff-review | TOOL-aPrunedIndex-1 TOOL-aPrunedIndex-2 TOOL-aPrunedIndex-3 TOOL-aPrunedIndex-4 TOOL-aPrunedIndex-5 TOOL-aPrunedIndex-6 TOOL-aPrunedIndex-7 TOOL-aPrunedIndex-8 TOOL-aPrunedIndex-9 TOOL-aPrunedIndex-10 TOOL-aPrunedIndex-11 TOOL-aPrunedIndex-12 TOOL-aPrunedIndex-13 TOOL-aPrunedIndex-14 TOOL-aPrunedIndex-15 TOOL-aPrunedIndex-16 TOOL-aPrunedIndex-17 TOOL-aPrunedIndex-18 TOOL-aPrunedIndex-19 TOOL-aPrunedIndex-20 TOOL-aPrunedIndex-21 TOOL-aPrunedIndex-22 TOOL-aPrunedIndex-23 TOOL-aPrunedIndex-25 TOOL-aPrunedIndex-26 PLAY-dClosedLoop-1 TOOL-aTwinnedPass-1 TOOL-dPlacedRequest-95 TOOL-dPlacedRequest-105 TOOL-dSettledStage-1 |
| [2026-11-26-review-TOOL-aPrunedIndex-24-spec-audit-round1.md](../reviews/2026-11-26-review-TOOL-aPrunedIndex-24-spec-audit-round1.md) | spec-audit | — |

<!-- /gen:spec-records -->

## 1. Goal

Unit 17's held git answers rest on three rules that no arm on the bar can turn red: the read table of
`tools/playbook/gov_tag.py#derive_held_key` with its `.git`-exists guard, the never-store-a-failure
rule of `tools/playbook/gov_tag.py#read_held_git`, and the members of `HELD_FLAGS`, whether one is added,
removed or shadowed. After this unit one plant, `held-key`, rowed in `tools/playbook/tag_bundle.py#SELFTEST_ROWS`, reds when any of them breaks,
and `HELD_FLAGS` loses the `"--"` member its code never reads. This is the one unit that BUILD-METHOD
M4 batches items 1, 4 and 5 of `2026-11-26-review-TOOL-aPrunedIndex-17-20-diff-review-round3` into, on
the owner's "Build them first" of 2026-11-26.

## 2. Scope (IN)

- **S1** — `tools/playbook/gov_tag.py` gains the plant `held-key`: its name is appended to `PLANTS`,
  and its body is one `if plant == "held-key":` block in `run_plant`, beside the `named-probe` block,
  defining no top-level function. Observed by AC1, and the no-top-level-function clause by AC4.
- **S2** — The plant's first check calls `derive_held_key` over the eleven reads of spec 17's AC2,
  at the fixture repository's root and, for the two reads spec 17 repeats at `tools/`, at the
  fixture's `memory` directory, where no `.git` entry stands. Each `<id>` is the fixture's own
  `rev-parse HEAD`. It holds when the vector of `key is not None` reads
  `[True, False, True, False, False, False, True, True, False, False, False]`. Observed by AC1 and AC2.
- **S3** — The plant's second check enters `with set_git_held():` itself and counts calls to
  `subprocess.Popen` through `unittest.mock.patch.object(subprocess, "Popen", wraps=subprocess.Popen)`.
  `ti.read_git(root, "rev-parse", "0" * 40 + "^{tree}")` raises `TagError` on each of two calls and
  spawns twice. `ti.read_git(root, "rev-parse", <id> + "^{tree}")` returns one answer on each of two
  calls and spawns once. Before it counts any spawn, the check asserts that
  `derive_held_key(root, ("rev-parse", "0" * 40 + "^{tree}"))` and
  `derive_held_key(root, ("rev-parse", <id> + "^{tree}"))` are both not `None`, and fails when either
  is, so an unkeyed read can never pass the spawn count. After the block, `ti.read_git_stdout` and
  `ti.git` are the objects they were before it. Observed by AC1 and AC2.
- **S4** — The plant's third check reads every member of `HELD_FLAGS`: for each flag `f`,
  `derive_held_key(root, ("ls-tree", f, <id>))` returns a key. A member that some earlier branch
  shadows, as the `arg == "--"` branch shadows `"--"`, returns `None` there and fails the check. The
  check also fails when `sorted(HELD_FLAGS)` is not `['--full-tree', '--name-only', '-r', '-z']`, so a
  member added to the set or taken out of it reds it, where the loop alone never iterates one taken
  out. Its line prints
  the members as `" ".join(sorted(HELD_FLAGS))`, never in the set's own iteration order, which moves
  with the hash seed. Observed by AC1 and AC2.
- **S5** — `"--"` leaves `HELD_FLAGS`, which then holds `{"--full-tree", "--name-only", "-r", "-z"}`.
  The `arg == "--"` branch of `derive_held_key` stays the one owner of the separator rule. The one
  `#:` line above `HELD_ID_RE`, which today reads `#: S1: the one full object id a held read names,
  alone or naming its tree, and every flag it may carry` (`tools/playbook/gov_tag.py@6c0431dd:444`)
  and covers both `HELD_ID_RE` and `HELD_FLAGS`, changes only in its flag clause, to `and every flag
  it may carry before its paths`; its id sentence stays as it is. S2's vector is unchanged by this
  edit. Observed by AC1 and AC3.
- **S6** — `SELFTEST_ROWS` gains one row, `held-key|0|held keys as listed, failures asked again,
  every flag read`, after the `gc-predates` row. The fourteen rows it holds today do not change.
  Observed by AC4 and AC5.

## 3. Non-goals (OUT)

- Any edit to `tools/playbook/tag_index.py` or to a module in its import closure. On 2026-11-26
  `import_walk.derive_module_closure` printed nine modules for it, and neither `gov_tag.py` nor
  `tag_bundle.py` is one.
- `HELD_PLANTS` and the five plants it names. Their bodies, verdicts and output lines stay as they
  are, and `held-key` is not added to `HELD_PLANTS`: it enters `set_git_held()` itself, so
  `run_fixture` runs it as it runs every plant outside the five.
- Any ceiling or budget row. `tools/gate-legs.json`, `tools/run-gates/selftest-budgets.txt` and
  `tools/run-gates/ceiling-evidence.txt` do not change.
- `tools/loop/position.py` and `tools/memory-tree/routed_commits.py`, which other sessions are landing.
- The review's second left-shift for item 1, that `harness arms (fail branches armed or pinned)`
  count the guard's false branch. The brief asks for the plant arm only.
- Items 2 and 3 of the same review, the ledger sentences and the hygiene check they propose. They
  are records and a separate mechanism, and the brief scopes this unit to items 1, 4 and 5.
- The unit builds on unit 17's closed code, `derive_held_key`, `read_held_git` and `set_git_held`,
  and on unit 20's pooled runner, and edits neither unit's spec.

## 4. Design

The plant reuses everything `run_fixture` already gives a plant: a scratch fixture repository at
`root`, the caller's git variables set aside, and `say` for its step lines
(`tools/playbook/gov_tag.py#run_fixture`, `tools/playbook/gov_tag.py#run_plant`). Its three checks
each print one `say` line ending `held` or `FAILED`, the convention of the `dead-versions` block, and
the plant prints its last line and returns 0 only when all three hold:

```
tags: plant held-key · keys: [True, False, True, False, False, False, True, True, False, False, False]; held
tags: plant held-key · a failing read: 2 reads, 2 spawns; a held read: 2 reads, 1 spawn, one answer; readers put back; held
tags: plant held-key · flags read: --full-tree --name-only -r -z; held
tags: plant held-key · held keys as listed, failures asked again, every flag read
```

The checks call `derive_held_key` and `read_held_git` through the module's globals, so the plant sees
whatever the source says at run time. `set_git_held` builds its `functools.partial` over the global
`read_held_git` when the block opens, so a variant of that function is the one the plant exercises.
The all-zero `^{tree}` read, spelled `rev-parse` and then the id, matches `HELD_ID_RE` under a verb
`derive_held_key` keys, so it is a keyed read: a store that kept its failure would answer the second
call without a spawn. Without the `rev-parse` verb the read gets no key at all
(`tools/playbook/gov_tag.py@6c0431dd:720`), which is why S3 spells the verb and asserts the key
first. The S4 check needs no patching: a member the membership test reaches gives
`ls-tree <flag> <id>` a key, a member an earlier branch shadows does not, and the pinned member list
catches a removed one. The flags line prints the members sorted, as AC3's probe does. Today the
liveness read gives `{'--': False, '--full-tree': True, '--name-only': True, '-r': True,
'-z': True}` over this repository, which is why S5 removes `"--"`.

On 2026-11-26 a probe of `derive_held_key` over this repository, with `memory` as the directory
holding no `.git` entry, printed S2's vector at `tools/playbook/gov_tag.py@6c0431dd:712`. (PINNED,
2026-11-26)

### What it cannot see

- A new held read that spec 17's table does not list. The vector pins eleven reads, and a widened
  rule that keys some twelfth read stays green.
- Whether a held answer is stale inside the five plants. That is their own rows' work.
- The `flags read:` line's words on the bar. The `held-key` row matches the plant's last line only
  (`tools/playbook/tag_bundle.py@212497e0:411`), so a wrong flags line reaches the bar through the
  plant's exit code, never its text.

### Migration

`tools/playbook/gov_tag.py` and `tools/playbook/tag_bundle.py` are in the import closure of
`instruction_units.py`, as `import_walk.derive_module_closure` printed on 2026-11-26. The edit
therefore re-versions the `instruction_units:extract_unit` and `instruction_units:extract_repo`
extractors, the cost units 17 and 20 accepted for their own edits to the same files.

### Files touched (estimate)

- `tools/playbook/gov_tag.py`
- `tools/playbook/tag_bundle.py`
- the unit's acceptance ledger under `memory/builds/aPrunedIndex/build/`, one line per criterion

`memory/map/generated/symbols.json` does not move: it lists top-level functions, and the plant adds
none.

### Alternatives rejected

- A row in `tag_bundle.py`'s own selftest that imports `gov_tag` and checks the table in process.
  The leg grades plants by exit and line, and a plant gets the fixture repository and the set-aside
  git variables for free, where an in-process row would rebuild both.
- Dropping the `arg == "--"` branch and letting membership gate the separator, the review's other
  option. The branch also turns later arguments into paths, which membership alone cannot say, so
  the branch stays and the dead member goes.
- Asserting `HELD_FLAGS` equals a pinned set alone. A pin catches an added or removed member and never
  a shadowed one, and the liveness read alone never sees a removed one, so S4 runs both.

## 5. Acceptance criteria

- **AC1** — When `python tools/playbook/gov_tag.py --fixture --plant held-key` runs on the built
  tree, it exits 0 and prints the four lines section 4 shows, the last ending
  `held keys as listed, failures asked again, every flag read`.
  Red when: any check prints `FAILED`, or the plant is missing from `PLANTS` and exits 2.
- **AC2** — When a probe script under the run's scratch puts `tools/playbook` on `sys.path`, imports
  `gov_tag`, and calls `gov_tag.main(["--fixture", "--plant", "held-key"])` once unbroken and once
  under each of five in-memory breaks, it returns 0 unbroken and 1 under each break, and each break
  prints `FAILED` on the line of the check it names. The breaks are these. The guard removed:
  `gov_tag.derive_held_key` wrapped to key the two `--git-common-dir` and `--show-toplevel` reads at
  any directory, so the keys line fails. A failed read stored: `gov_tag.read_held_git` replaced by a
  variant that stores the exception and re-raises it on replay, so the spawns line fails. A wrong key
  for a listed read: `gov_tag.HELD_ID_RE` set to `re.compile(r"([0-9a-f]{40}|HEAD)(\^\{tree\})?")`,
  so `rev-parse HEAD^{tree}` gets a key and the keys line fails. A dead flag:
  `gov_tag.HELD_FLAGS` set to the built set with `"--"` added, so the flags line fails. A removed
  flag: `gov_tag.HELD_FLAGS` set to the built set without `"-z"`, so the flags line fails.
  Red when: a break leaves the plant at 0, or a break fails a check other than the one it names.
- **AC3** — When a probe prints `sorted(gov_tag.HELD_FLAGS)`, it prints
  `['--full-tree', '--name-only', '-r', '-z']`, and AC1's keys line still prints S2's vector. When
  `grep -n -B2 '^HELD_FLAGS' tools/playbook/gov_tag.py` runs, one printed line is the `#: S1:` line,
  still naming `the one full object id a held read names, alone or naming its tree` and ending
  `and every flag it may carry before its paths`.
  Red when: `"--"` is still a member, its removal moves a key in the vector, no printed line contains
  `before its paths`, or the id sentence is gone.
- **AC4** — When `git diff --name-only <parent> <build commit>` runs, it names
  `tools/playbook/gov_tag.py` and `tools/playbook/tag_bundle.py` and none of
  `tools/playbook/tag_index.py`, `tools/gate-legs.json`, `tools/run-gates/selftest-budgets.txt`,
  `tools/run-gates/ceiling-evidence.txt`, `tools/loop/position.py` or
  `tools/memory-tree/routed_commits.py`. A probe that loads the parent's `tag_bundle.py`, written to
  the scratch by `git show <parent>:tools/playbook/tag_bundle.py`, prints the parent's
  `SELFTEST_ROWS` lines as a prefix of the built ones, and the one added line as the `held-key` row.
  The probe also prints `True` for `set(gov_tag.HELD_PLANTS) == {"dead-versions", "named-probe",
  "released-rows", "released-cost", "gc-predates"}`, and `defs same: True` comparing the names of
  the top-level `ast.FunctionDef` nodes of the parent's `tools/playbook/gov_tag.py`, written to the
  scratch by `git show`, with the built file's.
  Red when: an existing row changes, `HELD_PLANTS` changes, a top-level function is added or removed,
  or the diff touches a cut-line file.
- **AC5** — When the main loop, at the close, takes the load gauge, the mean wall of 20
  `git --version` spawns as units 17 and 20 took it, and then runs
  `python tools/playbook/tag_bundle.py --selftest` once on the built tree, it exits 0, prints
  `PASS — the tag plants, 15 rows`, and its wall is under the 159 s of the `tags bundle selftest` row
  of `tools/run-gates/selftest-budgets.txt`. The ledger records the wall with the gauge beside it. A
  wall at or over 159 s taken at a gauge over 0.10 s is a re-read, not a red: the main loop retakes
  the gauge and the reading, at most twice. A wall under 159 s is green at any gauge, since load only
  lengthens it. Where all three readings reach 159 s and every gauge is over 0.10 s, AC5 is recorded
  UNGRADED with its readings and gauges, and goes to the owner.
  Red when: a row fails, the count is not the built row count, or the wall reaches 159 s at a gauge
  at or under 0.10 s.
  permission: a pass runs no self-test leg, so this reading is the main loop's.
  figure: the 15 is DERIVED from `SELFTEST_ROWS` at observation time; the 159 s is PINNED from the
  budget row as it stood on 2026-11-26; the 0.10 s band is DERIVED from the gauges of unit 17's AC7
  pairs, 0.038 to 0.089 s in all but five of thirty runs, in
  `memory/builds/aPrunedIndex/build/2026-11-26-build-TOOL-aPrunedIndex-17-1-acceptance-ledger.md`.

## 6. Gates

`tags bundle selftest` · `tags (the resolver's checks)` · `instruction units selftest` · `instruction edits (manifest checks)` · `edges (every declared edge parses, is registered and resolves)` · `lexicon naming predicates` · `playbook render selftest` · `govkit acceptance matrix` · `policy fixtures` · `codebase-map coverage + freshness` · `recall floor` · `recall floor arms` · `spec tokens (a spec's own names resolve)` · `memory hygiene`

The four legs that open the live index, `tags (the resolver's checks)`, `instruction units selftest`,
`instruction edits (manifest checks)` and
`edges (every declared edge parses, is registered and resolves)`, are owed because the edit
re-versions two `instruction_units` extractors, as units 17 and 20 owe them. They run at the close
and in no pass before it.

New arm: tools/playbook/tag_bundle.py · covers AC1 AC2 · the `held-key` row, staged red by the `os.path.lexists` guard deleted from `derive_held_key` · none
New arm: tools/playbook/tag_bundle.py · covers AC1 AC2 · the `held-key` row, staged red by `read_held_git` storing a raised exception and re-raising it on replay · none
New arm: tools/playbook/tag_bundle.py · covers AC1 AC2 AC3 · the `held-key` row, staged red by `HEAD` added to `HELD_ID_RE`'s accepted revisions, again by `"--"` put back into `HELD_FLAGS`, and again by `"-z"` taken out of it · none

## 7. Open questions

none

## 8. Revision log

- rev-1 · 2026-11-26 · initial draft.
- rev-2 · 2026-11-26 · §1 §4 §6 S1 S3 S4 S5 AC2 AC3 AC4 AC5 · folded
  `2026-11-26-review-TOOL-aPrunedIndex-24-spec-audit-round1`: ids 6 and 1 (S3 spells both reads with
  `rev-parse` and asserts their keys before counting spawns; §4 says why), id 8 (S4 pins the member
  list too, AC2 gains a removed-flag break, §6's third arm a third staged break, §1 claims removal),
  id 3 (S4 and §4 print the flags sorted), id 5 (S5 edits only the flag clause of the shared `#: S1:`
  line and quotes it), ids 2 and 4 (AC3 greps that comment, AC4 pins the top-level functions, S1
  names the AC that reads its clause), id 7 (AC5 takes a 20-spawn gauge, a 0.10 s band, two retakes
  and an UNGRADED route to the owner).

## 9. Reuse audit

The seam extended is the plant table: `tools/playbook/gov_tag.py#PLANTS`, one `if plant ==` block in
`tools/playbook/gov_tag.py#run_plant`, and one row of `tools/playbook/tag_bundle.py#SELFTEST_ROWS`,
the way unit 17's five plants were added. The probe
`python tools/codebase-map/reuse_lookup.py "a selftest plant that checks a key derivation table and counts subprocess spawns"`
ranked name-stem neighbours only, `key`, `check`, `run_selftest_cases` and `derive_key` among them,
and none checks a git read rule. The spawn count reuses spec 17's AC3 probe shape, a `wraps` patch of
`subprocess.Popen`. The recall answered this unit's own brief and the round 3 review first, whose item
5 names the `held-key` arm, then spec 17's AC2.
Recall terms used: plant selftest row arm seen-red staged break derive_held_key HELD_FLAGS spawn count held answer
