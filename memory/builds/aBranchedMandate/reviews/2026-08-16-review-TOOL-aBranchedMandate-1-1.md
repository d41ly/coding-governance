**Serves:** spec-audit TOOL-aBranchedMandate-1..3  <!-- inferred: its opening names the three specs it audits -->

## Verdict: BLOCKED

Spec-set audit (M4) at base 96141aed, over `TOOL-aBranchedMandate-1`, `TOOL-aBranchedMandate-2` and
`TOOL-aBranchedMandate-3`, plus the build README and the reproduction record under
`memory/builds/aBranchedMandate/build/`.

Eighteen confirmed defects, nine refuted, none left unverified. Three block: the causal premise the
whole build rests on does not reproduce on this node; unit 3's S6 respecifies a gate predicate as
EQUALITY, the shape this kit's own source records having been moved off after a reproduced wedge; and
unit 3 prices a leg-side widening as "defaulted off" when it is unconditional.

Findings carry the id from the audit batch in parentheses so each one can be traced back.

## CONFIRMED

### C1 (35, 36) — BLOCKER — the worktree-CRLF premise does not reproduce, and four AC depend on it

Lands in `memory/builds/aBranchedMandate/build/2026-08-16-build-aBranchedMandate-1-worktree-refusal-reproduction.md`
sections C1 and C2, the build README table at lines 25-29, and unit 2 §4 chain step 1 (line 51).

The specs claim `git worktree add` lands CRLF on paths `.gitattributes` pins `eol=lf`, and that C1
and C2 therefore fire "in any fresh worktree on this fleet". Measured on node `a` at the specs' own
BASE, `git worktree add --detach <tmp> 96141aed` produced CR=0 on all three pinned Skill renders;
`bash tools/check-wiring.sh --check` there printed `ok eol — every eol=lf-pinned .claude/ file is LF
in the worktree` and exited 0; and `bash tools/memory-recall/adopt-memory-recall.sh --check` exited 0
in the same worktree even though `tools/memory-recall/adopt-memory-recall.sh:149` is still a bare
`render | diff -q - "$SKILL"` with no CR normalisation. The four existing worktrees do hold CRLF
(122/89/136 CR bytes), so some other writer put it there after checkout, and no record names it.
`tools/check-wiring.sh:194` says only that a worktree checkout CAN land CRLF; the specs upgraded that
to always.

Two things fall out. Unit 2 §4's sub-head "Why a working-copy CRLF is always an artifact and never a
defect" derives "only ever comes from the checkout filter" from a premise measurement contradicts —
if the unidentified writer is a renderer or a tool, CRLF is a defect signal and S1 removes the exit
status that reports it. And four acceptance criteria are keyed to a fixture the named command does
not produce: unit 1 AC3 is already green at BASE with S1 reverted, which is the
`fixture-passes-by-finding-nothing` class; unit 1 AC5 ("its eol arm still reports the CRLF paths") is
unsatisfiable, because the arm prints `ok` there; unit 2 AC3 is already true; and unit 2 AC1's
fixture ("a fresh worktree whose only finding is CRLF on pinned Skill renders") cannot be created by
`git worktree add`.

Fix, in two parts. First, identify the writer and re-state the reproduction record's C1/C2 "fires
when" column and the README table to what is measured — the CRLF appears in long-lived worktrees, not
at checkout — then re-make unit 2 §4's artifact-versus-defect argument against the writer actually
found, or record it as UNVERIFIED per the TEMPLATE-SPEC writing rule. Second, re-phrase unit 1 AC3
and AC5 and unit 2 AC1 and AC3 against a CONSTRUCTED fixture: write CRLF into the render in a scratch
copy, then assert. That is the only fixture shape that fails when the unit is reverted.

### C2 (12, 31) — BLOCKER — S6's second clause is equality against a tip the run itself moves

