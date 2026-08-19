# TOOL-aBoundedVerdict-16 — `closing-review-recorded` joins a diff-review, in range

**Status:** INPROGRESS · rev-1 · 2026-08-19 · node c · Tier-2 · base 098bebd9 · streams tooling

## 1. Goal

The Definition-of-Done item that asserts a closing review happened is a 7-hex substring search for the
run's pinned BASE across every markdown file under the build's `reviews/`, which makes it blind to the
record's KIND and blind to any round that reviewed a fold rather than the whole build. Measured over
the seven tracked runs: three have no matching record at all, and two of the four that match do so on a
**spec-audit** record. Join it to the thing it is named for.

## 2. Scope (IN)

- **S1** — the item requires a record whose `**Serves:**` line names the kind `diff-review`. The
  binding grammar already exists and its `<kind>` set is already closed; the item currently reads none
  of it.
- **S2** — the sha the record must name may be ANY commit in `BASE..HEAD`, not the pinned BASE alone.
  A fold-scoped round names the fold's base, which is a descendant of BASE — so under
  `TOOL-aBoundedVerdict-14` the honest closing round names a sha this item currently rejects.
- **S3** — the range membership is decided by git, not by string comparison: the named sha must be an
  ancestor of HEAD and BASE must be an ancestor of it. A substring test cannot express range membership
  and would accept a sha from any branch that happens to share a prefix.
- **S4** — the length floor stays and keeps its stated reason. `grep -F ""` matches every line of every
  file, so an absent or truncated base would select the first record in the build and the item would
  pass by finding anything — the same degeneration an empty base once caused in `check_authorization`,
  where it turned a provenance test into a read of the git index.
- **S5** — `DOD_OUT` names which of the failure modes fired, distinguishing at minimum: no record under
  `reviews/` · a record exists but is UNTRACKED · a record is tracked but names no in-range sha · a
  record names one but is not a `diff-review`. The untracked case is the likeliest and least guessable,
  because the arm reads `--cached`.
- **S6** — the leg's own copy of this predicate, if it has one, reads the same rule; if it does not, the
  spec says so rather than leaving a reader to assume parity.

## 3. Non-goals (OUT)

- Not judging what the review SAID. A `BLOCKED` closing review satisfies this item and must continue
  to: the item asserts that the review happened and is bound to this run, and the verdict's
  consequences are `TOOL-aBoundedVerdict-1`'s convergence rule. Anchoring a verdict here would make the
  item unsatisfiable against most of the corpus, which is the defect the driver's own comment records
  having already made once.
- Not retrofitting the corpus. Three tracked runs have no matching record and they are terminal
  history; this unit changes what a FUTURE close requires.
- Not the `**Serves:**` line's authorship. That the review harness writes a kind-less one is
  `TOOL-aBoundedVerdict-14` S7, and this unit's S1 is unsatisfiable in practice until that lands —
  stated in Rollout rather than left as a surprise.
- Not the review record filename grammar, which `memory/HYGIENE.md` check 5 owns.
- No change to which items are overridable, and no new DoD item.

## 4. Design

### What was measured

Per tracked run, the pinned base's 7-char prefix searched with `git grep --cached` under the build's
`reviews/`:

| run | matching records | kinds matched |
|---|---|---|
| aBranchedMandate | 1 | `diff-review` |
| aSiftedPlaybook | 1 | `diff-review` |
| aWalkedCorpus | 3 | `diff-review`, `spec-audit` |
| cBriefedPilot | 3 | `diff-review`, `spec-audit` |
| aDeclaredCeiling | 0 | — |
| aSealedCaravan | 0 | — |
| dClosedLexicon | 0 | — |

The three zeroes are runs that closed before the item existed. The two mixed rows are the defect: a
spec audit that happens to quote the base sha satisfies an item named for a closing review.

### The fold interaction, stated precisely

The audit raised this as "the honest fold-scoped round fails the item". That framing is **too strong and
is corrected here**: the item scans every record under `reviews/`, so round 1's record — which names
the pinned BASE — still satisfies it after any number of fold-scoped rounds. What is actually true is
narrower and still worth fixing:

- a build whose ONLY closing round was fold-scoped has no record naming BASE, and that is reachable on
  a resumed run whose round 1 record was written under a different build folder or never committed;
