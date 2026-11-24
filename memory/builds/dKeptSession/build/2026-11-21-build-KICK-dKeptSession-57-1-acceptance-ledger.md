# KICK-dKeptSession-57 — acceptance ledger

**Serves:** journal KICK-dKeptSession-57

No merge bar, no self-test suite and no gate leg ran in this pass. The criteria were observed on win32
from the pass's base `17933b416`, over the working tree of the pass's one commit, by the commands the
criteria state, run by direct CLI, and by one `python` probe that reads each named unit's Files touched
through `tools/check-spec-tokens.py#extract_files_touched` and hands those paths to the `--legs-for`
query.

## Reconciled at the build

The rev-4 spec was grounded on `71b22e42`; units 44 and 56 have since landed, and unit 56 is CLOSED at
rev-6. Every claim the spec makes about current code held at this base: `git show --stat 6178a65e`
lists `tools/memory-tree/build_records.py` and `tools/memory-tree/tree_lib.py`; `tools/gate-legs.json`
carries no `loop selftest` row and `tools/loop/selftest.py` is absent; the `loop transition record`
and `loop position fixtures` rows carry no `guard`; and `policy.py mirror --check` printed `policy:
mirror fresh` (PINNED 2026-11-23, this pass's base). The spec's design was built as written, with these
readings of its text:

- S2: `python tools/policy/policy.py mirror --write` ran once, at the base, and moved no byte of
  `.governance/policy.json` (DERIVED, `git status --porcelain` empty after it). This pass's one commit
  touches no mirror input, so the render is the one that runs after it, and no mirror commit is owed.
  AC2 is observed by `--check`.
- S3: the lines below are the query re-run over each named unit's Files touched at this pass, never a
  copy of unit 56's ledger. They differ from 56's in two ways. Unit 56 queried the paths each unit's
  `Pass:` commits touched, where this unit queries the Files touched its spec declares. And the
  `policy fixtures` row trips units 35, 36, 39 and 42 only through `tools/run-gates/`, a guard the
  query marks `broad`, so their lines do not name it, where 56's line named it for every unit but 39.
- S3: unit 44's line also names `loop transition record`, which 56 S27 owes unit 44 beside `loop
  position fixtures`.
- S3: unit 36's Files touched trip no guarded leg on a row the query leaves unmarked: every row it
  prints for them is marked `broad`, or the path trips nothing. Its line names the unguarded leg alone.

## The legs each named unit's pass owes (S3)

`python tools/check-spec-tokens.py --legs-for <paths>` over the paths `extract_files_touched` reads from
each unit's `### Files touched (estimate)` exited 0 for every unit, with no path untracked and no
UNEVALUATED row (DERIVED, that probe). Each line names every leg the query printed on a row not marked
`broad`. `loop transition record` and `loop position fixtures` carry no `guard` in `tools/gate-legs.json`,
so the query never names them; they run on every change and are named where the plants they run are
the unit's (DERIVED, the registry's rows).

