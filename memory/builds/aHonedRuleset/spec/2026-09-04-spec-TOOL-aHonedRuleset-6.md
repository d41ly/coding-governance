# TOOL-aHonedRuleset-6 — BUILD-METHOD's self-declared budget becomes enforceable or goes away

**Status:** SPECCED · rev-4 · 2026-09-04 · node a · Tier-2 · base 102e98f0 · streams tooling · order 1 · ratified 2026-09-04

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-09-04-build-TOOL-aHonedRuleset-1-prose-census.md](../build/2026-09-04-build-TOOL-aHonedRuleset-1-prose-census.md) | research | TOOL-aHonedRuleset-1 TOOL-aHonedRuleset-2 TOOL-aHonedRuleset-3 TOOL-aHonedRuleset-4 TOOL-aHonedRuleset-5 |
| [2026-09-04-build-TOOL-aHonedRuleset-1-prose-census.py](../build/2026-09-04-build-TOOL-aHonedRuleset-1-prose-census.py) | research | TOOL-aHonedRuleset-1 TOOL-aHonedRuleset-2 TOOL-aHonedRuleset-3 TOOL-aHonedRuleset-4 TOOL-aHonedRuleset-5 |
| [2026-09-04-review-TOOL-aHonedRuleset-2-spec-audit.md](../reviews/2026-09-04-review-TOOL-aHonedRuleset-2-spec-audit.md) | spec-audit | TOOL-aHonedRuleset-2 TOOL-aHonedRuleset-3 TOOL-aHonedRuleset-4 TOOL-aHonedRuleset-5 |

<!-- /gen:spec-records -->

## 1. Goal

`tools/memory-tree/BUILD-METHOD.template.md` declares a byte and line budget for itself in its own
opening prose, says at line 16 that no gate enforces the pair, and sits 12 bytes under the byte half.
The owner ruled on 2026-09-04 that the claim goes away rather than becoming enforceable: delete the
budget passage, re-render the guide, and add nothing. The file stops claiming a ceiling it does not
have.

## 2. Scope (IN)

Three items, all selected by the §8 F1 ruling and none of them conditional on anything.

- **S1** — delete lines 8 through 18 of `tools/memory-tree/BUILD-METHOD.template.md`, the whole
  budget passage: the `**Budget: ≤24 KB, ≤350 lines**` declaration and its reason, the three raises
  and the argument for each, the `**The BYTE half binds first**` sentence, and the
  `No gate enforces the pair` admission. Nothing is relocated and no replacement pointer is written.
- **S2** — re-render `memory/guides/BUILD-METHOD.md` from the edited template in the same commit,
  via the kit's own render path rather than by hand-editing the copy.
- **S3** — `memory/guides/SESSION-KICKOFF.md` gets its `last-audit` re-stamp bundled into the same
  commit, §B re-verified first. S2 stages `memory/guides/BUILD-METHOD.md`, which is the tenth
  `watch:` entry on line 6 of that manifest, so the obligation fires on this commit.

## 3. Non-goals (OUT)

- **Giving the template a ceiling anywhere else.** After S1 it has none, and that is the accepted
  consequence of the ruling rather than an oversight — see §4, "What the deletion leaves". Widening
  the uncapped-document set to cover it belongs to `TOOL-aScouredKit-23`, which owns that question
  and today names `WIRE-INTO-PROJECT.md` and `.claude/skills/unattended/SKILL.md`.
- **A size discipline on rendered kit docs, owned by the kit that renders them.** That is
  `TOOL-dSpentCeiling-4`, whose candidates are a per-template ceiling in `kit.toml` beside the
  `[[render]]` row or a rendered-versus-authored drift signal. This unit adds no gate and leaves that
  row entirely open.
- **Generalising the high-water ratchet to the `.memory-tree.conf` class caps.** That is
  `TOOL-dFoldedVerdict-7`. This unit adds no ratchet at all, and touches neither `GUIDE_CAP_BYTES`,
  `DOSSIER_CAP_BYTES` nor `INDEX_CAP_BYTES`.
