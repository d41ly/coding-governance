# DEPL-aHoistedPass-1 — a declared kit dependency that is actually checked

**Status:** SPECCED · rev-2 · 2026-09-04 · node a · Tier-2 · base c4fcf5ad · streams deployer · order 2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-09-04-build-TOOL-aHoistedPass-1-1-design-pass.md](../build/2026-09-04-build-TOOL-aHoistedPass-1-1-design-pass.md) | research | TOOL-aHoistedPass-1 TOOL-aHoistedPass-2 TOOL-aHoistedPass-3 TOOL-aHoistedPass-4 TOOL-aHoistedPass-5 TOOL-aHoistedPass-6 TOOL-aHoistedPass-7 TOOL-aHoistedPass-8 TOOL-aHoistedPass-9 |

<!-- /gen:spec-records -->

## 1. Goal

`requires` in a kit descriptor buys install ORDERING and nothing else, so `tools/unattended/kit.toml`
can name a dependency that no verb ever checks and no gate ever reds. This unit adds the
`review-harness` edge and makes plain `requires` mean something at both places it can: a registry-name
arm in `selfcheck`, and an installed-set refusal in the verb that actually installs.

## 2. Scope (IN)

- **S1.** `tools/unattended/kit.toml:7` becomes `requires = ["memory-tree", "review-harness"]`.
- **S2.** ARM A, the REGISTRY arm. Extend `selfcheck` check 7 (`govkit.py:1326-1341`) so a plain
  `requires` entry names a registry entry, modelled on the `requires_if` arm at `:1330-1333`.
- **S3.** ARM B, the INSTALLED-SET arm. In `_cmd_apply`, immediately after the AC8 foreign-kit block
  (`govkit.py:4282-4288`) and before `demand_writable_target` (`:4295`), refuse when a selected kit's
  `requires` target is neither in the selection nor in the target's receipt.
- **S4.** The same predicate in `cmd_plan` as a printed row, not a refusal. Its exit code does not
  move.
- **S5.** The `derive_install_order` docstring at `govkit.py:495-496` gains a clause naming the
  apply-time check, because its `--kits drift-audit` example is one of the selections arm B refuses.
- **S6.** Arms for both new branches, at the existing `requires` seam in `tools/govkit/selftest.py`
  (`:2405-2430`), plus repair of the nine existing `--kits` call sites arm B newly refuses.
- **S7.** Both refusal strings name the REMEDY, and neither spells a `tools/` path literal.
- **S8.** The version bumps the changed payload owes: `KIT_GOVKIT_VERSION` (`govkit.py:44`) and the
  `unattended` kit version, the latter subject to fork F1.

## 3. Non-goals (OUT)

- **Auto-expanding the selection.** `requires` does not pull a kit in, and this unit does not make it.
  Arm B refuses and names what to add; the owner ruled refuse, not expand.
- **A bypass flag.** No `--allow-unsatisfied-requires`. A new public surface is veto 2, and a gate
  that ships its own escape hatch is not a gate.
- **The mis-spelled KEY class.** A descriptor writing `require = [...]` declares nothing and is
  invisible to both arms, because both read literal key names (`govkit.py:504`, `:1330`). Backlog row.
- **`requires_if`.** Its registry arm already exists and is not touched.
- **Moving `BRANCH_PIN` or `FILE_PIN`** in `tools/govkit/refusal_join.py`. See §4 and §9.
- **Building a reached-set producer** so `refusal_join.py`'s join half runs. That is
  `TOOL-dUnstalledConvoy-36`, named in the file's own ledger at `:110-115`.
- **Check 31 in `check-unattended.sh`.** That is the gate-time announcement, a separate unit.
- **`WIRE-INTO-PROJECT.md:653`'s claim** that the resolver "never reads `deploy.toml`'s `kits`", which
  `resolve_selection:573-582` made false. Pre-existing drift, adjacent, not this unit's.

## 4. Design

