**Serves:** diff-review TOOL-dThriftyLanding-1 TOOL-dThriftyLanding-2 TOOL-dThriftyLanding-3 TOOL-dThriftyLanding-4 TOOL-dThriftyLanding-5 TOOL-dThriftyLanding-6

# Tier-2 closing diff review — dThriftyLanding, ROUND 1

*The closing review of build dThriftyLanding, over the cumulative diff at the integration boundary.
The build lets a push to the default branch whose every changed path is in a declared doc class run
only the bar legs that read a changed doc path. It has six units. The runner gains a `doc_reads`
manifest field and a `GATE_DOCS_BASE` mode (1). A full green earned in a linked worktree is shared
through the common git dir (2). The pre-push hook classifies a doc-only push from `GATE_DOC_PATHS`
read at the remote tip R (3). govkit carries `doc_reads` to adopters (4). gov declares its doc class
and thirteen legs' `doc_reads` (5). The carriers and versions follow (6). Node `d`, 2026-10-05.*

Reviewed range: `9c49bed108a9407d278b1ad701b86613f1046f0b...f765eb8e96d5243e1d15377bd9afc6789ce6bd80` · ROUND 1

## Verdict: CLEAN WITH FIXES

No blocker survived. Four highs were confirmed, and they reduce to two defects. First, both
history readers the docs mode relies on use git's default history simplification, so a `--no-ff`
merge whose side branch nets to zero hides its commits from them. Second, govkit's policy-key scan
cannot see `GATE_DOC_PATHS` in its documented multi-path spelling, so a check certifies the key absent
from shipped files while being blind to it. Both are on narrow paths, and both have a judged-sound
one-line fix. Twelve mediums and six lows were also confirmed. They are contained by the lag bound
(`GATE_FULL_MAX_LAG=10`), by remote CI running the full bar, or by being coverage gaps over code that
is correct today. Nothing here lands a wrong verdict on the common path, but the highs must be fixed
before this build is called done.

## Review shape

- Intensity full. Raw 25, confirmed 22, refuted 3, unverified 0 (0 uncertain). Precision 0.88.

| lens | returned | raw | confirmed | refuted | uncertain | unverified | precision |
|---|---|---|---|---|---|---|---|
| security | yes | 4 | 2 | 2 | 0 | 0 | 0.50 |
| correctness | yes | 5 | 5 | 0 | 0 | 0 | 1.00 |
| seams | yes | 6 | 6 | 0 | 0 | 0 | 1.00 |
| verification | yes | 6 | 5 | 1 | 0 | 0 | 0.83 |
| intent | yes | 4 | 4 | 0 | 0 | 0 | 1.00 |

- Adjudicated tally by raw confirmed finding: BLOCKER 0, HIGH 4 (ids 1, 5, 10, 22), MEDIUM 12
  (ids 2, 6, 7, 8, 9, 11, 12, 13, 16, 17, 23, 24), LOW 6 (ids 14, 15, 19, 20, 21, 25).
- Adjudicated tally by item: BLOCKER 0, HIGH 2 (H1, H2), MEDIUM 6 (M1 to M6), LOW 4 (L1 to L4).
- Items merge findings of one binding grade only. The history-simplification defect therefore
  appears twice: as H1 for its two high-graded findings and as M1 for its three medium-graded
  duplicates. One fix closes both items.
- Every binding grade was kept. No finding was re-graded in adjudication.
- Intent: 7 spec documents were supplied as `specs`, beside the range's commit messages.
- Checklist: 31 items, each assigned to exactly one of 5 lenses (security 7, correctness 6, seams 6,
  verification 6, intent 6).

## Run integrity

- Lenses 5/5 returned, 0 DIED. Skeptic batches 5/5 returned, 0 DIED.
- 0 contradictory verdicts demoted to unverified, 0 spurious verdicts discarded, 0 duplicates.
- Fixes on confirmed findings: 21 judged sound, 1 judged UNSOUND (finding 25, whose corrected fix is
  given below), 0 none proposed, 0 NOT JUDGED.
- Severity on confirmed findings: 0 UNGRADED by the skeptic, 0 RE-GRADED by the skeptic.
- Unverified findings: 0 answered UNCERTAIN by a skeptic, 0 with no usable verdict.
- Lens notes: none supplied, so every lens ran on the kit's generic brief. The zero-blocker result is
  evidence from generic-brief lenses only. No lens died, so the finding set is complete for those
  briefs.

## BLOCKER

None.

## HIGH

### H1 — a `--no-ff` merge whose side branch nets to zero hides its commits from both history readers (ids 1, 22)

- **Where:** `.githooks/pre-push:1221` (`classify_docs`, the `nl=$(git log ...)` line) and
  `tools/run-gates/run-gates.sh:305` (`check_doc_moved`, the `git log -1` line).
- **Defect:** Both calls are path-limited `git log` over `R..tip` without `--full-history`. Git's
  default history simplification follows a merge's TREESAME first parent and prunes the side branch.
  A side branch that adds a code file and removes it again (or edits and restores a doc path) is
  therefore never listed. Both comments claim the opposite: that a path changed and restored inside
  the range is still seen.
