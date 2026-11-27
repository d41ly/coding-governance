**Serves:** journal TOOL-dTotalRecall-121
**Caused-by:** TOOL-dTotalRecall-121

# TOOL-dTotalRecall-121 build pass 1 — the builder's return

The gov-builder return for the pass dispatched at `1ea35c769` from [2026-11-25-prompt-TOOL-dTotalRecall-121-build-brief](../prompts/2026-11-25-prompt-TOOL-dTotalRecall-121-build-brief.md), recorded whole, each number's line tagged by the recorder; the pass tip is `1ea35c769`.

## Why

DIVERGENCE: five points in spec TOOL-dTotalRecall-121 rev-2. The first two block the build; the other three are worth fixing in the same revision.

(1) §4 "The shape-run plants", row `malformed`, against AC7 (blocking). The row's edit is "a required field's line deleted". AC7 asks that, with each red branch of `check_shape_runs` cut, that branch's plant exits 0. Both cannot hold. Every required shape-run field but `Caused-by` is mandatory in the `review-shape` line, so a deleted one also reds the field compare. A deleted `Caused-by` also reds the cause branch. Observed with the malformed branch cut: the plant still exits 1 on `Round · record absent · line 1` (DERIVED 2026-11-25, probe). The other seven plants hold as written.
WHAT THE SPEC WOULD HAVE TO SAY: the row's edit is "a required field's line given twice", check "exit 1, the record and the field". Observed: it prints `Round is given twice, at lines 6 and 7` and exits 1, and with the branch cut it exits 0 (DERIVED 2026-11-25, probe).

(2) §2 S9, §4 "S9 — the floor" and AC9 (blocking). They have this pass set `FLOOR_ASSERTIONS` to the count of a whole suite run the main loop makes after the last suite edit, handed over in a brief. The last suite edit is this pass's own, the brief hands no count, and the same commit must close the spec, so no single pass can meet AC9.
WHAT THE SPEC WOULD HAVE TO SAY: the pass raises the floor by reading, as units 116 to 120 did (842 to 879 for the drafted arms, DERIVED 2026-11-25, counted by reading), and the pin to the observed count with its comment line is the main loop's at the close, AC9 owed there.

(3) §7, second `New arm:` line: "three claim arms ... red on today's compare". Two are. The arm "holder named and caller absent" is green today, because today's compare already refuses it. Its red needs another staged break: the rejected fix of finding 3, where an absent caller is admitted. (DERIVED 2026-11-25, the pass)

(4) §4 "The byte term". `FILE_REDIRECT` sees only a word that OPENS a redirect, so `echo x>f`, `cat a b>out` and PowerShell `ls *> f` each answer True from `check_read_call` (DERIVED 2026-11-25, probe). The same section says a read holds no file redirect but one to the null device, and its "Not read" list does not name this form. The spec should either add "a redirect glued behind its word" to that list (the draft's docstring says it) or widen the pattern.

(5) §2 S12. `ratchet.py widen` cannot take the measured count: `ratchet.py` raises a held key by exactly one per call. The suite needs 3752 to 3801 and adopt-playbook.sh 432 to 445 (DERIVED 2026-11-25, over the draft). Say that the row is widened through the verb and its count then set to the measure, as unit 116's row was.

## Summary

Nothing is committed. Every path I changed is restored to 1ea35c769; only RUN.md stays staged, as dispatched. `--brief` answered "already recorded, unchanged".

DRAFT: C:/Temp/claude/7a8436c9e3b87ce5/9067262b-db21-4497-8ba8-ef2deab46f53/scratchpad/u121/draft.patch covers 15 files (DERIVED 2026-11-25) and applies clean on this HEAD. It holds S1 to S8, S10, S11 and S14, the READMEs of S15, and the two templates of S13. It carries the `malformed` row as the spec now writes it; once the spec is revised, one tuple in `tools/memory-tree/shape_run.py#build_fixture` changes. Not drafted: `FLOOR_ASSERTIONS`, the shell-role widens, the guides installed by `adopt-unattended.sh`, the map and index regeneration, the ledger, the spec header.

I found (1) by running a drafted plant, after product edits had begun, not in the pre-edit read. I then finished the draft so that everything could be reported at once.

Probes over the draft (all DERIVED 2026-11-25), standing in for the hygiene suite, build-index, review-replay and playbook render legs:
- AC1 and AC3: `door-header` printed PASS with 24 cases at rc 0, `ask-door` PASS with 17 cases at rc 0. `write_record` raised for both planted names. `door-header` ran 7m26s, past its 400 s foreground bound, so it finished in the background. `ask-door` ran 4m47s. (DERIVED 2026-11-25, the pass)
- AC2: the stubbed probe answered as §4 says for all three cases. (DERIVED 2026-11-25, the pass)
- AC4: over a scratch bare remote with a landed `in-slug` policy, `slug` and `ask` of `d2026-10-26ClosedLoop` exited 0. `-x` and `9x` exited 2. The new `test_slug_claims` arms were written, not run.
- AC5: `section-outside` and `missing-section` exited 2, `unheld-blob` exited 0, each with the wanted lines. (DERIVED 2026-11-25, the pass)
- AC6: the grep printed 1; the table-only stub named the planted member and nothing on today's tuple.
- AC7: every row as written, except the cut of `malformed` (divergence 1).
- AC8: the three census plants printed PASS; the suite's join was green whole and named each plant whose arm was cut.
- AC10: read 2 searches and 1461 bytes; the verdict boundaries answered as specified; the two edited selftest arms, run as cut-out functions, answered green. (DERIVED 2026-11-25, the pass)
- AC11: both plants exited 0, the grep printed 2, and the join named each cut row. (DERIVED 2026-11-25, the pass)
- AC13: template half only: `newest one` absent from VERBS (STOPS not re-grepped after its edit), and the `--feed` entry names `duplicate` twice and `walk git refuses` once. The compare with the guides is open.
- AC14: `--cause-writers` printed no RED and the grep printed 0.
- AC15: all its greps answer as wanted.
- AC9 and AC12: not observed.
- Pre-edit claim probes held: the field-name grammar over kinds, `fields` rows and shape-run fields; both plant joins; the gov-claim pre-check; the feed sentences against `tools/lib/gov-feed.sh`. The naming lexicon admits the six names I asked it about, and `VERB_OFFENDER_PIN` re-measures at 1437, its present value. (DERIVED 2026-11-25, the pass)

RED FOR THE MAIN LOOP, outside this unit: the shell-role row of tools/memory-tree/check-memory-hygiene.test.sh reads 3752 while the suite at HEAD measures 3756 (DERIVED 2026-11-25). Unit 120 added five code lines and its one widen raised the row by one, so the portability leg should read red at HEAD until S12 lands.

Owed to the close once built: the whole suite count (AC9), §7's legs, and the RED-first observation of every `New arm:` line. The bug-class checklist was not run, because there is no commit.

Three commands were refused by guards and re-issued in another form: one by gate-guard for naming a suite in a `wc`, and several by the worktree guard for complex inline git text.
