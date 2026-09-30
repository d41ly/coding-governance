**Serves:** journal TOOL-dAlignedCarrier-6

# Fold brief — the closing review's round 1 into TOOL-dAlignedCarrier-6

The closing diff review, round 1, is `memory/builds/dAlignedCarrier/reviews/2026-09-30-review-TOOL-dAlignedCarrier-1-closing-diff-round1.md`.
Read it WHOLE: its four findings, M1, M2, L1 and L2, each carry a Where, a Defect, a Fix and a
Left-shift gate. The round recorded CONVERGED with zero blockers, so every finding is disposed BY
SEVERITY (BUILD-METHOD M4): each is FOLDED into this unit's spec as a rev-N bump with a section 9
line, and fixed in the code and text it names. This is ONE pass, one commit. The shared build brief
`2026-09-30-prompt-TOOL-dAlignedCarrier-1-build-brief.md` still binds every rule it states — read it
too — except that the spec is already CLOSED and stays CLOSED.

## What each finding owes

- **M1** — in `verb_phase`, `stage_or_fail` moves below `set_fact ... witness`, so the move stages the
  whole record. Then the unit-6 arm stops relying on its own `add -A` and asserts the move leaves
  nothing unstaged, and the TOOL-aBoundedVerdict-15 arm asserts an empty unstaged diff too.
- **M2** — the fork is RESOLVED as the review's option (a): the notice, the Skill's Close paragraph
  and its export line, the protocol's `SELFTESTS_OWED_PATHS` row and both conf comments name
  `GATE_FULL=1 GATE_SELFTESTS=1` as the pair the main loop exports into its one `--close`. The driver
  still sets neither. Record it in the spec's section 8 as a new F-item:
  `RESOLVED (agent, 2026-09-30, delegated)`. The reason: owner ruling TOOL-dDerivedDocket-70 names the
  flag the main loop exports and forbids the driver setting it, and the charter's kit Definition of
  Done names the pair. Adding `GATE_FULL=1` to the export keeps both true under `primary`, where the
  close's bar carries no `GATE_FULL`. Add the env-recording arm the review describes. The arm is
  written, not run.
- **L1** — the range read in `print_selftests_owed` uses `--no-renames` with
  `core.quotepath=off`, and a failed diff announces "unanswerable, not no" as the review's Fix spells
  it; add the rename-out arm.
- **L2** — check 45's header in `tools/unattended/check-unattended.sh`, and its blank-key echo and
  fail message, name the move into VERIFYING, not the in-place close. The fail-45 arm's literal in
  `check-unattended.test.sh` changes IN THE SAME COMMIT, because `hit` greps the whole message.

## Left-shift — every finding, no exceptions

M8: a finding fixed and not left-shifted returns. For each, EITHER a gate seen RED on a staged
instance, OR a class file under `memory/gotchas/` (its catalogue index re-rendered with
`python tools/memory-tree/gotchas.py --write`) where the class cannot be gated without false hits.
Before wiring any predicate, run it over the real tree and print hits AND near-misses (charter §7). A
predicate that would red an innocent line is a gotcha, not a gate. The review's own suggestions, in
order of preference:

- M1: a static predicate in `check-unattended.sh` — no function calls `set_fact` on a record after its
  last `stage_or_fail` of it.
- M2: the env-recording arm (a suite arm, so it is written, and its behaviour is observed through a
  scratch fixture that runs the same steps, as the unit-6 pass did).
- L1: a class entry — a prefix-matched porcelain `diff --name-only` carries `--no-renames` — since the
  review found one live hit, the defect itself.
- L2: generalise check 47 into a small table of retired premises and add "in-place close ... announce".

## Budgets and traps

- The protocol template is at 65288 of 65692 bytes: this pass may add at most 300 bytes to it.
- `.unattended.conf` is on the kickoff manifest's `watch:` list: the commit re-stamps `last-audit` in
  `memory/guides/SESSION-KICKOFF.md`, with a `manifest-audit:` line in its message.
- `tools/unattended/check-unattended.sh` is edited in BYTES; its CR count must stay 4.
- Declare every written path with `--dispatch` before the commit, generated ones included.
- Append a ledger line for every NEW section 6 criterion this fold adds to the existing ledger
  `memory/builds/dAlignedCarrier/build/2026-09-30-build-TOOL-dAlignedCarrier-6-1-acceptance-ledger.md`,
  in the same observed or amended form.
- Commit subject: `fold(dAlignedCarrier): TOOL-dAlignedCarrier-6 — the closing review's round 1`.
