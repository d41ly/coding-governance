# TOOL-dTrueNorth-8 — the as-built view re-rendered in the commit that changes its inputs, with an owner and a moment

**Status:** CLOSED · rev-3 · 2026-10-22 · node d · Tier-2 · base 271aa59d · streams tooling · order 4

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-21-build-TOOL-dTrueNorth-8-deviation-7.md](../build/2026-10-21-build-TOOL-dTrueNorth-8-deviation-7.md) | deviation | — |
| [2026-10-21-build-TOOL-dTrueNorth-8-ledger.md](../build/2026-10-21-build-TOOL-dTrueNorth-8-ledger.md) | journal | — |
| [2026-10-22-build-TOOL-dTrueNorth-1-runlog-2766a930.md](../build/2026-10-22-build-TOOL-dTrueNorth-1-runlog-2766a930.md) | journal | TOOL-dTrueNorth-1 TOOL-dTrueNorth-2 TOOL-dTrueNorth-3 TOOL-dTrueNorth-4 TOOL-dTrueNorth-5 TOOL-dTrueNorth-6 TOOL-dTrueNorth-7 TOOL-dTrueNorth-9 TOOL-dTrueNorth-10 TOOL-dTrueNorth-11 TOOL-dTrueNorth-12 TOOL-dTrueNorth-13 TOOL-dTrueNorth-14 TOOL-dTrueNorth-15 TOOL-dTrueNorth-16 TOOL-dTrueNorth-17 TOOL-dTrueNorth-18 TOOL-dTrueNorth-19 TOOL-dTrueNorth-20 TOOL-dTrueNorth-23 TOOL-dTrueNorth-24 TOOL-dTrueNorth-25 TOOL-dTrueNorth-26 TOOL-dTrueNorth-27 TOOL-dTrueNorth-29 TOOL-dTrueNorth-30 TOOL-dTrueNorth-31 TOOL-dTrueNorth-32 TOOL-dTrueNorth-33 |
| [2026-10-22-build-TOOL-dTrueNorth-8-deviation-37.md](../build/2026-10-22-build-TOOL-dTrueNorth-8-deviation-37.md) | deviation | — |
| [2026-10-21-prompt-TOOL-dTrueNorth-8-build-brief.md](../prompts/2026-10-21-prompt-TOOL-dTrueNorth-8-build-brief.md) | journal | — |
| [2026-10-21-review-TOOL-dTrueNorth-8-spec-audit.md](../reviews/2026-10-21-review-TOOL-dTrueNorth-8-spec-audit.md) | spec-audit | TOOL-dTrueNorth-9 TOOL-dTrueNorth-10 TOOL-dTrueNorth-11 TOOL-dTrueNorth-12 TOOL-dTrueNorth-13 TOOL-dTrueNorth-14 TOOL-dTrueNorth-15 TOOL-dTrueNorth-16 |
| [2026-10-22-review-TOOL-dTrueNorth-1-closing-diff-review-round1.md](../reviews/2026-10-22-review-TOOL-dTrueNorth-1-closing-diff-review-round1.md) | diff-review | TOOL-dTrueNorth-1 TOOL-dTrueNorth-2 TOOL-dTrueNorth-3 TOOL-dTrueNorth-4 TOOL-dTrueNorth-5 TOOL-dTrueNorth-6 TOOL-dTrueNorth-7 TOOL-dTrueNorth-9 TOOL-dTrueNorth-10 TOOL-dTrueNorth-11 TOOL-dTrueNorth-12 TOOL-dTrueNorth-13 TOOL-dTrueNorth-14 TOOL-dTrueNorth-15 TOOL-dTrueNorth-16 TOOL-dTrueNorth-17 TOOL-dTrueNorth-18 TOOL-dTrueNorth-19 TOOL-dTrueNorth-20 |

<!-- /gen:spec-records -->

## 1. Goal

