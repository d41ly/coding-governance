# TOOL-dDerivedDocket-36 — memory-tree docs, carriers and dossier

**Status:** SPECCED · rev-1 · 2026-09-14 · node d · Tier-2 · base abac6d59 · streams tooling · order 36

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-09-14-build-TOOL-dDerivedDocket-1-design.md](../build/2026-09-14-build-TOOL-dDerivedDocket-1-design.md) | research | TOOL-dDerivedDocket-1 TOOL-dDerivedDocket-2 TOOL-dDerivedDocket-3 TOOL-dDerivedDocket-4 TOOL-dDerivedDocket-5 TOOL-dDerivedDocket-6 TOOL-dDerivedDocket-7 TOOL-dDerivedDocket-8 TOOL-dDerivedDocket-9 TOOL-dDerivedDocket-10 TOOL-dDerivedDocket-11 TOOL-dDerivedDocket-12 TOOL-dDerivedDocket-13 TOOL-dDerivedDocket-14 TOOL-dDerivedDocket-15 TOOL-dDerivedDocket-16 TOOL-dDerivedDocket-17 TOOL-dDerivedDocket-18 TOOL-dDerivedDocket-19 TOOL-dDerivedDocket-20 TOOL-dDerivedDocket-21 TOOL-dDerivedDocket-22 TOOL-dDerivedDocket-23 TOOL-dDerivedDocket-24 TOOL-dDerivedDocket-25 TOOL-dDerivedDocket-26 TOOL-dDerivedDocket-27 TOOL-dDerivedDocket-28 TOOL-dDerivedDocket-29 TOOL-dDerivedDocket-30 TOOL-dDerivedDocket-31 TOOL-dDerivedDocket-32 TOOL-dDerivedDocket-33 TOOL-dDerivedDocket-34 TOOL-dDerivedDocket-35 PLAY-dDerivedDocket-1 DEPL-dDerivedDocket-1 |
| [2026-09-14-prompt-TOOL-dDerivedDocket-1-spec-brief.md](../prompts/2026-09-14-prompt-TOOL-dDerivedDocket-1-spec-brief.md) | journal | TOOL-dDerivedDocket-1 TOOL-dDerivedDocket-2 TOOL-dDerivedDocket-3 TOOL-dDerivedDocket-4 TOOL-dDerivedDocket-5 TOOL-dDerivedDocket-6 TOOL-dDerivedDocket-7 TOOL-dDerivedDocket-8 TOOL-dDerivedDocket-9 TOOL-dDerivedDocket-10 TOOL-dDerivedDocket-11 TOOL-dDerivedDocket-12 TOOL-dDerivedDocket-13 TOOL-dDerivedDocket-14 TOOL-dDerivedDocket-15 TOOL-dDerivedDocket-16 TOOL-dDerivedDocket-17 TOOL-dDerivedDocket-18 TOOL-dDerivedDocket-19 TOOL-dDerivedDocket-20 TOOL-dDerivedDocket-21 TOOL-dDerivedDocket-22 TOOL-dDerivedDocket-23 TOOL-dDerivedDocket-24 TOOL-dDerivedDocket-25 TOOL-dDerivedDocket-26 TOOL-dDerivedDocket-27 TOOL-dDerivedDocket-28 TOOL-dDerivedDocket-29 TOOL-dDerivedDocket-30 TOOL-dDerivedDocket-31 TOOL-dDerivedDocket-32 TOOL-dDerivedDocket-33 TOOL-dDerivedDocket-34 TOOL-dDerivedDocket-35 PLAY-dDerivedDocket-1 DEPL-dDerivedDocket-1 |

<!-- /gen:spec-records -->

## 1. Goal

After the switch-over, the prose that tells people and agents where backlog status lives still
describes authored shards. The memory-tree kit README has no section on per-build asks, five agent
prompts tell reviewers to search "the backlog shards", the memory root's own index calls each
family file a mutable shard, and the codebase map inventories the family files under a baseline no
dossier has claimed. Make every one of them describe both modes truthfully, give the kit README the
one section the adopter runbook points at, and gate the part of it that can drift.

