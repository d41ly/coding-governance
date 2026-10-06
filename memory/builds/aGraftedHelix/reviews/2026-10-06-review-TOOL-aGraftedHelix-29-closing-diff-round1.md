**Serves:** diff-review TOOL-aGraftedHelix-29 TOOL-aGraftedHelix-30 TOOL-aGraftedHelix-31 TOOL-aGraftedHelix-32 TOOL-aGraftedHelix-33 TOOL-aGraftedHelix-34

# Tier-2 closing diff review — aGraftedHelix, rotated run, ROUND 1

*Node `a`, 2026-10-06, Tier-2, on `branch/helixir-review-gov-adoption-ce32e1`. This is the closing
review of the ROTATED run of build aGraftedHelix (live record `RUN.md`; the previous run's record is
`RUN.ABORTED.6410435d.md`). It ran through `tier2-review.js`: five finder lenses, five skeptic
batches, then this synthesis. The range is everything since the previous run's closing review
(`2026-10-05-review-TOOL-aGraftedHelix-1-closing-diff-round1.md`, which reviewed
`c3ef6742...a49d53d5`). It holds `018b5675` (the check-wiring linked-worktree note), units 29 to 34,
`3f884e9a` (check-wiring's version constant), and one reconciling merge, `0e65ae59`, which brought
in `origin/main` `290d0d2d`'s 21 commits. That merge's main-side content is not this build's change
and was out of scope. Only its conflict resolutions over 44 conflicted paths were reviewed. The
previous review's H1, H2, H3 and M1 to M9, L1 to L4 are the KNOWN set: units 29, 30, 31 and 32 were
built to fix them, and this round checked those fixes rather than re-reporting the originals. Unit
34's whole unattended suites have NOT been re-run on its re-cut; they run once at VERIFYING. The
synthesis spot-checked findings 1, 2, 7, 8, 10, 11, 14 and 20 against the blobs at `3f884e9a`. The
other rows carry the skeptics' verified text.*

**Reviewed range:** `6707c4b10fd77ece45db1505a35ed74afba42087...3f884e9a8c72897312184bb37c3fd927954b7440`. **ROUND 1.**

## Verdict: CLEAN WITH FIXES

No confirmed finding is graded BLOCKER. The verdict is not CLEAN, because 15 findings stand, forming
11 items. One finding is HIGH.

The HIGH (H1, id 1) is the previous review's H1 class, still open on one route. Unit 29 made
`--for-diff` read the by-design block at the range's base. On the spec-audit route, though, the
build harness merges in a second checklist, the spec commit's own `--for-diff HEAD~1..HEAD`. That
checklist's base is the spec commit's parent, which lies inside the build. So an invariant the build
added in an earlier pass can still stand as by design on its own spec audit. The route needs the
owner's spec-audit opt-in, which this run did not declare, so it is narrow.

Three more of the known fixes are incomplete, each at MEDIUM or LOW:

- Unit 29 opened a rename hole of its own. A range that renames an invariant record keeps the base
  ruling in the by-design block (M2).
- Unit 29's base pin on the spec-audit route is never reached by the shipped caller, because the
  unattended skill does not pass `base` (M3).
- Unit 31 narrowed H3's wedge to a failed claim write, and handed the retry to the orchestrator. No
  unit and no park row carries that hand-off (M4).

Under the owner's mandate for this run, every discovery joins the build and nothing is backlogged.
Every item below is therefore owed a unit or a recorded park before `--close`. This synthesis mints
no ids; the orchestrator does.

## Review shape

Intensity full. Raw 20, confirmed 15, refuted 5, unverified 0 (0 uncertain). Precision 0.75.

| lens | returned | raw | confirmed | refuted | uncertain | unverified | precision |
|---|---|---|---|---|---|---|---|
| security | yes | 3 | 2 | 1 | 0 | 0 | 0.67 |
| correctness | yes | 3 | 1 | 2 | 0 | 0 | 0.33 |
| seams | yes | 7 | 5 | 2 | 0 | 0 | 0.71 |
| verification | yes | 3 | 3 | 0 | 0 | 0 | 1.00 |
| intent | yes | 4 | 4 | 0 | 0 | 0 | 1.00 |

- Adjudicated tally by raw confirmed finding: BLOCKER 0, HIGH 1 (id 1), MEDIUM 11 (ids 2, 7, 8, 9,
  10, 11, 14, 15, 17, 18, 19), LOW 3 (ids 6, 16, 20). That is 15 findings.
- Adjudicated tally by item: BLOCKER 0, HIGH 1 (H1), MEDIUM 7 (M1 to M7), LOW 3 (L1 to L3). That is
  11 items.
- Merges are mine, made at write time, and each joins findings of one binding grade only. Ids 2, 9
  and 17 are one defect (M2). Ids 8 and 19 are one defect (M4). Ids 11 and 14 are one defect on one
  line (M6). Id 18 (MEDIUM) is the same defect as id 1 (HIGH), so it stands apart as M1 beside H1.
  That split pair needs one fix.
- Every binding grade is kept. On id 18 I would grade HIGH, as id 1 is: the consequence is the same
  and so is the path. The skeptic graded it medium partly because none of today's three invariants
  reaches the route. The binding grade stands, and the pair's single fix makes the difference moot.
- Five refutals: two duplicates (ids 4 and 12 restate or predate a confirmed or base defect), two
  pre-existing behaviours the diff only narrowed (ids 3 and 13), and one design call on the
  checker's adopter scope (id 5).
- The correctness lens's precision of 0.33 is below the 0.5 floor. Its three findings were a
  duplicate, a design call and one LOW. A second round should tighten that lens's priming before
  adding agents.
- Intent: 8 spec documents supplied as `specs`, beside the range's commit messages.
- Checklist: 86 items, each assigned to exactly one of 5 lenses: security 18, correctness 17, seams
  17, verification 17, intent 17.
- By design: none supplied. There was no caller `byDesign` and no block.

## Run integrity

- Lenses: 5/5 returned, 0 DIED. Skeptic batches: 5/5 returned, 0 DIED.
- 0 contradictory verdicts demoted to unverified, 0 spurious verdicts discarded, 0 duplicates.
- Fixes on confirmed findings: 10 judged sound, 5 judged UNSOUND (ids 6, 10, 11, 14 and 18), 0 none
  proposed, 0 NOT JUDGED. Where a fix was judged unsound, only the skeptic's corrected fix appears
  below.
- Severity on confirmed findings: 0 UNGRADED by the skeptic (bound at the finder's grade), 0
  RE-GRADED by the skeptic.
- Unverified findings: 0 answered UNCERTAIN by a skeptic, 0 with no usable verdict.
- Lens notes: none supplied, so every lens ran on the kit's generic brief.
- Every count above that should be zero is zero, so the run is complete for those briefs.
- The empty by-design block is unit 29 working as built on the `--for-diff` route. The block is now
  read at the range's base, and the three invariants the previous round was handed are all records
  that range added. Unlike the previous round, no exemption reached this round's lenses.

## The known set, checked

| Known finding | Fixed by | This round |
|---|---|---|
| H1, by-design block written by the range | unit 29 | Fixed on `--for-diff`. Still open on the spec-audit route (H1, M1), not reached by the shipped caller (M3), and a new rename hole (M2). |
| H2, check 89 refuses the run's own record at `--close` | unit 30 | No finding. |
| H3, `--settle` never wrote the run claim | unit 31 | Fixed on the success path. A failed claim write still wedges the slug, and the hand-off has no disposition (M4). |
| M1, pathless commit in the spec commit stage | unit 32 | The commit is fixed. The new ban that gates its class is weak: no count, missed forms, and it reds on comments (M6). |
| M3, a claim push deletes push-main's verdict files | unit 32 | Narrowed, not closed (L1). |
| M7, a hand-off with no disposition | unit 32 | The class recurred in spec 31 (M4). |
| M2, M4, M5, M6, M8, M9, L1 to L4 | unit 32 | No finding. |

The "no finding" rows come from five lenses on generic briefs. No lens died, so the set is complete
for those briefs, but a zero here is not positive evidence that those fixes are complete.

## The rest of the range, judged

- `018b5675`, the check-wiring linked-worktree note: one finding (M5). For the shipped junction
  install, the note's guard compares the install with itself.
- Unit 33, the spec commit stage placing specs by id or by path: no finding.
- Unit 34, the suites' red arms, the two pool races and the shard 8 re-cut: three findings. The
  product half of the `run_bounded` race fix has no arm (M7). The re-cut seams lost the topology
  instrument, and the hoist rule is unguarded (L2). The roster row still states rev-1's mechanism
  (L3). The risk the brief named, a moved section that needs shell state its new region no longer
  provides, has no current instance: an `awk` over the file from the first `in_shard` line finds
  no region-defined helper. The whole suites have not run on the re-cut, so that is a static
  reading, not an observed green.
- `3f884e9a`, check-wiring's version constant: no finding.
- `0e65ae59`'s conflict resolutions (version markers bumped one past the higher side, suite floors
  merged as sums over the base, both lines' version notes kept): no finding. As above, this zero
  comes from generic briefs.

## BLOCKER

None.

## HIGH

### H1 — the spec-audit route still merges a by-design block read inside the build (id 1)

- **Where:** `tools/workflows/unattended-build.template.js:1379`, the call that merges the spec
  commit's checklist into the spec audit's checklist. The second input is `CHECKLIST`
  (`--for-diff HEAD~1..HEAD`, `:433`), run by the spec commit stage at `:1041`. The merge is
  `renderChecklistUnion` (`:506-524`).
- **Defect:** The first input is the run-base checklist (`--for-paths --base <auditBase>`), which
  unit 29 pinned at the run's base. The second is the spec commit's `--for-diff HEAD~1..HEAD`,
  whose base is the spec commit's parent. That parent lies after the run's base and holds every
  invariant earlier passes committed. `renderChecklistUnion` pushes every `- ` line under either
  input's by-design head into `design`, deduplicated only against `design`. So an invariant the
  first input lists as `NEW/CHANGED invariant <name>` can come back as a by-design entry from the
  second. The S9 comment at `:457-459` claims the opposite. Unit 29's spec section 4 kept this
  route on the premise that the spec commit's `--for-diff` is "a range already", but that range's
  base is `HEAD~1`, not the run's base.
- **Reproduced:** with the real `gotchas.py` in a scratch repo. Base B has no invariant. A pass
  commit adds `inv-build`, whose body backticks `memory/LIVE.md`. A spec commit writes
  `memory/LIVE.md` and `memory/builds/s/spec/a.md`. `--for-paths --base B` prints
  `- [ ] NEW/CHANGED invariant inv-build` and `# by design — 0`. The spec commit's `--for-diff
  HEAD~1..HEAD` prints `# by design — 1` with `inv-build`'s ruling. The union carries both.
- **Impact:** a build-added ruling reaches the spec audit's `byDesign` as intended behaviour, so its
  lenses and skeptics are told to refute findings the build's own ruling covers. That is H1's
  consequence. Reaching it needs the owner's `specAudit` opt-in plus a build-added invariant whose
  anchor selects a path the spec commit writes. `ANCHOR_RE` takes any backticked `.md` token, and
  `selectable`'s basename arm matches it, so the paths in reach are the specs, `LIVE.md`, the
  ledger and backlog views, and the build README.
- **Fix (judged SOUND by the skeptic):** When `auditBase` is set, have the spec commit stage run the
  checker pinned at the run's base: `gotchas.py --for-paths --base <auditBase> <the commit's
  --name-only paths>`, instead of `--for-diff HEAD~1..HEAD`. Alternatively, have
  `renderChecklistUnion` take by-design entries only from the base-pinned first input, and drop
  any entry whose invariant name either input lists as `NEW/CHANGED`.
- **Left-shift:** an arm in `unattended-build.test.sh` that feeds the real checker's two outputs
  over a build-added invariant and asserts that the invariant never reaches `byDesign`. Observe it
  RED on today's code before the fix lands.

## MEDIUM

### M1 — the same spec-audit route, at its lower binding grade (id 18)

- **Where:** `tools/workflows/unattended-build.template.js:1379`, with `CHECKLIST` at `:433` and
  `renderChecklistUnion` at `:506`.
- **Defect:** the same as H1, reached from the intent lens. A spec commit touches exactly the
  generated files a basename anchor selects: `1b53b54b` touched `README.md` and
  `memory/backlog/TOOL.md`, and `0bc5f0f8` touched `README.md`, `LIVE.md` and the ledger. The merged
  checklist also carries two `# invariants are read at` header lines naming different bases, and
  the first one promises "never by design".
- **Impact:** as H1. The skeptic graded it medium because none of the catalogue's three invariants
  reaches the route today. I would grade it HIGH with id 1, but the binding grade stands.
- **Fix (REJECTED by the skeptic; the corrected fix follows):** When `auditBase` is set, strip the
  spec commit checklist's whole by-design block before `renderChecklistUnion`: its head line, its
  entries and its `# invariants are read at` header. Also make the union drop any design entry
  whose name a `NEW/CHANGED invariant <name>` item in either input lists. If `--for-diff` gains a
  `--base` instead, derive `changed` there as every record that differs between that base and
  HEAD, as `--for-paths --base` does, and not from the range's name-only set.
- **Left-shift:** a GH arm in which the resolver output itemises `inv-x` and the spec-commit output
  lists `inv-x` by design. Assert the merged block omits it, and observe the arm red first. One fix
  and one arm close H1 and M1 together.

### M2 — a range that renames an invariant keeps the base ruling in the by-design block (ids 2, 9, 17)

- **Where:** `tools/memory-tree/gotchas.py:705`, in `cmd_for_diff`. The block filter is at `:625`.
- **Defect:** `changed` comes from `git diff --name-only <rng>`, which detects renames by default
  and names a rename by its destination only. The old path of a renamed invariant record is never
  in `changed`. The filter at `:625` excludes a base record only when its own path is in `changed`,
  so the base copy survives into the by-design block, while `derive_moved_invariants` lists the new
  name as `NEW/CHANGED`. That breaks the header's promise at `:32-33` that an invariant the subject
  "takes out" is never by design, and spec 29's S4 and AC1. AC1's take-out arm used a plain delete,
  so it never reached the rename. `--for-paths --base` compares by path text, so the two modes
  disagree on the same subject. Unit 29 introduced this: at `6707c4b1` the block came from the
  working tree, where the old record no longer existed.
- **Reproduced:** three times, independently, with the shipped checker and its own `_scratch`
  fixture. `git mv memory/gotchas/inv-one.md inv-two.md`, plus an edit to the ruling and to the
  anchored script, prints `# by design — 1` with inv-one's base ruling, and itemises only the new
  name.
- **Impact:** a subject can keep an exemption it retired by renaming the record rather than deleting
  it. Every lens and skeptic is told to refute findings that ruling covers. The exempting text is
  the base's ratified ruling, not text the range wrote, which keeps this below H1.
- **Fix (judged SOUND by the skeptic):** read the touched set with
  `git diff --no-renames --name-only -z <rng>` and split on NUL, as
  `memory/gotchas/porcelain-diff-names-a-rename-by-its-destination.md` already prescribes. The
  rename's source path then joins `changed` and is itemised from its base text.
- **Left-shift:** a `gotchas.py --selftest` arm beside the TAKES OUT arm. It `git mv`s an anchored
  invariant with a small edit and asserts the block holds 0 entries and both names are items.
  Observe it red on today's code. The class gotcha already exists, so also run its documented check
  over every `git diff --name-only` call this build added.

### M3 — the shipped caller never passes `base`, so unit 29's spec-audit pin is dead plumbing (id 7)

- **Where:** `tools/unattended/SKILL.template.md:716`, the harness-call paragraph (`:697-719`). The
  consumer is `tools/workflows/unattended-build.template.js:460` and `:1242`.
- **Defect:** unit 29 S9 forwards `--base` to the audit checker only when the caller passes a 7-40
  hex `base`. The unattended skill, the harness's only documented caller, makes `scratch` and
  `specAudit` mandatory and never mentions `base`. The harness header marks `repo`, `slug` and
  `scratch` REQUIRED and leaves `base` unmarked. Spec 29 line 118 labels the gap "hands-off
  external" and leaves it outside this build. The "external" owner is this repo's own unattended
  skill, which units 30, 31, 32 and 34 all edited, and RUN.md has no unit or park row for it.
- **Impact:** a caller that follows the skill gets `auditBase = ''` and runs `gotchas.py
  --for-paths` with no `--base`. The checker then reads invariants from the working tree, so an
  invariant this build added or edited stands in its own audit's by-design block, with only a
  workflow-log WARNING. That is the previous review's "still open" channel. A caller that copies
  its arguments from the harness header may pass `base`, so not every audit is hit. The discovery
  also left the build, against the owner's mandate.
- **Fix (judged SOUND by the skeptic):** require `base: <the run's pinned base fact>` beside
  `scratch` in the skill's harness-call paragraph, and re-render `.claude/skills/unattended/SKILL.md`.
  Alternatively, have `unattended-build` refuse a declared `specAudit` with no 7-40 hex `base`, as
  it refuses a missing `scratch`. The refusal is the stronger of the two, because it binds every
  caller.
- **Left-shift:** an arm that asserts the rendered skill's harness call names `base`. With the
  refusal option, add a harness arm that declares `specAudit` without `base` and expects the
  refusal.

### M4 — spec 31's settle claim-write retry was handed to the orchestrator and never disposed of (ids 8, 19)

- **Where:** `memory/builds/aGraftedHelix/spec/2026-10-05-spec-TOOL-aGraftedHelix-31.md:77-81`. The
  mechanism is `tools/unattended/unattended.sh:6047-6051` (the soft claim write in `run_settle`),
  `:5950` (the already-settled exit), `:1909` (`read_claims` maps `held` to verdict held at any age)
  and `:2023` (check 107).
- **Defect:** spec 31 says a settle whose claim status write fails leaves a hand-off's claim `held`,
  and that "this run's orchestrator adopts it as a unit or parks it". RUN.md's Parked section has
  one decision row, for unit 27's location-probe hand-off, and none for this. No unit exists past
  34. This is the class `memory/gotchas/orchestrator-hand-off-owed-a-disposition.md` records, which
  unit 32 wrote for M7. One sub-claim was overstated: that record's documented check is meant to
  run at the close and would catch this line. Its "1 at 9024901c" figure is a dated measurement,
  not a check that missed it.
- **Impact:** H3's wedge is still reachable on a narrow path. If the remote write fails during
  `--settle`, the claim stays `held`, which never ages to stale. A re-run of `--settle` takes the
  already-settled exit and writes nothing. The slug's next `--preflight` from any other session is
  refused at check 107 until someone deletes `refs/gov/runs/<slug>` by hand. Unit 32's S5 guard
  added a new way for that write to fail: `write_claim` returns rc 2 while `push-main-active`
  exists in the same git dir.
- **Fix (judged SOUND by the skeptic):** before the close, adopt a unit or park it. As a unit: on
  the already-settled exit with `RUN_CLAIMS` on, re-attempt the status write when the remote claim
  still reads `mine` and `held` or `live` under the record's keepalive. As a park: `--park
  aGraftedHelix --item settle-claim-retry --reason <question; options; the M2 veto>`. Either way,
  then run the class record's documented check over every spec of this build, so no other
  orchestrator hand-off is left without a disposition.
- **Left-shift:** with the unit, an arm that fails the first claim write under `--settle`, re-runs
  `--settle`, and asserts the claim reads the settled status. The hand-off class is ungateable by a
  line predicate today, so its documented check runs at the close as recorded.

### M5 — for the shipped junction install, the linked-worktree note's guard compares the install with itself (id 10)

- **Where:** `tools/check-wiring.sh:1239`, the `note` branch `018b5675` added, with the `pbad` loop
  at `:1229-1233`.
- **Defect:** the guard downgrades an install/worktree difference to `note` only when the install
  matches `$primary/$rel`. The shipped wiring, and the Fix line this arm prints, make the install a
  junction to exactly that directory. On node a, `~/.claude/skills/session-kickoff` links to
  `C:/projects/coding-governance/skills/session-kickoff`. So `pbad` is always empty for a correct
  install, and the "install drifts from the primary too" arm can only fire for a copy install,
  which is what the suite's `install_engine` fixture builds.
- **Impact:** in any linked worktree, every difference between the installed engine and the
  checkout's tracked engine becomes the note, which says "this worktree's branch edits the
  engine". Nothing checks that claim. With a lagging primary (node a's primary `main` sits at
  `c3ef6742`) or one on another branch, the note blames a branch that never touched the engine,
  `unwired` is not incremented, and `--check` goes green. The unattended preflight delegates to
  `--check`. At `6707c4b1` the same state was UNWIRED, so this diff introduced the regression. The
  header's WHAT THIS DOES NOT CHECK line admits the primary's currency is unchecked, but the note
  text asserts the opposite.
- **Fix (REJECTED by the skeptic; the corrected fix follows):** keep the install-vs-primary
  comparison unchanged, and add one condition to the note: every file in `$bad` must be changed by
  the branch itself, that is `! git diff --quiet "$(git merge-base HEAD <remote default tip>)" HEAD
  -- "$rel/$f"`. Otherwise fall through to UNWIRED, as at base.
- **Left-shift:** a suite arm with a link install over a primary whose engine lags a branch that
  never touched it, expecting UNWIRED. Observe it red on today's code.

### M6 — the pathless-commit ban reports no count, misses real forms and reds on comments (ids 11, 14)

- **Where:** `tools/workflows/check-workflow-syntax.js:39` (`COMMIT_LITERAL`), with the pass at
  `:94-99`. The pass came in with unit 32 (`525079d4e`) to gate the previous review's M1 class.
- **Defect:** `` /^[^'"`]*['"`]git commit\b/ `` is tested on every line, comments included, and
  matches only where `git commit` opens the line's first literal. A scratch fixture showed:
  - `` // a bare `git commit` takes the whole index `` is flagged.
  - `'git -C "$r" commit -q -m x'`, `'set -e; git commit -q -m y'` and `'git -c user.name=x commit
    -q -m z'` all pass.
  The header's DOES-NOT-CHECK list (`:24-25`) names none of those forms, and `git -C` is this repo's
  standard Windows spelling. The pass also keeps no count of the lines it graded. On the real tree
  it grades exactly one line, `unattended-build.js:1002`, because the template is excluded at
  `:55`. If that line were re-spelled past the regex, the pass would match nothing and the gate
  would still print "N workflow script(s) parsed clean". Spec 32 rev-3 added a liveness check to
  S4 for exactly this class, but not to S2.
- **Impact:** the ban certifies "no pathless git commit in a workflow script" while missing the
  forms a pathless commit is most likely to take here, so the M1 rider can come back unseen. The
  first comment that documents the rule reds the bar on its own remedy, though loudly. Today's
  result is right; the blind spot is latent.
- **Fix (REJECTED by the skeptic for both ids; the corrected fix follows):** skip lines whose
  trimmed text opens `//` or `*`. Match `\bgit(\s+-[cC]\s+\S+)*\s+commit\b` anywhere on a
  non-comment line. Print `graded N git commit line(s)` beside the green line. Refuse a zero count
  only when the discovered population contains the build harness render (`unattended-build.js`, or
  a file carrying its spec commit stage); otherwise print the zero as an announced count. Name the
  remaining unchecked forms in the header. The two corrected fixes differ on the zero count. Id
  11's says discovery mode itself must not exit 1 on a zero, and puts the floor in this repo's
  suite instead. Id 14's refuses a zero only when the harness render is present. Both agree an
  adopter tree with no commit line must not red, so the suite floor below satisfies both, and the
  conditional refusal is optional.
- **Left-shift:** three fixture arms, each observed red against the current predicate: a comment
  line passes, `git -C x commit` reds, `set -e; git commit` reds. Put the at-least-one floor in this
  repo's own suite: an arm that runs the checker in discovery mode over the real tree and asserts
  the count is at least 1. While the header is open, the checker-table row in
  `tools/workflows/README.md` (line 9) should also name the second pass; refutal 5 found it silent.

### M7 — the product half of unit 34's `run_bounded` race fix has no arm that can fail (id 15)

- **Where:** `tools/unattended/unattended.sh:263`, the `: >"$RB_UP"` exec marker and the bounded
  wait on `$_d/up` before `write_proc_record`.
- **Defect:** both extracted-`run_bounded` harnesses stub `write_proc_record() { :; }`
  (`unattended.test.sh:7402`, `:7529`, and `:11014`). No suite file mentions `RB_UP` or `_d/up`.
  The new `read_pl_exec_token` (`unattended.test.sh:13017`) guards only the suite's own ledger
  arms. Spec 34 AC6 says the product half has no observed red, and its measurement was a one-off
  probe, while S5 claims "Observed by AC6".
- **Impact:** deleting the wait loop, the marker write or the `RB_UP` prefix leaves every suite
  green. If that happened, the race reopens: under load the recorded start token is the forked
  shell's, so `derive_proc_state` reads the driver's own live bar as `reused`. `--hold`'s live-bar
  refusal and `--abort`'s KEPT ledger would then misread work in flight. The base measured the race
  at 0 of 130 because of incidental delay, so the effect is contained.
- **Fix (judged SOUND by the skeptic):** in the existing extracted-`run_bounded` harness (around
  `unattended.test.sh:7400`), add one arm whose stub is
  `write_proc_record() { [ -e "$_d/up" ] && echo up || echo early; } >>"$TMP/rb-up.log"`. Call
  `run_bounded bash -c 'exit 0'` and assert the log reads `up`. The stub runs the moment `&`
  returns, before the child has exec'd, so it reads `early` with the wait removed. Observe that
  red, then raise `FLOOR_SHARD_2` and `FLOOR_ASSERTIONS` by one.
- **Left-shift:** that arm is the gate.

## LOW

### L1 — the push-main-active guard checks, then acts, so the verdict-file collision is narrowed, not closed (id 6)

- **Where:** `tools/unattended/unattended.sh:2073` (`write_claim`). The other side is
  `.githooks/pre-push:334` (clears both verdict files before the skip-nondefault exit at `:909`)
  and `tools/push-main.sh:516`, `:617` (marker touch) and `:524`, `:623` (marker removal).
- **Defect:** `write_claim` tests `push-main-active`, then runs `mktree` and `commit-tree`, then
  pushes through `observe_remote`, which can take up to `REMOTE_BOUND`. Suppose a claim tests the
  marker just before push-main touches it, and its negotiation is slower than push-main's push plus
  the hook's vetting. Then its hook clears `pre-push-bar` after push-main's hook wrote it
  (`:1509`). `RUNLOG_GITDIR` and push-main's `git rev-parse --git-dir` both resolve to the
  per-worktree git dir, so the two collide in an in-place landing. The end-edge half of the claim
  is overstated: a claim that tests after the marker's removal needs seconds to reach its hook,
  and `write_lander_marker` reads within milliseconds. The comment "One writer per verdict file"
  still overclaims.
- **Impact:** if a `--beat` or holder renewal falls in the first seconds of an in-place landing,
  push-main prints that the hook recorded no vetted bar and does not write the lander marker.
  `--landed` then refuses a landing that did happen, and the run needs manual repair. The window is
  a few seconds per landing.
- **Fix (REJECTED by the skeptic; the corrected fix follows):** close the in-flight window with a
  lock rather than per-push paths. `write_claim` takes `mkdir <git-dir>/claim-push.lock` BEFORE it
  tests `push-main-active`, refuses and removes the lock if the marker exists, and holds the lock
  across the push. push-main touches the marker first, then waits, bounded by `REMOTE_BOUND` plus a
  margin, until `claim-push.lock` is absent before its `git push`. It removes the marker only after
  `write_lander_marker` and `derive_push_failure` have read the verdict files.
- **Left-shift:** an arm that holds `claim-push.lock` and asserts push-main waits for it, and one
  that touches the marker and asserts `write_claim` refuses without pushing. Correct the "One
  writer per verdict file" comment in the same change.

### L2 — the re-cut seams lost the topology instrument, and the hoist rule has no standing check (id 16)

- **Where:** `tools/unattended/check-unattended.test.sh:48` (the header), with the nine re-cut seams
  at `:4180-6115`.
- **Defect:** the nine seams open with `cd "$TMP"; anchor_restore` and call no `read_topo`. The
  header still says refs are carried by "read_topo at every boundary", which this diff made false.
  `anchor_restore` does not fully neutralise topology: `reset_tree` deletes only local heads, plus
  `ahead` and `trunk` on origin. Any other origin head an earlier section pushed survives an
  unsharded seam but is absent at shard start, and `read_topo` at the seam is the instrument that
  would show it. The hoist rule ("every region-defined helper is HOISTED") holds today, but spec 34
  AC8 observed it once, after 31 helpers had already drifted into region 8 against it.
- **Impact:** no current instance. Sections of one span now run in six different shards, so the
  next helper defined in a moved section and called from another is command-not-found in its
  shard. Its `hit` arms red, but its `miss` arms pass vacuously. The stale header misleads the next
  re-cut.
- **Fix (judged SOUND by the skeptic):** add `read_topo <seam-id>` after `anchor_restore` on each
  seam line; it is inert unless `CHECK_UNATTENDED_TOPO` is set. Correct the header to say the
  re-cut seams restore refs by `anchor_restore`.
- **Left-shift:** one prologue arm that runs `awk` over this file from the first `^if in_shard` line
  to the FLOOR line and fails, naming any `^[A-Za-z_][A-Za-z0-9_]*\(\) *\{` definition it finds. At
  the parent it would have named the 31.

### L3 — the roster row for unit 34 states rev-1's mechanism (id 20)

- **Where:** `memory/builds/aGraftedHelix/README.md:99`.
- **Defect:** the row reads "each red arm is fixed, proved already fixed, or proved inherited".
  Spec 34 rev-2 replaced filing with fixing, withdrew rev-1's six asks, and its H1 now reads "every
  red arm … is fixed". The row is new in this range.
- **Impact:** documentary only. The authored roster every reground reads contradicts the mandate
  ruling recorded in spec 34 section 8 F1.
- **Fix (judged SOUND by the skeptic):** reword the Mechanism cell to rev-2's outcome, for example
  "every red arm of the owed unattended suites is fixed, the two pool races are closed, and gate
  shard 8 is re-cut", in a records commit.
- **Left-shift:** ungateable by a line predicate. It joins the close's documented check: re-read
  each roster row against its spec's current revision title.

## Refuted

- **Id 3** (security, `gotchas.py:305`): a `git replace` of the base blob forges the by-design text.
  The lever reproduces, but the diff narrowed the exposure rather than opening it: at the base the
  block came from the working tree, editable with no forgery at all. The unpinned dereference is a
  pre-existing class across the whole review path, and the charter places the binding control on
  the remote.
- **Id 4** (correctness, `gotchas.py:705`): a duplicate of id 2, carried in M2.
- **Id 5** (correctness, `check-workflow-syntax.js:95`): the claim that the new pass breaks adopter
  scripts. Covering adopter scripts is the checker's declared design (TOOL-dRetiredFork-10). The
  predicates, run over every adopter repo on this node, found no workflow script at all. The
  documentation gap it surfaced is folded into M6's left-shift.
- **Id 12** (seams, `unattended.sh:6312`): `--preflight` can exit 0 after a failed `set_fact`. True,
  but pre-existing: the same body was inline in `verb_preflight` at the base with the same exit.
  Unit 32 moved it without changing that.
- **Id 13** (seams, `unattended.sh:261`): after the 5 s bound, `run_bounded` records the pre-exec
  token silently. That is the base behaviour on a smaller path, and spec 34 S5 states the fallback
  outright.

## Appendix — every finding

| id | lens | ref | severity | skepticSeverity | verdict | reason | fixVerdict |
|---|---|---|---|---|---|---|---|
| 1 | security | tools/workflows/unattended-build.template.js:1379 | high | high | confirmed | Reproduced with the real gotchas.py in a scratch repo. Base B has no invariant. A pass commit adds inv-build, whose body backticks `memory/LIVE.md`. A spec commit then writes memory/LIVE.md and memory/builds/s/spec/a.md. `--for-paths --base B <those paths>` prints `- [ ] NEW/CHANGED invariant inv-build` and `# by design — 0`. The spec commit's CHECKLIST, `--for-diff HEAD~1..HEAD` (unattended-build.template.js:433, run by the spec commit stage at :1041), reads the block at HEAD~1, which is the spec commit's parent and lies after the run base. It prints `# by design — 1` carrying inv-build's ruling. renderChecklistUnion (:506-524) pushes every `- ` line under either input's by-design head into `design` with no base check, and the call at :1379 merges that block into the spec audit's checklist. So on the spec-audit route a build-added ruling becomes an exemption, which is the H1 class. The S9 comment at :457-459 claims the opposite. Unit 29 spec §4 kept this route only on the premise 'ranges already', and the base of that range is HEAD~1, not the run's base. Reaching it needs specAudit declared, which is an owner opt-in, plus an invariant added earlier in the run whose derived anchors select a path the spec commit writes. ANCHOR_RE takes any backticked .md token, and the basename arm of `selectable` matches it, so the paths in reach are the specs, LIVE.md, the ledger and backlog views and the build README. The path is narrow and the consequence is the same as H1's, so high. | sound |
| 2 | security | tools/memory-tree/gotchas.py:705 | medium | medium | confirmed | Reproduced with the real checker. The range does `git mv` of inv-old.md to inv-new.md, edits the ruling and edits tools/some-gate.sh. `git diff --name-only HEAD~1..HEAD` lists only memory/gotchas/inv-new.md and tools/some-gate.sh, because rename detection is on by default. cmd_for_diff (gotchas.py:705) passes that list as both `paths` and `changed`. The block filter at :625 keeps inv-old, since it exists at the base, its path is not in `changed`, and its anchor selects some-gate.sh. The output prints the NEW/CHANGED item for inv-new and also `# by design — 1` with `- inv-old — ... It is the OLD ruling.` The header line beside it says 'adds, edits or takes out are listed as items, never by design'. This defect was introduced here: at the base, the block was read from the working tree, where inv-old no longer exists. The exempting text is the base's reviewed ruling, not text the range wrote, so the effect is contained to medium. | sound |
| 3 | security | tools/memory-tree/gotchas.py:305 | medium | - | refuted | The lever reproduces: a `git replace` of the base blob makes the block print forged text. But this diff neither introduced the defect nor made it reachable. At the base 6707c4b1, cmd_for_paths read the by-design block from the WORKING TREE, so anyone with local shell access could plant exemption text with an uncommitted file edit. That needed no forgery and was equally absent from the reviewed diff. The diff narrowed that exposure; it did not open it. The unpinned dereference is also a pre-existing class across the whole review path. `git diff --name-only` in this same function was unpinned at the base (base line 572). tier2-review.template.js and unattended-build.template.js pin nothing (0 hits for no-replace-objects/useReplaceRefs/GRAFT). So whoever can install a replace ref can rewrite the range's head commit and hide the change itself from the lenses, and pinning this one reader closes nothing. The charter states that a run with full shell access can defeat local checks and that the binding control is on the remote. Medium-graded, and not introduced by this diff. | sound |
| 4 | correctness | tools/memory-tree/gotchas.py:705 | medium | - | refuted | This duplicates finding 2. It has the same line (gotchas.py:705), the same root cause (`git diff --name-only` with default rename detection leaves the renamed record's old path out of `changed`, so the base copy survives the :625 filter into the by-design block), the same impact and the same `--no-renames` fix. The defect is real and I reproduced it under finding 2, which carries it. | sound |
| 5 | correctness | tools/workflows/check-workflow-syntax.js:95 | medium | - | refuted | Covering adopter scripts is the checker's declared design, not an accident. discovered() carries a NO PREFIX FILTER comment (check-workflow-syntax.js:47-51), and tools/workflows/README.md:96 says it covers the harnesses adopters keep under .claude/workflows/. The review-join ban was widened to that same adopter population by TOOL-dRetiredFork-10. The hazard the pass gates is real in any repo where a pathless commit runs over a pre-staged index, adopters running the unattended driver included, and gating the class rather than one repo's instances is the charter's rule (section 7). The breakage it predicts has not been observed. I ran the exact MARKER and COMMIT_LITERAL predicates over every adopter repo on this node (helixir, studio-os, swydee, vidyo, incms, nicocares, addi, qcu): none of them tracks a single workflows/*.js file, let alone a pathless commit line. The red, if one ever appears, names the file and line, says why, and is fixed by adding ` -- <paths>`, so its effect is contained. What does remain is a documentation gap. The README checker-table row (line 9) still reads 'every workflow script parses' and does not mention the second pass, and spec 32's migration line is silent on S2. That gap is cosmetic and is not the adopter-breaking defect the finding claims. | unsound |
| 6 | correctness | tools/unattended/unattended.sh:2073 | low | low | confirmed | The start edge is a real check-then-act race. write_claim (unattended.sh:2073) tests push-main-active, then runs mktree and commit-tree, then pushes through observe_remote, which can take up to REMOTE_BOUND. That claim push's pre-push hook clears both verdict files unconditionally at .githooks/pre-push:334, before the skip-nondefault exit at :909, and no exit comes earlier. Suppose a claim tests the marker just before push-main touches it (push-main.sh:516 and :617), and its negotiation is slower than push-main's push plus the hook's vetting. Then its hook runs after push-main's hook has written pre-push-bar (:1509) and erases it mid-bar. write_lander_marker then finds no vetted bar and refuses to write the marker for a push that landed. RUNLOG_GITDIR and push-main's `git rev-parse --git-dir` both resolve to the per-worktree git dir, so the two collide in an in-place landing. The end-edge half of the claim is overstated. A claim that tests the marker after the rm at :524 and :623 needs seconds to reach its hook, and write_lander_marker reads within milliseconds, so the end only matters for a claim already in flight from before the touch. The comment's 'One writer per verdict file' still overclaims. The window is narrow and the result is a recoverable refusal of --landed, so the grade is low. | unsound |
| 7 | seams | tools/unattended/SKILL.template.md:716 | medium | medium | confirmed | Closing review H1 named this channel explicitly as 'Still open after that fix': the --for-paths spec-audit channel in unattended-build, with rendering at the run's pinned BASE as the candidate cure. Unit 29 S9 forwards `--base` only when the caller passes a 7-40 hex `base` (unattended-build.template.js:460 and :1242). The unattended skill is the shipped caller instruction, and it makes `scratch` and `specAudit` mandatory but never mentions `base` (SKILL.template.md:697-719). The harness header lists base as unmarked, while repo, slug and scratch are marked REQUIRED. Spec 29 line 118 labels the gap `hands-off** external` and leaves it outside this build, yet the 'external' owner is this repo's own unattended skill, which units 30, 31, 32 and 34 of this build all edited. The README's mandate reads 'Discoveries are adopted into this build, never filed as asks', and RUN.md has no unit or parked row for this gap. 'Every real spec audit' is an overstatement, because a caller that copies args from the harness header may pass base. Even so, a caller that follows the skill gets a working-tree by-design block with only a log WARNING. That is H1's class left open on the audit route, so the fix of a known finding is incomplete. The impact is contained to the owner's opt-in audit and is announced, so the grade is medium. | sound |
| 8 | seams | memory/builds/aGraftedHelix/spec/2026-10-05-spec-TOOL-aGraftedHelix-31.md:77 | medium | medium | confirmed | Spec 31 lines 77-81 hand the retry path to 'this run's orchestrator', which 'adopts it as a unit or parks it'. RUN.md's Parked section holds only rescope, brief, dispatch and one location-probe decision row, and no unit exists past 34, so the hand-off has no disposition. That is exactly the class unit 32's own gotcha memory/gotchas/orchestrator-hand-off-owed-a-disposition.md describes. The mechanism checks out. run_settle writes the claim soft (unattended.sh:6047-6051) and only prints on failure. A re-run exits at 'already settled ... nothing was written' (:5950). read_claims maps `held` to verdict held at any age (:1909), so it never becomes stale, and a preflight that meets foreign-held falls to fail 107 (:2023). The take-over row that accepts foreign-held belongs to a HELD-record resume, not a settled LANDED record. The unit 32 S5 guard adds a new failure route, returning rc 2 while push-main-active exists. The original H3 wedge has been narrowed to a write-failure path but not closed, and the build's mandate disposition is missing. The effect is a slug wedged until someone deletes refs/gov/runs/<slug> by hand, on a narrow and announced path, so the grade is medium. | sound |
| 9 | seams | tools/memory-tree/gotchas.py:705 | medium | medium | confirmed | Reproduced in a scratch repo built by gotchas.py's own _scratch helper with git 2.54. A commit renamed memory/gotchas/inv-one.md to inv-uno.md, edited its Actually section and touched the anchored script. `git diff --name-only HEAD~1..HEAD` listed only inv-uno.md. cmd_for_diff (gotchas.py:705) then printed `NEW/CHANGED invariant inv-one` and also `# by design - 1` with the base's ruling `It is the ruling.`. That happens because the by-design filter at gotchas.py:625 excludes a base record only when its own path is in `changed`. This contradicts the header promise at lines 32-33 that an invariant the subject takes out is never by design. Unit 29 introduced the base-read block, so the defect is not pre-existing: at 6707c4b1 the block came from the working tree. The effect is contained. It needs a rename, and the leaked ruling is the base's ratified text rather than one the range wrote. | sound |
| 10 | seams | tools/check-wiring.sh:1239 | medium | medium | confirmed | On node a, ~/.claude/skills/session-kickoff is a link to C:/projects/coding-governance/skills/session-kickoff, which is the primary checkout. For that shipped wiring, the pbad loop at check-wiring.sh:1229-1233 compares the install with itself, so pbad is always empty. In any linked worktree, every install/worktree difference therefore becomes the `note`, which says 'this worktree's branch edits the engine'. Nothing checks that claim. With a primary that lags (node a's primary main sits at c3ef6742) or one on another branch, the note blames the branch, `unwired` is not incremented and `--check` goes green. At 6707c4b1 the same state was UNWIRED, so this diff introduced the regression. The header's 'WHAT THIS DOES NOT CHECK' line admits the primary's currency is unchecked, but the note text asserts the opposite, and the exit-code effect is real. The effect is contained to the kickoff engine's staleness. | unsound |
| 11 | seams | tools/workflows/check-workflow-syntax.js:39 | medium | medium | confirmed | The S2 pass, added at check-workflow-syntax.js:94-99 by unit 32, keeps no count of the lines COMMIT_LITERAL examined. On the real tree it examines exactly one line, unattended-build.js:1002, because the template is excluded at line 55. If that line were re-spelled past the regex, for example `git -c k=v commit` with no ` -- `, the pass would match nothing and the gate would still print 'N workflow script(s) parsed clean'. Nothing in the 'WHAT THE PASS DOES NOT CHECK' header covers that case. This breaks §7's liveness rule, and rev-3 of the same spec added liveness to S4 for exactly this class (vacuous-selector-empty-population) but not to S2. The effect is contained: there is no wrong result today, only a latent blind spot in the ban. | unsound |
| 12 | seams | tools/unattended/unattended.sh:6312 | low | - | refuted | The mechanics are real. The dispatcher runs `verb_preflight` and then `exit "$status"` (unattended.sh:12479, 12504), and set_fact can fail on `mktemp \|\| return 2` or on its final `mv` without calling fail, so status stays 0 and the driver exits 0. The defect is pre-existing, though. At 6707c4b1 the same body was inline in verb_preflight: `set_fact ... \|\| return 1` at base line 6328, `write_lease ... \|\| return 1` at 6342, and the same set_fact at 6556-6561. The same trigger exited 0 there too, leaving a live claim and a partial record. Unit 32 only moved that body into write_preflight_record and added the restore and abort messages. It did not introduce the exit-0 or make it reachable. | sound |
| 13 | seams | tools/unattended/unattended.sh:261 | low | - | refuted | Pre-existing and by design. At the base (6707c4b1:tools/unattended/unattended.sh:252) run_bounded called write_proc_record on $! with no wait at all, so on every call it recorded whatever token procfs held, which could be the pre-exec one. The diff only narrows that window. Spec 34 S5 and section 5 say the fallback outright: 'a wrapper that cannot write its marker costs at most the bound and records exactly what it records today, after the bound'. The silent pre-exec-token record after 5 s is the base behaviour, now limited to a smaller path. This diff did not introduce it. | sound |
| 14 | verification | tools/workflows/check-workflow-syntax.js:39 | medium | medium | confirmed | Reproduced against tools/workflows/check-workflow-syntax.js:39 with a scratchpad fixture. `// a bare `git commit` takes the whole index` is flagged (rc=1, one hit). `'git -C "$r" commit -q -m x'`, `'set -e; git commit -q -m y'` and `'git -c user.name=x commit -q -m z'` all pass. Comment lines are graded too. The header's DOES-NOT-CHECK list (lines 24-25) names a run-time-built command, agent prose, and a ` -- ` inside a message. It does not name the `git -C`/`git -c` or mid-literal forms, and `git -C` is this repo's standard Windows spelling. So a pathless commit of the M1 class can come back unseen. The pass came in with unit 32 (525079d4e), inside this range. The effect is contained: like M1 itself, it is a local, revertable rider commit. The comment false positive is loud, not silent. | unsound |
| 15 | verification | tools/unattended/unattended.sh:263 | medium | medium | confirmed | Verified. Both extracted-run_bounded harnesses stub `write_proc_record() { :; }` (unattended.test.sh:7402, :7529, plus :11014). No suite file mentions RB_UP or `_d/up`. read_pl_exec_token (unattended.test.sh:13017) guards only the arms' own ledger reads. Spec 34 AC6 states that the PRODUCT half has no observed red, and its product measurement was a one-off probe, not a standing arm. Deleting the wait loop, the marker write or the RB_UP prefix therefore leaves every suite green, while S5 claims 'Observed by AC6'. If it regressed, the race would reopen: derive_proc_state would read the driver's live bar as `reused`, so --hold's live-bar refusal could let a hold through with work in flight. The base measured that race at 0 of 130 thanks to incidental delay, so the effect is contained. | sound |
| 16 | verification | tools/unattended/check-unattended.test.sh:48 | low | low | confirmed | Verified. The nine re-cut seams (check-unattended.test.sh:4180-6115) open with `cd "$TMP"; anchor_restore` and call no read_topo. The header at :48 still says refs are carried by 'read_topo at every boundary', which this diff made false. anchor_restore does not fully neutralise topology: reset_tree deletes only local heads, plus `ahead`/`trunk` on origin. Any other origin head an earlier section pushed survives an unsharded seam but is absent at shard start, and read_topo at the seam is the instrument that would show it. The hoist rule holds today (an awk over the first `^if in_shard` to the end finds no column-0 definition), and the base had no standing check either. The interleaved re-cut is what makes a future cross-section helper a command-not-found in one shard. No current instance exists, so the impact is a stale header and an unguarded future edit. | sound |
| 17 | intent | tools/memory-tree/gotchas.py:705 | medium | medium | confirmed | Reproduced with the shipped tools/memory-tree/gotchas.py, using its own _scratch fixture. A commit git-mvs memory/gotchas/inv-one.md to inv-two.md, rewrites its Actually section and edits tools/some-gate.sh. `git diff --name-only HEAD~1..HEAD` prints only inv-two.md and the script, while `--no-renames` also prints inv-one.md. cmd_for_diff (line 705) then prints `# by design — 1 invariant(s)` with `- inv-one — ... It is the ruling.` and itemises only inv-two. So inv-one is never in `changed` (line 625), and derive_moved_invariants never itemises it. That breaks S4 ('every invariant a range moves is itemised') and AC1's take-out clause. The base-read logic was introduced by unit 29 in this range, so the finding is in scope. The effect is contained because the exempting text is the base's ratified ruling, not the range's. | sound |
| 18 | intent | tools/workflows/unattended-build.template.js:1379 | medium | medium | confirmed | The mechanism holds. CHECKLIST (line 433) is `--for-diff HEAD~1..HEAD`, so the spec commit's by-design block is read at HEAD~1, which holds every invariant the build's earlier passes committed. renderChecklistUnion (line 506) pushes each block's `- ` entries into `design`, deduped only against `design`. It never drops an entry whose invariant the first input lists as `NEW/CHANGED invariant <name>`, and the merged block keeps both `# invariants are read at` header lines. selectable's basename arm makes any invariant anchored on a README.md select the build README a spec commit touches. A build-added invariant can therefore stand as by design on its own spec audit, which contradicts the S9 comment at line 457 and spec 29's goal ('the channel the review left open is closed too'). The route existed at base, read from the working tree, but the context asks whether the H1 fix is complete, and this sibling route is left open. The new comment also claims a guarantee the code does not give. The path is narrow: it needs the owner's specAudit opt-in and a build-added invariant whose anchor selects a spec-commit path, and none of the catalogue's 3 invariants does today. Medium. | unsound |
| 19 | intent | memory/builds/aGraftedHelix/spec/2026-10-05-spec-TOOL-aGraftedHelix-31.md:77 | medium | medium | confirmed | Spec 31 line 77-81 hands the settle claim-write retry to 'this run's orchestrator adopts it as a unit or parks it'. RUN.md's Parked section has no row for it. It does have one for unit 27's location-probe hand-off. The README roster has no unit for it, and RUN.ABORTED carries only the H3 rescope. The wedge is real on the narrow path. run_settle's claim write (unattended.sh around 6046-6050) is soft and never fails the verb, so a failed remote write leaves a hand-off's claim `held`. A re-run takes the already-settled exit at 5947-5951, which writes nothing. Spec 31 introduced the hand-off line in this range, and the owner mandate requires a disposition. One sub-claim overstates: the class record's documented check is meant to run at the close and would catch this line. Its '1 at 9024901c' figure is a dated measurement, not a check that missed it. The missing disposition stands either way. | sound |
| 20 | intent | memory/builds/aGraftedHelix/README.md:99 | low | low | confirmed | README.md line 99's roster row for unit 34 reads 'each red arm is fixed, proved already fixed, or proved inherited'. That is rev-1's mechanism. Spec 34 is now rev-3, and its title and rev-2 changelog say every red arm is fixed and rev-1's six asks are withdrawn. The row is authored and new in this range, since the base README has no unit-34 row. The defect is documentary only. | sound |
