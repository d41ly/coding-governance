**Serves:** spec-audit TOOL-dDerivedDocket-15 TOOL-dDerivedDocket-16 TOOL-dDerivedDocket-17 TOOL-dDerivedDocket-18 TOOL-dDerivedDocket-19 TOOL-dDerivedDocket-20

# dDerivedDocket — spec audit of topic group G3, ask-driven unattended runs, round 2

*Node `d`, 2026-09-20. The second Tier-2 adversarial pass over the six specs of topic group G3: the
ask envelope, READY and the new-build scaffold (unit 15); the driver's ask-awareness (16); the
`asks-disposed` Definition-of-Done item and its freeze (17); the leg's second opinions (18);
authority grants (19); and the unattended carriers with the two-key refusal (20). This is a FOLD
review, regrounded on `fb07ca25`: origin/main moved 210 commits past the original BASE `abac6d59`,
HEAD merges it in, and every spec re-verified its claims there and moved its header base under a
section 9 line reading `regrounded on fb07ca25`. Code claims below are judged at HEAD. The pass was
aimed at the text no reviewer has seen — every section 9 line dated after the round-1 record — and at
whether each round-1 fix holds. Four primed finder lenses ran and all four returned; a skeptic stage
prompted to REFUTE each finding ran in five batches and all five returned; then this synthesis. The
sources were the ratified design record
`memory/builds/dDerivedDocket/build/2026-09-14-build-TOOL-dDerivedDocket-1-design.md`, the owner
mandate `memory/builds/dDerivedDocket/prompts/2026-09-14-prompt-TOOL-dDerivedDocket-1-owner-mandate.md`,
the spec brief's roster and edge tables, and the round-1 record
`memory/builds/dDerivedDocket/reviews/2026-09-14-review-TOOL-dDerivedDocket-15-spec-audit-g3-round1.md`.
Sibling specs outside G3 were read wherever an edge or an interface named them: units 1, 2, 4, 7, 22,
24, 28, 34 and 35, because contradiction between specs is in scope. Every entry below was re-checked
against the spec text and, where it rests on the behaviour of a tool, against source at HEAD; the
sites read are named in each entry. Three entries were re-measured by RUNNING the code rather than
reading it, and each says so. The six blobs below were confirmed equal to the working tree before
this report was written.*

**Round: 2.** Range at base `fb07ca25`, each subject pinned at the blob it was read at: `memory/builds/dDerivedDocket/spec/2026-09-14-spec-TOOL-dDerivedDocket-15.md@f02bf1ac17f81d6d6233bd395d067b7421260520`, `memory/builds/dDerivedDocket/spec/2026-09-14-spec-TOOL-dDerivedDocket-16.md@104cd0d9aef4826f354824f01c9d0f1f5f26830a`, `memory/builds/dDerivedDocket/spec/2026-09-14-spec-TOOL-dDerivedDocket-17.md@132d68bdee2d138cc390dd05c38f73c44e2334d5`, `memory/builds/dDerivedDocket/spec/2026-09-14-spec-TOOL-dDerivedDocket-18.md@840a31006680c05a30389cc1f2f81bb9455f92d4`, `memory/builds/dDerivedDocket/spec/2026-09-14-spec-TOOL-dDerivedDocket-19.md@40462f85a8b63846b64fdb82f659106277e640f5`, `memory/builds/dDerivedDocket/spec/2026-09-14-spec-TOOL-dDerivedDocket-20.md@d278a8b0b042ed643f09ec5597b3408e0978ee2d`

## Verdict: BLOCKED

One BLOCKER stands, and it is round 1's H1 coming back wearing the fix that was supposed to close
it. Round 1 found that `--tsv` did not own its stdout and ruled the fold cheap — "a clause in unit 15
and one stdout rule in unit 7, not a missing mechanism". Both clauses landed. Unit 15 section 4 now
routes the waiver line and unit 7's S11 liveness line to stderr. The defect survives anyway, because
the CONSUMER merges the streams straight back: units 16 and 17 run the witness through `run_bounded`,
which redirects with `>"$_f" 2>&1` in both of its branches
(`tools/unattended/unattended.sh:191-193`), and unit 28 S1 pins that capture as unchanged. Every
notice the producer was moved to stderr to keep out of the row stream therefore arrives inside the
text the TSV parse refuses on, and unit 17 section 4's own rule — a line whose first field is not
`ask` is a parse refusal — fires on a HEALTHY producer.

That is the blocker line this build's reports draw, on both halves. As specified, the build cannot
reach the outcome its mandate names: the first real `ASKS_CMD` call after unit 35 arms gov is a parse
refusal, every mandated preflight then refuses as a DEAD PROBE, and unit 17's witness and unit 18
S8's re-derivation inherit it through the same call. And the fold needs a mechanism no spec in the
set carries — a stream-splitting bounded runner, or a second capture file — which is the half round 1
explicitly said was absent.

**Decision needed:** the orchestrator owes one ruling, stated in B1. Either the witness gets its own
capture that keeps stderr on a separate channel, which unit 28 S1 must then stop pinning as
unchanged, or unit 17 section 4's parse rule is rewritten to tolerate and discard non-row lines,
which reverses round 1's H1 fix at the other end. The two are mutually exclusive and no spec in the
set picks one.

Six HIGH defects follow, carrying seven raw ids. Three of the seven land on one criterion — unit 15
AC13, the fix round 1 asked for under M11 — which observes nothing for two independent reasons and is
green before the unit acts. Nine MEDIUM and one LOW follow.

**The fold is still where the defects are.** Sixteen of the nineteen confirmed ids sit in text that a
section 9 line dated after the round-1 record introduced. Two sit in text that was byte-identical at
the round-1 blob and that round 1 walked past; both provenance claims were checked by reading the
round-1 blobs directly with `git cat-file -p`. The nineteenth, id 25, is a third class worth naming:
old text made load-bearing by new fold text. Unit 15's `--at` mode is unchanged since round 1, and
unit 18 section 8 F3 — entirely fold text, with no F3 in unit 18 at the round-1 blob — now resolves a
fork by asserting that READY at a pinned rev is a pure function of pinned inputs, a property nobody
ever specified and which the conf read breaks.

## Run integrity

- Lenses: 4 of 4 returned, 0 DIED.
- Skeptic batches: 5 of 5 returned, 0 DIED.
- Contradictory verdicts demoted to unverified: 0. Spurious verdicts discarded: 0. Duplicates: 0.
- Unverified findings: 0.

