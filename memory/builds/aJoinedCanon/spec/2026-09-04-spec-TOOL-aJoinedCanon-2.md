# TOOL-aJoinedCanon-2 — the fold procedure gains a re-read set

**Status:** SPECCED · rev-2 · 2026-09-05 · node a · Tier-1 · base 750ca0ca · streams tooling · order 2

<!-- gen:spec-records -->

*No record names this unit.*

<!-- /gen:spec-records -->

## 1. Goal

Folding a review correction is the corpus's most travelled route and its dominant defect source, and
the entire instruction for it is one clause that names no re-read set. Replace that clause with a
short procedure: a table keyed on the section you just edited, naming the sections that edit may have
invalidated.

## 2. Scope (IN)

- **S1** — `tools/memory-tree/BUILD-METHOD.template.md` M4 gains a fold procedure. Its fold sentence
  today is `**Fold fixes into the spec** (rev bump + §9 line), then **STOP**`. It gains a re-read
  table keyed on the edited section, and a pointer at
  `memory/gotchas/fold-text-is-unreviewed-surface.md` for the content practices the table does not
  supply.
- **S2** — the re-read table has one row per section a fold actually lands in, and each row lists the
  sections to re-read before the rev is bumped. The four rows are §2, §4, §6 and §7; the sets are
  derived in §4 below from the finding's own round-level distribution and from `A5`'s amended-arm
  count, not invented.
- **S2b** — a FIFTH row, `§8`, whose set is §2, §4, §6 and every criterion naming an `F<n>`. It is
  listed separately from S2's four because it was not derived the same way: the four came from the
  measured round distribution, and this one came from RUNNING S2's table on a real fold and watching
  it miss. §8 is the section a fork resolution ALWAYS edits, so a table with no §8 row triggers no
  re-read at all on the most common fold there is. Evidence is this build's own rev-2 pass,
  recorded in §4.
- **S3** — `tools/memory-tree/SPEC-TEMPLATE.template.md:183` — `Review corrections fold in here; bump
  the header rev and log it in §9.` — becomes a POINTER at M4's procedure and restates no row of it.
  One text, one home.
- **S4** — both live copies are re-rendered from the two templates by
  `bash tools/memory-tree/kit-dogfood-parity.test.sh --render`, never hand-edited, so
  `memory/guides/BUILD-METHOD.md` and `memory/TEMPLATE-SPEC.md` move in the same commit as their
  shipped twins.
- **S5** — the procedure ends at "log what moved per §9's own rule". It states no §9 grammar of its
  own, because `TOOL-aJoinedCanon-1` (order 1) owns that grammar and lands first.

## 3. Non-goals (OUT)

- **No new gate arm, and no new check-12 predicate.** §7 says why. Inventing an arm that grades a
  claim of re-reading would add a green that means nothing.
- **No change to `tools/workflows/tier2-review.js`.** Its fold priming is one sentence today, and
  whether the procedure must reach a fan-out fixer agent is the open fork in §8, not settled scope.
  Follow-up unit if the owner wants it.
- **No cutoff key, and no `.memory-tree.conf` edit.** The build's dated-cutoff rule binds a change
  that makes a landed spec red. This one adds no required field to any spec and grades nothing, so
  there is no retrofit to guard against and a cutoff key would be a knob with no rule behind it.
- **No rewrite of the four practices in `memory/gotchas/fold-text-is-unreviewed-surface.md`.** M4
  points at that record; copying its practices into M4 is the paraphrase-beside-its-source class the
  charter refuses.
- **Not a re-measurement of B1.** Whether the procedure lowered the fold-created share is a later
  measurement over later builds, named as the compensating check in §5 and not performed here.

## 4. Design

### The evidence the table is derived from

Finding B1 measured the fold across nine round-level measurements in five builds, and every one found
the fold created the MAJORITY of the next round's confirmed findings: 65–72% on `dBriefedPass`, 69%
twice on `dTieredTribunal-1`, 88.9% wide and 61.1% narrow on `dTieredTribunal-11`, 42 of 62 on
`dFramedEntrypoint`, four of five blockers on `dRetiredFork` round 2, both blockers on
`aGradedMandate` round 2. Only 12.0% of specs are still at rev-1, so this is the ordinary path and
not an edge case.

