# TOOL-dFoldedAudit-6 — an audit's own fold owes no hand `spec-revised` deviation record

**Status:** OPEN · rev-3 · 2026-11-01 · node d · Tier-2 · base 74274869 · streams tooling · order 60

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-11-01-build-TOOL-dFoldedAudit-1-3-design.md](../build/2026-11-01-build-TOOL-dFoldedAudit-1-3-design.md) | research | TOOL-dFoldedAudit-1 TOOL-dFoldedAudit-2 TOOL-dFoldedAudit-3 TOOL-dFoldedAudit-4 TOOL-dFoldedAudit-5 TOOL-dFoldedAudit-7 TOOL-dFoldedAudit-8 |
| [2026-11-01-build-TOOL-dFoldedAudit-1-4-spec-stage-returns.md](../build/2026-11-01-build-TOOL-dFoldedAudit-1-4-spec-stage-returns.md) | journal | TOOL-dFoldedAudit-1 TOOL-dFoldedAudit-2 TOOL-dFoldedAudit-3 TOOL-dFoldedAudit-4 TOOL-dFoldedAudit-5 TOOL-dFoldedAudit-7 TOOL-dFoldedAudit-8 |
| [2026-11-01-build-TOOL-dFoldedAudit-5-1-cross-read-return.md](../build/2026-11-01-build-TOOL-dFoldedAudit-5-1-cross-read-return.md) | journal | TOOL-dFoldedAudit-1 TOOL-dFoldedAudit-2 TOOL-dFoldedAudit-3 TOOL-dFoldedAudit-4 TOOL-dFoldedAudit-5 TOOL-dFoldedAudit-7 TOOL-dFoldedAudit-8 |
| [2026-11-01-build-TOOL-dFoldedAudit-7-1-token-fold-return.md](../build/2026-11-01-build-TOOL-dFoldedAudit-7-1-token-fold-return.md) | journal | TOOL-dFoldedAudit-1 TOOL-dFoldedAudit-4 TOOL-dFoldedAudit-7 |
| [2026-11-01-prompt-TOOL-dFoldedAudit-1-brief.md](../prompts/2026-11-01-prompt-TOOL-dFoldedAudit-1-brief.md) | research | TOOL-dFoldedAudit-1 TOOL-dFoldedAudit-2 TOOL-dFoldedAudit-3 TOOL-dFoldedAudit-4 TOOL-dFoldedAudit-5 TOOL-dFoldedAudit-7 TOOL-dFoldedAudit-8 |
| [2026-11-01-prompt-TOOL-dFoldedAudit-1-fix-brief.md](../prompts/2026-11-01-prompt-TOOL-dFoldedAudit-1-fix-brief.md) | research | TOOL-dFoldedAudit-1 TOOL-dFoldedAudit-4 TOOL-dFoldedAudit-7 |
| [2026-11-01-prompt-TOOL-dFoldedAudit-6-build-brief.md](../prompts/2026-11-01-prompt-TOOL-dFoldedAudit-6-build-brief.md) | research | — |
| [2026-11-01-prompt-TOOL-dFoldedAudit-6-spec-brief.md](../prompts/2026-11-01-prompt-TOOL-dFoldedAudit-6-spec-brief.md) | research | — |

<!-- /gen:spec-records -->

## 1. Goal

A spec audit that folds a local fix bumps the spec's revision, and today that move owes a hand
`spec-revised` deviation record, so the owner's fold-in-place rule would multiply hand records. A
revision move whose §9 entry cites a spec-audit review record of this build that names the spec
owes none, and a move with no such citation is still reported. The design's tag is [fold-records],
and the build's brief states the outcome as its acceptance line 6.

## 2. Scope (IN)

- **S1** — One predicate, `check_audit_fold(spec_text, unit, revs, audits, read)` in
  `tools/memory-tree/design_lib.py`, over a new reader `read_rev_log(text)`. It is true when `revs`
  is non-empty and each revision in it has a §9 entry citing, by file stem as a whole token, a record
  of `audits` whose text names `unit` as a whole token. Observed by AC5 and AC6.
- **S2** — `read_population` in `tools/memory-tree/deviation_join.py` asks the predicate once per
  material revision, before either revision arm appends a member, so a fold joins neither the
  `revision` arm nor the `audit` arm. Observed by AC1, AC2, AC3 and AC4.
