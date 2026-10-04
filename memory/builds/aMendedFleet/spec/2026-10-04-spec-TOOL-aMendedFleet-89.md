# TOOL-aMendedFleet-89 — measured history leaves the dossiers near the byte cap for the records that measured it

**Status:** SPECCED · rev-1 · 2026-10-04 · node a · Tier-1 · base 7af5f564 · streams tooling · ratified 2026-10-04 · order 89

<!-- gen:spec-records -->

*No record names this unit.*

<!-- /gen:spec-records -->

## 1. Goal

Seven codebase-map dossiers sit within 10% of the 20,480-byte `DOSSIER_CAP_BYTES` cap, so the next
true constraint any of them must record has to evict another one. A large share of their prose is
measured history: which node measured what, when, and the incident that led to a rule. That history
is not derivable from the code, but it is already written in the build record that measured it, and
a dossier that restates it is a second copy that rots. This unit writes the rule that measured
history lives in the record that measured it, with the dossier stating the constraint in the present
tense and citing that record's id, and applies the rule to the seven dossiers until each sits outside
the 10% band. Unit 43, from which this was split, renders cards from the toml fences and never reads
this prose.

## 2. Scope (IN)

- **S1** — THE RULE. One bullet joins the Rules list of `_README` in
  `tools/codebase-map/gen_map.py` and, with identical wording, the Rules list of its dogfood rendering
  `memory/map/README.md`: a dossier states a constraint and its reason in the present tense; WHEN,
  WHERE and ON WHICH NODE a figure was measured, and the incident that produced the rule, live in the
  record that measured it, which the dossier cites by id. `memory/map/README.md` is written only at
  `--scaffold`, so both copies are hand-edited in the one commit. Observed by AC3.
- **S2** — THE SEVEN. The prose of `memory/map/features/agent-cap.md`,
  `memory/map/features/unattended.md`, `memory/map/features/runlog.md`,
  `memory/map/features/run-gates.md`, `memory/map/features/lexicon.md`,
  `memory/map/features/memory-tree-hygiene.md` and `memory/map/features/memory-tree-merge-driver.md`
  is edited under S1's rule until each file is at most 18,432 bytes, which is 90% of the cap.
  A measurement passage becomes the constraint it justifies plus the id of the record that holds the
  measurement. A constraint, a seam or a gap that is not history stays. Observed by AC1 and AC2.
- **S3** — Every record id the edit cites is one this tree already defines, found by `git grep`
  under the build folders or in `memory/DECISIONS.md`; a measurement whose record cannot be found
  keeps its sentence, because deleting the only copy of a non-derivable fact is the loss the rule
  exists to prevent. Observed by AC2.
- **S4** — No toml fence moves. Only prose below each fence is edited, so `MAP.md`,
  `inventories.json` and the cards file unit 43 adds stay byte-identical. Observed by AC3.

## 3. Non-goals (OUT)

- The cards unit 43 renders from the fences, and any change to the cap or to how hygiene check 6
  prices a dossier.
- Dossiers outside the 10% band. The rule applies to them on their next edit, never by a sweep here.
- A new home for measured history, such as a per-feature history file. §8 F1 rejects it.
- A gate that grades dossier prose for history. Prose has no shape a gate can read for this, and
  unit 44 already lints dossier prose for typed population counts.
- Bumping the codebase-map kit version, owed once at the build's close.

### Edges

- **hands-off** external — the codebase-map kit version bump, owed once at the close, since S1
  moves `gen_map.py`.

## 4. Design

### Evidence

Measured at the worktree HEAD `8312d315`, whose bytes under `memory/map/` and `tools/codebase-map/`
equal base `7af5f564`'s. PINNED, measured 2026-10-04 on node a.

| Dossier | Bytes | Over 18,432 by |
|---|---|---|
| `agent-cap` | 20,479 | 2,047 |
| `unattended` | 20,478 | 2,046 |
| `runlog` | 20,315 | 1,883 |
| `run-gates` | 20,308 | 1,876 |
| `lexicon` | 20,258 | 1,826 |
| `memory-tree-hygiene` | 20,153 | 1,721 |
| `memory-tree-merge-driver` | 19,677 | 1,245 |

- The next largest dossier is `spec-tokens` at 15,247 bytes, so the band holds exactly these seven,
  as the review said.
- Each of the seven carries three to seven lines that a case-insensitive grep for `measured` or a
  full date hits, such as `agent-cap`'s node-spawn timing and `run-gates`'s 2026-08-20 measurement of
  the unattended legs. The prose around them narrates the incident at more length than the hit line.
- `memory/map/README.md` is written by `gen_map.py --scaffold` from `_README` and by nothing else, so
  `gen_map.py --check` never compares it; the two copies agree only because both are edited together.

### The rule's wording

```text
- Measured history lives in the record that measured it. A dossier states each constraint and its
  reason in the present tense and cites that record's id; when, where and on which node a figure was
  measured, and the incident behind a rule, stay in the record, never copied into the dossier.
```

### Files touched (estimate)

- `tools/codebase-map/gen_map.py`
- `memory/map/README.md`
- `memory/map/features/agent-cap.md`
- `memory/map/features/unattended.md`
- `memory/map/features/runlog.md`
- `memory/map/features/run-gates.md`
- `memory/map/features/lexicon.md`
- `memory/map/features/memory-tree-hygiene.md`
- `memory/map/features/memory-tree-merge-driver.md`

