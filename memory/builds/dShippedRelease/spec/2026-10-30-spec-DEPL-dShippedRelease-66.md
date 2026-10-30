# DEPL-dShippedRelease-66 — a retired leg stays resolvable for a live spec older than its retirement, by a row naming its successor

**Status:** OPEN · rev-1 · 2026-10-30 · node d · Tier-2 · base f4597719 · streams deployer · order 2 · advances DEPL-dShippedRelease-32

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-30-build-DEPL-dShippedRelease-1-agent-ledger.md](../build/2026-10-30-build-DEPL-dShippedRelease-1-agent-ledger.md) | journal | DEPL-dShippedRelease-1 DEPL-dShippedRelease-2 DEPL-dShippedRelease-3 DEPL-dShippedRelease-4 DEPL-dShippedRelease-5 DEPL-dShippedRelease-6 DEPL-dShippedRelease-7 DEPL-dShippedRelease-8 DEPL-dShippedRelease-9 DEPL-dShippedRelease-10 DEPL-dShippedRelease-11 DEPL-dShippedRelease-12 DEPL-dShippedRelease-13 DEPL-dShippedRelease-14 DEPL-dShippedRelease-15 DEPL-dShippedRelease-16 DEPL-dShippedRelease-17 DEPL-dShippedRelease-18 DEPL-dShippedRelease-19 DEPL-dShippedRelease-20 DEPL-dShippedRelease-21 DEPL-dShippedRelease-22 DEPL-dShippedRelease-23 DEPL-dShippedRelease-24 DEPL-dShippedRelease-25 DEPL-dShippedRelease-26 DEPL-dShippedRelease-27 DEPL-dShippedRelease-28 DEPL-dShippedRelease-29 DEPL-dShippedRelease-30 DEPL-dShippedRelease-31 DEPL-dShippedRelease-49 DEPL-dShippedRelease-50 DEPL-dShippedRelease-51 DEPL-dShippedRelease-52 DEPL-dShippedRelease-53 DEPL-dShippedRelease-54 DEPL-dShippedRelease-55 DEPL-dShippedRelease-56 DEPL-dShippedRelease-57 DEPL-dShippedRelease-58 DEPL-dShippedRelease-59 DEPL-dShippedRelease-60 DEPL-dShippedRelease-61 DEPL-dShippedRelease-62 DEPL-dShippedRelease-63 DEPL-dShippedRelease-64 DEPL-dShippedRelease-65 DEPL-dShippedRelease-67 DEPL-dShippedRelease-68 DEPL-dShippedRelease-69 DEPL-dShippedRelease-70 DEPL-dShippedRelease-71 DEPL-dShippedRelease-72 DEPL-dShippedRelease-73 DEPL-dShippedRelease-74 DEPL-dShippedRelease-75 DEPL-dShippedRelease-76 DEPL-dShippedRelease-77 DEPL-dShippedRelease-78 |

<!-- /gen:spec-records -->

## 1. Goal

Close finding id 58 of `reviews/2026-10-30-review-DEPL-dShippedRelease-1-spec-audit-round1.md`,
HIGH, item H10, which stands beside ids 5 and 40. `tools/check-spec-tokens.py:1548` hits any §7
token not in the manifest on a live spec, and unit 10 S9 and S10 retire sixteen legs. A join at this
base prints live specs of this build and of older builds naming them. The brief forbids editing a
foreign spec, `memory/project/spec-token-waivers.txt` is SHRINK-ONLY, and spelling the replacement
now is red as well, so unit 10 cannot land green as specified. This unit gives a retirement its own
record.

## 2. Scope (IN)

- **S1** — The record, `memory/project/ended-legs.txt`, one tab-separated row `<leg>`, `<ended-on>`,
  `<successor or none>`, `<retiring unit>` for each leg S9 and S10 of unit 10 end that a live spec's
  §7 names, derived at the pass by the join of §4. Its name joins `PROJECT_REGISTRY_EXTRA` in
  `.memory-tree.conf`. Observed by AC1.
- **S2** — The arm. `read_ended_legs(root)` in `tools/check-spec-tokens.py`, and the leg arm at
  `:1548`: a token not in the manifest, on a row, in a spec whose filename date is on or before that
  row's `ended-on`, counts as held and is no hit. A later spec naming the leg is a hit, so a new
  spec cannot lean on the row. Observed by AC1, AC2.
- **S3** — The line. Every run prints
  `spec-tokens: ended-leg join · <n> token(s) · <m> live spec(s) · <r> row(s)`, held tokens by name
  under `--list`, so the exception is never silent. Observed by AC1.
- **S4** — The refusals. A row naming a leg still in the manifest, a malformed date, a `<successor>`
  not in the manifest and not `none`, and a row no live spec produces each print as `ENDED` findings
  and red, as a stale waiver does. Observed by AC3.
- **S5** — The waiver file is untouched. Its SHRINK-ONLY header stands. Observed by AC4.

## 3. Non-goals (OUT)

- Editing a foreign spec's §7: the brief's rule, kept.
- The six sibling specs' lists: they are held by the rows, and review ids 5 and 40 are the minors
  batch's.
- A leg-factory `retire` step: the audit's left-shift item, which no clause of this build names.

### Edges