Lands in unit 3 §2 S6 (lines 31-34) and its restatement in §4 "Why the leg must not read
`anchor-kind`" (lines 140-141).

S6 respecifies check 9 as "an ancestor of the advertised HEAD tip, **or** equal to a tip the remote
advertises for any ref", and §4 justifies clause 2 with "Equality against an advertised tip is
exactly 'this commit is published on the remote'". It is not: equality is a strict subset of
published. Under S1 the recorded BASE is pinned to the advertised branch tip; the run then commits
and pushes that same branch again — the act S7's own Skill precondition trains an operator to
perform — and the advertised tip moves past BASE. BASE is then neither an ancestor of the advertised
HEAD tip (it lives on the branch, which the default tip does not contain until landing) nor equal to
any advertised tip, so check 9 reds. It reds permanently after a branch delete or a squash-merge
landing, and the leg iterates every tracked run-state file with no phase guard on check 9
(`tools/unattended/check-unattended.sh:131,137,193`).

This is the wedge class the source records verbatim at `tools/unattended/check-unattended.sh:271-277`
("Equality wedged the bar permanently … a LANDED record red every later default-branch push.
Reproduced on an honest fixture with no attacker") and again in `trusted_base` at
`tools/unattended/unattended.sh:326-333`. §4 Migration addresses only pre-existing records, §5's
risks name only self-authorization and driver/leg drift, and AC6's red case ("a BASE on no advertised
history") is indistinguishable from the state a legitimate branch-anchored record decays into.

Fix: restate S6's clause 2 as REACHABILITY — the recorded BASE is an ancestor of some tip the remote
advertises — in both S6 and the §4 block quote, and add an acceptance criterion that pushes the
branch a second time after preflight and asserts the leg still passes over that record. §4 Migration
gains the durability case: a record whose branch tip has moved, been deleted, or been squash-merged.

### C3 (3, 37) — BLOCKER — the leg-side widening is unconditional, and §5 prices it as defaulted off

Lands in unit 3 §5 security (lines 222-226) against §2 S5 (lines 27-30) and S6 (lines 31-34).

S5 defaults only the DRIVER off. S6 rewrites check 9's predicate with no condition — it names
`anchor-kind` and a branch name as things the leg must not read, and `ANCHOR_SCOPE` is never
mentioned for the leg at all. Today `tools/unattended/check-unattended.sh:280` reds any recorded BASE
that is not an ancestor of the default-branch anchor. After S6, a record whose BASE is a tip the run
itself published passes check 9 in EVERY repo, including one that declares `default-branch` or
declares nothing, and check 13 (`:333-354`) then resolves the README at that same branch-published
BASE and passes too. So a hand-written record pinning any published tip — a tag included, since
clause 2 accepts a tip advertised for ANY ref — passes the leg in a clean clone, which protocol §9
names as the only thing that actually binds. AC6 tests only the refusal for a BASE on no advertised
history and AC7 only that old records still pass, so nothing observes the widening.

Fix: §5's security bullet and §4's "this is the whole price of the unit" (line 111) must price the
leg-side widening separately from the driver-side one, and say plainly that it applies to adopters
who never opt in. Gating clause 2 on `ANCHOR_SCOPE` is not a sufficient answer on its own — the conf
is a working-tree file the run can commit, so it sits inside the subject's reach exactly as
`anchor-kind` does — so either the pricing changes or the clause narrows to something a
non-opted-in repo still refuses. Add an AC that runs the leg in a `default-branch`-declaring repo
over a branch-anchored record and states the expected verdict.

### C4 (1, 23, 41) — HIGH — S1's fallback trigger has no implementable mechanism as placed

Lands in unit 3 §2 S1 (lines 15-19) and S3 (lines 23-24), against §4's Inventory rows for
`resolve_base` and `trusted_base` (lines 168-169).

S1 puts the fallback's trigger inside `resolve_base` — "when the build README does not resolve at the
default-branch merge-base" — but `resolve_base` (`tools/unattended/unattended.sh:251`) takes no
arguments, knows no slug, never reads a README, and returns its value on stdout through
`fresh=$(resolve_base)` at `:277`. Its caller `trusted_base` (`:274`) takes the run-state file, not
the slug. The only code that answers "does the build README resolve at this commit" is
`check_authorization` (`:458`), which S3 and the Inventory both declare unchanged and whose miss path
is `fail 6` (`:466`) — and `fail` (`:66-67`) sets the global `status=1`, which has no reset anywhere
in the file and which `verb_preflight:830` turns into a refusal. So the two readings a builder will
reach for are both broken: probing through `check_authorization` either latches the refusal or
vanishes into a command substitution, and a second inline `git show "$base:$rel"` is a second
spelling of the authorization predicate — the driver/leg divergence §5 names as this unit's
second-largest risk.

Fix: S1 states the trigger's mechanism explicitly — a SILENT `GIT show "$base:$rel" >/dev/null`
existence probe inside `resolve_base`, which writes nothing to the value channel and does not route
through `fail` — and states that `resolve_base` and `trusted_base` both gain the slug (or the
resolved README path) as a parameter. §4's Inventory rows for both functions change from an equality
tweak to a signature change plus the new probe, and §4's flow diagram (lines 90-99) is annotated to
say the "build README resolves at BASE?" test is that probe and not `check_authorization`.

### C5 (2) — HIGH — the anchor SELECTION is not stable for the life of a run

Lands in unit 3 §4 Inventory, the `trusted_base` row (line 169), and is absent from §2, §3 and §5.

`trusted_base` re-derives the anchor through `resolve_base` at every later verb and refuses at
`tools/unattended/unattended.sh:350` unless the RECORDED base is an ancestor of the freshly derived
one. Today that derivation is monotone, so the recorded base is always an ancestor. With a second
anchor whose selection turns on "does the README resolve at the merge-base", the selection can flip
mid-run: another node lands the build folder, the run merges origin into its branch, the FIRST anchor
now fires, `fresh` becomes a commit on the default branch, and the recorded branch tip — which
carries the run's own commits — is not an ancestor of it, so `fail 18` refuses. `--close` is the
verb the mandate requires, its `authorization-reachable` DoD item is explicitly not overridable
(`:932-936`), and `LANDING` is close-only, so the run wedges in a non-terminal phase with `--abort`
as its only exit. The Inventory's single line covers only equality on the branch path.

Fix: add a scope item stating that the anchor KIND is pinned at preflight and read from the record
for the life of the run — the recorded `anchor-kind` selects which derivation `trusted_base` performs
on every later verb — or, if the kind must not be read back (it is run-written), state the rule that
makes the derivation monotone across both anchors and how `fail 18` is kept reachable. Either way the
`trusted_base` Inventory row is rewritten to name the re-derivation, and §5's risks gain the flip
case.

### C6 (4) — HIGH — no acceptance criterion carries a branch-anchored run past `--preflight`

Lands in unit 3 §6 AC1-AC5 (lines 254-266) and §9's rev-2 line (line 334).

AC1 through AC5 all stop at `--preflight`; AC6-AC8 are the leg, AC9-AC12 are docs, arms and the
adopter. Nothing observes `--close`, `--landed`, `--resume` or `dod_met` on a branch-anchored run,
even though F4's resolution (§8, lines 322-327) ratified that such a run reaches the terminal landing
phase, and §4's Inventory asserts four downstream consumers behave correctly. §9 records "F4 changed
no scope item" as though that discharges it. The four Inventory rows marked "none" are claims about
code whose behaviour changes under S1 and S2 — `dod_met` re-derives through `trusted_base`, which
re-derives through the modified `resolve_base` — so C5 above ships with all twelve AC green.

Fix: add an acceptance criterion that carries a branch-anchored run through `--close` (specifically
the `authorization-reachable` DoD item) and `--landed`, and a second that resumes one after the build
folder has reached the default branch. This is the observation F4's resolution owed and did not get.

### C7 (29, 38, 39) — HIGH — check 9 is four assertions in one loop, and S6 names one

Lands in unit 3 §2 S6 (lines 31-34) and §4 "Inventory — every consumer of the authorization"
(lines 164-176).

`tools/unattended/check-unattended.sh:269-316` is a single `for b in "refs/remotes/origin/$d"
"refs/remotes/$d"` loop that carries four things: the not-a-commit refusal (`:278`), the
ancestor-of-anchor test S6 names (`:280`), the ancestor-of-HEAD test (`:282`), the phase-keyed
`rb != HEAD` refusal at `LANDING|LANDED|VERIFYING` (`:294-297`), and — nested inside the same loop —
check 15's SECOND HALF (`:298-316`), whose own comment says "This half is INSIDE the loop BECAUSE it
needs the anchor" and which compares the LANDED witness against that loop's `$b`. S6's replacement
predicate is an observation of the remote and needs no `$b`, so the loop cannot survive as written;
the Inventory titled "every consumer" lists only check 9 and check 13, and §4's Files-touched row for
the leg names only "check 9".

Deletion is not the risk — `tools/unattended/check-unattended.test.sh:355-382` arms check 15's second
half and `:331-352` the phase-keyed clause, so removing either reds a leg loudly. RE-ANCHORING is:
`ARMS_FLOORS` for this file counts branches and textual arms, so a `fail 15` left comparing against
the wrong anchor stays green, and the loss of ancestor-of-HEAD is a real unpriced weakening (clause 2
has no relation to this run's history, so a BASE published on a wholly unrelated ref satisfies it).

Fix: S6 states, item by item, the disposition of all four in-loop assertions plus check 15's second
half — which survive, and what anchor each one uses once the loop is gone. §4's Inventory gains a row
for check 15's second half and one for the phase-keyed clause. If ancestor-of-HEAD is dropped, §4's
price list says so.

### C8 (22, 32, 40) — HIGH — S6 gives an unguarded merge-bar leg an unspecified network dependency

Lands in unit 3 §2 S6 (lines 31-34) and §5 perf/scale (lines 227-229).

`tools/unattended/check-unattended.sh` makes zero network calls today — grep finds no `ls-remote` and
no `fetch`; the anchor comes from local refs at `:264-270`. Both of S6's clauses are stated against
the remote's advertisement, and AC8 forbids the leg from reading `anchor-kind`, so it cannot know
which records need the observation and must observe for every one. §5's "one per leg run, both only
on the fallback path" is therefore not reachable — the leg has one predicate, not a fallback path.
The leg `unattended kit gate` in `tools/gate-legs.json` carries NO `guard`, so it fires on every bar
invocation including a records-only diff, under `.githooks/pre-push`, and inside `dod_met
gates-green`. Nothing says what it does when the remote does not answer: fail-closed reds the bar on
every offline or credential-less run, including for two tracked run-state records that are already
LANDED; fail-open disarms the only BASE check on the bar, reachable by a run that removes its remote,
and matches the silent-skip shape the same check's comment refuses by name at `:258-259`. The
driver's `GIT_TERMINAL_PROMPT=0` discipline (`tools/unattended/unattended.sh:209`) has no specified
counterpart for the leg, which runs concurrently under the pre-push hook.

Fix: S6 states the offline behaviour explicitly and §5 moves the line out of perf into error states.
Add an acceptance criterion observing the leg with the remote unreachable. Carry the
`GIT_TERMINAL_PROMPT=0` pin into S6 as a stated requirement, not only into S1.

### C9 (25) — HIGH — a second ratified property is spent, and §10 asserts the opposite

Lands in unit 3 §4 "What is preserved, and what is spent" (lines 106-131) and §10 (line 351).

§4 prices exactly one property and calls it "the whole price of the unit". §10 states "The region and
roster comparisons inside it apply to the branch anchor unchanged." They do not.
`check_authorization` (`tools/unattended/unattended.sh:493-507`) takes the roster region at BASE and
compares it against the WORKING COPY's README. Under the default-branch anchor BASE is a commit the
run cannot advance without a gated landing, so the comparison really does catch a roster the run
rewrote mid-flight — protocol §1's fourth mechanical property ("Its ROSTER, when present, may not
move under the run … INTEGRITY"). Under the branch anchor BASE is a tip the run committed and
pushed, and `trusted_base` only requires the recorded base to be an ANCESTOR of the derived one
(`:350`), so the run re-satisfies the comparison against its own new bytes in two commands. The
property is satisfiable by construction on one of the two anchors.

Fix: §4's price list gains the roster-integrity property as a second spent item, §10's sentence is
corrected, and S8 is amended so protocol §1's roster claim is qualified per anchor rather than left
standing as an unconditional mechanical property. This one matters beyond the spec: the owner
accepted the self-authorization cost on a price list that says the roster comparison is untouched.

### C10 (14, 26, 44) — HIGH — S4's "name the repair command" has no source the kit may read

Lands in unit 2 §2 S4 (lines 26-29) and §6 AC4 (lines 166-167).

S4 and AC4 require check 4's refusal to name the repair command. Nothing the kit may read holds one:
`.unattended.conf` declares `WIRING_CHECK` and no repairing counterpart; protocol §8's key table
(`memory/guides/UNATTENDED-PROTOCOL.md:219-233`) has no repair key; and `check_wiring`'s allow-list
(`tools/unattended/unattended.sh:411-418`) refuses any `WIRING_CHECK` token outside
`--check|--dry-run|--verify|-n`, so the repair spelling cannot be derived from the declaration
either. `tools/check-wiring.sh` is a gov tool outside the copy-installed kit, so an adopter may not
have it. Unit 2 §3 puts protocol text OUT and §4's Files-touched lists neither the conf nor the
protocol, so no scope item can add a key. Decisively, `tools/unattended/unattended.test.sh:921`
already carries a source-level arm — `grep -nE 'check-wiring[^"]*--fix' "$SCRIPT"` with comments
excluded — that FAILS the driver self-test if the driver source spells that command. A builder
implementing S4 literally reds a leg unit 2's own §7 names.

Also unmentioned: `check_wiring` discards the declared check's own output with `>/dev/null 2>&1`
(`:419`), and that output already carries a remedy — `tools/check-wiring.sh:277` prints
`Fix: bash tools/check-wiring.sh --fix`.

Fix: restate S4 and AC4 as naming the DECLARED check plus surfacing the check's own output on
failure — the alternative §4 never considered — or add a declaration and move `WIRING_CHECK`'s
neighbours in protocol §8's key table, which then contradicts §3's non-goal and must be re-scoped.
Either way S4 stops requiring a literal the kit cannot hold.

### C11 (9, 18) — HIGH — unit 1 §5 asserts an empty-render guard that the edited file does not have

Lands in unit 1 §5, error/empty/loading states (lines 90-92), against §4's Inventory (lines 47-51).

§5 reads "the existing empty-render guard is untouched. This unit must not weaken it".
`tools/memory-recall/adopt-memory-recall.sh` has no such guard: its `--check` path is `[ -f "$SKILL"
]` (`:148`) then `render | diff -q - "$SKILL"` (`:149`), with no temp file and no `[ -s ]` test. The
guard being described is the SIBLING's, at `tools/unattended/adopt-unattended.sh:121` — one line
above the `tr -d '\r'` seam at `:122` that S1 tells the builder to copy. The consequence is live: a
builder told the guard exists and must not be weakened will port the sibling's `render > "$TMP"` plus
normalising-diff shape WITHOUT the `[ -s ]` line, turning a pipe that at least reds on a non-empty
Skill into a two-empty-file comparison that greens. §4's three-column Inventory omits the column that
would have caught it.

Fix: §5's line is rewritten to state the truth — this adopter has NO empty-render guard, its two
siblings do — and either S1 gains the guard as an explicit sub-item (the sibling's `[ -s "$TMP" ]`
refusal) or §3 gains it as a named non-goal with the gap recorded. §4's Inventory gains a fourth
column for the empty-render guard.

### C12 (6, 15, 24, 33, 42) — MED — the authored-fact count moves to eight over a list of ten

Lands in unit 3 §2 S4 (lines 25-26) and §4 Data model (lines 155-162), against
`memory/guides/UNATTENDED-PROTOCOL.md:59`.

Protocol §2 reads "**Authored**, carrying exactly seven facts and nothing else" and enumerates them
1..7, counting one anchor observation as THREE separately numbered facts (5 the ref name, 6 the tip
sha, 7 the endpoint URL). §4's Data model adds three keys — `anchor-kind`, `branch-ref`,
`branch-sha` — and marks `anchor-ref`/`anchor-sha`/`anchor-url` unchanged, so at the document's own
granularity the new count is ten. S4 says eight, and is the only place the number appears. The result
is a binding document stating a count its own enumeration contradicts, in both copies, which check 10
of the leg byte-compares against each other and therefore passes. The alternative resolution — record
`anchor-kind` alone and drop `branch-ref`/`branch-sha` — deletes the facts §4 calls the thing that
lets an off-machine verifier see which anchor a run leaned on.

There is also a fleet collision the build README's tripwire does not name:
`memory/builds/cBriefedPilot/README.md` states "**No eighth authored fact.** Protocol §2 pins the
authored region at exactly seven facts" as the premise for routing its own waiver through fact 3.

Fix: S4 states the real count and maps each new key to a numbered item, including how the two
conditional ones are admitted when absent (protocol §2's "nothing else" clause is unconditional
today). Add the authored-fact count to the build README's stop-and-reconsider list beside the kit
version literal.

### C13 (27, 34, 43) — MED — S4's placement rule inverts what `check-arms.py` actually does

Lands in unit 2 §2 S4 (lines 26-29) and §10 (lines 223-226).

S4 places the remedy before the interpolation "because a literal word after it lands inside the
branch signature `check-arms.py` matches", and §10 generalises it as "a branch's literal signature
ends before its first interpolation". `signature()` at `tools/memory-tree/check-arms.py:104-113`
splits the message on EVERY interpolation and returns `max(parts, key=len)` — the longest surviving
literal run. Check 4's current message (`tools/unattended/unattended.sh:420`) yields one ~88-character
run that `tools/unattended/unattended.test.sh:188` asserts verbatim. Appending a remedy AFTER
`$WIRING_CHECK` makes a second, shorter part and leaves that signature — and the existing arm —
intact; inserting it BEFORE lengthens the winning run and invalidates the arm, forcing S5's rewrite
and the `ARMS_FLOORS` re-measure. The rule as stated selects the placement that maximises churn while
claiming to avoid it. The real trap the driver's own comments describe (`check_slug:368-370`,
`stage_or_fail:546-548`) is different: a bare positional `$1` is not matched by `INTERP_RE` (`:55`)
and so stays inside the literal run.

Fix: S4 drops the placement rule or reverses it, and §10's sentence is corrected to name the
longest-run mechanism and the bare-positional trap. If the remedy lands after the interpolation, S5's
arm rewrite is no longer forced and the `ARMS_FLOORS` re-measure for this file becomes a check rather
than a change.

### C14 (17) — MED — S1 makes a ratified `fail 16` refusal unreachable on the branch path

Lands in unit 3 §4 Inventory, the `trusted_base` row (line 169), which states a no-op.

`merge-base --is-ancestor X X` is true, so `trusted_base`'s cross-check already accepts a base equal
to the derived one and needs no change. The change S1 actually forces is to `resolve_base`'s RETURN
CONTRACT: rc=2 means "the derived base equals HEAD" (`tools/unattended/unattended.sh:256`) and it is
the sole gate on BOTH `fail 16` branches at `:309-317` — "the record pins no BASE" and "the recorded
BASE equals HEAD, so this run built nothing on top of the anchor and has nothing to land", whose cost
is recorded at `:302-307` as owner-accepted fork F3. On the fallback path BASE is the advertised
branch tip, reached through rc=0 after the merge-base test has already returned a non-HEAD value, so
unless the builder deliberately re-tests `fresh == HEAD` after the fallback, both refusals stop
firing for every branch-anchored run. `check-arms.py` stays green because the branches remain
reachable on the default-branch path.

Fix: the `trusted_base` Inventory row is replaced with a `resolve_base` return-contract row stating
that rc=2 must be returned for the fallback tip as well when it equals HEAD, and §4's price list
either keeps the refusal or names it as a second spent guard.

### C15 (5) — MED — AC10 is green whether or not S8 is done

Lands in unit 3 §6 AC10 (lines 276-277) against §2 S8 (lines 37-38).

S8 is the unit's headline deliverable — §1's Goal is "state what it costs in the document that
already states what the first one costs". Its only acceptance criterion observes check 10 of the leg
(`tools/unattended/check-unattended.sh:370-386`), which compares `PROTOCOL.template.md` against
`memory/guides/UNATTENDED-PROTOCOL.md` only for agreement WITH EACH OTHER. That is green today, green
if S8 is skipped entirely, and green if both copies are edited with content omitting the
`ANCHOR_SCOPE` row or the cost sentence. No other gate in §7 reads the protocol's content, and
nothing asserts that a conf key the driver reads appears in §8's table — so the driver would read a
key the binding document never declares, which the protocol's own preamble bans.

Fix: AC10 gains a content observation — `ANCHOR_SCOPE` appears in §8's key table in both copies, and
§1 carries a fifth cost — in the shape AC9 already uses ("with S7's precondition present").

### C16 (16) — MED — the named backstop for the AGENTS.md check count does not read AGENTS.md

Lands in unit 3 §7's last bullet (lines 293-294) against §4's Files-touched row for `AGENTS.md`
(line 201).

§7 offers `bash tools/check-playbook-parity.sh` as the gate that "reds if a value the playbook STATES
stops equalling the source that owns it, which the leg's check count is". That gate opens only
`parallel-coding-governance.{template,customize,domain-rules}.md`
(`tools/check-playbook-parity.sh:30-32`) and carries exactly two declared pairs (`:105-108`, the
lens-array bound and the agent-cap matcher). It never reads `AGENTS.md`, where the count lives
(`AGENTS.md:136`, "fifteen checks"), and no pair covers a leg check count. §4's Files-touched row
already hedges the AGENTS.md edit ("if S6 adds an ordinal rather than changing one"), so the edit is
conditional and its stated backstop does not exist — while node `c`'s `cBriefedPilot` is concurrently
moving the same count.

Fix: strike the "which the leg's check count is" clause from §7, and make the `AGENTS.md` row in §4's
Files-touched unconditional with a stated value, or add a declared pair to
`tools/check-playbook-parity.sh` binding the charter's count to the leg — which is then its own scope
item.

### C17 (20) — LOW — unit 1 §4 measures the truncation window on the wrong file

Lands in unit 1 §4, the paragraph justifying S2 (line 57).

§4 says "the diff this script prints is truncated to twenty lines", under a heading that claims
"Measured in this worktree at BASE, by running each adopter's `--check`".
`tools/memory-recall/adopt-memory-recall.sh:154` is `render | diff -u "$SKILL" - | head -40`. Twenty
is the siblings' number (`tools/unattended/adopt-unattended.sh:125`,
`tools/drift-audit/adopt-drift-audit.sh:136`). S2's whole rationale — that a reader cannot
distinguish a line-ending diff from a content drift inside the window — is priced against the wrong
window, and a builder verifying S2 looks for a hunk shape that never appears.

