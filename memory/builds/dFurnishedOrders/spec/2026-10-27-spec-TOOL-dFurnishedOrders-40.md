# TOOL-dFurnishedOrders-40 — a receipt target's kit home is the kit's declared home under the target's prefix, never the directory of a receipt row, so a merged or seed row at the repo root widens nothing

**Status:** DEFERRED · rev-2 · 2026-10-27 · node d · Tier-2 · base 08e30fef · streams tooling · order 7 · advances TOOL-dFurnishedOrders-21

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-27-build-TOOL-dFurnishedOrders-38-round3-fix-return.md](../build/2026-10-27-build-TOOL-dFurnishedOrders-38-round3-fix-return.md) | research | TOOL-dFurnishedOrders-38 TOOL-dFurnishedOrders-39 TOOL-dFurnishedOrders-41 TOOL-dFurnishedOrders-42 |
| [2026-10-27-build-TOOL-dFurnishedOrders-40-deviation-401.md](../build/2026-10-27-build-TOOL-dFurnishedOrders-40-deviation-401.md) | deviation | — |
| [2026-10-28-build-TOOL-dFurnishedOrders-1-agent-ledger.md](../build/2026-10-28-build-TOOL-dFurnishedOrders-1-agent-ledger.md) | journal | TOOL-dFurnishedOrders-1 TOOL-dFurnishedOrders-2 TOOL-dFurnishedOrders-3 TOOL-dFurnishedOrders-4 TOOL-dFurnishedOrders-5 TOOL-dFurnishedOrders-6 TOOL-dFurnishedOrders-7 TOOL-dFurnishedOrders-8 TOOL-dFurnishedOrders-9 TOOL-dFurnishedOrders-10 TOOL-dFurnishedOrders-11 TOOL-dFurnishedOrders-12 TOOL-dFurnishedOrders-13 TOOL-dFurnishedOrders-14 TOOL-dFurnishedOrders-15 TOOL-dFurnishedOrders-16 TOOL-dFurnishedOrders-17 TOOL-dFurnishedOrders-18 TOOL-dFurnishedOrders-19 TOOL-dFurnishedOrders-20 TOOL-dFurnishedOrders-22 TOOL-dFurnishedOrders-23 TOOL-dFurnishedOrders-24 TOOL-dFurnishedOrders-25 TOOL-dFurnishedOrders-26 TOOL-dFurnishedOrders-27 TOOL-dFurnishedOrders-28 TOOL-dFurnishedOrders-29 TOOL-dFurnishedOrders-30 TOOL-dFurnishedOrders-31 TOOL-dFurnishedOrders-32 TOOL-dFurnishedOrders-33 TOOL-dFurnishedOrders-34 TOOL-dFurnishedOrders-35 TOOL-dFurnishedOrders-36 TOOL-dFurnishedOrders-37 TOOL-dFurnishedOrders-38 TOOL-dFurnishedOrders-39 TOOL-dFurnishedOrders-41 TOOL-dFurnishedOrders-42 TOOL-dFurnishedOrders-43 TOOL-dFurnishedOrders-44 TOOL-dFurnishedOrders-45 TOOL-dFurnishedOrders-46 TOOL-dFurnishedOrders-47 TOOL-dFurnishedOrders-48 TOOL-dFurnishedOrders-49 TOOL-dFurnishedOrders-50 TOOL-dFurnishedOrders-51 TOOL-dFurnishedOrders-52 TOOL-dFurnishedOrders-53 TOOL-dFurnishedOrders-54 TOOL-dFurnishedOrders-55 TOOL-dFurnishedOrders-56 TOOL-dFurnishedOrders-57 TOOL-dFurnishedOrders-58 TOOL-dFurnishedOrders-59 TOOL-dFurnishedOrders-60 TOOL-dFurnishedOrders-61 |
| [2026-10-27-prompt-TOOL-dFurnishedOrders-38-round3-fix-brief.md](../prompts/2026-10-27-prompt-TOOL-dFurnishedOrders-38-round3-fix-brief.md) | research | TOOL-dFurnishedOrders-38 TOOL-dFurnishedOrders-39 TOOL-dFurnishedOrders-41 TOOL-dFurnishedOrders-42 |
| [2026-10-27-review-TOOL-dFurnishedOrders-38-spec-audit-round1.md](../reviews/2026-10-27-review-TOOL-dFurnishedOrders-38-spec-audit-round1.md) | spec-audit | TOOL-dFurnishedOrders-38 TOOL-dFurnishedOrders-39 TOOL-dFurnishedOrders-41 TOOL-dFurnishedOrders-42 |

