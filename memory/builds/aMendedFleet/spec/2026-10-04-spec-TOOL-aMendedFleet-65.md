# TOOL-aMendedFleet-65 — the lander mints kit versions, so a branch owes no bump

**Status:** CLOSED · rev-3 · 2026-10-05 · node a · Tier-2 · base 7af5f564 · streams tooling · ratified 2026-10-04 · order 65

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-04-build-TOOL-aMendedFleet-65-1-acceptance-ledger.md](../build/2026-10-04-build-TOOL-aMendedFleet-65-1-acceptance-ledger.md) | journal | — |
| [2026-10-06-review-TOOL-aMendedFleet-1-closing-diff-round1.md](../reviews/2026-10-06-review-TOOL-aMendedFleet-1-closing-diff-round1.md) | diff-review | KICK-aMendedFleet-1 KICK-aMendedFleet-2 KICK-aMendedFleet-3 KICK-aMendedFleet-4 PLAY-aMendedFleet-1 PLAY-aMendedFleet-2 PLAY-aMendedFleet-3 PLAY-aMendedFleet-4 TOOL-aMendedFleet-1 TOOL-aMendedFleet-2 TOOL-aMendedFleet-3 TOOL-aMendedFleet-4 TOOL-aMendedFleet-5 TOOL-aMendedFleet-6 TOOL-aMendedFleet-7 TOOL-aMendedFleet-8 TOOL-aMendedFleet-9 TOOL-aMendedFleet-10 TOOL-aMendedFleet-11 TOOL-aMendedFleet-12 TOOL-aMendedFleet-13 TOOL-aMendedFleet-14 TOOL-aMendedFleet-15 TOOL-aMendedFleet-16 TOOL-aMendedFleet-17 TOOL-aMendedFleet-18 TOOL-aMendedFleet-19 TOOL-aMendedFleet-20 TOOL-aMendedFleet-21 TOOL-aMendedFleet-22 TOOL-aMendedFleet-23 TOOL-aMendedFleet-24 TOOL-aMendedFleet-25 TOOL-aMendedFleet-26 TOOL-aMendedFleet-27 TOOL-aMendedFleet-28 TOOL-aMendedFleet-29 TOOL-aMendedFleet-30 TOOL-aMendedFleet-31 TOOL-aMendedFleet-32 TOOL-aMendedFleet-33 TOOL-aMendedFleet-34 TOOL-aMendedFleet-35 TOOL-aMendedFleet-36 TOOL-aMendedFleet-37 TOOL-aMendedFleet-38 TOOL-aMendedFleet-39 TOOL-aMendedFleet-40 TOOL-aMendedFleet-41 TOOL-aMendedFleet-42 TOOL-aMendedFleet-43 TOOL-aMendedFleet-44 TOOL-aMendedFleet-45 TOOL-aMendedFleet-46 TOOL-aMendedFleet-47 TOOL-aMendedFleet-48 TOOL-aMendedFleet-49 TOOL-aMendedFleet-50 TOOL-aMendedFleet-51 TOOL-aMendedFleet-52 TOOL-aMendedFleet-53 TOOL-aMendedFleet-54 TOOL-aMendedFleet-55 TOOL-aMendedFleet-56 TOOL-aMendedFleet-57 TOOL-aMendedFleet-58 TOOL-aMendedFleet-59 TOOL-aMendedFleet-60 TOOL-aMendedFleet-61 TOOL-aMendedFleet-62 TOOL-aMendedFleet-63 TOOL-aMendedFleet-64 TOOL-aMendedFleet-66 TOOL-aMendedFleet-67 TOOL-aMendedFleet-68 TOOL-aMendedFleet-69 TOOL-aMendedFleet-70 TOOL-aMendedFleet-71 TOOL-aMendedFleet-72 TOOL-aMendedFleet-73 TOOL-aMendedFleet-74 TOOL-aMendedFleet-75 TOOL-aMendedFleet-81 TOOL-aMendedFleet-82 TOOL-aMendedFleet-83 TOOL-aMendedFleet-84 TOOL-aMendedFleet-85 TOOL-aMendedFleet-86 TOOL-aMendedFleet-87 TOOL-aMendedFleet-88 TOOL-aMendedFleet-89 TOOL-aMendedFleet-90 TOOL-aMendedFleet-91 TOOL-aMendedFleet-92 TOOL-aMendedFleet-93 TOOL-aMendedFleet-94 TOOL-aMendedFleet-97 TOOL-aMendedFleet-98 TOOL-aMendedFleet-99 TOOL-aMendedFleet-100 TOOL-aMendedFleet-101 TOOL-aMendedFleet-102 TOOL-aMendedFleet-103 TOOL-aMendedFleet-104 TOOL-aMendedFleet-105 |

