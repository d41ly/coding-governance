**Serves:** spec-audit TOOL-aHonedRuleset-8

# aHonedRuleset — spec audit of unit 8, round 3

*Node `a`, 2026-09-06. Four finder lenses read the rev-7 text of the unit-8 spec, five skeptic
batches were run to REFUTE each candidate, and this is the consolidation. Round 1 graded rev-5 and
returned BLOCKED with two blockers; round 2 graded rev-6 and returned BLOCKED with one. The §9 rev-7
log line was read first as the map of what moved, and every surviving claim about source was re-run
against the tree before it was kept — `WIRE-INTO-PROJECT.md`, `govkit.py`, `refusal_join.py`,
`check_runbook_parity.py`, `check-microformats.kit.toml`, `gate-legs.json`, `selftest.py` and the
sibling `DEPL-aHoistedPass-1` spec were read at source, never through the spec's description of them.
Four claims were executed rather than read, including the AC17 command sequence against a fresh
scratch target. This round grades the SPEC, not the tree.*

Subject, pinned at the blob it was read at:

- `memory/builds/aHonedRuleset/spec/2026-09-04-spec-TOOL-aHonedRuleset-8.md@c17ea9635ab2037f82047704710452c6b1de4eac`

**ROUND: 3.**

## Verdict: BLOCKED

One blocker, and it is round 2's B1 surviving its own fold for the second time — one layer further
down again. rev-6 traced the right mechanism onto the wrong command; rev-7 corrected the command and
traced onto a command that does not run. Executed live from the gov root, AC17's run (1) —
`govkit.py intake --target <scratch> --kits playbook,playbook-render,check-microformats`, which the
criterion calls "exactly §2's line with this unit's id added" — exits 2 with `the selected kits need
answer(s) playbook_path and none was supplied. Refusing to invent one` and writes no
`.governance/deploy.toml` at all. So §4's rewritten central claim and §3(a)'s identical sentence,
"the §2 outcome today is a `deploy.toml` naming the entry with no engine in the tree", are false in
the other direction: there is no descriptor either. Run (2) then refuses with `no target descriptor`,
and none of AC17's THREE admissible outcomes is reachable.

**The loop does not re-arm.** Blockers went 2 → 1 → 1. The build method re-arms a round only when the
confirmed-blocker count is STRICTLY smaller than the round before, and 1 is not smaller than 1. So
there is no round 4: B1 is DISPOSED at this exit, and its disposition is **FOLD** — it is a defect in
a document this review read, its fix is one `--answer` clause plus two restated sentences, and the
corrected sequence was executed end to end to prove the fix lands. No blocker here needs a mechanism
this build does not have, so nothing is promoted.

Three HIGH findings follow, then four MEDIUM and four LOW. The dominant class is unchanged from round
2 and is now in its third consecutive round: **an amendment that leaves its other half standing.**
Seven of the twelve entries below are rev-7 edits that never reached the carriers describing them —
H3 is the exact clause the rev-7 H5 fold existed to fix, still stating the absolute S6 now forbids, in
both sites S6's own paragraph is answering; M2 is the sixth and seventh counts of a seven-file set
that rev-7's H1 fold claimed to have swept; L1 is the superseded three-item enumeration left standing
as the last line of the criterion that supersedes it. H1 is new and worse than a leftover: two rev-7
folds were made independently and now grade each other, so a build implementing §2 exactly can red its
own acceptance criterion.

The unit is buildable the moment B1 and the HIGH set land. Nothing was re-opened, no fork ruling is
reversed, and no scope item is challenged on the merits.

---

## Review shape

- Raw findings: **31**. Confirmed: **22**. Refuted: **9**. Unverified: **0**. Precision: **0.71**
  (round 2: 0.67 over the same lens set and protocol; round 1: 0.56).
- The 22 confirmed findings consolidate into the **12 entries** below. The pipeline reported zero
  duplicates because none were byte-identical, but six clusters are one defect seen through several
  lenses — the `grep -n apply` count alone came back four times. Each entry names the raw ids it
  carries, so nothing is lost and nothing is counted twice.
- Adjudicated severity is MINE and is stated per entry; where it differs from a raw grade, the entry
  says why. Two raw grades moved: id 1 up to the blocker it duplicates, id 19 down to MEDIUM.

### Run integrity

- lenses 4/4 returned, 0 DIED; skeptic batches 5/5 returned, 0 DIED; 0 contradictory verdict(s)
  demoted to unverified, 0 spurious verdict(s) discarded, 0 duplicate(s).

Every integrity count is zero, so this run is **complete**: the finding set is not truncated by a dead
lens or a lost skeptic batch, and a zero count in it is evidence rather than silence. The one place
this report reports an absence as a finding — M3, S2's header rewrite having no criterion — was
verified by enumerating all eighteen criteria in §6 at the pinned blob, not inferred from a lens
returning nothing.

---

## Findings

