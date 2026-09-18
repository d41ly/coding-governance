# DEPL-cMendedVintage-27 — the role re-resolution keeps the three-way merge a rendered row still needs

**Status:** CLOSED · rev-2 · 2026-09-19 · node c · Tier-2 · base 859daa67 · streams deployer · order 38

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-09-19-build-DEPL-cMendedVintage-27-acceptance-ledger.md](../build/2026-09-19-build-DEPL-cMendedVintage-27-acceptance-ledger.md) | journal | — |
| [2026-09-19-prompt-DEPL-cMendedVintage-27-2-build-brief.md](../prompts/2026-09-19-prompt-DEPL-cMendedVintage-27-2-build-brief.md) | journal | — |

<!-- /gen:spec-records -->

## 1. Goal

`DEPL-cMendedVintage-19` un-gated the role re-resolution in `cmd_update`'s row loop from
`if schema < 2 and row.get("kit") in descs:` to `if row.get("kit") in descs:`. A schema-3 row
recorded `engine` whose descriptor now resolves `rendered` therefore takes the new `role-moved`
branch: nothing is written, the row is not re-stamped, and it never reaches `classify_row`, the
verdict grid or the three-way. The kit's own regenerate writes that same destination later in the
same run, so the operator's local edit is destroyed with no conflict, no order and no line naming
it. Standing back only protects bytes nothing else in the run touches. Gate the branch on whether
the NEW role's own machinery writes that destination, so a move to `rendered` keeps its
reconciliation and a move to `project-owned` keeps standing back.

## 2. Scope (IN)

- **S1** The `role-moved` branch stands back only when `UPDATE_ROLE` maps the row's CURRENT role to
  a disposition that puts no bytes at that destination in this run. A move whose current role routes
  to `adopter` — the kit's declared `[[regenerate]]` argv — does not stand back. Observed by AC1,
  AC2 and AC4.
- **S2** A row that does not stand back keeps the disposition of the role it LANDED under, not the
  disposition of the role gov declares now. For the measured transition that is `table`, which is
  what reaches `classify_row`, the grid, the three-way and the `diverged and the three-way conflicts`
  refusal the migration runbook's block 2 keys on. Observed by AC1.
- **S3** The transition is still reported for such a row, once, and not as a second row line. The
  row prints its ordinary verdict line and the move is said on a `Report.note` line, so exactly one
  printed line both opens with two spaces and ends with that row's path. Observed by AC3.
- **S4** The disposition set is DECLARED beside `WRITING_DISPOSITIONS` rather than spelled inline at
  the branch, and `selfcheck` arm 7g's assertion extends to it: every member must be a disposition
  `UPDATE_ROLE` actually maps a role to. Observed by AC5.
- **S5** `tools/govkit/matrix.py`'s `check_role_move` gains the pair it has never had — an aged
  schema-3 receipt whose `engine` row's descriptor now resolves `rendered` under a kit that declares
  a regenerate — beside the `project-owned` pair it already carries. Observed by AC1 and AC2.
- **S6** Two paragraphs of `WIRE-INTO-PROJECT.md` are corrected: the Maintenance section's claim that
  nothing is written for a moved row, which now has one stated exception, and the harness-migration
  section's sentence that `update` "re-resolves it only below receipt schema 2", which has been false
  since `b52b5d80`. NOT OBSERVED — both are prose. The migration's fenced blocks are cut out of that
  file and run by the suite, and nothing reads the paragraphs around them.

## 3. Non-goals (OUT)

- No retirement of the harness migration. `DEPL-dPolishedVitrine-1` asks for that as a separate
  clause, and the runbook is the only thing in the suite that drives a `--kits`-scoped `update` end
  to end through a consumer's commit hooks. Retiring it in the unit that repairs it would spend that
  coverage to collect a prediction.
- No re-recording of the row's `role`. `DEPL-cMendedVintage-19`'s non-goal stands: `apply` is the
  verb that records a descriptor transition, and a row rewritten by `update` is a provenance claim
  nobody made.
- No new refusal against the regenerate. Making `update` decline a kit's `[[regenerate]]` over a
  destination whose row moved is the other way to stop the byte loss, and it removes the conflict
  path rather than restoring it — the runbook would still have nothing to set aside.