- **Any other cut on the aHonedRuleset ranked list.** Rows 1 through 5 of that list are other units.
- **The census script.** `memory/builds/aHonedRuleset/build/2026-09-04-build-TOOL-aHonedRuleset-1-prose-census.py`
  belongs to `TOOL-aHonedRuleset-1`. It needs no edit, verified in §4, and its one stale docstring
  phrase predates this unit.

## 4. Design

### Inventory

Every figure measured on this worktree at base `102e98f0`. The post-cut column is the base figure
minus the 1101 bytes and 11 lines S1 removes; the passage carries no `{{KIT_DIR}}` or `{{TOOL_ROOT}}`
token, verified by running the token grep over lines 8 through 18 and getting nothing, so the
substitution delta is unchanged by the cut and the render loses exactly the same 1101 bytes.

| fact | at base | after S1 and S2 | how it was measured |
|---|---|---|---|
| template bytes | 24564 | 23463 | `wc -c tools/memory-tree/BUILD-METHOD.template.md` |
| template lines | 317 | 306 | `wc -l` on the same file |
| rendered bytes | 24553 | 23452 | `wc -c memory/guides/BUILD-METHOD.md` |
| rendered lines | 317 | 306 | `wc -l` on the same file |
| declared byte budget | 24576 | none | the file's own line 8, `≤24 KB`, deleted by S1 |
| declared line budget | 350 | none | the file's own line 8, deleted by S1 |
| free against the byte budget | 12 B | not applicable | 24576 minus 24564 |
| ceiling on the render | 61440 B / 750 lines | unchanged | `GUIDE_CAP_BYTES` / `GUIDE_CAP_LINES`, `tools/memory-tree/check-memory-hygiene.sh:63` |
| ceiling on the template | none | none | no row in `tools/template-size-limits.txt`, no leg in `tools/gate-legs.json`, and it sits outside `MEMORY_ROOT` so hygiene check 6 never sees it |
| budget passage weight | 1101 B | removed | `sed -n '8,18p' … \| wc -c` |
| raise history within it | 825 B | removed | `sed -n '10,18p' … \| wc -c` |

The census reported 12 bytes free from its own script. This unit re-measured and got the same
number, so the census stands unamended on this carrier.

Two figures are worth stating together. The passage that declares a ceiling with 12 bytes of room
costs 1101 of the 24564 bytes it constrains, which is 4.5% of the file.

### The state today, precisely

Line 8 declares `**Budget: ≤24 KB, ≤350 lines**` and gives the reason: M7 re-reads this file whole at
every pass boundary, so a method too expensive to re-read is skipped exactly when it is needed. Lines
10 through 14 carry three raises and the argument for each. Line 15 says the byte half binds first,
line 16 says `No gate enforces the pair`, and line 18 says whether one is ever added is a separate
question nobody has ruled. The owner ruled it on 2026-09-04, and the ruling is that the passage goes.

### What the deletion leaves

Three consequences follow from the ruling, and all three were accepted when it was made. They are
recorded because a consequence nobody wrote down is a consequence the next session rediscovers.

**The template ends up with no declared ceiling anywhere.** Not a looser one — none. It has no row in
`tools/template-size-limits.txt`, no size leg in `tools/gate-legs.json`, and it sits outside
`MEMORY_ROOT`, so hygiene check 6 never sees it. Today the prose budget is the only thing making a
claim about its size, and after S1 nothing does. That makes `tools/memory-tree/BUILD-METHOD.template.md`
a third member of the population `TOOL-aScouredKit-23` describes, beside `WIRE-INTO-PROJECT.md` and
`.claude/skills/unattended/SKILL.md`. This unit ADDS a file to that backlog row rather than removing
one, which is the opposite direction from the one the row is travelling in, and it is deliberate.

