# TOOL-dQuietDisk-8 — the whole-tree readers clone without copying objects and check out only what they read

**Status:** CLOSED · rev-5 · 2026-11-22 · node d · Tier-2 · base 40def53f · streams tooling · order 2 · ratified 2026-11-20

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-11-20-build-TOOL-dQuietDisk-1-agent-ledger.md](../build/2026-11-20-build-TOOL-dQuietDisk-1-agent-ledger.md) | journal | TOOL-dQuietDisk-1 TOOL-dQuietDisk-2 TOOL-dQuietDisk-3 TOOL-dQuietDisk-4 TOOL-dQuietDisk-5 TOOL-dQuietDisk-6 TOOL-dQuietDisk-7 TOOL-dQuietDisk-9 TOOL-dQuietDisk-10 TOOL-dQuietDisk-11 TOOL-dQuietDisk-12 TOOL-dQuietDisk-13 TOOL-dQuietDisk-14 TOOL-dQuietDisk-15 TOOL-dQuietDisk-16 TOOL-dQuietDisk-17 TOOL-dQuietDisk-18 TOOL-dQuietDisk-19 TOOL-dQuietDisk-26 TOOL-dQuietDisk-28 TOOL-dQuietDisk-36 TOOL-dQuietDisk-37 |
| [2026-11-22-build-TOOL-dQuietDisk-8-1-acceptance-ledger.md](../build/2026-11-22-build-TOOL-dQuietDisk-8-1-acceptance-ledger.md) | journal | — |
| [2026-11-22-build-TOOL-dQuietDisk-8-deviation-1.md](../build/2026-11-22-build-TOOL-dQuietDisk-8-deviation-1.md) | deviation | — |
| [2026-11-23-build-TOOL-dQuietDisk-1-runlog-c9768b47.md](../build/2026-11-23-build-TOOL-dQuietDisk-1-runlog-c9768b47.md) | journal | TOOL-dQuietDisk-1 TOOL-dQuietDisk-2 TOOL-dQuietDisk-3 TOOL-dQuietDisk-4 TOOL-dQuietDisk-5 TOOL-dQuietDisk-7 TOOL-dQuietDisk-9 TOOL-dQuietDisk-10 TOOL-dQuietDisk-11 TOOL-dQuietDisk-12 TOOL-dQuietDisk-13 TOOL-dQuietDisk-14 TOOL-dQuietDisk-16 TOOL-dQuietDisk-18 TOOL-dQuietDisk-19 TOOL-dQuietDisk-26 TOOL-dQuietDisk-28 TOOL-dQuietDisk-36 TOOL-dQuietDisk-37 |
| [2026-11-23-build-TOOL-dQuietDisk-8-red-fix-17.md](../build/2026-11-23-build-TOOL-dQuietDisk-8-red-fix-17.md) | red-fix | — |
| [2026-11-20-prompt-TOOL-dQuietDisk-1-brief.md](../prompts/2026-11-20-prompt-TOOL-dQuietDisk-1-brief.md) | research | TOOL-dQuietDisk-1 TOOL-dQuietDisk-2 TOOL-dQuietDisk-3 TOOL-dQuietDisk-4 TOOL-dQuietDisk-5 TOOL-dQuietDisk-6 TOOL-dQuietDisk-7 TOOL-dQuietDisk-9 TOOL-dQuietDisk-10 TOOL-dQuietDisk-11 TOOL-dQuietDisk-12 TOOL-dQuietDisk-13 TOOL-dQuietDisk-14 TOOL-dQuietDisk-15 TOOL-dQuietDisk-16 TOOL-dQuietDisk-17 TOOL-dQuietDisk-18 TOOL-dQuietDisk-19 |
| [2026-11-20-prompt-TOOL-dQuietDisk-1-spec-brief.md](../prompts/2026-11-20-prompt-TOOL-dQuietDisk-1-spec-brief.md) | research | TOOL-dQuietDisk-1 TOOL-dQuietDisk-2 TOOL-dQuietDisk-3 TOOL-dQuietDisk-4 TOOL-dQuietDisk-5 TOOL-dQuietDisk-6 TOOL-dQuietDisk-7 TOOL-dQuietDisk-9 TOOL-dQuietDisk-10 TOOL-dQuietDisk-11 TOOL-dQuietDisk-12 TOOL-dQuietDisk-13 TOOL-dQuietDisk-14 TOOL-dQuietDisk-15 TOOL-dQuietDisk-16 TOOL-dQuietDisk-17 TOOL-dQuietDisk-18 TOOL-dQuietDisk-19 |
| [2026-11-20-prompt-TOOL-dQuietDisk-26-spec-task.md](../prompts/2026-11-20-prompt-TOOL-dQuietDisk-26-spec-task.md) | research | TOOL-dQuietDisk-10 TOOL-dQuietDisk-17 TOOL-dQuietDisk-19 TOOL-dQuietDisk-26 |
| [2026-11-22-prompt-TOOL-dQuietDisk-1-pins-task.md](../prompts/2026-11-22-prompt-TOOL-dQuietDisk-1-pins-task.md) | research | TOOL-dQuietDisk-1 TOOL-dQuietDisk-2 TOOL-dQuietDisk-3 TOOL-dQuietDisk-4 TOOL-dQuietDisk-5 TOOL-dQuietDisk-6 TOOL-dQuietDisk-7 TOOL-dQuietDisk-9 TOOL-dQuietDisk-10 TOOL-dQuietDisk-11 TOOL-dQuietDisk-12 TOOL-dQuietDisk-13 TOOL-dQuietDisk-14 TOOL-dQuietDisk-15 TOOL-dQuietDisk-16 TOOL-dQuietDisk-17 TOOL-dQuietDisk-18 TOOL-dQuietDisk-19 TOOL-dQuietDisk-26 |
| [2026-11-22-prompt-TOOL-dQuietDisk-2-reground-task.md](../prompts/2026-11-22-prompt-TOOL-dQuietDisk-2-reground-task.md) | research | TOOL-dQuietDisk-2 TOOL-dQuietDisk-3 TOOL-dQuietDisk-4 TOOL-dQuietDisk-5 TOOL-dQuietDisk-7 |
| [2026-11-22-prompt-TOOL-dQuietDisk-8-1-spec-writer.md](../prompts/2026-11-22-prompt-TOOL-dQuietDisk-8-1-spec-writer.md) | journal | — |
| [2026-11-22-prompt-TOOL-dQuietDisk-8-build-brief.md](../prompts/2026-11-22-prompt-TOOL-dQuietDisk-8-build-brief.md) | journal | — |
| [2026-11-22-review-TOOL-dQuietDisk-1-closing-diff-review-round1.md](../reviews/2026-11-22-review-TOOL-dQuietDisk-1-closing-diff-review-round1.md) | diff-review | TOOL-dQuietDisk-1 TOOL-dQuietDisk-2 TOOL-dQuietDisk-3 TOOL-dQuietDisk-4 TOOL-dQuietDisk-5 TOOL-dQuietDisk-7 TOOL-dQuietDisk-9 TOOL-dQuietDisk-10 TOOL-dQuietDisk-11 TOOL-dQuietDisk-12 TOOL-dQuietDisk-13 TOOL-dQuietDisk-14 TOOL-dQuietDisk-16 TOOL-dQuietDisk-18 TOOL-dQuietDisk-19 TOOL-dQuietDisk-26 TOOL-dQuietDisk-28 |