- OBSERVED KICK-dKeptSession-30: `format-guard self-test` · `runlog selftest` · `run-gates run-log line` · `pre-push run-log line` · `policy fixtures` · `routed-commits selftest` · `scratch-guard self-test` · `lexicon naming predicates` · `manifest-check self-test` · `recall floor` · `recall floor arms`.
- OBSERVED KICK-dKeptSession-32: `build-index selftest` · `gotchas selftest` · `routed-commits selftest` · `recall floor` · `recall floor arms` · `scratch-guard self-test` · `memory-recall kit selftest` · `policy fixtures`.
- OBSERVED KICK-dKeptSession-33: `routed-commits selftest` · `scratch-guard self-test` · `policy fixtures` · `build-index selftest` · `gotchas selftest` · `recall floor` · `recall floor arms` · `memory-recall kit selftest`.
- OBSERVED KICK-dKeptSession-34: `routed-commits selftest` · `scratch-guard self-test` · `policy fixtures` · `recall floor` · `recall floor arms`.
- OBSERVED KICK-dKeptSession-35: `scratch-guard self-test` · `tier2-review self-test` · `recall floor` · `recall floor arms`; and `loop transition record`, unguarded, for its notices plants.
- OBSERVED KICK-dKeptSession-36: no leg on an unmarked row; `loop transition record`, unguarded, for its guard-launch plants.
- OBSERVED KICK-dKeptSession-37: `lexicon naming predicates` · `manifest-check self-test` · `scratch-guard self-test` · `policy fixtures` · `recall floor` · `recall floor arms`.
- OBSERVED KICK-dKeptSession-38: `lexicon naming predicates` · `manifest-check self-test` · `scratch-guard self-test` · `policy fixtures` · `recall floor` · `recall floor arms`.
- OBSERVED KICK-dKeptSession-39: `kit/dogfood doc parity` · `recall floor` · `recall floor arms`.
- OBSERVED KICK-dKeptSession-40: `build-index selftest` · `gotchas selftest` · `routed-commits selftest` · `recall floor` · `recall floor arms` · `scratch-guard self-test` · `memory-recall kit selftest` · `policy fixtures`.
- OBSERVED KICK-dKeptSession-41: `routed-commits selftest` · `scratch-guard self-test` · `policy fixtures` · `recall floor` · `recall floor arms`.
- OBSERVED KICK-dKeptSession-42: `recall floor` · `recall floor arms`; and `loop transition record`, unguarded, for its acks plants.
- OBSERVED KICK-dKeptSession-43: `hook destinations self-test` · `scratch-guard self-test` · `format-guard self-test` · `agent-cap self-test` · `verifier fan-out self-test` · `review-join self-test` · `policy fixtures`.
- OBSERVED KICK-dKeptSession-44: `routed-commits selftest` · `scratch-guard self-test` · `policy fixtures` · `build-index selftest` · `gotchas selftest` · `recall floor` · `recall floor arms` · `memory-recall kit selftest` · `tier2-review self-test` · `lexicon naming predicates` · `manifest-check self-test` · `runlog selftest` · `run-gates run-log line` · `pre-push run-log line` · `format-guard self-test`; and, unguarded, `loop transition record` for `mail-read-crash` and `loop position fixtures`.

## Unit 56's criteria answered here (S4)

Unit 56 is CLOSED, so neither its spec nor its ledger is written (§8 F1); its three criteria are
answered here, each by name.

- `KICK-dKeptSession-56` AC11, red "when the factory row lands without the tuple member": answered by
  this unit's AC1. Unit 5's build commit `6178a65e` wrote both, and both are present at this pass.
- `KICK-dKeptSession-56` AC22, red when "a guarded leg is missing from a pass's record": answered by
  this unit's AC3, the lines in the section above, one per named unit, re-bound from each unit's pass
  to this one.
- `KICK-dKeptSession-56` AC24, which ran `mirror --check` "at each of unit 40's and unit 41's pass
  commits": answered by this unit's AC2. Unit 56 recorded it red at unit 40's pass commit `f9e192e9`
  and unit 41's first commit `cca4b703`; those commits are history no later unit rewrites, so the
  criterion is re-bound to this pass, where the mirror reads fresh over every input units 40 and 41
  changed.

## Criteria

**Evidences:** KICK-dKeptSession-57
- AC1 — `git grep -n "mailbox-message"` over `tools/memory-tree/tree_lib.py` and `tools/memory-tree/build_records.py` printed the `TYPED_RECORD_KINDS` member and the `KINDS` factory row, and `python -c "import sys; sys.path.insert(0, 'tools/memory-tree'); import build_records"` exited 0 (DERIVED, those commands).
- AC2 — `python tools/policy/policy.py mirror --check` exited 0 printing `policy: mirror fresh`, and no commit of this pass touches `.governance/policy.json` (DERIVED, that command and the pass's diff).
- AC3 — `check-spec-tokens.py --legs-for` over each named unit's Files touched: one OBSERVED line per unit of 30 and 32 to 44 in the legs section above, each naming every leg the query printed on a row not marked `broad`, with `loop transition record` on units 35, 36, 42 and 44 and `loop position fixtures` on unit 44 (DERIVED, that probe).
- AC4 — the squeezed `grep -c` over this ledger reads each of the three quoted passages of unit 56's criteria once, and `git diff --name-only` over the pass's build folder lists this ledger alone, both read at the pass commit, and the main loop confirms it.

## What the close owes

§7's legs: `build-index selftest`, `recall floor`, `recall floor arms`, `lexicon naming predicates`,
`memory hygiene` and `spec tokens (a spec's own names resolve)`, with the bar's preflight `mirror
--check`. This unit adds no arm, so no RED-first observation is owed.