**The rendered guide keeps a cap far looser than the one being deleted.** `GUIDE_CAP_BYTES` is 61440,
which is 2.5x the rendered file's current 24553 B and 2.6x its post-cut 23452 B, leaving 37988 B of
slack. "The guide cap governs" is therefore true and, for a long time, inert. Two further facts bear
on how much that cap is really worth here. The render's byte count is not purely prose: the template
carries four `{{KIT_DIR}}` and five `{{TOOL_ROOT}}` tokens, and
`tools/memory-tree/kit-dogfood-parity.test.sh` substitutes both from where the kit sits, so an
adopter's directory depth moves the measured size — the model `24564 + 4 × (17 − 11) + 5 × (6 − 13)`
predicts exactly the measured 24553 here, and gives 24499 at a root install. And the cap reaches only
the rendered copy under `memory/guides/`, never the template the author actually edits, so the one
file a size failure could name is the one file the cap cannot see.

**The reason survives the sentence.** M7 really does re-read this file whole at every pass boundary,
so a method too expensive to re-read really is skipped exactly when it is needed. Deleting the
paragraph deletes the expression of that reason, not the reason. After this unit lands, the
constraint exists in the mechanism and in nothing that states it. None of the three consequences is
an argument that the ruling was wrong — the owner weighed them and chose deletion; they are written
here so the choice is legible later.

### The census script needs no change

Verified by reading. `load_prose_budgets` extracts the number with a regex against the live file
rather than holding a constant, and its own comment says a budget edited away "stops being reported
instead of silently persisting as a stale constant", so the deletion degrades by design.
`ceiling_for` then falls through all three of its branches for this path — it is absent from
`load_declared_ceilings`, absent from the prose dict once the regex finds nothing, and not under
`memory/guides/`, so `GUIDE_CAP_BYTES` never catches it — and returns `(None, None)`, which is the
`# uncapped:` tally. The docstring's phrase "the two live instances" already disagrees with the
single-row dict at base; that is a pre-existing inaccuracy in another unit's file and is not fixed
here.

### Files touched (estimate)

| file | what changes |
|---|---|
| `tools/memory-tree/BUILD-METHOD.template.md` | lines 8 through 18 deleted, 1101 B recovered |
| `memory/guides/BUILD-METHOD.md` | re-rendered, 1101 B smaller |
| `memory/guides/SESSION-KICKOFF.md` | S3 — re-verify §B, re-stamp `last-audit` |

Nothing else. `tools/template-size-limits.txt`, `tools/gate-legs.json`,
`tools/template-size-highwater.txt` and `tools/govkit/subject-pins.tsv` are all untouched, which is
what F1(b) buys and what AC1 through AC3 assert rather than assume.

`memory/guides/BUILD-METHOD.md` is the tenth of the ten `watch:` entries on line 6 of
`memory/guides/SESSION-KICKOFF.md`, verified by reading that line whole rather than its first clause.
`.githooks/pre-commit` runs `manifest-check.sh --staged` unconditionally, so a commit staging it
without the re-stamp is refused at check 5. That is why S3 is in scope and not an afterthought.

### Alternatives rejected

- **Declaring the budget instead of deleting it.** This was §8 F1's option (a) and this spec's own
  recommendation; the owner ruled against it. Its full argument stays in §8 rather than being
  duplicated here.
- **Leaving the passage alone.** §8 F1's option (c). No argument was offered for it because none was
  found.
- **Keeping the line half as an explicitly unenforced note.** Moot under the ruling: the line half is
  inside the deleted passage, so there is no separate decision and nothing to keep. See §8 F2.

## 5. Production-readiness checklist

- security — N/A, no write path, no untrusted input, no new surface.
- perf / scale — N/A, no leg is added and no existing leg changes its subject, so the bar's cost is
  unmoved.
- a11y — N/A, no user interface.
- i18n — N/A, no user-facing strings.
- error / empty / loading states — N/A, this unit adds no executable path with states to enter.
- observability — the only new signal is a negative one: the census stops reporting a ceiling for
  this carrier and moves it into the `# uncapped:` tally, which AC4 observes.
