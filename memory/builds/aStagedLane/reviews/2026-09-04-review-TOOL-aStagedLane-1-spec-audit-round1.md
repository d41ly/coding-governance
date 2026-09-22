**Serves:** spec-audit TOOL-aStagedLane-1 TOOL-aStagedLane-2 TOOL-aStagedLane-3 TOOL-aStagedLane-4

# aStagedLane — spec audit of the four-unit set, round 1

*Node `a`, 2026-09-04. A Tier-2 adversarial pass over the four specs as DESIGNS, not as code: a
primed finder fan, a skeptic stage prompted to REFUTE each finding, one synthesis. Every claim a
finding made about the existing tree was re-checked at source before it was written here; the
re-check is quoted inline wherever it is the load-bearing part of the finding.*

**Round: 1.** Subjects, each pinned at the blob it was read at:

- `memory/builds/aStagedLane/spec/2026-09-04-spec-TOOL-aStagedLane-1.md@d49748eafa2881120073f1fdc20713f6b05cc6cc`
- `memory/builds/aStagedLane/spec/2026-09-04-spec-TOOL-aStagedLane-2.md@cc47cbca7acdf309dbae1db45c3d43cb39931bba`
- `memory/builds/aStagedLane/spec/2026-09-04-spec-TOOL-aStagedLane-3.md@a6c362e80e26031c8d3d7dd3e75d7be840a04e96`
- `memory/builds/aStagedLane/spec/2026-09-04-spec-TOOL-aStagedLane-4.md@3088f3f245dd06514457675179fd4e7a5d2a78f5`

## Verdict: BLOCKED

Four blockers stand, one per unit, and three of them are the same failure mode: a scope item that
describes the tree wrongly. Unit 4 is told to delete a charter sentence that does not exist. Unit 3
is told to reuse a helper that is not in the file it edits. Unit 2 counts three driver call sites
where the prompts name four, and two of the missed verbs hard-refuse in exactly the mode the unit
exists to create. Unit 1's blocker is different in kind and worse in consequence: the range anchor
the owner ruled for structurally exempts the flagrant instance of the very violation the widening
exists to catch — code committed first, the build folder and its spec created afterwards — because
that commit sits strictly before the anchor and lands in the `unbuilt-in-range` tally the leg's own
header warns must not be read as benign.

Two of the eight owner rulings rest on premises the tree contradicts. F2 on unit 4 was decided
against the spec's own recommendation on the strength of "the existing sentence becomes false when
unit 1 lands"; there is no such sentence. F2 on unit 1 offered two anchors and disclosed the hole in
neither. Those two want re-putting with corrected premises before any code is written; the other six
rulings are unaffected by anything here.

The design is sound in outline. Three stages without a run-state file is a coherent route, the
disjointness reasoning in unit 3 is the right shape of argument, and unit 1's move of the `opened:`
read to the graded commit is a real narrowing. What the set does not have is a reliable relationship
between what its scope items assert about the tree and what the tree contains.

## Review shape

Raw 56, confirmed 26, refuted 30, unverified 0, precision 0.46. The 26 confirmed findings fold to 17
distinct defects: three lenses independently found the missing charter sentence and three found the
missing helper, which is what a spec set gets when its false premises are the load-bearing ones.
Precision at 0.46 sits just under the ~0.5 floor §8 sets for adding agents rather than tightening
scope. The refutations concentrated in lenses grading the specs' prose against the template's shape
rules; every lens that instead checked a spec claim against source returned confirmable findings, so
a future document pass should spend its budget there and cut the conformance lenses.

| Defect | Raw ids folded in |
|---|---|
| B1 the charter sentence that is not there | 13, 31, 46 |
| B2 the helper that is not in the file | 14, 32, 45 |
| B3 the anchor that exempts the worst case | 44 |
| B4 the two verbs that refuse in attended mode | 15, 33 |
| H1 the liveness line already prints four | 17, 36, 49 |
| H2 the `base:` lever left standing | 37 |
| H3 the ceiling with two carriers | 22, 47 |
| H4 `opened:` narrowed, not removed | 48 |
| H5 the anchor's own commit | 38 |
| H6 the fan's receiver and its total | 21 |
| H7 the writers that commit | 20, 51 |
| H8 the refusal that stops firing | 40 |
| H9 the scope item with no criterion | 1 |
| H10 the criterion that is false today | 19 |
| M1 the header that miscounts its losses | 24 |
| M2 the preamble that still claims a mandate | 26 |
| M3 the gate that measures the other file | 28 |

