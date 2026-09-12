# Build journal — TOOL-dPolishedVitrine-1

**Serves:** journal TOOL-dPolishedVitrine-1

Tier-2 · node d · 2026-09-12 · base 24f8c712 · worktree `.claude/worktrees/derived-harness-paths`

## The bar at base, before any edit

`GATE_FULL=1 GATE_SELFTESTS=1 bash tools/run-gates/run-gates.sh` at `24f8c712` finished 105 of 106
legs green in sixteen minutes of wall (07:41 to 07:57 UTC). The one red is
`python resolver (behaviour + inline parity + idiom ban)`, on
`tools/run-gates/run-gates.evidence.test.sh:643`, where `DC_PY=python` is a launcher nobody
resolved. It is red at base and this unit touches neither file. The dMuffledSentinel ledger records
the same red as on `origin/main` since `d4c05068`.

## Every new arm, observed red before its fix

Each break below was staged, run, recorded and unstaged. The raw outputs were kept in the session
scratchpad; what matters from each is quoted.

1. **HEAD's verbatim harness, installed the way apply installs an engine file.** Base blob
   `75763c4e` went into a flat consumer layout at `scripts/workflows`, with a tracked
   `scripts/gotchas.py`, and was graded by the suite's own `check_layout` expecting all green.
   The harness ran to its hand-out, and arms (i) to (v) all failed. The driver read
   `bash tools/unattended/unattended.sh`, the checklist `python tools/memory-tree/gotchas.py
   --for-diff HEAD~1..HEAD`, and the class arm listed four untracked paths: the two workflow
   scripts, the driver and the checklist. That is all four install literals, named by the arm
   that does not know which four to look for.
2. **The prefix-only half-fix, on the real template.** With `CHECKLIST` changed to
   `{{TOOL_ROOT}}memory-tree/gotchas.py`, the flat layout redded (iv) and (v) on
   `scripts/memory-tree/gotchas.py`, and so did the flat root install and the override layout. The
   NESTED layout and the nested root install stayed green. That is the whole reason the flat
   fixture carries the weight. The same run also redded the hand-edit arm, which was the arm's own
   fault rather than the parity script's: its first cut edited a path in place, and under this
   template that path was spelled differently, so nothing was edited and no DRIFT could appear. It
   now appends a line, which cannot miss.
3. **The parity script's charset refusal, disabled.** With a space admitted to the allowed set, a
   tracked override `vendor/m t` rendered cleanly. Both new assertions redded, and nothing else did.
4. **The unattended adopter, before its fix.** With the suite's seed repaired (below) and the
   adopter unchanged, the flat layout rendered the literal nested path, a tree with no `gotchas.py`
   adopted at exit 0 and wrote a Skill, and an override naming nothing tracked adopted anyway.
   Arm 1's nested assertion PASSED against the unfixed adopter, because the nested seed is this
   repo's own layout. That pass is the defect in miniature, and it is why arms 7 to 9 exist.
5. **The adopter's charset refusal, disabled.** The three space-override assertions redded and
   nothing else did.
6. **A half-bumped version.** Reverting the Skill template's marker to 1.18 and the review-harness
   marker to 1.7 made `tools/check-kit-versions.sh` exit 1, naming both carriers.
7. **The adopter's new substitution, deleted.** `tools/check-kit-placeholders.py` exited 1 naming
   `{{MEMORY_TREE_DIR}}` on the unattended kit. `adopt-unattended.sh --check` exited 1 at Skill line
   583, where the template's placeholder would ship unfilled.
8. **The install-prefix ban, both ways.** With the new `rendered` rule deleted from the workflows
   descriptor, the render stayed a shipped source and its row read `6 -> 5` rather than dropping.
   So the claim is what removes it, not the rewording. With the old `tools/hooks/agent-cap.js`
   comment restored in the template, the template reported UNRECORDED.

## What the arms measure, and the population behind arm (v)

The class arm extracts every relative path ending in `.js`, `.sh` or `.py` from the harness's whole
output: the trace, the prompts it composed and the return. Over every layout the population was
exactly four tokens, the same four sites the other arms name, with no near-miss outside them.
The arm asserts at least four, so an extraction that silently found nothing reds rather than passing.

gov's own render against its base blob, by `diff`, differs at lines 3, 76 and 228, all three
comments. Every code line renders back to this repo's own path.

