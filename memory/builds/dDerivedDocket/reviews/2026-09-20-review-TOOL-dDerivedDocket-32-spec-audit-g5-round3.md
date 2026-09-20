**Serves:** spec-audit TOOL-dDerivedDocket-32 TOOL-dDerivedDocket-33 TOOL-dDerivedDocket-34 TOOL-dDerivedDocket-35 TOOL-dDerivedDocket-36 PLAY-dDerivedDocket-1 DEPL-dDerivedDocket-1

# dDerivedDocket — spec audit of topic group G5, the switch-over with its CI, arming and docs, round 3

*Node `d`, 2026-09-20. The third Tier-2 adversarial pass over the seven G5 specs: remote CI (unit
32), the delegated signing (33), the switch-over and its landing reconcile (34), arming and the
real-tree staged breaks (35), the memory-tree docs and agent carriers (36), the charter template
(PLAY-dDerivedDocket-1) and the adopter runbook (DEPL-dDerivedDocket-1). This is a FOLD review,
regrounded on `fb07ca25`: origin/main moved 210 commits past the original BASE `abac6d59`, HEAD
merges it in, and every spec re-verified its claims there and moved its header base under a section
9 line reading `regrounded on fb07ca25`. Code claims below are judged at HEAD. The pass was aimed at
the text nobody has reviewed — every section 9 line dated after the round-2 record, which for this
group is each spec's rev-3 and the regrounding revs of 2026-09-16 and 2026-09-20 — and at whether
each round-2 fix holds. Four primed finder lenses ran and all four returned; a skeptic stage
prompted to REFUTE each finding ran in five batches and all five returned; then this synthesis. The
sources were the ratified design record
`memory/builds/dDerivedDocket/build/2026-09-14-build-TOOL-dDerivedDocket-1-design.md`, the owner
mandate `memory/builds/dDerivedDocket/prompts/2026-09-14-prompt-TOOL-dDerivedDocket-1-owner-mandate.md`,
the spec brief `memory/builds/dDerivedDocket/prompts/2026-09-14-prompt-TOOL-dDerivedDocket-1-spec-brief.md`
with its roster and edge tables, and the round-2 record
`memory/builds/dDerivedDocket/reviews/2026-09-14-review-TOOL-dDerivedDocket-32-spec-audit-g5-round2.md`.
Sibling specs outside G5 were read wherever an edge or an interface named them. Every finding below
was re-checked against source at HEAD before it was written down, and the sites read are named in
each entry; where a claim rests on a tool's behaviour rather than on its text, the probe that
measured it is given with its output.*

**Round: 3.** Range at base `fb07ca25`, each subject pinned at the blob it was read at: `memory/builds/dDerivedDocket/spec/2026-09-14-spec-TOOL-dDerivedDocket-32.md@3df8aeb00067b297c5a1d44069076bf54086401b`, `memory/builds/dDerivedDocket/spec/2026-09-14-spec-TOOL-dDerivedDocket-33.md@26067903dbd70672d6d1fb85f075d0060d510b8a`, `memory/builds/dDerivedDocket/spec/2026-09-14-spec-TOOL-dDerivedDocket-34.md@03f7b9c70051b9d273c3981526c2c88938dc57f1`, `memory/builds/dDerivedDocket/spec/2026-09-14-spec-TOOL-dDerivedDocket-35.md@7489694e31f0157947c8e381ef139af9255efabc`, `memory/builds/dDerivedDocket/spec/2026-09-14-spec-TOOL-dDerivedDocket-36.md@46d4d27990ec5e66f04d7b58f089e6f84d6da803`, `memory/builds/dDerivedDocket/spec/2026-09-14-spec-PLAY-dDerivedDocket-1.md@ab0da00747147b619154d9feb72981c9411838c1`, `memory/builds/dDerivedDocket/spec/2026-09-14-spec-DEPL-dDerivedDocket-1.md@dbd3b051685b1a3c5cc26cd081f3427d223ff92a`

## Verdict: CLEAN WITH FIXES

No blocker stands, and round 2's six HIGH defects are all folded. What stands is three HIGH defects
carried by four finding ids, and six MEDIUM defects carried by six. No LOW defect survived the
skeptic stage.

The one defect that would break a shipped artefact on its first live run is H1: unit 32 pins the
`core.autocrlf false` step by its POSITION and never by its git config SCOPE, and a repo-local
`git config` in the pre-checkout workspace is fatal. Measured at HEAD on git 2.54.0.windows.1, that
command in a non-repo directory prints `fatal: not in a git directory` and exits 128, so a
repo-scoped implementation fails the first step of every job on every push while all fourteen of the
unit's criteria stay green.

The other two highs sit in unit 34's landing reconcile, which is where round 1's and round 2's
weight sat too, and both are in text written on 2026-09-20 that no round has seen: reconcile step 6
and AC29 were added by rev-5. H2 is that step 6 raises a moved kit's version by walking
`tools/check-kit-versions.sh`'s carrier list, which for memory-tree excludes the four renders under
`memory/` carrying the same marker, so the raise reds `kit/dogfood doc parity` mid-merge, outside
any unit pass and after the closing review. H3 is that step 1's conflict — the refusal steps 2 to 7
are built on — needs `merge.rows.driver` configured in the tree running the merge, which is
per-clone and untracked, and neither the step nor AC15's fixture asserts it; the sibling spec, unit
35 S2, states exactly that prerequisite for its own clone.

