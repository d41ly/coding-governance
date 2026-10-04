**Serves:** spec-audit TOOL-aGraftedHelix-16 TOOL-aGraftedHelix-17 TOOL-aGraftedHelix-18 TOOL-aGraftedHelix-19

# aGraftedHelix — Tier-2 spec audit of units 16 to 19, ROUND 1

*Node `a`, 2026-10-04, ROUND 1 for these four subjects. Units 16 to 19 are the promotions of the
four HIGHs from the round-1 audit of units 10 to 15. Unit 16 closes its H1 (finding 21), unit 17 its
H2 (finding 16), unit 18 its H3 (finding 22) and unit 19 its H4 (finding 31). Four lenses ran:
underspecification, contradiction, unstated assumption and prior art. Every finding in the body
survived a skeptic prompted to REFUTE it. The two findings the skeptics refuted appear only in the
appendix. The author of this report confirmed that each pinned blob below is the blob at HEAD
(`53adda2c5`), by `git rev-parse HEAD:<path>` against `git hash-object <path>`. Four rows were
spot-checked in the tree. For H2, unit 16 §4 step 1 records `git status --porcelain
--untracked-files=all` (spec line 78) and the step-4 paragraph pins a loop over plain
`git status --porcelain` (line 85). For H1, unit 18 §4 "The order" puts `write_lease` in the row
above the claim write. For M7, `tools/workflows/unattended-build.test.sh:170` traces
`String(prompt).replace(/\n/g, " ")`. For L3, unit 19 §4 "The constants" lists eight `CLAIM_READS`
members and four `CLAIM_MODES` members, and "The staged break" expects four phantom cells. The other
rows carry the skeptics' verified text and were not re-derived here.*

**Reviewed at ROUND 1, each subject pinned at its blob:** `memory/builds/aGraftedHelix/spec/2026-10-04-spec-TOOL-aGraftedHelix-18.md`@`f5fae9967bac28c41890b1df405108bc2df924d4`, `memory/builds/aGraftedHelix/spec/2026-10-04-spec-TOOL-aGraftedHelix-19.md`@`076cb215bccbb47b3414a03f9998c0541cca58da`, `memory/builds/aGraftedHelix/spec/2026-10-04-spec-TOOL-aGraftedHelix-17.md`@`507f2d71750571cccf1ed438197e13649d1f5965`, `memory/builds/aGraftedHelix/spec/2026-10-04-spec-TOOL-aGraftedHelix-16.md`@`1b51ac3553aaed1adc31403f64cbe7df05c5b384`.

## Verdict: CLEAN WITH FIXES

No confirmed finding is graded BLOCKER, so every spec is buildable as written. The verdict is not
CLEAN, because twenty-two confirmed findings stand and four of them are HIGH.

- H1 (id 9): unit 18 runs `write_lease` before the claim CAS. A changed-session holder call whose
  claim push does not complete leaves the record naming the new session and the claim naming the old
  one, which is the lockout unit 18 exists to close.
- H2 (id 22): unit 16's step 4 lists untracked paths in a different mode than step 1 records them.
  A wholly untracked foreign directory arrives as one `?? <dir>/` line that the record never holds,
  so `git add` stages the whole directory into the spec commit.
- H3 (id 17): unit 16's step 4 filters by a shell variable that step 1 set. Nothing makes the block
  one shell, and the agent's Bash tool keeps no variables between calls, so a split block stages
  every changed path.
- H4 (id 6): unit 19's read-axis refusal has no criterion. A build that omits it passes every §6
  criterion, and the derived arm then stays green over an uncovered cell.

Thirteen findings are MEDIUM and five are LOW. Adjudicated, the twenty-two confirmed findings form
eighteen items. Three merges were made, each within one binding grade: ids 4, 11 and 18 (all medium,
one fixture defect reached by three lenses), ids 1 and 10 (both medium, unit 17's S1 assertion
cannot be told apart from unit 14's), and ids 12 and 20 (both medium, unit 19's refusal has no
standing arm and no pinned form). No binding grade was changed. Two findings carry an adjudication
note because their fixes interact: H4's second criterion rests on the S2 clause that M3 (id 12)
deletes, and M4's foreign tracked file must sit outside the inputs that M5's rule guards.

Disposition, per `memory/guides/BUILD-METHOD.md`: every CONFIRMED finding is disposed by severity.
Each HIGH is promoted to a unit whose mechanism closes it, audited as a SPEC. Each MEDIUM and LOW is
folded into its spec as a rev bump with a §9 line. Units 16 to 19 are themselves promotions, so
promoting H1 to H4 extends the chain by one more link. The method ends a chain at a promoting round
whose precision falls below the review protocol's floor of 0.5. This round's precision, stated for
that rule to read, is 0.92, so the chain does not end here.

## Review shape

Intensity full. Raw 24, confirmed 22, refuted 2 (ids 7 and 21), unverified 0 (0 uncertain),
precision 0.92.

The adjudicated tally, counted both ways:

| severity | items | raw confirmed findings |
|---|---|---|
| BLOCKER | 0 | 0 |
| HIGH | 4 | 4 |
| MEDIUM | 9 | 13 |
| LOW | 5 | 5 |
| **total** | **18** | **22** |

By lens, raw then confirmed: underspecification 8 and 7, contradiction 7 and 7, unstated
assumption 6 and 5, prior art 3 and 3.

By unit, counting confirmed findings by the spec each one is anchored on: unit 16 holds 11, unit 17
holds 3, unit 18 holds 2 and unit 19 holds 6. Id 15 is anchored on unit 18 and names unit 1 too.

## Run integrity

- Lenses: 4 of 4 returned, 0 DIED.
- Skeptic batches: 5 of 5 returned, 0 DIED.
- 0 contradictory verdicts were demoted to unverified, 0 spurious verdicts were discarded, and 0
  duplicates were found.
- Fixes on confirmed findings: 14 judged sound, 8 judged UNSOUND (ids 1, 3, 4, 8, 9, 12, 15 and 22),
  0 with no fix proposed, and 0 NOT JUDGED. An unjudged fix would be the finder's proposal and
  nothing more; none occurs here. For each UNSOUND fix this report writes the skeptic's corrected
  fix and never the rejected one.
- Severity on confirmed findings: 0 UNGRADED by the skeptic, so none is bound at the finder's grade
  by default. 6 were RE-GRADED by the skeptic: ids 1, 2, 3 and 16 from high to medium, and ids 5
  and 8 from medium to low.
- Unverified findings: 0 answered UNCERTAIN by a skeptic, and 0 with no usable verdict.
- Lens notes: none were supplied, so every lens ran on the kit's generic brief.

This report does not call the run complete. Every lens and every skeptic batch returned, but no
checklist was swept, no intent was supplied, and every lens ran on the generic brief.

**Intent:** NEITHER `specs` nor `context` was supplied to this review. The lenses graded the four
specs against themselves, against each other, against the units they consume from and against the
tree, not against a stated intent for the build.

**Checklist:** NONE swept — absent. The count of recurring-bug-class findings in this report is
therefore not evidence that the project's recurring classes are absent from these specs. This is the
second consecutive round of this build with no checklist. A caller of the next round should pass
the output of `python tools/memory-tree/gotchas.py --for-paths` over the specs' Files-touched paths.

## How the findings cluster

A fold that repairs a class repairs every row in it, so the classes are named here before the rows.

| class | ids | where the gate belongs |
|---|---|---|
| A foreign-path filter stages work it was told to leave alone | 22, 17, 2, 23, 24 | one scratch fixture holding foreign paths of every shape, with a name-list assertion on HEAD |
| An arm whose green half holds when the step it certifies never ran | 4, 11, 18, 16 | a positive artifact of the step, asserted in the arm |
| An `Observed by` label that no criterion reads | 6, 1, 3, 5 | a candidate spec lint: every S-line's named AC reads that S-line's outcome |
| An assertion that cannot red without a sibling assertion reddening too | 1, 10, 19 | a staged break that deletes the assertion and observes its own message vanish |
| A refusal the design rests on, kept by no standing arm | 12, 20, 6 | a numbered `fail <n>` site, which `check-arms.py` already gates |
| A local write ordered before the CAS that decides it | 9, 15 | an incomplete-push arm in the driver suite |
| A stimulus or figure that cannot reach or match its cell | 8, 13 | a §10 checklist entry |
| A citation of a superseded rev, or a supersession nobody recorded | 14, 15 | a §10 checklist entry |
| A prior record of the same rule that the reuse audit did not surface | 23, 24 | a §10 checklist entry on recall terms |

The `Observed by` class recurs. The round-1 audit of units 10 to 15 had two LOW rows in it, and this
round has four rows, one of them HIGH. Two rounds is the point at which a lint earns its cost.

Ids appear in more than one class where the defect has two faces. Each id still sits in exactly one
graded item below.

# HIGH

## H1 · id=9 — unit 18 runs `write_lease` before the claim CAS, so a holder push that does not complete leaves the record and the claim naming different sessions

- **Address:** TOOL-aGraftedHelix-18 §4 "The order", against §5 error states and §4 "Alternatives
  rejected".
