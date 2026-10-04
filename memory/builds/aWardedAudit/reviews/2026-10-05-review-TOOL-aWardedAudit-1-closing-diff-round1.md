**Serves:** diff-review TOOL-aWardedAudit-1 TOOL-aWardedAudit-2 TOOL-aWardedAudit-3

# aWardedAudit — Tier-2 closing diff review, round 1

*Node `a`, 2026-10-05. An adversarial pass over the whole diff of the three-unit build: five primed
finder lenses, a skeptic stage prompted to refute each finding, and one synthesis. The build makes
the pre-code spec audit opt-in for the owner only. Check 89 in `check_authorization` refuses a
`spec-audit:` key in a README the run wrote. `SPEC_AUDIT_DEFAULT` is read at the default-branch side
of BASE. Rule 0 in `agent-cap.js` admits a live run only on its pinned RUN.md fact, and it now also
judges harness calls that carry `specAudit`. The carriers were updated to match.*

**Range reviewed: `856ad8a6856225bfe0d610d9a530b8fe852192b8...8cfe5678315d98b2f9206a0d14de594337f060de`**
(55 files, +387/-88).

**Round: 1.**

## Verdict: CLEAN WITH FIXES

There are no blockers. One HIGH finding remains: a run can still write the opt-in onto the default
branch through its own landing, and the protocol claims a parity with `may:` that has no bar leg
behind it. The MEDIUM items are one placement gap in the hook (three lenses reached it independently),
one reader disagreement over RUN.md, and two coverage gaps where an arm cannot fail. Everything else
is stale prose that names BASE where the code now reads the merge-base, or a fail-closed edge case.
Each item is a small, local repair. None of them reverses a unit's design.

## Review shape

Intensity full. Raw 23, confirmed 18, refuted 5, unverified 0 (0 uncertain), precision 0.78.

Adjudicated tally, by raw confirmed finding: 0 blocker, 1 high, 7 medium, 10 low (18).
By item: 0 blocker, 1 high, 4 medium, 7 low (12 items). Three groups of co-reported findings were
merged into one item each: ids 2, 9 and 19; ids 6, 12 and 23; and ids 11 and 20. Ids 14 and 18 were
also merged. Each merged group shares one binding grade.

Run integrity: 5 of 5 lenses returned and 0 died. 5 of 5 skeptic batches returned and 0 died.
0 contradictory verdicts were demoted to unverified, 0 spurious verdicts were discarded, and there
were 0 duplicates. Of the fixes on confirmed findings, 15 were judged sound, 3 were judged UNSOUND,
0 had no fix proposed and 0 were NOT JUDGED. On severity, 0 confirmed findings were left UNGRADED by
the skeptic and 1 was RE-GRADED (id 20, medium to low). For unverified findings, 0 were answered
UNCERTAIN and 0 had no usable verdict. No lens notes were supplied, so every lens ran on the kit's
generic brief. Five spec documents were supplied as `specs`, beside the range's commit messages. The
checklist had 28 items, each assigned to exactly one lens: security 6, correctness 6, seams 6,
verification 5, intent 5. Every counter that has to be zero for this run to count as complete is zero.

Security model handed to the reviewers: these guards stop drift by a cooperative but mistaken agent,
not a forging one. An agent with full shell access can edit RUN.md or local main. The control that
actually binds lives on the remote (protocol §9). The driver's `--close` re-derives the opt-in at BASE
and refuses a recorded fact that disagrees with it (check 53).

## HIGH

### H1 — a run can land the opt-in itself, and the protocol claims a parity guard that does not exist (id 1)

`tools/unattended/PROTOCOL.template.md:117`. The new text says the spec-audit opt-in is the owner's
"on the same reading" as `may:`. For `may:`, the bar has a leg behind that claim:
`check-unattended.sh` `scan_grant_writes` (check 19) reds any run-range commit that writes a `may:`
line into a build README. `spec-audit:` gets no such leg, and neither does a run commit that adds
`SPEC_AUDIT_DEFAULT` to `.unattended.conf`. Suppose a run lands either line on main with no owner
turn. The next run's BASE (first anchor) or merge-base (second anchor) then carries it,
`check_authorization` pins it, and check 53 agrees at `--close`. That is a self-opt-in delayed by one
run. Nothing on the bar reports it, and the parity sentence tells the next author that a guard exists.

