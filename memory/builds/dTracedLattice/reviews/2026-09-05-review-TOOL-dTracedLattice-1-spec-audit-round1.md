**Serves:** spec-audit TOOL-dTracedLattice-1 TOOL-dTracedLattice-2 TOOL-dTracedLattice-3 TOOL-dTracedLattice-4 TOOL-dTracedLattice-5

# dTracedLattice — spec audit of the five-unit set, round 1

*Node `d`, 2026-09-05. A Tier-2 adversarial pass over the five specs AND over the design dossier they
were folded from — a fold nothing had reviewed, which is this repo's own `fold-text-is-unreviewed-surface`
class. A primed finder fan, a skeptic stage prompted to REFUTE each finding, one synthesis. Every claim
any surviving finding makes about the tree was re-checked against source at `c4fcf5ad` before it was
written down here; where a sub-claim did not survive that re-check it is named inside the finding that
carried it.*

**Round: 1.** Subjects, each pinned at the blob it was read at:

- `memory/builds/dTracedLattice/spec/2026-09-05-spec-TOOL-dTracedLattice-1.md@4bafdbaa2753583beeae5c8746c8920f37bcb0fd`
- `memory/builds/dTracedLattice/spec/2026-09-05-spec-TOOL-dTracedLattice-2.md@b96182420ffc0cfb1d13e2092c01941faca59714`
- `memory/builds/dTracedLattice/spec/2026-09-05-spec-TOOL-dTracedLattice-3.md@53f6c06f091c6d923a87cd456455859fbd27ded9`
- `memory/builds/dTracedLattice/spec/2026-09-05-spec-TOOL-dTracedLattice-4.md@a58e89aea45996e62ad378ce47c3e0ae95aaa89c`
- `memory/builds/dTracedLattice/spec/2026-09-05-spec-TOOL-dTracedLattice-5.md@de0be89b1c84f32097ed02d1c5788f9767667d8f`

## Verdict: BLOCKED

Three blockers stand, and they are independent of each other. The build README licenses concurrent
dispatch on a disjointness claim that is false in three separate places, one of which is a shared
mutable backlog row that `memory/guides/BUILD-METHOD.md` M6 clause 3 forbids two passes to touch at all.
Unit 1's two headline acceptance criteria are scored by an instrument that no scope item builds and the
tree does not contain. Unit 5's resolved §8 question and three of its four acceptance criteria cannot
all hold on this repo's own tree, because the resolution picks a vocabulary the shipped conf value is
not written in.

The design answer itself is not in dispute. Rev-2's "commit nothing, on `AGENTS.md` §12 grounds" is
sound, its refutation record is honest about what rev-1 got wrong, and none of the findings below asks
for it to be revisited. What is wrong is downstream: the five units the dossier commissioned quote it
accurately and then specify less than they promise.

## Review shape

Raw 63, confirmed 14, refuted 49, unverified 0, precision 0.22. The 14 confirmed findings collapse to
13 distinct defects — only one pair folded, both lenses having landed on the same false independence
claim from opposite ends.

Precision at 0.22 is less than half the ~0.5 floor `AGENTS.md` §8 sets for adding agents rather than
tightening scope, and the failure mode is legible in the refuted set: lenses reading spec prose for
rule-conformance produced almost all of the 49 refutations, while lenses instructed to check a spec's
claim against source produced almost all of the 14 that survived. A document set is a target where a
finder can always manufacture a plausible-sounding complaint, so on the next pass over specs the
priming should require a `file:line` from the tree in every finding, not merely a section address in
the spec. That single constraint would have killed most of the 49 before a skeptic was spent on them.

Two coverage notes, so a green row here is not misread. The dossier itself was read in full and is the
source of several findings below, but its measured figures were NOT independently re-derived — the
precision table, the 1.761 s / 0.595 s medians and the 127-row / 329-edge ground truth are taken as the
dossier reports them, and B2 is precisely about the fact that nothing in the tree lets a builder check
them. And no finding here re-opens the relations question; the pass took the README's rule at its word
and audited the five units instead.

| Defect | Raw ids folded in |
|---|---|
| B1 the write sets intersect | 18, 59 |
| B2 the instrument that is not there | 20 |
| B3 three vocabularies for one layer | 41 |
| H1 `fan_in`'s four call sites | 39 |
| H2 the class AC over a population of one | 7 |
| H3 the AC that resolves the owner's fork | 10 |
| H4 the README claim three tracked files falsify | 58 |
| H5 the fork that was already decided | 57 |
| H6 the follow-up that is already filed | 56 |
| H7 the seam threshold's silent rescaling | 43 |
| H8 the landed sibling nobody cited | 50 |
| M1 the template twin | 9 |
| M2 the gate list that cannot fire | 30 |

## Findings

