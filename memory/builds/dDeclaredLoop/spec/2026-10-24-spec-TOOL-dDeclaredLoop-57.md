# TOOL-dDeclaredLoop-57 — `update` refuses a claimed kit whose `requires` it leaves unmet, on every admission path

**Status:** INPROGRESS · rev-4 · 2026-11-14 · node d · Tier-2 · base ed497191 · streams tooling · order 4 · advances TOOL-dDeclaredLoop-35

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-24-build-TOOL-dDeclaredLoop-1-agent-ledger.md](../build/2026-10-24-build-TOOL-dDeclaredLoop-1-agent-ledger.md) | journal | TOOL-dDeclaredLoop-1 TOOL-dDeclaredLoop-2 TOOL-dDeclaredLoop-3 TOOL-dDeclaredLoop-4 TOOL-dDeclaredLoop-5 TOOL-dDeclaredLoop-6 TOOL-dDeclaredLoop-7 TOOL-dDeclaredLoop-8 TOOL-dDeclaredLoop-9 TOOL-dDeclaredLoop-10 TOOL-dDeclaredLoop-11 TOOL-dDeclaredLoop-12 TOOL-dDeclaredLoop-13 TOOL-dDeclaredLoop-14 TOOL-dDeclaredLoop-15 TOOL-dDeclaredLoop-16 TOOL-dDeclaredLoop-17 TOOL-dDeclaredLoop-18 TOOL-dDeclaredLoop-19 TOOL-dDeclaredLoop-20 TOOL-dDeclaredLoop-21 TOOL-dDeclaredLoop-22 TOOL-dDeclaredLoop-23 TOOL-dDeclaredLoop-24 TOOL-dDeclaredLoop-25 TOOL-dDeclaredLoop-26 TOOL-dDeclaredLoop-27 TOOL-dDeclaredLoop-28 TOOL-dDeclaredLoop-29 TOOL-dDeclaredLoop-30 TOOL-dDeclaredLoop-31 TOOL-dDeclaredLoop-32 TOOL-dDeclaredLoop-33 TOOL-dDeclaredLoop-34 TOOL-dDeclaredLoop-36 TOOL-dDeclaredLoop-37 TOOL-dDeclaredLoop-38 TOOL-dDeclaredLoop-39 TOOL-dDeclaredLoop-40 TOOL-dDeclaredLoop-41 TOOL-dDeclaredLoop-42 TOOL-dDeclaredLoop-43 TOOL-dDeclaredLoop-44 TOOL-dDeclaredLoop-45 TOOL-dDeclaredLoop-46 TOOL-dDeclaredLoop-47 TOOL-dDeclaredLoop-48 TOOL-dDeclaredLoop-49 TOOL-dDeclaredLoop-50 TOOL-dDeclaredLoop-51 TOOL-dDeclaredLoop-52 TOOL-dDeclaredLoop-53 TOOL-dDeclaredLoop-54 TOOL-dDeclaredLoop-55 TOOL-dDeclaredLoop-56 TOOL-dDeclaredLoop-58 TOOL-dDeclaredLoop-59 TOOL-dDeclaredLoop-60 TOOL-dDeclaredLoop-61 TOOL-dDeclaredLoop-62 TOOL-dDeclaredLoop-63 TOOL-dDeclaredLoop-64 TOOL-dDeclaredLoop-65 TOOL-dDeclaredLoop-66 TOOL-dDeclaredLoop-67 TOOL-dDeclaredLoop-68 TOOL-dDeclaredLoop-69 TOOL-dDeclaredLoop-70 TOOL-dDeclaredLoop-71 TOOL-dDeclaredLoop-72 TOOL-dDeclaredLoop-73 TOOL-dDeclaredLoop-74 TOOL-dDeclaredLoop-75 TOOL-dDeclaredLoop-76 TOOL-dDeclaredLoop-77 TOOL-dDeclaredLoop-78 TOOL-dDeclaredLoop-79 TOOL-dDeclaredLoop-80 TOOL-dDeclaredLoop-81 TOOL-dDeclaredLoop-82 TOOL-dDeclaredLoop-83 TOOL-dDeclaredLoop-84 TOOL-dDeclaredLoop-85 TOOL-dDeclaredLoop-86 TOOL-dDeclaredLoop-87 TOOL-dDeclaredLoop-88 TOOL-dDeclaredLoop-89 TOOL-dDeclaredLoop-90 TOOL-dDeclaredLoop-91 TOOL-dDeclaredLoop-92 TOOL-dDeclaredLoop-93 TOOL-dDeclaredLoop-94 TOOL-dDeclaredLoop-95 TOOL-dDeclaredLoop-96 TOOL-dDeclaredLoop-97 TOOL-dDeclaredLoop-98 TOOL-dDeclaredLoop-99 TOOL-dDeclaredLoop-100 |
| [2026-10-24-build-TOOL-dDeclaredLoop-57-deviation-571.md](../build/2026-10-24-build-TOOL-dDeclaredLoop-57-deviation-571.md) | deviation | — |
| [2026-10-24-build-TOOL-dDeclaredLoop-57-promoted-fix-return.md](../build/2026-10-24-build-TOOL-dDeclaredLoop-57-promoted-fix-return.md) | research | TOOL-dDeclaredLoop-58 TOOL-dDeclaredLoop-59 TOOL-dDeclaredLoop-60 TOOL-dDeclaredLoop-61 TOOL-dDeclaredLoop-62 TOOL-dDeclaredLoop-63 TOOL-dDeclaredLoop-64 TOOL-dDeclaredLoop-65 TOOL-dDeclaredLoop-66 TOOL-dDeclaredLoop-67 |
| [2026-11-13-build-TOOL-dDeclaredLoop-57-deviation-572.md](../build/2026-11-13-build-TOOL-dDeclaredLoop-57-deviation-572.md) | deviation | — |
| [2026-11-14-build-TOOL-dDeclaredLoop-57-1-builder-return.md](../build/2026-11-14-build-TOOL-dDeclaredLoop-57-1-builder-return.md) | journal | — |
| [2026-11-14-build-TOOL-dDeclaredLoop-57-deviation-573.md](../build/2026-11-14-build-TOOL-dDeclaredLoop-57-deviation-573.md) | deviation | — |
| [2026-10-24-prompt-TOOL-dDeclaredLoop-57-promoted-fix-brief.md](../prompts/2026-10-24-prompt-TOOL-dDeclaredLoop-57-promoted-fix-brief.md) | research | TOOL-dDeclaredLoop-58 TOOL-dDeclaredLoop-59 TOOL-dDeclaredLoop-60 TOOL-dDeclaredLoop-61 TOOL-dDeclaredLoop-62 TOOL-dDeclaredLoop-63 TOOL-dDeclaredLoop-64 TOOL-dDeclaredLoop-65 TOOL-dDeclaredLoop-66 TOOL-dDeclaredLoop-67 |
| [2026-11-13-prompt-TOOL-dDeclaredLoop-57-1-spec-writer.md](../prompts/2026-11-13-prompt-TOOL-dDeclaredLoop-57-1-spec-writer.md) | journal | — |
| [2026-11-13-prompt-TOOL-dDeclaredLoop-57-reground-brief.md](../prompts/2026-11-13-prompt-TOOL-dDeclaredLoop-57-reground-brief.md) | research | — |
| [2026-11-14-prompt-TOOL-dDeclaredLoop-57-1-spec-writer.md](../prompts/2026-11-14-prompt-TOOL-dDeclaredLoop-57-1-spec-writer.md) | journal | — |
| [2026-11-14-prompt-TOOL-dDeclaredLoop-57-build-brief.md](../prompts/2026-11-14-prompt-TOOL-dDeclaredLoop-57-build-brief.md) | journal | — |
| [2026-11-14-prompt-TOOL-dDeclaredLoop-57-spec-brief.md](../prompts/2026-11-14-prompt-TOOL-dDeclaredLoop-57-spec-brief.md) | research | — |
| [2026-10-24-review-TOOL-dDeclaredLoop-57-spec-audit.md](../reviews/2026-10-24-review-TOOL-dDeclaredLoop-57-spec-audit.md) | spec-audit | TOOL-dDeclaredLoop-58 TOOL-dDeclaredLoop-59 TOOL-dDeclaredLoop-60 TOOL-dDeclaredLoop-61 TOOL-dDeclaredLoop-62 TOOL-dDeclaredLoop-63 TOOL-dDeclaredLoop-64 TOOL-dDeclaredLoop-65 TOOL-dDeclaredLoop-66 TOOL-dDeclaredLoop-67 |

