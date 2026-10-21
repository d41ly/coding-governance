# TOOL-dTrueNorth-17 — the order-3 transition of the as-built view: the render's code is a view input, and the second of units 4 and 6 to land re-renders

**Status:** OPEN · rev-1 · 2026-10-21 · node d · Tier-2 · base 271aa59d · streams tooling · order 5

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

*No record names this unit.*

<!-- /gen:spec-records -->

## 1. Goal

The round-2 spec audit (`memory/builds/dTrueNorth/reviews/2026-10-21-review-TOOL-dTrueNorth-8-spec-audit.md`)
confirmed finding **id 1 at HIGH**, its item **H1**: the order-3 transition re-renders the view with no
owner. `TOOL-dTrueNorth-4`'s pass writes deviation-1 and deviation-4 at order 3, and
`TOOL-dTrueNorth-6`, at the same order, lands the generator's compare of `DESIGN_VIEW` with its render.
Whichever lands second makes check 9 compare a view whose head counts no record with a render that
counts two, so that commit is refused or re-renders undeclared. `TOOL-dTrueNorth-8` owns the re-render
only at its own order-4 pass. This unit names the owner and the moment: the render's code is a view
input, so the commit that lands it re-renders, and the second of the two order-3 passes is that commit.
It repairs `TOOL-dTrueNorth-8`.

## 2. Scope (IN)

- **S1** — The rule, extended in the two homes `TOOL-dTrueNorth-8` S1 writes, the docstring of
  `tools/memory-tree/asbuilt_view.py` and its row in `tools/memory-tree/README.md`. The view's inputs
  are the records the glob `*/build/*-deviation-*.md` matches, `DESIGN_RECORD` at `DESIGN_BASELINE`,
  and the code that renders and compares it: `asbuilt_view.py`, `design_lib.py` and the host calls in
  `gen_build_index.py`. A commit that changes the render's code re-renders `DESIGN_VIEW` in that
  commit through `gen_build_index.py --write`, as a commit changing a record does. Observed by AC4.
- **S2** — The owner of the order-3 transition: of `TOOL-dTrueNorth-4` and `TOOL-dTrueNorth-6`,
  whichever pass lands second runs `gen_build_index.py --write`, stages `DESIGN_VIEW` in its own
  commit, and is dispatched with `DESIGN_VIEW` among its `--dispatch --writes` paths. By
  `TOOL-dTrueNorth-6`'s consumes-from edge that is usually unit 6. The rule reaches both passes through
  the hands-off bullet each one's §3 carries to this unit, and it supersedes `TOOL-dTrueNorth-6` §4
  Migration's "the file is not rewritten" for that pass. Observed by AC1 and AC2.
- **S3** — The arm that proves S1's refusal on a code-only commit. In the generator's self-test, a
  fixture holds one committed `amends` record and a view rendered over zero records; staging an edit
  of a kit path alone, `gen_build_index.py --check --staged` exits 1 with the view under
  `build-index DRIFT`, and after `--write` the same command exits 0. `TOOL-dTrueNorth-8` S3's arm
  stages a record; this one stages the renderer. Observed by AC3.

## 3. Non-goals (OUT)

- Writing any deviation record. Deviation-1 and deviation-4 stay `TOOL-dTrueNorth-4` S10's, written
  in the departing unit's own commit as `cl-dClosedLoop-0004` requires.
- Moving `TOOL-dTrueNorth-4`'s records to a later order, the finding's option (b). That option takes
  the records out of the departing unit's commit, which the clause names.
- The wording of S1's trigger for deleted and moved records and the `DESIGN_*` keys: the round-2
  audit's id 46, batched into `TOOL-dTrueNorth-20`.
- A spec-audit checklist entry per generated output, the finding's left-shift. S3's arm and check 9
  refuse the class at the commit that would land it.
- This unit's own departure record: the close writes one for each member recorded by nobody
  (README build-level rule 4).

### Edges