| # | Sev | Address | Defect | Raw ids |
|---|---|---|---|---|
| B1 | BLOCKER | §6 AC17 run (1); §4 *What the runbook path actually yields*; §3 non-goal (a) | AC17's command REFUSES — `intake` needs `--answer playbook_path` and the criterion supplies none, so §2's line writes no descriptor at all | 1, 24 |
| H1 | HIGH | §6 AC9 second half, against §2 S3 *The path-free form this unit uses instead* | Two rev-7 folds grade each other: S3 sanctions a wiring spelling that carries no `check-microformats`, and AC9 requires 4 matching lines | 2, 10, 18 |
| H2 | HIGH | §3 non-goal (a), clause (a); against §4's narrower sentence and `memory/backlog/TOOL.md:6` | "No numbered section runs `apply` or `update` at all" is false for `update` — `## 5b` runs it at `:602` | 3, 11 |
| H3 | HIGH | §5 testing bullet (`:504`); §7 `govkit refusal join` bullet (`:657`); against §2 S6 | S6 forbids the absolute and both sites still write 246, so the ledger comment is false the day it lands | 9, 27 |
| M1 | MEDIUM | §3 non-goal (a); §4 *What the runbook path actually yields*; `memory/backlog/TOOL.md:6` | `grep -n apply WIRE-INTO-PROJECT.md` returns TEN hits, not the eight enumerated in three carriers | 4, 15, 19, 28 |
| M2 | MEDIUM | §5 first risks bullet (`:484`) and security bullet (`:461`), against §4 Rollout and Files touched | The sixth and seventh counts of the seven-file set: one still reads six, one enumerates six under a SEVEN | 5, 14, 29 |
| M3 | MEDIUM | §6 (no criterion for S2's second half) | S2 rewrites the descriptor header at lines 6-8 and no criterion observes it; every gate stays green on a self-contradicting descriptor | 6 |
| M4 | MEDIUM | §2 S6, *What makes the +2 true* | "Routed through a helper contributes ZERO" is a false mechanism claim, one clause from the double-count claim it contradicts | 13 |
| L1 | LOW | §6 AC9, final sentence (`:556`) | The superseded three-item enumeration is still the last line of the criterion that supersedes it | 7 |
| L2 | LOW | §10, first paragraph (`:1254`) | Quotes §4's pre-rev-7 half and attributes it to the wrong subsection | 8, 29 |
| L3 | LOW | §8 F4, *The real byte cost against what was budgeted* (`:1018`) | "The cheapest of the three options" is refuted by its own subordinate clause | 16 |
| L4 | LOW | §8 F1 (`:783`); §5 risks second bullet (`:496`) | Two line pins name the wrong statement — the quoted sentence is not inside the cited range | 31 |

---

## B1 — BLOCKER. The criterion added so the outcome would be OBSERVED names a command that refuses

**Address:** §6 AC17, run (1); §4 *What the runbook path actually yields*, first paragraph; §3's last
non-goal bullet, clause (a). Raw ids 1 and 24.

**Disposition: FOLD. Document defect — no mechanism this build lacks.**

rev-7 answered round 2's B1 by rewriting §4 around the correct fact that the runbook's fresh path runs
no `apply`, and by adding AC17 so the outcome would be observed rather than asserted. AC17 names the
sequence explicitly, "because rev-6 said *the runbook's own command* and the runbook's own §2 command
is `intake` alone". Run (1) is spelled:

```
govkit.py intake --target <scratch> --kits playbook,playbook-render,check-microformats
```

Executed live from the gov root against a fresh scratch target, that command exits **2**:

```
govkit: the selected kits need answer(s) playbook_path and none was supplied. Refusing to invent one:
an answer this tool guesses is one the operator never made and cannot audit. Supply them as
--answer key=value
```

and writes no `.governance/` directory at all. Resolved through the module rather than inferred:
`needed_answers(descs, resolve_selection(reg, descs, 'kits', ['playbook','playbook-render',
'check-microformats']))` returns `['playbook_path']`, and `cmd_intake` raises `Refusal` on the missing
answer at `tools/govkit/govkit.py:8139-8145`, several statements before it writes anything. Run (2),
`apply --target <scratch>`, then exits 2 with `no target descriptor at …/deploy.toml`, so neither of
the two `apply` lines AC17 asks the builder to observe can be printed and none of its three admissible
outcomes is reachable.

**The "exactly §2's line" defence fails.** `grep -c -- '--answer' WIRE-INTO-PROJECT.md` is **0**, so
the runbook's own copy-paste line at `:81` refuses identically, with or without this unit's id in the
list. That is not a mitigation of the finding; it is a second instance of it, and it is what makes the
downstream sentences wrong.

**What the false premise costs, in three carriers.** §4's rewritten central claim and §3(a)'s
identical sentence both read: the §2 outcome today is "a `deploy.toml` naming the entry with NO ENGINE
IN THE TREE". Measured, §2's three lines produce no `deploy.toml` either — the refusal comes first.
The same sentence is already exported outside the spec, in capitals, at `memory/backlog/TOOL.md:6`.
And AC17 — the criterion whose stated purpose is that "admitting only the outcomes an `apply` run can
produce made rev-6's criterion grade a command the builder had to invent" — makes the builder invent
`--answer playbook_path=…`. That is the defect AC17 was folded in to remove, reproduced by the fold.

**The fix is executable and was executed.** With the answer supplied, `intake` exits 0
(`wrote …/deploy.toml for 3 kit(s); 1 answer(s) recorded; prefix "tools" (default)`),
`tools/check-microformats.sh` is absent from the target — AC17's third outcome, observable at last —
and `apply --target <scratch>` then exits 0 printing
`govkit apply — gate legs: ORDERED, not emitted — this target's deploy.toml declares no
[gate_runner]`, which is AC17's second. All three outcomes become reachable from one two-run sequence.

Prior art already recorded the working form: `memory/builds/aScouredKit/reviews/2026-08-30-review-TOOL-aScouredKit-2-wave2-lens-convergence.md:406-407` spells `intake … --answer playbook_path=AGENTS.md`
plus three more answers.

**Fold, precisely:**

1. AC17 run (1) gains `--answer playbook_path=<file>` (add `--answer prefix=<pfx>` only if the scratch
   target is not to take the `tools` default). Or state that the answer set is whatever
   `needed_answers` returns for the selection and must be supplied — the general form is safer, since
   a future kit's new token would silently re-break the literal one.
2. §4 and §3(a) restate the measured outcome: §2's literal three lines REFUSE before writing anything,
   because the runbook documents no `--answer` at all; with answers supplied the descriptor lands and
   the payload is still absent until `apply`. Both halves matter and only the second is currently
   written.
3. §4's *What the runbook path actually yields* carries the same clause, where it currently says "§2's
   install is exactly three lines" without saying that those three lines do not run.
4. `memory/backlog/TOOL.md:6` is corrected in the same commit, per §3's own precedent for that row.
   Either add the missing-`--answer` documentation as defect (c) of `TOOL-aHonedRuleset-15` or state
   why it is excluded — it is a third measured defect in the same install path and the row's title
   says TWO.

**Left-shift gate.** The general arm, and it would have caught B1, H2, M1 and L1 in one pass: **a spec
lint that EXECUTES every command a §6 criterion quotes verbatim, at the spec's declared base, and reds
when the exit status or the stated output does not reproduce.** This is `TOOL-aHonedRuleset-12`'s
anti-vacuity candidate widened from "does the pattern match anything" to "does the command run at
all", and it is cheap: criteria already quote their commands in fenced or backticked form. It needs a
declared allowlist of verbs it may run — `grep`, `git diff`, and gov's own read-only verbs against a
scratch target — because a criterion may legitimately name a destructive command. File it against
`memory/TEMPLATE-SPEC.md` on the `TOOL-aHonedRuleset-12` row, which already owns the
acceptance-criteria-that-cannot-fail class.

---

## H1 — HIGH. Two rev-7 folds grade each other, and a build that follows §2 exactly reds its own criterion

**Address:** §6 AC9, second half; against §2 S3, *The path-free form this unit uses instead*. Raw ids
2, 10, 18.

AC9 requires `grep -c 'check-microformats' WIRE-INTO-PROJECT.md` to return **at least 4** against the
0 measured at base, and enumerates the four: "the `--kits` id, the anchor, the body sentence and the
WIRING instruction". The criterion is explicit that the enumeration IS the derivation of the
threshold: "the enumeration is written out rather than left as a bare integer so the next scope change
to S3 is visibly a change to this count."

S3's wiring step, rewritten at rev-7 by the H3 fold, sanctions two spellings with an explicit
**and/or**: "name the leg by the NAME `tools/gate-legs.json` gives it, `micro-format definitions`,
and/or by the `{prefix}`-token argv the descriptor itself declares at `check-microformats.kit.toml:44`."

Only one of the two carries the id. Verified at source: `tools/gate-legs.json:34` is
`"name": "micro-format definitions"` — no occurrence of `check-microformats` — while
`check-microformats.kit.toml:44` is `argv = ["bash", "{prefix}/check-microformats.sh",
"{playbook_path}"]`, which does. `grep -c` counts matching LINES, so a build that lands all three S3
edits and spells the wiring instruction with the leg name alone returns **3** and reds AC9.

That is not a hypothetical builder being careless: it is a builder following the scope item exactly,
taking the first of two options the spec presents as equivalent. The rev-7 H3 fold rewrote S3's wiring
form to be path-free (correctly — the literal `tools/` form would take
`tools/install-prefix-carried.txt` from 47 to 48 and red AC6), and the rev-7 H4 fold independently
raised AC9's threshold to 4 on the assumption that the wiring line still spells the id. Both folds are
individually right and jointly unsatisfiable unless the builder reads AC9 back into S3 and infers that
the argv form is mandatory. Nothing says so.

**Fix — either half closes it, and the spec should pick one rather than leave the reader to:**

- **(a)** Tighten S3: drop the "and/or", require the `{prefix}/check-microformats.sh` argv form, and
  keep the leg name as a permitted ADDITION rather than an alternative. §4's carried-prefix analysis
  already shows the `{prefix}` token trips neither install-prefix arm, so this costs nothing.
- **(b)** Re-base AC9's fourth observation on something both spellings satisfy: assert
  `grep -c 'check-microformats'` returns at least 3, AND add a separate grep over the DERIVED anchor
  body — the new anchor line through to `<!-- govkit:entry memory-tree -->` — for an instruction
  naming both the local gate runner and CI. That is the form round 2 recommended for AC11 and it does
  not depend on which spelling the builder chose.

Either way, state in AC9 which of S3's forms it is written against. A threshold derived from an
enumeration must name the same population the scope item permits.

**Left-shift gate.** Cheap and specific: **red any §2 scope item containing an "and/or" over two
spellings when a §6 criterion grades that scope item by a count of occurrences.** It is a two-grep
arm over the fixed `S<n>` and `AC<n>` markers, and the class it catches — a criterion whose threshold
rests on a property its own scope item leaves optional — is the exact shape charter §7 calls a gate
satisfied by its own prose. Same `TOOL-aHonedRuleset-12` row.

---

## H2 — HIGH. The scope boundary states a measured universal that does not reproduce, for `update`

**Address:** §3, the two-runbook-defects non-goal, clause (a); against §4's narrower sentence and
`memory/backlog/TOOL.md:6`. Raw ids 3, 11.

§3(a) reads: **"No numbered section of the runbook runs `apply` or `update` at all"** — offered
evidence, `grep -n apply WIRE-INTO-PROJECT.md`.

Verified in the tree, the `update` half is false. `## 5b — A tree that already carries kits: bootstrap
its receipt (adopt)` is a numbered section by exactly the convention `## 3b` and `## 3c` use — heading
at `WIRE-INTO-PROJECT.md:587`, running to `## 6` at `:780` — and `:602` is a runnable line inside the
fenced block at `:598-603`:

```
python <gov>/tools/govkit/govkit.py update --target <project>                # now the tree is live
```

The offered evidence does not even test the half that is wrong: it greps `apply`.

**§4 states the true, narrower claim** — "Only §5b at `:589` asserts `apply` IS the fresh path, and no
numbered section runs it" — which is correct as written. §3 widened a true sentence into a false one,
and the two sections now disagree. The identical false universal is carried verbatim into the
`TOOL-aHonedRuleset-15` row at `memory/backlog/TOOL.md:6`, in capitals, where a later unit will act on
it. No §6 criterion covers the gap either: AC17 runs `intake` and `apply` and never `update`, so the
`update` half is both wrong and unobserved.

**A second, smaller mis-route in the same paragraph.** §4 writes "Whenever they do reach `apply`, by
§5b's path or their own, they get the ordered-not-emitted branch". §5b's documented sequence is
intake → adopt → adopt --write → update, and it never reaches `apply`. Confirmed at source:
`cmd_update` at `govkit.py:5722` onward contains no `gate legs:` emission line at all, so §5b's path
produces NEITHER of AC17's two `apply` lines. This does not reach AC17 itself — AC17 names `apply`
explicitly in run (2) — but it does make §4's sentence route the reader through a path that yields
neither outcome it promises.

**Fix.** Narrow §3(a) to what §4 measured and what reproduces: no numbered section runs `apply`; §5b
at `:598-603` runs `adopt` and then `update`, which is the path that lands bytes; and §2 — the section
an operator following the charter install copies — runs neither. Add the §5b fact and `cmd_update`'s
lack of leg emission to §4's paragraph, and strike "by §5b's path or their own" from the
ordered-not-emitted sentence. Correct the backlog row in the same commit.

**Left-shift gate.** Covered by B1's execute-the-quoted-command arm for the `apply` half, but the
`update` half is a universal whose evidence tests only one of two verbs. The narrower documented check
that catches this class: **a claim of the form "no X does Y or Z" must cite one probe per disjunct.**
That is a review checklist entry, not a gate — an automated arm cannot know which greps were meant to
be exhaustive. It belongs in §10's recurring-bug-class list as *a universal quantified over two
verbs, evidenced by a probe for one of them*, which is a variant of the green-by-absence class the
charter already names.

---

## H3 — HIGH. S6 forbids the absolute, and the spec writes it twice in the two sections a builder reads first

**Address:** §5 *testing + left-shift gates* bullet (`:504`); §7 `govkit refusal join` bullet
(`:657`); against §2 S6, *The count is a DELTA, never the absolute*. Raw ids 9, 27.

S6 was rewritten at rev-7 to state the refusal-join growth as a **delta of +2**, with the absolute
derived at landing, and its own paragraph gives the reason in terms that reach spec prose and not only
the ledger comment:

> Two SPECCED units each writing 246 means whichever lands second lands with a false figure in its own
> spec and a ledger comment wrong on the day it is written. Stating the delta and deriving the
> absolute at landing is what makes both correct.

Both sites S6 is answering still write the absolute:

- `:504`, §5's testing bullet — "the population grows 244 to 246 and only the shrink-only pin keeps
  the leg green".
- `:657`, §7's refusal-join bullet — "**S4 and S5 take it to 246, which is GROWTH.**"

Verified live: `python tools/govkit/refusal_join.py` reports **244** branches across 4 modules and
exits 0, with `BRANCH_PIN = 217` unmoved at `refusal_join.py:41`. And
`memory/builds/aHoistedPass/spec/2026-09-04-spec-DEPL-aHoistedPass-1.md` AC9 at `:262-263` already
claims "exactly two higher than the 244 measured at this base" for ITS OWN two branches in the same
file. So both SPECCED units add +2 to one population, and the second to land sees 246 → 248.

This is the amendment-leaves-its-other-half-standing class on the exact clause the rev-7 H5 fold
existed to fix. It is worse than the count staleness in M2 because §7 is the section a builder reads
to learn which leg owns the arms, and it is the section they read immediately before writing the
ledger comment that S6 exists to keep true. AC18 grades a delta while §5 and §7 assert an absolute
that holds only if this unit lands first.

**Fix.** Delete both occurrences of the literal 246 and replace with the delta form, pointing at S6's
paragraph rather than restating its argument:

- §7 → "S4 and S5 add TWO branches; the absolute is derived at landing, because `DEPL-aHoistedPass-1`
  adds two of its own to the same file (S6)."
- §5's testing bullet → "the population grows by 2 and only the shrink-only pin keeps the leg green."

Keep 244 anywhere it is named as the base measurement — that figure is correct and is what the delta
is taken against.

**Left-shift gate.** Genuinely cheap and worth the row: **red a spec that writes a numeric absolute
for a population its own §2 declares as a delta.** The predicate is a grep for the literal figure
appearing in the same document as a scope item containing "DELTA, never the absolute", which is a
narrow and honest arm. The broader and more valuable version — red any spec asserting a post-landing
absolute for a file a concurrently-SPECCED sibling also mutates — needs the LIVE work-state index to
resolve siblings, which `memory/LIVE.md` already renders, so it is buildable; but it is a bigger arm
and this build has no budget for it. File the narrow one on `TOOL-aHonedRuleset-12`.

---

## M1 — MEDIUM. A named command's stated output does not reproduce, in four carriers

**Address:** §3 non-goal (a); §4 *What the runbook path actually yields*, first paragraph;
`memory/backlog/TOOL.md:6`. Raw ids 4, 15, 19, 28.

`grep -n apply WIRE-INTO-PROJECT.md` returns **TEN** lines at HEAD:

```
309 373 589 635 638 843 847 876 878 883
```

The spec enumerates eight in both §3 and §4, omitting `:843` ("run through `git apply --check`") and
`:847` ("Read one before applying it"), both inside `## 5c — Send a fix back` at `:817`. The identical
eight-item list is carried in the `TOOL-aHonedRuleset-15` backlog row. **And in round 2's own report**,
whose B1 evidence block is where the enumeration originates — so the false figure has four carriers,
one of which is a review record. Worth naming: a review report is not exempt from the citation
discipline it enforces.

Not a stale-base artefact. At base `94958534` the count is NINE with different line numbers, and the
eight cited numbers match HEAD's numbering exactly — so the list is an incomplete transcription of the
command's current output, not an accurate transcription of an older one.

**The conclusion survives and the entry says so.** Both omitted hits are prose about `git apply` on the
contribute path, so there is still no `govkit apply` command block anywhere in the document. Adjudicated
MEDIUM for that reason; raw id 19 graded it HIGH and I am downgrading it, because the ruling it
supports does not move. What does not survive is the figure, in a spec that spends whole paragraphs
correcting figures.

**Fix.** Write the true set — ten hits, `:309 :373 :589 :635 :638 :843 :847 :876 :878 :883` — with
`:843` and `:847` named as `git apply --check` prose on the contribute path rather than dropped. Or
replace the raw grep with the assertion that actually carries the argument: no fenced command block in
the document invokes `govkit.py apply`, citing the fenced blocks at `:81-85` and `:598-603`. The second
form is better, because it is the claim §3 needs and it cannot drift when someone writes the word
"apply" in a new paragraph. Correct the backlog row in the same edit.

**Left-shift gate.** B1's execute-the-quoted-command arm, verbatim: run the grep, compare the output.
This is the single cheapest arm in the report and it catches three entries.

---

## M2 — MEDIUM. The sixth and seventh counts of a seven-file set that rev-7 claimed to have swept

**Address:** §5's first risks bullet (`:484`) and security bullet (`:461`); against §4's *Rollout*
(`:405`) and *Files touched (estimate)* (`:409-419`). Raw ids 5, 14, 29.

§4's Rollout reads "SEVEN files, one atom — six at rev-6", the Files-touched table carries seven rows
(`:413-419`), and §5's own migration/rollback bullet at `:508` says "all seven files". Two counts in
§5 did not move with them:

- `:484`, §5's first risks bullet — "there is no smaller thing to revert — §4's Rollout establishes
  the **six** files cannot be split". It cites §4 by name for a number §4 no longer states, four lines
  above a bullet that contradicts it.
- `:461`, §5's security bullet — claims "§4's SEVEN files" and then enumerates six of them: "two
  declaration edits, one runbook edit, two `r.fail` arms plus their selftest arms, and S6's comment".
  The missing seventh is `tools/govkit/entries/check-line-length.kit.toml`, S4's second half, which is
  its own row at `:417`.

The rev-7 §9 log claims "the table gains its row and five counts move", and five did — `:149`, `:405`,
`:421`, `:461`, `:508`. These two are the sixth and seventh, and one of them is inside the very bullet
the fold did move: `:461`'s figure was corrected to SEVEN while its enumeration was left at six.

That is the class `TOOL-aHonedRuleset-12` was widened to cover, landing again: the file count is still
not derivable from the document, and the bullet that prices what the F1 override costs at review time
is the one carrying the stale figure.

**Fix.** `:484` → "the seven files cannot be split". `:461` → "three declaration edits, one runbook
edit, two `r.fail` arms plus their selftest arms, and S6's comment", so the list sums to the seven it
claims.

**Left-shift gate.** `TOOL-aHonedRuleset-12`'s candidate (2), verbatim and unmodified: every
filesystem path named in a §2 scope item appears as a row in §4's Files-touched table, AND every
spelled-out number in the document claiming to be that row count equals it. The number words are a
closed set. This entry is the second consecutive round in which that candidate would have paid for
itself, which by this repo's own standard is when a check stops being a preference.

---

## M3 — MEDIUM. S2's second half has no criterion, and the descriptor it ships argues against itself

**Address:** §6 — the absence of a criterion for §2 S2's header rewrite. Raw id 6.

S2 has three parts: delete `selectable = "conditional"` at
`tools/govkit/entries/check-microformats.kit.toml:14`; **rewrite the descriptor's header paragraph at
lines 6 to 8**, whose argument is the `--all` exclusion the scope item removes; and leave
`requires = ["playbook"]` at `:15` exactly as it is.

All eighteen criteria in §6 were enumerated at the pinned blob. None mentions the header, the
paragraph, or lines 6-8. AC9 greps `^selectable` for 0 — anchored, so it cannot reach line 6's
the comment line `# selectable = "conditional" and it matters`. AC2 counts `all_kits` at 21, AC3
counts unclaimed paths at 0. S4's `why_conditional` arm cannot reach it either: after S2 the entry has
left the conditional population, which is precisely the point of S2.

So a build that deletes line 14 and leaves lines 6-8 standing passes every criterion and every gate,
and ships a descriptor whose own header still argues for the mark it no longer carries — verified at
source, lines 6-8 read "`selectable = \"conditional\"` and it matters … an adopter who does not should
not have it forced on them by `--all`". That is this spec's own named class landing in the PRODUCT
rather than in the document, and it is the state §4's *Why the mark is wrong* section exists to end.

AC18 exists because "S6 was the only scope item with no criterion at all". By that same standard S2's
second half has none either — one level down, at the clause rather than the scope item.

**Fix.** Two one-line additions to a criterion that already greps that file. Extend AC9 with a
whole-file observation, `grep -c 'selectable = "conditional"' tools/govkit/entries/check-microformats.kit.toml`
returns 0 with the comment included; and a positive grep asserting the replacement header names the
default selection. The positive half matters as much as the zero — round 2's own M-set found an
absence-only criterion and named it green-by-absence.

**Left-shift gate.** `TOOL-aHonedRuleset-12`'s candidate (1) — every `S<n>` in §2 named by at least
one §6 criterion — is the right family but **it does NOT catch this one**, and saying so is the point:
S2 IS named, by AC9. The gap is a half of a scope item. State that limit in the arm's own header when
it is built, per the charter's rule that a gate's header names what it does not check. The version
that would catch M3 is a documented review check: **for each scope item, count the imperative edits it
names and confirm a criterion observes each.** That is a human read, filed on the §10 checklist.

---

## M4 — MEDIUM. The constraint that protects AC18's figure misstates the mechanism that produces it

**Address:** §2 S6, *What makes the +2 true, and it is a constraint on S4 and S5 rather than on S6*.
Raw id 13.

S6 states, in one sentence: an arm written as an assignment, a ternary, a comprehension, "or routed
through a helper contributes ZERO"; and, in the next clause, that `enumerate_branches` "walks each
`FunctionDef` and then its whole subtree, so an arm in a nested helper is double-counted".

Read at source, the helper half is wrong. `enumerate_branches` at `refusal_join.py:142-156` collects
every `FunctionDef` in the module via `ast.walk(tree)`, then walks each one's whole subtree. So a bare
`r.fail(...)` expression statement in a **module-level helper** is counted **once**, not zero; and in a
**nested** helper it is counted **twice**, once under `selfcheck()`'s subtree walk and once as its own
`FunctionDef`. The two clauses are mutually exclusive as written, and the first is false on its own
terms.

The assignment/ternary/comprehension half IS correct — `_is_refusal` at `:129-140` matches
`<obj>.fail(...)` only as a bare `ast.Expr`. So is the double-count half. The finding as raised said
"neither is true"; that overstates, and this entry corrects it.

**Why it is not pedantry.** AC18's exact-+2 observation rests on this paragraph. A builder who factors
S4 and S5 through one shared module-level helper — a shape the ZERO clause presents as contributing
nothing, so a careful builder might reasonably read it as forbidden-and-harmless — lands **+1**, AC18
reds, and the ledger comment claiming two new branches is false the day it is written. The clause meant
to protect the count misdescribes the matcher that produces it, which is the false-mechanism-stamped-as-measured
class the rev-6 H3 fold corrected in the neighbouring §7 bullet.

**Fix.** State what the matcher does, then state the constraint positively:

> `_is_refusal` matches `<obj>.fail(...)` ONLY as a bare `ast.Expr` statement, so an assignment, a
> ternary or a comprehension contributes ZERO. A bare call inside ANY function still counts, once per
> enclosing `FunctionDef` — twice if that helper is nested inside `selfcheck()`, because
> `enumerate_branches` walks every `FunctionDef` in the module and then each one's whole subtree. The
> shape that makes +2 true is therefore exactly two bare `r.fail(...)` statements written directly in
> `selfcheck()`, no helper.

**Left-shift gate.** None fits, and the honest disposition is a documented check. An arm that grades
prose claims about a named function's behaviour would have to re-implement the function. What IS
buildable and cheap, if this class recurs: AC18 gains a staged-break arm in the shape charter §7
requires — factor one arm through a helper, observe the delta come back +1 rather than +2, revert. The
spec would then have observed its own constraint failing instead of asserting it. Note this on the
`TOOL-aHonedRuleset-12` row as the third instance of *a spec asserting a mechanism it did not run*.

---

## L1 — LOW. AC9's last line is the enumeration AC9 supersedes

**Address:** §6 AC9, final sentence (`:556`). Raw id 7.

AC9 ends with an orphaned fragment: *"Measured at base — the `--kits` id, the anchor and the
sentence."* Three items, presented as the base measurement — when the criterion two sentences above
enumerates **four** and states the base measurement is **0** (confirmed live:
`grep -c 'check-microformats' WIRE-INTO-PROJECT.md` returns 0). It is the pre-rev-7 three-item wording
that the H4 fold replaced and did not delete.

Not a style call. It is the last line a builder reads in the criterion, and it contradicts both the
count and the base figure the same criterion asserts. A builder taking the trailing sentence as
operative lands exactly the 3-count build the H4 fix was written to catch — which is the same failure
mode H1 reaches by a different route.

**Fix.** Delete the sentence.

**Left-shift gate.** The class is *a fold that replaces a sentence and leaves the original standing*,
which is this build's dominant class across three rounds and has no cheap automated predicate. The
documented check belongs in the fold protocol rather than in a gate: **when a fold rewrites a
criterion's threshold, re-read the whole criterion, not the sentence being replaced.** File on the
`TOOL-aHonedRuleset-12` row alongside its siblings, since the row already names this class.

---

## L2 — LOW. §10 quotes §4's pre-rev-7 half and attributes it to the wrong subsection

**Address:** §10, first paragraph, last sentence (`:1254`). Raw ids 8, 29 (second half).

§10 reads "…which is why §4's *Rollout* reads *three files at rev-2, six at rev-3*". Two errors:

- The quoted sentence lives at `:421` under §4's *Files touched (estimate)*, not *Rollout* (`:399`),
  and it now reads "Three files at rev-2, six at rev-3, **seven at rev-7**." §10 truncates it before
  the rev-7 clause.
- *Rollout*'s own count sentence at `:405` says something different: "SEVEN files, one atom — six at
  rev-6."

So a reader grepping §4 for §10's quoted string finds no exact match, and the section it names says
something else. Same count-did-not-move class as M2, in the section whose job is to point a future
session at the right seam.

**Fix.** "§4's *Files touched (estimate)* reads *three files at rev-2, six at rev-3, seven at rev-7*."

**Left-shift gate.** Cheap and slightly unusual, but real: **red an italic quotation attributed to a
named section when the quoted string does not appear in that section.** Both halves are greppable —
the attribution is `§<n>`'s *`<Subsection>`* and the quote is a `*…*` span — and the arm catches the
misattribution and the truncation in one pass. Smallest new arm in the report. File on
`TOOL-aHonedRuleset-12`.

---

## L3 — LOW. F4's superlative is refuted by its own subordinate clause

**Address:** §8 F4, *The real byte cost against what was budgeted* (`:1018`). Raw id 16.

After the rev-7 re-pricing, the bullet establishes the anchored S3 form at roughly **550 B** and 0.80%
of the document, and then in the same sentence calls it "the cheapest of the three options F4
considered: the `[[runbook_exempt]]` alternative costs zero runbook bytes but answers the question NO,
and the unanchored form costs 212 and leaves the checker still naming this entry."

On the only metric the sentence itself enumerates, the anchored form is the **most expensive** of the
three — and it was already the most expensive at rev-6's 254, so the re-pricing widened an error it
did not create. Reading "cheapest" as "cheapest that closes the gap" does not rescue it either: by the
same clause the unanchored form leaves the checker naming the entry, so only ONE of the three closes
the gap, and a superlative over a set of one is incoherent.

It changes no build action. It is a false statement of fact inside a ruling's own justification, in
the section where F3 sets the standard that "a right answer resting on wrong facts is a right answer
nobody can re-derive".

**Fix.** Say what is meant: of the three options it is the only one that CLOSES the machine gap, and it
is the more expensive of the two that put bytes in the runbook — the exemption costs nothing because it
answers the question NO.

**Left-shift gate.** None. A superlative contradicted by figures in its own sentence is a review read,
and it belongs on the §10 checklist as *a comparative claim whose own enumerated numbers refute it*.

---

## L4 — LOW. Two line pins name the wrong statement

**Address:** §8 F1, *Missing option, added at rev-2* (`:783`); §5 risks, second bullet (`:496`). Raw
id 31.

- `govkit.py:1913-1915` is cited for the quote "an omission wearing a label". Verified: `:1913` is the
  no-path `r.fail(f"an exemption row carries no path: {x!r}")`, `:1914` is `continue`, `:1915` is
  `if not why:` — and the quoted sentence is at `:1916-1917`, outside the cited range entirely. §4 at
  `:302` and §10 at `:1256` pin the same seam correctly at `:1910-1917`, so the document contains both
  the right pin and the wrong one, three sentences apart.
- `selftest.py:2354` is cited for the strict-subset arm. Verified: `:2354` is
  `_declared_writes = extract_plan_writes(pl3.stdout)`, a setup line; the strict-subset `check(` head
  is at `:2356` and its predicate at `:2357-2359`. This half is weaker than raised — the pin is two
  lines high inside the right block rather than pointing at a different arm — and the finding's own
  proposed replacement `:2357-2359` omits the head. Recorded at its true strength rather than the
  raised one.

The first half matters because §8 F1's ruling instructs the builder to COPY that `[[exempt]]`
empty-reason seam rather than invent one, and the range they are sent to does not contain the sentence
they are told to model.

**Fix.** Re-pin to `govkit.py:1916-1917` (or `:1910-1917` for the whole loop, matching §4 and §10) and
to `selftest.py:2356-2359`.

**Left-shift gate.** A widening of `TOOL-aHonedRuleset-14`, which already owns the wrong-line-pin class
for backlog rows: **when a `<path>:<n>[-<m>]` pin sits adjacent to a quoted string, red when the quoted
string does not appear inside the pinned range.** Unlike the backlog-pin grep, this one is testable
against the whole `memory/builds/` corpus before wiring, per the charter's run-the-predicate-over-the-real-tree
rule, and it catches the rev-6 M4 and rev-7 L2 instances retroactively. It cannot catch a pin with no
adjacent quote, and its header should say so.

---

## Refuted, and why the refutations are recorded

Nine of thirty-one raw findings were refuted by a skeptic and dropped. The three worth naming, because
each is a plausible reading a future round should not re-raise:

- **`cmd_update`'s lack of leg emission reaches AC17.** It does not. AC17's run (2) names `apply`
  explicitly, so the missing emission in `cmd_update` is a defect in §4's *by §5b's path or their own*
  sentence and nothing more. Recorded inside H2 at that reduced scope.
- **S6's nested-helper double-count claim is false.** It is correct. Only the helper-contributes-ZERO
  half is wrong, and M4 says so rather than carrying the raised finding's "neither is true".
- **The `grep -n apply` enumeration invalidates §3's ruling.** It does not — both omitted hits are
  `git apply` prose. The figure is the defect, not the boundary, which is why M1 is MEDIUM and not the
  HIGH one lens graded it.

Precision rose to 0.71 from round 2's 0.67 on the same lens set and the same skeptic protocol, which
is the third consecutive rise. The refuted set is now dominated by over-reach inside otherwise-correct
findings rather than by findings that were wrong outright — three of the nine were the same defect
raised twice with the second copy claiming more than the first.

---

## Disposition, and what closes the loop

Blockers: **2 → 1 → 1.** Not strictly smaller, so this round does not re-arm and there is no round 4.

- **B1 is DISPOSED by FOLD.** It is a defect in the spec — a document this review read at the pinned
  blob — its fix is one `--answer` clause plus two restated sentences plus a backlog-row correction,
  and the corrected two-run sequence was executed end to end so the fold is not another trace onto an
  unrun command. **No mechanism this build lacks is required**, so nothing is promoted to a specced
  unit of its own.
- The three HIGH, four MEDIUM and four LOW entries are all spec edits in the same document, foldable
  in the same commit. None re-opens a fork ruling, challenges a scope item on the merits, or removes
  anything from scope.
- Three defects reach OUTSIDE the spec and must be corrected in the same commit, per §3's own
  precedent for that row: `memory/backlog/TOOL.md:6` carries B1's false premise, H2's false universal,
  and M1's eight-hit enumeration.

Left-shift, consolidated: **the single arm worth building from this round is the one that executes
every command a §6 criterion quotes and compares its exit status and output to the stated one.** It
catches B1, H2's evidence, M1 and L1's base figure — four of twelve entries, including the blocker,
and it would have caught round 2's B1 as well. File it on `TOOL-aHonedRuleset-12`, which already owns
the acceptance-criteria-that-cannot-fail class and has now been widened twice by this same build. Six
of the twelve entries here are what that row predicted.

**Rev-8 is the fold. The unit is buildable the moment it lands.**