| # | Severity | Unit | Address | One line |
|---|---|---|---|---|
| B1 | blocker | README, 1, 3 | Build-level rules bullet 4, against `gen:build-order` | The declared write sets intersect in three places, one of them a shared mutable backlog row M6 clause 3 names outright. |
| B2 | blocker | 1 | §6 AC1 and AC2, against §2 and §10 | The precision harness and AST resolver that score both headline ACs are scratchpad-only; no scope item lands them. |
| B3 | blocker | 5 | §8 Q1, against §4, AC2, AC3, AC4 | Registry keys, extensions and language names are three vocabularies, and Q1 picks one the shipped conf value is not in. |
| H1 | high | 1 | §4 Data model | `fan_in` has four call sites in three files; §4 says "the caller", and `detect_collisions` cannot supply the head definer set. |
| H2 | high | 2 | §6 AC4, against §4 | The class criterion enumerates a population of one — the very tier AC1 already fixes — so it cannot fail. |
| H3 | high | 3 | §6 AC1, against §8 Q1 | AC1 is satisfiable only under one branch of a fork §8 marks NOT RESOLVED and reserves to the owner. |
| H4 | high | 3 | §2 S4 and §6 AC5 | The claim the kit README would carry is falsified by a tracked runbook, a rendered agent doc and a gate leg. |
| H5 | high | 3 | §8 Q1 | The fork was posed and decided as `bConvergentLodestar` F7 and BUILT; neither spec nor dossier names it. |
| H6 | high | 1 | §8 Q1 | The follow-up Q1 invents already exists as `TOOL-aScouredKit-17`, which says it should land with the row unit 1 amends. |
| H7 | high | 1 | §2 S1 and §4 | Definer subtraction rescales `SEAM_FANIN_THRESHOLD` for three consumers; 71 of 165 seams are already measured to fall out, and no unit owns it. |
| H8 | high | 5 | §4 Alternatives rejected, §10 | The lexicon kit already ships this design, built from this very decision, and the reuse audit does not name it. |
| M1 | medium | 2 | §8 Q1, against §2 and §6 | Q1 requires the template twin to change in the same commit; no scope item names it and no gate compares the pair. |
| M2 | medium | 4 | §7, against §4 | §7 names a leg whose guard this unit's write set never touches, and omits the leg whose subject is the adopter. |

---

### B1 — blocker — build README "Build-level rules" bullet 4, against the `gen:build-order` block and units 1 and 3

**The defect.** The bullet reads: "Units 2 to 5 are independent of unit 1 and of each other. Their write
sets do not intersect, so M6 clause 1 is satisfied and they may run concurrently. Unit 1 touches
`map_lib.py` and `reuse_lookup.py`; unit 2 the gate; unit 3 `map_diff.py`; unit 4 the adopter; unit 5 the
conf reader." Three of those clauses are false against the tree, and the two M6 clauses the bullet does
not cite are the ones that actually fail.

1. **Unit 1 must write `tools/codebase-map/map_diff.py`, which the bullet assigns to unit 3.**
   `map_diff.py:204` is `dead = sum(1 for r in head_rows if m.fan_in(ref_index, r["id"], r["file"]) == 0)`
   — the exact signature unit 1 S1 changes, passing a `str` where the new design takes a definer set. It
   is not optional: unit 1 §8 Q1 and §5 claim S1 grows the fan-in-0 population from 451 to 532, and that
   population is computed at this one line, so it cannot move unless this call site is edited. Q1's own
   resolution ("this unit REPORTS the new figure beside the old") is an edit to `map_diff.py:207`.
2. **Unit 1 and unit 5 both write `tools/codebase-map/reuse_lookup.py`.** Unit 1 AC3 rewrites its output
   banner to name bound and unresolved attribute sites and every unscanned layer; unit 5 S4 rewrites the
   same banner to report the derived dark set. The "conf reader" the bullet hands unit 5 IS
   `reuse_lookup.py` — `RECALL_DARK_LAYERS` has exactly one consumer, `reuse_lookup.py:172`, which unit
   5's own §10 states.
3. **Unit 1 and unit 3 both edit the same ROW of `memory/backlog/TOOL.md`.** Unit 1 S5/AC6 amends
   `TOOL-aScouredKit-16` with the measurement rejecting its second proposal; unit 3 S3/AC4 corrects the
   same row's three false clauses. M6 clause 3 names `memory/backlog/*.md` explicitly as a shared mutable
   record two passes may not touch together — so this pair is forbidden concurrency regardless of whether
   the rows overlap, and here they are the same row and the same sentence.

The bullet cites clause 1 only. Clause 2 (neither writes a file the other reads as a contract or an
acceptance input) and clause 3 (shared mutable records) are the ones that fail. And the README
contradicts itself: the generated `gen:build-order` block directly beneath sequences all five units with
Parallel `no`, so a run reading this file gets two answers to one question and the prose one is the
dangerous answer.

Severity is blocker rather than high because the consequence is not a wrong document, it is a wrong
dispatch. Run under the licence the bullet grants, two passes collide on one backlog row and on
`map_diff.py`; run sequentially per the generated block, the second amendment silently rewrites text the
first added, because neither spec tells its builder the other is editing the same sentence.

