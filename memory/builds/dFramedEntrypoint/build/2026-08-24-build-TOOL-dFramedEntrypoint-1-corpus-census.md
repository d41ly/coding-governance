**Serves:** research TOOL-dFramedEntrypoint-1

*Research lens for the `dFramedEntrypoint` design pass — the authored corpus measured and classified. Produced 2026-08-24, node d, against base 9ddcc5c9. Findings in this record were subsequently adversarially verified; where the verification corrected a claim, the verification record wins.*

# Build-README corpus census — the measurement lens

Repo: `C:/projects/coding-governance/.claude/worktrees/build-readme-governance-18d6ea`
Population: `git ls-files 'memory/builds/*/README.md'`. Tracked files only. Measured 2026-08-24.

Every figure below carries the command or script that produced it. Scripts live beside this report
in the scratchpad: `census.py`, `sections.py`, `classify2.py`, `evict.py`, `check7.py`, `gen.py`.

---

## 0. Correction to the brief, before anything else

**The brief says "There are 19." There are 61.**

```
$ git ls-files 'memory/builds/*/README.md' | wc -l
61
```

Nineteen is very probably the count of READMEs carrying **zero** authored `##` sections — that number
is exactly 19, so the brief's figure looks like the complement of the interesting set rather than the
population:

```
$ python census.py census.json | tail -4
READMEs with >=1 authored ## heading: 42
61 - 42 = 19 carry none.
```

Every number below is over the full 61. If a downstream design decision was sized against 19, it is
sized against 31% of the corpus.

Two more population facts that bound the whole proposal:

```
$ for s in spec build reviews; do echo "$s $(git ls-files memory/builds/ | grep -c "/$s/")"; done
spec 265 · build 74 · reviews 148

$ git ls-files memory/builds/ | grep -v '/README.md$' | wc -l
508
```

The 61 READMEs sit on top of 508 other tracked records. Every eviction target below has somewhere to
go; there is no shortage of destinations.

---

## 1. Per-README census — all 61

