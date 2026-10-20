# Fold return: writer 11, Stage 0 again

**Serves:** research PLAY-dClosedLoop-1

Dispatch 212's return, verbatim, any H1 demoted to bold. Its handoff is `prompts/prompts/2026-10-20-prompt-PLAY-dClosedLoop-1-50-spec-writer.md`, and its use is in
`build/2026-10-19-build-PLAY-dClosedLoop-1-whole-audit.md`.

---

I've written the fold script and the classes file. The dry run ends `ALL rc 0`, and Stage 0 on the dry copy goes from 98 findings to 12. All 12 are K3 leads that wait on the two forks below. The four editable design records are the only ones my script changes. The round record changes only through your `stage0_classes` step.

### 1. Dispositions

| arm | nodes | disposition | the fold's gist or the class and its reason |
|---|---|---|---|
| K2 | `entry.place` | fold | The late answer becomes "→ re-entry of the item it answers, as an amendment", which is a return form. |
| K2 | `plan.exit` | fold | "Design, once the card is re-rendered…": the re-render is part of the route to Design, not a second branch. |
| K2 | `design.overlaps` | fold | The "none" case under `refuse` now names `warn`'s two targets: "→ `design.streams` or `design.unit-spec`, as under `warn`". |
| K2 | `life.quiesce` | fold | "paused, held until the owner's next lifecycle request" (a wait form). |
| K2 | `adopt.decisions` | fold | Agreement below kappa 0.8 → "a re-run, the rubric revised…" (a return form). |
| K2 | `loop.file` | fold | The keep sentence becomes a branch: "a kept row's disposition → recorded as a keep record…". |
| K2 | `release.record` | fold | "→ recorded as the release slot's exit record…". |
| K2 | `kits.cut` | fold | "declined → recorded, the disposition its witness…". |
| K2 | `kits.offer` (both form findings, and "ends nowhere") | fold | "pushed → done, the adopter landing it…" and "→ an outbox order recorded for the adopter to run itself". With both targets in a form, `kits.offer` now ends. |
| K2 | `kits.install`, `kits.update` (both form findings each; they share one row) | fold | "then the walk re-run" and "→ nothing installed for it, its slot rendering not installed…". |
| K2 | `kits.cut`, `kits.currency`, `kits.adopters` (unreached) | class: external entry | Each is a cadence program on `kits.host`, and its Needs cell is a dash (layer-expansions `[design-distribution]`). |
| K2 | `kits.install`, `kits.update` (unreached) | class: external entry | Their Needs cell is a dash. The owner's operator order, an outbox order or the prepared merge starts them (cl-0025). |
| K2 | `kits.offer` (unreached) | class: external entry | Its Needs cell is `kits.adopters`, a cadence program. This follows the earlier `kits.install-attended` rows. |
| K3 | writers of ask, baseline, decision, dossier, fork, gotcha, maintenance-record, shape-run, transition | fold | Each kind's row now names the item the records already give as its writer. |
| K3 | readers of ask, baseline, decision, dossier, gotcha, shape-run | fold | Ask: `plan.dedupe` reads "open ask records". Baseline: `build.scope` reads "retrofit's `baseline` ledger". The other four get a reader through their new writer: an item that waits on that writer (`build.core`, `build.acceptance`, `probe.judge`). |
| K3 | readers of adopters, exception, kit-release, research-return, value-ledger | fold | `kits.offer` names its `adopters` record. `deploy.close` needs "an exception record". `kits.currency` reads the `kit-release` tags. `plan.record` reads the `research-return` it asked for. `loop.propose` reads `value-ledger` rows. |
| K3 | act, annotation-index, backlog-row, build-readme, commit, design-record, mailbox-message, node-ledger, recall-index, registry, return, session-binding, view, work-order (writer and reader findings) | class: program writer | One row per kind. Each reason names the program that writes it (memory-plan `[doors]`, layer-memory `[design]`) and the reader the records state. |
| K3 | lexicon-declaration, node-profile, witness (writer and reader findings) | class: external writer | The owner, or the witness's own owner, writes it. The reason also names its reader (cl-0271, cl-0338, cl-0312). |
| K3 | code, deviation, journal, lease, playbook (writer finding only) | class: program writer, except journal, which is hook writer | cl-0219; cl-0004 with the commit queue; the SubagentStart hook (layer-runtime `[enforce]`); the coordination verbs (cl-0505); a playbook is written through `record`. |
| K3 | exception (writer finding) | class: external writer | Written by the recording session `core.exceptions` admits, through a stand-in door (cl-0037, FK-1-1). |
| K3 | flake, loop-review, maintenance-record, adopter-register (reader finding) | class: program reader | Gate health (cl-0339); the next Loop Review (cl-0472); the `red-leg` leg (cl-0509); `kits.adopters`, gov's cadence program. Stage 0 reads `kits.adopters` as the register's writer only because the register's row names it. |
| K3 | archive, instrument, override, playbook-set, release, ruling, run-record (reader findings) | fork FK-11-1 | No record names a reader for these kinds. |
| K3 | archive, instrument, override, playbook-set, run-record (writer findings) | left with FK-11-1 or FK-11-2 | Classing the writer now would also silence the forked reader finding, because a class row covers every finding on its node. The writer classes to add once the reader is settled: archive by rotation, override by the session's agent (cl-0032), playbook-set by the set check (cl-0393), run-record by the journal reader (cl-0447). Instrument's writer is FK-11-2. |
| K4 | `roles.shape-enforce` | fold | cl-0297 now says a Workflow call whose shape differs is "refused or recorded as `roles.shape-enforce` says" (systems `[design-role-shapes]`). |

