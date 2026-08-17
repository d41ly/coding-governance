**Serves:** spec-audit TOOL-cFinalBerth-1 TOOL-cFinalBerth-2  <!-- inferred: three lenses over BOTH Tier-2 specs, per the record's own opening paragraph -->

## Verdict: BLOCKED

Three lenses over the two Tier-2 specs and the build README, 34 raw findings, 23 confirmed and 11
refuted by the skeptic pass, precision 0.68. No lens was dead — each of the three returned findings,
and the three overlapped on nine defects, which is what let the duplicates be merged rather than
counted twice. After merging, 16 distinct confirmed findings remain: 2 BLOCKER, 8 HIGH, 4 MEDIUM,
2 LOW. Findings are grouped by the file they edit, because the fold is per-file, and ordered
BLOCKER → HIGH → MEDIUM → LOW inside each group. New acceptance-criterion numbers assume the whole
fold lands in one rev; renumber consistently if it is split.

---

# Unit 1 — `memory/builds/cFinalBerth/spec/2026-08-13-spec-cFinalBerth-1.md`

### F1 - BLOCKER - `--close` is not the only writer of `LANDING`, so `--landed`'s precondition does not gate the Definition of Done

*Seen by lenses 2 and 3 (raw 11, 23), merged.*

**Claim.** §4 "The transition, and why it is shaped this way" (spec lines 70-76) states that
"`--close` is the only writer of `LANDING`", and S1 (spec lines 13-16) rests its entire
DoD-integrity argument on that sentence. The sentence is false about the driver at this spec's base.
`--phase <slug> LANDING --witness <sha>` followed by this unit's `--landed <slug>` reaches `LANDED`
with `dod_met` never invoked, which reopens the exact hole the unit was written to avoid.

**Evidence.** `tools/unattended/unattended.sh:71` puts `LANDING` in `PHASES_CORE`;
`unattended.sh:72` restricts `PHASES_TERMINAL` to `LANDED ABORTED`; `is_terminal` at
`unattended.sh:80` tests membership of that set alone. In `verb_phase` the vocabulary case at
`unattended.sh:587` matches `LANDING`, the terminal refusal at `unattended.sh:594-597` does not
fire, and `set_fact "$rel" phase LANDING` runs at `unattended.sh:599`. `verb_close` writes `LANDING`
at `unattended.sh:762`, but it is one writer, not the only one. The skipped gate is `dod_met`
(`unattended.sh:769-792`), including `keepalive-reaped` (`unattended.sh:785-786`) and
`parked-decisions-surfaced` (`unattended.sh:787-788`) — the two items
`memory/builds/aStandingWrit/reviews/2026-08-11-review-TOOL-aStandingWrit-1-2.md:100-105` establishes are
enforced in no other place. Check 15 as specced does not close the path either: S4 grades witness
shape and ancestry, both satisfied by a genuinely published HEAD. Lens 3 reproduced the transition
in a throwaway fixture: `--phase tRun LANDED` refuses, `--phase tRun LANDING --witness <sha>` exits
0 and the record reads `phase: LANDING` with no DoD evaluated.

**Spec edit.** Add to §2:

> **S9** — **`LANDING` becomes close-only.** `--phase` refuses `LANDING` with its own named
> refusal, in the shape of the terminal refusal at `unattended.sh:594`, so `--close` is its only
> writer.