<!-- /gen:spec-records -->

## 1. Goal

Today every branch that moves a shipped byte of a kit must bump that kit's version on the branch,
because the `kit epoch` and `verdict epoch` legs red a branch bar otherwise. Two branches bumping one
kit then conflict on the version line, a branch bumped early must bump again after its next move, and
the report counted version-only hunks as 71 of the 146 conflict hunks in merge `5cb052dab`. Main has
never published a duplicate version, so the harm is churn, not corruption. This unit moves the bump to
the one place that knows the final tip: the lander mints the version while it prepares the landing,
and the two epoch legs stop demanding a bump anywhere but at the push boundary.

## 2. Scope (IN)

- **S1** — A new verb, `python tools/govkit/govkit.py mint --base <rev> [--head <rev>]`. For every
  registry entry declaring a version, it takes the epoch verdict over `<base>..<head>` that
  `cmd_epoch` takes today, reading the version value from the WORKING TREE rather than from `HEAD`.
  An entry whose verdict would be FAILED gets a new value: the working-tree value with its last
  dotted component plus one. The verb writes that value on the entry's `version_from` line, writes
  every other carrier of that kit through unit 64's `write_version_carriers`, then runs the entry's
  declared `[[regenerate]]` argv, the next command unit 64's `--fix` prints. It prints one line per
  entry, `mint: <eid> · <old> -> <new>`, or `· clean`, or the announced `· skip` epoch prints for an
  entry with no declared version. `--head` defaults to `MERGE_HEAD` while a merge is in progress and
  to `HEAD` otherwise. Exit 0 when every write and regenerate succeeded, 1 on an unresolvable base, a
  failed write or a regenerate that exits non-zero, 2 on an unreadable registry. Observed by AC1, AC2,
  AC6.
- **S2** — The epoch verdict is computed ONCE. The per-entry body of `cmd_epoch` becomes a function,
  `derive_epoch_state`, that `cmd_epoch` and S1 both call, so the verb that mints and the leg that
  grades cannot disagree about which entry owes a bump. `cmd_epoch`'s printed lines and exit codes are
  unchanged by the extraction. Observed by AC2.
- **S3** — `tools/push-main.sh --prepare` makes its merge as today, runs the minter with `--base`
  set to the advertised tip and `--head` set to the branch tip, and, when the minter wrote anything,
  adds it and rewrites that merge in place with `git commit-tree`: the same two parents, today's
  subject, the minted tree. The minted value therefore enters through the prepared merge itself,
  which `cmd_epoch` already counts as a bump for every move the merge contains, and the idempotency
  check and `check_prepared_merge` still see one merge whose first parent is the tip. A minter exit other than
  0 aborts the merge, checks the branch back out unmoved, prints the minter's lines and returns 1,
  the shape of the CONFLICT refusal. Unit 3's merge-loss check keeps the place its S5 gives it, after
  a merge commit exists and before the compare-and-swap `update-ref`, so it grades the committed,
  minted merge. Observed by AC1, AC3, AC6.
- **S4** — The attended landing, `push-main.sh` with no argument, runs the minter after its reconcile
  step on every attempt, with `--base` set to the fetched remote tip. When the minter wrote anything,
  it commits the writes on the default branch with the subject
  `mint: kit versions onto <remote>/<branch> at <sha8>`, which names no unit id, with `--no-verify`
  for S3's reason; the pre-push bar grades it. A minter exit other than 0 restores the tree to `HEAD`
  and exits 1. Observed by AC4.
- **S5** — THE MINTER IS RESOLVED, NEVER SPELLED. The lander finds the deployer the way unit 3's
  merge-loss call finds its kit from this script, with the python resolver that unit adds. Where no
  deployer resolves, which is every adopter because govkit stays in gov, both landing paths print one
  line saying versions were not minted and why, and land as they do today. Observed by AC5.
