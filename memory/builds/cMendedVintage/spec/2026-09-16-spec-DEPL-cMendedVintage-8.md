# DEPL-cMendedVintage-8 — a descriptor shipping `rendered` rows must declare a regenerate

**Status:** CLOSED · rev-2 · 2026-09-16 · node c · Tier-2 · base 859daa67 · streams deployer · order 11

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-09-16-prompt-DEPL-cMendedVintage-1-1-spec-briefs.md](../prompts/2026-09-16-prompt-DEPL-cMendedVintage-1-1-spec-briefs.md) | journal | DEPL-cMendedVintage-1 DEPL-cMendedVintage-2 DEPL-cMendedVintage-3 DEPL-cMendedVintage-4 DEPL-cMendedVintage-5 DEPL-cMendedVintage-6 DEPL-cMendedVintage-7 DEPL-cMendedVintage-9 DEPL-cMendedVintage-10 DEPL-cMendedVintage-11 DEPL-cMendedVintage-12 DEPL-cMendedVintage-13 DEPL-cMendedVintage-14 TOOL-cMendedVintage-1 TOOL-cMendedVintage-2 TOOL-cMendedVintage-3 TOOL-cMendedVintage-4 TOOL-cMendedVintage-5 TOOL-cMendedVintage-6 TOOL-cMendedVintage-7 TOOL-cMendedVintage-8 TOOL-cMendedVintage-9 |
| [2026-09-16-prompt-DEPL-cMendedVintage-8-2-build-brief.md](../prompts/2026-09-16-prompt-DEPL-cMendedVintage-8-2-build-brief.md) | journal | — |
| [2026-09-16-review-DEPL-cMendedVintage-1-spec-audit-round1.md](../reviews/2026-09-16-review-DEPL-cMendedVintage-1-spec-audit-round1.md) | spec-audit | TOOL-cMendedVintage-1 TOOL-cMendedVintage-2 TOOL-cMendedVintage-3 TOOL-cMendedVintage-4 TOOL-cMendedVintage-5 TOOL-cMendedVintage-6 TOOL-cMendedVintage-7 TOOL-cMendedVintage-8 TOOL-cMendedVintage-9 DEPL-cMendedVintage-1 DEPL-cMendedVintage-2 DEPL-cMendedVintage-3 DEPL-cMendedVintage-4 DEPL-cMendedVintage-5 DEPL-cMendedVintage-6 DEPL-cMendedVintage-7 DEPL-cMendedVintage-9 DEPL-cMendedVintage-10 DEPL-cMendedVintage-11 DEPL-cMendedVintage-12 DEPL-cMendedVintage-13 DEPL-cMendedVintage-14 |

<!-- /gen:spec-records -->

## 1. Goal

Selfcheck arm 7l opens by skipping every descriptor that declares no `[[regenerate]]`, so its
population is the kits that already have the block and what it grades is their prose. The kits that
need the block are precisely the ones it cannot see. Invert the population: a descriptor shipping any
`role = "rendered"` row and declaring no regenerate is a refusal, derived from the descriptors
themselves, with no new declaration and no new file.

## 2. Scope (IN)

- **S1** A refusal is added ahead of arm 7l's existing skip in `tools/govkit/govkit.py`: for each
  descriptor, if any `[[files]]` rule carries `role = "rendered"` and the descriptor declares no
  `[[regenerate]]`, `selfcheck` fails naming the kit, the count of its rendered rows and the
  remedy — declare the block, or give the kit a render entrypoint first. Observed by AC1.
- **S2** The arm prints a note on every run counting both sides of the join: how many descriptors
  ship rendered rows and how many of those declare a regenerate. A refusal that reports nothing when
  it matches nothing is indistinguishable from a probe that cannot fire. Observed by AC2.
- **S3** The refusal is derived from the descriptor set `read_descriptors` already returns. No
  registry entry, no waiver file, no exemption key. A kit that genuinely wants a rendered row with no
  regenerate has no escape here, which is the point: at BASE there are four such kits and every one
  is a live defect. Observed by AC1.
- **S4** A failing case is observed before this lands, on a PURPOSE-BUILT fixture rather than by
  editing a shipped descriptor: a scratch gov tree carrying one entry whose descriptor has a rendered
  row and no `[[regenerate]]` reds `selfcheck`, and the same descriptor with the block declared does
  not. Observed by AC3. rev-2 states the fixture; rev-1 said "a scratch copy of the tree with one
  block removed", which stages the break inside a real kit's descriptor.

## 3. Non-goals (OUT)