Fix: correct the number to forty in §4. If the CONSTRUCTED fixture from C1 above is adopted, note
that a mutation must be placed past line 40 to discriminate.

### C18 (45) — LOW — AC8's stated conclusion is false as written

Lands in unit 3 §6 AC8 (lines 272-273).

AC8 greps the leg for `anchor-kind` and concludes it proves "the leg branches on nothing the run
wrote". The leg branches on run-written facts on every iteration: `ph=$(phase_of "$f")` used at
`tools/unattended/check-unattended.sh:207` and `:294`, `w=$(fact_of "$f" witness)` at `:239`, and
`rb=$(fact_of "$f" base)` at `:261` — the last being the very value checks 9 and 13 are about. The
leg's own comment concedes it at `:329-332`. The grep is a fine test; the conclusion is an overstated
boundary claim in the unit whose S8 rewrites the binding protocol's §9.

Fix: restate AC8 as what the grep buys — the leg gains no NEW run-written discriminator — and keep
that wording out of S8's protocol text.

## REFUTED

- (7) S10 has no acceptance criterion. Refuted: S10 states the rewrite-not-close requirement
  unambiguously and it is repeated in §3's non-goal and in F2's resolution; records-only scope items
  without a dedicated AC are this build's established shape, including unit 1's S4.