Method (`census.py`): front matter = bytes through the closing `---`. **Authored** = from the byte
offset of the `# ` title line up to the byte offset of the first line equal to one of the four `gen:`
open markers (`build-index`, `build-order`, `build-edges`, `build-docs`). **Generated** = that marker
to EOF. Headings are every `##`..`######` between the title and the first marker, quoted verbatim.
| # | slug | total B | front-matter B | authored B | generated B | authored ## | verbatim headings |
|---:|---|---:|---:|---:|---:|---:|---|
| 1 | `aBoundedVerdict` | 44872 | 851 | 32946 | 11074 | 16 | ## What the measurements said <br> ## The owner's three decisions <br> ## Units — the authored roster <br> ## Cross-unit rules <br> ## The reground, 2026-08-17 <br> ## Out of scope for this build <br> ## The 2026-08-19 re-decomposition <br> ### Classification, per the build method's four states <br> ### What the audit changed about the dependency order <br> ### The trap the ratified resolution must not fall into <br> ## The unattended run, 2026-08-19 — what it built and what it cost <br> ### Why it stopped <br> ### The four parked decisions — the owner's turn this run did not take <br> ### Recommendations, in the order that unblocks the most <br> ### The twelve defects the run found by EXECUTING <br> ### What the run corrected in its own specs |
| 2 | `cBriefedPilot` | 32023 | 904 | 21350 | 9768 | 11 | ## Start here <br> ## What was found <br> ## The design <br> ### Eleven handles, not eight <br> ### Three deltas — the rest are pointers <br> ### The waiver, end to end <br> ### What the gate can and cannot see <br> ## Units <br> ## Owner decisions — RESOLVED <br> ## Residual risks <br> ## Method |
| 3 | `aRuledFrontispiece` | 26947 | 383 | 20599 | 5964 | 7 | ## What the owner decided at kickoff <br> ## Two decisions this build must not silently reverse <br> ## Where the sources actually are <br> ## Units — the authored roster (M2) <br> ## The order is TOTAL, and this build has no parallel lane <br> ## Build-level rules <br> ## Parked — four RESOLVED by the owner, one still open |
| 4 | `aPacedTurnstile` | 25500 | 467 | 18982 | 6050 | 8 | ## The measurement this build starts from <br> ### Re-measured 2026-08-20 at `43a6c13`, and the shape changed <br> ## Units <br> ## What the first unit changed for the six that follow <br> ## The re-scope — 2026-08-20, `TOOL-aPacedTurnstile-16` <br> ## Build order, and the dependency that forces each edge <br> ## Owner decisions already taken <br> ## The risk this build carries |
| 5 | `aBranchedMandate` | 22020 | 385 | 16304 | 5330 | 7 | ## Units — the authored roster (M2) <br> ## What each unit is worth on its own <br> ## Build-level rules <br> ## UNPARKED 2026-08-17 — the owner re-priced, and the park rested on a measurement error <br> ## PARKED — unit 4 (`TOOL-aBranchedMandate-3`), by the unattended run of 2026-08-17 <br> ## Owner decisions — RESOLVED 2026-08-16 <br> ## The spec audit — BLOCKED, folded at rev-3 |
| 6 | `dUnstalledConvoy` | 35745 | 997 | 16060 | 18687 | 9 | ## Measured at BASE `2dc9df35` <br> ## Defect A — a run may not rescope, so it parks and stalls <br> ## Defect B — the parallelism directive names the opposite of its own handle <br> ## Defect C — nothing observes whether a build followed its specs <br> ## Defect D — LANDED is unreachable, and a run parked before it blocks the whole fleet <br> ## Owner decisions — RESOLVED 2026-08-20 <br> ## Build-level rules <br> ## The order is TOTAL <br> ## Units — the authored roster (M2) |
| 7 | `cKeyedLaunchpad` | 17282 | 266 | 13656 | 3359 | 11 | ## Start here <br> ## The findings this build answers <br> ## Units <br> ## Owner decisions — where the manifest lives <br> ## Owner decisions — what the new gates do <br> ## How the build phase is authorized <br> ## The invariant the audit earned <br> ## The remote moved under this build <br> ## Parked <br> ## Unit index <br> ## Method |
| 8 | `aSiftedPlaybook` | 18295 | 267 | 12762 | 5265 | 6 | ## Units — the authored roster (M2) <br> ## Coverage — every audit defect to the scope item that fixes it <br> ## Build-level rules <br> ## Owner decisions — RESOLVED 2026-08-16 <br> ### The second round — four more, resolved 2026-08-16 <br> ### The last two, resolved under delegated authority 2026-08-16 |
| 9 | `aStandingWrit` | 14343 | 296 | 12428 | 1618 | 6 | ## Start here <br> ## The units <br> ## Owner decision menu — all eight RESOLVED 2026-08-11 <br> ## Parked — RESOLVED 2026-08-11 <br> ## Ratified decisions <br> ## Review record |
| 10 | `aFusedCharter` | 16490 | 286 | 11862 | 4341 | 7 | ## Measured at BASE `497d25d0` <br> ## The four cuts, and the test each failed <br> ## The order is TOTAL <br> ## Build-level rules <br> ## Owner decisions — RESOLVED 2026-08-18 <br> ### The second round — RESOLVED 2026-08-18 <br> ## Units — the authored roster (M2) |
| 11 | `aUnmannedHelm` | 13416 | 327 | 9517 | 3571 | 4 | ## Start here <br> ## The units <br> ## Ratified decisions <br> ## Review record |
| 12 | `aRelaxedShard` | 11689 | 174 | 9248 | 2266 | 7 | ## What was measured <br> ## Why rotation is finished as a remedy <br> ## What the adopters inherit <br> ## The unit set <br> ### What unit 2 found, and why it is not what it was sequenced to be <br> ## Owner decision menu <br> ## What this build found on the way in |
| 13 | `dScriptedRepeat` | 24296 | 443 | 8985 | 14867 | 8 | ## What the grounding found <br> ## The seven forks, resolved at kickoff <br> ## The owner rulings <br> ## Constraints already measured <br> ## What the research changed <br> ## The unit set <br> ## What the spec audits changed <br> ## What is deliberately NOT in this build |
| 14 | `aLoosenedCeiling` | 11007 | 237 | 8112 | 2657 | 4 | ## Why now — both live ceilings are one edit from red <br> ## Units <br> ## What the pre-build survey changed <br> ## What the round-1 spec audit changed |
| 15 | `aPrunedCeremony` | 11716 | 267 | 7867 | 3581 | 6 | ## PLAY half — gate-economy uplift for the playbook (specs) <br> ### The specs <br> ### Owner decision menu <br> ## TOOL half — gate-economy uplift for the tooling kits (specs) <br> ### The specs <br> ### Owner decision menu |
| 16 | `aTetheredRecord` | 11236 | 253 | 7573 | 3409 | 4 | ## What this build decided <br> ## Units — the authored roster (M2) <br> ## Forks — all five RESOLVED by the owner, 2026-08-17 <br> ## Status |
| 17 | `aPromptedMandate` | 12700 | 434 | 7420 | 4845 | 4 | ## Start here <br> ## The one owner turn <br> ## Units <br> ## What the spec audit changed |
| 18 | `aDeclaredBound` | 11180 | 223 | 7045 | 3911 | 5 | ## The fourth is not like the other three <br> ## What round 2 changed, and the run that found it <br> ## What the round-1 spec audit changed <br> ## Order <br> ## Units |
| 19 | `aMooredAnchor` | 8918 | 153 | 6973 | 1791 | 4 | ## Start here <br> ## The unit <br> ## Owner decision menu — RESOLVED <br> ## Review record |
| 20 | `cFinalBerth` | 8842 | 183 | 6892 | 1766 | 4 | ## Start here <br> ## The units <br> ## Owner decision menu <br> ## Review record |
| 21 | `aWrittenMethod` | 11230 | 240 | 6860 | 4129 | 6 | ## Start here <br> ## Units <br> ## State of this pass <br> ## The two passes, and why there are two <br> ## What survives pass 1 <br> ## Ratified decisions |
| 22 | `aTetheredConvoy` | 10911 | 331 | 6233 | 4346 | 2 | ## Start here <br> ## The unit map |
| 23 | `aSealedCaravan` | 8723 | 325 | 5926 | 2471 | 1 | ## Start here |
| 24 | `aDeclaredCeiling` | 7664 | 203 | 5232 | 2228 | 3 | ## Units — the authored roster (M2) <br> ## Coverage — every follow-up to the unit that discharges it <br> ## Build-level rules |
| 25 | `aShardedFloor` | 8035 | 174 | 5158 | 2702 | 4 | ## What this build does, in landing order <br> ## How it closed <br> ## Owner decision, as it stood <br> ## What this build does NOT do |
| 26 | `aTetheredScratch` | 6878 | 189 | 5025 | 1663 | 2 | ## What the spec audit changed, and why both units are at rev-2 <br> ## Units — the authored roster (M2) |
| 27 | `dClosedLexicon` | 10952 | 463 | 4942 | 5546 | 1 | ## The 2026-08-16 unattended run — classification and what it carries |
| 28 | `cTracedPromise` | 6385 | 245 | 4857 | 1282 | 3 | ## Start here — the measurement, before the change <br> ## What this build changes <br> ## The owner decision menu |
| 29 | `cSettledDocket` | 8598 | 472 | 4828 | 3297 | 5 | ## Why these six together <br> ## Units <br> ## Provenance <br> ## Risks <br> ## Non-goals |
| 30 | `cSteadyMetronome` | 5944 | 117 | 4598 | 1228 | 5 | ## Start here <br> ## The unit <br> ## Owner decision menu <br> ## Review record <br> ## What this build hit and did not fix |
| 31 | `dSettledRoster` | 5842 | 281 | 4477 | 1083 | 5 | ## Start here <br> ## How a records close-out became a kit change <br> ## The rest of the roster — rows, not units <br> ## What the closing pass would have caught, had there been one <br> ## Units — the authored roster |
| 32 | `aWalkedCorpus` | 6644 | 301 | 3708 | 2634 | 3 | ## Units — the authored roster (M2) <br> ## Coverage — every follow-up to the unit that discharges it <br> ## Build-level rules |
| 33 | `bConvergentLodestar` | 4234 | 123 | 2863 | 1247 | 2 | ## Scope at a glance <br> ## Owner scope-approval menu (the §8 forks — decide before build) |
| 34 | `aNumeralWarden` | 4185 | 179 | 2457 | 1548 | 1 | ## Start here |
| 35 | `aFerriedDossier` | 3596 | 175 | 2264 | 1156 | 4 | ## What inCMS is <br> ## The one finding that is not a defect report <br> ## Open <br> ## Work state |
| 36 | `aMeteredTurnstile` | 4129 | 244 | 2177 | 1707 | 4 | ## Why it cannot answer <br> ## What this build does <br> ## What this build does NOT do <br> ## Units |
| 37 | `aMouldedFolio` | 5276 | 195 | 2070 | 3010 | 1 | ## Start here |
| 38 | `aFoldedQuarry` | 7283 | 279 | 2034 | 4969 | 2 | ## Units <br> ## Order |
| 39 | `aScannedThrottle` | 4467 | 359 | 1813 | 2294 | 2 | ## What the measurement says <br> ## What this build does NOT do |
| 40 | `aTimedTurnstile` | 3780 | 276 | 1745 | 1758 | 2 | ### The specs <br> ### What this build does NOT do |
| 41 | `aDrainedSluice` | 6595 | 289 | 1558 | 4747 | 2 | ## Units <br> ## Order |
| 42 | `aBatchedTribunal` | 3881 | 285 | 1542 | 2053 | 1 | ## Units |
| 43 | `aCandidStub` | 2396 | 216 | 903 | 1276 | 0 | _(none — one unbroken prose block)_ |
| 44 | `aKitHardener` | 2026 | 125 | 834 | 1066 | 0 | _(none — one unbroken prose block)_ |
| 45 | `aRatchetForge` | 2348 | 126 | 704 | 1517 | 0 | _(none — one unbroken prose block)_ |
| 46 | `dNomadicAtlas` | 1621 | 111 | 588 | 921 | 0 | _(none — one unbroken prose block)_ |
| 47 | `aRootedPrefix` | 1942 | 153 | 545 | 1243 | 0 | _(none — one unbroken prose block)_ |
| 48 | `bThriftyBellows` | 1752 | 153 | 528 | 1070 | 0 | _(none — one unbroken prose block)_ |
| 49 | `cSightedPlumb` | 1529 | 111 | 523 | 894 | 0 | _(none — one unbroken prose block)_ |
| 50 | `aMendedLedger` | 6580 | 288 | 507 | 5784 | 0 | _(none — one unbroken prose block)_ |
| 51 | `aPortableWarden` | 1406 | 131 | 495 | 779 | 0 | _(none — one unbroken prose block)_ |
| 52 | `aDeployScout` | 1259 | 126 | 365 | 767 | 0 | _(none — one unbroken prose block)_ |
| 53 | `dScrubbedConduit` | 2986 | 165 | 354 | 2466 | 0 | _(none — one unbroken prose block)_ |
| 54 | `aLeanRework` | 1166 | 123 | 287 | 755 | 0 | _(none — one unbroken prose block)_ |
| 55 | `aGuardedTally` | 1909 | 111 | 270 | 1527 | 0 | _(none — one unbroken prose block)_ |
| 56 | `aBatchedLintel` | 1904 | 135 | 265 | 1503 | 0 | _(none — one unbroken prose block)_ |
| 57 | `aQuarriedLantern` | 2981 | 165 | 259 | 2556 | 0 | _(none — one unbroken prose block)_ |
| 58 | `aWireWarden` | 1250 | 107 | 257 | 885 | 0 | _(none — one unbroken prose block)_ |
| 59 | `aRuledParchment` | 1691 | 138 | 255 | 1297 | 0 | _(none — one unbroken prose block)_ |
| 60 | `bTamedTempest` | 1836 | 111 | 251 | 1473 | 0 | _(none — one unbroken prose block)_ |
| 61 | `aLeasedGauntlet` | 1632 | 115 | 243 | 1273 | 0 | _(none — one unbroken prose block)_ |

