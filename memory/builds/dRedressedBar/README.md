---
slug: dRedressedBar
node: d
opened: 2026-10-13
streams: tooling
roster: TOOL
ids: TOOL-dRedressedBar-1 TOOL-dRedressedBar-2 TOOL-dRedressedBar-3 TOOL-dRedressedBar-4 TOOL-dRedressedBar-5 TOOL-dRedressedBar-6 TOOL-dRedressedBar-7 TOOL-dRedressedBar-8 TOOL-dRedressedBar-9 TOOL-dRedressedBar-10 TOOL-dRedressedBar-11 TOOL-dRedressedBar-12 TOOL-dRedressedBar-13 TOOL-dRedressedBar-14 TOOL-dRedressedBar-15 TOOL-dRedressedBar-16 TOOL-dRedressedBar-17 TOOL-dRedressedBar-18 TOOL-dRedressedBar-19 TOOL-dRedressedBar-20 TOOL-dRedressedBar-21 TOOL-dRedressedBar-22 TOOL-dRedressedBar-23 TOOL-dRedressedBar-24 TOOL-dRedressedBar-25 TOOL-dRedressedBar-26 TOOL-dRedressedBar-27
spec-audit: 2026-10-13
---

# dRedressedBar — every traced red of the full bar with self-tests at ebce889c7, fixed at its root

## The problem this build exists to solve

Local main at `ebce889c7` is two landings that met without a bar running the self-tests:
aOrientedCast's addenda and the reconcile of origin/main `2a9d8191`. The owner asked for the full
bar with every self-test, profiled, and every red it finds fixed. The run refused first on a stale
generated output, then, past that refusal, reported 16 of 140 legs red with the run-gates canary
still in its retry. Every red but the canary is traced to a cause, and all but push-main's two arms
are causes of their own.

## Expected improvements

- Each of the 16 legs red at `ebce889c7` reads `GATE ok` in one full bar with self-tests over the
  build tip, with the regen preflight fresh and no knob overriding it.
- Every stale suite fixture is re-armed against the code that moved, never waived.
- Local main can take a push whose forced full bar is green, canary aside.

## Detriments if this is not built

- Every push from local main forces a full bar that cannot pass.
- The next bar-less landing hides its own reds among sixteen inherited ones.
- Five suites grade nothing while reading red, so a real regression in their subjects goes unseen.

## Build-level rules

- **Classification (M2)**: seven units, MISSING at open, one mechanism each, authored by the build
  harness from the brief under `prompts/`.
- The run-gates canary is out of scope until its retry reports; a red there is added as a unit.
- **Amendment (M2 ADD), 2026-10-14**: unit 8 added before the audit. Both canary attempts hung
  in arm 11g AC14, past the 13200 s ceiling: the arm's FIFO server exited on one failed open while
  its nested bar ran with no wall. Its brief is
  `prompts/2026-10-14-prompt-TOOL-dRedressedBar-8-brief.md`.
- **Amendment (M2 ADD), 2026-10-14**: unit 9 added before the audit, by the owner's resolution of
  unit 3's F1 as (c). A writing `govkit update` that gains `settings-merge` but leaves `agent-cap`
  out fails on settings-merge's adopter; the owner chose to fix it here rather than record it. Its
  brief is `prompts/2026-10-14-prompt-TOOL-dRedressedBar-9-brief.md`, and unit 3's revision record
  is `prompts/2026-10-14-prompt-TOOL-dRedressedBar-3-2-revision.md`.
- **Amendment (M2 ADD), 2026-10-14**: unit 11 added after the round-1 spec audit, by the owner's
  resolution of unit 10's F1 as (c). Unit 10 narrows settings-merge's accepted stop to two probed
  paths, and unit 11 adds a receipt-reading probe term to the declared-outcome contract, so a hook at
  a receipt-recorded home also refuses the false accept. Its brief is
  `prompts/2026-10-14-prompt-TOOL-dRedressedBar-11-brief.md`, and unit 10's revision record is
  `prompts/2026-10-14-prompt-TOOL-dRedressedBar-10-2-revision.md`.
