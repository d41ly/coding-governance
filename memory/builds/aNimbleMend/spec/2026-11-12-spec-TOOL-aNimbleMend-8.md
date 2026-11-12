# TOOL-aNimbleMend-8 — the inline red-fix lane: an open red admits a product write, and a `Red-fix:` trailer admits its commit

**Status:** CLOSED · rev-2 · 2026-11-12 · node a · Tier-2 · base 1265772c · streams tooling · order 8

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-11-12-build-TOOL-aNimbleMend-8-1-acceptance-ledger.md](../build/2026-11-12-build-TOOL-aNimbleMend-8-1-acceptance-ledger.md) | journal | — |
| [2026-11-12-prompt-TOOL-aNimbleMend-1-brief.md](../prompts/2026-11-12-prompt-TOOL-aNimbleMend-1-brief.md) | research | TOOL-aNimbleMend-1 TOOL-aNimbleMend-2 TOOL-aNimbleMend-3 TOOL-aNimbleMend-4 TOOL-aNimbleMend-5 TOOL-aNimbleMend-6 TOOL-aNimbleMend-7 TOOL-aNimbleMend-9 TOOL-aNimbleMend-10 TOOL-aNimbleMend-11 TOOL-aNimbleMend-12 |
| [2026-11-12-prompt-TOOL-aNimbleMend-8-build-brief.md](../prompts/2026-11-12-prompt-TOOL-aNimbleMend-8-build-brief.md) | research | — |

<!-- /gen:spec-records -->

## 1. Goal

A red leg's fix is a product change, and today every product change needs a specced unit twice:
at the write gate and at the commit grader. This unit opens one lane through both. While a leg is
recorded red the write gate admits a product write with no routed unit, and a commit that names
the leg in a `Red-fix:` trailer passes the grader with no unit id. Every other write and commit
meets today's refusals.

## 2. Scope (IN)

- **S1** — `tools/hooks/scratch-guard.js` gains `readOpenReds`, exported: the names of the legs the
  gate ledger under a git dir records red, in ledger order. An absent, empty or unreadable ledger
  is the empty list. Observed by AC1.
- **S2** — `tools/hooks/scratch-guard.js` gains `checkRedLane`, exported, the lane's one decision:
  given the writer, the role index, the lane key's state and the open reds, it returns a witness
  that admits or null. The rows are §4, "The lane's decision". Observed by AC2.
- **S3** — `checkRouted` asks the lane wherever it is about to refuse a PRODUCT write: its steps 7,
  8, 9b and 9a. An admit prints one witness line naming the open legs and the trailer the commit
  owes. A null returns the refusal `checkRouted` had already composed, byte for byte under `off`.
  The lane key and the ledger are read on that path only, so an admitted write and every non-product write cost
  what they cost today. Observed by AC2 and AC3.
- **S4** — The lane key, `bar.inline-red-fixes`, is asked under TOOL-aNimbleMend-1's contract, as
  `readPolicy('bar.inline-red-fixes', { repo })` from the policy kit's `policy-mirror.js`, found by
  `tools/hooks/agent-cap.js#resolvePolicyHelper`, which that file exports for it. `on` opens the
  lane, and so does a repository with no policy kit. `off`, a refused read and any other value
  close it. Observed by AC2 and AC3.
- **S5** — `tools/memory-tree/tree_lib.py` holds the trailer's one spelling, `RED_FIX_TRAILER`, and
  `routed_commits.py#read_routed_commits` reads its values in the log pass it already makes: each
  commit gains `red_fix`, the list of its `Red-fix:` trailer values, one leg name per trailer line.
  Observed by AC4.
- **S6** — `routed_commits.py#check_routed_commits` admits a graded commit that names no unit when
  it carries at least one `Red-fix:` value and every value is a leg name of the leg manifest in
  that commit's own tree. The summary line counts the admitted commits. A value that names no leg,
  or a manifest that cannot be read, is a violation that says so. A commit naming a unit is graded
  as today and its trailer is not read by this rule. Observed by AC4 and AC5.
