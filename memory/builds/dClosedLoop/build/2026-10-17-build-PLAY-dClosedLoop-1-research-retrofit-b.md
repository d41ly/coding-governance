# Research: retrofitting gov's practices into an existing repository, run B

**Serves:** research PLAY-dClosedLoop-1

This is dispatch 84's return, verbatim. Its question is in
`prompts/2026-10-17-prompt-PLAY-dClosedLoop-1-1-researcher.md`, which dispatch 83 runs too, and its use is in
`build/2026-10-17-build-PLAY-dClosedLoop-1-retrofit.md`.

---

## 1. Verdict

Retrofit is a **sixth system across the layers**, like the five. It is not a layer and not an expansion. Its working core is three pieces:
- **A census at adoption.** It derives one set-keyed baseline per leg and per practice. It costs no agent tokens.
- **A drain on touch.** It is bounded per unit: a unit whose write set meets a baselined key drains it or carries it.
- **A provenance field.** Every record carries it, so a reconstructed record is marked apart.

Expansions add the rest. Observability ranks what is left by heat and drains it on a cadence. Distribution calls the census from the adopt scripts. Integrations import outside CI. The core must hold the census and the ratchet (P28): without a baseline, the code legs that have no tolerance list red on legacy no unit touched. That breaks "the core alone carries a build".

## 2. Today

| Part | What it does | Measured | file:line |
|---|---|---|---|
| Map baseline | inventory keys no dossier claims; may only shrink | 69 keys at the seed (2026-08-09) → 36 now; inventory 72 → 365, so 9.9% is unclaimed now. All 11 shrinking commits touched a dossier | `memory/map/baseline.toml:1-11` |
| Refusal of a gained key | refuses a key the merge-base lacked | landed only 2026-10-05 (`54c8d081f`); before that, "shrink-only" was a comment | `tools/codebase-map/test_codebase_map.py:13-14` |
| **Record ≠ code** | the header records one exception, the template-size rename | `b0f5247a9` also renamed `memory hygiene (20 checks)`→`(21 checks)`, which no record names | `baseline.toml:7-11` |
| drift BASELINES | set-keyed: a new id reds, and a fixed id that is still listed reds | 2 signals | `tools/drift-audit/drift_signals.py:371-403` |
| drift RATCHETS | a raised scalar pin needs an `<old> -> <new>` reason | 11 rows | `drift_signals.py:444-466` |
| Site lists | keyed by (file, arm, count), never by line; set-equal both ways | encoding 18→16 rows; substitution-fed loops 18→43; spawn idioms 292→303; unarmed branches 9→159 | `memory/project/encoding-posture-sites.txt:4-11` |
| Lexicon offender keys | `<path>\t<rule>\t<ident>`, line-free, for red attribution | 4 of 140 legs carry a `signature` | `tools/lexicon/lexicon.py:3482-3495` |
| Lexicon count pin | a scalar ceiling | `VERB_OFFENDER_PIN` went 412→1087 over 31 edits | `.lexicon.conf:268` |
| Lexicon marginal rate | offenders added per definition added | 12.0% overall; **9.1% in fresh files and 16.1% in files that predate the declaration** | `tools/drift-audit/drift_report.py:1434` |
| Red attribution | re-runs each red leg at the base: inherited or own; report-only | — | `tools/run-gates/run-gates.sh:4318-4330` |
| Leg guards | `changed()` against the merge-base | 76 of 140 legs guarded | `run-gates.sh:413` |
| Date cutoffs | exempt records dated before a key | 34 keys | `.memory-tree.conf`, `.unattended.conf` |
| Shrink watcher | `shrink_only_lists_not_shrinking` | 3 of 5 regrown; `gateable=False` | `drift_report.py:863` |
| Adoption recipes | seed the baseline; a mechanical "Serves: none" pass, then drain; a one-time affordance seed | — | `WIRE-INTO-PROJECT.md:409-420`, `:543-547`, `:2115` |
| govkit research | installs kits into a repo; brings no code under the practices | — | `aDeployScout/spec/governance-deployer-research.md:22-28` |
| IW-1 population | hand-written documents at load paths, found by a heuristic marker grep | 19 files, 241.5 KB, with no render marker in their first 3 KB | command below |

What the design already settles:
- set-keyed tags and the derived index (systems `[design-tags]`);
- the touched-block budget for annotations, with untouched blocks shrink-only (`[design-annotations]`);
- the IW-1 legacy list and `memory.legacy-anchors` (`[design-memory-structure]`);
- three-state optional slots (layer-library `[consult]`);
- readings with derived owners (layer-expansions `[design-observability]`).

