**Serves:** spec-audit TOOL-aWeldedTribunal-1 TOOL-aWeldedTribunal-2 TOOL-aWeldedTribunal-3 TOOL-aWeldedTribunal-4 TOOL-aWeldedTribunal-5 TOOL-aWeldedTribunal-6 TOOL-aWeldedTribunal-7 TOOL-aWeldedTribunal-8

# Spec audit — aWeldedTribunal, round 2

Tier-2 adversarial spec review of the same eight-unit set at rev-2, after round 1's sixteen findings
were folded. The subject of this round is the FOLD: prose written since round 1 that nobody has
reviewed. Round-1 findings are treated as addressed and are not re-reported; what follows is what
the fold got wrong, or what it newly contradicts. Fan of primed finder lenses, then a skeptic pass
prompted to REFUTE each finding, then this synthesis. Every source claim below was re-checked
against the tree while writing this report, and the blocker was reproduced by running the hook.

**Range — ROUND 2**, subjects pinned at these blobs (all eight re-hashed at write time and matching):
`memory/builds/aWeldedTribunal/spec/2026-09-04-spec-TOOL-aWeldedTribunal-1.md@6e1dec1c3503` ·
`…-2.md@5c363d5c5548` ·
`…-3.md@bf085494de4c` ·
`…-4.md@0173dc1cce38` ·
`…-5.md@aff546291f40` ·
`…-6.md@35b6b602c68c` ·
`…-7.md@f4e970831e2d` ·
`…-8.md@13615447ebc1`

## Verdict: BLOCKED

One blocker, and it is the same defect round 1 raised as H2 on the same criterion: unit 2's AC1 was
rewritten to reach this unit's mechanism and still cannot. I built AC1's script, ran it against the
shipped hook and against a copy patched with this unit's own take-back sweep, and got exit 0 both
times. The fold moved the criterion onto a `.map` fan but left the `agent()` call inside the `push`,
which is not where the hook looks. That is a criterion green before and after a faithful build, so
the unit cannot be built against it.

Everything else is repairable in place with the edits named below, and most of it is one class: the
fold corrected a table and left the prose beside it stating the old number. Five of the seventeen
defects are literally that shape, in three different specs, and the charter names the rule they
break. Two more are the round-1 dominant pattern recurring on fold-new scope items — an S-item with
no criterion that observes it.

**Review shape:** raw 41 · confirmed 20 · refuted 21 · unverified 0 · precision 0.49.

Precision 0.49 on a second pass over specs that just absorbed sixteen fixes is the expected shape:
the surface is harder than round 1's and the yield held. Read the count with the collapse below —
20 confirmed findings are 17 distinct defects.

