**Serves:** research TOOL-dTracedLattice-1 TOOL-dTracedLattice-2 TOOL-dTracedLattice-3 TOOL-dTracedLattice-4 TOOL-dTracedLattice-5
**Commissions:** TOOL-dTracedLattice-1 TOOL-dTracedLattice-2 TOOL-dTracedLattice-3 TOOL-dTracedLattice-4 TOOL-dTracedLattice-5

# dTracedLattice — relations in the codebase map, and the map as an orientation substrate

Design pass, rev-2. Node `d`, 2026-09-05, base `c4fcf5ad`. Five grounding lenses measured the tree,
then five skeptics attacked the result and killed most of it. **The recommendation reversed between
rev-1 and rev-2: rev-1 proposed committing a coarse import graph; rev-2 says commit nothing, and the
reason is not the one rev-1 argued.** Section 6 lists what was killed and why.

## 1. The premise verdict

Both of the owner's claims were attacked directly and the verdict below is what survived.

**Claim 1 — "the map carries no relations." PARTLY TRUE.**

No committed artifact carries a code relation: `symbols.json` rows are `{id, kind, file}`, `MAP.md`
is key-to-claimant tables, `[claims]` names inventory keys and `[paths].globs` names path patterns.

But four relation models already ship, and every command below was independently reproduced at
`c4fcf5ad`.

| Edge | Where | Authored or derived | Population |
|---|---|---|---|
| record to spec id | `**Serves:**` | authored, gated both directions by hygiene check 21 | **479 records, 481 lines** |
| bug class to path | `gotchas.py` anchors, at `:48` and `:176` | DERIVED from backtick tokens in the body | all of `memory/gotchas/` |
| feature to path | dossier `[paths].globs` | authored | all 20 dossiers |
| build to build | `parents:`, `children` inverted at `gen_build_index.py:1640` | half authored | 2 of 92 |

The `**Serves:**` figure is 479 records across 481 lines — two records carry two `Serves` lines, and
rev-1 reported 481 records because it summed grep LINE counts. A count of a derived population, wrong
in prose, in a dossier that criticises exactly that habit.

**Claim 2 — "the recall tools do not use the map." SPLIT.**

`reuse_lookup.py` is map-native and reads all four map sources; the premise is wrong there.
`tools/memory-recall/` has no map awareness at all; the premise is right there, and
`TOOL-aDeclaredCeiling-2` names the mechanism.

## 2. What already exists, and the decision that stopped it

`map_lib.build_reference_index()` and `fan_in()` build a token index on demand and never commit it.
The exclusion is ratified — `bConvergentLodestar` review finding 4:

> **`fanin` in the freshness-gated `symbols.json` churns.** A live reference count restales the
> artifact on nearly every commit ... Fix: `symbols.json` = `{id,kind,file}` only; fan-in computed on
> demand in reuse-lookup/converge-report, never committed/gated.

**It was never measured, and that was checked rather than assumed.** The claim appears in five places
in the tree with no number, no range and no command in any of them, while `map_lib.py` marks its
neighbouring claims "Measured on gov at b4f0cf1c" four lines away.

**Its rate is nonetheless roughly right for the artifact it describes.** If `fanin` lives INSIDE
`symbols.json`, the restale set is the union of row churn and count churn, measured at 12.0%. For a
SEPARATE fan-in artifact the like-for-like figure is 5.3%. Finding 4 is sound about its own proposal.

## 3. The measured picture

### The churn measurement, and what is wrong with it

Rev-1 built its case on a churn table. Three skeptics independently established that **the table
measures the token reference-index projection, not the import graph the design proposed to commit**.
`sym_total 2966`, `file_total 1612` and `kit_total 120` all fall out of `map_lib.build_reference_index`
at HEAD, reproduced to the unit. An independent `ast` walk over the same tree finds **51 file-to-file
and 5 kit-to-kit import edges** — 32x and 24x smaller. The corpus holds 454 Python and 11 JS import
statements in total, so 465 is the arithmetic ceiling for any import graph.

Three further defects in that table, all disclosed rather than repaired:

- **No producer survives.** `lens4-churn-harness.py` is byte-identical to `churn.py`, writes no file
  and emits none of the fields the analyzer reads. Nothing in the scratchpad writes the raw JSON.
  The analysis re-runs; the measurement does not.
- **The pair set is the full DAG**, `rev-list --topo-order` over 150 commits, each against its own
  first parent. Only 14 sit on main's trunk. A branch delta is counted twice while the denominator
  absorbs the branch's inert commits, which DEFLATES every rate relative to the landing boundary.
  108 of 150 pairs touch no code at all, and 90% of the window is a three-day burst.
- **Control and treatment use different methods.** G0 is the committed blob's change rate; every
  other row is a live re-derivation. One table, two methods, presented as commensurable.

**What the corrected measurement says.** Re-measured over the same window on the artifact actually
proposed: file-to-file import churn **0.5% topo / 4.5% first-parent**, kit-to-kit **1.1%**. The
conclusion rev-1 drew survives on evidence rev-1 did not have. Right answer, wrong measurement.