B1's second number is what shapes the table: the confirmed-finding distribution does not migrate
across rounds. §2+§4+§6 is 63.5% at round 1, 59.1% at round 2 and 65.0% at round 3. The fold keeps
breaking the same three sections, so a fixed table keyed on the edited section is sufficient — a
derived or per-build set would be machinery bought for a distribution that does not move.

A worked instance, verified at HEAD:
`memory/builds/aBoundedVerdict/spec/2026-08-16-spec-TOOL-aBoundedVerdict-1.md:534` logs `rev-3` as
"folded round 2, which found the rev-2 fold had not reached the whole spec: S6 still specified the leg
check over a round-count FACT the data model had deleted, and four further sites still described the
fact shape." That is a §4 edit that invalidated a §2 item and four more sites, found a round later.
It is the exact defect the §4 row exists to catch.

### The procedure

M4's fold sentence gains this, in M4's own voice:

> **A fold is not one edit.** The section you edited has neighbours the edit may have invalidated.
> Re-read them BEFORE bumping the rev, and log whatever moved per §9's own rule.
>
> | You edited | Re-read, in this order |
> |---|---|
> | §2 Scope | §3 Non-goals · §6 Acceptance |
> | §4 Design | §2 Scope · §6 Acceptance · §7 Gates |
> | §6 Acceptance | §2 Scope · §7 Gates |
> | §7 Gates | §6 Acceptance |
> | §8 Open questions | §2 Scope · §4 Design · §6 Acceptance · every criterion naming an `F<n>` |
>
> The set says WHERE to look. What goes wrong there is
> `memory/gotchas/fold-text-is-unreviewed-surface.md`, which the fold round's own checklist already
> selects — read its four practices rather than trusting the table alone.

Each set is earned, not symmetric by taste. §4 carries three because it is the section corrections
land in and the one the worked instance broke outward from. §7 is in §4's set on A5's evidence: at
least four criteria were amended because the arm landed elsewhere than the spec said, and in one case
the misplacement surfaced only at the closing review after 42 of 85 legs had silently left every
profile. §3 sits only in §2's set, because a scope item moving is the one edit that moves a cut-line.
§5 and §9 are deliberately absent: §5 is a fixed row sweep a fold rarely invalidates, and §9 is
written by the fold itself.

**The §8 row was earned differently, and the difference matters.** The four rows above come from
B1's measured round-level distribution. The §8 row comes from RUNNING those four rows on a real fold
and watching them miss: this build's own rev-2 pass folded ten owner rulings across ten specs on
2026-09-05, and a fork resolution edits §8 and often nothing else, so a four-row table keyed on the
edited section fires no re-read at all on the single most common fold there is. Two stale clauses
were caught in that pass by the mechanic rather than by the table — `TOOL-aJoinedCanon-1`'s AC1
named a fixture whose date fell PRE-cutoff under the very cutoff the fold had just ratified, making
a gate's own failing-case criterion unable to fail; and `TOOL-aJoinedCanon-3`'s AC5 still branched
on the outcome of a fork that had just been decided. Both are criteria naming an `F<n>`, which is
why that clause is in the row rather than a bare section list. A table derived from where defects
LAND cannot see the section a fold always TOUCHES, and only using it revealed that.

### Files touched (estimate)

| File | Change |
|---|---|
| `tools/memory-tree/BUILD-METHOD.template.md` | M4's fold sentence gains the procedure block |
| `tools/memory-tree/SPEC-TEMPLATE.template.md` | line 183's clause becomes a pointer at M4 |
| `memory/guides/BUILD-METHOD.md` | RENDERED, not hand-edited |
| `memory/TEMPLATE-SPEC.md` | RENDERED, not hand-edited |

The render direction is the parity test's own, stated in its header: `--render` writes TEMPLATE ->
LIVE, and hand-editing the live copy is what the leg exists to catch.

### Alternatives rejected

- **Put the procedure in `TEMPLATE-SPEC.md` instead of M4.** TEMPLATE-SPEC owns the section canon, so
  by subject it is the natural home. It is the wrong home by READER: the skeleton's §4 body is
  instructional prose the author replaces with real design, so the fold clause does not survive into
  the spec being folded, and a folding session is looking at the spec. M4 is what a run reads whole —
  M7's regrounding step 3 is `**This file, whole.**` at every pass boundary. The reader wins.