**Collapsed.** Three collapses, all within one spec: `9`+`16` are one defect (unit 4's §4 prose says
seven over an eight-row table) and `16` carries the fuller account; `14`+`27` are one defect (unit
5's S1 and its Alternatives bullet both restate the import claim the same document refutes);
`17`+`37` are one defect (unit 5's title, §1 and §4 heading say five over a six-row inventory).

| # | Sev | Unit | Address | Defect |
|---|-----|------|---------|--------|
| B1 | BLOCKER | 2 | §6 AC1, AC3 | The rewritten criterion is green before AND after a faithful build |
| H1 | HIGH | 6 | §2 S2 vs §6 AC6 | The declined-row half of S2 is observed by no criterion |
| H2 | HIGH | 6 | §2 S1b, §5 | Grading through `decline_findings` gives `update` twelve new refusals |
| H3 | HIGH | 4 | §7, AC5 | Denies the `GATE_SELFTESTS` leg this unit's own file triggers |
| H4 | HIGH | 3 | §6 AC5, §3 | The fallback re-opens the false-positive class rule 5's view narrowed away |
| H5 | HIGH | 8 | §2 S5, §4 row 5 | A false closure — the row's claim survives unit 6 by unit 6's own non-goal |
| M1 | MEDIUM | 5 | §4 inventory, row 5 | `row_grammar.load_conf` carries NO defaults and raises on an absent conf |
| M2 | MEDIUM | 4 | §2 S2 | The incompleteness clause — "the half that makes the block do work" — is uncriterioned |
| M3 | MEDIUM | 1 | §1, §4, §10 | Three sections still say five sites; S1, §4 and AC6 say six |
| M4 | MEDIUM | 1 | §2 S1 | S1's own arithmetic does not close: six sites, five direct plus two siblings |
| M5 | MEDIUM | 4 | §4 prose | "the seven" twice, over an inventory the fold grew to eight |
| M6 | MEDIUM | 5 | title, §1, §4 heading | Three counts say five over a six-row inventory that declares itself the source |
| M7 | MEDIUM | 5 | §2 S1, §4 Alternatives | The import claim the same document refutes three times survives in the scope item |
| M8 | MEDIUM | 6 | §2 S1b, §4 | `update` becomes call site three; three enumerations in the source stay wrong |
| M9 | MEDIUM | 7 | §2 S5, §6 AC8 | Half the gotcha record refreshed; the other half still says the check is unwritten |
| M10 | MEDIUM | 1,2,3,5,6,7 | §7 | Cites `AGENTS.md`'s "full pair" and prescribes one half of it |
| M11 | MEDIUM | 3 | §6 AC4, §4, §5 | "rule 4" is the file's RULE 5 — a wrong pointer, not just a stale count |

---

## B1 — BLOCKER · unit 2 · §6 AC1 (and AC3, which inherits its shape)

AC1 is the criterion the fold added to fix round 1's H2, and it still cannot reach the iter arm.
It spells the growth as `batches.push(() => agent(f.claim))` and the fan as `batches.map((b) => b())`
on a separate line. `fanoutFindings` judges only lines matching `/\bagent\s*\(/`
(`tools/hooks/agent-cap.js:851`), so the `.map` line is never examined at all. For the `push` line
the opener walk finds `push(`, whose preceding text ends in `batches.push` — which `ITER_CALL`
(`:426`) does not match — so `hit` stays null and the function returns with no finding. `markedWhy`
is read at exactly one site, `:918`, inside the `hit.kind === 'iter'` arm, and that arm is
unreachable for this shape.

Measured, not argued. I wrote AC1's script verbatim from its own text, wrapped it as a `Workflow`
payload and piped it to the shipped hook: exit 0, as AC1 itself predicts. Then I patched a copy of
the hook with this unit's take-back sweep (a `GROWS_RECEIVER` regex over `push|unshift|splice`,
placed beside the reassignment sweep, with a debug line on every take-back) and re-ran it: the sweep
fired twice on `batches` and the script still exited 0. The control — the same script with the agent
call moved inside the map receiver, `batches.map((f) => () => agent(f.claim))` — went 0 to 2 against
the patched hook, carrying this unit's own reason text, `` `batches` was GROWN by a mutation after
its bounded assignment ``.

So AC1 and AC3 are unobservable. A build can satisfy AC1, AC2, AC3, AC5 and AC6 while the take-back
sweep denies nothing, and AC4 (the five tracked harnesses still exit 0) passes vacuously because it
passes today. What the adjacency requires is that the `agent()` call sit lexically INSIDE the map
receiver's parens — the presence of `.map` on some other line buys nothing.

**Smallest fix:** respell AC1 and AC3 onto the shape that reaches `:912-919` — `const batches = []`
grown with a plain value (`batches.push(f)`), then fanned as
`await boundedParallel(batches.map((f) => () => agent(f.claim)), 5)`. State in AC1 that the agent
call must sit inside the map receiver's parens, because that adjacency, not the `.map`, is what the
opener walk reads. Note the bound must resolve: an unresolvable `MAX_VERIFIERS` in the fixture reds
under a different rule and hides the one being tested.

**Left-shift:** the class is a criterion that asserts a pre-state exit code and was never run. An
arm in `tools/hooks/agent-cap.test.sh` holding BOTH shapes — the push-plus-detached-map (must stay
0, it is legal) and the push-plus-inline-fan (must be 2, naming the mutation) — pins the difference
in both directions, which is the discipline the file's own rule-5 fixtures already follow. Beside
it, a documented check for the spec process: any AC of the form "today it exits N" is RUN before the
spec is ratified and its observed output pasted into §4. That is what would have caught this in
round 1 and again in the fold.

---

## H1 — HIGH · unit 6 · §2 S2 and §6 AC6

S2 has two halves. The undeclined half is covered several times over. The declined half — "A
DECLINED row prints too, as a declined row, because a gap that disappears from a report without
saying why is the exclusion-list shape the decline contract exists to avoid becoming" — is observed
by nothing. AC1 and AC5 are undeclined-gap arms, AC2 and AC3 are summary and zero arms, AC4 is
scope, AC7 is the gate. AC6, the one criterion that mentions declines at all, observes only the
ABSENCE of an undeclined `GAP` row plus a COMPLETE summary.

The cheapest build satisfying AC6 filters declined rows out of the report entirely. That passes
every criterion in this spec whole while committing exactly the exclusion-list failure S2 names and
`DEPL-dCarriedReceipt-5` exists to prevent — and it is the shape the reference call site goes out of
its way to avoid: `tools/govkit/govkit.py:2681-2689` prints the declined rows rather than dropping
them.

This is round 1's dominant pattern (an S-item with no criterion, confirmed four times there)
recurring on a fold-new scope item, one unit over from where round 1 found it.

**Smallest fix:** add an AC6b — against a fixture whose only gap is declined, the output prints a
`declined` row naming the kit and the destination, and the summary says COMPLETE. AC6 keeps the
absence half; AC6b takes the presence half.

**Left-shift:** a `govkit selftest` arm over that same fixture asserting both facts in one run — no
undeclined `GAP` row, one `declined` row, summary COMPLETE. It covers all three call sites' shared
contract, so a future fourth caller that filters instead of grading reds on the class rather than on
this instance.

---

## H2 — HIGH · unit 6 · §2 S1b and §5

`decline_findings` is not a pure grader. It calls `r.fail(...)` on twelve arms
(`tools/govkit/govkit.py:2489, 2500, 2508, 2515, 2520, 2524, 2539, 2553, 2559, 2567, 2600, 2609`),
`Report.emit` returns 1 whenever `problems` is non-empty (`:964-972`), and `_cmd_update` returns
`r.emit()` on every exit path (`:6419` read-only, `:7508`, `:7532`, `:7544`). S1b mandates grading
"the way both existing call sites do it", and both pass their own `r`.

So after this unit, a malformed or stale `[[decline]]` row — an empty `why`, a dest the target now
tracks, a dest no claimed kit ships at the measured revision — FAILS `govkit update`, a write verb
operators run constantly, for a defect that has nothing to do with the update.

§5 asserts the opposite: "no new write path; this unit strictly reads and prints", and the risks
bullet names only "a REPORT does not fix the adopter". AC6's fixture uses a valid decline row, so no
criterion observes the red path. "No new write path" is literally true and is not the question; the
question is a new refusal on a verb that had none.

**Smallest fix:** state in S1b that `decline_findings` writes findings into the Report and that
`update` emits it, then decide explicitly. Either accept the refusal — say so in §5's risks and pin
it with a criterion (a fixture with one stale decline row makes `update` fail, naming the row) — or
pass a throwaway Report so `update` reports gaps without inheriting decline hygiene. Record which,
and why.

**Left-shift:** a `govkit selftest` arm per verb asserting the exit code over a fixture with one
stale decline row, so the decline contract's blast radius is stated per call site rather than
inherited by whichever verb wires it next.

---

## H3 — HIGH · unit 4 · §7 (and AC5)

§7 says flatly "no `GATE_SELFTESTS=1` is owed by this unit". The unit's only code file is
`tools/workflows/tier2-review.js`, and `tools/gate-legs.json` carries
`{"name": "tier2-review self-test", "argv": ["bash", "tools/workflows/tier2-review.test.sh"],
"guard": ["tools/workflows/"], "chunk": "selftests", "subject": "kit", "ceiling": 1800}` — plus two
more kit-subject legs, `verifier fan-out self-test` and `review-join self-test`, that also guard on
`tools/workflows/`. The edited file sits squarely inside that guard.

So the unit's DoD runs the syntax leg only and never runs the self-test of the harness it edits: a
prompt edit that breaks that suite lands green. Worse for the set as a whole, AC5's "unlike the
kit-subject legs the other units name" puts two opposite rules about the same leg class inside one
spec set — five siblings say a DoD owes `GATE_SELFTESTS` for kit work, this one says it does not.

If the 1800 s ceiling is the real reason to hold it, that is a deliberate exemption owing a
compensating check, not a denial that the leg applies.

**Smallest fix:** name `GATE_SELFTESTS=1 bash tools/run-gates/run-gates.sh` for the
`tier2-review self-test` leg alongside the plain-bar `workflow script syntax` leg, and either drop
AC5's "unlike the kit-subject legs the other units name" clause or restate it as "in addition to".
If the leg is deliberately held, say so and name the compensating check.

**Left-shift:** a spec-lint arm that is genuinely derivable — read every path in a spec's §4
"Files touched", resolve which legs in `tools/gate-legs.json` guard on it, and red when §7 names
neither the leg nor an explicit exemption for it. It fires on this spec today, and it is the general
form of round 1's H7.

---

## H4 — HIGH · unit 3 · §6 AC5, against §3's third non-goal

The fold's new fallback re-exposes contents that `TOOL-dTieredTribunal-14 S2` deliberately narrowed
away, and no criterion pins the narrowing.

`tools/hooks/agent-cap.js:1406-1409` records the choice of `renderBlankedLiterals` for the join rule
as "a deliberate NARROWING: the awk kept string CONTENTS and only stripped comments, so it matched
the retired identifier inside a string. Two fixtures in the self-test pin the difference in both
directions." S3's fallback view is `renderStrippedView(l).split('//')[0]`, and `:1435-1437` records
that `renderStrippedView` "leaves backticks alone" — it does not blank template contents.

So on the unterminated branch the join rule tests text with template contents intact against the
BANS at `:1418-1421` (`/verdictByRef/` and the two `.ref`-keyed shapes), regaining exactly the
false-positive class those two fixtures exist to pin: a harness carrying an unterminated backtick —
unit 3's own standing regex-literal residual is the live way in — plus a lens prompt that mentions
`verdictByRef` or a `.ref`-keyed shape inside a backticked string is denied. §5's mitigation does
not reach it, because `runBothViews` UNIONS the two views, so a false positive under either denies.

AC5's negative arm tests only a LEGAL, terminated multi-line literal above a legal join, so it
passes while the class ships. Unit 3 also carries no S-item for the charter's pre-wiring predicate
run, which units 1, 2 and 5 all have and which is what refuted unit 2's vocabulary before a line was
written.

**Smallest fix:** add an AC mirroring the pinned fixtures onto the fallback — a script with an
unterminated backtick above a line whose TEMPLATE CONTENTS mention a banned pattern must still
report nothing. Cite `TOOL-dTieredTribunal-14 S2` in §3 and say whether the narrowing is preserved
on the fallback branch or knowingly traded. Add an S-item running the fallback over the tracked
harnesses before wiring, printing hits and near-misses.

**Left-shift:** the two existing self-test fixtures are the template — duplicate each onto the
unterminated branch, so every view this rule can take is pinned in both directions. Any future third
view inherits the pair.

---

## H5 — HIGH · unit 8 · §2 S5 and §4's evidence table, row 5

S5 flips `TOOL-aScouredKit-25` to CLOSED "against `TOOL-aWeldedTribunal-6`", and §4's evidence row
says "closed by `TOOL-aWeldedTribunal-6`, per its own text". The row's own text says something else.
`memory/backlog/TOOL.md:303` reads: "This is `TOOL-aFlaggedScaffold-3`, which already tracks it with
the inCMS measurement... Close this row against that one rather than working it twice."
`TOOL-aFlaggedScaffold-3` is still OPEN at `memory/backlog/TOOL.md:16`, and no unit in this build
closes it — S1 through S5 close dScrubbedConduit-2, dScaffoldedMirror-22, aGroundedOrientation-4,
aFlaggedScaffold-4 and aScouredKit-25.

The row's claim — `govkit update` cannot land a source gov ships — is still true after unit 6, by
unit 6's own first non-goal: "This unit reports; it does not land bytes", and the landing verb "is a
follow-up". So S6's required closure tail would have to name a fix that did not happen, leaving two
rows with identical headlines at opposite statuses. That is the stale-row harm this build exists to
remove, inverted.

Unit 6's §3 gets this right, incidentally — it says the row "says in its own text to close it
against `TOOL-aFlaggedScaffold-3`". Unit 8 quotes the same source and reverses it.

**Smallest fix:** in S5 and the §4 row, cite the closure as a DUPLICATE of `TOOL-aFlaggedScaffold-3`
— which stays OPEN and keeps tracking the landing verb — and have the tail say
`TOOL-aWeldedTribunal-6` adds the report rather than the landing. Adjust §1 so the fifth row is
described as a dedupe rather than a fixed defect.

**Left-shift:** a memory-tree hygiene arm — a row whose body names another id with a close-against
instruction cannot be closed against a THIRD id without the tail naming both. Derivable from the row
grammar the kit already parses, and it fires on this edit before it lands.

---

## M1 — MEDIUM · unit 5 · §4 Inventory, `row_grammar.py` row (with §2 S3 and §5)

The inventory credits `row_grammar.py` with defaults "`MEMORY_ROOT` `FAMILIES` and a pin". It
carries none. `tools/memory-tree/row_grammar.py:86-94` is `def load_conf(root): conf = {}` with a
bare `read(os.path.join(root, ".memory-tree.conf"))`, and `read` at `:56-58` is a plain `open` — so
it RAISES on an absent conf. The other four readers all open with a populated defaults dict AND
`if os.path.isfile(p)`: `corpus_ids.py:105-119`, `gotchas.py:83-93`, `gen_build_index.py:278-288`,
`check-arms.py:73-83`. Those `MEMORY_ROOT` and `FAMILIES` are keys row_grammar READS, not defaults
it holds.

This matters more after the fold than before it, because rev-2 made this table load-bearing — "This
inventory is the single source for the count", and L1 rewrote AC1 and AC2 onto it. Routing that
reader through a shared `load_conf(root, defaults)` carrying the isfile guard silently converts
today's hard failure on a missing conf into a quiet empty-dict success. That is the opposite of §5's
"an absent conf still yields the defaults, unchanged", which is true for four readers and false for
the fifth, and AC4 cannot see it because it compares only tracked confs that declare the key.

Borderline high: it is a real behaviour change with no criterion, and the direction is toward silent
success. It stays medium only because the builder must touch that function to make the change at
all, and the missing defaults are visible in the first line of it.

**Smallest fix:** correct the cell to "none — `conf = {}`, and it raises on an absent conf", and add
one line to §4 plus a criterion deciding whether row_grammar keeps refusing on a missing conf or
adopts the guard. The shared parser cannot preserve both behaviours by accident.

**Left-shift:** an arm per reader over a fixture root with NO `.memory-tree.conf`, asserting each
reader's documented disposition — four return defaults, the fifth refuses (or, post-decision,
whatever §4 chose). One arm makes the difference a fact rather than a table cell.

