# TOOL-aRuledFrontispiece-9 — the build method's roster claim and its parallelism test are corrected

**Status:** OPEN · rev-2 · 2026-08-16 · node a · Tier-2 · base 96141aed · streams tooling

## 1. Goal

Two rules in `memory/guides/BUILD-METHOD.md` are false against the code they govern. M2 describes the
`ids:` key as a reservation range the author writes; the generator derives it. M6's parallelism test
names generated indexes as shared writes, which forbids every pair of passes in this repo and so
selects nothing. Both are measured by this build rather than supposed, and both are fixed in the
template the live file renders from.

## 2. Scope (IN)

- **S1** — every edit lands in `tools/memory-tree/BUILD-METHOD.template.md` and reaches the live copy
  through `bash tools/memory-tree/kit-dogfood-parity.test.sh --render`. The live file is never
  hand-edited; that is the direction the harness's own header declares.
- **S2** — M2's Detect paragraph states the derivation the generator performs: `ids:` is rewritten
  from every tracked mention of an id under the memory root, excluding the build's own README, so it
  lags the authored plan and cannot name a unit no other record names. The conclusion is unchanged —
  it is not a roster — and only the reason and the failure mode change.
- **S3** — M6's parallelism test stops forbidding every pair. A DERIVED artifact leaves the write-set
  test, on the stated condition that no concurrent pass renders one and the pass that joins them
  renders every one before the join commits. Clause 2 drops `generator input` from its contract list
  and clause 3 drops the build README's generated regions and the generated indexes.
- **S4** — M1 stops citing `memory/HYGIENE.md` rule 6 as the authority for its own budget. Rule 6
  gives a guide 61440 bytes and 750 lines; M1's 20 KB and 250 lines is a stricter local constraint
  with a different reason, and attributing it to a carrier that says otherwise is the same
  two-answers-to-one-question class as S2 and S3.
- **S5** — the file does not grow. M9's gloss restating the governance template's §16 output shape is
  deleted and pays for S3's added sentence; M2's stale parenthetical example goes with the sentence
  S2 replaces.
- **S6** — `memory/guides/SESSION-KICKOFF.md` is re-stamped: `last-audit` advances to a new datetime
  and the merge-base sha, with the delta named in the commit subject. The file is on both the `watch:`
  and `verify-paths:` lists, so C5 reds an unaudited edit.

## 3. Non-goals (OUT)

- Changing what `tools/memory-tree/gen_build_index.py` does with `ids:`. That derivation is
  `TOOL-aMouldedFolio-2`'s decision and it is the half that is right; this unit moves the prose to
  meet it.
- Moving `KIT_MEMORY_TREE_VERSION` or the `gov:kit memory-tree@` marker at line 1 of either file.
  `check-kit-versions.sh` requires the marker to equal the engine constant, and the build README
  reserves that constant's single move for the corpus-retrofit unit.
- Raising M1's budget. The correction is net-neutral by construction; a rule that grows the file it
  caps in order to explain the cap is the worst available outcome.
- Changing M6's definition of a pass, its commit rule, or the bug-class checklist that follows one.
- Changing the fan-out and concurrency caps. `memory/guides/REVIEW-PROTOCOL.md` owns HOW MANY;
  M6 owns WHICH, and the pointer between them stays exactly as it is.