- **S7** — The lane key gates the pushed range and not the history: with the key off, a `Red-fix:`
  commit in the RANGE half is the violation `names no unit`, in today's words, and the WHOLE half
  still admits it. The key is read once, through one helper `tools/memory-tree/tree_lib.py` gains
  and `build_records.py#read_override_value` is rebuilt on, and only when a graded commit carries
  the trailer and names no unit. Observed by AC5 and AC6.
- **S8** — The gate's own account is current: the write gate's header comment and the evaluation
  order above `checkRouted` in `tools/hooks/scratch-guard.js`, the write-gate section of
  `tools/hooks/README.md`, and the docstring of `tools/memory-tree/routed_commits.py`, each with
  what the lane does not check (§4). Observed by AC7.
- **S9** — The suite arms §7 declares, in `tools/hooks/scratch-guard.test.sh` and the self-test of
  `tools/memory-tree/routed_commits.py`. NOT OBSERVED: a pass runs no suite, so the main loop
  observes these arms RED and then GREEN at the close.

## 3. Non-goals (OUT)

- The record written after the fix, its door and its join. TOOL-aNimbleMend-9.
- What a lane commit may touch: the size bound, guarded policy files, specs and new files.
  TOOL-aNimbleMend-10 grades them on the commit. The write gate here admits any product path while
  a red is open; it cannot tell the narrowest fix from a wide one.
- A spec write. The lane is consulted for the product class only, so a write under a build's
  `spec/` folder meets the role arm exactly as today.
- Proving at the push that the named leg was red. The ledger is per clone and untracked, so the
  grader cannot see it; the proof a reader gets is the record TOOL-aNimbleMend-9 joins.
- A commit-time refusal. `.githooks/commit-msg` ships with no kit, and the unattended kit's
  `--check-commit` already passes a commit that names no open pass.
- A write through a shell. The write gate never saw one, and the grader is its backstop here as it
  is for a routed unit.
- Closing a red. A leg leaves the open set when the runner next records it green, which the re-run
  a fix owes does. This unit writes nothing to the ledger.
- A reader for `verdict.red-route`, which stays TOOL-dWitnessedBar's.
- The help page, the build method and the protocol. TOOL-aNimbleMend-11.
- The kit version markers, which the lander's `mint` moves once.

### Edges

- **consumes-from** `TOOL-aNimbleMend-1` — the key `bar.inline-red-fixes`, its two values and the
  ask contract's five outcomes. Without it the lane has no switch and both readers have nothing to
  ask.
- **consumes-from** `TOOL-aNimbleMend-5` — a red pass leg reaches the gate ledger because the
  adapter runs through the bar runner, which writes a ledger row per leg it ran. Without it only a
  bar's red opens the lane.
- **hands-off** `TOOL-aNimbleMend-9` — the `Red-fix:` trailer on the fix commit, one leg name per
  trailer line, and its one spelling in the memory-tree kit.
- **hands-off** `TOOL-aNimbleMend-10` — the `Red-fix:` values on each commit `read_routed_commits`
  returns, which the limits pass reads with no second log pass.
- **hands-off** `TOOL-aNimbleMend-11` — the lane's help page says what opens the lane, what the
  commit owes and what the lane does not check.
- **hands-off** `TOOL-aNimbleMend-12` — the lane observed end to end, in a scratch adopter and in
  gov, with its key on and off.

## 4. Design

### Evidence

Read at 91ca33f2, which adds only records to the base.

- **The write gate.** `tools/hooks/scratch-guard.js#checkRouted` is the gate and its comment is the
  one evaluation order. A product write is refused at step 7 with no card, at step 8 with no route,
  at step 9b with no buildable unit, and at step 9a by `checkRoleWrite` when the writer is no role
  declaring `writes = product`. The main loop carries no `agent_type`, so with a role index present
  step 9a refuses it even on a buildable route. The spec class returns at step 6a, before any of
  these.