**Fix.** Rewrite the bullet to the actual write sets — unit 1: `map_lib.py`, `reuse_lookup.py`,
`map_diff.py`, `memory/backlog/TOOL.md`; unit 3: `map_diff.py`, `memory/backlog/TOOL.md`,
`tools/codebase-map/README.md`; unit 5: `reuse_lookup.py`, `map_extractors.py` — and state that clauses 2
and 3 are what govern, not clause 1. Then remove the collisions rather than documenting them: move the
whole `TOOL-aScouredKit-16` amendment into exactly ONE unit (unit 1 is the natural home, since it owns
the measurement that rejects the row's second proposal), give the `reuse_lookup` banner to exactly one
unit and make the other's AC read "the banner already carries the derived set", and declare `map_diff.py`
inside unit 1's scope. Whatever survives sequences explicitly, and the prose says so in the same words as
the generated block.

**Left-shift.** A `gen_build_index.py` check, because both halves of this are already in one file it
already parses: a README whose prose asserts units "may run concurrently" while the generated
`gen:build-order` block sequences those same units with Parallel `no` is a self-contradiction a machine
can see, and it should red. The harder half — deriving each unit's write set from its §2 and §4 and
intersecting them — is a spec-audit checklist entry until someone builds it: *a build claiming
disjointness writes both path lists down and the audit intersects them*, which is what M6 already demands
("If you cannot write both path lists down, the work is not known to be disjoint") and what no gate
currently reads.

---

### B2 — blocker — unit 1 §6 AC1 and AC2, against §2 and §10

**The defect.** AC1 and AC2 are scored "against the AST resolver" by "the precision harness", over "the
same 127 rows and 329 edges". Neither instrument exists in this repository. `git ls-files` matches no
precision harness, no variant runner and no AST import-edge resolver under any spelling; the dossier's
own §3 says the scoring came from `python variants.py`, a scratchpad script, and §8 concedes that the
resolver "binds only same-directory sibling imports and resolves 554 of 9666 attribute sites". No §2
scope item creates or vendors either one. No path names them. §5's testing row lands arms in
`tools/codebase-map/selftest.py` and nothing else.

So the unit's two headline criteria — 33.8% precision at 82.9% recall, 0.46 mean absolute error, each
against a shipped baseline — can be evaluated by nothing the unit builds and nothing the tree holds. A
builder reaching the Definition of Done has exactly three moves: assert the numbers (which is what §8
forbids), invent unspecified scope, or reconstruct a ~100-line prototype from a scratchpad that the
build's own README already says is unreproducible ("the churn producer is not on disk"). This is the same
class the README discloses for the churn figures, applied to the figures the whole unit is justified by,
and undisclosed.

One leg of the finding as first written does not survive and is recorded rather than dropped: the
scratchpad harness carries its own resolver, so §10's note that `tools/lexicon/lexicon.py`'s
`resolve_import` is SPECCED for deletion by `TOOL-aSurfacedLexicon-2` is not what makes the ACs
unevaluable. The deletion is a reason the prior art will not be available to borrow, not a reason the
criteria cannot be scored. The main claim stands without it.

**Fix.** Add a §2 scope item that lands the ground-truth resolver and the variant harness as tracked
files under `tools/codebase-map/`, name their paths in AC1 and AC2, and pin the ground-truth corpus
(the 127 rows and 329 edges) as a fixture rather than as a remembered number. If vendoring
`resolve_import` out of the lexicon kit before its deletion is the cheap route, say so and record it as
the rescue decision the build README currently parks. If the harness is deliberately NOT to be tracked,
then AC1 and AC2 must be restated as criteria something in the tree can observe — a selftest arm over a
fixture corpus with a known edge set is the obvious shape — and the 33.8% / 0.46 figures move into §4 as
the motivating measurement rather than standing as acceptance thresholds.

**Left-shift.** A `TEMPLATE-SPEC.md` rule with a mechanical check behind it: an acceptance criterion whose
verb is a measurement ("is scored", "is measured", "reports at most") must name a backticked path, and
hygiene check 15 then makes that path resolve against the tracked tree. Today check 15 catches a spec
that cites a dead path and says nothing about a spec that cites no path at all, which is strictly worse —
the criterion looks rigorous precisely because it names a number instead of an instrument.

---

### B3 — blocker — unit 5 §8 Q1, against §4, AC2, AC3 and AC4

**The defect.** Q1 resolves that "the layer name is whatever the extractor registry already keys on, so
the table is the registry and no second one is introduced; an extension no registry entry claims is
reported by extension". Three vocabularies are in play and that resolution does not reconcile them:

- `SYMBOL_EXTRACTORS` keys on `kit-py` and `kit-js` (`tools/codebase-map/map_extractors.py:222-228`),
  and those keys live in the PROJECT-owned extractors file, so each adopter authors its own.
- `symbols.json` rows carry `{id, kind, file}` and no layer tag at all, so nothing downstream can
  recover the registry key from the artifact.
- `.codebase-map.conf:27` declares `RECALL_DARK_LAYERS="bash"` — a language name, matching neither a
  registry key nor an extension. The kit's own fixture spells a third dialect again,
  `RECALL_DARK_LAYERS="web-ts"` at `tools/codebase-map/selftest.py:957`.

S2 compares derived-present against declared-dark and against the registered extractors. Under Q1's
resolution the derived uncovered layer on this tree is `.sh`, because no registry entry claims it. So:
AC4 demands the notice name `bash` and is unreachable without exactly the extension-to-language table Q1
forbids; AC2 says "the same layer is added to `RECALL_DARK_LAYERS`", which on this tree would mean adding
`.sh` to a key whose shipped value is `bash`; and AC1's refusal condition (`.sh` present, uncovered,
undeclared) and AC3's stale-declaration report (`bash` absent from the corpus entirely) both fire on
gov's own tree at the same moment — which directly contradicts §5's migration row, "this tree declares
`bash` dark today and would continue to; no data moves".