<!-- /gen:spec-records -->

## 1. Goal

Six readers each make their own full copy of the repository during a bar: a clone, often with every
object copied, and a checkout of all 15,122 tracked files, of which 14,141 sit under
`memory/builds/` (both DERIVED by `git ls-tree -r --name-only 40def53f7` on 2026-11-22). This unit
makes each reader clone with `--shared`, so no object is copied or hardlinked, and check out only the
paths it reads where that is proven not to move its output. A reader that cannot share is named with
its reason and left as today. Every reader's verdict and output stay what they were.

## 2. Scope (IN)

- **S1** — `tools/run-gates/foreign-prefix.gov.test.sh` and `tools/chain-packet.test.sh` replace
  `git clone -q --no-hardlinks` with `git clone -q --shared --no-checkout` followed by their existing
  `checkout -B`, which checks out the full tree as today. The clone's own commits land in its own
  object store. Observed by AC1 and AC5.
- **S2** — `tools/govkit/matrix.py`'s aged-gov clone adds `--shared` to its `clone` call.
  `tools/govkit/upgrade_walk.py`'s pinned clone adds `--shared --no-checkout`. Today that clone checks
  out the source's HEAD and then, on the next line, the pin
  (`tools/govkit/upgrade_walk.py@aea8e1c7386b:231`), so its existing `checkout --detach <pin>` is left
  as the one checkout. Observed by AC2 and AC5.
