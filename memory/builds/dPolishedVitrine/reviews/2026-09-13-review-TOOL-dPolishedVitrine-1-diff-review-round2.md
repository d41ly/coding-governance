**Serves:** diff-review TOOL-dPolishedVitrine-1

# dPolishedVitrine — Tier-2 diff review, round 2

*Node `d`, 2026-09-13. An adversarial pass over `TOOL-dPolishedVitrine-1` after round 1's fold. The
unit renders the unattended build harness at install from `unattended-build.template.js`, filling
`{{KIT_DIR}}`, `{{TOOL_ROOT}}` and `{{MEMORY_TREE_DIR}}`, and gives the unattended Skill's checklist
line the same token. The shape was four primed finder lenses, five skeptic batches prompted to
REFUTE each finding, and one synthesis. Round 1's confirmed set, F1 to F5, went to the lenses as
prior findings. The brief asked two questions. Is each round-1 finding actually fixed on the fixture
its fix names? And what did the fold break? It named four places to look hardest: the consumer
migration sequence, the regenerate ordering, the merge with `main` that took unattended to 1.20 at
every carrier, and every govkit change. Every `file:line` below was re-opened at the tip in this
worktree before it was written down. The consumer reproductions quoted are the skeptics' own, run on
scratch clones of core at `3a2ce818` and NicoCares at `3b4f79fc`. Where this synthesis ran or read
something itself, the text says so.*

**Range reviewed: `24f8c712...d36549fb50de39def4d0484b803a759bdd6c4f35`** (tip `d36549fb`, branch
`cld/derived-harness-paths`, 65 files, +3869/-228). Round 2. The fold this round exists to read is
`0c0e1757..d36549fb`, from round 1's recorded tip: the round-1 record, the fix `2814aaa5`, the merge
of `main` at `f0e61a2c`, and two records commits.

## Verdict: BLOCKED

One BLOCKER, and it is round 1's F1 still standing at one of its two consumers. The fold repaired F1
in scope with a two-step consumer migration in `WIRE-INTO-PROJECT.md`. At core, step 1's
`git add -A && git commit` is refused by core's own pre-commit receipt arm. The verb that would clear
that refusal, `adopt --re-adopt`, refuses a staged tree, so the runbook stops before step 2 and names
no way through. There are eight distinct defects in all: 1 blocker, 0 high, 3 medium and 4 low. Five
of the eight sit in the runbook's migration section. Apart from R2-1, and R2-6 on a path neither
consumer takes, none of them stops the migration, but each makes the receipt or the runbook state
something that is not true. Round 1's F2, F3 and F4 are fixed on the fixtures their fixes name. F5
is fixed in form and not in substance. The merge's version move is clean.

## Review shape

Raw 13 · confirmed 12 · refuted 1 · unverified 0 · precision 0.92.

The twelve confirmed findings carried three co-reported duplicate sets. Raw ids 3, 6 and 10 are the
step-1 commit wedge. Raw ids 1 and 9 are the declined renders pinned to the new vintage. Raw ids 4
and 8 are the pin set drawn from the old receipt. Merging those leaves **8 distinct defects**, R2-1
to R2-8 below, and each names the raw ids it absorbs. The merge is this synthesis's, and it is
separate from the pipeline's own duplicate count in the integrity section. Raw id 2 was refuted by
its skeptic. Its text did not reach synthesis and nothing of it is carried.

The severity counts in this report are over the eight distinct defects, as round 1's were over its
five, so the blocker count compares like with like across rounds. By raw id, 3, 6 and 10 are BLOCKER;
1, 7, 9 and 11 are MEDIUM; 4, 5, 8, 12 and 13 are LOW. Three raw findings moved from the severity
their lens gave them:

- Raw ids 3, 6 and 10 were filed HIGH. They are raised to BLOCKER, and R2-1 says why.
- Raw id 9 was filed LOW. It is the same defect as raw id 1, so it takes raw id 1's MEDIUM.
- Raw id 4 was filed MEDIUM. It is the same defect as raw id 8, so it takes raw id 8's LOW, for the
  reasons given under R2-5.

Five raw findings overstated a consequence, and the text below corrects each one:

- Raw id 1 said the staleness signal is gone "for good". It returns when the template next moves.
  At NicoCares the memory-tree kit's own `kit dogfood parity` leg still reds those renders. Core
  carries no such leg. Both gate manifests were read here.
- Raw id 1 listed the lexicon Skill among the pinned renders. NicoCares' receipt has no row for
  `.claude/skills/lexicon/SKILL.md`, which was read here, so the pin rule never sees it. That path
  belongs to R2-5.
- Raw id 10 called `--no-verify` forbidden at core. Core's hook describes it as a rare, deliberate
  bypass. The wedge stands either way, because the runbook names no bypass.