Blocker, on the same grounds unit 3 correctly applied to its own fork. Reconciling the vocabularies means
re-declaring what `RECALL_DARK_LAYERS` values ARE for every adopter that has already written one, which
is a change to a kit's shipped input contract — M3 veto 2, an owner turn — and unit 5 carries no fork for
it. As written the unit cannot be built without a decision it does not have and does not know it needs.

**Fix.** Pick one vocabulary in §4 and say which: extension is the only one both sides can actually
produce, since the derived set comes from a file walk and the registry key exists only in a project's own
Python. Then state the consequence honestly — `RECALL_DARK_LAYERS` values are re-declared as extensions,
gov's `bash` becomes `.sh`, and adopters need a named migration — and raise that as an owner fork in §8
rather than resolving it. Re-word AC2 and AC4 in the chosen vocabulary, and fix §5's migration row, which
is false under either choice.

**Left-shift.** Unit 5's own S2 is the gate, and the left-shift is to point it at gov's real
`.codebase-map.conf` rather than only at fixtures. An arm asserting that every `RECALL_DARK_LAYERS` token
is either a `SYMBOL_EXTRACTORS` key or an extension present in the corpus reds TODAY, on `bash`, and that
red is the cheapest possible way to force the vocabulary decision before the unit lands rather than
after. Generalised: a conf key whose values must be members of a derived set gets a membership arm at the
point the key is read, which is the same rule the lexicon kit already applies to `LANGS`.

---

### H1 — high — unit 1 §4 Data model, the `fan_in` signature change

**The defect.** §4 says "`fan_in` then takes a definer set rather than a single `def_file`", and S1 says
"the caller already holds `symbols.json` and can supply the definer set" — singular, in both places.
`fan_in` is defined at `tools/codebase-map/map_lib.py:823` and has four production call sites in three
files: `reuse_lookup.py:264` (inside `seed_affordances`), `reuse_lookup.py:274` (inside `_rank`),
`map_diff.py:204` (the `dead_exports` count) and `map_lib.py:1240` (inside `detect_collisions`). §4 plans
for one of them.

The fourth is the interesting one. `detect_collisions` receives `new_symbols` and `base_symbols` and
nothing else; `new_symbols` is defined in its own docstring as "head rows absent from base", so
`base ∪ new` is not the head symbol list and the definer set reachable inside that function is not the one
S1 specifies. Either the signature grows a required argument that `detect_collisions` cannot honestly
fill, or its caller in `map_diff.py` threads the head rows through — an edit §4 does not anticipate in a
file B1 already shows is misassigned.

Left unedited, the consequence is worse than an incomplete refactor: `reuse_lookup` ranks by the new
counting while `dead_exports` and the collision loop keep the old, so one symbol has two different
fan-ins inside one kit, and the `--converge` threshold test at `map_lib.py:1241` (`fe < threshold`) is
applied to a number the ranking no longer uses.

**Fix.** Enumerate all four call sites in §4 and state what each one passes. Say explicitly what definer
set `detect_collisions` is given and record it in that function's docstring, since the honest answer
(`base_symbols`, not head) changes what the collision threshold means. Declare `map_diff.py` inside unit
1's write set, and reconcile with B1.

**Left-shift.** A codebase-map selftest arm that pins ONE fan-in figure and reads it through two
consumers — `reuse_lookup`'s ranking and `map_diff`'s `dead_exports` — over the same fixture corpus, and
reds when they disagree. That is the class here (one metric, several call sites, no parity check), and it
would catch the next signature change as well as this one. It also gives H7 the population pin it needs.

---

### H2 — high — unit 2 §6 AC4, against §4

**The defect.** AC4 reads: "When every conditional tier in `test_generated_artifacts_are_fresh` is
enumerated, each one reports run-or-skipped, verified by an arm that removes a tier's population and greps
the output for that tier's name." Measured at HEAD, that function
(`tools/codebase-map/test_codebase_map.py:127-145`) builds its `fresh` map from two UNCONDITIONAL entries
and exactly one conditional tier — `if symbols:` at `:141`. That tier is the one S1 already fixes and AC1
already arms.