- **Reading another kit's record from the hook.** `scratch-guard.js#readDispatchedUnits` already
  reads the unattended kit's run-state rows directly, and `module.exports` already carries it and
  `loadRoleIndex` for other readers.
- **The policy read from a hook.** `tools/hooks/agent-cap.js#resolvePolicyHelper` finds
  `policy-mirror.js` through that file's marked `resolveKitDir` block and `readWriterBound` calls
  `readPolicy(key, { repo })`. `agent-cap.js` requires `scratch-guard.js` lazily, inside functions,
  so the reverse lazy require makes no load-time cycle. `scratch-guard.js` carries no
  `resolveKitDir` of its own.
- **The ledger.** `tools/run-gates/run-gates.sh` writes `gate-ledger.tsv` under the git dir it
  resolves as `RG_GIT_DIR`, the worktree's own. A row is nine tab-separated fields: name, seconds,
  status, input key, ended-at, run, full, manifest blob, head. The merge keeps the row of every leg
  the run did not measure, so a red row stands until that leg next runs. On node a's main checkout
  on 2026-11-12 the status column held 124 `ok` and 9 `fail`; this figure is PINNED and nothing
  depends on it. `gate-last-failure.txt` is rewritten only by the next red run, so it cannot say a
  red is closed.
- **The commit grader.** `routed_commits.py#read_routed_commits` makes one `git log` pass whose
  format reads the `Pass:` trailer with `%(trailers:key=Pass,valueonly,...)`.
  `check_routed_commits` grades RANGE and, at a resolvable base, WHOLE beside it; a graded commit
  with no id is the violation `names no unit`. The RANGE half reads no waiver.
- **The other commit readers.** `unattended.sh#check_commit_message` returns 0 for a message whose
  `Pass:` trailer says `none`, and for one with no trailer whose subject names no open pass. The
  unattended kit gate's check 23 reports a declared path of an open pass that moved while no commit
  names that pass; a lane commit made between passes moves no open pass's path. Whether any other
  check of that gate reads an unattributed commit is UNVERIFIED.
- **Leg names.** `.memory-tree.conf` declares `LEG_MANIFEST`, and
  `tools/memory-tree/gotchas.py#load_leg_names` is the kit's one reader of the names it holds.
- **The python policy read.** `build_records.py#read_override_value` resolves the policy kit with
  `resolve_kit_dir` and runs `policy.py get charter.override`. It is the kit's one such read today.

### The open reds

`readOpenReds(gitDir)` reads `<gitDir>/gate-ledger.tsv` and returns field 1 of each row whose field 3
is `fail` or `timeout`. A row with fewer than three fields is skipped. `ok`, `retried` and any other
status are not red. The git dir is the worktree's own, the one the runner wrote under, never the
common dir.

One file answers for both kinds of red. A bar writes the ledger, and a pass-leg run does too,
because TOOL-aNimbleMend-5's adapter starts the same runner.

### The lane's decision

`checkRedLane(w)` takes `agentType`, `index` as `loadRoleIndex` returns it, `lane` as
`{ on, why }`, and `reds`. `lane` is the contract's outcome: on for the answer `on` and for no
policy kit, where `why` is the NOTE the contract asks for; off otherwise, where `why` is empty for
the answer `off`, the reader's own line for a refusal, and one line naming the key and the value
for any other answer. First match wins.

| # | Condition | Result |
|---|---|---|
| 1 | `lane.on` is not true | null |
| 2 | `reds` is empty | null |
| 3 | the index is broken | null |
| 4 | `agentType` is empty: the main loop | witness |
| 5 | the index is absent | witness |
| 6 | `agentType` names an `agent`-true role declaring `writes = product` | witness |
| 7 | anything else, the untyped harness agent included | null |

The witness is one line: that the red-fix lane admits the write, the open leg names, and that the
commit owes `Red-fix: <leg>` beside `Pass: none`. It leaves through the witness channel
`checkRouted` already has, which exits 0.

