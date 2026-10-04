# TOOL-aMendedFleet-63 — `--close` and `--abort` render the run record themselves, after their own END line

**Status:** SPECCED · rev-2 · 2026-10-04 · node a · Tier-1 · base 7af5f564 · streams tooling · ratified 2026-10-04 · order 63

<!-- gen:spec-records -->

*No record names this unit.*

<!-- /gen:spec-records -->

## 1. Goal

The committed run record is how one node reads another node's run, and since 2026-09-14 the
unattended Skill has told every run to render it at `--abort` and at `--close`. Runs skip it: of the
17 tracked run-state files whose phase reads LANDING, LANDED or ABORTED and that moved after
2026-09-13, 4 build folders carry a record. This unit makes the two terminal verbs render the record
themselves, once their own call is journaled, and stage it with the index re-render it owes. An
instruction a run can skip becomes an act the verb performs.

## 2. Scope (IN)

- **S1** — `write_run_record` in `tools/unattended/unattended.sh` takes the slug. It is called from
  the block after the verb dispatch, once, only when the verb was `--close` or `--abort`, the call's
  `status` is 0, and the recorded phase now reads LANDING or ABORTED. Observed by AC1 and AC5.
- **S2** — THE END LINE FIRST. When the run-log trap is installed, `write_run_record` sets
  `RUNLOG_CLEAN=1`, calls `write_runlog_end 0` and clears the EXIT trap before anything else, so the
  journal holds this call's START and END before the record reads it, and the exit writes no second
  END. With journaling switched off it writes nothing and goes on. Observed by AC2.
- **S3** — THE RENDERER is found with `resolve_kit_dir` by home `runlog` and anchor `runlog.py`,
  run through `resolve_python` and `run_bounded` as `runlog.py record <slug> --write`, and its stdout
  is printed indented. A kit that does not resolve prints one `not asked` line naming the runlog
  kit, which is the Skill's own "no record is owed" case. The renderer's own no-record line passes
  through as the answer it is. Observed by AC1 and AC3.
- **S4** — THE INDEX. On a `record written` answer, `write_run_record` stages the record FIRST,
  because the generator lists its inputs with `git ls-files` and an untracked record is invisible to
  the render. It then lists `scan_dirty_paths`, runs the generator `resolve_index_generator` names
  with `--write` through `run_bounded`, lists again, and stages every path the second listing holds
  and the first did not. Paths that were dirty before it ran are never staged by it, and it renders
  nothing while a path under the memory root or `.memory-tree.conf` carries unstaged or untracked
  changes: one line names those inputs and the repair. Both rules are the ones `write_ask_views`
  carries, as `TOOL-aMendedFleet-1` restores it. Observed by AC1.
- **S5** — THE COMMIT, only where the close already commits. Under `LANDER_MODE` set to `in-place`,
  after `--close`, it commits the staged record and index as `records(<slug>): the run record`
  through the same `run_bounded git commit` shape `write_close_commit` uses. Under `primary`, and
  after `--abort` in either mode, it stages and prints the commit the operator owes. Observed by
  AC4.
- **S6** — NOTHING HERE CHANGES AN EXIT. A refused render, a failed generator or a failed commit
  prints one line naming it and leaves the verb's exit code as the verb set it. Observed by AC3.
- **S7** — THE CARRIERS. The protocol's sentence saying the record is rendered by the Skill and
  never by a verb, in `tools/unattended/PROTOCOL.template.md` and its copy
  `memory/guides/UNATTENDED-PROTOCOL.md`, now says the two verbs render it after their END line and
  the Skill re-renders it after `--landed`, in no more bytes. The Skill's "Record the run" section
  in `tools/unattended/SKILL.template.md` keeps the `--landed` placement and says the other two are
  the verbs' own; its `--abort` section's render step says the same. Both renders are re-made with
  `bash tools/unattended/adopt-unattended.sh`. Observed by AC5 and AC6.
- **S8** — An arm in `tools/unattended/unattended.test.sh` aborts a fixture run that dispatched one
  unit, with the runlog kit present and then absent. NOT OBSERVED by a criterion here: the suite
  runs once at the close, and the arm is declared under `New arm:` in §7.

## 3. Non-goals (OUT)

- Rendering after `--landed`. The brief names `--close` and `--abort`; the Skill's third placement
  stays as it is.
- A Definition-of-Done item for the record. `TOOL-dLoggedFlight-11` rejected it as circular inside
  `--close`, and S6 keeps the render out of every verdict.
- Changing the runlog kit or its record schema.
- Bumping the unattended kit version, owed once at the close.

### Edges

- **consumes-from** `TOOL-aMendedFleet-1` — the render-and-stage rules of `write_ask_views`, which
  S4 follows; the helper itself is not called, because its argument and its lines speak of filed
  asks and that unit restores its bytes unchanged.

## 4. Design

### Evidence

Read at the worktree HEAD `725b1449`, whose bytes under `tools/` equal base `7af5f564`'s.