- No per-pair rule for the transitions no shipped descriptor makes today. The disposition test covers
  `merged`, `forked` and `seed` moves by construction; writing a row per pair would be a table of
  hypotheticals graded by nothing.
- No change to the schema-1 refusal, which is about an untrusted role rather than about a transition.

### Edges

- **consumes-from** `DEPL-cMendedVintage-19` — that unit un-gated the re-resolution and built the
  `role-moved` report. This unit narrows which rows reach it and adds nothing it did not first
  create; without it there is no branch here to gate.
- **hands-off** external — the two live adopters get a reconciliation where HEAD gave them a silent
  overwrite; retiring the migration stays with `DEPL-dPolishedVitrine-1`.

## 4. Design

### What the branch can see, and which fact decides

The re-resolution already computes the answer it needs. `resolve_entry` returns `writes` for the
landable roles and `unlanded` for the rest, and the branch reads `now` out of whichever holds the
row's destination. Both `project-owned` and `rendered` arrive through `unlanded`, so "is the new role
landable" cannot tell them apart and neither can the presence of gov's blob: `project-owned` is a
source-level carve-out and gov's own copy of a carved source usually still sits in gov's tree.

The fact that separates them is what the CURRENT role's disposition does in this run.
`UPDATE_ROLE["project-owned"]` and `UPDATE_ROLE["generated"]` are `skip`, so standing back really
does leave the file alone. `UPDATE_ROLE["rendered"]` is `adopter`, and `WRITING_DISPOSITIONS`'s own
header already says why that one is different: the kit's declared argv "writes under its own
authority, keyed on the kit rather than on a receipt row". Standing back does not stop that argv. It
only removes gov's half of the same run — the half that reconciles the operator's edit and refuses
when it cannot.

The regenerate runs for every kit in `touched_kits`, which is the kits holding an acted row or a
landed source. A row that stands back contributes neither, but in the transition this unit is about
the same vintage introduces the template as an unclaimed source, and that landing is what puts the
kit in the set. So the two halves are reliably in one run for exactly the case where the row is
skipped.

rev-2, MEASURED against the fixture rather than reasoned: the template does NOT put the kit in that
set. It arrives as the `rendered` rule's own source, which is neither an acted row nor a landed one,
and a fixture carrying nothing else built at HEAD ran no regenerate at all — so the row stood back
AND the argv stayed silent, and the byte loss the goal describes never happened. What actually puts
the kit in the set is any OTHER row of it that this vintage moves, which is the real shape: a
vintage that re-roles one destination is a release that changes the kit. The permanent arm moves a
second row of the same kit for exactly that reason, so it grades this unit's branch rather than the
accident of which rows happened to act.

### What a row that does not stand back does

It falls through to the disposition of the role it landed under. Routing it to the NEW role's
disposition instead would lose the conflict just as surely: the write loop caps `adopter` at report,
turning `diverged` and `stale` into `re-rendered`, so such a row writes nothing and names nothing.
The recorded disposition is also the one whose inputs still resolve — the row's `commit`, `source`
and `gov_oid` are what the three-way and the runbook's restore block both read.

### The nine arms, and which of them this unit makes green

Nine `[-PV]` arms went red on `b52b5d80`, measured by reverting that commit alone in a throwaway
clone (2026-09-18, node c, PINNED): 68 red at HEAD, 59 with the two predicates reverted, zero new.
They are one `F1 PRECONDITION`, one `R3-3 PRECONDITION`, three `R2-6`, three `R3-9` and one `W4`.

Seven are the runbook losing its conflict path. Block 1's `update` no longer names a conflict, so
block 2 prints `STOP: block 1's last update named no three-way conflict, so there is nothing to set
aside.`, block 1 commits instead of stopping, and the arm asserting the operator's bytes were kept
byte for byte in the git directory fails. The arm immediately after it — block 1 runs clean and
renders the harness — still PASSES, which is the measurement that makes this a byte-loss finding
rather than a reporting one.

Two assert the pre-migration state: that after `update` alone the index holds gov's own render. The
fixture header at `tools/govkit/selftest.py` predicted that pair would flip when the durable repair
landed, and that the migration would retire with them. This unit un-flips them. The prediction's
premise was that both halves arrive together, and a precondition asserting the state a live runbook
starts from has to hold for as long as that runbook ships. They flip in the unit that retires it.