- Retrofitting build READMEs whose Units tables were authored under the old M2 reading.
- **Absorbing, pre-empting or restating `TOOL-cBriefedPilot-15`.** That spec is OPEN on node `c` and
  rewrites the SAME M6 paragraph: its branch A replaces M6's opening sentence, `**Sequence is the
  default; parallelism is a claim you substantiate.**`, in the same template, and re-renders the same
  live copy. Its own S3 holds M6's three conditions byte-identical — which is precisely the half S3
  here rewrites — so the two changes are disjoint in content and neither may carry the other. §4
  Migration prices the collision, which is positional and not resolvable by any driver on this bar.

## 4. Design

### Inventory

The render path and the budget, both measured against the tracked blobs at `base 96141aed`.

| Fact | Measurement |
|---|---|
| source of truth | `tools/memory-tree/BUILD-METHOD.template.md`, 236 lines, 16484 bytes |
| render command | `bash tools/memory-tree/kit-dogfood-parity.test.sh --render`, which substitutes `{{KIT_DIR}}` four times and `{{TOOL_ROOT}}` six times |
| live copy | `memory/guides/BUILD-METHOD.md`, 236 lines, 16466 bytes — the 18-byte delta is exactly those ten substitutions |
| M1's own budget | 20480 bytes and 250 lines, so 4014 bytes and 14 lines of headroom |
| hygiene check 6, guides class | 61440 bytes and 750 lines, which is not the binding constraint here |
| hygiene check 16 | the charter read path measures 70268 bytes against a `READ_PATH_CEILING` of 86476 |

The adopter `adopt-memory-tree.sh` renders the same pair with its own copy of the substitution, so it
is not the command to reach for on this repo: it rewrites the whole memory tree to fix one document.

### Data model

M6's test, clause by clause, with what changes and why.

| Clause | Today | After |
|---|---|---|
| 1 | write sets do not intersect | AUTHORED write sets do not intersect |
| 2 | neither writes what the other reads as a contract, `generator input` among the examples | the example list drops `generator input`; contract and acceptance inputs stay |
| 3 | neither TOUCHES a shared mutable record, the build README and any generated index among them | neither WRITES a shared authored record; the build README counts outside its generated regions |
| new | — | a derived artifact is not a write-set member: nobody renders one mid-pass, and the joining pass renders every one before the join commits |

The vacuity is in clauses 1 and 3 together, and it is total rather than partial. Every pass writes a
spec, a review record or code. Hygiene check 9 requires the build README's generated region to match
a fresh render, so every pass's write set contains that README. Under clause 1 the write sets of any
two passes intersect there, and under clause 3 both touch a named shared record. No two passes of any
build in this repo can run concurrently, which makes a rule written to admit some work admit none.
This build is the first evidence, and its own README declines a parallel lane on that ground.

The correction keeps the strict half. A real collision is two passes writing the same authored bytes,
and every one of those still sequences: two specs in one file, two rows appended to one backlog shard,
two edits to the run-state file. What stops being a collision is an artifact neither pass authors,
because the render is a function of the authored set and running it once after the join is both
cheaper and the only way to get a correct answer.

**The correction does not retroactively falsify this build's own order declaration**, and that was
checked pair by pair rather than assumed. The build README declares a TOTAL order with no parallel
lane, at the eleven positions of its `#` column. Corrected clause 1 still refuses the pairs that
order actually contains, because the correction removes only DERIVED artifacts from the write set
and this build's units collide on AUTHORED source: the three region units at orders 3, 4 and 5 all
write `tools/memory-tree/gen_build_index.py`, which the README already names as the reason they
sequence. Where corrected clause 1 stops refusing a pair, corrected clause 2 still does — orders 9
and 10 write the authored and the derived halves of the same READMEs, and order 10 re-renders what
order 9 restructured, so it depends on order 9's output and clause 2's dependency half sequences
them. The corrected M6 also keeps `Sequence is the default`, so declaring a total order can never be
a violation of it.

What the correction retires is the README's SECOND reason, not its declaration. That reason — under
M6 as written no two passes of any build in this repo can run concurrently — stops being why this
build is sequential once S3 lands; the authored write-set intersection is. The README hands this unit
the vacuity as its subject and calls this build its first evidence, so the record already anticipates
the change, and stating it here is what keeps the record right for the reason that survives.

### Migration

Edit the template, re-render, re-stamp the manifest. Nothing else in the corpus reads these rules
mechanically, and `tools/memory-tree/check-method-carriers.sh` is structural: it catches a copied
`## M<n>` section in a file outside the memory root, and this unit creates none.

**The sibling on node `c`.** `TOOL-cBriefedPilot-15` is OPEN, Tier-2, `base 37c05e1b`, and its
backlog row at `memory/backlog/TOOL.md:55` is OPEN. The two edits are disjoint in content and collide
in POSITION: at `base 96141aed` M6's opening sentence and the start of clause 1 share ONE line — line
148 of `tools/memory-tree/BUILD-METHOD.template.md` and line 148 of `memory/guides/BUILD-METHOD.md`,
the same bytes in both — so the sibling's replacement and this unit's clause rewrite land in the same
hunk of the same line of both halves of the rendered pair.

`git check-attr merge` reports `unspecified` for both files. The row-keyed driver that auto-resolves
`memory/DECISIONS.md` and `memory/backlog/*.md` does not cover this pair, so the fallback is
`git merge-file` and a conflict on line 148 is the failure mode. Neither edit can be merged into the
other's text mechanically.