### Corpus aggregates

```
N = 61
total bytes        563 963
front-matter bytes  16 251
authored bytes     347 381   (61.6% of the corpus)
generated bytes    200 270   (35.5%)
authored: mean 5 695 · median 4 477 · min 243 (aLeasedGauntlet) · max 32 946 (aBoundedVerdict)
authored ## sections: 199 across 42 READMEs; 19 READMEs carry none
READMEs already over BUILD_README_CAP_BYTES=25600: 4
READMEs carrying the <!-- roster:units --> authored plan pair: 11
```

The distribution is not gradual. The top 6 by authored bytes hold 126 241 B — **36.3% of all authored
prose in 10% of the files**. The bottom 19 (no `##` at all) hold 8 433 B between them, median 365 B
each. The owner's complaint is a complaint about roughly ten files.

Generated-region breakdown (`gen.py`); all 61 READMEs carry all four regions:

```
build-index  126 950 B  (includes the nested build-units region)
  build-units  51 654 B
build-order    9 638 B
build-edges    7 076 B
build-docs    56 177 B
Records-table rows (build/ + reviews/ bindings rendered inside build-index): 223
```

**`build-docs` alone is 56 177 B — 28% of everything generated — and it is a flat link dump of
`spec/`, `build/`, `reviews/`.** The owner's instinct that build/reviews links belong in the specs
they serve is worth 56 177 B of generated region plus the 223 Records rows, and those two regions
already duplicate each other today: every `build/` and `reviews/` file is listed twice per README.

---

## 2. Taxonomy of authored content

`classify2.py` assigns every one of the 260 authored blocks (199 headed sections + 61 untitled
preambles) to exactly one class. **Zero unclassified.** Total accounted 342 467 B; the 4 914 B gap to
347 381 is the 61 `# ` title lines, which the section walk starts after.

