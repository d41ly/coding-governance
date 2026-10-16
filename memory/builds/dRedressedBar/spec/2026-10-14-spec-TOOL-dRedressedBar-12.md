# TOOL-dRedressedBar-12 — an apply narrower than its receipt keeps every other installed kit's claim and rows, so a refused settings-merge exit stays refused on the next run

**Status:** CLOSED · rev-9 · 2026-10-15 · node d · Tier-2 · base ebce889c · streams tooling · order 8

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-14-build-TOOL-dRedressedBar-12-1-acceptance-ledger.md](../build/2026-10-14-build-TOOL-dRedressedBar-12-1-acceptance-ledger.md) | journal | — |
| [2026-10-14-prompt-TOOL-dRedressedBar-12-1-spec-writer.md](../prompts/2026-10-14-prompt-TOOL-dRedressedBar-12-1-spec-writer.md) | journal | — |
| [2026-10-14-prompt-TOOL-dRedressedBar-12-2-revision.md](../prompts/2026-10-14-prompt-TOOL-dRedressedBar-12-2-revision.md) | research | TOOL-dRedressedBar-14 TOOL-dRedressedBar-16 |
| [2026-10-14-prompt-TOOL-dRedressedBar-12-3-spec-writer.md](../prompts/2026-10-14-prompt-TOOL-dRedressedBar-12-3-spec-writer.md) | journal | — |
| [2026-10-14-prompt-TOOL-dRedressedBar-12-4-revision.md](../prompts/2026-10-14-prompt-TOOL-dRedressedBar-12-4-revision.md) | research | TOOL-dRedressedBar-11 |
| [2026-10-14-prompt-TOOL-dRedressedBar-12-5-spec-writer.md](../prompts/2026-10-14-prompt-TOOL-dRedressedBar-12-5-spec-writer.md) | journal | — |
| [2026-10-14-prompt-TOOL-dRedressedBar-16-4-revision.md](../prompts/2026-10-14-prompt-TOOL-dRedressedBar-16-4-revision.md) | research | TOOL-dRedressedBar-16 |
| [2026-10-14-prompt-TOOL-dRedressedBar-17-4-revision.md](../prompts/2026-10-14-prompt-TOOL-dRedressedBar-17-4-revision.md) | research | TOOL-dRedressedBar-17 TOOL-dRedressedBar-9 TOOL-dRedressedBar-13 TOOL-dRedressedBar-14 TOOL-dRedressedBar-15 |
| [2026-10-15-prompt-TOOL-dRedressedBar-19-4-revision.md](../prompts/2026-10-15-prompt-TOOL-dRedressedBar-19-4-revision.md) | research | TOOL-dRedressedBar-19 TOOL-dRedressedBar-14 TOOL-dRedressedBar-15 TOOL-dRedressedBar-16 TOOL-dRedressedBar-17 TOOL-dRedressedBar-18 |
| [2026-10-15-prompt-TOOL-dRedressedBar-23-2-revision.md](../prompts/2026-10-15-prompt-TOOL-dRedressedBar-23-2-revision.md) | research | TOOL-dRedressedBar-23 TOOL-dRedressedBar-14 TOOL-dRedressedBar-15 TOOL-dRedressedBar-16 TOOL-dRedressedBar-17 |
| [2026-10-14-review-TOOL-dRedressedBar-12-15-spec-audit-round1.md](../reviews/2026-10-14-review-TOOL-dRedressedBar-12-15-spec-audit-round1.md) | spec-audit | TOOL-dRedressedBar-13 TOOL-dRedressedBar-14 TOOL-dRedressedBar-15 |
| [2026-10-15-review-TOOL-dRedressedBar-1-20-diff-review-round1.md](../reviews/2026-10-15-review-TOOL-dRedressedBar-1-20-diff-review-round1.md) | diff-review | TOOL-dRedressedBar-1 TOOL-dRedressedBar-2 TOOL-dRedressedBar-3 TOOL-dRedressedBar-4 TOOL-dRedressedBar-5 TOOL-dRedressedBar-6 TOOL-dRedressedBar-7 TOOL-dRedressedBar-8 TOOL-dRedressedBar-9 TOOL-dRedressedBar-10 TOOL-dRedressedBar-11 TOOL-dRedressedBar-13 TOOL-dRedressedBar-14 TOOL-dRedressedBar-15 TOOL-dRedressedBar-16 TOOL-dRedressedBar-17 TOOL-dRedressedBar-18 TOOL-dRedressedBar-19 TOOL-dRedressedBar-20 |
| [2026-10-15-review-TOOL-dRedressedBar-21-24-diff-review-round2.md](../reviews/2026-10-15-review-TOOL-dRedressedBar-21-24-diff-review-round2.md) | diff-review | TOOL-dRedressedBar-14 TOOL-dRedressedBar-15 TOOL-dRedressedBar-16 TOOL-dRedressedBar-17 TOOL-dRedressedBar-18 TOOL-dRedressedBar-19 TOOL-dRedressedBar-21 TOOL-dRedressedBar-22 TOOL-dRedressedBar-23 TOOL-dRedressedBar-24 |

