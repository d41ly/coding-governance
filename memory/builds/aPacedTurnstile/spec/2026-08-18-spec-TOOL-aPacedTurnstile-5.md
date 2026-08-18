# TOOL-aPacedTurnstile-5 — the run record: a durable, machine-readable status emitter

**Status:** OPEN · rev-5 · 2026-08-18 · node a · Tier-2 · base 6517579f · streams tooling

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
  the `mktemp -d` it replaces already does; retention of older run dirs is bounded by a sweep that
  runs AFTER the verdict file is written, never before the first leg dispatches.
  **The two directories have separate lifetimes and separate owners, and round 2's R2/R3 are why
  this is now stated rather than implied.** `<git-dir>/gate-run/` is the DURABLE record: this unit
  owns it, the EXIT trap stops covering it, and the only deleter is the post-verdict sweep named
  above. The `mktemp -d` scratch survives this unit — it still holds the timings temporaries — and
  the trap goes on covering it; `TOOL-aPacedTurnstile-4` widens that trap to INT, TERM and HUP and
  its scope is the SCRATCH dir alone. A trap that swept `<git-dir>/gate-run/` would erase the record
  on every ordinary exit and on every caught signal, which is every path except the crash the record
  exists to make readable, and `-4` lands sixth so it would win by default. Nothing clears the
  record at the START of a run: per-run uniqueness is what closes blocker F2, and a start-of-run
  clear can partially fail on this platform against an open handle or an AV lock and inherit the
  previous run's verdicts — the exact branch F2 named.
- **S2** — `<git-dir>/gate-run/<run-id>/header` is written BEFORE the first leg dispatches, in a
  key-per-line grammar, carrying the schema version, run id, start time, head, base and how the base
  was resolved, the tree fingerprint, whether the tree was CLEAN at start, the manifest path and its
  blob hash, the full-run flag and the reason it was forced, the resolved width, the resolved
  DISPATCH ORDER, the leg count, and the worktree path. The dispatch order is here rather than in
  `TOOL-aPacedTurnstile-3` because this unit already writes the header at the point that value is in
  scope, and a record's key set must stay single-sourced; that unit's ordering criteria read it.
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
  Over-sensitive by construction, never under-sensitive; empty on any failure. It ships as
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
- **S6** — `<git-dir>/gate-ledger.tsv` replaces the timing cache: rows gain status, input key and a
  timestamp while KEEPING the duration in field 2, so the existing dispatch-order parser needs no
  edit. The carry-forward merge for guard-skipped legs is kept exactly as written, and the rewrite
  becomes an atomic rename rather than a copy.
- **S7** — `<git-dir>/gate-full-green` is written ONLY when the run failed nothing, skipped nothing,
  reused nothing, the tree did not move, AND the tree was CLEAN when the run started. This is the
  file `TOOL-aPacedTurnstile-7` reads, and those five preconditions are what make it mean what its
  name says. The clean-tree precondition is the one the spec audit found missing: a developer's
  ordinary full run on a dirty tree would otherwise stamp a green that the push boundary then treats
  as proof about a tree nobody ever tested. Each precondition carries its own negative control,
  because an implementation that forgets ONE of them passes every arm written for the others.
- **S8** — `tools/gate-legs.json` gains an optional `impure` key carrying reason strings, seeded from
  MEASUREMENT rather than guess: the unattended legs call out to the remote, so their verdicts are a
  function of the remote as well as of the tree.
- **S9** — record arms in `tools/run-gates/run-gates.evidence.test.sh`: the header is readable BY A
  LEG while the run is in flight, the verdict file is absent after a hard kill, a red leg's ledger
  row carries no reusable key, and a corrupt ledger is survived.
- **S10** — a canary arm pinning the manifest's known key set, so a mistyped `impure` cannot silently
  make a network-reading leg reusable.

## 3. Non-goals (OUT)

- Consuming the record. Reuse, resume and the base change are `TOOL-aPacedTurnstile-6`; the push
  boundary is `TOOL-aPacedTurnstile-7`. This unit writes and declares, and changes no verdict.