`requires` is read at exactly one place in the deployer: `derive_install_order`
(`govkit.py:486-518`). Its comprehension at `:504-505` is
`{d for d in (descs[i][0].get("requires") or []) if d in want and d != i}`, so an edge whose target is
outside the selection is dropped before it can constrain anything, and the only thing the function
raises is a cycle (`:510-515`). Its own docstring says so at `:495-496`:

> A dependency OUTSIDE the selection is not an error: `--kits drift-audit` is a legal install and
> orders one entry. Only the edges among the selected ids constrain the order.

`resolve_selection` (`:521-590`) has four `derive_install_order` call sites — `:558` for `--all`,
`:567` for `--kits`, `:582` for the target's own declared list, `:590` for the registry default. Each
passes `all_kits(descs)` or a `sorted()` of an already-fixed id list, and not one adds a `requires`
target. Observed rather than only read: `plan --target <virgin> --kits unattended` at this base exits
**0** and prints `selection: unattended`. The `memory-tree` edge that has existed all along pulled
nothing and complained about nothing.

### Arm A — the registry

Check 7 (`govkit.py:1326-1341`) already validates that a `requires_if` edge names a registry entry, at
`:1330-1333`. Plain `requires` gets no such arm, so a typo names nothing and reds nothing. The header
comment at `:1326-1327` gains the plain-`requires` clause and the body gains a loop shaped on its
sibling:

```python
for dep in d.get("requires") or []:
    if dep not in descs:
        r.fail(f"entry '{eid}' requires '{dep}', which is not a registry entry — the edge then "
               f"orders nothing and reds nothing, which is how it was found")
```

It extends check 7 rather than taking a new number, because check 7 is already the single place a
dependency edge's kit NAME is graded. `selfcheck` takes no `--target` and reads no receipt, so the
name is the only question it can answer.

### Arm B — the installed set

"Adopt time" is `apply`, not the verb named `adopt`. `cmd_adopt` (`:7650`, body `_cmd_adopt` at
`:7668`) writes "the receipt an already-installed tree never had" (`:7670`) and installs nothing, so a
check there could never fire. The verb that installs is `apply`.

`cmd_apply` at `:4243` is a thin wrapper whose only job is the lock's `finally`; the body is
`_cmd_apply` at `:4258`, and that is where the check lands. Placement is immediately after the AC8
block at `:4282-4288` and before `demand_writable_target` at `:4295`, so nothing has been written yet.

No new probe is needed, because AC8 already narrowed the question. `foreign_kit_present`
(`:3891-3898`) returns registry entries resolvable in the target that this target's receipt does not
claim, and `:4283` refuses when it returns anything. So by the time control reaches the new check, a
present-but-unclaimed kit has already killed the run, and the satisfied set is exactly:

```python
installed = set(selection) | set((receipt or {}).get("kits") or [])
```

with `selection` from `:4272` and `receipt` from `:4275-4276`. One `raise Refusal`, no new primitive.

### The preview row

`cmd_plan` (`:2615`, selection at `:2622`) reads no receipt today and needs the same two lines
`_cmd_apply` has at `:4275-4276`. The row is a bare `print`, NOT an `r.fail`: `cmd_plan` returns
`r.emit()`, so a finding there would move an exit code this unit is not moving. The precedent is
directly above it — the `SILENT [...]` row at `:2648` prints without moving the exit — and
`WIRE-INTO-PROJECT.md:658` states the convention: "A gap never changes the exit code — it is a state
of the world, not a fault in the run." A preview that promises an apply which will then refuse is the
defect class this build exists for; a preview that reds on it is a different verb.

Because the row is a `print`, it adds no refusal branch. This unit adds exactly TWO: arm A's `r.fail`
and arm B's `raise Refusal`.

### Inventory

The candidate predicates were RUN over all 25 registry entries, resolved through `registry.toml` by
`govkit.read_descriptors`, not reasoned about.

| measurement | result |
|---|---|
| registry entries | 25 |
| plain-`requires` edges | 9 |
| arm A HITS (an edge naming a non-entry) | **0** |
| arm B unsatisfied over the DEFAULT selection (`registry.toml:36`) | **0** |
| arm B unsatisfied over `--all` (20 non-conditional entries) | **0** |
| arm B unsatisfied over a single-kit selection into a virgin target | **9 of 25** |
| `refusal_join.py` live branch count at this base | **244** across 4 modules |