So AC4 enumerates a population of one, and is discharged in full by AC1's own arm. S3 is the class half of
the fix — "found by reading the function rather than by fixing the one instance — the class, not the
instance" — and §4 names its actual mechanism: "The reporter walks every record, so a tier cannot be
absent from the output by being absent from the map." No criterion in §6 observes that mechanism. An
instance fix and the class fix are indistinguishable under §6, which is this repo's recorded
`green-bar-over-a-population-of-one` shape and `AGENTS.md` §7's "gate the CLASS, not the instance" — inside
the unit written to remove exactly that defect.

**Fix.** Replace AC4 with a criterion over the mechanism rather than over today's population: an arm that
ADDS a synthetic tier to the freshness map without touching the reporter, and asserts it appears in the
output as run or skipped. That criterion holds for tiers that do not exist yet, which is what S3 promises
and what the next non-Python adopter will actually need.

**Left-shift.** The arm IS the gate, and it belongs in `tools/codebase-map/selftest.py` where a synthetic
tier can be injected without touching the shipped file. Beyond this unit, the reusable rule for the
spec-audit checklist: *a class AC names the population it enumerates and the arm ADDS a member rather than
removing one* — because an arm that removes a member of a one-element set can never distinguish a class
fix from an instance fix, and that is how three of this repo's prior could-not-fail arms read green.

---

### H3 — high — unit 3 §6 AC1, against §8 Q1

**The defect.** §8 Q1 is explicitly NOT RESOLVED and explicitly an owner turn: "this changes a kit's
shipped output contract, which is veto 2 in `memory/guides/BUILD-METHOD.md` M3". §6 then resolves it
anyway. AC1 requires that after `map_diff.py --converge` runs in a clean fixture worktree,
`git status --porcelain` is empty — and adds that the arm must be "observed RED before the fix", which
means the fixture run must actually produce flags, since that is how today's untracked file appears.
Under Q1's TRACKED disposition, a run that produces flags necessarily writes rows into a tracked artifact,
so `git status --porcelain` is non-empty and AC1 is unsatisfiable by construction.

S2's own wording is branch-neutral — "no UNTRACKED file appearing inside a gated directory" — so §6
over-tightens what §2 asks for. That matters because M3 veto 1 discards any option that "fails an
acceptance criterion or gate already written in the spec". §6 as written therefore eliminates one branch
of the fork §8 reserves to the owner, before the owner sees it.

The impact as first written was overstated and is corrected here: AC3, AC4 and AC5 survive either branch,
so the unit is not left with no criteria. What it is left with is a spec that pre-commits an owner's
decision in the one section a builder treats as binding.

**Fix.** Split §6 by branch. State the criteria that hold whichever way Q1 lands — the run names the path
it wrote to, the worktree ends in the state that disposition defines, no untracked file appears inside a
gated directory — and mark the branch-specific ones as such, so no AC pre-commits the fork. AC1 becomes
two criteria, one per disposition, and the `git status --porcelain` spelling is correct only for the
outside-the-worktree branch.

**Left-shift.** A `TEMPLATE-SPEC.md` rule the spec-audit checklist enforces: *a spec carrying a `NOT
RESOLVED` fork marks every acceptance criterion as branch-neutral or branch-tagged*. The mechanical half is
cheap — a hygiene check that a spec whose §8 contains `NOT RESOLVED` has at least one §6 criterion carrying
a branch tag, or an explicit line saying every criterion is branch-neutral — and it catches the general
case, which is that §6 is where an unresolved fork quietly becomes resolved.

---

### H4 — high — unit 3 §2 S4 and §6 AC5

**The defect.** S4 asks the kit README to state "that nothing invokes `--converge` on this tree", and AC5
pins it: "it states that no gate leg or script invokes `--converge` in this repository". That claim is
falsified by three tracked files.

`tools/codebase-map/selftest.py:220` sets `_sys.argv = ["map_diff.py", "HEAD~1..HEAD", "--converge"]` and
calls `md.main()` — a script in this repository invoking `--converge`, inside a file that IS a declared
gate leg (`codebase-map kit selftest` in `tools/gate-legs.json`). `WIRE-INTO-PROJECT.md`'s Definition of
Done instructs every adopter to "Also run `python <kit>/map_diff.py <base>..<head> --converge` (the closing
loop)" and says it "routes each to `<MAP_ROOT>/reinvention-backlog.md` (deduped)". And the shipped
`tools/codebase-map/reuse-lookup.agent.md:58-59` tells agents "The closing loop that catches reinvention
you shipped anyway is `map_diff --converge` at review time".

The kit README would be the newest copy a session reads, which makes this two answers to one question with
the wrong copy winning. It also undermines Q1's supporting premise — "nothing currently runs `--converge`
so no durable corpus is being lost" — which is false for any adopter following the runbook, and those
adopters are exactly the population receiving the untracked-file defect.

