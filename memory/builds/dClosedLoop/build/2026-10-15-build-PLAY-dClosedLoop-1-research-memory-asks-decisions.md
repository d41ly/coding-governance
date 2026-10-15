# Research: the memory layer, the ask register and the decision index

**Serves:** research PLAY-dClosedLoop-1

This is dispatch 23's return, verbatim. Its question is in
`prompts/2026-10-15-prompt-PLAY-dClosedLoop-1-4-researcher.md`, and its use is in
`build/2026-10-15-build-PLAY-dClosedLoop-1-layer-memory.md`.

---

## Inventory

| Unit | What it is today | Evidence |
|---|---|---|
| Ask row grammar | `- ID · filed DATE [· unit] · TEXT [· seen/accept/out/may/verify/data …] [→ POINTER]`, placed under `## Asks` | `tools/memory-tree/backlog.py:22-37`, parsed at `:278-307`, clauses at `:310-341` |
| Disposition rows | `CLOSED·by`, `WONTDO`, `BLOCKED·on`, `DEFERRED·until`, `KEEP`, `REOPEN·of`, `SEV`, `SCOPE`, `RELOCATED` | `backlog.py:29-37,81-100` |
| Status | Never typed. An order-free fold derives it from records and spec-header `closes`/`advances` | `backlog.py:903-940`, `:716` |
| Checks | Verdicts V1–V16 (`backlog.py:1010-1160`); READY rules R1–R6, where R4 = path present and R5 = `accept` or a runnable `seen` (`:1397-1440`); hygiene checks 13 and 26 (`memory/HYGIENE.md:330,512`) | — |
| Ask writers | Unattended driver functions `write_backlog_rows`/`write_ask_rows`/`write_inherited_asks`/`write_held_asks`/`write_ask_views` (`tools/unattended/unattended.sh:9650,9843,9879,10047,9713`); agents filing by hand under `memory/guides/UNATTENDED-ASKS.md` §5 (`:105`) | — |
| Ask readers | `gen_build_index.py --asks/--check/--write` (`:2691`, `:3271`); the unattended `--plan` mandate and `asks-disposed` (`unattended.sh:5103-5260`, `UNATTENDED-ASKS.md:127`); `drift_report.py:1658`; recall `extract.py:214`; `map_extractors.py:227`; `corpus_ids.py:545`; `merge-rows.py:279`; `transition_audit.py` | — |
| Decision index | `memory/DECISIONS.md`, 200 rows. No status. Two row shapes: 141 plain `·` rows and 59 bold `—` rows | — |
| Decision row checks | Entry cap of 300 chars (`HYGIENE.md:62`); check 13 collision (`:330`); check 20 one id per document (`:405`); check 27 near-match must name its relative (`:531`); check 28 exact text dup (`:549`) | — |
| Seam already present | Each dossier's `decisions = [...]` and `## Shared seams` are read by `reuse_lookup.py:98-123,251`. The card's task field `reuse` is rendered into every handoff (`tools/roles/handoff.py:97`). Path rules load by `paths:` glob (`.claude/rules/product.md:1-6`) | — |

**Where the records and the code disagree**
- `backlog.py:11-13` still says the module "ships dark", that `BACKLOG_MODE` defaults to `shards`, and that no spec carries a verb. In fact `.memory-tree.conf` sets `BACKLOG_MODE="builds"`, and the corpus has 126 links.
- `DECISIONS.md:140-142` reads `## DEPL` and then `*(none yet)*`, followed by 87 rows. Only 6 are DEPL: 80 are TOOL and 1 is PLAY. The "grouped by family" promise at `:7` is false for 81 rows.
- Three ids appear twice (`TOOL-aUnmannedHelm-5`, `TOOL-aUnmannedHelm-6`, `TOOL-aWrittenMethod-1` four times). They are tolerated by `ROW_DUPLICATE_PIN="3"`.
- `TEMPLATE-SPEC.md:414` requires a security model "in the decision log". `grep -ci security memory/DECISIONS.md` returns 0.
- The dossier `decisions` field holds unit ids, not decision rows: of 74 ids, 16 are rows.

## Sequence

**An ask:**
1. A flow item finds a red, a stray or a finding. The driver or an agent appends an ask row to the raising build's `BACKLOG.md`.
2. Optionally a `SEV` row.
3. The fold derives the status.
4. `--write` renders `memory/backlog/<FAMILY>.md`.
5. `--plan` grades READY.
6. A spec `closes` the ask, or a `CLOSED` / `WONTDO` row disposes of it.
7. `asks-disposed` freezes `asks-at-landing:`.

