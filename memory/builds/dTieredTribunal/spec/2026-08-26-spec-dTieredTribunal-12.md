# TOOL-dTieredTribunal-12 — M4 stops forbidding what the harness can now do

**Status:** INPROGRESS · rev-2 · 2026-08-26 · node a · Tier-2 · base cd971285 · order 5 · streams tooling

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-08-26-review-TOOL-dTieredTribunal-11-closing-diff.md](../reviews/2026-08-26-review-TOOL-dTieredTribunal-11-closing-diff.md) | diff-review | TOOL-dTieredTribunal-11 TOOL-dTieredTribunal-13 TOOL-dTieredTribunal-14 TOOL-dTieredTribunal-15 |
| [2026-08-26-review-TOOL-dTieredTribunal-11-spec-audit-round1.md](../reviews/2026-08-26-review-TOOL-dTieredTribunal-11-spec-audit-round1.md) | spec-audit | TOOL-dTieredTribunal-11 TOOL-dTieredTribunal-13 TOOL-dTieredTribunal-14 TOOL-dTieredTribunal-15 |
| [2026-08-26-review-TOOL-dTieredTribunal-11-spec-audit-round2.md](../reviews/2026-08-26-review-TOOL-dTieredTribunal-11-spec-audit-round2.md) | spec-audit | TOOL-dTieredTribunal-11 TOOL-dTieredTribunal-13 TOOL-dTieredTribunal-14 TOOL-dTieredTribunal-15 |

<!-- /gen:spec-records -->

## 1. Goal

`memory/guides/BUILD-METHOD.md:116` reads "**Not the harness.** `tier2-review.js` reviews DIFFS; a
spec is not code, so calling one reviewed by it is false." `TOOL-dTieredTribunal-11` gives that
harness a subject descriptor, and the moment it lands this sentence is false about the tool it names.
Replace it with a MECHANISM clause that says what the harness must be given before a spec audit may
claim it, so the rule stays checkable instead of resting on a category assertion nobody can refute.
The owner authorized exactly this amendment at `TOOL-dTieredTribunal-7` in `memory/DECISIONS.md:107`,
which is what lifts M3's veto 2 for this one rule and for nothing else.

The rule is worth restoring rather than deleting because it already lost its mechanism once. Its
wording history is in this build's research record: present with a mechanism clause on 2026-08-11,
deleted rather than displaced on 2026-08-20, and restored on 2026-08-21 shortened to "a spec is not
code" with no recorded decision. The version at HEAD states a conclusion whose stated ground cannot
be falsified. A deletion would leave M4 telling a reader to run a `Workflow` script while saying
nothing about which one or what it needs, which is the state the 2026-08-20 deletion produced and an
adversarial round caught.

Every line citation in this spec was re-derived against source at `96f11c0e`, the branch tip this
spec was authored on, not copied from the research record, whose own citations have drifted.

## 2. Scope (IN)

- **S1** — the paragraph at `memory/guides/BUILD-METHOD.md:116` is REPLACED, not extended, by the
  three lines §4 spells. The replacement keeps the rule's normative half — a run that did not declare
  the subject may not call a spec reviewed — and adds a mechanism clause naming the missing input.
- **S2** — the identical replacement lands at `tools/memory-tree/BUILD-METHOD.template.md:116`. That
  file is the authored source and the live guide is its render, and the two are paired in `PAIRS` at
  `tools/memory-tree/kit-dogfood-parity.test.sh:53`. Line 116 carries no `{{KIT_DIR}}` or
  `{{TOOL_ROOT}}` placeholder, so the two edits are byte-identical.
- **S3** — `--render` is NOT run. The ground is finding F3 of
  `memory/builds/aBoundedVerdict/reviews/2026-08-21-review-TOOL-aBoundedVerdict-1-round3.md`, which
  measured that `--render` copies template over live, so reaching for it as the remedy for a
  live-only edit deletes the fix being reported. Both files are edited by hand and
  `bash tools/memory-tree/kit-dogfood-parity.test.sh` is the check that they agree.
- **S4** — the net byte delta is MEASURED before the commit and stated in the commit message. The
  measured candidate is +161 bytes, which lands the live guide at 24546 and the template at 24557
  against a declared 24576. If a wording change pushes either file over, the WORDING is trimmed. The
  cap is not raised: `memory/guides/BUILD-METHOD.md:8` states it and M3's delegation at `:76`
  expressly does not reach M1's own budget.