This run is COMPLETE. Every lens reported and every finding reached a skeptic, so a zero here is
evidence and not the artefact of a missing lens: where this report says no confirmed finding covers
something, that means four lenses and a skeptic stage found nothing there, which is evidence and not
proof. Two id pairs and no triple are merged into single items below; the pipeline's duplicate count
of 0 comes from its own exact-match dedupe, which does not see a restatement.

## Review shape

Raw 37, confirmed 19, refuted 18, unverified 0. Precision 0.51, which sits just on the ~0.5 floor
section 8 of the charter sets. This surface has now been audited twice, the cheap defects are gone,
and the fan is spending more of its effort on text that holds; a round 3 over this group should
tighten lens priming or narrow scope before it adds agents. The 18 refuted findings are not
reproduced here.

Adjudicated tally, stated both ways, because merged items and raw ids do not agree:

| Severity | Items | Raw confirmed ids |
|---|---:|---:|
| BLOCKER | 1 | 1 |
| HIGH | 6 | 7 |
| MEDIUM | 9 | 10 |
| LOW | 1 | 1 |
| Total | 17 | 19 |

**Severity is adjudicated here, not copied from the finders**, on the scale round 1 used.

- BLOCKER means that, as specified, the build cannot reach the outcome its mandate names, and the
  fold needs a decision or a mechanism that no spec in the set carries.
- HIGH means a unit cannot be built or cannot pass as written for a reason visible only across specs,
  or it ships a layer that stays inert while its suite reads green.
- MEDIUM covers three kinds: a contradiction between specs with a bounded or visible consequence; a
  declaration whose absence reds a leg at the post-build bar; a claimed mechanism that does not exist.
- LOW is a rule whose break no criterion can see, where the reachable harm is small.

Four entries move against their finder's label, and each says so in place.

- Id 21 was filed high and is adjudicated BLOCKER, on the two-half test above.
- Id 7 was filed medium and id 32 high; they are one defect and merge into one HIGH item, H2.
- Id 20 was filed low and is adjudicated MEDIUM, merged with id 17 into M7. The two are one fold's
  residue in two specs with identical consequences, and splitting their severity would hide that.
- Id 2's impact argument is trimmed. The finder treated the grant path as a machine confinement;
  unit 19 section 3 declares veto enforcement to be agent judgement, so it is not one. That the
  declared guard is observed one way out of four is still the defect.

## Findings index

| # | Severity | Unit | Address | One line | Raw ids |
|---|---|---|---|---|---|
| B1 | BLOCKER | 16 | section 4, the `ASKS_CMD` contract; S5 | The witness runs through `run_bounded`, which merges stderr into the row stream | 21 |
| H1 | HIGH | 16 | section 6 AC18 | AC18 demands the UNDECIDED `next:` over a fixture section 4 says prints the MISSING one | 1 |
| H2 | HIGH | 15 | section 6 AC13, the `fixture:` line | The arm reaches `anchor_at` through a conf key the memory-tree kit does not declare | 7, 32 |
| H3 | HIGH | 15 | section 6 AC13, the fixture ids | `EXMP` is not an admitted family, so AC13 is green before the unit acts | 22 |
| H4 | HIGH | 18 | section 4, the `m-base:` re-derivation; S8 | Rotation renames inside the folder, so the announced ancestry fallback never fires | 24 |
| H5 | HIGH | 15 | S6; section 4, the `--at` mode | `--at` pins the record reads and leaves the conf at evaluation time | 25 |
| H6 | HIGH | 19 | section 4, the cross-run arm | The exclusion probe is history-simplified, not the reachability test it is used as | 27 |
| M1 | MEDIUM | 18 | S8 against AC11 and AC12 | Three of S8's declared branches have no criterion, including its skip and its bound | 3 |
| M2 | MEDIUM | 16 | section 6 AC13 | No observation says the named `SPEC_TOKENS_CLI` clause is the passage that left | 4 |
| M3 | MEDIUM | 17 | section 6 AC1 | The moved paragraph has no witness phrase, and the verbs template is never read | 5 |
| M4 | MEDIUM | 15 | S6 against AC5, AC7 and AC8 | "All write nothing and exit 0" is observed for `--at` alone | 8 |
| M5 | MEDIUM | 15 | section 4, the scaffold; AC10 | Generated slot bodies have no wrap against check 7's 350-character cap | 26 |
| M6 | MEDIUM | 20 | section 4, both budget paragraphs | Share arithmetic the closing consolidation pass already replaced | 14 |
| M7 | MEDIUM | 16, 17 | section 3 scope sentences | Two "writes only" sentences contradict the writes their own S-items mandate | 17, 20 |
| M8 | MEDIUM | 20 | section 6 AC3 | The pointer-phrase clause is green because unit 16 writes the same string first | 35 |
| M9 | MEDIUM | 19 | section 6 AC3 | S3's grant-path guard declares four negatives and AC3 exercises one | 2 |
| L1 | LOW | 18 | section 6 AC8 | No `recipe`-mode arm, where both siblings carry one | 11 |

## Blockers

### B1 — the witness runs through a capture that merges stderr into the row stream (21)

**Address.** `memory/builds/dDerivedDocket/spec/2026-09-14-spec-TOOL-dDerivedDocket-16.md`, section 4
"The `ASKS_CMD` contract" and section 2 S5. Inherited by unit 17 section 4 (the witness call) and
unit 18 S8 (the re-derivation), both of which route the same call the same way.

**What.** Unit 16 section 4 states the witness call runs through `run_bounded`. At HEAD that function
is, in both of its branches:

```
timeout -k 5s "$GATE_BOUND" "$@" </dev/null >"$_f" 2>&1; _rc=$?
...
"$@" </dev/null >"$_f" 2>&1; _rc=$?
...
RB_OUT=$(cat "$_f" 2>/dev/null)
```

`tools/unattended/unattended.sh:191-196`. One buffer, both streams. Unit 28 S1 confirms it stays that
way for this build: "the file capture and the `timeout -k` wrapper are unchanged".

The producer emits non-row lines on every healthy call. `collect()` prints its waiver line
UNCONDITIONALLY, including at zero — `tools/memory-tree/gen_build_index.py:822`, with the ratified F2
comment beside it explaining why a silent zero would be indistinguishable from a check that never
ran. Unit 7 S11's liveness line joins it on every run. Round 1's H1 fix moved both to stderr (unit 15
section 4: "unit 7's S11 liveness line and every other notice go to stderr"; unit 15 AC6's fixture
even asserts "the waiver line appears on stderr"). `run_bounded` merges them back into `RB_OUT`
before the consumer sees a byte.

