**Serves:** diff-review TOOL-dTieredTribunal-1 TOOL-dTieredTribunal-2 TOOL-dTieredTribunal-3

# Review — dTieredTribunal, the cumulative diff landing on main

**Measured on:** node `a`, worktree `C:/projects/coding-governance/.claude/worktrees/dtieredtribunal-build-spec-7218ea`, clean.
Every finding below was re-read in the shipped file before it was written down; line numbers are from
that read, not from the finder's report.

**Range:** `da9e4cd28072501cd4fe87a81db36c01b9a80f9e...HEAD` — eight commits, 23 files, +2048/-68.
Three product units (`4c9f752f`, `7ce98b64`, `668eb2e3`) sit on top of five records-only commits.

**Round:** 1. First adversarial review of the cumulative diff. The three spec-audit rounds already in
`reviews/` audited the SPEC; this is the first review of the CODE.

## Verdict: CLEAN WITH FIXES

Nothing here blocks the landing. Two high findings should be fixed before the merge because both are
one-line reorderings that restore the exact property the build was written to add, and shipping the
kit at 1.7 with either one in it exports the hole to every adopter.

**Shape:** raw 20 · confirmed 6 · refuted 14 · unverified 0 · precision 0.30.

The 6 confirmed collapse to **4 distinct defects** — the lens fan raised the note-ternary defect twice
(ids 2, 6) and the count-word defect twice (ids 3, 13). Adjudicated severity is **0 blockers · 2 highs
· 2 mediums**. That differs from the raw labels (five medium, one low): I raised D3 from low because
an acceptance criterion is unmet on its face, and I merged two mediums into one high (D1) because the
duplicate pair together establishes reachability the single report did not.

Precision 0.30 is below §8's ~0.5 floor. Fourteen of twenty findings were refuted, which says the
lens priming was loose for a diff this small, not that more agents were needed. Worth noting for the
next round on this build; not a finding.

## The findings

| # | Sev | Where | Defect |
|---|-----|-------|--------|
| D1 | HIGH | `drift-audit-state.js:466`, `drift-audit-code.js:446`, `tier2-review.js:447` | the `note` ternary tests the lesser degradation first, so a dead synthesis is announced as PARTIAL |
| D2 | HIGH | `drift-audit-state.js:430`, `drift-audit-code.js:413` | none of the seven new trust counters reaches the synthesis prompt, so the persisted report can certify a degraded run as clean |
| D3 | MEDIUM | `drift-audit-code.js:235`, `drift-audit-state.js:248` | the comment and AC4 both claim a `LENSES.length > 0` conjunction that no condition in either file spells |
| D4 | MEDIUM | `tier2-review.js:362` | "the only three things that may precede the body", followed by four |

---

### D1 — HIGH — the note announces the smaller failure and hides the larger one

`tools/workflows/drift-audit-state.js:466` (identical at `tools/workflows/drift-audit-code.js:446`):

```js
note: lensesDead || skepticsDead || unverified.length
  ? `PARTIAL: ${lensesDead} lens(es) and ${skepticsDead} skeptic batch(es) died, ${unverified.length} finding(s) unverified`
  : !synth
    ? 'UNVERIFIED: the synthesis agent died, so NO report was written'
    : 'complete',
```

The `!synth` branch — the one S6 exists to surface — is unreachable whenever any of the three lesser
conditions holds. `unverified.length > 0` alone is enough, and that is the ordinary case: a skeptic
batch that dies guarantees unverified findings, and the demote-on-conflict added at
`drift-audit-state.js:370` (`for (const id of conflictIds) vmap.delete(id)`) manufactures them on
otherwise healthy runs. So a run that lost its entire report reports itself as `PARTIAL: 1 lens(es)
and 0 skeptic batch(es) died, 3 finding(s) unverified` and never states that no report exists. The
honest string is emitted only in the least-degraded-otherwise combination, which is the rarest one.

This inverts the repo's own most-severe-first doctrine inside the single field a caller quotes as the
run's verdict. `report: null`, `summary: null` and the `WARNING: the synthesis agent DIED` log at
`drift-audit-state.js:447` are mitigations, not repairs — an orchestrator that reads `note` first will
not consult them.

The `!synth` branch is NEW in both drift files in this diff (TOOL-dTieredTribunal-3 S6), so the
defect is introduced here. `tools/workflows/tier2-review.js:447` has the same precedence and is
pre-existing; it is unchanged by this diff but must be fixed with the others, or kit 1.7 ships the
hole to adopters as the reference spelling.

**Fix.** Hoist the synthesis-death test to the front of the chain in all three files:

