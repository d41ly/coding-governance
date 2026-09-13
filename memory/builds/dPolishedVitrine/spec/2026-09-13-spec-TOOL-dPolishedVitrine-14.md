# TOOL-dPolishedVitrine-14 — brief-recorded grades only the units built while a run was live

**Status:** INPROGRESS · rev-3 · 2026-09-13 · node d · Tier-2 · base 09a22d2b · streams tooling · ratified 2026-09-13

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-09-13-build-TOOL-dPolishedVitrine-14-1-journal.md](../build/2026-09-13-build-TOOL-dPolishedVitrine-14-1-journal.md) | journal | — |
| [2026-09-13-prompt-TOOL-dPolishedVitrine-14-0-owner-ruling.md](../prompts/2026-09-13-prompt-TOOL-dPolishedVitrine-14-0-owner-ruling.md) | journal | — |
| [2026-09-13-review-TOOL-dPolishedVitrine-1-diff-review-round3.md](../reviews/2026-09-13-review-TOOL-dPolishedVitrine-1-diff-review-round3.md) | diff-review | TOOL-dPolishedVitrine-1 |

<!-- /gen:spec-records -->

## 1. Goal

The `brief-recorded` leg reds every CLOSED unit in a build whose run-state file pins a BASE. That
includes a unit built by hand after the build's unattended run had already finished, which is how
NicoCares' `PKG-dPolishedVitrine-14` went red. A brief is what a run hands the agent that builds a
unit, so a unit built outside any run owed none. By the owner's ruling of 2026-09-13, this unit takes
such a unit out of the graded population, ANNOUNCED, and grades every unit built during a run
exactly as before.

## 2. Scope (IN)

- **S1** — `tools/unattended/check-brief-recorded.sh` reads the run-state file's phase at each graded
  unit's build commit. A phase in the driver's `PHASES_TERMINAL` there takes the unit out of the
  graded population. The skip is announced on stdout with the unit id, the build commit, the phase
  and the reason, and it is counted on the liveness line. Observed by AC1, AC2, AC3, AC4, AC13 and
  AC14.
- **S2** — the skip is honoured only while HEAD still carries a record making the same claim, meaning
  the same base, phase and witness. That record is the run-state file itself, or a retired
  `RUN.<phase>.<8hex>.md` that was not yet tracked at the build commit. A claim HEAD does not bear
  out is announced, counted, and the unit is graded exactly as before. Observed by AC5, AC6 and AC7.
- **S3** — the terminal set is READ from the driver's declaration, and a set the leg cannot read as
  phase tokens is a DEAD PROBE refusal. Observed by AC8.
- **S4** — the leg's header states the predicate, its boundary, the corroboration, the rejected
  alternative, and the two things it still does not check. Observed by AC9.
- **S5** — the arms, in `tools/unattended/check-brief-recorded.test.sh`. Each new arm is observed
  against the leg at `f1e58789`, and each guard arm against a staged break of its own guard. The
  suite's truncated-cache arm stops copying the cwd-relative `$LEG` and copies from `$KIT`, because
  a run against a staged copy of the kit graded the wrong leg there. Observed by AC10.
- **S6** — the protocol's `BRIEF_RECORDED_CUTOFF` row says which units are graded, and the conf
  example's description points at that row rather than restating it (rev-3). The shipped protocol
  template and this repo's installed copy move together. Observed by AC11 and AC16.
- **S7** — the change rides unattended 1.20, which this branch carries and `main` has not released,
  so no version carrier moves. Observed by AC12.
- **S8** — before a skip is honoured, the leg asks every later commit that `build_commit`'s own
  predicate accepts for the id the same phase question, and grades the unit at the first one made
  while a run was live, announced with both commits and counted on the liveness line (rev-3).
  Observed by AC15.

## 3. Non-goals (OUT)

- **`pass-order` is not changed.** The ruling waives its red in NicoCares, because spec-first is
  general discipline and that unit's spec and code went into one commit. The two legs share
  `build_commit` and nothing else. Each leg's population code is inline in its own file, so no line
  of `pass-order`'s moves, and §4 says how that is proven.