## 2. Scope (IN)

- **S1** A section in `tools/memory-tree/README.md`, "Backlog modes — authored shards and per-build
  asks", which the adopter runbook's switch section names as the home of the grammar, the verdicts
  and the status fold. It states the absent-key default, the row kinds with who writes each, the
  fold's rules in their order, the verdict list, the ask clauses and READY, the print modes, and the
  transition audit with a pointer to the recipe `migrate_backlog.py --recipe` prints rather than a
  copy of it. Observed by AC1 and AC2.
- **S2** A drift arm in `gen_build_index.py --selftest`: every verdict id and every disposition kind
  the ask module's source declares must appear in that README section, and the arm prints the counts
  it compared, refusing when either count is zero. Observed by AC2.
- **S3** The rest of the kit README. Its "What's here" table carries a row for every tracked file
  under the kit directory that has none. Its merge-driver section carries the
  `memory/builds/*/BACKLOG.md merge=rows` line beside the two it shows, and says why the backlog line
  stays. Its M6 clause-3 section agrees with the build-method render at this unit's commit. An
  upgrade note says an upgrade changes nothing until `BACKLOG_MODE` is set. Observed by AC3.
- **S4** Five agent carriers read both modes. The prior-art lens in
  `tools/workflows/tier2-review.js`, the memory-rot lens in `tools/workflows/drift-audit-state.js`,
  `tools/drift-audit/SKILL.template.md`, `tools/workflows/REVIEW-PROTOCOL.template.md` and
  `tools/memory-recall/SKILL.template.md` each tell an agent to read the open asks through the build
  index generator's `--asks --json` and, when its `mode` field says `shards`, the backlog shards.
  None names a sibling kit's path by literal. Each rendered copy is regenerated. Observed by AC4 and
  AC5.
- **S5** `memory/README.md`'s backlog line says the family files are generated views of asks filed
  in `builds/<slug>/BACKLOG.md`. Observed by AC6.
- **S6** The map. A new dossier, `memory/map/features/memory-tree-backlog.md`, claims the four
  `backlog-shards` keys: `KICK.md`, `PLAY.md` and `TOOL.md` leave `memory/map/baseline.toml`, and
  `DEPL.md` moves from `memory/map/features/govkit.md`. The comment on the `backlog-shards`
  extractor in `tools/codebase-map/map_extractors.py` describes both modes, and the merge-driver
  dossier's title and prose name `BACKLOG.md`. The generated map is regenerated in the same commit.
  Observed by AC7.
- **S7** Kit versions. Each kit whose shipped bytes change here carries a matching constant and
  marker, and a kit an earlier unit of this build already moved in this landing range is not moved
  twice. The memory-tree constant follows `tools/memory-tree/check-verdict-epoch.sh`'s topological
  rule: its one bump for the landing range sits at or after the range's last engine change, which
  this unit places here when no later unit moves an engine line. Observed by AC8.

## 3. Non-goals (OUT)

- `memory/HYGIENE.md`, `memory/TEMPLATE-SPEC.md` and their templates are the hygiene-engine unit's,
  which describes both modes for every check it changes.
- `memory/guides/BUILD-METHOD.md` is the carriers unit's and the method-carriers unit's; this unit
  only makes the kit README's explanation of M6 agree with whatever they leave.
- The charter, `AGENTS.md` and the adopter runbook are the charter unit's and the runbook unit's.
  The kickoff manifest's backlog claims are the switch-over's.
- No rename of the `backlog-shards` inventory. Every dossier carries that field name, and renaming it
  would churn all of them to say what one comment can.
- No change to what the ask module parses or decides. S2's arm reads its source and changes none of
  it.

### Edges

- **consumes-from** `TOOL-dDerivedDocket-34` — the switched tree the docs describe, with its views
  rendered and asks filed. Written before it, every sentence here would describe a tree that does
  not exist.