- **S6** — THE OBLIGATION BINDS AT THE PUSH BOUNDARY ONLY. `cmd_epoch` reads `GATE_PUSH_BASE`, which
  `.githooks/pre-push` exports from git's own ref line and unsets for a branch push. When it is set and
  no `--base` is given, it is the base, and every FAILED line stands as today. An explicit `--base`
  grades as today too, whatever the environment: it is the caller asking for the whole verdict. When
  neither is given, an entry whose only fault is a move no bump dates prints
  `epoch: <eid> · owed at the lander · moved in <sha10> (<n> files)` and does not count as failed;
  every other FAILED line, an unresolvable base included, stands. Observed by AC7, AC8.
- **S7** — `tools/memory-tree/check-verdict-epoch.sh` takes the same rule: with `GATE_PUSH_BASE` set
  and no argument, or with an explicit base argument, it grades as today, and with neither its
  engine-moved-constant-did-not finding prints one `owed at the lander` line and exits 0. Its
  misconfiguration exit 2 is unchanged. Its bump search reads a merge against its FIRST parent, as
  `cmd_epoch`'s does, so the value S3 mints into the prepared merge dates the branch's moves at the
  push boundary. Observed by AC9.
- **S8** — The `push-main.sh` usage header, `cmd_epoch`'s docstring and the `check-verdict-epoch.sh`
  header each say where the bump is now made and what the off-boundary run does NOT check. Observed
  by AC10.
- **S9** — New arms in `tools/push-main.test.sh`, `tools/govkit/selftest.py` and
  `tools/memory-tree/check-verdict-epoch.test.sh` stage the moves AC1, AC7 and AC9 stage.
  NOT OBSERVED by a criterion here: those suites run once at the close, and each arm is declared
  under `New arm:` in §7.
- **S10** — `memory/map/generated/symbols.json` is regenerated for the new definitions.
  NOT OBSERVED by a criterion here: `python tools/codebase-map/gen_map.py --check` at the close is its
  check, and §7 names the leg that reads it.

## 3. Non-goals (OUT)

- Writing the carriers. Unit 64 owns the writer that turns one `version_from` value into every marker
  `check-kit-versions.sh` pairs, and the regenerate argv each kit declares; this unit calls both.
- Choosing a bump SIZE other than the last component plus one. A minor-versus-major judgement is the
  call the epoch rule refuses to make, and the minted value only has to differ.
- Minting a kit that declares no version, such as the `push-main` entry itself. Epoch announces those
  as `skip` today and the minter does the same.
- Rewriting the version history of any landed commit, or renumbering a value main already carries.
- Any change to `check-kit-versions.sh`; it grades agreement, which the carrier writer keeps.
- Re-stamping the kickoff manifest. A minted carrier on its `watch:` line, such as
  `check-memory-hygiene.sh`, is a watched move the lander cannot audit, so its C5 reds at the push
  bar; the remedy is the one it prints, a re-stamp committed on the prepared branch, and a later
  unit owns making the lander say so before the bar does.

### Edges

- **consumes-from** `TOOL-aMendedFleet-64` — `write_version_carriers`, which S1 calls for every marker
  of a minted kit, and the `[[regenerate]]` argv its `--fix` names; without them the minter moves one
  line and `kit version markers` reds on the rest.
- **consumes-from** `TOOL-aMendedFleet-3` — the python and kit resolution unit 3 adds to
  `tools/push-main.sh` for its merge-loss call, which S5 reuses; without it this unit would add a
  second resolver to the same script.
- **hands-off** external — the adopter-facing wording of the runbook's kit-version rule, which still
  holds: the bytes move and the version moves, and only gov's lander makes the move.

## 4. Design

### Evidence

Read at base `7af5f564`, re-verified 2026-10-04.

- `cmd_epoch` in `tools/govkit/govkit.py` grades, per registry entry, whether every commit in
  `<base>..HEAD` that moves an `EPOCH_ROLES` byte is an ancestor of a commit that changes the version
  VALUE. A merge whose value differs from its first parent counts as a bump for every move it
  contains, and the BASE votes first: an unchanged value against the base is FAILED outright.
- Its default base is the merge-base with `origin/<default>`. On a branch that moved a kit without
  bumping it, that is a FAILED line and exit 1, which is the per-branch obligation.
- `.githooks/pre-push` exports `GATE_PUSH_BASE` as the remote's sha for the default branch before the
  bar runs, overwriting an inherited value, and unsets it for a branch-bar push. No leg reads it
  today. Both epoch legs carry no `guard`, so they run on every bar, scoped or full.