| Class | sections | READMEs | bytes | % authored | Verbatim heading examples |
|---|---:|---:|---:|---:|---|
| **D — authored unit roster** | 37 | 33 | 50 980 | 14.9% | `## Units — the authored roster (M2)` · `## The unit set` · `## The unit map` |
| **A — untitled preamble** | 61 | 61 | 43 628 | 12.7% | _(no heading; the block under the `#` title)_ |
| **B — owner rulings / decision menus** | 30 | 22 | 42 369 | 12.4% | `## Owner decisions — RESOLVED 2026-08-16` · `## Owner decision menu — all eight RESOLVED 2026-08-11` · `## Ratified decisions` |
| **L1 — build description** | 21 | 20 | 41 960 | 12.3% | `## Start here` · `## What this build does` · `## Scope at a glance` |
| **F — build-level rules** | 8 | 8 | 22 260 | 6.5% | `## Cross-unit rules` · `## Build-level rules` |
| **I — research findings** | 19 | 12 | 22 077 | 6.4% | `## What was found` · `## What the research changed` · `## The findings this build answers` |
| **J — spec-audit / review narrative** | 13 | 12 | 21 865 | 6.4% | `## The spec audit — BLOCKED, folded at rev-3` · `## What the spec audit changed` · `## Review record` |
| **H — measurement / why-now** | 13 | 10 | 19 205 | 5.6% | `## What the measurements said` · ``## Measured at BASE `497d25d0` `` · `## Why it cannot answer` |
| **K — defect / run journal** | 13 | 5 | 15 687 | 4.6% | `## Defect B — the parallelism directive names the opposite of its own handle` · `### The twelve defects the run found by EXECUTING` · `## The unattended run, 2026-08-19 — what it built and what it cost` |
| **L2 — progress narrative** | 13 | 8 | 15 650 | 4.6% | `## State of this pass` · `## The reground, 2026-08-17` · ``## The re-scope — 2026-08-20, `TOOL-aPacedTurnstile-16` `` |
| **E — order rationale** | 10 | 9 | 15 541 | 4.5% | `## The order is TOTAL, and this build has no parallel lane` · `## Build order, and the dependency that forces each edge` · `## Order` |
| **C — parked / open forks** | 7 | 7 | 13 467 | 3.9% | `## Parked — four RESOLVED by the owner, one still open` · ``## PARKED — unit 4 (`TOOL-aBranchedMandate-3`), by the unattended run of 2026-08-17`` · `## Forks — all five RESOLVED by the owner, 2026-08-17` |
| **L3 — build-method boilerplate** | 4 | 4 | 6 763 | 2.0% | `## Method` · `## The two passes, and why there are two` · `### Classification, per the build method's four states` |
| **G — non-goals** | 8 | 8 | 6 116 | 1.8% | `## Non-goals` · `## Out of scope for this build` · `## What is deliberately NOT in this build` |
| **M — risks** | 3 | 3 | 4 899 | 1.4% | `## The risk this build carries` · `## Residual risks` · `## Risks` |

### Verdict on the taxonomy

The owner's word "dumping ground" is measurably accurate but **misattributed**.

The classes the owner names by name — B (owner-decision logs), C (the forks), I (what the research
changed / what the grounding found), J, K (defect records), L2 — total **131 115 B, 37.7% of authored
prose**. Real, and worth removing.

But the single largest class is **D, 50 980 B across 33 of 61 READMEs**, and it is not irrelevant
prose at all. It is a **hand-maintained duplicate of a table the generator already renders** into
`gen:build-units` (51 654 B). The corpus is carrying the same roster twice, in nearly identical
volume, and only 11 of the 33 authored rosters are even inside the `<!-- roster:units -->` plan pair
the generator knows about. That is the cheapest and least controversial byte on the table, and the
owner's list does not mention it.

Second-largest miss: **L3 (6 763 B) restates `memory/guides/BUILD-METHOD.md`**, which
`/session-kickoff` already loads at hand-back. Two answers to one question, in the repo whose charter
bans exactly that.

---

## 3. Class → slot mapping

Canonical spec sections cited are the ten in `tools/memory-tree/check-memory-hygiene.sh:729`
(`SPEC_CANON` / `SPEC_CANON10`), which check 12 enforces — not a list I invented.

| Class | S3 desc | S4 improve | S5 detriment | S6 rules | Verdict / where the homeless goes |
|---|:-:|:-:|:-:|:-:|---|
| **A — preamble** | ✅ primary | partial | partial | — | **Fits.** Every preamble already opens with the problem statement. |
| **L1 — description** | ✅ primary | ✅ | — | — | **Fits.** `## What this build does` is slot 4 nearly verbatim in 8 READMEs. |
| **F — build rules** | — | — | — | ✅ exact | **Fits, 1:1.** The only class with a clean slot. |
| **H — measurement** | — | — | ✅ | — | **Half fits.** The *conclusion* ("this repo cannot answer whether that is true") is slot 5. The **measurement tables** — BASE shas, budget margins, row counts — have NO home. → spec **§1 Goal** (grounding) or a `build/` journal record. |
| **G — non-goals** | — | — | — | — | **Homeless and cheap (6 116 B).** Per-unit exclusions → spec **§3 Non-goals**. A BUILD-level exclusion belongs to no single spec. Recommend folding into slot 6 or adding an optional slot 5b. |
| **D — unit roster** | — | — | — | — | **Homeless by construction — it IS slot 7.** Delete outright. The generator already renders it. |
| **E — order rationale** | — | — | — | partial | **Split.** ORDER # → slot 7 (generated). Per-edge *why* → spec **§4 Design**. Cross-unit constraints ("units 6 and 8 CO-LAND", "unit 8 is CONDITIONAL on unit 7") belong to no spec → **slot 6**. |
| **B — owner rulings** | — | — | — | — | **Homeless. Delete from the README.** Resolved forks → spec **§8 Open questions**. Build-wide rulings → a `build/` journal record. **The corpus has already proved this works**: `dScriptedRepeat` moved all four rounds verbatim to `build/2026-08-20-build-TOOL-dScriptedRepeat-1-owner-rulings.md` and kept an 811 B pointer. |
| **C — parked / open forks** | — | — | — | — | **Homeless AND partly load-bearing — see §7.** Resolved parks → spec §8. A build-level park taken by an unattended run has no owner anywhere in the proposal. |
| **J — spec audit** | — | — | — | — | **Homeless. Delete.** Already duplicated by 148 tracked files under `*/reviews/` (4 166 308 B). Rev history → spec **§9 Revision log**, which check 12 already requires. |
| **K — defect / run journal** | — | — | — | — | **Homeless.** Per-defect narrative → the **§1 Goal** of the unit that fixes it. Run-cost narrative → a `build/` journal record (74 exist). |
| **I — research findings** | — | — | — | — | **Homeless. Delete from the README.** → `build/` journal; `dScriptedRepeat` already does exactly this in 208 B. Some is spec **§10 Reuse audit**. |
| **L2 — progress narrative** | — | — | — | — | **Homeless and DERIVABLE. Delete with no destination.** `## State of this pass`, `## Status`, `## Work state` restate what slot 7's status column renders. |
| **L3 — method boilerplate** | — | — | — | — | **Homeless. Delete with no destination.** Restates `memory/guides/BUILD-METHOD.md`. |
| **M — risks** | — | — | — | — | **Homeless.** → spec **§5 Production-readiness checklist** or **§8**. |