- **Impact:** Reproduced in a scratch repo. Side commit X adds `tools/evil.sh` and edits
  `memory/builds/RUN.md`, side commit Y reverts both, main takes a doc commit, then a `--no-ff` merge
  of the side. Both commands print nothing; with `--full-history` X, Y and `tools/evil.sh` appear.
  The hook classifies the push doc-only and waives predicate 5 (the merge second parent), although
  that parent carried code commits. The runner reports `memory/builds/` unmoved, so the
  commit-grading legs (pass-order history, brief-recorded) are docskipped over commits that land
  permanently. Every build here lands as a `--no-ff` merge, and spec TOOL-dThriftyLanding-3 AC3 is
  tested on linear history only. The path is narrow because the side branch must net to zero, which
  is why this is high rather than blocker.
- **Fix (judged SOUND by the skeptic for both findings):** Add `--full-history` to both calls:
  `git log --full-history --no-renames --format= --name-only R..tip -- . <excl>` in `classify_docs`,
  and `git log --full-history --format=%h -1 DOCS_BASE..HEAD -- <paths>` in `check_doc_moved`. Also
  consider `-m` (or `--diff-merges=separate`) so content introduced only by a merge resolution is
  listed.
- **Left-shift:** Add a `pre-push.test.sh` DOCS arm whose brief code touch sits on the side branch of
  a `--no-ff` merge with first parent R, expecting no docs-only clause. Add a `run-gates.test.sh` 3i2
  arm that edits and restores a `doc_reads` path on a merged side branch, expecting the leg to run.
  Observe both RED against the current code first. Class-wide: a gotcha entry that any path-limited
  `git log` used to answer "did anything in this range touch X" must carry `--full-history`.

### H2 — check 7h3 cannot see `GATE_DOC_PATHS` in its documented multi-path spelling (ids 5, 10)

- **Where:** `tools/govkit/govkit.py:2714-2716` (`policy_re`), and selftest M5 at
  `tools/govkit/selftest.py:5024`.
- **Defect:** `GATE_DOC_PATHS` joined `POLICY_KEYS`, but the assignment arm is `KEY=\S*` followed by
  optional whitespace, an optional comment and end of line. A quoted space-separated value, the only
  useful spelling of a multi-path doc class, never matches. Gov's own line at
  `.githooks/gate-env.sh:104` (`"memory/ README.md ..."`) does not match, nor does `'a/ b/'`. The
  single-element `"memory/"` does. The hook's `read_policy_key` accepts the multi-path line as an
  assignment, so the hook and the check disagree on what an assignment is. M5 tests the
  single-element form only, a guard green over a population of one.
- **Impact:** Check 7h3 certifies no kit ships a doc class while being blind to the spelling gov
  itself uses. If a kit-shipped file ever carried gov's multi-path `GATE_DOC_PATHS`, every adopter
  would inherit gov's doc class without choosing it, and their doc-only pushes would skip legs. That
  is exactly what adding the key to `POLICY_KEYS` exists to refuse. No kit ships one today, so the
  path is narrow; the consequence is a check certifying what it does not check, hence high.
- **Fix (judged SOUND by the skeptic for both findings):** Widen the assignment arm to
  `(KEY)=(?:"[^"]*"|'[^']*'|\S*)`, keeping the trailing `[ \t]*(?:#.*)?$`. That matches the
  multi-path forms and still rejects `GATE_DOC_PATHS="a b" bash x`. A git grep of tracked non-md
  files finds no other bare assignment the widening would newly red.
- **Left-shift:** Add M5 arms for the double-quoted and single-quoted multi-element forms, an arm in
  which a shipped fixture file carrying `GATE_DOC_PATHS="a/ b.md"` reds 7h3, and an arm that runs
  `policy_re` over gov's real `.githooks/gate-env.sh` `GATE_DOC_PATHS` line and expects a match.
  Observe each RED first.

## MEDIUM

### M1 — the history-simplification defect, medium-graded duplicates (ids 6, 7, 23)

- **Where:** `.githooks/pre-push:1221` (id 6) and `tools/run-gates/run-gates.sh:305` (ids 7, 23).
- **Defect:** The same mechanism as H1, reported by the correctness and intent lenses and graded
  medium by them and their skeptics. Id 6 reproduced it in the hook with `src/y.sh`, ids 7 and 23 in
  the runner with a doc path changed and restored on a merged side branch. Each breaks the spec it
  names: TOOL-dThriftyLanding-3 S2/AC3 and TOOL-dThriftyLanding-1 S2/AC4.
- **Impact:** Contained in these graders' reading: the net tree carries no code change, and the lag
  bound still forces a full run. A commit-grading leg prints a false "no path it reads moved" skip.
- **Fix (judged SOUND by the skeptic for all three):** The H1 fix: `--full-history` (and `-m`) on both
  calls. One change closes H1 and M1.
- **Left-shift:** The H1 arms.

### M2 — the docs mode grades against R while the scoped decision rests on the record sha (ids 2, 8)

- **Where:** `.githooks/pre-push:1399-1401`, with the runner's docs decision at
  `tools/run-gates/run-gates.sh:1826-1833`.
- **Defect:** On a doc-only push scoped from a full green (or an inherited green), the hook exports
  `GATE_BASE=rec_sha` but `GATE_DOCS_BASE=R`, and doc-only is classified over `R..tip` alone. A
  declaring leg is decided only by `check_doc_moved` since R and `continue`s before the guard and
  `changed()` test against BASE. Code that moved in `rec_sha..R`, up to the lag bound, no longer
  re-runs the declaring legs the pre-diff scoped bar ran. The runner comment's premise, that no code
  path moved, holds only for `R..tip`.
