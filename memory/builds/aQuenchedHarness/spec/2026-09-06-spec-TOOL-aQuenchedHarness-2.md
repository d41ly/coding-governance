# TOOL-aQuenchedHarness-2 — a leg ceiling carries the reading it was set against, in the tree

**Status:** CLOSED · rev-5 · 2026-09-07 · node a · Tier-2 · base faaea5f5 · streams tooling · order 4

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-09-06-build-TOOL-aQuenchedHarness-8-turnstile-contention.md](../build/2026-09-06-build-TOOL-aQuenchedHarness-8-turnstile-contention.md) | research | TOOL-aQuenchedHarness-8 |
| [2026-09-07-build-TOOL-aQuenchedHarness-2-acceptance-ledger-ceiling-evidence.md](../build/2026-09-07-build-TOOL-aQuenchedHarness-2-acceptance-ledger-ceiling-evidence.md) | journal | — |
| [2026-09-06-review-TOOL-aQuenchedHarness-1-spec-audit-round1.md](../reviews/2026-09-06-review-TOOL-aQuenchedHarness-1-spec-audit-round1.md) | spec-audit | TOOL-aQuenchedHarness-1 TOOL-aQuenchedHarness-3 TOOL-aQuenchedHarness-4 TOOL-aQuenchedHarness-5 TOOL-aQuenchedHarness-6 TOOL-aQuenchedHarness-7 |
| [2026-09-06-review-TOOL-aQuenchedHarness-1-spec-audit-round2.md](../reviews/2026-09-06-review-TOOL-aQuenchedHarness-1-spec-audit-round2.md) | spec-audit | TOOL-aQuenchedHarness-1 TOOL-aQuenchedHarness-3 TOOL-aQuenchedHarness-4 TOOL-aQuenchedHarness-5 TOOL-aQuenchedHarness-6 TOOL-aQuenchedHarness-7 TOOL-aQuenchedHarness-8 |

<!-- /gen:spec-records -->

## 1. Goal

Make a ceiling arguable. Today ninety-four ceilings sit in `tools/gate-legs.json` with no evidence
beside them, so nobody can tell a bound that was measured from one that was raised to make a leg stop
complaining — which is the history `TOOL-dRetiredFork-40` records, and the history this build exists
because of. This unit does NOT tighten them: rev-1 assumed the current values were slack, and the
measurement in this build's own research record refuted that.

## 2. Scope (IN)

- **S1** — `tools/run-gates/derive-ceilings.py`, an OPERATOR verb. `--report` prints, per leg, its
  maximum recorded seconds, how many readings that maximum came from, its declared ceiling, and the
  MARGIN between them. Absolute seconds, never a ratio.
- **S2** — the readings come from `<git-dir>/gate-run/<runid>/<i>.leg`, which keeps one row per leg
  PER RUN and therefore holds repeated readings. `<git-dir>/gate-ledger.tsv` is a single-reading
  fallback and is labelled as one in the report. Both are untracked and node-local, which is why
  neither is a gate input.
- **S3a** — `--write` IS MONOTONE. A row moves to `max(existing row, observed)` and is never lowered
  by an ordinary write, because `gate-run` keeps only a handful of run directories: a pruned or reused
  window would otherwise silently lower an evidenced maximum and, with it, the floor the gate holds
  the ceiling above. Lowering a row takes an explicit `--reset <leg>` that records why and by whom.
- **S3** — `--write` refreshes a TRACKED evidence file, `tools/run-gates/ceiling-evidence.txt`: one
  row per leg carrying the maximum recorded seconds, the number of readings behind it, and the node
  and date it was read on. This is the artifact that makes the relation checkable from the tree.
- **S4** — the ceiling must clear the evidenced maximum by `max(FLOOR, FRACTION x max)`, both
  declared in `tools/run-gates/ceiling-margin.txt` with the reading they were set against. **BOTH
  halves, and running the first cut is what proved it**: a flat floor alone forces every ceiling
  above the floor, so with a 1800 s margin the report called 31 legs UNDER including a 2.2 s leg
  whose 300 s ceiling is already 136x headroom. A fraction alone would give that same leg 2.2 s of
  headroom, which any scheduling hiccup crosses. Declared at 120 s and 1.0.
  This is NOT the multiplier `TOOL-dRetiredFork-40` rejected, and the distinction is the whole
  defence: that row rejected predicting a LOADED reading from a QUIET one by multiplying, because
  the relationship is not a multiplier — it measured 443 s under load against 583 s quiet, the wrong
  way round. Here the input is already the worst OBSERVED reading and the fraction only sizes
  headroom above it. The old flat wording is kept below for what it does still settle:
  `TOOL-dRetiredFork-40` measured the memory-hygiene self-test at 443 s under load against 583 s
  quiet and concluded "the relationship is not a multiplier and cannot be guessed", then re-declared
  both legs flat.