The round-1 spec audit of this build (`memory/builds/dTrueNorth/reviews/2026-10-21-review-TOOL-dTrueNorth-1-spec-audit.md`)
confirmed finding **id 1 at HIGH**, its item **H1**: nobody owns re-rendering the as-built view, and
re-rendering it is forbidden. Deviation-1 and deviation-4 amend `cl-dClosedLoop-0004` and deviation-3
amends `cl-dClosedLoop-0002`. The instrument that renders the view writes `deviation <id>` on an
amended row and the record count in the head, so the view's bytes move the moment those records land.
`TOOL-dTrueNorth-6` §3 and its Migration say the file is never rewritten, and no unit names the
re-render, so either its AC11 or `TOOL-dTrueNorth-1` AC6 fails at the close. This unit names the
owner and the moment: the commit that changes a view input re-renders the view, through the
generator `TOOL-dTrueNorth-6` builds, and this unit's pass takes that act once over the records that
stand. It repairs `TOOL-dTrueNorth-6`. The same defect at MEDIUM, id 32 (item M15), and the AC6 half,
id 33 (item L8), are batched into `TOOL-dTrueNorth-16`.

## 2. Scope (IN)

- **S1** — The rule, in the two homes `TOOL-dTrueNorth-6` S8 gives the generator: the docstring of
  `asbuilt_view.py` and its row in `tools/memory-tree/README.md`. The view's inputs are every record
  the instrument's glob `*/build/*-deviation-*.md` matches and `DESIGN_RECORD` at `DESIGN_BASELINE`.
  A commit that adds or edits a record re-renders `DESIGN_VIEW` in the same commit, through
  `gen_build_index.py --write`, which `TOOL-dTrueNorth-6` makes the view's writer. No byte of the view
  is edited by hand. This supersedes `TOOL-dTrueNorth-6` §3's non-goal "any edit of the view file's
  bytes" and its §4 Migration sentence "the file is not rewritten". Observed by AC4.
- **S2** — The re-render at this unit's pass: `gen_build_index.py --write` runs once over the tree
  at the pass's base, and the pass stages the rendered `DESIGN_VIEW`. The records `TOOL-dTrueNorth-4`'s
  pass wrote at order 3, possibly before `TOOL-dTrueNorth-6` landed, are applied here. Observed by AC1
  and AC2.
- **S3** — The commit-time refusal that keeps S1 true, proved by a new arm. After
  `TOOL-dTrueNorth-6`, the generator's `--check` compares the view with its render. `check_index_input`
  returns true for any path under a build's `build/` folder, so a staged record makes
  `--check --staged` render rather than skip, and hygiene check 9, which the pre-commit hook runs
  under `--staged`, refuses a commit that lands a record with a stale view. The arm in the
  generator's self-test stages a new `amends` record over a fixture view and asserts the drift, then
  the fixed point after `--write`. Observed by AC3.

## 3. Non-goals (OUT)

- Writing deviation-2 and deviation-3: `TOOL-dTrueNorth-10`. Its own commit re-renders the view by
  S1, so whichever of the two passes lands second renders over every record that stands, and the
  two orders converge on one view.
- Declaring the view a generated output for the dispatch write-set checks (id 32, item M15), and
  amending `TOOL-dTrueNorth-1` AC6's expected `since` cells (id 33, item L8): `TOOL-dTrueNorth-16`.
- A spec-set coherence check over Files touched, the finding's suggested left-shift. S3's
  refusal acts at the commit that lands a record, which is the moment the defect would enter the
  tree, so a second check over spec prose would grade the same class later and weaker.
- Any edit of the bootstrap instrument `asbuilt.py`, of v2 or of the packet.
- This unit's own departure record, the member its `rescope · item add` row makes: the close writes
  a record for each member recorded by nobody (README build-level rule 4).

### Edges