<!-- /gen:spec-records -->

## 1. Goal

The spec audit of the round-2 promotions
(`memory/builds/dFurnishedOrders/reviews/2026-10-27-review-TOOL-dFurnishedOrders-31-spec-audit-round1.md`)
confirmed finding **id 28 at HIGH**, report item **H3**. Id 15 reports the flat-row form of the same
widening at MEDIUM as item M13 and takes `TOOL-dFurnishedOrders-41`.

`TOOL-dFurnishedOrders-36` S1 defines a receipt target's kit home as "the directory of each receipt
row whose `source` sits under that kit's home", and subtracts every tracked `*.test.sh` under it.
Merged and seed rows land at the repo root: `apply` writes a merged row with `path` set to its
destination (`tools/govkit/govkit.py:7787-7794`), pytest-parallel-guardrails' merged rule lands
`pyproject.toml` (`tools/pytest-parallel-guardrails/kit.toml:35-38`), and process-monitor's seed rule
lands `.process-monitor.conf` (`tools/process-monitor/kit.toml:39-42`). The directory of either row
is the root, so the root becomes a kit home, and on an adopter that applied either kit every
`*.test.sh` and every file matching a `project-owned` include anywhere in the tree leaves the scan.
An adopter's own suite, a run.test.sh under its scripts directory passing `checklist:`, is never
named, and `witness` and `up` exit 0 over a live call site, against unit 36 §3's "an adopter's own
suite outside every kit home ... the walk scans it". Unit 36 AC1's fixture holds only an engine row
under `tools/workflows`, so it cannot see this.

This unit derives a receipt target's kit homes from what each kit declares, never from where a row
landed. It repairs `TOOL-dFurnishedOrders-36` and builds one step after it (order 7).

## 2. Scope (IN)

- **S1** — The home is declared. On a target holding `.governance/install.json`, `derive_call_sites`
  (`tools/govkit/steps/retired_dispatch_args.py`) takes the kit homes of unit 36 S1 as follows: for
  each distinct `kit` value of the receipt's `files` rows, gov's descriptor of that entry id, read
  through `read_shipped_descriptors` (`tools/govkit/govkit.py:13283`) on the step's by-path
  `gov_govkit` load (`TOOL-dFurnishedOrders-35` S1); its `home` resolved under that entry's prefix
  on the target by `resolve_prefix_token` (`:180-191`). The prefix is the one `target_context`
  (`:1436-1477`) answers for the entry, given the target's `.governance/deploy.toml` when present,
  else a descriptor holding only the receipt's top-level `prefix` (written at `:7982`), else `tools`
  as `target_context` defaults. Observed by AC1 and AC3.
- **S2** — No row's directory is a home. The parent directory of a receipt row's `path` takes no
  part in the home set: a merged, seed or engine row landing outside its kit's declared home, at
  the repo root or under `.claude/`, adds nothing to it. Observed by AC1 and AC3.
- **S3** — The target root is never a home. A resolved home that is the target root, which a
  root install (`prefix` `.`) of an entry whose descriptor `home` is `.` resolves to, and a resolved
  home naming no directory on the target, add no directory to the home set; the kit's receipt rows
  stay subtracted by unit 35's receipt rule. Observed by AC2.
- **S4** — A refused prefix refuses the step. A per-entry prefix `target_context` refuses raises its
  `Refusal`, and the step exits 1 naming it before any scan, as unit 36 §5 refuses a descriptor
  that does not parse. Observed by AC2.

## 3. Non-goals (OUT)

- A flat entry's home at a prefix other than the root, a `{prefix}/` row landing at the prefix root:
  the minors batch `TOOL-dFurnishedOrders-41`, for id 15, which builds on S1 and S3.
- The `project-owned` rows' derivation and their mapping onto the target, and a home gov has no
  descriptor for: `TOOL-dFurnishedOrders-41`, for ids 17, 24, 33 and 8.
- The kit-file subtraction on each target kind: `TOOL-dFurnishedOrders-35`, unchanged.
- The report's left-shift gate, a checklist entry for a join key widened by a shared location: no
  clause of this build names it; S3 is its instance here.

### Edges