**This unit lands first**, as a scheduling fact rather than a preference.
`TOOL-cBriefedPilot-15` picks its branch from `TOOL-cBriefedPilot-21`'s verdict token — `parallelism
route: <R-id>` or `parallelism route: none` — so it cannot land in either branch until that unit
records one, and neither has landed. This unit has no such precondition. Whoever lands second
re-applies one sentence by hand against the other's text, in the TEMPLATE, and re-renders:
`kit-dogfood-parity.test.sh` reds a half-merged pair, and the live copy is never the merge target.

Order matters for a second reason. The sibling's branch A makes concurrency OWED under a standing
mandate for any pair meeting the three conditions, and this unit widens which pairs meet them. Landed
in that order, the inversion applies to the corrected conditions and obliges concurrency for pairs
the conditions refuse today. That composition is the sibling's to price against whatever this unit
has already landed, which is another reason the loser of the race re-derives rather than replays.

M1's rule that nothing here is stated anywhere else was checked against source for all three edits.
`memory/guides/REVIEW-PROTOCOL.md` states agent counts and concurrency ceilings and no write-set
disjointness rule, so S3 duplicates nothing there. `memory/HYGIENE.md:140` names `ids` as a
front-matter key and says nothing about its meaning, and `memory/TEMPLATE-SPEC.md` does not mention
it at all, so S2 duplicates nothing. S4 is the one edit that sits on the line, and it resolves the
other way: it removes a citation rather than adding a rule, and what survives is a number rule 6 does
not state, held for a reason rule 6 does not have.

### Alternatives rejected

**Deleting M6's clause 3 outright.** It would take the authored records with it, and
`memory/DECISIONS.md` and the backlog shards are exactly where two concurrent passes collide in
practice. The row-keyed merge driver resolves that collision across a MERGE, not across two writers
in one worktree.

**Leaving M2 alone and letting the generator be the answer.** The file is re-read whole at every pass
boundary under M7, so a false sentence in it is read more often than almost anything else in the repo,
and the observed rewrite of ten authored ids down to one is what it costs a reader who believed it.

**Raising M1's budget to pay for the additions.** M1's cap exists because M7 re-reads the file whole;
spending the cap to explain the cap inverts the reason for it.

### Files touched (estimate)

`tools/memory-tree/BUILD-METHOD.template.md` · `memory/guides/BUILD-METHOD.md` as its render ·
`memory/guides/SESSION-KICKOFF.md` for the `last-audit` stamp.

## 5. Production-readiness checklist

- security — N/A. A procedure document with no trust boundary and no executable surface.
- perf / scale — the file is re-read whole at every pass boundary, which is why S5's net-neutrality is
  a scope item rather than a preference.
- a11y — N/A. No user-facing surface.
- i18n — N/A. English prose, as the rest of the memory tree is.
- error / empty / loading states — N/A for a document; the render's failure states belong to
  `kit-dogfood-parity.test.sh`, which this unit runs rather than changes.
- observability — the parity leg names the pair it found drifted and prints the fix command, so a
  hand-edited live copy is reported rather than silently overwritten at the next render.
- risks — the live copy is regenerated, so an edit made there instead of in the template is lost at
  the next render while the parity diff passes over it; the map dossier for this feature records the
  same hazard. The second risk is scope: M6's clause set is load-bearing for every unattended run, and
  a correction that loosened it too far would license a genuinely colliding pair.
- testing + left-shift gates — `bash tools/memory-tree/kit-dogfood-parity.test.sh` is the binding leg
  for the pair, and `bash skills/session-kickoff/manifest-check.sh` is the binding leg for the stamp.
  Neither the roster claim nor the parallelism test is machine-checkable, and this unit does not
  pretend otherwise.
- migration / rollback — revert of two files plus the stamp; no generated artifact and no gate moves.
- user docs — this unit IS the user doc. `AGENTS.md` and the two Skills that point at the method point
  by path, so no pointer changes.

## 6. Acceptance criteria

- **AC1** — When `bash tools/memory-tree/kit-dogfood-parity.test.sh` runs at this unit's tip, it is
  clean, so `memory/guides/BUILD-METHOD.md` is the render of the edited template and not a hand-edit.
- **AC2** — When `memory/guides/BUILD-METHOD.md` is measured at this unit's tip, it is at most 236
  lines and at most 16466 bytes, which is the displacement rule M1 states made checkable.
- **AC3** — When M2's Detect paragraph is read, it contains no claim that `ids:` is a reservation
  range, and it names `gen_build_index.py` as the writer of that key.
- **AC4** — When M6's parallelism test is applied to two spec-authoring passes in one build folder,
  it admits them, whereas at `base 96141aed` clause 3 refuses them on the build README alone.
- **AC5** — When M6's parallelism test is applied to two passes both appending to
  `memory/backlog/TOOL.md`, it still refuses them.
- **AC6** — When `bash tools/memory-tree/check-memory-hygiene.sh` runs, checks 6 and 16 are clean
  against `READ_PATH_CEILING`, which is `86476` in `.memory-tree.conf` and is the only number check 16
  asserts, and the read-path total `python tools/memory-tree/corpus_ids.py` reports is no higher than
  at this unit's own PARENT commit. The total is not this unit's to pin: `memory/DECISIONS.md` and
  `memory/LIVE.md` are members of the same read set and grow with every unit of this build, so the
  70268 B measured at `base 96141aed` is stale by order 8 through no act of this unit.
- **AC7** — When `bash skills/session-kickoff/manifest-check.sh` runs after the edit, C5 is clean,
  which it is not if `memory/guides/BUILD-METHOD.md` moved without a `last-audit` re-stamp.
- **AC8** — When `bash tools/check-kit-versions.sh` runs, it is clean and the `gov:kit memory-tree@`
  marker on both files is unchanged from `base 96141aed`.
- **AC9** — When `git diff 96141aed -- tools/memory-tree/BUILD-METHOD.template.md` is read at this
  unit's tip, the sentence `**Sequence is the default; parallelism is a claim you substantiate.**` is
  byte-unchanged, so `TOOL-cBriefedPilot-15`'s branch A still has the exact string its S2 replaces.

## 7. Gates

`bash tools/memory-tree/kit-dogfood-parity.test.sh` · `bash tools/memory-tree/check-memory-hygiene.sh`
for checks 6 and 16 · `bash skills/session-kickoff/manifest-check.sh` and its self-test ·
`bash tools/check-kit-versions.sh` for the untouched marker ·
`bash tools/memory-tree/check-method-carriers.sh` and its self-test ·
`python tools/codebase-map/test_codebase_map.py`, because the guides inventory and this feature's
dossier both name the file.

## 8. Open questions

none — both defects are measured rather than argued, and the build README's ordering section already
records M6's vacuity as this unit's subject and this build as its first evidence.

## 9. Revision log

- rev-1 · 2026-08-16 · initial draft.
- rev-2 · 2026-08-16 · folded the M4 spec audit. The HIGH row "rewrites the same M6 paragraph as an
  OPEN spec on another node, and never names it": `TOOL-cBriefedPilot-15` is now cited in §3, §4
  Migration and §10, with the collision measured — both edits land on line 148 of both halves of the
  rendered pair, `git check-attr merge` is `unspecified` there, and this unit lands first because the
  sibling is gated on `TOOL-cBriefedPilot-21`'s verdict token. AC9 pins the sentence the sibling
  replaces as byte-unchanged. §4 Data model adds the check that the correction does not falsify this
  build's own total-order declaration under owner decision 4's `#` column, verified pair by pair.
  Found while folding, same class as the set-level MEDIUM the audit raised against other specs: AC6
  pinned the read-path TOTAL at the 70268 B measured at `base 96141aed`, a shared figure that grows
  with `memory/DECISIONS.md` and `memory/LIVE.md` through every unit of this build and that check 16
  does not assert. It now names `READ_PATH_CEILING` and this unit's own parent commit.