Three of the six mediums are unobserved contract properties in unit 32 and unit 36 — a property the
scope section declares and no criterion reads — which is the same class round 2 confirmed there as
M13 and the spec folded into AC1, AC2 and AC4. Two more are carrier lists that are not marker sets,
the same root as H2 one kit over. The last is unit 35's acceptance ledger, which no rollout step
commits, graded by a hygiene leg that enumerates its corpus from the index.

**Convergence** under `memory/guides/BUILD-METHOD.md` M4: confirmed findings fell from 39 to 10, the
blocker count held at 0, and the high count fell from 6 defects (9 ids) to 3 defects (4 ids). Every
count moved strictly down, so by the loop's own measure this group has converged. The prescribed act
is to fold and stop spec-auditing these seven specs; the rev-4/rev-5 fold text meets the closing
diff review, which should take the section 9 lines dated 2026-09-20 as its index and read unit 34's
reconcile step 6 first.

**Disposition, and it needs a call.** `.unattended.conf` declares `REVIEW_ROUNDS="1"`, which this
round already exceeds, so M4's exit rule applies now: a confirmed HIGH is PROMOTED to a unit whose
mechanism closes it, a confirmed MEDIUM is FOLDED as a rev bump. All three highs here are
paragraph-sized spec edits with no new mechanism behind them — H1 adds a flag and an arm, H2 widens
a list, H3 adds a precondition — so promoting each to its own unit would mint three units to carry
three sentences. The orchestrator should decide whether these three take the FOLD disposition
despite their severity, and record the decision; this record does not make that call for it. H2's
left-shift, unlike H2 itself, IS unit-shaped and is described under Left-shift below.

## Run integrity

- Lenses: 4 of 4 returned, 0 DIED.
- Skeptic batches: 5 of 5 returned, 0 DIED.
- Contradictory verdicts demoted to unverified: 0. Spurious verdicts discarded: 0. Duplicates: 0.
- Unverified findings: 0.

This run is COMPLETE. Every lens reported and every finding reached a skeptic, so a zero count below
is evidence rather than an artefact of a missing lens. Two ids, 2 and 12, describe one defect at two
severities and are merged into H2; the pipeline's duplicate count of 0 comes from its own
exact-match dedupe, which does not see a restatement.

## Review shape

Raw 29, confirmed 10, refuted 19, unverified 0. Precision 0.34, below the ~0.5 floor charter section
8 sets: a further round over this group would need tighter lens priming or a narrower scope before
it added agents, which is a second reason beyond convergence not to run one. The 19 refuted findings
are not reproduced here.

Adjudicated tally, stated both ways, because merged items and raw ids do not agree:

| Severity | Items | Raw confirmed ids |
|---|---|---|
| BLOCKER | 0 | 0 |
| HIGH | 3 | 4 |
| MEDIUM | 6 | 6 |
| LOW | 0 | 0 |
| Total | 9 | 10 |

Where the weight sits, by subject: unit 32 carries four ids, unit 34 four, unit 35 one and unit 36
one. Units 33, PLAY-dDerivedDocket-1 and DEPL-dDerivedDocket-1 carry none.

## Round-2 fixes: what this round found against them

All six round-2 highs hold as folded, and this round found no defect in five of the six fixes.

- **H1**, step 1 naming `--prepare`, which merges the other way and aborts on the conflict step 1
  resolves. Fixed: step 1 is now the manual `git merge --no-ff --no-commit <tip>` that unit 2's
  refusal names, with a new step 8 running `--prepare` over a branch that already contains the tip,
  and AC15 stages `--prepare`'s refusal first. The fix is sound. It does, however, leave the merge's
  own prerequisite unstated, which is H3 below — the fix moved the mechanism into the spec's hands
  and the configuration it needs did not come with it.
- **H2**, the confirmation rule reading text. Fixed: section 4 Confirmation now derives `<switch>`
  and `<fork>` by command, and "acted on" became a `BACKLOG.md` record targeting the id rather than
  a line naming it. No finding this round.
- **H3**, AC3's "zero differing ids". Fixed by naming the two exceptions. No finding this round.
- **H4**, the two asks the fold filed with nothing to dispose them. Fixed in unit 35 S9 and AC8. The
  ledger that records the arming REDs, which the same rollout carries, is the subject of M6 below;
  that is a different defect in the same rollout, not a failure of H4's fix.
- **H5**, AC12 expecting a DRIFT line that names a key. Fixed: AC12 keeps the bare DRIFT line and
  adds the write-mode read. No finding this round.
- **H6**, unit 35 setting the hooks path with a mode that writes nothing. Fixed: S2 and rollout step
  3 now run `check-wiring.sh --fix`, and S2 spells why. Worth noting for H3: that same S2 paragraph
  also wires `merge.rows.driver` in its scratch clone, "since a clone copies no local config" — the
  build knows the fact, states it in unit 35, and unit 34's fixture does not carry it.