- **hands-off** `DEPL-dDerivedDocket-1` — the kit README's backlog-modes section, which the
  runbook's switch section names as the home of the grammar, the verdicts and the fold. Added by
  this spec, answering that unit's declared edge.

## 4. Design

### The README section, and why it is the home rather than a copy

The runbook unit's proposed text says the grammar, the verdicts and the fold "are
`tools/memory-tree/README.md`'s", so the README is where an adopter lands. An author writing a row
by hand needs the grammar in prose, and the module states it as code. So the README section is the
author-facing statement, and S2 is what stops it drifting from the code: an arm over the module's
own source, not a promise.

| Part | Content | Owned by, and how the README stays true |
|---|---|---|
| default | absent `BACKLOG_MODE` reads `shards`, byte-identical to today | the conf reader; stated once |
| row kinds | ask, CLOSED, WONTDO, BLOCKED, DEFERRED, KEEP, REOPEN, SEV, RELOCATED, and who writes each | S2's arm, over the kinds the module declares |
| the fold | its rules in order, order-free over sets, REOPEN cancelling a named record | prose, citing the fold function by name |
| verdicts | each V-number with its one-line meaning | S2's arm, over the ids the module raises |
| ask clauses | `seen`, `accept`, `may`, `out`, `verify`, READY, and `PROBE_ALLOW` | prose, citing the envelope unit's parser |
| print modes | `--asks` with `--all`, `--json`, `--build`, `--ready`, `--tsv`, `--at` and `--probe`, and the `--new-build` scaffold | prose; a mode the generator lacks would fail AC1's walk |
| stragglers | the transition audit, `--stragglers`, `--relocate`, `--ingest`, `--repair` | a pointer to `--recipe`, which is single-sourced |

### The drift arm

`gen_build_index.py --selftest` gains one arm. It reads the ask module's source through the same
path the generator imports it by, collects every `V<digits>` verdict id it raises and every
disposition kind its row grammar admits, and reads the README section between its heading and the
next `## `. Each id or kind the module has and the section lacks is a failure naming it. The arm
prints `compared <v> verdicts and <k> kinds`, and zero on either side is a DEAD PROBE, because an
extractor that finds nothing agrees with every document. A kit README is a kit file, so the arm
reads within its own kit and names nothing outside it.

### The carriers, and the one sentence each must survive

At BASE the five carriers say "the backlog shards" (`tools/workflows/tier2-review.js:315`), "the
backlog rows" (`tools/workflows/drift-audit-state.js:198`), "the OPEN backlog rows"
(`tools/drift-audit/SKILL.template.md:109`), "the open backlog"
(`tools/workflows/REVIEW-PROTOCOL.template.md:188`) and "`DECISIONS.md` / `BACKLOG.md` index"
(`tools/memory-recall/SKILL.template.md:91`). DR cites the review protocol at `:179`; the sentence
sits at `:188` at BASE.

Under `builds` the family file an agent would open is a view of live asks only, so "search the
backlog" there silently omits every terminal ask and its reason. Under `shards`, which every adopter
runs until its own switch, `--asks --json` prints the mode notice and an empty set. So each carrier
names the generator's `--asks --json` and tells the agent to read the shards when the output's
`mode` field says `shards`. The two workflow scripts are deployed verbatim and carry no render
tokens, so they name the generator by its file name and never by a path with an install prefix,
which the install-prefix gate would refuse.

### The map

`memory/map/baseline.toml` lists `KICK.md`, `PLAY.md` and `TOOL.md` unclaimed, and
`memory/map/features/govkit.md` claims `DEPL.md`, measured at BASE. The new dossier claims all four,
since after the switch they are four views of one mechanism, and govkit's claim of one of them was
never about the deployer. The baseline only shrinks, which is exactly this move. The extractor keeps
its name and gains a comment saying the files are authored shards or generated views by mode.