- No change to arm 7l's existing prose checks. The claim sentence and the silence sentence keep their
  predicates, their population and their notes. rev-2 amends this: one line of that half's PATH
  RESOLUTION moved, because the control fixture found it crashing. No predicate, population or note
  moved with it. See section 9.
- No waiver mechanism. Adding one before a single case needs it would ship an escape from a rule
  whose whole value is that it has none.
- No refusal for the mirror shape — a descriptor declaring a regenerate while shipping no rendered
  row. That is harmless: the argv runs and re-renders nothing, and refusing it would red the
  review-harness kit, whose regenerate writes artifacts through its parity gate.
- This unit does not close any of the four hits. `DEPL-cMendedVintage-5` closes three and
  `TOOL-cMendedVintage-1` closes the fourth, which is why this unit is ordered after both.

### Edges

- **consumes-from** `DEPL-cMendedVintage-5` — three of the four descriptors this refusal names are
  drained by that unit. Landing this first would red `govkit selfcheck` in this repo.
- **consumes-from** `TOOL-cMendedVintage-1` — the fourth, `memory-tree`, needs a render entrypoint
  before its block can name one.
- **hands-off** external — an adopter running `selfcheck` against their own registry gets the same
  refusal over their own descriptors, which is the class this gates rather than the instance.

## 4. Design

### Data model

The join is over the descriptor map `selfcheck` already holds. Two facts per descriptor and no
lookup outside it:

| fact | source |
|---|---|
| ships a rendered row | any `[[files]]` rule whose `role` is `rendered` |
| declares a regenerate | a non-empty `regenerate` key on the descriptor |

The refusal fires on the first fact true and the second false. It sits BEFORE the existing
`if not d.get("regenerate"): continue`, because that line is what makes the offending population
invisible.

### Inventory

Nothing is minted. One `r.fail` message and one `r.note` line inside an arm that exists.

### Rollout

Red at BASE, by construction, on four kits. That is how the failing case is seen without staging one,
and it is also why this unit is last in its group: it lands green only once both closing units are
in. AC3 keeps the staged break anyway, because a gate whose only observed red was a state the build
then repaired has never been run against a tree that is otherwise clean.

### Alternatives rejected

- **Grade the claim prose over every kit rather than only over regenerate-declaring kits.** That
  widens a heuristic over prose, and the defect is structural: a rendered row with nothing that can
  refresh it. Prose is downstream of the declaration.
- **Make it a warning rather than a refusal.** The four hits at BASE are each a kit whose artifacts
  go a vintage stale at every adopter on every update. A warning is what the declines already are.

### Files touched (estimate)

| Path | Change |
|---|---|
| `tools/govkit/govkit.py` | the refusal and the note inside arm 7l |
| `tools/govkit/selftest.py` | one arm staging a descriptor with a rendered row and no regenerate |

## 5. Production-readiness checklist

- security — N/A. The arm reads descriptors this process already parsed and runs nothing.
- perf / scale — two dictionary reads per descriptor, inside a loop that already opens every tracked
  file of every regenerate-declaring kit.
- error / empty / loading states — a descriptor with no `files` key yields no rendered row and is
  silent. A malformed descriptor is refused upstream by the reader, unchanged.
- observability — S2's note is the liveness assertion: it prints the two counts whether or not the
  refusal fires, so a green run says what it examined.
- risks — the arm could red a kit legitimately shipping a rendered row it never refreshes. At BASE no
  such kit exists, and the four it names are all defects. Section 3 records that no waiver ships
  until one does.
- testing — AC1 and AC2 run the checker directly; AC3 runs it against a purpose-built scratch gov
  tree whose descriptor carries the break.
- migration — none.
- user docs — the arm's own header comment states what it does not check, per the gate rule; no page
  changes.

## 6. Acceptance criteria

- **AC1** — When `python tools/govkit/govkit.py selfcheck` runs at the tip of this build, it exits 0,
  and when it runs at this unit's own commit before `DEPL-cMendedVintage-5` and
  `TOOL-cMendedVintage-1` are in the tree, it fails naming each kit that ships a rendered row with no
  regenerate.
  Red when: the refusal is placed after the existing skip, in which case the offending kits are
  filtered out before it is reached and the arm passes over exactly the population it was written for.
  figure: DERIVED — the kit names and the row counts come from the run's own output, not from a list
  in this spec.
- **AC2** — When `python tools/govkit/govkit.py selfcheck` runs against a tree where no descriptor is
  in breach, its note line reports how many descriptors ship rendered rows and how many of those
  declare a regenerate.
  Red when: the note is printed only inside the failure branch, which makes a clean run silent and a
  broken predicate indistinguishable from a satisfied one.