- **Fix (the skeptic judged it sound):** mirror `scan_grant_writes` for spec-audit. Add a
  check-unattended leg that reds any run-range commit writing a `spec-audit:` front-matter line into
  any build README, or a `SPEC_AUDIT_DEFAULT` assignment into `.unattended.conf`. Otherwise, state the
  gap in protocol §9 next to property 4 and drop the "same reading" parity claim.
- **Left-shift gate:** the new scan_grant_writes sibling is the gate. Observe it RED on a staged run
  commit that adds each of the two lines. Also add a parity arm: every "on the same reading as
  `may:`" claim in the protocol must name a check-unattended scan that covers its key.

## MEDIUM

### M1 — a harness call is placed by `reviewDir` alone, so the live run's pinned fact can be routed around (ids 2, 9, 19)

`tools/hooks/agent-cap.js:1898`. Three lenses (security, seams, intent) reached this independently.
In harness mode (args carry `specAudit`), the hook locates the README and RUN.md from `reviewDir`
whenever one is passed. It never checks that path against `a.slug` or against the units' spec paths,
which are what `unattended-build.js` actually audits (lines 766-814). The `subjects` stray check only
fires when `a.subjects` is an array, and harness calls normally omit it. So a call such as
`{slug: X, specAudit: D, reviewDir: 'memory/builds/Y/reviews'}`, where X is a live build, skips X's
RUN.md rule (S1). It is admitted on Y's README key, or on the worktree conf default, which the run
can edit. The harness then audits X's specs with no owner opt-in, and the records land in Y's folder.
A stale `reviewDir` copied from an earlier call is enough; no forgery is needed. The damage is
contained, because `--close`/check 53 re-derives X at BASE and nothing wrong lands.

- **Fix:** the finders' fixes were REJECTED by the skeptic for ids 2 and 9, because units carry
  `specPath`, not `spec`. A check over `units[].spec` would read `undefined` for every unit and deny
  every legitimate harness call. The skeptic judged the fix for id 19 sound, and it agrees with the
  corrected fixes for 2 and 9. Write this one: when harness mode is true, deny when `a.slug` is not a
  single path segment, and deny when `reviewDir` is present and its build segment
  (`dir[dir.length-1]`) differs from `a.slug`. Then deny any unit whose `specPath` is a non-empty
  string and whose `extractBuildSlug(u.specPath)` differs from `a.slug`. Skip units with no
  `specPath`, because unspecced units are legitimate.
- **Left-shift gate:** add arms for both mismatches beside a live RUN.md that pins no fact: a foreign
  `reviewDir`, and a foreign `specPath`. Observe each one ADMIT on the current hook first, then deny
  after the fix.

### M2 — the hook reads RUN.md differently from the driver (id 3)

`tools/hooks/agent-cap.js:1945`. The hook takes the first column-1 `phase:` and `spec-audit:` lines
anywhere in the file, and treats every phase except LANDED and ABORTED as live. The driver's
`fact()` (`unattended.sh:1117`) reads only inside `## Run facts`, a scope adopted after a whole-file
reader took a stray `phase: LANDED` (TOOL-aRepatriatedFork-6 L2). `read_derived_phase` also derives
LANDED from a LANDING record whose landing commit is on the advertised tip. Twelve tracked RUN.md
files keep `phase: LANDING` after landing, including aBatchedMinors, aCollapsedScan and
aHalvedInstall, and none of those three pins a spec-audit fact. So an attended, owner-opted spec
audit on any of those builds is denied as a live unattended run. That is the wrong refusal AC4 exists
to prevent. It fails closed, so the effect is contained.

- **Fix (the skeptic judged it sound):** scope both regexes to the `## Run facts` section, as
  `fact()` does. Treat LANDING as terminal for this rule, or document it as live and give the owner a
  route.