- risks — the one operational hazard is a template edit landing without the re-render, caught by
  `kit/dogfood doc parity`. Beyond that, three ACCEPTED consequences of the owner's ruling, argued in
  §4 and repeated here because §5 is where a reader looks for them. First,
  `tools/memory-tree/BUILD-METHOD.template.md` ends up with no declared ceiling anywhere, which adds
  a file to `TOOL-aScouredKit-23`'s population rather than removing one. Second, the rendered guide's
  `GUIDE_CAP_BYTES` of 61440 is about 2.5x the file's current size, so the surviving cap has 37988 B
  of slack and does not bind in any near term. Third, the budget's stated justification — that
  BUILD-METHOD M7 re-reads this file whole at every pass boundary — survives the deletion of the
  sentence carrying it, so the reason persists with nothing expressing it.
- testing + left-shift gates — nothing is left-shifted, because nothing is added. §7's staged-break
  rule has no subject here and that skip is named in §7 and witnessed by AC2, never omitted.
- migration / rollback — reverting is restoring eleven lines to the template and re-rendering;
  nothing is generated downstream that would go stale.
- user docs — N/A, no user-facing behaviour changes.

## 6. Acceptance criteria

Every criterion below is graded, none is branch-conditional, and four of them assert an ABSENCE
because the product of this ruling is that nothing measures this file.

- **AC1** — `grep -c 'BUILD-METHOD.template.md' tools/template-size-limits.txt` and the same grep
  over `tools/gate-legs.json` each return 0 on the landed tree, as they do at base. The absence is
  asserted rather than assumed, because the ruling's whole product is that nothing measures this file.
- **AC2** — No leg is added, so §7's staged-break rule has no subject and no RED is owed. The witness
  is the absence: `grep -c 'check-template-size.sh' tools/gate-legs.json` returns the same count as at
  base, 3. Recorded as a named skip in the build record, never omitted, because a skip that looks like
  a pass is indistinguishable from coverage.
- **AC3** — When `python tools/govkit/govkit.py selfcheck` runs it exits 0 and
  `git diff --stat -- tools/govkit/subject-pins.tsv` is empty: no leg was added, so no pin moves.
- **AC4** — When
  `python memory/builds/aHonedRuleset/build/2026-09-04-build-TOOL-aHonedRuleset-1-prose-census.py`
  runs, it prints the BUILD-METHOD template carrier with source `NONE`, a `-` ceiling and a `-` free
  column, and the file joins the `# uncapped:` tally. `load_prose_budgets`'s regex finds nothing once
  the passage is deleted, and `ceiling_for` then falls through all three branches. That is the
  degradation the function's own docstring calls designed, and the criterion observes it rather than
  trusting it.
- **AC5** — When `bash tools/memory-tree/kit-dogfood-parity.test.sh` runs after the template edit, it
  exits 0, proving `memory/guides/BUILD-METHOD.md` was re-rendered rather than hand-edited.
- **AC6** — When `bash tools/memory-tree/check-memory-hygiene.sh` runs, check 6 passes on the
  re-rendered `memory/guides/BUILD-METHOD.md`.
- **AC7** — When `wc -c tools/memory-tree/BUILD-METHOD.template.md` is run after the cut it reports
  23463, exactly 1101 below the base measurement of 24564, and `wc -l` reports 306 against a base of
  317. Both are exact rather than a floor, because one branch now exists and its recovery is the
  measured weight of the deleted passage.
- **AC8** — When `grep -n 'No gate enforces the pair' tools/memory-tree/BUILD-METHOD.template.md`
  runs it returns no hit, and `grep -n 'Budget:'` on the same file returns no hit either. Both halves
  of the claim are gone, not one.
- **AC9** — When `bash skills/session-kickoff/manifest-check.sh` runs after the commit, it exits 0,
  proving the S3 `last-audit` re-stamp landed in the same commit as `memory/guides/BUILD-METHOD.md`,
  the watched pathspec this unit stages.

## 7. Gates

**This unit adds no gate.** §7's staged-break rule — a new gate is not landed until its failing case
has been observed — therefore has no subject here. That is stated as a named skip rather than left
out, and AC2 is its witness: the leg count riding `tools/check-template-size.sh` stays at 3.

