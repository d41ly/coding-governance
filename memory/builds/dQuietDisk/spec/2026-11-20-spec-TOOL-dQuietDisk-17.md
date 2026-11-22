# TOOL-dQuietDisk-17 — `govkit update` skips a kit's verify check when nothing moved since its baseline

**Status:** WONTDO · rev-5 · 2026-11-22 · node d · Tier-2 · base ebab8b90 · streams tooling · ratified 2026-11-20 · order 5 · retired: section 8 F2, the reuse fires only on a run that fails or wrote nothing, and adds git processes

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-11-20-build-TOOL-dQuietDisk-1-agent-ledger.md](../build/2026-11-20-build-TOOL-dQuietDisk-1-agent-ledger.md) | journal | TOOL-dQuietDisk-1 TOOL-dQuietDisk-2 TOOL-dQuietDisk-3 TOOL-dQuietDisk-4 TOOL-dQuietDisk-5 TOOL-dQuietDisk-6 TOOL-dQuietDisk-7 TOOL-dQuietDisk-8 TOOL-dQuietDisk-9 TOOL-dQuietDisk-10 TOOL-dQuietDisk-11 TOOL-dQuietDisk-12 TOOL-dQuietDisk-13 TOOL-dQuietDisk-14 TOOL-dQuietDisk-15 TOOL-dQuietDisk-16 TOOL-dQuietDisk-18 TOOL-dQuietDisk-19 TOOL-dQuietDisk-26 TOOL-dQuietDisk-28 TOOL-dQuietDisk-36 TOOL-dQuietDisk-37 |
| [2026-11-20-prompt-TOOL-dQuietDisk-1-brief.md](../prompts/2026-11-20-prompt-TOOL-dQuietDisk-1-brief.md) | research | TOOL-dQuietDisk-1 TOOL-dQuietDisk-2 TOOL-dQuietDisk-3 TOOL-dQuietDisk-4 TOOL-dQuietDisk-5 TOOL-dQuietDisk-6 TOOL-dQuietDisk-7 TOOL-dQuietDisk-8 TOOL-dQuietDisk-9 TOOL-dQuietDisk-10 TOOL-dQuietDisk-11 TOOL-dQuietDisk-12 TOOL-dQuietDisk-13 TOOL-dQuietDisk-14 TOOL-dQuietDisk-15 TOOL-dQuietDisk-16 TOOL-dQuietDisk-18 TOOL-dQuietDisk-19 |
| [2026-11-20-prompt-TOOL-dQuietDisk-1-spec-brief.md](../prompts/2026-11-20-prompt-TOOL-dQuietDisk-1-spec-brief.md) | research | TOOL-dQuietDisk-1 TOOL-dQuietDisk-2 TOOL-dQuietDisk-3 TOOL-dQuietDisk-4 TOOL-dQuietDisk-5 TOOL-dQuietDisk-6 TOOL-dQuietDisk-7 TOOL-dQuietDisk-8 TOOL-dQuietDisk-9 TOOL-dQuietDisk-10 TOOL-dQuietDisk-11 TOOL-dQuietDisk-12 TOOL-dQuietDisk-13 TOOL-dQuietDisk-14 TOOL-dQuietDisk-15 TOOL-dQuietDisk-16 TOOL-dQuietDisk-18 TOOL-dQuietDisk-19 |
| [2026-11-20-prompt-TOOL-dQuietDisk-26-spec-task.md](../prompts/2026-11-20-prompt-TOOL-dQuietDisk-26-spec-task.md) | research | TOOL-dQuietDisk-8 TOOL-dQuietDisk-10 TOOL-dQuietDisk-19 TOOL-dQuietDisk-26 |
| [2026-11-22-prompt-TOOL-dQuietDisk-1-pins-task.md](../prompts/2026-11-22-prompt-TOOL-dQuietDisk-1-pins-task.md) | research | TOOL-dQuietDisk-1 TOOL-dQuietDisk-2 TOOL-dQuietDisk-3 TOOL-dQuietDisk-4 TOOL-dQuietDisk-5 TOOL-dQuietDisk-6 TOOL-dQuietDisk-7 TOOL-dQuietDisk-8 TOOL-dQuietDisk-9 TOOL-dQuietDisk-10 TOOL-dQuietDisk-11 TOOL-dQuietDisk-12 TOOL-dQuietDisk-13 TOOL-dQuietDisk-14 TOOL-dQuietDisk-15 TOOL-dQuietDisk-16 TOOL-dQuietDisk-18 TOOL-dQuietDisk-19 TOOL-dQuietDisk-26 |
| [2026-11-22-prompt-TOOL-dQuietDisk-17-1-spec-writer.md](../prompts/2026-11-22-prompt-TOOL-dQuietDisk-17-1-spec-writer.md) | journal | — |
| [2026-11-22-prompt-TOOL-dQuietDisk-17-reground-task.md](../prompts/2026-11-22-prompt-TOOL-dQuietDisk-17-reground-task.md) | research | TOOL-dQuietDisk-9 |