- **S3** — `derive_past_pin_ids` in `tools/memory-tree/gen_build_index.py` asks the same predicate
  for the revisions past the pin, so an id every one of whose later revisions is a cited fold leaves
  the rendered `Ids whose spec moved past its audited revision:` line. Observed by AC5 and AC7.
- **S4** — Five new plants in the join's fixture: `audit-fold`, `audit-fold-pass`,
  `audit-fold-stranger`, `audit-fold-foreign` and `audit-fold-norev`, each with its `PLANT_EXITS`
  row and, where it reds, its needle. Observed by AC1, AC2, AC3 and AC4.
- **S5** — The pass re-renders the generated regions S3 moves, with
  `python tools/memory-tree/gen_build_index.py --write`, in its build commit, because check 9
  byte-compares them. Observed by AC8.
- **S6** — The join's docstring, its THE POPULATION paragraph, states the exemption and names the
  predicate, and `derive_past_pin_ids`' docstring says the same. NOT OBSERVED: a docstring sentence
  has no behaviour, and the closing review reads it against the code.

## 3. Non-goals (OUT)

- The §9 line itself. The disposal stage writes it, and the citation's text is that stage's to
  emit.
- M4's sentence "by anything but that review's own fold", which gains the sibling edit in
  `TOOL-dFoldedAudit-1`.
- The other four member arms: an `add` member for a promoted unit, a rescope row, an `amended rev-N`
  ledger line and a divergence hand-back all stay members. Only a spec revision is exempted.
- Landed records. The 26 records dMindYourWords carries stay on disk and stay joined to nothing that
  moved; none is retired, and no landed spec gains a citation.
- The `specs-audited` term at `--close`, which reads whether a record ever named the unit and not
  the revision.
- Grading whether the cited finding really caused the edit. The closing review judges that, as it
  judges a deviation record's reason today.
- A cutoff. The predicate reads what a §9 entry says, so an older entry that cites a record the same
  way is the same fact and takes the same answer.
- A kit version bump. A branch owes none, because the lander mints each version at the landing
  (`tools/push-main.sh:26-31`).

### Edges

- **consumes-from** `TOOL-dFoldedAudit-4` — the §9 line a sibling edit writes, naming the repair unit and the review record by its file stem, which is what admits that edit here; a line naming the repair unit alone stays reported
- **hands-off** `TOOL-dFoldedAudit-1` — the M4 sentence this predicate implements, which that unit rewrites to admit the disposal's sibling edit

## 4. Design

### The move today

`read_population` walks each chain-build spec's revisions and keeps those past a first pass or past
the newest audit pin (`tools/memory-tree/deviation_join.py:589-593`). A material one becomes a
`revision` member at `<unit>@rev-<N>` when it follows the unit's first pass (`:599-602`), and an
`audit` member at the pin when it follows the audit pin (`:603-607`).

The design's sentence names only the `audit` arm, and the two arms are not equally loaded. Of
dMindYourWords' 26 `spec-revised` records for spec revisions, 19 answer the `revision` arm and 7 the
`audit` arm. The cause is that spec run's authoring commit, `7fba335c5`, which names every unit in
its subject and reads as each unit's first pass. PINNED, measured 2026-11-01 from each record's
`**Evidence:**` line. So the exemption gates the move and never one arm: exempting only `audit`
would leave 19 of the 26 owed, which is what [fold-records] exists to stop.

### The predicate

```python
def read_rev_log(text):
    """`{N: entry}` from the section headed by the text `Revision log`, at any ordinal. An entry is a
    `- rev-<N>` line plus every non-blank line after it, REV_SCOPE_CUTOFF's own definition."""

def check_audit_fold(spec_text, unit, revs, audits, read):
    """True when `revs` is non-empty and every N in it has an entry citing a record of `audits`."""
```

`audits` holds repo-relative paths of one build's `spec-audit` records. `read(path)` returns a
record's text. The stem is the file name less `.md`. Matching uses the boundary
`check_approver` already uses (`tools/memory-tree/deviation_join.py:728`), `(?<![A-Za-z0-9-])` and
`(?![A-Za-z0-9-])`, so the stem `2026-10-21-review-FIX-dTrueNorth-2` is no citation of a record
whose stem continues `-26`, and the id `FIX-x-1` is no naming of `FIX-x-10`.