- JSON or JSONL. See the format argument below.
- A lock. One file per writer needs none, and `flock` does not exist on this platform.
- A new leg, a new process, or a daemon.
- Committing any of this. The record lives in the git dir, which is already where the summary,
  the failure record and the per-leg logs live.

## 4. Design

### The question, answered first: what is the best way to implement a status emitter?

**A directory of small append-once files under `<git-dir>/gate-run/`, written by the workers that
already write them, plus one keyed TSV ledger.** No JSON, no JSONL, no lock, no new process, no new
leg. Three requirements decide it before taste gets a vote.

Surviving a crash means the record is written INCREMENTALLY — a single document composed at the end
is lost precisely in the case it exists for. Eight concurrent writers mean an incrementally-written
SHARED file needs a lock, and there is none available here; one file per writer needs no lock at
all, because the atomicity is the filesystem's rename rather than ours. And it already exists: the
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

The per-leg rows are TSV instead, because they are single-line and written seventy times. Verified
against the manifest: no leg name contains a tab, a newline or a colon, and all seventy are unique.

### Data model

Every path below sits under the PER-RUN directory `<git-dir>/gate-run/<run-id>/`, and
`<git-dir>/gate-run/current` is a pointer to the in-flight one. The flat spelling is deliberately
absent: a completion file at a fixed path is a stale DISPATCH SUPPRESSOR, and that is the whole of
blocker F2. A reader that wants the live run resolves `current` first.

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
blob hashes of every dirty-or-untracked file that still exists. Measured on this repo: the status
plus hash-object pass completes in 0.41 s, once per run rather than per leg.

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
Capturing the fingerprint again at the end costs 0.4 s and is the difference between a green that
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

### Files touched (estimate)

| file | change |
|---|---|
| `tools/run-gates/run-gates.sh` | destination, trap narrowing, header, per-leg row, verdict, ledger, post-verdict sweep |
| `tools/run-gates/gate-fingerprint.sh` | NEW — S5's digest, shipped as its own executable and called by the runner and by `.githooks/pre-push` |
| `tools/run-gates/run-gates.evidence.test.sh` | S9's arms |
| `tools/run-gates/run-gates.test.sh` | S10's pinned key set |
| `tools/gate-legs.json` | the `impure` key on the measured legs |
| `AGENTS.md` | the durable-evidence bullet gains the record |

### Alternatives rejected

- **Append-only JSONL from every worker.** Rejected: interleaved writes from eight processes to one
  descriptor are not atomic beyond a pipe buffer, and there is no lock available.
- **One JSON document written at the end.** Rejected: lost in the crash case it exists for.
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
- perf / scale — 0.41 s for the fingerprint, twice per run; per-leg rows are one line each.
- a11y — N/A: no user interface.
- i18n — N/A: machine-readable keys and operator-facing English.
- error / empty / loading states — an in-flight run is exactly "header present, verdict absent", and
  that is the crash signal too; an arm asserts it after a hard kill.
- observability — this unit IS the observability.
- risks (concurrency, data-loss, rollback hazards) — the record is per-worker single-writer, so
  concurrency needs no lock. Data loss is bounded to the current run. The one real hazard is a stale
  record read by a later consumer, which is why the tree fingerprint and the manifest blob are both
  in the header.
- testing + left-shift gates — the pinned key set left-shifts the mistyped-declaration class.
- migration / rollback — the ledger supersedes the timing cache; an absent or corrupt ledger costs
  dispatch order only, which the existing arm already gates.
- user docs — the charter's durable-evidence bullet.

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
  `<git-dir>/gate-full-green` is written and its `manifest_blob` equals
  `git hash-object tools/gate-legs.json`.
- **AC8** — When a run is green but ANY leg was skipped, `<git-dir>/gate-full-green` is NOT written
  or updated — the precondition that makes the file's name true.
- **AC9** — When the working tree is modified while the run is in flight, the verdict file records
  the tree as moved and `<git-dir>/gate-full-green` is not written.
- **AC10** — When a leg row in `tools/gate-legs.json` carries a key outside the pinned known set,
  `bash tools/run-gates/run-gates.test.sh` exits non-zero naming that key.
