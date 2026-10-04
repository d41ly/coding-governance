# TOOL-aMendedFleet-1 — restore the views helper and the `--status` entry merge 01c22e155 lost

**Status:** CLOSED · rev-1 · 2026-10-04 · node a · Tier-1 · base 7af5f564 · streams tooling · order 1

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-04-build-TOOL-aMendedFleet-1-1-acceptance-ledger.md](../build/2026-10-04-build-TOOL-aMendedFleet-1-1-acceptance-ledger.md) | journal | — |
| [2026-10-04-prompt-TOOL-aMendedFleet-1-0-run-mandate.md](../prompts/2026-10-04-prompt-TOOL-aMendedFleet-1-0-run-mandate.md) | journal | — |
| [2026-10-04-prompt-TOOL-aMendedFleet-1-1-source-report.md](../prompts/2026-10-04-prompt-TOOL-aMendedFleet-1-1-source-report.md) | journal | — |
| [2026-10-04-prompt-TOOL-aMendedFleet-1-2-source-synthesis.md](../prompts/2026-10-04-prompt-TOOL-aMendedFleet-1-2-source-synthesis.md) | journal | — |
| [2026-10-04-prompt-TOOL-aMendedFleet-1-3-spec-brief.md](../prompts/2026-10-04-prompt-TOOL-aMendedFleet-1-3-spec-brief.md) | journal | — |
| [2026-10-04-prompt-TOOL-aMendedFleet-1-4-build-brief.md](../prompts/2026-10-04-prompt-TOOL-aMendedFleet-1-4-build-brief.md) | journal | — |

<!-- /gen:spec-records -->

## 1. Goal

Merge `01c22e155` ("origin/main (dMendedRecall) into the aRepatriatedFork run branch", 2026-10-01)
resolved `tools/unattended/unattended.sh` and `tools/unattended/VERBS.template.md` to its first
parent's side. Two CLOSED units of node d's dMendedRecall build lost their code on main:
`TOOL-dMendedRecall-2`'s views helper `write_ask_views` with its counter and call, and
`TOOL-dMendedRecall-3`'s field-by-field `--status` entry. Both records still read CLOSED. This unit
puts both back on main from the second parent `ef1dcdb61`, so an inherited-red close that files an
ask commits its own record again, and the verb contract again names every field `verb_status` prints.

## 2. Scope (IN)

- **S1** — `tools/unattended/unattended.sh` regains, from `ef1dcdb61`, the four pieces the merge
  lost: the auto-file header's sentences naming the views helper, the helper `write_ask_views`
  itself, the `filed` counter in `write_inherited_asks` (its `local` declaration and its increment
  after a read-back succeeds), and the once-per-call `write_ask_views "$filed"` call after the loop.
  The helper's body is byte-identical to `ef1dcdb61` and to node d's restore commit `e6e55d5ab`,
  which carry the same 79 lines. Observed by AC1, AC2, AC3.
- **S2** — The `--status` entry of `tools/unattended/VERBS.template.md` regains
  `TOOL-dMendedRecall-3`'s account from `ef1dcdb61`, byte-identical to that parent's entry, and its
  render `memory/guides/UNATTENDED-VERBS.md` is re-copied by the kit adopter. Observed by AC4, AC5.
- **S3** — The restored dMendedRecall acceptance is re-observed on this branch: `TOOL-dMendedRecall-2`
  AC5's counts and its view-render arms, and `TOOL-dMendedRecall-3` AC1 to AC3's spellings. Observed
  by AC3, AC4.
- **S4** — The acceptance ledger records, per file `01c22e155` conflicted on, only the two this unit
  restores; the census of the rest of that merge is unit 2's. Observed by AC6.

## 3. Non-goals (OUT)

- Node d's two reconciliations, which ride on its own unlanded units: the sentence that a BLOCKER
  filing counts as a HIGH one and its `sev` local, and the `LANDED (attended)` phase form in the
  verb entry. Main's driver prints no such form and files no BLOCKER, so writing either here would
  make main's contract describe code main does not hold. §8 F1 records the probe.
- Any other definition any other merge lost. That census and its restores are `TOOL-aMendedFleet-2`.
- The gate that refuses such a merge. That is `TOOL-aMendedFleet-3`.
- The two dMendedRecall records. They stay CLOSED: their units were built and landed, and this unit
  restores code a later merge lost.
- The unattended kit version marker. The build moves it once, in its one version sweep after the
  last unit that edits the kit, never per unit.

### Edges

none

## 4. Design

### Evidence

Measured at HEAD `af449c0b` (run BASE `7af5f564`, main `35438ba0`), 2026-10-04:

- `grep -c write_ask_views tools/unattended/unattended.sh` prints 0 at HEAD and 3 at `ef1dcdb61`.
- A definition-level comparison of the driver over the merge-base `1f915870`, both parents and the
  merge finds exactly one name the second parent added that the merge lacks, `write_ask_views`, and
  none the first parent added. HEAD still lacks it.
- The helper's body extracted by `awk` from `ef1dcdb61` and from `e6e55d5ab` is byte-identical.
- Every dependency the helper calls is defined at HEAD: `resolve_python`, `run_bounded` with its
  `RB_TOOK` and `RB_OUT`, `GIT`, `$M`, and the library's `resolve_index_generator` and
  `derive_index_repair` in `tools/unattended/lib-unattended.sh`.
- `verb_status` is byte-identical at `ef1dcdb61` and at HEAD, so `ef1dcdb61`'s `--status` entry
  describes HEAD's line exactly. Every literal fragment that entry names, from `asks as pinned` to
  `in the harness listing at`, prints at least once from HEAD's driver.
- `git apply --check` of `e6e55d5ab`'s driver diff onto HEAD fails at its second hunk: its context
  is `read_ask_back`'s SEV-aware signature from node d's unit 16, and HEAD's `read_ask_back` takes
  no SEV. The verb-entry hunk applies, but adds `LANDED (attended)`, which HEAD's driver never prints.
- The driver suite still carries the `TOOL-dMendedRecall-2` section and its `f4-views-double` arms
  (6 hits), so the arms exist and fail only for want of the helper.

### The restore

Hand-apply the `ef1dcdb61` bytes at their positions in HEAD's file, never a cherry-pick of
`9cba3c3f8` and never `e6e55d5ab`'s patch. Three dMendedRecall revisions sit between `9cba3c3f8`
and `ef1dcdb61`, and `e6e55d5ab`'s context does not exist on main.

| Piece | Source | At HEAD |
|---|---|---|
| auto-file header sentences | `ef1dcdb61` driver, the paragraph ending "whose line carries the repair" | after the `hold ·` sentence above `read_leg_argv` |
| `write_ask_views` with its header block | `ef1dcdb61`, 79 function lines plus the comment block above them | between `write_backlog_rows` and `read_ask_back` |
| `filed=0` local | `ef1dcdb61`: `local r8=${2:0:8} today filed=0` | `write_inherited_asks`'s second `local` line |
| `filed=$((filed + 1))` | `ef1dcdb61`, after the `gates-green: filed ask` echo | same position |
| the call | `ef1dcdb61`, after the loop: the S1 comment, `[ "$filed" -gt 0 ] \|\| return 0`, the call, `return 0` | end of `write_inherited_asks` |
| `--status` entry | `ef1dcdb61:tools/unattended/VERBS.template.md`, 29 lines | replaces HEAD's 3-line entry |

Then `bash tools/unattended/adopt-unattended.sh` re-copies the verb render.

### Rollout

When node d's branch lands, three hunks meet this restore: the header paragraph, the `local` line
and the verb entry's phase sentence. In each, node d's side is this side plus its own units'
additions, so the reconcile takes node d's side and loses nothing. The acceptance ledger states this
so the reconciler does not re-derive it.

### Files touched (estimate)

- `tools/unattended/unattended.sh`
- `tools/unattended/VERBS.template.md`
- `memory/guides/UNATTENDED-VERBS.md`

## 5. Production-readiness checklist

- security — N/A: it restores reviewed, landed code and adds no write path. The helper stages only
  its own render delta and refuses to render over a dirty input, as it did when it landed.
- perf / scale — one generator render per close that files at least one ask, as before.
- error / empty / loading states — the helper's named-miss lines return with it; a miss never refuses.
- observability — the `gates-green:` lines the helper prints return with it.
- risks — a hand-apply that misplaces the call; AC2 and AC3 observe both the placement and the arms.
- testing — the existing `TOOL-dMendedRecall-2` suite arms; no new arm.
- migration — none.
- user docs — the `--status` entry of the verb contract and its render.

## 6. Acceptance criteria

- **AC1** — When `grep -c write_ask_views tools/unattended/unattended.sh` runs it prints 3: the header
  sentence, the definition and the call. `grep -c -F 'filed=$((filed + 1))' tools/unattended/unattended.sh`
  prints 1. Red when: either prints 0, which is HEAD's reading of both.