### Rollout

Unit 43 edits the layout list of the same `_README` and `memory/map/README.md`, and is ordered
first; this unit edits the Rules list below it and rebases onto unit 43's commit.

### Alternatives rejected

- **A per-feature history file under the map root.** It is a third place a fact can live, a new
  file kind the map's layout and hygiene check 4 would both have to admit, and it is still a copy of
  what the build record holds.
- **A `## History` section at the end of each dossier.** It moves the bytes without saving any, so
  the seven stay inside the band.
- **Raising the cap.** The cap is the reason a dossier stays readable, and a raise is the move
  `TOOL-dFoldedVerdict-7` records capped documents making silently.

## 5. Production-readiness checklist

- security — N/A: prose edits to tracked records.
- perf / scale — the seven dossiers shrink by about 12.6 KB together, which every reader of them and
  the recall corpus stop paying for.
- error / empty / loading states — a measurement with no findable record keeps its sentence, per S3.
- observability — the byte sizes are the observation; AC1 derives them.
- risks — a dossier may not reach 18,432 bytes by moving history alone. The disposition is an M2
  amendment of this spec naming that dossier and its residue, never a cut of a constraint that is
  not history. Recall answers that quoted a dossier's measurement will cite the record instead.
- testing — AC1 to AC3 run directly; no suite arm, since nothing executable changes.
- migration — N/A: no stored shape changes.
- user docs — S1's rule in both README copies.

## 6. Acceptance criteria

- **AC1** — When a `python -c` reader reads `DOSSIER_CAP_BYTES` from `.memory-tree.conf` and the size
  in bytes of every file `git ls-files memory/map/features` lists, at the unit's tip, every file is at
  most 90% of the cap.
  Red when: any of the seven still sits within 10% of the cap.
  figure: DERIVED at observation time from the conf and the tree; the §4 table is PINNED at writing.
- **AC2** — When a `python -c` scanner splits each of the seven dossiers into blank-line-separated
  paragraphs and selects every paragraph matching `[Mm]easured|MEASURED`, each selected paragraph
  carries at least one record id of the shape the families in `.memory-tree.conf` define, and
  `git grep -l` finds each such id under `memory/builds` or in `memory/DECISIONS.md`.
  Red when: a measurement paragraph cites no record, or cites an id the tree does not define, which
  would mint an orphan.
- **AC3** — When `python tools/codebase-map/gen_map.py --check` runs at the tip, it exits 0, and
  `git grep -n "Measured history lives in the record" -- memory/map/README.md tools/codebase-map/gen_map.py`
  hits once in each file.
  Red when: a fence edit rode along and staled a generated artifact, or one README copy lacks the
  rule.

## 7. Gates

`codebase-map kit selftest` · `codebase-map gate coverage` · `codebase-map adopter e2e` · `codebase-map coverage + freshness` · `recall floor` · `recall floor arms` · `kit epoch (shipped bytes move, the version moves)` · `spec tokens (a spec's own names resolve)`

## 8. Open questions

- **F1** — Where does measured history live once it leaves a dossier?
  Options: the build record that measured it, cited by id; a per-feature history file beside the
  dossier; a closing section of the dossier itself. The second is a new file kind and a second copy;
  the third saves no bytes.
  RESOLVED (agent, 2026-10-04, delegated): the record that measured it, cited by id, per S1. It is
  the only option that removes a copy rather than moving one, and it is the charter's own rule that
  memory never re-narrates what a decision log already records.
- **F2** — How far must each dossier shrink?
  RESOLVED (agent, 2026-10-04, delegated): to at most 90% of the cap, which is outside the band the
  review flagged and leaves each dossier about 2 KB for its next true constraint.

## 9. Revision log

- rev-1 · 2026-10-04 · initial draft, split from unit 43's F1; sizes and measurement lines
  re-measured at `8312d315`.

## 10. Reuse audit

No existing seam fits: the change is prose in seven dossiers plus one rule bullet, and the only
code it touches is the `_README` string in `tools/codebase-map/gen_map.py`, which already carries the
map's Rules list and is extended rather than duplicated. `python tools/codebase-map/reuse_lookup.py
"move measured history out of a dossier near its byte cap into the record that measured it"` returned
name-stem neighbours only, such as `records` in `tools/memory-tree/gotchas.py`, `load_dossier_texts`
and `parse_dossier` in the map kit, and the runlog record writers; none relocates prose, and the scan
named `.sh` as unscanned, where no dossier is written. Recall returned `TOOL-dFoldedVerdict-7`, a
capped document paying for an addition by compressing prose, which is the pressure this unit relieves
before it bites, `TOOL-aRelaxedShard-1`, which declared the dossier cap, and unit 43's own spec. Where
the report and the tree disagree: they do not; the seven dossiers within 10% of the cap re-measured as
the same seven at `8312d315`.

Recall terms used: `python tools/memory-recall/query.py "where should measured history live when a
codebase-map dossier nears its byte cap" --terms "dossier byte cap DOSSIER_CAP_BYTES prose measured
history Constraints decision record pointer codebase-map rots"`