- **Defect:** the order table puts `write_lease`, a local write that stages the record, in the row
  before the claim write. §5 keeps a claim write that does not complete as unit 1's "announce,
  continue" row, unchanged. Together they break unit 1 §5's rule that the CAS precedes every local
  write. §4 "Alternatives rejected" cites that same premise ("check 90 must fire before any local
  write").
- **Impact:** take a holder `--resume` under a changed session (s1 to s2) whose claim push times out,
  or that runs offline, which unit 1 §4 supports on the holder path. Afterwards the record names s2
  and the claim names s1. On the next s2 call, `mine` fails, because it needs the record's keepalive
  AND session, and unit 11 §3 leaves that test unchanged. `same session` fails too, because the
  claim's s1 differs from the environment's s2. The claim reads as foreign, and the holder column
  answers check 90 for every foreign verdict. A live run is forced to `--abort --code claim-lost`,
  the exact consequence §1 exists to prevent. A lost race on that call likewise reaches check 90 only
  after `write_lease` has rewritten and staged the record. AC1 and AC2 cover only a completed push.
- **Fix — the skeptic judged the finder's fix UNSOUND; the skeptic's corrected fix:** decide `mine`
  against the before-facts, then CAS the claim with the after-facts under one lease stamp shared
  with `write_lease`, so that a lost race is check 90 before `write_lease` runs. Rewrite the §4
  order table to match. When the CAS does not complete, or the claim cannot be read, still run
  `write_lease`, and have it record the session it replaced as a lease fact, which the next holder
  claim write that lands clears. Widen the holder column's `mine` test to also accept a claim whose
  keepalive equals the record's and whose session equals that fact. Add an AC in which a git shim
  makes the claim push exit 124 on the s2 call, and a variant with the remote unreachable on the s2
  call. Both end with a second s2 call that exits 0 and leaves a claim naming s2.
- **Note for the promotion spec:** `write_lease` takes two arguments at HEAD
  (`tools/unattended/unattended.sh:5557`) and stamps `lease-utc` itself, so the spec must say how
  the shared stamp reaches it.
- **Left-shift gate:** the two incomplete-push ACs, kept as arms in
  `tools/unattended/unattended.test.sh` and observed RED under the order as unit 18 now states it.
  Add a §10 checklist entry: "an order table that puts a local write before the CAS deciding it
  states what the record holds when the CAS does not complete, and an AC drives that path."

## H2 · id=22 — step 4 lists untracked paths in a different mode than step 1 records them, so a wholly untracked foreign directory is staged whole

- **Address:** TOOL-aGraftedHelix-16 §4 "The block", step 1 and the step-4 loop paragraph; §2 S1;
  §6 AC2.
- **Defect:** step 1 records `git status --porcelain --untracked-files=all`, and §4 pins step 4's
  second half as a loop over plain `git status --porcelain` filtered by that record. Plain porcelain
  collapses a wholly untracked directory to `?? <dir>/`, a line that step 1's per-file record never
  holds. The filter passes it, and `git add -- <dir>/` stages every file inside. The finder
  reproduced this in a scratch repository: `-uall` printed `?? foreign/sub/brief.md` and the default
  printed `?? foreign/`. No repository config sets `status.showUntrackedFiles`. The recorded
  precedent for this render-then-stage-the-delta rule, TOOL-dMendedRecall-2 S2 (CLOSED), takes both
  sets with one listing.
- **Impact:** the spec commit carries another writer's untracked work, which breaks the FOREIGN rule
  that S1 says is unchanged. Unit 15 §5 names the live case: another writer's untracked build brief.
  A not-yet-tracked `build/` or `prompts/` folder has exactly this shape, and so does `__pycache__/`
  in an adopter that does not ignore it (M6). Neither AC2 nor the S4 arm's fixture holds a foreign
  path, so both stay green.
- **Fix — the skeptic judged the finder's fix UNSOUND; the skeptic's corrected fix:** take step 4's
  listing as `git status --porcelain --untracked-files=all`, the same command as step 1, and compare
  the path field rather than whole lines. Keep `-z` out, or use it only with the record written to a
  file, because §4 holds the record in a shell variable and bash command substitution drops NUL
  bytes. Add an untracked file inside an untracked directory to the arm's fixture, and assert that
  `git ls-tree -r --name-only HEAD` does not list it. Stage the break as step 4's listing without
  `--untracked-files=all`.
- **Left-shift gate:** the fixture assertion is the regression gate, and M4's foreign-path fixture
  is where it lives. Add a §10 checklist entry: "two listings compared as sets are taken with the
  same flags; a filter that compares a record against a listing taken differently passes the
  difference."

## H3 · id=17 — step 4 filters by a shell variable that step 1 set, and nothing makes the block one shell

- **Address:** TOOL-aGraftedHelix-16 §4 "The block", step 4 and the paragraph after it; §2 S3.
- **Defect:** §4 holds step 1's record "in a shell variable inside the block". S3 asks only for one
  fenced block. Nothing says the block runs as one invocation, and the agent's Bash tool keeps no
  variables between calls. Unit 15's step 2, which this replaces, kept the record in the agent's own
  context, so the dependence on shell state is new in this unit.
- **Impact:** if the block is split across calls, the record is unset at step 4 and filters nothing
  out. Every changed path, foreign tracked and untracked work included, is then staged into the spec
  commit. That breaks the foreign-path rule in unit 15's step 2 and §5, which calls the case live.
  S2 runs `git status` only over the spec paths, and the arm runs the block as one script, so neither
  catches it.
- **Fix — the skeptic judged it SOUND:** have the prompt say the block runs as ONE Bash invocation.
  Step 4 refuses with `committed: false` when the record variable is unset, tested as `${rec+x}` and
  not by emptiness, so a clean tree, where the record is set but empty, still proceeds.
  Alternatively, write the record to a file under `$(git rev-parse --git-dir)` and read it back at
  step 4. The file form is also the one under which H2's corrected fix may use `-z`.
- **Left-shift gate:** an arm that runs step 4 in a fresh shell with the record unset and asserts
  `committed: false` with HEAD unmoved, observed RED with the `${rec+x}` guard deleted. Add a §10
  checklist entry: "a prompt block that carries state between steps in shell variables is run by a
  tool that keeps no shell state between calls."

## H4 · id=6 — unit 19's read-axis refusal has no criterion, so a build that omits it passes every §6 criterion

- **Address:** TOOL-aGraftedHelix-19 §2 S2; §6.
- **Defect:** S2 states two refusals, one for a mode outside `CLAIM_MODES` and one for a derived
  claim-read class outside `CLAIM_READS`, and says "Observed by AC2". AC2 drives only a mode outside
  `CLAIM_MODES` at the `--hold` site. AC1 counts constant members and AC3 checks versions. §4's
  staged break and §7's arm stage only a phantom MODE. Nothing observes the read-axis refusal, and
  nothing observes S2's claim that a member added to a constant without a branch reaches the refusal.
- **Impact:** a build that omits the read-axis refusal passes every §6 criterion. S3's arm derives
  its cells from `CLAIM_READS`, so it never drives a class that `check_claim_writable` derives and
  the constant lacks. A class added to the function later neither refuses nor appears among the
  arm's derived cells, and the arm stays green over an uncovered cell. That is finding 31 of the
  round-1 audit of units 10 to 15, the finding this unit exists to close, reopened on the read axis.
- **Fix — the skeptic judged it SOUND:** add a criterion. A scratch copy of the driver with one
  member (for example `foreign-stale`) removed from `CLAIM_READS`, run over unit 1's fixture where
  the claim reads that class, prints the refusal naming the class and `CLAIM_READS`, and the remote
  claim ref's sha is unchanged. Add a second: a member appended to `CLAIM_MODES` and passed at a call
  site that has no case branch for it reaches the same named refusal.
- **Adjudication note:** the second criterion presumes S2's clause that a branchless member reaches
  the refusal. M3 (id 12) shows that clause is false as specified, because a member of the constant
  passes the membership test, and its corrected fix deletes the clause. A promotion spec that takes
  M3's fix drops this second criterion with the clause, and S3's derived-set assertion owns that
  direction. The first criterion and the read-axis half of M3's standing arm are the same
  observation and can be one arm.
- **Left-shift gate:** M3's standing arm in `tools/unattended/unattended.test.sh`, which keeps the
  refusal on both axes, plus the `Observed by` lint named in the class table.

# MEDIUM

## M1 · id=4, id=11, id=18 — the arm's scratch repository holds no generator at the rendered path, and the block has no fail-fast, so the arm's green half holds when the generator never ran

- **Address:** TOOL-aGraftedHelix-16 §4 "The block" step 3; §4 "The arm"; §2 S3 and S4; §6 AC2.
- **Defect:** step 3 is `python {{MEMORY_TREE_DIR}}/gen_build_index.py --write`. The render fills
  that token repo-relative as `tools/memory-tree`: the rendered harness at
  `tools/workflows/unattended-build.js:361` reads `python tools/memory-tree/gotchas.py`. S3 leaves
  `<spec paths>` as the only placeholder, so the arm cannot rewrite the path. §4 "The arm" builds the
  scratch repository on the `_b1` shape, a conf, a charter, a build README and the waiver, with no
  `tools/memory-tree/` in it. `_b1` runs the generator out of tree as
  `"$_PY" "$HERE/gen_build_index.py"` (`tools/memory-tree/check-memory-hygiene.test.sh:2706-2735`).
  The generator imports its siblings `tree_lib` (`gen_build_index.py:149`) and `backlog` (`:290`),
  so a one-file copy fails too. The block checks no step's exit status, and S4's "with the real
  gen_build_index.py" does not say where the generator sits.
- **Impact:** built as §4 states, step 3 fails with the file not found and steps 4 to 6 still run.
  The spec is committed unrendered, the status is clean, and `HEAD:<spec>` equals `hash-object`, so
  both of the arm's assertions pass with the generator never having run. The same vacuous green
  follows any later generator failure, such as a moved `MEMORY_TREE_DIR` or a node where `python` is
  the MS-Store stub that exits 9009. Only the one-time staged break would notice, by failing to red,
  at the cost of a pass cycle. The standing arm has no liveness witness at all. The id 18 skeptic
  judged the production half overstated: a generator failure leaves the region missing from the
  worktree spec, which the pre-commit's check 9 would normally refuse.
- **Fix — ids 11 and 18 judged SOUND; id 4's fix judged UNSOUND and replaced by the skeptic's
  corrected fix, which agrees with the other two.** Taken together:
  - Install the WHOLE memory-tree kit directory in the scratch repository's first commit, at the path
    the rendered block names, as unit 9's copy-install fixture (its AC12) does. Derive the
    destination from the rendered block, never from a literal typed in the suite. A two-file copy
    fails at `import backlog` (`gen_build_index.py:290`), and `extract` and `corpus_ids` are imported
    deferred, so the directory is the unit (id 4's skeptic).
  - Open the block with `set -e`, so that a failed step stops it (id 11). The prompt returns
    `committed: false` with step 3's output when step 3 exits non-zero (id 18), and the arm asserts
    the block's exit status is 0 (id 4).
  - Add a positive assertion to the arm and to AC2: `git show HEAD:<spec>` contains
    `<!-- gen:spec-records -->`, which proves the generator ran (ids 4 and 11).
  - Under `set -e`, step 4's filter must not be a `grep` that exits 1 on no match inside a command
    substitution, or a call with no foreign changes aborts before the commit (id 11's skeptic).
  - Without M6's `-B`, expect `tools/memory-tree/__pycache__/` to be staged into the scratch commit
    by step 4 (id 18's skeptic). With M6 folded, this same fixture is where M6's no-`__pycache__`
    assertion becomes observable.
- **Left-shift gate:** the positive region assertion is the liveness assertion §7 requires of any
  probe. Add a §10 checklist entry: "an arm whose green half is a clean status and an equal hash
  holds when the step under test never ran; every arm asserts a positive artifact of the step it
  certifies."

## M2 · id=1, id=10 — unit 17's premise is stale under unit 14 rev-2, and its S1 assertion cannot red without unit 14's reddening too

- **Address:** TOOL-aGraftedHelix-17 §1 Goal; §4 "Evidence" and "The staged break"; §2 S1;
  §6 AC1.
- **Defect:** §1 says unit 14's arm "stays green with check 27's status=1 deleted, because check 28
  still sets the exit", and §4 "Evidence" reads unit 14's branch row as a content duplicate. Unit 14
  rev-2 §4 pins that row as "a paraphrase, never a verbatim restatement", whose content key differs,
  so check 28 does not fire on it. Unit 14's AC1 already asserts "no other line opening check <n>:",
  with the red-when "another check holds the exit", and unit 17's own §3 says the same. S1's named
  assertion is therefore a strict subset of unit 14's and can never red alone (id 10). S1 is also
  labelled "Observed by AC1", but AC1 (spec lines 98-103) runs only the fixture's copy of the hygiene
  engine and reads the engine's output. It never runs the arm, so it stays green whether or not S1's
  assertion is added (id 1). Rev-2 relabelled S2 for exactly this reason and left S1 with the same
  defect.
- **Impact:** the shipped behaviour stays protected by unit 14's assertion, so the effect is
  contained. But the unit's only deliverable can be skipped with every §6 criterion green, and a
  builder or the next auditor reads a stale defect as live and keeps a duplicate assertion on that
  basis. The §4 staged-break rationale ("which a break deleting check 27's status=1 alone could
  not") is stale.
- **Fix — id 10 judged SOUND; id 1's fix judged UNSOUND, replaced by the skeptic's corrected fix:**
  - (id 10) Rewrite §1 and §4 "Evidence" / "The staged break" to the rev-2 premise. State that unit
    14's only-offending-check assertion already covers check 28, and that this unit's deliverable is
    observing that assertion red once check 28 exists, with a message naming check 28 as the
    exit-holder (S2). Either fold S1 into a message split of unit 14's assertion, or state in S1
    what the separate assertion catches that unit 14's does not.
  - (id 1, corrected) AC1 runs a slice of `tools/memory-tree/check-memory-hygiene.test.sh`: the
    prologue plus the check 27 engine arm. S1's assertion prints its own FAIL text, distinct from
    unit 14's only-offending-check message. With the fixture's branch row made a verbatim copy of the
    base row in a scratch copy, the slice reds AND its output carries S1's own message text. Staged:
    delete S1's assertion in a scratch copy, observe that message vanish while the slice still reds
    through unit 14's assertion, then restore.
  - The two compose. Id 1's corrected fix takes the second branch of id 10's choice: what S1 adds
    over unit 14's assertion is its own diagnosis text. The verbatim row keeps its own id (M9).
- **Left-shift gate:** the staged deletion in the corrected AC1. Add a §10 checklist entry: "an
  assertion that is a strict subset of a sibling's cannot red alone; its staged break deletes it and
  observes its own message vanish."

## M3 · id=12, id=20 — unit 19's refusal has no standing arm and no pinned form, and S2 promises a branchless-member guard the design does not build

- **Address:** TOOL-aGraftedHelix-19 §2 S2; §3 (case-label parsing rejected); §4 "Inventory";
  §7 New arm.
- **Defect:** S2 defines the refusal only for a mode outside `CLAIM_MODES` or a derived class
  outside `CLAIM_READS`. A member added to a constant is inside it and passes the membership test,
  so the clause "one added to the constant without a branch reaches the refusal too" is false as
  specified. S3's derived-set assertion catches that direction instead, through the missing typed
  outcomes (id 12). §3 rejects the case-label reader because "S2's refusal already makes the
  constants load-bearing", yet §7's only new arm is the derived-set assertion, and the refusal is
  observed once, by AC2 in a scratch copy. S2's "named internal error" also does not pin its form
  (id 20). `tools/unattended/unattended.sh:637` defines `fail()`, so
  `tools/memory-tree/check-arms.py` discovers it and requires every `fail <n>` branch to be armed or
  pinned. Unit 1 writes every claim refusal as a `fail` call (checks 89, 90 and 91). §4 "Inventory"
  says "no new check", and no in-scope arm drives the refusal.
- **Impact:** if a later change drops the refusal, nothing reds, and a class then added to the
  function without its constant goes undriven by the derived arm. That reopens finding 31's class,
  though it needs two later changes, so the effect is contained. If the refusal is written the
  natural way, as `fail <n>`, the "harness arms" leg §7 lists reds and the builder must write an arm
  this spec does not scope. The id 20 skeptic corrected two sub-claims. The pin file
  `tools/unattended/unarmed-branches.txt` already holds 10 `unattended.sh` rows, and adding one is
  not mechanically refused. Its policy still reserves rows for branches that cannot be armed, and
  AC2 shows this one can.
- **Fix — id 20 judged SOUND; id 12's fix judged UNSOUND, replaced by the skeptic's corrected fix.**
  Taken together:
  - Delete S2's clause "and one added to the constant without a branch reaches the refusal too"
    (id 12). S3's derived-set assertion is what catches that direction.
  - Pin the refusal's form in S2 (id 20). Either a `fail <n>` branch, with its check number in §4's
    inventory, the "no new check" line updated, and an arm in `unattended.test.sh` that runs a
    sed-mutated scratch copy of the driver and asserts the refusal text. Or a stderr line plus a
    return code that is not a `fail` call, stated as such.
  - Add a standing arm to §7 in `tools/unattended/unattended.test.sh` (id 12). In a scratch copy of
    the driver, remove one existing member from `CLAIM_MODES` and one from `CLAIM_READS`, so each
    value keeps its branch. Drive the call site and the seeded claim that reach each value. Assert
    the named refusal naming the value and its constant, and an unmoved claim ref. Stage the break by
    removing the membership test: the value then reaches its branch and the arm reds.
  - With the `fail <n>` form, id 12's standing arm is the arm id 20 asks for, and its read-axis half
    is H4's first criterion.
- **Left-shift gate:** `check-arms.py` already gates every `fail <n>` site, so choosing that form
  puts the refusal under an existing gate. Add a §10 checklist entry: "a refusal a design rests on is
  a numbered site with a standing arm, never a one-time scratch observation."

## M4 · id=2 — step 4's foreign-path loop is new shell code with no criterion

- **Address:** TOOL-aGraftedHelix-16 §2 S1 and S3; §4 "The block" step 4; §6 AC2.
- **Defect:** §4 (spec lines 85-86) makes step 4's second half new shell code in this unit: a loop
  over `git status --porcelain` filtered by step 1's record. S1 claims AC1 and AC2 observe it. AC1
  reads only prompt text. AC2 asserts only that `<spec>` is clean and that its HEAD blob matches its
  `hash-object`, in a scratch repository with no foreign paths, and never checks what else the commit
  holds.
- **Impact:** a loop that stages nothing leaves the generator's rewrite of the build README's
  build-index region out of the commit. A filter that is inverted, or that misparses porcelain lines,
  commits foreign work the owner had dirty in the tree. AC1 and AC2 stay green either way. The effect
  is contained: unit 15 §5 says the pre-commit's check 9 refuses a stale index by name, and an
  inverted filter mis-commits only when foreign dirty paths exist, on a branch.
- **Fix — the skeptic judged it SOUND:** in AC2's scratch repository, plant one foreign modified
  tracked file and one foreign untracked file before the block runs. Afterwards assert that
  `git status --porcelain` lists exactly those two, unchanged, and that
  `git show --name-only --format= HEAD` lists the spec and the generator-rewritten build README and
  no foreign path. Stage a break that inverts the loop's filter, and observe it red.
- **Adjudication note:** plant the foreign tracked file outside the generator's inputs, meaning
  outside the memory root, `.memory-tree.conf` and the kit directory. Otherwise M5's input rule
  refuses the render, correctly, and the AC observes that refusal instead. Put the foreign untracked
  file inside an untracked directory, and this one fixture also observes H2.
- **Left-shift gate:** this fixture is the gate for the whole foreign-path class (H2, H3, M4, M5 and
  M6). Build it once and extend it per finding.

## M5 · id=23 — the block renders generated views from foreign unstaged inputs and stages them

- **Address:** TOOL-aGraftedHelix-16 §4 "The block" steps 3 and 4; §2 S2; §6 AC2; §10.
- **Defect:** step 1 marks foreign tracked edits as never staged, but step 3 runs the generator over
  them anyway. `plan()` lists inputs with `git ls-files` (`gen_build_index.py:698`) and reads their
  bytes off the disk. A foreign unstaged edit to a sibling spec's status header, a `BACKLOG.md` or
  `DECISIONS.md` changes `memory/LIVE.md`, the ledger shard and the build README's regions. Those
  are clean at step 1 and changed after step 3, so step 4 stages them. TOOL-dMendedRecall-2 rev-3 S3
  (CLOSED, closing TOOL-dAlignedCarrier-9) already decided this case: when any input of the views
  carries an unstaged change, render nothing and stage no view. That record also measured that such a
  commit passes the pre-commit's worktree `--check` and reads `build-index DRIFT` over a clean
  checkout. Unit 16 §10 says no existing seam fits, and its recall probe did not surface that record.
  Unit 15 §5, which this block inherits, says check 9 refuses the mixed case at the hook. That is
  false: check 9 runs `gen_build_index.py --check` over the worktree
  (`check-memory-hygiene.sh:1039-1041`), and `cmd_check` (`:2130`) compares a disk render with disk
  bytes, never the index.
- **Impact:** the commit holds generated views that describe work it does not contain, and the hook
  certifies them fresh. The path is narrow, and the next render or a clean-checkout `--check`
  catches it.
- **Fix — the skeptic judged it SOUND:** adopt dMendedRecall-2's input rule in the block. Before
  step 3, if `git diff --name-only` over the memory root, `.memory-tree.conf` and the generator's
  directory names anything outside the spec paths, skip the render and return `committed: false`
  naming those inputs. Extend AC2 and the S4 arm to run `gen_build_index.py --check` over a clean
  checkout of HEAD, as dMendedRecall-2 rev-3 S6 does, with a fixture variant holding a foreign
  unstaged status-header edit. Correct unit 15's check-9 sentence, or point away from it.
- **Note:** `write_ask_views`, the function that record carries, is absent at this tree's HEAD.
  Merge `01c22e155` dropped it, and it was restored only on the dUnstuckLanding branch
  (`e6e55d5ab`). The fold should cite the spec record, not the function.
- **Left-shift gate:** the clean-checkout `--check` in the arm. Add a §10 checklist entry: "a reuse
  audit for a render-then-stage rule recalls with the mechanism's own terms (render, stage, generated
  view, unstaged input)." Unit 16's recall terms named only the harness's vocabulary, which is why
  the probe missed the record.

## M6 · id=24 — step 3 runs the generator without `-B`, so its bytecode caches are staged into the spec commit

- **Address:** TOOL-aGraftedHelix-16 §4 "The block" step 3.
- **Defect:** `gen_build_index.py` inserts its own directory on `sys.path`, imports `tree_lib`
  (`:149`) and `backlog` (`:290`), and never sets `dont_write_bytecode`, so the render writes
  `__pycache__/` beside the kit. Only this repository's `.gitignore:1` hides that, and
  `adopt-memory-tree.sh` adds no such ignore. In an adopter that does not ignore it, any cache path
  step 1 did not list, on a first run or under a new interpreter tag, is staged by step 4. Under step
  4's plain porcelain (H2), even existing caches collapse to an unlisted `?? .../__pycache__/` line
  and get staged. TOOL-dMendedRecall-2 rev-2 S2 added `-B` to the same rule after its fixture's
  first close committed two bytecode caches.
- **Impact:** junk bytecode lands in the spec commit of any adopter that does not ignore
  `__pycache__`. The S4 arm runs the rendered relative generator path inside a `_b1`-shaped
  repository with no `.gitignore`, so it commits the caches too, and its two assertions cannot see
  them.
- **Fix — the skeptic judged it SOUND:** write step 3 as
  `python -B {{MEMORY_TREE_DIR}}/gen_build_index.py --write`, together with unit 15's step text that
  the block replaces. Have the arm assert that `git ls-tree -r --name-only HEAD` holds no
  `__pycache__` path. Stage the break as the block without `-B`.
- **Left-shift gate:** the arm assertion. Add a §10 checklist entry: "a render step inside a
  stage-the-delta rule runs its interpreter with bytecode writes off."

## M7 · id=16 — the suite's stub hook flattens every traced prompt to one line, so the traced block cannot run

- **Address:** TOOL-aGraftedHelix-16 §2 S4; §4 "The arm"; §6 AC1.
- **Defect:** S4 extracts a runnable fenced block from the TRACED `commit:specs:` prompt.
  `tools/workflows/unattended-build.test.sh:170` traces every prompt as
  `String(prompt).replace(/\n/g, " ")`, so the traced prompt is one line and holds no block that can
  run. Neither §4 nor §10 says so.
- **Impact:** built as written, the arm fails on its unbroken run, because the flattened block cannot
  stage or commit and the spec stays untracked. That failure is visible. The obvious repair is to
  stop flattening, which splits every traced prompt across lines. The suite's 18 reads of the form
  `grep '^prompt:<label>:'` would then capture only the first line of each prompt, and their
  `hasnt_` assertions, such as the no-backslash-scratch arm at `:286-288`, would pass over text they
  no longer read. The skeptic graded this medium rather than high because most `hasnt_` captures
  share their variable with `has` arms that would red loudly, so the could-not-fail outcome needs a
  further careless step.
- **Fix — the skeptic judged it SOUND:** in S4, add a second trace line per agent call that carries
  the prompt JSON-encoded on one line, for example `promptjson:<label>:` followed by
  `JSON.stringify(prompt)`. The arm decodes it with node, and the existing `prompt:` line stays
  byte-identical. Name the same channel for AC1's probe, because "a git add line follows the --write
  line" needs the prompt's line structure. M8's predicate needs it too.
- **Left-shift gate:** a canary arm asserting that a multi-line prompt's `promptjson:` line decodes
  to a string containing a newline, so the channel cannot flatten silently. Add a §10 checklist
  entry: "a trace written for grep is not a source for execution; an arm names the channel it reads."

## M8 · id=3 — S3's "never restate a command" has no criterion

- **Address:** TOOL-aGraftedHelix-16 §2 S3; §6 AC1.
- **Defect:** S3 (spec lines 34-37) requires that the prose around the block never restate a
  command, and claims "Observed by AC1". AC1 asserts only that there is exactly one fenced block,
  plus what that block contains. Unit 15's prompt steps 2 and 3 (unit 15 lines 168-174) spell
  `git add -- <the spec paths>` and the generator call as inline code in prose. If they stayed, AC1
  would still see one fenced block and stay green.
- **Impact:** an agent that follows the stale prose commits the pre-render blob, and the resolver's
  HEAD-against-`hash-object` compare then throws the named dirty-tree refusal. That failure is loud,
  not silent, but every criterion stays green and the arm certifies a block the agent did not run.
- **Fix — the skeptic judged the finder's fix UNSOUND; the skeptic's corrected fix:** extend AC1 so
  that, outside the fenced block, no line or inline code span reproduces one of the block's own
  command lines (`git add -- <spec paths>`, `git commit`, `git status --porcelain`,
  `gen_build_index.py --write`). Before wiring the predicate, print its hits and near-misses over the
  real traced prompt. Staged: re-insert a prose `git add -- <spec paths>` step outside the block,
  and observe AC1 red. The predicate matches the block's own command lines rather than any `git add`
  text, because two correct prose lines stay: unit 15's step 1 names `gen_build_index.py` as the
  reader of the H1 key, and its step 3 rule "Never `git add -A` or `git add -u`" carries `git add`
  text.
- **Left-shift gate:** the corrected AC1 predicate, read over M7's `promptjson:` channel.

## M9 · id=19 — unit 17's staged break copies the whole base row, id included, so check 20 fires and check 28 does not

- **Address:** TOOL-aGraftedHelix-17 §4 "The staged break"; §6 AC1; §7.
- **Defect:** §4 says "a verbatim copy of the base row's text", while AC1 ("a verbatim copy of the
  base row") and §7 ("stage the branch row as a verbatim copy of the base row") say whole row. None
  of them says the new id is kept. `tools/memory-tree/row_grammar.py:53` has `CHECK = 20`, and
  `:677-681` reds an id appearing twice within one row document. Unit 6 grades only keys held by two
  or more distinct identities (unit 6 spec lines 35-40).
- **Impact:** a whole-row copy prints a `check 20:` line and no `check 28:` line. The arm reds anyway,
  on unit 14's only-offending-check assertion, so the close could read a red that is not S1's. AC1's
  pass observation demands a printed `check 28:` line and would expose it, so the effect is
  contained.
- **Fix — the skeptic judged it SOUND:** state that the branch row keeps its new id and that only its
  body becomes the base row's body, verbatim. Have AC1's break also assert that no `check 20:` line
  is printed, so the red it observes belongs to check 28. This applies to M2's corrected AC1 too,
  which makes the same row verbatim.
- **Left-shift gate:** the no-`check 20:` assertion. The class, a fixture not pinned clean under
  every other check, recurs from the round-1 audit of units 10 to 15 (its M3). The "only offending
  check is N" assertion form is the gate for it.

# LOW

## L1 · id=8 — AC2's `--hold <slug>` stimulus stops at argument validation before it reaches the refusal

- **Address:** TOOL-aGraftedHelix-19 §6 AC2.
- **Defect:** `--hold` requires `--code`, `--until`, `--reason`, and either `--reaped` or
  `--keepalive-unreachable` (`tools/unattended/unattended.sh:23`). At base `5266d22e`, `run_hold`
  refuses a bare `--hold` with `fail 55` or `fail 56` before any claim write. AC2's literal call
  therefore prints a check 55 line and never the mode refusal. The skeptic refuted the finder's
  second half, that AC2 misses local writes. Unit 1's call-site table puts the `--hold` claim write
  after `stage_or_fail` by design (unit 1 S9: the local record is the truth), and HEAD does not move
  inside `run_hold`.
- **Impact:** AC2 reds rather than greening falsely, which costs a pass cycle and ships nothing
  wrong. Refuted id 21 makes the same point from the other side: the shorthand is unit 1 AC9's.
- **Fix — the skeptic judged the finder's fix UNSOUND; the skeptic's corrected fix:** spell AC2's
  stimulus with `--hold`'s required arguments: `--code <a declared hold code> --until owner
  --reason <text> --reaped <the recorded keepalive>`, over a fixture whose branch tip is pushed.
  Keep AC2's observation to the named line and the unchanged claim ref. If a no-local-write
  observation is wanted, drive the undeclared mode at `--preflight`, whose claim write precedes every
  local write, and assert that the run-state file is absent afterwards, as unit 1 AC6 does.
- **Left-shift gate:** a §10 checklist entry: "a criterion's stimulus names the verb's full required
  argument set, or a fixture helper that supplies it."

## L2 · id=5 — the instruction to quote the porcelain lines in `why` has no observation

- **Address:** TOOL-aGraftedHelix-16 §2 S2; §6 AC1.
- **Defect:** S2 says a non-empty status returns `committed: false` with the porcelain output quoted
  in `why`, and claims AC1 and AC2 observe it. AC1 checks only that the prompt says a non-empty
  status returns `committed: false`. Its staged break covers only the re-add, and AC2 exercises only
  the clean path. The thrown-by-name half is unit 15's validation, which unit 15's AC4 already
  observes.
- **Impact:** a prompt that omits the quoting instruction degrades only the error text's detail. The
  throw still names the stage, and unit 15's step 5 still asks for the refusal's first lines. Close
  to cosmetic.
- **Fix — the skeptic judged it SOUND:** AC1 asserts that the prompt tells the agent to quote the
  porcelain lines in `why`, and stages a break deleting that sentence. Add one probe call whose
  commit double returns `{committed:false, why:' M <path>'}`, and assert that the run's thrown error
  text contains ` M <path>`. That probe duplicates unit 15's AC4, harmlessly.
- **Left-shift gate:** the `Observed by` lint named in the class table.

## L3 · id=13 — the staged break expects four phantom cells, where a phantom mode adds eight

- **Address:** TOOL-aGraftedHelix-19 §4 "The staged break", against §4 "The constants".
- **Defect:** §4 "The constants" lists eight `CLAIM_READS` members and four `CLAIM_MODES` members,
  and S3 derives the cell set as their product. A phantom appended to `CLAIM_MODES` therefore adds
  eight cells, one per `CLAIM_READS` member. The "four phantom cells" the staged break expects is
  the count for a phantom appended to `CLAIM_READS`.
- **Impact:** the built arm does not depend on the prose figure; only the recorded expectation of the
  observation is wrong. A builder could log a false mismatch, or reshape the derivation to fit.
- **Fix — the skeptic judged it SOUND:** say "the eight phantom cells, one per `CLAIM_READS` member",
  or move the phantom to `CLAIM_READS` and keep "four". The first option is clean. The second must
  also rewrite §5 testing ("a phantom mode") and §7's New arm line ("appended to CLAIM_MODES"), or it
  leaves a new contradiction.
- **Left-shift gate:** charter §7 already says no count of a derived population is written in prose.
  The spec should say "one cell per `CLAIM_READS` member" and let the arm print the figure.

## L4 · id=14 — unit 19's goal cites a superseded rev of unit 12

- **Address:** TOOL-aGraftedHelix-19 §1 Goal.
- **Defect:** §1 says the arm stays green over an uncovered cell "while unit 12's §3 calls it the
  class gate". Unit 12 at HEAD is rev-2, landed in fold commit `be389baa0`. Its §3 says the arm
  "becomes the class gate for this table only once TOOL-aGraftedHelix-19 derives its cells from the
  driver; built alone, it is an instance check".
- **Impact:** prose only, with no behavioural effect.
- **Fix — the skeptic judged it SOUND:** restate §1 against unit 12 rev-2: unit 12 declares the arm
  an instance check and hands the derivation to this unit.
- **Left-shift gate:** a §10 checklist entry: "a fold that rev-bumps a unit greps the build's specs
  for citations of the text it changed."

## L5 · id=15 — the claim's `lease-utc` now moves on a same-session renewal, and nothing records the supersession of unit 1's definition

- **Address:** TOOL-aGraftedHelix-18 §6 AC2, against TOOL-aGraftedHelix-1 §4 "The claim record".
- **Defect:** AC2 requires a holder `--resume` that changes only `CLAUDE_PID` to leave the claim's
  `lease-utc` equal to the record's, which `write_lease` has just reset. Unit 1 §4 defines
  `lease-utc` as "when this session took the claim", "kept across a holder's renewals and reset by a
  take-over". Unit 11 S1 already has holder renewals copy `lease-utc` from the record, so the
  inconsistency predates unit 18, which only pins the order and observes the result. Neither unit 11
  nor unit 18 records a supersession of unit 1's sentence.
- **Impact:** a stale interface sentence. No verdict, age or take-over line reads the claim's
  `lease-utc`; only the renewal comparison does, and it follows the record.
- **Fix — the skeptic judged the finder's fix UNSOUND; the skeptic's corrected fix:** add a §3 line
  to unit 18 stating that a holder-row `write_lease`, like the `--replaces` block under unit 11 S1,
  resets the claim's `lease-utc` to the record's new stamp. Say that this supersedes unit 1 §4's
  "kept across a holder's renewals" for a renewal whose `write_lease` moved a fact. Keep AC2 as it
  stands.
- **Left-shift gate:** a §10 checklist entry: "a unit that changes a field another unit's interface
  section defines records the supersession in its own §3."

## What a fold should do first

1. Unit 16, the spec commit stage, carries eleven of the twenty-two confirmed findings and two of
   the four HIGHs. Fold M1, M4, M5, M6, M7, M8 and L2 in one rev: install the whole kit in the
   scratch repository, `set -e`, `-B`, the positive region assertion, the `promptjson:` channel, the
   input rule, and one foreign-path fixture. Then promote H2 and H3. One promotion unit can close
   both, because both live in step 4's filter: take the listing with `--untracked-files=all` and
   compare by path, and keep the record in one invocation or in a git-dir file. It builds on the
   folded fixture rather than a second one.
2. Unit 18, the holder order. Promote H1, and fold L5 in the same pass, because both touch AC2's
   claim facts.
3. Unit 19, the claim write table. Fold M3 (delete the clause, pin the `fail <n>` form, add the
   standing arm), L1, L3 and L4. Then promote H4, and resolve its second criterion against M3's
   deleted clause in the promotion spec.
4. Unit 17, the check 28 assertion. Fold M2 and M9 together: rewrite the premise to unit 14 rev-2,
   give S1 its own message text, and keep the verbatim row's id.

H1 to H4 are promoted under the method rather than folded. A review of their promotion specs should
run with a checklist swept and an intent supplied. Neither this round nor the one before it had
either.

## Appendix — every finding

| id | lens | ref | severity | skepticSeverity | verdict | reason | fixVerdict |
|---|---|---|---|---|---|---|---|
| 1 | underspecification | memory/builds/aGraftedHelix/spec/2026-10-04-spec-TOOL-aGraftedHelix-17.md:section 2 S1 / section 6 AC1 | high | medium | confirmed | Unit 17 S1 (line 29) says 'Observed by AC1', but AC1 (lines 98-103) runs only the fixture's copy of the hygiene engine and reads the engine's own output. It never runs the test arm, so it stays green whether or not S1's assertion is added. Rev-2 (lines 124-126) relabelled S2 for exactly this reason and left S1 with the same defect. The impact is overstated, though. Unit 17 section 3 (lines 41-43) and unit 14's New-arm line (unit 14 line 126) say unit 14's arm already asserts that 27 is the only offending check. That assertion reds on any 'check 28:' line, so the arm is not the could-not-fail arm even without S1. The shipped behaviour is still protected, and the defect is a false observation label that misleads the next reader, with a contained effect. The fix is unsound because it cannot tell S1's assertion from unit 14's. With the row made verbatim, unit 14's only-offending-check assertion also reds with a message about check 28, so the rewritten AC1 goes red and green whether or not S1 exists. Its alternative, a relabel naming the section 7 close observation, names an observation with the same blindness. | unsound |
| 2 | underspecification | memory/builds/aGraftedHelix/spec/2026-10-04-spec-TOOL-aGraftedHelix-16.md:section 2 S1 and S3 (section 4 'The block' step 4) / section 6 AC2 | high | medium | confirmed | Unit 16 section 4 (lines 85-86) makes step 4's second half new shell code in this unit: a loop over 'git status --porcelain', filtered by step 1's record. S1 claims it is observed by AC1 and AC2, but AC1 (lines 131-137) reads only prompt text. AC2 (lines 138-142) asserts only that '<spec>' is clean and that its HEAD blob matches its hash-object, in a scratch repository with no foreign paths, and it never checks what else the commit holds. A loop that stages nothing, or one whose filter is inverted, leaves AC1 and AC2 green. The effect is contained. In a real tree, a stage-nothing loop leaves the generated index stale, and unit 15 section 5 says the pre-commit hook's check 9 refuses that by name. An inverted filter mis-commits only when foreign dirty paths exist, which is a narrow path, and it lands on a branch. The fix is sound: planted foreign paths plus a name-list check on HEAD observe both failure shapes, and the inverted-filter break proves the check can move. | sound |
| 3 | underspecification | memory/builds/aGraftedHelix/spec/2026-10-04-spec-TOOL-aGraftedHelix-16.md:section 2 S3 / section 6 AC1 | high | medium | confirmed | Unit 16 S3 (lines 34-37) requires that the prose 'never restate a command' and claims 'Observed by AC1'. AC1 asserts only that there is exactly one fenced block, plus what that block contains. Unit 15's prompt steps 2-3 (unit 15 lines 168-174) spell 'git add -- <the spec paths>' and the generator call as inline code in prose, so if they stayed, AC1 would still see one fenced block and stay green. The effect is contained. An agent that follows the stale prose commits the pre-render blob, and the resolver's HEAD vs hash-object compare then throws the named dirty-tree refusal: a loud failure, not a silent wrong result. The fix is unsound because its predicate is too broad and reds a correct prompt. Unit 15's step 1, which stays as prose outside the git sequence, names `gen_build_index.py` as the reader of the H1 key. Unit 15's step 3 prohibition 'Never `git add -A` or `git add -u`' is a rule, not a restated command, and it also carries 'git add' text. | unsound |
| 4 | underspecification | memory/builds/aGraftedHelix/spec/2026-10-04-spec-TOOL-aGraftedHelix-16.md:section 4 'The arm' / section 6 AC2 | medium | medium | confirmed | The rendered harness fills the token as 'tools/memory-tree' (unattended-build.js line 361 reads 'python tools/memory-tree/gotchas.py'), so the block's step 3 is a relative 'python tools/memory-tree/gen_build_index.py --write'. Section 4's _b1-shaped scratch repository places no generator at that path. The _b1 precedent runs '$HERE/gen_build_index.py' by absolute path (check-memory-hygiene.test.sh:2731), and the generator imports its siblings tree_lib and backlog (gen_build_index.py:149 and :290). S4 says only 'with the real gen_build_index.py', not where. AC2's green half holds even if the generator never ran: the spec is then committed unrendered, clean, with equal hashes. Only the staged half, a once-observed break, would fail to red and expose this. The permanent arm's green half has no witness that the generator ran, so a later regression in step 3 stays green. The effect is contained. The fix is unsound because its primary option, committing gen_build_index.py and tree_lib.py, still fails at 'import backlog' (gen_build_index.py:290). Only its parenthetical alternative, the whole kit directory, works. | unsound |
| 5 | underspecification | memory/builds/aGraftedHelix/spec/2026-10-04-spec-TOOL-aGraftedHelix-16.md:section 2 S2 / section 6 AC1 | medium | low | confirmed | Unit 16 S2 (lines 31-33) claims 'Observed by AC1 and AC2'. AC1 asserts only that the prompt says a non-empty status returns committed: false, and no criterion checks the instruction to quote the porcelain output in 'why'. AC1's staged break covers only the re-add, and AC2 exercises only the clean path. The thrown-by-name half is unit 15's validation, which unit 15's AC4 already observes ('the why text'). Only the quoting instruction is unobserved, and its omission degrades only the error text's detail: the throw still names the stage and whatever 'why' the agent writes, and unit 15's step 5 still asks for the refusal's first lines. The effect is close to cosmetic. The fix is sound. The prompt-text assertion and its staged break observe the quoting clause. The committed:false probe call duplicates unit 15's AC4, which is harmless and changes no unit 15 behaviour. | sound |
| 6 | underspecification | memory/builds/aGraftedHelix/spec/2026-10-04-spec-TOOL-aGraftedHelix-19.md:section 2 S2 / section 6 | high | high | confirmed | S2 states both refusals and says 'Observed by AC2', but AC2 drives only a mode outside CLAIM_MODES at the --hold site. AC1 counts constant members and AC3 checks versions, and section 4's staged break and section 7's arm stage only a phantom MODE. Nothing observes a derived claim-read class outside CLAIM_READS, or a constant member with no case branch reaching the refusal. A build that omits the read-axis refusal passes every section 6 criterion. S3's arm derives its cells from CLAIM_READS, so it would never drive a class the function derives but the constant lacks. That is finding 31's uncovered cell on the read axis, a check certifying coverage it lacks, on the narrow path of an omitted refusal plus a later class. | sound |
| 7 | underspecification | memory/builds/aGraftedHelix/spec/2026-10-04-spec-TOOL-aGraftedHelix-19.md:section 2 S3 / section 6 (versus section 7) | medium | - | refuted | Labelling a suite arm NOT OBSERVED and leaving it to the main loop at VERIFYING is the convention across the whole set: unit 11 S4, unit 14 S3 and unit 18 S3 use the same words. The staged break that observes S3 is named twice, in section 4 'The staged break' and in section 7's New arm line, which is where the build method carries a suite arm's red. So S3 is honestly labelled, and its closure does not rest on an unnamed break. Asking for an AC over the pass's slice is a preference about where the observation sits. It does not make the spec unbuildable or wrong. | unsound |
| 8 | underspecification | memory/builds/aGraftedHelix/spec/2026-10-04-spec-TOOL-aGraftedHelix-19.md:section 6 AC2 | medium | low | confirmed | Part (a) holds. tools/unattended/unattended.sh:23 and run_hold at base 5266d22e (fail 55 at about line 4860 for --code, 4868 for --until and 4876 for --reason, and fail 56 at about line 4912 for --reaped or --keepalive-unreachable) refuse a bare --hold before any claim write. AC2's literal '--hold <slug>' therefore prints a check 55 line and never the mode refusal. The AC goes red rather than passing falsely, which costs a pass cycle and ships nothing wrong, so the grade is low. Part (b) is refuted. Unit 1's call-site table puts the claim write for --hold, --landed and --abort 'after stage_or_fail', and run_hold writes its facts and stages the record before that point by design (unit 1 S9 says the local record is the truth). A record written before the refusal is that order, not a misplaced refusal. HEAD does not move inside run_hold, and the comment at lines 1008-1012 describes the agent's later commit. | unsound |
| 9 | contradiction | memory/builds/aGraftedHelix/spec/2026-10-04-spec-TOOL-aGraftedHelix-18.md:section 4 The order, against section 5 error states and section 4 Alternatives rejected | high | high | confirmed | Section 4's order table runs write_lease before the holder's claim write, and section 5 keeps a holder write that does not complete as unit 1's 'announce, continue'. Take a changed-session --resume (s1 -> s2) whose claim push times out, or that runs offline, which unit 1 section 4 says the holder path supports. Afterwards the record names s2 and the claim names s1. On the next s2 call, 'mine' fails: it needs the record's keepalive AND session, and unit 11 section 3 leaves that test unchanged. 'same session' fails too, because the claim's s1 differs from the environment's s2. The claim therefore reads as foreign, and the holder column answers check 90 for every foreign verdict. A live run is forced to --abort claim-lost, the exact consequence section 1 exists to prevent. A lost race on that call likewise reaches check 90 only after write_lease has rewritten and staged the record, which breaks unit 1 section 5's 'the CAS precedes every local write'. AC1 and AC2 cover only a completed push. The path is narrow (a session change plus an incomplete push) and the result is wrong, so the grade is high. | unsound |
| 10 | contradiction | memory/builds/aGraftedHelix/spec/2026-10-04-spec-TOOL-aGraftedHelix-17.md:section 1 Goal and section 4 Evidence / The staged break, against section 3 and section 2 S1 | medium | medium | confirmed | Section 1 says unit 14's arm 'stays green with check 27's status=1 deleted, because check 28 still sets the exit', and section 4 Evidence reads unit 14's branch row as a content duplicate. Unit 14 rev-2 section 4 pins that row as 'a paraphrase, never a verbatim restatement', whose content key differs so that check 28 does not fire. Its AC1 already asserts 'no other line opening check <n>:', with the red-when 'another check holds the exit'. Unit 17's own section 3 says the same thing. The 'arm that cannot fail' premise is therefore false under rev-2, and it is false even with a duplicate row, because unit 14's AC1 would red on the check 28 line. The staged-break rationale in section 4 ('which a break deleting check 27's status=1 alone could not') is stale. S1's separate assertion is a strict subset of unit 14's, so it can never red alone. The arm as built still works, and section 3 states the right premise, so the effect is contained and the grade is medium. | sound |
| 11 | contradiction | memory/builds/aGraftedHelix/spec/2026-10-04-spec-TOOL-aGraftedHelix-16.md:section 2 S3 and S4, against section 4 The arm and section 6 AC2 | medium | medium | confirmed | Unit 16 section 4 The block step 3 is `python {{MEMORY_TREE_DIR}}/gen_build_index.py --write`. The render fills that token repo-relative: the shipped harness's CHECKLIST line reads `python tools/memory-tree/gotchas.py`. Section 4 The arm defines the scratch repository as the _b1 shape: a conf, a charter, a build README and the waiver, committed once. The _b1 fixture (check-memory-hygiene.test.sh:2706-2735) runs the generator out of tree as `"$_PY" "$HERE/gen_build_index.py"` and never puts it in the tree. The generator also imports its siblings tree_lib and backlog, so copying one file would not work either. The block has no fail-fast, and the arm's only assertions are a clean status and HEAD:<spec> equal to hash-object. Both hold when the spec is committed unrendered. S4's phrase 'with the real gen_build_index.py' leaves the arm's shape ambiguous. The one-time staged break and AC2's staged clause would not go red as the spec predicts, so the builder would be pushed to fix the fixture at build time. The lasting defect is the one the finding names: the standing arm has no liveness assertion, so a later failure of the generator in scratch reads green. The effect is contained, so the grade is medium. Unit 9 does have a copy-install fixture (AC12). On the fix: with `set -e`, step 4's filter must not be a grep that exits 1 on no match inside a command substitution. Otherwise a call with no foreign changes aborts before the commit. | sound |
| 12 | contradiction | memory/builds/aGraftedHelix/spec/2026-10-04-spec-TOOL-aGraftedHelix-19.md:section 2 S2, against section 3 (case-label parsing rejected) and section 7 New arm | medium | medium | confirmed | Unit 19 S2 defines the refusal only for a mode outside CLAIM_MODES, or a derived class outside CLAIM_READS. A member added to a constant is inside it, so the membership test passes it, and the clause 'one added to the constant without a branch reaches the refusal too' is false as specified. S3's derived-set assertion catches that direction instead, through the missing typed outcomes. Section 3 rejects the case-label reader because 'S2's refusal already makes the constants load-bearing'. Section 7's only new arm, however, is the derived-set assertion, and S2's refusal is observed once by AC2 in a scratch copy. Section 4 Inventory says 'no new ... check', so the refusal is not a numbered `fail N` site. check-arms.py discovers only those sites, which means the listed 'harness arms' leg cannot force an arm or a pin onto it. If a later change drops the refusal, nothing reds. A class then added to the function without its constant goes undriven by the derived arm, which reopens finding 31's class. Two later changes are needed, so the effect is contained: medium. The fix is unsound as written. Its first option is a `*)` default that refuses with the SAME named error. Under that option, the staged break, which removes the membership test, still has the undeclared branchless mode refused by the default with the same text. The arm therefore cannot be observed red. | unsound |
| 13 | contradiction | memory/builds/aGraftedHelix/spec/2026-10-04-spec-TOOL-aGraftedHelix-19.md:section 4 The staged break, against section 4 The constants | low | low | confirmed | Unit 19 section 4 The constants lists eight CLAIM_READS members and four CLAIM_MODES members. S3 derives the cell set as the product of the two constants. A phantom member appended to CLAIM_MODES therefore adds eight cells, one per CLAIM_READS member. The four that section 4 The staged break expects would be the count for a phantom appended to CLAIM_READS. The built arm's behaviour does not depend on the prose figure; only the recorded expectation of the observation is wrong. Low. On the fix: the first option is clean. The alternative, moving the phantom to CLAIM_READS, must also rewrite section 5 testing ('a phantom mode') and section 7's New arm line ('appended to CLAIM_MODES'), or it leaves a new contradiction. | sound |
| 14 | contradiction | memory/builds/aGraftedHelix/spec/2026-10-04-spec-TOOL-aGraftedHelix-19.md:section 1 Goal | low | low | confirmed | Unit 19 section 1 says the arm stays green 'while unit 12's §3 calls it the class gate'. Unit 12 at HEAD is rev-2, landed in the same fold commit be389baa0. Its section 3 says the arm 'becomes the class gate for this table only once TOOL-aGraftedHelix-19 derives its cells from the driver; built alone, it is an instance check'. Its rev-2 log line says S3 and section 3 'stop calling the arm the class gate'. Unit 19's goal therefore cites the superseded rev-1 wording. This is prose only, with no behavioural effect: low. | sound |
| 15 | contradiction | memory/builds/aGraftedHelix/spec/2026-10-04-spec-TOOL-aGraftedHelix-18.md:section 6 AC2, against unit 1 section 4 The claim record | low | low | confirmed | Unit 18 section 1 states that write_lease resets lease-utc. AC2 requires the claim's lease-utc to equal the record's byte for byte after a same-session call with a changed CLAUDE_PID, so the claim's stamp moves without a take-over. Unit 1 section 4 still defines lease-utc as 'when this session took the claim', 'kept across a holder's renewals and reset by a take-over'. Unit 11 S1 already makes holder renewals copy lease-utc from the record, so the inconsistency predates unit 18, which only pins the order and observes the result. Neither unit 11 nor unit 18 records a supersession of unit 1's sentence, and grep of unit 11 for 'kept across' and 'supersed' finds nothing. No verdict, age or take-over line reads the claim's lease-utc; only the renewal comparison does, and it follows the record. The effect is a stale interface sentence: low. The fix's second option is unsound. Keeping the claim's lease-utc while the record's moves contradicts unit 11 S1, which says renewals copy lease-utc from the record, and S6, which says the claim equals the record byte for byte. Unit 11 S2's 'a field the write would set differs' would then find lease-utc differing on every later call, so every holder call would push. That breaks AC2's own 'leaves the claim ref's sha unchanged' clause. | unsound |
| 16 | unstated-assumption | memory/builds/aGraftedHelix/spec/2026-10-04-spec-TOOL-aGraftedHelix-16.md:section 2 S4; section 4 The arm; section 6 AC1 | high | medium | confirmed | Confirmed at tools/workflows/unattended-build.test.sh:170. run_wf traces every prompt as one line, joining the newlines with spaces. S4 tells the arm to take the TRACED commit:specs: prompt with the suite's stub hooks and extract its fenced block. Flattened, the block's commands run together on one line, and sections 4 and 10 never mention it. 18 grep '^prompt:<label>:' reads exist, and :286-288 pairs a has with a hasnt_ on one capture, as the finding says. Graded medium, not high. Built as written, the arm fails on its unbroken run, because the flattened block cannot stage or commit and the spec stays untracked. That failure is visible. Most hasnt_ captures share their variable with has arms, which would red loudly if someone stopped flattening. So the could-not-fail outcome needs a further careless step and does not follow from the spec itself. | sound |
| 17 | unstated-assumption | memory/builds/aGraftedHelix/spec/2026-10-04-spec-TOOL-aGraftedHelix-16.md:section 4 The block, step 4 | high | high | confirmed | Section 4 'The block' keeps step 1's record in a shell variable and filters step 4 by it. S3 asks only for one fenced block. Nothing says the block runs as one invocation, and the Bash tool keeps no variables between calls. Unit 15's step 2, which this replaces, kept the record in the agent's own context, so this unit adds the dependence on shell state. If the block is split across calls, the record is unset at step 4, nothing is filtered out, and foreign tracked or untracked work is staged into the spec commit. That breaks the foreign-path rule in unit 15's step 2 and section 5, which calls the case live. S2 runs git status only over the spec paths, and the arm runs the block as one script, so neither catches it. The path is narrow (an agent splitting the block), but the result is a wrong commit, so high. The fix works: a ${rec+x} test separates unset from empty, so a clean tree, where the record is set but empty, still proceeds. | sound |
| 18 | unstated-assumption | memory/builds/aGraftedHelix/spec/2026-10-04-spec-TOOL-aGraftedHelix-16.md:section 4 The block step 3; section 4 The arm | medium | medium | confirmed | Confirmed. The render runs python tools/memory-tree/... (unattended-build.js:361 shows the rendered CHECKLIST path). The _b1 fixture in check-memory-hygiene.test.sh:2706-2735 runs the generator as $HERE/gen_build_index.py and has no tools/ directory in its scratch tree. gen_build_index.py:148-149 and :290 import tree_lib and backlog through the sibling path insert, so copying the one file would not be enough either. The block's steps check no exit status. With step 3 failing, the spec is committed unrendered and both AC2 assertions pass with or without the re-add. The defect is contained, because the required staged-break observation fails to red and exposes it. The production half of the claim is overstated: a pre-commit hook running hygiene check 9 would normally refuse a stale index. The fix works. The copy destination should be derived from the path the rendered block names, not typed as a literal in the suite. Expect tools/memory-tree/__pycache__ to be staged into the scratch commit by step 4, which is harmless to AC2's spec-only assertions. | sound |
| 19 | unstated-assumption | memory/builds/aGraftedHelix/spec/2026-10-04-spec-TOOL-aGraftedHelix-17.md:section 4 The staged break; section 6 AC1 | medium | medium | confirmed | Confirmed. Section 4 says 'a verbatim copy of the base row's text', while AC1 ('a verbatim copy of the base row') and section 7 ('stage the branch row as a verbatim copy of the base row') say whole row. None of them says the new id is kept. row_grammar.py:53 has CHECK = 20, and :677-681 reds an id appearing twice within one row document. Unit 6 S-scope (spec :35-40) grades only keys held by two or more distinct identities, and a key held twice under one identity is not graded. A whole-row copy therefore prints check 20 and no check 28. The arm reds anyway, on unit 14's only-offending-check assertion, so the close could read a red that is not S1's. AC1's pass observation, which demands a printed check 28 line, would expose it, so the effect is contained. The fix works: keeping the id and copying only the body, with an assertion that no check 20 line is printed, pins the red to check 28. | sound |
| 20 | unstated-assumption | memory/builds/aGraftedHelix/spec/2026-10-04-spec-TOOL-aGraftedHelix-19.md:section 2 S2; section 4 Inventory; section 7 | medium | medium | confirmed | The core holds. unattended.sh:637 defines fail(), so check-arms.py discover() includes it, and classify() and cmd_check() require every fail branch to be armed or pinned. Unit 1 writes every claim refusal as a fail call (checks 89, 90 and 91). S2's 'named internal error' does not pin its form. No arm in scope drives it: S3's arm only reds on the staged phantom, and AC2 is a scratch run outside the suite. Section 7 lists the harness-arms leg, so the natural spelling reds a gate the spec owes. Two sub-claims are wrong. tools/unattended/unarmed-branches.txt already holds 10 unattended.sh pin rows, so 'today it has none' is false. Adding a row is not mechanically refused, so 'cannot be pinned' is overstated. Even so, the pin file's policy reserves rows for branches that cannot be armed, and AC2 shows this one can. Contained, because the leg reds visibly, so medium. Either fix option settles the form. Option 1 should also update the 'no new check' line in section 4. | sound |
| 21 | unstated-assumption | memory/builds/aGraftedHelix/spec/2026-10-04-spec-TOOL-aGraftedHelix-19.md:section 6 AC2; section 2 S2 | medium | - | refuted | AC2's `--hold <slug>` ... `over unit 1's fixture` is the same shorthand unit 1 AC9 uses (`When --hold ... run on a fixture run`). The suite's existing --hold arms already supply --code/--until/--reason/--reaped and write ANCHOR_SCOPE=published with a pushed tip (unattended.test.sh:7798, :8258). AC2 is a conjunction, and its first half requires a line naming the phantom mode and CLAIM_MODES. A refusal at check 55, 56 or 57, or at check_clean, cannot print that line, so an earlier refusal reds AC2 and never greens it falsely. S2's 'writes nothing' describes the decision's refusal, and AC2 observes exactly that write, the claim ref sha. Unit 1 F6/S9 say a status-write site announces a write it may not make and never fails the verb, and AC2 asserts no exit code, so there is no contradiction. 'Fails on its first use' refers to check_claim_writable refusing, not to the verb's exit status. The finding is medium, and it shows neither an unbuildable criterion nor a false green. | sound |
| 22 | prior-art | memory/builds/aGraftedHelix/spec/2026-10-04-spec-TOOL-aGraftedHelix-16.md:section 4 'The block' (step 1 and the step-4 loop paragraph); section 2 S1; section 6 AC2 | high | high | confirmed | Unit 16 section 4 pins step 1 as `git status --porcelain --untracked-files=all` and step 4's second half as 'a loop over `git status --porcelain` filtered by step 1's record'. Reproduced in a scratch repo: -uall printed `?? foreign/sub/brief.md` and the default printed `?? foreign/`. The collapsed directory line is not in step 1's record, so `git add -- foreign/` stages every foreign untracked file in it. That breaks the FOREIGN rule S1 says stays unchanged, and unit 15 section 5 names this as a live case (another writer's untracked brief). A not-yet-tracked `build/` or `prompts/` folder has this shape, and so does `__pycache__/` in an adopter that does not ignore it. No repo config sets status.showUntrackedFiles. Neither AC2 nor the S4 arm's fixture holds a foreign path, so both stay green. The consequence is a wrong commit on a narrow but named path, which is high. | unsound |
| 23 | prior-art | memory/builds/aGraftedHelix/spec/2026-10-04-spec-TOOL-aGraftedHelix-16.md:section 4 'The block' steps 3-4; section 2 S2; section 6 AC2; section 10 | medium | medium | confirmed | Step 1 marks foreign tracked edits as never staged, but step 3 runs the generator over them anyway. plan() lists inputs with `git ls-files` (gen_build_index.py:698) and reads their bytes off the disk with read_text. Suppose a sibling spec's status header or a BACKLOG.md carries a foreign unstaged edit. Then LIVE.md, the ledger shard and the README regions are clean at step 1, change at step 3, and are staged at step 4, so the commit holds views derived from work it does not contain. Unit 15 section 5 says check 9 refuses this at the hook. Check 9 runs `gen_build_index.py --check` (check-memory-hygiene.sh:1039-1041), and cmd_check (:2130) compares a disk render with disk bytes, never the index, so it passes. dMendedRecall-2 rev-3 S3 measured this exact DRIFT over a clean checkout. Unit 16 S1 keeps unit 15's FOREIGN rule, and its section 10 says no seam fits without citing that record. The effect is contained, because the next render or a clean-checkout --check catches it, which makes it medium. | sound |
| 24 | prior-art | memory/builds/aGraftedHelix/spec/2026-10-04-spec-TOOL-aGraftedHelix-16.md:section 4 'The block' step 3 | medium | medium | confirmed | Step 3 runs the generator without -B. gen_build_index.py inserts its own directory on sys.path, imports tree_lib (:149) and backlog (:290), and never sets dont_write_bytecode, so it writes `__pycache__/` beside the kit. Only this repo's .gitignore hides that, and adopt-memory-tree.sh adds no ignore. In an adopter that does not ignore it, any cache path step 1 did not list (a first run, or a new interpreter tag) is staged by step 4. Under step 4's plain porcelain (finding 22), even existing caches collapse to an unlisted `?? .../__pycache__/` line and get staged. The S4 arm runs the rendered relative generator path inside a no-.gitignore `_b1`-shaped repo, and its two assertions cannot see committed caches. dMendedRecall-2 rev-2 S2 added -B to the same render-then-stage rule for this reason. The effect is junk bytecode committed in the spec commit, contained, so medium. | sound |