**Nine classes totalling 148 893 B — 42.9% of authored prose — have no home in the eight-slot
proposal** (B, C, G, I, J, K, L2, L3, M). Of those, 22 413 B (L2 + L3) delete outright with no destination needed. The remaining
**126 480 B has to land somewhere, and the proposal does not say where.** That is the design pass's
largest open question and it is not a small one.

Add class **D** (50 980 B), which is homeless only because the generator already renders it, and the
classes the proposal does not give an explicit home to total **199 873 B — 57.5% of all authored
prose**.

---

## 4. The eviction, measured

Assumption: slots 3/4/5/6 survive on classes **A**, **L1**, **F**; everything else leaves.
Script: `evict.py`.

```
corpus authored now   347 381 B
corpus evicted        239 533 B   (68.9% of authored prose)
corpus total now      563 963 B
corpus total after    327 096 B   (-42.0%)
```

Ten heaviest evictions:

| slug | total now | authored | A+L1 kept | F kept | **evicted** | total after |
|---|---:|---:|---:|---:|---:|---:|
| `aBoundedVerdict` | 44 872 | 32 946 | 914 | 8 255 | **23 777** | 15 011 |
| `aPacedTurnstile` | 25 500 | 18 982 | 331 | 0 | **18 651** | 7 586 |
| `cBriefedPilot` | 32 023 | 21 350 | 3 625 | 0 | **17 725** | 11 900 |
| `aRuledFrontispiece` | 26 947 | 20 599 | 708 | 3 028 | **16 863** | 9 689 |
| `dUnstalledConvoy` | 35 745 | 16 060 | 419 | 3 215 | **12 426** | 22 224 |
| `aBranchedMandate` | 22 020 | 16 304 | 2 892 | 1 801 | **11 611** | 9 248 |
| `cKeyedLaunchpad` | 17 282 | 13 656 | 2 187 | 0 | **11 469** | 5 492 |
| `aFusedCharter` | 16 490 | 11 862 | 851 | 1 730 | **9 281** | 8 173 |
| `aRelaxedShard` | 11 689 | 9 248 | 407 | 0 | **8 841** | 3 891 |
| `aSiftedPlaybook` | 18 295 | 12 762 | 2 451 | 2 033 | **8 278** | 9 181 |

`total after` applies the §6 budgets (S3 900 B, S4 500 B, S5 500 B, S6 1 800 B, +140 B headings) and
holds the generated region constant.

### Against `BUILD_README_CAP_BYTES=25600`

Declared at `tools/memory-tree/check-memory-hygiene.sh:45`.

```
over cap TODAY:  4  — aBoundedVerdict 44872 · dUnstalledConvoy 35745 · cBriefedPilot 32023 · aRuledFrontispiece 26947
over cap AFTER:  0
largest after:   dUnstalledConvoy 22 224 B (87% of cap)
```

**Headroom becomes a renderer problem, not a prose problem.** After the eviction the largest file is
`dUnstalledConvoy` at 22 224 B, of which 18 687 B (84%) is generated. `dScriptedRepeat` follows at
17 000 B with 14 867 B generated (87%). Any future cap pressure lands somewhere no author can fix.

### Which `memory/project/curation-debt.txt` rows drain

The brief says "4-5 rows". There are **7** uncommented rows. Byte cap = check 6; entry cap
(`BUILD_README_ENTRY_CAP_CHARS=350`) = check 7. `check7.py` reproduces check 7's exact semantics —
front matter, fenced blocks, `^#` lines and table separator rows are all exempt, per the awk at
`check-memory-hygiene.sh:512-545`.

| debt row | why it is listed | drains? |
|---|---|---|
| `memory/builds/aUnmannedHelm/README.md` | one AUTHORED 412-char line, L78, inside `## The units` (class D) | **✅ FULLY. The only one.** |
| `memory/builds/aBoundedVerdict/README.md` | check 6 (44 872 B) + 5 authored offenders + **5 generated offenders** (max 584 ch) | ⚠️ Check 6 drains → 15 011 B. All 5 authored offenders sit in evicted classes (L33/L34 H-measurement, L96 D-roster, L283 L3-method, L338 B-owner-rulings). **The 5 generated ones remain.** Row stays. |
| `memory/builds/cBriefedPilot/README.md` | check 6 (32 023 B) + **2 generated offenders** (592, 593 ch) | ⚠️ Check 6 drains → 11 900 B. **Zero authored offenders.** Row stays on check 7. |
| `memory/builds/aRuledFrontispiece/README.md` | **3 generated offenders** (415, 415, 416 ch) | ❌ No. Its own debt note already says "renderer-shaped". |
| `memory/builds/dUnstalledConvoy/README.md` | **6 generated offenders** (438–463 ch) | ❌ No. Debt note already says "Renderer-shaped". |
| `memory/builds/aDrainedSluice/README.md` | **1 generated offender** (394 ch) | ❌ No. Authored max line is 202 ch. |
| `memory/backlog/TOOL.md` | not a build README | ❌ Out of scope entirely. |

**One of seven rows drains. Two more shed their check-6 leg but keep the row on check 7.** Every
surviving offender is a line the renderer emits. If draining curation debt is a goal of this build,
the README slot contract is the wrong lever — the roster/bindings row shape is.