**Fix.** Narrow S4 and AC5 to the true claim: no gate leg and no hook runs `--converge` as a merge-bar
step; `WIRE-INTO-PROJECT.md` and `reuse-lookup.agent.md` prescribe it to a human or an agent at review
time; `selftest.py` invokes it as a refusal arm. Then carry the correction into Q1's rationale, where it
strengthens rather than weakens the case for a durable destination — a loop the runbook tells adopters to
run at review time is precisely a loop whose output someone might want to review.

**Left-shift.** A `check-dead-paths.sh`-shaped gate for negative claims: a README sentence of the form
"nothing invokes X" is checkable by grepping the tracked tree for X, and the honest version of this claim
should be generated rather than authored. Concretely, a codebase-map selftest arm asserting that the set of
tracked files mentioning `--converge` equals a pinned list — so adding an invoker, or writing a README that
denies the invokers, reds. This is the `AGENTS.md` §6 "a value stated in prose beside the source that owns
it rots" rule applied to a claim of absence, which is the form of it nobody checks.

---

### H5 — high — unit 3 §8 Q1

**The defect.** Q1 offers the owner two options for where the reinvention rows live and recommends
outside-the-worktree. That fork was already posed and already decided.
`memory/builds/bConvergentLodestar/README.md:40` states it as F7: "collision-WARN / backlog home: (a)
append to the reinvention backlog file, dedup by {new,resembles} *(rec)* · (b) stdout-only · (c) per-node
sharded log". Option (a) was recommended, specced, and BUILT — `map_lib.append_backlog`'s docstring opens
"F7: append each collision flag to the reinvention-backlog text, deduped by (new, resembles) — a durable,
reviewable worklist. APPEND-ONLY ... (humans burn it down)".

Neither the spec nor the dossier names F7 or that docstring. Two consequences. The owner is asked to
choose between two of the same three options without the record that already chose, and the third option
F7 enumerated (stdout-only) has silently vanished from the menu. And Q1's recommendation argues from "rows
that no review ever sees and that do not travel between nodes" — which is the exact property option (a) was
selected to provide, so the reversal is being proposed against a rationale it never engages.

The build README's own rule makes this material rather than stylistic: "the record of what was refuted is
the build's main value". A fork re-posed without its prior decision is that rule failing on its own build.

**Fix.** Cite `bConvergentLodestar` F7 and its built implementation in Q1, restate the question as a
REVERSAL of a landed decision rather than as an open choice, restore the third option so the owner sees the
menu the first decision saw, and answer the durability rationale directly — the honest case for the
reversal is that the rows have never actually been reviewed by anyone, which is an observation about
practice, not a defect in F7's reasoning.

**Left-shift.** A spec-audit checklist entry with a cheap mechanical prompt: *before writing a §8 fork, run
the memory-recall query for the mechanism it decides and cite what comes back, or state that nothing did*.
`tools/memory-recall/query.py` exists precisely for this and §10 already forces a `reuse_lookup` probe for
code seams; the gap is that no section of a spec forces the equivalent probe over the DECISION corpus. The
gateable half is small: a spec's §8 that proposes changing a behaviour whose implementing function carries
a `F<n>`-style provenance marker must name that marker.

---

### H6 — high — unit 1 §8 Q1

**The defect.** Q1 dispositions `dead_exports`, concludes "narrow the population is out of scope here and
becomes a follow-up", and files nothing. That follow-up is already filed. `memory/backlog/TOOL.md:295`
carries `TOOL-aScouredKit-17`, OPEN, on exactly this: "`dead_exports: 412` ... is 100% false positives ...
385 of the 412 (93.4%) are module-private helpers zeroed by the `- {def_file}` subtraction in `fan_in` ...
this number gets reworded or dropped". It closes with "Shares its root with `TOOL-aScouredKit-16` and should
land with it" — and `TOOL-aScouredKit-16` is the row unit 1 S5 amends.

A grep across `memory/builds/dTracedLattice/` returns no citation of `-17` in any spec, in the dossier or
in the README. So the owner reads Q1 as a fresh open question rather than as an OPEN row about to be made
materially worse: unit 1 grows the fan-in-0 population from 451 to 532 by its own numbers, which is the
population `-17` says is already 100% false positives, while the row's explicit co-landing instruction is
declined without being mentioned. The 412-versus-451 gap also goes unreconciled — `-17` measured 412 at
`093730e4` and the figure reads 451 at `c4fcf5ad`.

**Fix.** Cite `TOOL-aScouredKit-17` in Q1. Record that 412 was measured at `093730e4` and reads 451 at
`c4fcf5ad`, so the row's next reader is not comparing two different trees. Resolve Q1 as "the disposition
belongs to `TOOL-aScouredKit-17`; this unit reports 451 → 532 so the movement is attributable", and either
honour the co-landing instruction or state plainly why this build declines it. Note that S5 is already
editing the neighbouring row, so the amendment costs one more sentence in a file the unit opens anyway.