```js
note: !synth
  ? 'UNVERIFIED: the synthesis agent died, so NO report was written'
    + (lensesDead || skepticsDead || unverified.length
      ? ` (also ${lensesDead} lens(es), ${skepticsDead} skeptic batch(es) died, ${unverified.length} unverified)`
      : '')
  : lensesDead || skepticsDead || unverified.length
    ? `PARTIAL: …`
    : 'complete',
```

In `tier2-review.js` the `judged === 0` branch stays first; `!synth` goes second, ahead of the
`lensesDead ||` test.

**Left-shift gate.** One awk leg over `tools/workflows/*.js`: in every `note:` ternary chain, assert
the `!synth` test appears before the first `lensesDead ||` test. Three files, one predicate, and it
reds on the next harness that copies this shape. Run it against the tree before wiring it — per §7,
print hits and near-misses, because the `judged === 0` branch in `tier2-review.js` is a legitimate
earlier test and the predicate must not red on it. If that proves too brittle, the fallback is a
`memory/gotchas/` class (`severity-ordered-chain-inverted`) so it joins the §10 checklist for every
diff touching a harness — weaker, but honest, and an exemption is not coverage.

---

### D2 — HIGH — the durable report cannot say the run was degraded

The synthesis DATA block at `tools/workflows/drift-audit-state.js:430` interpolates counts, precision,
the surviving lens writeups and the judged findings. `drift-audit-code.js:413` adds `severity
corrections ${downgrades}`. Neither passes `lensesDead`, `skepticsDead`, `conflicts`, `duplicates` or
`spurious`. All five reach the return object and the run log and stop there.

The partially-degraded path is reachable by construction: the all-dead early return fires only at
`lensesDead === LENSES.length`, so four of five lenses dying falls straight through to synthesis with
raw 0. The prompt then instructs the agent, at `drift-audit-state.js:414` and
`drift-audit-code.js:396`, to explain why a zero count is "positive evidence rather than an absence of
checking". The written drift-audit report — the artifact read months later, when the log is gone —
therefore certifies a degraded run as clean, in the unit whose entire subject is that absence is not
cleanliness.

`note: PARTIAL: …` covers the immediate caller only, and D1 above compromises even that. Spec-3 does
not require this interpolation, so this is a gap rather than an unmet AC. It is a gap in the unit's
own subject.

**Fix.** One line into each DATA block:

```
run health: ${lensesDead} of ${LENSES.length} lenses died, ${skepticsDead} of ${batches.length} skeptic batches died, ${conflictIds.size} verdicts demoted on conflict, ${spurious} spurious, ${duplicates} duplicate
```

Plus one prompt rule: if any of those is non-zero, the verdict paragraph says so before any count is
called positive evidence.

**Left-shift gate.** A grep leg asserting every synthesis prompt template in `tools/workflows/*.js`
interpolates `${lensesDead}`. One expression, three files, and it reds the moment a future harness
computes a liveness counter and forgets to hand it to the agent that writes the record. This is the
cheapest available form of §7's "a probe that cannot move says so", applied to the artifact rather
than to the return value.

---

### D3 — MEDIUM — the comment and AC4 describe a conjunction the code does not contain

`tools/workflows/drift-audit-code.js:235`, byte-identical at `drift-audit-state.js:248`:

> The predicate is guarded on `LENSES.length > 0` and never the bare `lensesDead === LENSES.length`.

The shipped predicate is exactly the bare form — `if (lensesDead === LENSES.length)` at
`drift-audit-code.js:252` and `drift-audit-state.js:265`. The empty case is excluded by branch ORDER,
by the `if (LENSES.length === 0)` early return above it, not by the stated conjunction.
`grep -n 'LENSES.length > 0' tools/workflows/*.js` returns the two comment lines and nothing else, so
a reader who greps for the guard finds only the claim that it exists.

Behaviour is correct today. Two things are not.

AC4 is unmet on its face. `memory/builds/dTieredTribunal/spec/2026-08-26-spec-dTieredTribunal-3.md:303`
requires that "The condition tests `LENSES.length > 0` as well as `lensesDead === LENSES.length`", and
line 44 spells the conjunction literally. No condition in either file tests it. The build is landing
against a criterion its code does not satisfy, and the comment restates the unmet half as accomplished
fact — the comment-prose-satisfies-itself shape the charter names in §7.

The protection is also positional, and in one file it is positional over a branch that can never fire.
`drift-audit-code.js:116` declares `LENSES` as a bare array literal with no caller filter, so its
`LENSES.length === 0` branch is unreachable. A future dead-code pass that deletes it silently
re-exposes the `0 === 0` misread the comment swears was never written. In `drift-audit-state.js` the
branch is reachable, so the two files are not equally fragile despite carrying the same comment.