---

## M2 — MEDIUM · unit 4 · §2 S2

S2 is the clause "if lenses died the finding set is INCOMPLETE and a zero is not evidence of
absence", which the spec itself calls "the half that makes the block do work". After the fold
dropped rev-1's AC2, AC3 and AC4, no criterion observes it. AC1's population is the eight counter
identifiers, AC2 observes a `RUN INTEGRITY` line "carrying those numbers", AC3 is the gotcha record,
AC4 and AC5 are the syntax leg.

A block interpolating all eight counters and omitting the incompleteness instruction passes every
criterion — which is precisely the "prints the counters and still opens with no issues found"
outcome S2 names, and this unit's whole subject is that sentence rather than the numbers.

Mitigated, which is why it is medium and not high: §4's block literal does carry both sentences
verbatim, so a builder copying the block ships them. The gap is that nothing FAILS if they do not.

**Smallest fix:** extend AC1 to the block's TEXT and not only its interpolations — the prompt
carries the do-not-call-this-run-complete sentence and the zero-is-not-absence sentence.

**Left-shift:** the owner ruling makes the left-shift here a record, not a scanner, so this one is a
documented check: the DoD line in `memory/gotchas/degradation-known-but-unreported.md` names the two
sentences alongside the counter set, so the next harness that adds a block is told what the block is
for rather than which variables it holds.