- **AC2** — When the helper is cut by `awk '/^write_ask_views\(\)/{p=1} p{print} p&&/^}/{exit}'` from
  the working file and from `git show` of `tools/unattended/unattended.sh` at `ef1dcdb61`, `diff`
  of the two cuts is empty, and the same cut from that file at `e6e55d5ab` is empty against it too.
  Red when: any byte of the body differs from either source.
- **AC3** — When `TOOL-dMendedRecall-2`'s AC5 is re-run, `grep -c 'fail 69 ' tools/unattended/unattended.sh`
  prints 1 and `python tools/lexicon/lexicon.py --suggest write_ask_views --as sh.function` prints a
  line opening `OK`. When the driver suite's prologue and its `TOOL-dMendedRecall-2` section are cut
  into one script under the scratchpad and run alone by `bash` over the restored driver, every
  assertion in that section passes, including the `f4-views-double: 1 filed` hit. Run the same
  slice over HEAD's driver first: it must fail those arms, or the slice proves nothing.
  Red when: an arm fails over the restored driver, or the slice passes over HEAD's driver too.
  cost: minutes for the slice; composing the cut is the expensive half.
  fixture: none in the tree; the slice builds its fixture repositories under the scratchpad, and a
  clone among them goes under a short `%TEMP%` path.
- **AC4** — When `grep -c -F` runs over `tools/unattended/VERBS.template.md` for each of
  `asks as pinned`, `asks moved at HEAD`, `worktree holds the run`, `worktree not the run` and
  `worktree unanswerable`, each prints at least 1, where HEAD prints 0; the entry cut by
  `awk '/^- .--status. /,/^- .--audit. /'` carries `check 73`, `check 58` and `lease-utc`; and
  `grep -c -F 'LANDED (attended)' tools/unattended/VERBS.template.md` prints 0.
  Red when: a verdict spelling is unnamed, or the entry names a phase form HEAD's `verb_status`
  does not print.
- **AC5** — When `cmp tools/unattended/VERBS.template.md memory/guides/UNATTENDED-VERBS.md` runs it
  exits 0, and `bash tools/unattended/adopt-unattended.sh --check` prints `in sync`.
  Red when: the render differs from its template.
- **AC6** — When `grep -c dUnstuckLanding tools/unattended/unattended.sh` runs it prints 0, as at
  HEAD, and the acceptance ledger names `TOOL-aMendedFleet-2` as the owner of the rest of the merge's
  census. Red when: the restore copied a sentence naming a unit main does not define.

## 7. Gates

The close's bar runs these; this unit's pass runs only the direct checks in §6.

`unattended kit gate` · `unattended skill wiring` · `lexicon naming predicates` · `kit version markers` · `kit epoch (shipped bytes move, the version moves)` · `memory hygiene` · `spec tokens (a spec's own names resolve)` · `recall floor` · `recall floor arms`

New arm: none. The `TOOL-dMendedRecall-2` arms already sit in the driver suite, and this unit makes them pass again.

## 8. Open questions

- **FACT-QUESTION · F1** — Is the restore byte-identical to node d's `e6e55d5ab` throughout, as the
  brief asks, or to the parent `ef1dcdb61`, which the brief also names? Probe: `git apply --check`
  of `e6e55d5ab`'s driver diff onto HEAD, plus `grep -c -F 'LANDED (attended)'` and
  `grep -c dUnstuckLanding` over HEAD's driver. The observation that decides: the patch fails on
  `read_ask_back`'s SEV signature, and both greps print 0, so node d's extra bytes describe code
  main does not hold. Liveness: the same `git apply --check` passes on the verb-entry hunk, so the
  probe can answer "applies". RESOLVED (agent, 2026-10-04, delegated): the helper's body is
  byte-identical to both sources, and every other byte comes from `ef1dcdb61`. The three hunks
  where node d's side is a superset reconcile to node d's side when its branch lands (§4 Rollout).

## 9. Revision log

- rev-1 · 2026-10-04 · initial draft.

## 10. Reuse audit

The seam is the helper itself, at its last landed blob `ef1dcdb61:tools/unattended/unattended.sh`,
and node d's restore `e6e55d5ab`, whose body this unit reuses byte for byte. `python
tools/codebase-map/reuse_lookup.py "re-render and stage generated views after filing inherited-red
ask rows"` ranked only Python name-stem neighbours, `render_family_view` in
`tools/memory-tree/backlog.py` the closest, and printed `unscanned layers: .sh`, so it cannot see the
shell seam; the evidence is the source read in §4. The recall probe returned `TOOL-dMendedRecall-2`
and `TOOL-dAlignedCarrier-9` as the binding records.

Recall terms used: write_ask_views inherited red auto-file views stale render stage close records commit merge dropped restore
