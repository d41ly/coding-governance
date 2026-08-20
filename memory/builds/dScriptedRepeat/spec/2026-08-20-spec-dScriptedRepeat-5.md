# TOOL-dScriptedRepeat-5 — the per-piece record: its writer, its reader, and its states

**Status:** SPECCED · rev-3 · 2026-08-20 · node d · Tier-2 · base d2a40aa8 · streams tooling · ratified 2026-08-20

## 1. Goal

Define the per-piece evidence record as a TRACKED artifact hash-joined to the piece it describes, the
VERB that writes it, and the reader that classifies it — so a merge-bar leg can read it with no
run-state file in sight, which is what makes fork 1's "ONE gate" true across both entry points.

## 2. Scope (IN)

- **S1.** The RECORD: one tracked file per piece, at a path DERIVED from the piece's own path, holding
  the piece's content hash, the playbook blob sha it was made under, each declared per-piece leg with
  its verdict, and each `CHECK` step with its verdict and witness where one was declared.
- **S2.** THE WRITER, and it is a scope item because the previous revision had four readers and no
  writer at all. A driver verb, `--record-piece <slug> --path <p> --leg <name> --verdict <v>`, reusing
  `verb_park`'s newline refusal, its ` · ` separator refusal, its bypass-flag refusal over every field,
  its exact-line idempotence and its `stage_or_fail`. A record written by hand is possible and is
  exactly what the hash join makes detectable when the piece then changes; a record with no writer is
  a requirement nothing can meet.
- **S3.** THE ATTENDED WRITER. The verb refuses with no run-state file, exactly as `verb_park` does, so
  it is unattended-only. The attended path therefore gets a second entry point to the SAME writer
  function that takes the playbook path explicitly instead of a slug. One writer, two callers — never
  two implementations, which would be the second-implementation-is-not-a-second-opinion class.
- **S4.** The HASH JOIN, answering PROVENANCE: does this record describe the piece as it stands?
- **S5.** THE VERDICT TERM, answering DONENESS: did every declared per-piece leg record a PASS? These
  are two questions and they get two terms. The previous revision derived all states from the join
  alone, which made `verified` a semantic word for a structural state — and since unit 6 keys "the
  build made what was asked" on that word, fork 5 was implemented by nothing.
- **S6.** THE FIVE STATES: `verified` (joined AND every declared leg PASS), `failed` (joined, a leg
  recorded FAIL), `stale` (record present, hash mismatch), `unrecorded` (piece present, no record),
  `orphan-record` (record present, piece gone). Five messages, never a boolean.
