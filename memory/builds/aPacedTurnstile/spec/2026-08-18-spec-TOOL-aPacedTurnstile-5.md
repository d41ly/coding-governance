# TOOL-aPacedTurnstile-5 — the run record: a durable, machine-readable status emitter

**Status:** OPEN · rev-8 · 2026-08-20 · node a · Tier-2 · base 6517579f · streams tooling

## 1. Goal

The runner forgets everything the moment it exits: the per-leg results it already computes live in a
scratch dir the EXIT trap deletes, and the three files that survive are prose for a human. Make the
run's state a durable, machine-readable record another session can read during and after the run,
including after a crash.

## 2. Scope (IN)

- **S1** — the per-leg completion files move from the `mktemp -d` scratch dir to a PER-RUN
  directory `<git-dir>/gate-run/<run-id>/`, with `<git-dir>/gate-run/current` naming the in-flight
  one for a concurrent reader. The per-run uniqueness is preserved deliberately, not incidentally:
  the completion file is the DISPATCH SUPPRESSOR, not a log, so a leftover one at a fixed path would
  make the runner skip a leg and print it green. Creating the run directory fails the run the way
  the `mktemp -d` it replaces already does. **Retention is `GATE_RUN_KEEP=5` run directories**, a
  DECLARED constant with its reasoning beside it in `TOOL-aPacedTurnstile-4` S8's shape rather than
  an unnamed number: five is enough that a crashed run's record — the one with a header and no
  verdict — survives the two or three ordinary runs an operator does before they come back to look
  at it, and small enough that a record of a header, one row per leg and a verdict cannot grow the
  git dir without practical limit. The sweep to that bound runs AFTER the verdict file is written,
  never before the first leg dispatches. Round 3's T14/T21: R6's fix asked for the bound AND its
  criterion, and only the criterion landed, so AC15 graded "the declared retention bound" against a
  declaration nothing made.
  **The two directories have separate lifetimes and separate owners, and round 2's R2/R3 are why
  this is now stated rather than implied.** `<git-dir>/gate-run/` is the DURABLE record: this unit
  owns it, the EXIT trap stops covering it, and the only deleter is the post-verdict sweep named
  above. The `mktemp -d` scratch survives this unit — it still holds the timings temporaries — and
  the trap goes on covering it; `TOOL-aPacedTurnstile-4` widens that trap to INT, TERM and HUP and
  its scope is the SCRATCH dir alone. A trap that swept `<git-dir>/gate-run/` would erase the record
  on every ordinary exit and on every caught signal, which is every path except the crash the record
  exists to make readable, and `-4` lands SECOND under the re-scoped order — immediately after this
unit — so it would win by default. The re-scope shortened that gap from four units to one, which
makes the separate-owners statement more load-bearing than it was when it was written, not less:
`-4`'s builder now opens this file's trap line within one unit of it being narrowed. Nothing clears the
  record at the START of a run: per-run uniqueness is what closes blocker F2, and a start-of-run
  clear can partially fail on this platform against an open handle or an AV lock and inherit the
  previous run's verdicts — the exact branch F2 named.
- **S2** — `<git-dir>/gate-run/<run-id>/header` is written BEFORE the first leg dispatches, in a
  key-per-line grammar, carrying the schema version, run id, start time, head, base and how the base
  was resolved, the tree fingerprint, whether the tree was CLEAN at start, the manifest path and its
  blob hash, the full-run flag and the reason it was forced, the RUN ENVELOPE below, the resolved
  DISPATCH ORDER, the leg count, and the worktree path. The dispatch order is here rather than in
  `TOOL-aPacedTurnstile-3` because this unit already writes the header at the point that value is in
  scope, and a record's key set must stay single-sourced; that unit's ordering criteria read it.
  **The run envelope is four keys, not one, and `TOOL-aPacedTurnstile-2` is why.** An earlier draft
  recorded "the resolved width" alone, written when the width was a number the runner computed. It is
  now a DECLARED row: `tools/run-gates/gate-profiles.txt` names rows with a width and a per-leg
  timeout each, and `run-gates.sh` composes the whole envelope as `PROF_LINE` before the first leg
  dispatches. The header therefore records the selected profile ROW NAME, the resolved width, the
  per-leg timeout, and the DETECTION SOURCE that picked the row. Recording the width alone loses the
  three facts that explain it, and a later reader comparing two runs cannot tell a re-detected row
  from a `GATE_JOBS` override. The keys are the components of `PROF_LINE` rather than a second
  derivation of the same four values, because S2 declares itself the single source of the record's
  key set and two derivations of one envelope is the two-answers-to-one-question class.
- **S3** — each worker writes one TSV row per leg alongside the files it already writes — name,
  status, rc, seconds, started, ended, input key — through the same temp-then-rename the worker
  already uses for its completion signal. The per-leg OUTPUT copy the worker also writes becomes
  durable by this move, so it takes the same redaction and the same restrictive mode the existing
  per-leg log already has; a durable copy of command output that skips the masking its sibling
  applies is a credential leak the current scratch-dir lifetime was hiding.
- **S4** — `<git-dir>/gate-run/<run-id>/verdict` is written last, carrying the end time, verdict, and the
  ran / failed / skipped / reused tallies plus the end-of-run fingerprint and whether the tree moved.
  Its ABSENCE is the crash signal, and is the only crash signal needed.
