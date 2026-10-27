# TOOL-dLinkedLibrary-60 — `propose` reads the call unit 19 spells, filing each seam as the part `<feature>.<n>` before that unit's pass

**Status:** OPEN · rev-2 · 2026-10-27 · node d · Tier-2 · base 5fede642 · streams tooling · order 9 · advances TOOL-dLinkedLibrary-26

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-26-build-TOOL-dLinkedLibrary-1-agent-ledger.md](../build/2026-10-26-build-TOOL-dLinkedLibrary-1-agent-ledger.md) | journal | TOOL-dLinkedLibrary-1 TOOL-dLinkedLibrary-2 TOOL-dLinkedLibrary-3 TOOL-dLinkedLibrary-4 TOOL-dLinkedLibrary-5 TOOL-dLinkedLibrary-6 TOOL-dLinkedLibrary-7 TOOL-dLinkedLibrary-8 TOOL-dLinkedLibrary-9 TOOL-dLinkedLibrary-10 TOOL-dLinkedLibrary-11 TOOL-dLinkedLibrary-12 TOOL-dLinkedLibrary-13 TOOL-dLinkedLibrary-14 TOOL-dLinkedLibrary-15 TOOL-dLinkedLibrary-16 TOOL-dLinkedLibrary-17 TOOL-dLinkedLibrary-18 TOOL-dLinkedLibrary-19 TOOL-dLinkedLibrary-20 TOOL-dLinkedLibrary-21 TOOL-dLinkedLibrary-22 TOOL-dLinkedLibrary-23 TOOL-dLinkedLibrary-24 TOOL-dLinkedLibrary-25 TOOL-dLinkedLibrary-37 TOOL-dLinkedLibrary-38 TOOL-dLinkedLibrary-39 TOOL-dLinkedLibrary-40 TOOL-dLinkedLibrary-41 TOOL-dLinkedLibrary-42 TOOL-dLinkedLibrary-43 TOOL-dLinkedLibrary-44 TOOL-dLinkedLibrary-45 TOOL-dLinkedLibrary-46 TOOL-dLinkedLibrary-47 TOOL-dLinkedLibrary-48 TOOL-dLinkedLibrary-49 TOOL-dLinkedLibrary-50 TOOL-dLinkedLibrary-51 TOOL-dLinkedLibrary-52 TOOL-dLinkedLibrary-53 TOOL-dLinkedLibrary-54 TOOL-dLinkedLibrary-55 TOOL-dLinkedLibrary-56 TOOL-dLinkedLibrary-57 TOOL-dLinkedLibrary-58 TOOL-dLinkedLibrary-59 TOOL-dLinkedLibrary-61 TOOL-dLinkedLibrary-62 TOOL-dLinkedLibrary-63 TOOL-dLinkedLibrary-64 TOOL-dLinkedLibrary-65 TOOL-dLinkedLibrary-66 TOOL-dLinkedLibrary-67 TOOL-dLinkedLibrary-68 TOOL-dLinkedLibrary-69 TOOL-dLinkedLibrary-70 TOOL-dLinkedLibrary-71 TOOL-dLinkedLibrary-72 TOOL-dLinkedLibrary-73 TOOL-dLinkedLibrary-74 TOOL-dLinkedLibrary-75 TOOL-dLinkedLibrary-76 TOOL-dLinkedLibrary-77 TOOL-dLinkedLibrary-78 TOOL-dLinkedLibrary-79 TOOL-dLinkedLibrary-80 TOOL-dLinkedLibrary-81 TOOL-dLinkedLibrary-82 TOOL-dLinkedLibrary-83 TOOL-dLinkedLibrary-84 TOOL-dLinkedLibrary-85 TOOL-dLinkedLibrary-86 TOOL-dLinkedLibrary-87 TOOL-dLinkedLibrary-88 TOOL-dLinkedLibrary-89 TOOL-dLinkedLibrary-90 TOOL-dLinkedLibrary-91 TOOL-dLinkedLibrary-92 TOOL-dLinkedLibrary-93 TOOL-dLinkedLibrary-94 TOOL-dLinkedLibrary-95 TOOL-dLinkedLibrary-96 TOOL-dLinkedLibrary-97 TOOL-dLinkedLibrary-98 TOOL-dLinkedLibrary-99 TOOL-dLinkedLibrary-100 TOOL-dLinkedLibrary-101 TOOL-dLinkedLibrary-102 |
| [2026-10-27-build-TOOL-dLinkedLibrary-54-promoted-fix-return.md](../build/2026-10-27-build-TOOL-dLinkedLibrary-54-promoted-fix-return.md) | research | TOOL-dLinkedLibrary-54 TOOL-dLinkedLibrary-55 TOOL-dLinkedLibrary-56 TOOL-dLinkedLibrary-57 TOOL-dLinkedLibrary-58 TOOL-dLinkedLibrary-59 TOOL-dLinkedLibrary-62 TOOL-dLinkedLibrary-63 TOOL-dLinkedLibrary-64 TOOL-dLinkedLibrary-16 TOOL-dLinkedLibrary-20 |
| [2026-10-27-build-TOOL-dLinkedLibrary-60-deviation-601.md](../build/2026-10-27-build-TOOL-dLinkedLibrary-60-deviation-601.md) | deviation | — |
| [2026-10-27-prompt-TOOL-dLinkedLibrary-54-promoted-fix-brief.md](../prompts/2026-10-27-prompt-TOOL-dLinkedLibrary-54-promoted-fix-brief.md) | research | TOOL-dLinkedLibrary-54 TOOL-dLinkedLibrary-55 TOOL-dLinkedLibrary-56 TOOL-dLinkedLibrary-57 TOOL-dLinkedLibrary-58 TOOL-dLinkedLibrary-59 TOOL-dLinkedLibrary-62 TOOL-dLinkedLibrary-63 TOOL-dLinkedLibrary-64 TOOL-dLinkedLibrary-16 TOOL-dLinkedLibrary-20 |
| [2026-10-27-review-TOOL-dLinkedLibrary-54-spec-audit.md](../reviews/2026-10-27-review-TOOL-dLinkedLibrary-54-spec-audit.md) | spec-audit | TOOL-dLinkedLibrary-54 TOOL-dLinkedLibrary-55 TOOL-dLinkedLibrary-56 TOOL-dLinkedLibrary-62 TOOL-dLinkedLibrary-61 TOOL-dLinkedLibrary-63 TOOL-dLinkedLibrary-57 TOOL-dLinkedLibrary-58 TOOL-dLinkedLibrary-59 TOOL-dLinkedLibrary-64 |

