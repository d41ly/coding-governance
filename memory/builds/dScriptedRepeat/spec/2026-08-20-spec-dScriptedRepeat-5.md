# TOOL-dScriptedRepeat-5 — the per-piece record as a property of the TREE

**Status:** SPECCED · rev-1 · 2026-08-20 · node d · Tier-2 · base d2a40aa8 · streams tooling

## 1. Goal

Define the per-piece evidence record as a TRACKED artifact hash-joined to the piece it describes, so a
merge-bar leg can read it with no run-state file in sight — which is what makes fork 1's "ONE gate"
literally true across an unattended entry point and an attended one.

## 2. Scope (IN)

- **S1.** The RECORD: one tracked file per piece, at a path DERIVED from the piece's own path, holding
  the piece's content hash, the playbook blob sha it was made under, each declared per-piece leg with
  its verdict, and each `CHECK` step with its verdict and witness where one was declared.
- **S2.** The HASH JOIN. The record names the piece's content hash. A record whose hash does not match
  the piece as it stands in the tree is STALE, and stale is a distinct verdict from absent — the
  research's strongest recurring lesson is that two failure states collapsed into one message send a
  reader to the wrong repair.
- **S3.** The READER: a function in the leg that enumerates pieces by the declared grain, joins each to
  its record, and classifies every piece as `verified`, `stale`, `unrecorded` or `orphan-record`. Four
  states, never a boolean.
- **S4.** The LIVENESS ASSERTION. The reader reports how many pieces it ENUMERATED alongside how many
  it verified. A zero-piece enumeration reports as a dead probe, never as a clean run. This is the
  charter's rule and it is the single control that stops this whole unit from being satisfiable by an
  empty tree.
- **S5.** Independence from the run-state file. The reader takes the playbook path and BASE as
  arguments and touches no `RUN.md`. Verified by an arm that runs it in a tree containing no
  run-state file at all.
- **S6.** Arms: a matching record verifies; an edited piece goes stale; a deleted record goes
  unrecorded; a record naming a piece that no longer exists is an orphan; the zero-piece case reports
  dead-probe; the whole reader runs green with no run-state file present.

## 3. Non-goals (OUT)

- The record does not carry the piece's CONTENT, a review write-up, or prose. It carries verdicts and
  joins. A large body goes in the build folder where records already live.
- The record is not authored by hand. It is written by whatever ran the legs, and unit 7 and unit 6
  read it. A hand-written record is possible and is exactly what the hash join makes detectable when
  the piece then changes.
- No opinion on WHO ran the legs. That is the attended/unattended difference and this unit is the
  thing both share.
- No change to the run-state file's grammar.

## 4. Design

### Why a tree property rather than a run-state region

The research proved an attended run cannot close through the driver: the leg refuses a run-state file
recording no BASE, and every run-state-keyed check sees nothing when no such file exists. So evidence
living in `RUN.md` is evidence only an unattended run can produce, and fork 1's "ONE gate" would have
meant one gate plus an honour system. Moving the per-piece record into the tracked tree makes the
evidence a property of what SHIPPED rather than of who invoked the run, which is also the more honest
thing to gate on.

### The four states, and why not two

`verified` and `unrecorded` are the obvious pair. `stale` is what a hash join buys and is the state a
boolean loses: a piece edited after its record was written looks exactly like a verified piece to a
presence check. `orphan-record` catches the reverse — a record for a piece that was deleted or renamed
— which is how a corpus silently reports coverage it no longer has.

### The liveness assertion is the load-bearing part

Every other control in this unit can be satisfied by a tree with no pieces in it. A reader that
enumerates zero pieces, joins zero records and reports zero failures is indistinguishable from a clean
run, and this repo reds that class by name. So the reader reports the ENUMERATION COUNT first, and a
zero enumeration is a dead probe with its own message. Unit 6 then compares that count against the
requested N; this unit's job is to make the count exist and be honest.

### Alternatives rejected

**A region in the build README.** Rejected: the README's generated regions are rendered from spec front
matter by a generator that knows nothing about pieces, and adding a fifth region would put piece
evidence inside the artifact the authorization compares across BASE.

**A single manifest file listing all pieces.** Rejected: one file every piece-pass rewrites is a shared
mutable index, which the charter bans by name and which would serialise passes that are otherwise
independent.

**Trusting a per-piece line in the run-state file.** Rejected by S5's whole reason.

