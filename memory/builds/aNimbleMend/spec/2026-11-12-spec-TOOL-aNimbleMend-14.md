# TOOL-aNimbleMend-14 — the red-fix lane opens only on a red of this branch's present state: an open red is bounded by its row's own head

**Status:** CLOSED · rev-1 · 2026-11-12 · node a · Tier-2 · base 97e0841d · streams tooling · order 14

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-11-12-build-TOOL-aNimbleMend-14-1-acceptance-ledger.md](../build/2026-11-12-build-TOOL-aNimbleMend-14-1-acceptance-ledger.md) | journal | — |
| [2026-11-12-prompt-TOOL-aNimbleMend-14-brief.md](../prompts/2026-11-12-prompt-TOOL-aNimbleMend-14-brief.md) | research | — |
| [2026-11-12-prompt-TOOL-aNimbleMend-14-build-brief.md](../prompts/2026-11-12-prompt-TOOL-aNimbleMend-14-build-brief.md) | research | — |

<!-- /gen:spec-records -->

## 1. Goal

The closing diff review's one HIGH item, H1: the red-fix lane reads every carried-forward `fail`
row of the gate ledger as an open red, so with `bar.inline-red-fixes` at its default the lane is
open in the primary checkout on landing, for a write that answers no current red. This unit makes
`tools/hooks/scratch-guard.js#readOpenReds` count a row only when the row's own head field places
it on this branch's present state, so the lane opens on a red measured here and on no other.

## 2. Scope (IN)

- **S1** — `tools/hooks/scratch-guard.js#readOpenReds` takes the worktree's toplevel as a second
  argument and returns a red row's name only when all four bounds of §4 hold: the row has the
  nine-field form, its name is a leg of the manifest the conf key `LEG_MANIFEST` names, and its
  head field is `HEAD` or an ancestor of `HEAD` that the landed revision does not reach. Ledger
  order is kept. Observed by AC1, AC3 and AC4.
- **S2** — The lane's call in `tools/hooks/scratch-guard.js#checkRouted` hands the reader the
  toplevel it already holds, so the write gate's refusal stands wherever the reader answers the
  empty list. `tools/hooks/scratch-guard.js#checkRedLane` is not edited. Observed by AC2 and AC5.
- **S3** — `tools/policy/policy-mirror.js` exports its existing function `readLandedRevision`
  beside `readPolicy` and `PolicyRefusal`. The function's body does not move. Observed by AC6.
- **S4** — A held leg stays eligible. The reader tests no `chunk`, no `subject` and no `pass_leg`
  field of the manifest row, so a held leg a full bar redded at `HEAD` opens the lane. Observed by
  AC3 and AC5.
- **S5** — `tools/hooks/scratch-guard.test.sh` gains the arm class "a carried-forward ledger row
  never opens the lane", and its existing lane arms are rebuilt on rows that satisfy the bounds
  (§4, "The suite"). Observed by AC3 and AC5, whose fixture is the arms' fixture; the suite's own
  verdict is the main loop's, declared in §7.
- **S6** — The texts say what S1 makes true: the closing sentence of "What opens the lane" and the
  third bullet of "What it does not check" in `help/red-fix-lane.md`, the lane paragraph of
  `tools/hooks/README.md`, and the row of `tools/policy/README.md` that lists what
  `policy-mirror.js` offers. Observed by AC7.
- **S7** — The comments of `tools/hooks/scratch-guard.js` that state the old rule are rewritten:
  the RED-FIX LANE block of the header, the comment of `readOpenReds`, and step 10 of
  `checkRouted`'s evaluation order. NOT OBSERVED: no probe tells a true comment from a stale one,
  and the closing review reads them against the code.

## 3. Non-goals (OUT)

- The newest-run bound. The review record rejects it: a later pass-leg run that does not measure
  a leg would close the lane on that leg's bar red. This unit builds the head bound alone.
- Any test of whether a leg is held. The rejected fix of finding 22 dropped held legs' rows.
- Any finding of the review record other than H1. M4, the `retried` status, M5, the suite guards,
  M7, the blank `LEG_MANIFEST` default, M11, the missing-kit arm, and L1, the read order of
  `checkLane`, each touch code this unit reads and none is repaired here.
