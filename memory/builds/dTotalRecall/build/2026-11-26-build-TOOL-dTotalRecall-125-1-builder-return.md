**Serves:** journal TOOL-dTotalRecall-125
**Caused-by:** TOOL-dTotalRecall-125

# TOOL-dTotalRecall-125 build pass 1 — the builder's return

The gov-builder return for the pass dispatched at `bed60eaea` from [2026-11-26-prompt-TOOL-dTotalRecall-125-build-brief](../prompts/2026-11-26-prompt-TOOL-dTotalRecall-125-build-brief.md), recorded whole, each number's line tagged by the recorder; the pass tip is `075330bdc`.

## Why

Every scope item S1 to S12 of spec rev-1 is built as written in one pass commit with `Pass: TOOL-dTotalRecall-125`. One thing the task asked for is missing: the spec header still reads INPROGRESS. scratch-guard refused my status-only edit to memory/builds/dTotalRecall/spec/2026-10-26-spec-TOOL-dTotalRecall-125.md because the session's orientation card still routes TOOL-dTotalRecall-124. The guard says it allows that same status-only edit from the main loop. Until the main loop flips the header to CLOSED, `--plan` will keep naming this unit. I did not try to get around the refusal.

## Summary

Built TOOL-dTotalRecall-125 at 075330bdc on base bed60eaea: 33 files, 559 insertions and 111 deletions (DERIVED 2026-11-26).

**Owed by the main loop first:** flip the spec's **Status:** cell from INPROGRESS to CLOSED in memory/builds/dTotalRecall/spec/2026-10-26-spec-TOOL-dTotalRecall-125.md. scratch-guard refused it to this builder because the card routes unit 124. A later status-only flip does not upset the pass-order leg, which only needs a conforming spec at the build commit's first parent.

**What changed, by scope item:**
- S1, tools/workflows/replay_scorer.py: added GIT_GLOBAL_READS, RUN_OPTIONS, GIT_GREP_PAGER and check_git_option. derive_segment_program now also returns a third value, `lead` (the env assignments and git options ahead of the subcommand). check_read_call refuses a call on any of these, and its docstring lists what it does not read. The map-transcript arm gains 16 acting calls and 7 reads. (DERIVED 2026-11-26, the pass)
- S7 and S10, same file: build_map_manifest takes `cases`. map-noise gains two refusal cases and map-verdict pins 15.46.
- S2: check_message_decisions now matches each `Decided` line one to one against git's parse, using DECIDED_LINE. The fixture gains two cases. The block is byte-identical in tools/lib, tools/memory-tree and tools/unattended (the three hash equal). In tools/unattended/unattended.test.sh the loop gains one continuation line, FLOOR_ASSERTIONS goes 4237 to 4239 and FLOOR_SHARD_4 445 to 447, each with a raise line. (DERIVED 2026-11-26, the pass)
- S3: map_lib.py#measure_dossier_staleness keeps commit ancestry for every claimed path no anchor names. The selftest's anchored fixture now also claims b.py. The codebase-map README, map_diff.py's docstring and the map_lib docstring state the rule.
- S4: test_anchor_resolves_at_head added to tools/codebase-map/test_codebase_map.py and its template, which stay byte-identical.
- S5: the playbook render selftest guard in tools/playbook/kit.toml now takes the code record leg's directories; tools/gate-legs.json re-rendered.
- S8: test_unheld_anchor_exits_one added and registered in the selftest's main.
- S9: two sentences added to the drift-audit README row.
- S11: a dated section with the variance table and the noise sentences appended to the 123 verdict record; nothing standing was rewritten. (DERIVED 2026-11-26, the pass)
- S12: the shell-role row widened to 17615, which matches the measure (widen record 42). (DERIVED 2026-11-26, the pass)
- The read-allowlist gotcha class is updated. Two new classes, refinement-replaces-the-rule-it-refines and record-omits-a-figure-its-spec-names, are written, claimed in their dossiers and indexed. Each names its relation with `coexists-with`.
- Regenerated: memory/map/generated, memory/gotchas/INDEX.md, memory/LIVE.md, the build README and the spec's records region. The acceptance ledger is written.
- Added outside the spec's file list: memory/guides/SESSION-KICKOFF.md, declared through `--dispatch` and re-stamped at bed60eaea, because tools/gate-legs.json is on its watch list.