<!-- /gen:spec-records -->

## 1. Goal

`govkit update --write` runs each touched kit's own `[check]` argv twice: once as a baseline before
the first byte moves, and once in the verify pass after the writes. The analysis puts a check at
10 to 16 s [PINNED] (`memory/builds/dQuietDisk/build/2026-11-20-build-TOOL-dQuietDisk-19-analysis.md`,
row G4). This unit keeps the baseline's result keyed by the touched kits' installed bytes and a
fingerprint of the target. The verify pass reuses it when neither moved and no target-side program
ran in between. Every receipt, write, rollback decision and tally is unchanged. Section 4 says why
the saving is narrow, and section 8 asks whether it is worth building.

## 2. Scope (IN)

- **S1** — After the baseline loop, `update` reads the run key once, through `derive_check_key`. The
  key is the target's `HEAD`, read by `git rev-parse --verify HEAD`, and the target's status, read
  by `read_worktree_status` with its new keyword `strict=True`. The key holds only the status
  entries outside `.governance/outbox/`. It also holds the SHA-256 of every receipt-row path of every
  touched kit, read in-process. Under `strict=True` a non-zero `git status` exit returns None; the
  default keeps every other caller's answer. The key is read only when a touched kit declares a
  `[check]` argv. Observed by AC1 and AC3.
- **S2** — Before the verify loop's first kit, the key is read again only when all three hold:
  - no target-side program ran since the first read;
  - every path in `written_paths` is among those the held restores put back, and none of them
    returned a path it could not restore;
  - `install.check-reuse` reads `reuse` (S5).

  The five target-side programs are a `[[regenerate]]` argv, a hole probe, the step walk's branch,
  which also writes the receipt, a fragment merge with a non-empty population, and a default-gained
  adopter. When both reads are equal and neither is None, each touched kit takes its baseline
  `(state, detail, rc)` as `now` instead of calling `run_kit_check`. Every decision after it reads
  `now` exactly as today. `derive_check_reuse` makes the decision and returns the reason it refused.
  Observed by AC1 and AC2.
- **S3** — A moved key, a key either read returned as None, or a failed precondition runs
  `run_kit_check` in the verify pass as today, and prints as today. Observed by AC2 and AC3.
- **S4** — A reused verify announces itself. Its verify line gains the tail `· baseline reused: no
  target byte moved and no target program ran since it`. The closing tally gains `· reused <n>` as
  its last field, printed with its zero. The rollback order a held kit writes is unchanged.
  Observed by AC1 and AC3.
- **S5** — The switch. `install.check-reuse` is read through `read_policy_value`, in the shape of
  `read_baseline_mode`: a failed read returns `rerun` and prints one line naming the key. `reuse`,
  the default, is S2. `rerun` is today's verify pass: every verify runs. The key lands with its
  catalogue row, `owner = "dQuietDisk"`, a `summary` and a `usage`, and `help/reference/policy.md`
  is re-rendered. Observed by AC4.

## 3. Non-goals (OUT)

- No reuse across invocations. A check may read the machine outside the target, which no
  fingerprint holds, so a second `update` never reads the first one's results.