- **Impact:** If R carries a red on a declaring leg (reachable through a `--no-verify` landing, an
  inherited-red landing, or an impure leg), a doc-only push now docskips that leg and runs green.
  Under `INHERITED_RED=park` it then lands over the inherited red that lines ~1524-1531 would have
  refused, so the repository's declared policy is silently bypassed. No new defect lands, and remote
  CI still runs the full bar, which keeps this contained.
- **Fix (judged SOUND by the skeptic for both findings):** Engage the docs mode only when R itself is
  proven. Either classify doc-only over the scoping base (`rec_sha..tip` or `inh_sha..tip`, net diff
  and commits) and set `GATE_DOCS_BASE` to that same base, or export `GATE_DOCS_BASE` only when the
  adopted record's sha equals R or the policy at R is `land`. A runner-side alternative: docskip a
  declaring leg only when its guard also did not move since BASE.
- **Left-shift:** A `pre-push.test.sh` park arm: R red on a leg declaring `doc_reads []`, a full green
  stamped below R, then a doc-only push, expecting a refusal. Observe it RED first.

### M3 — govkit's drift predicate ignores `doc_reads`, so an adopter's edit is silently overwritten (ids 9, 13)

- **Where:** `tools/govkit/govkit.py:3850-3851` (the drift predicate), with the writer at ~3820 and
  the receipt field at ~3874.
- **Defect:** The diff writes `doc_reads` into the gov-owned manifest row and records it in the
  receipt, but the hand-edit drift predicate still compares only `argv` and `guard`. The receipt value
  is computed and never read.
- **Impact:** An adopter who removes or widens `doc_reads` on a gov-owned row, because in their repo
  the leg reads a doc path gov's list omits, has the edit silently replaced by gov's narrower list on
  the next update. The leg then docskips on their doc-only pushes. That is the "ownership of the NAME
  is not ownership of the ROW" class, reopened for a narrowing knob that `guard` already gets
  compared for. Narrower than the finder implied: `WIRE-INTO-PROJECT.md:768-771` invites adopters to
  set `doc_reads` on their own legs only. Bounded by the lag bound.
- **Fix (judged SOUND by the skeptic for both findings):** Add
  `or tgt.get("doc_reads") != prev.get("doc_reads")` to the predicate. A missing key compares as None
  on both sides, so pre-floor and pre-1.13 receipt rows compare equal and no wedge forms.
- **Left-shift:** A selftest arm that hand-edits `doc_reads` on an owned row in a target manifest and
  expects the drift failure rather than an overwrite.

### M4 — canary 1b grades `doc_reads` with a character prefix where the runner uses pathspecs (ids 11, 16, 24)

- **Where:** `tools/run-gates/run-gates.test.sh:433`.
- **Defect:** Canary 1b now loops over `("guard", "doc_reads")` with `t == g or t.startswith(g)`.
  The runner hands the same elements to `git diff`/`git log` as pathspecs, which match only at a path
  component boundary, and govkit's `derive_doc_reads` (`govkit.py:5317`) uses the boundary rule.
  Three guards answer "does this element name a tracked path" differently. The bare prefix existed
  for guards at base; extending it to `doc_reads` is new.
- **Impact:** A typo such as `memory/build` passes the canary because tracked `memory/builds/...`
  starts with it, yet `git diff -- memory/build` lists nothing. The leg then docskips on every doc-only
  push: the "skip that looks like a declaration" the new comment says this arm prevents. Spec
  TOOL-dThriftyLanding-1 AC6's red half (an untracked doc path fails) is never staged in a fixture.
  Latent: every current element passes the boundary rule. Bounded by the lag bound.
- **Fix (judged SOUND by the skeptic for all three):** Grade both keys with the component-boundary
  rule, `t == g.rstrip('/') or t.startswith(g.rstrip('/') + '/')`, or better ask git with a non-empty
  `git ls-files -- <g>` so canary and runner share one matcher. The boundary rule reds nothing in the
  current manifest, so it is safe for guards too.
- **Left-shift:** Fixture arms running the 1b predicate over a manifest whose `doc_reads` is a string
  prefix of a tracked file (`notes/a` against `notes/a.md`) and one naming `nowhere/`, both expected
  RED, each counted with `n=$((n+1))`.

### M5 — the `GATE_DOC_PATHS` element filter admits `.` and `./`, which exclude the whole tree (id 12)

- **Where:** `.githooks/pre-push:1211` (the refusing `case` arm in `classify_docs`).
- **Defect:** The filter refuses a leading `:` or `/`, globs and `..`, but `.` and `./` pass and
  become `:(exclude,literal).`, which excludes everything. Verified: that exclude leaves 0 paths of a
  96-file code diff.
- **Impact:** With such a value committed at R, every default-branch push classifies doc-only, waives
  predicate 5 and exports `GATE_DOCS_BASE`. Declaring legs are then decided by `doc_reads` alone, so
  for example lexicon naming predicates skip on a push editing `tools/lexicon/lexicon.py`. This
  contradicts `gate-env.sh`'s contract that a non-plain element means no doc class applies. Reaching
  it needs the value committed at R by the owner, and the lag bound limits it. Note the refuted
  security finding 3: its skeptic held that an over-wide owner declaration is spec 3's accepted risk.
  This finding survived on the narrower ground that `.` is a shape the filter's own stated guarantee
  should refuse, not a breadth the owner chose.