The nine near-misses, every edge that passes arm A: `agent-cap→settings-merge` ·
`check-agent-cap-restatement→agent-cap` · `check-microformats→playbook` · `codebase-map→memory-tree` ·
`drift-audit→memory-tree` · `memory-recall→memory-tree` · `playbook-render→playbook` ·
`review-harness→agent-cap` · `unattended→memory-tree`.

With the new edge applied, `derive_install_order` over the whole chain returns
`['memory-tree', 'settings-merge', 'agent-cap', 'review-harness', 'unattended']`, so `review-harness`
orders before `unattended`, which is the whole of what the edge buys.

**What arm B breaks, stated before anything else.** All nine single-kit selections refuse, and one of
them is `--kits drift-audit`, the exact invocation `:495-496` calls legal. That docstring stays
literally true about `derive_install_order` and gains a clause naming the verb one layer up, in the
same commit.

**And a cost the design of record did not price: gov's own suite.** Nine `--kits` invocations in
`tools/govkit/selftest.py` name a kit whose dependency is not in their selection, so arm B refuses
them — `codebase-map` at `:455`, `:487`, `:2490`; `drift-audit` at `:2248`, `:2268`; `memory-recall`
at `:1510`, `:1527`, `:1535`, `:1551`. Two `plan` call sites (`:543`, `:2304`) gain the new row and
keep their exit code. Seventy-eight other `--kits` invocations stay green.

The repair is adding the missing dependency to each of those nine `--kits` values, and it was priced
rather than assumed:

- **The exit code does not move.** Measured into scratch targets: `apply --kits codebase-map` exits 0,
  and `apply --kits codebase-map,memory-tree` also exits 0. `memory-tree`'s seed-and-stop is a
  declared accepted outcome and does not turn a passing arm into a failing one.
- **No arm asserts an absolute count that a larger selection would move.** The nine sites' assertions
  key on receipt rows BY PATH, on stdout substrings, or on `>=` thresholds. The one count-sensitive
  assertion in range, after `:487`, is the relative idempotency compare
  `len(rec["files"]) == len(rec2b["files"])`, which survives a larger selection.

**What `refusal_join.py` actually demands, corrected.** It does not demand a named arm for a new
refusal branch. Its join half runs only when argv names a reached-set file (`:175-176`), and the leg's
argv is `["python", "tools/govkit/refusal_join.py"]` with no such argument, so the join never
executes. Run at this base it prints `refusal-join: 244 branch(es) across 4 module(s) — enumeration
only; pass a reached-set to join` and exits 0, and the file says the same thing about itself at
`:110-115`. What runs is a shrink-only FLOOR, `if len(branches) < BRANCH_PIN` at `:166`, against
`BRANCH_PIN = 217` (`:41`). The live population is 244, so the pin trails by 27 and two new branches
keep it green with no move.

`BRANCH_PIN` is therefore NOT bumped by this unit, and that is a deliberate choice rather than an
omission. A `217 → 219` move would write a ledger entry claiming two new branches took the pin to the
population, when the population is 246 — arithmetic on a base that is already 27 stale, asserting a
relationship that does not hold. Re-baselining the pin (and `FILE_PIN`, at 1 against a live 4) is its
own act with its own reason, and it is filed as a backlog row rather than smuggled in here. The arms
in `selftest.py` are still written, because the file's stated doctrine asks for them; what this spec
does not claim is that anything reds if they are absent.

### Migration

None. Arm A grades gov's own descriptors and changes no adopter tree. Arm B changes what a NEW
`apply` accepts and cannot reach an install already made — that population belongs to the gate-time
announcement unit, not this one.

### Files touched (estimate)

