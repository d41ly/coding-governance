# TOOL-aPacedTurnstile-5 — the run record: a durable, machine-readable status emitter

**Status:** OPEN · rev-2 · 2026-08-18 · node a · Tier-2 · base 6517579f · streams tooling

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
  the `mktemp -d` it replaces already does; retention of older run dirs is bounded by a sweep.
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
  Over-sensitive by construction, never under-sensitive; empty on any failure.
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

So the emitter is not a new subsystem. It is: retarget the directory, drop the trap, add a header
before dispatch and a verdict after.

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

`<git-dir>/gate-run/header` exists to prove the run started; its absence proves nothing ran. Keys are
listed in S2.

`<git-dir>/gate-run/<i>.leg` is keyed on the manifest INDEX, which is stable within a run and
lossless, with the leg name carried inside the row — so a slug-safe filename can never mis-attribute
a verdict. Status is one of ok, fail, skip, reuse; a skipped row carries a dash for rc and key.

`<git-dir>/gate-run/verdict` is written last and carries the tallies.

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

One commit. Rollback is restoring the trap and the scratch destination; the record is additive and
nothing reads it until `TOOL-aPacedTurnstile-6` lands.

### Files touched (estimate)

| file | change |
|---|---|
| `tools/run-gates/run-gates.sh` | destination, trap, header, per-leg row, verdict, fingerprint, ledger |
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

- security — the record carries paths and leg names, no credentials; the existing redaction on the
  per-leg logs is untouched and the new files carry no command output.
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

- **AC1** — When a run is in flight, a leg can read `<git-dir>/gate-run/header` and see this run's
  id — asserted by a fixture leg in `tools/run-gates/run-gates.evidence.test.sh`.
- **AC2** — When the runner is killed mid-run with `timeout -s KILL`, `<git-dir>/gate-run/header`
  exists and `<git-dir>/gate-run/verdict` does not.
- **AC3** — When a run completes, `<git-dir>/gate-run/` holds one `.leg` row per non-sentinel leg,
  and each row's first field equals the manifest name at that index.
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
- **AC14** — When a stale completion file for leg index 3 is planted before a run starts, that leg
  still EXECUTES and its reported verdict is the one it produced this run — asserted in
  `tools/run-gates/run-gates.evidence.test.sh`, because the completion file suppresses dispatch and a
  stale one would print a green nobody earned.
- **AC12** — When `bash tools/check-testsuite-counts.sh` runs, both moved harnesses report their
  executed assertion counts at or above their floors.

## 7. Gates

`bash tools/run-gates/run-gates.test.sh` · `bash tools/run-gates/run-gates.evidence.test.sh` ·
`bash tools/check-testsuite-counts.sh` · `python tools/govkit/govkit.py selfcheck` ·
`bash tools/memory-tree/check-memory-hygiene.sh` · `python tools/memory-tree/check-arms.py --check`.

## 8. Open questions

- **Whether the record directory is cleared at the start of a run or kept as a rolling history.**
  Options: clear each run (one run's state, simple, and the crash signal stays unambiguous), or keep
  N runs. Recommendation: clear. The ledger already carries cross-run history keyed per leg, and a
  rolling directory needs a retention policy nobody has asked for.
- **Whether `impure` carries reason strings or a bare boolean.** Recommendation: reason strings. A
  bare `true` is a claim with no evidence beside it, and this tree's settled pattern for a waiver is
  that it names its reason.

## 9. Revision log

- rev-1 · 2026-08-18 · initial draft.
- rev-2 · 2026-08-18 · folded the spec audit. The record directory becomes PER-RUN: at a fixed path
  a leftover completion file is not a stale log but a stale DISPATCH SUPPRESSOR, so the leg never
  runs and the bar prints it green — and two sibling units add exactly the writers that outlive a run
  (BLOCKER F2). `gate-full-green` gains a fifth precondition, a CLEAN tree at start, without which a
  developer's ordinary dirty-tree full run stamps a green the push boundary treats as proof about a
  tree nobody tested (BLOCKER F5). The failed-nothing precondition gains the negative control it was
  the only one of the five to lack (BLOCKER F3). The header gains the dispatch-order and
  forced-reason keys two siblings read (F13, F25), and the retargeted per-leg output copy inherits
  the redaction its sibling log already has (F39).

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