---

## M3 — MEDIUM · unit 1 · §1 Goal, §4 "Files touched", §10

Three sections still say five: "Replace the five copies" (§1), "five regex literals replaced" (§4),
"its five existing loop-header predicates" (§10). S1, §4's inventory table and AC6 say SIX. The tree
says six: `tools/hooks/agent-cap.js:705, 711, 738, 910, 934, 944`.

The Goal and the Files-touched estimate are the two lines a builder scopes a diff from, and the site
the fold added — `:910`, whose fail-open §4 devotes a whole subsection to — is exactly the one a
five-count drops. Only AC5 and AC6 would catch it, after the work.

Rider, verified while checking this: §4's inventory row and S1 both address the second site as
`:710`; the literal is at `:711`. One line off, and the same row is the one the sentence in M4 gets
wrong, so both are worth fixing in the same pass.

**Smallest fix:** §1 to "the six copies", §4's Files touched to "one constant plus two derived
siblings added, six regex literals replaced", §10 to six, and `:710` to `:711` in both places.

**Left-shift:** none available as a gate — a spelled-out count in prose is what the charter bans, so
the fix is deletion, not detection. Where a number must appear, it appears in the table. Documented
check: at fold time, grep the spec for number-words and confirm each against the table it describes.

---

## M4 — MEDIUM · unit 1 · §2 S1, the sentence "Five take the predicate directly"