- **AC3** — When `python tools/govkit/govkit.py selfcheck` runs against a scratch gov tree whose one
  entry's descriptor carries a rendered row and no `[[regenerate]]`, it fails naming that kit; the
  same descriptor with the block declared makes the same command exit 0.
  Red when: the predicate reads the key on the wrong object, so a descriptor with no block changes
  nothing and the arm has never been seen to fire.
  fixture: a scratch gov tree under the run's scratch root, built from the suite's own
  `build_scratch_gov_kit`, never the worktree itself and never a shipped descriptor edited in place.
  A fixture proves the mechanism only for the fixture's own values, so AC1's second half is what
  proves it over the SHIPPED descriptors.
- **AC4** — When `python tools/check-kit-placeholders.py` runs, it exits 0, confirming this arm did
  not change which rules the placeholder join reads.
  Red when: the new predicate mutates the descriptor dictionaries it walks, which the placeholder
  join would then read back.

## 7. Gates

`govkit selfcheck` · `govkit selftest` · `kit placeholders (a declared token its adopter substitutes)`

New arm: `tools/govkit/selftest.py` · a fixture descriptor carrying a `rendered` row and no
regenerate block, asserted to fail, beside one with both, asserted to pass · no assertion floor to
move.

## 8. Open questions

- **Q1 — should the refusal name the rendered rows individually or only count them?**
  RESOLVED (agent, 2026-09-16, delegated): count them and name the kit. The remedy is per KIT — one
  `[[regenerate]]` block — so a row list would be detail the operator cannot act on row by row, and
  the rows are one `grep` away in the descriptor the message names.

## 9. Revision log

- rev-1 · 2026-09-16 · initial draft.
- rev-2 · 2026-09-16 · AC3's CONTROL fixture — the first descriptor in the suite to declare a
  `[[regenerate]]`, and therefore the first to reach arm 7l's prose half on a scratch tree — died
  with a `ValueError` instead of passing. That half resolved the repo-relative descriptor path
  against the PROCESS CWD rather than against the tree being checked, and `repo_root()` walks up
  from the script's own file and inherits nothing, so `selfcheck` is meant to run from any
  directory. Reproduced at BASE from `C:/Temp`: `ValueError: 'C:\Temp\tools\memory-tree\kit.toml'
  is not in the subpath of ...`, raised on the first kit declaring a block, which here is every kit
  that ships a rendered row. So the divergence from section 3's non-goal is one operand,
  `pathlib.Path(dpath)` to `root / dpath`, and the sentence predicates, the population and the two
  notes are byte-identical. It is left-shifted by the same control arm: the fixture is the only
  exerciser of that code path outside gov's own checkout, and it reds without the fix.
- rev-2 · 2026-09-16 · S4 and AC3 restated. rev-1 asked for "a scratch copy of the tree with one
  `[[regenerate]]` block removed", which stages the break inside a shipped descriptor; the build
  brief forbids that, and it is the wrong shape anyway — a fixture proves a mechanism only for the
  fixture's own values. What was built is a purpose-built scratch gov tree, and AC1's second half is
  what carries the mechanism onto the SHIPPED descriptors: the arm as committed, run against a
  detached worktree at base 859daa67, exits 1 naming `memory-tree` with 4 rendered rows, and
  `memory-recall`, `drift-audit` and `lexicon` with 1 each, its note reading 6 shipping and 2
  declaring. At this unit's tip the same command exits 0 and the note reads 6 and 6.

## 10. Reuse audit

The seam this unit extends is arm 7l in `tools/govkit/govkit.py`, read from source: it already walks
every descriptor, already holds both facts the join needs, and already reports a note line in the
shape S2 follows. `python tools/codebase-map/reuse_lookup.py "selfcheck arm that refuses a kit
descriptor declaring the wrong thing"` returned no seam — its ranked output is name-token neighbours
such as `armed` in the memory-tree kit and the `*Refused` classes in process-monitor, none of which
is reachable from this arm — so the map contributed nothing here and the citation above comes from
the file. The recall probe returned the measurement that fixes the population: `TOOL-dRetiredFork-29`
counts six kits with twelve rendered rows and zero declarations at the time it was written, and
re-deriving that count over today's descriptors is what AC2's note line does rather than restating
it.

Recall terms used: `--terms "govkit update regenerate rerender descriptor kit.toml rendered role
adopter dark flag rollback receipt outcome"`, with the question "why does govkit update decline a
kit's re-render unless GOVKIT_RERENDER is set, and what did the dark landing buy".