- **`lib-unattended.sh` is not changed.** `build_commit` selects the same commit it always did. The
  new predicate lives in the leg, because only this leg asks it.
- **NicoCares is not touched.** It re-pulls the kit and records its own waiver.
- **A forgery that stands at HEAD is not closed here.** A run that forges a terminal claim AND keeps
  it, or commits a retired record carrying one, leaves that record at HEAD. The kit gate grades
  HEAD's record there, and check 15 judges a LANDED witness. This leg buys the trace.
- **`graded` keeps counting before the build-commit selection.** The leg's header already records
  that as a hole it shares with `pass-order`, and moving the increment would change what the
  sibling's identically named count means. The post-run count joins `unbuilt-in-range` as a subset.
- **The suite stays off the bar.** It is on demand under the 2026-08-23 ruling, like every self-test
  in this kit.

### Edges

- **consumes-from** external — the driver's `PHASES_TERMINAL` declaration, its `fact` grammar and its
  retired-record naming. This leg reads all three and owns none of them. A driver that drops the
  declaration makes this leg refuse rather than grade.
- **hands-off** external — NicoCares re-pulls unattended 1.20 and waives its `pass-order` red for
  `PKG-dPolishedVitrine-14` in its own tree. That is the NicoCares half of the owner's ruling.

## 4. Design

### Data model

A record's CLAIM is three of its facts, in the driver's `fact` grammar: `base`, `phase` and
`witness`. The first line opening with the key and a colon wins, a trailing CR is dropped, leading
spaces are dropped, and nothing else is touched. One awk program reads a claim, and the leg runs the
same program on the build commit's record and on HEAD's, so the two are read the same way.

The claim is joined one value per line and closed with a dot. A value is one line of the record, so a
newline cannot occur inside one. The dot matters because command substitution strips trailing
newlines. Without it, a record carrying a base and nothing else would collapse to one line, and the
phase read would return the base. The first draft had that shape, and the `baseonly` arm pins it.

### The predicate and its boundary

The leg already reads the run-state file at the build commit for the brief row. It now reads the
phase from the same blob. That path names the record that was live, or had last finished, at that
commit. `--preflight` retires a finished record by renaming it and scaffolds the next run's record in
the SAME commit, so the path never names a stale run (`TOOL-dClosedLexicon-11` is the rotation's own
record).

A phase that is one uppercase token and a member of the driver's `PHASES_TERMINAL` means the run had
finished. Anything else is graded exactly as before, and that includes an absent file and a record
with no phase line. The one-token test means a value carrying a space cannot match two members of
the set at once.

The boundary is the commit that WRITES the terminal phase. A unit whose code rides in it is outside
the run, because `--landed`'s witness is a commit already on the remote, so the code in the commit
recording it is not in what landed. LANDING is the last live phase and is still graded.

### A wrongly picked build commit

The predicate above is only as good as the commit it is asked about. `build_commit` returns the
EARLIEST in-range commit that names the id as a whole token and touches a path outside the build
folder and the conf's exclusions, and a hand commit made between two runs qualifies. At that commit
the record still reads the first run's terminal phase. The second run's preflight retires that record
only afterwards, so a retired record at HEAD still bears the claim out, and the unit, built during
the second run while it was live, was skipped. Round 3 of the closing review reproduced that, and it
contradicts §1, which grades every unit built during a run.

So before a skip is honoured, the leg walks `build_c..HEAD` in order and asks every commit that
`build_commit`'s own predicate accepts for this id the same phase question. The subject cache
filters first, so the predicate runs only on a commit whose subject names the id, and the predicate
itself is the library's, called on that one commit, so there is no second copy of it. The first
commit made while a run was live, an absent or phase-less record included, is where the unit is
graded. The leg announces it with both commits and both phases and counts it on the liveness line.