- `cmd_prepare` in `tools/push-main.sh` merges the branch with `--no-ff` at the detached advertised
  tip, refuses a conflict with the branch checked back out unmoved, and treats a `HEAD` that is
  already a two-parent merge onto the tip as prepared. `check_prepared_merge` takes the nearest
  first-parent merge, so a commit stacked on it would pass `--land` but defeat that idempotency check;
  S3 keeps the mint inside the merge for that reason.
- The `push-main` registry entry declares `version_from = { none = ... }`, so the lander itself has no
  version to bump. The deployer is gov-only: the runbook says `govkit.py epoch` stays in gov.
- Version carriers are many per kit. The memory-tree value sits in nine tracked files and the
  unattended value in at least six, PINNED from a `git grep -l` of each value on 2026-10-04, and the
  `kit version markers` leg pairs them.

### The rule, stated once

For an entry E, a base B and a head H, with V the value in the working tree:

```
moved(E)  = rev-list --no-merges H ^B -- <E's EPOCH_ROLES paths>     non-empty
state(E)  = derive_epoch_state(E, B, H, now = V)                      the cmd_epoch verdict
mint(E)  iff  moved(E) and state(E) is FAILED          new value = V with its last component + 1
```

At `--prepare`, B is the advertised tip and H is the branch tip, so a branch that bumped after its
last move mints nothing and its merge carries its own bump; a branch that did not, or bumped and then
moved again, gets one fresh value in the merge. Two landers racing on one kit both mint the same next
value from the same tip; the second's push is rejected as a race, it re-prepares onto the new tip,
and its mint then reads a value equal to the tip's and moves it one further.

### Inventory

- `cmd_mint` and `derive_epoch_state` — cell `py.function`; both answered OK by
  `python tools/lexicon/lexicon.py --suggest <name> --as py.function`.
- `run_minter` in `tools/push-main.sh` — cell `sh.function`; answered OK the same way.
- `mint` joins `govkit.py`'s `USAGE` and its `main` dispatch beside `epoch`.

### Files touched (estimate)

- `tools/govkit/govkit.py`
- `tools/govkit/selftest.py`
- `tools/push-main.sh`
- `tools/push-main.test.sh`
- `tools/memory-tree/check-verdict-epoch.sh`
- `tools/memory-tree/check-verdict-epoch.test.sh`
- `memory/map/generated/symbols.json`

### Rollout

Unit 64 lands its carrier writer first and unit 3 its resolver; this unit is ordered after both. The
build's own landing is the first lander run that mints, so its close exercises S3 on every kit the
build moved. From then on a pass leaves the version alone, and a spec saying a bump is owed at the
close is satisfied by the lander.

### Alternatives rejected

- **A separate mint commit stacked on the prepared merge.** It passes `--land`, but `cmd_prepare`'s
  idempotency check reads `HEAD^2`, so a re-prepare after a race would stack a second merge.
- **Minting in the unattended driver before `--prepare`.** The attended path would not mint, and the
  tip the driver reads can move before the merge is made.
- **A `GOV_MINT_CMD` key in `.githooks/gate-env.sh`.** It adds a declared command the lander would
  have to vet the way the hook vets `GOV_GATE_CMD`, for one gov-only call a resolver already finds.
- **Detecting the push boundary from the graph,** a prepared merge onto the merge-base. It misses the
  attended path, whose tip is the local default branch and carries no such merge.

## 5. Production-readiness checklist

- security — the minter is a tracked file found by the same resolver unit 3 vets, run with a fixed
  argv; the only new input is the advertised tip, a sha the lander already resolved. The regenerate
  commands it runs are the ones each kit declares in its own tracked `kit.toml`, the same argv
  `govkit update` already runs.
- perf / scale — one registry read and one epoch pass, the cost of the `kit epoch` leg, about the
  same few seconds, once per landing attempt.
- error / empty / loading states — no deployer, a clean verdict and a skipped entry each print one
  line; a failed write refuses the landing unmoved.
- observability — every minted kit is one `mint:` line in the lander's output, and the value change
  is in the prepared merge's own diff against its first parent.
- risks — a race re-mints one value further, so a published value can skip a number; the epoch rule
  needs a different value, never a contiguous one.
- testing — AC1 to AC10 directly; the three arms in S9.
- migration — none: a branch that still bumps by hand lands exactly as today.
- user docs — the headers in S8; the runbook's kit-version rule stays true as written.