- **Left-shift gate:** add an arm with a LANDING record and an arm with a stray `phase:` line above
  the heading. Better still, a parity arm that runs the hook's reader and `fact()` over the same
  fixture set.

### M3 — no arm covers a harness call made without a live run (id 15)

`tools/hooks/agent-cap.js:1893`. Every S4 arm in `agent-cap.test.sh` (lines 1026-1041) either writes
a BUILDING RUN.md first or is denied before RUN.md is read. The attended fall-through for a harness
call (the README key, the S2 mode deny, the conf default) never runs. That behaviour is new: the base
hook admitted every harness call. A mutation that returns null for a harness call when RUN.md is
absent leaves the suite green.

- **Fix (the skeptic judged it sound):** add two arms after `rm -f "$SARUN"` in the S4 block. First,
  `$SAH` beside a slug README with no key and no conf, expecting a deny that names `spec-audit:`.
  Second, `$SAH` beside an `authorized-by: prompt` README carrying `spec-audit: 2026-10-05`,
  expecting a deny that names `authorized-by: prompt;;admits nothing`.
- **Left-shift gate:** the two arms, each observed RED by staging the null-return mutation.

### M4 — the "not gradable" clear has no arm that can fail (id 16)

`tools/unattended/unattended.sh:2452`. Spec 1 S1 says clearing `AUTH_SPEC_AUDIT_DERIVED` is
"Observed by AC1 and AC2". Both arms (`unattended.test.sh:3677-3693`) run only `--preflight`. No arm
runs `--close` over a README that check 89 refuses and reads the specs-audited line. Deleting the
assignment leaves every arm green. `--close` would then grade specs-audited against the refused date
and print an owed-audit, no-evidence verdict. `authorization-reachable` already refuses that close,
so the only damage is a misleading DoD line.

- **Fix (the skeptic judged it sound):** add an arm that runs `--close` over a prompt README carrying
  `spec-audit:` and expects both `specs-audited — not gradable` and check 89. Commit the README after
  a successful preflight, or seed RUN.md. Otherwise, change S1's "Observed by" to say the clear is
  not observed.
- **Left-shift gate:** the arm, observed RED with the assignment deleted. Class-level: an
  "Observed by" claim in a spec should name an arm that exercises the code path, which a review
  checklist entry can check.

## LOW

### L1 — driver messages still name BASE where the conf is now read at the merge-base (ids 6, 12, 23)

`tools/unattended/unattended.sh:2381`, `:2387`, `:8265`, `:8269`, and the comment at about `:2343`.
On the second anchor the conf is read at `_cb = merge-base(ASHA, BASE)`. Fail 54, fail 55, fail 53
and the specs-audited not-owed sentence still say "the project conf at the pinned BASE" or "at BASE".
An operator who chases one of them inspects a blob that was never read. If the run committed a
default on its own branch, the not-owed line claims BASE declares none when it does; the driver just
ignored it. The verdicts themselves come from the right blob. `_cb` is a local (line 2284), so the
grader cannot name it today.

- **Fix:** the skeptic judged the fixes for ids 6 and 23 sound and REJECTED id 12's fix as incomplete.
  Write the corrected one: change the fail 54/55 messages (and fail 53 and the 8269 sentence) to name
  the commit actually read, for example "the project conf at the default-branch side of BASE
  ($_cb)". Store `_cb` in a global so the grader's sentence can name it too. In the same commit,
  update the three assertions that match the old wording verbatim: `tools/unattended/unattended.test.sh:7672`,
  `:7712` and `:7759`.
- **Left-shift gate:** one second-anchor arm that asserts the refusal names the merge-base sha, not
  BASE.

### L2 — the hooks README "limits" paragraph and the rule-0 header contradict the new text (ids 11, 20)

`tools/hooks/README.md:155-162` and `tools/hooks/agent-cap.js:1837`. The diff amended the paragraph to
say a live run is decided by RUN.md's pinned fact and the worktree is not read. It kept the sentence
saying the hook reads the worktree README and conf while the driver reads both at BASE, so the two
can disagree for exactly one uncommitted edit. Both halves are now wrong. "The programmatic route is
the driver's to refuse" also understates what the hook now judges. Id 20 was re-graded medium to low
by the skeptic; it is prose with no behaviour effect, which is low under the rubric.

