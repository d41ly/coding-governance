# TOOL-dSafePassage-64 — a `retired-edited` row takes back the role gov's descriptor gives its path once gov ships that path again

**Status:** CLOSED · rev-1 · 2026-10-27 · node d · Tier-2 · base 60d90cb7 · streams tooling · order 5 · advances TOOL-dSafePassage-14

**Derived:** TOOL-dSafePassage-5

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-26-build-TOOL-dSafePassage-64-ledger.md](../build/2026-10-26-build-TOOL-dSafePassage-64-ledger.md) | journal | — |
| [2026-10-27-prompt-TOOL-dSafePassage-64-build-brief.md](../prompts/2026-10-27-prompt-TOOL-dSafePassage-64-build-brief.md) | journal | — |
| [2026-10-28-prompt-TOOL-dSafePassage-37-close-arms-c-brief.md](../prompts/2026-10-28-prompt-TOOL-dSafePassage-37-close-arms-c-brief.md) | research | TOOL-dSafePassage-37 TOOL-dSafePassage-38 TOOL-dSafePassage-39 TOOL-dSafePassage-40 TOOL-dSafePassage-42 TOOL-dSafePassage-43 TOOL-dSafePassage-44 TOOL-dSafePassage-45 TOOL-dSafePassage-47 TOOL-dSafePassage-48 TOOL-dSafePassage-49 TOOL-dSafePassage-5 TOOL-dSafePassage-51 TOOL-dSafePassage-53 TOOL-dSafePassage-54 TOOL-dSafePassage-56 TOOL-dSafePassage-59 TOOL-dSafePassage-62 TOOL-dSafePassage-63 TOOL-dSafePassage-65 TOOL-dSafePassage-66 TOOL-dSafePassage-67 TOOL-dSafePassage-68 TOOL-dSafePassage-69 TOOL-dSafePassage-70 TOOL-dSafePassage-71 |
| [2026-10-28-review-TOOL-dSafePassage-1-71-closing-diff-round1.md](../reviews/2026-10-28-review-TOOL-dSafePassage-1-71-closing-diff-round1.md) | diff-review | TOOL-dSafePassage-1 TOOL-dSafePassage-2 TOOL-dSafePassage-3 TOOL-dSafePassage-4 TOOL-dSafePassage-5 TOOL-dSafePassage-6 TOOL-dSafePassage-7 TOOL-dSafePassage-8 TOOL-dSafePassage-9 TOOL-dSafePassage-10 TOOL-dSafePassage-11 TOOL-dSafePassage-12 TOOL-dSafePassage-13 TOOL-dSafePassage-15 TOOL-dSafePassage-16 TOOL-dSafePassage-17 TOOL-dSafePassage-18 TOOL-dSafePassage-19 TOOL-dSafePassage-20 TOOL-dSafePassage-21 TOOL-dSafePassage-22 TOOL-dSafePassage-23 TOOL-dSafePassage-24 TOOL-dSafePassage-25 TOOL-dSafePassage-26 TOOL-dSafePassage-27 TOOL-dSafePassage-28 TOOL-dSafePassage-29 TOOL-dSafePassage-30 TOOL-dSafePassage-31 TOOL-dSafePassage-32 TOOL-dSafePassage-33 TOOL-dSafePassage-34 TOOL-dSafePassage-35 TOOL-dSafePassage-36 TOOL-dSafePassage-37 TOOL-dSafePassage-38 TOOL-dSafePassage-39 TOOL-dSafePassage-40 TOOL-dSafePassage-41 TOOL-dSafePassage-42 TOOL-dSafePassage-43 TOOL-dSafePassage-44 TOOL-dSafePassage-45 TOOL-dSafePassage-46 TOOL-dSafePassage-47 TOOL-dSafePassage-48 TOOL-dSafePassage-49 TOOL-dSafePassage-50 TOOL-dSafePassage-51 TOOL-dSafePassage-52 TOOL-dSafePassage-53 TOOL-dSafePassage-54 TOOL-dSafePassage-55 TOOL-dSafePassage-56 TOOL-dSafePassage-57 TOOL-dSafePassage-58 TOOL-dSafePassage-59 TOOL-dSafePassage-61 TOOL-dSafePassage-62 TOOL-dSafePassage-63 TOOL-dSafePassage-65 TOOL-dSafePassage-66 TOOL-dSafePassage-67 TOOL-dSafePassage-68 TOOL-dSafePassage-69 TOOL-dSafePassage-70 TOOL-dSafePassage-71 |

<!-- /gen:spec-records -->

## 1. Goal

TOOL-dSafePassage-5's third build pass (`wf_0d024041-1eb`, HEAD `29665dd17`) walked a release-0
install whose `tools/hooks/README.md` the adopter had edited, up to a tip that no longer ships it and
back down to the pin. The walk up recorded the row `retired-edited`, as TOOL-dSafePassage-9 S2 asks.
The rollback to the pin, where gov ships the file again as `engine`, left the row `retired-edited`,
so the rolled-back receipt is not release-0's. The state is sticky in every direction gov re-ships a
path, forward too: the row is ordered on every run and gov's new bytes never reach it until `apply`
re-records it, the round-1 spec audit's D-42 (id 67), which TOOL-dSafePassage-26 S39 carried at
order 6 and which moves here, before unit 5.

