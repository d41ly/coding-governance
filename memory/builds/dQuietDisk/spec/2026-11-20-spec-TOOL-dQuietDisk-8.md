# TOOL-dQuietDisk-8 — the whole-tree readers clone without copying objects and check out only what they read

**Status:** SPECCED · rev-2 · 2026-11-20 · node d · Tier-2 · base 609cd40b · streams tooling · order 2 · ratified 2026-11-20

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-11-20-prompt-TOOL-dQuietDisk-1-brief.md](../prompts/2026-11-20-prompt-TOOL-dQuietDisk-1-brief.md) | research | TOOL-dQuietDisk-1 TOOL-dQuietDisk-2 TOOL-dQuietDisk-3 TOOL-dQuietDisk-4 TOOL-dQuietDisk-5 TOOL-dQuietDisk-6 TOOL-dQuietDisk-7 TOOL-dQuietDisk-9 TOOL-dQuietDisk-10 TOOL-dQuietDisk-11 TOOL-dQuietDisk-12 TOOL-dQuietDisk-13 TOOL-dQuietDisk-14 TOOL-dQuietDisk-15 TOOL-dQuietDisk-16 TOOL-dQuietDisk-17 TOOL-dQuietDisk-18 TOOL-dQuietDisk-19 |
| [2026-11-20-prompt-TOOL-dQuietDisk-1-spec-brief.md](../prompts/2026-11-20-prompt-TOOL-dQuietDisk-1-spec-brief.md) | research | TOOL-dQuietDisk-1 TOOL-dQuietDisk-2 TOOL-dQuietDisk-3 TOOL-dQuietDisk-4 TOOL-dQuietDisk-5 TOOL-dQuietDisk-6 TOOL-dQuietDisk-7 TOOL-dQuietDisk-9 TOOL-dQuietDisk-10 TOOL-dQuietDisk-11 TOOL-dQuietDisk-12 TOOL-dQuietDisk-13 TOOL-dQuietDisk-14 TOOL-dQuietDisk-15 TOOL-dQuietDisk-16 TOOL-dQuietDisk-17 TOOL-dQuietDisk-18 TOOL-dQuietDisk-19 |
| [2026-11-20-prompt-TOOL-dQuietDisk-26-spec-task.md](../prompts/2026-11-20-prompt-TOOL-dQuietDisk-26-spec-task.md) | research | TOOL-dQuietDisk-10 TOOL-dQuietDisk-17 TOOL-dQuietDisk-19 TOOL-dQuietDisk-26 |

<!-- /gen:spec-records -->

## 1. Goal

Six readers each make their own full copy of the repository during a bar: a clone, often with every
object copied, and a checkout of all 14,156 tracked files, of which 13,206 sit under
`memory/builds/` (both DERIVED by `git ls-tree -r --name-only 609cd40b1` on 2026-11-20). This unit
makes each reader clone with `--shared`, so no object is copied or hardlinked, and check out only the
paths it reads where that is proven not to move its output. A reader that cannot share is named with
its reason and left as today. Every reader's verdict and output stay what they were.

## 2. Scope (IN)

- **S1** — `tools/run-gates/foreign-prefix.gov.test.sh` and `tools/chain-packet.test.sh` replace
  `git clone -q --no-hardlinks` with `git clone -q --shared --no-checkout` followed by their existing
  `checkout -B`, which checks out the full tree as today. The clone's own commits land in its own
  object store. Observed by AC1 and AC5.
- **S2** — `tools/govkit/matrix.py`'s aged-gov clone and `tools/govkit/upgrade_walk.py`'s pinned
  clone add `--shared` to their `clone` call. Observed by AC2 and AC5.
- **S3** — A reader moves to a sparse checkout only where its own output, run once over a full
  checkout and once over a checkout leaving out `memory/builds/`, is byte-identical, an observation
  the build pass makes reader by reader and records in the acceptance ledger. Such a reader sets `git sparse-checkout set --no-cone` to every tracked
  path except `memory/builds/` before its checkout, through a two-line helper inlined in its own kit,
  since `tools/lib/` ships nothing. The candidates are `build_source_snapshot` in
  `tools/policy/check_policy.py`, which `tools/loop/factories.py` also calls, `matrix.py`'s
  aged-gov clone and `upgrade_walk.py`'s pinned clone. Observed by AC3 and AC4.