The function tests the stems against the entry first, and reads only a record an entry actually
cites, so an id with no citing entry costs no record read. This tree binds 399 `spec-audit` records,
PINNED 2026-11-01 by the probe below, and 184 specs carry a citing entry.

"Names the spec" reads the record's whole text and not only its `**Serves:**` line, because a scoped
round's record does not pin a sibling it did not audit, and that sibling is exactly what a repair
unit's edit moves. A record that names the id only in passing therefore satisfies it. That is the
cost of keeping this unit disjoint from `TOOL-dFoldedAudit-5`'s machine line, and it is stated under
§5 risks.

### The two callers

In `read_population`, the audits of build `b` are the tracked records under `reviews/` that
`read_bindings` binds as `spec-audit`, with or without a pin, filtered by the existing
`derive_slug` (`tools/memory-tree/deviation_join.py:553`). The list at `:561-562` is not reused,
because it drops an unpinned record. The test sits in the loop at `:594`, after the material test:

```python
rev = read_header_rev(before, HDR_RE)
now = read_header_rev(after, HDR_RE)
moved = range(rev + 1, now + 1) if rev is not None and now is not None else ()
if check_audit_fold(after or "", unit, moved, by_build.get(b, ()), read_text):
    continue
```

A material edit with no header move gives an empty range, which is false, so an edit made in place
under an old citation is still reported. A commit jumping two revisions owes a citing entry for
both.

In `derive_past_pin_ids`, a unit past its highest pin `top` is left out when
`check_audit_fold(text, unit, range(top + 1, rev + 1), audits, read)` is true, `audits` being the
`records` argument's `spec-audit` paths. The signature gains `root`, the third parameter, because a
record's path is repo-relative (`tools/memory-tree/gen_build_index.py:2716`) and a unit's is
absolute (`:2789`). `plan()` sets `b["root"]` and `render_region` passes it. Its `none` branch and
its pinned count do not change.

### The live effect

The candidate predicate ran over the real tree before this was written, per the charter's [class]
rule. 974 ids sit past their pin, 184 specs carry a citing entry, and 77 ids clear: 40 in
dRankedPlan, 23 in dFurnishedOrders and 14 in dDeclaredLoop. Nothing clears in dSafePassage. PINNED,
measured 2026-11-01 at `dccdeaa8` by a read-only probe; S5's diff re-derives them at the pass.

### What the other units write

The disposal prompt orders a §9 line naming `<report stem>`, the file name `lastReport` ends in less
`.md`, and the finding id (`TOOL-dFoldedAudit-3` §4 "The by-nature prompt"). That is the stem this
predicate matches, so a fold's own line satisfies it with no change here. `TOOL-dFoldedAudit-3` also
has a caller renaming the report rename the citation in the same commit. A sibling edit is admitted by the same test,
because `TOOL-dFoldedAudit-4`'s prompt has every §9 line the stage writes name the report's stem, a
§3 mirror's included. No criterion here rests on either, because every plant writes its own entry.

### Inventory

| Name | Kind | Cell |
|---|---|---|
| `check_audit_fold` | function | `py.function`, `OK` from the lexicon's suggest verb |
| `read_rev_log` | function | `py.function` |
| `audit-fold`, `audit-fold-pass`, `audit-fold-stranger`, `audit-fold-foreign`, `audit-fold-norev` | fixture plants | none: strings in `PLANTS` |

The plants append to `PLANTS` and to the `PLANT_UNITS` tuple's tail
(`tools/memory-tree/deviation_join.py:851`, `:879`), so no existing plant's unit number moves. Each
writes its §9 entry through `render_spec`'s `extra` argument (`:983`). `audit-fold-foreign` writes
its record under `FIXTURE_BUILDS[1]`, the second chain build.

### Rollout

No switch. It is a loosening of a report that the host runs at `report` policy
(`tools/memory-tree/deviation_join.py:144`), so no leg's exit moves on the real tree.

### Files touched (estimate)

`tools/memory-tree/design_lib.py` · `tools/memory-tree/deviation_join.py` ·
`tools/memory-tree/gen_build_index.py`