- **S3** — A reader moves to a sparse checkout only where its own output, run once over a full
  checkout and once over a checkout leaving out `memory/builds/`, is byte-identical. The pass makes
  that observation through each reader's scoped direct check, run over both checkouts and recorded
  in the acceptance ledger: `python tools/policy/check_policy.py --fixture <case>` for one case whose
  fixture builds a source snapshot, `python tools/govkit/upgrade_walk.py --case <case>` for one
  case, and, for `matrix.py`, which has no scoped form, a probe that makes its aged-gov clone as
  `tools/govkit/matrix.py@8bb81dbe52f9:976` does and runs that shape's `apply` and `update --write`
  over each checkout. The reader's whole run over both checkouts is owed to the main loop at the
  close, and a move there is a red the close repairs by returning that reader to its full
  checkout. Such a reader runs one `git sparse-checkout set --no-cone '/*' '!/memory/builds/'`,
  written at its clone site, between its `--no-checkout` clone and its checkout. `matrix.py`'s clone
  checks out today, so if it goes sparse it also takes `--no-checkout` and checks out its HEAD
  itself after the sparse set. The candidates are `build_source_snapshot` in
  `tools/policy/check_policy.py`, which `tools/loop/factories.py` also calls, `matrix.py`'s
  aged-gov clone and `upgrade_walk.py`'s pinned clone. Observed by AC3 and AC4.
- **S4** — Each changed clone keeps today's teardown, the suite's exit trap, the policy kit's own
  repository teardown or the caller's scratch root, so a `--shared` clone never outlives the leg
  that made it and the objects it borrows. Observed by AC5.
- **S5** — A comment beside each changed clone says why it is `--shared`, and for a sparse reader,
  which paths it leaves out and the observation that allowed it. Observed by AC6.

## 3. Non-goals (OUT)

- `tools/govkit/selftest.py`'s source-mode clone (`tools/govkit/selftest.py@c2b02d780af9:6322`)
  stays as it is. It is a plain local clone, so git already hardlinks its objects rather than
  copying them, and its arm runs `update --write` in source mode, whose plan lists the files on
  disk; a sparse checkout would change that plan and so the arm's verdict. It also sits in the file
  TOOL-dQuietDisk-18 rewrites at order 3.
- No sparse checkout for foreign-prefix or chain-packet. Foreign-prefix runs every self-test's
  prologue at each moved prefix, and chain-packet runs the real instruments over the chain builds'
  records, so either may read any tracked path.
- No change to what any reader tests, to the prefix moves, or to the policy snapshot's commit of the
  working tree.
- No runner-built snapshot, by F1's pick (b), so `tools/run-gates/run-gates.sh` is untouched and no
  path or environment variable is handed between legs.
- No cache and no switch: a clone that borrows objects and a checkout that omits unread paths are
  how a fixture is made, not stored answers.
- The upgrade walk's design is dSafePassage's (its unit 5, CLOSED); only its clone flags move here.

### Edges

- **consumes-from** external — dWitnessedBar's landing, `8b8b1374c` on main, merged into this branch
  at `40def53f7`. This unit is built on it, because that build changed five of these files
  (`git diff --stat 9e21ac760 fb6f1a74c`).

## 4. Design

### The readers today

All citations are read at `40def53f7`, each pinned to its blob there. Only
`tools/policy/check_policy.py` and `tools/govkit/selftest.py` moved since `59e882afd`, both before
dWitnessedBar's land tip `fb6f1a74c`; `build_source_snapshot`'s body is unchanged and only its lines
moved. The object store measured 167 MB in 92 files, PINNED, on 2026-11-20 by `du` and `find` over
this clone's common `objects/`.