- **S4** — Each changed clone keeps today's teardown, the suite's exit trap, the policy kit's own
  repository teardown or the caller's scratch root, so a `--shared` clone never outlives the leg
  that made it and the objects it borrows. Observed by AC5.
- **S5** — A comment beside each changed clone says why it is `--shared`, and for a sparse reader,
  which paths it leaves out and the observation that allowed it. Observed by AC6.

## 3. Non-goals (OUT)

- `tools/govkit/selftest.py`'s source-mode clone (`tools/govkit/selftest.py@609cd40b1:6143`) stays as
  it is. It is a plain local clone, so git already hardlinks its objects rather than copying them,
  and its arm runs `update --write` in source mode, whose plan lists the files on disk; a sparse
  checkout would change that plan and so the arm's verdict. It also sits in the file
  TOOL-dQuietDisk-11 and TOOL-dQuietDisk-18 rewrite at order 3.
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

- **consumes-from** external — dWitnessedBar's landed tip, which this unit is built on, because that
  branch changes five of these files.

## 4. Design

### The readers today

All citations are read at `609cd40b1`. The object store measured 167 MB in 92 files on 2026-11-20,
PINNED, by `du` and `find` over this clone's common `objects/`.

| Reader | Clone today | Checkout | Mutates its copy | After |
|---|---|---|---|---|
| `foreign-prefix.gov.test.sh` | `--no-hardlinks` (`tools/run-gates/foreign-prefix.gov.test.sh@609cd40b1:471`) | full | `git mv` of the tool root three times | `--shared --no-checkout`, full checkout |
| `chain-packet.test.sh` | `--no-hardlinks` (`tools/chain-packet.test.sh@609cd40b1:313`) | full | one commit of planted specs | `--shared --no-checkout`, full checkout |
| `check_policy.py` `build_source_snapshot` | `--shared --no-checkout` (`tools/policy/check_policy.py@609cd40b1:1101`) | full, of the committed working tree (`tools/policy/check_policy.py@609cd40b1:1117`) | installs and plants | sparse where S3 holds |
| `factories.py` | through `build_source_snapshot` (`tools/loop/factories.py@609cd40b1:598`) | as above | plants | inherits |
| `matrix.py` aged gov | `--local`, hardlinked (`tools/govkit/matrix.py@609cd40b1:976`) | full | edits the registry | `--shared`, sparse where S3 holds |
| `upgrade_walk.py` | plain local, hardlinked (`tools/govkit/upgrade_walk.py@609cd40b1:230`) | full, at the pin | walks to the tip | `--shared`, sparse where S3 holds |
| `selftest.py` source mode | plain local (`tools/govkit/selftest.py@609cd40b1:6143`) | full | `update --write` | unchanged, section 3 |

So the bytes saved by S1 are two copies of the object store per bar, and the files saved by S3 are
up to 13,206 checked-out files per sparse reader per run.

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

### Inventory

| Minted identifier | Kind | Naming cell | Graded by |
|---|---|---|---|
| `write_sparse_set` | a two-line inline helper per sparse reader's kit | none | AC3 |

### Alternatives rejected

| Alternative | Why it loses |
|---|---|
| A runner-built snapshot handed to every reader | Section 4: every reader mutates, so the handed path is cloned again at the same cost. |
| `git worktree add` from one shared clone | Parallel legs would race on one repository's refs, `worktrees/` and config. |
| `git archive` of named paths | It loses the history the policy snapshot and the upgrade walk read. |

## 5. Production-readiness checklist

- security: N/A — scratch copies of the repository's own tree, removed before the leg ends.
- perf / scale: two object-store copies per bar removed (S1); up to 13,206 checked-out files per sparse
  reader (S3), counted by AC5.