One detail of that prediction was already wrong and is worth recording rather than repeating: of the
two arms literally labelled `F1 PRECONDITION`, only the INDEX one flipped. Its sibling asserts the
receipt row is still `engine`, and `role-moved` deliberately re-stamps nothing, so it stayed green at
HEAD. The second arm that actually flipped is the `R3-3 PRECONDITION`, which asserts the same
pre-migration state after a flag-off pull.

### Inventory

| identifier | kind | where |
|---|---|---|
| `KIT_WRITING_DISPOSITIONS` | module constant | `tools/govkit/govkit.py`, beside `WRITING_DISPOSITIONS` |
| `build_role_pair` | function | `tools/govkit/matrix.py` — rev-2 |
| `read_verdict` | function | `tools/govkit/matrix.py` — rev-2 |
| `run_in_gov` | function | `tools/govkit/matrix.py` — rev-2 |

rev-2: the engine mints no function, method or type, and the line that said so for the whole unit is
now wrong for the arm. The second fixture needs the same recipe as the first with three values
changed, so the three closures `check_role_move` already carried were HOISTED to module level and
take the difference as data — one fixture builder rather than two spellings of one. Each leads with
a declared verb (`build`, `read`, `run`). The lexicon's `py` cell grades function definitions and
type suffixes, so no declared cell grades the module constant above — stated rather than left as an
absence.

### Alternatives rejected

- **Test the role name (`now == "rendered"`) inline.** One line either way, and it spells a role
  where the reason is a disposition. `selfcheck` cannot grade an inline literal, and a second role
  routed to `adopter` would silently not follow.
- **Test whether the row's `source` is in the resolution's `carved` set.** It separates the measured
  pair correctly and for the wrong reason: a move to `merged` carves nothing, so an `engine` row whose
  descriptor now claims a region of a target-owned file would take the whole-file table.
- **Compare all three answers and refuse on any disagreement.** That cannot tell a transition from a
  tamper, which is the defect `DEPL-cMendedVintage-22` closed one function over.
- **Leave the branch and repair the runbook to stop expecting a conflict.** The conflict is how a
  local edit is detected at all. Removing it leaves the regenerate overwriting edits quietly, which
  is the state HEAD is in.

### Files touched (estimate)

| Path | Change |
|---|---|
| `tools/govkit/govkit.py` | the declared set, the gated branch, the note, the arm 7g assertion |
| `tools/govkit/matrix.py` | the `rendered` pair beside the `project-owned` pair |
| `WIRE-INTO-PROJECT.md` | the two corrected paragraphs |

## 5. Production-readiness checklist

- security — this restores a write path, and the honest framing is which write is worse. At HEAD gov
  declines to reconcile and its own regenerate overwrites the file anyway, unreported; after this gov
  reconciles first and refuses when it cannot. The argv that does the overwriting is gov's in both
  cases, so the trust boundary does not move.
- perf / scale — one `UPDATE_ROLE` lookup per moved row, over a dict already in memory. The
  resolution itself is unchanged and stays memoised per kit.
- error / empty / loading states — a row whose kit is absent from `descs` is untouched; a destination
  the descriptor resolves under no rule leaves `now` as None and keeps today's path. A kit that
  DECLINES its regenerate still falls through, deliberately: whether the argv runs depends on
  `GOVKIT_RERENDER` and on the kit's own decline, and gating a row's disposition on an environment
  variable would make the same receipt grade two ways on one tree.
- observability — one note line per fall-through row naming both roles and the path, off the row
  channel. The `role-moved` tally and its summary paragraph keep counting only rows that stood back,
  so the sentence "NOTHING was written for them" stays true of everything it counts.
- risks — the sharp one is arrival. An adopter who ran `update --write` between `b52b5d80` and this
  landing may have committed a render over a local edit with nothing in the run naming it; the fix
  cannot recover that and the release note is where it belongs. Second: a reader who finds the fixture
  header's prediction unfulfilled needs the paragraph above to know it was un-flipped on purpose.