- No change to `run_kit_check`, `govkit check`, the baseline population `touched_kits`, or any
  rollback rule of DEPL-dCarriedReceipt-14.
- No skip of a held kit's verify by its held state alone. That would change the printed exits and
  the rollback order's text, which the verdict rule of the build forbids.
- No change to `blob_at` batching, which TOOL-dQuietDisk-16 built.
- No kit version bump by hand.

### Edges

none

## 4. Design

### The two runs today

All citations are read at `ebab8b90b`.

`run_kit_check` is the one runner of a kit's `[check]` (`tools/govkit/govkit.py#run_kit_check`). Its
docstring says `update` calls it twice per touched kit, and `_cmd_update` holds exactly those two
calls. The baseline loop runs it over `touched_kits` before the first write
(`tools/govkit/govkit.py@69a249216283:11324-11326`). The verify loop runs it again per touched kit
(`tools/govkit/govkit.py@69a249216283:12664`), after the held restores, the step walk, the
regenerate loop, the fragment merges and the default-gained adopters. A kit whose descriptor
declares no argv returns `landed-unmeasured` and starts no process. At `ebab8b90b`, 12 of the 30
registry entries declare a check argv [DERIVED: each `descriptor` of `tools/govkit/registry.toml`
read for `check.argv`].

TOOL-dQuietDisk-16 left `cmd_update` a wrapper that builds one blob batch and passes it to
`_cmd_update`. It does not touch the verify pass. Units 14 and 15 do not reach it either. The
receipt's `attestations` key (`tools/govkit/govkit.py#derive_kit_attestations`) attests that gov's
self-tests passed on a kit tree, and a kit's `[check]` grades the target's state, so the reuse reads
neither. The receipt write before the step walk sets that key
(`tools/govkit/govkit.py@69a249216283:12275`), and that write is one more reason the walk's branch
disables the reuse. Unit 15 is DEFERRED and nothing here consumes it.

### Why the reuse is narrow

`touched_kits` holds the claimed kits with a snapshotted row, plus the pre-write landing candidates
(`tools/govkit/govkit.py@69a249216283:11315-11316`). A snapshotted row is one whose verdict writes,
so a touched kit's bytes move unless the run puts them back. Only a held kit's are put back before
the verify pass: `write_kit_restore` runs for each held touched kit ahead of the step walk
(`tools/govkit/govkit.py@69a249216283:12248`). A kit whose regenerate was declined or refused keeps
its writes, so its key moves. Rev-3 named those kits as reuse cases, and that was wrong.

The reuse therefore fires only on a run where every write was put back by a held restore, or none
was made, and no target-side program ran. Every held kit takes the rollback arm whatever its check
says (`tools/govkit/govkit.py@69a249216283:12702`), and each one fails the run. So a held kit's
reused `now` reaches only the printed exits and the rollback order's `exits` line. A reuse cannot
move a decision there. The other firing case is a landing candidate that landed nothing. Its verify
reads `now`, and the fingerprint is what makes that safe.

The outbox exclusion is what lets the reuse fire at all. A hold from a conflicting three-way writes
an order under `.governance/outbox/`, as the `aHI-4` arms assert
(`tools/govkit/selftest.py@9f01615b4800:2349-2353`). The write lock is there too
(`tools/govkit/govkit.py#WRITE_LOCK_REL`). nicocares does not ignore that directory, and neither do
gov's fixture targets, whose `settle` commits with `git add -A`. A whole-status key would move on
every such run, and rev-3's AC1 could not have passed. No shipped check adopter names the outbox.
The count is 0 of 12 [DERIVED: `grep -c outbox` over each `adopt-*.sh` a check argv names].
The count naming `.governance/install.json` is 10 of 12 [DERIVED: `grep -l` over the same files].
The key still covers that file.

### Inventory

| Minted identifier | Kind | Naming cell | Graded by |
|---|---|---|---|
| `install.check-reuse` | policy key, values `reuse` and `rerun` | the catalogue's row | AC4 |
| `derive_check_key` | function in `govkit.py` | none | AC1, AC3 |
| `derive_check_reuse` | function in `govkit.py` | none | AC2 |
| `strict` | keyword of `read_worktree_status`, default False | none | AC3 |
| `reused` | the last field of the verify tally line | none | AC1, AC3 |

