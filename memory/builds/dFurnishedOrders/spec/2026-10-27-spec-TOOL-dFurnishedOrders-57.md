# TOOL-dFurnishedOrders-57 — unit 50's reach read from the spec-token checker itself: the `govkit selftest <- ` tokens its `[guards]` rows print over the whole resolved guard, and every waiver row keyed to one of them

**Status:** OPEN · rev-1 · 2026-10-27 · node d · Tier-2 · base 5647189e · streams tooling · order 29 · advances TOOL-dFurnishedOrders-21

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

*No record names this unit.*

<!-- /gen:spec-records -->

## 1. Goal

The spec audit of the round-6 promotions
(`memory/builds/dFurnishedOrders/reviews/2026-10-27-review-TOOL-dFurnishedOrders-50-spec-audit-round1.md`)
confirmed finding **id 23 at HIGH**, report item **H2**. No other id shares that item.

`TOOL-dFurnishedOrders-50` S3 limits its reach to paths that trip "a `govkit selftest` home row". Its
own §4 defines the guard as the home rows plus unit 48's S14 descriptor rows and S18 flat-source rows.
The checker names a spec's first declared path that trips ANY joined guard of the leg
(`tools/check-spec-tokens.py:1613-1618`). With S18's rows for the flat `kickoff-manifest` entry
(`tools/govkit/entries/kickoff-manifest.kit.toml:5`), the skeptic's re-run printed
`govkit selftest <- skills/session-kickoff/manifest-check.sh` for DEPL-aScoutedSeam-1 and
`govkit selftest <- skills/session-kickoff/SKILL.md` for KICK-aScoutedSeam-1. Unit 50's §4 table keys
`tools/unattended/.unattended.conf.example` and `tools/unattended/VERBS.template.md` instead. Rows keyed
that way waive nothing and go stale, which reds (`memory/project/spec-token-waivers.txt:3-5`), while
the real hits stay unwaived. Unit 50's AC3 re-derives the population by S3's rule, so it reads green
while the checker reds.

This unit makes the checker's own output the reach. It repairs unit 50 and builds one step after it
(order 29).

## 2. Scope (IN)

- **S1** — The reach is what the checker prints. The population is every `[guards]` row that
  `python tools/check-spec-tokens.py --list` prints, as `HIT` or `WAIVED`
  (`tools/check-spec-tokens.py:1733-1734`), whose token starts `govkit selftest <- `. The checker reads
  the leg's whole resolved guard: the home rows, unit 48's S14 and S18 rows and the rows already there.
  The token is taken as printed, never re-derived by a probe. Observed by AC1.
- **S2** — Every waiver row keyed to a printed token. Each row of
  `memory/project/spec-token-waivers.txt` whose token starts `govkit selftest <- ` carries a token S1
  prints for another build's spec, and each such token has one row. A row keyed otherwise is
  re-keyed in place, its reason naming this unit, as the row at `:41` re-keyed one for
  TOOL-dGroundRules-67. Observed by AC1 and AC2.
- **S3** — The table at authoring, re-keyed. The tokens the guard's reach printed in the skeptic's
  re-run, PINNED from the report's id 23 verdict (2026-10-27), are the §4 table below. The pass reads
  S1 again on its tip. Observed by AC1.
- **S4** — The asks and the record follow the reach. Unit 50 S5's ask for each other build names every
  spec S1 reaches in that build. A build S1 reaches that holds no ask gains one, with its `SEV` and
  `KEEP` rows in unit 50 S5's grammar. Where S1's row count exceeds the count unit 50's deviation 501
  records, this pass writes `2026-10-27-build-TOOL-dFurnishedOrders-57-deviation-571.md` in that
  record's grammar, naming the rise. Observed by AC3.
- **S5** — Keyed at unit 50's own pass. Before the build run's first code pass, M2's cross-read
  (`memory/guides/BUILD-METHOD.md:66-71`) holds unit 50 S3 and S5 to S1 and S2. So unit 50's pass keys
  its rows by S1's tokens. Where it did, this unit's pass records that in its ledger. Where it did
  not, this pass re-keys them (S2). §4 "Rollout" states why the first branch is the one that runs.
  Observed by AC1.

## 3. Non-goals (OUT)

- Revising another build's spec. The README refuses that write, so outside this build this unit
  writes only ask rows, as unit 50 S5 does.