<!-- /gen:spec-records -->

## 1. Goal

The spec audit of units 10 and 11
(`reviews/2026-10-14-review-TOOL-dRedressedBar-10-11-spec-audit-round1.md`) exited CONVERGED with
24 confirmed findings. One is HIGH: report id 23, item H1. BUILD-METHOD M4 promotes a HIGH to its own
unit, and this is that unit. It repairs `TOOL-dRedressedBar-11`, so its order is one above unit 11's.

| id | grade | item | sits in | what is wrong | closed by |
|---|---|---|---|---|---|
| 23 | HIGH | H1 | unit 11 §4 "Which receipt bytes", its first "What an adopter sees change" row, AC3 and fixture A | the refusal unit 11 adds lasts one run: the refused apply still writes a receipt holding only its selection's rows, so the next identical apply finds no hook and accepts the stop | S1 to S4 |

`_cmd_apply` writes `kits: selection` and `files: rows` (`tools/govkit/govkit.py:8019-8021`), and
`rows` holds only the selection's rows (`:7393`). So every apply narrower than the receipt's claimed
kits discards the other kits' claims and rows. The receipt is the only record of a renamed kit home
(`resolve_kit_dir`, `:196-230`), so unit 11's receipt-reading term reads absent on the next run.
The drop is not settings-merge's alone: after it, a re-apply of any dropped kit refuses that kit as
foreign. This unit keeps every claimed kit the selection did not name, with its rows verbatim, as
the `pins` union at `:7402-7407` already does for line-ending pins.

## 2. Scope (IN)

- **S1** — `_cmd_apply`'s RECEIPT step (`tools/govkit/govkit.py:8017-8030`) writes, after the
  selection, every kit the prior receipt claims that the selection does not name. It does so in the
  prior receipt's order, as `_carried_kits`. After this run's `rows` it writes every prior-receipt
  row whose `kit` is one of those kits, verbatim, as `_carried_rows`. `install.sums` and the
  `STEP_RECEIPT` line are derived from the same written list. When `_carried_kits` is non-empty, one
  line `govkit apply — receipt KEEPS <k> kit(s) this selection did not name, with their <n> row(s)
  verbatim: <ids>` prints before the step line. Observed by AC1 and AC3.
- **S2** — The `carry_out_of_scope` paragraph of `write_gate_legs`'s docstring (`:4039-4043`) stops
  saying that `apply` rewrites `kits` and `files` to its own selection. It says that `apply` keeps
  them whole for a kit its selection did not name (`TOOL-dRedressedBar-12`) and still passes no
  carry set, because a leg row such a kit loses from `emitted` is re-claimed by the same-argv rule
  (`:4143-4152`) on that kit's next run. Observed by AC4.
  Inline note (`TOOL-dRedressedBar-19`, units-16-18 report id 31): this rationale, the same-argv
  re-claim, is superseded by TOOL-dRedressedBar-16. An argv gov has changed is never claimable, so
  `apply` now passes the carry, and the paragraph keeps this unit's id beside unit 16's.
- **S3** — Two arms in `tools/govkit/selftest.py`. A new `[dRB-12]` block follows unit 11's
  `[dRB-11]` block, in the scope that defines `stale_target`. It applies a three-kit selection,
  applies a narrower one over it, and re-applies a kit the narrower one did not name. Unit 11's
  fixture A, in the `[dRB-11]` block, gains a third identical apply. Observed by AC1, AC2 and AC3,
  through the `New arm:` lines in §7.
- **S4** — Spec 11 is corrected in place by this unit's spec-writer pass, `<w12>`, which runs once
  unit 11 is CLOSED and before the build pass (§4 "The spec-11 correction's pass"). It takes one rev
  bump whose revision line names report id 23 and this unit's AC2. Two things change in its §4
  "Which receipt bytes". It states that a refused apply still writes its receipt and that a later
  run reads that receipt, which this unit keeps whole. The "After" cell of the first "What an adopter
  sees change" row says the refusal holds on every re-run. Spec 11's AC3 text does not move, and
  this unit's AC2 observes the re-run. The build pass writes no spec file but this one's status and
  date cells. Observed by AC5.