`checkRouted` gains step 10 in its comment: on a product-class refusal from step 7, 8, 9b or 9a,
read the lane key, then the ledger, then return `checkRedLane`'s witness or the refusal as composed.
A non-empty `why` is carried: on the witness line when the lane admits, and as one line appended to
the refusal when the read refused or answered another value. Under `off` the refusal is
byte-identical to today's.
A refusal for any other reason, the unarmed conf and a payload with no target among them, never
reaches the lane.

### The trailer and the grader

`RED_FIX_TRAILER` is the string `Red-fix`. The log format gains one field,
`%(trailers:key=Red-fix,valueonly,unfold,separator=%x1d)`, built from the constant, and `red_fix`
is its split, stripped, with empties dropped. A leg name holds spaces, commas and parentheses, so
the value is the whole line and nothing splits it further.

In `check_routed_commits`, a graded commit with no id and a non-empty `red_fix` is a lane
candidate. The candidates' manifests are read in one `git cat-file --batch` call over
`<sha>:<LEG_MANIFEST>`, made only when a candidate exists, so a history with no trailer costs no
spawn it does not cost today. Each blob's names are parsed by `gotchas.py#load_leg_names`'s rule,
reached by moving that rule's parse into `tree_lib.py` with `load_leg_names` calling it; the kit
keeps one manifest parser.

| Candidate | In RANGE, key on | In RANGE, key off | In WHOLE |
|---|---|---|---|
| every value a leg at its commit | admitted | `names no unit` | admitted |
| a value that is no leg | violation naming the value and the manifest | `names no unit` | violation naming the value and the manifest |
| `LEG_MANIFEST` blank, or no manifest at the commit | violation saying the trailer cannot be checked | `names no unit` | violation saying the trailer cannot be checked |

An admitted commit is counted, and the population's summary line gains ` · <n> red-fix` after the
waived count when `n` is above zero. With no admitted commit every line is today's.

The key is read by `tree_lib.py#read_policy_value(key, root)`, the read `read_override_value`
holds today, moved and parameterised, with `read_override_value` calling it. The key is the first
argument and each caller passes it as a literal, which is what TOOL-aNimbleMend-1's coverage arm
counts. `routed_commits.py#read_lane_state(repo)` calls it with `"bar.inline-red-fixes"` and
returns `(on, why)` by the same five outcomes as the hook: on for `on` and for no policy kit, off
for `off`, a refusal and any other value. A non-empty `why` is printed as one line after the
summary line.

### What the lane does not check

- Whether the write or the commit fixes the red. Any product path is admitted while any leg is
  open, and a trailer naming a real leg passes the grader.
- Whether the named leg was red. The grader reads no ledger.
- A red that no run has re-measured. A fixed leg whose guard the fix did not trip stays open until
  something runs it.
- A ledger edited by hand, as a hand-appended dispatch row is read like the driver's.
- A manifest moved since the commit: it is looked for at the path HEAD's conf names and reads as
  absent, the limit this grader already states for a moved spec.

### Inventory

| Minted | Where | Graded by |
|---|---|---|
| function `readOpenReds` | `scratch-guard.js` | the `lexicon naming predicates` leg, verb `read` |
| function `checkRedLane` | `scratch-guard.js` | the same leg, verb `check` |
| constant `RED_FIX_TRAILER` | `tree_lib.py` | AC4 |
| function `read_policy_value` | `tree_lib.py` | the same leg, verb `read` |
| function `read_lane_state` | `routed_commits.py` | the same leg, verb `read` |
| commit key `red_fix` | `read_routed_commits` | AC4 |
| trailer `Red-fix:` | commit messages | AC4, and TOOL-aNimbleMend-9's join |

### Rollout

The lane is live when the key reads on, which is its default. The write-gate half needs a red in
the ledger, so a clone that never ran a red bar or a red pass leg sees no change.

### The probes

`lane-probe.py`, written to the run's scratch directory and run from the repository root with the
key state and a short fixture root under the system temp directory:

```python
# usage: python lane-probe.py <on|off> <short fixture root>
import pathlib, sys, tempfile
sys.path.insert(0, "tools/memory-tree")
import routed_commits as rc
rc.read_lane_state = lambda repo: (sys.argv[1] == "on", "set by the probe")
root = pathlib.Path(tempfile.mkdtemp(prefix="rf-", dir=sys.argv[2]))
repo, s = rc.build_fixture(root, "lane", [
    {"msg": "init", "files": {"README.md": "x\n", "legs.json": '[{"name": "leg one"}]\n'}},
    {"msg": "fix: clear leg one\n\nRed-fix: leg one\nPass: none", "files": {"src/a.txt": "a\n"}},
    {"msg": "fix: names no leg\n\nRed-fix: leg nine", "files": {"src/b.txt": "b\n"}},
    {"msg": "chore: no id", "files": {"src/c.txt": "c\n"}},
])
rc.set_fixture_conf(repo, LEG_MANIFEST="legs.json")
for env in ({}, {"GATE_PUSH_BASE": s[0]}):
    code, lines = rc.check_routed_commits(repo, env)
    print("exit", code)
    print("\n".join(lines).replace(s[1][:8], "C2").replace(s[2][:8], "C3").replace(s[3][:8], "C4"))
```

Run at 91ca33f2, where the patched name does not exist, it prints C2, C3 and C4 each as
`no unit id — names no unit` in both halves. That output is the baseline AC5 compares with.

The ledger fixture for AC1 is five lines in a scratch directory's `gate-ledger.tsv`: `leg one` with
status `fail`, `leg two` with `ok`, `leg three` with `timeout`, `leg four` with `retried`, each
with nine fields, and one line holding a name alone.

### Files touched (estimate)

- `tools/hooks/scratch-guard.js`
- `tools/hooks/agent-cap.js`
- `tools/hooks/scratch-guard.test.sh`
- `tools/hooks/README.md`
- `tools/memory-tree/routed_commits.py`
- `tools/memory-tree/tree_lib.py`
- `tools/memory-tree/build_records.py`
- `tools/memory-tree/gotchas.py`

### Alternatives rejected

- **The write gate reads `gate-last-failure.txt`.** That file is rewritten only by the next red
  run, so it names a leg as failed long after it went green, and the lane would never close.
- **The write gate also reads the pass-leg run record.** The same legs' rows are in the ledger,
  written by the same runner, and the run record is replaced by the next run while the ledger
  keeps a skipped leg's row. Two files for one fact is the shape `[one-fact]` refuses.
- **A marker file or a card line that opens the lane.** The agent would write the fact the gate
  reads. The ledger is written by the runner.
- **A reader module in the run-gates kit, shared by the hook and the grader.** The grader cannot
  use it: it runs in remote CI over a clone that holds no ledger. One reader has one caller, so it
  lives beside its caller.
- **The grader admits any commit carrying the trailer.** A typed leg name is the least a trailer
  can be held to with tracked data, and a misspelt one would otherwise orphan the record's join.
- **A pseudo-unit id for lane commits.** It would need a spec to exist at the first parent, which
  is the cost the lane removes.

## 5. Production-readiness checklist

- security — the lane widens the write gate, so it closes at every unknown but one: a refused
  read, an unexpected value, a broken role index and an unreadable ledger each close it. A
  repository with no policy kit has no switch and keeps the lane, which is TOOL-aNimbleMend-1's
  contract for a default-on key. The writer is
  the main loop or a role already trusted with product writes. Ledger text is compared and printed,
  never evaluated. The grader's rule is tracked data only. What it does not check is in §4.
- perf / scale — the hook reads the key and the ledger on a would-be refusal only. The grader adds
  one batched git call and one policy read, and only for a history holding a lane candidate.
- error / empty / loading states — an absent ledger, an empty one, a short row, an absent or broken
  index, a refused key, a blank `LEG_MANIFEST` and a commit with no manifest each have a row in §4.