- **Fix (the skeptic judged it sound for both):** restate the limits. Attended sessions read the
  worktree README and conf. A live run reads the pinned RUN.md fact. The harness's nested `workflow()`
  is still unseen, but the call that carries `specAudit` is judged. The driver reads the README at BASE
  and the conf at the default-branch side of BASE. Make the same edit to the header comment at
  `agent-cap.js:1837`.
- **Left-shift gate:** none fits for prose; add it to the documented check that an edited paragraph
  is re-read whole.

### L3 — Skill and protocol still say "both keys are read at BASE" (id 21)

`tools/unattended/SKILL.template.md:247` and `tools/unattended/PROTOCOL.template.md:356`. Each carrier
now gives two answers: the old "at BASE" line and the new "default-branch side" text.

- **Fix (the skeptic judged it sound):** in the Skill, write "the README key at BASE, and the project
  default at the default-branch side of BASE". Make the same change in the specs-audited row at
  PROTOCOL:356, then re-render the dogfood copies.
- **Left-shift gate:** a grep arm over the rendered carriers for "read at BASE" beside
  `SPEC_AUDIT_DEFAULT`.

### L4 — BUILD-METHOD M4 names neither owner route and keeps the at-BASE read (id 22)

`tools/memory-tree/BUILD-METHOD.template.md:115`. Spec 3 S1 says M4 will say the opt-in comes from a
slug README on the default branch or a `SPEC_AUDIT_DEFAULT` there. The built M4 names neither route
and still says ".unattended.conf at BASE". AC1 greps only for "Recommended, never", so it passes.

- **Fix (the skeptic judged it sound):** in M4 "When", change the conf clause to "at the
  default-branch side of BASE". Add "counted only from a slug README landed on the default branch, or
  SPEC_AUDIT_DEFAULT there" to the OWNER's sentence, within the method's byte budget.
- **Left-shift gate:** extend AC1's grep to the two owner-route phrases.

### L5 — the terminal-phase set has an unchecked second copy in the hook (id 13)

`tools/hooks/agent-cap.js:1946` hard-codes LANDED/ABORTED, a copy of the driver's `PHASES_TERMINAL`
(`unattended.sh:651`). `drift-audit/selftest.py:2871` parity-checks the other copies, but not this one.
Behaviour is correct today.

- **Fix (the skeptic judged it sound):** add the pair to the playbook parity check, or derive the set
  from the driver source. At minimum, add an arm that greps `PHASES_TERMINAL` and compares it with the
  hook's set.
- **Left-shift gate:** that parity arm.

### L6 — the hook and the harness default `reviewDir` differently (ids 14, 18)

`tools/hooks/agent-cap.js:1899`. The harness uses `a.reviewDir || default`
(`unattended-build.js:231`). The hook applies the default only for undefined or null. With
`reviewDir: ""`, the hook denies as "not directly under builds/<slug>/" a call the harness would have
placed. It fails closed, with a misleading message.

- **Fix (the skeptic judged it sound for both):** use the harness's own falsy test,
  `if (harness && !rdir)`.
- **Left-shift gate:** one arm passing `reviewDir: ""` with the pinned fact, expecting allow.

### L7 — two S2 conditions have no arm that can fail (id 17)

`tools/hooks/agent-cap.js:1960`. No arm puts a conf default beside a prompt-mode README with no key,
and no arm uses phase ABORTED. Dropping `v !== null` from the S2 condition, or dropping
`phase !== 'ABORTED'`, leaves the suite green.

- **Fix (the skeptic judged it sound):** add an arm with no RUN.md, an `authorized-by: prompt` README
  with no key, and SACONF declaring `SPEC_AUDIT_DEFAULT="2026-09-21"`, expecting allow. Add one with a
  `phase: ABORTED` RUN.md beside a slug README key, also expecting allow.