Unit 17 section 4 then defines the consumer's parse: a line whose first field is not `ask`, or that
does not carry eleven fields, is a parse refusal rather than a row. So a healthy producer hands the
driver a parse refusal on every real call.

**Why it is real.** Reproduced by reading `run_bounded` at HEAD, not inferred from a spec. `grep` over
units 15 through 18 finds no stream split, no `2>/dev/null`, and no stderr handling anywhere on the
consumer side: the only stderr sentences in the group are unit 15's two, which are the PRODUCER's
half of round 1's fix. The blast radius is the whole feature. Preflight refuses as a DEAD PROBE on
every mandated run; unit 17's `asks-disposed` witness cannot be taken, so every close with a
non-empty scope is UNMET on T2, this build's own close included; and unit 18 S8's re-derivation, the
leg's only second opinion that executes a producer, refuses the same way. Unit 16's own AC15 runs the
DECLARED producer over a fixture holding a waiver-tolerated header, so that criterion reds for this
structural reason rather than for a real fault, and a builder chasing it will be debugging the wrong
thing.

**Fix.** The orchestrator picks one, and it is a decision, not an edit:

- (a) State in unit 16 section 4 that the witness captures STDOUT ALONE. Name the bounded-runner
  variant or the second capture file that keeps stderr on its own channel, add it to section 4
  Inventory and Files touched, and amend unit 28 S1 so it stops pinning the capture as unchanged.
  Units 17 and 18 then re-point at the named variant.
- (b) Rewrite unit 17 section 4's parse rule to skip non-row lines rather than refuse on them, and
  say explicitly what distinguishes a notice from a malformed row. This reverses round 1's H1 fix at
  the consumer instead of honouring it at the producer, and it gives up the ability to tell a dead
  probe from a chatty one, so it is the weaker option.

Whichever is chosen, give unit 16 AC6 an arm where the producer writes a notice to stderr while the
eleven-field rows still parse.

**Left-shift gate.** A criterion — unit 16 AC6 or AC15 — that runs the REAL declared producer, with a
stderr notice guaranteed present (the waiver line is unconditional, so it always is), and asserts the
driver reaches a row count rather than a DEAD PROBE. Red when: the witness call captures stderr into
the row stream, so a healthy producer reads as a dead probe. This is the charter section 7 rule that
a guard sharing a channel with the thing it guards is not a guard, and it is the arm whose absence
let round 1's H1 fix look landed.

## High

### H1 — AC18 asserts the one `next:` shape its own fixture forbids (1)

**Address.** `memory/builds/dDerivedDocket/spec/2026-09-14-spec-TOOL-dDerivedDocket-16.md`,
section 6 AC18, against section 4 "Plan, next and rank" and section 2 S8.

**What.** Section 4 pins the rule: "The UNDECIDED shape is ... printed only when no unit shape
remains", and S8 repeats it ("prints only after every unit shape"). AC7 fixes the competing shape for
a fixture holding MISSING units: `next: EXMP-tRun-2 (MISSING - spec it first)`. AC18's fixture holds
`-2` and `-10` MISSING plus two live units, and demands that `--status` and `--resume` print "the
same UNDECIDED `next:` as `--plan`". An implementation cannot satisfy section 4 and AC7 and AC18 at
once.

**Why it is real.** The clash traces to round 1's M18, whose fix list folded four separate
observations onto one fixture: the hold-edge rank, `-2` before `-10`, the duplicate-closer row,
`ready=-`, and the four summary keys all ride the same run, so the whole criterion is unlandable, not
just its first clause. Worse, S8's ordering rule is then observed by NOTHING: AC17's fixture has no
units and AC7's has no mandate, so no criterion anywhere puts an undecided mandated ask and a
remaining unit shape in one tree — which is the exact state the rule exists to decide.

**Fix.** In AC18, assert `next:` is the MISSING shape naming `-2`, and that `--status` and `--resume`
print the same. Add a second arm over the same fixture with both MISSING units retired, or their
specs written, asserting the shape flips to UNDECIDED. S8 then gains its failing case and the rest of
AC18's assertions keep their run.

**Left-shift gate.** The second arm is the gate. Red when: the UNDECIDED shape is printed while a
unit shape remains.

### H2 — AC13 reaches `anchor_at` through a conf key the memory-tree kit does not declare (7, 32)

**Address.** `memory/builds/dDerivedDocket/spec/2026-09-14-spec-TOOL-dDerivedDocket-15.md`,
section 6 AC13, the `fixture:` line; it observes section 4 "The scaffold".

**What.** AC13 routes a `gen_build_index.py --selftest` arm — a memory-tree KIT selftest, and section
7's `build-index selftest` gate — to `anchor_at` through `RECALL_CLI`. That key is declared at
`.unattended.conf:89` and `tools/unattended/.unattended.conf.example:90` and nowhere else; neither
`.memory-tree.conf` nor `tools/memory-tree/.memory-tree.conf.example` carries it, and this unit's S7
adds only `PROBE_ALLOW` while section 4 Files touched adds nothing.

**Why it is real.** Both halves were verified against the tree. In gov the memory-tree kit would read
another kit's conf to run its own selftest; in an adopter that took memory-tree without the
unattended kit the key does not exist, so AC13 takes its named skip FOREVER and the anchor assertion
the round-1 fold added for M11 is observed on no tree at all. The kit's own route is already decided
and armed one import away: `GRAMMAR_DIR = HERE.parent / "memory-recall"` at
`tools/memory-tree/corpus_ids.py:47`, `grammar()` at `:259-279` with a named refusal when `extract.py`
is absent, `_anchor(E, line) -> extract.anchor_at(line, E)` at `:460-464`, and an exit-3 degradation
with its own selftest arm at `:857-870`; `merge-rows.py:168-180` repeats the same two-layout probe,
and `gen_build_index.py:283-284` already imports `parse_conf` from `corpus_ids` as the kit's one conf
parser. Choosing a foreign kit's undeclared key over an in-kit seam is also the cross-kit literal the
charter section 12 bans. It compounds with H3: AC13 asserts a NEGATIVE — that a generated body
anchors nothing — which a wrong route and a skipped arm both satisfy while proving nothing.

**Fix.** Rewrite AC13's `fixture:` line to reach `anchor_at` through `corpus_ids`' existing grammar
bundle (`grammar_for(root)` / `_anchor`), and take that module's exit-3 named degradation as the
arm's skip condition. Drop `RECALL_CLI` from this spec entirely; it stays correct for unit 18 S3,
whose leg is an unattended-kit file. Add a line to section 10 recording the prior art so the next
reader does not derive a second route. If the key is genuinely wanted here, it owes an S-item, a
section 4 Files touched row, and an example-conf row, which
`tools/memory-tree/check-memory-hygiene.test.sh` asserts for every key the engine reads.