- error / empty / loading states: a clone that fails exits as today, with the reader's own message.
- observability: each reader's output is unchanged.
- risks: a sparse reader that reads a left-out path would change its verdict; S3's observation
  gates every sparse move, and AC3 and AC4 are its witnesses.
- testing: each reader's own run before and after (AC1 to AC4) and the entry counts (AC5).
- migration: none.
- user docs: `help/` holds no page for these fixtures; the comments beside each clone (S5).

## 6. Acceptance criteria

- **AC1** — When the foreign-prefix suite, filtered by its `--kit` flag to one family, and the
  chain-packet suite each run before and after their clone becomes `git clone -q --shared
  --no-checkout`, in one scratch clone of the real tree, each pair prints the same arm results and
  exits the same.
  Red when: a `--shared` clone changes an arm's result.
  cost: the foreign-prefix suite's declared budget is long, and the filter bounds it to one family.
  fixture: a clone under `%TEMP%` with its own `TEMP`.
- **AC2** — When `python tools/govkit/upgrade_walk.py` runs before and after over the same clone, its
  printed lines and exit are the same, and the walk's clone holds an `objects/info/alternates` file.
  Red when: the walk's output moves, or its clone still carries its own copy of every object.
- **AC3** — When `build_source_snapshot` is called on the same working tree by the old and the new
  `tools/policy/check_policy.py`, the two snapshot commits carry the same tree id, and every sparse
  reader's run prints what its old run printed.
  Red when: a sparse checkout drops a path the reader reads, so its output moves.
- **AC4** — When S3's observation finds a reader's output moved with `memory/builds/` left out, that
  reader keeps its full checkout, and `grep -c 'sparse-checkout' <its file>` prints 0. The
  observation is trusted only after a planted read of one `memory/builds/` README inside the
  reader's scratch run makes the two outputs differ.
  Red when: a reader goes sparse against a moved observation, or the comparison cannot fail.
- **AC5** — When each changed reader runs with `TEMP`, `TMP` and `TMPDIR` pointed at a scratch dir
  watched every 0.5 s, its peak entry count is lower than the old reader's and its residue after exit
  is 0, both printed beside the old figures.
  Red when: a reader's peak does not fall, or a clone outlives its leg.
  figure: both counts are DERIVED at observation.
- **AC6** — When `grep -n -- '--shared' tools/run-gates/foreign-prefix.gov.test.sh tools/chain-packet.test.sh tools/govkit/matrix.py tools/govkit/upgrade_walk.py`
  runs, each file names it beside a comment saying why.
  Red when: a clone still carries `--no-hardlinks`.

## 7. Gates

`foreign-prefix parity (every self-test at three prefixes)` · `chain-packet self-test` · `policy check` · `policy fixtures` · `loop factories fixtures` · `govkit acceptance matrix` · `upgrade-walk` · `govkit selftest` · `govkit refusal join` · `scratch-guard self-test` · `routed-commits selftest` · `recall floor arms` · `line length` · `spec tokens (a spec's own names resolve)`

No suite arm is added or moved: each reader is itself a suite or a fixture, and its own arms
re-observe it at the close.

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

## 10. Reuse audit

The seam extended is `build_source_snapshot` (`tools/policy/check_policy.py#build_source_snapshot`),
the one reader already cloning `--shared --no-checkout`; S1 and S2 bring the other clones to its
form. The chain builds owning the area are dWitnessedBar (Test: suites and budgets), which changes
five of these files on its branch, and dSafePassage (Supersession), whose CLOSED unit 5 owns the
upgrade walk's design; only the walk's clone flags move here.

`python tools/codebase-map/reuse_lookup.py "clone a repository snapshot shared without copying objects"`
named `build_source_snapshot`, the seam above, beside name-token neighbours. Recall returned
TOOL-dPlacedRequest-2, TOOL-dSafePassage-88's briefs on the upgrade walk's clone, and this build's
analysis rows G1c, G1e and G1f. The source agreed with each.

Recall terms used: foreign-prefix clone no-hardlinks snapshot build_source_snapshot sparse checkout shared alternates upgrade_walk matrix