- **S5** — `memory/map/features/build-method.md:87-91` is the dossier bullet that paraphrases this
  rule, and its claims block names `BUILD-METHOD.md` under `guides`. It is rewritten to describe the
  amended rule. The charter's Definition of Done already owes a dossier refresh on touch, and this is
  the dossier that owns the touched file.
- **S6** — `memory/map/features/review-harnesses.md:84-86` opens "The build method forbids
  `tier2-review.js` on a spec audit", which is a premise this unit falsifies. That dossier's claims
  block names `tier2-review.js`, so `TOOL-dTieredTribunal-11` owes it under the same
  dossier-on-touch rule and is expected to have refreshed it. This unit is the BACKSTOP and edits it
  only if the sentence still asserts the ban when this unit runs. It runs last, so there is no
  concurrent writer either way.
- **S7** — the `TOOL-dHonouredPark-5` row at `memory/backlog/TOOL.md:204` contains the clause "M4
  rules that harness out for spec audits because it reviews diffs, which is true and is not the
  point". That clause is corrected in place. The row's ASK is untouched and the row stays OPEN: it
  asks M4 to carry the orchestrator-assigned-id rule so a bespoke script inherits it, and a bespoke
  script is still writable after this unit.
- **S8** — the replacement names the CAPABILITY, never the field spelling. It says the call must name
  the spec kind and points at the harness's own `args` header at
  `tools/workflows/tier2-review.js:27-32` for how. `TOOL-dTieredTribunal-11` owns that spelling, and
  a rule that hardcoded it would go stale the first time that unit renamed an argument.

## 3. Non-goals (OUT)

- **Any change to `tools/workflows/tier2-review.js`.** This unit edits documents. The capability the
  amended rule describes is `TOOL-dTieredTribunal-11`'s, and this unit is sequenced after it for that
  reason.
- **Any other paragraph of M4.** The lens sentence at `memory/guides/BUILD-METHOD.md:124-126`, the
  `Workflow`-not-`Agent` paragraph at `:118-122`, the record paragraph at `:128-133` and the BLOCKED
  disposition at `:135` are all untouched. The owner's grant at `TOOL-dTieredTribunal-7` names the
  `Not the harness` rule and nothing else, so any other M4 edit is back under M3's veto 2.
- **The lens-catalogue carrier count.** After `TOOL-dTieredTribunal-11` the four M4 lens names may
  exist in three places: M4's own sentence, `tools/memory-tree/README.md:210-214`, and a lens array
  in the harness. That is proposal P3 in this build's research record, it is PARKED at build level,
  and deleting M4's four names to close it would contradict M11's own stated pattern of names here
  and scopes there. Recorded, not fixed.
- **Raising, lowering or gating M1's budget.** Whether a gate should ever enforce the pair is called
  a separate question nobody has ruled at `memory/guides/BUILD-METHOD.md:16-18`, and it stays one.
- **`memory/guides/REVIEW-PROTOCOL.md`, `coding-governance-agents.template.md` and `AGENTS.md`.**
  Verified: `git grep -n "reviews DIFFS"` and `git grep -ni "pointed at a document"` return no hit in
  any of the three, so none of them carries this rule. They describe the harness generically and this
  amendment does not reach them.
- **Historical records.** The build README problem slot at
  `memory/builds/dTieredTribunal/README.md:13`, the research record, and the review records under
  `memory/builds/` all quote the rule as it stood. M3 reserves the README's description slot from a
  run under the mandate, and a review record is a dated observation. None is rewritten.
- **A new gate leg.** Nothing here is gateable that is not already gated. `kit/dogfood doc parity`
  reds on template-against-render drift and `method carriers (every pointer declared)` reds on an
  undeclared pointer. A leg asserting that a prose rule is falsifiable would be a structural check
  reading as a semantic one.
- **A memory-tree kit version bump.** `tools/memory-tree/check-verdict-epoch.sh:68-69` scans
  `check-memory-hygiene.sh` and six named Python delegates, and no doc template is in that set, so a
  prose edit to the shipped method does not arm the epoch rule. The `gov:kit memory-tree@` marker on
  line 1 of both files is unchanged.

## 4. Design

### The replacement

Three lines replace one. The candidate wording, measured at 275 bytes:

```
**The harness needs a DECLARED subject.** `tier2-review.js` audits a spec only when the call
names the spec kind. Undeclared, it acquires a diff and primes code-shaped lenses, so calling
a spec reviewed by that run is false. The spelling is in that file's own `args` header.
```

Sentence by sentence, because each one does a job the rule at HEAD stopped doing.

The bold lead states a REQUIREMENT rather than a prohibition. "Not the harness" named a tool and
banned it, so a reader who then reads `TOOL-dTieredTribunal-11`'s code finds the ban false and has no
way to tell which half of the rule survived.