- **Amendment (M2 ADD), 2026-10-14**: unit 14 added by the owner ("add the apply prefix defect"), the
  defect unit 11's writer measured. A first `apply` at a per-kit agent-cap prefix exits 1, because
  CONFIGURE runs before the receipt exists. It was drafted as unit 12 and re-id'd to 14 when the
  round-2 disposal claimed 12 and 13 in the same minute. Its brief is
  `prompts/2026-10-14-prompt-TOOL-dRedressedBar-14-brief.md`.
- **Amendment (M2 ADD), 2026-10-14**: unit 15 added by the owner's resolution of unit 14's F1 as
  (a). agent-cap's adopter argv runs `{prefix}/settings-merge.py` at agent-cap's own prefix, a file
  that kit never installed there. Its brief is
  `prompts/2026-10-14-prompt-TOOL-dRedressedBar-15-brief.md`, and the edge revisions are
  `prompts/2026-10-14-prompt-TOOL-dRedressedBar-14-2-revision.md`.
- **Amendment (M2 ADD), 2026-10-14**: unit 18 added by the owner: a gate profiler that runs every
  leg in `tools/gate-legs.json`, serially or concurrently under 80% CPU and 90% memory load. Each leg
  runs with no knob, no ceiling and every log kept, and is profiled down to each process it spawns,
  with stall detection that reports and never kills. It is ordered after every other unit. Its brief
  is `prompts/2026-10-14-prompt-TOOL-dRedressedBar-18-brief.md`.
- `GATE_REGEN_CHECK` reaching the canary's nested runners is a separate finding and not this build's.
- Write sets overlap on `tools/roles/adopt-roles.test.sh`, so order sequences them: units 1 and 8
  are disjoint from everything at step 1; units 2 and 9 both commit a regenerated
  `memory/map/generated/symbols.json` (the pre-commit codebase-map gate refuses a stale one), so
  they are built one after the other, never together; 3 follows 9, whose fix its three unscoped arms witness; 4 follows 1; 5 follows
  4; 6 follows 5; 7, the records and kit versions, is measured over the code units 1 to 6, 8 and 9
  leave. Units 10, 11, 12, 13 and 14 follow 7 in that order. Each touches only govkit-exempt files
  and adds no function, so none moves a kit version or the symbol index unit 7 regenerates. Unit 15
  follows 14, and because it moves the hooks kit's shipped bytes after 7, it bumps that version itself.
- Tiers per the manifest's tier rule: a unit moving a shipped engine's bytes is Tier-2, a stale
  fixture, a registry row, a pin or a regenerated output Tier-1.
- No `tools/unattended/` self-test suite runs: standing owner instruction, 2026-08-23.
- Owner rulings, 2026-10-13: confirm the four unconfirmed reds, then fix every traced red; spec
  audit declared; go.
- **Owner ruling, 2026-10-14, the audit chain's end**: run spec-audit round 4 over units 16, 17
  and 18, then build. Every unit round 4 promotes is built from its spec as written, under a
  recorded override of `specs-audited` for those units only. No round 5 runs. Each round so far
  confirmed a new high plus about 22 minors at precision 1.00, 1.00 and 0.92, so the chain would not
  end on M4's precision floor. The closing diff review covers the promoted units' code.
- **Amendment (M2 ADD), 2026-10-14**: unit 20 added by the owner ("Fix the class") after unit 7's
  builder diverged. `govkit mint` let the `playbook` entry's version pattern rewrite a selftest
  fixture in `tools/playbook/render_playbook.py`, playbook-render's file, moving that kit's bytes
  without a bump. Unit 20 tightens the carrier writer so a pattern counts only inside its own entry's
  file group, at order 4, before unit 7. It is built from its spec under the same recorded override
  as round 4's promotions; no further audit round runs. Its brief is
  `prompts/2026-10-14-prompt-TOOL-dRedressedBar-20-brief.md`, and unit 7's revision record is
  `prompts/2026-10-14-prompt-TOOL-dRedressedBar-7-2-revision.md`.
