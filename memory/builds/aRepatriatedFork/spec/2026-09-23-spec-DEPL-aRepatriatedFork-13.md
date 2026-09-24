# DEPL-aRepatriatedFork-13 — an adopter's own engine is declared, not "unattributed"

**Status:** CLOSED · rev-4 · 2026-09-24 · node a · Tier-2 · base a7c78ad2 · streams deployer+tooling · order 2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-09-24-build-DEPL-aRepatriatedFork-13-1-acceptance-ledger.md](../build/2026-09-24-build-DEPL-aRepatriatedFork-13-1-acceptance-ledger.md) | journal | — |
| [2026-09-23-prompt-DEPL-aRepatriatedFork-13-build-brief.md](../prompts/2026-09-23-prompt-DEPL-aRepatriatedFork-13-build-brief.md) | journal | — |
| [2026-09-24-prompt-DEPL-aRepatriatedFork-13-fold-b-brief.md](../prompts/2026-09-24-prompt-DEPL-aRepatriatedFork-13-fold-b-brief.md) | journal | — |
| [2026-09-24-review-TOOL-aRepatriatedFork-1-closing-diff-round1.md](../reviews/2026-09-24-review-TOOL-aRepatriatedFork-1-closing-diff-round1.md) | diff-review | DEPL-aRepatriatedFork-1 TOOL-aRepatriatedFork-2 TOOL-aRepatriatedFork-3 TOOL-aRepatriatedFork-4 TOOL-aRepatriatedFork-5 TOOL-aRepatriatedFork-6 TOOL-aRepatriatedFork-7 TOOL-aRepatriatedFork-8 TOOL-aRepatriatedFork-9 TOOL-aRepatriatedFork-10 TOOL-aRepatriatedFork-11 TOOL-aRepatriatedFork-12 DEPL-aRepatriatedFork-14 TOOL-aRepatriatedFork-15 TOOL-aRepatriatedFork-16 DEPL-aRepatriatedFork-17 TOOL-aRepatriatedFork-18 TOOL-aRepatriatedFork-19 DEPL-aRepatriatedFork-20 DEPL-aRepatriatedFork-21 TOOL-aRepatriatedFork-21 |

<!-- /gen:spec-records -->

## 1. Goal

inCMS runs four memory-tree programs it wrote BEFORE gov wrote its own, under the same filenames,
plus its own hygiene engine under a different one. Govkit has only two words for such a file:
`engine`, which it grades and would overwrite, or `unattributed`, which blocks the receipt's
`gov_commit` re-stamp forever (`govkit.py:9461-9471`). Neither is true. This unit gives the target a
declared third word, `adopter-owned`, backed by a per-file contract gov holds stable, so `update`
neither grades nor merges such a file, still reports whether it keeps the contract the other kits
call, and stands down the holes that only gov's own engine could discharge.

## 2. Scope (IN)