<!-- /gen:spec-records -->

## 1. Goal

The spec audit of units 37 to 53
(`memory/builds/dLinkedLibrary/reviews/2026-10-27-review-TOOL-dLinkedLibrary-37-spec-audit.md`) confirmed
finding **id 2 at HIGH**, report item **H4**. No other id shares the item.

`TOOL-dLinkedLibrary-19` (order 10) files each of the 82 `seam:` lines through `python reuse_entries.py
propose --feature <feature> --name <feature>-<ordinal> … --unit TOOL-dLinkedLibrary-19` (its S3), and runs
that over every dossier at its own pass (S6). `TOOL-dLinkedLibrary-1` (order 8) builds `--feature` as a
bare flag (its S3), so that call does not parse. The repair, `TOOL-dLinkedLibrary-38`, sits at order 11,
after the pass it repairs: unit 19's migration fails at its own pass, or its builder improvises an
interface; and where proposals are filed under the hyphenated name, 38's S4 must reject and re-file all
82, with an AC5 that counts rejections and never the live re-files.

This unit changes the verb unit 19 calls, at the step after the unit that builds it: `propose` reads the
valued `--feature <feature>` and the name `<feature>-<n>` as the part `<feature>.<n>`, the part shape 38
settles. Unit 19's migration then parses and files every seam as its own part from the start, and 38's
S4 finds no hyphenated proposal to re-file. It repairs `TOOL-dLinkedLibrary-1`'s `propose`, so it builds
one step after that unit (order 9), the one position that precedes unit 19's pass.

## 2. Scope (IN)

- **S1** — The valued flag. `reuse_entries.py propose` (`TOOL-dLinkedLibrary-1` S3) takes `--feature`
  with an optional value. Bare, it behaves as unit 1 builds it. Valued `--feature <feature>`, the `--name`
  must be `<feature>`, `<feature>.<n>` or `<feature>-<n>`, `<n>` a positive integer with no leading zero;
  `<feature>.<n>` and `<feature>-<n>` both name the part `<feature>.<n>`. Any other name exits 2 naming
  the name and the feature, and writes nothing. Observed by AC1 and AC2.