Correct the §4 sentence to say `--close` *becomes* the only writer of `LANDING` as part of this
unit, not that it already is. Add the branch to §4's Inventory as `new · --phase · the phase is
LANDING, which only --close may write`, add **AC12** — "When `--phase` is asked for `LANDING`, it
refuses naming `--close` as its sole producer, and the record is byte-identical afterwards" — and
fold the branch into S8's raised arms floor, which unit 2's S6 nets against. If instead
`--phase LANDING` is to stay legal, `--landed` must key on a close OUTCOME (a `closed-at` /
`close-witness` fact `--close` writes) rather than on the phase, per F2's left-shift recommendation
at `memory/builds/aStandingWrit/reviews/2026-08-11-review-TOOL-aStandingWrit-1-2.md:119-123`, and §4 must
say so.

### F2 - HIGH - S3 has no acceptance criterion, and no AC as written can distinguish a build that honours it

*Raw 3.*

**Claim.** S3 (spec lines 20-23) requires `--landed` not to call the branch guard. No AC observes
it, and the fixture every candidate AC would run in cannot tell the two states apart.

**Evidence.** `check_branch` refuses when the current branch IS the default one
(`tools/unattended/unattended.sh:356-362`), and landing happens there because the mandated lander
refuses to run anywhere else (`tools/push-main.sh:36-40`), so `--landed` is invoked at exactly the
moment the guard would fire. §6 carries no AC naming the branch its fixture stands on: AC3 (spec
lines 162-163) says only "at `LANDING` with HEAD published", and the driver's fixture works on a
feature branch — `git checkout -qf unit` at `tools/unattended/unattended.test.sh:322` — where
`check_branch` returns 0 whether or not it is called. §5's blanket "a positive arm per new refusal
branch" (spec lines 150-151) cannot reach an OMITTED guard, and `check-arms.py` only demands arms
for `fail` branches that exist. `memory/TEMPLATE-SPEC.md:108` requires every scope item to be
verifiable at DoD.

**Spec edit.** Add **AC13** — "When `--landed` runs at `LANDING` with the default branch checked
out, it writes `LANDED`; the arm stands on the default branch explicitly, because that is the only
state that distinguishes S3 from a branch guard nobody removed." Name AC13 in S3 as its
observation.

### F3 - HIGH - check 15's obligation is stated unconditionally, but its stated placement makes it conditional on three preconditions no AC names, and one half needs none of them

*Seen by lenses 1 and 3 (raw 4, 32), merged.*

**Claim.** S4 (spec lines 24-26) states check 15's obligation without qualification, while §10 (spec
line 213) places it inside check 9's anchor loop, where it can be silently skipped entirely.
AC8/AC9 name no precondition, so both arms are satisfiable on the one fixture that happens to have
an anchor, and AC9's sha-SHAPE half is gated by an anchor it does not need.

**Evidence.** The loop is reached only when the record carries a `base:` line
(`tools/unattended/check-unattended.sh:242-245` — an absent one is its own `fail 9`), only when a
default-branch name resolves (`check-unattended.sh:246-248`, from `GOV_DEFAULT_BRANCH` or
`refs/remotes/origin/HEAD`), and only when a candidate remote-tracking ref verifies
(`check-unattended.sh:251-252`, `|| continue`). The `if [ -n "$d" ]` block has no `else`, and the
`for b in …` loop falls off the end with no refusal, so on a clone with `origin/HEAD` unset and the
variable unset check 15 runs zero times, silently. That state is measured and ordinary for this
kit's own harness: `memory/builds/aMooredAnchor/reviews/2026-08-11-review-TOOL-aMooredAnchor-1-1.md` D7
records that the leg fixture never runs `git remote set-head` and that its only default-branch input
is the suite-level `export GOV_DEFAULT_BRANCH=main`, and D11 calls the `origin/HEAD`-absent state
ordinary. `memory/builds/aMooredAnchor/spec/2026-08-11-spec-aMooredAnchor-1.md:26-28` (its S4 and
AC6) specced named refusals for exactly those exits; the shipped file carries none, and rev-4's
carried-forward list at spec lines 337-340 omits S4. Unit 1's §3 discloses only the anchor
INDEPENDENCE limit owned by `TOOL-aStandingWrit-6`, which is about a FORGED tracking ref, not an
absent one — so the silence is owned by nobody.

**Spec edit.** Split S4: "the witness at `LANDED` is sha-shaped" is checked per run-state file,
OUTSIDE the anchor loop, beside check 5's presence test; only "the witness is an ancestor of the
anchor" goes inside check 9's loop. State in S4 that the ancestry half is silent when no `base:` is
recorded or no anchor ref resolves. Add that precondition to AC8 — "…in a fixture carrying a
recorded BASE and a resolvable remote-tracking anchor…". Add **AC14** — "When the leg runs over a
`LANDED` record in a fixture with `GOV_DEFAULT_BRANCH` unset and `refs/remotes/origin/HEAD` absent,
the sha-shape half of check 15 still fires." Add to §3: "check 15 inherits check 9's SILENT skip
where the anchor does not resolve; that is distinct from `TOOL-aStandingWrit-6`, which owns a forged
ref rather than an absent one."

### F4 - HIGH - `--abort` reaches a terminal phase enforcing only one of the two agent-attested DoD items

*Raw 12.*

**Claim.** S2 (spec lines 17-19) requires only the keepalive attestation before `ABORTED` is
written. §4's justification enumerates "the four machine-checked Definition-of-Done items" plus the
keepalive — five of six — and gives no reason for dropping the sixth. §4 in the same breath defines
the hole this unit exists not to reopen as those two items being enforced in exactly one place.

**Evidence.** `DOD_CORE` at `tools/unattended/unattended.sh:76` declares both
`keepalive-reaped:agent` and `parked-decisions-surfaced:agent`, and `dod_met` reads them at
`unattended.sh:785-788`. `memory/guides/UNATTENDED-PROTOCOL.md:136` declares
`parked-decisions-surfaced` a core, non-deletable item asserting that every parked entry reached the
wrap-up, and `memory/guides/BUILD-METHOD.md:208` derives the owner's only turn from those parked
entries. An abort is the maximal case of decisions the owner never saw, and as scoped it reaches
`ABORTED` with all of them unsurfaced. The ordering objection does not save it: `--close` demands
the same attestation before its own wrap-up, so the circularity is identical and was accepted there.

**Spec edit.** In S2, require BOTH agent-attested items before `--abort` writes `ABORTED`. If the
abort exit must not be blockable, say so explicitly in S2 and route the obligation somewhere
machine-visible — `--abort` writes `parked-surfaced: no` and check 15 fires on an `ABORTED` record
carrying it — and add **AC15** for whichever shape is chosen. Amend §4 paragraph 3 to name
`parked-decisions-surfaced` and state the reason it is or is not required, instead of enumerating
only the four machine items.

### F5 - HIGH - check 15's sha-shaped-witness requirement contradicts the BINDING protocol, and S6 does not amend the sentence it breaks

*Seen by lenses 2 and 3 (raw 13, 30), merged.*

**Claim.** S4 and AC9 (spec lines 173-174) make a non-sha witness at `LANDED` a refusal, while the
binding protocol declares that shape legal and the leg's own check 6 deliberately skips it. S6 (spec
lines 29-33) enumerates the protocol edits and the witness sentence is not among them.

**Evidence.** `memory/guides/UNATTENDED-PROTOCOL.md:114` states "**Every phase claim carries a
witness** — a sha, a tag, or a workflow id", with no phase-scoped narrowing, and §3 of the same
document (`UNATTENDED-PROTOCOL.md:99`) lists `LANDED` as an ordinary vocabulary member.
`tools/unattended/check-unattended.sh:219-224` implements exactly that permission and states the
discipline in its own comment: "not sha-shaped: unjudgeable, and skipping it is the discipline, not
an omission". The driver's own refusal repeats the three-form grammar at `unattended.sh:598`. So
check 6 and check 15 would answer the same question two ways one loop apart, and the leg would red a
record the binding contract permits.

**Spec edit.** Take one of two routes and say which. (a) Narrow S4 and AC9 to check 6's discipline —
check 15 asserts ancestry only when the witness is sha-shaped, and is silent on unjudgeable shapes.
(b) Extend S6 to amend `UNATTENDED-PROTOCOL.md` §3 with an explicit terminal narrowing — "a claim of
a TERMINAL phase carries a sha, because the ancestry assertion IS the claim" — record the narrowing
and its reason in §4, and add the protocol edit to §2 and to §4 Files touched. Do not leave the leg
and the binding document disagreeing.

### F6 - HIGH - `--phase` can un-finish a finished run: F2's third recommendation is dropped without a word

*Seen by lenses 1 and 3 (raw 8, 29), merged.*

**Claim.** Unit 1 cites review F2 as its root cause (§4 spec lines 70-76, §9 spec lines 195-198) and
builds two of its three recommendations. The third — refuse moving a run that is already terminal —
is neither built nor named as deferred, and this unit is the one that makes it reachable.

**Evidence.** `memory/builds/aStandingWrit/reviews/2026-08-11-review-TOOL-aStandingWrit-1-2.md:117` ends
the fix with "Also refuse moving a run that is already terminal." `verb_phase`
(`tools/unattended/unattended.sh:582-603`) validates the slug, the file's existence, vocabulary
membership, the terminality of the TARGET phase and witness presence — it never reads the record's
CURRENT phase. So `--phase <slug> BUILDING --witness <sha>` on a `LANDED` record succeeds and
returns the run to `check_single_live` (`unattended.sh:389-399`) and leg check 7
(`check-unattended.sh:328`), which is the counter §1 of this spec exists to free. Unit 1 adds the
symmetric refusal to `--abort` (§4 Inventory spec line 101, AC5) and leaves `--phase` exempt, while
S5 touches that same verb's refusal MESSAGE; §3 names no such non-goal. Before this unit no record
could be terminal, so the gap becomes reachable here for the first time.

**Spec edit.** Extend S5: "`--phase` also refuses when the record's CURRENT phase is terminal,
naming the phase it found." Add the row to §4's Inventory, add **AC16** — "When `--phase` runs
against a record at `LANDED`, it refuses naming the current phase, and the record is byte-identical
afterwards" — and include the branch in S8's raised arms floor. If it is deliberately deferred
instead, add to §3: "**Refusing `--phase` on an already-terminal record.** F2's third
recommendation, not built here because <reason>; filed as backlog row `TOOL-cFinalBerth-<n>`."

### F7 - HIGH - the record `--abort` writes reds the merge bar until the operator commits it, and no AC or gate item covers it

*Raw 25.*

**Claim.** Leg check 9 lists `ABORTED` among the phases at which a recorded BASE equal to HEAD is a
refusal. §4 argues in the same breath that an aborted run has no such obligation, without noticing
that the bar imposes one on the `ABORTED` record itself. Unit 1 makes that arm reachable for the
first time.

**Evidence.** `tools/unattended/check-unattended.sh:271-273` fires on
`LANDING|LANDED|ABORTED|VERIFYING` when `rb` equals `GIT rev-parse HEAD`. Every run's recorded base
is pinned at preflight through the degenerate path (`unattended.sh:276-283`, keyword passed at
`unattended.sh:629`), so a run that aborts before its first commit stages a record reading
`phase: ABORTED` with `base:` equal to HEAD, and check 9 fires. Lens 3 reproduced it on a fixture
whose only run-state file read `phase: ABORTED`. §7 (spec lines 182-185) lists the leg as a gate
this unit must be green under, and §6 checks a `LANDED` record against it (AC8, AC9) but never an
`ABORTED` one. The window is bounded — committing the record moves HEAD past the pinned base — but
it is real, reachable, and unaddressed.

**Spec edit.** Add to S4: "`ABORTED` is removed from check 9's work-claiming phase list at
`check-unattended.sh:272`; an aborted run authorizes no landing, so the clause buys nothing there."
Add **AC17** — "When the leg runs over an `ABORTED` record whose recorded BASE equals HEAD, check 9
is silent; the control is that `LANDING`, `LANDED` and `VERIFYING` still fire." If the list is to
stay as it is, say so in §4 and add an AC stating that an abort before the run's first commit reds
the bar until the record is committed.

### F8 - MEDIUM - the `--landed` refusal for an unobservable anchor has no behaviour, no AC and no arm, and the two precedents differ

*Raw 5.*

**Claim.** §4's Inventory (spec line 98) declares a `--landed` refusal for an unobservable anchor.
No AC, no design sentence and no arm says what the verb actually does there, and the two existing
anchor-consuming verbs behave differently.

**Evidence.** `--preflight` calls `observe_anchor || true` (`tools/unattended/unattended.sh:614`)
and lets the accumulated `status` refuse later with the observation's own message visible.
`--close` calls `observe_anchor >/dev/null 2>&1 || true` (`unattended.sh:726`), suppressing the
message entirely and reporting only the downstream unmet DoD item while still exiting 1 through
`exit "$status"` (`unattended.sh:823`). Unit 1 picks neither. §10 (spec line 208) says
`observe_anchor` is "reused unchanged", so no new `fail` branch lands and `check-arms.py` demands no
arm — §5's "a positive arm per new refusal branch" has nothing to attach to, and §6 carries no AC
(AC1 is the wrong phase, AC2 non-ancestor, AC3 success). The kit already carries a scar for this
exact message-channel class at `unattended.sh:266-270`, where `--close` "printed only the downstream
symptom and never said why".

**Spec edit.** State in S1 which shape `--landed` takes — "`observe_anchor`'s refusal is fatal and
its message is NOT suppressed: `observe_anchor || return 1`" — and add **AC18** — "When `--landed`
runs where the anchor cannot be observed, it refuses printing the observation's own refusal text,
and the record is byte-identical afterwards."

### F9 - MEDIUM - reusing `park` unchanged records an abort as a DoD OVERRIDE

*Seen by lenses 1 and 2 (raw 6, 18), merged.*

**Claim.** §4 Data model (spec lines 61-66) routes `--abort`'s reason through the existing `park`
helper and §10 (spec line 212) reuses it unchanged, without deciding what `park`'s item argument is
or noticing that its line is hardcoded to the override grammar. The record an aborted run leaves
claims an override that never happened, and AC7 cannot catch it.

**Evidence.** `park` writes one fixed shape —
`printf '\n%s override · item %s · reason %s\n'` — at `tools/unattended/unattended.sh:794-796`, takes
three arguments, and has exactly one caller today: the override branch of `verb_close` at
`unattended.sh:756`. An abort reason written through it lands as "override · item <invented> · reason
<abort reason>", and the builder must invent a value for `$2` for a verb that has no item. AC7 (spec
lines 169-170) asks only that "the reason appears in the parked region", which any spelling
satisfies. `memory/guides/BUILD-METHOD.md:208` derives the owner's open/parked row from parked
entries "plus any recorded DoD override", so the mislabel lands in the one turn the owner gets — and
it contradicts §4's own framing of `ABORTED` as "a recorded refusal" and §3's untouched DoD set.

**Spec edit.** Decide it in §4 Data model: give `park` a leading KIND argument
(`park <file> <kind> <item> <reason>`, with `--close` passing `override` and `--abort` passing
`abort`), name the one existing call site that must be updated, and add the change to §4's
Inventory. Add **AC19** — "When `--abort` runs with a reason, the parked region gains a dated line
naming the entry as an abort, and the word `override` does not appear in it."

### F10 - MEDIUM - neither documentation scope item has an acceptance criterion, and the only candidate names gates structurally unable to observe them

*Raw 7.*

**Claim.** S6 (spec lines 29-33) and S7 (spec lines 34-36) have no AC in §6. AC11's green bar (spec
lines 177-178) cannot observe either edit, so a builder who bumps the version marker in both
protocol copies and touches nothing else satisfies every AC in the section.

**Evidence.** Leg check 10 byte-compares the shipped and installed protocol after prefix
normalisation (`tools/unattended/check-unattended.sh:337-346`): it sees DRIFT between the pair,
never CONTENT, so two copies that both omit the new verbs are green. The skill wiring check compares
a render against its template plus the conf — the same property. Leg check 12
(`check-unattended.sh:352-372`) reads the kickoff engine for exactly three things: the literal
`Step 5b`, the literal READY prompt string, and a count of `^[0-9]+\. \*\*Step ` lines against
`KICKOFF_EXITS`. None of them can tell whether Step 5b names the abort verb. §5's "user docs" line
(spec line 154) restates the scope rather than supplying an observation.

**Spec edit.** Add **AC20** — "A grep for `--landed` and `--abort` in
`tools/unattended/PROTOCOL.template.md` and in `memory/guides/UNATTENDED-PROTOCOL.md` returns a hit
in each, in the §7 verb list and the §3 phase section." Add **AC21** — "A grep for `--abort` in the
kickoff engine returns a hit inside Step 5b, and check 12's exit count is unchanged."

### F11 - MEDIUM - the unit fixes one lying verb enumeration in the driver and leaves the other two naming a set that omits the verbs it adds

*Raw 19.*

**Claim.** S5 and AC10 (spec lines 27-28, 175-176) correct the `--phase` refusal message only. The
driver spells its verb set in three places, and after this unit two of them omit `--landed` and
`--abort` — including the one an operator sees when they mistype a verb. The unit CREATES the
omission; §3 names no such non-goal, and `unattended.sh` is already in Files touched.

**Evidence.** The header docstring lists six verbs
(`tools/unattended/unattended.sh:5-10`); the `fail 14` unknown-argument message lists six
(`unattended.sh:812`) and is pinned verbatim by an arm in `tools/unattended/unattended.test.sh`; the
`usage:` line lists FOUR (`unattended.sh:815` — `--plan` and `--phase` are already missing). This is
the class `memory/builds/aStandingWrit/reviews/2026-08-11-review-TOOL-aStandingWrit-1-2.md:451-470` (F11)
named and asked to be fixed in both the usage string and the header comment; only the header landed.

**Spec edit.** Add to §2:

> **S10** — **The driver's three verb enumerations are brought to one set.** The header docstring,
> the `usage:` line and the `fail 14` message all name `--landed` and `--abort`, and the arm pinning
> the `fail 14` text moves with them.

Extend AC10 to assert that the three enumerations list the same verbs.

### F12 - LOW - AC7 does not observe the staging S2 requires, although AC3 observes it for `--landed`

*Raw 9.*

**Claim.** S2 (spec lines 17-19) requires `--abort` to stage the run-state file. AC3 (spec line 163)
ends "and the file is staged"; AC7 (spec lines 169-170) observes the phase, the witness and the
parked reason and stops there. The asymmetry is inside one document.

**Evidence.** Staging is load-bearing enough in this driver to carry its own refusal —
`tools/unattended/unattended.sh:667`, whose message says the leg's whole per-run population is the
index — and it is the single row in `memory/project/unarmed-branches.txt`, so it is a known-unarmed
path. An abort is precisely the path where nobody is watching, so an unstaged terminal write is the
one most likely to be lost. `memory/TEMPLATE-SPEC.md:108` requires every scope item to be verifiable
at DoD, and nothing else in §6 or §7 reaches it.

**Spec edit.** Append "and the file is staged" to AC7, matching AC3.

### F13 - LOW - the charter's gate-suite entry is not in Files touched, and S4 does not say the check counts move with check 15

*Seen by lenses 1 and 2 (raw 10, 22); the second lens's broader framing was refuted — see the
Refuted section — and this is the half that survived.*

**Claim.** `AGENTS.md` carries a prose count of this leg's checks and is absent from §4 Files touched
(spec lines 116-121); S4 (spec lines 24-26) does not say either count moves with the new check.

**Evidence.** `tools/unattended/check-unattended.sh:2` reads "THIRTEEN checks over the tree" while
the file already numbers checks 1 through 14, and `AGENTS.md:127` repeats "thirteen checks"; check 15
puts both two behind. Nothing on the bar counts checks: the drift-audit's only charter signal,
`_charter_mentions_every_leg` in `tools/drift-audit/drift_signals.py`, matches leg SCRIPT PATHS from
`tools/gate-legs.json` against the gate-suite section and cannot see a stale count. The drift is
pre-existing, but this unit is the one that widens it while editing both carriers' subject.

**Spec edit.** Add to S4: "the leg's header count and the charter's gate-suite entry move with it —
both read thirteen against fourteen today." Add `AGENTS.md` to §4 Files touched.

---

# Unit 2 — `memory/builds/cFinalBerth/spec/2026-08-13-spec-cFinalBerth-2.md`

### F14 - BLOCKER - §8 signs an owner decision the owner was never asked, for a reversal of an owner-ratified refusal the spec never cites

*Raw 1.*

**Claim.** Unit 2 deletes a refusal that a prior spec scoped deliberately and the owner ratified by
name, cites none of the three records that established it, and then signs its only stated fork as an
owner decision about a different question. As written the spec classifies READY under M2 when its
real state is FORKED.

**Evidence.** The branch being deleted is `fail 16` in `trusted_base`
(`tools/unattended/unattended.sh:276-284`). Its own docstring says why it survives: "Still a
refusal: F2 ratified equality over ancestry, because relaxing a guard for a hazard nobody has
reproduced…" (`unattended.sh:244-248`). That F2 is
`memory/builds/aStandingWrit/spec/2026-08-11-spec-aStandingWrit-1.md:414-419` — "RESOLVED (owner,
2026-08-11): keep equality". The by-verb split is that spec's S3 (:44-46, "stays a refusal at
`--close` and in the gate leg"), and it carries a dedicated paired arm in
`tools/unattended/unattended.test.sh:392-402`. Unit 2 names none of them: §4 "Why the premise
expired" (spec lines 65-77) echoes the phrase "a hazard nobody reproduced" without citing F2,
`aStandingWrit`, or the arm. §8 (spec lines 170-176) then reads "RESOLVED (owner, 2026-08-13) by the
same decision that folded this unit into the build" for the fork "a run that built nothing may now
reach `LANDING`" — but that decision, at `memory/builds/cFinalBerth/README.md:71-72`, is a SCOPE
answer ("fold in the post-landing close") that says nothing about the relaxation.
`memory/TEMPLATE-SPEC.md:89-90` and `memory/guides/BUILD-METHOD.md:78` both forbid signing
`(owner, …)` for a decision the owner did not make, and the hygiene gate reads §8's first non-blank
line, so the misclassification is mechanical as well as substantive.

**Spec edit.** Rewrite §8 as an OPEN fork carrying a recommendation:

> **F1 — may the merge-base-equals-HEAD refusal at `--close` be deleted?** It was scoped by verb as
> `aStandingWrit` S3 and ratified as that spec's F2 (owner, 2026-08-11, "keep equality"), and
> `unattended.sh:244-248` cites that ratification as the reason it survives. This unit argues the
> premise expired because the anchor moved from a local ref to an observation; the property it
> bought survives at leg check 9. Recommendation: delete. Needs the owner.

Add the same three citations — `aStandingWrit` AC3, its S3, and its §8 F2 — to §4 "Why the premise
expired", and delete the `(owner, 2026-08-13)` attribution until the owner answers this question
rather than the scope one.

### F15 - HIGH - S2 states the security direction backwards and contradicts §5 and §8 of the same spec

*Seen by all three lenses (raw 2, 14, 27), merged.*

**Claim.** S2's closing sentence (spec lines 17-20) — that the change makes `--close` "strictly
stricter on the degenerate path than it is today, not looser" — is false about the caller it names.
It is the one sentence a reviewer of an authorization change reads first.

**Evidence.** The early return in `trusted_base` is reached only when the caller passes
`allow-degenerate` (`tools/unattended/unattended.sh:277-280`), and the only caller that does is
`verb_preflight` (`unattended.sh:629`). `--close` reaches `trusted_base` through `dod_met`'s
`authorization-reachable` arm with no second argument (`unattended.sh:777`), so today it lands on
`fail 16` at `unattended.sh:282` and refuses, 100% of the time — which is what this spec's own §4
reproduction table records (spec lines 54-58). After the change that path becomes a conditional
acceptance. Refusal is the strictest state, so the change is strictly stricter for `--preflight`,
which is the verb that actually took the skipped early return, and LOOSER for `--close`. §5 (spec
lines 141-142, "the change removes a refusal on the authorization path", "a run which built nothing
can now close") and §8 (spec lines 172-176) both say the opposite of S2.
`memory/TEMPLATE-SPEC.md:65` requires every claim about existing code to match source.

**Spec edit.** Replace S2's final clause with: "…and the same cross-check runs. `--preflight`, the
only caller that took the early return, therefore gains a check it used to skip; `--close` is LOOSER
on this path — an unconditional refusal becomes a conditional acceptance, bounded by leg check 9 as
§4 shows, and priced in §5 and §8." Amend §3's second bullet to read: "the item's ASSERTION is
unchanged; its VERDICT on the degenerate path changes from refuse to conditional pass."

---

# Cross-file — `memory/builds/cFinalBerth/README.md` and unit 1 §3

### F16 - HIGH - the owner-facing reason for folding unit 2 into this build is contradicted by unit 2's own scope, and rests on a premise that is false about the driver

*Raw 15.*

**Claim.** The README argues unit 2 is required to unwedge `aSealedCaravan`. Unit 2's own §3 rules
out running `--close` against that record at all, and S5 repairs it by hand, independently of
S1-S4 and of unit 1. The premise's second link is also false: `LANDING` is reachable through
`--phase` today. This is an M2 scope-axis disagreement between the overview and a sub-spec, and it
is the sentence the owner's F2 scope resolution rests on.

**Evidence.** `memory/builds/cFinalBerth/README.md:49-53` argues "reaching `LANDED` requires
reaching `LANDING`, which requires `--close`, which refuses post-landing". Unit 2 §3 (spec lines
37-40) rules out running `--close` against that record, and S5 (spec lines 29-30) moves it to
`LANDED` as a records repair — so S1-S4 are not what unwedges the record; S5 is, and S5 depends on
neither S1-S4 nor unit 1. On the second link, `LANDING` is in `PHASES_CORE`
(`tools/unattended/unattended.sh:71`) and not in `PHASES_TERMINAL` (`unattended.sh:72`), and
`verb_phase` refuses only terminal phases (`unattended.sh:594-597`), so `--phase` writes `LANDING`
today — which likewise falsifies unit 1 §3's "cannot reach `LANDING`" (unit 1 spec lines 43-45).
`memory/guides/BUILD-METHOD.md:52-57` requires the sub-specs and the overview to agree on scope, and
names the fix as a change to exactly one document.

**Spec edit.** In the README, rewrite the paragraph at lines 49-53 to the reason that survives: unit
2 exists because the kit cannot close ANY run whose HEAD is already published, and because the false
premise in the refusal text sits on the authorization path — not because it is the only way to
unwedge `aSealedCaravan`. State separately that S5 repairs that record directly and that the repair
is independent of S1-S4. In unit 1 §3, change "is at `BUILDING` and cannot reach `LANDING`" to "is
at `BUILDING`, and this unit does not move it."

---

## Refuted

- **raw 16 — unit 1 S1 "sole producer" vs unit 2 S5's hand repair.** "Sole producer" is a claim
  about the driver's verb set, not about tracked bytes; unit 1 §3 and unit 2 §3/S5 acknowledge the
  seam in both directions, and check 15 grades the repaired record like any other.
- **raw 17 and raw 33 (same claim, two lenses) — S3's "correct for every other verb" is false
  because only `--preflight` calls the guard.** The call-site fact is right
  (`unattended.sh:356`, called only at `:616`) but does not falsify a normative statement about
  whether the guard's semantics fit; shell has no inheritance to suppress, and the proposed remedy
  is a prose preference.
- **raw 20 — the build raises the arms floor in unit 1 and lowers it in unit 2.**
  `check-arms.py:283-285` explicitly permits lowering a floor "in a commit that says why", unit 2 S6
  states the reason, and neither spec spells a numeric value, so there is no interface disagreement.
- **raw 21 — S8's "two bumps behind" is wrong; the marker is one bump behind.** The base facts hold
  (`PROTOCOL.template.md:1` and `UNATTENDED-PROTOCOL.md:1` read `unattended@1.2` against
  `KIT_UNATTENDED_VERSION=1.3`), but 1.2 against the 1.4 this unit writes is two bumps under a
  defensible reading of the sentence.
- **raw 22 — the leg header count and `AGENTS.md` are outside Files touched.** Files touched lists
  FILES, and `check-unattended.sh` is listed. The surviving half — `AGENTS.md` absent, and S4 silent
  on the counts — is folded into **F13**.
- **raw 24 — the property the deleted refusal protected does not survive at check 9 because the
  records commit silences it.** The deleted guard has the identical window: `fail 16` fires only
  while the run has committed nothing beyond published history. `--close` also evaluates
  `gates-green` (`unattended.sh:779`) before it writes `LANDING`, so the bar sees `rb == HEAD` at the
  decision point.
- **raw 26 — the spec never says which agent-attested item `--abort` drops.** §4 says "That SINGLE
  attestation is required" against a six-item set, which identifies it. What is missing is one
  sentence of rationale — a prose completeness preference. The substantive half is **F4**.
- **raw 28 — unit 2's history is contradicted by the commit order.** The finding dated the guard by
  `git log -S'allow-degenerate'`, which dates the preflight relaxation, not the refusal. The refusal
  text first appears in `b94818b`, which is an ancestor of `a2d929e` ("the anchor becomes an
  observation"), so §4's history is true as written. Its citation-hygiene residue is **F14**.
- **raw 31 — unit 1 silently declines F2's left-shift `closed-at` gate.** §4 Data model states the
  decision plainly ("No new authored key… nothing new is observed"), and a `closed-at` fact would be
  run-written exactly as `phase:` is — the one-line-escape objection the spec itself records.
- **raw 34 — AC10 and AC4's "a grep returns nothing" walk into the
  `absence-assertion-over-whole-file-text` class.** That class is about a SHIPPED gate that reds
  forever on its own remedy comment; both ACs are one-time acceptance greps over a diff whose comment
  wording the builder controls.

## Unverified

none — every raw finding received a skeptic verdict.