<!-- /gen:spec-records -->

## 1. Goal

The round-2 spec audit (`memory/builds/dDeclaredLoop/reviews/2026-10-24-review-TOOL-dDeclaredLoop-36-spec-audit.md`)
confirmed finding **id 52 at HIGH**, its item **H6**, alone in that item. `TOOL-dDeclaredLoop-36`
relies on `update`'s default-gained path to install the loop kit beside a roles kit that now requires
it. That path gains nothing when the receipt records no `gov_commit`, or when the registry does not
resolve or parse at either vintage: `tools/govkit/govkit.py#derive_default_gained` returns an empty
list and a reason for each. The only `requires` read in `tools/govkit/govkit.py#_cmd_update` passes
the gained kits alone to `derive_unsatisfied_requires`, never the kits the receipt already claims. On
those paths an adopter's roles kit updates to a version that reads a loop kit the target lacks, and
the run prints one `default-gained: none computed` line and goes on. This unit takes the report's
fix. It repairs `TOOL-dDeclaredLoop-36`.

## 2. Scope (IN)

- **S1** — One predicate call once the gained set is final. A new function
  `demand_claimed_requires(claimed, gained, descs, receipt, why)` in `tools/govkit/govkit.py` passes
  the claimed kits plus the gained ones to `tools/govkit/govkit.py#derive_unsatisfied_requires`, the
  one predicate `apply` refuses by. A non-empty answer raises `Refusal`, naming each
  `(kit, dependency)` pair and `apply --kits <kit>,<dependency>` as the route.
  `tools/govkit/govkit.py#_cmd_update` calls it once, on every run that is not source mode: the
  unscoped run, the `--kits`-scoped run and the `--rollback` run, read-only or writing. Observed by
  AC1, AC2.