## Findings

| # | Severity | Unit | Address | One line |
|---|---|---|---|---|
| B1 | blocker | 4 | §2 S5, §6 AC3 and AC6, §8 F2 | The charter carries no description of the pass-order leg to delete, so S5 has no subject and AC3 cannot pass. |
| B2 | blocker | 3 | §2 S2, §4 Files touched, §10 | `boundedParallel` is not in `unattended-build.js`; the reuse claim and the §10 seam are both false. |
| B3 | blocker | 1 | §2 S2, §6 AC1, §8 F2 | The folder anchor puts code-first-spec-later outside the range, so the worst violation is structurally invisible. |
| B4 | blocker | 2 | §4 The mode boundary, §2 S2 and S5 | `--brief` and `--rescope` also refuse without a run-state file; the attended BUILD stage stops at unit one. |
| H1 | high | 1 | §2 S3, §6 AC3 | The line already prints four counts; AC3's "four counts" is satisfied by the unmodified script. |
| H2 | high | 1 | §2 S2 | A malformed or unresolvable `base:` still exempts a build silently, and after S1 it is the only skip left. |
| H3 | high | 1 | §2 S4, §6 AC5, §7 | The ceiling that binds the merge bar is `gate-legs.json`'s 900; the spec re-declares the runner's 90. |
| H4 | high | 1 | §8 F1, §2 S6, §6 AC6 | "Removes the lever entirely" contradicts the parent build's M1 — the run still authors the committed value. |
| H5 | high | 1 | §2 S2, §4 The range | Nothing says whether the anchor commit is inside the range, and the reused walk excludes it. |
| H6 | high | 3 | §2 S2 and S3, §4, §7 | The receiver is a caller-supplied slice list of unknown length, which `agent-cap` denies at the tool call. |
| H7 | high | 3 | §4 Why the fan is permitted, §2 S4 | Nothing says whether the writers commit; M6 says they must, and the ratified record says that race is untested. |
| H8 | high | 3 | §2 S5, §6 AC4 | After the merge, an all-dead spec stage returns a truthy object and the stage's own refusal never fires. |
| H9 | high | 4 | §2 S2 against §6 | No acceptance criterion reads the passes paragraph, so half the unit's content edit is unobserved. |
| H10 | high | 4 | §6 AC4, second clause | "No second spelling of the four unit states" is false in the tree today, and the literal reading is destructive. |
| M1 | medium | 2 | §2 S5, §6 AC6 | The honesty header enumerates one verb twice and omits the `--review` recording it actually drops. |
| M2 | medium | 2 | §2 (no scope item) | `GROUND` tells every spawned agent it is under a mandate, in both modes, and nothing in scope changes it. |
| M3 | medium | 4 | §6 AC3, §7 | The bare `check-template-size.sh` measures the template; `AGENTS.md` is the separate `charter size` leg. |

---

### B1 — the charter sentence that is not there

**Unit 4** · `§2 S5`, `§6 AC3` and `AC6`, `§8 F2`

`grep -inE 'pass.?order|check-pass-order|predates|built before|spec-before-build'` over `AGENTS.md`
and `coding-governance-agents.template.md` returns nothing, and no near-spelling exists either. The
only prose description of the leg in the tree is the byte-compared pair
`memory/guides/UNATTENDED-PROTOCOL.md:469` / `tools/unattended/PROTOCOL.template.md:469`, which §3's
third non-goal explicitly refuses to touch, plus the checker's own header, which unit 1 S1 removes.

Three separate things fall over. S5's "the charter's DESCRIPTION of the pass-order leg is deleted"
has no subject. AC3's "the charter's byte count after this unit is LOWER than before it, because S5
deletes more than it adds" is unachievable, because with nothing to delete the pointer plus
instruction can only add. AC6's "carries no description of what the pass-order leg checks" is
satisfied by the tree as it stands, so it cannot distinguish a landed unit from an unlanded one.

It is worse than vacuous. `AGENTS.md` is 64506 bytes against the 64512 declared for it in
`tools/template-size-limits.txt` — six bytes of headroom. An honest implementation adds a pointer,
a command and a binding boundary, and reds the `charter size` leg outright. The dishonest one edits
nothing and passes every criterion.

F2's premise, "the pass-order leg is already described there in terms that will be wrong after unit
1, so leaving it is not an option", is false, and the owner ruled against the spec's own
recommendation on it.