- **S7.** TWO NAMED ENUMERATION SCOPES, because unit 6 needs to distinguish them and the previous
  revision offered only one: `enumerate_run` (the declared grain intersected with the paths this run
  introduced, per unit 8's population) and `enumerate_corpus` (the grain over the whole tree).
- **S8.** THE LIVENESS ASSERTION. The reader reports how many pieces it ENUMERATED alongside how many
  it verified, per scope. A zero-piece enumeration reports as a dead probe, never as a clean run.
- **S9.** THE GRADING RULE, which the audit found undefined. The READER classifies and never grades.
  `check-playbook.sh` reports `stale` and `failed` with their counts and does not red on them alone;
  only `pieces-complete` at `--close` treats them as blocking. This resolves the two-moment question
  the previous revision deferred to unit 6, which answered only the close half.
- **S10.** Independence from the run-state file. The reader takes the playbook path and BASE as
  arguments and touches no `RUN.md`.
- **S11.** Arms: each of the five states; the zero-piece dead probe; the reader running with no
  run-state file; a record written by the VERB and not by hand; a stale piece NOT redding the bar.

## 3. Non-goals (OUT)

- The record does not carry the piece's CONTENT, a review write-up, or prose. It carries verdicts and
  joins. A large body goes in the build folder where records already live.
- No opinion on WHO ran the legs. That is the attended/unattended difference and this unit is the
  thing both share — which is why S3 gives the writer two callers rather than two implementations.
- No change to the run-state file's grammar.

## 4. Design

### Why a tree property rather than a run-state region

The research proved an attended run cannot close through the driver: the leg refuses a run-state file
recording no BASE, and every run-state-keyed check sees nothing when no such file exists. So evidence
living in `RUN.md` is evidence only an unattended run can produce. Moving the per-piece record into the
tracked tree makes the evidence a property of what SHIPPED rather than of who invoked the run, which is
also the more honest thing to gate on.

### Provenance and doneness are two questions

The hash join says "this record describes this piece". It says nothing about whether the piece is any
good, and `verified` reading as though it did was the defect the audit named. So `verified` now
requires both terms and `failed` exists to name the gap. This is what makes fork 5 — "piece-done is its
declared legs green" — actually implemented rather than merely cited.

### The liveness assertion is the load-bearing part

Every other control here can be satisfied by a tree with no pieces in it. A reader that enumerates
zero, joins zero and reports zero failures is indistinguishable from a clean run. So the reader reports
the ENUMERATION COUNT first, per scope, and a zero enumeration is a dead probe with its own message.
Two zero-states stay distinct and both must survive: no playbook at all is not the same fact as a
declared grain resolving to zero pieces, and the leg's exit code differs.

### Alternatives rejected

**A region in the build README.** The README's generated regions are rendered from spec front matter by
a generator that knows nothing about pieces, and a fifth region would put piece evidence inside the
artifact the authorization compares across BASE.

**A single manifest file listing all pieces.** One file every piece-pass rewrites is a shared mutable
index, which the charter bans by name and which would serialise otherwise-independent passes.

**Trusting a per-piece line in the run-state file.** S10's whole reason.

## 5. Production-readiness checklist

- security — the record is written by the run and read by the leg, so protocol §9's reduction applies:
  it is a record, not a proof. The hash join raises the cost of a false record from editing one line to
  editing one line AND keeping a hash consistent, which is a cost and not a barrier. The writer's reuse
  of `verb_park`'s refusals is the security-relevant part, and each of those refusals exists because of
  a recorded defect.
- perf / scale — one hash per piece per leg run, two enumerations.
- a11y — N/A.
- i18n — piece paths may be non-ASCII; the join is on bytes and the reader must not normalise.
- error / empty / loading states — the five states ARE this row, plus the dead-probe report per scope
  and the two distinct zero-states named in §4.
- observability — the reader prints the five counts per scope on every run.
- risks — a grain glob matching too broadly inflates the enumeration and looks like MORE coverage. The
  compensating controls are unit 4's refusal of an unresolvable grain and unit 6's comparison against a
  declared N.
- testing + left-shift gates — S11, and specifically the zero-piece arm, which proves the liveness
  assertion is armed, and the written-by-the-verb arm, which proves S2 exists.
- migration / rollback — new artifacts. A tree with no pieces and no records reports through the leg's
  real verdict channel, whose exact exit code and bar line unit 3 owns.
- user docs — the template's section 4 documents what a piece is; the record's own header documents its
  five states.

## 6. Acceptance criteria

- **AC1** — When a piece and its record agree on the content hash AND every declared per-piece leg is
  recorded PASS, the reader classifies it `verified`. Observed via
  `bash tools/unattended/check-playbook.sh`.
- **AC2** — When a piece is edited after its record is written, the reader classifies it `stale`, with
  a message distinct from `unrecorded`. Staged and observed.
- **AC3** — When a record is deleted, its piece classifies `unrecorded`.
- **AC4** — When a piece is deleted and its record survives, the record classifies `orphan-record`.
- **AC5** — When a record is hash-fresh and carries a FAILING leg verdict, the reader classifies it
  `failed`, distinct from all four other states. Staged and observed.
- **AC6** — When the declared grain enumerates ZERO pieces, `bash tools/unattended/check-playbook.sh`
  reports a DEAD PROBE per scope and does not report a clean run.
- **AC7** — When the reader runs in a tree containing no run-state file at all,
  `bash tools/unattended/check-playbook.sh` completes and reports the same five counts. Observed,
  because this is the property the attended path depends on.
- **AC8** — When a record is written by `--record-piece`, it is staged and idempotent on re-issue
  against an EXACT line compare; and when the verb runs with no run-state file it REFUSES, while the
  attended caller of the same writer function succeeds. Two arms.
- **AC9** — When a piece is `stale`, `bash tools/unattended/check-playbook.sh` reports it and does NOT
  red; the same tree at `--close` BLOCKS. Two observations of one state, which is S9's whole point.
- **AC10** — When a piece path contains a non-ASCII byte, the join still resolves, verified by an arm in
  `check-playbook.test.sh` rather than assumed.

## 7. Gates

`bash tools/unattended/check-playbook.sh` · `bash tools/unattended/check-playbook.test.sh` ·
`bash tools/unattended/unattended.test.sh` for the writer verb ·
`bash tools/unattended/cross-component.test.sh` · `bash tools/run-gates/run-gates.sh`.

## 8. Open questions

none — every fork below is RESOLVED in place.

- **F1 — where the per-piece record physically sits.** RESOLVED (agent, 2026-08-20, delegated): under
  the build folder, at a path derived from the piece's repo-relative path. The output tree is the
  DELIVERABLE, and a governance artifact sitting in it is the thing an owner will delete.
- **F2 — should `stale` RED or WARN?** RESOLVED (agent, 2026-08-20, delegated) in S9: the reader
  classifies and never grades; the leg warns with a count; `--close` blocks. The previous revision
  deferred this to unit 6, which answered only the close half and left the leg's mid-fold verdict
  undefined — the audit caught the gap and the ruling now lives where the reader lives.

## 9. Revision log

- rev-3 · 2026-08-20 · pre-code fork sweep under the mandate (M3). Every §8 fork RESOLVED in
  place with its resolver and authority named, and §8's first non-blank line made machine-legal —
  the driver classified nine of eleven specs FORKED on that line alone.
- rev-1 · 2026-08-20 · initial draft. The tree-property design was ruled by the owner after the research
  proved an attended run cannot close through the driver.
- rev-2 · 2026-08-20 · folded the M4 spec audit. F6 added S2 and S3, the writer and its second caller —
  the largest gap in the set, since four units read a record nothing wrote. F5 split provenance from
  doneness and added the `failed` state, without which `pieces-complete` was met by N pieces whose every
  leg had failed. F2 added the two named enumeration scopes. F7 moved the grading ruling here as S9.
  F11 replaced the bare word "skipped" with a pointer at unit 3's real verdict channel.

## 10. Reuse audit

The HASH JOIN is prior art in this fleet twice over: the reference corpus's review records bind a
verdict to the body it reviewed by content hash, and this repo's own gate-freshness checks compare a
recorded tree fingerprint against a re-derivation at the sha it names. Both establish that a verdict
with no join to what it judged is a verdict about nothing. The WRITER reuses `verb_park` wholesale —
its three refusals, its exact-line idempotence, its `stage_or_fail` — each of which exists because of a
recorded defect, and the audit's finding that this unit previously had no writer is the reason that
reuse is now a scope item rather than an aside. The FIVE-STATE classification rather than a boolean
follows the DoD evaluation code's own repair, where ANDed terms were split so each could say which one
failed. The LIVENESS ASSERTION is `drift-audit`'s shape, copied because the alternative was measured to
be indistinguishable from success. Recall terms used: record verdict hash join provenance doneness
stale orphan failed enumeration scope run corpus liveness dead probe reader writer verb tracked
artifact merge bar leg run state independence.
