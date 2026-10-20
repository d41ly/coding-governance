# Fold return: writer 11 resumed, Stage 0 again finished

**Serves:** research PLAY-dClosedLoop-1

Dispatch 213's return, verbatim, any H1 demoted to bold. Its handoff is `prompts/prompts/2026-10-20-prompt-PLAY-dClosedLoop-1-50-spec-writer.md`, and its use is in
`build/2026-10-19-build-PLAY-dClosedLoop-1-whole-audit.md`.

---

I finished the pass. Stage 0 on the dry copy now reports findings 0, with 50 classed. The only reds are the two reruns that read git (line coverage and review debt), because the dry folder is not a repository. The dry run ends `ALL rc 0`.

### 1. Dispositions
Every finding from the first pass is accounted for. Rows marked "earlier" were in the first return and are unchanged; the rest are new or changed in this pass.

| arm | nodes | disposition | the fold's gist or the class and its reason |
|---|---|---|---|
| K2 | `entry.place`, `plan.exit`, `design.overlaps`, `life.quiesce`, `adopt.decisions` | fold (earlier) | Each Then cell now ends in a form Stage 0 reads (re-entry, an edge to Design, `warn`'s two targets, held until, a re-run). The meaning is unchanged. |
| K2 | `loop.file`, `release.record`, `kits.cut`, `kits.offer` (two forms, and "ends nowhere"), `kits.install`, `kits.update` | fold (earlier) | The Routes cells end recorded, done, re-run or nothing, so `kits.offer` now ends. |
| K2 | `adopt.instructions`, `adopt.declarations` | fold (new) | These were hidden by writer 10's class rows. "ruled → recorded as the unit, the amendment or the drop" and "ruled → recorded as the overlay row". |
| K2 | the six unreached `kits.*` | none needed | Stage 0 now reads the Needs column and counts them as entries. I dropped my six `external entry` rows. |
| K3 | writers of ask, baseline, decision, dossier, fork, gotcha, maintenance-record, shape-run, transition | fold (earlier) | Each kind's row names the item the records already give as its writer. |
| K3 | readers of ask, baseline, decision, dossier, gotcha, shape-run, adopters, exception, kit-release, research-return, value-ledger | fold (earlier) | Each reader item's cell names the kind, or the reader waits on the new writer. |
| K3 | archive reader | fold and program reader | cl-0220 now says `record find` reads rotated records under `memory/archive/` (FK-11-1). It is the same build as the kind's owner, so it also needs a class row. |
| K3 | override reader | fold | cl-0462 (dCalibratedLens): the Loop Review proposes a charter amendment for a rule whose override records recur (FK-11-1). |
| K3 | playbook-set reader | fold | `test.verdict`'s Does: the set check, a leg at Test's leg-pack point, reads the playbook set record (FK-11-1). |
| K3 | release reader | fold | `release.route` reads E's last verified SHA from E's release records (FK-11-1). |
| K3 | ruling reader | fold | cl-0429: the integrations import reads each CI job's ruling record. `test.seed` seeds the other practices that a ruling record imports or translates (FK-11-1). |
| K3 | run-record reader | fold | `loop.gather` reads each run from its run records (FK-11-1). |
| K3 | instrument writer and reader | fold and class | Its row now names the record's session as writer (FK-11-2) and on-demand re-runs by its owner and reviewers as reader (FK-11-1). Classed external writer and external reader. |
| K3 | adopter-register writer | fold and class | Its row names govkit's registration as writer and "gov's adopters program" as reader, with no item tag (FK-11-2). `kits.adopters` reads `adopter-register` rows. Classed program writer. |
| K3 | writer findings of act, annotation-index, archive, backlog-row, build-readme, code, commit, design-record, deviation, lease, mailbox-message, node-ledger, playbook, playbook-set, recall-index, registry, return, run-record, session-binding, view, work-order | class: program writer | Each row names its program (memory-plan `[doors]`, layer-memory `[design]`, the clause cited). |
| K3 | writer findings of exception, instrument, lexicon-declaration, node-profile, override, witness | class: external writer | Written by the owner, the session, or the witness's own owner. |
| K3 | journal writer | class: hook writer | SubagentStart's journal entry (layer-runtime `[enforce]`). |
| K3 | reader findings of act, annotation-index, archive, backlog-row, build-readme, commit, flake, lexicon-declaration, loop-review, mailbox-message, node-ledger, node-profile, recall-index, registry, return, session-binding, view, witness, work-order | class: program reader | One row per kind, each naming the program the records state. |
| K3 | instrument reader | class: external reader | Its owner and reviewers re-run it (FK-11-1). |
| K3 | maintenance-record and adopter-register readers | none needed | Stage 0 now recognises "maintenance record" written in words, and the Needs fix closed adopter-register. I dropped both reader rows. |
| K4 | `roles.shape-enforce` | fold (earlier) | cl-0297 refuses or records a call whose shape differs, as the key says. |

### 2. Fold script and classes file
- **Fold script:** `C:/Users/d41ly/AppData/Local/Temp/claude/C--projects-coding-governance--claude-worktrees-gov-architecture-plan-e34297/1799cb98-0882-4ab8-a308-19495d2a487a/scratchpad/fold/w11/fold-11.py`, updated in place.
  - **v2:** 5 edits. cl-0297, cl-0220, cl-0462, cl-0429, and the revision note before "Revised: 2026-10-17, after the folds' closing review".
  - **flow-steps:** 14 edits.
    - Then cells: 5 earlier, plus the two `adopt.*` cells.
    - Reader cells: `plan.dedupe`, `plan.record`, `deploy.close`, `build.scope`, `test.seed`, `test.verdict`.
    - The revision note.
  - **layer-memory:** 12 edits. 9 writer rows, the instrument and adopter register rows, and the revision note.
  - **layer-expansions:** 14 edits.
    - Routes edits: 7.
    - Does edits: `kits.currency`, `kits.offer`, `loop.propose`, `release.route`, `loop.gather`, `kits.adopters`.
    - The revision note.
  - No clause is new, so there are no placeholder ids. Mint ran with 0 minted, and the next free id stays `cl-dClosedLoop-0510`.
- **Classes file:** `C:/Users/d41ly/AppData/Local/Temp/claude/C--projects-coding-governance--claude-worktrees-gov-architecture-plan-e34297/1799cb98-0882-4ab8-a308-19495d2a487a/scratchpad/fold/w11/classes.md`, 49 rows, all K3:
  - program writer: 21
  - external writer: 6
  - hook writer: 1
  - program reader: 20
  - external reader: 1
  - `stage0_unclass` removed writer 10's four idle rows, and `stage0_classes` added all 49 of mine.
  - Stage 0 reports no row that answers no finding.

### 3. Forks
None. The owner answered FK-11-1 and FK-11-2, and both are folded as answered.

### 4. The dry run and Stage 0
- **Dry run:** the last line is `ALL rc 0`, and every check ran rc 0.
- **Stage 0 per arm:**
  - K1 0
  - K2 0, classed 1 (writer 10's `mailbox.answer` row)
  - K3 0, classed 49
  - K4 0
  - K5 0
- **Total:** findings 0, classed 50, reruns red 2 (line coverage and review debt, which read git).
- **Output files:** `.../scratchpad/fold/w11/dry-run.out` and `.../scratchpad/fold/w11/stage0-dry.out`.

### 5. Read outside the list above
- **Main-loop files, read only:** `<scratch>/fold/unclass.txt` and the `COVERS` block in the updated `stage0.py`, which I re-ran without editing.
- **Design records for this pass:** v2's cl-0220, cl-0429 and cl-0462, and the `test.verdict`, `test.seed`, `release.route`, `loop.gather` and `kits.adopters` cells, to anchor the reader folds.

I edited nothing outside the scratchpad.