- and the item cannot distinguish "reviewed once at the start" from "reviewed after the last fold",
  which is the question a reader of a DoD item called `closing-review-recorded` believes it answers.

S2 and S3 fix the second, which is the one that will mislead someone, and the first falls out.

### Inventory

| Concern | Today | After |
|---|---|---|
| the record's kind | unread; a spec-audit satisfies it | must be `diff-review` |
| the sha | the pinned BASE only | any commit in `BASE..HEAD` |
| how membership is decided | 7-hex substring anywhere in the file | git ancestry, both directions |
| a truncated or absent base | matches the first record in the build | refused at the length floor |
| the failure mode | one indistinguishable silence | named, four ways |
| an untracked review record | invisible, and unguessable | named, with the remedy |

### Migration

None on disk. Three tracked runs would not satisfy the tightened item, and all three are terminal —
this unit does not re-grade a closed run. One forward-looking consequence worth stating: until
`TOOL-aBoundedVerdict-14` S7 lands, the harness writes a kind-less `**Serves:**` line, so S1 is
satisfiable only by a hand-edited record. That is a real ordering dependency and it is in Rollout.

### Rollout

`TOOL-aBoundedVerdict-14` S7 first — it makes the harness write the kind, without which S1 requires a
hand edit on every close. Then S5's messages, which are independently useful and depend on nothing.
Then S1-S3, then S6's parity statement.

### Files touched (estimate)