## 6. Acceptance criteria

- **AC1** — When, in a fixture made by `git clone --bare` of the unit's tip and a working clone of
  that bare repository under a short `%TEMP%` path, a branch commits a comment line in
  `tools/runlog/extract.py` and `bash tools/push-main.sh --prepare --slug tMint` runs on it, the
  prepared merge's diff against its first parent moves `KIT_RUNLOG_VERSION` in
  `tools/runlog/runlog_lib.py` to the tip's value plus one, and stdout carries one `mint: runlog` line.
  Red when: the merge carries the move and the old value.
  cost: one local clone and one bare clone, about a minute on node a.
  figure: the expected value is DERIVED from the tip at observation time.
- **AC2** — When `python tools/govkit/govkit.py epoch --base <tip>` then runs at the AC1 merge, it
  prints `epoch: runlog · clean`, and `bash tools/check-kit-versions.sh` exits 0 there.
  Red when: the merge leaves a runlog marker carrying the old value, or the verdict is FAILED.
- **AC3** — When `--prepare` runs a second time on the AC1 branch, `git rev-parse HEAD` is unchanged
  and no second `mint:` line names a new value.
  Red when: a second merge is stacked or the value moves again.
- **AC4** — When, in the same fixture, the default branch takes the same comment commit and
  `bash tools/push-main.sh` runs from it, the default branch it pushes to the bare repository carries
  a `mint: kit versions onto` commit whose diff moves `KIT_RUNLOG_VERSION`.
  Red when: the attended path pushes the move with the old value.
  fixture: a fresh clone has no `core.hooksPath`, so no bar runs on that push; the observation is the
  lander's mint, not the gate.
- **AC5** — When the fixture branch commits the removal of `tools/govkit/govkit.py` and `--prepare`
  runs, stdout carries one line saying versions were not minted and naming the missing deployer, and
  the prepared merge exists.
  Red when: the lander refuses, or prepares silently.
- **AC6** — When the fixture branch commits a TOML syntax error into `tools/govkit/registry.toml` and
  `--prepare` runs, it exits 1, prints the minter's refusal, and `git rev-parse HEAD` equals the
  branch tip before the call. This is the staged break for S3's refusal.
  Red when: a merge is kept, or the exit is 0.
- **AC7** — When `python tools/govkit/govkit.py epoch` runs on the AC1 branch tip before any prepare,
  with `GATE_PUSH_BASE` unset, it prints `epoch: runlog · owed at the lander` and exits 0.
  Red when: it prints FAILED for runlog or exits 1.
- **AC8** — When the same call runs with `GATE_PUSH_BASE` set to the tip's sha, it prints a FAILED
  line for runlog and exits 1. This is the staged break proving the boundary still binds.
  Red when: the push boundary accepts the unbumped move.
- **AC9** — When the fixture branch commits a behaviour line into
  `tools/memory-tree/check-memory-hygiene.sh` and `bash tools/memory-tree/check-verdict-epoch.sh`
  runs at its tip, it exits 0 with one `owed at the lander` line when `GATE_PUSH_BASE` is unset, and
  exits 1 when it is set to the tip's sha.
  Red when: either run takes the other's exit.
- **AC10** — When `grep -n "mint" tools/push-main.sh tools/memory-tree/check-verdict-epoch.sh` runs,
  the usage header names the minting `--prepare` and the attended mint commit, and the epoch header
  names the push-boundary rule.
  Red when: a header still tells a branch to bump.

## 7. Gates

`kit epoch (shipped bytes move, the version moves)` · `verdict epoch (kit version dates the engine)` · `kit version markers` · `govkit selfcheck` · `govkit acceptance matrix` · `govkit refusal join` · `govkit selftest` · `codebase-map coverage + freshness` · `recall floor arms` · `install-prefix (shipped surface)` · `lexicon naming predicates` · `line length` · `spec tokens (a spec's own names resolve)` · `recall floor`

New arm: `tools/push-main.test.sh` · a fixture branch moving a runlog byte, prepared against the base lander, which merges the old value · none
New arm: `tools/govkit/selftest.py` · `mint` over a fixture registry with one moved kit, against a base govkit with no such verb · none
New arm: `tools/memory-tree/check-verdict-epoch.test.sh` · an unbumped engine move with and without `GATE_PUSH_BASE`, against the base gate, which reds both · none