Incidental finding while measuring this: `aRuledFrontispiece`'s P7 park states
"the shrink-only `memory/project/curation-debt.txt`, which is empty today". It has seven rows. That
is authored README prose that rotted, in a build whose subject was rot.

---

## 5. Sample-write — slots 3/4/5/6 for three real builds

Every sentence below is sourced from what the README or its specs already say. Nothing is invented;
where I compressed, the source phrase survives. Byte counts are MEASURED on the slot body with the blockquote
prefix stripped, excluding the slot heading (`verify_samples.py`).

### 5a. `dScriptedRepeat` — 24 296 B today, 8 985 authored, 8 headings

**Slot 3 — immutable description (587 B, measured)**

> Playbook mode is a third authorization discipline for the unattended kit. It creates
> fully-functional playbooks — detailed checklists of instructions and steps for producing repeating
> content (plans, images, videos, articles, web pages, websites, tests) — and follows an existing
> playbook to the letter to create the number of pieces the owner needs. With no playbook it
> researches the topic and the code it must relate to, then specs a new checklist from a PLAYBOOK
> TEMPLATE, itself researched and reviewed for a format that excludes ambiguity. It **refuses
> ordinary code builds.**

_Source: the `**The owner's ask, verbatim.**` preamble block, compressed from 1 108 B. Nothing was
added._

**Slot 4 — expected improvements (343 B, measured)**

> - Repeating content gets one authorization discipline instead of being re-improvised per run.
> - Composition failures become visible: the Definition of Done measures the SET, not each piece, so
>   N monocultured pieces can no longer report GREEN.
> - Playbook improvements surfaced during a build are logged and put to the owner rather than lost.