What it lacks: one baseline primitive, a touch obligation, provenance, and a census at adoption.

**Commands and output:**

```text
$ for c in $(git log --follow --format=%h -- memory/map/baseline.toml); do ... grep -cE '^\s+"'
2026-08-09 f9cf666c8 keys=69 … 2026-08-17 22f3e12c1 keys=54 … 2026-09-10 c09646577 keys=42 … 2026-10-11 83269a93e keys=36
$ git log --since=2026-08-09 --format=%h -- tools/<kit> | wc -l     # kits still baselined
agent-instructions 15  drift-audit 192  lib 41  pytest-parallel-guardrails 14  workflows 278
$ python tools/drift-audit/drift_report.py --json   (read-only, 28 s)
lexicon_marginal_offense_rate v=597 of=4963 … fresh 9.1% … predate 16.1%
shrink_only_lists_not_shrinking v=3 of=5 gate=False
```

**Reach** (gov's tree is 108 days old and churns heavily):

| Measure | Result |
|---|---|
| Code files changed in the last 7 / 30 / 90 / 365 days | 181 / 274 / 293 / 293 of 294 |
| Never changed after landing | 20 |
| Concentration of change | the top 20% of files take 70.0% of file-touches |
| Agents' reads, 1,461 transcripts over 30 days | 22,971 code reads |
| Reads on a file changed within 7 / 30 days before the read | 94.1% / 99.2% |
| Concentration of reads | the top 20% of files take 85.9% of reads |
| Reads landing on the top-20% most-touched files | 73.4% |
| Files never read | 81 files, 5.5% of code bytes |

**Derivable sources:**

| Source | What gov yields | A check can trust |
|---|---|---|
| commit messages | 6,001 commits: 79% have conventional subjects, 49% a unit id, 1,829 a `Decided:` trailer | structure and date only |
| docstrings and comments | 95% of modules, 67% of 3,426 defs; 1,250 cited ids, 2 dangling | resolution of ids, yes; prose, no |
| decision-shaped documents | `DECISIONS.md`: 200 rows, all cite ids, 20 owner-marked; 25 build records with a Decision heading | existence and id; "major", no |
| tests | 85 test files, 140 legs | a leg's verdict, yes |
| CODEOWNERS, lint configs | none | — |

**What gates do on code no record describes:**
- **Red on legacy:** `install-prefix`, which has no waiver registry (`tools/check-install-prefix.sh:25`).
- **Pass by finding nothing:** map coverage where the extractors enumerate nothing (`test_codebase_map.py:19-20`), and the `gov:feature` and annotation checks (0 lines today).
- **Read a baseline:** the map, the drift BASELINES and RATCHETS, the 4 site lists, `unarmed-branches`, the lexicon pin, and the dead-path waivers (`tools/check-dead-paths.sh:65`).

## 3. Across the layers

| Layer | Needs from it | Gives it |
|---|---|---|
| instruction | a step-scoped unit for the Build reach of "drain what you touch"; the slot template | the IW-1 list becomes one baseline population |
| flow | an item point in Build and a leg in Test | `build.retrofit` and the `ratchet` leg pack |
| roles | the builder's work order | a `retrofit` slot of at most 1 KB |
| memory | the contract's `provenance` field, the `baseline` kind, the map's inventories | reconstructed records, marked |
| runtime | a command adapter with an idempotence probe; red attribution | the census as a registered command |
| observability | the cadence item and readings | a `retrofit-heat` reading, which ranks what is left |
| integrations | none in core | adopts foreign CI jobs as legs (expansion) |
| distribution | none in core | adopt and update call `retrofit.census` |

| System | Needs | Gives |
|---|---|---|
| tags | stable tags as baseline keys (labels churned: `b0f5247a9`) | a `baseline` namespace |
| annotations | the touched-block scope, at most 12 lines | the drain fills `gov:note` on touched blocks only |
| instruction writing | the IW-1 list | the IW-1 list is one population of the primitive |
| role shapes | a builder at `high` | no new role |
| memory structure | `memory.legacy-anchors` | the same derive-don't-rewrite rule for records |

## 4. Candidates

| | A: big-bang reconstruction | B: passive baseline | **C: baseline plus drain on touch** | D: cadence sweep |
|---|---|---|---|---|
| Mechanism | at adoption, agents author dossiers, notes, classes and a log for the whole tree, then gates arm at zero | derive the baseline; refuse new offenses; shrink only by choice | derive the baseline; refuse new keys; a unit that touches a baselined key drains it or carries it, capped per unit | a period program drains the remaining keys in heat order |
| Efficiency | 18.47 MB read, about 4.6M tokens at 4 B per token; authoring on top | 0 agent tokens | 0 agent tokens at adoption; drains ≤2 keys per unit, in 1.1% of units; slot ≤1 KB | budget per period |
| Losing test | loses if more than 20% of authored records are stale within 60 days | loses if any baselined key on a path touched ≥10 times survives | loses if owed drains exceed 3 at p90, or if a block-scoped drain cannot bound the code offenses | loses as the primary mode if fewer than 5% of reads land on code untouched in the prior 30 days |
| Result | **loses**: 25 of 31 dossiers are older than their paths (drift, live) | **loses**: 5 kits survive with 14–278 touches | **passes** (below) | **loses here**: 0.8% (181 of 22,971 reads). It is kept as an expansion; low-churn repositories are untestable in this tree |

**C's probe:** for each unit since the seed, the seed's keys mapped to paths (26 of 69) and intersected with the files the unit touched.

```text
units since seed 1217; units touching >=1 baselined key 503
keys per touching unit: median 1 p90 3 max 10
first-touch drains 15; units carrying a drain 13; max per unit 2
first drain 2026-08-10, median 2026-08-16, last 2026-09-14
```

Under drain on first touch, 15 of 26 keys clear with a median of 7 days. The passive baseline cleared 48% in 63 days and left the hottest kits.

**C's file-scope variant loses:**

```text
files carrying baselined code offenses 134, sites 2358
commits in 30d 2956, touching such a file 831
file-scoped drain owed per touching commit: median 97 p90 326 max 1920
```

So code offenses drain only inside the touched block, under the annotations' block scope. Record claims drain per key.

## 5. The pick, specified

- **Owner:** the system belongs to no one layer. Its core parts sit in Test (the leg pack), Memory (the kinds) and Flow (the item).
- **Chain builds:**
  - **dWitnessedBar** owns the ratchet primitive, the `ratchet` leg pack and the gate on widened predicates. It already registers `leg` and `check`.
  - **dTotalRecall** owns `baseline` and `provenance` in the memory contract, the census command and the slot rows.
  - **dDeclaredLoop** owns `build.retrofit`.
  - Distribution's build owns the adopt hook, and observability's owns `retrofit-heat` (fork RT-1).
- **The primitive (extract a factory: this is the sixth instance, and the charter rule says at the second):** one shrink-only set file per population, under `memory/<layer>/baseline/<population>.tsv`.

```text
<key> TAB <practice> TAB <since-sha8> TAB <disposition: carried|deferred:<ask>>
key := <path> TAB <rule> TAB <ident>[#k]      # code legs: lexicon's line-free signature
     | <ns>.<tag>                              # record practices: a stable tag, never a label
```

- **Census** (`gov retrofit census`, a command, idempotent per base SHA):
  - runs each registered leg's `--offenders` and the map's inventories at the base;
  - writes the set files, byte-identical on a rerun;
  - spends no agent tokens. Its cost is one full bar run plus the map passes, measured at 7.8 s and 4.4 s.
- **Provenance:** every record kind gains `provenance = written | reconstructed@<sha8> | imported:<path>`, plus `from=`.
  - It is derived, never typed. A record is `written` only if it is committed in the same build as its subject's change.
  - A `reconstructed` record renders in work orders with its mark, ranks below `written` in the reuse digest, and never seeds a `MUST`.
- **Read-path cost:** the slot holds at most 8 rows and 1 KB (p90 is 3 rows at about 150 B), and overflow renders as "k carried". No new orientation lookups. The ratchet diffs offender sets over the touched paths only, estimated under 1 s; the whole-tree lexicon read at two SHAs costs 0.957 s.

**Checks:**

| Check | Red on |
|---|---|
| new key | a planted offense in a touched file that is absent from the base set |
| stale row | a fixed offense whose row is still listed |
| grown set | a set that gained a key with no `widen` record (cases: 9→159 and 18→43) |
| touch join | a unit whose write set meets a baselined key with no drain and no carry line |
| untouched quiet | the negative arm: a planted offense outside the diff must stay green; a red there reds the check |
| no count pin over code | a code population pinned by a scalar (case: `VERB_OFFENDER_PIN`) |
| provenance | `written` on a record whose subject predates its build's base |
| key shape | a label key holding a number (the `(20 checks)` case) |

**Per practice:**

| Practice | Derived | Agent's judgment | Owner |
|---|---|---|---|
| tags | namespaces from inventories and the map | the names of touched sites | none |
| annotations | resolve-check rows from cited ids | `gov:note` on touched blocks only | none |
| map and reuse | definitions, callers, inventories | the dossier on first touch; a reuse proposal | accepts each entry (LR-6) |
| decision log | candidates from ADR-shaped documents and `Decided:` trailers | routing by two raters, kappa 0.8 (layer-memory `[decisions]`) | ratifies each reconstructed major decision |
| bug classes | none | a class on a confirmed finding | none |
| specs | none: legacy gets none | a spec only for new units | none |
| instruction units | the IW-1 list | migration per step | none |
| records | the `Serves: none` pass | binding on touch | none |

**Foreign practices:**
- **Imported:** lint configs and test jobs become legs. Each joins the ratchet at the census.
- **Translated:** ADRs become decision rows by routing; the originals are kept, never edited.
- **Kept alongside:** anything else, until the owner rules.
- **Retired:** only by the owner.

The owner rules once per foreign practice. A practice's question covers every key in its population, so asks are ranked by keys × heat.

**What it never does without an owner's ask:** edit, reformat or annotate a file outside a unit's write set; fix offenses outside the touched block; grow a set; rewrite a foreign record; red on legacy no unit touched.

## 6. Items and policies

| Item | Actor | Does | Witness | Routes |
|---|---|---|---|---|
| `adopt.census` | command | derives every baseline at the base SHA | set files keyed by SHA; a rerun is a no-op | done → Plan; a leg with no `--offenders` → that population is recorded unarmed, never green |
| `build.retrofit` | builder, inside `build.unit-pass` | drains the touched keys up to `retrofit.per-unit`, and carries the rest | the touch join over the unit's commit | over the cap → `deferred:<ask>` |
| `test.ratchet` | command, a leg pack | new, stale, grown and quiet checks | verdict record | red → own fix |
| `plan.retrofit-ask` | owner | rules on a foreign practice | the policy value | import / translate / alongside / retire |
| `maintain.retrofit-heat` | command, a reading (observability) | ranks what is left by touches × reads, and files patch builds | journal plus ask | absent → "not installed: observability; touch drain only" |

**Progress cell:** "baselined N of M; −k this period; hot share: the share of last-30-day reads on files carrying no baselined key".

| Key | Values | Default | Why |
|---|---|---|---|
| `retrofit.on-touch` | drain, carry, off | drain | the passive baseline left the hottest kits |
| `retrofit.touch-scope` | block, file | block | file scope costs a median of 97 sites per commit |
| `retrofit.per-unit` | 1, 3, 5 | 3 | the measured p90 |
| `retrofit.widen` | record-reason, refuse | record-reason | lists regrew 9→159 unseen |
| `retrofit.reconstructed-major` | owner-ratifies, author-rubric | owner-ratifies | "major" cannot be derived from history |
| `retrofit.foreign` | alongside, import, translate | alongside | the owner decides per practice |
| `retrofit.cadence` | off, hot-first | off | reads beyond touch are 0.8% here |

## 7. Gaps

This closes the root of `gap-mem-03`'s retrofit side (no anchors exist on legacy code) and replaces `gap-lex-08`'s count pin with a set. The register itself was outside my read set, so I name ids only as the sections I read cite them.

New gaps it exposes:

| Gap | Severity | Evidence |
|---|---|---|
| no single baseline primitive: 6+ shapes; a leg with no list reds on legacy | HIGH | `check-install-prefix.sh:25` and the census of lists |
| baselines are not tied to touch | MED | 5 kits touched 14–278 times stay baselined |
| count pins over code act as waivers | MED | 412→1087 over 31 edits |
| a widened predicate regrows a list ungated | MED | `gate=False`, 3 of 5 lists regrown |
| no provenance on records | LOW | — |
| label keys churn | LOW | `b0f5247a9` |

## 8. Forks

| Fork | Options, the recommendation first |
|---|---|
| RT-1 owner | split across dWitnessedBar, dTotalRecall and dDeclaredLoop; or one new chain build |
| RT-2 touch obligation | drain with a per-unit cap; carry only (report); or a required drain with no cap |
| RT-3 reconstructed major decisions | the owner ratifies each; or the author's rubric |
| RT-4 foreign practices before a ruling | kept alongside; or imported by default |
| RT-5 cadence | off until an adopter measures reads beyond touch above 5%; or hot-first by default where observability is installed |

The probe script is in the session scratchpad: `C:\Users\d41ly\AppData\Local\Temp\claude\C--projects-coding-governance--claude-worktrees-gov-architecture-plan-e34297\1799cb98-0882-4ab8-a308-19495d2a487a\scratchpad\reads.py`.