- **S5** — The unit adds no module-level function or class, no text-IO site without an encoding,
  and no kit version. Observed by AC6.
- **S6** — Every reading below goes to this unit's acceptance ledger under
  `memory/builds/dRedressedBar/build/`, carrying `**Serves:** journal TOOL-dRedressedBar-12`.
  Observed by AC5.

## 3. Non-goals (OUT)

- No change to how the selection's own rows are built, staged or stamped. A carried row is the prior
  receipt's dict, unchanged. It gets no new `oid` and no new `commit`.
- No carry of `gate_runner.emitted` in this unit. `write_gate_legs` is still called with no carry
  set (`:7953-7955`). That carry was taken by `TOOL-dRedressedBar-16` (the units-12-15 spec audit's
  report id 7), because the same-argv rule (`:4143-4152`, DEPL-aRepatriatedFork-17 S8) does not
  reach an argv gov has changed. `check_leg_claimable` demands exact argv equality (`:4003-4008`),
  so once gov changes a leg a carried kit lost from `emitted`, that kit's next `update --write` or
  `apply --kits` meets the "already has a leg named" Refusal (`:4153-4159`).
- No carry of an orphan row, one whose `kit` the prior receipt does not claim. `apply` drops it as
  today. The orphan arm (`tools/govkit/selftest.py:10978-11010`) grades that state under `update`.
- No early return on a refused CONFIGURE exit (§4, alternatives).
- No edit to `_cmd_adopt`'s receipt write (`:12653`). It also writes `kits: selection`, and no step
  of this route runs it. Whether a narrower `adopt` drops claims was not measured.
- No receipt schema move. `RECEIPT_SCHEMA` (`:49`) stays 3, because no field is added.
- No repair of a receipt an earlier engine already narrowed. The rows it dropped are on no record
  this engine reads.
- No `help/` page. `help/` holds `README.md` and `roles.md`, and neither covers govkit.

### Edges

- **consumes-from** `TOOL-dRedressedBar-11` — its `must_not_resolve` term, whose receipt reading the
  carried row keeps fed, and its `[dRB-11]` block's fixture A, which S3 runs a third time. Its spec's
  §4 "Which receipt bytes" paragraph and first table row are what S4's pass `<w12>` corrects. Without that unit
  there is no receipt-reading term, and the third run has nothing to refuse. AC2's red half reads its
  pass commit `<p11>`.
- **hands-off** `TOOL-dRedressedBar-13` — the tree this unit leaves. That tree holds spec 11 at this
  unit's rev bump, which unit 13's bump of spec 11 follows. It holds the `[dRB-11]` block with fixture
  A's third run, beside which unit 13 rebuilds fixture B through `write_vintage_receipt`. And it holds
  `_cmd_apply` with S1's carry, in which unit 13 changes how the CONFIGURE call decodes.
- **hands-off** `TOOL-dRedressedBar-14` — `_carried_kits` and `_carried_rows`, which unit 14 binds
  once ahead of CONFIGURE so its early receipt write and the RECEIPT write both carry them. Without
  the carry, fixture A's planted `agent-cap` row leaves the receipt during CONFIGURE.
- **hands-off** `TOOL-dRedressedBar-16` — the `emitted` carry §3 leaves out, which the units-12-15
  spec audit found wedges a carried kit once gov changes one of its leg argvs (report id 7). That
  unit makes `apply` pass `carry_out_of_scope`, rewrites the docstring paragraph S2 writes, and
  corrects this spec's §3 second non-goal and §4 row C5.
- **hands-off** `TOOL-dRedressedBar-17` — the `[dRB-12]` block and the RECEIPT carry, whose
  `install.sums` sidecar and `STEP_RECEIPT` counts S1 claims observed and no criterion here reads
  (report ids 2 and 12). That unit adds those checks to the block and names its AC2 in this spec's
  revision line.
- **hands-off** `TOOL-dRedressedBar-19` — the docstring paragraph S2 writes, whose unit-12 id that
  unit keeps beside unit 16's after unit 16 rewrites the paragraph, and S2 itself, which it marks
  superseded by unit 16 in place (units-16-18 report ids 8 and 31).
