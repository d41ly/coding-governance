# PLAY-aMendedFleet-1 — the AGENTS.md wrapper's merge-bar section moves to a guide, without its repeated catalog or dated history

**Status:** CLOSED · rev-2 · 2026-10-04 · node a · Tier-2 · base 7af5f564 · streams playbook · ratified 2026-10-04 · order 79

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-04-build-PLAY-aMendedFleet-1-1-acceptance-ledger.md](../build/2026-10-04-build-PLAY-aMendedFleet-1-1-acceptance-ledger.md) | journal | — |

<!-- /gen:spec-records -->

## 1. Goal

`AGENTS.md` loads into every session and every workflow agent, and at base it measures 64344
bytes and 586 lines, PINNED 2026-10-04 with `wc -c -l`. Its authored merge-bar section is 8587 of
those bytes. It spells a five-line command block that the rendered §6 command catalog already
carries in three of its lines, and it keeps a dated paragraph of 2026-08-23 measurements that its
own text says live in `<git-dir>/gate-ledger.tsv`. This unit moves the section's body into a guide
the wrapper points at, drops the repeated catalog and the dated history on the way, and keeps in
the always-loaded file only the facts a session needs before it opens the guide. The brief's third
item, the duplicate node registry, is a separate mechanism and is split out (§8 F1).

## 2. Scope (IN)

- **S1** — A new guide, `memory/guides/MERGE-BAR.md`, holds the body of the wrapper's
  `## The merge bar` section verbatim, minus what S2 and S3 drop and minus the push-boundary opening
  sentence S4 keeps in the wrapper. It opens with an H1 and one line naming when to read it: before
  running, scoping or debugging a bar, and before a push. Observed by AC3 and AC4.
  **Readers:** by name: `AGENTS.md` holds the section, and `.unattended.conf` cites it as "the
  charter's merge-bar section", which S4 keeps under the same heading. by value: NO VALUE READERS —
  no checker parses the section's text; the leg list it describes is read from `tools/gate-legs.json`.
- **S2** — The section's five-line command block is not carried into the guide. Its first three
  lines repeat the rendered §6 everyday-command catalog. Its two self-test lines are carried by S4's
  wrapper sentence instead, and the "NOT the whole bar" caveat on its third line becomes that same
  sentence's clause. Observed by AC2.
  **Readers:** by name: `AGENTS.md` alone spells the block; `.unattended.conf` cites the kit
  Definition of Done pair it named, which S4 keeps. by value: NO VALUE READERS — no checker parses
  the block, and the leg list is read from `tools/gate-legs.json`.
- **S3** — The paragraph opening "Measured on node `d` 2026-08-23" is dropped, not moved. Its own
  last sentences say none of its figures is authored and that the per-leg table is a `sort -rn`
  over `<git-dir>/gate-ledger.tsv`; the build record that measured it stays reachable from
  `memory/LIVE.md`. Observed by AC2.
  **Readers:** by name: `AGENTS.md` alone spells the paragraph. by value: NO VALUE READERS — prose
  figures that nothing computes from; the ledger is the measured source.
- **S4** — The wrapper keeps a `## The merge bar` section of at most 1100 bytes, PINNED as this
  design's ceiling. It says, in this order: the leg list is `tools/gate-legs.json` and the everyday
  invocations are §6's catalog; `GATE_SELFTESTS` also runs the held self-tests, which `GATE_FULL`
  alone does not, on demand only with no boundary setting it (owner, 2026-08-27), and KIT work owes
  the two together at its Definition of Done; a default-branch push runs the bar once in
  `.githooks/pre-push`, which blocks a red one unless the inherited-red policy in
  `.githooks/gate-env.sh` lands it; everything else is the guide, read at S1's moments. The heading
  keeps its text, so a reader citing "the charter's merge-bar section" still lands on it. Observed by
  AC1.
- **S5** — The guide is claimed in `memory/map/features/run-gates.md`, whose `guides` list is empty
  at base, and the map's generated artifacts are re-rendered in the same commit. Observed by AC6.
- **S6** — The charter's byte high-water in `tools/template-size-highwater.txt` is re-recorded with
  `--bump` at the shrunk size, so regrowth toward today's figure prints the gate's WARN. Observed by
  AC5.

## 3. Non-goals (OUT)

- The wrapper's `## Node registry` table. It is split out to `PLAY-aMendedFleet-4` (§8 F1), and
  this unit leaves it byte-identical.