## 5. Production-readiness checklist

- security — the record is written by the run and read by the leg, so §9's reduction applies: it is a
  record, not a proof. The hash join raises the cost of a false record from editing one line to
  editing one line AND keeping a hash consistent, which is a cost and not a barrier. Stated plainly.
- perf / scale — one hash per piece per leg run. At the corpus sizes this mode targets, negligible;
  at very large N the reader is the thing to profile first.
- a11y — N/A.
- i18n — piece paths may be non-ASCII; the join is on bytes and the reader must not normalise.
- error / empty / loading states — the four states ARE this row. Plus the dead-probe report for zero
  enumeration.
- observability — the reader prints the four counts on every run.
- risks — a grain glob that matches too broadly inflates the enumeration and therefore looks like
  MORE coverage. The compensating control is unit 4's refusal of an unresolvable grain plus unit 6's
  comparison against a declared N.
- testing + left-shift gates — S6, and specifically the zero-piece arm, which is the one that proves
  the liveness assertion is armed.
- migration / rollback — new artifacts. A tree with no pieces and no records is the ordinary
  pre-adoption state and reports as skipped.
- user docs — the template's section 4 documents what a piece is; the record's own header documents
  its four states.

## 6. Acceptance criteria

- **AC1** — When a piece and its record agree on the content hash, the reader classifies it
  `verified`. Observed via `bash tools/unattended/check-playbook.sh`.
- **AC2** — When a piece is edited after its record is written, the reader classifies it `stale`, with
  a message distinct from `unrecorded`. Staged and observed.
- **AC3** — When a record is deleted, its piece classifies `unrecorded`.
- **AC4** — When a piece is deleted and its record survives, the record classifies `orphan-record`.
- **AC5** — When the declared grain enumerates ZERO pieces, `bash tools/unattended/check-playbook.sh` reports a
  DEAD PROBE and does not report a clean run. Observed in a scratch tree; this is the arm that proves the rest mean
  anything.
- **AC6** — When the reader runs in a tree containing no run-state file at all, `bash tools/unattended/check-playbook.sh` completes and
  reports the same four counts. Observed, because this is the property the attended path depends on.
- **AC7** — When a piece path contains a non-ASCII byte, the join still resolves, verified by an arm in
  `check-playbook.test.sh` rather than assumed.

## 7. Gates

`bash tools/unattended/check-playbook.sh` · `bash tools/unattended/check-playbook.test.sh` ·
`bash tools/unattended/cross-component.test.sh` · `bash tools/run-gates/run-gates.sh`.

## 8. Open questions

- **F1 — where the per-piece record physically sits.** Beside the piece (`<piece>.record.md`) is
  self-joining and pollutes the output tree an owner ships; under the build folder is clean and needs
  a derived path mapping. Recommendation: under the build folder, at a path derived from the piece's
  repo-relative path, because the output tree is the DELIVERABLE and a governance artifact in it is
  the thing an owner will delete. **Agent-resolvable, recorded because both are defensible.**
- **F2 — whether `stale` should RED or WARN.** A stale record on a piece deliberately edited after
  review is the ordinary path during a fold. Recommendation: red at close, warn during the run —
  which needs unit 6 to distinguish the two moments. Deferred to unit 6 rather than guessed.

## 9. Revision log

- rev-1 · 2026-08-20 · initial draft. The tree-property design was ruled by the owner on 2026-08-20
  after the research proved an attended run cannot close through the driver; S4's liveness assertion is
  the charter's rule applied to the one reader that would otherwise be vacuous.

## 10. Reuse audit

The HASH JOIN is prior art in this fleet twice over: the reference corpus's review records bind a
verdict to the body it reviewed by content hash, and this repo's own gate-freshness checks compare a
recorded tree fingerprint against a re-derivation at the sha it names. Both establish that a verdict
with no join to what it judged is a verdict about nothing. The FOUR-STATE classification rather than a
boolean follows the DoD evaluation code's own repair, where five ANDed terms were split so each could
say which one failed. The LIVENESS ASSERTION is the charter's rule and has a worked example in
`drift-audit`, where every signal carries one so a probe that cannot move prints DEAD PROBE instead of
a reassuring zero — that is the shape copied here, and it is copied because the alternative was
measured to be indistinguishable from success. Recall terms used: record verdict hash join stale
orphan enumeration liveness dead probe reader tracked artifact merge bar leg run state independence.