- A fallback for a blank `LEG_MANIFEST`. Under a blank key the lane is closed (§4), which agrees
  with the commit grader's refusal of every lane commit under the same key.
- A new line on the refusal. A refusal that stands because no row is open is byte for byte the
  one the gate composed, as it is today with no red in the ledger.
- The bug-class record `carried-forward-row-read-as-current` under `memory/gotchas/`. It is a
  separate document with a generated index beside it, so by the build method's M2 it is no part of
  this mechanism. The regression gate M8 asks for is the arm class of S5.
- Any edit to `tools/hooks/scratch-guard.js#checkRedLane`, to the witness line, to the commit
  grader, or to the runner's ledger write.
- Any kit version, which the lander's `mint` moves.
- Any edit to a CLOSED spec of this build. Each correction is stated here.

### Edges

- **consumes-from** external — the nine-field ledger row and its head field, landed by
  TOOL-aFrugalTurnstile-4. Without the head field no row can be bounded and the lane never opens.
- **consumes-from** external — the lane of this build's CLOSED unit 8, which this unit corrects:
  `readOpenReds`, `checkRedLane` and step 10 of the write gate. This spec states the correction;
  spec 8's sentence that a row stands until the runner next records its leg is superseded by §4.
- **consumes-from** external — the policy kit's landed-revision read, `policy-shim.sh landed`
  behind `readLandedRevision`. Without it only a row whose head is `HEAD` opens the lane.
- **hands-off** external — the bug-class record `carried-forward-row-read-as-current`, which the
  main loop writes under `memory/gotchas/` with its index render, citing this unit's arm class.
- **hands-off** external — the guard of the `scratch-guard self-test` leg, which names no path
  under `tools/policy/` although the suite runs the policy kit; review item M5 owns it, and S3
  adds one more read of that kit.
- **hands-off** external — the adopter default of `LEG_MANIFEST`, review item M7. Until it is
  seeded the lane is closed on a default install, at the hook as at the grader.

## 4. Design

### Evidence

Read at `d5b59614`, the branch tip.

- **The reader tests the status and nothing else.** `tools/hooks/scratch-guard.js@e68c8d09522a:1180`
  admits any row of three or more fields whose third field is `fail` or `timeout`.
- **The runner carries rows forward.** `tools/run-gates/run-gates.sh@970e3e89a3e9:5404` appends
  every old row whose name this run did not measure, so a red of a held or guard-skipped leg
  stands until a run measures that leg again.
- **Every row the runner writes carries its head.** `tools/run-gates/run-gates.sh@970e3e89a3e9:5392`
  writes nine tab-separated fields, the ninth `HEAD_SHA`, which is the full sha `rev-parse` printed
  at `tools/run-gates/run-gates.sh@970e3e89a3e9:114`. A carried-forward row keeps the head of the
  run that executed it, by the comment at line 5354 of the same blob.
- **The primary checkout's ledger opens the lane today.** `readOpenReds` over the primary git
  directory returned 9 names, all 9 from five-field rows (PINNED, 2026-11-12, re-measured for
  this spec). The hook run against the primary checkout, by AC2's command, exited 0 and printed
  the admitting witness naming those legs (PINNED, 2026-11-12).
- **The call site holds everything the bound needs.** At
  `tools/hooks/scratch-guard.js@e68c8d09522a:1336` the gate holds `top`, the worktree's toplevel,
  and `tools/hooks/scratch-guard.js#readConfKey` reads one conf key from bytes.
- **The conf names the manifest.** This repository's `.memory-tree.conf` sets `LEG_MANIFEST` to
  `tools/gate-legs.json`, a JSON list of rows each carrying `name`. The shipped example conf sets
  the key blank.
- **The landed revision is read in one place.** `tools/policy/policy-mirror.js@3b45d08fa574:93`
  defines `readLandedRevision`, which runs `policy-shim.sh landed` and returns the full sha. The
  module exports `readPolicy` and `PolicyRefusal` only, at line 188 of that blob. The hook already
  finds the module through `tools/hooks/agent-cap.js#resolvePolicyHelper`.
