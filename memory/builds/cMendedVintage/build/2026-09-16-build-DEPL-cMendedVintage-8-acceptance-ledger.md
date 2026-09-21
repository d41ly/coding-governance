# cMendedVintage — the acceptance ledger for unit 8

**Serves:** journal DEPL-cMendedVintage-8

*Node `c`. BACK-FILLED 2026-09-17 by a later pass, NOT by the pass that built the unit — the
filename carries the date of the unit's own commit, `8295fb18`, 2026-09-16. Where a criterion is
answered by a command it was replayed at the shell against this worktree and its result is given;
where it is answered by what the building pass measured, the commit is cited AS the record and named
as such. No merge bar, no `*.test.sh` and no self-test runner ran in this pass:
`tools/govkit/selftest.py` was READ, never executed.*

## The one thing worth reading twice

**The red was observed TWICE by the building pass, and neither observation is reproducible from
here.** A fixture proves a mechanism only for the fixture's own values, so after the scratch tree
refused, the predicate as committed was run over the SHIPPED descriptors at a detached worktree at
base `859daa67`: exit 1, naming `memory-tree` with 4 rendered rows and `memory-recall`,
`drift-audit` and `lexicon` with 1 each, its note reading 6 shipping and 2 declaring. The first
needs the suite this pass may not run; the second needs the tree this build repaired. Both reach
this ledger through the commit and the spec's section 9, and through nothing else.

**The control fixture found a defect that nothing else in the suite could reach.** It is the first
descriptor there to declare a `[[regenerate]]`, so it is the first to reach arm 7l's prose half on a
scratch tree — and that half died with a `ValueError`, having resolved the repo-relative descriptor
path against the PROCESS CWD. One operand moved. That repair IS observable here and was observed:
`selfcheck` run from `C:/Temp` with the script's absolute path exits 0 and prints the same notes as
a run from the tree itself. The BASE red behind it is the commit's record, not this pass's.

**Evidences:** DEPL-cMendedVintage-8

- AC1 — `python tools/govkit/govkit.py selfcheck` — two halves, and only the first is replayable. At
  this tip: exit 0, note `rendered rows: 6 descriptor(s) ship at least one, 6 of those declare
  [[regenerate]]`. Run again from the foreign cwd `C:/Temp`: exit 0, byte-identical note. The SECOND
  half — the same arm failing over the shipped descriptors before `DEPL-cMendedVintage-5` and
  `TOOL-cMendedVintage-1` are in the tree — is the building pass's, recorded in the commit with the
  four kit names and row counts quoted above. This pass did not rebuild that worktree, and the state
  it measured no longer exists at any ref this build left behind. What was read here instead is the
  criterion's Red-when in the source: the refusal sits at `tools/govkit/govkit.py:2091` and the skip
  it inverts at `:2107`, so the offending population reaches the join before anything filters it.
- AC2 — `python tools/govkit/govkit.py selfcheck` — REPLAYED at this tip, which is a tree where no
  descriptor is in breach. Exit 0, and the note still prints: `rendered rows: 6 descriptor(s) ship
  at least one, 6 of those declare [[regenerate]]`. So the note lives outside the failure branch,
  which is precisely this criterion's Red-when, and a clean run says what it examined instead of
  going silent. Its mirror — the note on a run where the refusal DID fire — is not observed here;
  the committed arm asserts a note reading 1 shipping and 0 declaring on the red fixture, and the
  commit records that run.
- AC3 — `build_scratch_gov_kit` — NOT OBSERVED IN THIS PASS, and this tree offers no way to observe
  it. The criterion is answered only by building the scratch gov tree from the suite's own helper,
  and the arms that do it live in `tools/govkit/selftest.py`, which this pass was forbidden to run.
  They were READ at this tip instead, at `selftest.py:2587` through `:2602`: the break fixture
  `rendered-no-regen` is asserted to exit 1, with the refusal naming the entry, its rendered-row
  count and what goes stale; the note is asserted on that red run as well as on the clean one; and
  the control `rendered-regen` — the same descriptor plus the block — is asserted to exit 0 with the
  note reading 1 and 1. What the criterion asks was observed by the building pass and commit
  `8295fb18` is the record for it. Reading an arm is not running it, so AC3 is owed to the
  `govkit selftest` leg.
- AC4 — `python tools/check-kit-placeholders.py` — REPLAYED at this tip. Exit 0, and its summary
  reports 6 kits graded over 27 rule-token pairs, 8 kits declaring none and 1 exempt by a declared
  `why_no_adopter`, which is workflows. The replay is the weaker half of this answer and the source
  read is the stronger one: the criterion's Red-when is the new predicate MUTATING the descriptor
  dictionaries it walks, the predicate at `tools/govkit/govkit.py:2082`-`:2091` reads
  `d.get("files")` and `d.get("regenerate")` and assigns to neither, and the two checkers are
  separate processes in any case, so a mutation could not have shown up in this run at all.

## What this ledger does NOT claim

That the merge bar is green, or that any leg of it ran, in either pass. `govkit selftest` owns the
four arms this unit added — two for AC1, one for AC2 and the AC3 control — and it is unobserved for
this unit end to end. It is owed at the run's close, and AC3 is owed with it.

That any arm in `tools/govkit/selftest.py` passes, or that the file even imports. It was read at
this tip and executed by nothing.

That the refusal has ever fired over gov's own registry since the build repaired it. By design it
cannot: every descriptor shipping a rendered row now declares a block, which is the state this gate
exists to HOLD, so the only live exercisers are the fixture and the base-sha run, and both are the
building pass's. A predicate with no exerciser in its own tree is why the note counting both sides
of the join is asserted on the red run too.

That an adopter was tested. gov keeps no `.governance/install.json`, and the external edge the spec
names — an adopter running `selfcheck` over their own registry and getting the same refusal — was
not reached from here.
