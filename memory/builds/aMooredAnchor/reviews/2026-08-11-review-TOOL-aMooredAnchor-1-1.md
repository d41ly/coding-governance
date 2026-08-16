# Review 1 — Tier-2 adversarial pass over the aMooredAnchor spec (design, no code)

**Serves:** spec-audit TOOL-aMooredAnchor-1  <!-- inferred: this build defines exactly one spec id, so the record can serve nothing else -->

**Verdict: FOLD AND REBUILD THE SPEC.**

**Scope:** `spec/2026-08-11-spec-aMooredAnchor-1.md` rev-1, its build README decision menu, and the
reproduction transcript + harness in `build/`, read against the code they govern
(`tools/unattended/unattended.sh`, `check-unattended.sh`, both sibling suites) at base `1192c96`.
No code exists yet; every finding is about what the spec would cause to be built.
**Method:** five primed lenses over the spec — (1) is the proposed **trust root** actually outside
the run's reach; (2) **completeness** — does the scope close the class it names, or one spelling of
it; (3) **gate cascade** — what else on the bar moves when this lands; (4) **source accuracy** — is
every line, count and file reference the spec asserts true of the tree; (5) **new defeats** — attack
the *hardened* design, i.e. assume every fork is picked well and find what still passes — then
default-refute skeptics in batches, then this synthesis pass.
**Result:** 38 raw findings, 32 confirmed, 6 refuted, 0 unverified. Precision 0.84.
**Dead lenses:** none. Every lens produced at least one confirmed finding and at least one *distinct*
defect no other lens reached — lens 5 alone produced two of the four blockers, and both of those are
orthogonal to the fork the owner is being asked to decide.
**Severity of the confirmed set:** the 32 confirmed findings consolidate to **17 distinct defects** —
**4 blockers, 6 highs, 4 mediums, 3 lows**. Every row names the raw ids it merges and the lenses that
arrived at it independently.

---

## Verdict

**Fold and rebuild the spec.** The problem this build was opened against is real, is reproduced with
controls, and deserves a unit. The spec is not the unit. Three things are wrong at the level of the
document rather than at the level of a paragraph:

**1. The recommended trust root does not hold, and the sentence that says it does is the same kind of
sentence the build exists to delete.** §4 argues option A is sound because *"To forge it the run must
land a default-branch push, which is the act under authorization."* `git fetch origin` resolves
`origin` through `remote.origin.url` — a line in `.git/config`, a file git does not track, that
appears in no commit, and that therefore has no value "at BASE" for anything to compare against. One
`git config` line repoints it at a bare repo the run just created and the "server-blessed" anchor is
the run's own commit; `url.<x>.insteadOf` does the same while leaving `remote.origin.url` reading
honest. Reproduced three times independently, by three lenses. R1 is not closed by A; it is renamed,
and made cheaper.

**2. Two total defeats sit entirely outside fork F1, so no answer to F1 reaches them.** A single
`git update-ref refs/replace/<base>` makes `git show <BASE>:RUN.md` — the one read the whole kit rests
on — return bytes the run authored seconds earlier, with `base:`, `origin/HEAD`, `GOV_DEFAULT_BRANCH`
and the remote-tracking ref *all left honest*. And `region()`'s marker test is a **prefix** test
followed by `next`, so text appended to the `<!-- run:mandate -->` line itself is never part of the
slice on either side: a run widens its own authorization inside the block a human reads, and both the
driver and check 13 certify the mandate as byte-identical to BASE. Options A, B, C and D all leave
both open. The spec's entire substance is *which ref names the base commit*; these are about *how the
base commit's content is read* and *what counts as the block*.

**3. The spec cannot answer its own F4, and the unit as drafted wedges the merge bar on its first
success.** Checks 4, 5, 6, 8, 9, 11 and 13 apply to **every** tracked run-state file regardless of
phase — line 139 of the leg is the only phase-conditional line in the loop, and it only tallies
`nlive`. Once a run does the thing its mandate authorizes (merge to the default branch, push), the
anchor advances past the pinned base and check 9's equality can never hold again. Reproduced with an
honest fixture, no attacker: gate green before landing, gate red forever after. Nothing in the
protocol or the Skill archives or exempts the record at close. F4's premise — that non-terminal files
are "almost never" — is backwards; terminal files are the steady state of every adopter that has ever
completed a run, and they are already the population that reds. The spec has no terminal-file story,
so F4 has no answer and S2/S4 make the wedge tighter.

Underneath those three, the unit as scoped would also red the existing self-test suite on its own
green control (eight assertions, six of them controls, reproduced), remove one subject-supplied
default-branch source while leaving two, contradict the gate leg's own READ-ONLY header with an arm
that structurally cannot notice, and contradict itself between §7 and §8 F2 about whether a gate leg
is added.

**What is right and should survive the rebuild.** The reproduction discipline is the best thing here:
two controls, four defeats, the harness run *before* the spec was written, and a recorded harness bug
(the reset helper eating `origin/HEAD`) that turned into R4 rather than being quietly fixed. That is
how §4's table gets to be measured rather than argued, and it is why this review could attack a
design instead of a claim. S2's direction is correct — a silent path in an authorization check is a
disarmed check, and converting each to a named refusal is the right move (the enumeration is wrong;
see D13). S4's *evidence-only, never an input* framing is the right rule even though the value it
picks carries no information under A (D12). S6 is worth writing on its own merits. And the spec is
honest about the thing that matters most: it says out loud that the finding it was opened against
under-states the problem. That instinct is correct and this review extends it — the spec under-states
it too.

**What a rebuilt spec should be.** Split the unit. The read-integrity and grammar work (D3, D4) and
the lifecycle work (D5) close reproduced defeats, depend on no fork, and are cheap. The trust-root
fork is a separate, larger question whose menu is currently mispriced in three of its four entries —
see the F1 section below. Landing the first group does not commit the owner to an answer on the
second, and the second cannot be decided from the menu as written.

---

## Distinct defects, severity-ranked

Legend: **raw** = the confirmed finding ids this row merges. **lenses** = which of the five arrived at
it independently. Every row ends with the *exact spec edit* that resolves it, because the deliverable
under review is a document.

---

### D1 — BLOCKER — option A's trust root is `remote.origin.url`, an untracked value the run writes

**spec §4 "The trust root" (lines 82-91), §8 A (228-231), README decision menu (65-67)** ·
raw: **1, 6, 34** · lenses: trust-root, completeness, new-defeats

