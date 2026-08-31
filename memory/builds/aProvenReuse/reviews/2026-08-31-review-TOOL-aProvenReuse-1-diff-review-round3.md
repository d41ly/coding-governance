**Serves:** diff-review TOOL-aProvenReuse-1 TOOL-aProvenReuse-2 TOOL-aProvenReuse-5

# aProvenReuse — closing diff review: round 2's fold, round 3

Round 3 · 2026-08-31 · node `a` · branch `branch/unattended-kit-gaps-a3b869` · one synthesis pass
over the finder/skeptic corpus, with every load-bearing claim re-run against the worktree before it
was written down. The predicate findings below were reproduced by EXECUTING the shipped awk over
constructed sections and over the tracked corpus, never by reading it.

**Range reviewed:** `a32227b6...HEAD` — HEAD `67b84988`, one commit, 11 files, +460/−38. The subject
is round 2's FOLD and nothing earlier. Round 1 graded `3bfc5e87..62b6ec19`, round 2 graded
`62b6ec19..a32227b6`; their findings are inputs here, not targets.

## Verdict: BLOCKED

One blocker, one high, three mediums, three lows. The loop does NOT converge this round. The blocker
is not new work — it is the unapplied half of round 2's own F10 fix, and the fold's code comment, the
ratified spec and the commit message all cite as justification a page that says the opposite. Round 1
found 2 blockers, round 2 found 1, round 3 finds 1; the count has stopped falling, and every round's
blocker has been in the FOLD TEXT rather than in the code the fold was closing.

**Review shape:** raw 15 · confirmed 11 · refuted 4 · unverified 0 · precision 0.73. The 11 confirmed
are reported as 8 findings: four of them (ids 1, 3, 6, 12) are four anchors on one defect and are
consolidated into F1, whose fix touches every anchor at once. Nothing was dropped in the merge.

## Findings

| # | Sev | File:line | One line |
|---|---|---|---|
| F1 | **BLOCKER** | `tools/memory-tree/SPEC-TEMPLATE.template.md:141` | The authoring contract still documents the per-LINE terms cut this commit deleted, and three carriers assert "the template states the order" when it states none |
| F2 | HIGH | `tools/memory-tree/check-memory-hygiene.sh:1112` | The probe-arm failure line names remedies already on the page; the fault is ORDER and the message never says so — and this fold WIDENED the class |
| F3 | MEDIUM | `memory/builds/aProvenReuse/spec/2026-08-31-spec-TOOL-aProvenReuse-1.md:79` | S7 claims a self-test arm that reds on "the SKELETON's own §10 body"; no arm reads the skeleton's body |
| F4 | MEDIUM | `memory/builds/aProvenReuse/spec/2026-08-31-spec-TOOL-aProvenReuse-2.md:41` | S2's `met` outcome specifies a timestamp `DOD_OUT` never emits |
| F5 | MEDIUM | `memory/builds/aProvenReuse/RUN.md:34` | Five of round 2's confirmed findings carry no disposition at the round that decides closure |
| F6 | LOW | `tools/memory-tree/check-memory-hygiene.sh:1101` | A terms list whose marker is written LAST still satisfies both arms alone — the could-not-fail hole the arm exists to close, in a different spelling, undeclared |
| F7 | LOW | `tools/memory-tree/check-memory-hygiene.test.sh:215` | "Both specs" against the checker's newly-rewritten "All three specs" — a two-answers-to-one-question created by this commit |
| F8 | LOW | `tools/unattended/unattended.test.sh:3424` | The retired `kit-absent` vocabulary survives in the comment that justifies the three-skip pin |

---

### F1 — BLOCKER · the §10 authoring contract describes a mechanism this commit deleted

`tools/memory-tree/SPEC-TEMPLATE.template.md:141-143`, and byte-for-byte its render
`memory/TEMPLATE-SPEC.md:141-143`.

The fold replaced the probe blob's per-LINE terms cut with a whole-SECTION truncation at the first
terms marker (`check-memory-hygiene.sh:1099-1101`). It touched neither the template nor the render:
`git diff a32227b6 67b84988 -- tools/memory-tree/SPEC-TEMPLATE.template.md memory/TEMPLATE-SPEC.md`
is empty. Both still read:

> The probe half is scanned over the section with each TERMS VALUE removed … The line PREFIX
> survives, so the ordinary one-line form — the finding, then the terms — still satisfies both.

Per-VALUE removal imposes no ordering at all and is strictly wider than what shipped. Nothing after
the first marker is scanned any more, on any line. I ran the shipped expressions over constructed
sections:

| §10 body, line by line | hasT | hasP | verdict |
|---|---|---|---|
| `Recall terms used: alpha … theta.` / `No existing seam fits; reuse_lookup.py named nothing.` | 1 | 0 | **RED** |
| `The recall CLI needs 8-14 terms passed via --terms.` / `reuse_lookup.py cites tools/x.py:10.` | 1 | 0 | **RED** |
| a fenced `query.py --terms "a b c"` invocation / `reuse_lookup.py names tools/x.py.` | 1 | 0 | **RED** |
| `Recall terms used: alpha beta.` / `reuse_lookup.py names tools/x.py.` / `Re-run with the same recall terms.` | 1 | 0 | **RED** |
| `No existing seam fits.` / `Recall terms used: alpha beta gamma.` | 1 | 1 | pass |

The first row reds with *"does not record the probe result"* about a section that records it
verbatim. The second is the natural shape for any spec whose subject IS the recall kit — a prose
mention of `--terms` before the finding is enough to red it. The third is the shape a diligent author
reaches for: paste the invocation you actually ran in a fence, then state what it returned. There is
no fence tracking in the predicate, so a marker inside a code block cuts the section exactly as one
in prose does. I confirmed that row against BOTH revisions: it PASSED under the per-line cut at
`a32227b6` and REDS at `67b84988`, so it is fold-introduced, not inherited.

Measured over the tracked corpus with the old and new predicates side by side: 286 Tier-2 specs, 82
pass both arms under the per-line cut, 76 under the whole-section cut, **6 flip pass → red**
(`aRuledFrontispiece-2/-4/-6/-10`, `aPrimedKeepalive-6`, `dFramedEntrypoint-1`). All six are
grandfathered by `SPEC10_EVIDENCE_CUTOFF="2026-09-01"` — which is tomorrow. The class is live, the
population is not.

The second half is worse than the drift. Three carriers state a fact that is false:

- `tools/memory-tree/check-memory-hygiene.sh:1094` — "The template states the order"
- `memory/builds/aProvenReuse/spec/2026-08-31-spec-TOOL-aProvenReuse-1.md:65` — "the template states the order"
- the HEAD commit message — "all 5 are grandfathered, the template states the order"

It does not. Its §10 prose states no order; only the copyable skeleton's bullet sequence (probe
first, then terms, at lines 259-260) implies one, and a bullet order inside a skeleton is not a
stated rule. So the ordering constraint — the entire reason the new cut is defensible rather than
arbitrary — is written down nowhere, and its stated source contradicts it.

Round 2's F10 asked for the constraint in the header comment **and** the §10 doc section. Only the
comment half landed, citing the half that refutes it. That is precisely the
amendment-leaves-its-other-half-standing class this round was convened to close.

**Fix.** Replace `SPEC-TEMPLATE.template.md:141-143` with the shipped semantics — *the probe half is
scanned over the section TRUNCATED AT THE FIRST terms marker, so record the probe result BEFORE the
terms line* — delete the "line PREFIX survives" sentence, re-render `memory/TEMPLATE-SPEC.md` via
`bash tools/memory-tree/kit-dogfood-parity.test.sh --render`, and re-run
`bash tools/check-kit-versions.sh`. Add the ordering to spec-1's S5 so a scope item owns it. Then,
and only then, `check-memory-hygiene.sh:1094` and spec-1's S3 become true. `tools/memory-tree/README.md:40`
names the two facts and no order either; add it there or it becomes the next stale carrier.

If the ordering is judged too strict for authors, take F10's other branch instead: cut at the terms
VALUE's end (blank line or next bullet head) rather than at the end of the section, and the doc's
current text becomes true again.