- Raw id 11 said govkit's printed remedy "reverses the migration". It does not move the role back,
  because `adopt` takes the role from the descriptor (`tools/govkit/govkit.py:8049`). It does drop the
  pinned evidence and every edited row's base.
- Raw id 8 said each new unattributed row keeps every later `update` from re-stamping. Both
  consumers already carry older unattributed rows that withhold the stamp (R2-4), so the extra cost
  is small.

## Run integrity

- Lenses: **4/4 returned, 0 DIED.**
- Skeptic batches: **5/5 returned, 0 DIED.**
- 0 contradictory verdicts demoted to unverified · 0 spurious verdicts discarded · 0 duplicates
  removed by the pipeline.
- 0 findings left UNVERIFIED. Nothing in this report is outstanding for lack of a skeptic verdict.

The run is COMPLETE. No lens died, so the zero counts above are measurements rather than gaps, and
"found clean" below means the area was read.

## Round 1's findings, fixed or not

| Round 1 | Status at `d36549fb` | What says so |
|---|---|---|
| F1 BLOCKER, the receipt keeps the harness `engine` | **NOT CLOSED.** The silent green is gone: nothing the runbook prescribes certifies gov's `tools/`-spelled render as current. But the runbook wedges at core (R2-1), its pin rule is wrong in three ways (R2-2, R2-5, R2-6), and it promises a Done state neither consumer can reach (R2-4). | The `[-PV] F1` arms pass here, on fixtures built by `apply` in hookless repos, which cannot show any of the four. |
| F2 HIGH, the regenerate ran before its input | **FIXED** on its fixture. The unclaimed-source landing (`govkit.py:7030`) now precedes the re-render block (`:7291`), and the failure text depends on whether the kit has a `[check]` argv (`:7380-7390`). | The `[-PV] F2` arms and the F2 NEGATIVE pass here. Now that the regenerate runs at a consumer, it surfaced R2-3. |
| F3 MEDIUM, one pair's refusal blocked both | **FIXED** in code. Only the pair whose template carries `{{MEMORY_TREE_DIR}}` is skipped (`tools/workflows/check-protocol-parity.test.sh:94-108`, `:169-175`). | The ten `PV-F3` arms pass here. The fold left spec S3, §5 and two README bullets saying "refusal" (R2-8). |
| F4 LOW, the guard missed the leg's new input | **FIXED.** `guard = []` at `tools/workflows/kit.toml:97`, and neither carrier in `tools/gate-legs.json` has a guard. | Read here. |
| F5 LOW, carriers promised a re-render without the flag | **HALF.** Every carrier names `GOVKIT_RERENDER`, and selfcheck arm 7l gates that. Three carriers now say a flag-off `update` prints nothing, which is false (R2-7). | `govkit.py selfcheck` here: 10 claim sentences across 2 kits, all naming the flag, exit 0. |

## Findings

| # | Sev | Where | One line | Raw ids |
|---|---|---|---|---|
| R2-1 | **BLOCKER** | `WIRE-INTO-PROJECT.md:1006` | step 1 commits the render while the row is still `engine`; core's pre-commit refuses it and `adopt` refuses the staged tree | 3, 6, 10 |
| R2-2 | MEDIUM | `WIRE-INTO-PROJECT.md:1015` | the pin rule dates every commit-less render at the new vintage, including renders step 1 declined to regenerate | 1, 9 |
| R2-3 | MEDIUM | `tools/workflows/check-protocol-parity.test.sh:208` | the regenerate creates `REVIEW-PROTOCOL.md` in a consumer that never installed it, and govkit prints nothing about it | 7 |
| R2-4 | MEDIUM | `WIRE-INTO-PROJECT.md:1046` | "the next update re-stamps" cannot happen at either consumer, and govkit's printed remedy drops the pins | 11 |
| R2-5 | LOW | `WIRE-INTO-PROJECT.md:1013` | pins come from the old receipt's rows, so a tracked destination it never rowed comes back `unattributed`, and the read-only check passes it | 4, 8 |
| R2-6 | LOW | `WIRE-INTO-PROJECT.md:1015` | after a three-way conflict in step 1 the row keeps its old commit, and the pin names a base where gov has no template | 5 |
| R2-7 | LOW | `tools/workflows/check-protocol-parity.test.sh:23` | round 1's F5 rewording says a flag-off `update` prints nothing, but it prints `re-rendered` | 12 |
| R2-8 | LOW | `memory/builds/dPolishedVitrine/spec/2026-09-12-spec-TOOL-dPolishedVitrine-1.md:35` | spec S3, §5 and the build README still say an unanswered probe refuses | 13 |

---

### R2-1 — BLOCKER · `WIRE-INTO-PROJECT.md:1006` · step 1's commit wedges at core

The mechanism, step by step:

- Core's receipt rows `scripts/workflows/unattended-build.js` as `engine`, with `oid == gov_oid ==
  75763c4e`. This was read here from core's `.governance/install.json`. At the tip gov's source is
  `ac362480`, so step 1's `update` grades the row `stale` and takes the raw arm. That arm stages gov's
  `tools/`-spelled blob through the index and records it as the row's `oid`
  (`tools/govkit/govkit.py:6719-6742`).
- The review-harness regenerate then writes the correct render to the worktree only. It is a `cp`
  (`tools/workflows/check-protocol-parity.test.sh:216`), and nothing re-records the row afterwards.
- The runbook's `git add -A` stages that render. Core's pre-commit (core `.githooks/pre-commit:85-92`,
  installed at its `core.hooksPath`) runs `scripts/check-receipt.sh --staged` whenever
  `.governance/kits.json` exists and a `scripts/**` path is staged. `OWNED_BY_TARGET` in core's
  `scripts/check_receipt.py:38` is `seed, project-owned, rendered, attributes, forked`. `engine` is not
  in it, so the staged render is compared with the recorded `ac362480`, and the hook exits 1. All
  three were read here.
- The hook's remedy is `adopt --re-adopt --write`. `demand_adopt_index_clean` (`govkit.py:7878-7902`)
  refuses any index that differs from HEAD, on read-only runs as well. Step 2 cannot run before step
  1's commit, and step 1's commit cannot land.

Two skeptics reproduced it on a scratch clone of core at `3a2ce818`, with gov at `d36549fb`. Step 1's
update exited 0 and ran both regenerates. After `git add -A`, `bash scripts/check-receipt.sh --staged`
printed `scripts/workflows/unattended-build.js is 4d1fe818… but the receipt records ac362480…` and
exited 1. `adopt --re-adopt` on the same staged tree refused with `25 path(s) in the target's index
differ from HEAD`. With the commit forced, step 2 converged and core's full receipt-sync leg was
green, so only the intermediate commit is blocked. One skeptic also saw the hook red earlier, on
core's hygiene checks 3 and 21, over files step 1 created, among them the `REVIEW-PROTOCOL.md` of
R2-3. The build journal records this exact state in its F1 entry: "receipt-sync reds"
(`memory/builds/dPolishedVitrine/build/2026-09-12-build-TOOL-dPolishedVitrine-1-1-journal.md:180-181`).
The runbook does not carry it. Core already tracks this deadlock class as `ABL-dMuffledSentinel-3`,
which is OPEN (read here). NicoCares has no staged receipt arm: nothing under its hooks path names
`check-receipt`, checked here. So NicoCares does not wedge.

This is the `fixture-removes-the-path-under-test` class. The `[-PV]` fixtures commit through
`settle()` in repos with no hooks, so the consumer's commit-time gate never runs against the
sequence.

**Why BLOCKER, when the lenses filed it HIGH.** Round 1 made the hand-off to core and NicoCares wait
on "the sequence that actually converges", verified on a schema-3 fixture before any consumer is
handed it. The sequence that was handed does not converge at core as written, and neither the
runbook nor the refusal it hits names a way through. That is round 1's F1 still open at one of its
two named consumers, not a new and lesser defect. Two things keep it from being worse: it fails
loudly, and it writes nothing wrong. It stops at the commit, and the index holds exactly what
`update` recorded.

**Fix.** Route (b) is preferred, because it needs no bypass:

- In step 1, commit what `update` staged and leave the regenerated harness unstaged, for example
  `git add -A -- . ':(exclude)<kit>/unattended-build.js'`. The index then holds update's blob, which
  equals the receipt `oid`, and the hook passes.
- Step 2's `adopt` permits unstaged edits. It takes `oid` from the index and `sha256` from the
  worktree (`govkit.py:8078-8084`).
- Then stage the render and the receipt, and commit. By then the row is `rendered`, which
  receipt-sync exempts.
- The row's recorded `oid` then names update's blob rather than the committed render. `classify_row`
  reads the index live (`govkit.py:5732-5734`) and receipt-sync exempts `rendered`, so the stale `oid`
  is inert. The fold should still decide whether a closing pinned `adopt --write` tidies it, and
  assert whichever end state it picks.

Route (a) also converges, as the skeptics measured. It names a sanctioned `--no-verify` for step 1's
commit at any target whose pre-commit compares staged blobs to the receipt, and says why: the row
stays `engine` until step 2. It is the smaller edit. Whichever route is chosen, amend the spec's §3
hand-off (`:99-105`) and §4 Rollout step 1 (`:213-214`) in the same fold.

**Left-shift gate.** Give the `[-PV]` target the consumer's commit-time gate. That is a pre-commit
hook in the fixture that reds when any staged row outside `seed, project-owned, rendered,
attributes, forked` has an index blob that differs from its receipt `oid`, which is
`check_receipt.py`'s rule. Commit the runbook's steps through `git commit` rather than `settle()`, and
assert each commit lands. For the class: every `[-PV]` arm that ends at a consumer commit commits
through that hook, so a fixture cannot pass by lacking a gate the consumer has.

### R2-2 — MEDIUM · `WIRE-INTO-PROJECT.md:1015` · the pin rule dates renders nobody regenerated at the new vintage

`base = f.get("commit") or (to if f.get("role") == "rendered" else "")` pins every tracked `rendered`
row that records no `commit` to TO. `apply` writes every `rendered` row without a commit
(`govkit.py:4667-4668`), and `adopt` records none for an unattributed row (`:8113-8118`). Step 1
regenerates only kits that declare `[[regenerate]]`, which at the tip are review-harness and
unattended. Every other kit that ships rendered rows is declined with "this kit ships `rendered` rows
and declares no [[regenerate]] argv, so they stay one vintage stale" (`:7334-7344`). The pin rule then
records those rows at TO anyway. `adopt` stamps `commit` = TO, `gov_oid` = the template at TO and
`evidence` = `pinned` (`:8099-8107`) on bytes rendered from an older template.

On the next `update`, the index blob differs from the new `gov_oid` while gov's template equals it,
so the row grades `patched`, which reads as a local edit. Pinned at its true vintage, the same row
reads `re-rendered` (`:6385-6386`). The runbook erases update's stale-render label.

The evidence:

- Reproduced on a fixture applied at `24f8c712`, at prefix `scripts` with memory-tree flat, against a
  TO vintage that adds one line to `HYGIENE.template.md`. Step 1 printed `DECLINED memory-tree`. After
  the runbook, `memory/HYGIENE.md` was rowed `pinned` at TO without the new line, and the next update
  graded it `patched [rendered]`. A control pinned at `24f8c712` printed `re-rendered`.
- On the NicoCares clone, `memory/HYGIENE.md`, `memory/TEMPLATE-SPEC.md` and
  `memory/guides/BUILD-METHOD.md` hold memory-tree 2.68 bytes, while the templates at `d36549fb` carry
  2.69. The re-adopt pinned all three `<- d36549fb`. The first update had graded them `re-rendered`,
  and the second graded them `patched`.
- Read here: NicoCares' receipt holds 8 commit-less rendered rows. Five of them come from
  memory-tree, drift-audit and memory-recall, and none of those kits declares `[[regenerate]]`. Core's
  receipt holds 8 unattributed `rendered` rows, and the finder counts 6 of them from kits without a
  regenerate.

The reach has limits. No bytes move, and the label returns when the template next moves. At
NicoCares the `kit dogfood parity` leg still reds the memory-tree renders. Core has no such leg, so
there update's report is the only staleness signal it has. The effect is the base move that
`DEPL-dGaugedVintage-8` withholds the stamp to prevent, done in one step by an operator following the
runbook. No backlog row covers it.

**Fix.** Pin a render to TO only when its kit's regenerate ran at exit 0 in step 1. Leave every other
commit-less render unpinned. It then comes back `unattributed`, which at both consumers is what it
already is. Pinning it to the receipt's pre-step-1 `gov_commit` instead is true only if that stamp is
the vintage the render was made at. A flag-off `update` or `--allow-ungraded` can advance a stamp
without re-rendering, so treat that pin as an operator's assertion, never a default. Say this in "Why
the pins" (`WIRE-INTO-PROJECT.md:1026-1032`) and in spec §4 Rollout step 2 (`:215-219`). The
consolidated rule is under "One fold for the runbook" below.

**Left-shift gate.** A `[-PV]` arm with a second fixture kit that ships a rendered row, declares no
`[[regenerate]]`, and changes its template between A and B. After the migration, assert that the next
`update` grades that row `re-rendered` and not `patched`. And retire the second copy of the rule.
`derive_pv_pins` (`tools/govkit/selftest.py:8521-8537`) is a hand-kept copy of the runbook's snippet,
so R2-2, R2-5 and R2-6 each live in two places. Have the `[-PV]` arms extract and run the snippet from
`WIRE-INTO-PROJECT.md` itself, so the arm grades the text an operator will copy.

### R2-3 — MEDIUM · `tools/workflows/check-protocol-parity.test.sh:208` · the regenerate installs a document the consumer never installed

`--render` now creates a missing live copy, with `mkdir -p` and `cp` (`:208-217`). At base, the script
refused a missing live copy before it rendered anything (`[ -f "$LIVE" ] || … exit 1`, base `:43`),
and the kit declared no `[[regenerate]]`. Both changes land in this unit (`tools/workflows/kit.toml:80-81`).
Both were already present at round 1's tip, but F2 kept the regenerate from ever running there.
Round 1's F2 fix makes it run on the introducing update. So `GOVKIT_RERENDER=1 update` now writes
`{memory_root}/guides/REVIEW-PROTOCOL.md` into a consumer that has never had one.

govkit runs the regenerate with its output captured (`govkit.py:7355-7356`) and prints only `ran
review-harness: … -> exit 0` (`:7370-7372`), so the script's own `rendered …` line is swallowed. No
receipt row is minted, no tally line names the file, and nothing stages it. Nothing at the regenerate
site consults a per-file decline either. The only check is `inert`, which skips the whole kit
(`:7318`).

Core does not hold that file, on purpose. It keeps a 46-line extract at
`memory/review-workflow-protocol.md`, and `ABL-dReadoptedConvoy-8` is OPEN, asking the owner to
decide gov's template and its parity leg. Both were read here, and core has no
`memory/guides/REVIEW-PROTOCOL.md`. The runbook's `git add -A` then commits a second protocol copy
ahead of that decision, and step 2's re-adopt rows it `unattributed` (R2-5). On the core clone the
skeptics saw it appear untracked after step 1, and one saw core's pre-commit red hygiene checks 3
and 21 over it, which compounds R2-1. This is a regression the F2 fix exposed rather than one it
wrote.

**Fix.** Give the regenerate a mode that refreshes an install rather than creating one, for example
`--render --tracked-only`. It skips, by name and out loud, any pair whose live copy is absent and
untracked. Use that mode in the argv at `kit.toml:81`. The harness pair is unaffected, because every
consumer that runs this migration tracks the harness already. Creation stays with the hand `--render`
that a fresh install runs (`WIRE-INTO-PROJECT.md:671`). In the runbook, stage named paths instead of
`-A`.

**Left-shift gate.** An arm in `tools/workflows/unattended-build.test.sh`, next to the `PV-F3` layout:
a tree with the harness tracked and no protocol live copy. Run the regenerate argv exactly as
`kit.toml` declares it, and assert that it writes nothing for the protocol pair and names the skip.
For the class, in govkit: take `git status --porcelain --untracked-files=all` before and after each
regenerate, and print every path it created that no receipt row claims. That makes a regenerate that
writes a file nobody rows visible for every kit. It is a govkit change outside §3, so it belongs with
`DEPL-dPolishedVitrine-2`.

### R2-4 — MEDIUM · `WIRE-INTO-PROJECT.md:1046` · the Done criterion cannot be met, and govkit's remedy undoes the pins

The runbook's Done state says "The next `update` writes nothing to the harness and re-stamps".
`_cmd_update` withholds the stamp whenever any receipt row carries `evidence: "unattributed"`,
whatever its role (`govkit.py:7775-7787`). The pin rule leaves unpinned every row that records no
commit and is not `rendered`, and adopt's unattributed branch records no commit (`:8113-8118`). So
every such row that was unattributed before the migration stays unattributed after it. Read here:
core carries 56 unattributed rows, which are 27 `engine`, 13 `project-owned`, 8 `rendered`, 6 `seed`
and 2 `forked`. NicoCares carries 18. By the skeptic's count, 48 stay at core and 10 at NicoCares
after the pin rule, which fits the role breakdown read here. So the next update prints "The receipt
is NOT re-stamped … Clear them with `govkit adopt --re-adopt --write`".

That printed remedy is the unpinned re-adopt. It keeps the harness `rendered`, but it drops the
`pinned` evidence and every edited row's base. That is exactly the state the `[-PV] F1 CONTROL` arm
asserts is the cost of skipping the pins (`tools/govkit/selftest.py:8646-8652`). The runbook sends the
operator from a Done check nobody can pass to a command that discards what step 2 bought.

The `[-PV] F1 ...and re-stamps` arm (`selftest.py:8635-8637`) passes only because an apply-built
fixture receipt starts with no unattributed rows. That is the `fixture-passes-by-finding-nothing`
class.

**Fix.** Restate Done in the runbook and in spec §4 Rollout: the next `update` re-stamps, OR it
withholds the stamp naming only rows that were unattributed before step 2. Add a warning: when the
stamp is withheld, re-run the PINNED adopt, never the bare `--re-adopt` that the message suggests, or
pass `--allow-ungraded` knowingly. Making the message itself name the pinned form is a govkit change,
and it belongs with `DEPL-dPolishedVitrine-1`.

**Left-shift gate.** A `[-PV]` arm whose fixture receipt starts with one unattributed `engine` row,
which is the consumer shape. Assert that the migrated rows end `pinned`, that the stamp is withheld,
and that the withheld message counts exactly that one pre-existing row.

### R2-5 — LOW · `WIRE-INTO-PROJECT.md:1013` · the pin set comes from the old receipt, and `adopt` measures more than it names

`_cmd_adopt` measures every destination the TO descriptors plan and the index tracks, and pins only
those that `--pin` names (`govkit.py:8091-8118`). The runbook builds `--pin` from the old receipt's
rows (`:1013-1017`), and `derive_pv_pins` copies that (`selftest.py:8527-8537`). So a tracked
destination the old receipt never rowed is measured unpinned. A render then comes back
`unattributed`, because a render never equals its template. A receipt bootstrapped by `adopt` rows
only what was tracked when it was adopted, so both consumers have such destinations. A receipt
written by `apply` rows every rendered destination as `written: False` (`govkit.py:4667`), which is
why the fixtures cannot show this.

The instances:

- Core: `memory/guides/REVIEW-PROTOCOL.md`, created by R2-3's regenerate and committed by
  `git add -A`. The skeptics' pin script emitted 135 pins and none for it, and the read-only adopt
  printed `unattributed [rendered] memory/guides/REVIEW-PROTOCOL.md`.
- NicoCares: `.claude/skills/lexicon/SKILL.md`, which is rendered, and
  `scripts/check-memory-hygiene.test.sh` and `scripts/unattended/unattended.test.sh`, which are
  project-owned. All three are tracked and have no receipt row, which was read here.

The read-only guidance at `:1034-1035` asks for "no `unattributed` row that the old receipt
attributed", and it passes every one of them. The Done line at `:1044-1045`, "No row is
`unattributed` that was not before", is false at both consumers.

**Why LOW, when raw id 4 filed MEDIUM.** The new rows are honest, because `adopt` says it cannot
attribute them and that is true. Both consumers' stamps are already withheld by older rows (R2-4).
And the two project-owned rows would stay unpinned even if the receipt had rowed them, by the pin
rule's own design. What is wrong is the runbook's check and its Done claim, not the receipt.

**Fix.** Derive the rendered pins from `adopt`'s own plan, for example from the `[rendered]` lines of
a first read-only run, rather than from the receipt. Tighten `:1034` so it flags every `unattributed`
rendered row, and every row new to the receipt, unless the runbook states why it is expected. Say in
the runbook that rows new to the receipt are measured unpinned.

**Left-shift gate.** Add two destinations to the `[-PV]` fixture that the base receipt lacks: a
tracked rendered destination and a tracked, edited project-owned one. Assert that the pin derivation
covers the rendered one, and that the read-only check flags the other.

### R2-6 — LOW · `WIRE-INTO-PROJECT.md:1015` · a conflicted step 1 leaves a pin gov cannot resolve

When step 1's three-way merge conflicts on the harness, `update` leaves the row untouched, still
`engine` and still at its old commit. It writes an order file, takes an `r.fail` and does not
re-stamp (`govkit.py:6948-6959`). The regenerate still runs, because its loop does not look at earlier
failures (`:7313` onward). So the parity check the runbook prescribes at `:1005` passes, and nothing in
step 1 checks update's exit code. Step 2 then emits `--pin <kit>/unattended-build.js=<old commit>`.
The TO descriptor sources that destination from the template, which gov did not have at that commit,
so `adopt` raises `gov holds no blob for …template.js at <old>` (`:8099-8102`). Nothing is written, and
the runbook gives no recovery.

It was reproduced on a synthetic fixture whose harness delta the relocate rung cannot explain. On the
real blobs, `git merge-file` with base `75763c4e`, theirs `ac362480`, and ours equal to base with only
the `CHECKLIST` line at `:229` edited, exits 1 with markers at 228-234. Gov's comment edit at `:228`
sits directly above the line an adopter would hand-fix.

**Why LOW.** Neither named consumer hits it. Core takes the raw arm, and NicoCares' actual delta
merges cleanly. The failure is a loud refusal that writes nothing.

**Fix.** Make step 1 require that `update` exit 0 with 0 conflicts before its commit, and say to
resolve the conflict order and re-run `update` otherwise. Under the consolidated rule below, a
rendered destination's pin comes from the TO plan and never from a recorded commit, so a stale commit
cannot reach `--pin`.

**Left-shift gate.** A `[-PV]` arm whose harness delta sits next to gov's change. Assert that step 1
stops, with `update` exiting 1 and the conflict named, and that the pin derivation never emits a pin
for a rendered destination at a commit where the TO source does not exist.

### R2-7 — LOW · `tools/workflows/check-protocol-parity.test.sh:23` · round 1's F5 rewording trades one false sentence for another

Three carriers now say that with the flag off, `update` says or prints nothing:

- `tools/workflows/check-protocol-parity.test.sh:22-23`: "re-renders nothing and says nothing about
  it".
- `tools/workflows/README.md:29-30`: "re-renders nothing and prints nothing about it".
- Spec `:221`: "runs neither regenerate and prints nothing about it".

In `_cmd_update`'s verdict loop, a `rendered` row whose verdict is `diverged` or `stale` is relabelled
`re-rendered` and printed (`govkit.py:6385-6386`, `:6394`), before `GOVKIT_RERENDER` is read at
`:7309`. A moved template always makes the template side differ, so a flag-off update prints
`re-rendered [rendered] <kit>/unattended-build.js` while no render ran. What is true is narrower: the
regenerate is declined without output, and the DECLINED lines print only under the flag
(`:7395-7403`). `tools/workflows/kit.toml:70-72` already says exactly that. It reads "declines this
block without printing anything" and "with no output naming GOVKIT_RERENDER", and it is the wording
to copy.

Round 1's F5 named the `re-rendered` label as the source of the misreading. The fold's text now
asserts silence beside it, so an operator who reads "prints nothing" will take that line as proof the
render ran. Arm 7l grades only that the flag is named, which its own comment states.

**Fix.** Reword the three carriers to `kit.toml`'s form, and add that the row is still printed as
`re-rendered` although nothing ran. Relabelling the verdict is the alternative. It trades against
`DEPL-dRetiredFork-3`'s rule that flag-off output stays byte-identical, and that trade is the owner's.

**Left-shift gate.** A `[-PV]` arm that runs a flag-off `update` over a moved template and asserts the
render's output line, so the behaviour the carriers describe is pinned. Then extend arm 7l with the
negative half: in a kit that declares `[[regenerate]]`, a sentence claiming a flag-off `update`
prints or says nothing is a red. This is the `two-answers-to-one-question` class.

### R2-8 — LOW · `memory/builds/dPolishedVitrine/spec/2026-09-12-spec-TOOL-dPolishedVitrine-1.md:35` · the F3 fold left the refusal standing in its siblings

Rev-5 amended S8, §4's probe paragraph and AC4 to the per-pair skip. These still say an unanswered
probe refuses:

- S3 says the parity script "probes `{{MEMORY_TREE_DIR}}` and refuses when the probe finds nothing"
  (`:35`).
- §5's error-states line lists "a failed probe" among the cases that "each have their own refusal.
  None of them writes anything." (`:253-255`).
- The build README says "A missing checklist script is a refusal at render time"
  (`memory/builds/dPolishedVitrine/README.md:26`) and "A path nobody has proved exists is a refusal
  that names the override" (`:35-36`). Both are true of the unattended adopter and false of the parity
  path.

§5's risks line, "The first is probed and refused" (`:258-259`), can be defended through the refusal
of a misplaced override, so it is the weakest of the set. The code skips per pair, exits 0 and still
writes the protocol (`tools/workflows/check-protocol-parity.test.sh:94-108`, `:169-175`). The spec
now gives two verdicts for one case. A lander checking against S3 or §5 would red a correct parity
script, or accept a refusal as conforming. This is the `amendment-leaves-its-other-half-standing`
class, and the skeptic notes this spec already fixed one instance of it at rev-3.

**Fix.** In the same rev, amend S3, §5's error-states and risks lines, and the two README bullets to
the per-pair skip. Keep "refusal" only for a misplaced override and for the unattended adopter, as S8
and §4 already say.

**Left-shift gate.** None new. Spec prose against a script is not machine-gradable here. Record it as
a live instance of the catalogued class, and have the fold's rev line list every clause that
`grep -n 'refus'` returns over the spec and the README, each with its disposition. That is the
gotcha's own Check, applied.

---

## One fold for the runbook

R2-1, R2-2, R2-4, R2-5 and R2-6 all touch `WIRE-INTO-PROJECT.md:999-1051` and its mirrors in spec
§3 and §4. Their fixes interact, so here they are as one sequence. It is a sketch. It has to be
verified on a fixture bootstrapped by `adopt`, carrying a `--staged` receipt hook and one
pre-existing unattributed row, before any consumer is handed it.

1. Run `GOVKIT_RERENDER=1 update --write`. Require exit 0 and 0 conflicts (R2-6). Keep its output,
   and require a `ran <kit>: … -> exit 0` line for review-harness and for unattended (R2-2).
2. Commit what `update` staged, leaving the regenerated renders unstaged, and stage named paths
   rather than `-A` (R2-1, R2-3).
3. Derive the pins. Take every tracked destination the TO descriptors resolve as `rendered` from a
   read-only `adopt`'s plan, not from the old receipt (R2-5). Pin it to TO when its kit's regenerate
   ran at exit 0 in step 1, and leave it unpinned otherwise (R2-2). Never pin a rendered destination
   to a recorded commit (R2-6). Pin every other tracked row that records a commit to that commit, as
   now.
4. Read the read-only run. The only `unattributed` rows should be rows that were unattributed before,
   plus the declined renders (R2-5).
5. Run `adopt --re-adopt --write` with the pins. Stage the renders and the receipt, and commit.
6. Done: the harness row is `rendered` and `pinned`. The next `update` grades nothing on the harness
   as stale, and either re-stamps or withholds the stamp naming only rows that were unattributed
   before. Never follow that message with the bare re-adopt (R2-4).

The `[-PV]` arms should run this sequence from the runbook's own text (R2-2's gate), so that the
runbook and its test cannot drift apart again.

## What was checked and found clean

These are measurements, not silence. All four lenses returned, so a zero here means the area was
read.

- **The merge's version move.** Run here at the tip, `git grep 'gov:kit unattended@'` finds 15
  carriers, all at 1.20: the four script constants with their same-line markers, the five templates,
  the five gov renders and the kit README. None is left at 1.19. `bash tools/check-kit-versions.sh`
  exits 0, which also covers review-harness 1.8 and govkit 1.11 (`KIT_GOVKIT_VERSION`,
  `govkit.py:45`). No lens reported a merge defect. The journal's per-file check that every line
  either parent added survived was not re-run here.
- **The govkit reorder.** The unclaimed-source landing (`govkit.py:7030`) now runs above the re-render
  block (`:7291`). `touched_kits` already includes kits whose only change is a landing (`:6657-6658`),
  so the swap does not drop a kit from the regenerate loop. The failure text depends on the kit's
  `[check]` argv (`:7380-7390`). The full govkit selftest ran here at the tip: `all arms held`, 1153
  arms, exit 0, in 5m41s, including all 23 `[-PV]` arms. The fold's other govkit changes are
  selfcheck arm 7l and the version constant. `govkit.py selfcheck` exits 0 here. No lens found a
  govkit regression. R2-3 is a consequence of the reorder working, not of the reorder being wrong.
- **Gov's own render.** Run here, `bash tools/workflows/check-protocol-parity.test.sh` printed `in
  parity — 2 rendered pair(s) match their templates for 'tools/workflows' (MEMORY_TREE_DIR
  'tools/memory-tree')` and exited 0.
- **The F3 skip.** Run here, `bash tools/workflows/unattended-build.test.sh` printed `222 arms, exit
  0`, and all ten `PV-F3` arms passed. The skip is loud: it names the pair, the reason and the
  override (`check-protocol-parity.test.sh:170-173`), and the green line counts the skipped pairs
  (`:262-263`). A skip cannot be read as a pass.
- **F4.** The parity leg is unguarded in both carriers, as the fix says.

## Disposition

Round 1 confirmed 1 blocker, and round 2 confirms 1: R2-1, which is round 1's F1 not yet closed at
core. `memory/guides/BUILD-METHOD.md` M8 says to fix every blocker and then re-review the FIX, and that
a blocker unfixable inside the mandate's scope is a park, not a waiver. R2-1 is fixable in scope. The
fix is a runbook and spec change plus a fixture arm. The same file states a convergence rule, under
M4: a review loop re-arms only when its confirmed-blocker count is STRICTLY SMALLER than the round
before, and a standing blocker is then disposed by FOLD when it is a defect in a document the review
read. One followed by one is not smaller. If that rule governs this loop, R2-1 is a FOLD into
`WIRE-INTO-PROJECT.md`, spec §3 and spec §4, and the fold is not re-reviewed. Either way, R2-1's
hook-carrying fixture arm has to land in the same fold, because it is the only check that repair
will get.

The MEDIUM and LOW defects are folds to this unit's own files: the runbook, the spec, the build
README, the parity script, the carriers and the `[-PV]` arms. Two govkit improvements came up along
the way. One is a withheld-stamp message that names the pinned re-adopt (R2-4). The other is govkit
reporting files a regenerate created (R2-3). Both are outside §3, and they belong with
`DEPL-dPolishedVitrine-1` and `DEPL-dPolishedVitrine-2`.

The hand-off to core waits on R2-1, R2-2 and R2-3. The hand-off to NicoCares waits on R2-2, because
the runbook as written records five stale renders there as current.

## Scope and limits of this review

- Findings are anchored to this worktree at `d36549fb`. Every cited line was re-read at the tip.
- This synthesis ran the parity leg, `check-kit-versions.sh`, `unattended-build.test.sh`, the full
  govkit selftest and `govkit.py selfcheck`. It also read core's and NicoCares' live receipts, core's
  pre-commit and `check_receipt.py`, NicoCares' hooks directory, both consumers' gate manifests, and
  core's backlog rows `ABL-dReadoptedConvoy-8` and `ABL-dMuffledSentinel-3`.
- The consumer-clone reproductions behind R2-1 to R2-6 are the skeptics'. They were not re-run here.
  The after-migration counts in R2-4, 48 at core and 10 at NicoCares, are a skeptic's. This synthesis
  read only the before-counts and the role breakdown.
- **The binding line names one unit, on purpose.** The range includes `f0e61a2c`'s merge of `main`,
  which brings in `TOOL-dMuffledSentinel-2` and `TOOL-dMuffledSentinel-3`, and their spec files are in
  the diff. This review read those units only at the merge seam, the unattended version carriers.
  Naming them on the `**Serves:**` line would record a diff review of units no lens reviewed. Build
  dMuffledSentinel carries no diff-review record at all, so a binding here would be read as its only
  one.
- Not covered: the unattended kit's regenerate run end to end at a consumer; a fresh `apply` at the
  tip; and the other hand-off items spec §3 lists, which are NicoCares carrying its cap carve-out into
  the template, the retirement of both consumers' untagged deltas, and adding core's parity leg.
- This is a diff review, not a gate run. The build's AC11 record is the full bar.