## 8. Open questions

- **F1 — Where does the minted value enter the history?**
  Options: inside the prepared merge; a mint commit stacked on it; the unattended driver before
  `--prepare`. A stacked commit defeats `cmd_prepare`'s idempotency check, and the driver misses the
  attended path and reads a tip that can move.
  RESOLVED (agent, 2026-10-04, delegated): inside the prepared merge, and as its own commit on the
  attended path, which has no prepared merge, per S3 and S4.
- **F2 — How does the lander find the minter?**
  Options: a declared `GOV_MINT_CMD` key; the deployer resolved beside the lander, announced when
  absent. A key is new surface the hook would have to vet; unit 3 already adds a resolver here.
  RESOLVED (agent, 2026-10-04, delegated): resolve it with unit 3's resolver, per S5.
- **F3 — Is ending the per-branch obligation a second mechanism?**
  Options: one unit; split the epoch legs' boundary rule into its own unit. Neither half can land
  alone: minting with the legs unchanged leaves every branch bar red, and relaxing the legs with no
  minter lands moves under an old value.
  RESOLVED (agent, 2026-10-04, delegated): one unit, S1 to S7.
- **F4 — How does an epoch leg know it is at the push boundary?**
  Options: `GATE_PUSH_BASE` set; a prepared merge on `HEAD`'s first-parent line. The second misses
  the attended path, whose landing carries no prepared merge.
  RESOLVED (agent, 2026-10-04, delegated): `GATE_PUSH_BASE`, which only the default-branch push sets,
  per S6 and S7.

## 9. Revision log

- rev-1 · 2026-10-04 · initial draft, from a read of `cmd_epoch`, `cmd_prepare`, the attended
  landing, `check-verdict-epoch.sh`'s base rule and the hook's `GATE_PUSH_BASE` export at base.
- rev-2 · 2026-10-04 · S3 · cross-read with `TOOL-aMendedFleet-3`: its S5 runs the merge-loss check
  "after its merge", and this unit makes that merge `--no-commit` until the mint; S3 now places the
  check after the minted merge is committed, so the two edits to `cmd_prepare` compose. S10, §4 and
  §7: the two Python definitions move `memory/map/generated/symbols.json`, which the build's other
  Python-adding units declare with the coverage leg and this spec omitted.
- rev-3 · 2026-10-05 · S3, S4, S6, S7, §3 · found building. S3: `--no-commit` concluded by
  `git commit` fires the pre-commit staged legs over the whole landing diff, which `git merge` never
  fires, so the merge is made as today and rewritten with the minted tree by `git commit-tree`; S4's
  commit skips the hooks for the same reason. S6, S7: an explicit base grades as today, because the
  existing epoch self-test arms pass one and expect FAILED. S7: its `-G` search skipped merges, so
  the minted merge would not have dated the move at the push boundary. §3: the manifest seam.

## 10. Reuse audit

The seam extended is `cmd_epoch` in `tools/govkit/govkit.py`: its per-entry verdict becomes
`derive_epoch_state`, which the new verb calls, so minting is the inverse of the grade rather than a
second reading of history. The landing seam is `cmd_prepare` in `tools/push-main.sh`, whose
unmoved-branch refusal S3 reuses, and the resolver unit 3 adds to that script. `python
tools/codebase-map/reuse_lookup.py "bump a kit version when its shipped bytes moved, at landing"`
returned path-resolution helpers such as `resolve_kit_dir` and the `registry.toml` affordance seam,
and no existing minter; the scan names `.sh` as unscanned, so `git grep` over `tools/push-main.sh`
and `.githooks/` was the probe for the shell layer, and it found no version write in either. Recall
returned `TOOL-aBoundedVerdict-29` and `TOOL-dSettledRoster-4`, on bump remedies naming fewer carriers
than exist, which is why S1 calls unit 64's writer instead of writing one line, and the
`aRepatriatedFork` unit 15 spec that lifted the topological rule to every registry entry, which S2
keeps as the one verdict. Where the report and the tree disagree: none found; the 71 of 146 hunk
count was not re-measured and is the report's, PINNED at `ac65de998`.

Recall terms used: `python tools/memory-recall/query.py "where should kit versions be bumped, on the
branch or at landing, and why do version bumps conflict" --terms "kit version bump epoch govkit lander
push-main prepare carriers churn conflict hunks version_from"`