| file | change |
|---|---|
| `tools/unattended/kit.toml` | `:7` gains `review-harness` |
| `tools/govkit/govkit.py` | check 7 arm, `_cmd_apply` refusal, `cmd_plan` row and receipt read, `:495-496` clause, `KIT_GOVKIT_VERSION` |
| `tools/govkit/selftest.py` | two new arms at the `:2405-2430` seam, nine `--kits` repairs |
| `memory/backlog/DEPL.md` | the mis-spelled-key row and the stale-pin row |

`tools/install-prefix-carried.txt` does NOT move. `tools/unattended/kit.toml` carries a row at `:111`
at count 2, and a kit id in a `requires` array is not a path literal. `govkit.py` and `selftest.py`
carry no row at all, which is why S7 requires the new strings to name kit ids and never a `tools/`
path — the ratchet is a BAN (`check-install-prefix.sh:315-319`), so any rise is hand-justified.

### Alternatives rejected

- **A new check number for arm A.** Splitting `requires` into its own check puts one class in two
  places. Check 7 already owns the "does this edge name a real kit" question.
- **Making arm B report instead of refuse.** `_cmd_apply` is a refuse-before-writing verb and both its
  neighbours refuse. Install happens once, so a report at install time is a line in a stream nobody
  re-reads.
- **Scoping arm B to `unattended` alone** to spare the other eight edges. That is an instance gate
  wearing a class gate's clothes, and it is the shape §7 names outright.

## 5. Production-readiness checklist

- **security** — arm B reads `selection` and the target's own receipt, both already trusted inputs on
  this path. It refuses BEFORE `demand_writable_target`, so it cannot widen a write.
- **perf / scale** — two set operations over a selection of at most 25 ids. Not measurable.
- **a11y** — N/A: a CLI refusal on an operator's terminal.
- **i18n** — N/A: this repo's tooling is English-only by construction.
- **error / empty / loading states** — an entry with no `requires` key yields `[]` via
  `d.get("requires") or []`, the same guard `derive_install_order:504` uses; a target with no receipt
  yields `set()` via `(receipt or {}).get("kits") or []`.
- **observability** — arm B's refusal and `cmd_plan`'s row both name the kit, the missing dependency
  and the remedy. Nothing is logged elsewhere.
- **risks** — the named one is that arm B refuses nine selections that are legal today, nine of gov's
  own selftest call sites among them. Priced in §4 and raised as fork F2. Rollback is a one-line
  revert of the refusal; the edge and arm A can stand without it.
- **testing + left-shift gates** — arm A's failing case is a staged typo observed RED before landing.
  Arm B's four arms are §6's AC3 through AC6. Both arms' behaviour rides `govkit selftest`, which no
  boundary runs, and §7 says so rather than implying coverage.
- **migration / rollback** — no migration. See §4.
- **user docs** — `WIRE-INTO-PROJECT.md` gets no new section; the docstring clause at `:495-496` is the
  documentation change, because that sentence is the one a reader quotes back.

## 6. Acceptance criteria

- **AC1** — When `python tools/govkit/govkit.py selfcheck` runs on the untouched tree, it exits 0.
  Already observed at this base, so arm A's green half needs no staging.
- **AC2** — When `tools/unattended/kit.toml:7` is staged as `requires = ["memory-tree",
  "reviewharness"]` and `selfcheck` is re-run, it exits non-zero naming entry `unattended` and id
  `reviewharness`; unstage after. This is arm A's FAILING CASE and it is observed before landing.
- **AC3** — When `python tools/govkit/govkit.py apply --target <virgin> --kits unattended` runs
  against a target seeded with `.governance/deploy.toml`, it refuses naming BOTH `memory-tree` and
  `review-harness`. Both, because an arm expecting one name passes on a half-built check.
- **AC4** — When the selection names every link, `apply --kits
  memory-tree,settings-merge,agent-cap,review-harness,unattended` passes the new check.
- **AC5** — When a target whose receipt already claims `review-harness` and `memory-tree` is given
  `apply --kits unattended`, it passes; the carve-out reading that receipt at `govkit.py:4275-4276`
  is exercised, not assumed.
- **AC6** — When `plan --target <virgin> --kits unattended` runs, it prints the unsatisfied-dependency
  row AND still exits 0. The baseline is observed: at this base it exits 0 and prints nothing about
  the missing dependency.