- **Fix (judged SOUND by the skeptic):** Add `.|./|./*` (or any element that normalizes to the repo
  root) to the refusing `case` arm, or canonicalize each element and refuse an empty result.
- **Left-shift:** A DOCS arm in `pre-push.test.sh` with `GATE_DOC_PATHS='.'` at R, expecting a code
  push NOT to be doc-only and the refusal reason in `DOCS_WHY`.

### M6 — the D2 check proving the manifest writer emits `doc_reads` is a source-text grep (id 17)

- **Where:** `tools/govkit/selftest.py:5104-5107`, against the writer at `tools/govkit/govkit.py:3816-3822`.
- **Defect:** The check is green whenever `derive_doc_reads(leg, ctx, have)` and
  `floor=DOC_READS_FLOOR_RUN_GATES` appear anywhere in `govkit.py`. No arm installs a descriptor leg
  declaring `doc_reads` into a target, though spec TOOL-dThriftyLanding-4 section 7 names exactly
  that arm.
- **Impact:** An inverted floor condition, a dropped `row["doc_reads"] = _dr`, a missing
  `doc_reads omitted` print (spec 4 AC2) or a wrong receipt field would all leave the selftest green.
  Emitting below the floor would red the adopter's canary; never emitting would make the adopter keep
  paying the full bar. The current code reads correctly, so nothing wrong ships today.
- **Fix (judged SOUND by the skeptic):** Add an install-level arm copying how `subject` emission is
  exercised: a scratch gov whose descriptor leg declares `doc_reads = ["{memory_root}/builds/"]`, a
  target tracking a file under `memory/builds/`. At run-gates 1.25 assert the row carries
  `["memory/builds/"]`; at 1.24 assert the key is absent; with an untracked element assert the key is
  absent and stdout contains `doc_reads omitted`. Drop the source grep or keep it as a secondary
  assertion.
- **Left-shift:** The install-level arm is the gate. Class-wide: a selftest check that only greps
  the subject's source text certifies spelling, not behaviour; treat one as a gap in review.

## LOW

### L1 — the shared full-green stamp is one last-writer-wins slot per clone (id 14)

- **Where:** `tools/run-gates/run-gates.sh:3424-3436`, and `tools/run-gates/README.md:160`.
- **Defect:** Any linked worktree's full green is copied to the single
  `<common-dir>/gate-full-green.shared` with `mv -f`, so the last worktree to earn one evicts the
  others. The comment's and spec 2's claim that `.shared` "can only add a usable record, never
  remove one" is inaccurate across linked worktrees, and the README does not mention the slot.
- **Impact:** Lost savings only: a landing whose shared record was evicted pays a full bar. Never a
  wrong verdict, because pre-push re-validates every candidate with predicates 2-8.
- **Fix (judged SOUND by the skeptic):** Key the shared file by stamped sha or branch (for example
  `gate-full-green.shared/<sha>`) and have pre-push evaluate the candidate whose sha is an ancestor of
  the pushed tip. At minimum, document the single-slot eviction in the README paragraph and correct
  the comment.
- **Left-shift:** If keyed, a `pre-push.test.sh` arm with two linked worktrees stamping in turn,
  asserting the first one's landing still scopes.

### L2 — the FULL path's re-read of the own record is dead plumbing with a misleading comment (id 15)

- **Where:** `.githooks/pre-push:1248`.
- **Defect:** After the candidate loop, `read_green_file "${green_candidates[0]}"` restores
  `rec_sha/rec_fp/rec_blob/rec_st`, but nothing on the FULL path reads them, and `lag` is not reset,
  so it holds the last candidate's value. The comment "a FULL decision reports the own record"
  describes nothing the code does.
- **Impact:** None today. A later edit printing `rec_sha` and `lag` on the FULL line would mix the
  own record's sha with another candidate's lag.
- **Fix (judged SOUND by the skeptic):** Drop the re-read, or reset `lag` alongside it and actually
  use the restored fields in the FULL message. Either way make the comment match the code.
- **Left-shift:** None proportionate; a §10 note that a restore-for-reporting must restore every
  field the report could read.

### L3 — three new paths have no arm that observes them (ids 19, 20, 21)

- **Where:** `.githooks/pre-push:1390` and `:1109` (id 19), `tools/run-gates/run-gates.sh:295`
  (id 20), `tools/run-gates/run-gates.test.sh:1159` (id 21).