S1's own arithmetic does not close. It declares SIX sites, then says "Five take the predicate
directly; `:710` and `:910` take siblings" — five plus two is seven. §4's table shows exactly four
rows taking `LOOP_HEADER` (705, 738, 934, 944) and two taking derived siblings, so the correct word
is four.

A builder counting from S1 expects five direct substitutions and one sibling, which leaves one of
`:710`/`:910` to be substituted wrongly. `:910` is `/\b(for|while)\s*$/` tested on the text BEFORE
an opener, so a pattern ending in `\(` or `do\s*\{` can never match there — the silent fail-open the
fold added the sixth row to close.

**Smallest fix:** S1 reads "FOUR take the predicate directly; `:711` and `:910` take siblings
DERIVED from the same source".

**Left-shift:** an arm in `agent-cap.test.sh` asserting the `:910` sibling matches `for await` at
end-of-text and that a script fanning inside `for await (` is denied. It is the behaviour the count
is a proxy for, and unlike the count it cannot be miscounted.

---

## M5 — MEDIUM · unit 4 · §4, prose under the counter inventory and under "The left-shift"

The fold's H9 change added `conflicts.size` to §4's inventory, making it eight rows. Two sentences
below it still say seven: "the seven above that describe RUN HEALTH rather than finding counts do
not", and "what a static check CAN see is that the seven identifiers appear inside the synthesis
prompt". AC1 enumerates all eight and calls itself "the SET, not a sample".