**Left-shift.** A hygiene check in the `TEMPLATE-SPEC.md` family: a §8 question that resolves to "becomes a
follow-up" must either name the id it files or name the id that already owns it — a follow-up with no id is
a follow-up nobody will find. The cheap version greps the backlog shards for the spec's own §10 recall
terms and prints candidate rows at spec-authoring time, which would have surfaced `-17` here without anyone
remembering it existed.

---

### H7 — high — unit 1 §2 S1 and §4, on the seam threshold

**The defect.** Subtracting same-name definers lowers every fan-in. `SEAM_FANIN_THRESHOLD` — 3 in this
repo, and the kit default — is compared against that number in three places:
`reuse_lookup.py:265` inside `seed_affordances`, `reuse_lookup.py:275` inside `_rank`'s `is_seam`, and
`map_lib.py:1241`'s `fe < threshold` inside `detect_collisions`. No section of unit 1 re-derives or pins
it.

The magnitude is already measured, in the row unit 1 is amending: `TOOL-aScouredKit-16` records that
"71 of 165 SEAMs fall below threshold on that filter alone" — definer subtraction removes 43% of the seam
set. So the same configured `3` silently becomes a stricter bar: SEAM labels disappear from the output of
the `TEMPLATE-SPEC.md` §10 probe every Tier-2 spec is required to cite, `--seed-affordances` returns fewer
candidates, and `--converge` flags fewer collisions — here and in every adopter whose threshold was tuned
against the old metric.