Legs that must stay green, all of them named from `tools/gate-legs.json` rather than from memory:

- `kit/dogfood doc parity` — catches a template edit landed without the render. AC5 observes it.
- `memory hygiene` — check 6 over the re-rendered guide, which the cut makes smaller and so cannot
  push toward `GUIDE_CAP_BYTES`. AC6 observes it.
- `govkit selfcheck` and `govkit acceptance matrix` — the generated subject pins, which must not move
  because no leg is added. AC3 observes that they do not.
- `line length` — the edited template and the rendered guide.
- `kickoff-manifest ratchet` — `bash skills/session-kickoff/manifest-check.sh`. Owed because S2
  stages a watched pathspec. S3 is the scope item that keeps it green; AC9 observes it.

The three legs reading `tools/template-size-limits.txt` — `template size <=48KiB`, `charter size` and
`kickoff engine size <=18KiB` — are NOT owed by this unit, because it no longer edits that file. They
were listed at rev-2 only because option (a) would have added a row to it.

## 8. Open questions

**F1 — what happens to the budget.** RESOLVED (owner, 2026-09-04): option (b), DELETE the budget
passage. This goes AGAINST this spec's recommendation of (a), which is left standing below and not
retro-edited. The unit is now the deletion of `tools/memory-tree/BUILD-METHOD.template.md` lines 8
through 18, the re-render of `memory/guides/BUILD-METHOD.md`, and the kickoff re-stamp that staging
the watched guide obliges — no row, no leg, no high-water seed, no regenerated pin, and no relocated
history. Three consequences were accepted with the ruling and are recorded in §4 and §5: the template
ends up with no declared ceiling anywhere, which adds it to `TOOL-aScouredKit-23`'s population rather
than removing a member; the rendered guide's surviving `GUIDE_CAP_BYTES` of 61440 is about 2.5x the
file's current size, so it does not bind in any near term; and the budget's stated justification,
that M7 re-reads this file whole at every pass boundary, survives the deletion of the sentence
carrying it, so the reason persists with nothing expressing it.

- **(a) Declare it.** A row in `tools/template-size-limits.txt` at 24576, a leg, a seeded high-water
  row, a regenerated subject pin, and the raise history relocated into the row's comment. The row
  goes on `tools/memory-tree/BUILD-METHOD.template.md`, not on the rendered guide, because the render
  is already capped by hygiene check 6, its byte count moves with the install prefix, parity makes
  the template bound the render rather than the reverse, and a failure must name the file the author
  may edit. Recovers about 950 B in a file with 12 B free. Costs about 1.28 s a bar, measured from the
  three sibling size legs in `.git/gate-ledger.tsv` at 1.286 s, 1.277 s and 1.282 s. Leaves the
  adopter-side gap open for `TOOL-dSpentCeiling-4`, because `tools/check-template-size.sh` and
  `tools/template-size-limits.txt` are gov-internal and appear in no `kit.toml`, so an adopter would
  still receive a guide with a budget nothing enforces.
- **(b) Delete it.** Drop the passage and let `GUIDE_CAP_BYTES` govern the rendered copy. Recovers
  1101 B, which is 151 B more than (a). Closes the adopter question by removing the claim. Against
  it: 61440 is 2.5x the current size, so 36887 B of slack means "the guide cap governs" is
  functionally "no ceiling for a long time"; the template itself stays capped by nothing at all; and
  the stated reason for the budget, that M7 re-reads this file whole at every pass boundary, is a
  real reason that survives the deletion of the sentence carrying it.
- **(c) Leave it.** The status quo. A constraint that binds whoever remembers to read the paragraph,
  on a file with 12 bytes free, whose own line 16 admits nothing enforces it. No argument is offered
  for this option because none was found.