"audits a spec only when the call names the spec kind" is the mechanism, and it is checkable from
outside: read the `Workflow` call and see whether it named one. The old wording's ground was "a spec
is not code", which no observation can contradict.

"Undeclared, it acquires a diff and primes code-shaped lenses" says what actually goes wrong. It is
the surviving true half of the 2026-08-11 wording, re-pointed from the tool to the call.

"so calling a spec reviewed by that run is false" is the original normative clause, carried verbatim
in force if not in bytes. This is the sentence M4 exists to say.

"The spelling is in that file's own `args` header" is the pointer M1's one rule requires. The
argument's name and legal values live at `tools/workflows/tier2-review.js:27-32`, and M4 restating
them would make the method the second carrier of an interface it does not own.

### The byte budget

| file | at `96f11c0e` | after +161 | declared cap |
|---|---|---|---|
| `memory/guides/BUILD-METHOD.md` | 24385 B, 315 lines | 24546 B, 317 lines | 24576 B, 350 lines |
| `tools/memory-tree/BUILD-METHOD.template.md` | 24396 B, 315 lines | 24557 B, 317 lines | 24576 B, 350 lines |

The cap is declared in M1 at `memory/guides/BUILD-METHOD.md:8` and was set by the owner at
`TOOL-dHonouredPark-2`, which named the BYTE half as the binding one. The template is 11 bytes larger
than its render because six placeholder tokens are longer than the paths they resolve to, so the
template is the tighter of the two and 19 bytes is what this edit leaves it. That figure is a
disclosure, not a problem this unit solves: M1's own text says exceeding the budget silently was the
one option not taken, and the next M4 change will have to trim or ask the owner.

The line half is not close. Two lines are spent against 35 available, which is exactly what M1 means
by most of the line figure being headroom the bytes do not grant.

### Inventory

Every carrier of this rule found in the tree, and what happens to each. Four sweeps found them, each
run over the whole tree: `git grep -n "reviews DIFFS"`, `git grep -n "spec is not code"`,
`git grep -ni "pointed at a document"` and `git grep -n "Not the harness"`.

| carrier | what it holds | disposition |
|---|---|---|
| `memory/guides/BUILD-METHOD.md:116` | the rendered rule | replaced, S1 |
| `tools/memory-tree/BUILD-METHOD.template.md:116` | the authored source | replaced, S2 |
| `memory/map/features/build-method.md:87-91` | a paraphrase in the dossier's Gaps section | rewritten, S5 |
| `memory/map/features/review-harnesses.md:84-86` | the ban as a premise about the harness | `TOOL-dTieredTribunal-11` owns it, backstop S6 |
| `memory/backlog/TOOL.md:204` | one clause inside the `TOOL-dHonouredPark-5` row | clause corrected, S7 |
| `memory/DECISIONS.md:107` | the owner ruling quoting the rule it amends | append-only, never edited |
| `memory/builds/dTieredTribunal/README.md:13` | the build's problem statement | M3 reserves the slot |
| `memory/builds/` records | the research record and four review records | dated observations |

Nothing outside `memory/` and `tools/memory-tree/` carries the rule.
`memory/gotchas/fold-text-is-unreviewed-surface.md:70-71` comes closest and does not: it says a spec
audit gets its fold instruction from the driver rather than from a rule, which stays true.

### Migration

None. Both files are read by humans and agents, and neither is parsed by a program that keys on this
text. `tools/memory-tree/check-method-carriers.sh` greps for the DOC NAME and excludes everything
under `memory/` plus the template itself, so no registry row is owed for any carrier above.

### Rollout

Order matters within the commit in one respect only: the template and the live guide must move
together or `kit/dogfood doc parity` reds. Edit the template first, then the live render, then run
the parity check before anything else.

### Files touched (estimate)

`memory/guides/BUILD-METHOD.md`, `tools/memory-tree/BUILD-METHOD.template.md`,
`memory/map/features/build-method.md`, `memory/backlog/TOOL.md`, and conditionally
`memory/map/features/review-harnesses.md` under S6.

### Alternatives rejected

- **Delete the paragraph.** Rejected. That is the 2026-08-20 state, which left M4 telling a reader to
  run a `Workflow` script with no rule about which one, and an adversarial round had to find it.
- **Keep the sentence and append an exception for a declared kind.** Rejected on bytes and on the
  fold rule. `memory/gotchas/fold-text-is-unreviewed-surface.md` names appending a negation beside
  the text it contradicts as its own defect class: two sentences that disagree are worse than one
  wrong sentence, because a reader cannot tell which is live.