### 2. Fold script and classes file
- **Fold script:** `C:/Users/d41ly/AppData/Local/Temp/claude/C--projects-coding-governance--claude-worktrees-gov-architecture-plan-e34297/1799cb98-0882-4ab8-a308-19495d2a487a/scratchpad/fold/w11/fold-11.py`
  - **v2:** cl-0297, plus a revision note before "Revised: 2026-10-17, after the folds' closing review". 2 edits.
  - **flow-steps:** 5 K2 cells, 4 reader cells (`plan.dedupe`, `plan.record`, `deploy.close`, `build.scope`), and a revision note. 10 edits.
  - **layer-memory:** 9 kind-table rows and a revision note. 10 edits.
  - **layer-expansions:** 7 Routes edits, 3 Does edits (`kits.currency`, `kits.offer`, `loop.propose`) and a revision note. 11 edits.
  - No clause is new, so there are no placeholder ids. Mint ran with 0 minted, and the next free id stays `cl-dClosedLoop-0510`.
- **Classes file:** `C:/Users/d41ly/AppData/Local/Temp/claude/C--projects-coding-governance--claude-worktrees-gov-architecture-plan-e34297/1799cb98-0882-4ab8-a308-19495d2a487a/scratchpad/fold/w11/classes.md`, 33 rows:
  - **K2 external entry:** 6.
  - **K3 program writer:** 19.
  - **K3 external writer:** 4.
  - **K3 hook writer:** 1.
  - **K3 program reader:** 3. One of them, adopter-register, rests on Stage 0's misreading of its row.
  - `stage0_classes` accepted all 33, and Stage 0 printed no idle-row finding.

### 3. Forks

### FK-11-1 — Who reads each of the seven kinds no record names a reader for?
- **(a) Name a reader for each, as a clause in that reader's build (recommended):**
  - archive: `record find`, over rotated records beside live ones (cl-0220).
  - instrument: no reader is stated. I recommend its row declare it on-demand evidence that its owner and reviewers re-run, which is an external reader.
  - override: the Loop Review, proposing a charter amendment when an override recurs (foundations, step 1: "so a standing override becomes a charter amendment").
  - playbook-set: `test.verdict`, through the set check's leg (night pass, point 6).
  - release: `release.route`, reading E's last verified SHA from the release records.
  - ruling: the practice's migration. For an imported CI job that is the integrations import (cl-0429), and `test.seed` otherwise.
  - run-record: `loop.gather`, for cycle times and cost per run.