- **The policy suite's two lane cases keep their order.** In
  `tools/policy/check_policy.py@743b1e144707:4812` the adapter runs over the pass commit and step
  4 sends the product write with no commit between, so the row's head is `HEAD` there. Steps 5
  and 8 expect a refusal. No step expects an admit after `HEAD` moved, so the cases need no edit.

### The four bounds

A row of the ledger is an open red when all of these hold, tested in this order.

| Bound | Test | A row that fails it |
|---|---|---|
| form | the row splits into nine or more tab-separated fields, and its third is `fail` or `timeout` | a legacy five-field row, a short row, an `ok` or `retried` row |
| head shape | the ninth field is a full hex sha | a row whose head is empty |
| manifest | the first field equals the `name` of a row of the manifest `LEG_MANIFEST` names | a leg the manifest dropped |
| head place | the ninth field is `HEAD`, or is in the unlanded set | a row measured at a landed commit, or on another line of history |

The unlanded set is what `git rev-list HEAD --not <landed>` prints in the toplevel, where
`<landed>` is the sha `readLandedRevision` returns. It is the commits of this branch the landed
revision does not reach. `HEAD` itself is tested first and by equality, so a red measured at a
`HEAD` that is already landed still opens the lane: that is a full bar's red in the primary
checkout.

### The flow of `readOpenReds(gitDir, top)`

1. An empty `gitDir` or an empty `top` answers the empty list, as does an absent or unreadable
   ledger.
2. The rows that pass the form and head-shape bounds are the candidates. With no candidate the
   reader returns the empty list and reads nothing further, which is every refusal in a worktree
   whose ledger holds no red.
3. The reader takes `LEG_MANIFEST` from `<top>/.memory-tree.conf` through `readConfKey`, and reads
   that file under `top` from the working tree as JSON. A blank or absent key, an unreadable file,
   a parse failure, and a value that is no list each answer the empty list. Candidates whose name
   no row carries are dropped.
4. `git rev-parse --verify -q HEAD` in `top` gives `HEAD`. A failure answers the empty list.
5. Only where a surviving candidate's head differs from `HEAD` does the reader ask for the
   unlanded set: the policy helper's `readLandedRevision(top)`, then the one `rev-list`. No
   helper beside the hook, a refused read and a failed `rev-list` each leave the set empty, so
   only rows at `HEAD` open the lane.
6. The names of the candidates that pass the head-place bound are returned in ledger order.

Every failure closes the lane. The reader never throws: each read sits in its own guard, as the
ledger read does today.

The call in `checkRouted` becomes `readOpenReds(gitDir, top)`. Nothing else of `checkLane` moves,
so the key is still read first; review item L1 owns that order.

### Why the head bound keeps the lane useful

A pass commits, the pass legs run at that commit, and a red row carries that commit as its head.
The fix is written with `HEAD` at the row's head. The fix commits under its `Red-fix:` trailer and
`HEAD` moves; the row's head is now an unlanded ancestor, so a second write for the same red is
still admitted until a run measures the leg again. Once the branch lands, the row's head is
reachable from the landed revision and the row is closed for good.

### The suite

The lane block of `tools/hooks/scratch-guard.test.sh` writes its ledger through `write_ledger`,
whose rows carry the literal head `h`. Under S1 no such row is open, so every existing arm that
expects an admit reds. The block is rebuilt on the fixture below, in the linked worktree it
already uses: the worktree's conf gains `LEG_MANIFEST`, a manifest file names the legs, the
worktree gains the commits the fixture needs, and `write_ledger` plants a head per row. The two
L-AC1 calls pass the toplevel as the second argument.

The new arm class holds these arms, each sent through the real hook as the L-AC2 rows are.

| Arm | Ledger | Expected |
|---|---|---|
| a `fail` row with an empty head | one such row | the route refusal stands |
| a `fail` row whose head is a landed commit | head `C0` | the route refusal stands |
| a `fail` row for a leg absent from the manifest | head `HEAD` | the route refusal stands |
| a legacy five-field `fail` row | no head field | the route refusal stands |
| a `fail` row whose head is on another line of history | head `C3` | the route refusal stands |
| a held leg redded at `HEAD` | head `HEAD`, manifest row with `chunk` `selftests` | the witness naming the leg |
| a `fail` row at an unlanded ancestor of `HEAD` | head `C1` | the witness naming the leg |