- **Spell the pointer as the repo-relative path `memory/guides/BUILD-METHOD.md`.** Verified cost:
  `tools/memory-tree/check-method-carriers.sh` selects carriers with `grep -lF -- "BUILD-METHOD.md"`
  over every tracked file outside `memory/`, excluding only `BUILD-METHOD.template.md` itself, and
  `tools/memory-tree/SPEC-TEMPLATE.template.md` is not in `memory/project/method-carriers.txt`. The
  path spelling would therefore red the `method carriers (every pointer declared)` leg until a
  registry row is added. Rejected in favour of the pathless `BUILD-METHOD M4` spelling the same file
  already uses at line 138 for M7 — zero new gate obligation. A builder who wants the path anyway
  owes the registry row and now knows it.
- **Restate the gotcha record's four practices in M4.** Two carriers of one rule is the shape that rot
  is measured in, and the gotcha's own fourth practice is about exactly that failure.
- **A derived per-build re-read set.** The distribution does not move across rounds, so a derivation
  would compute a constant at cost.

## 5. Production-readiness checklist

- security — N/A — prose in two shipped documents, no execution path, no input.
- perf / scale — N/A — the diff is prose; no leg's runtime changes.
- a11y — N/A — no user interface.
- i18n — N/A — this repo's documents are English-only by construction.
- error / empty / loading states — N/A — no runtime.
- observability — the only signal is the §9 lines the procedure produces, which `TOOL-aJoinedCanon-1`
  makes structured; this unit adds no signal of its own.
- risks (concurrency, data-loss, rollback hazards) — the live copies are GENERATED. Hand-editing one
  instead of rendering is the single failure mode, and `kit/dogfood doc parity` catches it. Rollback
  is a revert of one commit; nothing is stateful.
- testing + left-shift gates — no arm is added, so the exemption is documented here with its
  compensating check: `memory/gotchas/fold-text-is-unreviewed-surface.md` is the standing documented
  check for this class, it is reached by `python tools/memory-tree/gotchas.py --for-diff` on any diff
  touching `memory/guides/BUILD-METHOD.md`, and the M4 spec-audit loop is the instrument that
  measures whether the procedure worked — B1's own numbers came from those review records. Re-running
  B1's by-kind split over the next builds is the verdict, and it is a later measurement, not a gate.
- migration / rollback — no corpus migration. Landed specs are untouched and no cutoff key is added,
  per §3.
- user docs — N/A — `help/` is for user-facing product features; this is an agent-facing rule, and its
  two carriers ARE the documentation.

## 6. Acceptance criteria

- **AC1** — When M4 of `memory/guides/BUILD-METHOD.md` is read at HEAD, its fold sentence is followed
  by a re-read table with one row each for `§2`, `§4`, `§6`, `§7` and `§8`; the §4 row lists §2, §6
  and §7; and the §8 row lists §2, §4, §6 and the `F<n>` criterion clause.
- **AC2** — When `bash tools/memory-tree/kit-dogfood-parity.test.sh` runs on the landing commit, it
  exits 0, proving both live copies were produced by `--render` from
  `tools/memory-tree/BUILD-METHOD.template.md` and `tools/memory-tree/SPEC-TEMPLATE.template.md`
  rather than hand-edited.
- **AC3** — When the fold clause at `memory/TEMPLATE-SPEC.md:183` is read, it names `BUILD-METHOD` M4
  and contains no row of the table, so `grep -c 'Re-read, in this order' memory/TEMPLATE-SPEC.md`
  returns 0 while the same grep over `memory/guides/BUILD-METHOD.md` returns 1.
- **AC4** — When `bash tools/memory-tree/check-method-carriers.sh` runs after the edit, it exits 0
  with `memory/project/method-carriers.txt` unchanged, because the pointer uses the pathless
  `BUILD-METHOD M4` spelling.
- **AC5** — When `python tools/memory-tree/gotchas.py --for-diff <base>..HEAD` is run over this unit's
  own diff, `fold-text-is-unreviewed-surface` appears in the checklist, because that record's derived
  anchors include `memory/guides/BUILD-METHOD.md`.
- **AC6** — When `bash tools/run-gates/run-gates.sh` runs at the push boundary, the `memory hygiene`,
  `kit version markers`, `line length` and `kit/dogfood doc parity` legs are all green.

## 7. Gates