- (8) unit 1 S2 has no AC that fails without it. Refuted: AC2 exists to prove S1 does not
  over-normalise real drift, not to cover S2; S2 changes the legibility of a truncated print, which
  no consumer branches on.
- (10) unit 3 AC11 maps to no scope item. Refuted: the `ARMS_FLOORS` obligation appears in §4's
  Files-touched table, in AC11 and in §7's gate list, and the build README makes it binding on every
  unit. TEMPLATE-SPEC carries no rule that every AC trace to a numbered scope item.
- (11) no AC observes S5's out-of-set value. Refuted: S9 carries that arm explicitly ("a blank and a
  misspelled `ANCHOR_SCOPE` both keep the strict anchor"), and a scope item is DoD-verifiable.
- (13) the Inventory's omission of check 15 loses it silently. Refuted on the "silently" claim —
  `tools/unattended/check-unattended.test.sh:355-382` arms check 15's second half and would red
  loudly. The surviving re-anchoring risk is carried as C7.
- (19) unit 2 bundles two mechanisms. Refuted: the second half is a wording change to one existing
  `fail 4` branch plus its arm, not a separate document, gate, adopter or artifact in M2's sense, and
  §2/§4/§6 already split the halves.
- (21) a builder implementing S6 silently drops check 15 and AGENTS.md's count goes stale. Refuted:
  §3's non-goal and S10 prescribe leaving the other consumers of the derivation in place, the
  self-test arms make a deletion loud, and S6 changes an ordinal rather than adding one.
- (28) S3 misses a second arm and leaves the failed-repair branch undecided. Refuted: S2 states
  "Neither behaviour moves; only the exit status of `--check` does", and the failed-repair branch at
  `tools/check-wiring.sh:264-266` is inside the `--fix` block. The spaced-path arm at `:278-280` is
  entailed by S1 and reds loudly on the leg S3 already edits.
- (30) no route satisfies S1 and S3 together. Refuted: a silent existence probe is a third route, and
  a `status=1` set inside `fresh=$(resolve_base)` cannot propagate to the parent. The residual — that
  the spec never names the probe or the slug plumbing — is carried as C4.

## UNVERIFIED

None. Every finding in the batch carried a verdict, and the two blockers resting on a measurement
(C1) were re-measured during this pass, on node `a`, at BASE 96141aed.