Round 2's mediums are not re-audited line by line here. Two of them are visibly re-opened one level
up rather than broken: M13's unobserved-property class returns as M1, M2 and M5, and M8's
version-move class returns as H2 and M4.

## Findings index

| # | Ids | Severity | Subject | One line |
|---|---|---|---|---|
| H1 | 19 | HIGH | unit 32 | the autocrlf step is pinned by position, never by config scope, and is fatal outside a repo |
| H2 | 12, 2 | HIGH | unit 34 | step 6's landing kit raise walks a carrier list that excludes four live renders |
| H3 | 20 | HIGH | unit 34 | step 1's conflict needs `merge.rows.driver`, and neither the step nor its fixture wires it |
| M1 | 1 | MEDIUM | unit 32 | S3's `checkout -B main <sha>` is read by no criterion, so nothing observes the per-sha verdict |
| M2 | 5 | MEDIUM | unit 32 | two of S4's four plan-job refusals have no arm anywhere in the spec |
| M3 | 14 | MEDIUM | unit 32 | S7's trim destination is inside the install-prefix gate's population, and nothing budgets a row |
| M4 | 18 | MEDIUM | unit 34 | memory-recall ships a third marker that nothing raises and no criterion reads |
| M5 | 3 | MEDIUM | unit 36 | AC8's render read covers one render of four, against S7's own "and its render" |
| M6 | 7 | MEDIUM | unit 35 | the acceptance ledger is never committed, and the hygiene read over it is unordered |

## High

### H1 — the `core.autocrlf false` step is specified by position and never by scope, and outside a repository that command is fatal (19)

**Where.** `memory/builds/dDerivedDocket/spec/2026-09-14-spec-TOOL-dDerivedDocket-32.md`, section 2
S1 and S5, observed by section 6 AC1.

**What.** S1 says every job's checkout comes "after a step setting `core.autocrlf false`". S5's
contract list says "the autocrlf step precedes each checkout and the `bar` job's clone". Both pin
the step's PLACE in the job and neither pins the git config SCOPE it writes at. On a GitHub runner
that step runs in `$GITHUB_WORKSPACE`, which exists and is empty before `actions/checkout`
initialises a repository there — that is the whole point of putting the step first, so the checkout
cannot smudge CRLF. A bare `git config core.autocrlf false` in a directory that is not inside a
repository does not write a file; it fails.

**Why it is real.** Measured at HEAD on this node, git 2.54.0.windows.1:

```
$ mkdir nonrepo_probe && cd nonrepo_probe && git config core.autocrlf false
fatal: not in a git directory
exit=128
```

So scope is load-bearing here, and only `--global` (or `--system`) can work in a pre-checkout
workspace. The spec pins comparably fine-grained YAML properties everywhere else — `fetch-depth: 0`,
`persist-credentials: false`, `git remote set-head origin main`, `if-no-files-found: error` — so
this is not an altitude question about how much detail a spec owes.

Nothing in section 6 can see it. AC1's only autocrlf arm is placement, and its staged break is "the
autocrlf step moved after a checkout"; it reads neither a scope flag nor the step's exit. AC4 reads
`GATE_WALL`, `timeout-minutes` and `permissions`. AC12 runs render and drift commands by hand in a
runner-shaped clone. AC13 reads `on:` and each job's `if:`. AC14 runs synthetic held-matrix argv in
a local Git-Bash shell. Section 3 states that the workflow's first live run happens after landing
and that no criterion depends on it, and section 8 F2 resolved that the file is observed only by
staged breaks recorded in the journal. A repo-scoped implementation therefore fails the first step
of all four jobs on every push, on the schedule and on dispatch, while the unit closes green — and
the first signal is a wall of red CI runs after the landing, on the one layer D11-b added precisely
because no node can skip it.

**Fix.** Spell the step in S1 and S5 as a GLOBAL write, `git config --global core.autocrlf false`,
and say why a repo-local write cannot work before `actions/checkout` initialises the workspace. Add
an AC1 arm reading the step's scope flag, with a staged break that drops `--global` and a Red-when
naming the exit-128 case. The arm costs nothing: it is a grep over the same scratch copy AC1 already
makes.

**Left-shift.** Section 8 F2 already records option (b), a permanent repo-subject contract gate over
the workflow file, as an ADD candidate under M2's amendment acts. This finding, with M1 and M2
below, gives that candidate four concrete properties to read that a staged-break list keeps missing.
When the ADD candidate is written, derive its property list from S5 rather than retyping it, and
give it one arm that runs the workflow's first step in an empty directory — a contract gate that
never executes a line of the file it grades is the same class one level up.

### H2 — the landing kit raise walks a carrier list that excludes four live renders (12, 2)

**Where.** `memory/builds/dDerivedDocket/spec/2026-09-14-spec-TOOL-dDerivedDocket-34.md`, section 4
"The landing reconcile" step 6, with section 2 S15 and section 6 AC29. Both the step's kit-re-check
paragraph and AC29 were added by rev-5 on 2026-09-20 and have not been reviewed before.