**Left-shift gate.** `kit-dogfood-parity.test.sh:53` pairs template against render, so both are
stale together and the leg stays green — the pair is ungated in the direction that matters. Add an
arm to `check-memory-hygiene.test.sh` that extracts the §10-rules paragraph from
`SPEC-TEMPLATE.template.md` and asserts it contains the string the predicate actually implements
(`truncated at the first` / `before the terms`) and does NOT contain `each TERMS VALUE removed`.
That is a coupling gate between a predicate and its remedy page, and it is the only thing that would
have caught this fold.

---

### F2 — HIGH · the probe-arm diagnostic names the wrong fault, over a surface this fold widened

`tools/memory-tree/check-memory-hygiene.sh:1110-1112`.

Whenever the probe fact sits after the terms marker, the emitted line is:

> `§10 Reuse audit does not record the probe result (a reuse_lookup citation, an explicit "no
> existing seam fits", or a named reuse-first waiver); required at/after SPEC10_EVIDENCE_CUTOFF …`

All three named remedies are already on the page. The author's only possible next move is to add a
fourth copy of a fact they already wrote. The word "order" appears nowhere in the message, and per
F1 it appears nowhere in the page the message implicitly sends them to.

This is round 2's F10 not merely unfixed but **widened**. `git log -S'substr(s10, 1, cutT - 1)'`
puts the whole-section truncation in this fold. Under the per-line cut only the remainder of the
marker's own line was discarded; under the new cut every subsequent line is. The multi-line
terms-then-probe section that passed at `a32227b6` reds at `67b84988` — that is the 6-spec flip
measured in F1. The message did not change.

The comment at `:1094` asserts "the failure message names the missing fact". For this class the fact
is not missing.

**Fix.** Split the message. When a probe token is present in `s10` but absent from `s10p`, print
*"§10 Reuse audit records the probe result only AFTER the recall terms — move it above them"*
instead of the missing-fact line. Both blobs are already in scope; this is one `else if`.

**Left-shift gate.** A fixture whose §10 carries the terms first and a `reuse_lookup` citation
second, with a `hit` on the new ordering message — the same shape as fixture 86 with the two
appended lines swapped. Without it the ordering branch is a message nobody has ever seen fire, which
is the assertion-about-nothing class §7 names.

---

### F3 — MEDIUM · S7 claims skeleton-body coverage the suite does not have

`memory/builds/aProvenReuse/spec/2026-08-31-spec-TOOL-aProvenReuse-1.md:79`.

The fold rewrote S7 to claim an arm in which "the SKELETON's own §10 body reds". No arm reads the
skeleton's body. `evskel()` at `check-memory-hygiene.test.sh:223` is
`sed 's|^No existing seam fits\.$|REPLACE both bullets. Delete this paragraph.|'` — one hand-typed
sentence lifted out of the skeleton. The real skeleton §10
(`SPEC-TEMPLATE.template.md:248-260`) is a bolded paragraph, that sentence, and two bullets. Grep
over `tools/` shows the template's bytes are read by exactly two things — `adopt-memory-tree.sh`
(renders it) and `kit-dogfood-parity.test.sh` (diffs render against source) — and neither feeds any
of it to the §10 predicate.

Concrete failure path: add "or no existing seam fits" to the first skeleton bullet and every
unfilled §10 scores `hasP=1` while fixture 85 stays green. I confirmed the current body scores
`hasT=0 hasP=0`, so this is a coverage gap and not a live break.

Round 2 raised this as F6 and prescribed deriving the fixture body from the source. The fold answered
with prose — S9 plus AC10, a one-shot manual observation nothing re-runs — and then restated the
false coverage claim in stronger words.

**Fix.** Either implement F6 as prescribed (awk the `## 10. Reuse audit` block out of the fenced
skeleton region of `$HERE/SPEC-TEMPLATE.template.md`, splice it into fixture 85, and assert the
extraction is non-empty so a stale range fails loudly instead of splicing nothing), or reword S7 to
say what the arm actually grades — "the skeleton's REPLACE-both-bullets sentence" — and file the
class gap as a backlog row beside `TOOL-aProvenReuse-3`.

**Left-shift gate.** The non-empty assertion on the extraction is the gate: it is what makes a
skeleton edit that moves the section heading fail rather than silently grade an empty string.

---