- **S2** — The refusal says why the default-gained path did not cover the pair, carrying the reason
  string `derive_default_gained` already returns, so "no vintage" and "registry unreadable at a
  vintage" read differently from "the default never held it", which carries no reason clause.
  Observed by AC1, AC2, AC3.
- **S3** — Every claimed kit's edges are graded, not only those of `roles`. `tools/loop/kit.toml`
  declares an empty `requires` at HEAD, and `TOOL-dDeclaredLoop-56` S17 gives it `memory-tree`; from
  then a receipt claiming `loop` without `memory-tree` refuses naming that pair, through this same
  call. Observed by AC3, over fixture descriptors.
- **S4** — The gained-only `while` loop in `_cmd_update` is unchanged and runs first, so a gained
  entry it leaves out is never the subject of S1's refusal, and the ordinary path, a receipt with a
  resolvable `gov_commit` whose default gained `loop`, still gains it. Observed by AC4.
- **S5** — `help/upgrade-steps.md` states the refusal where it already states the loop kit's join: the
  bullet "The `loop` kit joins the default selection" under "What this release's steps do to your
  repository" says that an `update` which cannot work the gain out, or is `--kits`-scoped, over a
  receipt claiming `roles` without `loop`, is refused before it writes, and names the
  `apply --kits roles,loop` route. No bullet is added, so the count word in that section's opening
  sentence stands. Observed by AC5.
- **S6** — `memory/map/generated/symbols.json` is re-rendered by the codebase-map kit's generator,
  `python tools/codebase-map/gen_map.py --write`, so it lists the new function. Observed by AC6.
- **S7** — The one existing selftest fixture S1 reaches, the dRB-11 "fixture B" receipt in
  `tools/govkit/selftest.py`, claims `kickoff-manifest` beside `check-wiring`, so its `update` passes
  S1's call and its arms observe the settings-merge problem line they were written for. §4 "The
  fixture the refusal reaches" holds the evidence and §8 F3 the choice. Observed by AC7, AC8.

## 3. Non-goals (OUT)

- Widening the selection. A `--kits`-scoped update over a receipt that claims roles and not loop is
  refused by S1 too, which is the narrower statement's own consequence; adding the missing kit stays
  the operator's act, as the owner ruled for `apply`
  (`tools/govkit/govkit.py#_cmd_apply`, its ARM B comment).
- The default-plan pins `TOOL-dDeclaredLoop-36` does not re-measure: the audit's id 41, batched into
  `TOOL-dDeclaredLoop-67`.
- A selftest arm over every admission path of every verb, the finding's left-shift at full width: the
  arm under §7 covers the paths of `update` the finding names.
- `tools/govkit/refusal_join.py`'s `BRANCH_PIN`. It is a shrink-only floor and the population is
  already above it, so one more refusal site moves nothing: §7 states the figures.