This fails CLOSED. A later commit that names the id while a run is live grades the unit even when it
touched only a file the conf forgot to exclude, which at NicoCares, whose conf declares no exclusions,
includes a records commit. That is the pre-unit verdict for such a unit, and it is announced, so a
reader who looks sees why. `lib-unattended.sh` is not changed, so `pass-order` keeps its pick, and the
wrong pick there is older than this unit.

### The corroboration

The run authors the phase it commits. A record reading LANDED at one commit and BUILDING at the next
would otherwise buy a unit out of this leg with two hand edits that leave nothing at HEAD. No driver
verb can produce that history, because every phase writer refuses a finished record. But this leg
cannot assume the driver was the only writer.

So the skip is honoured only while HEAD still carries a record making the same claim. The first
place looked is HEAD's run-state file, whose claim is read once per build from the blob the leg
already holds. The second is every retired record at HEAD whose name has the driver's shape,
`RUN.<phase>.<8hex>.md`, provided that name was NOT tracked at the build commit. The absence test is
what stops a run copying the claim of a record retired BEFORE the unit was built.

The claim and not the bytes, because finished records ARE edited after they finish. A kit migration
added a halt code to six aborted records, two of them already retired, and a later merge fix did the
same to a seventh. None of those edits moved the claim. The retired record's name is not required to
match its own blob for the same reason: a migrated retired record keeps its name and changes its
bytes, so that equality is already false in this tree.

A claim HEAD does not bear out is announced as GRADED ANYWAY and counted, and the unit is graded
exactly as a live one. Both hand edits and forgeries land there, and a reader should see both.

### Retired records

The leg never reads a retired record for a brief row or a base, before this unit or after it. The
base still comes from HEAD's run-state file, so the range is the current run's. A retired record
takes part in exactly one question: whether a finished claim the build commit read still stands at
HEAD after a later run moved the record off the path.

### Why pass-order is untouched, and how that is proven

`build_commit` is the only shared code, and it is not edited. The population code, meaning the
cutoff, the base read, the CLOSED-unit selection and the liveness line, is written inline in each
leg. So `pass-order` cannot inherit the scoping. The proof has three parts. `git diff` over
`check-pass-order.sh` and `lib-unattended.sh` between `f1e58789` and this unit's commits is empty.
The `pass-order` suite passes unchanged. And the leg's stdout over the real tree is byte-identical
before and after.

### Inventory

No new function is defined in either file, so the lexicon's verb population does not move. The
leg gains the shell variables `TERMINAL_PHASES`, `CLAIM_AWK`, `postrun`, `unborne` and `announced`,
and rev-3 adds `regraded`, `_live_c` and `_live_ph`. No gate leg, file, kit or conf key is added.

### Rollout

The leg lands with a population this repo's tree does not exercise. At `f1e58789` its graded builds
hold no unit built under a finished record, so the bar's verdict and every existing count are
unchanged. Two zero counts join the liveness line. NicoCares' `PKG-dPolishedVitrine-14` is the first
real population, and it arrives when NicoCares re-pulls the kit.

### Files touched (estimate)

- `tools/unattended/check-brief-recorded.sh` — the predicate, the corroboration, the terminal set
  read, the two counts and the header.
- `tools/unattended/check-brief-recorded.test.sh` — ten fixture modes, their arms, and the `$KIT` copy.
- `tools/unattended/PROTOCOL.template.md` and `memory/guides/UNATTENDED-PROTOCOL.md` — one sentence
  in the `BRIEF_RECORDED_CUTOFF` row, which rev-3 extends by the later-commit condition.
- `tools/unattended/.unattended.conf.example` — the key's description, which rev-3 turns into a
  pointer at that row.

### Alternatives rejected

- **Reachability from the terminal witness.** It needs the phase at the build commit anyway, to know
  which record's witness to read. It has no answer for an aborted run whose witness is not a sha,
  which the protocol permits. And against the two-edit forgery it adds nothing, because the witness
  at the build commit is written in the same edit as the phase.
- **The phase alone, with no corroboration.** It makes the cheapest possible bypass of this leg two
  hand edits that leave nothing at HEAD. The leg's own header already records that a check reading
  a value its subject authors reads the subject's answer.