### The fixture

One git repository with no remote, used by AC3 to AC5 and by the arms. `<F>` is its toplevel.

- Branch `main` holds commit `C0`. Branch `work`, checked out, holds `C1` then `C2` above `C0`,
  so `HEAD` is `C2`. Branch `side` holds `C3` above `C0`.
- `<F>/.memory-tree.conf` sets `MEMORY_ROOT`, a `ROUTED_PATHS` of `src/`, and `LEG_MANIFEST` to
  `legs.json`. No role index and no policy file exist, so the lane key reads its default.
- `<F>/legs.json` is a list whose rows are named `at-head`, `held-at-head`, `unlanded`, `landed`,
  `no-head`, `legacy`, `foreign` and `green`. The row `held-at-head` carries `chunk` `selftests`.
- The ledger under the repository's git directory holds these rows.

| Name | Status | Head | Fields | Open |
|---|---|---|---|---|
| `at-head` | `fail` | `C2` | nine | yes |
| `held-at-head` | `timeout` | `C2` | nine | yes |
| `unlanded` | `fail` | `C1` | nine | yes |
| `landed` | `fail` | `C0` | nine | no |
| `no-head` | `fail` | empty | nine | no |
| `legacy` | `fail` | none | five | no |
| `gone` | `fail` | `C2` | nine | no, the manifest lacks it |
| `foreign` | `fail` | `C3` | nine | no |
| `green` | `ok` | `C2` | nine | no |

Every probe over `<F>` runs with `GOV_DEFAULT_BRANCH=main`, so `C0` is the landed revision. For a
pass's probe the repository is built under `%TEMP%` in a short-named folder, outside the worktree.

### What it does not check

- Whether the write fixes the red. Any product path is admitted while a row is open.
- Whether the tree the run graded was clean. A run over a dirty tree stamps `HEAD`, so a red
  caused by uncommitted content reads as a red of `HEAD`.
- Whether a later commit of the branch already fixed the red. A row at an unlanded ancestor stays
  open until a run measures its leg again or the branch lands; for a held leg that is the next
  full bar.
- A ledger edited by hand, which is read like the runner's, and a manifest edited in the working
  tree, which is read uncommitted.
- A clone that works on its landed branch with no remote. There the landed revision is the local
  branch tip, the unlanded set is empty, and the lane closes at the fix commit until the leg is
  measured again.
- A red whose retry failed, which the runner records as `retried`. Review item M4 owns it.

### Inventory

| Minted | Where | Cell |
|---|---|---|
| the export `readLandedRevision` | `module.exports` of `policy-mirror.js` | `js.function`; `lexicon.py --suggest` answered OK on 2026-11-12, and the function already carries the name |

`readOpenReds` keeps its name and gains a parameter. No new function is required; a builder that
extracts a helper names it by the lexicon.

### Migration

None for data. A caller of `readOpenReds` that passes one argument receives the empty list; the
tree holds one caller outside the suite, the lane's own.

### Rollout

No new switch. `bar.inline-red-fixes` gates the lane as before, and this unit only narrows what
the lane admits. On landing, the primary checkout's lane closes with no action there.

### Files touched (estimate)

- `tools/hooks/scratch-guard.js`
- `tools/hooks/scratch-guard.test.sh`
- `tools/hooks/README.md`
- `tools/policy/policy-mirror.js`
- `tools/policy/README.md`
- `help/red-fix-lane.md`

### Alternatives rejected

- **Only rows of the ledger's newest run.** Rejected by the review record: a pass-leg run that
  does not measure a leg writes the ledger and would close the lane on that leg's bar red.
- **Only rows whose head equals `HEAD`.** Sound and stricter, as the skeptic of finding 4 said,
  but the lane would shut at the fix commit, and a second write for the same red would need a
  rerun first. The review's corrected fix names the ancestor range, and the brief asks for it.
- **Dropping the rows of held legs.** The rejected fix of finding 22. A held leg a full bar
  redded at the close is the case the lane was built for.