- A kit version. `tools/govkit/govkit.py` and `help/upgrade-steps.md` ship in no registry entry's
  files, so no descriptor's version moves.
- The source-mode walk on gov's own tree. `_cmd_update` returns from that branch before it reads a
  receipt's claim, and a source-mode receipt grades no kit.

### Edges

- **consumes-from** `TOOL-dDeclaredLoop-36` — `loop` in the registry's default set and the default-gained migration it relies on, whose uncovered paths this unit refuses
- **hands-off** `TOOL-dDeclaredLoop-73` — the `requires` the refusal grades, which that unit reads at `to_commit` (the round-3 spec audit's id 39)
- **hands-off** `TOOL-dDeclaredLoop-75` — the refusal's committed fixture, its write-path observation and its every-pair route (the round-3 spec audit's ids 11, 36, 40)

## 4. Design

### Evidence

Read at HEAD `32915e09`, 2026-11-13.

- `tools/govkit/govkit.py#derive_default_gained` returns `([], why)` for a receipt with no
  `gov_commit`, for a registry blob that does not resolve at either vintage, and for one that does
  not parse there.
- `tools/govkit/govkit.py#_cmd_update` reads the receipt's `kits` into `claimed`, carries or releases
  each retired claim through `upgrade_steps.resolve_claim`, then computes `gained`. A `--kits` run
  skips the derivation and gains nothing. Its `while True` loop passes `gained` alone to
  `derive_unsatisfied_requires`, so a claimed kit's dependency is never asked about.
- `tools/govkit/govkit.py#_cmd_apply` refuses through the same predicate, so the update and the
  install answer one question one way after this unit.
- `tools/roles/kit.toml` requires `kickoff-manifest`, `memory-tree` and `loop`, and
  `tools/govkit/registry.toml` holds `loop` in `[selection] default`: both landed with
  `TOOL-dDeclaredLoop-36`. At base `ed497191` the default set holds `roles` and not `loop`.
- The `--kits` flag takes one comma-joined argument (`tools/govkit/govkit.py#parse_args` splits its
  value on `,`), and a second bare word is refused as an unknown argument. rev-2's route spelled the
  pair with a space; the route here is comma-joined.
- `tools/govkit/govkit.py#main` catches `Refusal`, writes `govkit: <text>` to stderr and returns the
  refusal exit, which AC1's probe read as `2`.
- Today's red, observed by AC1's probe at HEAD: over a receipt claiming `kickoff-manifest`,
  `memory-tree` and `roles` with no `gov_commit`, `update` prints `default-gained: none computed` and
  goes on to a later, unrelated refusal about the absent `deploy.toml`. The predicate over that
  claimed set answers `[('roles', 'loop')]`, PINNED, measured 2026-11-13.

### The call

```python
def demand_claimed_requires(claimed, gained, descs, receipt, why):
    unmet = derive_unsatisfied_requires(list(claimed) + list(gained), descs, receipt)
    if unmet:
        pairs = ", ".join(f"'{k}' requires '{d}'" for k, d in unmet)
        raise Refusal(f"update would leave {pairs} unmet"
                      + (f"; default-gained did not cover it: {why}" if why else "")
                      + f"; `apply --kits {unmet[0][0]},{unmet[0][1]}` installs both")
```

`_cmd_update` calls it as `demand_claimed_requires(claimed, gained, descs, receipt, _gained_why)`,
directly after the gained-only `while True` loop closes and before the `default-gained` and
`would gain` lines print. So a refused run never prints a gain it did not make, the reason reaches
the operator inside the refusal, and nothing is written: the receipt's claim, `deploy.toml` and the
index are all touched after that point. A writing run has already taken the write lock by then, and
`cmd_update`'s `finally` releases it.

The function sits beside `derive_unsatisfied_requires` and `derive_default_gained`, the two it
joins. Its name follows the `demand_` functions `_cmd_update` already calls for a precondition that
refuses.

### The fixture the refusal reaches

Read at HEAD `0d9bdeb4`, 2026-11-14, after the builder return named in §9's rev-4 line.

- The dRB-11 "fixture B" block builds its target with `stale_target("rq11b", ...)` and no `kits`
  argument (`tools/govkit/selftest.py@866a0710f:6194`), so `apply --kits check-wiring` writes the
  receipt and it claims `check-wiring` alone. The block then appends `agent-cap` to the receipt's
  `kits` by hand (`tools/govkit/selftest.py@866a0710f:6206`) and runs `update --write`
  (`tools/govkit/selftest.py@866a0710f:6227`).
