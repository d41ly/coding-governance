# TOOL-aDeclaredCeiling-3 — a landed run's frozen region stops being compared to a moving source

**Status:** CLOSED · rev-3 · 2026-08-16 · node a · Tier-2 · base 96141aed · streams tooling

## 1. Goal

`check-unattended` check 8 compares every run-state file's generated region against the build
README slice it was copied from. For a LIVE run that is exactly right: the copy is a cache and a
divergence means someone hand-edited a generated artifact. For a TERMINAL run it is wrong, because
the README legitimately keeps moving after the run ends and the driver — correctly — refuses to
rewrite a finished record. Scope the comparison to non-terminal runs so a landed record stops being
graded against a document it can no longer track.

## 2. Scope (IN)

- **S1 — check 8 skips terminal runs.** `tools/unattended/check-unattended.sh`'s check-8 loop reads
  each run-state file's `phase` and compares the region only when that phase is non-terminal. The
  terminal members are the kit's own `LANDED` and `ABORTED`; they are read from the same place every
  other check reads the vocabulary, never re-spelled in the loop.
- **S2 — the skip is OBSERVABLE, and it is not a print.** `check-unattended.sh`'s own header states
  the contract: "Exit 0 + no output = clean. Anything printed is a violation." A per-file skip line
  would break that on every clean run — both real run-state files in this tree are `LANDED`, so the
  gate would print two lines and exit 0 from the day this lands, which is precisely the ambiguity
  the contract exists to remove. The skip is therefore SILENT in the gate, and its observability is
  S4's arms: a terminal file whose region drifts is proved skipped by a fixture, not by a message.
  Stated at length because "a silent skip is indistinguishable from nothing to check" is a real
  objection and the answer is that the distinguishing evidence belongs in the harness, not in the
  output of a gate whose contract is silence.
- **S3 — the protocol says so.** `memory/guides/UNATTENDED-PROTOCOL.md` §2 describes the generated
  region as byte-compared against a fresh render with no phase qualification. It gains the
  qualification and the reason: at a terminal phase the region is a HISTORICAL SNAPSHOT of what the
  build looked like when it landed, and the build README is a live document.
- **S4 — the arms.** `tools/unattended/check-unattended.test.sh` gains two: a NON-terminal run whose
  region drifts still reds (the check did not become vacuous), and a TERMINAL run whose region
  drifts is skipped with its line printed. Both are fixtures, not assertions about the source.
- **S5 — the kit/dogfood parity.** The shipped `tools/unattended/PROTOCOL.template.md` and the
  installed `memory/guides/UNATTENDED-PROTOCOL.md` are gate-compared, so S3's edit lands in both or
  the parity leg reds. **The shipped file is `PROTOCOL.template.md`** — the `UNATTENDED-` prefix is
  the INSTALLED name only, and a first draft of this item spelled a path that does not exist.

## 3. Non-goals (OUT)

- **Changing what `ids:` means.** `gen_build_index.py:16` states plainly that `ids` is an OUTPUT
  derived from every id carrying the slug, and `:261-266` records that admitting sub-ids once
  multiplied a roster from 8 to 38. That design is deliberate and correct; the defect is not that
  the README moves, it is that a frozen copy is graded against it forever.
- **A driver verb that refreshes a terminal record.** Considered and rejected in §4 — it is the
  option that reopens a finished record, which is the one thing the protocol's own check 26 exists
  to prevent.
- **The other checks in the same loop.** There is ONE per-run-state-file loop and seven distinct
  `fail` ordinals inside it — an earlier draft of this bullet said three, which both undercounts
  them and invites an implementation that scopes the LOOP instead of the CHECK. **S1 gates check 8
  and nothing else**: the phase read must not become a `continue` for the whole iteration, or six
  other checks silently stop running on every terminal file. Widening this unit to "audit every
  check for terminality" is a different mechanism and would make the diff unreviewable.

## 4. Design

### The failure, reproduced

`aSiftedPlaybook` landed, then minted a backlog row under its own slug to discharge a
landing-time obligation. `gen_build_index` re-derived the build README's `ids:` from the new row,
rewriting both the front matter and the generated region. `RUN.md`'s copy of that region no longer
matched, and:

- `check-unattended` check 8 redded, which redded the merge bar;
- `--preflight`, the only verb that re-splices the region, refused with check 26 — "the run is
  already finished and a finished record is not something to move, re-open or re-pin".

There is no legitimate way out of that state. The row had to be reverted, and the follow-up it
recorded was surfaced in prose instead. That is a gate making correct records impossible.

### Why the fix goes here and not in the driver

Three options were considered against the tree:

1. **A `--refresh` verb for terminal runs.** Rejected: check 26 refuses to move a finished record
   precisely because "every later run is measured against the counter this record left". A verb that
   rewrites a landed record's bytes is that move wearing a different name, and it would need its own
   exception in the one check built to have none.
2. **Stop deriving `ids` from backlog rows.** Rejected as a non-goal above — `ids` is documented as
   an output and the derivation is load-bearing for live builds.