- **consumes-from** `DEPL-dShippedRelease-10` — S9 and S10, the sixteen retirements, and `kit version (one check)` and `kit wiring (every descriptor's check)`, the successors
- **hands-off** `DEPL-dShippedRelease-78` — `ended-legs.txt`, whose held tokens that unit reads for review ids 5 and 40

## 4. Design

### Evidence

- `tools/check-spec-tokens.py:1548` hits a §7 token outside the manifest, on specs at OPEN, SPECCED, INPROGRESS or BLOCKED (`:331`).
- A scratch join over tracked specs at this base printed 18 live specs with a retired leg on a list line, six of them units 1, 2, 4, 13, 14 and 15; the report's reading, with a looser line test, was 24. Both are PINNED at `f4597719`, and S1 re-derives the population.
- The waiver header says the count may fall, never rise.

### The join

For every leg S9 and S10 retire: every live spec whose list line in §7 holds that name. A leg with no such spec needs no row.

### Inventory

| Minted | Kind | Naming cell |
|---|---|---|
| `read_ended_legs` | function, `tools/check-spec-tokens.py` | `py.function`, OK by `--suggest` at writing |
| `memory/project/ended-legs.txt` | record file | none |

### Files touched (estimate)

- `tools/check-spec-tokens.py`: S2, S3, S4
- `memory/project/ended-legs.txt` (new): S1
- `.memory-tree.conf`: S1
- `tools/check-spec-tokens.test.sh`: the arm of §7
- `memory/map/features/spec-tokens.md`: the arm's sentence

## 5. Production-readiness checklist

- security — N/A — a read over tracked files.
- perf / scale — N/A — a read or a compare on a path that already runs once per landing.
- error / empty / loading states — the criteria of §6 name each refused and empty state.
- observability — the join's line on every run, and `--list` naming each held token.
- risks — a row goes stale when the last live spec naming its leg closes, and then reds an unrelated
  landing until the row is deleted, as a stale waiver does; the printed remedy names the row.
- testing — the criteria of §6 and the arm of §7.
- migration — N/A — the code it changes lands in this same build, so no installed state moves.
- user docs — N/A — a repo-root tool; `memory/map/features/spec-tokens.md` states the arm.

## 6. Acceptance criteria

- **AC1** — When `python tools/check-spec-tokens.py --list` runs on a scratch copy with the sixteen
  legs taken out of `tools/gate-legs.json` and the rows in place, it prints no `[leg]` hit on those
  names and prints `ended-leg join`.
  Red when: retiring a leg reds a live spec nobody may edit.
  cost: a full run of the checker, a minute on a Windows node.
- **AC2** — When the same copy holds a spec dated after a row's `ended-on` naming that leg, it
  prints a `[leg]` hit on that spec.
  Red when: a new spec can name a dead leg.
- **AC3** — When `ended-legs.txt` holds a row naming a leg still in the manifest, or a row no live
  spec names, the run prints `ENDED` and exits 1.
  Red when: a stale row hides a live hit, the rule the waiver file keeps.
- **AC4** — When `git diff --stat <base> -- memory/project/spec-token-waivers.txt` runs at the
  close, it prints nothing.
  Red when: the retirement grew the SHRINK-ONLY file after all.

## 7. Gates

`memory-hygiene self-test` · `kit/dogfood doc parity` · `build-index selftest` · `recall floor` · `recall floor arms` · `transition-audit arms` · `straggler-guard arms` · `policy fixtures` · `spec tokens (a spec's own names resolve)` · `memory hygiene`

New arm: tools/check-spec-tokens.test.sh · covers AC1 AC2 AC3 · a fixture manifest with one leg taken out and one row, its failing case the row read for a later spec · none

## 8. Open questions

- **F1 — How does a live spec survive a retirement it cannot be edited for?** Options: (a) a
  retirement record keyed to the date and the successor; (b) waiver rows; (c) editing the foreign
  specs; (d) keeping no-op legs in the manifest. (b) breaks the file's SHRINK-ONLY rule, (c) is
  refused by the brief, and (d) keeps gates that run nothing, which `[gate]` refuses. RESOLVED
  (agent, 2026-10-30, delegated): (a), rung 3, a route the audit names and no governance carrier
  moves. The audit asks an owner grant for a waiver route, and this option takes no waiver. widens:
  none · relaxes: none

## 9. Revision log

- rev-1 · 2026-10-30 · initial draft, promoted from review id 58 (HIGH, item H10) of the round-1 spec audit.

## 10. Reuse audit

The seam extended is the leg arm of `tools/check-spec-tokens.py`, and `read_waivers` at `:1216` is
the shape of the new reader.
`python tools/codebase-map/reuse_lookup.py "compare kit version markers with their constants"`
ranked no token registry, and a read of the checker found `read_waivers` the one exception reader.
`TOOL-dSafePassage-1`'s `[[retired]]` rows are the nearest idiom: they retire registry entries and
no leg, so they hold no row for this. The recall probe surfaced report item H10.

Recall terms used:
`python tools/memory-recall/query.py "which checks does check-kit-versions assert that a single version verb must carry" --terms "kit version markers epoch MANIFEST_FORMAT KIT_UNATTENDED_VERSION meta.version retired leg successor"`