- observability — the admit prints a witness line naming the open legs; the grader counts admitted
  commits on its summary line and names each refused value.
- risks — the lane stays open for every product path while one red is open, and TOOL-aNimbleMend-10
  bounds what a lane commit may hold only at the commit. Until that unit lands, the lane is wider
  than the build means it to be; the build order lands both before the close.
- testing — AC1 to AC7 are probes; the arms of §7 re-observe AC1 to AC6 through the real hook and
  the real key read at the close.
- migration — none: no stored shape changes, and a history with no trailer is graded as today.
- user docs — the hooks kit's README and the grader's docstring are S8. The help page is
  TOOL-aNimbleMend-11's.

## 6. Acceptance criteria

- **AC1** — When `node -e` requires `tools/hooks/scratch-guard.js` and prints
  `JSON.stringify(readOpenReds(dir))` over the ledger fixture of §4, it prints
  `["leg one","leg three"]`, and over an empty directory it prints `[]`.
  Red when: `retried` or `ok` counts as red, a short row throws, or an absent ledger throws.
- **AC2** — When `node -e` requires `tools/hooks/scratch-guard.js` and calls `checkRedLane` once per
  row of §4, "The lane's decision", each call returns what its row states: a `witness` string
  naming `leg one` and `Red-fix:` for rows 4, 5 and 6, and null for rows 1, 2, 3 and 7.
  Red when: the lane admits with the key off, with no open red, on a broken index, or for an agent
  type the index gives no product write.
- **AC3** — When `grep -c "checkRedLane(" tools/hooks/scratch-guard.js` runs, it prints at least 2,
  and `node -e` over `String(checkRouted)` prints `true` for this test: the text holds
  `checkRedLane`, and its first occurrence comes after the `checkRoleWrite('spec'` call that
  returns the spec class.
  Red when: `checkRouted` never asks the lane, or asks it before the spec class has returned, so a
  spec write could reach it.
- **AC4** — When `python lane-probe.py on` runs with a fixture root, both halves list C3 with the
  value `leg nine` and the manifest `legs.json`, list C4 as `names no unit`, do not list C2, and
  the WHOLE summary line and the RANGE summary line each hold `1 red-fix`. The script and its
  fixture are §4, "The probes".
  Red when: the trailer is not read, a value that is no leg is admitted, or the admitted commit is
  not counted.
- **AC5** — When `python lane-probe.py off` runs, the RANGE half lists C2, C3 and C4 each as
  `no unit id — names no unit`, exactly as the 91ca33f2 baseline does, and the first block, graded
  WHOLE, still admits C2.
  Red when: the key off leaves a pushed lane commit admitted, or turning the key off reds a lane
  commit already in history.
- **AC6** — When `python -c` imports `tools/memory-tree/build_records.py` and
  `tools/memory-tree/tree_lib.py` and prints whether `read_policy_value` is defined in `tree_lib`
  and named in the source of `read_override_value`, it prints `True True`; and
  `grep -c "policy.py" tools/memory-tree/routed_commits.py` prints 0.
  Red when: the grader carries a second copy of the policy read.
- **AC7** — When `grep -c "Red-fix"` runs over `tools/hooks/README.md` and over the docstring lines
  of `tools/memory-tree/routed_commits.py`, each prints at least 1, and
  `grep -ci "red-fix lane" tools/hooks/scratch-guard.js` prints at least 2, one for the header
  comment and one for the evaluation order's new step.
  Red when: the lane is built and the gate's own account of what it admits still says a product
  write always needs a routed unit.

## 7. Gates

`scratch-guard self-test` · `agent-cap self-test` · `format-guard self-test` · `verifier fan-out self-test` · `review-join self-test` · `hook destinations self-test` · `policy fixtures` · `routed-commits selftest` · `routed commits name a specced unit` · `lexicon naming predicates` · `codebase-map coverage + freshness` · `install-prefix (shipped surface)` · `kit epoch (shipped bytes move, the version moves)` · `kit version markers` · `memory hygiene` · `spec tokens (a spec's own names resolve)`