- testing — AC1 to AC5 over scratch fixtures. The nine `[-PV]` arms are already RED at HEAD, so this
  unit's failing case was observed before the fix existed rather than staged after it.
- migration — none for a healthy target. A target already carrying a moved row sees a reconciliation
  on its next `update` where the previous one reported and skipped.
- user docs — S6's two paragraphs. The Maintenance section is currently unconditional and would be
  wrong for every row this unit changes.

## 6. Acceptance criteria

- **AC1** — When a scratch fixture holds a schema-3 receipt rowing a destination `engine` under a kit
  that declares a regenerate, gov's descriptor now resolves that destination `rendered`, and the
  target's own copy carries an edit that conflicts with gov's bytes at the new vintage,
  `python tools/govkit/govkit.py update --target <fixture> --write`
  refuses naming that path and the three-way conflict, writes one conflict order for it, and leaves
  the target's own bytes standing in the git directory for that path.
  Red when: the row still short-circuits at the branch, in which case the run exits 0, reports the
  move, and the kit's regenerate writes gov's render over the edit — the shipped defect, reproducible
  at HEAD before the change.
  fixture: a scratch fixture target under the run's scratch root; this repo keeps no `install.json`
  and can host no criterion in this section.
  rev-2: the criterion used to end "and the file on disk is the target's own", which CANNOT hold and
  is not what this unit buys. Measured on the fixture at both vintages: the kit's declared regenerate
  runs after the row is graded and puts its render in the WORKTREE either way, so that clause is
  green before the fix and green after it. What the fix moves is the git directory and the run's
  own account of itself — gov writes nothing for a conflicted row, so the index entry is untouched,
  and the run refuses, names the path and leaves an order where before it exited 0 saying nothing.
  The worktree overwrite is the standing ceiling this unit's third non-goal declines to close, and
  the permanent arm asserts it as a ceiling rather than leaving it unstated.
- **AC2** — When the same fixture is built with no local edit,
  `python tools/govkit/govkit.py update --target <fixture> --write`
  takes the recorded role's raw write for that row and the target's INDEX holds gov's bytes for it
  afterwards.
  Red when: the fall-through is gated on a conflict having been found rather than on the role move,
  so an unedited row still stands back and the migration's block 1 stages nothing for it.
- **AC3** — When the AC2 run of
  `python tools/govkit/govkit.py update --target <fixture> --write`
  finishes, exactly one printed line both opens with two spaces and ends
  with that row's path, and a further line names the role the row landed under, the role gov declares
  now and the path.
  Red when: the move is reported as a second row line, which shadows the row's own verdict for every
  reader keying on the path suffix — `read_verdict` returns the FIRST such line, and one suite arm
  asserts a single match.
  rev-2: the criterion named its own observation only as "the AC2 run" and carried one backticked
  token, the READER it protects, so nothing joined it to the command that makes the observation.
  The command is now written into it.
- **AC4** — When the existing aged fixture whose destination moved to `project-owned` is updated,
  the moved row still reports `role-moved`, gov does not put its bytes back at the destination the
  adopter emptied, and not one field of that receipt row is rewritten.
  Red when: the gate is written over role NAMES and admits every move except the one that fixture
  spells, so `generated` — whose disposition is also `skip` — falls through and gov writes over a
  file its own rule says it never supplies.
- **AC5** — When a member of the new declared set is staged to a value `UPDATE_ROLE` maps no role to,
  `python tools/govkit/govkit.py selfcheck`
  names that member and exits non-zero; unstaged, it exits 0.
  Red when: the assertion is written over the shipped value only, so a typo empties the set, every
  moved row stands back again and the whole of S1 becomes unreachable in silence.

## 7. Gates

`govkit selftest` · `govkit selfcheck` · `govkit refusal join` · `govkit acceptance matrix`

New arm: `tools/govkit/matrix.py` · an aged schema-3 receipt whose `engine` row's descriptor now
resolves `rendered` under a kit declaring a regenerate, asserted to reach the table · no floor moves.

New arm: `tools/govkit/selftest.py` · nothing staged — the nine `[-PV]` arms this unit turns green
are RED at HEAD and were measured red before the fix was designed · no floor moves.