## 2. Scope (IN)

- **S1** — The return. In `_cmd_update`'s role re-resolution (`tools/govkit/govkit.py:10126-10143`),
  a row whose recorded role is `retired-edited`, and for whose path the `--to` resolution names a
  role whose `UPDATE_ROLE` disposition is not in `KIT_WRITING_DISPOSITIONS` (`:8797`), takes that
  role as its own and is dispatched under it in the same run, with no `--accept-role-moves`. Its
  `path`, `source`, `commit`, `gov_oid` and `kit` are left as they are, so the verdict grid classifies
  it from them as any row of that role. Under `--write` the receipt records the role. A row the
  resolution names nothing for, or a role whose disposition is `adopter`, is handled as today.
  **Readers:** by name: `_cmd_update` in `tools/govkit/govkit.py`, which spells the role in its
  ordered arm and in this branch · by value: `UPDATE_ROLE` in `tools/govkit/govkit.py`, whose row the
  returned role selects for the dispatch. Observed by AC1.
- **S2** — The plant. `tools/govkit/fixtures/retired_edits.py` gains `edited-reshipped`: the
  `edited-gone` setup, its first `update --write` committed, then gov ships `gone.txt` again with the
  bytes it held at `A`, and `update --write` runs again. Observed by AC1.
- **S3** — The docs. The section "A file you edited that gov stopped shipping" of
  `help/update-edits.md` says that the row keeps the role until gov ships the file again, when it
  returns to the role gov's kit gives it and is graded as any file of that role. Observed by AC2.

## 3. Non-goals (OUT)

- A row whose adopter reverts the edit while gov still does not ship the file. It stays as
  TOOL-dSafePassage-9 §3 leaves it, `withdrawn` and reported, until `apply`.
- A return into a role whose disposition is `adopter`. That role's regenerate writes the destination
  in the same run, so returning the row there would write over the edit with no conflict
  (DEPL-cMendedVintage-27 S1, the comment at `:10157-10171`); it keeps today's note.
- An order for a row that returns with no conflict. The grid's `patched` keeps the bytes and asks
  nothing of the adopter; a moved gov side grades `diverged` and reaches the three-way, whose conflict
  writes its own order (`:11350-11358`), the audit fix's "conflict candidate".
- The upgrade-walk leg and its `down` case, which TOOL-dSafePassage-5 owns.

### Edges

- **hands-off** `TOOL-dSafePassage-5` — the `down` and `reup` cases' receipt over the `withdraw-one` plants, whose `tools/hooks/README.md` row reads `engine` again after the rollback to the pin

Read and closed, so named here rather than joined: TOOL-dSafePassage-9's `retired-edited` role, the
ordered arm that sets it (`:11040-11041`) and its `edited-gone` plant. TOOL-dSafePassage-26 gives up
S39 and AC38 to this unit and names no edge, since this unit takes nothing from it and builds first.

## 4. Design

### Why the role stuck

At the rollback, the receipt row reads `role: retired-edited`. The re-resolution resolves the pin's
descriptor, which ships the path as `engine`, so `now` is `engine` and differs (`:10141-10143`). The
run writes but takes no role moves, and `table`, `engine`'s disposition, is not kit-writing, so the
row is counted `role-moved` and skipped (`:10207-10217`): the role stays as recorded until `apply`,
as DEPL-cMendedVintage-19 S2 rules for a role a descriptor moved. That rule is right for a role a
descriptor declared, which is a fact about the vintage the row landed at. `retired-edited` is not one:
no descriptor declares it (TOOL-dSafePassage-9 §4), and only the write loop sets it, on the verdict
the grid gives where gov holds no blob at the row's `source` (`VERDICT_GRID`, `:8650`; `classify_row`,
`:9131-9133`). Once gov holds one again, the state's one premise is false.

### The return

```
role re-resolution, per row:
  role == "retired-edited" and now and UPDATE_ROLE[now] not in KIT_WRITING_DISPOSITIONS:
      row["role"] = role = now; how = UPDATE_ROLE[now]     # dispatched under it below
  otherwise                                               # unchanged
```

The fields TOOL-dSafePassage-9 §4 step 4 kept are the row's vintage evidence, so the grid needs no
re-attribution. The ordered arm moves no field but the role (`:11040-11042`) and reaches none of the
arms that stamp `commit` (`:11122`, `:11267`, `:11408`), so at the rollback `commit` and `gov_oid`
still name the pin's blob, gov's bytes at the pin equal them, and the target's index differs by the
edit: `patched`, the edit kept, nothing written. Over a re-ship with moved bytes the row grades `diverged` and the
three-way merges or orders. A kit gov retired is carried to its successor before this loop
(`:9640-9667`), so a `[[retired]]` successor's descriptor is the one resolved.