- **AC7** — When `plan --target <t> --kits review-harness,unattended` runs, its `selection:` line
  orders `review-harness` before `unattended`, which is the only thing the edge itself buys.
- **AC8** — When `python tools/govkit/selftest.py` is run BY HAND, it exits 0 with all nine repaired
  `--kits` call sites and both new arms. No boundary runs this, so the landing report states that it
  was run by hand and gives the exit code.
- **AC9** — When `python tools/govkit/refusal_join.py` runs, it exits 0 and reports a branch count
  exactly two higher than the 244 measured at this base, with `BRANCH_PIN` unmoved at 217.
- **AC10** — When `bash tools/check-kit-versions.sh` runs, it exits 0 with `KIT_GOVKIT_VERSION` and
  every `unattended` carrier agreeing.
- **AC11** — When `bash tools/check-install-prefix.sh` runs, it exits 0 and
  `tools/install-prefix-carried.txt` is unchanged, because the two new strings name kit ids and no
  `tools/` path.
- **AC12** — When the `derive_install_order` docstring is read at `govkit.py:495-496`, its
  `--kits drift-audit` sentence carries a clause naming the apply-time check, landed in the same
  commit as arm B.
- **AC13** — When arm B refuses, its message names the remedy (add the dependency to the selection, or
  install it first) and not only the fault, matching the house style `_check_kits_shape` sets at
  `govkit.py:544-554`.

## 7. Gates

- **`govkit selfcheck`** — chunk `declarations`, subject `repo`, no guard, so every bar. This is arm
  A's standing boundary and the only standing reader of either arm.
- **`govkit refusal join`** — chunk `declarations`, subject `repo`, guard `tools/govkit/`, which this
  diff touches. It grades the branch COUNT against a shrink-only floor. It does NOT grade that either
  new branch is armed, because its join half never executes under the leg's argv.
- **`kit version markers`** — every bar, for S8.
- **`install-prefix (shipped surface)`** — every bar, for AC11.
- **`memory hygiene`** — every bar, for this spec and the backlog rows.
- **`govkit selftest`** — chunk `selftests`, subject `kit`. It is the ONLY reader of arm B's
  behaviour and NO boundary runs it, not even `GATE_FULL=1`, which holds every `subject = kit` or
  `chunk = selftests` leg. It needs `GATE_SELFTESTS=1` or a hand run. This is a disclosed exemption,
  and AC8's by-hand run is its compensating check.

This unit adds no gate leg and registers nothing in `tools/gate-legs.json` or `registry.toml`.

## 8. Open questions

- **F1 — the `unattended` version bump collides with the route unit.** `tools/unattended/kit.toml`
  ships to adopters (its `[[files]] include = "**"` row is role `engine`, and a `plan` for
  `--kits unattended` lists 40 rows, `kit.toml` among them), so this unit's descriptor change owes the
  1.17 → 1.18 bump. The route unit in this same build also bumps `unattended` 1.17 → 1.18, and the
  bump has eight carriers, five of them `tools/unattended/*.template.md` markers
  (`check-kit-versions.sh:179-192`). Two units cannot both make the same move.
  **Recommendation: whichever of the two lands FIRST performs the bump across all eight carriers, and
  the second asserts `bash tools/check-kit-versions.sh` exit 0 without moving the version again.**
  Nothing machine-enforces the bump either way — `check-kit-versions.sh` grades marker PRESENCE
  (`:17-19`) and marker/constant AGREEMENT (`:164-192`), and no branch in it reads a diff to ask
  whether a body change earned a bump — so the risk of the wrong choice is a stale version, not a red
  bar. Note the consequence: because the bump edits `SKILL.template.md`'s marker, whichever unit takes
  it becomes an owner turn under D1.