The `BRANCH_PIN` floor in `tools/govkit/refusal_join.py` is re-derived only if the branch count moves.
This unit adds a note and a gate on an existing branch and adds no refusal, so it does not move.

## 8. Open questions

- **Q1 — should this unit also retire the harness migration, honouring the fixture header's
  prediction?** The two preconditions would then flip as written and the seven runbook arms would be
  deleted rather than repaired. RECOMMENDATION: no. Those 104 arms are the only end-to-end exercise
  of a `--kits`-scoped `update` through a consumer's hooks, and 103 of them were green at BASE
  (PINNED, 2026-09-18, node c). Retiring the runbook is `DEPL-dPolishedVitrine-1`'s remaining clause
  and owes a replacement for that coverage before it lands.
  RESOLVED (agent, 2026-09-19, delegated): no. The recommendation is taken as written and the
  migration ships. The build measured the consequence rather than assuming it: the two `PRECONDITION`
  arms are un-flipped along with the seven, because a precondition asserting the state a live runbook
  starts from must hold for as long as that runbook ships, and the fixture header's prediction had
  both halves arriving together.
- **FACT-QUESTION · Q2 — does any shipped descriptor move a destination from a landable role to one
  whose disposition is `block`?** A scan of the registry's descriptors against each adopter receipt
  decides it. RECOMMENDATION: leave the disposition test as specified, which handles such a move by
  standing back, and file the handling as a follow-up if the scan finds an instance. The test's
  answer for that pair is deliberate rather than accidental, and the scan only says whether anyone
  is living with it.
  RESOLVED (agent, 2026-09-19, delegated): leave the test as specified, and the probe is NOT run
  here rather than run and reported. It is defined against adopter receipts, and this repository
  holds none — a scan of gov's descriptors alone answers a different question and would report a
  reassuring zero for a population it never had. It runs in an adopter tree or not at all.

## 9. Revision log

- rev-1 · 2026-09-18 · initial draft, authored from a read-only attribution that ran the suite at
  BASE in a throwaway clone and reverted `b52b5d80` surgically.
- rev-2 · 2026-09-19 · built. Three corrections, each measured on the scratch fixtures rather than
  reasoned. AC1's closing clause asked for a worktree state the kit's own regenerate makes
  impossible at BOTH vintages, so it was rewritten onto the git directory, the refusal and the
  order — the three things the fix actually moves — with the worktree overwrite recorded as the
  standing ceiling the third non-goal already declines to close. Section 4's `touched_kits`
  paragraph named the template as what puts the kit in the run's touched set; it does not, and a
  fixture built on that claim ran no regenerate at all, so the paragraph now names the other moved
  row and the arm moves one. The inventory's "no function is minted" became false when the second
  fixture needed the first's recipe: three closures were hoisted to module level and are listed.

## 10. Reuse audit

`python tools/codebase-map/reuse_lookup.py "keep a receipt row on its recorded disposition when the descriptor moved its destination to a role whose own machinery still writes it"`
returns NO EXISTING SEAM FITS: its ranked rows are name-token neighbours on `write`, `row` and
`record`, and the two govkit symbols among them — `classify_row` and `raw_write_cells`, both at
fan-in 1 — are consumers of the decision this unit gates rather than the decision itself. The seam is
in the file already: `UPDATE_ROLE` is the declaration that answers "what does this role's disposition
do", and `WRITING_DISPOSITIONS` is the precedent for reading that table as a SET rather than per role,
declared beside it and asserted by `selfcheck` arm 7g. S4 adds a second member of that pattern rather
than a mechanism, which is why this is a gate change and not a new resolution path.

The recall probe returned the record that owns the gap: `DEPL-dPolishedVitrine-1`, OPEN in
`memory/backlog/DEPL.md`, whose three clauses are the re-resolution, the pinned re-adopt and `adopt`'s
evidence — and `TOOL-dPolishedVitrine-12`, which records that F1 was repaired by the migration rather
than by a role move, which is the coverage Q1 refuses to spend.

Recall terms used: `--terms "govkit update role re-resolution role-moved rendered engine three-way
merge migration receipt schema descriptor disposition"`, with the question "what decided that update
re-resolves a receipt row's role and what owns the vintage migration's three-way conflict path".