**Left-shift gate.** The existing example-conf assertion in
`tools/memory-tree/check-memory-hygiene.test.sh` already reds a key the engine reads and the shipped
example does not declare; the gate that is missing is its mirror — a check that no memory-tree module
reads a key declared only in another kit's conf. Red when: a kit resolves a dependency through a
sibling kit's conf key instead of its own declared seam.

### H3 — AC13's fixture ids are in a family the grammar does not admit, so it is green before the unit acts (22)

**Address.** `memory/builds/dDerivedDocket/spec/2026-09-14-spec-TOOL-dDerivedDocket-15.md`,
section 6 AC13 (the round-1 M11 fix), with section 4 "The scaffold".

**What.** `anchor_at`'s id grammar is an ALLOWLIST of the recall conf's FAMILIES:
`FAMILIES = CONF.families` at `tools/memory-recall/extract.py:68`, composed into
`ID = (?:FAMILIES)-(?:ERAS)` at `:106`. In gov `.memory-tree.conf:15` declares
`FAMILIES="playbook:PLAY kickoff:KICK tooling:TOOL deployer:DEPL"`. AC10's fixture files carry
`EXMP-aFoo-3` and `-4`.

**Why it is real.** Measured at HEAD by running the function, not by reading it:

```
'- EXMP-aFoo-3 — the ask'  -> None
'| `EXMP-aFoo-3` | x |'    -> None
'- TOOL-dDerivedDocket-15 — the ask'  -> TOOL-dDerivedDocket-15
'| `TOOL-dDerivedDocket-15` | x |'    -> TOOL-dDerivedDocket-15
```

The second pair uses a DEFINED id of this build, because an undefined one in a declared family
is itself a hygiene finding (check 14). So AC13's assertion that the generated bodies anchor nothing is TRUE before the unit writes a line,
and its Red-when ("a generated bullet reads `- EXMP-aFoo-3 — …`") cannot fire. The round-1 M11 fix
observes nothing, and a scaffold that genuinely anchors a foreign id under the new build ships green.
The allowlist is deliberate — `extract.py` says so in its own comment — and a scratch fixture cannot
substitute its own FAMILIES, because `recall_conf.repo_root()` anchors on the kit file. This is the
charter section 7 ban on a gate that has only ever been seen pass, and it is the same defect class
this build's own `memory/gotchas/green-bar-over-a-population-of-one.md` records.

**Fix.** Pin AC13's fixture ids in a family the grammar admits — file the fixture asks under a
declared family, or state that the arm binds `grammar_for(<fixture root>)` over a fixture conf that
declares the example family. Then require the arm to be SEEN RED on a staged `- <id> — …` body line
before it is allowed to pass.

**Left-shift gate.** The staged-RED requirement written into AC13's `new arm:` line, which is this
build's own convention elsewhere (unit 28 AC13, unit 19 AC11). Red when: a criterion asserting that a
population is empty passes over a fixture whose members could never have entered the population.

### H4 — rotation renames inside the folder, so the announced ancestry fallback never fires (24)

**Address.** `memory/builds/dDerivedDocket/spec/2026-09-14-spec-TOOL-dDerivedDocket-18.md`,
section 4 "S2 the `m-base:` re-derivation", with section 2 S8.

**What.** Section 4 assumes a rotated record makes the introducing commit unfindable, and cites "a
rotated record whose path changed" as the canonical case for its announced ancestry fallback. At HEAD
rotation is a rename inside the SAME folder: `archive_name_of` prints
`'%s/RUN.%s.%.8s.md' "${rel%/RUN.md}"` (`tools/unattended/unattended.sh:1692-1697`) and the move is
`git mv -f -- "$rel" "$arch"` (`:2748`), both sides staged in one operation.

**Why it is real.** The rotated path therefore exists and its blob carries `m-base:`, so a
path-scoped search for the earliest commit whose copy of the record carries that line answers with
the ROTATION commit, not the preflight one. The fallback never fires where section 4 says it does,
and the arm grades against merge-base(`anchor-sha:`, rotation-commit^), which is not the recorded
`m-base:`. Check 19 then reds a correct archived record silently — the "reds the archive for ever"
class this build closes elsewhere. S8's freeze half inherits it: its first-parent tree is the tree
before the NEXT run's preflight, never the one `--landed` examined, so `asks-at-landing:` is compared
against a tree nothing ever looked at. Either way there is a defect: follow the spec's guidance and
the verdict is wrong, or follow renames and AC4's "cannot be found" arm is unreachable by the one
case section 4 names for it.

**Fix.** Say in section 4 how the introducing commit is found across the rename — follow it with
`--follow`, or search the live and rotated paths together — and replace AC4's assumed case with two
arms: a rotated-record arm that must grade against the RECORDED `m-base:`, and a genuinely unfindable
one, for which a shallow clone is the cheap fixture.

**Left-shift gate.** The rotated-record arm. Red when: a record graded after rotation resolves its
introducing commit to the rotation commit, so the re-derived base differs from the recorded
`m-base:` and the record reds with no fallback line printed.

### H5 — `--at` pins the record reads and leaves the conf at evaluation time (25)

**Address.** `memory/builds/dDerivedDocket/spec/2026-09-14-spec-TOOL-dDerivedDocket-15.md`,
section 2 S6 and section 4 "READY / the `--at` mode".

**What.** `--at <rev>` re-points the RECORD reads at a pinned tree and never says which tree supplies
the CONF. At HEAD `load_conf(root)` reads `.memory-tree.conf` from the WORKING-TREE root
(`tools/memory-tree/gen_build_index.py:286-292`) and is called before mode dispatch, so `ASK_CUTOFF`
and `BACKLOG_MODE` stay evaluation-time values whatever `<rev>` is.