The first eight are held or guarded on a default bar, and the close runs them as its flags decide.
The kit epoch and version legs expect the lander's `mint`.

New arm: tools/hooks/scratch-guard.test.sh · covers AC1 AC2 AC3 · a hook payload for a product write with no route, over a fixture ledger holding a red row, with the lane key on and then off · none
New arm: tools/memory-tree/routed_commits.py · covers AC4 AC5 AC6 · the probe's four commits, graded WHOLE and RANGE with the key on and off, and a trailer-free history for the spawn count · none

## 8. Open questions

- **F1 — With the key off, does the grader also refuse the lane commits already in history?**
  The grader reads the key at grading time, and its WHOLE half grades every commit ever landed.
  - **A, the key gates the pushed range only.** RANGE refuses a lane commit under a key that is
    off; WHOLE admits a well-formed one whatever the key says. Turning the key off stops new lane
    commits at the push and reds nothing that landed. A plain local run with no push base grades
    WHOLE, so with the key off it still admits a lane commit the push will refuse.
  - **B, the key gates both halves.** With the key off the output is today's for every history,
    which is the build's byte-for-byte sentence read literally. An adopter who used the lane and
    then turns it off has every past lane commit red in WHOLE and in remote CI, and must list each
    in `ROUTED_COMMIT_WAIVED`.
  - **Recommendation: A.** The owner asked for one key that turns the mechanism off, and under B
    that key cannot be turned off after first use without a waiver per commit. Under A the
    byte-for-byte sentence holds for a history that holds no lane commit, which is every repository
    that never turned it on. S7, the table of §4 and AC5 are written to A; under B the WHOLE column
    takes the key and AC5's last clause inverts.
  RESOLVED (agent, 2026-11-12, delegated): A, the key gates the pushed range only. Under B the key could not be turned off after first use without a waiver per landed commit.

## 9. Revision log

- rev-1 · 2026-11-12 · initial draft.
- rev-2 · 2026-11-12 · every §8 fork resolved in place under the run's mandate (M3).

## 10. Reuse audit

The seams are four that exist. The write gate is `tools/hooks/scratch-guard.js#checkRouted`, and
the lane is one more step of its one evaluation order, read the way `readDispatchedUnits` already
reads another kit's record. The hook-side policy read is `tools/hooks/agent-cap.js#resolvePolicyHelper`
with `policy-mirror.js#readPolicy`. The commit grader is
`tools/memory-tree/routed_commits.py#read_routed_commits` and `check_routed_commits`, whose log
pass already reads one trailer. The python policy read is `build_records.py#read_override_value`,
and this unit is its second instance, so it is extracted into `tree_lib.py` and not copied; the leg
names come from `gotchas.py#load_leg_names`'s parse, moved the same way. `python
tools/codebase-map/reuse_lookup.py "admit a product write that names an open red leg through a
commit trailer"` returned name-stem neighbours only (`write`, `legs`, `opened`, `write_commit`); for
a reader of open reds, no existing seam fits, on this evidence: `grep -rn "gate-ledger"` over the
shipped kits finds the ledger read by `run-gates.sh` and its measuring scripts and by no hook.

Recall returned TOOL-aOrientedCast-6, which added the role arm after the route arm and is the
order step 9a keeps; TOOL-aRoutedQuill-3 and TOOL-aRoutedQuill-10, the grader and its WHOLE half;
and TOOL-dScopedBuild-3 and TOOL-dWitnessedBar-21, which design a scoped push arm and a fix pass
routed by `verdict.red-route` in builds that are DEFERRED, so no built seam exists there and this
unit reads neither key.

Recall terms used: `python tools/memory-recall/query.py "how does the write gate admit a product
write with no routed unit and how does the commit grader attribute it" --terms "write gate
checkRouted routed commits Pass trailer names no unit ROUTED_PATHS role arm scratch-guard waiver
red fix"`