- **S5** — a fingerprint helper computing one digest over the committed tree object plus the
  porcelain status lines plus the blob hashes of every dirty-or-untracked file that still exists.
  Over-sensitive by construction, never under-sensitive; empty on any failure.
  **It takes an optional REV argument, and round 3's blocker T1 is why this signature is declared
  here rather than left to a builder.** Two forms, one implementation:

  - `gate-fingerprint.sh` with no argument — the WORKING-TREE form. All three components: the tree
    object at `HEAD`, the sorted porcelain lines, the dirty-or-untracked blob hashes. This is what
    the runner stamps into the header and into `gate-full-green`.
  - `gate-fingerprint.sh <rev>` — the AT-A-REV form. The tree object at `<rev>`, and the other two
    components supplied EMPTY rather than omitted, so both forms hash the same input arity. This is
    what `.githooks/pre-push` calls for `TOOL-aPacedTurnstile-7`'s predicate 0.

  **The binding property, and the whole reason the two forms exist:** on a CLEAN tree the two forms
  produce the SAME value, because the porcelain component and the dirty-blob set are empty in both.
  S7 refuses to write `gate-full-green` unless the tree was clean at start, so every recorded digest
  is one the rev form reproduces at the sha it names. Without this, `-7`'s corrected predicate 0
  names a computation this interface cannot perform, and a builder's three options are: call the
  no-argument form from the hook, which takes the digest at the pushed tip and is round 2's blocker
  R1 restored verbatim; reimplement an at-a-rev digest inside the hook, which is the
  two-answers-to-one-question class this item exists to prevent and which fails toward FULL forever;
  or invent the mode, where an arity mismatch between the two makes predicate 0 fire
  unconditionally. Round 2's R19 gave the helper a name; the signature is what was still missing. It ships as
  `tools/run-gates/gate-fingerprint.sh` — its OWN executable inside the kit, named here by repo
  identifier and spelled identically in `TOOL-aPacedTurnstile-7` S2b and in
  `TOOL-aPacedTurnstile-1`'s kit-dir layout — rather than as a function private to the runner,
  because `TOOL-aPacedTurnstile-7`'s predicate 0 has to compute the same digest from a git hook.
  Round 2's R19: the one interface in this build that both specs insist must have exactly one
  implementation was the only one with no identifier, which made reimplementing the digest the path
  of least resistance for `-7`'s builder. Two
  independent implementations of one digest is the `two-answers-to-one-question` class, and here it
  fails toward FULL forever — safe, and it would permanently defeat the scoped path this build
  exists to enable, which is the kind of failure nobody investigates because it looks like caution.
  **It SHIPS, and that is a decision rather than an accident of the payload rule.**
  `tools/run-gates/kit.toml` claims the kit dir with a single `**` rule, so any new file in that
  directory lands in every adopting tree unless another rule withholds it. The withholding precedent
  is `run-gates.gov.test.sh`, and its stated reason is that its arms are keyed on THIS repo's corpus.
  This helper has no corpus in it: it hashes a tree object, the porcelain lines and the dirty blobs,
  which are true statements in any git repository, and its only caller inside gov is
  `.githooks/pre-push`, which an adopter may or may not have. So it ships as a public kit affordance,
  and this unit adds its row to `tools/run-gates/README.md`'s piece table so an adopter meets it as a
  documented tool rather than as an unexplained executable. An adopting tree with no pre-push hook
  simply never calls it, which costs nothing.
- **S6** — `<git-dir>/gate-ledger.tsv` replaces the timing cache: rows gain status, input key and a
  timestamp while KEEPING the duration in field 2, so the existing dispatch-order parser needs no
  edit. The carry-forward merge for guard-skipped legs is kept exactly as written, and the rewrite
  becomes an atomic rename rather than a copy.
  **`gate-timings.tsv` has a SECOND reader now, and switching the cache without it is a blocker this
  item owns.** The compatibility argument above surveyed one parser — the runner's own dispatch-order
  block, which splits on tab, reads field 2 and ignores every extra column — and that survey was
  complete when it was written. The sibling build `aMeteredTurnstile` has since landed
  `tools/run-gates/profile_bar.py`, which resolves the cache at a HARDCODED path, snapshots its mtime
  before and after the run, and REFUSES with a non-zero exit when it did not move, on the stated
  ground that every duration then available belongs to an earlier run. A ledger that silently stops
  writing the old cache therefore does not degrade the profiler — it makes it refuse on every
  invocation, which turns the `profile-bar selftest` leg into a leg whose subject can no longer run.
  This unit takes the edit rather than leaving a compatibility shim behind: the profiler's path
  resolution, its two mtime probes and its orphan measurement all move to the ledger, and
  `aMeteredTurnstile`'s own spec authorizes exactly this by pledging to read this unit's ledger and
  delete its wrapping path once `-5` lands. Keeping both files written for one release was the other
  option and is refused: two stores of one fact, with the older one read by the only tool that grades
  the newer one, is the shape this unit exists to remove.