- **F2 — arm B refuses nine selections that are legal today, and gov's own suite is nine of them.**
  The owner ruled REFUSE on evidence that named the docstring's `--kits drift-audit` example and
  nothing else. This spec's measurement adds that nine `govkit selftest` call sites across three kits
  break, and that the repair is nine one-token edits whose exit codes and assertions were measured
  safe (§4). D4 was already retaken once when the facts under it turned out to be wrong, so this
  belongs in front of the owner rather than absorbed quietly.
  **Recommendation: keep REFUSE as ruled and land the nine repairs inside this unit.** The evidence
  strengthens the ruling rather than undermining it — a dependency edge that gov's own suite can
  ignore nine times over is exactly the dead declaration this unit exists to end — but the owner sees
  the number at scope approval, not in the landing report.

## 9. Revision log

- rev-1 · 2026-09-04 · initial draft, grounded on `origin/main` at `c4fcf5ad` with every cited line
  re-opened locally. Five corrections to the design of record, each measured rather than argued:
  (1) `refusal_join.py` does NOT demand a named arm for a new refusal branch — its join half runs only
  when argv names a reached-set (`:175-176`), the leg's argv passes none, and a run at this base
  prints `enumeration only` and exits 0. The design priced it as a standing demand.
  (2) `BRANCH_PIN` is a shrink-only floor at `:166`, the live population is 244 against a pin of 217,
  and two new branches keep it green. The design's `217 → 219` bump is not owed and is not taken,
  because it would assert a pin-to-population relationship that is 27 short of true.
  (3) The `cmd_plan` row adds NO refusal branch. `cmd_plan` returns `r.emit()`, so the design's own
  "its exit code does not move" forces a bare `print` rather than an `r.fail`, and a `print` is not in
  `_is_refusal`'s two shapes. The design counted it as one of the pair.
  (4) `cmd_apply` at `:4243` is a lock wrapper; the body is `_cmd_apply` at `:4258`. The AC8 placement
  is correct, but `refusal_join.py` anchors on the ENCLOSING function, so arm B's anchor is
  `_cmd_apply`.
  (5) The design omits `KIT_GOVKIT_VERSION = "1.9"` (`govkit.py:44`), asserted at
  `check-kit-versions.sh:238`. A change to the deployer engine owes that bump by the same convention
  the design applies to `unattended`, and S8 takes it.
  Also new and unpriced anywhere in the design: nine `govkit selftest` `--kits` call sites break under
  arm B. Measured, repaired in scope, and raised as fork F2.
- rev-2 · 2026-09-05 · AC5's witness re-pointed. It named `.governance/install.json`, which lives in
  an adopter target and is not tracked here, so the criterion asserted the existence of a file this
  repo will never hold. It now names the receipt by role and cites the read at `govkit.py:4275-4276`,
  which is the seam the carve-out actually exercises. No criterion was weakened or dropped, and the
  set of things AC5 observes is unchanged.

## 10. Reuse audit

`python tools/codebase-map/reuse_lookup.py "validate a kit descriptor dependency edge against the
registry and against the target's installed receipt at install time"` returns a corpus of 645 symbols,
188 inventory keys, 19 affordance seams and 20 dossiers, and its ranked shortlist names the seams this
unit extends rather than any it should have reused instead: `derive_install_order`
(`tools/govkit/govkit.py`), `read_descriptors` (same), `foreign_kit_present` (same), and the
`registry.toml` affordance seam under the `govkit` dossier. The seam this unit extends is therefore
`tools/govkit/govkit.py` at two existing sites — `selfcheck` check 7 (`:1326-1341`), whose
`requires_if` arm at `:1330-1333` the registry arm is modelled on byte-for-byte, and `_cmd_apply`'s
refusal sequence (`:4282-4295`), whose AC8 block already computes the installed-set narrowing arm B
needs. The test seam is `tools/govkit/selftest.py:2405-2430`, the existing `requires` arm cluster. No
new module, helper or primitive is created, and the probe surfaced no candidate that would let either
arm be written somewhere cheaper.

Recall terms used: requires, requires_if, registry entry, derive_install_order, resolve_selection,
selfcheck check 7, cmd_apply, receipt, foreign_kit_present, install order, refusal branch, kit
descriptor, adopter, install-time validation