## Found red at base, and fixed because the new arms needed it

`tools/unattended/adopt-unattended.test.sh` was red at `24f8c712` with 22 failures. Its `seed()`
copied a hand list of three templates. The adopter gained the verb carrier and the playbook
fixture's template after that list was written, so every adopt in the suite stopped at the fixture
render and exited 1. The suite runs only on demand, so nothing noticed. It now copies the kit's
`*.template.md` by glob, which is the class and not the instance.

## Traps met, recorded so the next session does not pay for them again

- **A Python text-mode rewrite eats raw CR bytes.** `adopt-unattended.sh` carries twelve literal CRs
  inside `tr -d` arguments. Reading and writing it through Python's universal-newline mode turned
  each one into a line break, and the adopter stopped working for reasons unrelated to the break
  being staged. Every later edit went through `sed -i` on a line number or through `cp` restores,
  and CR counts were compared against HEAD before each commit.
- **This session's shell mangles `\\` in a command.** A `sed` replacement meant to insert a
  backslash-escaped space inserted a bare one, which ends a `case` pattern. The staged break was
  redone without a backslash.

## The full bar at the tip, and what its three reds were

`GATE_FULL=1 GATE_SELFTESTS=1 bash tools/run-gates/run-gates.sh` at `2a29ae3c` ran 08:36 to 09:02
UTC. 103 of 106 legs were green. Three were red:

- `python resolver (behaviour + inline parity + idiom ban)` was red for the reason recorded at base.
- `run-selftests self-test` timed out at its 300 s ceiling. The session had put other work on the
  node during the bar, and this run came in under that load. Run alone at the same tip it printed
  `PASS (43 arms, width 1)` in 103 s.
- `memory-hygiene self-test` timed out at its 900 s ceiling. Run alone, it did NOT pass. Its
  project-keys block copies the tree with `git archive HEAD` into a fresh repository that has no
  history. Since `BASE_RESOLVE_CUTOFF`, check 12 resolves a live spec's `base` against the object
  database, and this unit's own INPROGRESS spec names `base 24f8c712`, which that fixture could not
  hold. So the clean-fixture arm and the four arms after it redded, and any branch in the middle of
  an ordinary Tier-2 build hits the same five reds. Reproduced by hand with the same steps: check 12
  names this spec's base.

  The fixture now borrows the real object database through an alternates entry. It gets the same
  objects without a copy, and nothing else the checker reads changes. With the entry, the same
  reproduction exits 0, and the suite run alone at the same tree prints `PASS (374 assertions)`.
  The sibling fixture in `hygiene-parity.test.sh` has the same exposure, but it was not observed,
  so it is carried as `TOOL-dPolishedVitrine-9` rather than changed.

## The unattended kit's on-demand self-tests, tip against base

Work touching the unattended kit owes the seven suites `run-unattended-gates.sh` delegates to, and
`run-selftests.sh --kit tools/unattended --list` names them. Each was run directly at the tip. The
two that are red at base were also run at `24f8c712`, in a scratch repository holding
`git archive 24f8c712`, side by side with the tip on the same node:

- `adopt-unattended.test.sh` printed `PASS (71 assertions)` at the tip. It was red at base with 22
  failures, which is the seed defect recorded above.
- `cross-component.test.sh`, `check-playbook.test.sh`, `check-pass-order.test.sh` and
  `check-brief-recorded.test.sh` all exited 0 at the tip.
- `unattended.test.sh` and `check-unattended.test.sh` each ran as `--shard 1/2` and `--shard 2/2`.
  Their FAIL lines were compared shard by shard, with the kit directory and temp paths normalised,
  and every pair of sets is identical. The driver's shard 1 prints `PASS (240 assertions)` at both,
  and its shard 2 fails the same 53 lines at both. The checker fails the same 12 lines in shard 1
  and the same 23 in shard 2. No FAIL line is new at the tip, and none went missing. These reds
  predate this unit: `TOOL-aHoistedPass-38` and `TOOL-aTracedSpawn-3` carry them, and rev-4 records
  why the runner cannot print GREEN at base.

## The full bar at `44be8934`, and its reruns

The bar ran again at `44be8934`, 10:15 to 10:44 UTC, while other sessions' suites were running on
the node. 102 of 106 legs were green, and four were red:

- `python resolver (behaviour + inline parity + idiom ban)` was red, as it is at base.
- `memory-hygiene self-test` and `hook destinations self-test` both timed out at their 900 s
  ceilings. This unit touches the first suite's fixture and not the second. Rerun alone through the
  runner at the same tip, they passed in 422 s and 135 s.
- `run-gates turnstile` failed two arms after its own control could not establish, because the
  holder did not claim the beacon within 30 s. This unit touches nothing under `tools/run-gates/`.
  Run directly at the same tip, it printed `PASS (65 assertions)` in 703 s.

The first turnstile rerun is not evidence, and it is recorded here as a trap. It went through the
runner with `GATE_LEGS` naming a three-leg file. The suite's inner runners inherit that variable,
and it outranks their own legs file, so eight arms failed. Run directly with the variable unset,
the suite passed. `TOOL-dPolishedVitrine-10` carries the leak.

The records commit after it, `ff663e2e`, ran the same bar with `GATE_REUSE=1`, so 54 legs whose
inputs were unchanged reused their green and the other 52 executed. Two were red. One was the
python resolver. The other was the turnstile, on one timing arm, `not every queued runner
acquired`, while another session's suite held the node. The turnstile suite was then run at the
tip and at base side by side. Both printed `PASS (65 assertions)`, in 688 s and 686 s, and both
skipped the same two arms because the holder did not claim the beacon within 30 s.

## Found by the bug-class checklist, after the build

`python tools/memory-tree/gotchas.py --for-diff 24f8c712..HEAD` named 30 classes over this diff. Two
of them applied, and both were acted on in rev-3.

- **amendment-leaves-its-other-half-standing.** rev-2 moved the new inventory key from the
  unattended dossier to the review-harnesses dossier in S7. The same move was left undone in two
  places in §4, which still named the unattended dossier. rev-3 corrects both.
- **two-answers-to-one-question.** The `MEMORY_TREE_DIR` probe is written twice, once in each kit,
  because the kits install separately and share no code. Two comments claimed the two carriers
  "cannot disagree", and nothing checked that claim. AC12 and its arm now check it. One layout is
  rendered through both kits' own renderers, and the two checklist commands they produce are
  compared, flat and nested. The arm was observed RED by a staged break: with the adopter forced to
  the prefix-only answer after its probe, the flat layout's Skill said
  `python scripts/memory-tree/gotchas.py` while the harness said `python scripts/gotchas.py`.

## What the round-1 review changed

The round-1 Tier-2 diff review of `24f8c712...0c0e1757` returned BLOCKED on five defects. Its
report is committed under `reviews/` beside this journal. Each defect is below: what changed, the
gate it left behind, and the red that gate showed before the fix. The consumer fixture behind F1
and F2 was built by `govkit apply` from a gov clone at `24f8c712`. The target sits at prefix
`scripts`, with the memory-tree kit flat and the review harness at `scripts/workflows`. Its receipt
is schema 3 and rows `scripts/workflows/unattended-build.js` as `engine`, with both identities at
`75763c4e`, which is the consumer shape the review read off both real receipts.

- **F1, blocker: the existing receipt keeps the harness an engine row.** Reproduced first. At the
  tip, `GOVKIT_RERENDER=1 update --write` graded the row `stale` and raw-wrote gov's render
  `ac362480`, which carries all four `tools/` literals. Once committed, the index held a correct
  render while the receipt still named `ac362480`, so receipt-sync reds. The next `update` graded
  the row `patched [engine]`. The repair in scope is the consumer migration now in §4 Rollout, the
  runbook's Maintenance section and the kit README. It ran verbatim on two fixtures, one with the
  review harness alone and one with the unattended kit as well, and each carried one local edit.
  Both ended with the row `rendered` and `pinned`, and no row `unattributed`. In both, every
  non-rendered row's index blob equalled its receipt `oid`, the next `update` wrote nothing and
  re-stamped, every parity and wiring check passed, and the harness spelled no `tools/` path. The
  pins are load-bearing. An unpinned re-adopt left the harness render, the protocol render and the
  edited row `unattributed`, and the next `update` withheld its re-stamp over all three. The gate is
  the govkit selftest's `[-PV] F1` arms on a synthetic kit of the same shape, with an unpinned
  control. Observed red: with the re-adopt swapped for a `check`, which is the old hand-off, five
  migration arms redded, and the next `update` graded the correct render `carried (relocate)
  [engine]`. NOT done here: `update` re-resolving roles at schema 3, filed as `DEPL-dPolishedVitrine-1`.
  Its blast radius reaches every row whose descriptor role moved, including the self-tests
  `TOOL-aQuenchedHarness-3` withheld as `project-owned`, and that is an owner's call. Until it lands,
  `update` still grades such a row as an engine file rather than naming the move.
