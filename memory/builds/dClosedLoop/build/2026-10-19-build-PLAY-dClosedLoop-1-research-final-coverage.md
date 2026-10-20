# Research: The control that the whole design is specced as planned: clause ids, pins and the coverage join

**Serves:** research PLAY-dClosedLoop-1

This is dispatch 156's return, verbatim, except that a title line would be demoted to keep one H1 per record, and that its one example of an id the roster would read is written `missing:<id>`, so the build index does not take it for a unit of this build. Its question is in `prompts/2026-10-19-prompt-PLAY-dClosedLoop-1-29-researcher.md`, and its use is in `build/2026-10-19-build-PLAY-dClosedLoop-1-final-questions.md`.

---

## Answer: how the chain is held to v2 when it is specced

**Recommendation.** Every v2 clause gets a stable id. Each spec states which clause ids it carries, pinned to the hash of each clause's text. A deterministic join then reds whatever its arms can see, a model review covers the meaning it cannot, and the owner reads a coverage report at each chain build's Design exit.

Today nothing joins a design clause to the spec that carries it. Every probe below was run read-only. The prototype ran in my scratch folder `d156`, which I have now deleted. The tree is unchanged.

### 1. Precedents

| # | What was lost | Hand-off | How and when it was caught | What would have caught it at once |
|---|---|---|---|---|
| 1 | An owner's answer reversed: LR-3 chose "as `run.on-owner-question` says", but the draft wrote "an owner breakpoint parks the build" | owner answer → design draft (dDeclaredLoop's input) | The fold's diff review, M4, about a day later (`reviews/2026-10-16-review-PLAY-dClosedLoop-1-fold.md:91-98`) | A join from a sentence that cites an answer to that answer's chosen option |
| 2 | v2's clause (v2:1504) moved the agent cap to `runtime.agents-in-flight`; `systems.md:425` still names `FANOUT_CAP`, so a spec read from systems.md would wire a retired carrier | design record → design record → (future) spec | Night-pass-two closing review, M1, after the fold (`reviews/2026-10-19-review-PLAY-dClosedLoop-1-night-pass-two-b.md:45-60`) | A spec pinning the clause and the sections it rests on, plus a retired-name census |
| 3 | Thirteen places where a later round overtook an earlier record | design ↔ design | Dispatch 104, a model pass, days later (`night-pass-instruments` `[stale]`) | Section-level pins. Whether a section was already stale belongs to Q1 (one line) |
| 4 | **Latent, measured now:** 218 of 498 owned design nodes are named in none of their owning build's clauses. Example: `build.acceptance`, owned by dScopedBuild, defined only in `flow-steps` | design → spec (not yet happened) | Not caught. A spec writer reading only the chain row drops it | A coverage join over the owned nodes as well as the clauses |
| 5 | A carrier of a count dropped: ratified `TOOL-aClosedDocket-4` S6 dropped `check-pass-order.sh`, and rev-1 of the next spec reproduced the drop "without ever seeing the diagnosis" | spec → spec, then → revised spec | Unit 1's Q3, then a later revision (`dFoldedVerdict/spec/2026-09-01-spec-TOOL-dFoldedVerdict-2.md:534-536`) | A population derived from the source rather than a typed count |
| 6 | Eight findings of "prose that contradicts the design or a sibling spec" and seven of "a prior ruling the spec did not engage". Examples: #43, the DECISIONS.md:198 ruling unengaged; #47, claims always-on with no switch and no ruling | design → spec | Spec audit round 1, the same day (`aGraftedHelix/reviews/2026-10-04-…-spec-audit-round1.md:87-100`). Only because an audit ran: 47 of 167 builds have any spec-audit record | A clause join for the dropped half; a model lens for the contradicted half |
| 7 | Four of nine audit defects came from amendments made twenty minutes earlier; one rule then returned two verdicts | spec → revised spec | Post-acceptance spec audit (`gotchas/amendment-leaves-its-other-half-standing.md`) | Revision drift needs a recorded decision per revision; the semantic half needs the model lens |
| 8 | The fold created the defects: 25 + 17 of 62 findings in one build, 20 of 32 in another | spec → revised spec | The next audit round (`gotchas/fold-text-is-unreviewed-surface.md`) | The same as row 7 |
| 9 | A compaction summary rewrote 3 of 355 "verbatim" map lines, and the owner was told the map came through verbatim | context → session (the owner's "lost chain of thought") | A re-read (`gotchas/summary-rewrites-the-text-it-carries.md`) | A hash pin compared against disk, not memory |
| 10 | The planned-but-unspecced join (`missing_units`) was pointed at the generated region and became a tautology | the control itself | Mid-build (`tools/unattended/unattended.sh:4589-4594`) | Read the authored plan, never a list derived from specs |
| 11 | A discovery handed to "this run's orchestrator" was dropped | spec → build | Closing diff review, TOOL-aGraftedHelix-32 (`gotchas/orchestrator-hand-off-owed-a-disposition.md`) | Every hand-off resolves to a unit or a parked row |
| 12 | Check 24's RETIRE arm, "the one predicate that refuses a silently dropped unit", joined ids by mention, so a foreign id exempted a dropped unit | the drop control itself | Closing diff round 2, M2 (`aGradedMandate/reviews/2026-08-31-…-round2.md:207-222`) | Ownership joins, never mention joins |
| 13 | Five times, "a scope item that names a deliverable no acceptance criterion observes" | design → spec set | Spec audit round 1 (`dRetiredFork/reviews/2026-09-02-…-round1.md:17`) | Already in spec-audit coherence; check 23 at build |
| 14 | Reviewers handed a task audited the task instead of doing it | hand-off reinterpreted by role | The owner, comparing ask to return (`gotchas/task-handed-as-the-spec-is-reviewed-not-done.md`) | A typed input (P26) |
| 15 | A legitimate deviation: units 4 and 5 adopted after measurement, order reversed, recorded in roster prose (`aBatchedArm/README.md:71-85`) | spec set → revised set | — (recorded, but only as prose) | A rescope row carrying a decision id |

### 2. What exists

| Control | What it checks | What it cannot see |
|---|---|---|
| Write gate (`tools/hooks/scratch-guard.js:74-99`, fails closed) | A product write needs a routed unit whose spec is buildable (INPROGRESS) | Whether that spec carries its design. Spec writes under `memory/` are outside it |
| Kickoff card scope (`skills/session-kickoff/SKILL.md:126`, Step 5) | A closed scope derived from the message and memory | Any design clause |
| TEMPLATE-SPEC status header and §9 (`memory/TEMPLATE-SPEC.md:55-93`) | rev-N has a §9 line; `base` resolves; `closes`/`advances` reach asks | No field binds a spec to a design (measured: 0 of 1322 specs; 118 cite a design record path in prose) |
| BUILD-METHOD M2 / M7 (`memory/guides/BUILD-METHOD.md:32-72, 231-250`) | MISSING / THIN / FORKED / READY over roster units; regrounding re-reads the current spec | A clause never put on the roster is never MISSING. Regrounding never re-reads the design |
| Spec audit (`tools/workflows/tier2-review.template.js:741-772`; sibling context `:1045-1060`) | Coherence, grounding, reuse, blast radius, failure envelope. A caller may hand design records as "sibling context" | Opt-in and probabilistic. No lens grades conformance to an upstream design |
| Check 23, the acceptance ledger (`memory/HYGIENE.md:595-625`) | Every criterion of a closed spec is OBSERVED or AMENDED rev-N | Spec → build only; shape, not truth |
| Unattended check 24 (`tools/unattended/check-unattended.sh:3902-3975`); `missing_units` (`unattended.sh:4600-4786`) | Roster add/retire/supersede needs a rescope row; planned-but-unspecced ids | Unit ids only, and only under the unattended kit |
| `spec-tokens` (`tools/check-spec-tokens.py:4-110`) | legs, paths, cites, bar, guards, claims, handoff, size. `handoff` checks that a promised token is named by the sibling spec's text | Nothing upstream of the spec set |
| `gen_build_index.py` "Ids no record names" (`:1445-1458`) and the roster (`:75-86, 767-830`) | Unit ids with no evidence record; ids with no spec-audit record | Design → spec direction |
| Planned: dIndexedDesign (`flow-steps:181-193`) | `design.decompose` writes the roster; `design.ready` derives MISSING/THIN/FORKED; `design.inventory` gives completed units a verdict after a plan revision; the design index runs over write sets for overlaps (`:187`); `implements=` edges (v2 dIndexedDesign.12) point code or build at a feature | Roster ← plan clause is authored by the architect, with no join. `implements=` has no clause target (`research-relational-syntax.md:118`) |
| Planned: dScopedBuild (`build.scope`, `build.acceptance` in `flow-steps`, `build.reuse-check`) | Commit paths against the write set; acceptance re-run; reuse | Build-side only. `build.acceptance` is in no v2 dScopedBuild clause (row 4) |
| Planned: dFairHearing's design-audit preset (v2 dFairHearing.1-2) | Coherence and grounding of design records. Its own bar is 45 of 59 known defects | Records, not spec-versus-design; probabilistic |
| This build's instruments (`night-pass-instruments` final `[final]`; `map.py:584-603, 785-799`) | Gap join (378 gaps, each owned once); clause scan (split safety); critical path; owner per node; chain echo (a clause cited by its opening words) | All build-level. Chain echo "does not check … that every clause the plan builds has a row" |

**Is there any join from a design clause to the spec that carries it? No.** The nearest seams are the `handoff` join, check 23's two-form ledger, check 24's rescope verbs and the map's owned-node registry.

### 3. The unit of control (measured at `930120e45`)

- **484 clauses, none with an id.** I split them with the clause scan's own quote-aware rule and got 484, matching the handoff.
- **Clauses move and change too often for positional or text-based ids.** Over v2's 104 commits, 80 changed `[chain]`: 467 clause edits, 464 inserts and 99 deletes. 297 unchanged clauses changed position, 924 clause texts were new at their commit, and 72 moved to another build's row. v2 is still moving: 23 commits on 2026-10-19 alone.
- **Provenance is thin.** 196 clauses cite no fork, answer or round; only 4 cite a gap id.
- **Tokens and nodes leave holes.** 283 clauses carry backticked tokens and 201 carry none. 64 clauses name no owned node, and 218 of 498 owned nodes appear in no clause of their owner. So the unit has to be clauses plus owned nodes.
- **Section tags are unique.** Outside fences, no record repeats a `## [tag]` (69 records, 666 sections), so `<record> [<tag>]` is a safe address for a section pin.

What a spec cites, so a join can grade it:

- `**Carries:** <clause-id>@<hash8> whole|part k/n` for each clause, plus `node:<ns>.<key>` for each owned node it builds.
- The record sections a carried node rests on are derived from the map's declared source, not typed.
- A spec that carries no clause declares `**Derived:** <decision-id>`. This is DO-178C's derived requirement.

Stable ids:

- Grammar `cl-<minting-slug>-NNNN`, put at the **end** of each clause in backticks. The minting slug follows the `[ids]` rule (never a shared counter); a later revision by another session mints under its own slug.
- Probed against the real regexes, `cl-dClosedLoop-0001` matches neither the roster id regex nor `GENERIC_ID`. `missing:PLAY-dClosedLoop-1001` and `CL-…` both would: the first would add phantom units to rosters.
- In a simulation, putting the id at the front broke the chain echo on 17 of 17 memory-plan rows; at the end it broke 0 of 17. Clause counts per build were unchanged.
- An id is never reused: retired ids are listed in a `[clause-ids]` section.

Splits and merges:

- A split is declared as `part k/n` on each carrier; a merge is one spec listing several ids.
- A move, retirement or deferral is a rescope row `clause move|retire|defer <id> [-> dX] <decision-id>`, check 24's grammar extended.

Amendments (P19):

- The hash is the clause's revision, as with an OpenFastTrace revision or a Doorstop fingerprint. When a clause is amended, its carriers go suspect.
- A live spec re-pins through a rev bump whose §9 line names the amendment.
- A frozen, built spec cannot re-pin, so the report shows "owed: a new unit at @new".

### 4. Survey (all read 2026-10-19)

| Method | Requirement → spec/task/code tie | How it detects drift |
|---|---|---|
| **DO-178C** | Bidirectional trace data: system → high-level requirements → low-level requirements → source; derived requirements made visible. I used secondary sources: a search summary of a Parasoft whitepaper whose PDF would not decode, plus [Wikipedia](https://en.wikipedia.org/wiki/DO-178C), which says traces are "documented bidirectional connections" | Trace analysis. Known failure: "None of this traceability demonstrates that requirements are being met" ([Parasoft](https://www.parasoft.com/learning-center/do-178c/requirements-traceability/)) |
| **ISO 26262-8** | The standard was not read directly; secondary sources only. Assessors check that bidirectional traceability is "adequately implemented", how is not prescribed; change impact analysis per change ([Verification Academy](https://verificationacademy.com/topics/functional-safety/intelligent-requirements-traceability-for-iso-26262/), [itemis](https://www.itemis.com/en/glossary/impact-analysis/)) | Impact analysis. No suspect-link rule found in the standard |
| **Doorstop** | Stable UID; a link stores "the parent item UID and the fingerprint of the parent when it last reviewed" ([item.md](https://github.com/doorstop-dev/doorstop/blob/develop/docs/reference/item.md)) | SHA256 fingerprint compared at review time |
| **OpenFastTrace** | `type~name~revision`; `Covers` / `Needs`; "Incrementing the revision voids all existing links" ([concepts](https://openfasttrace.itsallcode.org/user_guide/introduction/concepts_and_terms.html)) | Link statuses outdated, predated, ambiguous, orphaned; deep coverage ([system requirements](https://github.com/itsallcode/openfasttrace/blob/main/doc/spec/system_requirements.md)) |
| **sphinx-needs** | `needs_id_required`, `needs_id_regex`, links, `needs.json` ([configuration](https://sphinx-needs.readthedocs.io/en/latest/configuration.html)) | `needs_warnings` filter strings at build time |
| **jamb** (IEC 62304) | Content hash recorded at link time ([traceability](https://jamb.readthedocs.io/en/latest/iec-62304/traceability.html)) | A hash mismatch marks links suspect until re-acknowledged |
| **GitHub Spec Kit** `/analyze` | FR-/SC- ids as keys; tasks mapped "by keyword / explicit reference" ([analyze.md](https://raw.githubusercontent.com/github/spec-kit/main/templates/commands/analyze.md)) | An LLM prompt, read-only: reports requirements with zero tasks and tasks with no requirement. Not deterministic |
| **Kiro** | requirements.md (EARS), design.md, tasks.md ([requirements-first](https://kiro.dev/docs/specs/feature-specs/requirements-first/)) | None documented. On a requirements change, "ask Kiro to update the design"; task-to-requirement links not documented |
| **OpenSpec** | Requirements keyed by header name; ADDED / MODIFIED / REMOVED deltas ([repo](https://github.com/Fission-AI/OpenSpec)) | `validate --strict` catches a MODIFIED block that drops a scenario ([v1.9.0 notes](https://newreleases.io/project/github/Fission-AI/OpenSpec/release/v1.9.0)). Keying by name breaks on a rename |
| **Tessl** | `targets`, `[@test]` links ([tile](https://tessl.io/registry/tessl-labs/spec-driven-development)) | Only "verify … synchronized"; the mechanism is undocumented (closed beta) |

The pattern across these tools: the ones that work deterministically all pair a stable id with a revision or hash pin (Doorstop, OpenFastTrace, jamb). The agent tools rely on a model or nothing.

### 5. Candidates, each with the test that could make it lose

| Candidate | Mechanism | Losing test, and result | Verdict |
|---|---|---|---|
| **A. Model review only** | Hand the clause and its sections to the spec audit as sibling context, plus a conformance lens (Spec Kit's model) | It must red a planted dropped clause every time it runs. **Lost:** it is opt-in (47 of 167 builds ever audited), its own bar is 45 of 59, and precedents 1, 2, 6 and 7 were found late or only when it ran | Rejected as the control. **Kept as a complement**: it alone sees plant p9 below |
| **B. Positional ids** (`dScopedBuild.3`) | Derived by splitting the row | `[ids]` forbids renumbering. **Lost:** 297 renumbers and 72 cross-build moves in history | Rejected |
| **C. Text hash as the id** | The id is a content hash | Must survive a typo fix. **Lost:** 924 new hashes in history; amended and new clauses look the same | Rejected as identity; **kept as the pin** |
| **D. Opening words as the key** (chain echo, OpenSpec style) | The key is a clause prefix | Must survive edits. **Lost:** 62 of 354 one-to-one edits changed the opening six words; 2 collisions at four words | Rejected |
| **E. Clause id = a pre-minted unit id** (`PLAY-dScopedBuild-N`) | Reuses roster and `missing_units` | Must survive moves and splits. **Lost:** 72 moves would leave ids naming the wrong build; it forces one clause per unit | Rejected |
| **F. Owned nodes only** | Every map node owned by a build must be named by a carrier | **Lost:** 64 clauses name no node | Rejected alone; **kept as the second population** |
| **G. Recommended: stable clause id + hash pin + deterministic join** (extends `handoff`, check 23's two forms, check 24's rescope verbs, the map's owners) | See section 6 | Run as a scratch prototype on fixtures, results in the next table. **Holds**, except the stated blind side | **Recommended** |

The test that could make G lose, with its results:

| Fixture | Arm that should fire | Result |
|---|---|---|
| clean | none | rc 0 |
| p1, a dropped clause | `uncarried: cl-…0002` | rc 1 |
| p2, a spec citing no clause | `unbound: 5.md` | rc 1 |
| p3, two specs carrying one clause and disagreeing | `ambiguous: … carried whole by 2 specs` | rc 1 |
| p4, a spec revised away from its clause with no decision | `silent: … rev-2 stopped carrying …0004` | rc 1 |
| p4b, the same revision with a decision id and a move row | none | rc 0 |
| p5, the design amended after the pin | `suspect` (plus the `token` arm) | rc 1 |
| p6, a split clause whose part dropped a token | `token: …second-pass` | rc 1 |
| p7, a ghost id | `ghost` | rc 1 |
| p8, no specs | "measured NO spec" | rc 2, never green |
| **p9, a carrier contradicting its clause while keeping every token** | — | **rc 0: the blind side, which is A's job** |

On the real tree the prototype's design parser refused at once ("a clause of dGroundRules carries no id"), and 0 specs carry a `**Carries:**` line. Minting simulated in scratch gave 484 ids with 484 unique hashes. The token arm is blind for 201 clauses, per build from 1 of 12 (dSafePassage) to 19 of 60 (dWellOiledMachine).

On pin granularity, history shows a per-clause pin goes suspect on 2.0% of (clause, commit) pairs. A per-row pin goes suspect on 17.0%, and a whole-record pin on every commit.

### 6. Recommendation

**What it witnesses, at speccing time with today's tools.** Arms per spec: ghost, unbound, suspect, ambiguous or split, and silent revision. Arms per build: uncarried clause or node, and token coverage. It also announces when it measured nothing.

**Its gate and leg.**
- The spec arms join the existing leg `spec tokens (a spec's own names resolve)` (`tools/gate-legs.json:1651`) as a ninth join, `carries`, behind a `.memory-tree.conf` cutoff the way `SPEC_HANDOFF_CUTOFF` is.
- The build arms render unconditionally into the build README beside "Ids no record names", with an explicit "none" line, and refuse through memory hygiene when a spec of a chain build is at INPROGRESS while its build's coverage is red.
- The model lens runs at the Design exit with each carried clause's text and its sections handed in as sibling context.

**Must exist before speccing starts:**
1. **dClosedLoop, records only:** mint `cl-dClosedLoop-NNNN` at the end of all 484 clauses, plus a `[clause-ids]` section. Re-run the clause scan, chain echo, gap join and critical path, which my simulation kept unchanged.
2. **dClosedLoop, records only:** a new dIndexedDesign clause that carries the control into the product. `design.ready` gains an UNCARRIED class; `implements=` gains a clause target; the design index renders coverage; the bootstrap join is absorbed.
3. **One bootstrap tooling unit (product code under `tools/`), specced and built with today's tools before any chain spec.** It needs an owner decision on its home (below), because this build writes no product code. My lean is unit 0 of dGroundRules, the chain root at 11 units on the critical path, rather than waiting for dIndexedDesign at 187.

**Policy keys** (structural choices excepted: the id grammar and the hash pin):

| Key | Values | Default |
|---|---|---|
| `design.coverage` | `refuse` \| `warn` \| `off` | `refuse` at the Design exit |
| `design.coverage.population` | `clauses-and-nodes` \| `clauses-only` | `clauses-and-nodes` |
| `design.coverage.suspect` | `refuse-at-exit` \| `refuse-always` \| `warn` | `refuse-at-exit` |
| `design.coverage.derived` | `decision` \| `allowed` \| `refused` | `decision` |
| `design.coverage.semantic` | `every-exit` \| `with-spec-audit` \| `off` | `every-exit` |

**The coverage report the owner reads at each Design exit** (proposed format):

```
design coverage — <build> at <sha> · design v2 @<blob8>
clauses N · carried (whole w, split s) · disposed (moved/retired/deferred, each with its decision) · uncarried 0 · suspect 0 · ambiguous 0
owned nodes M · named by a carrier · unnamed 0
specs K · derived (no clause), each with its decision id
token arm blind on b of N clauses — the semantic lens read them: <verdict>
```

### Where a record and the code disagree
- The handed facts say `spec-tokens` has seven joins; the code lists eight (`size` is the eighth, `check-spec-tokens.py:37-40`).
- `build.acceptance` is handed as part of dScopedBuild; it lives only in `flow-steps`, in no v2 clause.
- The gap register's diagram says "spec audit (opt-in, 3/173)"; I measured 47 of 167 builds with any spec-audit record. The two probably count different things.
- The design map lists 256 policy-key nodes; the catalogue has 261. The reconciliation probe reads 491 owned nodes; the map's namespaces list 498. Neither gap was resolved.
- The design map's chain echo splits clauses on a bare "; ", where the clause scan's split is quote-aware. They agree today only because the clause scan finds no split inside a clause.

**For the other researchers, one line each:**
- Q1 (whole-design audit): rows 2 and 3 are records that disagree with each other, and the 218 owned nodes no clause names belong to its audit.
- Q3 (spec deviation and its log): the rescope rows and the AMENDED form above are the deviation log's seam.

**Decision for you:** where the bootstrap join is built. Unit 0 of dGroundRules (my lean) puts it on the first spec of the chain. A separate tooling build keeps the chain clean but sits outside your 21-build plan.

Files cited:
- `C:\projects\coding-governance\.claude\worktrees\gov-architecture-plan-e34297\memory\builds\dClosedLoop\build\2026-10-14-build-PLAY-dClosedLoop-1-architecture-v2.md`
- `C:\projects\coding-governance\.claude\worktrees\gov-architecture-plan-e34297\memory\builds\dClosedLoop\build\2026-10-15-build-PLAY-dClosedLoop-1-flow-steps.md`
- `C:\projects\coding-governance\.claude\worktrees\gov-architecture-plan-e34297\memory\builds\dClosedLoop\build\2026-10-17-build-PLAY-dClosedLoop-1-map.py`
- `C:\projects\coding-governance\.claude\worktrees\gov-architecture-plan-e34297\tools\check-spec-tokens.py`
- `C:\projects\coding-governance\.claude\worktrees\gov-architecture-plan-e34297\tools\unattended\check-unattended.sh`
- `C:\projects\coding-governance\.claude\worktrees\gov-architecture-plan-e34297\tools\memory-tree\gen_build_index.py`
- `C:\projects\coding-governance\.claude\worktrees\gov-architecture-plan-e34297\memory\HYGIENE.md`