**A decision:**
1. An agent appends a row to `DECISIONS.md`, by hand. Nothing requires this.
2. Checks 7, 13, 20, 27 and 28 grade the row's shape.
3. Recall indexes it.
4. M5 queries recall after the dossier lookup (`BUILD-METHOD.md:153-158`).

**What requires a decision row.** No check refuses a change for lacking one. Only prose points at the index:

| Rule | Location |
|---|---|
| "DECISIONS.md is the durable home" | `HYGIENE.md:50` |
| Counted at closeout ("rows this build minted") | `BUILD-METHOD.md:299` |
| Every other choice goes to a `Decided:` trailer instead | `BUILD-METHOD.md:318` |
| Read at kickoff per family | `memory/guides/SESSION-KICKOFF.md:57,77-80` |
| Charter Facts | `AGENTS.md:167` |
| Security model | `TEMPLATE-SPEC.md:414` |

## Measurements

**Asks.** All counts below come from the read-only print mode:

```
$ python tools/memory-tree/gen_build_index.py --asks --all --json   (stderr)
build-index: backlog 859 ask(s) · 1238 row(s) · 126 link(s) in 126 file(s) · 521 live · 0 verdict(s)
```

| Status | Count |
|---|---|
| CLOSED | 321 |
| DEFERRED | 302 |
| OPEN | 218 |
| WONTDO | 17 |
| INPROGRESS | 1 |

| Severity (live) | Count |
|---|---|
| unlabelled | 435 |
| HIGH | 39 |
| MED | 24 |
| LOW | 22 |
| BLOCKER | 1 |

| Age of live asks | Count |
|---|---|
| ≤7 days | 63 |
| 8–30 days | 58 |
| 31–60 days | 360 |
| >60 days | 40 |

- Live asks by family: TOOL 492, DEPL 26, KICK 3.
- `DEFERRED until TOOL-aMendedFleet-106`: 297.
- Live asks with a pointer: 264. Live asks marked `unit`: 2.

```
$ … --asks --tsv --status OPEN      → yes 50 · legacy 74 · no 94 ; failing R5 132, R4 99
$ … --asks --tsv --status DEFERRED  → no 301 · yes 1 ; failing R3 301, R5 301, R4 197
```

**Which parts the flow needs:**

| Core (the flow cannot run without it) | Bookkeeping |
|---|---|
| Ask row + `seen`/`accept` clauses | Family views `backlog/<FAMILY>.md` |
| Disposition verbs and the fold | `RELOCATED` rows, check 26, `ASK_CUTOFF` (migration only) |
| `SEV` (inherited-red escalates to BLOCKER) | Live-row and unlabelled pins, excerpt cap |
| V1/V3/V7 and READY R1–R6 (mandate grading) | The `unit` marker, the shards merge driver |
| The writers in `unattended.sh` | `SCOPE`/`may` grants (owner-scope, optional) |

**Decision rubric.** Each row gets the first class whose question it answers yes:
1. **Waiver or exception:** grants a named exception, raises a pin, cap or ceiling, or overrides for one build.
2. **Major product decision:** changes what ships or its architecture (a kit boundary, a mode, a shipped default, a new seam).
3. **Feature or convention to reuse:** names a primitive or rule that later code must use.
4. **Owner ruling on a fork:** owner-attributed and not covered by 1–3.
5. **Process or tooling rule:** how a gate, check, review or method behaves.
6. **Minor choice or finding:** an implementation choice, a bug found, or a lesson measured.

My line→class map is in my session scratchpad at `C:/Users/d41ly/AppData/Local/Temp/claude/C--projects-coding-governance--claude-worktrees-gov-architecture-plan-e34297/1799cb98-0882-4ab8-a308-19495d2a487a/scratchpad/map.txt`. The tally confirms coverage:

```
$ python -I tally.py map.txt memory/DECISIONS.md
rows 200 mapped 200 unmapped [] extra []
```

| Class | Live index (200 rows) | Examples | Archive sample (every 4th row, 20) |
|---|---|---|---|
| 1 Waiver or exception | 15 | PLAY-aOrientedCast-3, TOOL-aSiftedPlaybook-1 | 0 |
| 2 Major product | 12 | KICK-aReplayedCard-1, TOOL-aUnmannedHelm-1 | 3 (TOOL-aFoldedQuarry-1, TOOL-aMendedLedger-5) |
| 3 Feature or convention to reuse | 16 | TOOL-cSpliceWarden-6, TOOL-bQuiltedLantern-2 | 2 (PLAY-cDerivedGlossary-1, TOOL-aDrainedSluice-6b) |
| 4 Owner ruling | 47 | PLAY-dDerivedDocket-1, TOOL-aProbedUnit-9 | 0 |
| 5 Process or tooling | 58 | PLAY-aCandidStub-1, TOOL-aRelaxedShard-4 | 5 |
| 6 Minor or finding | 52 | TOOL-cSpliceWarden-8, TOOL-aUnmannedHelm-10 | 10 (TOOL-aBatchedTribunal-6g, TOOL-aRootedPrefix-1d) |