- **S1** — THE DECLARATION. A target's `.governance/deploy.toml` gains `[[own]]` rows:
  `path` (the adopter's file), `implements` (`<entry id>:<gov source path relative to the kit home>`)
  and `why`. `path` is graded by the STRICT path class (`demand_safe_token` with `prose=False`,
  `govkit.py:910-937`) and by `demand_contained_dest`. `implements` must name a source some rule of
  that entry ships under `role = "engine"`. A row naming a `seed`, `rendered`, `generated` or
  `forked` source is refused, because each of those already states who owns the bytes, and so is
  a source ANY such rule reaches beside an `engine` one. `adopt` also refuses a row whose entry is
  not in the target's selection, and one whose `path` the target's index does not track, because
  the row's `oid` is read from there. Observed by AC1, AC2.
- **S2** — THE ROLE. `UNLANDED_REASON` (`govkit.py:245-257`) gains `adopter-owned`, and
  `UPDATE_ROLE` (`govkit.py:6186-6207`) maps it to a new disposition, `contract`. `ROLE_KINDS` does
  NOT gain it: that table is the vocabulary a DESCRIPTOR may spell (selfcheck arm 3b), and this role
  is a target's claim, so leaving it out makes a descriptor that spells it a refusal. `update` takes
  an `adopter-owned` row's role from the receipt and never re-resolves it against the descriptor,
  which would read it as `engine` and report `role-moved`. `adopt` records such a row with
  `role: "adopter-owned"`, `implements`, `evidence: "declared"` and the target's own `oid` and `sha256`, and no `commit` or `gov_oid`.
  `EVIDENCE_STATES` (`govkit.py:9503`) gains `declared`. The row is NOT counted by the
  `unattributed` tally, so it never withholds the `gov_commit` re-stamp. `cmd_check`'s integrity
  arm already skips every role other than `engine` (`govkit.py:3750`) and so skips it
  unchanged. Observed by AC3, AC4.
- **S3** — THE CONTRACT. A kit descriptor declares `[[contract]]` per engine source other kits
  depend on: `source`, `id`, and clauses of two kinds. A `probe` clause is an argv containing the
  new token `{own}` plus an `expect` regex over its stdout. An `imports` clause is a list of module
  names another shipped file imports from this one. The memory-tree descriptor declares every
  contract the Contract table below lists, each clause citing its consumer. Observed by AC5.
- **S4** — THE PARITY REPORT. For every `adopter-owned` row, `update` and `check` run that
  contract's clauses against the adopter's file and print one line per contract:
  `contract <id> <- <path>: <held>/<total> clauses hold`, followed by each failing clause and the
  consumer that needs it. A failing clause is a REPORT and never `r.fail`, because the adopter owns
  the file. A failing clause whose consumer is itself a receipt row under `role = "engine"` is
  marked `INSTALLED CONSUMER CANNOT RUN` on its report line, because gov then ships a program the
  target cannot execute. It stays a report: at inCMS five such consumers are installed and none is
  wired to a leg, and F3 asks when that should escalate. Per F3's resolution it escalates to
  `r.fail` only when that consumer's installed path appears in the argv of a leg the receipt's
  `gate_runner.emitted` records. Per F2's, a gov `engine` row sharing the owned row's source at
  another path prints one line saying it stays installed, and whether an emitted leg runs it. An
  owned source with no declared contract prints `contract (none)`. Observed by AC6, AC7.
- **S5** — HOLES STAND DOWN. The `stands_down` table `DEPL-aRepatriatedFork-1` adds to `[[hole]]`
  gains `when_owned = ["<source>", ...]`. A hole stands down when every listed source is
  `adopter-owned` at the target, and `check` prints the reason. `measured-pins`
  (`tools/memory-tree/kit.toml:174-180`), whose probe runs `{kit}/corpus_ids.py --check`, declares
  `when_owned = ["corpus_ids.py"]`. `stale-header-waiver` (`tools/memory-tree/kit.toml:300-306`),
  read only by gov's `gen_build_index.py`, declares `when_owned = ["gen_build_index.py"]` for as
  long as that hole exists. Observed by AC8.
- **S6** — THE INCMS DECLARATION, handed over rather than written. The build journal records the
  five `[[own]]` rows inCMS would add, and a scratch-clone run proves they discharge AC3, AC6 and
  AC8. Gov writes nothing in inCMS. The rows are a bridge: `DEPL-aRepatriatedFork-20` deletes
  all five in its one landing. Observed by AC9.

## 3. Non-goals (OUT)

- Converging any of the four programs with gov's. Audit-A measured each as a parallel
  reimplementation, not a stale copy. The owner ruled on 2026-09-23 that inCMS converges, and
  `DEPL-aRepatriatedFork-20` owns that work, including migrating inCMS's build READMEs. This role
  is the BRIDGE that lets inCMS pull gov verbatim while that unit is in flight. Every other adopter
  that owns an engine can use it too.
- A contract for every engine file in every kit. S3 covers the memory-tree sources another shipped
  file calls. A kit gains a contract when an adopter first needs to own one of its files.
- nc. Its forks are carve-outs patched onto gov's bytes, not parallel programs, and TOOL units in
  this build take their fixes upstream instead.
- inCMS's `.githooks/pre-push` and `scripts/recall/README.md`, which also read `unattributed`. Their
  disposition belongs to `TOOL-aRepatriatedFork-8` and `TOOL-aRepatriatedFork-12`; either may use
  this role once it exists.
- The sibling-kit lookups at `corpus_ids.py:47` and `merge-rows.py:169-180`. They decide whether
  gov's OWN copies run at inCMS's layout, which `TOOL-aRepatriatedFork-2` repairs from its own brief;
  this unit leaves nothing for it to do.
- Withdrawing gov's `check-memory-hygiene.sh` from inCMS, where it is installed and unwired beside
  the adopter's own hygiene engine. F2 asks the question.

### Edges

- **consumes-from** `DEPL-aRepatriatedFork-1` — the `stands_down` table on `[[hole]]`. Without it S5
  has no key to extend and would invent a second stand-down mechanism.
- **consumes-from** `TOOL-aRepatriatedFork-3` — the `declares: yes|no` line from
  `gotchas.py --declares`. At rev-3 no shipped consumer reads that line yet, so section 4 declares
  no clause for it; the clause lands with its first consumer.
- **hands-off** `DEPL-aRepatriatedFork-14` — the `stale-header-waiver` hole itself, which that unit
  may retire. S5 declares a stand-down for it only while it exists.
- **hands-off** `DEPL-aRepatriatedFork-17` — the nearest-vintage pin suggestion, which names this
  role as the remedy when no vintage is near.
- **hands-off** `DEPL-aRepatriatedFork-20` — inCMS's convergence onto gov's programs, which deletes
  S6's five rows in one landing. Without this unit, inCMS's pulls stay blocked until the convergence
  lands.
- **hands-off** `DEPL-aRepatriatedFork-21` — `resolve_owned_rows`, which `apply` calls so it never
  lands gov's bytes on a file the target owns. This unit left `apply` out of scope.

## 4. Design

### Data model

```toml
# .governance/deploy.toml at the target
[[own]]
path = "scripts/gen_build_index.py"
implements = "memory-tree:gen_build_index.py"
why = "written 2026-08-07, before gov's; roster is session slugs and ids is an authored high-water"
```

```toml
# tools/memory-tree/kit.toml in gov
[[contract]]
source = "corpus_ids.py"
id = "memory-tree/corpus-ids"
[[contract.clause]]
probe = ["python3", "{own}", "--print-defined-ids"]
expect = "(?m)^# id-ere: "
consumer = "kickoff-manifest:manifest-check.sh"
[[contract.clause]]
imports = ["ask_shell"]
consumer = "gotchas.py"
```

A consumer is a path relative to the declaring kit's home, or `<entry>:<path>` relative to that
entry's home. It is never a repo-root literal, because the descriptor ships and
`check-install-prefix.sh` bans a new carried `tools/` literal in a shipped file.

### The contract list gov holds stable

Re-derived at build time, at 73113582. Each row names the clause and the consumer that reads it. A
clause without a consumer is not a contract and is not declared, and neither is a clause a read-only
verb cannot run.

| Source | Clause | Consumer |
|---|---|---|
| `gen_build_index.py` | `--check` prints a `build-index: ` line | `check-memory-hygiene.sh`, check 9 |
| `gen_build_index.py` | `--print-bindings` emits an `N` row | `check-memory-hygiene.sh`, check 21 |
| `gen_build_index.py` | imports `apply_region`, `Problem`, `MARK_OPEN`, `MARK_CLOSE` | `marker-contract.test.sh` |
| `corpus_ids.py` | `--print-defined-ids` prints the `# id-ere: ` header | `manifest-check.sh`, `CARD_ID_ERE_KEY` |
| `corpus_ids.py` | imports `ask_shell` | `gotchas.py`, loaded by path |
| `gotchas.py` | `--for-paths` prints a checklist | the kickoff Skill, `SKILL.md`, and the unattended Skill, `SKILL.template.md` |
| `check-memory-hygiene.sh` | `--print-index-set`, `--print-append-only-ere` | `corpus_ids.py` |
| `check-memory-hygiene.sh` | `--print-rotated-archive-ere` | `row_grammar.py` |

What the a7c78ad2 table held and this one does not, and why:

- `unfenced_lines`, `STATUS_TOKENS`, `TERMINAL` and `parse_conf` are imported from `tree_lib.py`
  since `TOOL-aRepatriatedFork-9`, so no consumer imports them from either engine any more.
- `gen_build_index.py --write` and the `merge-rows.py` driver WRITE into the tree, and a read-only
  `check` must not run either. `check-wiring.sh` already runs a no-op three-way through whatever
  driver the target installed, so the merge contract is observed by its own consumer. An owned
  `merge-rows.py` prints `contract (none)`.
- `--selftest`, `--check-format`, `corpus_ids.py --check` and `gotchas.py --check` have no stdout
  signature on a clean tree, and a non-zero exit from them reports the adopter's corpus rather than
  the contract.
- `gotchas.py --declares` has no shipped consumer. Only the kit README names it.
- `--for-diff` depends on the range it is handed; `--for-paths` over the owned file is the probe.

### Evidence, measured at a7c78ad2

- The inCMS receipt carries 12 `unattributed` rows in `govkit update`'s read-only run on
  2026-09-23. Four of them are the four programs above: `corpus_ids.py`, `gen_build_index.py`,
  `gotchas.py` and `merge-rows.py`. PINNED at that run.
- A nearest-vintage search, which diffs the target file against gov's blob at every revision of its
  source, finds each program far from every vintage. The nearest distances were 2364, 1255, 1147 and
  250 changed lines, against files of 1837, 774, 664 and 303 lines. A `--pin` to such a vintage
  records a base the bytes never descended from, which is the same lie `unattributed` avoids.
  PINNED at that run.
- dRetiredFork's census already recommended reclassifying `gen_build_index.py` as project-owned,
  "a second program … under the same filename"
  (`memory/builds/dRetiredFork/build/2026-09-03-build-DEPL-dRetiredFork-7-1-census-incms.md:149-185`),
  and it was never applied because govkit had no role for it.
- inCMS's own `.governance/kits.json` already keeps a `role_dispositions` list whose rows each say
  "receipt `engine`, declared `project-owned`" for `corpus_ids.py` and `merge-rows.py`: the adopter
  maintains by hand the disagreement this role removes.
- `scripts/row_grammar.py` at inCMS is a receipt `engine` row and dies on import there, because
  inCMS's `corpus_ids.py` lacks `parse_conf` (audit-A, side finding). Nothing wired calls it. S4's
  installed-consumer mark is what surfaces that state instead of hiding it.

### Inventory

- `resolve_owned_rows(root, target, deploy, descs)` — `py.function`, snake, verb `resolve`. It
  resolves each entry at THIS target, because whether a source ships under `engine` is a question
  about the rule that reaches it here.
- `measure_contract_parity(target, contract, own_path)` — `py.function`, snake, verb `measure`.
- `derive_parity_lines(target, receipt, descs, r)` — `py.function`, snake, verb `derive`. The one
  printer both verbs call.
- `adopter-owned` — a new `UNLANDED_REASON` and `UPDATE_ROLE` key. `contract` — a new disposition.
  `declared` — a new `EVIDENCE_STATES` member. `{own}` — a new token, resolved only inside a
  `[[contract]]` clause.
- `[[own]]` — a new `deploy.toml` table. `[[contract]]` — a new descriptor table.

### Adopter deletions this unit enables

inCMS keeps its bytes. What it deletes is the bookkeeping that works around govkit's two-word
vocabulary:

| Deleted | Where |
|---|---|
| the `divergence` row and the `KIT_GEN_BUILD_INDEX_DELTA` marker for `gen_build_index.py` | `.governance/kits.json:317-321` and the file's own header |
| the `role_dispositions` rows for `corpus_ids.py` and `merge-rows.py` | `.governance/kits.json:736-747` |
| the `owned_why` prose for the four programs | moved into each `[[own]]` row's `why` |

### Rollout

Additive and defaulted. A target with no `[[own]]` rows produces byte-identical `update` and `check`
output, which AC10 observes. The new role reaches a receipt only through `adopt`, which already
requires `--write` and an explicit `--re-adopt`.

### Files touched (estimate)

`tools/govkit/govkit.py` · `tools/govkit/selftest.py` · `tools/memory-tree/kit.toml` ·
`WIRE-INTO-PROJECT.md`. Govkit has no README; the runbook is where its operator docs live.

### Alternatives rejected

- Reusing `forked`. That role is a claim GOV's descriptor makes about a file gov derived from a
  target (`govkit.py:250-256`). Here the TARGET makes the claim, per target, about a file gov never
  derived from. One role for both would let gov's descriptor speak for one adopter's tree.
- Reusing `project-owned`. That role means gov supplies no bytes for the source, ever, at every
  target (`govkit.py:246`). Gov ships `gen_build_index.py` to nc and means to keep shipping it.
- Pinning each program to its nearest vintage. The evidence above measures that as a base the bytes
  never had.
- A contract enforced as a gate. The adopter owns the file, and redding their bar for a clause no
  wired consumer calls would recreate the fork pressure this unit removes. S4 marks an installed
  consumer and leaves the escalation to F3.

## 5. Production-readiness checklist

- security — a contract probe runs the ADOPTER's file under the operator's uid. The argv is gov's,
  from a gov descriptor, and the one target-supplied value, `{own}`, is graded by the strict path
  class and contained to the target. `SHELL_EXEC_SITES` (`govkit.py:3196-3239`) gains the site as
  `target`. It is not `target-code`: the census demands a `target-code` site be reached only from a
  writing verb, and this one is reached from `check`. The path comes off the receipt, which is
  hand-editable, so it is re-graded by the strict class and by containment on every run.
- perf / scale — one subprocess per probe clause per owned row. The contract table is that
  population, and no count of it is typed here.
- error / empty / loading states — an `[[own]]` row naming a missing file refuses. A contract with
  zero clauses is refused by `selfcheck`, because it would report `0/0 hold`.
- observability — one parity line per owned row on every `update` and `check`, failing clauses named.
- risks — a clause that is wrong about its consumer reports a false gap forever. Every clause cites
  its consumer by path, and `selfcheck` refuses a clause whose consumer is not a tracked gov file.
- testing — `govkit selftest` fixtures for each S item, plus a clause observed failing on a
  deliberately non-conforming fixture engine.
- migration — receipt schema is unchanged in shape. New values appear only after `adopt --re-adopt`.
- user docs — `WIRE-INTO-PROJECT.md` gains the declaration and the role.

## 6. Acceptance criteria

- **AC1** — When a fixture `deploy.toml` declares `[[own]]` with a `path` carrying a space or a
  `..` segment, `python tools/govkit/govkit.py adopt --target <fixture> --re-adopt` exits 1 naming
  the row.
  Red when: a hostile `path` reaches a probe argv.
- **AC2** — When a fixture `[[own]]` row's `implements` names a `seed` source, `adopt` refuses naming
  the role that already owns the bytes.
  Red when: the declaration silently overrides a seed.
- **AC3** — When `python tools/govkit/govkit.py update --target <fixture>` runs over a receipt whose
  only non-current row is `adopter-owned`, the summary line counts it under `adopter-owned` and the
  run re-stamps `gov_commit`.
  Red when: the row is counted `unattributed`, or the re-stamp is withheld.
- **AC4** — The AC3 fixture with the row recorded `unattributed` instead is observed withholding the
  re-stamp on a7c78ad2's `govkit.py`, recorded in the build journal as the red-first control.
  Red when: the control does not withhold, so AC3 proves nothing.
- **AC5** — When `python tools/govkit/govkit.py selfcheck` runs, it names every `[[contract]]` in
  the memory-tree descriptor, and a fixture clause citing an untracked consumer or a contract with
  zero clauses is refused.
  Red when: a contract row with no consumer is accepted.
- **AC6** — When `govkit check` runs on a fixture target whose owned file lacks one declared import,
  the parity line reads `<n-1>/<n>` and names the import and its consumer, and the exit code does not
  move for it.
  Red when: the missing clause is silent, or it reds an adopter whose consumer is not installed.
- **AC7** — When the same fixture also carries the importing consumer as a receipt `engine` row,
  the parity line for that clause carries `INSTALLED CONSUMER CANNOT RUN` naming both files, and
  the exit code still does not move.
  Red when: an installed program that cannot import is reported like an unwired one, or reds a bar
  whose owner never wired it.
- **AC8** — When `govkit check` runs on a fixture owning `corpus_ids.py`, `measured-pins` prints as
  stood down, and the same fixture without the `[[own]]` row reports it as before.
  Red when: the hole still runs a gov probe against the adopter's program.
- **AC9** — In a scratch clone of the inCMS worktree carrying the five journal rows,
  `python tools/govkit/govkit.py update --target <clone>` reports 8 `unattributed` rows, not 12,
  prints five contract parity lines, and `govkit check` prints `measured-pins` as stood down and
  marks `row_grammar.py` as an installed consumer that cannot import `parse_conf`.
  Red when: any of the four programs is still `unattributed`.
  fixture: a `--shared` clone of the inCMS worktree; the tree holds none today.
  figure: 12 and 8 are PINNED from the 2026-09-23 read-only run and re-derived at build time.
  The `row_grammar.py` mark is re-derived too: since `TOOL-aRepatriatedFork-9` gov's `row_grammar.py`
  imports `parse_conf` from `tree_lib.py`, so the marks that print are whichever installed consumers
  fail the contract as section 4 re-derives it.
  cost: one `adopt --re-adopt --write` inside the clone, several minutes.
- **AC10** — When `govkit update` and `govkit check` run on a fixture with no `[[own]]` rows, their
  output is byte-identical to a7c78ad2's.
  Red when: the additive table changes behaviour for a target that never used it.

## 7. Gates

`govkit selfcheck` · `govkit selftest` · `govkit refusal join` · `govkit acceptance matrix` · `govkit runbook parity` · `recall floor arms` · `memory hygiene` · `spec tokens (a spec's own names resolve)`

New arm: `tools/govkit/selftest.py` · an `[[own]]` fixture per S item, a non-conforming fixture engine for S4, and the AC4 `unattributed` control · none

## 8. Open questions

- **F1 — where does `[[own]]` live, `deploy.toml` or the receipt?** The deploy descriptor is the
  owner's standing decisions and the receipt is what happened. Recommendation: `deploy.toml`, with
  `adopt` copying the declaration into the row, the same split `[[decline]]` uses.
  RESOLVED (owner, 2026-09-23): `deploy.toml`, with `adopt` copying the declaration into the row, as
  recommended.
- **F2 — when an owned file stands in for a gov source at a DIFFERENT path, does gov keep landing
  its own copy?** inCMS's `check-docs-hygiene.sh` stands in for `check-memory-hygiene.sh`, which gov
  keeps installing unwired beside it. Recommendation: keep landing it and print one line saying the
  stood-in copy is unwired. Withdrawing it is a separate, reversible decision the operator makes with
  `--write-withdrawals`.
  RESOLVED (owner, 2026-09-23): keep landing it and print one unwired line, as recommended.
- **F3 — when does `INSTALLED CONSUMER CANNOT RUN` become `r.fail`?** Measured at inCMS on
  2026-09-23, five gov engine rows would carry the mark against its own programs:
  `check-memory-hygiene.sh`, `row_grammar.py`, `marker-contract.test.sh`, `manifest-check.sh` and
  `check-arms.py`. None is on an inCMS leg. Recommendation: escalate only when the consumer's argv
  is on a leg the receipt records as emitted, which inCMS's receipt does not record today, so the
  escalation is inert there until it does.
  RESOLVED (owner, 2026-09-23): escalate only when the consumer's argv is on a leg the receipt
  records as emitted, as recommended.

## 9. Revision log

- rev-1 · 2026-09-23 · initial draft, grounded at a7c78ad2 with audit-A's measurements, the
  2026-09-23 read-only `update` of the inCMS worktree and a nearest-vintage search over its four programs.
- rev-2 · 2026-09-23 · §8 resolved by the owner. The owner also ruled that inCMS converges, which
  §3 had called inCMS's decision. This unit becomes the bridge, and `DEPL-aRepatriatedFork-20`
  owns the convergence.
- rev-3 · 2026-09-24 · build-time divergences, each measured at 73113582. S2: `ROLE_KINDS` does not
  gain the role, so a descriptor spelling it stays a refusal, and `update` keeps the receipt's role
  for such a row. S1: a source any non-`engine` rule reaches is refused too, and so are an
  unselected entry and an untracked `path`. Section 4 Inventory: `resolve_owned_rows` takes the root
  and the target, and `derive_parity_lines` is added. Section 4's contract table is re-derived,
  because `TOOL-aRepatriatedFork-9` moved four imported names to `tree_lib.py`, and it drops every
  clause a read-only verb cannot run or has no consumer for. S3 and section 4's data model cite a
  consumer relative to a kit home. S4 states F2's line and F3's escalation.
  Section 5: the census label is `target`, and govkit has no README. Section 3's edge to
  `TOOL-aRepatriatedFork-3` records that no clause reads its line yet. AC9's `row_grammar.py` mark
  is re-derived.
- rev-4 · 2026-09-24 · §3 gains the **hands-off** edge to `DEPL-aRepatriatedFork-21`, which closes the
  gap in `apply` this unit's builder reported.

## 10. Reuse audit

`python tools/codebase-map/reuse_lookup.py "a target declares it owns an engine and the deployer reports contract parity instead of grading bytes"`
ranked `report`, `owners_of` and govkit's `Report` class, none of which models a role. No existing
seam fits as a mapped symbol. The live seams are in `govkit.py` and are extended, not copied: the
`UPDATE_ROLE` dispatch, the `ROLE_KINDS` table that `selfcheck` arm 7g grades for coverage, and the
`[[decline]]` contract's split between a `deploy.toml` declaration and a graded receipt effect.

Recall terms used: `adopter-owned forked project-owned unattributed pinned evidence receipt role
UPDATE_ROLE contract parity gen_build_index corpus_ids gotchas merge-rows`.