- `tools/hooks/kit.toml` declares `agent-cap`'s `requires` as `settings-merge` and
  `kickoff-manifest`. `OLD` resolves to `24f39915` itself, whose registry default already holds
  `kickoff-manifest`, so the update never gains it. The gained-only loop leaves `run-gates`,
  `settings-merge` and `loop` gained, PINNED, measured 2026-11-14 by replaying
  `derive_default_gained`'s set difference and the loop over the live descriptors.
- Over that claim and that gained set the predicate answers `[('agent-cap', 'kickoff-manifest')]`,
  PINNED, measured 2026-11-14. S1's call would refuse the update with exit 2 before the gained
  settings-merge adopter runs, so the arm `[dRB-11] update over fixture B: exactly one problem line
  names settings-merge, and it carries the adopter's cannot read`
  (`tools/govkit/selftest.py@866a0710f:6239`) goes red. The block's "exits non-zero", "no line
  carries the declared stop's means" and "leaves the receipt's gov_commit where it was" arms stay
  green, but against the wrong cause.
- The `rq9p` fixture beside it already passes `kits="check-wiring,kickoff-manifest"` to the same
  helper (`tools/govkit/selftest.py@866a0710f:6117`). With `kickoff-manifest` added to fixture B's
  claim, the predicate answers `[]` and the gained set is the same three kits, PINNED, measured
  2026-11-14, so the update reaches the settings-merge adopter as it does today.

The repair, on F3 (a): fixture B's `stale_target` call passes `kits="check-wiring,kickoff-manifest"`,
as `rq9p` does, and the block's header comment gains one sentence saying the claim carries
`kickoff-manifest` because `agent-cap` requires it and the update now refuses a claim that leaves it
unmet. No arm's text or expectation moves.

### Files touched (estimate)

- `tools/govkit/govkit.py`
- `tools/govkit/selftest.py`: the new arm in `check_roles_default`, and fixture B's `stale_target`
  call and header comment (S7)
- `help/upgrade-steps.md`
- `memory/map/generated/symbols.json`

The last is generated: `gen_map.py --write` rewrites it for the new function. No registry row, usage
row, subject pin or leg row moves, since the unit adds no entry, verb, flag or gate leg; the kickoff
manifest's watch list and the verdict-epoch gate's delegate list name nothing this unit touches; and
the new lines spell no install-prefix path.

### Alternatives rejected

- **Pulling the missing dependency in.** It widens the operator's selection, which the owner ruled
  against for `apply`; the refusal names the route instead.
- **A warning line.** The finding's consequence is a broken install that prints one line today; a
  second line is the same defect.
- **Calling after the gain lines print.** A writing run would print `default-gained loop` and then
  refuse, which reports a gain that never landed.

## 5. Production-readiness checklist

- security — a refusal before any write; no new write path.
- perf / scale — one predicate call over the claimed set, which is at most the registry's entries.
- error / empty / loading states — an empty claimed set and an empty gained set pass; the refusal
  names every pair, never only the first, and its route names the first pair.