**And the coarse-versus-fine split does not survive at all.** Of the 136 pairs where the committed
`symbols.json` did NOT change, fan-in moved on 4 (2.7%), file edges on 2 (1.3%), kit and feature
edges on none. On all 14 pairs where `symbols.json` did change, fan-in moved too. The commit boundary
rev-1 drew rests on a two-commit difference in a 150-pair window whose 20 most recent pairs moved
nothing at all. Rates swing 0.0% to 16.0% with window size.

**G3's 0.0% is saturation, not stability.** 120 token kit-edges is 76.9% of the complete 156-pair kit
digraph, and density rose from 56.9% to 76.9% in three weeks. Walking back to 2026-07-03 the
population reads 41, 54, 80, 98, 118, 119, 120 — it moved on 6 of 24 comparisons, every move a new
kit appearing. **The metric stabilises precisely as it becomes vacuous**, and rev-1's liveness
paragraph asserted liveness for two OTHER probes and then concluded about this third one. That is
`AGENTS.md` §7 applied to the wrong probe, in a dossier quoting §7.

### Precision — the part that held up

`python variants.py` reproduces byte-identically. Scored against the AST resolver's confirmed import
edges, over 127 rows and 329 true edges:

| Variant | edges | confirmed | precision | recall | mean abs err |
|---|---|---|---|---|---|
| A — shipped `fan_in` | 2734 | 397 | 14.5% | 100.0% | 1.38 |
| B — minus same-name definers | 974 | 329 | **33.8%** | **82.9%** | **0.46** |
| C — bare-occurrence only | 2045 | 100 | 4.9% | 25.2% | 1.87 |
| D — both | 285 | 32 | 11.2% | 8.1% | 2.25 |

**The dot-prefix filter is harmful and `TOOL-aScouredKit-16` should be amended, not implemented.**
D discards 198 of 211 AST-verified edges — 93.8% — because this repo's dominant idiom is
`import map_lib as m` then `m.fan_in(...)`, which is a real reference and is dotted. Under D every
symbol rev-1 cited as the heuristic's success reads 0, including `attribute_paths`, the function
rev-1 simultaneously ranked first for promotion and filed under dead exports.

**A fifth variant was measured rather than argued.** E2 — bare occurrence, OR a dotted occurrence
whose receiver binds to a repo module, plus definer subtraction — is about 40 lines of stdlib `ast`
and costs a median 1.761 s against `build_reference_index`'s 0.595 s, taking the on-demand path to
roughly 2.4 s.

**"0 under-counted" was a tautology.** The resolver's edge set is a provable subset of the occurrence
index, so A can never score below truth. Confirmed over all 769 rows.

**The 6.4x headline was a stratification artifact.** Five rows drawn from the top ten of 645 ids
supply 79.7% of the summed heuristic. Excluding that band it is 2.64x; over the resolver-covered
population, 1.53x.

**The ranking is worst where sessions trust it most.** Precision by fan-in band: 7.2% at 18+, 47.1%
at 10-17, 30.9% at 3-9, 51.8% at 1-2. `reuse_lookup` sorts fan-in descending, so rank one comes from
the 7.2% band — and `TEMPLATE-SPEC.md` §10 REQUIRES every Tier-2 spec dated on or after
`SPEC10_EVIDENCE_CUTOFF` to cite one of those answers, with hygiene check 12 refusing the spec
otherwise.

### `--converge` reaches nobody

No gate leg names `converge` or `map_diff`; no script, hook or guide invokes it.
`memory/map/reinvention-backlog.md` has never been tracked on any branch and is not gitignored — yet
`map_diff.py:171` writes it into the tracked `memory/map/` tree unconditionally. The `--converge` run
made for this dossier wrote 168 rows into that untracked file inside the memory tree. It also printed
`collision_flags: 207`, and rev-1 quoted the smaller number.

### Map coverage — the ceiling on any path-keyed integration

1303 of 1510 tracked files are UNMAPPED (86.3%); 51 of the unmapped are code. Pushed through the
consumers rev-1 named: the kickoff pointer map's kickoff row resolves 0 of 4, deployer 0 of 3,
drift-audit 1 of 8 — and that one is `kit.toml` attributing to `govkit`, a **wrong** owner, because
the govkit dossier globs `tools/*/kit.toml`. Over 150 commits only 25.3% of file-touch events resolve.

**And the ceiling is by rule, not by backlog.** `memory/map/README.md:27-29`: path globs are
digest-only and never gated, and shared mega-modules are documented in Shared-seams prose and never
glob-claimed. So the most-shared code in the tree is by design not glob-claimed, and 86.3% cannot be
driven down by writing more dossiers.

## 4. The recommendation — commit nothing, and not for the ratified reason

**Do not build a committed relations artifact.** The churn objection is measured weak at every
granularity, so finding 4's stated reason is not why. The binding reason is `AGENTS.md` §12, which
rev-1 quoted while dropping the conditional that governs it: prefer runtime derivation, and commit
plus parity-gate an artifact ONLY when a cross-language or cross-layer consumer must read it. Every
consumer here is same-language and in-process, derivation is sub-second, and the artifact would be
**five kit-to-kit rows** — a population that was 0 until 2026-08-08 and 1 until 2026-08-16.