- `git ls-files` for run records under every build's `build/` folder names four builds:
  `aBatchedMinors`, `aRepatriatedFork`, `aSightedSkeptic` and `dLoggedFlight`. The 17 terminal
  run-state files are those whose `phase:` reads LANDING, LANDED or ABORTED and whose last commit is
  dated after 2026-09-13. PINNED, node a, 2026-10-04; the report's own figure was 6 of 9 runs
  without one.
- `TOOL-dLoggedFlight-11` put rendering in the Skill and wrote, as a non-goal, that a verb may not
  read a log it would then be judged by. The concrete form of that is in the runlog model: a verb
  START with no END becomes a `killed-verb` anomaly, so a record rendered inside `--close` would
  report the close it was rendered by as killed. S2 removes that cause rather than the render: the
  END line is written first.
- `measure_commitment` in `tools/runlog/record.py` hashes the first N attributed journal lines, so
  lines the run appends after the render change nothing a later `runlog.py verify` reads.
- `write_runlog_end` is called by the EXIT trap alone today, and the dispatch block ends
  `RUNLOG_CLEAN=1; exit "$status"`, so the post-dispatch call site sees the verb's status.
- Under `in-place`, `verb_close` commits `records(<slug>): close — LANDING` itself through
  `write_close_commit`, and the lander's `--land` accepts commits after the prepared merge as long
  as that merge stays on HEAD's first-parent line. A records commit after the close commit is
  therefore pushable, and the Skill already asks an in-place run for one.
- `runlog.py record --write` prints `runlog: record written <path>` and two follow-ups, the index
  re-render and the commit; with no spec-defined unit it prints one no-record line and exits 0.
- `resolve_index_generator` in the library already names the memory-tree generator this install
  holds, and `resolve_kit_dir` resolves a sibling kit by receipt or probe, so no sibling path is
  spelled.
- `memory/guides/UNATTENDED-PROTOCOL.md` measures 65274 of 65692 bytes, 418 under its ceiling.
  PINNED, node a, 2026-10-04.

### Inventory

- `write_run_record` — cell `sh.function`; `python tools/lexicon/lexicon.py --suggest
  write_run_record --as sh.function` answered OK.

### Files touched (estimate)

- `tools/unattended/unattended.sh`
- `tools/unattended/PROTOCOL.template.md`
- `memory/guides/UNATTENDED-PROTOCOL.md`
- `tools/unattended/SKILL.template.md`
- `.claude/skills/unattended/SKILL.md`
- `tools/unattended/README.md`
- `tools/unattended/unattended.test.sh`

### Alternatives rejected

- **Render inside `verb_close` before `write_close_commit`.** The journal would hold the close's
  START and no END, and the record would carry a `killed-verb` anomaly for the very call that wrote
  it.
- **Write the END line early and commit after it inside the verb.** A commit failing after an END
  that said clean leaves the journal claiming a call that refused; S5's commit comes after the verb
  returned, so its failure is a printed line and not a false verdict.
- **A new conf key naming the renderer.** It needs a protocol key row, and the resolver already
  finds the kit.

## 5. Production-readiness checklist

- security — fixed argv through `run_bounded`; the slug was validated by the verb; staging is
  limited to paths the generator newly dirtied.
- perf / scale — one record render and one index render per terminal verb, seconds each per
  `TOOL-dLoggedFlight-11`'s estimate, UNVERIFIED on this tree until AC1 measures it.
- error / empty / loading states — S3's not-asked line, the renderer's no-record line, and S6's
  one-line failures.
- observability — the renderer's own lines, indented, and one staged-or-committed line.
- risks — a generator that dirties a path for another reason would have that path staged too; the
  before-and-after listing limits it to paths that were clean when the verb returned.
- testing — AC1 to AC6; the arm in S8.
- migration — N/A: nothing stored changes shape.
- user docs — S7, and one line in `tools/unattended/README.md` where it describes the two verbs.

## 6. Acceptance criteria

- **AC1** — When a scratch script built from the unattended suite's prologue and a fixture run that
  dispatched one unit runs `bash tools/unattended/unattended.sh --abort` with a reason and a halt
  code, stdout carries an indented `runlog: record written` line, `git diff --cached
  --name-only` in the fixture lists that record and the run-state file, and
  `python tools/memory-tree/gen_build_index.py --check` passes there.
  Red when: the post-dispatch call is staged out, so the verb aborts and no record exists, or the
  record is staged after the render, so the index the commit carries omits it.
  cost: under a minute for the slice; the suite whole is never run.
  fixture: the suite prologue's fixture builder under a short `%TEMP%` root; that the builder
  reaches a dispatched unit cheaply is UNVERIFIED and the builder decides it.
- **AC2** — When `grep -c "killed-verb"` runs over the record AC1 wrote, it prints 0, and the last
  two driver-journal lines for the fixture's slug are the `--abort` START and its END.
  Red when: S2's END call is staged after the render, so the record names the abort as killed.
- **AC3** — When the AC1 fixture's runlog kit directory is renamed away before the abort, stdout
  carries one `not asked` line naming the runlog kit and the verb exits 0, as it does with the kit.
  Red when: a missing kit is silent, or it moves the exit.