The classes are subjective and come from one rater; 47 owner rulings needed the precedence order to resolve. Only classes 2 and 3 match the owner's intent: 28 of 200 rows (14%) in the live index, and 5 of 20 in the archive sample.

**Fields the rows carry** (same script, regex per field, 200 rows):

| Field | Rows |
|---|---|
| date | 81 |
| `builds/<slug>` path | 65 |
| code or file reference | 77 |
| owner attribution | 65 |
| supersedes / reverses / narrows / amends | 47 |
| **reuse instruction** | **0** |

- Longest row: 299 chars, against a cap of 300. 79 rows are at 280 or more.
- Rows added per month (`git log -p`): 2026-08 185, 2026-09 89, 2026-10 19. 194 commits touch the file.

**How often rows are read.** This is node-local: `.git/recall/queries.jsonl`, 697 records.

```
query 570 · opened 121 · refused 6 ; span 2026-08-08..2026-10-15
results shown 2850, decision rows 248 ; queries surfacing ≥1 decision row 188/570
opened 121, opened DECISIONS 0 ; opened by dir: memory/builds 92, guides 19, map 3
```

Decision rows are shown inline in a third of recall queries. No agent opened the file itself.

**The dossier seam:**
- 31 dossiers; 17 declare `decisions`; 31 of 31 carry `## Shared seams`.
- 6 of the 12 class-2 rows and 6 of the 16 class-3 rows are cited in a dossier.
- Size headroom against `DOSSIER_CAP_BYTES=20480`: 3 dossiers have under 1 KB, 5 under 2 KB. `agent-cap.md` has 6 bytes left.

## Gaps

1. **No record holds the owner's intended entry.** No row anywhere carries a reuse instruction (0 of 200), and the ladder makes rows evidence only (level 7). A row cannot instruct without breaking the charter's `[memory]` rule.
2. **The index holds the wrong things.** 86% of rows are rulings, process rules, findings or waivers. Each already has a truer home: policy values (level 2), method or protocol text (level 3), gotchas, `memory/project/` registries, or spec §8 and `Decided:` trailers.
3. **Nothing decides when a row is owed.** No rule requires one, so the class mix depends on whoever writes.
4. **What holds now has to be folded.** 47 rows supersede or narrow another row, so the current state of anything means walking a chain.
5. **Asks:**
   - 435 of 521 live asks are unlabelled.
   - 301 of 302 DEFERRED asks fail R3 and R5: they are parked on one ask and lack an acceptance.
   - 132 OPEN asks lack an acceptance.
   - The grammar cannot refuse an ask filed without `accept`, because R5 is a grade, not a verdict.

## Candidates

Every candidate's reuse instruction ends up in one of two delivery routes:
- **Rendered:** the Plan/Design reuse probe matches the entry's trigger tags and writes the directive into the card's `reuse` field. `handoff.py:97` then carries it into every work order. The instruction lives at level 1 (card) and level 6 (task), so it is an instruction, not recalled memory.
- **On demand:** `reuse_lookup.py` or recall at M5 (`BUILD-METHOD.md:153`).