- **Byte equality with HEAD's record.** Measured over the real tree, it bears out 8 of the 25 units
  built under a finished record. A kit migration edited the other 17 records and moved no claim.
- **A walk of the record's history after the build commit.** It would catch a record reopened in
  place, but it has to reason about merge topology. A topological-order walk over the real tree
  reported three reopenings that are only interleaved branches, and every real parent-to-child edge
  out of a terminal phase turned out to be a rotation. The claim comparison needs no topology.
- **A shared predicate in `lib-unattended.sh`.** Only this leg asks the question. Putting it in the
  library would make `pass-order` source a changed file for nothing and turn a trivially proven
  byte-identity into a behavioural one.

## 5. Production-readiness checklist

- security — the leg reads the driver's declaration by parsing it, never by sourcing it. A value
  admitted to a `case` pattern is shape-checked to uppercase tokens first. The corroboration closes
  the cheapest forgery, and §3 names the one it does not close.
- perf / scale — one awk per graded unit with a build commit, and one per build. A finished claim
  that HEAD's record does not match costs one `ls-tree` per retired record at HEAD. Over the real
  tree the leg's wall moved from 14 s to 16 s. Rev-3's walk runs only for a unit whose build commit
  read a terminal phase: one `rev-list` over the commits after it, and the library's predicate only
  on a commit whose cached subject names the id.
- error / empty / loading states — an unreadable terminal set refuses. An absent record, an absent
  phase and a malformed phase are graded as live, which is the pre-unit verdict.
- observability — every skipped unit and every unborne claim gets its own line naming the unit, the
  build commit, the phase and the record path. Both populations are counted on the liveness line.
- risks — a future driver verb that edits a finished record's base, phase or witness would make a
  legitimate post-run unit read as unborne and red. None does today, because every phase writer
  refuses a finished record, and the arm for a migrated record pins the fields that may move.
- testing — ten fixture modes. The post-run, flip, rotated and migrated arms were red against the
  leg at `f1e58789`. The forgery, absence-test, terminator and claim-not-bytes arms were each red
  against a staged break of their own guard.
- migration — none. No record is rewritten and no conf key is added.
- user docs — N/A as a `help/` tree, which this repo does not ship. The protocol row and the conf
  example are the operator-facing text, and S6 updates both.

## 6. Acceptance criteria

- **AC1** — When `tools/unattended/check-brief-recorded.test.sh` builds a fixture whose record reads
  LANDED before a unit is built with no brief, the leg exits 0. It prints `NOT GRADED` naming the
  unit, the phase and the record that still makes the claim, and its liveness line counts one unit
  built after its run finished.
  Red when: the unit is graded, the skip prints nothing, or the count stays at zero.
- **AC2** — When the same suite builds the fixture under an ABORTED record, the leg exits 0 and
  names the phase. When `PHASES_TERMINAL` in the fixture's driver is staged down to LANDED alone,
  the same history exits 1 with the ordinary `NO brief row` violation.
  Red when: the staged driver leaves the verdict at 0, which would mean the leg spells the set itself.
- **AC3** — When the suite builds fixtures whose records read BUILDING and LANDING at the build
  commit, both exit 1 with `NO brief row`, and neither prints `NOT GRADED`.
  Red when: a unit built during the run, or under its last live phase, is skipped.
- **AC4** — When the suite's `flip` fixture's build commit itself writes LANDED, the leg exits 0 and
  prints `NOT GRADED` for the unit.
  Red when: the boundary commit is graded.
- **AC5** — When the suite's `rotated` fixture retires the finished record through a second run's
  preflight after the unit is built, the leg exits 0 and names the retired `RUN.ABORTED.` record as
  the one that still makes the claim.
  Red when: a rotation reads as a forgery and the unit is graded.
- **AC6** — When the suite's `reopened` fixture writes LANDED at the build commit and BUILDING one
  commit later, the leg exits 1 with `NO brief row` and prints `GRADED ANYWAY` for the unit. When
  the `copied` fixture forges the claim of a record retired before the build commit, the leg exits 1
  and prints `GRADED ANYWAY`.
  Red when: the corroboration is removed, or the absence test is. Each is a staged break in the
  journal.
