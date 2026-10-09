# Appendix — Refusal surface vs value: unattended kit — research + retirement-review design

**Serves:** none — research that precedes this build's specs; its units await the owner's scope ruling

A read-only research pass by one of five agents on 2026-10-09, kept verbatim below its first heading. Figures are estimates from static counts and one-line timings unless marked measured; the ranked synthesis is `2026-10-09-build-TOOL-aSparedSpawn-0-research.md`.


Research only. Nothing was run except read-only `grep`/`git log`/`git show` and three in-process Python
scans over file text (scripts and outputs in this scratchpad: `extract.py`, `prov.py`,
`r2-sites.json`, `prov.json`). No suite, leg or `*.test.sh` was executed. Tree: worktree
`gate-runner-profiling-optimization-5d1f1e` at `6bc6c949c`.

## 0. Headline

- **The refusals that never fire are about 92% of the surface.** I found real-run evidence (outside
  any suite) for 16 of the 110 driver check numbers and 10 of the 50 leg check numbers. Measured by
  site it is narrower: those checks own 121 of 359 driver sites and 96 of 264 leg sites, and in most
  of them only one or two message variants ever fired. My estimate is **~334 of 359 driver sites and
  ~244 of 264 leg sites never observed firing in a real run.**
- **Most of what did fire was a refusal that turned out to be wrong.** Of 26 checks with real-run
  evidence, 13 fired as a wedge, a false positive or two guards disagreeing, and each of those cost a
  repair build (table in §2.3). One check (leg check 7) has already been demoted from fail to report.
- **The surface is dominated by repetition, not distinct conditions.** In the driver, roughly 30% of
  sites (~107) are the same five conditions repeated per verb:
  - the run-state file is missing (23 sites);
  - a required flag is missing (36);
  - a field carries a newline, carriage return or separator, or spells the bypass flag (~37 unique);
  - an internal table or environment step failed (11).

  In the leg, ~45% (~120 sites) guard the gate's own inputs (liveness and code-shape) rather than
  any run.
- **Nothing can lower the count today.** `ARMS_FLOORS` (`.memory-tree.conf:581`; the driver floor is
  362:348 and the leg's 264:256) is a shrink-guard. Its history comments say "Raising lowers
  nothing" three times, and no commit has ever lowered an unattended pair. The repo's two
  retirements of a *mechanism* each **added** a refusal: a tombstone at `check-unattended.sh:3953`,
  a retired-premise ban at `:6022`/`:6024`, and the argv refusal of `--emit-ceiling`.
- **Cost driver:** the driver suite's last whole reading was **17,142 s** (`selftest-budgets.txt`,
  pooled at `90a6f6fae`). That is 940 `$(run …)` driver invocations, about 18 s each, or 2.6
  invocations per refusal site. Retiring or consolidating the candidates below saves an estimated
  **~1.9–4.9 ks on the driver suite (11–28%)** and **~4.3–8.4 ks serial on the leg suite (22–43%)**. The
  ranges are wide, and §5 states why.

Growth (my count of non-comment `fail <n>` sites at the last commit of each date):

| date | driver sites | leg sites | driver-suite `$(run` calls | leg-suite lines |
|---|---|---|---|---|
| 2026-08-23 | 168 | 154 | 355 | 2,494 |
| 2026-09-10 | 194 | 178 | 431 | 3,192 |
| 2026-09-20 | 206 | 179 | 485 | 3,374 |
| 2026-09-30 | 298 | 250 | 774 | 5,809 |
| 2026-10-09 | 359 | 264 | 939 | 6,780 |

That is +153 driver sites in the last 19 days against +38 in the 28 days before, so growth is
accelerating. Check numbers are per-verb buckets rather than conditions: driver check 49 has 40
sites, 47/48/37 have 22 each, and leg check 16 has 34 and leg check 28 has 31.

Not in scope: the 8 non-numbered `REFUSING … exit 2` sites in the driver's load path. They are
not armed by `check-arms.py`, so they do not carry the per-arm cost.

---

## 1. Classification

### 1.1 Method and basis

- **Population.** I took every non-comment `fail <n>` site: 359 in `tools/unattended/unattended.sh`
  and 264 in `tools/unattended/check-unattended.sh`. The extraction is `extract.py` and the output
  is `r2-sites.json`.
- **Sample.**
  - Driver: every 4th site, **90 sites** (25%). The extrapolation factor is 359/90 = 3.99.
  - Leg: every 3rd site, **88 sites** (33%). The extrapolation factor is 3.0.

  Each sampled site was read and classified by hand with one primary class.