- **F2, high: the regenerate ran before its input.** govkit's unclaimed-source landing now precedes
  the re-render block. That is a swap of two adjacent blocks, and nothing in the landing reads
  what the re-render writes. The failure text no longer promises a rollback. It now says what the
  kit's own check can and cannot undo. govkit moves 1.10 to 1.11, because consumers run it from gov
  and the hand-off has to name the vintage that works. The gate is the `[-PV] F2` arms, plus a
  NEGATIVE in which a failing regenerate in a `[check] none` kit fails the run and promises nothing.
  Observed red on HEAD's engine: four F2 arms, and two F1 arms that need the render. On the consumer
  fixture the run read `ran review-harness: … --render -> exit 1 REFUSED` and `rolled back 0`, and
  withheld its stamp. After the fix it read `-> exit 0`, re-stamped, and the parity leg was green.
  These are the first arms anywhere that set `GOVKIT_RERENDER=1`. The `_D1_ANNOUNCED` comment said
  "the S6 arms below" did, none of them does, and that comment is corrected. NOT done: running a
  regenerate when no row touched its kit, filed as `DEPL-dPolishedVitrine-2`.
- **F3, medium: one pair's refusal blocked both.** The parity script resolves `MEMORY_TREE_DIR` per
  pair. When the probe finds nothing and no override is set, only the pairs whose template carries
  the token are SKIPPED, by name and with the override named. A misplaced override still exits 2.
  The gate is the `PV-F3` arms over a review-harness-only layout with no memory-tree and no
  unattended kit. There `--render` renders the protocol and names the skip, `--check` passes counting
  it, and a drifted protocol still reds. Observed red: eight of the ten before the fix. AC4's arm
  now asserts the skip.
- **F4, low: the guard missed the leg's new input.** The parity leg is unguarded in both carriers,
  and the kickoff manifest is re-stamped in the same commit. No new gate. It is recorded as the
  known positive on `TOOL-aPacedTurnstile-9`.
- **F5, low: carriers promised a flag-off re-render.** Every carrier now names `GOVKIT_RERENDER` in
  the sentence that promises the re-render, and says what happens without it. The gate is govkit
  selfcheck arm 7l. For each kit declaring `[[regenerate]]`, a sentence in its tracked files or
  descriptor that names `update` with a re-render word must also name the flag. Before it was wired,
  the predicate ran over the real tree, printing hits and near-misses. It found the four in-kit
  carriers the review named, plus one it did not, in `tools/unattended/kit.toml`, and no near-miss
  that was a claim. Observed red: `5 problem(s)` on the unfixed carriers, then two more on this
  round's own first rewording, which said "that flag".

Found while fixing, and not this unit's:

- The unattended fixture shows `fixture-records/tools~…` churning on every update. `update` restores
  them as `missing`, and the regenerate deletes them again. Filed as `TOOL-dPolishedVitrine-11`.
- The first names for the new selftest helpers took a `pv_` prefix. The verb gate counted five
  offenders over its pin, 991 against 986, so they were renamed through `--suggest`.
- Citing this unit's id from product source while its spec is INPROGRESS raised drift signal
  `non_terminal_specs_cited_by_product_source` to 3 over its pin of 2. Those comments now cite
  the build slug instead.

## Hand-off to the lander

`main` moved while this branch was open. `09a22d2b` landed the third unit of build
dMuffledSentinel, which bumps the unattended kit 1.18 to 1.19 for its own changes. This branch also bumps the unattended kit 1.18 to
1.19, for different content. A trial `git merge-tree` of `main` with this branch conflicts only on the
generated `memory/ledger/2026-09.md`, which is re-rendered and never reconciled. Every unattended
version line merges CLEANLY, because both sides wrote the same bytes, and that is the hazard: two
different kits would both ship as 1.19, and `check-kit-versions.sh` would pass, because every
carrier agrees. The merge has to take the unattended kit to 1.20 at every carrier the version gate
reads.