The re-rendered generated regions of `memory/builds/dRankedPlan/README.md`,
`memory/builds/dFurnishedOrders/README.md` and `memory/builds/dDeclaredLoop/README.md`, and whatever
else the index generator derives from them.

`tools/memory-tree/design_lib.py` is one file beyond the unit brief's list. Both callers already
import it at module level, and it is where the kit's spec-text readers live
(`tools/memory-tree/design_lib.py:528`, `:543`).

### Alternatives rejected

- **Exempt only the `audit` arm**, as the design's sentence reads. Rejected on the 19-of-26
  measurement above.
- **Home the predicate in `deviation_join.py`** and import it lazily in the generator. That stays
  inside the brief's file list, but it loads the routed-commit host on every render with a unit past
  its pin, to read one section of a spec.
- **Grade `**Serves:**` pins only.** Rejected because a scoped round's record pins no sibling, so
  every sibling edit after round 1 would owe a hand record, which is the multiplication this unit
  exists to end.
- **Read every `spec-audit` record up front.** Rejected on cost: the citation test needs only the
  records an entry names.

## 5. Production-readiness checklist

- security: N/A. A read of tracked files, on no new write path and no new input.
- perf / scale: one extra read per cited record, in a process that already reads every spec. An id
  with no citing entry reads no record.
- error / empty / loading states: an empty `revs` is false, and so is an absent Revision log. A
  `read` of a tracked record gone from the tree is the absence `read_text` already reports.
- observability: the join's summary line counts members, so a cleared fold reads as one fewer
  member. No new output, because a member that does not exist has nothing to print.
- risks:
  - A record renamed after a fold leaves the citation stale, and the move is then reported. That
    fails loud, as a false member, never as a silent exemption. M8's rename rule is the reason to
    rename before folding.
  - A record naming the id only in passing satisfies "names". A run could therefore clear a
    non-fold by citing a real record. The citation is a claim in a tracked file, the closing review
    reads it, and a hand record's reason is the same kind of claim.
  - S5 writes three landed READMEs' generated regions, and the brief bars a write to a build with a
    live run claim. The pass runs `--claims` first. A live claim on any of the three is a park with
    the question, the options and the reason, because the regions cannot be skipped by a list.
- testing: five plants and two generator arms, per §6, with their `New arm:` lines in §7.
- migration: none on disk. The landed records stay; S5 is a re-render.
- user docs: N/A. No page under `help/` describes the deviation join.

## 6. Acceptance criteria

- **AC1** — When `python tools/memory-tree/deviation_join.py --fixture --plant audit-fold --policy refuse`
  runs, it exits 0 and prints no member for the plant's unit: the spec moved from rev-1 to rev-2 past
  an audit pin at rev-1, and its §9 entry for rev-2 cites that record's stem.
  Red when: `read_population` never asks `check_audit_fold`, and the plant exits 1 naming
  `past its audited revision rev-1`.
- **AC2** — When `python tools/memory-tree/deviation_join.py --fixture --plant audit-fold-pass --policy refuse`
  runs, it exits 0: the same cited fold, committed after the unit's first pass.
  Red when: the predicate gates only the `audit` arm, and the plant exits 1 at
  `spec-revised` naming `recorded by nobody`.
- **AC3** — When `python tools/memory-tree/deviation_join.py --fixture --plant audit-fold-stranger --policy refuse`
  runs, and the same with `--plant audit-fold-foreign`, each exits 1 naming
  `past its audited revision rev-1`: the first entry cites a `spec-audit` record of this build whose
  text never names the unit, and the second cites a record of the other chain build that does.
  Red when: the predicate tests only that the cited stem exists, or reads stems across builds.
- **AC4** — When `python tools/memory-tree/deviation_join.py --fixture --plant audit-fold-norev --policy refuse`
  runs, it exits 1 naming `past its audited revision rev-1`: the spec changed materially with no
  header move, and an older entry cites the record. `--plant audit-pin` still exits 1 with no
  citation at all.
  Red when: the predicate reads the entry at the header's revision instead of the revisions moved.
- **AC5** — When a `python -c` probe imports `design_lib` and calls `check_audit_fold` directly, it
  answers true for an entry whose citation wraps onto a continuation line and for a `## 8. Revision log`
  heading, and false for an empty `revs`, for a stem that is a prefix of the cited stem, and for an id
  that is a prefix of the named id.
  Red when: the reader finds the section by ordinal, or either match drops its boundary.