### F4 — MEDIUM · S2's `met` outcome specifies a timestamp the driver never emits

`memory/builds/aProvenReuse/spec/2026-08-31-spec-TOOL-aProvenReuse-2.md:41`.

S2 says the `met` outcome's `DOD_OUT` "reports the count and the newest row's timestamp, so the
wrap-up carries a number rather than a verdict". `tools/unattended/unattended.sh:3279` emits:

```
DOD_OUT="$_rn recall quer$([ "$_rn" = 1 ] && echo y || echo ies) recorded for this tree"
```

No timestamp — none of the six `DOD_OUT` assignments in the `reuse-probed` arm carries one. AC4
(line 262) pins only "the message carries the row count", and the self-test at
`unattended.test.sh:829-831` asserts only `1 recall query recorded for this tree`. The scope item
disagrees with the code, with its own acceptance criterion, and with its own test — in the rev-6
fold whose stated job was making this spec describe what shipped. Still present in the working tree.

**Fix.** Delete "and the newest row's timestamp" from S2's `met` bullet. (Implementing it instead
costs an extra `tail -1` plus an AC4 amendment plus a test arm, for a field nothing asked for.)

**Left-shift gate.** Not gateable as prose. This belongs in the recurring-bug-class checklist under
the class the build already names: at every `rev-N` bump, diff each amended scope item against the
AC and the self-test that observe it, because an amendment that lands in one of the three is
indistinguishable from one that lands in all three.

---

### F5 — MEDIUM · five of round 2's confirmed findings have no disposition, at the round that decides closure

`memory/builds/aProvenReuse/RUN.md:34`.

The fold's commit message accounts for the blocker plus F2, F3, F4 and F5. Five confirmed defects
are neither fixed nor recorded anywhere as parked:

- **F6** — fixture 85 grades a hand-typed line, not the skeleton (F3 above; `evskel` unchanged).
- **F8** — `unattended.sh:3265-3266` still reads "…and that mismatch returns / correct run.", a
  sentence with its middle clause missing.
- **F9** — the byte-identical `hit 'tFixture-80.md (§10 Reuse audit does not record the probe result'`
  at `check-memory-hygiene.test.sh:702` and `:708`, both still present, still padding the `n` that
  `FLOOR_ASSERTIONS` ratchets. The fold added a new `hit` at `:711`, three lines below the duplicate,
  without noticing it.
- **F10** — widened rather than fixed (F1, F2 above).
- **F11** — `unattended.test.sh:3421-3424` still asserts "dod_met does not clear DOD_OUT on entry"
  while `unattended.sh:2814-2817` carries "CLEARED ON ENTRY" followed by `DOD_OUT=""`, and still
  says "kit-absent" (F8 below). Neither half of F11 was applied; `git show --stat 67b84988` lists
  neither `unattended.sh` nor `unattended.test.sh`.

`README.md:136` "Parked decisions" still reads "None yet". `RUN.md` gained only
`2026-08-31T08:04:46Z review · item aProvenReuse · reason verdict BLOCKED · blockers 1`.
`memory/backlog/TOOL.md` names `TOOL-aProvenReuse-3`, `-4` and (uncommitted in the working tree)
`-6`; none of them is any of the five. Against §1's "every confirmed finding left-shifted" and §7,
five confirmed defects carry no gate, no checklist entry, no backlog row and no park — at the round
the fold declares CONVERGING.

One correction to the finding as raised: the round-2 review record IS committed in this fold with
all eleven findings written out, so they are recorded. They are undispositioned, which is a
different and smaller fault than unrecorded.

**Fix.** Before the loop is allowed to exit, add a parked line per undispositioned finding to
`RUN.md` (or a backlog row under `TOOL`) naming F6, F8, F9, F10 and F11, each with the reason it was
not folded.

**Left-shift gate.** `unattended.sh --close` already reads `parked-decisions-surfaced` with an
optional count. The gateable version of this rule is the same idiom one level up: a `--review`
that writes the confirmed-finding count into `RUN.md` and a `--close` that refuses unless every
confirmed finding from every round is either named by a later fold's commit message or carries a
`park` line. That is a real gate for the one rule this build has now broken twice.

---