**What.** Step 6 says the re-check reads "every kit version this build moved against `<tip>`, across
the carriers `tools/check-kit-versions.sh` names for that kit", and binds itself to that list
explicitly: "the step walks `tools/check-kit-versions.sh`'s carrier list rather than a list written
here". AC29's fourth arm spells the memory-tree carriers the same way — "the
`KIT_MEMORY_TREE_VERSION` constant and its `tools/memory-tree/*.template.md` markers" — and then
grades the whole step with `bash tools/check-kit-versions.sh` exiting 0. Memory-tree is named in
scope at order 36.

**Why it is real.** Reproduced at HEAD in this worktree. `tools/check-kit-versions.sh:130-147`
derives memory-tree's carriers as the `KIT_MEMORY_TREE_VERSION` constant in
`tools/memory-tree/check-memory-hygiene.sh` plus `git ls-files 'tools/memory-tree/*.template.md'`.
That glob resolves to four files and nothing under `memory/`:

```
tools/memory-tree/ANNOTATION-STYLE.template.md
tools/memory-tree/BUILD-METHOD.template.md
tools/memory-tree/HYGIENE.template.md
tools/memory-tree/SPEC-TEMPLATE.template.md
```

Four live renders carry the same marker at the same value and are read by that script nowhere:
`memory/HYGIENE.md:1`, `memory/TEMPLATE-SPEC.md:1`, `memory/guides/ANNOTATION-STYLE.md:1` and
`memory/guides/BUILD-METHOD.md:1`, all `<!-- gov:kit memory-tree@2.78 -->`.
`tools/memory-tree/kit-dogfood-parity.test.sh:58` pairs all four renders with their templates and
byte-compares the rendered template against the live copy, marker line included.