- **Left-shift gate:** the two arms, each observed RED under its mutation.

## Refuted (not carried)

Ids 4, 5, 7, 8 and 10 were refuted. Id 4 needs a forged decoy README, which is out of scope. Id 5 is
the designed attended behaviour. Ids 7 and 10 are by design: spec 1 S2 says an uncomputable
merge-base reads as no default, and the path needs grafted history to reach. Id 8 needs a hand-edited
RUN.md. The skeptic notes that scoping the regexes is still sound hygiene, and M2 does that anyway.

## Appendix — every finding

| id | lens | ref | severity | skepticSeverity | verdict | reason | fixVerdict |
|---|---|---|---|---|---|---|---|
| 1 | security | tools/unattended/PROTOCOL.template.md:117 | high | high | confirmed | PROTOCOL.template.md:117 is new in this diff and claims the spec-audit opt-in is the owner's 'on the same reading' as may:. The run mandate reads 'only the OWNER' as D12-j does for may:. For may:, check-unattended.sh scan_grant_writes (line 1598, check 19 at 2326-2343) reds any run-range commit that writes a may: line into a build README. grep finds no spec-audit or SPEC_AUDIT_DEFAULT counterpart in check-unattended.sh. So a run can land a slug README carrying spec-audit:, or a SPEC_AUDIT_DEFAULT in .unattended.conf, on main with no owner turn. The next run's first-anchor BASE, or its second-anchor merge-base, then carries that line, check_authorization pins it, and check 53 agrees at --close. This is a delayed self-opt-in that the ruling forbids, nothing on the bar reports it, and the parity claim tells the next author a guard exists that does not. | sound |
| 2 | security | tools/hooks/agent-cap.js:1898 | medium | medium | confirmed | agent-cap.js:1893-1905: in harness mode, reviewDir wins over slug when present, and nothing compares the two. The subjects stray check (1911) fires only when Array.isArray(a.subjects). Usually the harness resolves subjects internally from units[].specPath (unattended-build.js:766-814) and audits with reviewDir passed through (851). Take a live run on X with no pinned fact whose worktree conf carries a self-written default. A call with reviewDir memory/builds/X/reviews is denied by S1. The same call with reviewDir memory/builds/Y/reviews reads Y's README and Y's RUN.md. Y has no RUN.md, so the call falls to the worktree conf default and is admitted. It audits X's specs into Y's folder. This is a workaround of a deny, not forgery of the files that are out of scope. The diff introduced the harness judgement, so the gap is in scope. The proposed fix is unsound as written because units carry `specPath`, not `spec`. A literal `units[].spec` check gives extractBuildSlug(undefined) = null for every unit, so it would deny every legitimate harness call. Unspecced units also carry no path and have to be skipped. | unsound |
| 3 | security | tools/hooks/agent-cap.js:1945 | medium | medium | confirmed | agent-cap.js:1945 matches the first column-1 phase: anywhere in RUN.md and treats every phase except LANDED and ABORTED as live. The driver's fact() (unattended.sh:1117) reads only inside '## Run facts', and read_derived_phase derives LANDED from a LANDING record whose landing commit is on the advertised tip. Landed builds keep 'phase: LANDING' committed: 12 tracked RUN.md files carry it, including aBatchedMinors, aCollapsedScan and aHalvedInstall, and none of those three pins a spec-audit fact. So an attended, owner-opted spec audit on any such build is denied as a 'live unattended run', which is a wrong refusal of a legitimate opt-in. The fail-closed direction keeps the effect contained. The stray-line-above-the-heading direction is speculative, but scoping the read is still the correct reader. | sound |
| 4 | correctness | tools/hooks/agent-cap.js:1939 | medium | - | refuted | The bypass needs a decoy README at x/builds/tX/README.md. Without it, readFileSync on the README placed under the moved reviewDir throws ENOENT, and the outer catch denies (fail closed). Writing a fabricated build README at a fabricated path to get past S1 is forgery, not the drift of a cooperative-but-mistaken agent. The stated security model excludes forgery, and a run with a shell can equally edit RUN.md, which is out of scope. The slug-only containment of subjects is also unchanged from base (closing review F2). | sound |
| 5 | correctness | tools/hooks/agent-cap.js:1960 | low | - | refuted | readFrontMatterKey (scratch-guard.js:617-625) returns null for a bare key or a key with a trailing comment, so S2 does not fire. The call then falls to the worktree conf default, and S2's own scope says that default still admits in an attended session (spec 2 S2). That is the same verdict the hook gives a README with no key at all, so the admission matches the designed attended behaviour. The bare-key disagreement with the driver is a limit stated at base in the rule-0 header comment. No live-run path is affected, because the RUN.md branch decides first. | sound |
| 6 | correctness | tools/unattended/unattended.sh:8269 | low | low | confirmed | unattended.sh:2371-2373 now reads the conf at _cb, which is merge-base(ASHA, base) on the run-branch anchor. The diff left the fail 55 text (2381), the fail 54 text (2387), the fail 53 text (8265) and the specs-audited not-owed sentence (8269) saying 'the project conf at the pinned BASE' or 'at BASE'. On the second anchor those name a blob that was never read. Only the operator-facing text is wrong: the verdicts are computed from the right blob. _cb is a local (line 2284), so the grader cannot name it today. | sound |
| 7 | correctness | tools/unattended/unattended.sh:2373 | low | - | refuted | By design. Spec TOOL-aWardedAudit-1 S2 says in so many words 'A merge-base that cannot be computed reads as no default', and the code comment at 2369-2370 records the same choice: an opt-in that cannot be placed on the owner's side is not the owner's. The path is also effectively unreachable. Check 30 (1652) guarantees ASHA is local, resolve_base already found merge-base(ASHA, HEAD), and base is a tip this run pushed off that history. For merge-base(ASHA, base) to fail, base would need history unrelated to the default branch, which means a forged or grafted history, and that is out of scope. | sound |
| 8 | seams | tools/hooks/agent-cap.js:1945 | medium | - | refuted | The hook's whole-file /^phase:/m and /^spec-audit:/m (agent-cap.js, RUN.md block) differ from fact()'s section scope (unattended.sh:1117) only when a key-shaped column-1 line sits outside '## Run facts'. The driver never writes one there. scaffold_runmd (2614-2627) writes prose that has no column-1 key lines, then an empty generated region; the DoD at 7769 even requires that region to stay empty. set_fact writes only under the heading (5545-5557), and parked rows open with a timestamp. The only way to get a decoy phase: LANDED or spec-audit: line into the file is to hand-edit RUN.md, which the by-design list puts out of scope as forgery. The proposed fix of section-scoping the regexes is still harmless hygiene. | sound |
| 9 | seams | tools/hooks/agent-cap.js:1898 | medium | medium | confirmed | Reachable as described. The harness takes reviewDir and slug independently (unattended-build.js:228,231) and never checks that they agree. It resolves audit subjects from units[].specPath (766-790) and hands that reviewDir to the nested tier2-review spec-audit (840-853), which no hook sees. In checkSpecAuditDeclared, a harness call with an explicit reviewDir places the README and RUN.md from reviewDir alone, and the stray-subject check reads only a.subjects, which harness calls normally omit. So a call with slug set to the live build X and reviewDir memory/builds/Y/reviews skips X's live RUN.md rule (S1) and is admitted on Y's README key or on the worktree conf default, which the run can edit. That spends an audit on X with no owner opt-in, the exact act this build exists to stop. The harm is contained: --close/check 53 re-derives X at BASE, so nothing wrong lands. A direct tier2-review call cannot do this, because its subjects are checked against reviewDir. The fix as written is unsound, because units carry the field specPath (renderRoster, unattended-build.js:376), not spec. A check over a.units[].spec reads undefined, and extractBuildSlug(undefined) is null, so every harness call would be denied. Unspecced units legitimately carry no path at all. | unsound |
| 10 | seams | tools/unattended/unattended.sh:2373 | medium | - | refuted | Duplicate of finding 7, and covered by the same design statement. Spec TOOL-aWardedAudit-1 S2 says 'A merge-base that cannot be computed reads as no default', and the comment at unattended.sh:2369-2370 records that intent. The path is not reachable without unrelated or grafted history. ASHA is guaranteed local by check 30, merge-base(ASHA, HEAD) already succeeded in resolve_base, and base is a run-pushed tip on that same history. Failing open toward 'no audit' is also in line with the owner's ruling that only an owner-placed opt-in counts. | sound |
| 11 | seams | tools/hooks/README.md:161 | low | low | confirmed | tools/hooks/README.md:155-157. The diff amended this paragraph to say that in a live run only RUN.md's pinned fact admits and 'the worktree is not read'. It kept the base sentence saying the hook reads the WORKTREE README and conf while the driver reads both at BASE, so the two can disagree for exactly one uncommitted edit. Both halves are now wrong. A live run does not read the worktree, and on the run-branch anchor the driver reads the conf at merge-base(ASHA, BASE) (unattended.sh, _cb). The diff introduced the contradiction inside a paragraph it edited. It is prose only. | sound |
| 12 | seams | tools/unattended/unattended.sh:2387 | low | low | confirmed | unattended.sh: the diff added `_cb=$(GIT merge-base "$ASHA" "$base")` on ANCHOR_KIND=run-branch and reads `$_cb:.unattended.conf`. The fail 55 and fail 54 messages directly below still say 'the project conf at the pinned BASE'. SKILL.template.md:247 still says 'both keys are read at BASE'; the line the diff added after it only partly corrects this. The diff made the existing text stale. The effect is limited to an operator's diagnosis. | unsound |
| 13 | seams | tools/hooks/agent-cap.js:1946 | low | low | confirmed | agent-cap.js hard-codes `phase !== 'LANDED' && phase !== 'ABORTED'`, a new copy of the driver's PHASES_TERMINAL="LANDED ABORTED" (unattended.sh:651). The repo already parity-checks the other copies of this set: drift-audit/selftest.py:2871 compares _RUN_PHASES_TERMINAL against the driver. Nothing checks the hook's copy. Today's behaviour is correct, so this is a latent drift risk introduced by the diff with no current misbehaviour. | sound |
| 14 | seams | tools/hooks/agent-cap.js:1899 | low | low | confirmed | unattended-build.js:231 uses `a.reviewDir \|\| 'memory/builds/' + slug + '/reviews'`, so an empty string gets the default. The hook substitutes the default only when rdir is undefined or null. With `reviewDir: ""`, parts=[''], dir=[] and the call is denied as unplaceable. The diff introduced this mismatch in the new harness branch. It fails closed, it needs an unusual argument to reach, and its effect is a refused call, not an admitted one. | sound |
| 15 | verification | tools/hooks/agent-cap.js:1893 | medium | medium | confirmed | agent-cap.test.sh:1026-1041: every S4 arm that passes `specAudit` either writes a BUILDING RUN.md first or is denied before RUN.md is read (the unplaceable-slug arm). The 'no specAudit' arm is not judged at all. A harness call in an attended session, which falls through to the README key, the S2 mode deny and the conf default, has no coverage. This is behaviour the diff changed: the base hook admitted every harness call. A mutation that returns null for a harness call when RUN.md is absent would leave the suite green. The proposed arms run after `rm -f "$SARUN"`, and SACONF has already been removed, so their expected denials match the existing AC3 and U7 arms. | sound |
| 16 | verification | tools/unattended/unattended.sh:2452 | medium | medium | confirmed | Spec 1 S1 (line 27-29) claims that leaving specs-audited not gradable is 'Observed by AC1 and AC2'. The AC1 and AC2 arms (unattended.test.sh:3677-3693) run only --preflight. They hit the check-89 message and that RUN.md is absent. Nothing runs --close or reads the specs-audited DoD line. The assignment AUTH_SPEC_AUDIT_DERIVED="" at unattended.sh:2452 can be deleted without any arm going red. The effect is contained: authorization-reachable already refuses the close, so the only result is a misleading DoD line. | sound |
| 17 | verification | tools/hooks/agent-cap.js:1960 | low | low | confirmed | agent-cap.test.sh has no arm for phase ABORTED. Its only authorized-by arm (line 1001) is a prompt README carrying a key. The conf-default arms (lines 950-993) use READMEs with no authorized-by line, so mode is null. Dropping `v !== null` from the S2 condition therefore leaves every arm green, and so does dropping `phase !== 'ABORTED'`, even though the code at agent-cap.js:1957-1962 would change verdict. This is a test-coverage gap with no shipped behaviour change. | sound |
| 18 | verification | tools/hooks/agent-cap.js:1899 | low | low | confirmed | The two placement rules do differ. The harness (unattended-build.js:231) uses `a.reviewDir \|\| default`. The hook (agent-cap.js:1898) applies the default only when reviewDir is undefined or null. Given reviewDir "", parts becomes [""] and dir becomes [], so the hook denies with the 'not directly under builds/<slug>/' message, while the harness would have used the default. The input is unlikely, and the error fails closed with a misleading message. | sound |
| 19 | intent | tools/hooks/agent-cap.js:1898 | medium | medium | confirmed | When the harness passes an explicit reviewDir, the hook places the call by that reviewDir alone (agent-cap.js:1898-1906). It never checks a.slug against dir[-1], and it never checks units[].specPath. The subjects stray check only fires for a.subjects, and the harness normally derives subjects at runtime from its units (unattended-build.js:766-789). Its nested tier2-review call is then unseen. So a call {slug: run, specAudit: d, reviewDir: memory/builds/<landedSlugBuildWithKey>/reviews} reads that other build's README and its absent or LANDED RUN.md, and gets admitted. The run's own live RUN.md is never consulted. That defeats S4's purpose, and it takes a mistaken reviewDir, not forgery. Before this diff the harness path was not judged at all, so the hole is in the new guard: S4 claims a coverage it does not have. | sound |
| 20 | intent | tools/hooks/README.md:157 | medium | low | confirmed | The 'TWO LIMITS' text (hooks README:157-162) and the agent-cap.js:1837 comment predate this diff, but the diff made them stale. Both still say the hook reads the WORKTREE README and conf and leaves the unattended run to the BASE read. The new text one sentence earlier, and the code at agent-cap.js:1942-1955, decide a live run by RUN.md's pinned fact and skip the worktree. The first limit (the nested workflow() is unseen) is still true, but 'the programmatic route is the driver's to refuse' now understates what the hook judges. It is a doc and comment contradiction with no effect on behaviour. | sound |
| 21 | intent | tools/unattended/SKILL.template.md:247 | low | low | confirmed | SKILL.template.md:246-247 still says 'both keys are read at BASE', and the new sentence two lines below says the project default is read only from the default branch. PROTOCOL.template.md:356 (specs-audited) still says 'the project conf at BASE', while line 119 and the conf row at 499 say the default-branch side or the merge-base. The code (unattended.sh, _cb=merge-base(ASHA,base) under ANCHOR_KIND=run-branch) matches the new wording. The diff changed the behaviour and edited these same paragraphs, so the stale claim is its own. It is doc-only: the code refuses the self-opt-in whatever the text says. | sound |
| 22 | intent | tools/memory-tree/BUILD-METHOD.template.md:115 | low | low | confirmed | M4 'When' (BUILD-METHOD.template.md:115-116) still reads ".unattended.conf at BASE". The diff added the OWNER sentence but did not name either owner route, which spec 3 S1 calls for: a slug README on the default branch, or SPEC_AUDIT_DEFAULT there. This is a carrier/spec mismatch with no behavioural effect. | sound |
| 23 | intent | tools/unattended/unattended.sh:2387 | low | low | confirmed | On the second anchor, the conf blob that is evaluated is now $_cb (the merge-base), not BASE. Fail 55 and fail 54 (unattended.sh, inside the same block the diff rewrote) still say 'the project conf at the pinned BASE'. The not-owed DOD_OUT and fail 53 also still say 'project conf at BASE'. The refusal is still correct, but the message names the wrong commit. | sound |