Legs this unit must keep green, all named as they appear in `tools/gate-legs.json`:

- `kit/dogfood doc parity` — the leg that binds the four files this unit touches.
- `kit version markers` — every `tools/memory-tree/*.template.md` must carry a
  `gov:kit memory-tree@` marker equal to `KIT_MEMORY_TREE_VERSION`; this unit does not bump the
  constant, so both markers stay as they are.
- `method carriers (every pointer declared)` — see AC4 and the rejected alternative in §4.
- `memory hygiene` — this spec is itself graded by check 12.
- `line length` — both documents are prose and hard-wrap at ~100 columns.

**This unit adds NO gate arm, deliberately.** A re-read is an ACT, not an artifact. Nothing in the
tree distinguishes "opened §6 and confirmed it still holds" from "never opened §6", so the only thing
an arm could grade is a §9 line CLAIMING a re-read — which is the liveness gap `TEMPLATE-SPEC.md`
already names for §10: the check cannot see whether the fact is true. A commit-level arm asserting
"a rev bump touching §4 also names §2 or §6 in its §9 line" would be worse, not better: it grades the
same claim, it needs a git-replay checker where check 12 is file-level, and it sits on top of a
grammar `TOOL-aJoinedCanon-1` owns. The exemption's compensating check is recorded in §5's testing
row, per charter §7.

## 8. Open questions

- **Q1 — does the procedure reach a fold performed by fan-out agents?** For a run that folds its own
  corrections, M4 reaches: M7's regrounding step 3 reads this file whole at every pass boundary. For a
  fold delegated to parallel sub-agents, only what the harness primes reaches, and
  `memory/gotchas/fold-text-is-unreviewed-surface.md` records that `tools/workflows/tier2-review.js`
  "carries exactly one sentence of fold priming today". That same record measured the parallel case on
  `dTieredTribunal`: round 1 folded by four agents, 20 fold-created findings of 29; round 2 folded by
  hand, 20 of 32 — the same absolute count, so author count is not the driver and a hand-fold does not
  escape this. **Recommendation:** land the two document carriers now, since they are where the rule
  belongs regardless, and treat the harness priming line as a separate unit the owner may decline.
  Adding it here would put a `.js` change inside a Tier-1 doc unit and make the tier wrong.
  UNRESOLVED — the owner's call at scope approval.

## 9. Revision log

- rev-1 · 2026-09-04 · initial draft.
- rev-2 · 2026-09-05 · §2 · §4 · added S2b, the §8 row, after this build's own fold pass ran S2's
  four-row table against ten specs and measured it missing the §8 case. §8's fork remains OPEN.

## 10. Reuse audit

`python tools/codebase-map/reuse_lookup.py "folding a review correction back into a spec"` returned
`fold-text-is-unreviewed-surface.md [gotcha-classes]` as a direct hit, and that is the seam this unit
extends rather than a new one. That record already owns the fold as a named recurring class, already
declares "**No machine gate**, and this is a documented check rather than an unwritten one", and
already reaches a fold diff through `python tools/memory-tree/gotchas.py --for-diff` — verified live,
the command runs and prints an anchored checklist. What it does NOT hold is a SECTION closure: its
four practices are about the content a fold writes, and its nearest neighbour, "when a finding names
several carriers, edit all of them or record the refusal", covers carrier closure and not the
neighbouring sections of one document. This unit adds that half in M4 and points at the record for the
rest, so neither restates the other. The probe's other candidates were `REVIEW-PROTOCOL.md` and
`tier2-review.js`, both fan-out shape rather than fold content, and the `gen_build_index.py` spec
parsers, which read the header and not §4.

Recall terms used: `python tools/memory-recall/query.py "why does the fold instruction name no
re-read set, and what decided the fold procedure's shape" --terms "fold rev bump revision log re-read
set spec audit round blocker disposition acceptance criteria scope item"`. It returned 40 hits over
909 records; the load-bearing one is
`memory/builds/aBoundedVerdict/spec/2026-08-16-spec-TOOL-aBoundedVerdict-1.md:534`, quoted in §4, and
`memory/builds/dTieredTribunal/reviews/2026-08-26-review-TOOL-dTieredTribunal-1-spec-audit-round3.md`,
which records a fold dropping the half of its own finding that made a criterion resolvable. Neither
record proposes a re-read set, so nothing prior is being re-invented.