- **hands-off** `TOOL-dRedressedBar-23` — the receipt's `orders`. `apply` writes `orders` for its
  selection alone (`:7666-7712`), so an outbox order a carried kit's hole or machine-scoped rule
  owns leaves the receipt on a narrower apply. `check` grades only the orders a receipt records
  (`:5394-5405`), so the loss is a missing instruction and never a refusal. That unit carries every
  prior order of a carried kit after this run's, as S1 carries its rows, and extends the `[dRB-12]`
  block to observe it (round-1 closing diff review report id 4).

## 4. Design

### The drop, measured

Measured on 2026-10-14 at `29c72f51`, whose `tools/` equals `ebce889c`'s
(`git diff --stat ebce889c7 HEAD -- tools skills` prints nothing). One scratch target was used, at
`%TEMP%/drb12`, with `.governance/deploy.toml` holding `DEPLOY_FULL`'s answers
(`tools/govkit/selftest.py:700-710`). The target was committed after each apply. Nothing in the tree
was written.

| Step | Reading |
|---|---|
| 1. `apply --kits agent-cap,settings-merge,kickoff-manifest` | exit 0; `kits` is `kickoff-manifest`, `settings-merge`, `agent-cap`; 18 rows: `(govkit)` 1, `kickoff-manifest` 5, `settings-merge` 1, `agent-cap` 11 |
| 2. `apply --kits settings-merge` | exit 0; `[11/RECEIPT] 2 row(s), 1 kit(s)`; `kits` is `settings-merge`; rows: `(govkit)` 1, `settings-merge` 1 |
| 3. `apply --kits kickoff-manifest` | exit 2: `the target already carries agent-cap (at tools/hooks/agent-cap.js), kickoff-manifest (at tools/manifest-check.sh) and this target's receipt does not claim it` |

So a narrower apply that succeeds drops 16 rows and two claims. After that, a re-apply of either
dropped kit is refused as foreign by `foreign_kit_present` (`:6679-6688`), which reads only the
receipt's `kits`. Report id 23 traced the same drop on unit 11's route. The apply that refuses
settings-merge's exit still writes its receipt, because a non-accepted CONFIGURE exit only calls
`r.fail` (`:7760-7772`). The next identical apply then finds the hook at neither static home and in
no receipt row, and accepts the stop.

The engine already states the rule this breaks, twice. The `pins` union (`:7402-7407`) says that
"a narrower later apply must not un-pin files whose kit is still installed". The seed-row comment
(`:7612-7615`) records that a receipt serialized from one run's writes shrank from one apply to
the next, "taking every later evidence loop with it". `tools/govkit/selftest.py:3115-3117` asserts
that the row count does not shrink, but only over a same-selection re-apply.

### The carry

```python
_carried_kits = [k for k in (receipt or {}).get("kits") or [] if k not in selection]
_carried_rows = [f for f in (receipt or {}).get("files") or []
                 if isinstance(f, dict) and f.get("kit") in _carried_kits]
```

The receipt then writes `"kits": selection + _carried_kits` and `"files": rows + _carried_rows`.
`receipt` is bound once, at `:7251`, before anything is written, and nothing in `_cmd_apply`
rebinds or mutates it. So the carry reads the prior receipt. Both locals are unbound anywhere in
`tools/govkit/govkit.py` (`grep -c '_carried_kits\|_carried_rows'` reads 0).

The carry is keyed on the CLAIM and never on "a kit outside the selection". The synthesized
`.gitattributes` row carries `kit = "(govkit)"` (`:7424-7429`), which no receipt claims. It is
rebuilt on every apply whose pins union is non-empty, so a carry keyed on the selection alone would
write it twice. AC3 shows that this break is visible.

No path dedupe is needed. Selfcheck 4 (`:1993-2002`) refuses two registry entries that write one
destination, so a carried row and a row this run wrote cannot share a path. The carried rows are
appended at the write and enter no list that this run's later steps read. `run_fragment_merges`
(`:7777-7780`) and the index stamp (`:7926-7936`) both see this run's `rows` exactly as today.

### What an adopter sees change

| Situation | At unit 11's tip | After |
|---|---|---|
| `apply --kits settings-merge` over an install that also claims agent-cap and kickoff-manifest | exit 0; the receipt claims settings-merge alone | exit 0; the receipt claims all three and keeps their rows; one `KEEPS` line |
| then `apply --kits kickoff-manifest` | exit 2, refused as foreign | exit 0 |
| unit 11's fixture A, a third identical apply | exit 0; `no-agent-cap-to-wire [accepted stop]` | exit 1; the problem line ends with `cannot read` |
| an apply whose selection covers every claimed kit | as before | unchanged; no `KEEPS` line |