- **Defect:** (19) The inherited-green branch's `GATE_DOCS_BASE` export and its docs-only clause have
  no arm, and neither does the linked-worktree candidate (the common dir's own `gate-full-green`),
  because test 30 runs in a plain clone where the git dir equals the common dir. (20) The runner's
  `unset GATE_DOCS_BASE` is unobserved: every 3i2 leg is `fx/a.sh`, which never reads its
  environment. (21) The 3i2 absence arm for `gate-full-green` has no positive control, and the
  fingerprint script it depends on is copied with `|| true`; the fixture does stamp today, so the arm
  is latent rather than vacuous.
- **Impact:** Regressions in any of these are silent. The costs are a lost saving (19), an OFF notice
  or a narrowed nested run (20), or an absence arm passing for the wrong reason (21).
- **Fix (judged SOUND by the skeptic for all three):** (19) A DOCS arm with a usable
  `gate-inherited-green` at R and no usable full green, asserting the scoped, docs-only,
  inherited-green line and `docs=$R` at the stub; and a test-30 variant from a `git worktree add`
  checkout that stamps only the common dir's own record and asserts it is the one adopted. (20) A 3i2
  leg that writes `${GATE_DOCS_BASE-unset}` to a file, run with a moved declared path, asserting
  `unset`. (21) After the `GATE_FULL=1` run in 3i2, assert with `n=$((n+1))` that
  `$D/.git/gate-full-green` now exists.
- **Left-shift:** The arms are the gates.

### L4 — the charter's doc-only sentence reverses the undeclared-leg rule, and a sentence was dropped unrecorded (id 25)

- **Where:** `AGENTS.md:541`, and the same wording at `.githooks/gate-env.sh:71` and `:102`.
- **Defect:** The line says a doc-only push "runs only legs whose `doc_reads` moved", which read
  literally skips undeclared legs, the reverse of the runner's rule that an undeclared leg always
  runs. It also says the shared green serves doc-only pushes, while spec 6 S4 says it serves every
  push. The same edit removed "Earlier runs are diff-scoped and are developer-choice." with no
  record; the commit's Decided lines name only the dropped "since landing stays a direct push"
  clause. `WIRE-INTO-PROJECT.md` states the rule correctly, so the docs now disagree.
- **Impact:** Documentation only, in a file loaded every session; no behaviour effect.
- **Fix (finder's proposal judged UNSOUND by the skeptic; this is the skeptic's corrected fix):**
  Reword byte-thriftily, for example: "A doc-only push, every path in `GATE_DOC_PATHS` at R, skips a
  declared leg whose `doc_reads` did not move; any worktree's full green serves every push." Make the
  same wording change in `.githooks/gate-env.sh`, and record the developer-choice sentence's removal
  in `memory/DECISIONS.md` instead of restoring it. The finder's longer reword plus restoring the
  sentence would likely red the charter's byte cap, since spec 6 records only 73 bytes of headroom
  and this diff spent most of it.
- **Left-shift:** None gateable for meaning; the charter byte-cap check already bounds the fix.

## Refuted findings (for the record)

- **3** (security, `.githooks/pre-push:1210`): `.` as an element is an over-wide owner declaration
  read at R, the accepted risk in spec 3. See M5 for the confirmed shape-guarantee reading.
- **4** (security, `tools/unattended/unattended.sh:8795`): only pre-push exports `GATE_DOCS_BASE`,
  the runner unsets it before legs, and the driver's treatment matches its existing pass-through of
  `GATE_BASE`/`GATE_LEGS`; the in-place arm sets `GATE_FULL=1`, which outranks the docs mode.
- **18** (verification, `.githooks/pre-push.test.sh:1407`): the missing predicate-5 forcing arm is a
  pre-existing gap, and AC4 does red if the waiver is reverted.

## Appendix — every finding

| id | lens | ref | severity | skepticSeverity | verdict | reason | fixVerdict |
|---|---|---|---|---|---|---|---|
| 1 | security | tools/run-gates/run-gates.sh:305 | high | high | confirmed | Reproduced in a scratch repo. The side branch has X, which adds tools/evil.sh and edits memory/builds/RUN.md, and Y, which reverts both. Main gets a doc commit and then a --no-ff merge of the side. classify_docs' `git log --no-renames --format= --name-only R..HEAD -- . ':(exclude,literal)memory/'` prints nothing, and check_doc_moved's `git log -1 R..HEAD -- memory/builds/` prints nothing. With --full-history, X and Y and tools/evil.sh appear. Default history simplification prunes the TREESAME merge's side parent. So the push classifies as doc-only, which waives predicate 5, and the commit-grading legs are docskipped over commits that land. Both code comments claim the opposite. The path is narrow because the side branch must net to zero, so the grade is high. | sound |
| 2 | security | .githooks/pre-push:1399 | medium | medium | confirmed | In pre-push's else-branch, GATE_BASE=rec_sha but GATE_DOCS_BASE=main_remote. In run-gates, a declaring leg under DOCS_BASE is decided only by check_doc_moved since R, and it `continue`s before the guard/changed() test against BASE. Code in rec_sha..R, which is up to the lag bound, therefore no longer re-runs the declaring legs that the pre-diff scoped bar ran. The runner comment's premise ('no code path moved') holds only for R..tip. The effect matters only when that code is already red at R: landed with --no-verify, or ungated. Remote CI still runs the full bar, so the effect is contained. | sound |
| 3 | security | .githooks/pre-push:1210 | medium | - | refuted | `.` is an over-wide declaration in the owner's own gate-env file read at R. It is not a pushed-tree or environment control. Spec 3 S1 lists the rejected element shapes (leading `:` or `/`, glob, `..`), and `.` is not among them. Spec 3's risks line names exactly this class as accepted: 'an over-wide declaration, such as tools/, would scope code pushes; it is the owner's file.' Declaring `.` is the extreme of that by-design risk, not a parser escape. | sound |
| 4 | security | tools/unattended/unattended.sh:8795 | low | - | refuted | pre-push is the only thing that exports GATE_DOCS_BASE, into its own bar, and run-gates unsets it before any leg runs. So a driver can inherit it only from a person who exported it by hand in the driver's shell. The driver already passes inherited narrowing knobs such as GATE_BASE and GATE_LEGS through unscrubbed at both run_bounded calls, so this is the pre-existing treatment, not a new hole. The in-place arm sets GATE_FULL=1, which outranks the docs mode. The binding control, the push boundary, scrubs the knob, as the finder concedes. Contained and low. | sound |
| 5 | correctness | tools/govkit/govkit.py:2714 | high | high | confirmed | Reproduced with the compiled policy_re. `GATE_DOC_PATHS="memory/ README.md AGENTS.md"` and `GATE_DOC_PATHS='a/ b/'` do not match, because the bare non-whitespace run after = stops at the first space and the tail then requires a comment or end of line. The single-element `"memory/"` matches. Selftest M5 tests only the single-element form. Gov's real line at .githooks/gate-env.sh:104 is multi-element and does not match; that file is counted only through its INHERITED_RED lines. A kit-shipped file carrying only a multi-path doc class would be certified absent. The path is narrow (no kit ships one today), and the consequence is a check that certifies what it does not check, so the grade is high. git grep finds no other bare GATE_DOC_PATHS assignment in tracked non-md files, so widening it would not red an innocent file. | sound |
| 6 | correctness | .githooks/pre-push:1221 | medium | medium | confirmed | Reproduced in a scratch repo. R is followed by a side branch that adds src/y.sh, removes it, and edits docs/b.md, then a doc edit on main, then a --no-ff merge. The hook's exact git log over R..HEAD with the exclude pathspec printed nothing. The same command with --full-history printed src/y.sh twice. The default history simplification follows the TREESAME first parent, so classify_docs (pre-push ~1221) reports doc-only. That contradicts the hook's own comment, which says a code file added and removed again inside the range is still code a leg should have seen. Predicate 5 is then waived and GATE_DOCS_BASE is exported. The impact is contained: the net tree carries no code change, and the lag bound still forces a full run. | sound |
| 7 | correctness | tools/run-gates/run-gates.sh:305 | medium | medium | confirmed | Same mechanism in check_doc_moved (run-gates.sh ~305). In the same scratch repo, git log --format=%h -1 R..HEAD -- src/ printed nothing, and with --full-history it printed the side commit. A doc_reads path changed and restored on a side branch merged --no-ff therefore reads as not moved. A commit-grading leg that declares memory/builds/ is skipped with a false 'no path it reads moved' line. That contradicts spec 1 S2 and the function's own comment. The effect is contained to commit-grading legs on merge pushes. | sound |
| 8 | correctness | .githooks/pre-push:1399 | medium | medium | confirmed | In pre-push ~1399-1412, the scoped branch exports GATE_BASE=rec_sha (or inh_sha) but GATE_DOCS_BASE=main_remote. The doc-only classification is taken over R..tip only. A leg declaring doc_reads [] is therefore skipped on any doc-only push, regardless of whether R itself was ever proven by a bar. Before the change, an unguarded leg ran on that push. gate-env.sh documents INHERITED_RED=park\|land as 'whether a push may land over a red its default branch already carries'. Lines ~1524-1531 refuse a red unless the policy is land. With R red on a [] leg (reachable via a --no-verify landing or an impure leg), a doc-only push under park now runs green and lands over the inherited red, so the declared policy is bypassed. No new defect lands, which keeps the impact contained. The spec's security model does not cover an unproven R, and no BY DESIGN item covers it. | sound |
| 9 | correctness | tools/govkit/govkit.py:3850 | medium | medium | confirmed | In govkit.py ~3850, the drift predicate compares only tgt argv/guard against prev, while this diff now writes doc_reads into the gov-owned row (~3820) and records it in the receipt (~3874). Suppose an adopter removes or widens doc_reads on a gov-owned row because, in their repo, the leg reads a doc gov's list omits. The predicate stays false, and existing[by_name[nm]] = row silently restores gov's narrower list. That is exactly the hand-edit class the 'ownership of the NAME is not ownership of the ROW' failure exists to report, and doc_reads is a narrowing knob like guard, which IS compared. This diff made it reachable, since the base had no doc_reads field (subject's identical omission is pre-existing). The proposed .get comparison treats an absent key as None on both sides, so pre-floor and pre-1.13 receipts compare equal. The withheld path keeps the prior receipt rows, so no wedge forms. | sound |
| 10 | seams | tools/govkit/govkit.py:2716 | high | high | confirmed | Verified with python against govkit.py ~2713's regex. 'GATE_DOC_PATHS="memory/ README.md AGENTS.md"' does not match, because the non-space-star value term cannot cross the space and the tail requires EOL or a comment. 'GATE_DOC_PATHS="memory/"' and 'INHERITED_RED=land' do match. gov's own gate-env.sh:104 uses the multi-path quoted form, and pre-push's read_policy_key accepts it. Check 7h3 therefore certifies GATE_DOC_PATHS absent from shipped files while being blind to its documented spelling. A multi-path doc class written into a kit-shipped file would pass and narrow every adopter's bar. The defect is a check certifying what it does not check, on the narrow path where someone writes the key into a shipped file. The proposed widening matches the multi-path form and still rejects 'GATE_DOC_PATHS="a b" bash x'. A git grep of tracked non-memory, non-.md files finds no other bare assignment line that the widening would newly red: only gate-env.sh lines 99, 100 and 104, which are not shipped. | sound |
| 11 | seams | tools/run-gates/run-gates.test.sh:433 | medium | medium | confirmed | run-gates.test.sh canary 1b now loops over ('guard','doc_reads') with `t == g or t.startswith(g)`. The guard half is unchanged from base (base line 418), but extending it to doc_reads is new in this diff. The runner's check_doc_moved (run-gates.sh:301-306) hands the elements to `git diff`/`git log` as pathspecs, which match only at a component boundary, so a prefix-typo element such as `memory/build` passes the canary while never matching in the runner. The leg then docskips on every doc-only push. Today no declared element is mis-shaped, because every gate-legs.json guard/doc_reads value is a dir ending in `/` or a file. The defect is therefore latent for the next declaration, and the lag bound limits its consequence. | sound |
| 12 | seams | .githooks/pre-push:1211 | medium | medium | confirmed | classify_docs (.githooks/pre-push ~1209-1215) refuses `:`, `/`, globs and `..` shapes, but `.` and `./` pass and become `:(exclude,literal).`. Reproduced here: that exclude leaves 0 of 84 changed paths, so every push classifies doc-only, waives predicate 5 and exports GATE_DOCS_BASE. Declaring legs are then decided by doc_reads alone (run-gates.sh:1831 `continue`s before the guard). That contradicts gate-env.sh's documented contract that each element is a file or a dir ending in `/`, with non-plain elements meaning no doc class. Reaching it needs such a value committed at R, and a broad plain value like `tools/` could narrow the bar the same way. That keeps the defect contained to the filter's stated shape guarantee, with the lag bound limiting it. | sound |
| 13 | seams | tools/govkit/govkit.py:3850 | medium | medium | confirmed | govkit.py ~3850 compares only argv and guard between the target row (tgt) and the receipt row (prev) before replacing the row with `existing[by_name[nm]] = row`. This diff adds doc_reads to both the emitted row and the receipt (line ~3874), yet the receipt value is never read. A target-side edit to a kit leg's doc_reads is therefore overwritten silently on the next update, which is the 'wrong on the way IN' class the adjacent DEPL-cMendedVintage-22 comment exists to prevent. WIRE-INTO-PROJECT.md:768-771 invites adopters to set doc_reads, though only on their own legs, so this path is narrower than the finder implies. The effect is contained: one leg may docskip, bounded by the lag bound. | sound |
| 14 | seams | tools/run-gates/run-gates.sh:3435 | low | low | confirmed | run-gates.sh:3424-3436 copies any linked worktree's full green to the single `<common-dir>/gate-full-green.shared` with `mv -f`, so whichever linked worktree earns a full green last evicts the others. That makes the comment's and spec-2's claim that a separate .shared file 'can only add a usable record, never remove one' inaccurate across linked worktrees. The consequence is a lost scoped decision, which means paying a FULL bar. It never produces a wrong verdict, because pre-push re-validates every candidate with predicates 2-8. The README paragraph at tools/run-gates/README.md:160 does not mention the single slot. | sound |
| 15 | seams | .githooks/pre-push:1248 | low | low | confirmed | After the candidate loop, `read_green_file "${green_candidates[0]}"` restores rec_* on a FULL force. On the FULL path no later code reads rec_sha/rec_fp/rec_blob/rec_st: the FULL echo prints only $force/$inh_why, and the only rec_sha reads after it are the scoped branch at ~1400-1401, which runs only when force is empty. `lag` is not reset alongside it, so it holds the last candidate's value. On the inherited branch it is overwritten by check_green_record only on the else arm, and the FULL message never prints it. The comment 'a FULL decision reports the own record' therefore describes nothing the code does. This is dead plumbing that misleads a future edit, with no current behavioural effect. | sound |
| 16 | verification | tools/run-gates/run-gates.test.sh:433 | medium | medium | confirmed | run-gates.test.sh:430-433 now loops over (guard, doc_reads) and grades with `t == g or t.startswith(g)`, a character prefix. The runner's check_doc_moved (run-gates.sh:301-307) passes the same elements to `git diff --quiet BASE -- $@` and `git log -- $@` as pathspecs, which match only at a directory boundary. So `notes/a` certifies as tracked because `notes/a.md` exists, yet it never matches a change to notes/a.md, and the leg docskips. govkit derive_doc_reads (govkit.py:5317) already uses the boundary rule, so the canary and the deployer disagree. Extending this loose rule to guards was pre-existing, but grading doc_reads with it is new in this diff, and a doc_reads miss means a skip, not an extra run. The arm's red half is never staged in a fixture: 1b runs only over the real manifest, and 3i2 has no untracked-doc_reads arm, so spec-1 AC6's 'untracked doc path fails' is unobserved. Every gov doc_reads value passes the boundary rule today, so nothing is shipped wrong. The effect is contained by the lag bound. | sound |
| 17 | verification | tools/govkit/selftest.py:5105 | medium | medium | confirmed | selftest.py:5104-5107 only greps govkit.py's source for the two strings. The D2 checks at 5089-5103 call derive_doc_reads directly, and D1 (5065-5081) tests check_target_reads_subject at the floor. Nothing exercises the writer block at govkit.py:3816-3822. An inverted floor condition, a dropped `row["doc_reads"] = _dr`, or a missing 'doc_reads omitted' print would all leave the selftest green. Spec-4 section 7 still names the new arm as 'a descriptor leg declaring doc_reads, installed by the base writer'. The rev-2 note moved AC1-AC3 to the helper, but the install-level arm was never added. The current emission code reads correctly, so this is a verification gap with no wrong output shipped. | sound |
| 18 | verification | .githooks/pre-push.test.sh:1407 | medium | - | refuted | The missing control is a PRE-EXISTING gap. At base, predicate 5's forcing half had no arm either: the finder says so itself, and base pre-push.test.sh has no 'second parent' arm. The non-doc branch of `[ -z "$DOCS_ONLY" ] && ...` (pre-push:1162) is exactly the base behaviour, unchanged, so deleting predicate 5 outright passing every arm was already true at base. The other claim, that AC4 cannot tell 'waived' from 'never fires', does not hold for this fixture. AC4 stamps at R, then commits on a new side branch and merges it. The second parent is a fresh commit that is not an ancestor of R, so by construction the line-1162 predicate fires unless DOCS_ONLY is set. Reverting the waiver therefore reds AC4. | sound |
| 19 | verification | .githooks/pre-push:1390 | low | low | confirmed | Both paths are new in this diff and neither has an arm. The inherited-green branch's export (pre-push:1390, plus the docs clause at 1388 on that line) has none: the DOCS arms (pre-push.test.sh:1382-1453) all stamp a full green via set_docs_stamp, and the IR inherited-green arms (1040-1072) never build a doc-only push. The common dir's own gate-full-green candidate is added only when the git dir differs from the common dir (pre-push:1109). Test 30 runs in a plain clone, per its own comment at 477, so that candidate and the ordering claim are never exercised. A regression here costs a lost saving, or it touches an ordering whose additivity is asserted only in prose. | sound |
| 20 | verification | tools/run-gates/run-gates.sh:295 | low | low | confirmed | run-gates.sh:295 `unset GATE_DOCS_BASE` was added by this diff. Every 3i2 leg (run-gates.test.sh:1129-1136) is fx/a.sh copied from instant.sh, which never reads its environment. A grep finds no arm that observes the variable inside a leg. Deleting or moving the unset reds nothing. Today's impact is mostly an OFF notice inside nested runs whose scratch repos cannot resolve the sha, so it is low. | sound |
| 21 | verification | tools/run-gates/run-gates.test.sh:1159 | low | low | confirmed | run-gates.test.sh 3i2: the gate-full-green absence arm (`[ -f "$D/.git/gate-full-green" ] && fail`) has no positive control. The GATE_FULL=1 run right after it asserts only the 4/4 GREEN line, never that the stamp appeared. gate-fingerprint.sh is copied with `\|\| true`. The arm is latent rather than vacuous today, since the finder showed the fixture stamps. That is the could-not-fail shape the file warns about, with no effect on behaviour now. | sound |
| 22 | intent | .githooks/pre-push:1221 | high | high | confirmed | Reproduced in a scratch repo. Setup: R; a side branch adds src/x.sh, removes it and edits notes/b.md; then `merge --no-ff side`. `git log --no-renames --format= --name-only R..HEAD -- . ':(exclude)notes'`, the shape of .githooks/pre-push:1221, prints nothing. The merge is TREESAME to its first parent R on the non-doc pathspec, so default simplification drops the side branch. With `--full-history` it prints src/x.sh twice. So a --no-ff landing whose branch transiently touched code is classified doc-only: predicate 5 is waived and GATE_DOCS_BASE is exported. That contradicts spec 3's stated reason for reading commits. The path is narrow because the net tree is unchanged, so only commit-grading legs could differ. It is still a wrong classification on the merge shape every build lands in. | sound |
| 23 | intent | tools/run-gates/run-gates.sh:305 | medium | medium | confirmed | check_doc_moved (run-gates.sh ~305) uses `git log --format=%h -1 "$DOCS_BASE..HEAD" -- paths` with default simplification. In the same scratch repo, notes/c.md added and removed on the merged side branch prints nothing, while `--full-history` prints the commit. A declaring commit-grading leg therefore records a docskip on exactly the touched-and-restored case the runner's own comment says the second half exists for. The 3i2 arm tests only linear history. By-design item (d) covers a range that moves nothing under memory/builds/, not one whose side branch did. The lag bound limits the damage. | sound |
| 24 | intent | tools/run-gates/run-gates.test.sh:433 | medium | medium | confirmed | Canary arm 1b now grades doc_reads with `t == g or t.startswith(g)` (the bare prefix existed at base for guards only, so this diff made it reach doc_reads). govkit derive_doc_reads (govkit.py:5317) uses the component boundary `t == v.rstrip('/') or t.startswith(v.rstrip('/') + '/')`, which matches git pathspec semantics. A typo like `memory/build` passes the canary but matches nothing in git diff/log, so the leg silently docskips. Latent: no current element is misspelled. Running the boundary rule over the current manifest reds nothing, so the fix is safe to apply to guards too. | sound |
| 25 | intent | AGENTS.md:541 | low | low | confirmed | The AGENTS.md diff replaces 'Earlier runs are diff-scoped and are developer-choice.' with 'A doc-only push ... runs only legs whose `doc_reads` moved, and any worktree's full green serves it'. Read literally, that skips undeclared legs, which reverses the runner's rule that an undeclared leg runs. The gate-env.sh notes at ~71 and ~102 repeat the wording. The shared green also serves every push, not only doc-only ones. The commit's Decided lines record only the dropped 'since landing stays a direct push' clause, not the dropped developer-choice sentence. Documentation only, with no behaviour effect. The proposed fix is unsound as written. Spec 6 records that the charter had only 73 bytes of cap headroom, and this diff spent most of it. The longer reword plus restoring the ~54-byte sentence would likely red the charter's byte cap (check 6). | unsound |