- **AC7** — When the suite's `migrated` fixture adds a halt code to the finished record after the
  build commit, the leg exits 0 and prints `NOT GRADED`.
  Red when: the comparison is made on the record's bytes rather than its claim.
- **AC8** — When the fixture driver's `PHASES_TERMINAL` line is deleted, or carries a lowercase
  member, the leg exits 2 with `DEAD PROBE` and prints no liveness line.
  Red when: a set the leg cannot read is treated as empty and every unit is graded as live.
- **AC9** — When `tools/unattended/check-brief-recorded.sh` is read, its header names the predicate,
  the boundary, the corroboration, the rejected reachability predicate and both new things it does not
  check, and it points at the owner's 2026-09-13 ruling in build `dPolishedVitrine`. It does not cite
  this unit's id while this spec is live; `tools/unattended/check-brief-recorded.test.sh` does.
  Red when: a reader has to open this spec to learn why a unit went ungraded.
- **AC10** — When `tools/unattended/check-brief-recorded.test.sh` runs from a directory other than
  the repository root, and when it runs against a staged copy of the kit, every arm grades the leg
  beside the suite, and the whole suite exits 0 against this unit's leg.
  Red when: the truncated-cache arm copies a leg from the invoking directory.
- **AC11** — When `tools/unattended/check-unattended.sh` runs, its protocol parity check passes over
  `tools/unattended/PROTOCOL.template.md` and `memory/guides/UNATTENDED-PROTOCOL.md`, and both carry
  the new sentence in the `BRIEF_RECORDED_CUTOFF` row.
  Red when: one copy moves without the other.
- **AC12** — When `tools/check-kit-versions.sh` runs, it exits 0 with every unattended carrier still
  at 1.20.
  Red when: a carrier moves, or the leg's marker disagrees with the driver's.
- **AC13** — When `tools/unattended/check-pass-order.sh` runs over this repo before and after the
  unit, its stdout is byte-identical, and `tools/unattended/check-pass-order.test.sh` passes
  unchanged.
  Red when: `pass-order`'s verdict or counts move.
- **AC14** — When `tools/unattended/check-brief-recorded.sh` runs over this repo with the cutoff
  lifted in a scratch clone, it skips exactly the units an independent probe finds built under a
  finished record, and HEAD bears out every one of them.
  fixture: the clone is scratch and is not this tree, because lifting the cutoff here would grade 101
  builds that predate briefs.
  figure: DERIVED at observation time; the journal records the count it found.
  Red when: the leg and the probe disagree on any unit, or the leg reports an unborne claim in history
  that no forgery produced.
- **AC15** — When the suite's `misselect` fixture lands a first run, then a hand commit naming the
  unit that touches a path outside the record surface, then a second run's preflight retiring the
  first record, then the unit's build with no brief, the leg exits 1 with `NO brief row`, prints
  `GRADED AT A LATER COMMIT` naming the unit, never prints `NOT GRADED`, and counts one such unit on
  its liveness line.
  Red when: `build_commit`'s earliest pick decides the skip, which is what the leg at `c9bc0b2a` did.
- **AC16** — When `tools/unattended/.unattended.conf.example` is read, its `BRIEF_RECORDED_CUTOFF`
  description points at the protocol's row for which units are graded and states no population of
  its own.
  Red when: the example restates the graded population, which is the copy round 3 found missing the
  claim-at-HEAD condition.

## 7. Gates

`brief-recorded` · `pass-order history` · `unattended kit gate` · `unattended skill wiring` · `kit version markers` · `install-prefix (shipped surface)` · `lexicon naming predicates` · `shell hygiene (a loop fed by a command substitution)` · `harness arms (fail branches armed or pinned)` · `memory hygiene` · `spec tokens (a spec's own names resolve)` · `drift-audit records` · `kickoff-manifest ratchet`