### F6 — LOW · a terms list whose marker is written last still satisfies both arms alone

`tools/memory-tree/check-memory-hygiene.sh:1101`.

The truncation removes jargon only AFTER the first marker. Observed silent against the shipped
expressions — a §10 whose entire body is:

```
Terms: reuse_lookup reuse-first seam probe alpha beta gamma delta, passed via `--terms`.
```

scores `hasT=1 hasP=1`. `cutT` resolves to the trailing `--terms`, so `s10p` is everything before it
— the jargon list itself — and the probe half is bought by the terms list alone, recording no probe
result at all.

Not a regression: the per-line cut had the same hole. But the arm's own comment states the two-blob
design exists because "scanning ONE blob let a terms line alone satisfy BOTH arms and the probe half
could not fail", and in this spelling it still can. The section's blind-spot paragraph
(`:1052-1056`) declares only that neither arm is checked for TRUTH; it does not name this structural
hole, and §7 requires a structural check's own header to state what it does not check.

**Fix.** Declare the limit rather than chase it: add to the comment block above the blob computation
that the probe half is defeated by a terms list written before its marker and the predicate cannot
see it. A code fix (require the probe token before the first marker AND at a position preceded by
fewer than N corpus-jargon tokens) buys a narrow case for real complexity.

**Left-shift gate.** None wanted. This is the declared-limit branch of §7, and a fixture pinning a
known-undetectable shape would be a test asserting the gap stays open.

---

### F7 — LOW · "Both specs" against the same sentence's rewrite to "All three specs"

`tools/memory-tree/check-memory-hygiene.test.sh:215`.

`git show HEAD~1:tools/memory-tree/check-memory-hygiene.test.sh` line 215 read "Both specs of the
build that added this arm did exactly that", identical to the pre-fold checker comment. The fold
rewrote `check-memory-hygiene.sh:1083-1084` to "All three specs …" and spec-1's S3 to "all three of
this build's own specs", and left this copy at "Both specs". Three is correct: all three files under
`memory/builds/aProvenReuse/spec/` carry `reuse-first` inside their `Recall terms used:` value,
which is exactly the single-blob defect both comments describe.

Two answers to one question, created by this commit, in the two comments that jointly justify the
two-blob split.

**Fix.** "Both specs" → "All three specs" at `check-memory-hygiene.test.sh:215`.

**Left-shift gate.** Not worth one. The durable fix is to stop stating the count twice: the fixture
comment should point at the checker's comment rather than restate its measurement, which is §6's
"point at the source, or gate the pair" applied to two comments.

---

### F8 — LOW · the retired `kit-absent` vocabulary survives in the three-skip pin's rationale

`tools/unattended/unattended.test.sh:3424`.

Still reads "whose kit-absent outcome is a THIRD legitimate skip". `grep -rn kit-absent tools/`
returns that one live hit and nothing in `unattended.sh`, whose arm 2 is labelled "THE RECALL CLI IS
NOT ADOPTED" and keys on `[ -z "$RECALL_CLI" ] || [ ! -f "$ROOT/$RECALL_CLI" ]`
(`unattended.sh:3236-3242`). This fold retired the label from the protocol row and its render; the
working tree shows the same retirement being applied to spec-2's N6 (`kit absent` → `not adopted`),
uncommitted, which confirms it was deliberate and this carrier was missed. Round 2's F11 named this
exact line.

One correction to the finding as raised: the mechanism was not deleted, only the LABEL was retired,
and the comment's next clause names the real trigger ("the fixture conf declares no `RECALL_CLI`").
The pin's rationale is substantively sound; the vocabulary is stale.

**Fix.** "whose kit-absent outcome" → "whose no-readable-`RECALL_CLI` outcome". The rest of the
sentence is already correct. Fix F11's other half in the same touch: the sentence above it still
asserts "dod_met does not clear DOD_OUT on entry" against `unattended.sh:2814-2817`.

**Left-shift gate.** Fold into the F5 gate. A vocabulary retirement is exactly the class a
`--close` disposition check catches and nothing else does.

---

## Checked and clean

Recorded so the next round does not re-derive them.