- **Provenance.** The record ids cited in the message, or in the comment block up to 40 lines above
  the site, were resolved to their spec's §1 Goal or to their `DECISIONS.md` row. 96 distinct ids
  were cited. A heuristic (`prov.py`) marked a record as an *incident* when its Goal cites an
  observed occurrence (`RUN.md:<n>`, `i<nnn>`, census, "measured", "live run", "reproduced"). The
  result was 29 incident, 18 review-finding, 32 feature or other, and 17 with no spec. I spot-read
  the top 12 by citation count to calibrate.
- **Coverage.** 206 of 359 driver sites and 130 of 264 leg sites cite no record at all.

Classes, each site taking the first one that fits:

| code | meaning |
|---|---|
| **I** | guards a reproduced incident: a cited record, or a run record, shows it happening in a real run |
| **D** | duplicates another refusal's condition: the same predicate elsewhere in the kit, in another kit, or on the merge bar |
| **V** | a message variant of one condition repeated per verb (missing run-state file, missing required flag, newline, CR or separator injection, bypass-flag spelling) |
| **F** | reachable only through a fixture: no real run state produces it, only a git or clock shim, mktemp failure, or a code defect |
| **G** | guards a defect in the gate itself: the gate's inputs are empty or unreadable, its floor is malformed, its parser is uncertified, a code-shape lint over the kit's own source, or the kit's own docs disagree with the driver |
| **H** | guards a hypothetical: a designed-in or review-constructed condition with no observed occurrence |

### 1.2 Driver (`unattended.sh`): 90 sampled

| class | sample | extrapolated (×3.99) | sample examples (line · check) |
|---|---|---|---|
| I | 8 | ~32 | 3283·c89 spec-audit opt-in · 3547·c26 terminal record · 5360·c31 · 5474·c32 · 5521/5566·c34 marker · 8476·c59 · 9935·c13 DoD unmet |
| D | 6 | ~24 | 2736·c39 ↔ leg c17 · 4580·c87 ↔ leg c19 · 6279·c97 ↔ leg c15 · 6527·c85 ↔ leg c42 · 12417·c49 ↔ leg c23 · 12481·c49 ↔ spec-tokens leg |
| V | 27 | ~108 | no run-state (2229, 6241, 7193, 7824, 9775, 11780, 12140) · newline/CR/separator/bypass (5709, 5935, 6941, 9861, 11388, 11561, 11586, 11785, 11852, 11968, 12033, 12169) · required flag (5885, 7590, 11521, 11716, 11840, 12070, 12096, 12156) |
| F | 7 | ~28 | 1787·c27 mktemp · 3198·c55 conf unevaluable · 5962/5997·c56 HEAD/clock · 6688·c29 (pinned unarmed) · 7606·c88 append · 9711·c69 · 12317·c49 no message file |
| G | 1 | ~4 | 2019·c111 undeclared claim-read class; its twin is 1995·c110 |
| H | 41 | ~164 | 1735·c22 env git config · 2556·c1 slug shape · 3323·c79 may: token · 4635·c75 · 5761·c35 · 6318·c101 · 7472·c51 · 8137·c58 · 12578/12604/12706·c49 dispatch shape |

Direct counts from the classifier over all 359 sites, which back the V extrapolation:
- missing run-state: 23 sites across checks 10, 37, 43, 47, 48, 49, 51, 52 and 88;
- newline or CR: 17 sites;
- separator: 11 sites;
- bypass flag: 14 sites.

The last three overlap, about 37 unique sites between them. Required flag accounts for 36 sites
and internal or environment failure for 11.

### 1.3 Leg (`check-unattended.sh`): 88 sampled

| class | sample | extrapolated (×3) | sample examples (line · check) |
|---|---|---|---|
| I | 8 | ~24 | 839·c2 review bookkeeping · 2071·c15 landed facts · 2148·c8 generated copy · 2214·c9 BASE not ancestor · 2295·c15 no anchor kind · 3825·c24 roster moved · 4250·c23 undeclared write · 4402·c20 probe order |
| D | 12 | ~36 | 1096·c38 · 2114·c15 · 2182/2188/2233·c9 · 2415/2673·c19 · 2469·c13 · 2636·c17 · 3051·c10 · 3205·c45 · 5882·c42 |
| G | 41 | ~123 | liveness: 494, 610, 892, 981, 1014, 1174, 3039, 3422, 3544, 3613, 3629, 3729, 4441, 4777, 5519 · code-shape: c28 ×31 (4891–5357), 5084 replace pin, 5121 inlined parser drift, 5769·c39, 5812·c15 `--diff-filter` lint · floors: 879, 892, 1014, 1042 |
| H | 27 | ~81 | doc-parity Skill/protocol ↔ driver: 3082, 3430, 3467, 3571, 3643, 3659, 4381, 4464, 4510, 4597, 4620, 5928, 6024 (14 in the sample, ~42 extrapolated) · record: 2002·c5, 2348·c13, 2577·c19, 2698, 2735, 2771·c37, 2808 |
| V, F | 0 | — | Leg G-class sites are fixture-reachable only by editing the kit's own source, so G is a subset of F here |