- **(b)** Treat a kind read only through `gov trace` and `gov why` as read. That needs a new K3 class in stage0's `CLASSES`, which is your edit.
- **(c)** Retire any kind that has no reader.
- **Rests on** these 12 open findings: the reader findings of all seven kinds, and the writer findings of archive, instrument, override, playbook-set and run-record.

### FK-11-2 — Who writes the adopter register and the instrument kind?
- **Adopter register:**
  - (a) govkit's registration of an adopter, whose grant probe `kits.offer` names. That is a program writer (recommended).
  - (b) The owner's hand edit of `adopters.toml`. That is an external writer.
  - Either way, the row should name its reader `kits.adopters` in words Stage 0 won't take for a writer.
- **Instrument:**
  - (a) The session that writes the record the instrument serves, through `record` once dTotalRecall lands it. That is an external writer (recommended).
  - (b) `record` itself.
- **Rests on** adopter-register's reader lead, which hides that the register names no writer, and instrument's writer finding.

**Four defects in Stage 0 itself.** Fixing them is your call, since `stage0.py` is the main loop's:
- **It ignores the expansions' Needs column.** stage0.py:150 sets `needs=""`, and line 10 says expansion items have no Needs column. layer-expansions' item tables do have one (lines 220, 257, 385 and 454). I ran a scratch copy of stage0 that reads that column, with no edit to the build's script:
  - all six unreached `kits.*` leads close;
  - the adopters, value-ledger and adopter-register leads close;
  - 9 class rows go idle and red: the earlier `kits.install-attended` and `kits.update-attended` rows, and seven of mine.
- **A class row covers every finding on its node.** It is keyed by arm and node only. So the earlier `adopt.instructions` and `adopt.declarations` rows hide two form findings that Stage 0 never prints: "the unit, the amendment or the drop written" and "the overlay row written". The same keying is why 17 of my K3 rows each cover a writer and a reader finding under one class name.
- **K3 can't recognise a kind whose name ends in "record" written out in words.** stage0.py:403's pattern becomes "maintenance records? records?" for maintenance-record and run-record, so only the backticked key is recognised.
- **Two reruns go red in the dry copy.** These are line coverage and review debt, which read git, and the dry folder is not a repository.

### 4. The dry run and Stage 0
- **Dry run:** the last line is `ALL rc 0`. Output is in `.../scratchpad/fold/w11/dry-run.out`.
- **Stage 0 on the dry copy:**
  - K1 0.
  - K2 0, classed 13.
  - K3 12, classed 44.
  - K4 0.
  - K5 0.
  - Total: findings 12, classed 57.
  - Reruns red: 2, the git-reading line coverage and review debt, which I left alone.
  - Output is in `.../scratchpad/fold/w11/stage0-dry.out`.

### 5. Read outside the list above
I read these to find evidence and to match the earlier folds' form:
- **dClosedLoop design records:** layer-memory, flow-steps, layer-expansions, v2's `[chain]`, memory-plan, layer-runtime, systems, retrofit, lexicon, night-pass, away-pass, flow, flow-interactions and foundations.
- **The fold machinery:** `fold_lib.py`, `stage0_classes.py`, `mint.py`, `all.py`, `dry_run.sh`, and writer 10's `fold-10.py` with its Stage 0 outputs.
- **My own scratch copy of stage0:** `.../scratchpad/fold/w11/sim/stage0_sim.py` reads the Needs column, and I used it only for the measurement above.

I edited nothing outside the scratchpad.