**Why it is real.** READY at a pinned rev is therefore not a pure function of that rev — and purity
is exactly what this build's own resolved forks rest on. Unit 18 section 8 F3 closes with "It relies
on unit 16 rev-2 passing no live-build set, which makes the READY call a pure function of pinned
inputs", and S8 re-runs the same call at the recorded `m-base:` later, requiring equality with the
pinned `asks-ready:`. `ASK_CUTOFF` does move: unit 12's `--ingest` prints one, unit 34 S4 sets one,
and unit 34 F10 asks whether the landing reconcile moves it. It is the sole discriminator of the
`legacy` grade, and `BACKLOG_MODE` flips to `builds` in the same unit. After that flip, every
`legacy` grade and every shards-mode `no` changes and check 19 reds a record nobody forged. Nothing
closes this: AC8 edits a BACKLOG row, never the conf; unit 16's call-shape section distinguishes "at
a rev" from "over the WORKING TREE" for record reads only; S11 treats a `BACKLOG_MODE` divergence
between trees as a live condition handled by a NOTICE rather than as something pinned. The finding's
secondary argument — that section 5 prices `--at` at "two git processes" — is weak, since the conf
blob could ride the same `cat-file --batch`, and it is not relied on here.

**Fix.** State in section 4 which tree supplies the conf under `--at`. Either read it at `<rev>`
through the same `cat-file`, or name the conf keys a grade depends on, so unit 16 pins them beside
`asks-ready:` and unit 18 S8 skips BY NAME when they have moved. Correct section 5's cost line to
match whichever is chosen.

**Left-shift gate.** An arm in unit 18 AC11 that moves `ASK_CUTOFF` between the pin and the
re-derivation and asserts the leg either reproduces the pinned grades or announces a named skip. Red
when: a conf change between preflight and the leg's re-derivation reds a record nobody forged.

### H6 — the cross-run exclusion probe is history-simplified (27)

**Address.** `memory/builds/dDerivedDocket/spec/2026-09-14-spec-TOOL-dDerivedDocket-19.md`,
section 4 "The cross-run arm", the terminal-record exclusion function.

**What.** Section 8 F8 resolves the predicate as "the parent from which a commit since BASE touching
the record's run-state path is REACHABLE". Section 4 then spells it
`git rev-list -1 <parent> ^<BASE> -- <run-state path>`, which is a history-SIMPLIFIED query and
answers a different question.

**Why it is real.** Reproduced in a scratch repo at HEAD. With BASE holding `f='a'`, a branch commit
setting `f='b'`, a default-branch commit touching only `g`, and a merge resolving `f` back to `'a'`:
`git rev-list -1 HEAD ^BASE -- f` printed NOTHING, while
`git rev-list -1 --full-history HEAD ^BASE -- f` printed the merge. Any merge below a parent that is
TREESAME to one side for the path — a reconcile taking one side's `RUN.md`, a rotation that deletes
it — prunes the other side entirely. The consequences section 4 already names then fire on wrong
inputs: a pruned run side reads as "neither parent", the walk stops with no exclusion and the range
widens to every default-branch commit since BASE, so an owner's `may:` commit reds the record for
ever; or the other parent wins, the wrong side is excluded, and the run's own `may:` commit leaves
the range — the fail-open that F8 was rewritten to remove. Section 4's "Stated residual" covers a
side with NO touching commit, which is a different population from a side whose touching commit
`rev-list` hides.

**Fix.** Spell the probe unsimplified in section 4 —
`git rev-list -1 --full-history <parent> ^<BASE> -- <run-state path>` or an equivalent — and say in
one clause why, so the next reader does not "simplify" it back.

**Left-shift gate.** An AC6 arm whose merge resolves the run-state path to the other side's content.
Red when: the exclusion probe answers empty for a parent from which a touching commit is reachable.
This is the charter section 7 rule about running a candidate predicate over the real tree before
wiring it — printing hits AND near-misses would have caught this at authoring time.

## Medium

### M1 — three of S8's declared branches have no criterion (3)

**Address.** `memory/builds/dDerivedDocket/spec/2026-09-14-spec-TOOL-dDerivedDocket-18.md`,
section 2 S8, against section 6 AC11 and AC12.

**What.** S8 declares that a bounded `ASKS_CMD` breach "is never answered, not a red"; that with the
tip unobserved "every mandated record is re-derived and the reason printed"; and that where the
introducing commit cannot be found, S2's announced fallback applies and "this arm skips by name".
AC11 observes the forged `asks-ready:` pair and the published-and-not-re-derived line; AC12 observes
the forged freeze and a REOPEN. None of the three branches above is observed.

**Why it is real.** S8 is the leg's only branch that EXECUTES a producer, so the dead-probe and
skip-announce behaviour of the one arm that can hang or silently do nothing is exactly what charter
section 7 requires be observed. A breach reported as a red sends a bar owner hunting a forged pin
that does not exist, and an arm that skips without saying so reads as coverage. The omission is an
asymmetry inside this same spec, not a matter of taste: unit 16 AC6 pins the sleep-past-bound "never
answered" for the driver side, unit 18 AC4 pins S2's fallback announce for `m-base:`, and unit 18 AC6
pins the blank-`RECALL_CLI` skip for S3.

**Fix.** Add three arms to AC11, each with its own Red-when: a stub `ASKS_CMD` that sleeps past the
bound, reported as never answered and not as a red; a fixture whose remote advertises no tip, where
every mandated record is re-derived and the reason printed; and a record whose introducing commit is
unfindable, where the arm prints its skip by name and the leg exits on the other arms' verdicts.

**Left-shift gate.** The skip arm doubles as the gate for the whole leg: assert the leg's output
carries a `skipped` line naming the arm, so a green row can never be misread as a verified one.

### M2 — no observation says the named passage is the one that left (4)

**Address.** `memory/builds/dDerivedDocket/spec/2026-09-14-spec-TOOL-dDerivedDocket-16.md`,
section 6 AC13, against section 2 S1.

**What.** S1 spends a paragraph naming one passage — the `SPEC_TOKENS_CLI` row's closing clause —
settling an overlap in this unit's favour and pricing the trim at 374 B against the ~200 B the new
`ASKS_CMD` row costs. AC13's only mechanized reads are `wc -c` strictly below the parent plus the
check-10 pair identity. Any trim of any paragraph satisfies that.