_Source: the preamble ask; `## What the research changed` ("every composition failure in the
reference corpus was found by measuring the SET, never a piece")._

**Slot 5 — detriments if not built (351 B, measured)**

> - Every content run re-improvises its checklist, and the two reference playbooks already disagree
>   on what a "step" is.
> - The reference corpus the template derives from contains four measured instances of fork 5's own
>   defect, which any new playbook inherits.
> - Piece-wise green stays the only signal, so a monocultured set ships reporting success.

_Source: `## What the research changed`, verbatim phrases._

**Slot 6 — build-level rules (435 B, measured)**

> - No unit writes a budget figure into this file. Every one re-measures from
>   `tools/check-template-size.sh` and `python tools/memory-tree/corpus_ids.py --report`.
> - Raising `BUILD-METHOD.md`'s stated 22 KB / 290-line budget is an owner fork, never an edit.
> - Units 6 and 8 CO-LAND: 6's piece count consumes 8's diff population. Units 6 and 7 CO-LAND:
>   `CORE_FLOOR`'s Definition-of-Done half moves ONCE, from eight to ten, not twice.

_Source: `## Constraints already measured` and `## The unit set`. **Note this build has no
`## Build-level rules` section today** — the rules were scattered across two other sections. The slot
finds them._

**What leaves:** 7 503 B (83.5% of its authored prose) — the grounding pointer, the seven forks, the
owner rulings, the research narrative, the unit set table, the spec-audit summary, the non-goals.
Four of those seven are already pointers to `build/` records, so their destination is proven.
The non-goals (1 053 B, `## What is deliberately NOT in this build`) are the one real loss.

---

### 5b. `dUnstalledConvoy` — 35 745 B today, 16 060 authored, 9 headings

**Slot 3 — immutable description (452 B, measured)**

> An unattended run may change its own scope, dispatch disjoint work concurrently, evidence what it
> built, and reach a terminal state it can actually get to. Four breaking issues in both unattended
> build modes: a run may not rescope, so it parks and stalls; the parallelism directive names the
> opposite of its own handle; nothing observes whether a build followed its specs; and `LANDED` is
> unreachable, so a run parked before it blocks the whole fleet.

_Source: the `#` title verbatim plus the preamble and the four `## Defect X` heading clauses._

**Slot 4 — expected improvements (344 B, measured)**

> - A run can retire or supersede a unit inside its stated goal instead of stalling on a scope call.
> - `LANDING` becomes terminal-reachable, so a locally-merged build stops counting live against every
>   later run on the fleet.
> - Spec conformance becomes observable: an acceptance ledger joins each built unit back to its own
>   numbered criteria.

_Source: `## Owner decisions — RESOLVED 2026-08-20` and Defects A, C, D._

**Slot 5 — detriments if not built (436 B, measured)**

> - 5 of the 13 run-state files in this tree are `ABORTED`, and **all 5 aborted for exactly these four
>   causes** — 38 per cent of every run ever made here.
> - `PHASES_TERMINAL="LANDED ABORTED"` omits `LANDING`, so leg check 7's `nlive <= 1` counts one stuck
>   run against every later run on the fleet.
> - A full green bar with complete work stopped anyway: `cBriefedPilot` refused to decide whether 16
>   of 22 units is a landable build.

_Source: `## Measured at BASE 2dc9df35` and the quoted abort reasons in Defects A and D. **This is the
strongest slot 5 in the corpus** — the detriment is measured, not argued._

**Slot 6 — build-level rules (1 094 B, measured; six bullets at 142–204 B)**

> - **Every unit touching a budgeted carrier re-measures from its gate.** `BUILD-METHOD.md`'s SEVEN-line
>   headroom binds units 4 and 8, which both edit it; if the pair does not fit, that is a fork.
> - **A new CHECK inside an existing gate, never a new gate LEG.** A leg costs the manifest, a kit
>   descriptor row and a coverage assert; a check costs an `ARMS_FLOORS` bump and one arm per `fail`
>   site.
> - **A kit-shipped document and this repo's installed copy are ONE mechanism.** Any unit whose
>   Files-touched names a kit template moves that template's render in the SAME commit.
> - **Every new check gets its failing case OBSERVED before it lands** — stage the break, confirm RED,
>   unstage. Checks grading records the run itself writes owe a statement of what they cannot buy.
> - **`.memory-tree.conf` is a BUILD-WIDE shared write.** Seven of thirteen units move one line range
>   of it, so no two of them may ever be dispatched as a concurrent pair.
> - **`TOOL-dUnstalledConvoy-8` is CONDITIONAL**: if the measurement records E3 or E4 as anything other
>   than CLEARED, it ships no inversion.

_Source: `## Build-level rules` (3 215 B) compressed, **plus one rule imported from `## The order is
TOTAL`** — the CONDITIONAL unit. That fact is cross-unit, belongs to no spec, and would otherwise be
evicted. See §7._

**What leaves:** 12 426 B (77.4%) — the BASE measurement table, the four defect narratives, the owner
decision table, the total-order table with its rationale, and the authored roster.

---

### 5c. `aMeteredTurnstile` — 4 129 B today, 2 177 authored, 4 headings (the small clean one)

Chosen because its four headings are already `## Why it cannot answer` / `## What this build does` /
`## What this build does NOT do` / `## Units` — the closest thing in the corpus to the proposed slot
set, written by someone who had never seen it.

**Slot 3 — immutable description (328 B, measured)**

> Two builds have already made this bar faster, and both were designed against a measurement taken by
> hand, once, and never repeated. The owner reports the bar is extremely slow and getting slower, and
> this repo cannot answer whether that is true. This build adds one instrument to the `run-gates` kit
> and uses it once, properly.

_Source: the preamble + `## What this build does`, near-verbatim._

**Slot 4 — expected improvements (352 B, measured)**

> - The instrument records a RUN rather than a leg and appends rather than overwrites, so a
>   measurement next month is comparable to this one.
> - It classifies the bar into a regime, so the next fix is chosen from a measurement instead of a
>   guess.
> - Adopters get the same instrument: regime classification is a property of any bounded-pool gate
>   bar.

_Source: `## What this build does`, verbatim._

**Slot 5 — detriments if not built (366 B, measured)**

> - `<git-dir>/gate-timings.tsv` is a dispatch hint read as a profile: last-write-wins across runs at
>   different pool widths, with no run identity, timestamp, width, commit or host.
> - It never evicts a renamed leg — measured on node `a` at commit `56b945c`, 88 rows against 85
>   manifest legs.
> - Reading that file as a profile is how a stale number becomes a plan.

_Source: `## Why it cannot answer`, verbatim including the measurement._

**Slot 6 — build-level rules: EMPTY.**

> _(none)_

_The build has no cross-unit rules; it has one unit. `## What this build does NOT do` (324 B) is a
non-goal, not a rule, and has **no slot**. Under the proposal it would go to the spec's §3._

**What leaves:** 1 326 B (60.9%) — almost all of it the authored roster and the non-goals.

### The reality check

**All three fit.** No slot needed to invent content, and in two of the three (`dScriptedRepeat`,
`aMeteredTurnstile`) the source text was shorter than the slot budget. The one thing the proposal
**cannot carry in any of the three** is the build-level non-goal — present in all three, homeless in
all three, and cheap (324–1 053 B). The second thing is `dUnstalledConvoy`'s CONDITIONAL unit, which
I had to smuggle into slot 6.

---

## 6. Recommended budgets, derived from the measured distribution

| Slot | Budget | Derivation | Builds that fit as-written |
|---|---:|---|---:|
| **3 — immutable description** | **900 B** | The A-preamble distribution is min 52 · p25 329 · **median 525** · p75 802 · p90 1 409 · max 3 579. 900 B sits between p75 and p90. | **49 of 61** on preamble alone; 35 of 61 if `## Start here` is folded in too. All three §5 samples fit: 452 / 587 / 328 B measured. |
| **4 — expected improvements** | **500 B** | No existing class is a clean analogue. The corpus's own **shortest disciplined bullets measure 150–190 B** (F-section min 150, p25 244). 500 B = 3 bullets at ~165 B, which is exactly the shape of `## What this build does`. | Not directly measurable (slot is new). All three §5 samples measured 343 / 344 / 352 B — written from real source, none needed 500. |
| **5 — detriments if not built** | **500 B** | Same derivation, symmetric with slot 4. Cross-check: the G-nongoals class, the only existing SHORT bulleted class, is min 228 · p25 324 · **median 597**. | 4 of 8 existing non-goal sections fit under 500 B as written. All three §5 samples measured 351 / 436 / 366 B. `dUnstalledConvoy`, the richest detriment in the corpus, used 436 of 500. |
| **6 — build-level rules** | **1 800 B** | 45 bullets exist across the 8 F sections: min 150 · p25 244 · **median 360** · p75 693 · max 1 520. **1 800 = 5 bullets at the median.** Five is also the observed mode: the 8 sections carry 3, 4, 4, 5, 5, 7, 7, 10 bullets. | **56 of 61** (53 have no such section at all). Of the 8 that do: `aWalkedCorpus` 885, `aDeclaredCeiling` 1 313, `aFusedCharter` 1 730 fit. `aBranchedMandate` 1 801 misses by 1 byte. `aSiftedPlaybook` 2 033, `aRuledFrontispiece` 3 028, `dUnstalledConvoy` 3 215, `aBoundedVerdict` 8 255 do not. **Cross-check from §5b:** a disciplined rewrite of `dUnstalledConvoy`'s 3 215 B section came to 1 094 B in six bullets of 142–204 B, so 1 800 is headroom rather than a squeeze. |

**Total authored budget per README: 3 700 B + title + headings ≈ 3 950 B.** Against today's authored
median of 4 477 B that is a 12% cut for the median build and a 88% cut for `aBoundedVerdict`. Against
the 25 600 B cap it leaves 21 650 B for the generated regions, which is 3 000 B more than the largest
generated region in the corpus today (`dUnstalledConvoy`, 18 687 B). **The cap stops binding on
authors and starts binding on the renderer, with about 16% of headroom.** That is worth saying out
loud in the spec, because it changes who can fix a red check 6.

### The one budget I would argue about

**Slot 6 at 1 800 B will not hold `aBoundedVerdict`, and that is the correct outcome, not a problem.**
Its `## Cross-unit rules` is 8 255 B — the largest single authored section in the corpus, 4.6× the
budget — and it contains this, inside a bullet:

> **Its own history, because the rule changed twice in one day and a reader deserves to know why.** It
> read "moves exactly once" until the morning of 2026-08-20…

That is a change log living inside the one section the owner intends to keep. **Slot 6 will inherit
the dumping-ground problem unless the cap is hard and gated**, because it is the only remaining
authored slot with no obvious ceiling in the author's mind. Three of its ten bullets measure 1 480,
1 489 and 1 520 B each — any one of them nearly fills the whole budget.

**Recommend a per-bullet cap as well as a section cap**: ~400 B per bullet (just above the measured
median of 360) and 1 800 B for the section. A single-figure section cap lets one 1 520 B bullet
survive, and that bullet is the failure mode.

---

## 7. Load-bearing content the owner called irrelevant

Three findings. I am not defending the volume — I am defending specific facts inside it.

### 7.1 Cross-unit ordering constraints — CONFIRMED load-bearing, 15 541 B, 9 READMEs

Class **E**. The owner keeps the ORDER # (generated, slot 7) and drops the rationale. The ORDER #
tells a resuming session *what* order; it cannot tell it *whether a unit ships at all*.

Evidence, `memory/builds/dUnstalledConvoy/README.md`:

> `TOOL-dUnstalledConvoy-8` is CONDITIONAL: if the measurement records E3 or E4 as anything other than
> CLEARED, it does not ship an inversion, and the build records the loss per M12 rather than shipping
> the rule anyway. The owner's answer authorized the inversion ON the measurement, not instead of it.

And `memory/builds/dScriptedRepeat/README.md`:

> Units 6 and 8 land together because 6's piece count consumes 8's diff population and counts the
> wrong thing without it.

Neither fact belongs to a single spec — a CO-LAND constraint is a property of a *pair*, and §4 Design
in either spec would be the second answer to one question. A session resuming `dUnstalledConvoy` at
unit 7 that sees only "8 comes after 7" will build the inversion. **Fix: slot 6 is the right home;
say so explicitly in the slot's definition, or the class is silently deleted.**

### 7.2 Build-level non-goals — CONFIRMED load-bearing, 6 116 B, 8 READMEs

Class **G**, and it is the cheapest class in the taxonomy at 1.8%. `dScriptedRepeat` states the
argument for its own existence in its own first line:

> Named here because the research raised each one and an unstated exclusion reads as an oversight.

Spec §3 Non-goals is per-unit and cannot hold "no content producers in this build" or "no migration
of the reference playbooks", which are properties of the *build*. Three of the eight are one-liners
(228, 320, 324 B). **Fix: an optional slot 5b at ~500 B, or explicitly admit non-goals into slot 6.**
Deleting 6 116 B to avoid one more slot is the wrong trade.

### 7.3 Live, unresolved parks — CONFIRMED load-bearing, subset of 13 467 B

Class **C**. The owner is right that *resolved* rulings are log noise; `dScriptedRepeat` has already
proved they externalise cleanly. But an **unresolved** park is live state.

`memory/builds/aRuledFrontispiece/README.md`, `## Parked — four RESOLVED by the owner, one still open`:

> **P6 · position 6 — restructuring another node's roster table.** … The first spec audit named this an
> owner item; it was then answered by a spec rather than by an owner, which is how an unasked question
> becomes a decision nobody made. The surgery unit proceeds on the reading that Option A authorises
> it, and the owner may overrule.

Slot 7's status column can render `DEFERRED`. It cannot render *who parked it, under what authority,
and what would unpark it*. Same shape in `aBranchedMandate`:
`## PARKED — unit 4 (TOOL-aBranchedMandate-3), by the unattended run of 2026-08-17` (1 978 B) — a park
taken by a *run*, not by a spec author, so no spec §8 owns it.

**Fix: this is genuinely homeless.** Either slot 7 gains a derived "open forks" line sourced from
non-terminal spec §8 sections, or a ninth slot carries live parks only, gated to drop on resolution.
Note the failure mode the corpus already recorded, in the same section:

> The closing review caught this paragraph still reading "still open" while the spec recorded it
> resolved and the code still read 1.4 — one question with three answers, in the build whose subject
> is that class.

So an authored park slot rots. **A derived one does not.** If a park must survive, derive it.

### 7.4 Classes I judge the owner is RIGHT to evict, with evidence

- **B — owner rulings (42 369 B).** `dScriptedRepeat` externalised four rounds verbatim to
  `build/2026-08-20-build-TOOL-dScriptedRepeat-1-owner-rulings.md` and kept an 811 B pointer. It works.
  One caveat the corpus itself records: that same move left four citations dangling, because the moved
  tables numbered their forks bare in the first column. The eviction needs a rule that moved records
  spell their fork numbers in prose.
- **J — spec audit (21 865 B).** 148 tracked files under `*/reviews/` totalling 4 166 308 B already
  hold this. The README carries a summary of a summary.
- **L2 — progress (15 650 B)** and **L3 — method (6 763 B).** Both derivable or already stated
  elsewhere. `## Method` restates `memory/guides/BUILD-METHOD.md`, which `/session-kickoff` loads at
  hand-back. Delete with no destination.
- **D — authored roster (50 980 B).** Not on the owner's list, and the single biggest win. Delete
  outright; `gen:build-units` renders it.

---

## 8. Questions the corpus cannot answer

- **Whether slots 4 and 5 are writable at authoring time.** All three of my §5 samples were written
  *backwards*, from a finished build's own findings. `aScannedThrottle`'s detriment ("deleting the
  canary outright moves the bar's wall clock by 0.0 %") was a measurement the build produced, not a
  premise it started from. Whether a build can state its own improvements and detriments at DoR — the
  moment the README is created — is not something 61 finished READMEs can tell you. Recommend the spec
  treat slot 4/5 as revisable-once rather than immutable.
- **Whether the 350-char entry cap should apply to the new slots at all.** Every current authored
  offender is in an evicted class, so after this build the cap would guard nothing authored.
- **Whether `build-docs` (56 177 B) should exist once the bindings move to specs.** The Records table
  and `build-docs` already list the same 74 + 148 files twice per README. That is 28% of the generated
  region and outside the eight-slot proposal's stated scope, but it is the largest single duplicate in
  the corpus after class D.