## 10. Reuse audit

Recall terms used, recorded so a resumed session re-runs the same query: `build method template render
parity dogfood ids derived roster front matter parallelism write set generated index displacement
budget`.

| Behaviour needed | Existing seam | Decision |
|---|---|---|
| render a shipped template into its live copy | `kit-dogfood-parity.test.sh --render` and its `PAIRS` list | REUSE unchanged — the pair is already declared and already gated |
| know what `ids:` actually holds | `apply_front_matter_ids` at `gen_build_index.py:473` and `rosters` at `:260` | REUSE unchanged — this unit describes it, never changes it |
| keep the live copy under a read budget | hygiene checks 6 and 16 | REUSE unchanged — S5 keeps the file inside both without moving either |
| re-stamp a watched manifest | `manifest-check.sh` C5 and the stamp rule in the manifest's own ratchet section | REUSE unchanged |
| edit M6 without colliding with the open sibling that also edits it | `TOOL-cBriefedPilot-15` branch A, over line 148 of both halves of the pair | NO SEAM — `git check-attr merge` is `unspecified` for both files, so the collision is hand-resolved by whoever lands second |

The map probe for "render a governance document from a shipped template" returned
`kit-dogfood-parity.PAIRS` under the `build-method` dossier as the only seam for this pair, and the
`render_*` family in `map_lib.py` and `gen_build_index.py` as unrelated renderers of generated data.
Every measurement in §4 was taken from the tracked blobs at writing time; every claim about M2, M6,
M9 and M1 was read from `memory/guides/BUILD-METHOD.md` itself.