**Claim.** The specified resolver is `git fetch --quiet origin "+refs/heads/$d:refs/unattended/anchor"`
followed by a `rev-parse`. `origin` is not an identity; it is a lookup in `.git/config`, through
`remote.origin.url` and `url.<base>.insteadOf`. `.git/config` is untracked, so unlike `base:` or
`RUN.md` there is no value "at BASE" any comparison could be made against. The security sentence in
§4 — *"To forge it the run must land a default-branch push"* — is therefore false, and it is the
load-bearing justification for the option the owner is being asked to pick.

**Evidence.** Reproduced independently three times, by three lenses, each with a live control.
Control with an honest bare remote: the resolver returns the honest anchor and the mandate at BASE is
the owner's. Then one command — `git config remote.origin.url <run-created bare repo>`, after
`git push <that repo> <forged>:refs/heads/main` — and the same verbatim snippet returns the run's own
forged commit as the anchor, with the real origin verified untouched. The `insteadOf` variant is
worse and also reproduced: `git config url.<evil>.insteadOf <honest>` redirects the fetch while
`git config remote.origin.url` still *reads* honest. One lens ran the whole route with the real
`.githooks/pre-push` wired via `core.hooksPath` and **no** `--no-verify`: the honest route
(`git push origin <forged>:refs/heads/main`) is blocked by the hook; the three-command route is not.
`grep -rn 'remote\.origin\.url|insteadOf|ls-remote' tools/ .githooks/` returns nothing — no leg on the
bar reads the URL. `GIT_CONFIG_COUNT/KEY/VALUE`, `GIT_DIR` and a second hook-less clone are the same
class and equally unaddressed.