- **consumes-from** `TOOL-dFurnishedOrders-36` — S1's kit home on a receipt target, which S1 to S3 define from the kit's declaration (id 28)
- **consumes-from** `TOOL-dFurnishedOrders-35` — the step's by-path `gov_govkit` load, through which S1 reads gov's descriptors (id 28)
- **hands-off** `TOOL-dFurnishedOrders-41` — the declared-home derivation and its target-root guard, which unit 41 extends to flat entries at the prefix root, maps `project-owned` rows through, and gives an outcome for a kit gov has no descriptor for (ids 15, 17, 24, 33, 8)
- **hands-off** `TOOL-dFurnishedOrders-43` — S1's receipt-home branch and AC1's fixture, which unit 43 S1 to S3 derive from `apply`'s own rules (id 1 of the fourth audit)
- **hands-off** `TOOL-dFurnishedOrders-45` — S1's home sketch, S4's prefix read, §5 and AC2 and AC3's fixtures, which unit 45 S1, S5, S6 and S8 settle (ids 25, 5, 13, 27 of the fourth audit)
- **hands-off** `TOOL-dFurnishedOrders-46` — the govkit selftest arm whose sibling reads unit 46 S8 guards (id 22 of the fourth audit)

## 4. Design

### The home set on a receipt target, after this unit

```
for eid in {row["kit"] for row in receipt["files"]}:
    desc  = read_shipped_descriptors(gov_root)[eid]          # absent: no home (unit 41 names it)
    pfx   = target_context(target, deploy_or_receipt, eid, desc)["prefix"]
    home  = resolve_prefix_token("{prefix}/" + desc["home"], pfx), normalised
    home == "." (the target root)        -> no home
    home names no directory on target    -> no home
    else                                 -> home   (unit 36 subtracts its *.test.sh and project-owned files)
```

### Why the declaration and not the rows

A row's `path` is where a rule landed, and a rule may land anywhere its `to` says: a merged block in
`pyproject.toml`, a seed at `.process-monitor.conf`, agent-cap's hook under `.claude/hooks/`. A
kit's `home` is the one directory the kit claims, and `target_context` is the one reader of where
that home sits on a target. Reading both from gov keeps the step agreeing with `apply`.

### Inventory

Minted: nothing. S1 to S3 are a branch of `derive_call_sites`, and every function they call exists in
`govkit.py`.

### Migration

None: the steps have never run.

### Rollout

Live at landing, at order 7, after units 35 and 36.

### Files touched (estimate)

- `tools/govkit/steps/retired_dispatch_args.py`
- `tools/govkit/selftest.py`

### Alternatives rejected

- **Keep the row-directory rule and skip merged, seed and rendered rows.** An engine row landing
  outside its home, agent-cap's under `.claude/hooks/`, still makes that directory a home and hides an
  adopter's script beside it.
- **Take the home from the receipt's `source` column.** A `source` spells gov's layout, and a
  `{prefix}/` source on a flat entry resolves to the prefix root, the widening id 15 reports.

## 5. Production-readiness checklist

- security — the step reads gov's descriptors, the target's deploy descriptor and its receipt, and
  writes nothing; every prefix passes `target_context`'s strict token class.
- perf / scale — one descriptor read per run and one `target_context` call per receipt entry.
- error / empty / loading states — a refused prefix exits 1 naming it (S4); a receipt with no `files`
  rows yields no home.
- observability — unit 36 S2's `kit suite(s)` count on the scan line.
- risks — a kit whose descriptor moved its `home` since the target applied it reads the new home;
  the step runs from gov at the version being applied, which is the layout `up` writes.
- testing — AC1 to AC3 by fixtures; the arm of §7 at the close.
- migration — none.
- user docs — none: the step's printed line is what the walk shows.

## 6. Acceptance criteria

- **AC1** — When `python retired_dispatch_args.py witness <target> checklist` runs over a scratch
  target whose `install.json` under `.governance` carries `prefix` `tools` and three rows, an
  `engine` row `tools/workflows/unattended-unit.js` of kit `review-harness`, a `merged` row
  `pyproject.toml` of kit `pytest-parallel-guardrails` and a `seed` row `.process-monitor.conf` of kit
  `process-monitor`, and which tracks a copy of the build-harness suite under `tools/workflows/` and an
  adopter suite, run.test.sh under the fixture's scripts directory, naming `unattended-unit.js` and
  passing `checklist: 'x'`, it exits 1 naming that adopter suite alone, and its scan line counts
  `1 kit suite(s)`.
  Red when: a merged or seed row at the root makes the root a kit home, so the adopter's suite is
  never scanned.
  fixture: a scratch target repository under `%TEMP%`, built by the pass.