- **Name the argument in the rule.** Rejected under S8. The field belongs to
  `TOOL-dTieredTribunal-11` and a rule spelling it becomes a second carrier of that interface.
- **Restore the 2026-08-11 wording verbatim.** Rejected. Its mechanism clause was that the harness
  cannot be pointed at a document, which `TOOL-dTieredTribunal-11` makes false in the same breath.
  The clause has to be re-pointed at the CALL, not restored at the TOOL.
- **Fund the bytes by trimming M4's lens sentence.** Rejected. It would delete the four lens names M4
  is the right place to carry, and the owner's grant does not reach that paragraph.

## 5. Production-readiness checklist

- security — N/A. Two prose documents, a dossier and a backlog row. No input, no write path, no
  outbound request.
- perf / scale — N/A. No executable change.
- a11y — N/A. Agent-facing and human-facing markdown with no interface.
- i18n — N/A. Same reason.
- error / empty / loading states — N/A. There is no runtime.
- observability — the rule becomes checkable, which is the point of the unit. A reader can now answer
  whether a spec audit was legitimate by reading the call, where before the rule offered only a
  category claim.
- risks — one, and it is the byte budget. This edit spends 161 of the 180 bytes the template has, so
  a later M4 change needing more will have to trim first or go to the owner. A second risk is
  ordering: if `TOOL-dTieredTribunal-11` does not land, this unit ships a rule describing a
  capability that does not exist, which is why the build order puts it last and why AC7 reads the
  harness rather than trusting the sequence.
- testing + left-shift gates — the observations are greps and byte counts over the edited files, plus
  the existing parity leg. No new gate: the class here is a prose rule losing its mechanism, and
  nothing static separates a mechanism clause from a category assertion. That is the same ground on
  which `TOOL-dTieredTribunal-9` ruled a gotcha record rather than a scanner for the fold class.
- migration / rollback — revert the commit. Nothing reads the text programmatically.
- user docs — none owed. `memory/guides/BUILD-METHOD.md` IS the document, and its dossier is
  refreshed under S5.

## 6. Acceptance criteria

- **AC1** — When `grep -n "a spec is not code" memory/guides/BUILD-METHOD.md` runs, it returns no
  match, and `grep -n "DECLARED subject" memory/guides/BUILD-METHOD.md` returns exactly one line
  inside M4.
- **AC2** — When the same two greps run over `tools/memory-tree/BUILD-METHOD.template.md`, they
  return the same results, and `sed -n '116,118p'` over each of the two files yields identical bytes.
- **AC3** — When `bash tools/memory-tree/kit-dogfood-parity.test.sh` runs, it exits zero.
- **AC4** — When `git diff -U0 cd971285 -- memory/guides/BUILD-METHOD.md` runs, it shows exactly one
  hunk and that hunk is the rule paragraph. This is the tripwire for a whole-file rewrite. It proves
  no other line moved; it does not by itself prove `--render` was never run.
- **AC5** — When `wc -c memory/guides/BUILD-METHOD.md tools/memory-tree/BUILD-METHOD.template.md`
  runs, both figures are at or under 24576, and `wc -l` on the same pair is at or under 350 for both.
- **AC6** — When `git grep -n "Not the harness" -- ':!memory/builds' ':!memory/DECISIONS.md'` runs,
  it returns no match. The two exclusions are named because a build record is a dated observation and
  `memory/DECISIONS.md` is append-only and quotes the rule its own ruling amended.
- **AC7** — When `tools/workflows/tier2-review.js` is read at the commit that lands this unit, its
  `args` header documents a review-kind argument, and the sentence M4 now points at is answerable
  from that header. If it is not, this unit does not land, because the rule would describe a
  capability the tree does not have.
- **AC8** — When `grep -n "pointed at a document" memory/map/features/build-method.md` runs, it
  returns no match, and the rewritten bullet names `TOOL-dTieredTribunal-12` as the unit that amended
  the rule.
- **AC9** — When `grep -n "rules that harness out for spec audits" memory/backlog/TOOL.md` runs, it
  returns no match, and `grep -n "TOOL-dHonouredPark-5" memory/backlog/TOOL.md` still shows the row
  with an `OPEN` token and its ask about orchestrator-assigned ids intact.
- **AC10** — When `grep -n "forbids" memory/map/features/review-harnesses.md` runs, no hit asserts
  that the build method forbids `tier2-review.js` on a spec audit. S6 makes this unit the backstop
  for that sentence, so the criterion is answered whether `TOOL-dTieredTribunal-11` fixed it or this
  unit did.
