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

## Hand-off to the lander

`main` moved while this branch was open. `09a22d2b` landed the third unit of build
dMuffledSentinel, which bumps the unattended kit 1.18 to 1.19 for its own changes. This branch also bumps the unattended kit 1.18 to
1.19, for different content. A trial `git merge-tree` of `main` with this branch conflicts only on the
generated `memory/ledger/2026-09.md`, which is re-rendered and never reconciled. Every unattended
version line merges CLEANLY, because both sides wrote the same bytes, and that is the hazard: two
different kits would both ship as 1.19, and `check-kit-versions.sh` would pass, because every
carrier agrees. The merge has to take the unattended kit to 1.20 at every carrier the version gate
reads.

## The criteria

**Evidences:** TOOL-dPolishedVitrine-1

- AC1 — `75763c4e` — OBSERVED: `diff` of the base blob against the render shows lines 3, 76 and 228
  and nothing else, and the parity leg exits 0 with `2 rendered pair(s)`.
- AC2 — `bash tools/workflows/unattended-build.test.sh` — OBSERVED: the flat layout passes arms (i)
  to (v), after the same arms were seen red on base blob `75763c4e` in that layout.
- AC3 — `tools/workflows/unattended-build.test.sh` — OBSERVED: nested, root, and root-with-flat
  memory-tree layouts pass all five arms. The root driver renders without a prefix.
- AC4 — `MEMORY_TREE_DIR` — OBSERVED: no tracked `gotchas.py` refuses at exit 2 naming the override,
  and no harness is written. The override renders `vendor/mt`, an untracked override is refused,
  and a tracked override holding a space is refused.
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
- AC10 — `bash tools/check-kit-versions.sh` — OBSERVED: exit 0 at 1.8 and 1.19. Item 6 above is the
  red.
- AC11 — amended rev-4 — the unattended clause now compares the tip's FAIL set with base's, and
  every shard's set is identical at both. The full bar at `44be8934` was green on 102 of 106 legs.
  The python resolver is red at base too, and the other three pass when run alone at that tip.
- AC12 — `tools/workflows/unattended-build.test.sh` — OBSERVED: the flat and nested layouts, rendered
  through both kits' own renderers, name one checklist command. With the adopter forced to the
  prefix-only answer, the flat layout redded naming both commands.