**Checks this pass ran.** All are probes over scratch copies, or a break staged in the worktree and restored byte-equal. They stand in for the legs named in brackets.
- AC1 [review-replay selftest]: all 16 acting calls answer False and the 7 reads True; the base admits all 16. map-transcript returns None and fails with each of its three refusals cut, and with `-C` removed. The `--experiment` re-run is byte-equal to the run before the change. (DERIVED 2026-11-26, the pass)
- AC3 [unattended kit gate]: `--fixture` exits 0 in all three carriers. Restoring today's count compare fails the spaced-key case; cutting the prefix clause fails the folded case. (DERIVED 2026-11-26, the pass)
- AC5 and AC11 [codebase-map kit selftest]: both functions return. Restoring today's stale line fails at b.py; deleting `return 1` gives exit 0, so the test fails. (DERIVED 2026-11-26, the pass)
- AC7 [codebase-map coverage + freshness]: returns in about 1.2 s (DERIVED 2026-11-26, node a). Renaming one lexicon.md key to `gone` fails naming that key. The pre-commit freshness leg printed `ok test_anchor_resolves_at_head`.
- AC8 [gate-leg conformance]: every code record guard entry is in the playbook guard.
- AC10 and AC13 [review-replay selftest]: map-noise fails with the condition cut to `len(sent) > 1`; map-verdict fails with NOISE_FACTOR set to 1.
- AC14: the probe's `statistics.variance` figures equal the table's eight figures; numstat shows 0 deleted lines. (DERIVED 2026-11-26, the pass)
- AC2, AC4, AC6, AC12, AC15 [memory hygiene, gotchas selftest]: the greps hit. `gotchas.py --check` has no finding (advisory count stays 55). After the commit, `--check-relations 33706662` reads `2 near match(es), 2 satisfied` with no `check 27:` line. (DERIVED 2026-11-26, the pass)
- AC16 [ratchet (both ways), portability]: the measure reads 17615. `lexicon.py --measure` leaves VERB_OFFENDER_PIN at 1443 (DERIVED 2026-11-26).

**Owed to the close:** AC9 (S6: the playbook render selftest leg run under the bar, the ceiling-evidence row and the budget row), the observed count for AC16, every section 7 leg, and the RED-first observations of the four `New arm:` lines (replay_scorer, unattended.test.sh, the codebase-map selftest and the freshness gate). Under budget-row-not-remeasured-after-added-arms, the budget rows of the codebase-map selftest, review-replay and unattended suites are owed too, since each gained arms. (DERIVED 2026-11-26, the pass)

**Bug-class checklist:** `gotchas.py --for-diff HEAD~1..HEAD` exited 0 and selected 69 classes (DERIVED 2026-11-26). Acting on it, I renamed a noun-named nested helper to `render_dossier`. Two things are left as they are:
- The new fixture's git calls inherit the environment exactly as the existing anchored test does (fixture-inherits-ambient-machine-state).
- No arm reds S4's shallow-history assert (refusal-branch-with-no-arm).

**Spec note, not a divergence:** after the b.py commit the dossier is already stale, so the later `f's body moved` assertion can no longer fail on its own. The spec's "the steps after it keep their meaning" is weaker than it reads there.

**Commit trailer:** the commit ends with `Co-Authored-By: Claude Opus 5 <noreply@anthropic.com>`, the charter's spelling, not the session reminder's "Opus 5.5".

Scratch probes are under C:/Temp/claude/7a8436c9e3b87ce5/9067262b-db21-4497-8ba8-ef2deab46f53/scratchpad (probe_s1.py, red_s1.sh, red_s2.py, red_s3s8.py, probe_s4.py, variances.py). No command was skipped for its bound.