- **Owner ruling, 2026-10-15, the closing review's findings**: the round-1 closing diff review
  (`reviews/2026-10-15-review-TOOL-dRedressedBar-1-20-diff-review-round1.md`, CLEAN WITH FIXES, no
  blocker) confirmed 1 high, 7 mediums and 5 lows; the owner promoted all 13 into this build. Units
  21 (H1, the profiler's dead-run sweep), 22 (the profiler's M1, M2, M5, M7, L1, L2, L3 and L5) and
  23 (govkit's M3, M4, M6 and L4) follow unit 19 in that order, built from their specs under the same
  recorded override as round 4's promotions. Closing review round 2 reviews their fold. Their brief
  is `prompts/2026-10-15-prompt-TOOL-dRedressedBar-21-brief.md`.
- **Owner rulings, 2026-10-15, H1's class**: unit 21 also takes the capture path's open, read and
  delete, and every Python fixed-name temp-then-replace writer under `tools/run-gates/`. Unit 21's
  F1 resolved as its own unit: unit 24 gives the 19 bash `mv` sites and the heredoc writer in
  `run-gates.sh`, `post-merge.sh` and `run-selftests.sh` unpredictable temps under a bash-side static
  check, after unit 23 and before the bar. Its brief is
  `prompts/2026-10-15-prompt-TOOL-dRedressedBar-24-brief.md`.
- **Owner ruling, 2026-10-15, the round-2 closing review**: the fold review
  (`reviews/2026-10-15-review-TOOL-dRedressedBar-21-24-diff-review-round2.md`, CLEAN WITH FIXES, no
  blocker) confirmed 2 highs, 6 mediums and 6 lows; the owner promoted all 14, "then stop". Unit 25
  takes the profiler's arms and guards (H1, M1, L1, L6), unit 26 the temp-name lint and the runner's
  temps (H2, M2, M3, M4, L2, L3, L4, L5), after unit 24 in that order. A round-3 review covers their
  fold; it fixes blockers only, and its other findings go to a follow-up build. Their brief is
  `prompts/2026-10-15-prompt-TOOL-dRedressedBar-25-brief.md`.
- **Owner ruling, 2026-10-15, check 23**: the base bar's `memory hygiene` leg was red on check 23 as
  well as check 17, on ledger lines in builds aSparedSpawn and aOrientedCast that this branch never
  touched (`prompts/2026-10-15-prompt-TOOL-dRedressedBar-1-4-researcher.md`). The owner chose to fix
  them here. Unit 27, a records-only unit after unit 26, rewrites those ledger lines in a legal form
  and writes the acceptance ledgers units 2, 4, 5, 7, 9, 11, 18 and 20 never wrote. Its brief is
  `prompts/2026-10-15-prompt-TOOL-dRedressedBar-27-brief.md`.

## Parked decisions

None yet.

<!-- roster:units -->

| # | Unit | Mechanism |
|---|---|---|
| 1 | `TOOL-dRedressedBar-1` | stale suite fixtures re-armed against the code the bar-less landings moved |
| 2 | `TOOL-dRedressedBar-2` | the one verb offender over the lexicon pin, renamed |
| 3 | `TOOL-dRedressedBar-3` | the govkit selftest's reds, each at its root |
| 4 | `TOOL-dRedressedBar-4` | shipped-surface bans: the `workflows` homonyms install-prefix reads as a kit path |
| 5 | `TOOL-dRedressedBar-5` | fork idioms past the spawn-idiom registry, converted |
| 6 | `TOOL-dRedressedBar-6` | the adopt-roles exits the harness-arms leg finds unarmed, armed |
| 7 | `TOOL-dRedressedBar-7` | records, the regenerated index and the kit versions, measured over the fixed tree |
| 8 | `TOOL-dRedressedBar-8` | the canary's memory-pause arm 11g AC14 hangs when its FIFO server dies, bounded and its server kept alive |
| 9 | `TOOL-dRedressedBar-9` | govkit update's gained settings-merge no longer fails an update that left agent-cap out |
| 10 | `TOOL-dRedressedBar-10` | PROMOTED: the round-1 spec audit's 12 mediums and 11 lows, batched — report ids 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22 and 23 |
| 11 | `TOOL-dRedressedBar-11` | a receipt-reading probe term in govkit's declared-outcome contract, closing settings-merge's last false-accept route |
| 12 | `TOOL-dRedressedBar-12` | PROMOTED: the units-10-11 spec audit's one high, report id 23 — an apply narrower than its receipt keeps every other installed kit's claim and rows |
| 13 | `TOOL-dRedressedBar-13` | PROMOTED: the units-10-11 spec audit's 5 mediums and 18 lows, batched — report ids 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22 and 24 |
| 14 | `TOOL-dRedressedBar-14` | a first apply at a per-kit prefix writes its receipt before CONFIGURE, so settings-merge finds the hook it just installed |
| 15 | `TOOL-dRedressedBar-15` | agent-cap's adopter resolves settings-merge at settings-merge's own home, not at agent-cap's prefix |
| 16 | `TOOL-dRedressedBar-16` | PROMOTED: the units-12-15 spec audit's one high, report id 7 — an apply that keeps a carried kit's claim keeps that kit's gate-leg ownership too |
| 17 | `TOOL-dRedressedBar-17` | PROMOTED: the units-12-15 spec audit's 12 mediums and 9 lows, batched — report ids 1, 2, 3, 4, 5, 6, 8, 9, 10, 11, 12, 13, 15, 16, 18, 19, 20, 21, 22, 23 and 24 |
| 18 | `TOOL-dRedressedBar-18` | a gate profiler: every leg run clean and unbounded, serially or under a load cap, each profiled to its processes, stalls reported and never killed |
| 19 | `TOOL-dRedressedBar-19` | PROMOTED: the units-16-18 spec audit's 19 mediums and 22 lows, batched — report ids 1, 2, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42 and 43 |
| 20 | `TOOL-dRedressedBar-20` | govkit's mint writes a version only into its own entry's file group, never another kit's |
| 21 | `TOOL-dRedressedBar-21` | PROMOTED: the closing review's one high, finding H1 — the profiler's dead-run sweep trusts no path a shared temp dir supplies |
| 22 | `TOOL-dRedressedBar-22` | PROMOTED: the closing review's profiler findings M1, M2, M5, M7, L1, L2, L3 and L5, batched |
| 23 | `TOOL-dRedressedBar-23` | PROMOTED: the closing review's govkit findings M3, M4, M6 and L4, batched |
| 24 | `TOOL-dRedressedBar-24` | the runner scripts' fixed-name temp-then-replace writers take unpredictable temps, under a bash-side static check |
| 25 | `TOOL-dRedressedBar-25` | PROMOTED: the round-2 review's profiler arm and guard findings H1, M1, L1 and L6 |
| 26 | `TOOL-dRedressedBar-26` | PROMOTED: the round-2 review's temp-name lint and runner temp findings H2, M2, M3, M4, L2, L3, L4 and L5 |
| 27 | `TOOL-dRedressedBar-27` | hygiene check 23 green: this build's eight missing acceptance ledgers written, and the base's foreign ledger lines put in a legal form |
<!-- /roster:units -->

<!-- gen:build-index -->
**Build status:** SPECCED · 27 unit(s) · node d · opened 2026-10-13 · streams tooling
ids TOOL-dRedressedBar-1 TOOL-dRedressedBar-2 TOOL-dRedressedBar-3 TOOL-dRedressedBar-4 TOOL-dRedressedBar-5 TOOL-dRedressedBar-6 TOOL-dRedressedBar-7 TOOL-dRedressedBar-8 TOOL-dRedressedBar-9 TOOL-dRedressedBar-10 TOOL-dRedressedBar-11 TOOL-dRedressedBar-12 TOOL-dRedressedBar-13
ids TOOL-dRedressedBar-14 TOOL-dRedressedBar-15 TOOL-dRedressedBar-16 TOOL-dRedressedBar-17 TOOL-dRedressedBar-18 TOOL-dRedressedBar-19 TOOL-dRedressedBar-20 TOOL-dRedressedBar-21 TOOL-dRedressedBar-22 TOOL-dRedressedBar-23 TOOL-dRedressedBar-24 TOOL-dRedressedBar-25 TOOL-dRedressedBar-26
ids TOOL-dRedressedBar-27

<!-- gen:build-units -->
| Unit | Order | Tier | Status | Rev | Last change |
|---|---|---|---|---|---|
| [TOOL-dRedressedBar-1 — stale suite fixtures re-armed against the code the bar-less landings moved](spec/2026-10-14-spec-TOOL-dRedressedBar-1.md) | 1 | 1 | CLOSED | rev-3 | 2026-10-14 |
| [TOOL-dRedressedBar-2 — the one verb offender over the lexicon pin, renamed to a declared verb](spec/2026-10-14-spec-TOOL-dRedressedBar-2.md) | 1 | 2 | CLOSED | rev-3 | 2026-10-14 |
| [TOOL-dRedressedBar-8 — arm 11g AC14 bounded, and its FIFO server kept alive through MSYS's failed opens and broken pipes](spec/2026-10-14-spec-TOOL-dRedressedBar-8.md) | 1 | 1 | CLOSED | rev-3 | 2026-10-14 |
| [TOOL-dRedressedBar-9 — settings-merge's adopter exit with no agent-cap hook declared an accepted stop, so a gaining update completes](spec/2026-10-14-spec-TOOL-dRedressedBar-9.md) | 1 | 2 | CLOSED | rev-7 | 2026-10-14 |
| [TOOL-dRedressedBar-3 — the govkit selftest's 56 reds, traced to four root causes and re-armed](spec/2026-10-14-spec-TOOL-dRedressedBar-3.md) | 2 | 1 | CLOSED | rev-4 | 2026-10-14 |
| [TOOL-dRedressedBar-4 — the `workflows` homonyms the install-prefix ban reads as a kit path, held in a named constant](spec/2026-10-14-spec-TOOL-dRedressedBar-4.md) | 2 | 2 | CLOSED | rev-3 | 2026-10-14 |
| [TOOL-dRedressedBar-5 — fork idioms past the spawn-idiom registry, converted to their no-fork forms](spec/2026-10-14-spec-TOOL-dRedressedBar-5.md) | 3 | 2 | CLOSED | rev-6 | 2026-10-14 |
| [TOOL-dRedressedBar-20 — govkit's carrier writer counts an entry's version pattern only inside that entry's own basis, so a mint never writes another kit's file](spec/2026-10-14-spec-TOOL-dRedressedBar-20.md) | 4 | 2 | CLOSED | rev-2 | 2026-10-14 |
| [TOOL-dRedressedBar-6 — the roles adopter's two exit-1 refusals, armed in its own suite](spec/2026-10-14-spec-TOOL-dRedressedBar-6.md) | 4 | 1 | CLOSED | rev-3 | 2026-10-14 |
| [TOOL-dRedressedBar-7 — records, the regenerated index and the kit versions, measured over the fixed tree](spec/2026-10-14-spec-TOOL-dRedressedBar-7.md) | 5 | 2 | CLOSED | rev-5 | 2026-10-14 |
| [TOOL-dRedressedBar-10 — the round-1 spec audit's 12 mediums and 11 lows, batched: each criterion observed in a form that can pass and fail, each false sentence corrected, and settings-merge's accepted stop narrowed](spec/2026-10-14-spec-TOOL-dRedressedBar-10.md) | 6 | 2 | CLOSED | rev-6 | 2026-10-14 |
| [TOOL-dRedressedBar-11 — a receipt-reading probe term in govkit's declared-outcome contract, closing settings-merge's last false-accept route](spec/2026-10-14-spec-TOOL-dRedressedBar-11.md) | 7 | 2 | CLOSED | rev-6 | 2026-10-14 |
| [TOOL-dRedressedBar-12 — an apply narrower than its receipt keeps every other installed kit's claim and rows, so a refused settings-merge exit stays refused on the next run](spec/2026-10-14-spec-TOOL-dRedressedBar-12.md) | 8 | 2 | CLOSED | rev-9 | 2026-10-15 |
| [TOOL-dRedressedBar-13 — the units-10-11 spec audit's 5 mediums and 18 lows, batched: each criterion half observed in a form that can fail, each false sentence corrected, and the code sites they describe made to say what the specs claim](spec/2026-10-14-spec-TOOL-dRedressedBar-13.md) | 9 | 2 | CLOSED | rev-6 | 2026-10-14 |
| [TOOL-dRedressedBar-16 — an apply that keeps a carried kit's claim keeps that kit's gate-leg ownership too, so a later argv change does not wedge the kit](spec/2026-10-14-spec-TOOL-dRedressedBar-16.md) | 9 | 2 | CLOSED | rev-5 | 2026-10-15 |
| [TOOL-dRedressedBar-14 — a first apply at a per-kit prefix configures against the homes it just wrote: the receipt is written ahead of CONFIGURE](spec/2026-10-14-spec-TOOL-dRedressedBar-14.md) | 10 | 2 | CLOSED | rev-8 | 2026-10-15 |
| [TOOL-dRedressedBar-15 — agent-cap's adopter runs settings-merge's own adopter at settings-merge's home, declared as `[adopt] via`, and selfcheck refuses any argv naming another entry's file](spec/2026-10-14-spec-TOOL-dRedressedBar-15.md) | 11 | 2 | CLOSED | rev-7 | 2026-10-15 |
| [TOOL-dRedressedBar-17 — the units-12-15 spec audit's 12 mediums and 9 lows, batched: each faulted criterion observed in a form that can pass and fail, each false sentence corrected, and the code sites they describe made to hold what the specs claim](spec/2026-10-14-spec-TOOL-dRedressedBar-17.md) | 12 | 2 | CLOSED | rev-6 | 2026-10-15 |
| [TOOL-dRedressedBar-18 — a gate profiler: every leg run clean and unbounded, serially or under a load cap, each profiled to its processes, stalls reported and never killed](spec/2026-10-14-spec-TOOL-dRedressedBar-18.md) | 13 | 2 | CLOSED | rev-8 | 2026-10-15 |
| [TOOL-dRedressedBar-19 — the units-16-18 spec audit's 19 mediums and 22 lows, batched: the profiler's census, path, launch, turnstile, redaction and leg-declaration gaps closed, the receipt sidecar made atomic, and specs 12 and 14 to 18 corrected](spec/2026-10-14-spec-TOOL-dRedressedBar-19.md) | 14 | 2 | CLOSED | rev-8 | 2026-10-15 |
| [TOOL-dRedressedBar-21 — the profiler trusts no path a temp dir supplies: a dead run's logs land in this run's record, no capture is opened, read or deleted through a link, and run-gates' Python temp files take unpredictable names](spec/2026-10-15-spec-TOOL-dRedressedBar-21.md) | 15 | 2 | CLOSED | rev-3 | 2026-10-15 |
| [TOOL-dRedressedBar-22 — the closing review's profiler findings, batched: an interrupt names every kept capture, the probe spawns the base interpreter, and each faulted arm proves its work](spec/2026-10-15-spec-TOOL-dRedressedBar-22.md) | 16 | 2 | CLOSED | rev-2 | 2026-10-15 |
| [TOOL-dRedressedBar-23 — the closing review's govkit findings M3, M4, M6 and L4: a narrower apply keeps a carried kit's orders and order-file legs, target spawns decode stderr through one helper, a leg guard widens, and a routing arm grades each member](spec/2026-10-15-spec-TOOL-dRedressedBar-23.md) | 17 | 2 | CLOSED | rev-1 | 2026-10-15 |
| [TOOL-dRedressedBar-24 — the runner scripts' fixed-name temp writers take unpredictable temps, and a shell-hygiene mode reds a new one](spec/2026-10-15-spec-TOOL-dRedressedBar-24.md) | 18 | 2 | CLOSED | rev-2 | 2026-10-15 |
| [TOOL-dRedressedBar-25 — the round-2 review's profiler findings, batched: the A/B verdict gate grades the condition, the selftest's guard covers its kit dir, and AC9's orphan is waited on](spec/2026-10-15-spec-TOOL-dRedressedBar-25.md) | 19 | 2 | CLOSED | rev-1 | 2026-10-15 |
| [TOOL-dRedressedBar-26 — the round-2 temp-name findings, batched: every command-word `mv` is read, no positional or two-hop source reds, no bare `SRANDOM` is admitted, and the cache writer and leftover check hold on every runtime](spec/2026-10-15-spec-TOOL-dRedressedBar-26.md) | 20 | 2 | CLOSED | rev-1 | 2026-10-15 |
| [TOOL-dRedressedBar-27 — hygiene check 23 green by evidence: this build's eight missing acceptance ledgers written, and the base's 37 foreign ledger lines put in a legal form](spec/2026-10-15-spec-TOOL-dRedressedBar-27.md) | 21 | 1 | SPECCED | rev-1 | 2026-10-15 |
<!-- /gen:build-units -->

Records: 114 bound to this build, across 4 record folder(s).

Ids no record names: none — every unit id is named by a record.

Ids no `spec-audit` record has ever named: TOOL-dRedressedBar-19 TOOL-dRedressedBar-20 TOOL-dRedressedBar-21 TOOL-dRedressedBar-22 TOOL-dRedressedBar-23 TOOL-dRedressedBar-24 TOOL-dRedressedBar-25 TOOL-dRedressedBar-26 TOOL-dRedressedBar-27.
<!-- /gen:build-index -->

<!-- gen:build-order -->

| Step | Units | Parallel |
|---|---|---|
| 1 | `TOOL-dRedressedBar-1`, `TOOL-dRedressedBar-2`, `TOOL-dRedressedBar-8`, `TOOL-dRedressedBar-9` | yes |
| 2 | `TOOL-dRedressedBar-3`, `TOOL-dRedressedBar-4` | yes |
| 3 | `TOOL-dRedressedBar-5` | no |
| 4 | `TOOL-dRedressedBar-20`, `TOOL-dRedressedBar-6` | yes |
| 5 | `TOOL-dRedressedBar-7` | no |
| 6 | `TOOL-dRedressedBar-10` | no |
| 7 | `TOOL-dRedressedBar-11` | no |
| 8 | `TOOL-dRedressedBar-12` | no |
| 9 | `TOOL-dRedressedBar-13`, `TOOL-dRedressedBar-16` | yes |
| 10 | `TOOL-dRedressedBar-14` | no |
| 11 | `TOOL-dRedressedBar-15` | no |
| 12 | `TOOL-dRedressedBar-17` | no |
| 13 | `TOOL-dRedressedBar-18` | no |
| 14 | `TOOL-dRedressedBar-19` | no |
| 15 | `TOOL-dRedressedBar-21` | no |
| 16 | `TOOL-dRedressedBar-22` | no |
| 17 | `TOOL-dRedressedBar-23` | no |
| 18 | `TOOL-dRedressedBar-24` | no |
| 19 | `TOOL-dRedressedBar-25` | no |
| 20 | `TOOL-dRedressedBar-26` | no |
| 21 | `TOOL-dRedressedBar-27` | no |
<!-- /gen:build-order -->

<!-- gen:build-edges -->

*This build declares no parent and no build declares it as one.*
<!-- /gen:build-edges -->