### Files touched (estimate)

`tools/govkit/govkit.py` · `tools/govkit/selftest.py` · `tools/policy/catalogue.toml` ·
`help/reference/policy.md` · `memory/map/generated/symbols.json`

- `help/reference/policy.md` is rendered by `render_playbook.py --reference`. The two new column-0
  functions join the symbol index, re-rendered by `gen_map.py --write`.
- The main loop re-renders gov's policy mirror, `.governance/policy.json`, with
  `policy.py mirror --write` after the pass commit, as it did for unit 18.
- TOOL-dQuietDisk-9's Files touched shares `tools/govkit/selftest.py`; unit 9 is order 6.
- The kickoff manifest's `watch:` line names none of these paths.
- `_cmd_update` is thousands of lines long, so each new local takes a `_ck` prefix no other block
  binds (`a-new-local-collides-in-a-long-function`).
- No shell line, heredoc loop or `$(...)` assignment is added.

### Alternatives rejected

| Alternative | Why it loses |
|---|---|
| A key per kit over its own paths alone | A kit's check reads files other kits write, so a verify skipped because its own bytes held could miss a break another kit's write caused. |
| Rev-3's per-kit `hash-object` and `status` | That design read two git processes per touched kit at both reads, on every write run. One run key costs two at each read, and the verify-side read is taken only when S2's preconditions hold. |
| A whole-status key with the outbox kept | gov writes the outbox itself, and a held run always writes an order there, so the key would move on every held run at nicocares and on gov's fixtures. |
| Persist results for the next `update` | Section 3: a check may read the machine outside the target. |
| Skip silently | govkit's verify pass announces every skip (its S8 comment), so a reused result reading as a run would claim a measurement nobody made. |

## 5. Production-readiness checklist

- security: N/A — reads of the target the verb already writes, and nothing new is written there.
- perf / scale: on a write run with a touched kit that declares an argv, the first read costs two git
  processes [DERIVED: one `rev-parse`, one `status`]. The verify side costs two more and the policy
  read when S2's preconditions hold. One `policy.py get` launched 8 git processes in gov's tree
  [PINNED 2026-11-22, `GIT_TRACE2_EVENT` file count]. The saving is one check per touched kit with
  an argv, at 10 to 16 s [PINNED] each, only where the reuse fires.
- error / empty / loading states: an unreadable key or switch reads as moved, and the check runs
  (S3, S5).
- observability: the announced tail and the tally field (S4).
- risks: a fingerprint that misses a change the check reads, such as a check that reads the outbox.
  The rule that any target-side program disables the reuse is the second defence. A future spawn
  site between the two loops that records nothing in the run's program list is not caught by any
  criterion here.
- testing: fixture updates in the deployer's suite (AC1 to AC4), a probe of the two new functions
  (AC2, AC3), and the adopters' read-only check (AC5).
- migration: none.
- user docs: `help/reference/policy.md` (S5).

## 6. Acceptance criteria

The saving, as a count. Each reused verify saves one `run_kit_check` call: the kit's `[check]` argv
and every process it starts, at 10 to 16 s [PINNED] (row G4, PINNED 2026-11-20). The run's saving is
the tally's `reused <n>`, so `n` calls.

The cost, as a count. On a write run with a touched kit that declares an argv, the unit adds two git
processes [DERIVED] and saves none unless the reuse fires. On an ordinary version-bump update every
touched kit's writes stand, no verify is reused, and the unit costs those two. Where it fires, it adds
two more git processes [DERIVED] and the policy read, which launched 8 [PINNED 2026-11-22]. It saves
`n` checks. The git count falls on that run only when the reused checks launch more than those
twelve [DERIVED: 2 + 2 + 8] between them, which no shipped check has been measured to do
(UNVERIFIED). Section 8 F2 weighs this.