| Reader | Clone today | Checkout | Mutates its copy | After |
|---|---|---|---|---|
| `foreign-prefix.gov.test.sh` | `--no-hardlinks` (`tools/run-gates/foreign-prefix.gov.test.sh@fe5ce9d67e73:471`) | full, then `checkout -B` | `git mv` of the tool root three times | `--shared --no-checkout`, full checkout |
| `chain-packet.test.sh` | `--no-hardlinks` (`tools/chain-packet.test.sh@396018d9b00e:313`) | full, then `checkout -B` | one commit of planted specs | `--shared --no-checkout`, full checkout |
| `check_policy.py` `build_source_snapshot` | `--shared --no-checkout` (`tools/policy/check_policy.py@6cbdf64bc9c3:1363`) | full, of the committed working tree (`tools/policy/check_policy.py@6cbdf64bc9c3:1379`) | installs and plants | sparse where S3 holds |
| `factories.py` | through `build_source_snapshot` (`tools/loop/factories.py@835d45ef996f:598`) | as above | plants | inherits |
| `matrix.py` aged gov | `--local`, hardlinked (`tools/govkit/matrix.py@8bb81dbe52f9:976`) | full | edits the registry | `--shared`, sparse where S3 holds |
| `upgrade_walk.py` | plain local, hardlinked (`tools/govkit/upgrade_walk.py@aea8e1c7386b:230`) | full at the source's HEAD, then the pin (`:231`) | walks to the tip | `--shared --no-checkout`, sparse where S3 holds |
| `selftest.py` source mode | plain local (`tools/govkit/selftest.py@c2b02d780af9:6322`) | full | `update --write` | unchanged, section 3 |

So the bytes saved by S1 are two copies of the object store per bar. S2 saves the upgrade walk's
first full checkout, and S3 saves up to 14,141 checked-out files per sparse reader per run.

### Why one runner-built snapshot buys nothing here

Every reader in the table mutates its copy, so none can be handed a shared checkout by path. A
runner-built `clone --shared --no-checkout` holds no files to share, and a reader cloning from it
with `--shared` pays exactly what it pays cloning `--shared` from the repository itself. F1 is
resolved (b): each reader takes its own `--shared` clone of the repository.

### `--shared` and its one hazard

A `--shared` clone reads the source's objects through `objects/info/alternates`. Its own commits go
to its own store. The hazard is the source pruning an object the clone still reads. Every object
these readers read is reachable from the source's HEAD or a ref, which `git gc` never prunes, and
every clone here is removed before its leg ends (S4).

### Files touched (estimate)

`tools/run-gates/foreign-prefix.gov.test.sh` · `tools/chain-packet.test.sh` · `tools/policy/check_policy.py` · `tools/govkit/matrix.py` · `tools/govkit/upgrade_walk.py`

No file gains a column-0 function, so the codebase map's generated symbol index is not
regenerated. None of these paths is on the kickoff manifest's `watch:` line, and the pass writes no
other path.

### Paths shared with order-2 units

None. TOOL-dQuietDisk-2 writes the pass-order leg and its suite, TOOL-dQuietDisk-3 the
brief-recorded leg and its suite, TOOL-dQuietDisk-4 the routed-commits reader, TOOL-dQuietDisk-5 the
bar runner, its suite and the kickoff manifest, and TOOL-dQuietDisk-7 the template-cache files and
their registrations. None of them names a path above, so this unit builds in parallel with each.
Later orders do share paths: TOOL-dQuietDisk-9, at order 6, also writes `tools/policy/check_policy.py`
and `tools/govkit/upgrade_walk.py`, and it is built on this unit's text.

### Inventory

The unit mints no identifier. The sparse step is one git argv at each sparse reader's clone site,
so no helper is named.

### Alternatives rejected