### Inventory

| Identifier | Kind | Cell |
|---|---|---|
| the README section heading | kit README heading | none |
| the drift arm | a `--selftest` arm in `gen_build_index.py` | lexicon `py.function`; its helper names pass `python tools/lexicon/lexicon.py --suggest <name> --as py.function` first |
| `memory/map/features/memory-tree-backlog.md` | map dossier | `feature = "memory-tree-backlog"` |

### Files touched (estimate)

`tools/memory-tree/README.md` · `tools/memory-tree/gen_build_index.py` (the arm) ·
`tools/workflows/tier2-review.js` · `tools/workflows/drift-audit-state.js` ·
`tools/drift-audit/SKILL.template.md` and its render · `tools/workflows/REVIEW-PROTOCOL.template.md`
and `memory/guides/REVIEW-PROTOCOL.md` · `tools/memory-recall/SKILL.template.md` and its render ·
`memory/README.md` · `memory/map/features/memory-tree-backlog.md` (new) ·
`memory/map/features/govkit.md` · `memory/map/features/memory-tree-merge-driver.md` ·
`memory/map/baseline.toml` · `tools/codebase-map/map_extractors.py` · `memory/map/generated/`.

### Alternatives rejected

- **The README points at the module and states nothing.** The runbook unit names the README as the
  home, and a row written by hand needs its grammar in prose; S2 is the price of stating it.
- **Carriers naming `--asks --json` alone.** Every shards-mode adopter's agents would read an empty
  set as "no open asks".
- **Leaving `DEPL.md` with the govkit dossier.** Four views of one mechanism split across two
  dossiers is the map disagreeing with itself.

## 5. Production-readiness checklist

- security — N/A: documentation, agent prompt wording and a read-only self-test arm; nothing new
  executes and nothing new is written at run time.
- perf / scale — one more file read in a self-test.
- error / empty / loading states — the drift arm refuses a zero count on either side instead of
  agreeing with an empty extraction.
- observability — the arm's compared counts; the regenerated map's claim table.
- risks — a carrier's wording changes what a reviewer reads, and a review run after this unit reads
  asks where it read shards. The `mode` fallback keeps every shards-mode tree on the old reading.
- testing — S2's arm, observed RED by deleting one verdict line from a scratch copy of the README;
  the render and map legs for the rest.
- migration — none; every carrier reads both modes.
- user docs — this unit is the user docs for the backlog modes.

## 6. Acceptance criteria

- **AC1** — When each read-only print mode the README section names is run as
  `python tools/memory-tree/gen_build_index.py <mode>` on the switched tree, it exits 0; the
  `--new-build` scaffold, which writes, is matched by name against the generator's own usage text
  instead of being run.
  Red when: the section names a flag the generator does not have, which an adopter following the
  runbook meets as an unknown-argument error.
- **AC2** — When `python3 tools/memory-tree/gen_build_index.py --selftest` runs against a scratch copy
  of the README with one verdict's line deleted, the drift arm fails naming that verdict; on the real
  README it prints non-zero compared counts and passes.
  Red when: the arm reads verdict ids from the README instead of the module, so it can only confirm
  itself.
- **AC3** — When `git ls-files tools/memory-tree` is compared with the README's "What's here" table,
  every tracked kit file has a row, and the merge-driver block carries three attribute lines.
  Red when: a file this build added under the kit, such as the transition audit module, has no row.
- **AC4** — When `grep -n 'backlog shards' tools/workflows/tier2-review.js` runs, it finds the phrase
  only inside the sentence naming the `mode` fallback, and `bash tools/check-install-prefix.sh`
  passes.
  Red when: the lens names the generator by a prefixed path, which the install-prefix gate refuses
  for a file deployed verbatim.
- **AC5** — When `bash tools/workflows/check-protocol-parity.test.sh`,
  `bash tools/memory-recall/adopt-memory-recall.sh --check` and
  `bash tools/drift-audit/adopt-drift-audit.sh --check` run, each rendered carrier matches its
  template.
  Red when: a template moves and its render is left behind.