So the answer to "should the map carry relations" is **no, not as committed data** — and the honest
grounds are population size and §12, not staleness.

**Do fix the relation data that already ships and is already mandatory.** `reuse_lookup` is a
required probe whose top-ranked answer is right 7.2% of the time. That is the defect worth building.

## 5. What the skeptics killed

Recorded rather than quietly dropped, because rev-1 asserted each of these.

- **The coarse-import-graph unit.** Killed twice: the measurement described a different artifact, and
  §12 forbids committing what an in-process same-language consumer derives in under a second.
- **The `attribute_paths` promotion.** Not refuted as a mechanism — refuted as value. It resolves
  0/4, 0/3 and 1/8 on the three consumer rows named, its one drift-audit hit is a wrong owner, and
  the map README rules out ever glob-claiming the shared modules. `gotchas.py --for-paths` needs
  nothing from it: its derived anchors already cover the whole tree and return identical output on
  mapped and unmapped files. `KEYED_ATTRIBUTORS` is `()` here, so the tested half never runs.
- **The recall-annotation join. Fatal.** `attribute_paths` returns UNMAPPED for 479 of 479 record
  paths and 82 of 82 build folders; only 3 of 20 dossiers declare a decision id; no feature-to-build
  or feature-to-spec edge exists in any committed front matter. The annotation is empty by
  construction, and `git grep` already returns 296 records for the file the join was tested on.
- **The `reuse_lookup` liveness log, as re-proposed.** `TOOL-aProvenReuse-4` records why it was
  declined and names the cheap shape — codebase-map writes its own
  `<git-common-dir>/codebase-map/lookups.jsonl` so no kit learns another kit's path. Rev-1 also
  spelled `<git-dir>` where every existing consumer uses `--git-common-dir`, which differ in the
  linked worktree this pass ran in.
- **Variant D.** Rev-1 recommended a variant it never scored; no column in it could have shown D
  failing. The ground-truth table needed an under-count column per variant and had one column total.

## 6. Live defects found in the map kit, independent of any design

Each was observed, not inferred.

1. **The freshness gate silently skips its optional tier.** `test_generated_artifacts_are_fresh`
   compares `symbols.json` only `if symbols:`; with an empty population the committed artifact is
   never compared and nothing is printed. Staged and OBSERVED: the gate passed with the symbol tier
   absent and said nothing. That is §7's "a skip must announce itself", violated inside the function
   any new tier would extend, and inherited verbatim by every non-Python adopter.
2. **The adopter's gate file is a frozen copy.** `adopt-codebase-map.sh` copies the gate template
   only when absent and leaves it untouched thereafter, while `gen_map.py` does update. A new
   generated artifact therefore starts being WRITTEN into upgraded adopters whose gate never compares
   it, and nothing gates template-versus-installed drift.
3. **`reinvention-backlog.md` is written into a tracked directory, has never been tracked, and is not
   ignored.** `TOOL-aScouredKit-16` says the rows go to "the tracked reinvention-backlog", that "the
   fiction is permanent" and that "it SHIPS to adopters" — all three false at HEAD.
4. **`RECALL_DARK_LAYERS` is an ungated authored declaration.** One consumer, at
   `reuse_lookup.py:172`, which splits the string and prints a banner. Nothing derives it from the
   languages present and nothing reds when a layer appears undeclared.
5. **`map_diff` truncates a dossier's decisions to three** with no ellipsis and no count, and emits a
   dangling separator when the list is empty — 17 of 20 dossiers.
6. **Dossier prose is ungated and already stale.** The codebase-map dossier's Gaps section still says
   "Two feature dossiers so far"; there are 20.

## 7. Forks for the owner

1. **`TOOL-aSurfacedLexicon-2` is SPECCED at order 1 to delete the tree's only AST import resolver** —
   `resolve_import` and seven sibling functions, 164 lines, with a directional kit-to-kit LAYERS rule.
   If a relation capability is ever wanted, that code is it. Rescue it into codebase-map, or let it go
   and accept that rebuilding costs those 164 lines again.
2. **Map coverage is capped by rule, not by effort.** Driving 86.3% down requires changing
   `memory/map/README.md`'s digest-only and never-glob-claim rules, which is a map-contract decision.
   Until then no path-keyed orientation feature can be worth much.
3. **Backlog pressure.** `drift_report.py` flags `live_backlog_rows_per_shard` at 268/4, out of
   tolerance. This pass declines to file new rows and carries its findings in specs instead.

## 8. What was not measured

- No AST import-graph churn existed before the skeptics measured it; the corrected 0.5%/4.5%/1.1%
  figures come from one skeptic's re-derivation and have not themselves been adversarially checked.
- The AST resolver binds only same-directory sibling imports and resolves 554 of 9666 attribute
  sites, so it is structurally incapable of producing a cross-kit edge — which makes the "5 cross-kit
  edges" figure a floor from the permissive rule, not a resolved count.
- Nothing here observed a session orienting faster. Every value claim is an argument from what a tool
  could answer.