The suite carrying this unit's arms is on no bar, like every self-test in this kit. It runs on demand
through `run-unattended-gates.sh`, which is where the journal's green verdict comes from.

New arm: `tools/unattended/check-brief-recorded.test.sh` · the leg at `f1e58789`, the corroboration removed, the absence test removed, the claim terminator removed, and a byte comparison in place of the claim · none
New arm: `tools/unattended/check-brief-recorded.test.sh` · the leg at `c9bc0b2a`, whose skip trusted `build_commit`'s earliest pick · none

## 8. Open questions

- **F1 — which predicate decides that a unit was built during a run?** The options were the phase of
  the run-state file at the build commit, or reachability from the finished record's witness.
  RESOLVED (agent, 2026-09-13, delegated): the phase at the build commit, honoured only while HEAD
  still carries the same base, phase and witness. §4 gives the grounds and the rejected options.
  The orchestrating session delegated the choice in its brief.
- **F2 — how does a retired `RUN.<phase>.<8hex>.md` take part?** It could be ignored, read for brief
  rows, or accepted as the survivor of the build commit's record.
  RESOLVED (agent, 2026-09-13, delegated): accepted as a survivor only, and only when it was not yet
  tracked at the build commit. It is never read for a brief row or a base.
- **F3 — does `pass-order` share the scoping?** RESOLVED (owner, 2026-09-13): no. The ruling waives
  `pass-order`'s red in NicoCares and fixes only this leg. That the two legs share no population code,
  so nothing in `pass-order` moves, is this spec's finding in §4.

## 9. Revision log

- rev-1 · 2026-09-13 · initial draft.
- rev-2 · 2026-09-13 · §6 · AC9 · the leg's header points at the ruling and the build instead of
  citing this unit's id. The full bar redded `drift-audit records` on it: signal 2 reads a live
  spec's id in shipped source as a status nobody closed, and its pin is shrink-only. The suite, which
  that signal does not read, carries the id, as `TOOL-dPolishedVitrine-1`'s own suite does.
- rev-3 · 2026-09-13 · S6 · S8 · §4 · §5 · AC15 · AC16 · §7 · AMENDED by the round-3 Tier-2 diff
  review. R3-4, HIGH: a unit built during a live run skipped grading when `build_commit` picked an
  id-naming hand commit made between two runs, where the record still read the first run's LANDED
  and a retired record at HEAD bore that claim out. S8 and §4's new subsection walk the later commits
  the library's predicate accepts and grade the unit at the first one made while a run was live;
  AC15 is its `misselect` arm, red against the leg at `c9bc0b2a`. R3-10, LOW: the conf example stated
  the graded population without the claim-at-HEAD condition, so S6 and AC16 turn it into a pointer
  at the protocol row, which now also carries the later-commit condition.

## 10. Reuse audit

No existing seam fits the population filter, and the probe that should have said so could not see
the candidates. `python tools/codebase-map/reuse_lookup.py "grade only units built while an unattended
run was live; skip a unit whose build commit carries a finished run-state record"` returned
name-stem neighbours in Python, the `run` and `build_*` families, and reported `unscanned layers:
.sh`. Every candidate here is shell, so they were found by reading the kit. `build_commit` in
`lib-unattended.sh` is reused unchanged. The driver's `PHASES_TERMINAL` is read rather than
re-spelled, with the parse grammar of the kit gate's `core_of`. The driver's `fact` grammar is
mirrored in one awk program rather than sliced, because `fact` takes a file and the leg holds blobs.
The retired-record shape is `archive_name_of`'s, matched by name and never by blob.

Recall terms used: `brief-recorded BRIEF_RECORDED_CUTOFF build_commit PHASES_TERMINAL LANDED ABORTED
run-state rotation archive_name_of preflight terminal witness pass-order`, against the question
"which units does the brief-recorded leg grade, and what happens to a unit built after its unattended
run finished". It returned `TOOL-dClosedLexicon-11`, the rotation's own record, cited in §4, and the
leg's origin under `TOOL-aHoistedPass-7`. No record binds the population the other way.