Unit 1 does carry a disposition for the TAIL effect of the same change (Q1, `dead_exports`) and says
nothing about the HEAD effect. No §3 non-goal withholds it, and sibling unit 3's non-goal assigns it here
("Not changing collision detection, its threshold, or its output — `TOOL-dTracedLattice-1` moves the
precision that feeds it"). A measured 43% change in a shipped label's population, owned by no unit.

**Fix.** Add a scope item that re-derives the threshold against the new metric, or states with the
measurement that `3` still means what it meant. Add an AC pinning the seam count before and after on this
tree, the way AC4 already pins `load_conf`'s fan-in. Add a line to `.codebase-map.conf`'s comment and to
the kit README telling adopters the scale changed, since their tuned values do not travel with this fix.

**Left-shift.** The parity arm from H1, extended: pin the SEAM population — the count `seed_affordances`
returns on a fixture corpus at a fixed threshold — so any change to `fan_in` that moves the seam set reds
until the arm's number is deliberately re-declared with a reason. That is `AGENTS.md` §7's cost-is-a-verdict
shape applied to a metric rather than to wall clock: a threshold whose meaning silently changes is the same
defect as a ceiling nobody re-declares.

---

### H8 — high — unit 5 §4 Alternatives rejected and §10 Reuse audit

**The defect.** The lexicon kit already ships this unit's design, and was built FROM this very decision.
`tools/lexicon/lexicon.py:17-24` declares a three-mode per-extension coverage vocabulary — `parser`
(complete over its extension), `probe` (incomplete by construction, reported every run), `dark` (declared
explicitly, named every run) — and states its provenance outright: `map_extractors.py` "refuses to ship a
regex extractor for shell and declares that language recall-dark instead ... That law binds here".
`lexicon.py:524` raises the `UNDECLARED EXTENSIONS` refusal, which is S2's mechanism. Neither §4 nor §10
names any of it.

Three things are lost with the citation. The three-mode vocabulary: unit 5's model is two-state
(covered / dark), and this kit's own `kit-js` layer is an export-scan-union-definition-probe, which a
two-state model must call "covered" while it is exactly what `probe` was invented to describe.
`scaffold_lexicon.py:110-116`'s seeding rule, whose comment records that "Every fresh adoption hit that in
its first five minutes" — unknown extensions are seeded `dark` so a new adopter is not red on first commit,
which is the failure AC1 reproduces. And the S6 lesson at `lexicon.py:733`: an arm phrased as "some dark
extension carries a definition" reds an honest adopter whose dark extensions are all data files, and was
replaced by an agreement assertion. AC3 ("a layer named in `RECALL_DARK_LAYERS` is absent from the corpus
entirely → report the stale declaration") is that same shape and has not been checked against that lesson.

The "a kit file names nothing outside itself" rule does not excuse the omission: §10 is a reuse audit, not
kit code, and unit 1's own §10 cites `tools/lexicon/lexicon.py` as prior art.

**Fix.** Add the lexicon kit to §10 as the prior art it is, cite `AGENTS.md` §12's coverage-mode rule
(declare a mode per language; an undeclared one is a named refusal) rather than only §7, and state in §4
whether this unit adopts the three-mode vocabulary or deliberately keeps a two-state model, with the
reason. Re-check AC3 against the `lexicon.py:733` lesson before pinning it, and decide whether a fresh
adopter's first run should refuse or seed.

**Left-shift.** Nothing gateable covers "you re-derived a landed sibling's design", and the honest left-shift
is a spec-audit checklist entry: *a unit adding a declaration-plus-refusal greps the tree for existing
declaration-plus-refusal implementations before §4 is written, and §10 records what it found or that it
found nothing*. The mechanical assist already exists and was used here — `reuse_lookup` returned no seam,
which is correct, because the prior art is a sibling kit's DESIGN rather than a callable seam. That gap is
worth stating in `reuse-lookup.agent.md`: a null lookup result is evidence about seams, never about prior
art.

---

### M1 — medium — unit 2 §8 Q1, against §2 and §6

**The defect.** Q1 resolves that `test_codebase_map.template.py` and the installed `test_codebase_map.py`
"both change in the same commit". No §2 scope item names the template, and no acceptance criterion pins
their equality. The two are byte-identical today — verified with `cmp` — and nothing in the tree compares
them: `kit/dogfood doc parity` is a memory-tree document check (see M2), and
`tools/codebase-map/selftest.py:241` and `:350` copy the TEMPLATE into fixtures while the
`codebase-map coverage + freshness` leg runs the INSTALLED copy.

So the resolution is a remembered instruction with no scope item, no criterion and no gate, in a build
whose own subject is frozen-copy divergence. The concrete failure: arms land against the template, the
installed gov gate keeps skipping silently, and the bar is green with the fix half-landed — or the
reverse, and the kit ships an unfixed template to every adopter.

Medium rather than high because Q1 does state the right instruction and a builder following the spec does
the right thing; what is missing is anything that catches a builder who does not.

**Fix.** Add `tools/codebase-map/test_codebase_map.template.py` to §2 as an explicit write target, and add
an AC asserting the two files are byte-identical after the unit lands. That needs a new arm, since no
existing leg covers the pair.

**Left-shift.** A codebase-map selftest arm doing exactly that byte comparison, for gov's tree only. Note
that unit 4 §4 explicitly rejects byte-equality as an adopter check — correctly, since adopters may
customise — but gov is not an adopter here: its `GATE_FILE` points inside the kit directory, so the two
files are one file's two names and equality is the right assertion. The general rule for the checklist: a
kit that ships a template AND dogfoods its render asserts equality on its own tree, and asserts coverage
rather than equality on an adopter's.

---

### M2 — medium — unit 4 §7 Gates, against §4 Inventory

**The defect.** §7 lists `kit/dogfood doc parity` as one of this unit's gates. That leg is
`{"argv": ["bash", "tools/memory-tree/kit-dogfood-parity.test.sh"], "guard": ["memory/HYGIENE.md",
"memory/TEMPLATE-SPEC.md", "memory/guides/BUILD-METHOD.md", "tools/lib/", "tools/memory-tree/"]}`, and its
header shows it compares two memory-tree documents against their templates. It has no relation to
codebase-map's gate template, and none of unit 4's write set (`tools/codebase-map/*`, `kit.toml`, the kit
README) is inside its guard — so it is guarded out on every run of this diff and can only ever report as
skipped.

Meanwhile `codebase-map adopter e2e` (`{"argv": ["bash", "tools/codebase-map/adopt-codebase-map.test.sh"],
"guard": ["tools/codebase-map/"]}`), whose subject is the adopter path §1 blames for the frozen copy, is
absent from §7. The declared bar therefore overstates coverage in one direction and understates it in the
other, which is the `AGENTS.md` §16 rule about naming every leg failing at the point where the leg list is
authored rather than read.

One adjacent fact worth carrying into the fix, verified in the manifest: `codebase-map kit selftest` and
`codebase-map adopter e2e` both carry `subject: kit`, so both are HELD unless `GATE_SELFTESTS=1`. Four of
the five specs list the selftest leg as their gate. A Definition of Done for kit work owes
`GATE_FULL=1 GATE_SELFTESTS=1`, and none of the five §7 sections says so.

**Fix.** Drop `kit/dogfood doc parity` from unit 4 §7, add `codebase-map adopter e2e`, and check each
remaining leg's guard in `tools/gate-legs.json` against this unit's write set before listing it. Add a line
to each spec's §7 stating that the kit-subject legs need `GATE_SELFTESTS=1`, since a builder reading §7 and
running the plain bar will see them silently held.

**Left-shift.** This one is fully gateable and is the most useful check in this report: a spec's §7 leg
names are validated against `tools/gate-legs.json` — every named leg exists, and every named leg's guard
intersects the unit's declared write set or the spec says why it is listed anyway. The manifest is already
the single source `AGENTS.md` points every reader at; nothing yet checks that a spec's copy of a leg name
resolves. The same check gives B1 its write-set list for free, since both need the same declaration.

---

## What this pass did not cover

- The dossier's measured figures were read, not re-derived. The precision table, the medians and the
  ground-truth corpus are taken as reported; B2 is the finding that nothing in the tree lets anyone check
  them, and it does not claim they are wrong.
- The relations answer itself was not re-litigated. The README rules it closed on `AGENTS.md` §12 grounds
  and this pass took that as given.
- No finding here is about the dossier's rev-1 record. Keeping the refuted version is a deliberate build
  rule and it is the right one.
- The specs were audited against the tree at `c4fcf5ad`. Nothing here was run against a build; no code
  exists yet.