**Why it is real.** AC13's Red-when asserts an equivalence that does not hold: "the section 8 row
lands without the `SPEC_TOKENS_CLI` trim beside it, so a copy is LARGER" catches only "no trim at
all". A unit that trims something else lands green and the duplicate S1 exists to remove survives.
The build's own convention for this move is a phrase witness — unit 28 AC13 greps `unlike the sibling
above`, counting 1 at the parent and 0 at the build commit, plus the destination phrase; unit 19 AC11
and unit 20 do the same. The finder's double-spend narrative is stale, since unit 28 has already
moved its funding claim to the `BRIEF_RECORDED_CUTOFF` tail; the assertion gap is not.

**Fix.** Add to AC13: `git grep -c 'The checker gov declares is gov-internal'` over both protocol
copies returns 1 at this unit's parent and 0 at its commit, and the same phrase still counts 1 in
`tools/unattended/.unattended.conf.example`, the home S1 says already carries it.

**Left-shift gate.** The parent-and-commit phrase count, which is already this build's standard
shape. Red when: the copies shrank by trimming some other passage, so the named duplicate survives.

### M3 — the moved paragraph has no witness, and one half of the pair is never read (5)

**Address.** `memory/builds/dDerivedDocket/spec/2026-09-14-spec-TOOL-dDerivedDocket-17.md`,
section 6 AC1, against section 2 S5.

**What.** AC1's destination half reads only that `memory/guides/UNATTENDED-VERBS.md` sits under the
61440 B cap "with the moved paragraph in it" — no phrase to grep — and
`tools/unattended/VERBS.template.md` is never read at all, although S5 requires both halves to carry
the move and check 10 byte-compares that pair.

**Why it is real.** AC1's own third Red-when demands the move be told apart from a deletion — "the
paragraph is deleted rather than moved, so the verbs half never gains what section 4 gave up" — and a
size read under a cap cannot do that, because a file well under its cap is under it either way. AC1
also never asserts the protocol pair is byte-identical, which S5 requires and which unit 16 AC13 does
assert for the same pair. The sibling moving a paragraph into the SAME file, unit 19 AC11, greps
`fork-unresolvable` and reads both halves. The finder's timing argument is weaker than it reads,
since AC1's permission line already defers its run to the post-build bar; the witness gap stands on
its own.

**Fix.** Name a witness inside the moved paragraph — `git grep -c 'the only way to write one'` — and
assert it returns 1 in BOTH `tools/unattended/VERBS.template.md` and
`memory/guides/UNATTENDED-VERBS.md` and 0 in both protocol copies at this unit's commit, with the
reverse at its parent. Assert check 10 finds the protocol pair AND the verbs pair byte-identical.

**Left-shift gate.** The four-way phrase count above. Red when: a paragraph leaves its source and
lands in neither half of the destination pair, or in only one of them.

### M4 — "all write nothing and exit 0" is observed for one mode (8)

**Address.** `memory/builds/dDerivedDocket/spec/2026-09-14-spec-TOOL-dDerivedDocket-15.md`,
section 2 S6, against section 6 AC5, AC7 and AC8.

**What.** S6 declares of the print modes: "All write nothing and exit 0." Every criterion was
checked. AC10 reads exit 0 from `--check` and `--check-format`, AC11 reads non-zero from the
scaffold, AC9 prints a probe's exit status, and AC8 alone reads `git status --porcelain`, for `--at`.
No criterion reads the exit status or the tree state of `--asks --tsv`, `--ready`, `--target` or
`--live-builds`.

**Why it is real.** The consequence is cross-unit and concrete. Unit 16 runs this producer inside
`--preflight`, which refuses a dirty tree and stages the record, and unit 16 AC6 makes a non-zero
producer exit a refusal NAMING the exit status. An all-`no` mandate is a different refusal, printing
each id's failing rules. A grader that exits non-zero when nothing is ready — the obvious temptation
in a tool that also has verdict-bearing `--check` modes — swaps the second fault for the first, and
the two have different owner actions. A print mode that writes a cache or a log also dirties the tree
`--preflight` just required clean. Both behaviours are stated in S6 and observed nowhere.

**Fix.** Extend AC7 to assert exit 0, including over a fixture where every examined ask grades `no`
and over an empty `--ready` set, and extend AC8's `git status --porcelain` assertion to cover a
`--tsv --ready --target --live-builds` run as well as `--at`.

**Left-shift gate.** The all-`no` arm. Red when: the grade decides the exit status, so an all-`no`
mandate reaches the driver as a producer failure.

### M5 — the scaffold's generated slot bodies have no wrap against check 7's cap (26)

**Address.** `memory/builds/dDerivedDocket/spec/2026-09-14-spec-TOOL-dDerivedDocket-15.md`,
section 4 "The scaffold" (generated slot bodies), with section 6 AC10.

**What.** The five `SLOT_CANON` slots get generated bodies "naming the asks and the tree they were
read at". Those are ordinary body lines of a build README, which hygiene check 7 caps at
`BUILD_README_ENTRY_CAP_CHARS=350` per unfenced line
(`tools/memory-tree/check-memory-hygiene.sh:94`, applied per line at `:778-806`). Section 4 fixes no
wrap and no bound, so the line length is proportional to the mandate size.

**Why it is real.** Every cited mechanism was checked. The front-matter block is explicitly NOT
measured (`:790-796`, exempted because `--write`'s `ids:` line is 479 characters) and `RUN.md` and
`guides/*.md` are exempt from check 7, but `README.md` is not, and gov's `.memory-tree.conf`
overrides `INDEX_CAP_*` and `DOSSIER_CAP_*` without touching this key. A dozen ~22-character ids plus
framing prose already crosses 350. So the one line section 4 worried about is safe and the ones it
did not are not: the `memory hygiene` leg that section 7 itself names for this unit reds the README
the owner's one command just wrote — the outcome AC10 exists to prevent. AC10 sees nothing, because
it runs only `--check` and `--check-format`, and the generator's own docstring (`:10-14`) says
`--check-format` never grades how large any slot is.

**Fix.** Say in section 4 that generated slot bodies wrap at the build-README entry cap, reusing the
generator's existing `_render_wrapped_ids` (`gen_build_index.py:957`) and its `IDS_WRAP` cap (`:918`).

**Left-shift gate.** Have AC10 run the hygiene leg itself over a fixture whose mandate exceeds 350
characters unwrapped. Red when: the scaffold's own output reds the gate that grades the tree it
writes into.

### M6 — section 4 still prices two carriers as shares of free space (14)

**Address.** `memory/builds/dDerivedDocket/spec/2026-09-14-spec-TOOL-dDerivedDocket-20.md`,
section 4, "The companion guide" and "The build method's budget", against section 2 S3 and S7,
section 6 AC3 and AC7, and unit 19 section 4 Budgets.

**What.** Section 4 reads "This unit's S3 spends at most 250 B of that and unit 19's at most 350 B",
and "the three shares are trimmed to fit ... which leaves 104 B of the 384 B unspent". S3 and S7 now
say each edit "IS PAID FOR IN THE SAME EDIT" and each copy is "SMALLER at this unit's commit than at
its parent", and AC3 and AC7 red on a copy that is the same size or larger, "which is why the
comparison is against the parent commit rather than against a declared share".

**Why it is real.** The closing consolidation pass made S3 and S7 net-zero-or-negative and moved AC3
and AC7 to a parent comparison, and section 4 did not follow, although its revision log claims it
moved. Unit 19's Budgets goes further — "NO CAP IS RAISED IN THIS BUILD, and no SHARE of one is
claimed either" — and hands headroom back, so section 4's attribution of 350 B to unit 19 contradicts
the sibling it names. A builder sizing the edit to section 4's allowance, without making the named
trims, lands a net-positive edit that AC3 and AC7 red. The "whether all of this build's protocol
shares sum under 1116 B is the orchestrator's to settle" sentence parks a question the fold already
closed.

**Fix.** Rewrite both section 4 paragraphs to the net-zero-or-negative rule: name the passage each
edit trims, say it is larger than what the unit adds, and drop the share arithmetic and the
orchestrator-sum sentence. Keep the measured BASE figures (60324 B of 61440 B, 27264 B of 27648 B) as
context for why the companion guide exists.

**Left-shift gate.** None needed beyond AC3 and AC7, which already red the wrong outcome; this is a
prose-versus-source contradiction, and the left-shift is the charter section 6 rule that a value
stated in prose beside the source that owns it rots. A sweep for share arithmetic in any spec whose
S-items now say "paid for in the same edit" is the cheap way to find the rest.

### M7 — two section 3 scope sentences contradict the writes their own S-items mandate (17, 20)

**Address.** `memory/builds/dDerivedDocket/spec/2026-09-14-spec-TOOL-dDerivedDocket-17.md`,
section 3 first bullet, against S5, section 4 Files touched and section 5; and
`memory/builds/dDerivedDocket/spec/2026-09-14-spec-TOOL-dDerivedDocket-16.md`, section 3 fourth
bullet, against S1.

**What.** Unit 17 section 3 says "This unit writes only the protocol section 4 row that leg check 16
requires", while S5 also rewrites `tools/unattended/VERBS.template.md` and
`memory/guides/UNATTENDED-VERBS.md` with the moved attested-verb paragraph and adds a byte-decision
record to protocol section 7. Unit 16 section 3 says "This unit writes only the protocol section 8
row that leg check 22 requires", while S1 also deletes the `SPEC_TOKENS_CLI` row's closing clause
from that same section 8 table as the funding for the new one.

**Why it is real.** Both are one fold's residue. Unit 17's revision log lists the closing
consolidation pass as "S5 · section 4 · section 5 · section 10 · AC1 AC12" and never section 3, so
Files touched and the user-docs line were re-pointed and the scope sentence was not; even the
narrowest reading fails, because section 7 is protocol text. Unit 16's S1 carries a long orchestrator
ruling dated 2026-09-20 settling which unit takes the `SPEC_TOKENS_CLI` tail, and section 3 predates
it. The trims are load-bearing in both: unit 17's moved paragraph measures 579 B at HEAD against a
~200 B addition, unit 16's clause 374 B against ~200 B, and S1 says outright that narrowing the trim
is not an option. A builder scoping from either section 3 under-writes and reds that unit's own
criterion — precisely AC1's third Red-when in unit 17, and AC13's Red-when in unit 16. Id 20 was
filed low; it is the same defect as id 17 with the same consequence, so both are MEDIUM here.

**Fix.** Amend unit 17's sentence to "this unit writes the protocol section 4 row that leg check 16
requires, the section 7 byte-decision line, and the `--attest` entry of the verbs pair that section
4's paragraph moves into", leaving the companion-guide contract prose with unit 20. Amend unit 16's
to name both edits: the `ASKS_CMD` section 8 row, and the `SPEC_TOKENS_CLI` closing clause removed to
fund it.

**Left-shift gate.** A spec-set sweep, not a code gate: every "writes only" sentence in a section 3
compared against that spec's own Files touched list. Red when: a scope sentence names fewer carriers
than Files touched does.

### M8 — AC3's pointer clause is green because a sibling writes the same string first (35)

**Address.** `memory/builds/dDerivedDocket/spec/2026-09-14-spec-TOOL-dDerivedDocket-20.md`,
section 6 AC3, the `UNATTENDED-ASKS.md` clause.

**What.** Section 4's table pins the greped phrase for S3's pointer sentence as the bare string
`UNATTENDED-ASKS.md`, and AC3 relaxes it to "at least 1" because the `ASKS_CMD` row unit 16 writes
also names it.

**Why it is real.** Unit 16 is order 16 and its section 4 Rollout writes the protocol section 8 row
naming `UNATTENDED-ASKS.md`; unit 20 is order 20. The count in each protocol copy is therefore
already 1 when this unit's pass begins, and AC3 accepts at least 1, so a pass that never writes S3's
pointer sentence passes green. No other clause in unit 20 observes that sentence — AC4 grades the
guide's install and its headings, not the protocol — and AC3's own Red-when claims the greps catch "a
new sentence is absent, which an empty edit under the budget would pass". Unlike unit 17's AC1, the
wording positively ADMITS the state it is meant to refuse. This is the could-not-fail class this
spec's own rev-3 verification pass already repaired twice, in AC2's `MANDATES a backlog row` spanning
a line break and AC3's lower-case `a planned unit is minted…` against the protocol's capital `A`,
left in place for the one phrase a sibling supplies.

**Fix.** Witness S3's pointer sentence with a phrase unique to it — section 4's table already carries
a phrase column for every other row — or assert the count is exactly one MORE at this unit's commit
than at its parent, the parent-comparison shape AC3 already uses for bytes. Update section 9 to stop
recording "at least 1" as the accepted reading.

**Left-shift gate.** The parent-and-commit delta count. Red when: a phrase criterion is satisfied by a
string an earlier unit of the same build already wrote.

### M9 — the grant-path guard declares four negatives and is observed on one (2)

**Address.** `memory/builds/dDerivedDocket/spec/2026-09-14-spec-TOOL-dDerivedDocket-19.md`,
section 6 AC3, against section 2 S3.

**What.** S3 declares four refusals for a grant token — bad id grammar, a leading `/`, a `..`
segment, a backslash — and AC3 exercises the malformed id prefix plus two positive spellings.
Section 7's new-arm list likewise says "a malformed grant", singular.

**Why it is real.** The path half of a grant is what bounds veto 2, "a change confined under that
path", so `/etc/passwd`, `../../other-repo/x` and `tools\push-main.sh` are the tokens that matter
most and none is observed. An implementation that checks the id grammar and then accepts any token
containing a `/` passes AC3 while pinning a grant that points outside the repo, and AC4's leg arm only
compares the pinned fact against the README line, so it AGREES with the bad pin rather than catching
it. Severity is held at MEDIUM rather than raised: section 3 declares veto enforcement to be agent
judgement, so the grant is not a machine confinement and the finder's framing overstated it. The
class is still this repo's own recorded one, containment tested in a single direction.

**Fix.** Extend AC3's fixture set with one `may:` value per refused shape — `/tools/push-main.sh`,
`../x/y.sh`, `tools\push-main.sh`, and a bare token with neither a `/` nor an extension — each
refusing preflight and naming the token.

**Left-shift gate.** A Red-when on AC3 for a guard that admits an absolute or escaping path because it
only tested for a `/`. Red when: any one of S3's four declared negatives is accepted.

## Low

### L1 — no `recipe`-mode arm, where both siblings carry one (11)

**Address.** `memory/builds/dDerivedDocket/spec/2026-09-14-spec-TOOL-dDerivedDocket-18.md`,
section 6 AC8, against section 2 S5.

**What.** S5's predicate is "a record carrying an `asks:` fact must record mode `slug`", and AC8's
fixture carries only `prompt`.

**Why it is real.** `SECOND_ANCHOR_MODES="prompt recipe"` (`tools/unattended/unattended.sh:580`), and
`recipe` resolves at the anchor the run can write, so it is the same hazard. An arm implemented as
`mode = prompt` passes AC8 while a recipe record carrying a pinned mandate goes ungraded — the record
S5 exists to catch, written around the driver. Both sibling criteria for this same predicate carry a
recipe fixture with an explicit Red-when: unit 16 AC16 and unit 19 AC2. Round 1 confirmed exactly this
class twice, as L4 against unit 19 AC2 and H6 against unit 16, and both folded it; unit 18's AC8 is
byte-identical to its round-1 blob, so the fix was applied where the finding was filed and not to the
class. LOW because the harm needs a record written in a mode the driver did not choose.

**Fix.** Add a `recipe`-mode record carrying an `asks:` fact to AC8's fixture set, and name the
one-mode arm in the Red-when: "the refusal keys on `prompt` alone, so a `recipe` record carries a
pinned mandate".

**Left-shift gate.** Whenever a criterion enumerates members of a named constant set, assert the arm
count equals that set's size, read from the constant. Red when: a criterion covers a proper subset of
`SECOND_ANCHOR_MODES` and reads as coverage.

## Does each round-1 fix hold?

This is a fold review, so the question is asked entry by entry. Of the round-1 findings whose fixes
this round could reach:

- **H1 (`--tsv` stdout ownership) — DOES NOT HOLD.** Both clauses landed and the defect survives at
  the consumer. B1.
- **H6 (a non-`slug` README carrying `asks:`) — HOLDS where filed, not as a class.** Units 16 and 19
  gained recipe arms; unit 18's AC8 did not. L1.
- **H7 (the cross-run arm walks only the run's own commits) — HOLDS in its resolution, fails in its
  spelling.** F8's predicate is right; the command section 4 writes for it answers a different
  question. H6.
- **H10 (the scaffold writes `ids:` and `status: OPEN`, AC10 staged end to end) — HOLDS, with a new
  hole beside it.** The slot bodies the fix introduced have no wrap. M5.
- **M9 (S8 re-derives `asks-ready:` and the freeze) — HOLDS in shape, not in coverage.** The two
  forged-pin arms landed; three declared branches and one false premise did not. M1, H4.
- **M11 (generated bodies anchor nothing) — DOES NOT HOLD.** The criterion it produced cannot fail,
  twice over. H2, H3.
- **M18 and M19 (S8's rank, the duplicate closer, the shared next) — DOES NOT HOLD.** The fix folded
  four observations onto one fixture and contradicted section 4. H1.
- **M23 and M25 (carrier content and byte budgets get criteria) — HOLD in part.** The criteria exist;
  three of them are satisfied by states they mean to refuse. M2, M3, M8.
- **L4 (a `recipe` arm and the grant token grammar) — HOLDS for the mode, not for the path.** The
  grammar landed in S3 with four negatives and one of them is observed. M9.

## Left-shift, by class

Five classes carry the nineteen ids, and four of the five are gateable by a sweep rather than by a
new mechanism.

- **A criterion that cannot fail** — H2, H3, M2, M3, M8, and half of H1. Six entries, and the single
  largest class in this build. Every one is a phrase, size or negative assertion that a correct
  implementation and an empty edit both satisfy. The standing fix is the one unit 28 AC13 already
  uses: count a witness phrase at the parent AND at the commit, and require the arm to be SEEN RED
  once. A sweep for criteria whose only mechanized read is `wc -c` or a bare "at least 1" finds the
  rest of this class across the other groups.
- **A declared branch nobody observes** — M1, M4, M9, L1. The charter section 7 rule about skips
  announcing themselves covers the worst of these; the cheap sweep is to count each S-item's declared
  negatives and compare that number against the arms its criterion names.
- **A predicate that does not match its population** — H4, H6, H5. All three are a git or a config
  read used as if it answered a question it does not answer, and all three are the charter's
  run-the-candidate-predicate-over-the-real-tree rule. None was catchable by reading the spec alone,
  which is why this round re-measured them.
- **Prose beside a source that owns the value** — M6, M7. Two folds moved the S-items and left the
  narrative behind. The sweep is mechanical: compare each section 3 "writes only" sentence against
  that spec's Files touched, and each section 4 budget figure against the S-item it prices.
- **A capture that merges two channels** — B1 alone, and it is the one class here that needs a
  decision rather than a gate.

## What this round did not cover

- **The refuted 18.** Not reproduced, per the build's convention. Four of them were refuted on the
  ground that a sibling spec already carries the missing clause, which is a reason to re-read those
  siblings if the fold changes them.
- **Implementation feasibility beyond the cited seams.** Where an entry rests on tool behaviour it
  names the file and line at HEAD, and three entries ran the code. Everything else is judged from the
  spec text.
- **Units outside G3.** Read only where an edge or an interface named them. Unit 28 S1 is quoted in
  B1 and it is a G5 subject; if B1's fold takes option (a), that spec changes and its own group owes
  the re-read.
- **The interaction between H5 and unit 34's switch-over.** This round establishes that the conf is
  an unpinned input; which of unit 34's conf moves actually land before the leg's first re-derivation
  is a question for the G5 and G6 records, not settled here.