`tools/unattended/unattended.sh` (the `closing-review-recorded` arm) ·
`tools/unattended/unattended.test.sh` (an arm per failure mode plus the in-range and wrong-kind arms) ·
`tools/unattended/check-unattended.sh` if S6 finds a second copy · `memory/guides/UNATTENDED-PROTOCOL.md`
and `tools/unattended/PROTOCOL.template.md` (the DoD table's Asserts cell for this item) · the kit
version constant.

### Alternatives rejected

- **Require the record to name the pinned BASE exactly, and let a fold round also name BASE.** Simpler,
  and rejected: it asks the record to carry a sha the round did not review, which is provenance
  pointing at the wrong thing.
- **Decide range membership by string comparison against a list of shas in the range.** Rejected on
  S3's reason: it is a substring test wearing a range's clothes, and it grows with history.
- **Join on the review record's FILENAME instead.** Rejected for the reason the driver's own source
  already gives: every filename and sequence join was measured wrong on 7 of 7 multi-unit builds in
  this corpus.
- **Anchor the verdict token as well as the kind.** Refused in §3: it makes the item unsatisfiable
  against the corpus, which the driver's comment records having already tried.
- **Drop the item and let the review protocol carry the obligation.** Rejected: a DoD item is what a
  close reads, and an obligation with no reader is what the 90-record verdict corpus already
  demonstrates.

## 5. Production-readiness checklist

- **security** — the item is a provenance test, so the failure mode that matters is passing by finding
  anything. S4's length floor is the guard and it must keep its comment: the reason is a measured
  historical degeneration, not a hypothetical.
- **perf / scale** — one or two `merge-base --is-ancestor` calls per candidate record. Bounded by the
  number of records under one build's `reviews/`, measured at most 10 in this corpus.
- **a11y** — N/A.
- **i18n** — N/A.
- **error / empty / loading states** — S5 is this line. The empty case: zero records under `reviews/`
  must be distinguishable from records present but none matching.
- **observability** — S5, and it is what makes the item's refusal actionable rather than a re-run.
- **risks** — the ordering dependency on `TOOL-aBoundedVerdict-14` S7 is the real one, and it is stated
  in Migration and Rollout rather than discovered at build time. Second: an ancestry check against a
  sha in a shallow or grafted clone — the driver already refuses a clone carrying an
  object-substitution lever, which covers the graft case by construction.
- **testing + left-shift gates** — a fixture per failure mode, and a green fixture that satisfies the
  item with a FOLD-scoped sha, which is the arm that fails against the shipped predicate.
- **migration / rollback** — none; revert is the arm.
- **user docs** — the protocol's DoD table cell for this item, in both halves.

## 6. Acceptance criteria

- **AC1** — When a fixture build's only review record is a `spec-audit` that quotes the pinned base,
  `--close` refuses on `closing-review-recorded` naming the kind it wanted; against the shipped driver
  it passes.
- **AC2** — When the record is a `diff-review` naming a sha that is a descendant of BASE and an
  ancestor of HEAD, the item is met — the fold-scoped green arm.
- **AC3** — When the record names a sha that is NOT an ancestor of HEAD, the item is unmet even though
  the 7-hex string appears in the file — asserted with `git merge-base --is-ancestor` in the arm's own
  fixture, which commits the off-branch sha.
- **AC4** — When the record exists but is untracked, `DOD_OUT` says so and names `git add`; asserted by
  `git grep --cached` returning nothing while the file is on disk.
- **AC5** — When the run-state file's `base` fact is absent or shorter than the floor, the item is
  unmet and does not select the first record in the build — the arm that proves S4's guard, with a
  fixture carrying at least two records.
- **AC6** — When the four failure modes are driven in turn, four distinguishable `DOD_OUT` values
  result, asserted as four arms in `tools/unattended/unattended.test.sh`.
- **AC7** — When `memory/guides/UNATTENDED-PROTOCOL.md` and `tools/unattended/PROTOCOL.template.md` are
  compared, this item's Asserts cell describes kind and range in both, and
  `bash tools/unattended/check-unattended.sh` is clean over the pair.

## 7. Gates

`tools/unattended/unattended.test.sh` · `tools/unattended/check-unattended.sh` +
`check-unattended.test.sh` · `bash tools/unattended/adopt-unattended.sh --check` ·
`python tools/memory-tree/check-arms.py` · `tools/check-testsuite-counts.sh` ·
`tools/check-kit-versions.sh` · `bash tools/run-gates/run-gates.sh`.

## 8. Open questions

- **F1 — does the item require the record to name a sha in range, or the LATEST such round?** Requiring
  the latest is what a reader of the item's name expects, and it needs a total order over the records,
  which their filenames do not reliably give — the join this corpus has measured wrong seven times.
  **Recommendation: in-range, not latest.** The convergence rule in `TOOL-aBoundedVerdict-1` is what
  makes "the last round was clean" checkable; this item stays a provenance test.
  RESOLVED (agent, 2026-08-19, delegated): in-range. Mechanism-only, and "latest" needs an ordering the
  corpus has already refuted.

- **F2 — is the kind read from the `**Serves:**` line by this arm, or through the existing parser?**
  The hygiene engine's binding parse lives in `gen_build_index.py`, which the unattended kit cannot
  depend on — it ships independently. **Recommendation: a local grep for the kind token on the
  `**Serves:**` line,** with a comment naming the grammar's owner so the two cannot silently diverge in
  their idea of where the kind sits.

- **F3 — should the item accept a record filed under ANOTHER build's `reviews/`?** The binding grammar
  explicitly allows a record to name a spec in another build, because one closing review legitimately
  covers two builds. This item scopes its search to this build's folder. **Recommendation: keep the
  scope,** and note the limit: a genuinely shared closing review must be filed under both builds or
  named in both, which is the grammar's own answer.

## 9. Revision log

- rev-1 · 2026-08-19 · initial draft. Derived from the close-path audit's high 21 and low 26, with the
  audit's framing CORRECTED in §4: it claimed the honest fold-scoped round fails the item, and the item
  scans every record under `reviews/`, so round 1's record still carries it. The narrower true defects
  — kind-blindness, measured on 2 of 4 matching runs, and the inability to distinguish a start-of-build
  review from a post-fold one — are what this unit fixes. F1 resolved under the delegated fork rule;
  F2 and F3 carry recommendations and stay open as build-time judgements.

## 10. Reuse audit

The seams are `memory/HYGIENE.md`'s record-binding grammar, whose `<kind>` set already contains
`diff-review` and which this unit reads rather than extends; `GIT()`, the driver's git wrapper, through
which S3's ancestry calls run so the object-substitution lever stays inert; and `DOD_OUT`, the message
channel `TOOL-aBranchedMandate-12` built and `TOOL-aBoundedVerdict-12` widens — S5 adds a caller, not a
channel.

The length floor in S4 is itself a reused rule: the driver's own comment records the same degeneration
in `check_authorization` when an empty base turned a provenance test into a read of the git index. This
unit keeps the guard and its reason rather than re-deriving why it is there.

Recall terms used, at the SET level for this build: `closing review round cap blocked verdict
adversarial diff fold unattended close build-complete DoD stall halt`.