- **The `RECALL_CLI` row and check 22 (hunt item 2).** The row is present at
  `PROTOCOL.template.md:546` and describes the shipped arm correctly, including the blank-or-
  unreadable trigger and the declarations-not-constants rationale. The `reuse-probed` row at `:326`
  was rewritten in the same commit and no longer describes the deleted kit-absence probe. The render
  is byte-current: substituting `{{TOOL_ROOT}}` → `tools/` makes `PROTOCOL.template.md` and
  `memory/guides/UNATTENDED-PROTOCOL.md` identical. Check 22's join is satisfied in both directions
  by hand — `RECALL_CLI` is in `.unattended.conf:70`, in `kit.toml`'s `optional_keys`, and in the §8
  table. The one carrier still describing the old behaviour is F8's comment, which check 22 does not
  read. **Caveat:** I could not run `check-unattended.sh` to completion — it exceeded 500 s waiting
  on the remote HEAD advertisement — so the leg's exit code is verified by hand, not observed.
- **Fixture 86 and `evwrap` (hunt item 4).** It constructs the shape it claims. Generated it and
  read the bytes: `## 10. Reuse audit` is the last section `good10` emits, so the `printf` append
  lands inside §10, and the result is a wrapping terms list with `reuse_lookup` on the continuation
  line. It reds for the right arm (`hasT=1 hasP=0` → "does not record the probe result"), which is
  the arm the `hit` at `:711` names. It cannot pass by finding nothing: `hit` asserts presence, and
  if a future `## 11.` were added to `good10` the appended lines would land outside §10, §10 would
  then miss BOTH facts, and the emitted message would be "…the recall terms used AND the probe
  result" — which does not contain the asserted substring, so the arm fails loudly rather than going
  silent. Two cosmetic mismatches, neither worth a finding: the comment says the fixture is "Built by
  DELETING the one-line finding" and the `sed` blanks it rather than deleting it, leaving a stray
  empty line; and the construction's dependence on §10 being `good10`'s last section is load-bearing
  and unstated.
- **§10 as the last section vs followed by another (hunt item 1).** No difference, and no leak in
  either direction. `in10` is set only by `^## 10\. Reuse audit` and cleared by the next `^## `, so
  the blob is bounded by the section. Ran three fixtures: §10 last with probe-then-terms passes; a
  §11 carrying a stray `Recall terms used:` does not disturb a clean §10; and a §11 carrying the
  probe token does NOT rescue a §10 that has terms only, which still reds. The section boundary is
  the one part of this arm that is exactly right.

  *(A marker inside a code fence is NOT clean and is filed under F1 — the predicate has no fence
  tracking, and that shape flipped pass → red in this fold.)*
- **Units 1 and 2 against each other and the build README (hunt item 3).** Scope, interface and
  ordering agree. The unit table at `README.md:158-159` carries rev-4 / rev-6, matching both status
  headers, and the record tables regenerated consistently across all three specs. The only
  acceptance divergences are F3 and F4.
- **Round-2 AC arithmetic — NOT verified.** AC6's "254 before this unit, 262 after its first five
  arms" and the commit message's "memory-hygiene 270 assertions" are unobserved here.
  `bash tools/memory-tree/check-memory-hygiene.test.sh` was started twice on node `a` and produced no
  total within either budget — 10 minutes in the foreground, and still running past 25 minutes in the
  background when this record was written. No assertion count, no exit code. Stated as unverified
  rather than assumed green, and worth its own look: a suite whose own build cites its assertion
  total in an acceptance criterion is a suite somebody has to be able to finish running.

## Not findings, by prior agreement

The bounded-observation wall-clock arms in the unattended suite flaked once under cross-session load
and pass clean (shard 1/2 226, shard 2/2 669). The diff touches zero lines of that machinery, and
the class is already filed as `TOOL-aProvenReuse-6` (uncommitted in the working tree at review time).

## One thing outside the range, noted not filed

The skeleton bullet at `SPEC-TEMPLATE.template.md:259` offers "or that none fits" as the sanctioned
phrasing for a negative probe result. The predicate matches `no existing seam` and `no seam fits`,
neither of which "none fits" contains. An author who follows the skeleton's own wording literally
reds. Pre-existing, untouched by this fold, and the right home for it is the same edit F1 already
requires to that file.