- **`readPolicy` returning the landed sha as a new field.** It changes the shape the mirror's
  parity case compares against the python reader. An export changes no return value.
- **The hook computing the landed revision itself.** A second derivation of one fact; the policy
  kit owns the remote ladder.
- **`git merge-base --is-ancestor` per row.** Two spawns per candidate row; the one `rev-list`
  answers every row.
- **Reading the manifest from `HEAD`'s tree.** One more spawn per refusal, and the runner that
  wrote the row read the working-tree file.

## 5. Production-readiness checklist

- security — the change narrows an admit and adds no write path. Every unreadable input closes
  the lane: the conf key, the manifest, `HEAD`, the landed revision. The ledger and the manifest
  are local files the writer can edit, as before; the commit grader's limits still bound what
  lands.
- perf / scale — a refusal in a worktree whose ledger holds no candidate row costs what it costs
  today. A candidate row adds the manifest read and one `rev-parse`; a candidate off `HEAD` adds
  the shim's landed read and one `rev-list` over the branch's unlanded commits.
- error / empty / loading states — an absent ledger, a blank key, a manifest that does not parse,
  an unborn `HEAD`, no policy kit and a refused landed read each answer per §4's flow, none with
  a throw.
- observability — the witness still names each open leg. A lane closed by a bound prints the
  gate's composed refusal and no reason; the help page states the bounds.
- risks — the suite's lane arms red until rebuilt on bounded rows, and the builder moves the
  linked worktree's `HEAD` to make the fixture's commits, which later arms of the suite may read.
  The policy suite's lane cases are expected to hold by the evidence above; the close's bar is
  where that is seen.
- testing — AC1 to AC7 are probes a pass runs. The arm class of §7 is the main loop's.
- migration — N/A — no stored shape moves; the reader tolerates every row form by closing on it.
- user docs — `help/red-fix-lane.md`, and the two kit READMEs, S6.

## 6. Acceptance criteria

`<primary>` is the first `worktree` path `git worktree list --porcelain` prints. `<F>` is the
fixture of §4. Each command runs from the toplevel of the worktree the unit is built in.

- **AC1** — When
  `node -p "JSON.stringify(require('./tools/hooks/scratch-guard.js').readOpenReds('<primary>/.git','<primary>'))"`
  runs, it prints `[]`.
  Red when: the form bound is absent, which prints the names of the legacy rows.
  fixture: the primary ledger held 9 red rows, each of five fields (PINNED, 2026-11-12); a ledger
  rewritten since holds no such row, and then AC3 is the criterion that can fail.
- **AC2** — When
  `printf '{"tool_name":"Write","cwd":"<primary>","tool_input":{"file_path":"<primary>/tools/hooks/scratch-guard.js","content":""}}' | CLAUDE_PROJECT_DIR=<primary> node tools/hooks/scratch-guard.js`
  runs, it exits 2, its stderr holds `BLOCKED by scratch-guard`, and no line holds
  `red-fix lane admits`.
  Red when: the call site still passes one bound-free read. At `d5b59614` the command exits 0
  and prints the witness.
  fixture: the same ledger as AC1. The hook decides and writes nothing.
- **AC3** — When
  `GOV_DEFAULT_BRANCH=main node -p "JSON.stringify(require('./tools/hooks/scratch-guard.js').readOpenReds('<F>/.git','<F>'))"`
  runs, it prints `["at-head","held-at-head","unlanded"]`.
  Red when: a bound is missing, which adds the name of the row that bound closes, or the reader
  tests a held leg's `chunk`, which drops `held-at-head`, or the bound is `HEAD` alone, which
  drops `unlanded`.
- **AC4** — When AC3's command runs with `GOV_DEFAULT_BRANCH=no-such-branch`, it prints
  `["at-head","held-at-head"]`; and when it runs again as AC3 spells it with the `LEG_MANIFEST`
  line taken out of `<F>/.memory-tree.conf`, it prints `[]`.
  Red when: a refused landed read throws or admits every ancestor, or a blank key reads as every
  leg.