- **AC11** — When a run REDS, `<git-dir>/gate-full-green` is neither written nor updated, asserted in
  `tools/run-gates/run-gates.evidence.test.sh` against a pre-existing file from an earlier green — so
  the arm distinguishes not-written from not-updated. This is the precondition the push-boundary
  inversion rests on and it was the only one of the five with no negative control.
- **AC13** — When the working tree is DIRTY at the start of an otherwise fully green run,
  `<git-dir>/gate-full-green` is not written, asserted in
  `tools/run-gates/run-gates.evidence.test.sh`.
- **AC14** — When the run id is pinned through a test seam and a stale completion file for leg index
  3 is planted INSIDE that exact run directory before the run starts, that leg still EXECUTES and its
  reported verdict is the one it produced this run — asserted in
  `tools/run-gates/run-gates.evidence.test.sh`. The seam is load-bearing for the ARM, not for the
  runner: without a pinned id the plant lands in a directory the run never opens, so the arm passes
  by finding nothing and proves the opposite of what it claims. A second plant at the retired FLAT
  path must also be ignored.
- **AC15** — When a run completes, run directories older than the declared retention bound are gone
  and the current one and its predecessor remain, asserted in
  `tools/run-gates/run-gates.evidence.test.sh` against a fixture carrying more than the bound. Its
  control is the same fixture with the run KILLED before the verdict is written: nothing is swept,
  because the sweep runs after the verdict and never before dispatch. Without this pair the bound S1
  states has no owner and the record grows without limit (round 2's R6).
- **AC16** — When a fixture leg emits a token the runner's redaction masks, the DURABLE per-leg
  output copy under the run directory contains only the masked form, and both that file's mode and
  the run directory's mode are the restrictive ones the existing per-leg log already uses — asserted
  in `tools/run-gates/run-gates.evidence.test.sh`. Its control is the same fixture with the masking
  removed, which must red. S3 made this copy durable and §5 said the new files carried no command
  output; the criterion is what stops the two from disagreeing again (round 2's R24).
- **AC12** — When `bash tools/check-testsuite-counts.sh` runs, both moved harnesses report their
  executed assertion counts at or above their floors, and the count registry carries no row naming
  either of them. Round 2's R4/R5 found this unsatisfiable while `TOOL-aPacedTurnstile-1` S11 kept
  both rows: satisfying the count reds the registry's staleness arm the other way, so there was no
  green state. The counters and BOTH row deletions now land together in `-1`, which owns the move
  and the rows; this criterion is unchanged in substance and gains only the registry clause that
  makes the join visible from this side.

## 7. Gates

`bash tools/run-gates/run-gates.test.sh` · `bash tools/run-gates/run-gates.evidence.test.sh` ·
`bash tools/check-testsuite-counts.sh` · `python tools/govkit/govkit.py selfcheck` ·
`bash tools/memory-tree/check-memory-hygiene.sh` · `python tools/memory-tree/check-arms.py --check`.

## 8. Open questions

none — the forks below are RESOLVED. Every pick is the M3 ratification of the fork's own
recommendation; the reason each survived the veto order is recorded with it.

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

## 10. Reuse audit

The seam this extends is the worker's existing per-leg completion protocol in
`tools/run-gates/run-gates.sh` — output, then duration, then an atomic temp-then-rename commit. That
IS the emitter; this unit retargets it and adds the two bookends. The key-per-line grammar and its
fork-free reader come from `tools/unattended/unattended.sh`, cited rather than reinvented. The
durable-evidence guarantee and its harness are `TOOL-dNomadicAtlas-1`'s, already gated by
`tools/run-gates/run-gates.evidence.test.sh`, which is where this unit's arms land. The
carry-forward merge on the timing cache is review finding F6 from the aTimedTurnstile review and is
preserved verbatim.

Recall terms used: gate, leg, verdict, reuse, cache, lock, beacon, queue, concurrent, session,
worktree, scoped, diff, GATE_FULL, guard, skip. The probe returned the aTimedTurnstile review's F6
(the cache rewrite dropping skipped legs' rows, preserved here), `TOOL-dNomadicAtlas-1` (durable
per-leg evidence, the seam extended) and `TOOL-aLeasedGauntlet-1` S3 (the durable summary this
record joins).