- **AC4** — When `grep -n "write_run_record" tools/unattended/unattended.sh` runs, it prints the
  definition and exactly one call, inside the post-dispatch block and guarded by the two verb names;
  and `grep -n "): the run record" tools/unattended/unattended.sh`, which hits nothing at base, hits
  the in-place commit subject.
  Red when: a second caller exists, or the in-place close leaves its record uncommitted.
- **AC5** — When `grep -c "never by a verb" memory/guides/UNATTENDED-PROTOCOL.md` runs it prints 0,
  `cmp tools/unattended/PROTOCOL.template.md memory/guides/UNATTENDED-PROTOCOL.md` exits 0, and
  `wc -c memory/guides/UNATTENDED-PROTOCOL.md` at the unit commit is not larger than at its parent.
  Red when: the protocol still says no verb renders the record, or the sentence grew it.
  figure: both byte counts are DERIVED at observation time.
- **AC6** — When `bash tools/unattended/adopt-unattended.sh --check` runs, it prints its in-sync
  line; and `grep -n "Render the run record before you commit the ABORTED record"
  .claude/skills/unattended/SKILL.md` prints nothing.
  Red when: the Skill still tells a run to render what the verb now renders, or its render is stale.

## 7. Gates

`unattended kit gate` · `unattended skill wiring` · `unattended protocol size` · `kit/dogfood doc parity` · `check-wiring self-test` · `recall floor` · `recall floor arms` · `lexicon naming predicates` · `install-prefix (shipped surface)` · `line length` · `kit epoch (shipped bytes move, the version moves)` · `spec tokens (a spec's own names resolve)`

New arm: `tools/unattended/unattended.test.sh` · a fixture run that dispatched one unit is aborted with the runlog kit present, then absent; staged red by deleting the post-dispatch call · none

## 8. Open questions

- **F1** — Where in the verb's life does the render run?
  Options: inside the verb before it returns; after the dispatch, with the END line written first;
  in the EXIT trap after the END. Inside the verb the record names its own call as killed. The trap
  runs on every exit, refusals included, and staging from a trap is a write nobody's control flow
  shows. After the dispatch, the status and the phase are both known and the END can be written
  deliberately.
  RESOLVED (agent, 2026-10-04, delegated): after the dispatch, END first, per S1 and S2.
- **F2** — Does the verb commit what it renders?
  Options: always; never; only where the verb already commits. Under `primary` the operator makes
  the close's records commit and the merge follows it, so a verb commit there adds one the protocol
  does not have. Under `in-place` the close commits its own record and the run otherwise owes a
  second commit the Skill asks for by hand.
  RESOLVED (agent, 2026-10-04, delegated): only after an in-place `--close`, per S5.
- **F3** — The protocol states the record is rendered by the Skill and never by a verb. Is editing
  that sentence inside this build's authority?
  Options: edit it; leave a protocol that contradicts its driver. The mandate's third answer opens
  the governance carriers to stale-fact fixes, and the sentence is stale the moment S1 lands.
  RESOLVED (agent, 2026-10-04, delegated): edit it in no more bytes, per S7.

## 9. Revision log

- rev-1 · 2026-10-04 · initial draft, from the spec brief's unit 63, report item [B#15], the runlog
  model's anomaly rules, the record's journal commitment, and a read of the dispatch block,
  `verb_close`, `verb_abort` and the Skill's record section at base.
- rev-2 · 2026-10-04 · S4 AC1 §3 · cross-read with `TOOL-aMendedFleet-1`, which restores the
  driver's other render-and-stage step: S4 rendered before staging the new record, which the
  tracked-only generator cannot see, and rendered over a dirty input, the defect that helper's
  rev-3 closed. S4 now stages first and refuses a dirty input as the helper does; AC1 reads the
  index fresh.

## 10. Reuse audit

The seams are `runlog.py record --write`, called as the Skill calls it; `resolve_kit_dir` and
`resolve_index_generator` in `tools/unattended/lib-unattended.sh`, which find a sibling kit and the
generator without spelling either path; `scan_dirty_paths` for the before-and-after listing; and
`write_close_commit`'s bounded commit shape for S5. `python tools/codebase-map/reuse_lookup.py
"render the committed run record when a run closes or aborts"` returned the runlog kit's
`build_run_model` and the map kit's render functions, none of which the driver calls, and printed
`unscanned layers: .sh`, so `git grep` over `tools/unattended/` was the shell probe; it found no
existing call of the renderer. Recall returned `TOOL-dLoggedFlight-11`, whose non-goal S2 answers,
`TOOL-dLoggedFlight-25` on the model reading the working-tree phase, and the protocol's own
sentence. Where the report and the tree disagree: the report's 6 of 9 was re-measured as 4 of 17
build folders over a wider window.

Recall terms used: `python tools/memory-recall/query.py "why is the committed run record rendered by
the Skill and never by a driver verb" --terms "runlog record render Skill never by a verb close
abort placement dLoggedFlight run record committed build folder"`