**Spec edit.** §4 "The trust root": delete the circularity paragraph as a guarantee. Add
`remote.origin.url` (and `url.*.insteadOf`) as the first row of the §4 inventory table, on the
subject-supplied side. If A survives at all, it must (a) pin the remote — compare
`git config remote.origin.url` against a declaration reachable from a commit the run did not author
(e.g. a `REMOTE_URL` key read via `git show "$anchor:.unattended.conf"` after the fetch, so the
server's own copy vouches for it) and refuse on disagreement; (b) resolve in ONE step from
`git ls-remote` stdout rather than writing `refs/unattended/anchor` and reading it back, which leaves
a run-writable, cross-worktree-shared ref between the write and the read; (c) restate A's value as
cost-raising rather than unforgeability. §8 A and the README decision menu carry the same sentence and
must move in the same edit — the README is the artifact the owner decides from. Add a
`remote.origin.url`-swap arm to AC1, which today only fixes `refs/remotes/origin/main`.

---

### D2 — BLOCKER — the default-branch NAME stays in the run's reach; S1 leaves two of three sources

**spec §2 S1 (14-16), §4 inventory (112-118), AC3 (185-187)** · raw: **2, 7, 14, 36** ·
lenses: trust-root, completeness, gate-cascade, new-defeats

**Claim.** S1 says the gate *"derives the default branch itself and never from a value the subject
supplies."* The only derivation in the code is `git symbolic-ref --short refs/remotes/origin/HEAD`
(`check-unattended.sh:178`, `unattended.sh:108`) — an ordinary local symbolic ref that
`git remote set-head origin <anything>` rewrites with no push and no network. That is R1's class with
one fewer moving part: **no environment variable at all**. §4's inventory has a row for the default
branch resolving *empty* and no row for whether the resolved *name* is trustworthy.

**Evidence.** Reproduced twice, in both shapes. Env-var-free shape, `env -u GOV_DEFAULT_BRANCH`: with
a forged mandate and untouched refs the gate correctly reds (control); then two commands —
`git update-ref refs/remotes/origin/fakedefault <forged>` and
`git symbolic-ref refs/remotes/origin/HEAD refs/remotes/origin/fakedefault`, with
`refs/remotes/origin/main` verified unmoved — give **gate green, exit 0, silent** and
`driver rc=0 :: preflight OK — base <the forged commit>`. Server-blessed shape, which is strictly
worse: `.githooks/pre-push` classifies on the remote ref and `[ -z "$main_local" ] && exit 0`
(`:28`, `:31`), so a push to any non-default branch is **completely ungated** — exercised directly
against the real hook, `refs/heads/side` exits 0 with no output while `refs/heads/main` exits 1 with
`pre-push: refusing a raw push to main`. Push the forgery to a side branch on the *real* origin, then
`git remote set-head origin side`, and spec §4's resolver verbatim returns `d=side`, the anchor is the
forgery, and the mandate at BASE is the run's own text. No AC in §6 covers this: AC1 is the
`update-ref`-on-`origin/main` spelling and AC3 is explicitly the `GOV_DEFAULT_BRANCH` spelling.

**Spec edit.** §4: add an inventory row for *the default branch resolves to a name the run chose*,
beside the existing *resolves empty* row, and state in S1 that `refs/remotes/origin/HEAD` is
subject-supplied for the same reason `GOV_DEFAULT_BRANCH` is. Specify what `$d` derives FROM under
each F1 option: under A, from the same round trip that fetches the anchor
(`git ls-remote --symref <remote> HEAD`), with a named refusal when it disagrees with the local
symbolic ref; under D, say plainly that no purely local derivation exists and that S1 narrows the
attack rather than removing it. Add an AC and an arm for the env-var-free `git symbolic-ref` variant,
and one for a forgery pushed to a non-default branch with `origin/HEAD` repointed. **Caveat to carry
into the spec:** `git ls-remote --symref origin HEAD` returned empty against a plain `git init --bare`
origin in two independent fixtures, so the proposed replacement needs validating — including against
the kit's own fixture — before it is written into S1 as the source.

---

### D3 — BLOCKER — `refs/replace/*` rewrites what `git show BASE:RUN.md` returns; F1 cannot reach it

**not in the spec at any section** · raw: **32** · lens: new-defeats

**Claim.** Both the driver (`check_mandate`, `unattended.sh:259`) and the gate (check 13,
`check-unattended.sh:201`) establish "the mandate as committed at BASE" by reading an object through
git's normal object layer, which applies `refs/replace/*`. The spec's whole substance is about which
*ref* names the base commit. This defeat is in how the base commit's *content is read*, so options A,
B, C and D all leave it open — A fetches an honest anchor and then reads a replaced object through the
same `git show`.

**Evidence.** Reproduced by two lenses on independent fixtures; I rebuilt it a third time for this
synthesis. Honest fixture (real bare origin, `git remote set-head origin main`, honest mandate,
correct recorded base): gate exit 0 silent. Run forges its mandate and commits, leaving `base:`,
`refs/remotes/origin/main` and `origin/HEAD` all honest: gate reds with
`check 13 FAILED — a run-state file's mandate differs from the one at its recorded BASE`. Then ONE
command — `git commit-tree` a same-parent commit carrying the forged tree, then
`git update-ref refs/replace/<truebase> <that commit>` — and with a non-root base:
`merge-base now: 1cf1e44…  recorded: 1cf1e44…` (check 9 passes on a **match**, not a skip),
`git show <truebase>:memory/builds/tRun/RUN.md` returns the forged mandate, and the gate exits **0,
silent**. The same tree with `GIT_NO_REPLACE_OBJECTS=1` reds again on check 13; an honest tree with
that variable set stays green. No env var, no push, no network, no ref in `refs/remotes/` touched.
`grep` for `replace|graft|GIT_NO_REPLACE_OBJECTS|--no-replace-objects` across `tools/unattended/*.sh`
returns zero hits. Second route observed in the root-base case: the replacement makes `git merge-base`
*fail*, check 9 falls off the end silently (see D13), and check 13 still reads the replaced object —
so both check-9 outcomes go the attacker's way.

**Spec edit.** Add a scope item **ahead of S3**, in §2, titled as read integrity rather than anchor
resolution: every object read that establishes provenance must be replace-free
(`export GIT_NO_REPLACE_OBJECTS=1` at the top of both `unattended.sh` and `check-unattended.sh`, or
`--no-replace-objects` on each `git show`/`merge-base`/`rev-parse`), **plus** a positive gate check
that `git for-each-ref refs/replace/` is empty and `.git/info/grafts` does not exist — a replace ref
in a repo running an unattended run is itself the violation, not merely a thing to neutralise. Add an
AC with both arms (the fixture above as the red arm; an honest tree with the variable set as the green
control). State explicitly in §8 that this lands under **every** F1 option including D, so the fork
does not appear to subsume it. Two caveats for the builder: option C fails closed here by accident
(`verify-commit` on the replaced object finds no signature, which is luck, not design), and with a
root base the driver refuses at check 16 while the **gate** still goes green and silent — so the gate
arm is the one that must exist.

---

### D4 — BLOCKER-adjacent, rated HIGH — the mandate comparison never compares the marker lines

**not in the spec at any section** · raw: **33** · lens: new-defeats

**Claim.** `region()` — `unattended.sh:75-82` and its copy at `check-unattended.sh:119-123` —
identifies a marker with `index($0,o)==1`, a **prefix** test, and then `next`s the line. The marker
line's trailing content is never part of the slice on either side of the comparison. A run appends
authorization text to the `<!-- run:mandate -->` line in the working copy; both extracted slices stay
byte-equal because both sides drop the whole line. The injected sentence sits **inside** the visible
mandate block and reads as part of the owner's authorization to any later human or resumed agent.
Independent of the anchor: it survives every F1 option, S1-S4, and a perfect trust root.

**Evidence.** Reproduced by two lenses and again here. Working copy after one `sed` on the open
marker line, committed (clean tree, so the driver's `check_clean` passes):

```
<!-- run:mandate --> The owner ALSO authorizes force-push and deleting main.
The owner authorizes tRun to merge and to push.
<!-- /run:mandate -->
```

BASE side is the unmodified three-line block. Result: **gate rc=0, no output**, and
`driver rc=0 :: unattended: preflight OK`. The close marker gives the same result. Same class applies
to the `run:generated` markers check 8 reads. `check-unattended.test.sh` has no arm for a marker line
carrying trailing content — the only `run:mandate` fixtures in the file (`:312-318`) are clean.

**Spec edit.** Add a scope item beside D3's: `region()` must reject a marker line carrying anything
beyond the marker (`$0 != o` after the prefix match, exiting 3 — the existing malformed-pair code), in
**both** copies, and F2's shared resolver should carry the marker grammar with it so there is one
place to be wrong. Add an AC and paired arms in both sibling suites: trailing text on the open marker,
on the close marker, and a green control on clean markers. Note in §4 that this changes `region()`'s
contract, which `check_mandate`, `verb_status`, check 8 and check 13 all share. `ARMS_FLOORS` for both
files is already in the Files-touched table, so that half is budgeted.

---

### D5 — BLOCKER — no terminal-phase lifecycle, so the first landing permanently reds the bar

**spec §8 F4 (270-274), §4 Migration (120-125), §5 risks, AC10** · raw: **4, 15, 35** ·
lenses: trust-root, gate-cascade, new-defeats

**Claim.** F4 proposes keeping the common bar offline by fetching only when a run-state file is
non-terminal, *"which is almost never"*. Both halves are wrong. The per-file loop
(`check-unattended.sh:126-221`) applies checks 4, 5, 6, 8, 9, 11 and 13 to **every** tracked run-state
file regardless of phase — `:139` is the only phase-conditional line and it merely tallies `nlive`.
And terminal files are not "almost never": they are the steady state of every adopter that has ever
completed a run, and that population **already reds permanently**, because check 9 asserts the
recorded `base:` *equals* the merge-base, and merging + pushing (the two acts the mandate authorizes)
moves the merge-base past the pin forever.

**Evidence.** Reproduced twice with **honest** fixtures and no attacker. Step 1, live run on a unit
branch: exit 0, silent. Step 2, `phase: LANDED` still on the unit branch: exit 0, silent — so
terminality is not the trigger; the merge-base moving is. Step 3, `git merge --no-ff` to main +
`git push origin main`: **gate reds** with BOTH `check 9 FAILED — a recorded BASE is not the
merge-base this history reproduces (recorded 227cf710…, computed b17ce80d…)` and
`check 9 FAILED — the merge-base equals HEAD`. Step 4, a fresh unrelated branch off main afterwards:
still red on the first. `.githooks/pre-push` runs this leg on every later default-branch push
(`tools/gate-legs.json:292-295`). `verb_close` (`unattended.sh:417`) only writes `phase: LANDING`;
nothing in `PROTOCOL.template.md` or `SKILL.template.md` moves, archives or deletes the record, and
`UNATTENDED-PROTOCOL.md:90` contemplates terminal files persisting. `git ls-files 'memory/builds/*/RUN.md'`
is empty in this repo, which is why it has never been observed here — and why §4's Migration paragraph
(*"No live run exists in this repo"*) reasons about the wrong population: the one that breaks is the
**landed** records, and the first of them is this build's own if it is landed unattended.

**Spec edit.** Add a scope item and an AC for the terminal case, **before** S3 is implementable, and
answer F4 from it. Record in §8 F4 that *"skip terminal phases"* is not a safe fix: `phase:` is
written by the run (`set_fact`, `unattended.sh:337-349`; the driver's own writes at `:328` and `:417`),
so a phase-keyed carve-out hands the run a one-line escape from checks 9 and 13, and the two existing
mandate fixtures (`check-unattended.test.sh:320-336`) already set `phase: LANDED` and still expect
check 13 to fire. The two defensible shapes: require `--close` to move the record under a path the
leg does not select and gate that the move happened; or change check 9's **question** for a landed
record from equality to *the recorded base is an ancestor of the anchor and carries a byte-equal
mandate* — which is already the shape §8 F2 recommends for the gate, but F2 is framed as a
code-organisation fork and S2/S4 keep the equality form. Correct the §4 Migration paragraph to name
landed records. Add an AC: *the gate is green on a tree containing a LANDED run*. Note that AC10 is
unreachable today for a build landed unattended by this kit.

---

### D6 — HIGH — S1 is scoped to the gate; the driver keeps the tainted variable and no AC covers it

**spec §2 S1 (14), §3 OUT (37-40), Files-touched (137), AC2-AC5** · raw: **2 (part), 9** ·
lenses: trust-root, completeness

**Claim.** S1 names `check-unattended.sh` only. `unattended.sh:106-110` `default_branch()` still
returns `$GOV_DEFAULT_BRANCH` verbatim, and §3's non-goals enumerate five other readers
(`.githooks/*`, `push-main.sh`, `drift_report.py`, `check-verdict-epoch.sh`) without listing the
driver's own — so the driver's read is neither in scope nor explicitly out. The driver is what
authorizes the run to **start**, and under option A its value chooses which refspec is fetched.

**Evidence.** `default_branch()` feeds `resolve_base` -> `trusted_base` -> both `verb_preflight`
(`:303`) and `dod_met`'s `mandate-reachable` re-derivation at `--close` (`:430`), so the close-time
re-derivation inherits the same taint. Measured: with a forged mandate,
`git update-ref refs/remotes/origin/fakedefault <forged>` and
`GOV_DEFAULT_BRANCH=fakedefault bash tools/unattended/unattended.sh --preflight tRun --keepalive-id k1`
prints `preflight OK — base <forged>` with rc=0; an option-A driver inherits it unchanged, because
the fetch of `refs/heads/fakedefault` succeeds when the branch was pushed. Read all ten ACs: AC1,
AC3, AC4, AC5 and AC7 say the **gate** reds; AC2 is the only driver AC and covers R1 only. The repro
transcript itself records *"driver: not run"* for R2, R3 and R4. Separately, S4's premise — the gate
compares the driver's recorded ref name against its own — requires the two to derive the name the same
way, which S1 as scoped guarantees they will not.

**Spec edit.** Bring `unattended.sh:default_branch()` into S1 explicitly, or move it to §3 with the
reason; do not leave it unnamed. Name which component **owns** the derivation, because S4 is
unimplementable while the two disagree. Add ACs mirroring AC3/AC4/AC5 for the driver. Add
`unattended.test.sh:145-146` to the Files-touched table — its pinned refusal string
`cannot resolve the default branch (set GOV_DEFAULT_BRANCH)` becomes a lie once the driver stops
reading the variable — and `:218`, whose `GOV_DEFAULT_BRANCH=nosuchbranch` arm changes meaning under
option A (an unresolvable name becomes a fetch failure, a different refusal).

---

### D7 — HIGH — S1+S2 red the shipped self-test's own green control, and §4 misdescribes the fixture

**spec §2 S5 (25-26), Files-touched (139), AC3 (185-187), AC8 (196-198), §4 (51)** ·
raw: **5, 8, 21, 30** · lenses: trust-root, completeness, source-accuracy

**Claim.** `check-unattended.test.sh:75-76` builds `origin` with `git init --bare` + `git remote add`
+ `git push` and **never** `git remote set-head`, so `refs/remotes/origin/HEAD` is UNSET; `:81` then
exports `GOV_DEFAULT_BRANCH=main` for the whole suite. That export is the **only** default-branch
input the fixture has. Once S1 stops the gate reading the variable and S2 makes an empty default a
named refusal, the derived branch is empty and every arm reds — the green controls included. S5
budgets no fixture change; the Files-touched row says only *"arms for R1 through R4, each with a
control."* AC3 (*"passes by the variable having no effect"*) and AC8 (*"the honest fixture stays
green"*) are both unsatisfiable on today's fixture.

**Evidence.** Executed against the real test file. Unmodified suite: `PASS (57 assertions)`. Copied
the kit to scratch, applied the minimal S1+S2 (delete the `d=${GOV_DEFAULT_BRANCH:-}` read at `:177`,
make an empty derived `$d` a `fail 9`), `bash -n` clean, re-ran: **eight failures** —
`a conforming tree exits 0` (got 1), `a conforming tree prints nothing`,
`a project phase EXTENSION is green`, `a project DoD EXTENSION is green`,
`a conforming kickoff engine is green`, `a blank KICKOFF_ENGINE turns the check off`, plus the two
check-9 red arms that **stop firing**: `a recorded BASE is not the merge-base this history reproduces`
(`:219`) and `the merge-base equals HEAD` (`:300`). All six green assertions carried the identical new
refusal, proving the derived `$d` was empty. A second lens isolated the same fact from the other side:
changing only `:81` to `unset GOV_DEFAULT_BRANCH` on the **unmodified** gate produces exactly those two
failures and nothing else. So the shipped fixture has been running permanently in the R4 state and its
only check-9 coverage exists because of the export. `unattended.test.sh` has the same shape (`:102-110`)
and at `:145-146` arms the driver's refusal *on the variable being unset* — an arm that can only pass
because `origin/HEAD` is unset.

The false-equivalence half compounds it. §4 line 51 and the transcript both say the harness *"builds
the fixture `check-unattended.test.sh` builds."* The harness runs `git remote set-head origin main`
(`repro.sh:64`) and never exports the variable; the shipped fixture does the exact opposite on both.
Those are precisely the two inputs the four defeats manipulate. Stating the fixtures are the same is
what kept the fixture rework out of the spec.

**Spec edit.** Add to S5 and to the Files-touched rows for **both** sibling suites: the fixtures gain
`git remote set-head origin main` and the gate arms lose `export GOV_DEFAULT_BRANCH=main`. Re-word AC3
to name the required control rather than asserting the pass mechanism, and add an AC that both suites
run green with the variable unset **and** with it set to a hostile value. Give each of the R2/R3/R4
arms a control distinguishing *red because the anchor is forged* from *red because no default branch
resolved* — the two refusals must be asserted by distinct text, or the arm proves S2's refusal was
reached and not that R2 is closed. Correct §4 line 51 and the transcript to *"builds the same shape,
with two deliberate differences"*, name both, and record the consequence. Note that AC8's *"a higher
assertion count than today"* cannot notice an arm that stopped **reaching** its check.

---

### D8 — HIGH — option A makes the READ-ONLY bar leg a writer, and its guarding arm cannot see a fetch

**spec §4 (82-85), §5, §7, Files-touched (137, 139)** · raw: **13, 16, 23, 37** ·
lenses: completeness, gate-cascade, source-accuracy, new-defeats

**Claim.** `check-unattended.sh:9-12` declares the leg *"READ-ONLY, which is what lets it run on the
bar. It writes nothing, renders nothing and derives nothing"*, and `check-unattended.test.sh:338-343`
arms that claim at source level. Option A has the gate write `refs/unattended/anchor` (and
`FETCH_HEAD`) into the repository it is judging, on every full-bar run, from inside `.githooks/pre-push`
while a push is in flight. The spec acknowledges neither the contract nor the arm.

**Evidence.** Ran the arm's exact detector,
`grep -nE '(^|[^-[:alnum:]])(mv|rm|cp|sed -i|tee|> *"?\$)'`, over a file containing the spec's own
lines — the fetch, the `rev-parse`, a bare `git update-ref`, and `git ls-remote --symref`: **no match**
on all four. So the invariant would become false while the assertion written to protect it stays
green — the same shape as the `unattended.sh` comment S7 exists to correct, one file over.
`tools/gate-legs.json:292-295` confirms the leg is on the bar. `refs/unattended/*` is a **common** ref,
not per-worktree: verified with a real `git worktree add` that a ref written in the main tree reads
back identically from the linked one, and this repo runs its bar from linked worktrees under
`.claude/worktrees/`. Separately, §4's Files-touched row for `check-unattended.sh` reads *"S1, S2, S4;
independent derivation"* with no S3, while §2 S3 says *"in the driver and in the gate."*

**Spec edit.** Decide in §4 whether the leg may write, and say which. The cheap answer that keeps the
invariant: use `git ls-remote origin refs/heads/<d>` — it answers the same provenance question, reads
the server, writes nothing to the local ref store or object store, resolves in one step (removing D1's
write-then-read window and the cross-worktree collision) and needs no header rewrite. If a real fetch
is required, then in the same edit: rewrite `check-unattended.sh:9-12`, **replace** the source-level
arm with one that can express *writes a ref* (the current verb list cannot), name the ref it may
write, state the bar's new side effect in §5 observability, and add both `check-unattended.sh`'s header
and `check-unattended.test.sh`'s read-only arm to the Files-touched table. Add S3's gate half to the
`check-unattended.sh` row.

---

### D9 — HIGH — C is not "the only purely-local unforgeable root": three `git config` lines forge it

**spec §8 C (237-239), README decision menu (71-73)** · raw: **3** · lens: trust-root

**Claim.** Under this spec's own stated threat model (§5: an agent process with full repo write
access), `gpg.format`, `user.signingkey` and `gpg.ssh.allowedSignersFile` are ordinary repo-local
config. The run generates its own key, writes its own allowed-signers file, points git at both, and
signs the mandate commit itself. Nothing in the repo constrains any of them. C is presented to the
owner as the strongest option on the list, and the sentence the owner would decide on is wrong.

**Evidence.** Reproduced end to end. `ssh-keygen -t ed25519` (run-generated), then repo-**local**
`git config gpg.format ssh`, `git config user.signingkey <runkey.pub>`,
`git config gpg.ssh.allowedSignersFile <the run's own file>`, then `git commit -S`.
`git verify-commit HEAD` prints a Good signature and exits 0; `git log -1 --format='%G?'` prints `G`.
`git config --local --list` shows all three deciding values are repo-local.
`grep -rn 'gpg\.program|allowedSigners' tools/ .githooks/` returns nothing — no leg constrains them.

**Spec edit.** Rewrite the §8 C entry and the README menu line to state the precondition that IS the
cost of C: verification must pass `-c gpg.ssh.allowedSignersFile=<absolute path outside the repo>`
(and `-c gpg.format` / `-c gpg.program`) on the git command line so repo config cannot override it,
and the allowed-signers file must be provisioned out of band. Then re-price C against that. Drop
*"the only purely-local unforgeable root"* from both places. This must land **before** the owner picks
from the menu; otherwise a builder ships `git verify-commit` plus a written guarantee that is false —
exactly the failure the build was opened against.

---

### D10 — HIGH — §7's "no new gate leg" contradicts §8 F2, and F2's cost note misreads `check-arms.py`

**spec §7 (218-219), §8 F2 (258-262), Files-touched** · raw: **17, 27** ·
lenses: gate-cascade, source-accuracy

**Claim.** §7 asserts `tools/gate-legs.json` does not move. §8 F2 recommends a shared sourceable
`tools/unattended/anchor.sh`, and the charter's rule is that a kit's siblings *"are LEGS, not files
someone remembers to run."* F2's cost note — *"a new `*.sh` in a kit dir is discovered by
`check-arms.py` and needs its own sibling test and `ARMS_FLOORS` entry"* — is wrong on **both** halves,
which means the owner is pricing a fork with a false number.

**Evidence.** `check-arms.py` discovery (`:115-131`, `HELPER_RE = ^\s*fail\(\)\s*\{` at `:52`) skips
`*.test.sh`, then requires the file to **define** `fail() {` **and** carry a `fail <n> "` call site.
`adopt-unattended.sh:14` records the identical rule in a comment as the reason it deliberately has no
`fail()` helper. Reproduced: added `tools/unattended/anchor.sh` with two `fail 22 "…"` call sites and
no `fail() {` definition, committed — `check-arms.py --check` exits 0 and `--report` shows no rows for
it. So a sourced resolver holding the unit's refusals is **structurally invisible** to the harness
meta-gate and needs no floor at all. The other direction: `ARMS_FLOORS` in `.memory-tree.conf:64`
reads `tools/unattended/unattended.sh:31:31 tools/unattended/check-unattended.sh:33:33` — both files sit
**exactly** at their pins, so every refusal relocated out of either drops below a shrink-only floor
(measured: moving one `fail 11` call site gives `has 32 fail branch(es) against a floor of 33`). And a
`fail()`-defining `anchor.sh` with the sibling test the charter requires moves `gate-legs.json`
(which carries five unattended legs at `:292-324`), `memory/map/features/unattended.md:11` (which pins
those five names), and the regenerated map artifacts — all of which §7 denies.

**Spec edit.** Make §7 conditional on the F2 outcome and say so in one sentence: a `fail()`-free
sourced resolver adds no leg and no floor; a `fail()`-defining `anchor.sh` plus its sibling adds a
`gate-legs.json` entry, a `memory/map/features/unattended.md` gate-legs row, a fresh map render, and a
charter gate-suite bullet — and the drift-audit pin
`handkept_inventories_disagreeing_with_source = 7` (`tools/drift-audit/drift_signals.py:145`) must be
re-checked. Correct F2's cost note to the actual discovery predicate. Fix §4's Files-touched line
*"ARMS_FLOORS for both files, which gain branches"*, which has the direction backwards if refusals
move out. Restate AC9 as *the floors are RAISED to the measured counts*: `check-arms.py` only reds
when a count **falls** (`if got[i] < want[i]`, `:279-283`), so *"in both directions"* is unverifiable
and a forgotten raise is silent.

---

### D11 — MEDIUM — S2's empty-default refusal is the wrong remedy under A, and reds ordinary clones

**spec §2 S2 (16-18), §4 inventory (112-118), AC5 (190-191), §5 risks** · raw: **12** ·
lens: completeness

**Claim.** S2 makes *the default branch resolving to empty* an unconditional named refusal. Under
option A the default branch is obtainable from the server even when `refs/remotes/origin/HEAD` is
absent, so the absence is not a reason to refuse — it is a reason to ask the remote. As specified, any
tree with a run-state file and no `origin/HEAD` reds the merge bar with no attacker and no defect.

**Evidence.** The `origin/HEAD`-absent state is ordinary: `.githooks/pre-push:19` already carries
`git remote set-head origin -a` as a remedy string, and the kit's own fixture is in that state
(measured — see D7). With the minimal S1+S2 applied, all four green controls in the shipped suite red
with `UNATTENDED check 9 FAILED — cannot derive the default branch`. **Correction to carry into the
spec:** `git ls-remote --symref origin HEAD` returns nothing against a bare `git init` origin whose
HEAD is an unborn `refs/heads/master`, so the network remedy is not automatic either — it works
against a real server and needs the fixture's origin HEAD set.

**Spec edit.** Under option A, make the refusal *the remote could not be asked*, not *the local
symbolic ref is absent*, and derive the branch from the same round trip that resolves the anchor. Keep
the empty-default refusal only under D. Either way, split §4's inventory row *"default branch resolves
empty"* into the two cases it currently conflates, and give AC5 a green control: an honest tree with
no `origin/HEAD` and a correct recorded base must be GREEN.

---

### D12 — MEDIUM — S4's `base-ref:` is a tautology under the recommended option A

**spec §4 Data model (99-108), §4 The trust root (83-84), AC7 (194-195), §8 F3** · raw: **10, 20** ·
lenses: completeness, gate-cascade

**Claim.** Under option A the anchor is always fetched into the fixed local ref
`refs/unattended/anchor`, so *"the full ref name the anchor resolved to"* is a constant string on both
sides and AC7's disagreement branch compares `"refs/unattended/anchor"` with itself — this corpus's own
`assertion-between-two-derived-values` class. The values that actually discriminate an honest run from
a forged one are the upstream branch name and the anchor sha, and S4 records neither.

**Evidence.** Spec `:83-84` fixes the fetch destination; `:103` defines `base-ref:` as the ref name the
anchor resolved to; option A removes the candidate loop, so no other name exists.
`memory/gotchas/assertion-between-two-derived-values.md` is in the corpus, its "Where it bit" section
names `tools/unattended/check-unattended.sh`, and its test (`:44-47`) is *name the edit that should
make it red and MAKE that edit*. **One correction to the raw finding:** the disagreement branch is not
wholly unreachable — under S1 as scoped the driver derives `$d` from `GOV_DEFAULT_BRANCH` and the gate
does not, so an attacker who sets only the env var trips it. The defect is the ambiguity about which
name is recorded, plus the tautology under the literal reading. Against that, S4 buys an
adopter-visible run-state grammar change and the hard migration break §4 already states.

**Spec edit.** In §8 F3, apply the gotcha's own test to S4 in writing: name the edit that makes the
disagreement branch red and show it is an edit an attacker would make. Then either record the
discriminating pair — the remote name plus the upstream branch the fetch used, plus the anchor sha —
rather than the local ref the fetch happens to write into; or keep only the presence half (the
`TOOL-aUnmannedHelm-5` rule S4 already cites) and say that under A the local ref name carries no
information; or defer S4 to a follow-up. Whichever, §4's Data model and §4's trust root must stop
contradicting each other about what a "ref name" is here.

---

### D13 — MEDIUM — S2's "three silent paths" double-counts one and omits the merge-base-failure exit

**spec §2 S2 (16-18), §4 inventory (112-118)** · raw: **25** · lens: source-accuracy

**Claim.** S2 enumerates *"the default branch resolving to empty, the ref-candidate loop completing
with no match, and the loop being skipped wholesale."* The first and third are one branch — the loop is
skipped wholesale precisely when `[ -n "$d" ]` is false (`check-unattended.sh:179`). §4's inventory
honestly lists only two. The genuinely distinct third exit — a candidate ref that **resolves** but
whose `git merge-base` fails (`:184`, `|| continue`) — appears in neither, and it is the one an
unrelated-history or shallow clone lands on.

**Evidence.** Isolated: a fixture with `refs/remotes/origin/main` resolving, `origin/HEAD` set, HEAD on
an orphan history and a recorded `base:` of 40 zeros — `git merge-base` exits 1, `:184` continues, the
loop falls off the end, and the gate exits 0 with **empty output**. No env var, no attacker. Observed
again as the second route in D3's root-base variant, where the replacement commit makes `merge-base`
fail and check 13 then reads the replaced object. It also survives option A: merge-base against a
freshly fetched anchor can still fail in a shallow clone.

**Spec edit.** Replace S2's enumeration with the three real exits: (a) the default branch is
unresolvable, (b) no candidate ref resolves, (c) a candidate resolves but `git merge-base` fails. Add
row (c) to the §4 inventory, and add an AC plus an arm with an orphan-history or shallow fixture.

---

### D14 — MEDIUM — the run-state population is word-split, so a spaced folder drops out of every check

**not in the spec at any section** · raw: **38** · lens: new-defeats

**Claim.** `check-unattended.sh:109` builds `RUNS` as a newline-joined string and `:126` iterates
`for f in $RUNS` unquoted under default IFS. A tracked path with a space matches the POP regex at
`:110` — so check 4's mis-segmentation guard at `:111-113` correctly does not fire — but splits into
two non-existent paths, both discarded by `[ -f "$f" ] || continue` at `:127`. Checks 4, 5, 6, 8, 9, 11
and 13 then never run on that file. The driver's `check_slug` (`unattended.sh:176-187`) refuses such a
slug, but the gate has no slug grammar and the **gate** is what runs on the bar.

**Evidence.** Reproduced twice. Committed `memory/builds/t Run2/RUN.md` carrying a forged mandate and a
40-zero base alongside a normal one; `git ls-files` lists both; the gate exits 0 and mentions
`t Run2` **zero** times. Scope caveat, verified: this repo's memory-tree hygiene check 4 would red the
folder name, so the exposure is the standalone copy-installed adopter the leg explicitly designs for
(comment at `check-unattended.sh:227-229`).

**Spec edit.** Add to S2's silent-path inventory: iterate the population with `while IFS= read -r f`,
and make an unreadable selected path a **named refusal** rather than a `continue` — a run-state file
in the index but not readable at its selected path is exactly the condition check 4 was written to
catch. Arm it with a spaced-folder fixture plus the existing green control. It belongs in this unit
because S2 already opens check 9's silent-path inventory, and it is one loop.

---

### D15 — LOW — §5's perf plan is unrunnable here: no run-state file exists, so the loop never runs

**spec §5 perf (161-162), AC10 (202)** · raw: **29** · lens: source-accuracy

**Claim.** §5 says *"one `git fetch` … per gate run. The gate runs on every full bar, so the fetch is
measured before it lands and refused if it is not fast."* This repo contains no `RUN.md`, tracked or
untracked, so the per-file loop that check 9 lives in never runs and the gate would issue zero fetches
here. Under F4's narrowing that is permanent, not incidental.

**Evidence.** `git ls-files 'memory/builds/*/RUN.md'` and `find memory/builds -name RUN.md` both
return nothing. `RUNS`/`POP` derive from `git ls-files` at `:109-110`, and checks 4-13 all sit inside
`for f in $RUNS` (`:126-221`). §4's Migration paragraph states the same fact and draws no consequence
from it.

**Spec edit.** Correct §5 to say the fetch is exercised and measured by the **self-test**, not by this
repo's bar, and move the offline-refusal proof into the fixture arms (`check-unattended.test.sh`
already builds a local bare origin) with an explicit unreachable-remote arm. Note against AC10 that a
green full bar on this tree exercises none of the new refusal or fetch paths.

---

### D16 — LOW — §7 credits the wiring leg with seeing the protocol change; it reads only the Skill

**spec §7 (210-211), Files-touched** · raw: **31** · lens: source-accuracy

**Claim.** §7 lists the wiring leg and the adopter as *"both of which see the protocol text change."*
`adopt-unattended.sh` renders `SKILL.template.md` against `.unattended.conf` and diffs the result
against `.claude/skills/unattended/SKILL.md`; `PROTOCOL.template.md` appears nowhere in it. The leg
that sees the protocol pair is check 10 **inside `check-unattended.sh`** — the leg under change —
which §7 does not name.

**Evidence.** `adopt-unattended.sh:62` sets `TEMPLATE="$KIT_DIR/SKILL.template.md"`; `:83-101` renders
to a temp file, `diff -q`s it, then checks for surviving `{{`-shaped placeholders.
`adopt-unattended.test.sh:30` copies the protocol only as fixture setup.
`check-unattended.sh:227-243` is the protocol-pair comparison. The consequence is live, not
hypothetical: `SKILL.template.md:20-21` already tells the agent *"the preflight will refuse it anyway
by comparing against the pinned BASE"*, which is the contract S3 rewrites, and option A adds a network
precondition the agent must know about.

**Spec edit.** Name check 10 as the protocol-parity leg in §7, and decide explicitly in Files-touched
whether `SKILL.template.md` and the tracked `.claude/skills/unattended/SKILL.md` render move — if they
do, `adopt-unattended.sh --check` reds until the render is regenerated and committed, and AC10 fails
until then.

---

### D17 — LOW — S7 cites the wrong line: the false sentence is at `unattended.sh:119-120`, not `:113`

**spec §2 S7 (29-31), §4 (72), README (44), transcript (66)** · raw: **24** · lens: source-accuracy

**Claim.** S7 says *"Correct the false comment at `tools/unattended/unattended.sh:113`."* Line 113 is
`# reach. It was not. Three separate defeats, all reproduced:` — it carries no claim at all. The false
sentence is the second bullet, at `:119-120`.

**Evidence.** At HEAD: `:119` *"A remote-TRACKING ref is the weakest thing the run cannot rewrite.
Moving it requires a push,"* / `:120` *"which is the act being authorized, so using it is not
circular."* The same wrong pointer sits in §4 line 72, README line 44 and the transcript line 66, so it
is propagating into the permanent record. Mitigating: both the README and the transcript quote the
sentence itself, and `:113` is inside the same comment block (`:112-122`), so a builder is unlikely to
be actually misled.

**Spec edit.** Change S7, §4 and the README to cite `tools/unattended/unattended.sh:119-120`, and
quote the bullet in full so the target survives later line drift.

---

## F1 — the trust root: this review's recommendation

The owner is being asked to pick from a four-item menu. **Three of the four entries are mispriced, and
the fourth is priced correctly but under-scoped.** Before anything else, the menu has to be corrected:

- **A** is recommended on a guarantee that does not hold (D1). Its trust root is an untracked
  `.git/config` line, its cost is a permanent network dependency on the merge bar, and its
  optimisation (F4) rests on a false premise about which run-state files exist (D5). Net: A costs
  more than D and buys a defeat that is one `git config` cheaper than the one it closes.
- **B** was already admitted only as corroboration, which is the right call and needs no change.
- **C** is described as *"the only purely-local unforgeable root"*. As a naive `git verify-commit` it
  is forgeable by three repo-local config lines (D9). It can be made true — but only with the
  verification keyring and gpg program supplied on the git command line from outside the repo, and the
  allowed-signers file provisioned out of band. That precondition is C's entire cost and it is absent
  from both the spec and the menu.
- **D** is honest about the bound, and this review's evidence strengthens the case for it. But D as
  drafted would ship S1 plus a protocol paragraph asserting the gate no longer reads a subject-supplied
  input — while the input S1 leaves behind (`refs/remotes/origin/HEAD`) is equally subject-supplied and
  **cheaper** to abuse than the one removed (D2). So D's paragraph would be false too unless it is
  written to say so.

**Recommendation: D, restated honestly — and move the unit's substance off the fork entirely.**

The reasoning is that F1 is not where this build's value is. Four defeats were reproduced against the
current kit, and of the new work that would actually close a reproduced defeat, **none of it depends on
which trust root is chosen**: replace-free object reads (D3), the marker grammar (D4), the terminal
lifecycle (D5), the merge-base-failure exit (D13), the word-split population (D14). Those land under A,
B, C or D identically. Meanwhile the fork's own headline option does not close R1, and its cost — a
network dependency on a bar that runs constantly — falls on every adopter forever.

So: take D, and write the bound into the protocol as what it actually is. Not *"no local anchor is
unforgeable"*, which is too weak to be useful, but the specific, checkable version:

> The anchor is unforgeable only by a process that does not edit `.git/config` and does not write
> `refs/replace/*`. No in-repo mechanism can verify the first, because `.git/config` is untracked and
> appears in no commit. The second **is** checkable and this kit checks it. The guarantee therefore
> rests on the pre-push hook and on the absence of a config-level redirect, and a run with full repo
> write access can defeat it — which is the boundary, stated rather than argued.

That paragraph is worth more than option A, because it is true, and because the next reviewer can test
it. It also makes the residual risk legible to the owner in a way *"forging the anchor requires landing
a default-branch push"* actively prevented.

**If the owner picks A anyway**, four non-negotiable amendments before code: pin the remote URL against
a declaration reachable from the anchor; resolve through `git ls-remote` in one step (read-only, no
intermediate ref, no cross-worktree collision, no header rewrite); derive `$d` from the same round trip;
and delete the unforgeability sentence from §4, §8 and the README. **If the owner wants a real trust
root**, C is the only candidate that can be made true, its price is out-of-band key provisioning across
the fleet, and it should be its own build with its own spec — not a bullet in an open-questions
section.

---

## What the review did NOT find

Named so the next reader knows the coverage rather than guessing it. Each of these was checked and came
back clean, or was checked and the objection did not survive.

- **The prior review's landed fixes hold.** `region()` and `splice()` now carry the close-after-open
  order clause (`cat < oat`) in all three copies, including the gate's at `check-unattended.sh:123`.
  `trusted_base` returns via the `TB` global rather than stdout, so a refusal is no longer captured
  into the caller's variable. `CORE_FLOOR` shape validation at `check-unattended.sh:76-81` refuses the
  malformed shapes, not only the absent one. Check 13 exists and its four branches are live — the
  mandate-differs branch reds correctly in every fixture this review built, which is what gave the
  green results below their meaning.
- **Check 13's mandate comparison is well designed.** Every defeat found against it (D3, D4) attacks an
  input or a read path, never the comparison. Re-extracting both sides from scratch and refusing
  anything that is not exactly one well-formed block on each side is right and should not change.
- **S2's direction, S6, and S7's substance.** No finding survived against the principle that a silent
  path in an authorization check is a disarmed check; the enumeration is wrong (D13) and the remedy for
  one path is wrong under A (D11), but the move is correct. The gotcha record S6 proposes is worth
  writing as specced. S7's substance is right; only its line citation is wrong (D17).
- **The §10 reuse audit's conclusion.** Challenged and refuted: the wording about where
  `drift_report.py` takes its base ref from is loose, but the decision — do **not** wire the unattended
  anchor through `Git` in `tools/drift-audit/drift_report.py` — is correct and correctly reasoned, and
  that reader's `GOV_DEFAULT_BRANCH`-first ladder is the opposite of what S1 wants.
- **`base-ref:` as a sixth authored key.** Challenged against `UNATTENDED-PROTOCOL.md` §2's
  authored-facts rule and refuted: the tree already re-derives `base:` independently
  (`check-unattended.sh:184-185`, `unattended.sh:151-171`) and admits it, so independent derivation
  cannot disqualify `base-ref:` without disqualifying `base:`. Nothing in the tree counts authored keys,
  so no gate reds on a sixth. The objection to `base-ref:` is D12's, and it is about information
  content, not admissibility.
- **AC6's differential.** Challenged as *"break the remote, expect a red"* with no green half, and
  refuted: AC6 says the driver and gate each refuse **by name**, §5 requires the refusal to name the
  unreachable remote, AC9 requires every new `fail` branch to be armed by a positive assertion naming
  its own text, and AC8 is the green half. Under this repo's arming discipline that combination cannot
  be satisfied by a silent fall-back.
- **The kickoff-manifest ratchet.** `.claude/SESSION-KICKOFF.md:6` does list `.memory-tree.conf` in
  `watch:`, so an `ARMS_FLOORS` edit does require a re-stamp — but AC10 already binds the builder to a
  green full bar, of which the ratchet is a leg, and §7 is explicitly a partial list. Checklist
  completeness, not a spec defect.
- **The install-prefix trap on a kit path in the protocol document.** Real mechanism (check 10 strips
  the prefix from the installed copy only, and `check-install-prefix.sh` would hit a prefix-free
  `unattended/anchor.sh` spelling), but conditional on an authoring choice the spec does not make:
  grepped both protocol copies and found zero kit-path spellings today, and neither S7 nor §5 asks for
  one.
- **The `rb`-consumed-by-check-13 path.** Check 13 reads the run-written `rb` (`:200-201`) and today can
  compare forged-at-`rb` against forged-in-worktree when check 9 goes silent — reproduced, but it is
  R4's mechanism weaponised, and R1-R4 are out of re-report scope. Once S2 closes every silent path,
  `rb` is validated one branch earlier in the same loop iteration or the gate has already set
  `status=1`, so it produces no green forgery. No re-ranking of the scope follows from it.
- **Deliberately not re-audited, because §3 puts them out of scope and this review agrees:**
  `resolve_base`'s candidate loop and its `base == HEAD` refusal (both armed, both explicitly out); the
  five other `GOV_DEFAULT_BRANCH` readers; the `--no-verify` git-level bypass; the `.unattended.conf`
  key set; adopter install-prefix work. The one place a scope boundary bit is D6 — the **driver's** own
  read is in neither list.
- **Not independently reproduced, and flagged as such rather than asserted:** the cross-worktree
  collision consequence in D8 (the shared-ref mechanism was verified with a real linked worktree; two
  concurrent bar runs colliding was not staged), and the TOCTOU window between D1's fetch and its
  `rev-parse` (mechanism reasoned, not exercised). Both are secondary to their rows' verified cores.

---

## Refuted (6 of 38)

Recorded so a future reader does not re-raise them: ids **11** (AC6 has no differential), **18** (the
manifest ratchet's re-stamp is unbudgeted), **19** (a prefix-free kit path in the protocol trips
`check-install-prefix.sh`), **22** (check 13's use of `rb` should re-rank the scope), **26** (the §10
reuse audit misreads `drift_report.py` and its ladder is a precedent for S2), **28** (`base-ref:`
violates the protocol's authored-facts rule). Each is summarised under *What the review did NOT find*
above. No confirmed finding was downgraded to unverified; the outstanding set is empty.