- **AC6** — When a `python -c` probe imports `deviation_join` and `design_lib`, then
  `deviation_join.check_audit_fold is design_lib.check_audit_fold` prints `True`, and
  `grep -c check_audit_fold tools/memory-tree/gen_build_index.py` prints at least 1.
  Red when: either caller keeps a copy of the predicate.
- **AC7** — When a `python -c` probe calls `derive_past_pin_ids` over a fixture build with a unit at
  rev-3 pinned at rev-1, it omits the unit where the entries for rev-2 and rev-3 both cite the record,
  and returns `<unit>@rev-1` where the rev-3 entry cites none.
  Red when: the function clears a unit on one citing entry, or never reads the entries.
- **AC8** — When `python tools/memory-tree/gen_build_index.py --write` runs in the pass, `git diff --name-only`
  over the build READMEs lists dRankedPlan, dFurnishedOrders and dDeclaredLoop, and
  `git diff --quiet -- memory/builds/dSafePassage` exits 0.
  Red when: a build outside the measured three moves, which means the predicate reads wider than the
  probe did.
  figure: PINNED, the three builds measured 2026-11-01 at `dccdeaa8`; a differing list at the pass is
  compared against the same probe's re-run, not edited here.
  permission: `--claims` runs first, and a live claim on any of the three stops the write (§5 risks).

## 7. Gates

`build-index selftest` · `routed-commits selftest` · `tier2-review self-test` · `policy fixtures` · `memory hygiene` · `kit/dogfood doc parity` · `kit version markers` · `kit epoch (shipped bytes move, the version moves)` · `verdict epoch (kit version dates the engine)` · `spec tokens (a spec's own names resolve)` · `recall floor` · `recall floor arms`

New arm: tools/memory-tree/deviation_join.py · covers AC1 AC2 AC3 AC4 · the five plants in `PLANTS` under `PLANT_EXITS`, read by its arms and by `routed_commits.py`'s; the failing case is staged by making `check_audit_fold` return False for AC1 and AC2 and True for AC3 and AC4 · none
New arm: tools/memory-tree/gen_build_index.py · covers AC5 AC6 AC7 · the past-pin arm beside `TOOL-dTrueNorth-5 AC6` at `gen_build_index.py:6074`, plus the predicate's boundary cases; the failing case is staged by clearing a unit on its first citing entry · none

## 8. Open questions

none

## 9. Revision log

- rev-1 · 2026-11-01 · initial draft, from the design's [fold-records], the brief's acceptance line
  6 and the reuse scout's Q2.
- rev-2 · 2026-11-01 · §4 · M2's cross-read: this spec said the disposal prompt names the path
  `lastReport` holds, where `TOOL-dFoldedAudit-3` §4 and `TOOL-dFoldedAudit-4` §4 write
  `<report stem>`. The predicate and every criterion stand, because the stem is what they read.
- rev-3 · 2026-11-01 · §7 · the fix brief's item 3. The three build READMEs under Files touched trip
  the guard `memory/`, which `recall floor` and `recall floor arms` both carry, and §7 named neither.
  The leg line now names both, which clears the guards join's two hits.

## 10. Reuse audit

`reuse_lookup.py` on "exempt a spec revision from a deviation record when a review fold made it"
named `read_spec_revisions` and `read_spec_edges` in `tools/memory-tree/design_lib.py` as the seam,
fan-in 5 and 2, and `read_records` in the join. This unit extends the two revision-arm branches at
`tools/memory-tree/deviation_join.py:594-607`, `derive_past_pin_ids` at
`tools/memory-tree/gen_build_index.py:1621` and the spec-text readers of `design_lib.py`. It reuses
`read_bindings`, `read_header_rev`, `derive_slug` and the REV_SCOPE_CUTOFF entry definition. The
scout's return said the exemption belongs at `deviation_join.py:589-606` and at
`gen_build_index.py:1612-1615`; both hold, and the second is the call site of the function at
`:1621`. The recall hits on `TOOL-dTrueNorth-4` and `TOOL-dTrueNorth-5` agree with the source. No
stale hit changed the design.

Recall terms used: deviation_join audit member spec-revised rev move past pin fold section-9 citation review record