- **AC1** — When `python tools/govkit/govkit.py update --target <t> --write` runs on the `aHI-4`
  `hg` fixture shape, its one kit `demo` has a check argv and is held by a conflicting row. The run
  prints `HELD BACK demo`. `demo`'s verify line carries the `baseline reused` tail, and the tally
  ends `reused 1`. The receipt, the target's tracked files, its outbox and the exit equal those of
  the same run on a second copy under `install.check-reuse = "rerun"`. So does every stdout line
  with that tail and that field removed.
  Red when: the reused kit's state or exits differ from a run that re-checks it, the reuse is
  silent, or the conflict order is missing from the outbox, so the outbox exclusion was not
  exercised (`fixture-passes-by-finding-nothing`).
  fixture: built in the deployer's suite through `build_gov17` and `build_target17`, on the
  template cache unit 11 gave `build_target`; the tail is matched on `demo`'s verify line alone,
  never over the whole output (`line-claim-matched-over-the-whole-output`).
  figure: the saving is one `run_kit_check` call [DERIVED at observation from the two tallies].
  It is the tally's `reused 1`, against the `rerun` run's `reused 0`.
- **AC2** — When `derive_check_reuse` is called with two equal keys and one program in its run list,
  it returns a reason naming that program. With a written path that no restore put back, it returns
  a reason naming the path. With either key None, it returns a reason. With equal keys, an empty run
  list and no standing path, it returns the empty string. The probe is
  `python -c "import sys; sys.path.insert(0, 'tools/govkit'); import govkit; ..."` making each of
  those calls.
  Red when: a ran program, a standing write or an unreadable key still yields a reuse.
- **AC3** — When the AC1 fixture is run without the target's conflicting edit, `demo`'s writes
  stand. Its verify runs and prints as the `rerun` run does, and the tally ends `reused 0`. When
  `derive_check_key` is called on a fresh directory that is not a git work tree, it returns None.
  Red when: a moved key or an unreadable key reuses the baseline, or `read_worktree_status`
  without `strict` answers differently from today.
- **AC4** — When `python tools/policy/policy.py get install.check-reuse` runs in gov, it prints
  `reuse`. After `python tools/playbook/render_playbook.py --reference`,
  `grep -c '^## .install.check-reuse.$' help/reference/policy.md` prints 1, and
  `python tools/policy/policy.py lists --check` exits 0. Under `rerun` the AC1 run's verify lines
  carry no reuse tail and its tally ends `reused 0`.
  Red when: the default is not `reuse`, the key has no section, or `rerun` does not restore today's
  verify pass.
- **AC5** — When `python tools/govkit/govkit.py check --target C:/projects/incms/main` and the same
  for `C:/projects/nicocares/main` run read-only from gov before and after this unit, each prints the
  same lines and exits the same.
  Red when: an adopter's check reading moves.
  permission: both are read and never written; nothing runs in either `gov-upgrade` worktree.
- **AC6** — The main loop runs the AC3 fixture's update, the ordinary landed-write run, with
  `GIT_TRACE2_EVENT` pointed at an empty directory. It runs once at the build base and once at this
  unit's commit, and counts the files. The unit's count exceeds the base's by 2 [DERIVED].
  Red when: the excess is not 2 [DERIVED], so the first read costs more than stated, or the
  verify-side read ran when its preconditions failed.
  figure: the excess of 2 is DERIVED from S1's two git calls; both counts are taken at observation.
  permission: a role pass may not run the deployer's suite (`tools/unattended/gate-guard.js` row
  D4), so the main loop observes AC1 to AC4's suite halves and this count at VERIFYING.

## 7. Gates

`govkit selftest` · `govkit refusal join` · `govkit acceptance matrix` · `policy check` · `policy fixtures` · `scratch-guard self-test` · `routed-commits selftest` · `recall floor` · `recall floor arms` · `line length` · `spec tokens (a spec's own names resolve)`

New arm: tools/govkit/selftest.py · covers AC1 AC3 AC4 · the `hg`-shaped held update under `reuse` and `rerun`, then the same with the conflict removed; its failing case is staged by reusing the baseline whatever the key says · none