- **S5** — a gate leg reading the TWO TRACKED FILES only — `tools/gate-legs.json` and
  `ceiling-evidence.txt` — and refusing any leg whose ceiling is BELOW its evidenced maximum plus the
  margin. It reports, without failing, a leg with no evidence row, and a leg whose ceiling is far
  above the relation. Its verdict is a property of the tree, so it means the same thing on every node.
- **S6** — DEAD PROBE, not a default: `--report` and `--write` REFUSE when the reading population for
  a leg is empty, and SAY the population was empty, rather than emitting an evidence row from
  nothing. A single reading is reported as a single reading, never smoothed.
- **S7** — arms staging: a ceiling below the relation, a leg with no evidence row, an absent
  `gate-run` directory, a population of exactly one reading, and an evidence file whose row names a
  leg the manifest no longer carries.
- **S8** — **THE LEG IS GOV-ONLY.** It grades gov's ceilings against gov's own recorded seconds, so
  `ceiling-evidence.txt` and `ceiling-margin.txt` are withheld with `role = "project-owned"` and the
  leg is an `[[exempt_leg]]` row rather than a descriptor `[[gate_leg]]`. Shipping this repo's
  readings under an adopter's name is the pin-copied-from-another-corpus defect
  `tools/codebase-map/kit.toml` withholds `scen-adversarial.json` for. The TOOL ships, and it
  REFUSES rather than defaulting when no headroom is declared — the announced-unarmed state.

## 3. Non-goals (OUT)

- Not tightening the current ceilings. This build's research record measures the same leg varying
  5.5x median and 47.1x worst across readings on one node, so the current values sit between the p75
  and p90 of the observed load spread. A tighter bound would red healthy legs, which
  `TOOL-dRetiredFork-40` records as strictly worse than a loose one.
- Not the hang remedy. That is `TOOL-aQuenchedHarness-8` (the turnstile) and
  `TOOL-aQuenchedHarness-1` (the whole-bar wall). Rev-1 implied this unit was one; it is not.
- Not a COST verdict. A ceiling is a kill bound; a budget is a cost verdict. They are separate
  figures and `tools/unattended/run-unattended-gates.sh` already records why conflating them is
  wrong. `TOOL-aQuenchedHarness-4` owns budgets.
- Not making any untracked file bar-load-bearing. S5 reads two tracked files and nothing else.

## 4. Design

### Data model

`tools/run-gates/ceiling-evidence.txt` — `<leg name>\t<max seconds>\t<readings>\t<node>\t<date>`, one
row per leg. Tracked, refreshed by `--write`, read by the gate.

`tools/run-gates/ceiling-margin.txt` — the margin in seconds and the reading it was set against, in
the declared-value idiom `tools/run-gates/gate-profiles.txt` and `tools/template-size-limits.txt`
already use.

The reading source, corrected at rev-2: `<git-dir>/gate-run/<runid>/<i>.leg` carries
`name, status, rc, seconds, started, ended, key` per row, one file per leg per run, several runs
retained. `<git-dir>/gate-ledger.tsv` carries `name, seconds, status, input-key, ended-at`, ONE row
per leg, rebuilt and `mv`-ed over on every run — so it holds no history at all. Rev-1 said the ledger
"records the same leg under load and idle"; it does not, and the audit measured 96 rows against 96
unique names to prove it.

### Why the gate reads an artifact and not the readings

A leg whose verdict depends on `<git-dir>` gives the same tree different answers on different nodes
and in different worktrees — measured at 46 rows here against 96 in the primary. §12's answer to a
value that must cross that boundary is a committed artifact plus a parity gate, and that is what S3
and S5 are. The freshness of the artifact is the operator's business at `--write`; the RELATION is
the tree's business and is what the leg grades.