### The spec-11 correction's pass

No one role can write S4's correction and the product files in one commit. Under
`.claude/roles.json`, only `gov-spec-writer` writes spec files and only `gov-builder` writes
product files, and scratch-guard admits a builder's spec edit only where it moves the status and
date cells of a spec its card routes (`tools/hooks/scratch-guard.js:91-99`). So S4 is this unit's
spec-writer pass, `<w12>`, M6's "a review's fixes folded in". The main loop dispatches it at this
unit's turn, once unit 11 is CLOSED, with S4 as its brief, and before the build pass. Spec 11 then
takes its correction as a records fix with its status unchanged. It does not run earlier: spec 11
is unbuilt until then, and unit 11 builds against its §4 as written. A build pass that finds no
`<w12>` returns that to the main loop before any write.

### Files touched (estimate)

- `tools/govkit/govkit.py`
- `tools/govkit/selftest.py`
- `memory/builds/dRedressedBar/build/`

Spec 11 is `<w12>`'s write set, not the build pass's.

### Inventory

| Identifier | Kind | Naming cell |
|---|---|---|
| `_carried_kits`, `_carried_rows` | locals in `_cmd_apply` | none |
| `[dRB-12]` | the check-label prefix of the new selftest block | none |

### Versions

No kit version moves. Both product files sit under `{prefix}/govkit`, which the registry exempts as
the deployer itself (`tools/govkit/registry.toml:295-297`). No function is minted, so
`memory/map/generated/symbols.json` stays as unit 7 regenerates it, and unit 7 need not follow.

### Alternatives rejected

Each candidate was written down with the test that could make it lose, and the pick is M3's.