Done at the merge, after round 1's repairs. Every carrier the gate reads moved to 1.20: the four
script constants and their same-line markers, and the five templates. So did the kit README's
line-1 marker, which the gate does not read (`DEPL-aHoistedPass-10`). The five gov renders were
re-rendered by the adopter and not edited, and each moved by its marker line alone. The only
conflict was the generated ledger, which was re-rendered. `memory/DECISIONS.md` merged cleanly
through the row-keyed driver. Checked per file against the merge base: every line either parent
added is in the result, 48 files on this side and 31 on `main`'s. review-harness 1.8 and govkit
1.11 are unclaimed on `main`, which holds 1.7 and 1.10. `main` touched no kickoff watch path, and
`manifest-check.sh` passes after the merge, so the manifest was not re-stamped again.

## The criteria

**Evidences:** TOOL-dPolishedVitrine-1

- AC1 — `75763c4e` — OBSERVED: `diff` of the base blob against the render shows lines 3, 76 and 228
  and nothing else, and the parity leg exits 0 with `2 rendered pair(s)`.
- AC2 — `bash tools/workflows/unattended-build.test.sh` — OBSERVED: the flat layout passes arms (i)
  to (v), after the same arms were seen red on base blob `75763c4e` in that layout.
- AC3 — `tools/workflows/unattended-build.test.sh` — OBSERVED: nested, root, and root-with-flat
  memory-tree layouts pass all five arms. The root driver renders without a prefix.
- AC4 — amended rev-5 — no tracked `gotchas.py` now SKIPS the harness pair at exit 0 and still
  renders the protocol, where it used to refuse the whole run at exit 2. The skip names the override
  and writes no harness. The override still renders `vendor/mt`, and an untracked override or one
  holding a space is still refused. That is spec section 9's rev-5 line.
- AC5 — `DRIFT` — OBSERVED: a hand-edited render reds, an unpaired template reds naming its path,
  and a missing live copy reds under the check mode and is created by the render mode.
- AC6 — `tools/workflows/unattended-build.test.sh` — OBSERVED: the verbatim spelling reds all five
  arms, and the prefix-only half-fix reds (iv) and (v) only, on every run of the suite.
- AC7 — `bash tools/check-install-prefix.sh` — OBSERVED: exit 0 after `--write-ratchet` dropped
  exactly the two rows. Both breaks in item 8 above redded as the criterion says.
- AC8 — `bash tools/unattended/adopt-unattended.test.sh` — OBSERVED: `PASS (71 assertions)`, after
  arms 7 to 9 were seen red against the unfixed adopter.
- AC9 — `python tools/check-kit-placeholders.py` — OBSERVED: exit 0 with the placeholder declared,
  `adopt-unattended.sh --check` in sync, and gov's Skill line 583 unchanged. Item 7 above is the red.
- AC10 — amended rev-6 — the gate exits 0 at review-harness 1.8, unattended 1.20 and govkit 1.11
  after the merge. Item 6 above is still the red, and spec section 9's rev-6 line logs the move.
- AC11 — amended rev-4 — the unattended clause now compares the tip's FAIL set with base's, and
  every shard's set is identical at both. The full bar at `44be8934` was green on 102 of 106 legs.
  The python resolver is red at base too, and the other three pass when run alone at that tip.
- AC12 — `tools/workflows/unattended-build.test.sh` — OBSERVED: the flat and nested layouts, rendered
  through both kits' own renderers, name one checklist command. With the adopter forced to the
  prefix-only answer, the flat layout redded naming both commands.
- AC13 — `tools/govkit/selftest.py` — OBSERVED: the `[-PV] F1` arms pass inside the whole suite,
  which printed `all arms held`. With the re-adopt swapped for the old hand-off, five of them redded.
  The same sequence converged on both consumer fixtures described above.
- AC14 — `GOVKIT_RERENDER` — OBSERVED: the `[-PV] F2` arms pass, and on HEAD's engine three of them
  and the negative's no-promise arm redded. The consumer fixture read `-> exit 1 REFUSED` before
  the move and `-> exit 0` after it.
- AC15 — `check-protocol-parity.test.sh --render` — OBSERVED: the `PV-F3` arms in
  `tools/workflows/unattended-build.test.sh` pass, and eight of the ten redded against the unfixed
  parity script.
- AC16 — `govkit selfcheck` — OBSERVED: arm 7l reported `5 problem(s)` on the unfixed carriers and
  exits 0 on the corrected ones.