So an instructed landing-time memory-tree raise moves five files, leaves four renders at the
branch's value, still exits 0 under `bash tools/check-kit-versions.sh`, and reds `kit/dogfood doc
parity`. That leg's guard in `tools/gate-legs.json` names `tools/memory-tree/` and those very
renders, so the merge commit triggers it. The red lands at the landing bar, mid-merge, after the
closing review and outside any unit pass, in a merge that must conclude. AC29's positive arm is
written against the same wrong list, so it cannot observe the miss — the guard shares its variable
with the thing it guards.

This repo has already paid for this exact defect twice. `memory/backlog/TOOL.md` row
TOOL-dSettledRoster-4 records it on 2026-08-20 and again on 2026-08-21, with the remedy stated:
"Derive the list from the markers."

**Fix.** Make step 6 raise every tracked `gov:kit <kit>@` marker for a moved kit rather than only the
carriers `check-kit-versions.sh` names, and have it re-render the live copies with
`bash tools/memory-tree/kit-dogfood-parity.test.sh --render` inside the merge commit. Extend AC29's
fourth arm to assert that after the memory-tree raise the marker in each of the four renders equals
the constant, or equivalently that `bash tools/memory-tree/kit-dogfood-parity.test.sh` exits 0 over
the merged tree, and add the stale-render case to its Red-when.

**Left-shift.** This one is unit-shaped and closes H2, M4 and M5 together. Extend
`tools/check-kit-versions.sh` so each kit's carrier population is DERIVED from the markers —
`git grep -o 'gov:kit <kit>@[0-9][0-9.]*'` over `git ls-files`, every hit asserted against that
kit's constant, with an empty population a refusal rather than a pass, which is the posture the
memory-tree block's own header already argues for its templates. Then no spec ever has to name a
carrier list again, the next shipped carrier is covered by existing, and backlog row
TOOL-dSettledRoster-4 can be closed by the mechanism it asked for.

### H3 — step 1's conflict needs `merge.rows.driver`, and neither the step nor its fixture wires it (20)

**Where.** `memory/builds/dDerivedDocket/spec/2026-09-14-spec-TOOL-dDerivedDocket-34.md`, section 4
"The landing reconcile" step 1, and the fixture line of section 6 AC15.

**What.** Step 1 says "the row driver refuses on each view and the merge stops conflicted", and the
paragraph above it derives the entire reconcile from that refusal, citing unit 10 S2. Steps 2 to 7
run inside that conflicted merge. AC15's fixture is "a scratch repository with a local bare remote,
built in the pass", with no driver wiring, and AC24, AC25, AC28 and AC29 all reuse that fixture.

**Why it is real.** `merge=rows` in `.gitattributes` does nothing unless `merge.rows.driver` is set
in git config, which is per-clone and untracked. Both sources at HEAD say the fallback is silent:
`.gitattributes:61` says an unconfigured node "falls back to git's built-in three-way text merge",
and `tools/check-wiring.sh:861` says an unset driver means "git falls back to a line merge that can
duplicate a row". With the driver unset, the scratch merge COMPLETES rather than conflicting: the
tip's shards line-merge into the branch's generated views, step 1 has nothing to resolve, and the
rehearsal that exists to prove the refusal exercises the opposite path — while every downstream
expectation in AC15 (dispositions, the cutoff, `gen_build_index.py --check` over regenerated views)
still appears reachable, so the arm can pass and certify nothing about the mechanism it names.

The build knows the prerequisite and states it one spec over. Unit 35 S2 wires `merge.rows.driver`
in its scratch clone "since a clone copies no local config", and unit 10 S8 drives its arms "through
a real `git merge` in a scratch repository with the driver wired", with its non-goals handing node
configuration to check-wiring. Unit 34 omits it. This is not a house convention being followed; it
is an inconsistency inside the build. DEPL-dDerivedDocket-1 step 6 copies the same procedure for
adopters, where the driver is less likely to be wired than it is here.

**Fix.** Add to step 1 a precondition that `git config merge.rows.driver` resolves in the tree about
to merge — `bash tools/check-wiring.sh --check`, stopping when it reports `UNWIRED merge`, or
`--fix` — and add the same wiring line to AC15's fixture clause. Give AC15 a Red-when for a
driverless fixture merging clean, which is the mutation arm that proves the fixture can fail at all.

**Left-shift.** The class is "a fixture that does not carry the configuration the behaviour under
test needs", and it is gateable inside the rehearsal rather than in prose: have the fixture builder
assert the driver resolves before it makes the merge, and have the arm assert that the merge
CONFLICTED before it asserts anything about the resolution. Beyond this build, the durable form is a
gotcha — a per-clone git config that a tracked `.gitattributes` depends on is invisible to every
scratch fixture by construction, and this is the second mechanism in this build (after the hooks
path, round-2 H6) to trip on it.

## Medium

### M1 — S3's sha pin is read by no criterion, so nothing observes that the bar job grades the pushed sha (1)

**Where.** `memory/builds/dDerivedDocket/spec/2026-09-14-spec-TOOL-dDerivedDocket-32.md`, section 2
S3, against section 6 AC1, AC4, AC10, AC12 and AC13.

**What.** S3's `bar` job clones with a plain anonymous `git clone` and then runs
`git checkout -B main <sha>`. Because the job does not use `actions/checkout`, that checkout is the
only thing making the verdict per-sha, and a per-sha verdict is the job's whole purpose (D12-i12);
section 4's triggers table publishes it as `bar-<sha>`. No criterion reads the checkout.

**Why it is real.** Verified against the spec. AC12 reads only the clone PATH
(`C:/projects/coding-governance`) plus the render and drift behaviour in a runner-shaped clone. AC1
reads fetch-depth, persist-credentials, autocrlf placement, set-head, the symref assertion, the
runner, the shell and the absence of `secrets.` in the clone URL. AC4 reads `GATE_WALL`,
`timeout-minutes` and `permissions`. AC10 reads the copy and upload steps. AC13 reads `on:` and each
job's `if:`. S5's staged-break contract list — the spec's own catch-all for file properties —
enumerates ten properties and the sha pin is not among them, and section 4's "Why one file"
discusses only the clone path.

A plain `git clone` takes the branch tip at clone time, so on a busy push window the `bar` job can
validate a later commit than the one its check run is attached to, and a workflow whose clone step
simply omits the checkout passes all five criteria and publishes a green verdict against a tree
nobody pushed. That is the class `.githooks/pre-push` already guards against by requiring the
validated tree to be the pushed tip. Same unobserved-contract-property class that round 2 confirmed
here as M13.

**Fix.** Add to AC1 — which already reads the clone step's other properties — a read that the `bar`
job's clone is followed in the same job by a checkout pinning the event's sha, with one staged break
on the scratch copy deleting the checkout line, and name the failure in AC1's Red-when as a per-sha
verdict earned at a tree the push never named.

**Left-shift.** Same gate as H1: the F2(b) contract-gate ADD candidate, with its property list
derived from S5 rather than retyped. S5 is the list that is supposed to be complete, so the durable
fix is a check that S5 and the criteria cover the same property set, not a longer S5.

### M2 — two of S4's four plan-job refusals have no arm anywhere in the spec (5)

**Where.** `memory/builds/dDerivedDocket/spec/2026-09-14-spec-TOOL-dDerivedDocket-32.md`, section 2
S4, against section 6 AC5.

**What.** S4 declares four refusals for the `held-plan` job: a row that does not parse, a parsed
count differing from the `row(s)` figure `--list` prints, a `--kit "<argv>" --list` selecting
anything but that one row, and entries exceeding the platform's 256-entry matrix limit. AC5 stages
two breaks — one entry dropped, and one key shortened to a bare directory — which map to the count
refusal and the one-row refusal. The unparseable-row refusal and the matrix-limit refusal have no
arm.

**Why it is real.** Verified by grep over the whole spec: `256` and "does not parse" occur only in
S4, and no criterion in section 6 mentions either. The one-row check does not substitute for the
parse refusal, because `--kit` is a substring filter (section 4, and section 8 F6): a truncated or
mis-parsed argv is still a substring of its own row, selects exactly that one row, and passes both
of AC5's reads — while the daily held job runs a command that is not the suite's. A derivation that
silently DROPS a row it cannot parse is caught by the union check only when the dropped row is also
absent from `--list`; a row it mis-parses into a plausible argv passes the union by name.

The 256-entry refusal is the charter's assertion-about-nothing shape: 63 rows never approach the
limit, so the guard is declared with no way to fire and no synthetic-population arm. A gate nobody
has seen red is a gate nobody has seen.

**Fix.** Extend AC5 with two scratch-copy arms: a `--list` fixture holding one row the parser cannot
read, where the plan job reds naming the row rather than emitting 62 entries; and a fixture whose
row count exceeds 256, where it reds naming the limit. If the second cannot be reached cheaply,
state in S4 that the limit check is unstaged and why, so a green plan job is not misread as a
verified one — a skip that announces itself is coverage information, and a silent one is not.

**Left-shift.** The plan job's own refusals are the right place for a self-check: have the
derivation take a `--selftest` flag that runs its parser over a fixture of malformed and oversized
rows, so the class is gated in the deriving code rather than in a workflow YAML nobody can run
locally. Failing that, the same F2(b) contract gate.

### M3 — S7's trim destination is inside the install-prefix gate's population, and nothing budgets a row (14)

**Where.** `memory/builds/dDerivedDocket/spec/2026-09-14-spec-TOOL-dDerivedDocket-32.md`, section 2
S7 and section 4 Files touched, against section 7 Gates.

**What.** S7 trims two sentences from `AGENTS.md`'s merge-bar section and MOVES the one fact the kit
README does not carry into `tools/unattended/README.md`. That file is a shipped kit doc inside the
install-prefix gate's population. Section 7 names no `install-prefix (shipped surface)` leg, and no
criterion reads the carried-prefix registry.

**Why it is real.** Verified end to end at HEAD. `install-prefix (shipped surface)` is an UNGUARDED
`subject = repo` leg in `tools/gate-legs.json`, so it runs on every bar;
`tools/check-install-prefix.sh:153` builds its population from `git ls-files -- 'tools/*' 'skills/*'
…`, and it does grade kit READMEs — `tools/agent-instructions/README.md` carries a row of 4 and
`tools/drift-audit/README.md` a row of 4 in `tools/install-prefix-carried.txt`.
`tools/unattended/README.md` carries ZERO `tools/` occurrences today and has NO row at all, while
every other tracked file in that kit does.

The sentence S7 moves reads, in `AGENTS.md` at HEAD: "Its `*.test.sh` legs left both
`tools/gate-legs.json` and the kit's own `kit.toml`, so adopters stop receiving them too." That is a
`tools/` literal, and `tools/gate-legs.json` counts under the gate's `(loose)` kit. The registry's
own header states that `--write-ratchet` can no longer ADD a row or RAISE a count, so the remedy is
reserved to a person writing a row in the pass that needs it. AC8 only requires
`grep -c 'adopters stop receiving' tools/unattended/README.md` to print at least 1, which a verbatim
move satisfies while ROSE-ing the leg at the post-build bar, with no pass of this unit left to fix
it. Unit 32 mentions `install-prefix`, the carried list and literals nowhere — grep over the spec
returns nothing.

The same build prices this exact class elsewhere: DEPL-dDerivedDocket-1 carries a dedicated S7, an
AC7 reading `bash tools/check-install-prefix.sh` for no `ROSE`, the leg in its section 7, and a
budgeted hand-raise of the `WIRE-INTO-PROJECT.md` row with a dated reason. So the omission is an
inconsistency inside the build rather than a style call.

**Fix.** Either state in S7 that the moved sentence spells no `tools/<kit>/` or loose `tools/`
literal — deriving or eliding the descriptor's path — and have AC8 assert
`grep -c 'tools/' tools/unattended/README.md` prints 0; or add `install-prefix (shipped surface)` to
section 7 and a criterion reading that file's row in `tools/install-prefix-carried.txt`, raised by
hand with a dated reason as DEPL's S7 does.

**Left-shift.** No new gate is needed — the leg exists and is unguarded. What is missing is the
rule that any unit moving prose INTO `tools/**` names that leg in its section 7 and prices a row if
the prose carries a path. That belongs in `memory/TEMPLATE-SPEC.md`'s gate-selection guidance, where
it costs one line and reaches every future spec, rather than in this unit.

### M4 — memory-recall ships a third marker that nothing raises and no criterion reads (18)

**Where.** `memory/builds/dDerivedDocket/spec/2026-09-14-spec-TOOL-dDerivedDocket-34.md`, section 2
S9 and the section 4 recall row of "What the one commit carries", observed by section 6 AC27 and
AC29.

**What.** S9, the section 4 recall row, AC27 and AC29 each name exactly two carriers for the
memory-recall move: "the constant and its `gov:kit memory-recall@` README marker". The kit ships a
third marker inline.

**Why it is real.** Verified against the tree. `tools/memory-recall/recall_conf.py` carries
`gov:kit memory-recall@1.8` in its module docstring at line 4 AND
`KIT_MEMORY_RECALL_VERSION = "1.8"` at line 39, with the third at `tools/memory-recall/README.md:3`.
`tools/check-kit-versions.sh:200-206` pairs the constant with the README marker only, so the inline
one is ungraded there — unlike the unattended block immediately below it, which pairs every same-line
marker precisely because "same line is NOT same value" is a recorded defect. AC27 diffs
`recall_conf.py` but asserts only that the constant moved, and both AC27 and AC29 scope their
comparison to "each carrier `tools/check-kit-versions.sh` names". Following the spec as written
therefore leaves the shipped file self-identifying as the version it just left, one line above the
constant that disagrees with it, and that stale number ships into every adopting tree.

**Correction to the finding as filed, and it lowers the severity.** The finding claimed no leg
anywhere can see this. That is false: `tools/memory-recall/selftest.py:1308-1320`,
`test_version_marker`, reads the markers in BOTH `README.md` and `recall_conf.py` and asserts each
equals the constant. That leg is `memory-recall kit selftest`, `chunk: selftests`, `subject: kit` —
HELD on a plain bar, guarded on `tools/memory-recall/`, which the bump touches. So the defect is
caught by the post-build `GATE_FULL=1 GATE_SELFTESTS=1` run this build owes as kit work, not by the
ordinary bar, and unit 34's section 7 does not list that leg. The cost is a post-build red outside
any unit pass, not a shipped stale marker — provided the held run actually happens.

**Fix.** Name the third carrier in S9 and the section 4 recall row, and extend AC27's assertion to
require that `git grep -o 'gov:kit memory-recall@[0-9][0-9.]*' -- tools/memory-recall/` prints the
moved value and no other. Make AC29's step-6 arm read the same set rather than the constant-plus-README
pair. Add `memory-recall kit selftest` to section 7 with the held-leg note unit 36's section 7
already models.

**Left-shift.** H2's derived-carrier change to `tools/check-kit-versions.sh` closes this one too:
derive each kit's marker population from the tree, and the inline docstring marker is covered by
existing rather than by a second implementation inside a held kit selftest.

### M5 — AC8's render read covers one render of four, against S7's own "and its render" (3)

**Where.** `memory/builds/dDerivedDocket/spec/2026-09-14-spec-TOOL-dDerivedDocket-36.md`, section 6
AC8, against section 2 S7 and section 4 Files touched.

**What.** S7 says the constant and "the `gov:kit memory-tree@` marker on every tracked
`tools/memory-tree/*.template.md` and its render move together", and Files touched spells it "in
each `tools/memory-tree/*.template.md` and in its render under `memory/`". AC8 greps the four
templates as a glob, then reads exactly one render, `memory/guides/BUILD-METHOD.md`.

**Why it is real.** There are four templates and four renders at HEAD, all at 2.78 (paths and
markers listed under H2). A bump that moves the constant and all four templates but leaves
`memory/HYGIENE.md`, `memory/TEMPLATE-SPEC.md` or `memory/guides/ANNOTATION-STYLE.md` at the old
value passes AC8's grep, passes `tools/check-kit-versions.sh`, which reads no render, and reds
`kit/dogfood doc parity` at the post-build bar — the same post-build red AC8's own Red-when says it
exists to pre-empt, in the same sentence that describes the hazard generically ("a stale render is
byte-identical"). Section 3's non-goals hand the hygiene-engine unit the PROSE of `memory/HYGIENE.md`
and `memory/TEMPLATE-SPEC.md`, not the marker — S7 makes memory-tree's one move this unit's, the
build's declared exception — and `memory/guides/ANNOTATION-STYLE.md` is withheld by no non-goal at
all. AC5's three parity commands are memory-recall, drift-audit and review-protocol, not the
memory-tree pair.

The containment, stated so the severity is not misread: unit 36's section 7 DOES list
`kit/dogfood doc parity`, and that leg is `subject = repo` with a guard naming `tools/memory-tree/`,
so it runs on the post-build bar and the miss is caught inside the build. The cost is a red at the
wrong moment, not a shipped defect. That is also exactly why this is a criterion widened for a
hazard and then applied to one instance of four — gate the class, not the instance, one level up
from the fix that prompted it.

**Fix.** Replace AC8's single-render grep with one over the render set —
`git grep -h -o "gov:kit memory-tree@[0-9][0-9.]*" -- memory/HYGIENE.md memory/TEMPLATE-SPEC.md
memory/guides/ANNOTATION-STYLE.md memory/guides/BUILD-METHOD.md` prints the new value and no other —
and keep the byte and line reads on `BUILD-METHOD.md` alone, since it is the only capped carrier.

**Left-shift.** H2's derived-carrier change again, plus the cheaper local form: have AC8 run
`bash tools/memory-tree/kit-dogfood-parity.test.sh` in the pass rather than naming render paths, so
the criterion reads the same pair list the leg does and cannot fall behind it when a fifth template
ships.

### M6 — the acceptance ledger is never committed, and the hygiene read over it is unordered (7)

**Where.** `memory/builds/dDerivedDocket/spec/2026-09-14-spec-TOOL-dDerivedDocket-35.md`, section 4
Rollout steps 4 and 5, against section 2 S8 and section 6 AC7.

**What.** The rollout has five steps and only step 2 commits, carrying the conf, the KEEP rows and
the re-stamp. The acceptance-ledger journal is a declared tracked write — Files touched names it —
that gains three REDs at step 4 in the pass and two more at the deferred VERIFYING staging, with no
commit or stage step anywhere after step 2. AC7 asserts that `check-memory-hygiene.sh` "names no
orphan id in the ledger that copied the REDs", and its permission line defers that reading over the
real tree to "the one post-build bar".

**Why it is real.** `tools/memory-tree/check-memory-hygiene.sh` enumerates its corpus from the index
— `git ls-files` at lines 219, 1902 and 2015 — so an uncommitted and unstaged ledger is invisible to
check 14. AC7's arm and its Red-when ("a fixture carried a real-family id") cannot fire over content
that is not in the index: the could-not-fail shape charter section 7 names. This is the class
`memory/gotchas/gates-see-only-tracked-files.md` already records.

The ordering half holds independently. S2 defers S6's and S7's breaks to "the one post-build run the
orchestrator makes at VERIFYING", and AC7 defers the hygiene read to "the one post-build bar" — the
same run at which those two REDs are still being staged and copied into the ledger. Nothing in S2,
S8, AC5, AC6 or AC7 orders the copy before the leg, so the leg can grade ledger content that is not
the content that ships.

Unit 34's rollout step 12 commits its acceptance ledger explicitly, so the omission is not a house
convention this unit is following.

**Fix.** Add a rollout step after the deferred staging that commits the completed ledger, and state
in AC7 that the `memory hygiene` reading is taken after that commit. If the bar must run first, say
so and add a second hygiene read over the ledger's final content.

**Left-shift.** The gateable form is already half-built: `asks-disposed` and V10 grade this build's
records at its close. Add to the memory-tree hygiene engine a check that a build folder's acceptance
ledger is TRACKED when its build README reads VERIFYING or later — an untracked ledger is the one
state in which every ledger-reading check passes vacuously. Cheaper interim: make "stage before the
hygiene read" an explicit line in `memory/TEMPLATE-SPEC.md`'s rollout guidance, since this is the
second build to trip on the index-enumeration fact.

## Left-shift, by class

Four classes carry the ten ids, and two of them collapse into one gate.

1. **The carrier list that is not the marker set** — H2 (12, 2), M4 (18), M5 (3). Six of the ten ids
   by weight, across three specs and two kits. One change closes all three: derive each kit's
   carrier population inside `tools/check-kit-versions.sh` from
   `git grep -o 'gov:kit <kit>@[0-9][0-9.]*'` over `git ls-files`, assert every hit against that
   kit's constant, and make an empty population a refusal. The memory-tree block's own header
   already argues this posture for its templates and stops at the tree boundary; extending it past
   that boundary is the whole fix. It also closes `memory/backlog/TOOL.md` row TOOL-dSettledRoster-4,
   which recorded this defect twice in two days and prescribed exactly this remedy. This is the one
   left-shift here that is genuinely unit-shaped.
2. **The declared property no criterion reads** — H1 (19), M1 (1), M2 (5), and M5's render read.
   Unit 32's section 8 F2 already carries the contract-gate ADD candidate; these findings give it
   its property list. The rule that makes the class stop recurring is that the staged-break contract
   list in S5 and the criteria in section 6 must cover the SAME set, checked once at fold time
   rather than discovered one property at a time by successive review rounds. H1's arm additionally
   has to EXECUTE the step, not read it: every criterion that reads YAML properties was blind to a
   command that exits 128.
3. **The fixture that cannot reach the behaviour it grades** — H3 (20), and M6's index-blind hygiene
   read (7). Both are "the check ran, over a tree in which it could not fail". The general gate is a
   liveness assertion inside each rehearsal: assert the PRECONDITION (driver resolves, ledger
   tracked) and assert the NEGATIVE transition (the merge conflicted, the id was visible) before
   asserting the outcome. Charter section 7 already requires a probe that cannot move to say so; the
   rehearsals in this build do not yet carry that assertion.
4. **The shipped-surface literal with an owner-reserved remedy** — M3 (14). The leg exists and is
   unguarded; only the spec's awareness is missing. One line in `memory/TEMPLATE-SPEC.md`: a unit
   that writes prose into `tools/**` names `install-prefix (shipped surface)` in its section 7 and
   budgets a registry row if that prose carries a path.

## What this round did not cover

- **No criterion of any G5 spec was executed.** This is a spec audit: the specs are read against
  each other, against the design and the mandate, and against source at HEAD. `.github/workflows/remote-ci.yml`
  does not exist yet, so every statement about unit 32's workflow is a statement about the spec's
  text, not about a file.
- **Units 33, PLAY-dDerivedDocket-1 and DEPL-dDerivedDocket-1 carry no confirmed finding.** All four
  lenses returned and every finding reached a skeptic, so that zero is evidence rather than a
  missing-lens artefact — but it is evidence about a fan aimed at fold text and the round-2 record's
  index, not a fresh full reading of those three specs. DEPL inherits H3 through its step 6, which
  copies unit 34's procedure; that is entered against unit 34, where the fix belongs.
- **The 19 refuted findings are not reproduced.** Precision 0.34 means roughly two in three lens
  findings did not survive a skeptic, which is itself a signal about lens priming rather than about
  the specs.
- **Round-2 mediums were not re-audited one by one.** The fold-fix check above covers the six highs
  and the two medium classes that visibly recurred. A medium fix that quietly failed and introduced
  nothing new would not have been seen by this pass.