- Which homes the guard holds, and whether the broad set moves: unit 50 S1 and S2.
- AC2's and S3's other re-typings (the broad-set count and the join's reader): the minors batch
  `TOOL-dFurnishedOrders-58` (id 19), which reads S1's population.
- The report's left-shift gate (a spec-lint on waiver rows proposed without a `--list` run): no
  clause of this build names it.
- Where a landed criterion of unit 50 cannot hold as written, its ledger answers it AMENDED, naming
  this unit.

### Edges

- **consumes-from** `TOOL-dFurnishedOrders-50` — S3's reach, S5's waiver rows and asks and AC3, whose population S1 reads from the checker and whose keys S2 holds to its tokens (id 23)
- **hands-off** `TOOL-dFurnishedOrders-58` — S1's population, the checker's printed `govkit selftest <- ` tokens, which unit 58 reads for unit 50 AC3 and for the reach of the `govkit selftest` row it adds (ids 23, 19 and 24)

## 4. Design

### The reach, after this unit

```
reach   := [(spec, token) for each `spec-tokens: HIT|WAIVED [guards] <spec> :: <token> — ...`
            line of `check-spec-tokens.py --list`, token starting "govkit selftest <- "]   S1
waivers := rows of spec-token-waivers.txt whose token starts "govkit selftest <- "
require   {token of reach on another build's spec} == {token of waivers}               S2
```

### The reach at authoring, re-keyed (S3)

| reached spec | composite token |
|---|---|
| `memory/builds/aOrientedCast/spec/2026-10-13-spec-TOOL-aOrientedCast-28.md` | `govkit selftest <- tools/workflows/unattended-build.template.js` |
| `memory/builds/aScoutedSeam/spec/2026-10-11-spec-DEPL-aScoutedSeam-1.md` | `govkit selftest <- skills/session-kickoff/manifest-check.sh` |
| `memory/builds/aScoutedSeam/spec/2026-10-11-spec-KICK-aScoutedSeam-1.md` | `govkit selftest <- skills/session-kickoff/SKILL.md` |
| `memory/builds/aScoutedSeam/spec/2026-10-11-spec-TOOL-aScoutedSeam-3.md` | `govkit selftest <- tools/workflows/reuse-scout.js` |

Each of the four lists its token's path first among its declared paths, which this unit read in each
spec's `### Files touched` at `5647189e`.

### What it does not check

- A spec that writes under a guarded path and never declares it. The join reads Files touched as
  written (`tools/check-spec-tokens.py:99-100`), and so does S1.
- This build's own specs. Unit 50 S4 gives them the leg rather than a waiver row.

### Inventory

Minted: one BACKLOG ask id per other build S1 reaches that unit 50's asks do not cover, the next
free `TOOL-dFurnishedOrders` ids, and the deviation record of S4 where the count rises. None at
authoring: the four specs sit in the two builds unit 50 S5 already asks.

### Migration

Re-keying keeps the row count, as the precedent at `memory/project/spec-token-waivers.txt:41` does.

### Rollout

Live at landing, at order 29, beside unit 52. The only reader between unit 50's pass and this one is
`--dispatch`, which runs the spec-token checker over the live tree and refuses on a red
(`tools/unattended/unattended.sh:13670-13683`). A unit 50 pass that keyed its rows by its own S3 would
red it, and `--dispatch` would then refuse every unit at order 29, this one included. That is why S5
places the keying at unit 50's pass through M2's cross-read, before any code is written.

### Files touched (estimate)

- `memory/project/spec-token-waivers.txt`
- `memory/builds/dFurnishedOrders/BACKLOG.md`
- `memory/builds/dFurnishedOrders/build/2026-10-27-build-TOOL-dFurnishedOrders-57-deviation-571.md`
  (only where S4's count rises)
- `memory/builds/dFurnishedOrders/README.md` and `memory/backlog/TOOL.md` (regenerated by the
  memory-tree kit's build index generator with `--write`, only where S4 mints an ask id)

### Alternatives rejected

- **Widen unit 50 S3's own rule to every row of the guard.** It is still a second copy of the join,
  which can drift from the leg it certifies, as the report's id 19 measured.
- **Key the rows by every tripping path of each spec.** The join names one path per missing leg, so
  every other row goes stale and reds.

## 5. Production-readiness checklist

- security — no surface moves. The waiver rows widen a declared registry under unit 50's recorded
  ruling, and S4 records any rise.
- perf / scale — one checker run per pass.
- error / empty / loading states — an empty reach leaves no `govkit selftest <- ` row, and S2 then
  requires none.
- observability — each waiver reason names its spec and this unit or unit 50.
- risks — a spec authored elsewhere after this pass enters the reach. The close's `spec tokens` leg
  names it, and the main loop disposes of it the same way.
- testing — AC1 to AC3 by checker runs and greps; no new suite arm.
- migration — none.
- user docs — none: no user-facing step changes.

## 6. Acceptance criteria

- **AC1** — When `python tools/check-spec-tokens.py` runs on the pass tip, it prints no line naming a
  `[guards]` token that starts `govkit selftest <- ` and no `STALE` line naming one. Under `--list`,
  each `WAIVED [guards]` line whose token starts `govkit selftest <- ` names a token that is a row of
  `spec-token-waivers.txt`.
  Red when: a waiver row is keyed to a token the checker never prints, or a printed token has no row.
  figure: 4 reached specs of other builds, PINNED from the report's id 23 verdict (2026-10-27); the
  pass's reach is DERIVED from the checker's output.
- **AC2** — When the same checker runs in a scratch clone of the tip with one `govkit selftest <- `
  row removed from `memory/project/spec-token-waivers.txt` and committed, it prints that token as an
  unwaived `[guards]` hit and exits 1. With one such row's path replaced by
  `tools/unattended/VERBS.template.md`, it prints that row as `STALE`.
  Red when: the criterion reads green while the checker reds.
  fixture: a scratch clone under `%TEMP%`.
- **AC3** — When `grep -n "govkit selftest" memory/builds/dFurnishedOrders/BACKLOG.md` runs, each other
  build AC1's reach names has an ask row naming every reached spec of that build.
  Red when: a reached spec carries a waived row that no ask will cure.

## 7. Gates

`spec tokens (a spec's own names resolve)` · `recall floor` · `recall floor arms` · `memory hygiene` · `lexicon naming predicates`

The close's `spec tokens` leg is the whole-tree reading of AC1.

## 8. Open questions

- **F1 — Where does unit 50's reach come from?** Options: (a) the checker's own `--list` rows; (b)
  unit 50 S3's probe, widened to every guard row; (c) unit 50 S3 as written. (c) keys tokens the
  checker never prints (the finding). (b) is a second copy of the join that can drift. (a) is the
  leg's own reading. RESOLVED (agent, 2026-10-27, delegated): (a), rung 3, the skeptic-judged fix of
  id 23 ("have AC3 run `check-spec-tokens.py` ... and grade its printed `[guards]` tokens"). widens:
  none · relaxes: none
- **F2 — When are the rows keyed?** Options: (a) at unit 50's pass, by M2's cross-read, with this
  pass re-keying as the fallback; (b) only at this pass. (b) leaves `--dispatch` red over order 29,
  this unit included (§4 "Rollout"). RESOLVED (agent, 2026-10-27, delegated): (a), rung 3, M2's
  sub-spec agreement rule and the precedent of `TOOL-dFurnishedOrders-52` S26, which places a write
  at an earlier unit's pass. widens: none · relaxes: none
- **F3 — Which binding line does a unit the spec audit promoted carry?** RESOLVED (agent,
  2026-10-27, delegated): `**Derived:**` naming `PLAY-dClosedLoop-2`, rung 3, the precedent
  `TOOL-dBoundRoles-39` §8 F1 records. widens: none · relaxes: none

## 9. Revision log

- rev-1 · 2026-10-27 · initial draft, promoted from the spec audit of the round-6 promotions, id 23
  (HIGH, item H2).

## 10. Reuse audit

The seams extended:

- The guards join and its `--list` rows (`tools/check-spec-tokens.py:1592-1618`, `:1733-1734`), the
  leg's own reading, for S1.
- The `[guards]` waiver grammar and its re-key precedent (`memory/project/spec-token-waivers.txt:3-5`,
  `:36-41`), for S2.
- Unit 50 S5's ask, SEV and KEEP rows, for S4.

`python tools/codebase-map/reuse_lookup.py "key a waiver row to the token the spec-token checker
prints for a guards hit"` ranked `rows`, `row`, `key` and `hit`, name-token neighbours none of which
reads the checker's tokens. The recall probe returned TOOL-dGroundRules-109 to -111, the deviation
records of TOOL-dGroundRules-18, -25 and -67 and TOOL-dTrueNorth-12, and TOOL-dGroundRules-67 §4,
whose re-key states the one-path-per-missing-leg rule S2 keys by. None disagrees with source.

Recall terms used: `python tools/memory-recall/query.py "how is a guard widening's reach keyed to
the spec-token checker's own printed tokens" --terms "guards join waiver row composite token first
tripping path list HIT WAIVED stale re-key spec-token-waivers"`