The `[-14] §5 EVERY tally prints` arm gains `reused 0` in its list, as DEPL-cMendedVintage-1 added
its own count there.

## 8. Open questions

- **F1** — Build the within-run reuse, whose saving section 4 shows is confined to touched kits whose
  writes did not land, or retire the unit?
  - (a) Build S1 to S5 as written. Every criterion here holds, and on an ordinary version-bump update
    the reuse rarely fires, so the measured saving is small.
  - (b) Retire the unit, `WONTDO`, with section 4 as its reason, and file the cross-invocation reuse
    as an ask for the owner, since a stored check result can outlive a change outside the target.
  - Recommendation: (b). The charter's YAGNI rule is level 0 and a skip that seldom fires is
    machinery for its own sake; M3's feature-rich rule would pick (a), so the resolver should weigh
    the two openly.
  - RESOLVED (agent, 2026-11-20, delegated): (a), build S1 to S5 as written. It is the most
    feature-rich option, it is what the owner's prompt asked for, and P18 ranks the decision rule
    above the YAGNI practice in an unattended fork; section 6 states the saving it buys.
- **F2** — The re-ground at `ebab8b90b` found facts F1 did not have. The reuse fires only on a run
  whose every write a held restore put back, or that wrote nothing. There a held kit's verify
  decides nothing. Rev-3's whole-status key would never have fired on a held run at nicocares or on
  gov's fixtures. Rev-3's reads cost four git processes per touched kit on every write run. The
  switch's read launches 8 git processes [PINNED 2026-11-22]. Build, narrow or retire?
  - (a) Build rev-4's S1 to S5. The cost is two git processes [DERIVED] on every write run with a
    touched kit that declares an argv. Where it fires it saves 10 to 16 s [PINNED] per reused
    check, and its git count falls only when those checks launch more than twelve [DERIVED]. The
    brief's acceptance asks `update` for fewer git processes, and every ordinary update gets two
    more. So M3's veto 1 discards (a) if that clause binds each unit, as the spec brief's "Count what
    was saved" rule says it does.
  - (b) A record-only variant. Strike S1's key. S2's first two preconditions become the whole test,
    read from the run's own lists, and the policy is read only when they hold. This changes the
    goal's fingerprint sentence, AC2's key halves and AC3's unreadable-key half. It adds no git
    process to an ordinary run. Where it fires it adds the policy read's 8 [PINNED 2026-11-22] and
    saves the same checks. It cannot see an edit made outside the run while the run is going, and
    it trusts `write_kit_restore`'s own list of what it could not put back. On gov's fixtures,
    whose check launches no git, the fired run's git count rises, so veto 1 reads on (b) the same
    way.
  - (c) Retire the unit, `WONTDO`, with this fork as its reason pointer. Its saving falls only on a
    run that fails by construction or wrote nothing, and both forms cost git processes the build
    exists to remove. File two asks for the owner. The first is the cross-invocation reuse. The
    second is a held kit's verify, which decides nothing and whose printed exits are the only reader
    of its result. Skipping it needs a change to the printed output, and only the owner can make it.
  - Recommendation: (c). Under M3, (a) and (b) each fail the brief's fewer-git-processes acceptance
    on a run this spec can name, so neither survives veto 1. The tie-break does not arise, and (c)
    fails no written criterion. If the resolver reads that clause as build-wide, which unit 16's
    batch already meets, (b) is the most feature-rich survivor, and (a) is the next.
  - RESOLVED (agent, 2026-11-22, delegated): (c), retire the unit. The reuse fires only on a run
    that fails by construction or wrote nothing, and both build forms add git processes on runs
    this spec names, so neither survives M3 veto 1. The cross-invocation reuse and the held kit's
    verify skip go to the owner as asks TOOL-dQuietDisk-34 and TOOL-dQuietDisk-35.

## 9. Revision log

- rev-1 · 2026-11-20 · initial draft. Ordered 5, not the brief's 2: `tools/govkit/govkit.py` is
  written by TOOL-dQuietDisk-16 at order 1 and TOOL-dQuietDisk-18 at order 3, and every order-2 and
  order-4 sibling whose acceptance installs kits through govkit reads it, so this unit runs alone
  after them.