- The rendered `gov:playbook` region, the template and `.governance/deploy.toml`. §6's catalog line
  is the surviving copy and is not edited, so the render-wiring leg sees no change.
- Lowering the charter's 64512-byte ceiling in `tools/template-size-limits.txt` (§8 F3).
- The kickoff manifest's own gate-command block, a third catalog in a different carrier, which the
  brief does not name and which sits 36 bytes under its own cap.
- Rewording the moved paragraphs, including the closing line that spells the drift report and the
  `--for-diff` checklist; the build method's M6 already spells that command, unit 78 adds the
  path-set commands beside it in M5, and a reword here would re-review prose this unit only moves.
- The wrapper's "What ships here" and "Layout" sections, and running `/doctor prompt-audit`, which
  is interactive-only.
- Measuring the context diet. `TOOL-aMendedFleet-94`, split from unit 74, is ordered after that
  measurement; this unit records the byte delta in its commit and nothing more.

### Edges

- **hands-off** `PLAY-aMendedFleet-4` — the node-registry deduplication, split to that unit at §8 F1:
  the template's single-row §2 table, the renderer's drop list, and the wrapper's table.

## 4. Design

### Evidence

Read at base `7af5f564`; `AGENTS.md`, the size records and the run-gates dossier are byte-identical
at the worktree tip `efc4b0c9`.

- `AGENTS.md` lines 467-570 are the section, 8587 bytes, which is the report's figure exactly. Lines
  476-481 are the command block, 595 bytes; lines 515-522 are the dated paragraph, 808 bytes.
- Line 226 is the rendered §6 catalog, from `command_catalog` in `.governance/deploy.toml`: the bar,
  `GATE_JOBS=1`, `GATE_FULL=1` and the lander. The block's first three lines repeat it.
- `memory/DECISIONS.md` row `TOOL-dDerivedDocket-73` is an owner ruling that "AGENTS.md's merge-bar
  sentence points at the inherited-red policy"; S4 keeps that sentence in `AGENTS.md`.
- `.unattended.conf` lines 26-30 cite "the pair the charter's kit Definition of Done names" and the
  on-demand use "the charter's merge-bar section sanctions"; S4 keeps both facts in that section.
- `tools/check-template-size.sh AGENTS.md` grades the whole file against the 64512 row;
  `tools/template-size-highwater.txt` records 60930, below today's 64344, so the leg prints an
  advisory WARN at base. `--bump` writes whatever it measures, downward included.
- Hygiene check 6 caps every file under `memory/guides/` at `GUIDE_CAP_BYTES`, 98304, so the guide is
  watched and check 16 rule 3 is satisfied for a charter pointer at it. Checks 14 and 15 grade
  ids and paths cited inside `guides/`, so every moved citation must resolve; at base each does in
  `AGENTS.md`.
- `tools/codebase-map/map_extractors.py` inventories `memory/guides/*.md` by filename, so a new guide
  is an unclaimed key until a dossier claims it. `memory/map/features/run-gates.md` measures 20308
  of the 20480-byte dossier cap, so S5's claim of about 16 bytes fits.
- The wrapper's `## Node registry` heading is read by name: `skills/session-kickoff/manifest-check.sh`
  derives the card's `node —` cell from the first table under it, in the file the kickoff manifest's
  `registry:` key names, which is `AGENTS.md`. `tools/drift-audit/drift_report.py` matches every
  tag row in the charter. The rendered §2 table holds node `a` alone, from the template's single-row
  placeholders. This is why F1 splits rather than deletes.

### The wrapper section, as it will read

```markdown
## The merge bar — `bash tools/run-gates/run-gates.sh`

The leg list is `tools/gate-legs.json`, and the everyday invocations are §6's command catalog.
`GATE_SELFTESTS=1` also runs the held self-tests, which `GATE_FULL=1` alone does not: on demand
only, since no boundary sets it (owner, 2026-08-27), and KIT work owes the two together at its
Definition of Done. A default-branch push runs the bar once in `.githooks/pre-push`, which blocks
a red one unless the inherited-red policy in `.githooks/gate-env.sh` lands it. How the bar behaves
beyond that is `memory/guides/MERGE-BAR.md`: read it before you run, scope or debug a bar, and
before a push.
```

About 690 bytes. With the moved 8587 bytes gone, `AGENTS.md` lands near 56450, an ESTIMATE that
AC5 re-derives.

### The guide