**Fix.** Spell what the comment and the spec both already say — `if (LENSES.length > 0 && lensesDead
=== LENSES.length)` — in both files. That is a two-token edit that makes the code, the comment and
AC4 agree, and it is a smaller diff than any gate. The alternative, rewording the comment to describe
branch order, leaves AC4 unmet and leaves the fragility.

**Left-shift gate.** None needed if the fix is taken: the class here is
`two-answers-to-one-question`, and making the code match the words removes the second answer rather
than policing it. If the comment is reworded instead, the compensating check is a spec-audit arm that
greps the shipped source for each literal predicate an AC names — which is the more general gate, and
worth building only if this recurs.

---

### D4 — MEDIUM — a count word contradicted by its own list

`tools/workflows/tier2-review.js:362-365` emits:

> THE RECORD'S OPENING IS ORDERED, and these are the only three things that may precede the body.
> First the `**Serves:**` binding line described below. Then the report's title and provenance. Then
> the range line named above. Then, as a heading of its own, the literal ``## Verdict: `` …

Four items, introduced as three. All four precede the body — the prompt itself sends counts and
caveats "in the paragraph beneath that heading" — so the count is off by one.

The source comment above it is correct and is where the number came from: it counts three claiming
SENTENCES (binding line, range line, verdict heading), title-and-provenance not being one. The word
was carried into the emitted prompt, where it counts a different population. Spec-1
(`spec/2026-08-26-spec-dTieredTribunal-1.md:54`) has the same split: "Three sentences claim an
opening" beside an S4 enumeration of four elements.

This is live, not hypothetical: the prompt that produced THIS report carried the sentence verbatim,
and resolving "three" against four was work the instruction was written to eliminate. It is the one
sentence in the prompt whose stated job is to stop the agent resolving an opening collision by itself.

Impact is bounded by the gates downstream. A dropped ``## Verdict: `` heading reds hygiene check 22
(`REVIEW_VERDICT_CUTOFF="2026-08-22"` is live in `.memory-tree.conf`; `check-memory-hygiene.sh:623-656`
fails a post-cutoff record with no verdict line). A `**Serves:**` line pushed past the binding-head
window reds check 21. The unguarded casualty is the range line, which the unattended kit's
`closing-review-recorded` joins on.

**Fix.** Delete the count: `THE RECORD'S OPENING IS ORDERED, and nothing but the following may
precede the body.` The enumeration already carries the rule, and §7's "no count of a derived
population is written in prose" says the number should not have been there. Fix the spec's S4 sentence
in the same commit or the two records disagree again.

**Left-shift gate.** Ungateable cheaply — no predicate distinguishes a correct cardinal from a wrong
one. It joins §10 through the class this build itself added, `fold-text-is-unreviewed-surface`: the
count was introduced in fold prose and never re-read against the list beneath it. The documented
check is that a fold re-reads any sentence carrying a cardinal against the enumeration it introduces.
Deleting the count is the stronger move, because it removes the thing that can go stale.

---

## What I did not check

- **No gate was run.** This review is a read of the diff; `bash tools/run-gates/run-gates.sh` was not
  executed here and no leg verdict in this record is measured. The landing still owes a green bar.
- **The three drift/review harnesses were not executed.** Every claim about runtime behaviour above is
  from reading the control flow, not from a run. D1 and D2 are deterministic from the source and do
  not need one; nothing else here asserts a runtime outcome.
- **Unit 2's generated artifacts were not re-derived.** `memory/gotchas/INDEX.md`,
  `memory/map/generated/MAP.md` and `inventories.json` are asserted fresh by their own gate legs and I
  did not re-render them to confirm. The `baseline.toml` shrinks by seven keys, which is the direction
  the ratchet requires, but I checked the direction and not the key identities.
- **The kit 1.6→1.7 version bump was checked for count, not content.** Five sites were named in the
  task; I did not verify each one, nor that the BREAKING migration paragraph describes every breaking
  change (the `lensesRun` array-to-integer change is documented; I did not audit the paragraph against
  the full diff).
- **The 14 refuted findings were not re-litigated.** The skeptic verdicts stand.

## One note on this record

The class `fold-text-is-unreviewed-surface` that unit 2 adds applies to this file. Nothing has
reviewed the prose above, and D4 exists precisely because a previous round's fix was folded into fresh
sentences nobody re-read. If a second round runs on this build, the four findings here are already
adjudicated — the unreviewed surface is this report's own wording.