3. **Scope check 8 to non-terminal runs.** Taken. It is the only option where nothing that is
   currently true stops being true: a live run's region is still byte-compared, and a landed run's
   region keeps saying what the build looked like at landing, which is what a historical record is
   for.

### The terminal set is read, never re-spelled

The driver already owns the vocabulary and the gate already reads it. Re-typing `LANDED|ABORTED`
inside the loop would be a second spelling of a set the kit declares once, which is the
`two-answers-to-one-question` class this repo gates elsewhere. The check reads the terminal members
from the same source the rest of the file does.

### Files touched

| File | Change |
|---|---|
| `tools/unattended/check-unattended.sh` | check 8 gains the phase scope + the skip line |
| `tools/unattended/check-unattended.test.sh` | two arms (S4) |
| `.memory-tree.conf` | `ARMS_FLOORS` — AC6 requires the pair to equal the measured value; the pin is one-sided, so a floor left stale passes |
| `memory/guides/UNATTENDED-PROTOCOL.md` | §2's qualification (S3) |
| `tools/unattended/PROTOCOL.template.md` | the same edit, or the parity leg reds (S5) |

No depth-1 `tools/` path is created, so no `govkit/registry.toml` row is owed. Stated rather than
omitted, because the build-level rule requires every unit to answer that question.

### Rollout

One commit. The gate change and its arms cannot land separately: an unarmed new branch reds
`check-arms`, and an arm for a branch that does not exist cannot pass.

## 5. Production-readiness checklist

- security — N/A. A gate reads more state and writes none.
- perf / scale — N/A. One extra `phase` read per run-state file, of which the tree has few.
- a11y / i18n — N/A.
- error / empty / loading states — a run-state file with NO readable phase is the interesting empty
  case, and it is already handled: check 4 refuses it and `continue`s before check 8 sees it, so
  "unreadable" cannot be mistaken for "finished" by construction. S1 must not weaken that — a
  phase read that treats an unreadable phase as terminal would turn a refusal into a skip. AC4
  observes the refusal where it lives.
- observability — deliberately NOT in the gate's output, per S2. The gate's contract is that a clean
  run is silent, and a skip line would make every clean run in this tree non-silent. The evidence
  that the skip is real lives in S4's arms.
- risks — **the real risk is scoping the check into vacuity, and it is live rather than
  hypothetical**: both run-state files in this tree are already `LANDED`, so on the day this lands
  check 8 compares NOTHING. The check is correct and exercises nothing, which is the
  `fixture-passes-by-finding-nothing` class. It is answered by AC1 — a non-terminal file whose
  region drifts must still red — which is the only criterion here that proves the check still has
  teeth, and it is why that AC is first.
- testing + left-shift gates — S4 is the left-shift, and its first arm exists to prove the check did
  not become vacuous rather than to prove the new behaviour.
- migration / rollback — revert the commit; no state format changes and no record is rewritten.
- user docs — S3, and the Skill render is unaffected because it does not describe check 8.

## 6. Acceptance criteria

- **AC1** — When a run-state file at a NON-terminal phase has its generated region altered by hand,
  `bash tools/unattended/check-unattended.sh` reds naming check 8 and that file. The check is not
  vacuous.
- **AC2** — When a run-state file at `LANDED` has its generated region altered, the gate exits 0 and
  prints NOTHING, honouring its own "anything printed is a violation" contract.
- **AC3** — Same as AC2 for `ABORTED`, because the terminal set has two members and an arm for one
  of them proves nothing about the other.
- **AC4** — When a run-state file carries no readable `phase`, `bash tools/unattended/check-unattended.sh`
  reds at **check 4**, not check 8. **This replaces a criterion that could never pass.** The draft
  required the region to be COMPARED for a phase-less file, on the reasoning that "unreadable is
  not terminal". Measured: check 4 already refuses a file with no phase and `continue`s to the next
  file, so such a file never reaches check 8 today and S1 does not change that. The property the
  draft wanted is real and is enforced UPSTREAM — a phase-less file is refused outright rather than
  quietly skipped — so this AC observes where it actually lives.
- **AC5** — When `bash tools/unattended/check-unattended.test.sh` runs it exits 0; inverting any
  single arm's expectation reds naming that arm.
- **AC6** — When `python tools/memory-tree/check-arms.py --report` runs, every new `fail` branch in
  `check-unattended.sh` is ARMED and the `ARMS_FLOORS` pair in `.memory-tree.conf` equals the
  measured `<branches>:<armed>`. An undeclared floor is silently skipped, not refused, so this AC
  reads the report rather than trusting the gate to complain.
- **AC7** — When `bash tools/unattended/adopt-unattended.sh --check` runs it exits 0: the shipped
  template and the installed protocol AGREE.
- **AC7b** — When the INSTALLED `memory/guides/UNATTENDED-PROTOCOL.md` §2 is read, it states that
  the generated region is compared only while the run is non-terminal, and why. **AC7 cannot
  substitute:** `adopt-unattended.sh --check` is a symmetric diff of template against render, so it
  proves the two agree and is blind to both being stale. An edit made in neither file passes AC7.