- observability — the refusal text carries the default-gained reason.
- risks — an adopter that removed the loop kit by hand while its receipt claims roles is now refused
  on update; that install was already broken, and the route is named. The refusal reaches an
  `update` only over a receipt whose claim, after succession, has an edge outside the claimed and
  gained kits. Every receipt producer in `tools/govkit/selftest.py` and `tools/govkit/matrix.py`,
  read at HEAD `0d9bdeb4`:
  - a receipt `apply` writes is closed, since `_cmd_apply` refuses through the same predicate over
    the same working-tree descriptors the later update reads. Matrix's aged gov (its SHAPE 7) edits
    only the registry default between the apply and the update, never a descriptor.
  - a receipt `update --write` writes claims the old claim plus a gained set the gained-only loop
    has already closed.
  - a receipt `adopt` writes claims the deploy's `kits` or the registry default, and is not graded
    by `requires`. Every fixture deploy list names kits whose `requires` is empty, or the default,
    which `check_roles_default` grades closed. The three lists naming a kit with an edge
    (`memory-recall` in `pin_target`, `drift-audit` and `codebase-map` in `a_evil_target`) are only
    run through `apply`, `check` and `plan`.
  - hand-written receipts claim `pytest-parallel-guardrails` or `memory-tree` (empty `requires`), a
    scratch gov's `demo`, whose descriptor declares no `requires`, or a `ghost` id, which
    `upgrade_steps.resolve_claim` refuses before this call. `a_evil_target`'s receipts go only to
    `check` and `plan`. Matrix's receipt-only hook receipt has no `kits` key and feeds
    outcome-state checks, not `update`.
  - the only scratch descriptor that declares an edge is the `demo` of `build_scratch_gov_cross`,
    and those govs are only run through `selfcheck`.
  - dRB-11 fixture A (`rq11a`) claims `agent-cap` without `kickoff-manifest` too. Only `apply` runs
    over it, and this unit leaves `apply` as it is.
  - dRB-11 fixture B (`rq11b`) is the one hit, and S7 repairs it (§4 "The fixture the refusal
    reaches").
- testing — AC1 to AC8 as probes; the arm under §7, observed at the close.
- migration — none: a refusal on a path that produced a broken install. Reversal is reverting the
  call.
- user docs — `help/upgrade-steps.md`, S5.

## 6. Acceptance criteria

- **AC1** — When a probe commits `.governance/install.json` holding `"kits": ["kickoff-manifest",
  "memory-tree", "roles"]`, `"files": []` and no `gov_commit` into a scratch git repository and runs
  `python tools/govkit/govkit.py update --target <scratch>`, the run exits `2`, its stderr names
  `'roles' requires 'loop'`, `gov_commit` and `apply --kits roles,loop`, its stdout holds no
  `default-gained: none computed` line, and `git status --porcelain --untracked-files=all` in the
  target prints nothing. The same receipt under `--kits roles` refuses naming the same pair.
  Red when: the update goes on past the claim and prints `default-gained: none computed`, which is
  what HEAD does.
  fixture: a scratch repository under the session's temp directory holding that one file; the tree
  needs none committed, and `--to` defaults to `HEAD`, so the probe runs before the unit's commit.
- **AC2** — When a probe imports `govkit`, reads the live descriptors and calls
  `demand_claimed_requires(["kickoff-manifest", "memory-tree", "roles"], [], descs, {"kits":
  ["kickoff-manifest", "memory-tree", "roles"]}, "registry.toml does not resolve at 00000000")`, it
  raises `Refusal` whose text names `'roles' requires 'loop'` and `does not resolve`; the same call
  with `gained` set to `["loop"]` returns.
  Red when: the first call returns, so the unreadable-vintage path writes a roles kit without loop,
  or the second raises, so a gained dependency does not satisfy the claim.
- **AC3** — When the same probe passes fixture descriptors in which `loop` requires `memory-tree`, a
  claimed list and receipt holding `loop` alone and an empty reason, `demand_claimed_requires` raises
  `Refusal` naming `'loop' requires 'memory-tree'` with no `default-gained did not cover it` clause.
  Red when: only the edges of `roles` are graded, or an empty reason still prints the clause.
- **AC4** — When AC1's receipt also records `"gov_commit"` as the full sha of `ed497191` and the
  probe runs `python tools/govkit/govkit.py update --target <scratch>`, stdout holds
  `would gain loop` and neither stream holds `update would leave`.
  Red when: S1 refuses over a claim the gained set satisfies, so the ordinary migration breaks.
  fixture: the registry at `ed497191` holds `roles` and not `loop` in its default; the line prints at
  HEAD today, so this criterion is green before the unit and guards it after.
- **AC5** — When `grep -n 'apply --kits roles,loop' help/upgrade-steps.md` runs, it prints one line
  inside the bullet that opens "The `loop` kit joins the default selection", and that bullet says the
  update is refused before it writes.
  Red when: the page still says only that a `--kits`-scoped `update` gains nothing.
- **AC6** — When `grep -c 'demand_claimed_requires' memory/map/generated/symbols.json` runs, it prints
  a count above zero.
  Red when: the generated map was not re-rendered after the function landed.
- **AC7** — When a probe imports `govkit`, reads the live descriptors and calls
  `demand_claimed_requires(["check-wiring", "agent-cap"], ["settings-merge"], descs, {"kits":
  ["check-wiring", "agent-cap"]}, "")`, fixture B's claim before S7, it raises `Refusal` naming
  `'agent-cap' requires 'kickoff-manifest'`. The same call with `kickoff-manifest` added to the
  claimed list and to the receipt's `kits` returns.
  Red when: the first call returns, so the refusal never reached fixture B and S7 repairs nothing,
  or the second raises, so claiming `kickoff-manifest` does not carry fixture B past the call.
  fixture: `settings-merge` is the one gained kit `agent-cap` needs; the others the update gains
  (§4) require nothing fixture B lacks, so the probe leaves them out.
- **AC8** — When `grep -n -A1 'stale_target("rq11b"' tools/govkit/selftest.py` runs, the call it
  prints passes `kits="check-wiring,kickoff-manifest"`, and
  `sed -n '/\[dRB-11\] fixture B: begin/,/\[dRB-11\] fixture B: end/p' tools/govkit/selftest.py | grep -c kickoff-manifest`
  prints at least `2`, the call and the header comment's sentence.
  Red when: fixture B still claims `agent-cap` without `kickoff-manifest`, so its settings-merge
  problem-line arm meets the new refusal instead of the adopter's `cannot read`; the second
  command prints `0` at HEAD `0d9bdeb4`, measured 2026-11-14.

## 7. Gates

`govkit selftest` · `govkit refusal join` · `govkit acceptance matrix` · `policy fixtures` · `recall floor` · `recall floor arms` · `codebase-map coverage + freshness` · `docs` · `help page commands` · `memory hygiene` · `spec tokens (a spec's own names resolve)`

New arm: tools/govkit/selftest.py · covers AC1 AC2 AC3 AC4 · a committed receipt with no gov_commit run through the verb, an unreadable-vintage reason and a loop claim without memory-tree passed to the function, and the base-vintage receipt that gains loop · none

The arm's home is `tools/govkit/selftest.py#check_roles_default`, the module-level function that
already grades the roles kit's default membership and its gain, beside its `OC8 AC2` checks. It adds
seconds to a leg whose declared ceiling in `tools/gate-legs.json` does not move.

What the arm does not check: a `--to` whose descriptors differ from the working tree's
(`TOOL-dDeclaredLoop-73`); the write path's lock and receipt bytes after a refusal, and a route
naming every pair (`TOOL-dDeclaredLoop-75`).

The dRB-11 fixture B arms are existing arms, not a new one, and their text does not move. After S7
the `govkit selftest` leg at the close observes them green over a claim the new refusal passes:
fixture B's update still exits non-zero on exactly one settings-merge problem line carrying the
adopter's `cannot read`, prints no declared-stop means, and leaves `gov_commit` where it was. Their
red, without S7, is §4's measured predicate answer, which AC7 re-observes on the unit's own function.
What they do not check: an update over a receipt claiming `agent-cap` without `kickoff-manifest`,
which the new arm's AC1 to AC3 cases grade through the `roles` and `loop` pairs instead.

What `govkit refusal join` does not check here: the leg runs with no reached-set, so it enumerates
and joins nothing, and the new refusal site is graded by the arm above alone. Its floor is 335 and
the walk finds 499 refusal sites, PINNED, measured 2026-11-13 by `refusal_join.enumerate_branches`
over HEAD.

## 8. Open questions

- **F1 — Which binding line does a unit the spec audit promoted carry?** RESOLVED (agent, 2026-10-24,
  delegated): `**Derived:** PLAY-dClosedLoop-2`, rung 3, as `TOOL-dDeclaredLoop-36` §8 F1 records.
  widens: none · relaxes: none
- **F2 — Does a `--rollback` run take the refusal too?** `_cmd_update` reads descriptors from the
  working tree, so until `TOOL-dDeclaredLoop-73` lands, a rollback to a vintage whose roles kit
  needed no loop is graded by today's edge.
  - (a) Grade every non-source run, rollback included. One call, no branch, and the title's "every
    admission path" holds. The wrong-vintage read is the defect `TOOL-dDeclaredLoop-73` already owns
    for the forward run, and its fix covers the rollback with it.
  - (b) Skip the call under `--rollback`. The escape route is never refused on a newer edge, at the
    cost of a branch that `TOOL-dDeclaredLoop-73` must then take out, and of a rollback that can
    leave a claimed kit without its dependency at the vintage it lands on.
  - Recommendation: (a). The body is written on it.
  widens: none · relaxes: none
  RESOLVED (agent, 2026-11-13, delegated): (a), rung 3: every non-source run takes the refusal, rollback included, one call with no branch.
  widens: none · relaxes: none
- **F3 — How does the dRB-11 fixture B arm stay green once the update refuses its claim?** Its
  receipt claims `agent-cap` without `kickoff-manifest`, and §4 "The fixture the refusal reaches"
  measures that S1 refuses it before the settings-merge adopter runs.
  - (a) Claim `kickoff-manifest` in fixture B: its `stale_target` call passes
    `kits="check-wiring,kickoff-manifest"`, as the `rq9p` fixture beside it does. The gained set does
    not move, so the update still reaches the adopter's `cannot read`, and every arm keeps its text
    and its subject, the update half of TOOL-dRedressedBar-11. Cost: one fixture argument and one
    comment sentence.
  - (b) Let the arm observe the new refusal: fixture B leaves the loop over the three settings-merge
    runs, and an arm of its own expects `update would leave 'agent-cap' requires 'kickoff-manifest'`.
    The fixture then grades the new refusal a second time and no longer grades a hook the receipt
    alone locates through an update's gain, so the dRB-11 update half loses its only fixture.
  - Recommendation: (a). The body is written on it (S7, AC7, AC8).
  widens: none · relaxes: none
  RESOLVED (agent, 2026-11-14, delegated): (a), rung 3: the fixture claims kickoff-manifest as the rq9p fixture beside it does, so its arm still reaches the adopter's line and the update half keeps its only fixture.
  widens: none · relaxes: none

## 9. Revision log

- rev-1 · 2026-10-24 · initial draft, promoted from the round-2 spec audit's id 52 (HIGH, item H6).
- rev-2 · 2026-10-24 · §3 · the Edges block gains the bullets mirroring the edges of
  TOOL-dDeclaredLoop-73 and TOOL-dDeclaredLoop-75, written by the round-3 spec audit's disposal; nothing else moved.
- rev-3 · 2026-11-13 · §1 §2 S1 S3 S5 S6 §3 §4 §5 §6 AC1 AC2 AC3 AC4 AC5 AC6 §7 §8 §10 · re-grounded
  at 32915e09 over the landed TOOL-dDeclaredLoop-36. The mechanism, the function's name and
  signature, the edges, the order and the status did not move. Moved by reading HEAD: the route is
  comma-joined, since `--kits` takes one argument; the call sits before the gain lines print and
  its host is `_cmd_update`; S3 says the loop kit's edge arrives with TOOL-dDeclaredLoop-56; the
  help page that states the loop kit's join (S5) and the generated symbols map (S6) join the write
  set; AC1 and AC4 are probes over a hand-written receipt, run before the commit, and AC2 passes a
  claimed set whose only unmet edge is the loop's; the leg line gains the legs the write set trips;
  every line citation is a symbol citation. F2 is new and open.
- rev-4 · 2026-11-14 · §2 S7 §4 §5 §6 AC7 AC8 §7 §8 F3 §10 · repaired after the divergence in
  2026-11-14-build-TOOL-dDeclaredLoop-57-1-builder-return, which found that the dRB-11 fixture B
  receipt in `tools/govkit/selftest.py` claims `agent-cap` without `kickoff-manifest`, so S1 would
  red its settings-merge arm. Re-read at 0d9bdeb4: §4 gains the fixture's evidence and its repair,
  S7 and AC7, AC8 observe it, §5's unverified risk is replaced by every receipt producer read in
  `tools/govkit/selftest.py` and `tools/govkit/matrix.py`, §7 states what the fixture's arms observe
  after the repair, and F3 is new and open with (a) recommended. The mechanism, the function, its
  call site, the edges, the order and the status did not move.

## 10. Reuse audit

The seam is govkit's one requires predicate, `tools/govkit/govkit.py#derive_unsatisfied_requires`,
the function `apply` refuses by; this unit adds one call to it over the claimed set and no second
reader. `python tools/codebase-map/reuse_lookup.py "update refuses a claimed kit whose requires are
unmet"`, re-run at HEAD, ranks `derive_unsatisfied_requires` and `default_kits` among its
candidates; the others it ranks, `resolve_kit_dir`, `claims`, `kit_rel` and the refusal classes of
other kits, read no `requires`. The predicate was read above and agrees with source. The arm's
fixture seam is the hand-written receipt `tools/govkit/selftest.py#main` already writes into a
scratch target, and its home is `check_roles_default`. S7's repair reuses `stale_target`'s own
`kits` argument, the seam the `rq9p` fixture already uses to claim `kickoff-manifest`, and adds no
helper.

Recall terms used: govkit update requires claimed gained default-gained gov_commit vintage receipt roles loop refusal