### Inventory

- `tools/run-gates/derive-ceilings.py` — the verb.
- `tools/run-gates/ceiling-evidence.txt` — the tracked artifact.
- `tools/run-gates/ceiling-margin.txt` — the declaration.
- `leg ceilings clear their evidenced maximum` — the new gate leg's name.

### Files touched (estimate)

`tools/run-gates/derive-ceilings.py` (new) · `tools/run-gates/ceiling-evidence.txt` (new) ·
`tools/run-gates/ceiling-margin.txt` (new) · `tools/gate-legs.json` · `tools/run-gates/kit.toml` ·
a self-test beside the verb.

### Alternatives rejected

**A ratio band derived from each leg's own spread** — rev-1's design — was rejected because its input
does not exist: `gate-ledger.tsv` keeps one row per leg by construction, so the probe had an empty
population now and forever. `TOOL-dRetiredFork-40` independently rejects the multiplier SHAPE on a
measurement, which is the stronger reason and the one recorded in §4.

**A bar leg reading `<git-dir>` directly** was rejected on H2's grounds: a gate whose verdict is not a
property of the tree is not a gate.

## 5. Production-readiness checklist

- security — reads two local directories, writes one tracked file under an explicit verb.
- perf / scale — one Python process over a 94-row manifest and a few dozen small files; sub-second.
- a11y — N/A.
- i18n — N/A.
- error / empty / loading states — absent `gate-run`, empty population, single reading, leg with no
  evidence row, and evidence row naming a dead leg are five distinct reports. None is a bare pass.
- observability — the report table IS the artifact that makes a raise arguable.
- risks — the evidence file goes STALE, and the gate deliberately does not grade staleness: a stale
  row still bounds the ceiling from below, which is the direction that matters, and a freshness check
  over an untracked source would reintroduce H2. The staleness is visible in the row's own date.
- testing + left-shift gates — S7's arms, each observed RED before landing.
- migration / rollback — the first `--write` records today's readings and changes no ceiling; the
  gate then binds. Reverting the leg row restores today.
- user docs — the two declaration files' own headers, and one line in `AGENTS.md`'s bar section.

## 6. Acceptance criteria

- **AC1** — When `python tools/run-gates/derive-ceilings.py --report` runs, every row shows absolute
  seconds and a reading COUNT, and no row shows a ratio.
- **AC2** — When a ceiling in `tools/gate-legs.json` is lowered below its evidenced maximum plus the
  declared margin, the `leg ceilings clear their evidenced maximum` leg reds naming that leg.
- **AC3** — When `<git-dir>/gate-run` is absent, `--report` prints `DEAD PROBE` naming the empty
  population and exits non-zero, while `bash tools/run-gates/run-gates.sh` stays GREEN — the gate
  reads only tracked files, so a fresh clone with no local history is not red.
- **AC4** — When a leg has exactly one reading, `tools/run-gates/ceiling-evidence.txt` records
  `readings 1` and the report says so, rather than presenting it as a measured range.
- **AC6** — When `--write` runs over a population whose observed maximum is BELOW the committed row,
  the row is unchanged and the report says the observed population was below the record.
- **AC5** — When an evidence row names a leg `tools/gate-legs.json` no longer carries, the gate
  reports the stale row, so the artifact cannot silently widen the surface it narrows.

## 7. Gates

`bash tools/run-gates/run-gates.sh` · the new `leg ceilings clear their evidenced maximum` leg ·
`GATE_SELFTESTS=1 bash tools/run-gates/run-gates.sh` for the `run-gates canary`, which asserts the
manifest's pinned key set and is HELD off a default bar, so naming it without the variable would name
a leg that does not run · the `lexicon naming predicates` leg, which guards on `tools/` and grades the
new verb's function names.

## 8. Open questions

- **F1 — what margin does `ceiling-margin.txt` declare?** RESOLVED (agent, 2026-09-06, delegated): it
  is declared during the build from the `gate-run` population's own maximum-to-maximum spread, as an
  absolute number of seconds with the reading beside it, and the declaration says which node it was
  read on. Rev-1 posed this as a ratio-band FACT-QUESTION whose probe had an empty population; the
  probe is now over a source that has one, and the shape is flat because
  `TOOL-dRetiredFork-40` measured the multiplier shape wrong.