- **AC5** — When
  `printf '{"tool_name":"Write","cwd":"<F>","tool_input":{"file_path":"<F>/src/a.txt","content":""}}' | GOV_DEFAULT_BRANCH=main CLAUDE_PROJECT_DIR=<F> node tools/hooks/scratch-guard.js`
  runs, it exits 0 and its one stderr line holds `at-head, held-at-head, unlanded` and no
  `landed,`; and when it runs again with the three open rows taken out of the ledger, it exits 2
  and prints no `red-fix lane admits`.
  Red when: the call site passes no toplevel, which refuses the first run, or a closed row still
  opens the lane, which admits the second.
- **AC6** — When
  `node -p "typeof require(require('path').resolve(process.argv[1])).readLandedRevision" tools/policy/policy-mirror.js`
  runs, it prints `function`.
  Red when: the export is absent, which prints `undefined`, as it does at `d5b59614`.
- **AC7** — When `grep -c 'closes when the leg next runs green' help/red-fix-lane.md` runs it
  prints 0, `grep -c 'LEG_MANIFEST' help/red-fix-lane.md` prints 1 or more,
  `grep -c 'since a row stands until the runner next' tools/hooks/README.md` prints 0, and
  `grep -c 'readLandedRevision' tools/policy/README.md` prints 1 or more.
  Red when: a text still says the lane waits for the leg's next green run and names no bound. At
  `d5b59614` the four print 1, 0, 1 and 0.

## 7. Gates

`scratch-guard self-test` · `agent-cap self-test` · `format-guard self-test` · `verifier fan-out self-test` · `review-join self-test` · `hook destinations self-test` · `policy fixtures` · `docs` · `install-prefix (shipped surface)` · `kit epoch (shipped bytes move, the version moves)` · `lexicon naming predicates` · `harness arms (fail branches armed or pinned)` · `memory hygiene` · `spec tokens (a spec's own names resolve)`

The first seven are owed by the manifest's guards over the files of §4. The brief's close is the
full bar once, without the self-tests and without the unattended kit gate leg, so the self-test
legs among them do not run there, and the main loop observes the arm below RED and then GREEN by
itself. The kit epoch leg expects the lander's `mint`.

New arm: tools/hooks/scratch-guard.test.sh · covers AC3 AC5 · the arm class "a carried-forward ledger row never opens the lane", seven arms over the fixture of section 4 sent through the real hook, staged by restoring the bound-free row test in a scratch copy of the hook so each refusal arm exits 0 · `FLOOR_ASSERTIONS`, raised by the assertions added

## 8. Open questions

none

## 9. Revision log

- rev-1 · 2026-11-12 · initial draft.

## 10. Reuse audit

The seam is the lane's own reader, `tools/hooks/scratch-guard.js#readOpenReds`, extended in place
as the review record's `Where` line names it, with `tools/hooks/scratch-guard.js#readConfKey` for
the conf key and `tools/policy/policy-mirror.js` for the landed revision, reached through
`tools/hooks/agent-cap.js#resolvePolicyHelper` as the lane's key read already is.
`python tools/codebase-map/reuse_lookup.py "bound a gate ledger row by its own head so a
carried-forward red row does not open the red-fix lane"` ranked name-stem neighbours only and
named no ledger reader. For a shared JavaScript reader of the ledger's head lineage, no existing
seam fits: the two ancestry tests of the runner, at
`tools/run-gates/run-gates.sh@970e3e89a3e9:3183` and line 3837 of that blob, are shell and
embedded python inside the runner and export nothing a hook can call. The recall probe's first
hit was TOOL-aFrugalTurnstile-4, whose spec states that a carried-forward row keeps the `run` and
`head` of the run that executed it and that a five-field row is never lineage-qualified, which is
the form bound here. `gotchas.py --for-paths` over the estimate selected
`fixture-passes-by-finding-nothing`, which is why AC1 names AC3 as its liveness, and
`empty-field-collapses-unless-it-is-last`, which is why the reader splits on the tab and counts
fields with the row's empty `full` field kept.

Where the review record and the source disagreed: nothing. Its probe figures were re-measured
and held.

Recall terms used: `python tools/memory-recall/query.py "which reader bounds a carried-forward
gate ledger row by the head it was measured at" --terms "gate ledger carried-forward row head
lineage red-fix lane readOpenReds landed revision stale fail"`