### 1.4 What the classes say

- The **I** share is about 9% of each file, roughly 56 of 623 sites.
- Even I is generous. Several "incident" provenances are **incidents caused by an earlier refusal**,
  for example check 34's no-ff wedge and leg check 7 blocking the fleet. The new refusal guards the
  kit's own previous fix rather than a run.
- **V + F + G** together are ~263 of 623 sites (42%). These are guards whose number could fall
  without losing a single distinct condition.
- **H** is the largest single class at ~245 sites (39%). It contains security-shaped guards I would
  *not* put up for retirement:
  - git config or object substitution through the environment (1735, 1745);
  - the self-authorizing `may:` and `spec-audit:` writes (leg 2577; driver 3283).

  Charter §9 and the ponytail boundary rule ("never simplify away security") both apply.

---

## 2. Evidence of value: firing outside the suite

### 2.1 Sources searched

1. Every tracked run-state record, `memory/builds/*/RUN*.md` plus the archive (82 files). I
   captured each `check N` with its context (`runctx.txt`, 143 hits) and read all of them.
2. The nine committed runlog records (`*-runlog-*.md`). They carry **no check numbers**: verb rows
   are withheld (for example, the aGraftedHelix runlog shows `withheld rows: verb 186`). The driver
   writes `RUNLOG_CHECKS` (`unattended.sh:675-676, 12974`) only into the machine-local store, and
   that store is **absent on node a** (`%LOCALAPPDATA%\runlog` does not exist). The best firing
   ledger the kit has is therefore not available to this research.
3. `memory/gotchas/*`, every `memory/builds/*/BACKLOG.md`, `memory/DECISIONS.md`, and the auto-memory
   notes in `~/.claude/projects/C--projects-coding-governance/memory/`.
4. The literal `UNATTENDED check N FAILED` text across `memory/`: 48 distinct numbers. These are
   **almost all acceptance ledgers, specs and spec-audit reviews**, meaning suite or AC evidence
   rather than real runs (for example, 25 hits for check 90 sit in aGraftedHelix ledgers). The driver
   and the leg share this message prefix and overlapping numbers, so the literal alone cannot
   attribute a firing. I attributed each one by context.

Hygiene-gate checks with the same numbers were excluded: memory-tree checks 6, 12, 14, 16 and 23
appear in the same run records.

### 2.2 Checks with real-run evidence