`# The merge bar — how it behaves`, the when-to-read line, then the section's paragraphs in their
order: the leg-list paragraph, "Guards scope a run", "How the bar behaves", the kit self-test
paragraph, the leg-count sentence, the gate-logs paragraph, the push-boundary paragraph from its
second sentence onward, "Two protocols are BINDING" with both bullets, and the drift and checklist
line. The push paragraph's opening sentence is S4's; the guide's paragraph opens on what follows it
and reads as a sentence. About 7.2 KB.

### Files touched (estimate)

- `AGENTS.md`
- `memory/guides/MERGE-BAR.md`
- `memory/map/features/run-gates.md`
- `memory/map/generated/MAP.md`
- `memory/map/generated/inventories.json`
- `tools/template-size-highwater.txt`

### Rollout

One commit: the guide, the trimmed wrapper, the claim with its regenerated map, and the bump. The
wrapper is gov's own and no adopter receives it, so nothing ships.

### Alternatives rejected

- **Moving the section without the wrapper keeping anything.** It strands the owner ruling's
  inherited-red sentence and the kit Definition of Done pair outside the always-loaded file, and
  two carriers cite them as the charter's.
- **Keeping the command block in the guide and repointing §6 at it.** §6 requires the instantiated
  doc to carry the catalog, so the always-loaded copy is the one that stays.
- **Moving the dated paragraph into the guide.** Its own text says the figures live in the ledger; a
  guide copy would be the stale-prose-beside-its-source class one level down.

## 5. Production-readiness checklist

- security — N/A — prose moved between two tracked documents; no new write path.
- perf / scale — every session and workflow agent reads about 7.9 KB less, ESTIMATED.
- error / empty / loading states — N/A — no runtime behaviour.
- observability — the charter-size leg prints the new figure, and S6's bump makes regrowth WARN.
- risks — a session that never opens the guide loses the guard and push detail; S4 keeps the facts
  two carriers and one owner ruling cite, and names when to open the guide.
- testing — direct greps over both files, one size check, the id and path checker, and the map's
  coverage checker.
- migration — N/A — no stored state.
- user docs — N/A — the charter and the guide are the user docs.

## 6. Acceptance criteria

- **AC1** — When `awk '/^## The merge bar/,/^## Conventions/' AGENTS.md` runs, its output is at most
  1100 bytes counted with `wc -c` and names `.githooks/gate-env.sh`, `tools/gate-legs.json` and the
  guide's basename `MERGE-BAR.md`.
  Red when: the section keeps its moved body, or drops the inherited-red pointer or the guide pointer.
  figure: 1100 is PINNED as this design's ceiling; 8587 is the base measurement.
- **AC2** — When `grep -c -e "Measured on node" -e "^GATE_" -e "^bash tools/run-gates" AGENTS.md`
  runs, it prints 0, and `grep -rc "Measured on node" memory/guides` prints 0 for every guide.
  Red when: the dated paragraph or a command-block line survives in the wrapper or the guide.
- **AC3** — When `grep -rl -e "Guards scope a run" -e "Two protocols are BINDING" -e "Every leg's output is persisted" memory/guides AGENTS.md`
  runs, it prints one path, the guide's.
  Red when: a moved paragraph is still in `AGENTS.md`, or was lost in the move.
- **AC4** — When `grep -n -e "before you run, scope or debug a bar" -e "TOOL-aRepatriatedFork-5" -e "core.hooksPath" memory/guides AGENTS.md -r`
  runs, the first phrase hits both the guide's opening and the wrapper section, and the other two
  hit the guide only.
  Red when: the guide lacks its when-to-read line, or the push paragraph's detail stayed behind.
- **AC5** — When `bash tools/check-template-size.sh AGENTS.md` runs after S6's bump, it exits 0, prints
  a byte figure at least 7000 below 64344 and prints no WARN line, and
  `grep -n "^AGENTS.md" tools/template-size-highwater.txt` prints that same figure.
  Red when: the charter did not shrink, or its high-water still reads 60930.
  figure: 64344 and 60930 are PINNED at base; the new figure is DERIVED by the run.
- **AC6** — When `python tools/codebase-map/test_codebase_map.py` and
  `python tools/codebase-map/gen_map.py --check` run, each exits 0, and
  `grep -n "MERGE-BAR.md" memory/map/features/run-gates.md` hits the `guides` claim.
  Red when: the new guide is an unclaimed inventory key, or the generated map is stale.