- **AC11** — When `bash tools/memory-tree/check-method-carriers.sh` and
  `python3 tools/codebase-map/test_codebase_map.py` run, both exit zero over the edited tree.

## 7. Gates

The named legs this unit must keep green are `kit/dogfood doc parity`,
`method carriers (every pointer declared)`, `memory hygiene`,
`codebase-map coverage + freshness`, `dead-path carriers (deleted files still named)`,
`drift-audit records` and `kit version markers`.

`kit/dogfood doc parity` is the only one this diff ARMS by its guard: `tools/gate-legs.json` gives it
a guard naming `memory/guides/BUILD-METHOD.md` and `tools/memory-tree/`, and S1 and S2 touch both
sides of that pair. The other six carry no guard and run on every bar whatever the diff, so naming
them is a statement about what must stay green rather than about what this change provokes. No count
of legs is written here: `tools/gate-legs.json` owns the population and a number beside a manifest is
wrong on the next commit.

This unit adds no gate leg, per §3. The rule it amends is prose, and the only mechanical property a
scanner could assert about it — that the paragraph exists — is already covered by the parity leg
comparing the two files byte for byte.

One thing is knowingly NOT gated, and it is said plainly rather than implied. Nothing checks that the
rule's mechanism clause stays true of the harness. If a later unit removes the review-kind argument
from `tools/workflows/tier2-review.js`, M4 goes stale again and every leg above stays green. That is
the same multi-carrier class this build's research names as `TOOL-dUnstalledConvoy-16`, its fix is a
parity pair rather than spec text, and this spec does not close it.

## 8. Open questions

none.

Two questions live near this unit and neither is a fork of its design, so both are named here with
where they actually sit rather than left to look resolved.

The lens-catalogue carrier count after `TOOL-dTieredTribunal-11` is proposal P3 in this build's
research record and is PARKED at build level, with the reason in this build's run-state file. §3
records why this unit does not pre-empt it.

Whether a gate should ever enforce M1's byte and line budget is called a separate question nobody has
ruled, in M1's own text at `memory/guides/BUILD-METHOD.md:16-18`. This unit spends the budget and does
not answer that.

## 9. Revision log

- rev-1 · 2026-08-26 · initial draft. Citations re-derived against `96f11c0e`; the header base is the
  default-branch sha the build is pinned to. The replacement wording was measured before it was
  written down, so §4's byte table is an observation and not an estimate.
- rev-2 · 2026-08-26 · spec-audit round 1 fold. Closes 19 and 32: S3's ground is now finding F3 of
  the aBoundedVerdict round-3 record rather than a build rule no carrier holds, and AC3's
  unobservable second sentence is deleted along with AC4's cross-reference to it. Closes 8: the
  replacement block's label reads 275 bytes, re-measured with `wc -c` over the extracted lines,
  which is the figure §4's +161 delta already used.

## 10. Reuse audit

The seam is `PAIRS` at `tools/memory-tree/kit-dogfood-parity.test.sh:53`, and this unit wires through
it without extending it. The `build-method` dossier names that seam itself, in the Reuse affordance
section of `memory/map/features/build-method.md`: reuse for shipping any kit-authored document into
an adopter's tree under drift and placeholder gating, extended by one row. The row this unit needs —
the live guide against the shipped template — is already the third entry in `PAIRS`, so there is
nothing to add and the whole reuse decision is to edit both sides and let the existing leg grade
them.

`python tools/codebase-map/reuse_lookup.py "a rule in the build method that names which review
harness may be pointed at a spec"` returned no symbol that implements a rule edit, which is the
expected answer for a documentation unit and is recorded as an answer rather than a failure. What it
did return is the two inventory keys `BUILD-METHOD.md` and `REVIEW-PROTOCOL.md` under `guides`, plus
the `agent-cap` dossier's shared-seam prose. The `guides` hit is the join that led to
`memory/map/features/build-method.md` and from there to the `PAIRS` affordance above.

Recall terms used with `python tools/memory-recall/query.py`: `M4 build method spec audit
tier2-review harness rule carrier template render parity dossier amendment`, against the question of
why the build method forbids the harness on a spec audit and what amending that rule costs. Forty
hits. Four decided something here. `TOOL-dTieredTribunal-7` is the grant. The `build-method` dossier
bullet and the `TOOL-dHonouredPark-5` backlog row are two of the carriers §4's inventory now lists,
and the four greps alone had not surfaced the backlog one. The aBoundedVerdict round-3 record is the
F3 finding behind S3, where following the parity leg's own printed remedy would have undone the fix
it was reporting.