- **S2** — The part composed. For the part `<feature>.<n>`, the composed file is
  `memory/map/features/<feature>.<n>.reuse.toml`, its `[[unit]]` tag `unit.reuse.<feature>.<n>` and its
  `reuse.tag` `feature.<feature>`, the shapes `TOOL-dLinkedLibrary-38` S1 checks. Observed by AC1.
- **S3** — The record. The proposal record for the part `<feature>.<n>` is
  `<date>-build-<unit id>-reuse-proposal-<feature>-<n>.md`, the dot spelled as a hyphen because the
  record-name tail admits none (`REC_TAIL`, `tools/memory-tree/check-memory-hygiene.sh:577`); its body
  names the part `<feature>.<n>`. `propose` exits 2 naming an existing record of that name and writes
  nothing. Observed by AC3.
- **S4** — Unit 19's call as spelled. The `--fixture` plant `seam-call` runs the call
  `TOOL-dLinkedLibrary-19` S3 spells, `propose --feature alpha --name alpha-1 --text "MUST reuse x" --need
  y --anchor "gov:feature alpha" --build <slug> --unit <id>`, in a scratch tree holding `alpha.md`, and
  reads the part `alpha.1`. Observed by AC1.

## 3. Non-goals (OUT)

- `check_reuse_entries`'s reading of a numbered part: `TOOL-dLinkedLibrary-38` S1, at order 11, before any
  owner accepts a proposal.
- `dossier_move.py`'s call: `TOOL-dLinkedLibrary-19`'s, which spells the valued form this unit admits, and
  `TOOL-dLinkedLibrary-38` S3's re-spelling of it.
- `accept`, `reject` and `owed`: unit 1's, unchanged.

### Edges

- **consumes-from** `TOOL-dLinkedLibrary-1` — `propose` and `--feature`, the verb and flag S1 widens (id 2)
- **hands-off** `TOOL-dLinkedLibrary-19` — `propose`, which reads S3's `<feature>-<ordinal>` call as the part `<feature>.<n>` from this unit on, so the migration of S6 parses (id 2)
- **hands-off** `TOOL-dLinkedLibrary-38` — `<feature>.<n>`, the part name unit 19's migration files from the start, so S4 finds no hyphenated proposal to re-file; and S2's record name, which this unit lands first (id 2)
- **hands-off** `TOOL-dLinkedLibrary-74` — `propose`'s duplicate refusal and its tag, which unit 74 completes (ids 7, 6 of the spec audit of units 54 to 64)

## 4. Design

### Evidence

- `TOOL-dLinkedLibrary-1` S3: `propose --name <n> (--feature | --convention)`, both bare flags, writing
  `<date>-build-<unit id>-reuse-proposal-<n>.md`.
- `TOOL-dLinkedLibrary-19` S3: `propose --feature <feature> --name <feature>-<ordinal> … --build
  dLinkedLibrary --unit TOOL-dLinkedLibrary-19`; S6 runs `apply` at that unit's pass.
- `TOOL-dLinkedLibrary-38` S1 and S2: the part `<feature>.<n>.reuse.toml`, keyed by the stem before its
  first dot, and its record `…-reuse-proposal-<feature>-<n>.md`.
- `tools/memory-tree/check-memory-hygiene.sh:577`: `REC_TAIL='(-[a-z0-9][a-z0-9-]*)?'`.

### The names after S1 to S3

| Call | Part | Record tail |
|---|---|---|
| `--feature --name roles` | `roles` | `-reuse-proposal-roles` |
| `--feature roles --name roles-1` | `roles.1` | `-reuse-proposal-roles-1` |
| `--feature roles --name roles.1` | `roles.1` | `-reuse-proposal-roles-1` |
| `--feature roles --name tags-1` | refused, exit 2 | none |

### Why the order is 9

The defect is an ordering one: the verb unit 19 calls must parse before unit 19's pass at order 10. A
promotion builds one step after the unit it repairs, and the unit whose interface this changes is unit 1
at order 8, so order 9 closes the defect at the next step. Re-ordering unit 38 itself would edit another
unit's status header, a fold BUILD-METHOD M4 refuses.

### Files touched (estimate)

- `tools/memory-tree/reuse_entries.py`: S1 to S3, and the `seam-call` plant of S4