*Recommendation: (a).* The seam exists, the codebase map already declares its extension recipe, the
cost is measured and small, the history is preserved rather than deleted, and it recovers all but
151 B of what (b) recovers while keeping the constraint. (b)'s single genuine advantage is the
adopter half, and that advantage is `TOOL-dSpentCeiling-4`'s to bank properly rather than this
unit's to buy by deletion.

**F2 — the line half.** RESOLVED (owner, 2026-09-04): MOOT under F1(b). The line half is declared
inside the passage F1 deletes, on the same line 8 as the byte half, so there is no separate decision
to take and no separate edit to make. This is recorded as moot rather than as "drop the line half",
because the two are different records: nothing here judged the line budget on its merits. The
analysis below is kept for what it weighed, and its measured premise is restored here: `tools/check-template-size.sh` measures bytes only and has no line arm, and `tools/check-line-length.sh` measures line LENGTH in characters rather than line COUNT, so `≤350 lines` could not have been enforced by any existing seam. Check 6 does bound the rendered guide's line count, at `GUIDE_CAP_LINES` 750, more than twice the declared 350. (That paragraph was dropped when the mark was inserted; restored at rev-4, because a mark asserting the analysis was kept must not be the thing that removed it.)

- **Drop the line half.** The file already argues against it: at its own stated ~100 B prose line the
  bytes run out near line 316, so most of the 350 is headroom the bytes do not grant. Measured, the
  file is at 317 lines and 12 bytes free, which confirms the byte half binds first.
- **Keep it as an explicitly unenforced note.** Honest, but it re-creates in one line the state this
  unit exists to end.

*Recommendation: drop it.* A pair where one half is gated and the other is prose is the same defect
at half the size, and the file's own measurement says the line half never binds.

## 9. Revision log

- rev-1 · 2026-09-04 · initial draft. Design pass only, no target file edited.
- rev-2 · 2026-09-04 · folded the three spec-audit findings addressed to this unit, from
  `2026-09-04-review-TOOL-aHonedRuleset-2-spec-audit.md`. **B3** — AC1 through AC4 presumed option
  (a) while §8 F1 stays unsigned; each is now split into an (a) half and a (b) half, the shape AC8
  already had. F1 is NOT resolved by this rev. **S1** — the unit stages `tools/gate-legs.json` and
  `memory/guides/BUILD-METHOD.md`, both watched on line 6 of `memory/guides/SESSION-KICKOFF.md`, with
  no re-stamp in scope; added S8 (branch-independent), its files-touched row, the
  `kickoff-manifest ratchet` leg in §7, and AC9. **A3** — AC2's 13-byte append could not go red on the
  landed tree, because S5 takes roughly 950 B out of the same file it appends to; the append is now
  sized from the post-S5 measurement as `24576 − M + 1`. Re-measured against source: the template at
  24564 B and 317 lines, its budget on line 8 and `No gate enforces the pair` on line 16, the ten
  `watch:` entries on `SESSION-KICKOFF.md:6`, `.githooks/pre-commit:54` running the staged arm
  unconditionally, and the two greps AC1(b) asserts both returning 0. AC7 was rescoped in the same
  pass: it named S5, which does not exist under option (b), and now names the cut under either
  branch with a floor below both recoveries. Every §8 fork stays UNRESOLVED and unsigned.