| Candidate | The test that rejected it | Verdict |
|---|---|---|
| C1 — a refused CONFIGURE exit returns before the receipt write | The bytes are already landed and staged by then. That is the half-install-with-no-receipt state the F4 comment (`:7634-7637`) says this verb is built to avoid. Step 2 above also drops the rows on an apply that refuses nothing | Rejected |
| C2 — only a refused CONFIGURE keeps the prior rows of kits outside the selection | Step 2 exits 0 and drops 16 rows. A later malformed `settings.json` then reaches the accepted stop with no refusal anywhere on the route | Rejected; closes the instance, not the class |
| C3 — every apply keeps the claims and rows of claimed kits it did not select | Its losing test is step 3 and fixture A's third run: either still exiting as at `<p11>` would lose. Both are AC1 and AC2 | Chosen |
| C4 — a hands-off edge naming the drop as an open false-accept route | It leaves a route the review graded HIGH, and the foreign-refusal wedge of step 3 | Rejected |
| C5 — also pass `carry_out_of_scope` so `emitted` keeps a carried kit's legs | The rejection rested on the premise that the same-argv rule re-claims those legs on the kit's next run (`:4143-4152`). That premise is false for an argv gov has changed, which `check_leg_claimable`'s exact equality (`:4003-4008`) refuses (report id 7) | Rejected as YAGNI on that false premise; `TOOL-dRedressedBar-16` takes C5 |
| C6 — the spec-11 correction in the build pass's own commit, as rev-4 wrote it | scratch-guard refuses a builder's edit to another spec, and the spec writer writes no product file, so no role can make that commit (unit 10's divergence, `prompts/2026-10-14-prompt-TOOL-dRedressedBar-10-4-revision.md`) | Refused by the hook |

## 5. Production-readiness checklist

- security — Widens nothing. A carried row is a row this engine wrote into the prior receipt, kept
  verbatim, so no new path is trusted. `resolve_kit_dir` still applies its containment rule to every
  row it reads (`:222`), and `foreign_kit_present` now sees the claims the target really holds.
- perf / scale — N/A — two list comprehensions over the prior receipt, once per apply.
- error / empty / loading states — No prior receipt, or one claiming nothing the selection omits,
  carries nothing. That is the same-selection case, and its output is unchanged. A prior row that is
  not a dict is skipped.
- observability — One `KEEPS` line names each carried kit. The `STEP_RECEIPT` counts are the written
  totals, never this run's alone.
- risks — An existing arm that applies a narrower selection over an applied target and asserts the
  drop would red. A grep of `tools/govkit/selftest.py` for `["kits"] ==` finds `:3514`, an `update`
  arm, and `len(…["files"])` finds `:3116`, a same-selection non-shrink arm. Neither asserts a drop.
  The `govkit selftest` leg grades the rest at the close.
- testing — AC1 to AC6 are scratch fixtures under `%TEMP%`, a source grep and an in-process scan.
  The two arms are declared in §7.
- migration — N/A — no receipt field, conf key or deploy shape moves. A receipt an earlier engine
  narrowed stays narrowed (§3).
- user docs — N/A — `help/` holds no govkit page, and `WIRE-INTO-PROJECT.md` holds no sentence about
  what a narrower apply writes into the receipt (`grep -n -i 'receipt.*kits'` finds only `:1605`,
  about `update`).

## 6. Acceptance criteria

`<p11>` and `<p12>` are the commits of units 11 and 12's build passes, as their acceptance ledgers
name them. `<w12>` is the commit of this unit's spec-writer pass, which §4 "The spec-11 correction's
pass" describes; its subject names `TOOL-dRedressedBar-12`, and this unit's ledger names it. Every command runs from the worktree root. Fixtures live in fresh `git init` targets under
`%TEMP%/<short-name>`, never inside the worktree, with `.governance/deploy.toml` holding
`DEPLOY_FULL`'s answers. Each target is committed after every apply, as `settle` does
(`tools/govkit/selftest.py:583-597`).

- **AC1** — Run the three steps of §4's table with `python tools/govkit/govkit.py apply` at the tip.
  After step 2, `.governance/install.json` claims `settings-merge`, `kickoff-manifest` and
  `agent-cap` in that order. Its `agent-cap` and `kickoff-manifest` rows equal step 1's rows as JSON
  objects, and it holds 18 rows. Step 2's output carries one line opening
  `govkit apply — receipt KEEPS 2 kit(s)`. Step 3 exits 0, and no line carries `already carries`.
  Red when: step 2 leaves `kits` at `settings-merge` alone with 2 rows, and step 3 exits 2 refusing
  both kits as foreign.
  fixture: the red half was observed at spec time on `29c72f51` (§4). The `[dRB-12]` block makes the
  same three applies.
  figure: 18 rows and the 11 and 5 row split are PINNED from step 1 at `29c72f51` on 2026-10-14. The
  arm derives them from step 1's own receipt.
  cost: three applies, about a minute.
- **AC2** — Fixture A of spec 11's AC3, built as it states. After the second apply exits 1, the target
  is committed, and the receipt still holds the `guard/agent-cap.js` row as planted. When
  `python tools/govkit/govkit.py apply --target <t> --kits settings-merge` runs a third time, it exits
  1. No line carries `no-agent-cap-to-wire`, and exactly one line opening `govkit: kit 'settings-merge'`
  carries `cannot read`.
  Red when: the same fixture over a gov clone checked out at `<p11>` writes a receipt with no
  `agent-cap` row on the second apply, and its third apply exits 0 and prints `[accepted stop]`.
  fixture: the red half is the report's traced reading for id 23 and was not run at spec time,
  because unit 11 is unbuilt. The pass observes it first, in a `<p11>` clone under `%TEMP%`. A red
  half that does not exit 0 is returned to the main loop and is not counted.
  cost: a local `git clone` of gov to `%TEMP%` for the `<p11>` half, about a minute.
- **AC3** — When step 1's `apply` runs twice over one target, the second run prints no `KEEPS` line
  and writes the same `kits` list and the same row count. After §4's step 2, exactly one row has role
  `attributes`. In a scratch copy of gov whose carry is keyed on `f.get("kit") not in selection`,
  the same step 2 writes two `attributes` rows.
  Red when: the carry is keyed on the selection and not on the claim, as the staged copy shows.
- **AC4** — When `tr '\n' ' ' < tools/govkit/govkit.py | tr -s ' ' | grep -o 'rewrites .kits. and .files. to its own selection' | wc -l`
  runs at the tip, it prints 0. The docstring of `write_gate_legs`, read with `ast.get_docstring`,
  carries `TOOL-dRedressedBar-12`.
  Red when: the docstring still states the narrowing, as at `ebce889c`, where the count reads 1.
- **AC5** — When `git diff <w12>~1 <w12> -- memory/builds/dRedressedBar/spec/` runs, spec 11 shows
  one header rev change and one new revision line, and that line names report id 23 and this unit's
  AC2. Spec 11 carries a CLOSED header at `<w12>~1`. Spec 11's Design section at `<w12>`, cut with
  `sed -n '/^## 4. Design/,/^## 5/p'` and joined with `tr '\n' ' ' | tr -s ' '`, carries
  `TOOL-dRedressedBar-12`. `git diff --name-only <p12>~1 <p12> -- memory/builds/dRedressedBar/spec/`
  names no file but this spec. The ledger S6 names exists and carries
  `**Serves:** journal TOOL-dRedressedBar-12`.
  Red when: spec 11 takes no bump or two, its revision line misses id 23 or AC2, it was folded before
  it closed, its §4 cut names no unit 12 (as at the audited blob `1b4ea08c`), or the build pass
  writes another spec.
- **AC6** — When `git diff <p11> <p12> -- tools/govkit/ | grep -E '^[+-](def|class) '` runs, it prints
  nothing. A python program that imports `tools/gate-lint/encoding_posture.py` and runs `scan_text_io`
  over `tools/govkit/govkit.py` and `tools/govkit/selftest.py` at `<p12>` counts, per arm, exactly the
  rows `memory/project/encoding-posture-sites.txt` declares.
  Red when: the pass minted a function, or added an unencoded text-IO site.
  figure: DERIVED from the registry at observation; 36 subprocess sites in `govkit.py`, and 24
  subprocess and 1 file-io in `selftest.py`, PINNED 2026-10-14 at `29c72f51`.

## 7. Gates

`govkit selftest` · `govkit acceptance matrix` · `govkit refusal join` · `govkit selfcheck` · `receipt sync (installed files match the receipt)` · `encoding posture (text IO names its encoding)` · `spec tokens (a spec's own names resolve)` · `recall floor` · `recall floor arms` · `memory hygiene`

New arm: tools/govkit/selftest.py · covers AC1 AC3 · the `[dRB-12]` block over the base engine, where step 2 leaves `kits` at `settings-merge` alone and step 3 refuses as foreign · none
New arm: tools/govkit/selftest.py · covers AC2 · fixture A's third identical apply in the `[dRB-11]` block over unit 11's pass `<p11>`, where it exits 0 on the accepted stop · none

The refusal join's floor does not move: S1 adds one print and no refusal branch. The main loop
observes both arms red, then green, at the close.

## 8. Open questions

none

## 9. Revision log

- rev-1 · 2026-10-14 · initial draft, promoted at the CONVERGED exit of the units-10-11 spec audit
  for report id 23 (H1). The drop was reproduced on a three-kit install at `29c72f51`, and five
  candidates were graded by M12, with the pick taken by M3's rule.
- rev-2 · 2026-10-14 · §3 · Edges gain the hands-off to `TOOL-dRedressedBar-14`, which consumes this
  unit's two carried lists for the receipt it writes ahead of CONFIGURE. No scope, design or
  criterion moves.
- rev-3 · 2026-10-14 · §3 · Edges gain the hands-offs to `TOOL-dRedressedBar-16` and
  `TOOL-dRedressedBar-17`, the units the units-12-15 spec audit's findings were promoted into: report
  id 7 to unit 16, and ids 2 and 12 to unit 17. No scope, design or criterion moves.
- rev-4 · 2026-10-14 · §3 · Edges gain the hands-off to `TOOL-dRedressedBar-19`, the batch the
  units-16-18 spec audit's minors were promoted into, for that report's ids 8 and 31. No scope,
  design or criterion moves.
- rev-5 · 2026-10-14 · S4 · §3 · §4 · AC5 · unit 10's builder divergence, applied here
  (`prompts/2026-10-14-prompt-TOOL-dRedressedBar-10-4-revision.md`): no role can make a build-pass
  commit that also edits another spec, because scratch-guard admits a builder's spec edit only to
  its own status and date cells (`tools/hooks/scratch-guard.js:91-99`). The moved item: S4, spec
  11's rev bump with its §4 "Which receipt bytes" and first-row corrections, is now this unit's
  spec-writer pass `<w12>`, dispatched once unit 11 is CLOSED and before the build pass. It is not
  folded now, because unit 11 is unbuilt. §4 gains "The spec-11 correction's pass", Files touched
  lists product files and the ledger only, AC5 reads spec 11 at `<w12>` and observes that the build
  pass writes no other spec, §3's consumes-from edge names `<w12>`, and Alternatives rejected gains
  row C6. No product design or other criterion moves.
- rev-6 · 2026-10-14 · §3 · §4 · a records fix for TOOL-dRedressedBar-16, closing the units-12-15
  spec audit's report id 7 (H1), written by that unit's spec-writer pass `<w16>` as its S4. The
  status stays CLOSED. §3's second non-goal states that the `emitted` carry was taken by
  TOOL-dRedressedBar-16, because the same-argv rule does not reach an argv gov has changed. §4
  Alternatives rejected row C5 states that its rejection rested on that false premise and that unit
  16 takes C5, which TOOL-dRedressedBar-16's AC1 and AC2 observe. S2 and the criteria do not move:
  unit 12 built against them as written.
- rev-7 · 2026-10-14 · S1 · a records fix for TOOL-dRedressedBar-17, closing the units-12-15 spec
  audit's report ids 2 and 12 (item M2), written by that unit's spec-writer pass `<w17>`. The
  status stays CLOSED, and no text above this line moves. S1 says `install.sums` and the
  `STEP_RECEIPT` counts are derived from the written list and are observed by AC1 and AC3. No
  criterion of this spec read either: AC1 to AC6 read neither the sidecar nor the step line, so a
  build carrying kits and rows into `install.json` alone would have passed them. Unit 12 built
  against them as written. TOOL-dRedressedBar-17's AC2 observes the corrected form over §4's steps 1
  and 2: the step line's counts against the receipt's own `files` and `kits`, the sidecar's
  `(sha256, path)` pairs against every receipt row carrying `sha256`, the carried rows included, and
  `govkit check` printing no sidecar mismatch.
- rev-8 · 2026-10-15 · S2 · a records fix for TOOL-dRedressedBar-19, closing the units-16-18 spec
  audit's report id 31 (item L6), written by that unit's spec-writer pass `<w19>`. The status stays
  CLOSED. S2 gains an inline note that its rationale, the same-argv re-claim, is superseded by
  TOOL-dRedressedBar-16, whose rev-6 correction of §3 and row C5 had left S2's half standing. S2's
  claim and AC4 do not move: unit 12 built against them as written, and at `997fc294f` the
  docstring of `write_gate_legs` still carries this unit's id beside unit 16's
  (`tools/govkit/govkit.py:4248-4253`). TOOL-dRedressedBar-19's AC31 observes the note, and its AC8
  observes both ids in the docstring.
- rev-9 · 2026-10-15 · §3 · a records fix for TOOL-dRedressedBar-23, closing the round-1 closing
  diff review's report id 4 (item M3), written by that unit's spec-writer pass `<w23>`. The status
  stays CLOSED, and no scope, design or criterion moves. The external hand-off on `orders` becomes
  the hands-off to TOOL-dRedressedBar-23, the unit the owner promoted id 4 into, which carries a
  carried kit's orders as this unit carries its rows. Its base citations stand. At `c84518fff`
  `_cmd_apply` builds the orders at `tools/govkit/govkit.py:7962-7963` and `:7993-7994` and writes
  them at `:8341-8344`, and `check` grades them at `:5611-5631`. TOOL-dRedressedBar-23's AC1
  observes the carried orders.

## 10. Reuse audit

`python tools/codebase-map/reuse_lookup.py "a narrower apply keeps the install receipt rows and
claims of kits outside its selection"` ranked `resolve_kit_dir` as a SEAM, then name-stem matches
(`rows`, `claims`, `kit_rel`) of other kits. None is a receipt carry. No existing function fits.
The seam extended is inline in `_cmd_apply`. It is the `pins` union at
`tools/govkit/govkit.py:7402-7407`, the one place this verb already reads the prior receipt's claims
past its selection, and S1 applies the same union to `kits` and `files`. A carried row is kept
the way `update` keeps a row it does not touch: left in the receipt it rewrites (`:12010-12068`),
so no row is re-derived. The gotchas checklist for the
two product paths selected `verdict-printed-before-the-step-that-reverts-it`, the report's class for
id 23, which is why AC2 runs the verb once more after the refusal. It also selected
`a-new-local-collides-in-a-long-function`, which is why both locals were grepped unbound, and
`two-answers-to-one-question`, which is why S2 corrects the `write_gate_legs` docstring in the same
pass.

The recall probe returned `memory/builds/cMendedVintage/spec/2026-09-16-spec-DEPL-cMendedVintage-13.md:46-50`
and its ledger. They record that `apply` "rewrites `kits` and `files` to its own selection" as a
fact that unit had to leave alone, not as a ruling. They also record the class in `update`'s terms:
a scoped run that replaced the whole list "would revoke gov's claim", after which later runs refuse.
It returned `TOOL-dRetiredFork-38`, the scoped-`update` stamp defect, as a neighbour of another
mechanism. The review's citation `:7393` and `:8016-8022` held when re-read.

Recall terms used: `python tools/memory-recall/query.py "what does a narrower apply do to the
install receipt rows of kits it did not select" --terms "narrower apply receipt kits selection rows
union pins carry forward foreign kit claimed install.json"`