### Alternatives rejected

- **Leave `propose` as unit 1 builds it.** Unit 19's S6 fails at its pass, which is the finding.
- **Re-file at unit 38's pass, as 38's S4 writes it.** The re-filed record collides with the rejected one
  (id 25 of the same audit), and a pass that rejects and re-files none reads green.

## 5. Production-readiness checklist

- security — no new write path: `propose` writes one record under the named build, as before.
- perf / scale — one name split per call.
- error / empty / loading states — a name that disagrees with the feature, or an existing record, exits 2
  naming it and writes nothing.
- observability — `propose` prints the part name it composed.
- risks — an operator writes both spellings of one part; both resolve to one record name, and the second
  call refuses.
- testing — AC1 to AC3 by the module's fixture.
- migration — none: no proposal exists before unit 19's pass.
- user docs — none under `help/`: `propose`'s usage line names the valued form.

## 6. Acceptance criteria

- **AC1** — When `python reuse_entries.py --fixture --plant seam-call` runs, unit 19's
  call as spelled exits 0 and the record's fenced part names `alpha.1.reuse.toml`, tag
  `unit.reuse.alpha.1` and `reuse.tag` `feature.alpha`.
  Red when: the valued flag does not parse, or the part is read as the feature `alpha-1`.
- **AC2** — When the same plant runs `propose --feature alpha --name beta-1`, it exits 2 naming `beta-1`
  and `alpha`, and writes no record.
  Red when: a name that disagrees with its feature is filed.
- **AC3** — When the plant runs the S4 call twice, the first writes `…-reuse-proposal-alpha-1.md` and the
  second exits 2 naming it; `--name alpha.1` after it exits 2 naming the same record.
  Red when: a record name carries a dot, or a second call overwrites the first.

## 7. Gates

`memory hygiene` · `spec tokens (a spec's own names resolve)`

New arm: tools/memory-tree/reuse_entries.py · covers AC1 AC2 AC3 · the `seam-call` plant with its disagreeing name and repeated call, the failing case staged by unit 1's bare-only `--feature` · none

## 8. Open questions

- **F1 — Which binding line does a unit the spec audit promoted carry?** Options: (a) `**Derived:**`
  naming `PLAY-dClosedLoop-2`; (b) a `part k/n` carry of the repaired unit's clause. (b) splits a clause
  unit 1 carries whole; veto 1 discards it. RESOLVED (agent, 2026-10-27, delegated): (a), rung 3, the
  precedent `TOOL-dTotalRecall-40` set for this chain. widens: none · relaxes: none
- **F2 — How does unit 19's call parse at its own pass?** Options: (a) `propose` admits the valued
  `--feature` beside the bare flag, with a refusal for a disagreeing name, landed at order 9; (b) unit 38
  re-ordered ahead of unit 19; (c) unchanged, with 38's re-file. (b) edits another unit's header, a fold
  M4 refuses (veto 2, the build method's own rule); (c) fails unit 19's AC7 at its pass (veto 1). Unit 38
  rejected (a) for spelling the feature twice; S1's refusal answers that cost. RESOLVED (agent, 2026-10-27,
  delegated): (a), rung 3, the one survivor. widens: none · relaxes: none

## 9. Revision log

- rev-1 · 2026-10-27 · initial draft, promoted from the spec audit of units 37 to 53, id 2 (HIGH, item
  H4).
- rev-2 · 2026-10-27 · §3 · the Edges block gains the bullets mirroring TOOL-dLinkedLibrary-74, promoted from the spec audit of units 54 to 64; nothing else moved.

## 10. Reuse audit

The seam extended is `TOOL-dLinkedLibrary-1`'s `propose` and its `--fixture` harness in
`tools/memory-tree/reuse_entries.py`; the part grammar is `TOOL-dLinkedLibrary-38`'s and the record tail
`REC_TAIL`, neither minted again. `python tools/codebase-map/reuse_lookup.py "accept a valued flag that
names the feature of a reuse proposal"` ranked `read_host_name`, `outcome_accepted` and `read_conf_value`,
none a proposal-name reader, so no existing seam fits beyond the verb being widened.

Recall terms used: `python tools/memory-recall/query.py "how does a promoted high finding repair a spec-audited unit at the next order step" --terms "spec-audit promoted high finding repairs order inline parity block tree-kill witness before-image"`