- **AC7** — When `python tools/memory-tree/corpus_ids.py --check` runs, it exits 0.
  Red when: a citation moved into the guide names an id or a path that does not resolve, which
  checks 14 and 15 grade under `guides/` and not in `AGENTS.md`.
  cost: about 10 s, measured 2026-10-04.

No new refusal or gate clause is added, so nothing here is observed RED on a staged break; each
`Red when:` names the break an existing checker or grep reports.

## 7. Gates

`charter size` · `line length` · `playbook render wiring` · `agent-cap restatement` · `codebase-map coverage + freshness` · `recall floor` · `recall floor arms` · `memory hygiene` · `drift-audit records` · `spec tokens (a spec's own names resolve)`

The two recall legs are owed by the `memory/` guard, since the guide joins the recall corpus. All
run once, at the close.

## 8. Open questions

- **F1** — Does this unit delete the wrapper's `## Node registry` table?
  Options: delete it and leave the rendered §2 table, which holds node `a` alone, as the registry;
  delete it and teach the renderer to render every node's row from `.governance/deploy.toml`, then
  move the card's reader and the kickoff manifest's `registry:` key to §2; keep it here and split the
  deduplication out. The first silently drops nodes `b`, `c` and `d` from the card's `node —` cell
  and from drift-audit's node resolution. The second spans the template, the renderer, the deploy
  answers and the kickoff kit's reader, which is a second mechanism and a new deploy-time surface.
  Recommendation: split. `WIRE-INTO-PROJECT.md` also tells adopters the charter's §2 serves as the
  registry, which the heading-keyed reader cannot find; the new unit, `PLAY-aMendedFleet-4`, puts
  that adopter-facing claim out of its scope (its §3), so no unit of this build owns it.
  RESOLVED (agent, 2026-10-04, delegated): split — the node-registry deduplication moves to a new
  unit the run adds; this unit keeps the table byte-identical.
- **F2** — Is the dated measurement paragraph moved into the guide or dropped?
  Options: move it; drop it. The brief's sentence binds "moves to a guide" loosely, and the report's
  delete list names the dated history as a deletion. Its own text says the figures are derived from
  the ledger.
  RESOLVED (agent, 2026-10-04, delegated): drop it; the section's remaining body moves.
- **F3** — Does the charter's 64512-byte ceiling drop with the trim?
  Options: lower the row to the new size plus headroom; keep it and re-record the high-water. A row
  movement is a deliberate act whose justification lives beside it, and several units of this build
  edit the rendered region the ceiling also prices. The high-water ratchet already prices regrowth.
  RESOLVED (agent, 2026-10-04, delegated): keep the row, re-record the high-water.

## 9. Revision log

- rev-1 · 2026-10-04 · initial draft, from the wrapper, the size records, the two registry readers
  and the run-gates dossier at base.
- rev-2 · 2026-10-04 · §3 · §8 · M2 cross-read: the registry split now names `PLAY-aMendedFleet-4`
  in the non-goal and the edge; F1 said that unit owns the runbook's §2-registry claim, which its
  §3 puts out of scope; §3 said unit 74 waits on the diet measurement, but unit 74 builds dark at
  its order and the wait travels with `TOOL-aMendedFleet-94`; and §3 credited unit 78 with the
  `--for-diff` command's home, which M6 already is.

## 10. Reuse audit

The seams are the memory tree's existing guide slot, `memory/guides/`, which check 6 caps and
check 16 accepts as a charter pointer target, and the existing size ratchet,
`tools/check-template-size.sh --bump`. The guide follows the shape of the four existing guides the
charter already points at. No code is added. `python tools/codebase-map/reuse_lookup.py "move a long
section of the always-loaded charter into a guide the charter points at"` returned only `load_*`
helpers by name stem and the `.unattended.conf` affordance seam, which is the carrier S4 keeps true;
no existing mechanism moves charter prose, so no existing seam fits beyond the guide slot itself.
Recall named `TOOL-dDerivedDocket-73`, the owner ruling S4 preserves, and the dDerivedDocket run's
record of the on-demand self-test ruling the wrapper keeps. Where the report and the tree disagree:
the report's 64,344 bytes and 8,587-byte slot both hold at base; its "second node registry
(`:154-156` disagrees with `:62-67`)" holds too, and is split out by F1 rather than deleted.

Recall terms used: `python tools/memory-recall/query.py "which record decides what the AGENTS.md
merge bar section holds and whether it may move out of the charter" --terms "AGENTS.md wrapper
merge bar section charter size high-water externalize guide context diet always-loaded command
catalog node registry"`