- rev-2 · 2026-11-20 · §1 · §6 · AC1 · §8 · F1 resolved (a) under
  `2026-11-20-prompt-TOOL-dQuietDisk-26-spec-task`: S1 to S5 are built as written, and §6 now states
  the saving the narrow reuse buys, with a `figure:` line on AC1.
- rev-3 · 2026-11-22 · wording only, under `2026-11-22-prompt-TOOL-dQuietDisk-1-pins-task`. In section
  1, section 5 and section 6 the analysis's per-kit check time is marked PINNED on each line that
  quotes it. Design, scope and acceptance unchanged.
- rev-4 · 2026-11-22 · §1 · S1 · S2 · S3 · S4 · S5 · §3 · §4 · §5 · §6 · AC1 · AC2 · AC3 · AC4 · AC6 ·
  §7 · §8 · F2 · §10 · re-grounded at ebab8b90b (orders 1 to 4 built), under
  `2026-11-22-prompt-TOOL-dQuietDisk-17-reground-task`. Moved, with the reasons:
  - Every citation is re-read and re-pinned at `ebab8b90b`.
  - §4 corrects the narrowness. Only a held kit's bytes are put back, so declined and refused kits
    are not reuse cases, and a held kit's verify decides nothing.
  - S1 becomes one run key, `HEAD` plus `read_worktree_status` under a new `strict` keyword, with
    the outbox dropped. Rev-3's per-kit `hash-object` reads cost four git processes per touched kit,
    and its whole-status key could not fire on a held run, which made rev-3's AC1 unobservable.
  - S2 gains the fragment merge, which rev-3 missed, and the standing-write precondition. Its
    switch is read last.
  - AC2 becomes a probe of `derive_check_reuse`, because no fixture runs a target program without
    moving a byte.
  - AC3's stub on `PATH` is replaced. A script named `git` is not found by Windows process
    creation, and govkit calls git everywhere.
  - AC6 counts the cost.
  - F2 is opened on these facts, F1's resolution stands as written, and units 14 and 15 are stated
    as not consumed. The goal is unchanged.
- rev-5 · 2026-11-22 · §8 · F2 resolved (c) by the main loop under the run's mandate: the unit is
  retired, WONTDO, with section 8 F2 as its reason pointer. The cross-invocation reuse and the held
  kit's verify skip are filed for the owner as asks TOOL-dQuietDisk-34 and TOOL-dQuietDisk-35.

## 10. Reuse audit

The seams extended are the verify pass's own baseline map, `baseline`, and `run_kit_check`, the one
runner of a kit's check (`tools/govkit/govkit.py#run_kit_check`). Its docstring forbids a second
implementation, so this unit adds none and reuses its triple. The fingerprint extends
`tools/govkit/govkit.py#read_worktree_status`, the status reader the regenerate snapshot already
uses, with one keyword, rather than adding a second status parser. The switch reads through
`tools/govkit/govkit.py#read_policy_value`, in the shape of
`tools/govkit/govkit.py#read_baseline_mode`, unit 18's reader for `install.baseline`.
The chain build owning the area is dSafePassage (Supersession: govkit update and apply). Its CLOSED
units 5, 10 and 25 to 27, and unit 66's held restore before the step walk, leave the verify pass's
transition rule as DEPL-dCarriedReceipt-14 wrote it, and this unit keeps it.

`python tools/codebase-map/reuse_lookup.py "fingerprint a target worktree to tell whether anything moved between two reads"`
returned name-token neighbours only (`read_text`, `read_git`, `read_policy_value`). The map does not
index `read_worktree_status`, which reading `_cmd_update` found. Recall returned this spec,
DEPL-dSealedTally-1 and DEPL-cMendedVintage-1, which shaped the verify pass's population and exits.
None proposes a reuse. The source agreed with each.

Recall terms used: run_kit_check baseline verify touched_kits held restore rollback transition update fingerprint worktree status reuse