- **AC2** — When the receipt instead carries `prefix` `.` and one `engine` row `check-wiring.sh` of kit
  `check-wiring`, whose descriptor `home` is `.` (`tools/govkit/entries/check-wiring.kit.toml:6`),
  and the target tracks an adopter suite, mine.test.sh at its root, passing `checklist: 'x'`,
  `witness <target> checklist` exits 1 naming that suite; and with a `deploy.toml` under `.governance`
  whose `[kit.check-wiring]` sets `prefix` to a value holding a space, it exits 1 naming
  `kit.check-wiring.prefix` and scans nothing.
  Red when: a root install's flat entry makes the target root a home, or a refused prefix passes as
  an empty home set.
- **AC3** — When the receipt carries a `review-harness` row whose `path` is the drift-audit-code.js
  workflow under the target's `.claude/workflows/`, as
  `tools/govkit/fixtures/adopter-ic-2cff5855.receipt.json` does, and the target tracks an adopter
  suite, mine.test.sh in that same directory, passing `checklist: 'x'`, `witness <target> checklist`
  exits 1 naming it.
  Red when: a row's directory, not the kit's declared home, is taken as a home.

## 7. Gates

`govkit selftest` · `govkit refusal join` · `govkit acceptance matrix` · `recall floor arms` · `policy fixtures` · `lexicon naming predicates` · `memory hygiene` · `spec tokens (a spec's own names resolve)`

New arm: tools/govkit/selftest.py · covers AC1 AC2 AC3 · receipts carrying root-landing merged and seed rows, a root-install flat entry and a row outside its kit's home, each beside an adopter suite, staged by restoring the row-directory rule · none

## 8. Open questions

- **F1 — What is a receipt target's kit home?** Options: (a) the kit's descriptor `home` under the
  entry's prefix as `target_context` answers it; (b) the row-directory rule with merged, seed and
  rendered rows skipped; (c) the directory of each row's `source`. (b) still widens on an engine row
  outside its home; (c) widens on every flat entry. RESOLVED (agent, 2026-10-27, delegated): (a),
  rung 3, the skeptic-judged fix of id 28. widens: none · relaxes: none
- **F2 — Which binding line does a unit the spec audit promoted carry?** RESOLVED (agent,
  2026-10-27, delegated): `**Derived:**` naming `PLAY-dClosedLoop-2`, rung 3, the precedent
  `TOOL-dBoundRoles-39` §8 F1 records. widens: none · relaxes: none
- **F3 — The units this one repairs are unbuilt.** `TOOL-dFurnishedOrders-25`, `-35` and `-36` are
  specced and unbuilt at `08e30fef`, and `tools/govkit/steps/` does not exist. RESOLVED (agent,
  2026-10-27, delegated): the build run re-grounds on each at the pass and stops this unit if unit
  36 S1 is still absent then, rung 1, the brief's rule for unbuilt parents. widens: none · relaxes:
  none

## 9. Revision log

- rev-1 · 2026-10-27 · initial draft, promoted from the spec audit of the round-2 promotions, id 28
  (HIGH, item H3, related to id 15 at MEDIUM).
- rev-2 · 2026-10-27 · §3 · the Edges block gains the **hands-off** bullets mirroring TOOL-dFurnishedOrders-43, TOOL-dFurnishedOrders-45, TOOL-dFurnishedOrders-46, promoted from the spec audit of the round-3 promotions (`memory/builds/dFurnishedOrders/reviews/2026-10-27-review-TOOL-dFurnishedOrders-38-spec-audit-round1.md`); nothing else moved.

## 10. Reuse audit

The seams extended: `read_shipped_descriptors` (`tools/govkit/govkit.py:13283`), the registry's one
descriptor reader; `target_context` (`:1436-1477`), the one reader of an entry's prefix on a target;
`resolve_prefix_token` (`:180-191`), the `{prefix}` resolution; and the receipt's top-level `prefix`
(`:7982`). `python tools/codebase-map/reuse_lookup.py "the directory a kit homes on a target that
holds an install receipt"` ranked `resolve_kit_dir`, `kit_rel`, `kit_dir` and `ask_home_of`;
`resolve_kit_dir` finds one kit file through a receipt row or a probe and lists no home, and the
others resolve gov's own kit directories, so no seam beyond the four named derives a home on a
target. The recall probe returned the audit's H3 text and TOOL-dRenderedAnchor-3's rendered-row join,
neither disagreeing with source.

Recall terms used: `python tools/memory-recall/query.py "which directory is a kit's home on an
adopter that holds an install receipt" --terms "install receipt kit home descriptor prefix merged
seed row repo root target_context resolve_prefix_token"`