| file | check | evidence (record) |
|---|---|---|
| driver | 13 DoD unmet at `--close` | 27 `override · item …` rows in 22 RUN records (gates-green 11, build-complete 11, specs-audited 5) |
| driver | 14 unknown argument | dBriefedPass/RUN.md; dMispairedQuote/RUN.md (the Skill documented a flag the driver refused) |
| driver | 15 LANDED claim | aDeclaredBound/RUN.md:35 |
| driver | 18 preflight BASE | aSealedCaravan/RUN.md, BACKLOG -6 (driver equality vs leg ancestry) |
| driver | 26 terminal record | aDeclaredBound/RUN.md:37 (owner bypassed it by hand); aGroundedOrientation BACKLOG |
| driver | 28 no HEAD symref | cBriefedPilot/RUN.md |
| driver | 31 LANDED only from LANDING | dUnstalledConvoy/BACKLOG ("Hit at this build own landing 2026-08-21") |
| driver | 32 HEAD not ancestor | aGroundedOrientation/RUN.md; aFusedCharter/BACKLOG -4 (deadlock) |
| driver | 34 lander marker | dTieredTribunal/RUN.md; aGroundedOrientation BACKLOG; dScaffoldedMirror BACKLOG -22 (REPRODUCED on dPromptedSeam); cBriefedPilot |
| driver | 37 review | aLeakedHandle/RUN.md; dUnstuckLanding/RUN.md |
| driver | 48 rescope/units | dUnstalledConvoy/RUN.md, gotcha `two-guards-one-question-two-answers.md` |
| driver | 49 dispatch | aHoistedPass, cMendedVintage, dDerivedDocket, aGraftedHelix RUN.md; aMendedFleet BACKLOG -107 |
| driver | 54 `--landed` | gotcha `witness-graded-against-a-fact-written-after-it.md` |
| driver | 59 resume take-over | DECISIONS ("logs check 59 at every pass boundary") |
| driver | 89 spec-audit opt-in | aEvidencedLens, aGraftedHelix (record rotated), aWardedAudit RUN.md |
| driver | 90 claim | aGraftedHelix RUN.ABORTED.6410435d.md (with live-run Goal text in specs -18 and -20) |
| leg | 2 review bookkeeping | dMispairedQuote/RUN.md |
| leg | 7 live-count (**now report-only**) | aBoundedVerdict RUN.ABORTED, aGroundedOrientation, dTieredTribunal; demoted by TOOL-aUnblockedFleet-2 (`check-unattended.sh:1984-1986`) |
| leg | 8 generated-region copy | aSealedCaravan/RUN.md; aDeclaredCeiling BACKLOG |
| leg | 9 BASE ancestry | aMooredAnchor BACKLOG -1; aSealedCaravan |
| leg | 15 landed facts | dScaffoldedMirror BACKLOG (red on main for two days) |
| leg | 17 waiver handle | cBriefedPilot/RUN.md (found a defect while building) |
| leg | 19 grant / asks | aEvidencedLens/RUN.md |
| leg | 22 conf-key join | aHoistedPass, aTunedCompass, aWokenSentinel RUN.md |
| leg | 23 undeclared writes | aHalvedInstall, aSightedSkeptic, aRepatriatedFork, aUnblockedFleet, aLeakedHandle RUN.md; auto-memory `declare-generated-writes-at-dispatch` |
| leg | 24 roster moved | aBatchedArm, aThawedCorpus, aClosedDocket, aRepatriatedFork, dUnstalledConvoy RUN.md |
| leg | 51 terminal-phase writer scan | aGraftedHelix/RUN.md (fired on the kit's OWN code at VERIFYING, a G-class firing) |

**Count never observed.**

- By check number:
  - driver: 110 − 16 = **94 (85%)**;
  - leg: 50 present − 10 = **40 (80%)**.
- By site: the fired checks own 121 driver and 96 leg sites, and the run records name one or two
  variants each (for example, only the shared-record overlap and MISSING variants of check 49's 40).
  At ≤2 fired variants per check, that is about 25 driver and 20 leg sites, so **~334/359 driver
  (93%) and ~244/264 leg (92%) sites never observed firing in a real run**.

**Caveat.** This is a lower bound on value, not an upper bound on firing. The local runlog store is
the authoritative per-check ledger, and node a has none. A run that refused, was corrected in the
same turn and recorded nothing leaves no trace. Before any retirement, the review should read the
runlog stores on nodes b, c and d.

### 2.3 What the firings were

| verdict | checks |
|---|---|
| true positive, refusal was right | driver 13, 15, 37; leg 8, 15 (the cause was a driver bug), 24 (aThawedCorpus: "exists to refuse exactly the silent scope move this was") |
| wedge or false positive, needed a repair build | driver 34 (no-ff marker, fixed by -38 and -22), 26 (owner bypassed it by hand), 32 (deadlock, aFusedCharter-4), 48 with leg 24 (mutually unsatisfiable), 89 (forced a record rotation), 49 (no legal path for a shared record; dDerivedDocket options a–c all refused), 14 (Skill vs driver drift), 18 vs leg 9 (two answers to one property); leg 7 (blocked the fleet, demoted), 23 (shrink-only ceiling raised repeatedly, then redesigned), 9 (landed runs redding the bar, aMooredAnchor-1), 51 (fired on the kit's own code) |

**Duplication is the mechanism behind several wedges.** The gotcha
`two-guards-one-question-two-answers.md` and aSealedCaravan-6 are both two refusals over one property
that drifted apart.

---

## 3. Overlap with other gates

### 3.1 Driver ↔ leg (both sides cited)

| condition | driver | leg | note |
|---|---|---|---|
| path under both SHARED_RECORDS and GENERATED_INDEXES | `unattended.sh:664` (load, exit 2) | `check-unattended.sh:1096` c38 | same library predicate `scan_shared_index_overlaps` |
| GATE_WALL below largest leg ceiling | `:6527` c85 | `:5882` c42 | near-identical message |
| clone has ≠1 remote | `:1852` c24 | `:2182` c9 | — |
| remote observation killed by bound | `:1791` c27 | `:2188` c9 | — |
| recorded BASE equals HEAD | `:2472` c16 | `:2233` c9 | — |
| no build README at BASE | `:3109` c6 | `:2469` c13 | — |
| authorization mode outside closed set | `:3236` c44 | `:2415` c19 | — |
| LANDER_MODE outside closed set | `:564` (load, exit 2) | `:3205` c45 | — |
| HANDOFF_CUTOFF missing or not a date | `:6279` c97 | `:2114` c15 | — |
| `--waive` or parked waiver names an undeclared handle | `:2736` c39 | `:2636` c17 | — |
| `asks:` not an id list | `:4580` c87 | `:2673` c19 | — |
| pass writes outside its declared set | `:12417` c49 (`--check-commit`) | `:4250` c23 | **justified**: only the commit-time one is repairable (TOOL-aWindowedPass-3) |

**Why the leg re-checks.** The leg re-grades what the run wrote because a run could hand-edit its own
`RUN.md` (TOOL-dDerivedDocket-18). That rationale is real for the authorization and mandate rows. It
is **not** real for conf rows: `.unattended.conf` is a committed file both sides read. Charter §9's
"Sanitize untrusted input at the WRITE boundary, once; trust storage at render" argues for one side
on the conf rows.

### 3.2 Driver or leg ↔ another merge-bar leg

| refusal | other leg covering it (`tools/gate-legs.json`) |
|---|---|
| driver `:12481` c49 "spec-token checker reds" | `spec tokens (a spec's own names resolve)`, `python {prefix}/check-spec-tokens.py`; the driver re-runs that leg inside `--dispatch` |
| driver `:3414` c20 README units pair malformed | `build README slot contract`, `gen_build_index.py --check-format` (partial: the slot contract grades the README shape, the driver grades working copy against BASE) |
| leg `:3051` c10 shipped VERBS carrier vs installed copy drift | `receipt sync (installed files match the receipt)` and `unattended skill wiring` (`adopt-unattended.sh --check`) cover the installed-copy-vs-shipped class; **verify** the receipt lists the verb carrier before retiring |
| leg c28 parser certification (31 sites, `:4891–5357`) and `:5121` inlined parser drift | `python resolver (behaviour + inline parity + idiom ban)` already certifies the inline-copy class, for `resolve_python` only. A parser self-test is the natural home for c28; it is not on the leg today |
| leg c8 `:2148` generated region must be empty | the header (`check-unattended.sh:44-48`) says README freshness is hygiene check 9's, deliberately not duplicated. Not an overlap: the checks are distinct |
| leg c37 `:2771` folder anchors another build's id | memory hygiene id checks (14 and the corpus-ids leg) grade id ownership; **verify** before retiring |

---

## 4. Retirement review design

### 4.1 Criteria

A site is a **retirement candidate** only when every one of R1–R4 holds:

- **R1, never fired.** There is no real-run evidence in run records, BACKLOG, gotchas or DECISIONS,
  and none in the local runlog store of any node. A firing in the site's own suite or an acceptance
  ledger does not count.
- **R2, no incident provenance.** The site cites no record whose Goal shows an observed occurrence.
  A review-constructed finding counts as hypothetical.
- **R3, the condition survives elsewhere.** One of these must hold:
  - (a) another refusal or leg still asserts the same predicate, cited by line (§3); or
  - (b) the site is a V-variant whose condition survives in the consolidated helper; or
  - (c) the site is G or F and its class is held by one structural check that spawns no driver.
- **R4, not security-shaped.** The site does not guard self-authorization, git object or config
  substitution, record forgery at the write boundary, or a §9 surface. These are never candidates,
  whatever R1–R3 say. Forgery guards consolidate (R3b); they are never retired.

**Consolidate, don't retire** (a cheaper class, same review):
- **V-families** (missing run-state, required flags, field shape) become one declared per-verb table
  (`VERB_REQUIRES`, `VERB_FIELDS`) that a single helper enforces. Arm the helper once per family,
  plus one in-process structural check that every verb's parsed flags route through it. The
  dDerivedDocket BACKLOG already proposes "a declared per-verb required-flag table in the driver
  that renders the synopsis and that check 26 joins against every Skill invocation".
- **G-liveness** becomes one `require_population <name> <value>` helper.
- **Doc-parity** joins become generated carriers: render the Skill and protocol tables from the
  driver declarations and byte-compare them. This is charter §7's "Single source of truth →
  generated artifacts → parity gate" and §12's "commit + parity-gate an artifact ONLY when a
  cross-layer consumer must read it". One byte compare replaces N join branches.

### 4.2 Who decides

**The owner**, per batch. The agent may only *propose* a candidate list with the evidence columns
filled. This mirrors the existing rule that spec-audit opt-in is owner-only (auto-memory
`spec-audit-is-the-owners-opt-in`), and the charter's rule that a raised floor or waiver needs a
dated, attributed reason. No retirement rides an unattended run's mandate.

### 4.3 How a retirement is recorded, in one commit per batch

1. **`memory/DECISIONS.md` row** (append-only supersession):
   `TOOL-<slug>-N · RETIRES <gate> check <n> "<signature head ≤60 chars>" (×k sites) · R1 <evidence query + node stores read> · R2 <provenance ids, none incident> · R3 <surviving predicate file:line | helper | structural check> · supersedes <originating id>`.
   The originating record stays; the new row supersedes it, as the charter requires.
2. **`ARMS_FLOORS`** (`.memory-tree.conf:581`) is lowered in the same commit, with a comment line
   naming the DECISIONS id. This is the path `check-arms.py:820` already asks for ("lower the floor
   in a commit that says why") and the repo has never used.
3. **Arm removal** from `<stem>.test.sh`, the same commit, so `check-arms` sees no armed-but-absent
   signature.
4. **`unarmed-branches.txt` row removal**, central or sidecar, when the site was pinned.
   `check-arms` already reds a pin whose branch disappeared, so the removal is forced.
5. **No tombstone.** A retirement must not add a refusal that polices the retired surface (cf.
   `check-unattended.sh:3953` c23, `:6022`/`:6024` c47, the `--emit-ceiling` argv refusal). If a
   retired conf key needs migration, it gets one generic `RETIRED_KEYS` table line handled by an
   existing branch, not a new numbered one.

### 4.4 The check that proves nothing load-bearing went

- **Surviving-predicate assertion (static, in-process).** For each R3a row, the review's checker
  greps the cited surviving site's signature at HEAD. A retirement whose cited survivor no longer
  exists reds. This is the DECISIONS-row join §7 asks for ("a gate's own header states what it does
  NOT check"). It belongs in `check-arms.py` as a `--retirements` mode reading the DECISIONS rows,
  costing one process.
- **Mutation replay of the retired arm.** The review runs the deleted arm's *fixture* once against
  the post-retirement tree, as a slice (auto-memory `slice-a-suite-to-debug-one-arm`). It must still
  produce a refusal from the surviving site, or from the consolidated helper. The output, or the
  `UNATTENDED check M FAILED` line it produced, goes into the DECISIONS row. This is the charter's
  "a new gate is not landed until its failing case has been observed", applied in reverse.
- **No-silent-pass guard.** The run-record grep from §2 is re-run as part of the review, against
  every node's local runlog store, so R1 is re-measured rather than remembered.

### 4.5 Cadence

- **On every kit minor bump of `unattended`**, or monthly, whichever comes first, the agent emits a
  candidate list by the method in §1–§2. Generate it rather than hand-write it: the extraction is
  ~100 lines of Python and needs no suite run.
- **Mandatory when the budget in §4.6 is hit.** The review is the only way to raise the budget.

### 4.6 Growth budget

- Add `REFUSAL_CEILINGS="tools/unattended/unattended.sh:<n> tools/unattended/check-unattended.sh:<n> …"`
  beside `ARMS_FLOORS`, read by `check-arms.py --check`. A gate's site count above its ceiling reds
  the bar.
- **Raising the ceiling** takes a dated, attributed reason line, the same shape as the lexicon kit's
  unfreeze line (charter §12: "one dated, attributed, REASONED line, refused without one"), naming
  the review that ran.
- **Seeding** at today's census would freeze the problem in place. Instead, seed it at today's census
  *minus the approved consolidation*. The ceiling then becomes the review's output, not its input.
- **Floor and ceiling** together form a band. A deleted guard still reds through the floor, and
  unbounded growth reds through the ceiling.
- **New-site cost pricing.** Require each new `fail <n>` site's commit to name its class from §1.1,
  and refuse a new **V** site outright: extend the family table instead. This is the "decide the
  extension pattern before the SECOND instance" rule (§12), which the per-verb variants already
  broke.

---

## 5. Estimated cost effect

### Basis

- **Driver suite.** The whole reading is 17,142 s (pooled, `90a6f6fae`). It makes 940 `$(run`
  driver calls, about **18.2 s per call** including fixture build, and 2.6 calls per site
  (939/359).
- **Leg suite.**
  - The shard readings in `tools/run-gates/selftest-budgets.txt` sum to about 10.6 ks serial. That
    is 1,301 + 1,147 + 925 + 1,407 + 1,127 + 1,059 + 1,546 + 2,083.
  - The TOOL-aGraftedHelix-34 re-cut added sections worth about 8.9 ks more, for **~19.5 ks**
    serial in total.
  - The suite makes ~431 leg invocations, with about 1.6 per site. The budget comments put a
    conforming-tree leg run at 16–22 s, which gives **~22–45 s per invocation** including fixture.
- **Range.** The low end assumes one invocation per retired site at the bare-call cost (usage
  refusals exit early). The high end assumes the per-site average.

| candidate set | sites | driver suite saved | leg suite saved |
|---|---|---|---|
| A. V-family consolidation (missing run-state 23, required flag 36, field shape ~37, minus ~6 helper arms kept) | ~90 driver | 90×1×18 ≈ **1.6 ks** to 90×2.6×18 ≈ **4.3 ks** | — |
| B. F/G internal-environment branches to one exit-2 helper plus one structural check (c27 mktemp, c29, c56 ×2, c69, c88, c110, c111, …) | ~11 driver | 0.2–0.5 ks | — |
| C. Conf-validation duplicates, keeping the library predicate on one side (§3.1 rows 1, 2, 3, 4, 8, 9) | ~8 (split) | ~0.1 ks | ~0.3 ks |
| D. Leg G-liveness to one `require_population` helper (48 sites, ~6 kept) | ~42 leg | — | 42×1.6×22 ≈ **1.5 ks** to 42×1.6×45 ≈ **3.0 ks** |
| E. Leg c28 parser certification to one in-process parser self-test (31 sites) | ~31 leg | — | **1.1–2.2 ks** |
| F. Leg doc-parity joins to generated Skill/protocol tables plus one byte compare (~40 of the 75 matched; the rest are G) | ~40 leg | — | **1.4–2.9 ks** |
| **Total** | ~220 of 623 sites (35%) | **~1.9–4.9 ks (11–28% of 17.1 ks)** | **~4.3–8.4 ks serial (22–43% of ~19.5 ks)** |

Notes on the totals:

1. **Wall clock is sharded, the work is not.** Both suites run 8-wide, so wall ≈ the longest shard.
   The serial saving shows up as less contention on node a, where the budgets record that
   contention dominates the readings. It does not reduce wall proportionally unless the shards are
   re-cut afterwards.
2. **The H class is not in the totals.** It is ~245 sites, never fired, with no incident provenance.
   If the owner retired even a third of the non-security H sites through R1–R4, roughly 60 driver
   and 20 leg sites, a further **~1.1–2.8 ks** (driver) and **~0.7–1.4 ks** (leg) would come off.
3. **The estimates are proportional, not measured.** Per-site cost varies by orders of magnitude:
   leg shard 8 alone is 2,456 lines holding 139 leg runs. The review's first act should be a
   per-arm timing of the candidate arms, using the existing `--attribute` and slicing tools, before
   the owner rules. That is the "measure the metric the owner named" lesson in auto-memory.

---

## 6. Candidate list (the review's first batch, for the owner)

| # | gate · check · line(s) | class | fired in a real run? | overlap / survivor | proposed action |
|---|---|---|---|---|---|
| 1 | driver · c10/37/43/47/48/49/51/52/88 · 2229, 5149, 5330, 5691, 5868, 6160, 6241, 7193, 7469, 7588, 7824, 8159, 9744, 9775, 11417, 11513, 11714, 11780, 11839, 12077, 12108, 12140, 12429 | V (missing run-state, 23 sites) | no | one `require_run_state` helper | consolidate: 1 arm plus a structural route check |
| 2 | driver · 11 checks · 2738, 5698, 5730, 5885, 5900, 5908, 5944, 7589, 7590, 7614, 9854, 11418, 11515, 11521, 11536, 11539, 11548, 11626, 11652, 11661, 11715, 11716, 11781–3, 11840–1, 12069–70, 12095–7, 12149, 12156, 12317, 12433 | V (required flag, 36) | no (check 14 unknown-argument did fire, and is not in this set) | `VERB_REQUIRES` table that also renders the synopsis | consolidate |
| 3 | driver · newline/CR/separator/bypass · 2748, 2754, 5509, 5709, 5717, 5912, 5921, 5935, 6941, 6945, 7592, 8013, 9861, 9869, 11388, 11561, 11569, 11582, 11586, 11721, 11725, 11730, 11785, 11790, 11792, 11848, 11850, 11852, 11968, 11970, 11972, 12033, 12035, 12037, 12169, 12171, 12173, 12584, 12591 | V (field shape, ~37 unique) | no | one `require_record_field` at the write boundary (§9) | **consolidate, never retire**: security-shaped (R4) |
| 4 | driver · c110 1995 · c111 2019 | G (driver's own tables) | no | the closed case is the declaration; a static lint can join `CLAIM_MODES`/`CLAIM_READS` to the case arms | replace with a structural check; drop both fixture arms |
| 5 | driver · c27 1787 · c29 6688 · c56 5962, 5997 · c69 9711 · c88 7606, 7621 · c48 6421, 12201 | F (env/internal failure) | no | — | one `die_env` exit-2 helper exempt by class; drop the shim arms; c29 is already pinned unarmed |
| 6 | driver c85 6527 ↔ leg c42 5882 | D | no | identical predicate | keep one, in the library; arm once |
| 7 | driver c24 1852 ↔ leg c9 2182; driver c27 1791 ↔ leg c9 2188 | D | no | same remote-observation helper | keep the driver side (preflight); retire the leg variants |
| 8 | driver 664 (load) ↔ leg c38 1096 | D | no | `scan_shared_index_overlaps` | keep one caller's arm; the other becomes a structural "calls the predicate" check |
| 9 | driver 564 (load) ↔ leg c45 3205 | D | no | closed set read off the driver | same as 8 |
| 10 | driver c97 6279 ↔ leg c15 2114 | D | no | `HANDOFF_CUTOFF` shape | retire the leg side |
| 11 | driver c49 12481 ↔ leg `spec tokens` | D | no | the leg runs on every bar | owner call: keep only as an early warning, or drop the arm and the branch |
| 12 | leg G-liveness · 494, 508, 591, 610, 634, 875, 882, 892, 899, 960, 969, 981, 1014, 1017, 1174, 2146, 3039, 3049, 3062, 3106, 3199, 3225, 3422, 3459, 3544, 3556, 3613, 3629, 3653, 3729, 3958, 4424, 4441, 4452, 4495, 4541, 4588, 4777, 4995, 5282, 5357, 5358, 5519, 5520, 5771, 5916, 6118, 6236 | G (48) | only c51 6236 fired, on the kit's own code | one `require_population` helper | consolidate (the §7 liveness rule is kept, the count is not) |
| 13 | leg c28 · 31 sites, 4891–5357 | G (code-shape / parser certification) | no | python-resolver inline-parity leg (one precedent) | move to one in-process parser self-test; leg keeps 1 branch |
| 14 | leg doc-parity · 3082, 3430, 3467, 3571, 3643, 3659, 4381, 4464, 4510, 4597, 4620, 5928, 6022, 6024, … (~40) | H (doc-parity) | c22 and c20 fired at build time | — | render the tables from driver declarations, then one byte compare (§7, §12) |
| 15 | leg c47 6022, 6024 · leg c23 3953 | tombstone | no | — | retire; policy §4.3.5 |
| 16 | driver H singletons: c75 4635, c35 5761, c51 7472, c101 6318, c81 6455, c49 12578, 12604 | H | no | none | owner review case by case (R3 fails, so these need an explicit ruling) |
| — | **NOT candidates**: driver 1735 c22, 1745 c23, 3283 c89, 3109 c6, 3236 c44; leg 2577 c19, 2469 c13, 2415 c19 | security / authorization | some fired (c89) | — | keep (R4) |

## 7. Uncertainties to resolve before the owner rules

- **Per-node runlog stores.** The stores on nodes b, c and d were not read. The node a store does not
  exist. R1 rests on prose records only.
- **Hand classification.** The incident-versus-hypothetical split depends on a keyword heuristic
  over spec Goals, calibrated on 12 records. Several "incident" ids are incidents of the kit's own
  refusals.
- **Unverified overlaps.** Rows 3.2/c10 (receipt coverage of the verb carrier) and 3.2/c37 (id
  ownership) are marked verify.
- **Proportional costs.** §5 is a proportional estimate, not a timing. Time the candidate arms by
  slice first.