- rev-3 · 2026-09-04 · applied the owner's rulings of 2026-09-04 and swept the spec to agree with
  them. **F1** — RESOLVED as option (b), delete the passage, AGAINST this spec's recommendation of
  (a); (a)'s and (c)'s options and the recommendation paragraph are kept verbatim. **F2** — RESOLVED
  as MOOT under F1(b), since the line half sits inside the deleted passage; its two options are kept.
  **Order** — `order 3` became `order 1` at the owner's re-ordering, because `TOOL-aHonedRuleset-3`
  must repoint two pointers in the same file and this deletion frees the space; `ratified 2026-09-04`
  added to the header tail. Downstream sweep forced by F1(b): §1 now states the decided direction
  rather than asking for one; §2 dropped S1 through S6 (the limits-file row, the new leg, the seeded
  high-water row, the regenerated subject pin, the passage-to-pointer rewrite and its re-render) and
  renumbered the survivors S1 through S3, the old S7 and S8 becoming the deletion, the render and the
  kickoff re-stamp; §3's first non-goal was inverted, since the template now JOINS the uncapped
  population instead of being excluded from it, and the option-(a) references were removed from the
  `TOOL-dSpentCeiling-4` and `TOOL-dFoldedVerdict-7` rows; §4 lost "Which file the row belongs on",
  "What option (a) costs, corrected", "What happens to the prose", "The ceiling value after the cut"
  and "What option (a) does not reach", gained "What the deletion leaves" carrying the three accepted
  consequences and the surviving install-prefix measurement, gained a post-cut column on the
  inventory table, and had its files-touched table cut to three rows and its alternatives rewritten;
  §5 lost the added-leg perf line and the gate-exit-code states, gained the three accepted
  consequences under risks, and now records that nothing is left-shifted; §6 kept only the (b) halves
  and renumbered AC1 through AC4 cleanly, with AC7 restated as the exact 23463 B / 306 lines and AC8
  reduced to its two absence greps; §7 now opens with the no-new-gate skip and drops the three
  `tools/template-size-limits.txt` readers, which this unit no longer edits. Measured for this rev:
  template 24564 B / 317 lines, passage `sed -n '8,18p' … | wc -c` 1101 B over 11 lines and carrying
  no `{{KIT_DIR}}` or `{{TOOL_ROOT}}` token, so post-cut 23463 B / 306 lines and the render
  23452 B / 306 lines; `GUIDE_CAP_BYTES=61440` at `check-memory-hygiene.sh:63`;
  `grep -c 'check-template-size.sh' tools/gate-legs.json` = 3 and both AC1 greps = 0;
  `memory/guides/BUILD-METHOD.md` present as the tenth `watch:` entry on `SESSION-KICKOFF.md:6`.

- rev-4 · 2026-09-04 · restored the measured premise under F2's MOOT mark. Inserting the mark
  had deleted the three sentences establishing that no seam could enforce `≤350 lines`, while the
  mark itself claimed the analysis was kept — found by the ratification verify pass.

## 10. Reuse audit

`python tools/codebase-map/reuse_lookup.py "declare a byte ceiling for a document and enforce it with
a size gate"` ranked `check-template-size.sh [playbook]` as an affordance seam and returned the
inventory keys `template size <=48KiB`, `charter size` and `kickoff engine size <=18KiB` from
`gate-legs`. That seam is named verbatim in `memory/map/features/playbook.md` under "Reuse
affordance": "check-template-size.sh subject resolution — reuse for gating ANY file's byte size on
the merge bar without writing a sibling script; extend via one `tools/gate-legs.json` entry naming
the subject alone, one row in `tools/template-size-limits.txt` giving its ceiling and the reason for
it, and one `--bump` to seed its high-water row." The probe therefore found a fitting seam and the
extension recipe for it. **The owner's F1(b) ruling took the branch that extends nothing**, so this
unit writes no new script AND uses no existing one; the finding is recorded as what was available
rather than as what was taken. The recipe's own drift is recorded while it is in front of us: the
dossier names three carriers and the tree now needs four, because `tools/govkit/subject-pins.tsv` is
a generated per-leg pin that did not exist when the affordance was written, verified by finding
`charter size`, `kickoff engine size <=18KiB` and `template size <=48KiB` at its lines 21, 43 and 94.

Recall terms used: `python tools/memory-recall/query.py "why does a document declare its own byte
ceiling in prose instead of taking a row in the declared size registry" --terms "template-size-limits
high-water ratchet declared ceiling GUIDE_CAP_BYTES rendered template parity gate-legs leg subject
BUILD-METHOD budget uncapped"` — 40 hits, of which `TOOL-aScouredKit-23`, `TOOL-dSpentCeiling-4`,
`TOOL-dFoldedVerdict-7`, `TOOL-aDeclaredCeiling-1` and `memory/map/features/playbook.md:105` are the
records that bind this change.