### Inventory

Minted: the fixture plant `edited-reshipped` in `tools/govkit/fixtures/retired_edits.py`. No
function, verdict, role, conf key, gate leg, policy key or receipt field.

### Migration

None. A receipt holding a `retired-edited` row whose path gov ships again gets its role back on its
next `update --write`; every other row is untouched.

### Rollout

Live at landing, in order 5 beside TOOL-dSafePassage-5, which consumes it and builds after it.

### Files touched (estimate)

- `tools/govkit/govkit.py`
- `tools/govkit/fixtures/retired_edits.py`
- `tools/govkit/selftest.py`
- `help/update-edits.md`

### Alternatives rejected

- **Read the role as output in TOOL-dSafePassage-5's compare.** No record declares a row's role
  output or re-derived per run, and the sticky row loses gov's later bytes in the field; a defect is
  not a normalization.
- **The `role-recorded` branch, taken without the flag.** It re-attributes the row and drops its
  `commit`, `gov_oid` and `carry` (`:10172-10206`), a different row from the one release-0 holds,
  for a vintage the kept fields already name.
- **Edit TOOL-dSafePassage-9.** It is CLOSED; this unit extends its role as the seam.

## 5. Production-readiness checklist

- security: no new write path; the row then takes its role's existing arms, each already guarded.
- perf / scale: one comparison per row in a loop that already resolves its role.
- error / empty / loading states: a row the resolution names nothing for is unchanged.
- observability: the row's verdict line prints under its returned role.
- risks: a return into a writing disposition would lose the edit, so `adopter` is excluded (§3).
- testing: the `edited-reshipped` plant through the arm of §7.
- migration: none.
- user docs: `help/update-edits.md` (S3).

## 6. Acceptance criteria

- **AC1** — When `python "tools/govkit/fixtures/retired_edits.py" --plant edited-reshipped` runs, it
  exits 0: the first run's verdict `retired-edited`, then after gov ships the file again the verdict
  `patched`, the receipt role `engine`, no second `update-retired-edited-` order, and the edited
  bytes kept.
  Red when: the role stays `retired-edited` while gov ships the path, as the re-resolution without
  the return leaves it.
- **AC2** — When `git grep -n -e "ships the file again" -- help/update-edits.md` runs, it prints the
  section's sentence, and `python "tools/govkit/docs_leg.py"` exits 0.
  Red when: the page still says every later run treats the row the same way.

## 7. Gates

`govkit selftest` · `govkit refusal join` · `govkit acceptance matrix` · `govkit selfcheck` · `recall floor arms` · `policy fixtures` · `encoding posture (text IO names its encoding)` · `lexicon naming predicates` · `docs` · `memory hygiene` · `spec tokens (a spec's own names resolve)`

New arm: tools/govkit/selftest.py · covers AC1 · the `_rte_cases` rows (`tools/govkit/selftest.py:18329-18337`) gain `edited-reshipped`, its failing case staged by the return taken out of a working copy · none

## 8. Open questions

- **F1 — How this unit binds to the clause.** As TOOL-dSafePassage-63 §8 F2: a third carrier of
  `cl-dClosedLoop-0022` reds the carries join until CLOSED TOOL-dSafePassage-62's `part 2/2` moves.
  Options: (a) carry a part and leave 62's line to the main loop; (b) bind
  `**Derived:** TOOL-dSafePassage-5`. RESOLVED (agent, 2026-10-27, delegated): (b), rung 1, the
  brief's non-goal on CLOSED specs. widens: none · relaxes: none

## 9. Revision log

- rev-1 · 2026-10-27 · initial draft, from TOOL-dSafePassage-5's third build-pass measurement of a
  `retired-edited` role left after a rollback to the pin, taking TOOL-dSafePassage-26 S39 and AC38, by
  `2026-10-27-prompt-TOOL-dSafePassage-5-6-spec-writer.md`.

## 10. Reuse audit

The seam extended is the role re-resolution of `_cmd_update` (`tools/govkit/govkit.py:10126-10143`,
DEPL-cMendedVintage-19 S1), which already resolves every row's role at `--to`, and TOOL-dSafePassage-9's
`retired-edited` role and `edited-gone` plant, whose setup the new plant reuses. `python
tools/codebase-map/reuse_lookup.py "return a receipt row to the role gov's descriptor resolves once gov
ships its path again"` ranked `rows`, `row`, `resolve`, `resolve_entry` and `read_descriptors`:
`resolve_entry` is the resolver the re-resolution already calls, and no other seam moves a receipt
role. The recall probe found the round-1 audit's D-42 and its `edited-reshipped` plant, the fix this
unit builds, and DEPL-cMendedVintage-27, which keeps a move into a rendered role on its landed role.

Recall terms used: `python tools/memory-recall/query.py "what happens to a retired-edited row when gov ships the file again or a rollback returns to an older vintage" --terms "retired-edited role re-resolution role-moved reshipped rollback descriptor sticky state apply re-records"`