**Fix.** Either re-point S5 at the carrier that actually holds the description — naming the file and
line — or withdraw the deletion and restate S5 as a pure addition. If it becomes an addition, AC3's
LOWER clause is dropped and replaced by a bounded-growth criterion priced against the `AGENTS.md
64512` row, with the six-byte headroom named in §5 as the risk it is. AC6 is rewritten to grade the
file it names. Re-put F2 to the owner with the corrected premise either way.

**Left-shift.** A spec-lint arm (G1, below): a scope item asserting that something EXISTS in the tree
carries a backticked witness command, and the linter fails when that command's current output is
empty. This defect is exactly "a spec asserted the tree said something and nobody ran the grep", and
one grep at rev time would have caught it three times over.

---

### B2 — the helper that is not in the file

**Unit 3** · `§2 S2`, `§4 Files touched`, `§10 Reuse audit`

`grep -n boundedParallel tools/workflows/unattended-build.js` returns nothing. The helper is inlined
at `tools/workflows/tier2-review.js:17`, a different script, with its own `// gov:bounded-fanout`
marker at :20; the other copies are in the two drift-audit workflows. `unattended-build.js` contains
no `boundedParallel`, no `Promise.all` and no fan at all — its four `agent(` calls at lines 230, 294,
388 and 485 are single awaited calls, and its header says so at length ("DISPATCH IS STRICTLY
SEQUENTIAL", "EACH STAGE IS ONE AGENT").

So S2's "the `boundedParallel` helper already inlined at the top of the file", "at its existing cap"
and "reused rather than re-spelled, because `check-verifier-fanout.sh` already grades that shape" are
all false about the file this unit edits, and §10 states the same false seam as the RESULT of the
reuse probe — the one section whose entire job is to have been checked against source. The unit's
§10 obligation is discharged by a claim that does not hold.

The consequence is unscoped work, not a wording nit. The helper and a cap constant must be inlined
afresh, which changes the file's `agent-cap` posture, puts a second copy of a constant `tier2-review.js`
owns into a second file, and gives `check-verifier-fanout.sh` — which grades every workflow `.js` — a
new shape to grade. The file's own header records that `agent-cap` denied every earlier fan-shaped
draft there, which is precisely why no helper was ever inlined.

**Fix.** S2 states that the fan INTRODUCES a bounded receiver: `boundedParallel` is inlined into
`unattended-build.js` as a new marked copy of the `tier2-review.js` one, the cap literal it carries is
named, and the spec says which file owns that number and how the two copies stay in agreement. Add
`tools/workflows/tier2-review.js` to §4 as the copy source. Correct §10 to say the seam is in a
sibling harness rather than in this file.

**Left-shift.** Same G1 arm as B1, and it is the same class: a §10 reuse audit that names a symbol in
a file is a claim, so the linter greps the named symbol in the named file. A reuse audit nobody can
falsify is a section that certifies itself.

---

### B3 — the anchor that exempts the worst case

**Unit 1** · `§2 S2`, `§6 AC1`, `§8 F2`

Anchoring the derived range at the build folder's own first commit makes the flagrant violation
structurally invisible. A commit that writes product code naming a unit id touches nothing under
`memory/builds/<slug>/`, so it is strictly earlier than "the earliest commit touching that folder"
and sits outside the derived range however inclusivity is settled (see H5). The unit is then graded,
no build commit is found inside the range, and it lands in `unbuilt-in-range`.

That count is the one `check-pass-order.sh`'s own liveness block warns about in writing: "DO NOT READ
A NON-ZERO `unbuilt` AS BENIGN … no build commit is found, and the leg reports a clean bill with a
count a reader has been taught to ignore." The build exists to make "a unit built before its spec
reds the bar on any build" true, and the derived range exempts code-first-spec-later — the most
flagrant instance of exactly that. The unattended population does not have this hole, because its
base is pinned before the run starts.

Both of F2's options share the hole, and neither the fork text nor the design section discloses it,
which the charter's own "a gate's header states what it does NOT check" rule requires. AC1's fixture
does not pin its build commit relative to the derived range, so it can pass without touching the
question.

**Fix.** Add a scope item: for a run-state-free build, a CLOSED unit whose build commit is not found
inside the derived range is a REFUSAL, not an `unbuilt-in-range` tally — or the range has no lower
bound for that population. Add an acceptance criterion observing a fixture whose product commit
precedes the build folder's first commit and asserting RED. Re-put F2 to the owner with this residual
stated in both options, and write the residual into the leg's header whichever way it goes.

**Left-shift.** An arm in the leg's own self-test with that fixture, asserting RED — and, more
generally, a rule that every `unbuilt-in-range` increment in the widened population is accompanied by
a named reason, so the tally cannot absorb a class the leg was built to red.

---

### B4 — the two verbs that refuse in attended mode

**Unit 2** · `§4 The mode boundary`, `§2 S2` and `S5`

§4 counts three driver call sites; the prompts name four driver invocations. Beyond `--review`
(:391) and `--dispatch` (:493), the BUILD prompt instructs the agent to run `--brief` (:495) for
every unit and, on a non-CLEAN verdict, `--rescope` (:480). Both hard-refuse without a run-state
file: `verb_brief` fails 49 at `tools/unattended/unattended.sh:4184` ("no run-state file, so there is
no run to record a brief against") and `verb_rescope` fails 48 at :4481, exactly as `verb_dispatch`
does at :4584.

Attended mode as scoped drops only the `--review` recording and the `--dispatch` order refusal. The
BUILD prompt still tells the agent to run `--dispatch` and `--brief` per unit, and adds "a refusal is
this harness telling you the order is wrong. Read it and stop — do not work around it." In attended
mode that refusal is caused by the mode itself, so the build stage stops at unit one, after units are
already being written. That is a strictly worse failure than the refusal the mode was meant to trade
away, and it means the unit does not achieve its stated goal. M4's PROMOTE disposition is also
unavailable, leaving the method with one of its two admitted routes.

The driver already ships an attended records-root path for `record_set`/`record_piece`
(`unattended.sh:4418`, :4449) and none for `--brief`, so the two cannot be disposed of the same way.

**Fix.** Put the BUILD prompt text under the mode branch: in attended mode the `--dispatch`, `--brief`
and `--rescope` instructions are removed or replaced with their records-root equivalents, and the
spec says which. Enumerate ALL driver invocations reached from the prompts in §4 rather than counting
call sites, note that one of the three §4 counts is the caller's `--plan` and not this script's, and
name what attended mode does with M4's PROMOTE disposal.

**Left-shift.** G4: a check that cross-references every driver verb named in a harness prompt against
the verbs `unattended.sh` refuses without a run-state file, per declared mode, and reds when a mode's
prompt names a verb that mode cannot run. It is two greps and a set difference, and it is the only
thing that keeps a mode split honest as the driver grows verbs.

---

### H1 — the liveness line already prints four

**Unit 1** · `§2 S3`, `§6 AC3`

`check-pass-order.sh:262` prints four counts, not three: `graded`, `skipped_cutoff`, `skipped_norun`
("with no pinned run BASE") and `unbuilt`. Only the block comment above it at :246 says "THREE
COUNTS", and S3 copied the stale comment rather than the line.

So S3's inventory is factually wrong about its own subject, and AC3's arithmetic is off by one. A
correct implementation — add a run-state-free-graded count, keep `skipped_norun` for the skips that
remain — yields five, which AC3's "four counts … and none of the four is absent" rejects; an
implementer satisfying AC3 literally drops `skipped_norun`, which the leg's own doctrine ("COUNTED
and announced, never silently skipped") forbids. Either way the builder invents the disposition and
AC3 grades the invention. And AC3 as written is satisfied by the unmodified script, so the one
criterion covering the widening's observability cannot fail.

**Fix.** Correct S3 to name the four counts that exist, state the post-change set explicitly, and say
what becomes of `skipped_norun` — repurposed as the run-state-free-graded count, or retained for the
residual skips of H2. AC3 asserts the specific new count by name with a non-zero value on the real
tree, not a cardinality. Fix the ":246 THREE COUNTS" comment in the same commit.

**Left-shift.** A self-test arm asserting that every counter variable incremented in the script
appears in the liveness `echo`, and that the count of `$` fields in that echo matches the number the
comment above it claims. A comment that miscounts the line it introduces is what produced this
finding.

---

### H2 — the `base:` lever left standing

**Unit 1** · `§2 S2`

Three paths increment `skipped_norun`: the missing `RUN.md` at :160, a `base:` line that is not
hex-shaped at :162, and a base that `git cat-file -e "$base^{commit}"` cannot resolve at :163. S1/S2
widen only the first. After this unit the `opened:` lever is closed (S6) and the `base:` lever is the
last one standing: a run that commits a malformed or unresolvable base exempts its own build from the
leg, silently, in a bucket the liveness line teaches readers to skim. A build with a garbage `RUN.md`
becomes more exempt than a build with none.

That is the same shape S6 spends an object read to remove, left open in the same file, and no
non-goal covers it while the unit's goal claims the leg will red "on any build". The folder-derived
range S2 is already building is the obvious fallback and the spec does not reach for it.

**Fix.** S2 states that a build whose `RUN.md` yields no usable base falls back to the folder anchor
rather than being skipped. If the skip is deliberate, it becomes its own named count and the line
says which of the reasons applied. Either way an arm covers a `RUN.md` carrying a garbage `base:`.

**Left-shift.** That arm, plus the rule generalised: every skip path in a merge-bar leg is reachable
from a fixture in its self-test, and a skip with no fixture is a skip nobody has seen.

---

### H3 — the ceiling with two carriers

**Unit 1** · `§2 S4`, `§6 AC5`, `§7`

The leg has two declared ceilings. `tools/gate-legs.json` gives `pass-order history` `"ceiling": 900`
with `"guard": []`, so it runs on every bar; `tools/unattended/run-unattended-gates.sh:71` still holds
`BUDGET_pass_order_history=90` under the comment "Matches the ceiling its gate-legs.json row declares
— one figure, two readers", which the tree has made false (90 → 300 in `8889b403`, 300 → 900 in
`42b9c18b`).

S4 and AC5 move only the runner's value, and `gate-legs.json` is absent from §4's Files-touched list.
The 900 is the ceiling that fires at the merge bar, which is where this leg's verdict matters, and
AC5 measures the on-demand kit runner instead. The premise driving S4 and the Alternatives-rejected
paragraph — "already over its declared ceiling", 134 s against 90 — is true only of the runner; 134 s
is comfortably inside 900. Meanwhile the population widens from the 38 builds carrying `RUN.md` to all
92 build folders, and a breach of 900 would red the bar with no criterion having looked at it, while
§5 calls perf "the binding concern" and names S4 alone.

`TOOL-dSealedTally-2` is stale the same way on its sibling half: `BUDGET_kit_gate` is 240 after
`TOOL-aCollapsedScan-4`, not the 120 it cites.

**Fix.** S4 names both carriers, states which binds where, re-measures against both, and either
restores the parity or deletes the "one figure, two readers" comment it invalidates. AC5 asserts the
two declarations agree after the edit, or a second AC covers the manifest row. Restate §2's premise
against 900.

**Left-shift.** G3: a parity check asserting every `BUDGET_*` in `run-unattended-gates.sh` equals its
`gate-legs.json` row's ceiling, in the shape `check-playbook-parity.sh` already uses for its five
values. A comment claiming two readers share one figure is a claim, so gate it or delete it.

---

### H4 — `opened:` narrowed, not removed

**Unit 1** · `§8 F1`, `§2 S6`, `§6 AC6`

F1's "it removes the lever entirely" contradicts the recorded finding it cites. The parent build's
closing review M1
(`memory/builds/dBriefedPass/reviews/2026-09-01-review-…-closing-diff-round1.md:166-180`) names the
class as "the grading cutoff is read from a field the graded run authors", states that "the doctored
value survives into a clean clone", and prescribes a git-derived date
(`git log --diff-filter=A -1 --format=%cs -- "$readme"`) or a red on disagreement — not a committed
read.

Reading `opened:` from the graded commit closes the working-tree edit and nothing else. The run
commits the README, so the committed value is still the run's to choose, and this unit multiplies the
population that field governs. AC6 observes only the working-tree bypass, so the unit lands reporting
a lever removed that the prior record says is still there.

**Fix.** Restate S6 and F1 as a NARROWING, cite M1's actual finding and its recommended git-derived
date, and either adopt that date (or the disagreement-red) or record in §5 and in the script header
why the committed authored value is accepted. Add an AC covering a build whose COMMITTED `opened:` is
back-dated.

**Left-shift.** An arm with a back-dated committed `opened:`; and, if the git-derived date is adopted,
a red on disagreement, which is the version that cannot be argued with later.

---

### H5 — the anchor's own commit

**Unit 1** · `§2 S2`, `§4 The range, for a build with no pinned base`

Neither S2 nor §4 says whether the anchor commit is inside the range. The walk being reused is
`git rev-list --reverse "$base..HEAD"` at :206, which excludes its anchor, so the build folder's own
first commit is dropped unless the implementer silently converts to `anchor^..HEAD` — and a root
commit has no parent to convert to.

A commit that creates the build folder and writes product code for a unit in one go is precisely the
violation this widening exists to catch, with the spec added afterwards, and it lands in
`unbuilt-in-range` and reports clean. That is B3's hole one commit later, at the first commit of the
newly added population. Inclusivity at a gate boundary is not a style detail and nothing in the spec
or the ACs pins it.

**Fix.** S2 states the range is inclusive of the folder's first commit — anchor at `<first>^`, or walk
`HEAD -- <build dir>` and take the boundary in — notes the root-commit case, and S5 adds an arm whose
violating commit IS the folder's first commit.

**Left-shift.** That arm. A range gate with no fixture on its own boundary is a range gate nobody has
tested at the only place ranges go wrong.

---

### H6 — the fan's receiver and its total

**Unit 3** · `§2 S2` and `S3`, `§4`, `§7`

S3 makes the fan receiver a caller-supplied grouping of `units` by the `order` verb, whose length
nothing bounds. `tools/hooks/README.md:53-60` and :94-96 admit an `agent(` fan only over a receiver
the hook can PROVE bounded: a `chunk(x, Math.ceil(x.length / K))` or `splitInto(x, K)` split with a
resolvable K under a `gov:fixed-verifiers` marker, an array LITERAL it can count, or an identifier
already proven bounded — "a branch it cannot delimit never qualifies". `tier2-review.js:397` shows the
sanctioned spelling the spec does not adopt.

§4 argues disjointness at length and never argues the bounded receiver, while §7 names the hook as a
gate, so the shape as specified is denied at the tool call. AC1 compounds it by tying the agent count
to the caller's slice count ("three slices, three writer agents"): that bounds concurrency and leaves
the TOTAL unbounded, which is the second of the two rules §8 insists are not one rule.

**Fix.** Write the marker and the chunking into S2 as the shape to be BUILT, naming the grammar in
`tools/hooks/README.md` it must satisfy, and state the total-agent bound the caller's grouping must
respect alongside the concurrency cap. Widen AC5 to observe `agent-cap.js`'s verdict on the changed
file rather than exit 0 on two workflow checks.

**Left-shift.** Make that AC5 widening permanent: `check-verifier-fanout.sh` already grades every
workflow `.js` on the bar, so the criterion is a delegation, not a new gate. The left-shift is that a
spec proposing a fan names its marker spelling at spec time, which G1 can enforce by requiring the
marker string to appear in the scope item.

---

### H7 — the writers that commit

**Unit 3** · `§4 Why the fan is permitted`, `§2 S4`

Clause 3, "no writer touches a shared mutable record", is contradicted by the procedure every writer
is bound by. `GROUND` (`unattended-build.js:220-224`) tells each stage agent to read
`memory/guides/BUILD-METHOD.md` WHOLE, and M6 makes "a spec authored" a pass and orders "Commit at the
end of every pass". So N concurrent writers each commit in one worktree, contending on one git index.
Worse for clause 3 specifically: M6 names `memory/backlog/*.md` as a shared mutable record, and the
spec template mandates a backlog row per spec — recorded at `check-pass-order.sh:193-196` as the reason
a conforming spec commit writes it — so the writers contend on a record clause 3 enumerates by name.
The spec's proof covers spec file paths and the generated index (S4) and never the commit.

This is the recorded experiment E4, "each pass can commit at its own end without the two commits
racing one index"
(`memory/builds/cBriefedPilot/build/2026-08-15-build-TOOL-cBriefedPilot-15-2-parallelism-routes.md:25`).
R2, the Workflow-sidechain route S2 proposes, is recorded at :76 as failing E3 and E4;
`TOOL-cBriefedPilot-21` ratified "parallelism route: none"; `TOOL-cBriefedPilot-28` is open because E3
and E4 were never actually run. Both ids sit in the header of the very file this unit edits
(`unattended-build.js:34-38`) and neither appears anywhere in the spec or its §10 recall. Unit 1's
widened leg grades on commit order, so a botched interleaving is now a merge-bar red rather than a
nuisance.

**Fix.** Add a scope item stating that spec writers AUTHOR and never commit, with the caller
committing once after the fan alongside the single index regeneration S4 already gives it — or run E4
and record the result before clause 3 claims it. Add a paragraph distinguishing this stage from
`TOOL-cBriefedPilot-21`'s ratified verdict by name, so the two records do not read as contradicted.

**Left-shift.** A recall arm in the spec lint: a spec proposing parallelism in a file whose header
cites a ratified `parallelism route` decision must name that decision id. Cheap, and it is the exact
miss here — the record was in the file being edited.

---

### H8 — the refusal that stops firing

**Unit 3** · `§2 S5`, `§6 AC4`

`if (!specced) throw` at `unattended-build.js:242` fires only on a falsy return. S5's merged
per-slice object is always truthy, and AC4 requires a dead slice's units to be reported while the
other slices return, so after this unit a spec stage in which EVERY writer died presents as a clean
object with empty arrays. The refusal the file spends six lines justifying — "continuing would put
the BUILD stage on a spec set nothing confirmed exists" — becomes unreachable, and nothing downstream
gates on `specRefused` (logged at :249, carried in the return, never checked).

The empty-subject net at :309 does not reliably catch it either: :292 takes a caller-supplied
`a.subjects` and skips the resolver entirely, which the test fixture itself does. So a totally dead
spec stage can reach AUDIT and BUILD on pre-existing specs.

**Fix.** S5 states that the merge REFUSES when every slice returns nothing — a null or empty merge is
a throw, not an empty result. AC4 gains a second arm: all slices dead must throw; one slice dead must
return with those units in `refused`.

**Left-shift.** A self-test arm per failure mode, which is the general rule this misses: a refusal
whose trigger condition is changed by a diff gets an arm in the same diff, or the diff has deleted a
guard without saying so.

---

### H9 — the scope item with no criterion

**Unit 4** · `§2 S2` against `§6`

S2 requires the passes paragraph of `BUILD-METHOD.md` to name the harness and its two modes, and not
one of AC1–AC6 observes that paragraph. AC4 reads only the detect paragraph; AC1, AC2, AC3 and AC5 are
gate invocations that pass whether or not S2 was written; AC6 reads the charter.

The asymmetry is the tell: this is a documentation-only unit whose entire product is text, and the
spec's own convention for observing text is an AC that reads the paragraph — AC4 and AC6 both do
exactly that for other paragraphs. S2 is the one deliverable with no observation of any kind, and it
is the half the build's goal rests on. Unit 4 lands last and is the only carrier unit, so the attended
route ships undocumented with a green bar. Non-goal 2 excludes restating mode SEMANTICS, not naming
the route, so nothing withholds the criterion deliberately.

**Fix.** Add an AC in AC4's shape: "When the passes paragraph of `memory/guides/BUILD-METHOD.md` is
read, it names `tools/workflows/unattended-build.js` and both mode values `attended` and
`unattended`." Pin the exact spelling of the two tokens so a paraphrase cannot satisfy it.

**Left-shift.** G2: a spec-lint arm asserting every `S<n>` in §2 is named by at least one criterion in
§6. It is a two-column set difference over the section the template already mandates, and it would
have caught this, M1 and part of M3 in one pass.

---

### H10 — the criterion that is false today

**Unit 4** · `§6 AC4`, second clause

"The guide contains no second spelling of the four unit states" is false in the current tree:
`memory/guides/BUILD-METHOD.md:41-46` spells MISSING, THIN, FORKED and READY under "**Classify, first
match wins**", with precedence, and repeats them in M2's Act paragraph and the M1 loop line. §3's
non-goal ("not restating the classifier's grades") is written as if already satisfied, and it is not.

So AC4 either cannot pass without deleting M2's Classify block — which no scope item covers, and which
is the method's own act rule — or it silently means "this unit adds none". An acceptance criterion
with a destructive literal reading is a defect in the criterion, not a matter of interpretation.

**Fix.** Scope AC4 to what this unit adds ("this unit introduces no second spelling"), or put the
deletion of M2's Classify list in §2 with an explicit statement of what M2 keeps and where a reader is
sent for the grades.

**Left-shift.** The same G1 witness rule, in its negative form: a criterion asserting that a file
contains NO instance of something carries the grep that proves it, and the linter runs it at rev time.
A negative claim nobody ran is the cheapest kind of false one.

---

### M1 — the header that miscounts its losses

**Unit 2** · `§2 S5`, `§6 AC6`

S5 names the pair as "the `--dispatch` refusal and the write-set recording", which are two properties
of ONE verb (`unattended-build.js:493`), while the `--review` round recording S2 actually drops (:391)
is absent from the list; B4's `--brief` and `--rescope` losses are missing too. AC6 then grades the
header against that same list and calls all of it "refusals", though a recording is not one. The spec
knows the round record is lost — F2 resolves what replaces it — yet the artefact §5 relies on to stop
a reader treating the modes as equivalent would not say so. The miscount is landed and certified in
one pass.

**Fix.** Name the losses separately in S5 and AC6: the `--review` round record, `--dispatch`'s order
refusal, `--dispatch`'s write-set record, and whatever B4 settles for `--brief` and `--rescope`.

**Left-shift.** G4 again: derive the header's list from the driver-verb inventory rather than typing
it, and the count cannot drift from the verbs the prompts name.

---

### M2 — the preamble that still claims a mandate

**Unit 2** · `§2`, no scope item

`GROUND` (`unattended-build.js:220-224`) hard-codes "You are one stage of a harnessed unattended
build" and "Speak only in your return value: nobody reads a transcript under a mandate", and it
prefixes EVERY agent this file spawns in both stages. No scope item touches it: S5 is scoped to the
file's own comment header, and §5 answers the two-modes risk with S5 alone.

A builder implementing S1–S7 literally ships a harness that tells every attended-mode agent it holds a
mandate — which in this repo is precisely the authority to merge and push with no owner turn. The unit
creates the falsehood and covers nothing that removes it. §5 names "a reader treating the two modes as
equivalent" as the real risk and then fixes only the human-facing comment; the text the agents
actually read stays false.

**Fix.** Add a scope item making `GROUND` mode-aware, and an AC observing the attended wording in a
spawned prompt.

**Left-shift.** A grep arm over the composed attended-mode prompt for the mandate vocabulary
(`mandate`, `unattended`), red on a hit. One line, and it covers every future prompt edit.

---

### M3 — the gate that measures the other file

**Unit 4** · `§6 AC3`, `§7`, against `§4 Files touched`

The bare `bash tools/check-template-size.sh` measures `coding-governance-agents.template.md` — its
default subject at `tools/check-template-size.sh:49`, `FILE=${1:-"$ROOT/coding-governance-agents.template.md"}`.
`AGENTS.md` is measured by a different leg: `charter size`, argv `check-template-size.sh AGENTS.md`,
against the 64512 row. §4 touches `AGENTS.md` and not the template, so AC3 and §7 run a gate over a
file this unit never edits: the exit-0 half grades an untouched file, and the byte-count half names a
subject the command did not measure.

This matters concretely rather than pedantically, because `AGENTS.md` sits at 64506 of 64512 — six
bytes — and B1 turns the edit into a net addition.

**Fix.** Name the `charter size` leg's argv in §7 and AC3, and say which of the two gated subjects
"the charter" means throughout the spec.

**Left-shift.** G1's variant for commands: a spec naming a gate invocation in §7 or an AC has that argv
matched against a row in `tools/gate-legs.json`, and an argv matching no row is a lint failure. It
would also have caught the wrong-subject half here, because the bare command IS a row — just not this
unit's.

---

## Left-shift summary — four candidate gates

Every finding above routes into one of four checks, none of which exists today. Ranked by how many of
these seventeen defects it would have caught before the owner ever read the specs.

- **G1 — the spec-claim probe.** A scope item, non-goal, §10 reuse audit or acceptance criterion that
  asserts the tree DOES or DOES NOT contain something carries a backticked witness command; the linter
  runs it at rev time and fails on an empty result (or a non-empty one, for the negative form). Would
  have caught B1, B2, H1, H10 and M3 — five defects including two blockers, and both of the owner
  rulings taken on a false premise.
- **G2 — the S↔AC coverage ratchet.** Every `S<n>` in §2 is named by at least one criterion in §6; a
  scope item with no observation is a lint failure. Would have caught H9 and M1.
- **G3 — the ceiling parity check.** Every `BUDGET_*` in `run-unattended-gates.sh` equals its
  `gate-legs.json` row's ceiling, in the shape `check-playbook-parity.sh` already uses. Would have
  caught H3, and would catch the stale `TOOL-dSealedTally-2` half it turned up.
- **G4 — the driver-verb-per-mode inventory.** Every driver verb named in a harness prompt is checked
  against the verbs the driver refuses without a run-state file, per declared mode. Would have caught
  B4 and M1.

The remainder — B3, H2, H4, H5, H7, H8 — left-shift into arms in the two self-test suites the units
already touch, and are named in their own sections. They share one rule worth stating once: a skip
path, a range boundary or a refusal whose trigger a diff changes gets a fixture in the same diff.