- **AC8** — **The reproduction is closed, end to end.** With `aSiftedPlaybook`'s run-state file at
  `LANDED`, a backlog row carrying the slug `aSiftedPlaybook` is minted, `gen_build_index --write` is
  run, and `bash tools/run-gates.sh` is GREEN. This is the exact sequence that had no legitimate
  exit before this unit, and it is the only criterion here that observes the original defect rather
  than the mechanism chosen to fix it. **The row is reverted afterwards** — the criterion is that
  the bar stays green, not that the row lands.
- **AC9** — When `bash tools/run-gates.sh` runs, it is green.

## 7. Gates

- `bash tools/unattended/check-unattended.sh` — the subject.
- `bash tools/unattended/check-unattended.test.sh` — its arms.
- `bash tools/unattended/unattended.test.sh` — the driver is untouched; run it to confirm that.
- `python tools/memory-tree/check-arms.py` — new `fail` branches enter its population.
- `bash tools/unattended/adopt-unattended.sh --check` — protocol parity.
- `bash tools/memory-tree/check-memory-hygiene.sh`, `python tools/memory-tree/gotchas.py --for-diff`.
- `bash tools/run-gates.sh` at the push boundary.

## 8. Open questions

none.

## 9. Revision log

- rev-3 · 2026-08-16 · **S1's MECHANISM is SUPERSEDED, and the better solution is not mine.**
  `dClosedLexicon` r2 landed on main while this build ran and removed the COPY entirely: the
  run-state file's generated region is now EMPTY by contract and the unit list is derived from
  the build README on every read. That is the same invariant with the failure mode designed out
  rather than scoped around — this unit made a stale copy legal at terminal phases; theirs makes
  a stale copy impossible at any phase. Taken at the reconcile, and S1's four arms retired with
  their reason recorded in the self-test.

  **What this unit still contributed, and it is not nothing.** The defect was FOUND here, by
  hitting it during `aSiftedPlaybook`'s landing and recording it as a row rather than working
  around it; and the fix for `GIT_GRAFT_FILE` leaking from the driver into its own selftest
  stands on its own — that one was found by `--close` blocking on a bar that was green, and
  nothing in the superseding change touches it.
- rev-2 · 2026-08-16 · folded the round-1 spec audit. **B3**: AC4 required a phase-less run-state
  file to reach check 8; check 4 refuses one and `continue`s, so it never does and the criterion
  could not pass. It now observes the refusal where it lives, and §5's error-states bullet with it.
  **H5**: AC7 inferred that a symmetric `--check` diff proves an edit landed — it proves the two
  copies agree and is blind to both being stale; **AC7b** reads the installed protocol. **H8**:
  S2's per-file skip line falsifies the gate's own "anything printed is a violation" contract on
  every clean run, both real run-state files being LANDED. The skip is silent and S4's arms are the
  evidence. **M2**: the shipped template is `PROTOCOL.template.md`; the draft named a path that
  does not exist. **M3**: seven `fail` ordinals share one loop, not three, and S1 must scope the
  CHECK rather than the iteration or six other checks stop running on terminal files. **M1**:
  `.memory-tree.conf` added to Files touched. The vacuity risk is restated as live rather than
  hypothetical: both files here are already terminal, so AC1 is the only thing proving teeth.
- rev-1 · 2026-08-16 · initial draft. The defect was found by hitting it during `aSiftedPlaybook`'s
  landing rather than by review: a landing-time obligation the build had recorded for itself could
  not be discharged without redding the bar. Three fixes were weighed against the tree and the two
  rejected ones are recorded in §4 with the reason, because "scope the check" reads like the obvious
  answer only after the other two are known to be worse.

## 10. Reuse audit

`python tools/codebase-map/reuse_lookup.py "declared byte budget pin justified beside its value"`
returned `tools/memory-tree/gotchas.py:declares` (fan-in 5, SEAM) and the `unattended` dossier's
`.unattended.conf` affordance seam. Neither is the seam this unit extends: **the seam here is
`check-unattended.sh`'s own per-run loop**, which already reads each run-state file's facts, so the
phase this unit needs is a field the loop is positioned to read rather than a new traversal.

`python tools/memory-recall/query.py "why is a repo constraint declared in a conf file rather than
hardcoded in the gate that enforces it" --terms "declared pin conf ceiling budget shrink-only floor
ratchet constant gate justification movement recorded"` returned 40 hits, top of which are this
build's own freshly-minted rows and `memory/map/features/playbook.md:81`. **It did NOT return
`READ_PATH_CEILING` itself** — which is the subject of `TOOL-aDeclaredCeiling-2` and is quoted here
as live evidence for that unit rather than as a miss for this one.

The prior art that DOES bind this unit is protocol §9's own reasoning about what a check running
under the run's own uid can and cannot buy: it is the section that establishes the kit's habit of
naming what a check does NOT cover, which S2's skip line and §5's vacuity risk both follow.