| # | Candidate (mechanism) | How the instruction reaches an agent | Losing test | Result |
|---|---|---|---|---|
| C1 | Keep `DECISIONS.md` and add fields to each row: date, slug, code tags, description, directive and rank | On demand (recall) | The owner's entry must fit the 300-char entry cap, and rows must actually be read | **Rejected.** Rows already reach 299 chars, with 79 at 280 or more and no new fields yet. 0 of 121 opened reads hit the file |
| C2 | Two-tier index (ADR-style): build-local decisions stay in the build folder (§8 marks, `Decided:` trailers); only major and feature entries leave, as one file per entry under `decisions/` (exempt per `HYGIENE.md:52`) with Nygard's or MADR's sections | On demand | (a) Volume: the tier must shed most rows. (b) Determinism: two independent classifiers agree at kappa ≥ 0.8 over the 200 rows. (c) What holds now must be readable without folding a chain | (a) passes: 28/200. (b) **not run**: needs a second rater; my pass needed a precedence order for 47 rows. (c) fails as built: Nygard keeps superseded records and links forward, so the 47-row chain pattern persists |
| C3 | A separate feature and convention registry, `memory/registry/*.toml`, modelled on a Backstage Component (type, lifecycle, owner, provides, dependsOn, tags) | Rendered by tag, plus on demand | The charter's `[reuse]` rule: the registry must not restate the identity, paths and seams a dossier already holds | **Rejected.** Every dossier already carries the Component analogues: `feature`, `status`, `streams`, `[claims]`, `[paths]` and `## Shared seams` (31/31). A registry would be a second home for one fact |
| C4 | The dossier as the home, inline: a `[[reuse]]` array in dossier front matter. `reuse_lookup` already reads that front matter | Rendered plus on demand | Entries (about 300–500 B each) must fit `DOSSIER_CAP_BYTES` | **Rejected as inline.** 3 dossiers have under 1 KB headroom; `agent-cap.md` has 6 B |
| C4′ | A dossier sidecar: `memory/map/features/<feature>.reuse.toml`, keyed by the dossier's `feature`, one entry per convention. Each entry carries a directive with a rank, trigger tags, code anchors, `since` date, build slug and decision ids. Cross-cutting conventions go to `FOUNDATION` (`memory/map/FOUNDATION.md:1-8` is the declared substrate home) | Rendered: the reuse probe matches triggers and writes the card's `reuse` field. Also on demand: `reuse_lookup` prints the entry beside the seam | (i) Every class-3 row has a feature or FOUNDATION home. (ii) An adopter with memory-tree but without codebase-map (`kit.toml`: codebase-map `requires = ["memory-tree"]`, not the reverse) loses only an expansion, never a core step. (iii) The owner's media-picker case: a unit whose write set misses the picker's globs still receives the directive | (i) passes on inspection: the 16 class-3 rows name a kit or are substrate. (ii) passes only if the core declares the card's `reuse` slot as its extension point. (iii) passes for rendered delivery and **fails for path-rule delivery**, because a `paths:` rule loads only when matching files are opened |
| C5 | Reuse directives as path rules under `.claude/rules/*.md` (level 4) | Loaded when a matching path is opened | Test (iii) above | **Rejected** by test (iii): "anywhere a media selector is needed" is a need, not a path |

On ranking: a directive's rank is how the ladder already ranks units. Each entry uses statement type `directive` or `constraint` and a `policy` tag, so the owner can switch it. This matches MADR's optional "Confirmation" element, which says how compliance is checked.

**Prior art, as it bears here:**
- **Nygard** limits records to "architecturally significant" decisions (structure, dependencies, interfaces, construction techniques). That supports the class filter. He keeps superseded records, which supports a log but not a statement of what holds now.
- **MADR** adds date and decision-makers metadata and a Confirmation section, which supports the rank-and-verify field.
- **Backstage** keeps current-state catalog entries separate from decision history. That is the C4′ split, with the dossier as the catalog that already exists.

## Pick

**C4′, with C2's routing for everything else.** C4′ is the only candidate that passes the losing tests I ran: C1, C3, C4 and C5 each fail a measured test. Two tests are still owed (below).

1. **The intended record is an instruction unit, not a record.** It is a sidecar entry beside its dossier, at level 3 with a `kind` tag, statement type `directive` or `constraint` with a rank, and an owner-switchable `policy` tag. It is authored once and edited in place, so it always says what holds now. The decision row that created it stays evidence and points to it. This keeps the charter's `[memory]` rule: what instructs is never the recalled row.
2. **Delivery is rendered by tag.** The Plan/Design reuse probe (M5) matches trigger tags and writes the directive into the card's `reuse` field, and `handoff.py:97` puts it in every role's work order. `reuse_lookup` also prints it on demand. Because the codebase map is an expansion, the core must declare the card's `reuse` slot as an extension point.
3. **`DECISIONS.md` narrows to class 2 only** (about 12 rows). Each row carries date, slug and a pointer to its sidecar entry, in a template that one grammar checks. The other classes are routed by a fixed table:

   | Class | Destination |
   |---|---|
   | 1 Waiver or exception | `memory/project/` registry |
   | 4 Owner ruling | Policy value |
   | 5 Process or tooling | Method or protocol text |
   | 6 Minor or finding | Gotcha or `Decided:` trailer |

4. **Asks keep their core** (the row, verbs, fold, `SEV`, READY). One change follows from R5: making `accept` required at filing would turn the 132-ask gap from a grade into a refusal.

**Tests the build must run before this is final:**
- Two-rater kappa ≥ 0.8 on the routing table over the 200 rows.
- A handoff fixture in which a card whose behaviour phrase matches a sidecar trigger renders the directive and a non-matching card does not.
- A memory-tree-only install in which every core step still runs with the registry absent.

Sources:
- [Nygard, Documenting Architecture Decisions](https://www.cognitect.com/blog/2011/11/15/documenting-architecture-decisions)
- [MADR](https://adr.github.io/madr/)
- [Backstage descriptor format](https://backstage.io/docs/features/software-catalog/descriptor-format/)