- **consumes-from** `TOOL-dTrueNorth-6` — the generator `asbuilt_view.py`, its host `cmd_write` that writes `DESIGN_VIEW`, and `cmd_check`'s drift compare; without them there is no writer to own the re-render and no refusal to hold it
- **hands-off** `TOOL-dTrueNorth-17` — S1's rule extended to the render's code and the order-3 transition, and S3's arm extended to a staged kit edit (the round-2 spec audit's id 1)
- **hands-off** `TOOL-dTrueNorth-20` — S1's trigger reworded from the view's whole input predicate, S3's arm given a record taken out, and the chain packets' re-render filed as an ask (the round-2 spec audit's ids 46 and 27)

## 4. Design

### Evidence

- The instrument renders an amended row as `deviation `<rid>`` and the record count in the head
  (`memory/builds/dClosedLoop/build/2026-10-19-build-PLAY-dClosedLoop-1-asbuilt.py:70`, `:77`), over
  every record its glob finds, sorted by path (`:140`). When two records amend one clause the later
  path supplies the row (the `changes` map is overwritten per record, `:64`), so `cl-dClosedLoop-0004`'s row cites
  deviation-4.
- The committed view's head reads `0 deviation records`
  (`memory/builds/dClosedLoop/build/2026-10-19-build-PLAY-dClosedLoop-1-as-built.md:5`), and
  `git ls-files 'memory/builds/*/build/*-deviation-*'` prints nothing at base.
- `check_index_input` (`tools/memory-tree/gen_build_index.py:831-857`) returns true for a path of
  three or more segments under `<MEMORY_ROOT>/builds/` whose second segment is a record folder, which
  includes `build/`.
- Check 9 runs `gen_build_index.py --check --staged` under `--staged`
  (`tools/memory-tree/check-memory-hygiene.sh:1251-1253`), and the pre-commit hook runs the hygiene
  engine with `--staged` (`.githooks/pre-commit:181-182`).
- `TOOL-dTrueNorth-6` §4 "The host" has `cmd_write` call the generator after every artifact `plan()`
  returns and write the view, and `cmd_check` list the view's drift under `build-index DRIFT`.

### The pass

1. Read the records that stand at the pass's base; nothing is written before the render.
2. `python3 tools/memory-tree/gen_build_index.py --write`, then stage `DESIGN_VIEW` and whatever
   shared renders the same run moved (README rule 7).
3. The new arm (S3) and the two docs sentences (S1), in the same commit, with the unit id in the
   subject.

### Files touched (estimate)

- `tools/memory-tree/gen_build_index.py` (the self-test arm only)
- `tools/memory-tree/asbuilt_view.py` (its docstring only)
- `tools/memory-tree/README.md`
- `memory/builds/dClosedLoop/build/2026-10-19-build-PLAY-dClosedLoop-1-as-built.md` (re-rendered by `--write`, never edited)

### Alternatives rejected

- **Unit 4's pass re-renders the view.** At order 3 the generator may not exist yet, since unit 6
  shares that order, and the instrument's `--write` would then be the writer the product is meant
  to succeed.
- **Leaving the view stale until the close.** Unit 6 AC11 and the close's `deviations.py` steps read
  the view, and a red at the close names a defect no pass owns.

## 5. Production-readiness checklist

- security — no new write path: the view is already the generator's declared output under
  `TOOL-dTrueNorth-6`.
- perf / scale — one `--write` at the pass; the arm adds one fixture render to the generator's
  self-test.
- error / empty / loading states — with no record the render cites `baseline` on every row and the
  head reads `0 deviation records`, as the instrument writes it.
- observability — the generator's `build-index DRIFT` list names the view when it is stale.
- risks — a commit made with `--no-verify` skips check 9 and can land a stale view; the full
  hygiene run and the close still read it.
- testing — AC1 to AC4 as probes; the arm under §7.
- migration — none.
- user docs — the generator's docstring and the kit README row; no page under `help/` covers the
  view.

## 6. Acceptance criteria

- **AC1** — When `python3 "tools/memory-tree/asbuilt_view.py" --check` and
  `python3 memory/builds/dClosedLoop/build/2026-10-19-build-PLAY-dClosedLoop-1-asbuilt.py --check`
  run on the tree after the pass, both exit 0 against the one view file.
  Red when: the pass does not stage the re-rendered view, so its head still counts no record and
  both checks name the first differing line.
- **AC2** — When `grep -o '[0-9]* deviation records' memory/builds/dClosedLoop/build/2026-10-19-build-PLAY-dClosedLoop-1-as-built.md`
  runs after the pass, it prints the count `git ls-files 'memory/builds/*/build/*-deviation-*.md' | wc -l`
  prints, and `grep -c 'cl-dClosedLoop-0004.*| deviation ' memory/builds/dClosedLoop/build/2026-10-19-build-PLAY-dClosedLoop-1-as-built.md`
  prints 1.
  Red when: the head or the amended row was rendered over fewer records than the tree holds.
  figure: both counts are DERIVED at observation.
- **AC3** — When a probe in a scratch clone under `%TEMP%` adds one `amends` record under a chain
  build's `build/` folder, stages it and runs `python3 tools/memory-tree/gen_build_index.py --check --staged`,
  it exits 1 with the view's path under `build-index DRIFT` and no `SKIPPED` line; after
  `python3 tools/memory-tree/gen_build_index.py --write` and staging the view, the same command exits 0.
  Red when: a staged record skips the render, or `--write` leaves the view unchanged.
  fixture: a scratch clone under a short `%TEMP%` path; the tree holds none today.
- **AC4** — When `git grep -n -e "re-render" -- tools/memory-tree/README.md "tools/memory-tree/asbuilt_view.py"`
  runs, it prints the rule of S1 in both homes, naming the record glob and `--write`.
  Red when: either home still says the view is never rewritten.

## 7. Gates

`build-index selftest` · `memory hygiene` · `kit/dogfood doc parity` · `recall floor` · `recall floor arms` · `spec tokens (a spec's own names resolve)`

New arm: tools/memory-tree/gen_build_index.py (its selftest) · covers AC3 · a fixture view rendered over zero records and a staged amends record, red while the view is stale and green after --write · none

## 8. Open questions

- **F1 — Which binding line does a unit the spec audit promoted carry?** The carries join of
  `TOOL-dTrueNorth-2` reds a chain spec that carries nothing and derives from nothing (`unbound`),
  and from that unit's landing every `--dispatch` runs it. (a) `**Derived:**` naming
  `PLAY-dClosedLoop-2`, the owner's ruling that a run carries the units it adds (ER:320).
  (b) No binding line. (c) A `part k/n` carry of the repaired unit's clause. (b) reds `unbound` and
  (c) reds `parts` against the repaired unit's whole carrier, so veto 1 discards both.
  Recommendation (a). Rung 3. RESOLVED (agent, 2026-10-21, delegated): (a).
  widens: none · relaxes: none
- **F2 — Does the build's grant lift veto 2 for the kit edits here?** Every path under `tools/` is
  a governance carrier by `PLAY-dClosedLoop-10`'s list. `cl-dClosedLoop-0006` names the view as
  "generated and never hand-edited", and S1 and S3 are that clause's own generation and refusal.
  RESOLVED (agent, 2026-10-21, delegated): lifted by `PLAY-dClosedLoop-3`, rung 3. grants:
  PLAY-dClosedLoop-3 the memory-tree kit's as-built generator docs and build-index self-test arm for
  the view cl-dClosedLoop-0006 names · widens: none · relaxes: none

## 9. Revision log

- rev-1 · 2026-10-21 · initial draft, promoted from the round-1 spec audit's id 1 (HIGH, item H1).
- rev-2 · 2026-10-21 · §3 · the Edges block gains a hands-off to TOOL-dTrueNorth-17 and TOOL-dTrueNorth-20,
  promoted by the round-2 spec audit, the mirror of their consumes-from; no other section moves.
- rev-3 · 2026-10-21 · §6 · the acceptance criteria name the modules this build creates (`deviation_join.py`, `asbuilt_view.py`, `design_lib.py`) quoted or bare, and a `git show`/`json.load` argument quoted, so the spec-tokens paths join, which reads the live tree at every `--dispatch`, stops refusing every unit before those modules exist. No criterion's observation moves.

## 10. Reuse audit

Probe: `python tools/codebase-map/reuse_lookup.py "re-render a generated view in the commit that
changes its inputs"` ranked `render`, `render_family_view` (`tools/memory-tree/backlog.py`) and
`resolve_generated_indexes` (`tools/unattended/lib-unattended.sh`). The seam this unit extends is
`TOOL-dTrueNorth-6`'s host pair in `tools/memory-tree/gen_build_index.py`, `cmd_write` and `cmd_check`,
with the staged classifier `check_index_input` that already routes a `build/` record to a render;
`render_family_view` is the precedent of a generator re-rendering a view from records in the commit
that moves them. No hit named an owner for the as-built view, and none disagreed with source.

Recall terms used: `python tools/memory-recall/query.py "how is a spec audit finding promoted to a
repair unit and its generated view kept fresh" --terms "spec-audit promoted unit repairs order
as-built view deviation record re-render guard selftest pin"`