- **AC6** — When `memory/README.md` is read, its backlog line names each build folder's `BACKLOG.md`
  and calls the family files generated, and `bash tools/memory-tree/check-memory-hygiene.sh` passes.
  Red when: the line still calls each file a mutable shard, the claim this repo's own index makes
  about a file nobody may edit.
- **AC7** — When `python3 tools/codebase-map/test_codebase_map.py` runs, it passes with
  `memory/map/baseline.toml` holding no `backlog-shards` key and the new dossier claiming all four.
  Red when: `DEPL.md` is claimed by both dossiers, which the map's collision flag reports.
- **AC8** — When `bash tools/check-kit-versions.sh` runs, and the verdict-epoch check
  `tools/memory-tree/check-verdict-epoch.sh` runs over the build's range, every kit whose bytes this
  unit moved carries an agreeing constant and marker, and the memory-tree constant's last bump is at
  or after the range's last engine change.
  Red when: a marker is left behind its constant after a template edit, or the epoch bump lands
  before an engine line this unit moved.

## 7. Gates

`build-index selftest` · `review-protocol parity (kit vs dogfood)` · `memory-recall skill wiring` · `drift-audit wiring` · `workflow script syntax` · `install-prefix (shipped surface)` · `codebase-map coverage + freshness` · `kit version markers` · `verdict epoch (kit version dates the engine)` · `memory hygiene` · `line length`

New arm: `tools/memory-tree/gen_build_index.py --selftest` · a scratch README missing one verdict line, and a module whose extraction yields nothing · the build-index selftest's arm count

## 8. Open questions

- **F1** — Does the README state the grammar, or point at the module? The runbook unit names the
  README as the home. RESOLVED (agent, 2026-09-14, delegated): it states it, and S2's arm keeps it
  honest against the module's source.
- **F2** — Which `backlog-shards` keys does the new dossier claim? Options: the three in the
  baseline; all four, moving `DEPL.md` from the govkit dossier. RESOLVED (agent, 2026-09-14,
  delegated): all four, since the brief's "the backlog-shards keys" are one mechanism's.
- **F3** — The design record names five carriers; how does each read a tree still in shards mode?
  RESOLVED (agent, 2026-09-14, delegated): through the `mode` field of `--asks --json`, falling back
  to the shards, because the generator prints an empty set there by design.

## 9. Revision log

- rev-1 · 2026-09-14 · initial draft. Adds one edge the brief's table does not list, hands-off the
  runbook unit, which declares the matching consumes-from.

## 10. Reuse audit

The README section, the arm and the carriers extend seams that exist. The kit README is the kit's
own documentation home, and its merge-driver section is where the attribute block already lives.
The drift arm joins the existing `gen_build_index.py --selftest`, and its compare-two-populations
shape with a zero-count refusal is the one `tools/check-kit-versions.sh` uses for its marker pairs.
The dossier follows the shape of every file under `memory/map/features/`, and claiming keys out of
`memory/map/baseline.toml` is the move that file's header prescribes. `python
tools/codebase-map/reuse_lookup.py "document the per-build backlog asks and point agent carriers at
the generated asks view"` returned `backlog_keys` and `append_backlog` in
`tools/codebase-map/map_lib.py`, which serve the map's own reinvention backlog and are unrelated,
and name-stem `build_*` neighbours; no seam documents or carries ask status today. Recall returned
the design record's list of the five carriers and the map's current claim table, where `DEPL.md`
sits with govkit.

Where DR and the source disagree at BASE: DR cites the review protocol's sentence at `:179`, and it
sits at `:188`. DR says the dossier claims "the three `backlog-shards` keys", and there are four
inventory keys, one already claimed (§8 F2).

Recall terms used: `backlog shards carriers dossier baseline backlog-shards map_extractors README
merge driver asks view prior-art lens`