All eight rows are run-health counters by §4's own argument for `conflicts`, so seven is simply
stale. AC1 and §4 now state different sizes for the same set, and §4 is the text a gotcha record or
a later reader copies — so `conflicts.size` can be dropped from the record while §4 still reads as
satisfied.

**Smallest fix:** replace both occurrences with a pointer to the table ("every counter in the table
above"), per the same no-count-in-prose rule unit 5's §4 applies to itself.

**Left-shift:** the record in AC3 names the counter set by pointing at the inventory rather than
listing it, so the record cannot fall behind the table either. Same rule, one document over.

---

## M6 — MEDIUM · unit 5 · title, §1 Goal, §4 inventory heading

The title reads "read by all five python readers", §1 says "Five python readers" and "Route all
five", and §4's heading reads "Inventory — the five copies" — over a SIX-row table whose sixth row
is `corpus_ids.read_declared_keys`, added by the fold's H10 and made load-bearing by S3b and AC2b.
Two sentences under that heading, the spec declares "This inventory is the single source for the
count" and that no criterion states a number, citing the charter's no-count-in-prose rule.

A heading that contradicts the table it heads, in the paragraph nominating that table as the count's
only source, is wrong text rather than a style preference. The title and the Goal are what a builder
scopes from, and the reader who scopes from them ships the five-reader change S3b says creates a
fresh two-answers-to-one-question inside `corpus_ids.py`.

One half of the original finding is refuted and worth recording: §3's last non-goal is bold-headed
"The drift-audit copy." and names `TOOL-aScouredKit-5`, so it cannot reasonably be read as excluding
S3b, which is an explicit in-scope item with its own criterion. The word "sixth" doing double duty
in one file is still worth removing.

**Smallest fix:** retitle to the mechanism rather than the count ("read by every python reader"),
change §1 to name the readers instead of counting them, change the §4 heading to "Inventory — the
copies", and rename §3's non-goal so "sixth" names one thing in this file.

**Left-shift:** none as a gate; deletion is the fix. Documented check, same as M3.

---

## M7 — MEDIUM · unit 5 · §2 S1 and §4 "Alternatives rejected", first bullet

S1 justifies the parser's home with "`corpus_ids.py`, which already holds `load_conf` and is already
imported by `gotchas.py`", and the first Alternatives bullet repeats "already the import target of
one of the four". Both are the claim this same document refutes three times.

Verified: `grep -n corpus_ids tools/memory-tree/*.py` hits only inside `corpus_ids.py` itself, and
`gotchas.py` imports os, pathlib, re, subprocess, sys and tempfile — no sibling. §4's measurement
paragraph says so ("this adds four import edges where the row promised zero"), and §9's rev-2 entry
and §10's stale-hit paragraph say it again.

So the spec gives two answers to "is this reuse free", and the false one sits in the binding scope
section. A reader who stops at S1 re-adopts the retired justification, under-plans the four new
`sys.path` sibling imports, and reads §4's priced trade as a build mistake.

**Smallest fix:** rewrite S1's clause to match the measurement — `corpus_ids.py` already OWNS the
conf and carries the widest defaults, which is why it hosts the parser; the four import edges are
new and §4 prices them. Change the Alternatives bullet to "already owns the conf; the four import
edges are priced in §4".

**Left-shift:** a documented check at fold time — when a measurement refutes a claim, grep the spec
for the claim's own words before closing the fold. Two of this round's findings are the same fold
correcting one section and leaving the premise standing in another.

---

## M8 — MEDIUM · unit 6 · §2 S1b and §4 "Files touched"

S1b makes `update` the THIRD `decline_findings` call site, which falsifies that function's own
docstring and both numbered call-site comments. All three verified verbatim: `govkit.py:2438` reads
"ONE PREDICATE, TWO CALL SITES — `cmd_check` and `plan --coverage`" inside the docstring, `:2674`
reads "DEPL-dCarriedReceipt-5 S7, call site one of two", `:2859` reads "call site two of two".

Those three sentences are the record of the decision S1b reuses, and the fold quotes them as its
evidence while leaving them to become wrong on landing. §4's Files touched says only "one call, one
print loop, one summary field". A build passing AC1 through AC7 whole leaves the decline contract's
own docstring telling the next reader there are two graders when there are three — the same class
sibling unit 7 spends S4, S5, AC7 and AC8 on for two other carriers, in the file this unit edits.

**Smallest fix:** add to S1b that the three enumerations at `govkit.py:2438`, `:2674` and `:2859`
are renumbered in the same commit, list the docstring and comments in §4's Files touched, and add a
criterion that reading `decline_findings`'s docstring names all three call sites.

**Left-shift:** a `govkit selftest` arm counting the call sites of `decline_findings` by scanning
the file and comparing against the number its docstring states. The count is derived, the docstring
is authored, and the arm is the parity gate between them — it generalises to any "call site N of M"
comment in that file.

---

## M9 — MEDIUM · unit 7 · §2 S5 and §6 AC8

The gotcha refresh is scoped to the record's "Its gate" section alone. Round 1's finding named "Its
gate" AND "What to do", and the second section carries the same false assertion.

`memory/gotchas/hookspath-resolves-into-another-checkout.md:59-62`, under "What to do", reads:
"**A gate on this is possible and is not written.** `check-wiring.sh` already resolves
`core.hooksPath`; it could compare the resolved directory's blob against the tracked one at HEAD and
report a mismatch." That is a description of exactly what S1 builds, in the conditional.

So a build satisfying AC8 whole leaves the cited class record still asserting that the thing just
built does not exist — verbatim the defect S5 exists to remove, one paragraph up, and the same
half-fix S4 closes for the hook header one section over.

**Smallest fix:** widen S5 and AC8 to name both sections, or better, write them over the record's
carriers rather than one heading: after the refresh, no paragraph of that file may assert the
comparison is unwritten or unopened.

**Left-shift:** a memory-tree hygiene arm — a gotcha record whose "Its gate" section names a written
gate cannot carry "is not written" or "is opened as a backlog item" anywhere else in the file. It is
a within-file contradiction, cheaply derivable, and it fires on this record today.

---

## M10 — MEDIUM · units 1, 2, 3, 5, 6, 7 · §7 Gates (one shared sentence)

Six specs' §7 prescribes `GATE_SELFTESTS=1 bash tools/run-gates/run-gates.sh` and then cites
`AGENTS.md` as recording "that a DoD owes the full pair for KIT work, which this is". The full pair
in `AGENTS.md:488` is `GATE_FULL=1 GATE_SELFTESTS=1 bash tools/run-gates/run-gates.sh   # every leg
there is. Owed by a DoD only for KIT work`. The specs prescribe one half of it.

`GATE_FULL=1` is what bypasses the per-leg guards (`AGENTS.md:486, 494`), so without it the kit legs
outside the touched directory stay held. §7 therefore states an obligation its own command does not
discharge, and a builder either under-runs the DoD or cannot tell whether `GATE_FULL=1` was dropped
deliberately — with no `skipped` line to say which legs went unexercised. In units 3, 5, 6 and 7
only ONE leg is named, so "the pair" has no local referent either.

**Smallest fix:** either prescribe `GATE_FULL=1 GATE_SELFTESTS=1` where the cited rule is invoked,
or keep `GATE_SELFTESTS=1` and say plainly why the guards are left in force for this unit. In all
six specs, since the sentence is shared.

**Left-shift:** the same §4-derived spec-lint arm proposed under H3 covers this too — it resolves
the legs a spec's touched paths trigger and reds when §7's command would not run them. One arm,
both defects, and it is the only mechanical answer to a sentence copied into six files.

---

## M11 — MEDIUM · unit 3 · §6 AC4, §4 inventory, §5

The spec calls `scanJoinFindings` "rule 4" in S4, in §4's inventory table and in AC4; §5 compounds
it with "two of four rules". The file's own numbering disagrees: `agent-cap.js:1398` is
"TOOL-dTieredTribunal-14 S1 - RULE 5, the ref-keyed verdict join", `:1592` is "RULE 5 - the
ref-keyed verdict join. LAST", `:1214` is "RULE 4 — the ARITY of DIRECT `Agent` spawns", and the
header at `:91` says the file has five rules.

This is a wrong POINTER, not merely a stale count. AC4 is the criterion the fold added specifically
so the join rule cannot be left blind, and RULE 4 never reads `renderBlankedLiterals` and cannot
satisfy it — a verifier following the number lands on the wrong function. The function name carried
alongside it limits the damage without making the criterion right.

**Smallest fix:** renumber to 5 in AC4, §4's inventory and §5, or drop the numbers and name
`scanJoinFindings` directly. The function name is unambiguous and the file owns the numbering.

**Left-shift:** the general form is the reuse-lint the charter already implies — a spec naming a
source construct by an ordinal must match the source's own label. Cheaply approximated: grep the
spec for `rule <n>` and confirm each against the `RULE <n>` comments in the file §4's inventory
names. Documented check at fold time if it is not worth a leg.