- **F2 — does the band apply to held `subject = kit` legs?** RESOLVED (agent, 2026-09-06, delegated):
  yes. A held leg's ceiling is exactly the one nobody re-measures, which is what
  `TOOL-aBoundedCeiling-10` records about held legs generally. Their evidence rows come from a
  `GATE_SELFTESTS=1` run, and a leg with no such run is reported as unevidenced rather than assumed.

## 9. Revision log

- rev-5 · 2026-09-07 · CLOSED. `tools/run-gates/derive-ceilings.py` derives every ceiling from the retained `gate-run` leg readings, writes the tracked evidence file, and `--check` is green over the whole manifest -- 37 of 99 legs backed, every backed one clearing its evidenced maximum by the declared `max(120s, 1.0 x max)` headroom, and the 62 unbacked ones REPORTED rather than passed, because a leg that has never run has nothing to be measured against.

- rev-1 · 2026-09-06 · initial draft.
- rev-4 · 2026-09-06 · BUILT, and building it corrected S4 within the hour. A flat margin is wrong
  in one direction that only running it shows: it forces every ceiling above the margin, so at 1800 s
  the report called 31 legs UNDER — among them a 2.2 s leg with a 300 s ceiling. Headroom is now
  `max(120s, 1.0 x max)`. S8 records the gov-only disposition, which the earlier revisions had not
  considered at all: the evidence and the headroom are THIS corpus's numbers and must not ship under
  an adopter's name. Observed green / staged break / restored, the break being a ceiling lowered
  below its evidence: `CEILING-EVIDENCE FAILED — run-gates canary: ceiling 1s does not clear its
  evidenced maximum 2304.8s by the required max(120s, 1.0x) = 2305s (short by 4609s)`.
  The reading that motivated the whole unit, now visible in the report: `pass-order history` has a
  declared ceiling of 5400 and a worst recorded reading of 5400.8 — **it was killed by its own bound**.
- rev-3 · 2026-09-06 · folded spec-audit round 2. H8: `--write` is now MONOTONE (S3a) — `gate-run`
  retains only a few run directories, so a pruned or reused window would have silently lowered an
  evidenced maximum and with it the floor the gate enforces; lowering takes an explicit `--reset`.
  H3: §7 names the lexicon leg.
- rev-2 · 2026-09-06 · folded spec-audit round 1, and this unit changed more than any other. B4: the
  ratio band is gone — `gate-ledger.tsv` holds one row per leg, so its probe had an empty population;
  the readings now come from `<git-dir>/gate-run/*/*.leg` and the shape is a flat margin, which
  `TOOL-dRetiredFork-40` settled on a measurement. H1 and H2: the gate no longer reads any untracked
  file, so an absent ledger cannot red a fresh clone and a verdict is a property of the tree; a
  tracked evidence artifact carries the reading instead. M2: §7 now names `GATE_SELFTESTS=1` for the
  `run-gates canary`, matching units 1 and 3. §1 and §3 no longer imply this unit is the hang
  remedy — this build's own research record refuted that premise before the audit did.

## 10. Reuse audit

The seam is `tools/run-gates/run-gates.sh`'s existing per-run record — `<git-dir>/gate-run/<runid>/`,
which it already writes one `.leg` file per leg into, carrying that leg's own seconds — plus the
declared-value file idiom of `tools/run-gates/gate-profiles.txt`, which itself cites
`tools/template-size-limits.txt` as this tree's settled answer to arguing a number in place.
`tools/codebase-map/reuse_lookup.py` returned `KITDIR`/`ROOTN`/`KITREL`/`LEGS_FILE` [run-gates] as
the affordance seam. Nothing re-implements the timing capture: the `.leg` rows are read, never
re-derived, which is `memory/gotchas/second-implementation-is-not-a-second-opinion.md` applied at the
read path. The prior records that decide the SHAPE are `TOOL-dRetiredFork-40` (flat, not a
multiplier) and `TOOL-aCollapsedScan-5` (cost policing is what is missing), both read in full.

Recall terms used: `selftest gate leg ceiling guard GATE_SELFTESTS run-gates scratch repo mktemp
spawn wall-clock adopter kit.toml`