- **consumes-from** `TOOL-dTrueNorth-4` — deviation-1 and deviation-4 in the tree, the records whose arrival S2's transition re-renders over
- **consumes-from** `TOOL-dTrueNorth-6` — `asbuilt_view.py`, `cmd_write` and `cmd_check`'s view compare; without them there is no writer for S2's act and no refusal for S3's arm
- **consumes-from** `TOOL-dTrueNorth-8` — S1's rule in its two homes and S3's staged-record arm, which this unit extends
- **hands-off** `TOOL-dTrueNorth-20` — S1's trigger reworded from the view's whole input predicate, and S3's arm given a deleted-record case (the round-2 audit's id 46)

## 4. Design

### Evidence

- `check_index_input` (`tools/memory-tree/gen_build_index.py:831-857`) returns true for any path
  under the kit directory as well as for a build's `build/` folder, so staging only a kit file makes
  `--check --staged` render every output, the view included once `TOOL-dTrueNorth-6` lands.
- Check 9 runs `gen_build_index.py --check --staged` under `--staged`
  (`tools/memory-tree/check-memory-hygiene.sh:1251-1253`), from the pre-commit hook
  (`.githooks/pre-commit:181-182`).
- `--check-commit` refuses an open pass's undeclared staged path (`tools/unattended/unattended.sh:31`),
  and `GENERATED_INDEXES` is blank today (`.unattended.conf:406`); `TOOL-dTrueNorth-16` S18 declares
  the view there only at order 5, so at order 3 the view must be on the dispatch's `--writes`.
- `TOOL-dTrueNorth-6` AC11 already demands that `asbuilt_view.py --check` and the instrument's
  `--check` both exit 0 against the one view after that pass, which holds only with the view
  re-rendered over the records that stand.

### The history probe

AC1 reads the transition after the fact, at this unit's pass: for each commit in
`271aa59d..HEAD` whose tree holds `tools/memory-tree/asbuilt_view.py` and that touches a record or a
kit path, the count in the view's head equals the records that commit's tree holds. Before the
generator exists the instrument's view is not compared, so those commits are not read.

### Files touched (estimate)

- `tools/memory-tree/asbuilt_view.py` (its docstring only)
- `tools/memory-tree/README.md`
- `tools/memory-tree/gen_build_index.py` (the self-test arm only)

### Alternatives rejected

- **Unit 8's pass alone owns the re-render.** It runs at order 4, after the order-3 commit that is
  refused.
- **Holding the view's compare off until unit 8.** It would ship `TOOL-dTrueNorth-6`'s gate dark
  behind a switch no clause names, and the refusal is what keeps the view honest.

## 5. Production-readiness checklist

- security — no new write path: the view is already the generator's declared output.
- perf / scale — S3 adds one fixture render to the generator's self-test; AC1 walks the run's range
  once.
- error / empty / loading states — with no record the render reads `0 deviation records`, and the
  transition renders the same bytes as before it.
- observability — the generator's `build-index DRIFT` list names the view when a code commit leaves
  it stale.
- risks — a pass that lands second without reading its hands-off bullet is refused at check 9, the
  loud direction; AC1 finds any stale commit that reached the range.
- testing — AC1 to AC4 as probes; the arm under §7, observed at the close.
- migration — none.
- user docs — the docstring and the kit README row; no page under `help/` covers the view.

## 6. Acceptance criteria

- **AC1** — When a probe walks `git rev-list 271aa59d..HEAD` and, for each commit whose tree holds
  `tools/memory-tree/asbuilt_view.py` and whose diff touches `memory/builds/*/build/*-deviation-*.md`
  or `tools/memory-tree/`, compares `git show <c>:memory/builds/dClosedLoop/build/2026-10-19-build-PLAY-dClosedLoop-1-as-built.md`'s
  `<n> deviation records` with the count `git ls-tree -r --name-only <c> -- memory/builds` gives for
  `/build/*-deviation-*.md`, every pair is equal.
  Red when: the order-3 pass that landed second committed the view still counting no record.
  figure: both counts are DERIVED per commit.
- **AC2** — When `grep -E 'dispatch · item [^ ]+ TOOL-dTrueNorth-(4|6) ' memory/builds/dTrueNorth/RUN.md`
  runs, the row of whichever of the two landed second names the view's path among its writes.
  Red when: the pass that re-rendered the view staged a path its dispatch never declared.