- **S7** — `<git-dir>/gate-full-green` is written ONLY when the run failed nothing, skipped nothing,
  reused nothing, the tree did not move, AND the tree was CLEAN when the run started. **CLEAN means
  exactly `git status --porcelain` EMPTY, untracked-and-unignored files included** — the same
  predicate §4 computes the fingerprint's own porcelain component from, and it is spelled out here
  because S5's binding property is exactly as strong as this precondition and nothing else in the set
  defines the word. The obvious `git diff --quiet` pair ignores untracked files and would satisfy
  every other word of this item with a `??` line present; the record would then carry a digest whose
  porcelain and dirty-blob components are NON-empty, which the rev form cannot reproduce at any sha,
  so predicate 0 would mismatch on every later push and force full forever while printing `the record
  describes a different tree` — the blocker back in its unconditional-mismatch form, and neither AC17
  (which grades the helper) nor a diff-only fixture could see it (round 4's V3). This is the
  file `TOOL-aPacedTurnstile-7` reads, and those five preconditions are what make it mean what its
  name says. The clean-tree precondition is the one the spec audit found missing: a developer's
  ordinary full run on a dirty tree would otherwise stamp a green that the push boundary then treats
  as proof about a tree nobody ever tested. Each precondition carries its own negative control,
  because an implementation that forgets ONE of them passes every arm written for the others.
- **S8** — `tools/gate-legs.json` gains an optional `impure` key carrying reason strings, seeded from
  MEASUREMENT rather than guess: the unattended legs call out to the remote, so their verdicts are a
  function of the remote as well as of the tree.
  **The key is GOV-ONLY and cannot travel, and the spec states that rather than leaving a builder to
  discover it.** Since `TOOL-aPacedTurnstile-1`, a target's manifest is no longer hand-authored:
  `tools/govkit/govkit.py` emits each target leg row from a descriptor's `[[gate_leg]]` block and
  reads `name`, `argv` and `guard` from it, and nothing else. An `impure` declaration written in a
  descriptor is dropped on the floor, so gov can mark its own legs impure and no adopting tree can
  mark any. Extending the descriptor grammar and govkit's emission is the obvious repair and is
  explicitly OUT of this unit — it is a deployer-side change to a file this unit otherwise never
  touches, and the re-scope that authorized this revision cut the arm that would have made the
  omission visible rather than funding the extension. What an adopting tree's reuse path does with no
  impure declarations at all is `TOOL-aPacedTurnstile-6`'s question, because that unit owns the reuse
  verb and the denial rule; it is carried in §8 as an open fork with the two options, not resolved
  here. The optional-key spelling is what makes the omission survivable in the meantime: a manifest
  with no `impure` anywhere is a legal manifest, so the shipped canary of S10 grades the key's SHAPE
  and never its presence.
- **S9** — record arms in `tools/run-gates/run-gates.evidence.test.sh`: the header is readable BY A
  LEG while the run is in flight, the verdict file is absent after a hard kill, a red leg's ledger
  row carries no reusable key, a corrupt ledger is survived, and the header's run-envelope keys match
  the `PROF_LINE` the same run printed across two fixtures whose profile rows differ. The migration
  arm is not here: S6's obligation is graded where its subject's own gate already lives, in
  `tools/run-gates/profile_bar.test.sh`, because an arm asserting a tool still works belongs beside
  that tool rather than beside the store it reads.
- **S10** — a canary arm pinning the manifest's known key set, so a mistyped `impure` cannot silently
  make a network-reading leg reusable. **It is a SCHEMA arm and it lives in the shipped canary, and
  the corpus-keyed half that used to ride with it is CUT.** `TOOL-aPacedTurnstile-1` split the canary
  in two and reserved the gov-only file for arms keyed on this repo's own legs, naming the reuse
  unit's network-calling leg names as one of the three it expected. The key-set pin is not one of
  those: it asserts that every row carries `name`, `argv` and optionally `guard` and `impure` and
  nothing else, which is true of any manifest in any tree, so it belongs in
  `tools/run-gates/run-gates.test.sh` and must read the manifest the way that file already derives
  it. Hardcoding `tools/gate-legs.json` inside a harness that SHIPS is the
  pin-copied-from-another-corpus class the kit's own README refuses by name. The other half — any
  assertion about WHICH of gov's legs are declared impure — has no home left after the re-scope cut
  `TOOL-aPacedTurnstile-6`'s network predicate, so nothing lands in `run-gates.gov.test.sh` from this
  unit. That is recorded in §3 as a cut rather than dropped, because the reservation in the gov
  harness's own header still names an arm nobody is now writing.

## 3. Non-goals (OUT)

- Consuming the record. Reuse, resume and the base change are `TOOL-aPacedTurnstile-6`; the push
  boundary is `TOOL-aPacedTurnstile-7`. This unit writes and declares, and changes no verdict.
- JSON or JSONL. See the format argument below.
- A lock. One file per writer needs none, and `flock` does not exist on this platform.
- A new leg, a new process, or a daemon.
- Committing any of this. The record lives in the git dir, which is already where the summary,
  the failure record and the per-leg logs live.
- Making `impure` travel to an adopting tree. `tools/govkit/govkit.py` reads `name`, `argv` and
  `guard` out of a descriptor's `[[gate_leg]]` block and emits nothing else, so extending it means
  editing the descriptor grammar, the emitter and the deployer's own selfcheck. That is a deployer
  unit, not a record unit, and §8 carries the fork.
- The gov-corpus canary arm S10 used to carry. CUT by the 2026-08-20 re-scope, which cut
  `TOOL-aPacedTurnstile-6`'s network predicate on the evidence that the predicate was run over the
  real manifest for the first time during that re-scope and matched six legs, every one of them
  hermetic. The arm existed to police that predicate's declarations; with the predicate gone it
  polices nothing. The reservation for it still stands in `tools/run-gates/run-gates.gov.test.sh`'s
  header, so this is a refusal on the record rather than a silent non-delivery.
- AC12, the assertion-count criterion. CUT by the same re-scope, and the reason is the spec's own
  green-by-absence rule turned on itself: `TOOL-aPacedTurnstile-1` landed both floors and left no row
  for either harness in the count registry, so the criterion is green today, before this unit starts,
  and cannot fail as a result of anything this unit does. The live obligation it was reaching for —
  that the new arms RAISE the executed counts and the floors move with them — is a different sentence
  and is stated in §5's testing line instead of pretending to be a criterion.

## 4. Design

### The question, answered first: what is the best way to implement a status emitter?

**A directory of small append-once files under `<git-dir>/gate-run/`, written by the workers that
already write them, plus one keyed TSV ledger.** No JSON, no JSONL, no lock, no new process, no new
leg. Three requirements decide it before taste gets a vote.

Surviving a crash means the record is written INCREMENTALLY — a single document composed at the end
is lost precisely in the case it exists for. CONCURRENT writers mean an incrementally-written
SHARED file needs a lock, and there is none available here; one file per writer needs no lock at
all, because the atomicity is the filesystem's rename rather than ours. How many writers there are is
not a constant this spec may state: `TOOL-aPacedTurnstile-2` made the pool width a DECLARED row in
`tools/run-gates/gate-profiles.txt`, one width per hardware row, with `GATE_JOBS` overriding it. The
argument holds at every width above one and is vacuous only at width one, which is the serial
rollback and not a design point. An earlier draft said "eight", which was the width the runner
computed before that row table existed. And it already exists: the
worker writes its output, then its duration, then commits its completion through a temp-then-rename.
That is already a per-leg, lock-free, atomically-committed completion record. The only reasons it is
not durable are the scratch dir and the EXIT trap that deletes it.

So the emitter is not a new subsystem. It is: retarget the completion files to the per-run
directory, NARROW the trap so it covers the `mktemp -d` scratch and no longer the record, add a
header before dispatch and a verdict after, and sweep older run dirs once the verdict is on disk.
"Drop the trap" is what an earlier draft said, and it was wrong in a way that mattered: the scratch
dir is still there and still needs covering, and the sentence read as licence for
`TOOL-aPacedTurnstile-4` to claim the cleanup line for a widened trap over the record.

### Format

Key-per-line text, not JSON. `tools/unattended/unattended.sh` already establishes this grammar and
its reader, with the stated reason that a grep is the parser and no verb needs a second one, and its
reader is deliberately fork-free because process spawn dominates on this platform. The consumers
here are shell — the pre-push hook and the runner itself — and bash cannot emit JSON safely without
a helper process per write. Key-per-line is grep-, awk- and python-parseable, and cannot be
corrupted by an unescaped value.

The per-leg rows are TSV instead, because they are single-line and written once per non-sentinel leg.
The count is DERIVED from `tools/gate-legs.json` and is not stated here — it was 70 when this spec
was drafted, and re-deriving it on 2026-08-20 at `43a6c13` returns 86, so a number typed into this
paragraph would have been wrong within two days of being written. TSV is legal only while three
properties hold of the manifest, and the builder re-derives all three rather than trusting this
sentence: no leg name contains a tab, a newline or a colon, and every name is unique. Re-derived at
`43a6c13` on 2026-08-20 over the whole manifest, all three hold. If a later manifest breaks one, the
row format changes and this paragraph is what says so.

### Data model

Every path below sits under the PER-RUN directory `<git-dir>/gate-run/<run-id>/`, and
`<git-dir>/gate-run/current` is a pointer to the in-flight one. The flat spelling is deliberately
absent: a completion file at a fixed path is a stale DISPATCH SUPPRESSOR, and that is the whole of
blocker F2. A reader that wants the live run resolves `current` first.

**`<git-dir>` is ONE variable, and this unit collapses the pair the runner currently carries.**
`run-gates.sh` resolves the git dir twice under two names: once early, guarded against an empty
answer before any path is composed from it, and again later for the durable-summary and timing-cache
paths. This unit adds four more git-dir-rooted paths — the run directory, the pointer, the ledger and
the full-green file — so a builder inheriting two answers would be choosing which one to hang them
off, and a third resolution would follow the next time somebody adds a fifth path. The record uses
the EARLY, guarded resolution, and the later one is folded into it in the same commit. That fold is
the one behavioural change this unit makes to a path that already worked, and it is here rather than
in a sibling because this is the unit that makes the ambiguity expensive.

`<run-id>/header` exists to prove the run started; its absence proves nothing ran. Keys are listed in
S2, and the dispatch-order key is the one `TOOL-aPacedTurnstile-3`'s ordering criteria read.

`<run-id>/<i>.leg` is keyed on the manifest INDEX, which is stable within a run and lossless, with
the leg name carried inside the row — so a slug-safe filename can never mis-attribute a verdict.
Status is one of ok, fail, skip, reuse; a skipped row carries a dash for rc and key.

`<run-id>/verdict` is written last and carries the tallies.

`<git-dir>/gate-ledger.tsv` is the cross-run keyed store. Field 2 stays the duration, so the
dispatch-order block reads it unchanged — it splits on tab and ignores every extra column. A failed
leg records its status and a dash for the key, so a red verdict is in the record and can never be
reused. The carry-forward is kept exactly as written: a guard-skipped leg produces no duration, and
blanking its cached row is a bug this repo has already paid for and already gates.

`<git-dir>/gate-full-green` carries the schema, head, manifest blob, tree fingerprint, timestamp and
leg count. Nothing else reads it in this unit.

### The fingerprint

One digest over three things: the committed tree object, the sorted porcelain status lines, and the
blob hashes of every dirty-or-untracked file that still exists. Its cost is measured rather than
assumed, and the measurement carries its own envelope: the status plus hash-object pass completed in
0.44 s on node `a` at `43a6c13` on 2026-08-20, once per run rather than per leg. The 0.41 s this
paragraph carried before was taken at the drafting base and re-measuring moved it, which is the
expected behaviour of a figure that depends on the size of the working tree — a builder who needs the
number for a decision re-runs the pass rather than quoting either value.

**Two invocation forms over that one definition, per S5.** With no argument the tree object is
`HEAD`'s and the other two components are measured from the live worktree — the runner's form. With
a `<rev>` argument the tree object is that rev's and the other two components are supplied EMPTY,
which is the form `.githooks/pre-push` calls. They are EQUAL on a clean tree, since the porcelain
and dirty-blob components are empty in both, and that equality is what lets `TOOL-aPacedTurnstile-7`
recompute a recorded digest at the sha the record names. Empty rather than OMITTED is the load-
bearing word: an at-a-rev form that hashed one component where the working-tree form hashes three
would mismatch unconditionally, and predicate 0 would force full forever while reading as caution.

The porcelain lines carry deletions and renames that a blob list cannot, and a path containing a
newline arrives quoted but still CHANGES when the path changes. That asymmetry is the whole
contract: **the fingerprint may be over-sensitive, never under-sensitive.** A false difference costs
a re-run; a false match would license a wrong skip. Any failure anywhere yields empty, which means
no reuse.

One precondition is load-bearing and is documented rather than assumed: this repo's ignore rules
cover the python bytecode dirs, so the python legs do not move the tree under their own run —
measured, with two of them leaving the porcelain output byte-identical. A repo without those rules
would see its fingerprint move every run and would never reuse, which is the safe direction, but it
is a stated ceiling rather than a mystery.

### `tree_moved` is not decoration

A concurrent editor moved a worktree underneath a measurement during this build's own kickoff.
Capturing the fingerprint again at the end costs one more pass of the measurement above and is the
difference between a green that
describes a tree and a green that describes no tree at all. When it is set, the ledger is not
updated and the full-green file is not written.

### What this unit does and does not claim

The record is a fact about what ran. It licenses nothing on its own — every consumer is a sibling
unit, and each states its own soundness argument. The one claim made here is the negative one: a
failed or skipped or reused leg is recorded as such, so no consumer can mistake it for a green.

### Rollout

One commit. Rollback is restoring the trap's original scope and the scratch destination; the record
is additive and nothing reads it until `TOOL-aPacedTurnstile-6` lands. "Restoring the trap" named
the whole trap in an earlier draft, which contradicted this unit's own narrowing — the trap is
never removed, only its coverage of `<git-dir>/gate-run/` is.

**This unit lands FIRST** in the re-scoped order `-5 → -4 → -6 → -7 → -3`, and the reason is the one
the re-scope stated: the record is what `-4`, `-6` and `-7` all read, and nothing can be built against
a record that does not exist. It has no upstream edge left. The old order put `-2` ahead of it so the
record writer could gain the profile line, and `-2` has since landed, so that edge is discharged
rather than dropped — S2's run-envelope keys are what discharging it looks like. The one edge OUT of
this unit that is not simply "everything reads the record" is `-5 → -4`: `-4` widens the EXIT trap
this unit narrows, so the trap's final shape has to be settled before it is widened.
The rollback above is not made harder by landing first, because it restores a file no other unit in
this build has touched yet.

### Files touched (estimate)

| file | change |
|---|---|
| `tools/run-gates/run-gates.sh` | destination, trap narrowing, header, per-leg row, verdict, ledger, post-verdict sweep, and the collapse of the duplicate git-dir resolution onto the guarded one |
| `tools/run-gates/gate-fingerprint.sh` | NEW — S5's digest in BOTH forms: no argument for the runner's working-tree stamp, `<rev>` for the hook's at-a-rev recomputation, equal on a clean tree |
| `tools/run-gates/run-gates.evidence.test.sh` | S9's arms, plus AC15/AC16/AC17. `TOOL-aPacedTurnstile-7` also lands ONE arm here — AC6d's, reading the forced-full reason out of the header this unit writes — because that unit's own suite stubs the gate. Recorded on both sides so the file has one ownership statement (V4) |
| `tools/run-gates/run-gates.test.sh` | S10's pinned key set, read off the manifest path this harness already derives — never a gov spelling |
| `tools/run-gates/profile_bar.py` | S6's obligation: the cache path it resolves, the two mtime probes that decide its did-not-move refusal, and its orphan measurement all move to the ledger. Authorized by `aMeteredTurnstile`'s own spec, which pledges the switch and the deletion of its wrapping path when this unit lands |
| `tools/run-gates/profile_bar.test.sh` | AC18's arms: the migrated profiler still passes its own fixtures, and its did-not-move refusal still fires against a store that genuinely did not move |
| `tools/run-gates/README.md` | S5's decision made visible: a piece-table row for `gate-fingerprint.sh`, which ships |
| `tools/gate-legs.json` | the `impure` key on the measured legs. Gov-only by construction, per S8 |
| `AGENTS.md` | the "How the bar behaves" paragraph gains the record, beside the sentence that already describes the per-leg logs and the failure file. The durable-evidence BULLET an earlier draft named here was dissolved when `TOOL-aPacedTurnstile-1` collapsed that section into prose |

### Alternatives rejected

- **Append-only JSONL from every worker.** Rejected: interleaved writes from CONCURRENT processes to
  one descriptor are not atomic beyond a pipe buffer, and there is no lock available. The rejection is
  scoped to the IN-RUN multi-writer case and condemns nothing else — `tools/run-gates/profile_bar.py`
  writes a JSONL record of its own and is a single writer appending one line after the run has
  finished, where neither half of this reason applies.
- **One JSON document written at the end.** Rejected: lost in the crash case it exists for. This is
  the reason the profiler's own record does not deliver this unit: it is composed after the run,
  which is exactly the case the crash makes unreachable.
- **A committed file.** Rejected: it is per-run machine state, and committing it would put a
  timestamp in every diff.
- **git notes.** Rejected: keyed on a commit, and a run measures a working tree.

## 5. Production-readiness checklist

- security — the record carries paths and leg names, and S3's per-leg OUTPUT copy DOES carry command
  output, which is what makes the redaction load-bearing here rather than untouched. It takes the
  same masking and the same restrictive mode the existing per-leg log already has; the record
  directory takes the restrictive mode too. An earlier draft of this line said the opposite — that
  the new files carry no command output — while S3 said they do, and §5 is the section a builder
  grades the security line against, so the contradiction sat in the half that gets read (round 2's
  R24). AC16 observes it.
- perf / scale — the fingerprint runs twice per run at the cost §4 measures, and per-leg rows are one
  line each. The figure is re-derived rather than restated here, so this line cannot disagree with §4.
- a11y — N/A: no user interface.
- i18n — N/A: machine-readable keys and operator-facing English.
- error / empty / loading states — an in-flight run is exactly "header present, verdict absent", and
  that is the crash signal too; an arm asserts it after a hard kill.
- observability — this unit IS the observability.
- risks (concurrency, data-loss, rollback hazards) — the record is per-worker single-writer, so
  concurrency needs no lock. Data loss is bounded to the current run. The one real hazard is a stale
  record read by a later consumer, which is why the tree fingerprint and the manifest blob are both
  in the header.
- testing + left-shift gates — the pinned key set left-shifts the mistyped-declaration class. The new
  arms must RAISE the executed assertion counts both harnesses already report, and the declared floors
  move with them in the same commit; a new arm that leaves a floor where it was is an arm the count
  gate cannot see. This is the live obligation the cut AC12 was reaching for.
- migration / rollback — the ledger supersedes the timing cache, and the profiler that reads that
  cache migrates with it in the same commit rather than being left to refuse. An absent or corrupt
  ledger costs dispatch order only, which the existing arm already gates.
- user docs — the charter's "How the bar behaves" paragraph, and the kit README's piece table for the
  fingerprint helper that now ships.

## 6. Acceptance criteria

- **AC1** — When a run is in flight, a leg can resolve `<git-dir>/gate-run/current` and read that
  run's `header`, seeing this run's id — asserted by a fixture leg in
  `tools/run-gates/run-gates.evidence.test.sh`.
- **AC2** — When the runner is killed mid-run with `timeout -s KILL`, that run's `header` exists
  under `<git-dir>/gate-run/<run-id>/` and its `verdict` does not.
- **AC3** — When a run completes, `<git-dir>/gate-run/<run-id>/` holds one `.leg` row per
  non-sentinel leg, and each row's first field equals the manifest name at that index.
- **AC4** — When a leg fails, its row in `<git-dir>/gate-ledger.tsv` carries status `fail` and a
  dash in the input-key field.
- **AC5** — When a guard-skipped leg produces no duration, its previously cached ledger row survives
  the rewrite in `<git-dir>/gate-ledger.tsv` — the carry-forward the existing arm already gates,
  re-asserted against the new row shape.
- **AC6** — When the ledger is corrupted to arbitrary bytes, the run still completes and reports its
  ordinary verdict, asserted in `tools/run-gates/run-gates.evidence.test.sh`.
- **AC7** — When a run is green with nothing skipped, nothing reused and an unmoved tree,
  `<git-dir>/gate-full-green` is written and its `manifest_blob` equals `git hash-object` of THE
  MANIFEST THAT RUN READ — the fixture the arm points `GATE_LEGS` at, resolved the way the runner
  resolves it, never a literal `tools/gate-legs.json`. Every arm in
  `tools/run-gates/run-gates.evidence.test.sh` drives the runner against a fixture manifest in a
  scratch git dir, so hashing gov's manifest would grade a file the run under test never opened; and
  that harness ships, so the gov spelling would also name a path an adopting tree may not have.
- **AC8** — When a run is green but ANY leg was skipped, `<git-dir>/gate-full-green` is NOT written
  or updated — the precondition that makes the file's name true.
- **AC9** — When the working tree is modified while the run is in flight, the verdict file records
  the tree as moved and `<git-dir>/gate-full-green` is not written.
- **AC10** — When a leg row in the manifest that harness DERIVES carries a key outside the pinned
  known set, `bash tools/run-gates/run-gates.test.sh` exits non-zero naming that key. The arm reads
  the derived path — the same `GATE_LEGS`-or-sibling resolution the file already performs for its
  other arms — so it grades whatever manifest the tree it runs in actually has. Its control is a
  manifest carrying no `impure` key anywhere, which must PASS: the key is optional and gov-only per
  S8, and an arm that reds on its absence is the arm that reds in every adopting tree on arrival.
- **AC11** — When a run REDS, `<git-dir>/gate-full-green` is neither written nor updated, asserted in
  `tools/run-gates/run-gates.evidence.test.sh` against a pre-existing file from an earlier green — so
  the arm distinguishes not-written from not-updated. This is the precondition the push-boundary
  inversion rests on and it was the only one of the five with no negative control.
- **AC13** — When the working tree is DIRTY at the start of an otherwise fully green run,
  `<git-dir>/gate-full-green` is not written, asserted in
  `tools/run-gates/run-gates.evidence.test.sh`, **across TWO fixtures whose only difference is what
  makes them dirty**: one with a modified tracked file, and one whose ONLY dirtiness is an untracked,
  unignored file. The second is the fixture that separates S7's definition of CLEAN from the
  `git diff --quiet` reading, and without it the two definitions are graded identically while
  selecting genuinely different populations (round 4's V3).
- **AC14** — When the run id is pinned through a test seam and a stale completion file for leg index
  3 is planted INSIDE that exact run directory before the run starts, that leg still EXECUTES and its
  reported verdict is the one it produced this run — asserted in
  `tools/run-gates/run-gates.evidence.test.sh`. The seam is load-bearing for the ARM, not for the
  runner: without a pinned id the plant lands in a directory the run never opens, so the arm passes
  by finding nothing and proves the opposite of what it claims. A second plant at the retired FLAT
  path must also be ignored.
- **AC15** — When a run completes against a fixture carrying more than `GATE_RUN_KEEP` run
  directories, exactly `GATE_RUN_KEEP` remain and they are the most recent, asserted in
  `tools/run-gates/run-gates.evidence.test.sh` and graded against that constant BY NAME rather than
  against a bound stated only in this criterion. Its control is the same fixture with the run KILLED
  before the verdict is written: nothing is swept, because the sweep runs after the verdict and never
  before dispatch. Without the named constant the criterion is satisfied by any bound a builder
  picks, including one above the fixture's size, which passes by finding nothing (round 2's R6,
  round 3's T14/T21).
- **AC17** — Three invocations, and the third is the one that binds the ARGUMENT. (a) With no
  argument on a CLEAN tree and with `HEAD` as its rev argument, the two print the SAME digest.
  (b) When the tree is made dirty, they DIFFER, with the rev form unchanged from its clean-tree
  value. (c) **On a clean tree with at least two commits whose trees differ, the helper at `HEAD~1`
  DIFFERS from the helper at `HEAD`, and equals the no-argument form measured with that rev checked
  out clean.** Without (c) an implementation that computes the tree object at HEAD unconditionally
  and reads the argument COUNT only — to decide whether to include the porcelain and dirty-blob
  components — passes (a) and (b) including (b)'s unchanged-rev clause, and the argument is dead.
  That form is precisely what restores round 2's blocker: the hook calls at the recorded sha, gets
  the digest at the tip, and predicate 0 fires on every push whose tree moved. It fails toward FULL,
  so no leg reds. (c) is the only assertion in the seven specs that invokes the helper at a rev whose
  tree differs from HEAD's (round 4's V2). Asserted in
  `tools/run-gates/run-gates.evidence.test.sh`. Both halves: the equality alone is satisfied by a rev
  form that ignores its argument, and the difference alone by two unrelated digests. This is the
  criterion `TOOL-aPacedTurnstile-7`'s predicate 0 rests on — the recorded value must be reproducible
  at the sha it names — and without it the blocker returns in its most expensive form, an
  unconditional mismatch that reads as caution (round 3's T1).
- **AC16** — When a fixture leg emits a token the runner's redaction masks, the DURABLE per-leg
  output copy under the run directory contains only the masked form, and both that file's mode and
  the run directory's mode are the restrictive ones the existing per-leg log already uses — asserted
  in `tools/run-gates/run-gates.evidence.test.sh`. Its control is the same fixture with the masking
  removed, which must red. S3 made this copy durable and §5 said the new files carried no command
  output; the criterion is what stops the two from disagreeing again (round 2's R24).
- **AC18** — When the ledger has replaced the timing cache,
  `bash tools/run-gates/profile_bar.test.sh` is green AND a real `python tools/run-gates/profile_bar.py`
  invocation completes without taking its did-not-move refusal branch. Both halves bind and neither
  alone does: the self-test drives the profiler against its own fixtures and would stay green while
  the real tool refuses on every run, and a single non-refusing invocation proves nothing about the
  orphan measurement or the record it writes. Its control is the pre-migration profiler run against a
  post-migration runner, which MUST take the refusal — if that control passes, the freshness probe is
  reading something that still moves and the migration was not the switch it claims to be.
- **AC19** — When a run's `header` is read, it carries the selected profile row NAME, the resolved
  width, the per-leg timeout and the detection source, and those four values equal the components of
  the `PROF_LINE` the same run printed — asserted in
  `tools/run-gates/run-gates.evidence.test.sh` across two fixtures whose profile rows differ. One
  fixture cannot separate a header that records the envelope from a header that hardcodes the
  catch-all row's values, which is the shape S2 exists to prevent.

## 7. Gates

`bash tools/run-gates/run-gates.test.sh` · `bash tools/run-gates/run-gates.evidence.test.sh` ·
`bash tools/run-gates/profile_bar.test.sh` · `bash tools/check-testsuite-counts.sh` ·
`python tools/govkit/govkit.py selfcheck` · `bash tools/memory-tree/check-memory-hygiene.sh` ·
`python tools/memory-tree/check-arms.py --check`.

`profile_bar.test.sh` joins the list because S6 edits its subject. A unit that migrates the store a
tool reads and does not name that tool's own gate is relying on the full bar to notice, which it
would — as a red leg nobody predicted, at the push boundary, after the commit is written.

## 8. Open questions

One fork is OPEN and the two below it are RESOLVED. Each resolved pick is the M3 ratification of the
fork's own recommendation; the reason each survived the veto order is recorded with it.

- **What an adopting tree's reuse path does with no `impure` declarations, given that the key cannot
  travel.** OPEN, and named here rather than guessed at. S8 establishes the fact: `govkit.py` emits
  `name`, `argv` and `guard` out of a descriptor and drops anything else, so gov can mark its own legs
  impure and no target can mark any. `TOOL-aPacedTurnstile-6` makes the declaration the sole thing
  that denies reuse, which means that in a target every leg is reusable on a byte-identical tree,
  including one that reads the network. Three options, none of them this unit's to take. (a) Extend
  the `[[gate_leg]]` grammar and govkit's emission so a descriptor can declare `impure`, which is a
  deployer unit and touches the emitter, the grammar and the deployer selfcheck. (b) Keep `GATE_REUSE`
  gov-only — it is already default-OFF — and say so in the kit README, which costs an adopter the
  feature and costs nobody a wrong green. (c) Make the shipped reuse path deny by DEFAULT on any leg
  with no declaration either way, inverting the key's polarity for targets only, which is safe and
  makes reuse buy nothing in a tree that cannot declare. The owner of this fork is
  `TOOL-aPacedTurnstile-6`, which owns the reuse verb and the denial rule; this unit records it
  because this unit is what adds the key, and a key whose consumer is undecided should not look
  settled from the writer's side.

- **Whether the record directory is cleared at the start of a run or kept as a rolling history.**
  Options: clear each run (one run's state, simple, and the crash signal stays unambiguous), or keep
  N runs. Recommendation: clear. The ledger already carries cross-run history keyed per leg, and a
  rolling directory needs a retention policy nobody has asked for.
  RESOLVED (agent, 2026-08-18, delegated), and CORRECTED after round 2's R6: **per-run
  directories, nothing cleared at start, older run dirs bounded by a sweep that runs after the
  verdict is written.** The first ratification took "clear each run" off an option set written
  BEFORE blocker F2 was folded in, and both halves of it contradicted the text the rest of this file
  now carries. S1 says the per-run uniqueness is preserved deliberately; §4 says the flat spelling is
  deliberately absent "and that is the whole of blocker F2". F2 is closed by the RUN ID, not by
  clearing — and a builder following the old answer would have restored the branch F2 named: a
  start-of-run clear with no failure branch, which on this platform can partially fail against an
  open handle or an AV lock and inherit the previous run's verdicts. AC14 cannot tell the two
  designs apart, because with the id pinned and the directory cleared at start the planted file is
  deleted, the leg executes, and the arm is green either way. The retention policy the old answer
  dismissed as unasked-for is the one S1 already states, and AC15 now grades its bound.
- **Whether `impure` carries reason strings or a bare boolean.** Recommendation: reason strings. A
  bare `true` is a claim with no evidence beside it, and this tree's settled pattern for a waiver is
  that it names its reason.
  RESOLVED (agent, 2026-08-18, delegated): reason strings. It is the more feature-rich option -
  a bare `true` is a claim with no evidence beside it - and it matches this tree's settled
  pattern that a waiver names its own reason.

## 9. Revision log

- rev-1 · 2026-08-18 · initial draft.
- rev-3 · 2026-08-18 · folded the blocker re-review, which found F2 only PARTLY closed. The first
  fold-in repointed the scope items and left §4 Data model and AC1 through AC3 spelling the flat
  path, so a builder grading against §6 would have built the very thing S1 forbids — and it stranded
  sibling `-3`'s AC7 and AC8 on a file that no longer exists. AC14 was also unfalsifiable as written:
  under a per-run directory a plant made before the run starts lands where the run never looks, so
  the arm passed by finding nothing. It now pins the run id through a seam and plants inside that
  exact directory. S5's fingerprint becomes a shipped executable rather than a private function,
  because `TOOL-aPacedTurnstile-7` predicate 0 must compute the same digest from a git hook and two
  implementations of one digest is the two-answers-to-one-question class.
- rev-2 · 2026-08-18 · folded the spec audit. The record directory becomes PER-RUN: at a fixed path
  a leftover completion file is not a stale log but a stale DISPATCH SUPPRESSOR, so the leg never
  runs and the bar prints it green — and two sibling units add exactly the writers that outlive a run
  (BLOCKER F2). `gate-full-green` gains a fifth precondition, a CLEAN tree at start, without which a
  developer's ordinary dirty-tree full run stamps a green the push boundary treats as proof about a
  tree nobody tested (BLOCKER F5). The failed-nothing precondition gains the negative control it was
  the only one of the five to lack (BLOCKER F3). The header gains the dispatch-order and
  forced-reason keys two siblings read (F13, F25), and the retargeted per-leg output copy inherits
  the redaction its sibling log already has (F39).
- rev-4 · 2026-08-18 · swept section 8 under the standing mandate: every fork RESOLVED in
  place per M3, and the section's first non-blank line made machine-legal so the classifier
  reads this unit as READY instead of FORKED.
- rev-5 · 2026-08-18 · folded the round-2 spec audit. R2/R3: the two directory lifetimes are now
  stated separately with an owner each — the EXIT trap keeps the `mktemp -d` scratch and stops
  covering `<git-dir>/gate-run/`, whose only deleter is the post-verdict sweep — because
  `TOOL-aPacedTurnstile-4` had claimed the cleanup line for a widened trap over the record, lands
  sixth, and would have erased the record on every ordinary exit and every caught signal. §4's bare
  "drop the trap" and Rollout's "restoring the trap" are narrowed to match. R6: §8's first
  resolution is CORRECTED — this run's own sweep ratified a pre-fold option set and credited F2's
  closure to clearing, which re-licensed the branch the fold-in removed and which AC14 cannot
  detect; the answer is now per-run directories with a post-verdict sweep, and AC15 grades its
  bound. R19: S5's helper is named `tools/run-gates/gate-fingerprint.sh` and added to Files touched,
  so `-7`'s builder has a path to call rather than an incentive to reimplement the digest. R24: §5's
  security line said the new files carry no command output while S3 said they do; corrected, with
  AC16 observing the masking and both modes. R4/R5: AC12 gains the registry clause and the counters
  move to `-1`, which owns the waiver rows.
- rev-6 · 2026-08-18 · folded round 3's BLOCKER T1/T2/T3, which is the R1 fix not landing whole.
  R19 gave `gate-fingerprint.sh` a name and nobody gave it a SIGNATURE, so `-7`'s corrected
  predicate 0 named a computation this interface could not perform. S5 now declares two forms of one
  implementation — no argument for the runner's working-tree stamp, `<rev>` for the hook's
  recomputation, the working-tree components supplied EMPTY rather than omitted so both hash the
  same arity — with the binding property that on a clean tree they are EQUAL, which is what makes
  S7's clean-at-start refusal the thing that guarantees every recorded digest is reproducible at its
  own sha. AC17 arms both halves. T14/T21: the retention bound R6 asked for is declared as
  `GATE_RUN_KEEP=5` with its reasoning, in `-4` S8's shape, and AC15 grades it by name instead of
  grading a declaration nothing made.
- rev-7 · 2026-08-18 · folded round 4. V2: AC17 named the argument-ignoring hazard in its own text
  and then armed only the worktree-reading half of it — both its invocations were at HEAD, so a
  helper computing at HEAD unconditionally and reading only the ARGUMENT COUNT passed both halves
  with the parameter dead, which is exactly the shape that restores round 2's blocker. A third
  invocation at a rev whose tree differs is now the one assertion in the set that binds the argument.
  V3: S7 defines CLEAN as `git status --porcelain` EMPTY with untracked included — the same predicate
  the fingerprint's own porcelain component uses — because S5's whole binding property rests on it
  and nothing in the set defined the word; the `git diff --quiet` reading would record a digest the
  rev form can never reproduce. AC13 gains the untracked-only fixture that separates the two
  definitions. V4: §4's row for the evidence suite names `TOOL-aPacedTurnstile-7`'s cross-unit AC6d
  arm, so the file has one ownership statement rather than two units editing it silently.
- rev-8 · 2026-08-20 · folded the owner's re-scope, which re-grounded all five unbuilt units against
  what `-1` and `-2` actually landed. The forcing finding for THIS unit is that three things landed
  under its feet while it sat at rev-7, and two of them made a scope item wrong rather than merely
  dated. `aMeteredTurnstile` shipped `profile_bar.py`, which resolves `gate-timings.tsv` at a
  hardcoded path and REFUSES when the file's mtime did not move; S6's compatibility argument surveyed
  the runner's own parser, found it unaffected, and was complete when it was written and incomplete by
  the time it was read — so retiring the cache silently would not have degraded the profiler, it would
  have turned a green leg's subject into a tool that refuses on every invocation. S6 now takes the
  profiler's three touch points into its own Files-touched table on the authority of
  `aMeteredTurnstile`'s own pledge to switch. `-2` replaced the computed pool width with a DECLARED
  row carrying a name, a timeout and a detection source, and S2's key list still said "the resolved
  width", which records the number and discards the three facts that explain it; the header now
  carries the four components `PROF_LINE` already composes, and AC19 grades them across two differing
  profile rows because one fixture cannot tell a recorded envelope from a hardcoded catch-all. `-1`
  split the canary and reserved the gov-only half for corpus-keyed arms, so S10's single item was
  really two: the key-set pin is schema and stays in the shipped file reading the DERIVED manifest,
  while the half that would have named gov's legs is CUT, because the re-scope cut the predicate it
  policed on the evidence that the predicate matched six legs and every one of them was hermetic.
  AC12 is CUT for the reason this spec's own §7 gives against green-by-absence: `-1` landed both
  assertion floors and left no registry row for either harness, so the criterion was green before this
  unit started and could not fail from anything it does; §5's testing line carries the live obligation
  instead. Under D1 every pinned figure went: the leg count is derived rather than stated (70 at
  drafting, 86 re-derived at `43a6c13` on 2026-08-20), the eight concurrent writers become the width
  the selected profile row declares, and the fingerprint's 0.41 s becomes 0.44 s carrying its node,
  sha and date — a figure that moves with the size of the working tree and should be re-run, not
  quoted. Two dead pointers repaired: the `AGENTS.md` row named a durable-evidence bullet `-1`
  dissolved into the "How the bar behaves" prose, and AC7 and AC10 both hashed the literal gov
  manifest inside harnesses that SHIP and that drive the runner against fixtures, which grades a file
  the run under test never opened. S5 gained the shipping decision its path implied but never stated,
  and the `impure`-cannot-travel finding is recorded in S8 with its consequence carried to §8 as the
  build's one open fork rather than resolved by this unit, which does not own the reuse verb. The
  order edge changed: this unit is now FIRST, `-4` follows it immediately instead of four units later,
  and the separate-trap-owners statement in S1 is more load-bearing for it. `base` is deliberately
  unchanged — it is the sha this design was grounded against, and the re-scope's figures carry
  `43a6c13` on their own faces instead of rewriting it.

## 10. Reuse audit

The seam this extends is the worker's existing per-leg completion protocol in
`tools/run-gates/run-gates.sh` — output, then duration, then an atomic temp-then-rename commit. That
IS the emitter; this unit retargets it and adds the two bookends. The key-per-line grammar and its
fork-free reader come from `tools/unattended/unattended.sh`, cited rather than reinvented. The
durable-evidence guarantee and its harness are `TOOL-dNomadicAtlas-1`'s, already gated by
`tools/run-gates/run-gates.evidence.test.sh`, which is where this unit's arms land. The
carry-forward merge on the timing cache is review finding F6 from the aTimedTurnstile review and is
preserved verbatim.

A fourth prior arrived after this audit was first written and is both nearest neighbour and downstream
consumer: `tools/run-gates/profile_bar.py`, from the sibling build `aMeteredTurnstile`. It writes an
overlapping envelope — sha, host, width, width source, full-run flag, wall clock, exit and per-leg
durations — and it does NOT deliver this unit, for reasons that are this spec's own: it composes its
record after the run finishes, so the crash case is exactly where it has nothing; no leg can read it
in flight; it carries no per-leg input key, no full-green stamp and no tree fingerprint; and on an
anomaly it refuses and records nothing at all. It is prior art for the envelope keys and it is the
tool S6 migrates, and its own spec already pledges to read this unit's ledger and delete its wrapping
path once this lands, which is why S6 takes the edit rather than leaving a shim.

Recall terms used: gate, leg, verdict, reuse, cache, lock, beacon, queue, concurrent, session,
worktree, scoped, diff, GATE_FULL, guard, skip. The probe returned the aTimedTurnstile review's F6
(the cache rewrite dropping skipped legs' rows, preserved here), `TOOL-dNomadicAtlas-1` (durable
per-leg evidence, the seam extended) and `TOOL-aLeasedGauntlet-1` S3 (the durable summary this
record joins).