| Alternative | Why it loses |
|---|---|
| A runner-built snapshot handed to every reader | Section 4: every reader mutates, so the handed path is cloned again at the same cost. |
| A module-level helper per sparse reader (rev-4's `write_sparse_set`) | It wraps one git argv. Each copy would add a row to the codebase map's symbol index, and two copies would sit in the govkit kit, whose second instance owes a factory. |
| `git worktree add` from one shared clone | Parallel legs would race on one repository's refs, `worktrees/` and config. |
| `git archive` of named paths | It loses the history the policy snapshot and the upgrade walk read. |

## 5. Production-readiness checklist

- security: N/A — scratch copies of the repository's own tree, removed before the leg ends.
- perf / scale: two object-store copies per bar removed (S1); the upgrade walk's first full checkout
  removed (S2); up to 14,141 checked-out files per sparse reader (S3), counted by AC5.
- error / empty / loading states: a clone that fails exits as today, with the reader's own message.
- observability: each reader's output is unchanged.
- risks: a sparse reader that reads a left-out path would change its verdict; S3's observation
  gates every sparse move, and AC3 and AC4 are its witnesses.
- testing: each reader's own run before and after (AC1 to AC4) and the entry counts (AC5).
- migration: none.
- user docs: `help/` holds no page for these fixtures; the comments beside each clone (S5).

## 6. Acceptance criteria

- **AC1** — When a probe under `%TEMP%/<short-name>` builds a repository of at least 50 committed
  files and makes two copies of it, one by today's `git clone -q --no-hardlinks` and one by
  `git clone -q --shared --no-checkout`, each followed by the same `checkout -B`, the two copies'
  `git ls-files -s`, `git status --porcelain` and work-tree file lists are byte-identical, and only
  the shared copy holds an `objects/info/alternates` file. When the main loop runs the
  foreign-prefix suite, filtered by its `--kit` flag to one family, and the chain-packet suite before
  and after the change at the close, each pair prints the same arm results and exits the same.
  Red when: a `--shared` clone changes the checked-out tree, or an arm's result.
  cost: the foreign-prefix suite's declared budget is long, and the filter bounds it to one family.
  permission: a role agent runs no suite (scratch-guard row G3), so both suites' pairs are owed to
  the main loop; the pass makes the clone probe.
- **AC2** — When a probe imports `tools/govkit/upgrade_walk.py` and calls `build_release_tree` with
  `with_target=False` over a scratch root, the clone it leaves at `<root>/gov` holds an
  `objects/info/alternates` file and the pinned commit checked out: its `git ls-files` equals
  `git ls-tree -r --name-only <pin>` and its `git status --porcelain` prints nothing. When
  `python tools/govkit/upgrade_walk.py --case <case>` runs for one case before and after over the same
  clone of gov, its printed lines and exit are the same. When the main loop runs the whole walk
  before and after at the close, its printed lines and exit are the same.
  Red when: the walk's output moves, its clone still carries its own copy of every object, or its
  work tree differs from the pin's.
  permission: the whole walk is the `upgrade-walk` leg, owed to the main loop (scratch-guard row
  G1); the pass makes the probe and the one-case run.
- **AC3** — When `build_source_snapshot` is called on the same working tree by the old and the new
  `tools/policy/check_policy.py`, the two snapshot commits carry the same tree id, and each sparse
  reader's scoped direct check of S3 prints over the sparse checkout what it prints over the full
  one. A sparse reader's work tree holds no file under `memory/builds/` and every other tracked
  file of its checked-out commit. The main loop observes each sparse reader's whole run unchanged
  at the close.
  Red when: a sparse checkout drops a path the reader reads, so its output moves.
  permission: each reader's whole run is owed to the main loop; the pass makes the snapshot probe
  and the scoped checks.
- **AC4** — When S3's scoped check finds a reader's output moved with `memory/builds/` left out, that
  reader keeps its full checkout, and `grep -c 'sparse-checkout' <its file>` prints 0. The
  observation is trusted only after a planted read of one `memory/builds/` README inside the
  reader's scratch run makes the two outputs differ.
  Red when: a reader goes sparse against a moved observation, or the comparison cannot fail.
- **AC5** — When AC1's and AC2's probes and each scoped check of S3 run with `TEMP`, `TMP` and
  `TMPDIR` pointed at a scratch dir watched every 0.5 s, each changed clone's peak entry count is
  lower than the old clone's and the residue after exit is 0, both printed beside the old figures.
  When the main loop takes the same watch over each changed reader's whole run at the close, the
  same holds.
  Red when: a reader's peak does not fall, or a clone outlives its leg.
  figure: both counts are DERIVED at observation.
  permission: the whole runs are owed to the main loop; the pass makes the probe readings.
- **AC6** — When `grep -n -- '--shared' tools/run-gates/foreign-prefix.gov.test.sh tools/chain-packet.test.sh tools/govkit/matrix.py tools/govkit/upgrade_walk.py`
  runs, each file names it beside a comment saying why.
  Red when: a clone still carries `--no-hardlinks`.

## 7. Gates

`foreign-prefix parity (every self-test at three prefixes)` · `chain-packet self-test` · `policy check` · `policy fixtures` · `loop factories fixtures` · `govkit acceptance matrix` · `upgrade-walk` · `govkit selftest` · `govkit refusal join` · `scratch-guard self-test` · `routed-commits selftest` · `recall floor arms` · `line length` · `spec tokens (a spec's own names resolve)`

No suite arm is added or moved: each reader is itself a suite or a fixture, and its own arms
re-observe it at the close, run by the main loop. No criterion has the pass run a suite, a gate
leg's own argv or the bar.

## 8. Open questions

- **F1** — One runner-built snapshot per bar, or each reader's own `--shared` clone?
  - (a) The runner builds `clone --shared --no-checkout` once under `$WORK` at HEAD and exports its
    path; each reader clones from it. This matches the brief's wording, adds a runner surface and an
    environment variable, and writes `tools/run-gates/run-gates.sh`, which TOOL-dQuietDisk-5 writes
    at order 2, so this unit would move to order 3.
  - (b) Each reader clones `--shared` from the repository itself and nothing is handed between legs.
    Section 4 shows (a) saves nothing (b) does not, because every reader mutates its copy.
  - Recommendation: (b). It satisfies every criterion here, adds no surface, and keeps the unit at
    order 2.
  - RESOLVED (agent, 2026-11-20, delegated): (b). Every reader mutates its copy, so (a) saves
    nothing over (b) and would add a runner surface.

## 9. Revision log

- rev-1 · 2026-11-20 · initial draft.
- rev-2 · 2026-11-20 · §3 · §4 · §8 · F1 resolved (b) under
  `2026-11-20-prompt-TOOL-dQuietDisk-26-spec-task`: each reader takes its own `--shared` clone, and
  nothing is handed between legs.
- rev-3 · 2026-11-22 · under `2026-11-22-prompt-TOOL-dQuietDisk-1-divergence-task`. S3, AC1, AC2, AC3
  and AC5 had the pass run the readers, which are suites and gate legs a role agent may not run.
  The pass now makes clone probes and each reader's scoped direct check, and every whole reader run
  is owed to the main loop at the close. `write_sparse_set`, the one name the spec mints, passes
  `--suggest` in both cells.
- rev-4 · 2026-11-22 · wording only, under `2026-11-22-prompt-TOOL-dQuietDisk-1-pins-task`. In section
  4 the object-store figures' PINNED moves onto the line that quotes them. Design, scope and
  acceptance unchanged.
- rev-5 · 2026-11-22 · §1 §2 §3 §4 §5 §6 §10 · S2 · S3 · AC2 · AC3 · re-grounded at 40def53f7
  (order 1 built, dWitnessedBar landed), under `2026-11-22-prompt-TOOL-dQuietDisk-2-reground-task`.
  What moved: `build_source_snapshot`'s clone and checkout lines and the source-mode clone in
  `tools/govkit/selftest.py`, both re-cited by blob. Every other cited file is byte-identical to
  `59e882afd`. The tree counts are re-derived at 40def53f7. TOOL-dQuietDisk-11 no longer writes
  `selftest.py`, so §3 names only TOOL-dQuietDisk-18. Scope widens by one flag: re-reading the
  walk's clone showed it checks out HEAD before its own checkout of the pin, so S2 adds
  `--no-checkout` there, as S1 does for the two suites. This stays inside §1's goal of checking out only what a reader reads, and AC2 now
  observes the pin's work tree. `write_sparse_set` is retired. As a column-0 function it would
  move `memory/map/generated/symbols.json`, and two copies would sit in govkit. The sparse step
  is now one inline git argv, and the helper is a row of Alternatives rejected. Design names no
  order-2 unit sharing a path.

## 10. Reuse audit

The seam extended is `build_source_snapshot` (`tools/policy/check_policy.py#build_source_snapshot`),
the one reader already cloning `--shared --no-checkout`; S1 and S2 bring the other clones to its
form. The chain builds owning the area are dWitnessedBar (Test: suites and budgets), which changed
five of these files and has landed, and dSafePassage (Supersession), whose CLOSED unit 5 owns the
upgrade walk's design; only the walk's clone flags move here. No dWitnessedBar unit touched any of
these clones' flags: `git log -S'no-hardlinks'` and `git log -S'sparse-checkout'` over
`59e882afd..40def53f7 -- tools/` list no commit, and its specs name neither. So there is no
dWitnessedBar work to extend here.

`python tools/codebase-map/reuse_lookup.py "clone a repository snapshot shared without copying objects"`
named `build_source_snapshot`, the seam above, beside name-token neighbours. Recall returned
TOOL-dPlacedRequest-2, TOOL-dSafePassage-88's briefs on the upgrade walk's clone, and this build's
analysis rows G1c, G1e and G1f. The source agreed with each.

Recall terms used: foreign-prefix clone no-hardlinks snapshot build_source_snapshot sparse checkout shared alternates upgrade_walk matrix