- **AC3** — When a probe in a scratch clone under `%TEMP%` commits one `amends` record without
  re-rendering the view, then stages only an edit of `tools/memory-tree/asbuilt_view.py`'s docstring
  and runs `python3 tools/memory-tree/gen_build_index.py --check --staged`, it exits 1 with the view's
  path under `build-index DRIFT`; after `python3 tools/memory-tree/gen_build_index.py --write` and
  staging the view, the same command exits 0.
  Red when: a staged kit edit alone skips the view's render.
  fixture: a scratch clone under a short `%TEMP%` path, with no hook installed; the tree holds none.
- **AC4** — When `git grep -n -e "render" -- tools/memory-tree/asbuilt_view.py tools/memory-tree/README.md`
  runs, both homes name the render's code among the view's inputs and the second order-3 pass as the
  owner of the transition.
  Red when: either home still names only the records and the design as inputs.

## 7. Gates

`build-index selftest` · `memory hygiene` · `kit/dogfood doc parity` · `recall floor` · `recall floor arms` · `spec tokens (a spec's own names resolve)`

New arm: tools/memory-tree/gen_build_index.py (its selftest) · covers AC3 · a committed amends record over a view rendered with none, and a staged kit-path edit alone, red while the view is stale and green after --write · none

## 8. Open questions

- **F1 — Which binding line does a unit the spec audit promoted carry?** The carries join of
  `TOOL-dTrueNorth-2` reds a chain spec carrying nothing and derived from nothing. (a) `**Derived:**`
  naming `PLAY-dClosedLoop-2`, the owner's ruling that a run carries the units it adds (ER:320).
  (b) None. (c) A `part k/n` carry of the repaired unit's clause. (b) reds `unbound` and (c) reds
  `parts`; veto 1 discards both. Recommendation (a). Rung 3. RESOLVED (agent, 2026-10-21,
  delegated): (a). widens: none · relaxes: none
- **F2 — Who owns the order-3 transition?** (a) The second of units 4 and 6 to land, told through the
  hands-off bullets of their own §3. (b) Unit 4's records moved to a later pass. (c) Unit 8's pass,
  as written. (b) fails `cl-dClosedLoop-0004`'s "written in the departing unit's own commit" and (c)
  leaves the order-3 commit refused, so veto 1 discards both. Recommendation (a). Rung 3. RESOLVED
  (agent, 2026-10-21, delegated): (a). widens: none · relaxes: none
- **F3 — Does the build's grant lift veto 2 for the kit edits here?** `cl-dClosedLoop-0006` names the
  view as generated and never hand-edited, and S1 to S3 are its generation and refusal. RESOLVED
  (agent, 2026-10-21, delegated): lifted by `PLAY-dClosedLoop-3`, rung 3. grants: PLAY-dClosedLoop-3
  the memory-tree kit's as-built generator docs and build-index self-test arm for the view
  cl-dClosedLoop-0006 names · widens: none · relaxes: none

## 9. Revision log

- rev-1 · 2026-10-21 · initial draft, promoted from the round-2 spec audit's id 1 (HIGH, item H1).

## 10. Reuse audit

Probe: `python tools/codebase-map/reuse_lookup.py "re-render a generated output in the commit that
lands its renderer"` ranked `render`, `build_commit` (`tools/unattended/lib-unattended.sh`) and
`render_family_view` (`tools/memory-tree/backlog.py`) by name stem; none names an owner for a
transition between two passes. The seam extended is `TOOL-dTrueNorth-8`'s rule and arm over
`check_index_input` (`tools/memory-tree/gen_build_index.py:831-857`), which already classes a kit
path as an index input, so no existing seam needed a second classifier. No hit disagreed with source.

Recall terms used: `python tools/memory-recall/query.py "how does a spec audit's promoted repair unit
close a defect a pass before it would hit" --terms "spec-audit promoted unit repairs order transition
re-render as-built view argv pathspec supersedes amends"`
