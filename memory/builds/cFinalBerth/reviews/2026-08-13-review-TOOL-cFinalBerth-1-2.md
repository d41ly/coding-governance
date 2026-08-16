# Tier-2 code review — cFinalBerth units 1 + 2 (the two terminal phases)

**Serves:** diff-review TOOL-cFinalBerth-1 TOOL-cFinalBerth-2  <!-- inferred: code review of units 1 and 2 as built -->

**Verdict: CHANGES REQUESTED.** No blocker. Two HIGH, three MEDIUM, one LOW.

**Review shape.** Raw 13, confirmed 9, refuted 4, unverified 0, precision 0.69. The nine confirmed
raw findings collapse to **six distinct defects**: three lenses independently hit the `verb_close`
terminal-guard gap (raw 1, 6, 10) and two hit the `--preflight` witness rewrite (raw 3, 9). Merged
severity takes the higher of the duplicates. Every confirmed finding below was reproduced live in a
scratch fixture, not argued from reading; the repro is quoted in each **Evidence** block.

**Lens coverage.** Six bug-class lenses ran. Four returned surviving findings:
*two-answers-to-one-question* (F1, F2, F3), *second-implementation-is-not-a-second-opinion* (F4),
*heredoc-escape-reaches-the-regex* (F5, in its untrusted-text-reaches-a-pattern-matcher form), and
*fixture-passes-by-finding-nothing* (F6). Two returned nothing that survived the skeptic:
*assertion-between-two-derived-values* and *pin-copied-from-another-corpus*. That is reported rather
than omitted — a lens that found nothing is a coverage fact, and on this diff both are plausible
silences: the diff adds no new derived-vs-derived comparison and copies no pin.

**The one structural theme.** This diff is what first makes a run-state record *terminal*, and it
correctly adds "a terminal record cannot be moved" to `--phase` (`fail 26`) and `--abort`
(`fail 34`), and states it as binding protocol text
(`memory/guides/UNATTENDED-PROTOCOL.md:130` — "A run that is already terminal cannot be moved at
all"). It does not add it to the other two verbs that write a record. F1 and F2 are that single
omission seen from two sides, and F6 is the reason the bar cannot see it: every population the tests
walk is a hand-written literal. The lazy fix for all three is one derived loop (see the shared gate
suggestion under F6).

Security note: none of the six defects lets a run forge the anchor or the authorization comparison.
`observe_anchor` is intact and `--landed`'s ancestry refusal holds. What F1 and F2 break is the
*durability* of what the record says afterwards — the field leg check 15 judges can be re-pointed
through driver verbs alone, and the single-live counter can be silently re-armed or silently
disarmed. That is inside the boundary §9 already draws (a run with shell access can rewrite its own
file), but these paths need no shell — the shipped verbs do it and print OK.

---

## F1 — HIGH — `verb_close` is the fourth write site of the terminal invariant and the only writer without it

**Where.** `tools/unattended/unattended.sh:929` (`set_fact "$rel" phase LANDING`), inside
`verb_close` (`tools/unattended/unattended.sh:887`). The guard is missing at the natural insertion
point, `tools/unattended/unattended.sh:895`, right after the `[ -f "$rel" ]` check.
*Raw findings 1, 6, 10 — three lenses, merged.*

**Claim.** `--close <slug>` on a `LANDED` or `ABORTED` record exits 0, prints `close OK`, and rewrites
the phase back to the non-terminal `LANDING`.

**Evidence.** Reproduced end to end, three times independently, in scratch repos built like
`tools/unattended/unattended.test.sh`: `--preflight` → `--close` → push → `--landed`
(`phase: LANDED`, `witness: 70f188d9`) → `--close tRun` printed
`close OK — every declared DoD item met; phase LANDING` at rc 0, and the record then read `LANDING`.
The DoD loop passes in the landed state: `authorization-reachable` now takes the degenerate-base path
unit 2 (`f0666a5`) added, and `records-current`, `landed-via-lander`, `gates-green` plus both attested
lines are all still satisfied — so unit 2 is precisely what makes this reachable. Structurally,
`verb_close` reads `phase` nowhere and calls `is_terminal` nowhere, while `verb_phase`
(`unattended.sh:649-652`, `fail 26`) and `verb_abort` (`unattended.sh:750-753`, `fail 34`) both
refuse it.

**Why it matters.** Three consequences, all newly reachable:

1. A finished run re-enters `check_single_live` (`unattended.sh:430`) and leg check 7
   (`tools/unattended/check-unattended.sh:361`) — the exact counter this unit exists to free, and the
   exact harm `fail 26`'s own message names ("re-opening one returns it to the single-live counter
   every later run is measured against").
2. From the re-opened `LANDING`, `--landed` succeeds again and rewrites `witness` to the current HEAD
   — reproduced, witness moved from `70f188d9` to `c71d94aa`. The one field check 15 judges is
   re-pointed at a different commit through driver verbs alone, and the bar stays green because the
   new HEAD is also on the anchor's history.
3. `--close` on an `ABORTED` record likewise reaches `LANDING` at rc 0, so `--close` then `--landed`
   converts a recorded refusal into a recorded landing.

The bar does not catch any of it: with one run in the tree, check 7 sees one live record (`≤ 1`), and
check 9's degenerate clause cannot fire because the recorded base no longer equals HEAD once work
landed. It only surfaces when the *next* run starts. It also falsifies two shipped claims —
`memory/backlog/TOOL.md:81` ("a terminal record cannot re-open") and spec unit 1 S5 ("a record whose
CURRENT phase is terminal cannot be moved at all").

**Fix.** Insert the guard `verb_abort` already carries, after `unattended.sh:895` and *before* any DoD
evaluation or write:

```sh
cur=$(fact "$rel" phase)
if [ -n "$cur" ] && is_terminal "$cur"; then
  fail <n> "the run is already finished and closing it again would return it to the single-live counter every later run is measured against: $cur"
  return 1
fi
```

Reuse the sentence shape of `fail 34` so the writers refuse identically. A new `fail` needs a positive
arm in `unattended.test.sh` naming the full literal message, plus the matching `ARMS_FLOORS` bump for
`tools/unattended/unattended.sh` in `.memory-tree.conf` — the harness meta-gate
(`tools/memory-tree/check-arms.py`) reds otherwise.

**Left-shift gate.** See the shared suggestion under F6: derive the phase-writer set and loop it. A
table-driven arm over (writer × terminal record) would have failed on this diff as written.

---

## F2 — HIGH — `--preflight` preserves a terminal phase while unconditionally re-witnessing it, which reds the bar on a record the driver just wrote

**Where.** `tools/unattended/unattended.sh:833` (`set_fact "$rel" witness "$(GIT rev-parse HEAD)"`),
inside `verb_preflight` (`tools/unattended/unattended.sh:773`).
*Raw findings 3, 9 — two lenses, merged; merged severity HIGH.*

**Claim.** A second unattended run over a build whose `RUN.md` already reads `LANDED` gets
`preflight OK`, keeps `phase: LANDED`, and has its landing witness replaced by the current
feature-branch HEAD — a commit the remote never advertised.

**Evidence.** Reproduced twice. From a fresh unit branch over a record already at `LANDED`,
`--preflight tRun --keepalive-id k2` exited 0 with `preflight OK`; afterwards `phase: LANDED` and
`witness: a864fab` / `a24c4ab` (the unpushed tip, per fixture). The line immediately above is
*deliberately* conditional — `unattended.sh:832`, "ONLY when the file carries no phase yet", added
because preflight is the documented post-compaction re-entry verb — but the witness write on the next
line never got the same treatment, and before this diff no record could be terminal, so it could not
matter. `verb_preflight` has no `is_terminal` branch, and `check_single_live` explicitly skips
terminal records (`unattended.sh:430`), so nothing else stops it.

**Why it matters.**

1. Check 15's second half fires (`tools/unattended/check-unattended.sh:305`) — verified live, the leg
   printed exactly "a record claims LANDED with a witness that is not an ancestor of the anchor". The
   merge bar reds on a record the driver itself wrote, with the operator having knowingly edited
   nothing.
2. The new run is **unrecordable**: `--phase tRun BUILDING --witness …` refuses with `fail 26`
   ("the run is already finished") and `--landed` refuses because the phase is not `LANDING` — both
   verified. The only exit is hand-editing a file the kit calls generated.
3. `check_single_live` and leg check 7 count zero live runs, so the one-run-at-a-time guard is
   silently *off* for the new run.

**Fix.** Refuse the verb on a terminal record — re-preflighting a finished run is not a resume of
anything: after `rel=$(runmd_of "$slug")`, `fail <n> "the run-state file records a finished run and
preflight would keep its terminal phase while re-witnessing it against this branch: $cur"`, so a
follow-up run must archive or reset the record. If a refusal is judged too strong, the minimum is to
gate the witness write at `unattended.sh:833` exactly as the phase write above it is gated — that is
the half that reds the bar. Same arm + `ARMS_FLOORS` obligation as F1.

**Left-shift gate.** Shared with F1/F6: the derived writer-set loop covers `verb_preflight` too. Add
one leg-side arm asserting the invariant from the other end — no driver verb sequence leaves a record
that check 15 reds — since a leg that reds on driver output is the highest-cost failure mode here.

---

## F3 — MEDIUM — `--abort`'s refusal names the DoD *item*, but `dod_met` greps a differently-spelled *key*, so following the message verbatim blocks the abort forever

**Where.** message at `tools/unattended/unattended.sh:760` (`fail 35`, naming
`parked-decisions-surfaced`, item list at `unattended.sh:757`) vs the grep at
`tools/unattended/unattended.sh:955` (`grep -qE '^parked-surfaced: (yes|true)'`, case arm at
`unattended.sh:954`). *Raw finding 4.*

**Claim.** An agent that reads the refusal and records `parked-decisions-surfaced: yes` gets the
identical refusal on every retry.

**Evidence.** Reproduced on a fixture built from the kit's own harness: with
`parked-decisions-surfaced: yes` — the exact token `fail 35` names — written into `RUN.md`, `--abort`
returned the same refusal and left `phase: RUNNING`; appending `parked-surfaced: yes` produced
`phase ABORTED` immediately. The key is documented nowhere an agent reads: `scaffold_runmd` writes an
empty `## Run facts`, `tools/unattended/SKILL.template.md:83-86` and `:128-130` say only "Record them
honestly" while naming neither key, and `memory/guides/UNATTENDED-PROTOCOL.md:148` lists the *item*
name. The sibling item
`keepalive-reaped` uses key == item name, which makes the wrong inference the natural one, and the
wildcard branch at `unattended.sh:957` assumes item == key for every project-declared item — so
`parked-decisions-surfaced` is the lone exception, unannounced.

**Why it matters.** The two attested items are the only preconditions on the abort exit, and abort is
the exit that exists for a run which cannot otherwise finish. There is no override budget on
`--abort` to escape through (unlike `--close`), and nobody is watching. A run that cannot guess the
key stays non-terminal forever — the counter this unit was built to free.

**Fix.** One token, either direction. Preferred: rename the key at `unattended.sh:955` to
`^parked-decisions-surfaced:` so item and key are one string and the wildcard branch's assumption
holds universally (update `unattended.test.sh:430,512,696,708,866,877` and
`check-unattended.test.sh:165`). Cheaper: make the message name the line the driver reads —
`… : $item (record it as \`parked-surfaced: yes\`)`.

**Left-shift gate.** In `unattended.test.sh`, derive the agent-attested items from `DOD_CORE`
(`unattended.sh:78`) and assert, for each, that the literal `^<item>:` appears inside `dod_met` — one
loop, and it fails today. Same shape as this repo's derived install-prefix alternation.

---

## F4 — MEDIUM — check 15's second half runs on a witness its first half already rejected, so one record reds twice with contradictory sentences

**Where.** `tools/unattended/check-unattended.sh:302` (the `if [ "$ph" = LANDED ] && [ -n "$w" ]`
guard) and the comment at `:296-300`; first half at `:239`; `fail()` at `:40`. *Raw finding 7.*

**Claim.** The comment states a precondition the code does not establish, and the second half then
asserts something false about the record.

**Evidence.** Reproduced: a `LANDED` record with `witness: wf_3c665f96` prints **both**
"check 15 FAILED — … not sha-shaped" and "check 15 FAILED — … resolves to no commit in this history,
so the landing it claims cannot be located". `fail()` is `echo …; status=1` with no `continue` or
`break`, so the first half's refusal never stops the walk — yet `:297-298` reads "The first half above
already refused a witness that is not sha-shaped, so reaching this with an unjudgeable one is
impossible and no skip is needed."

**Why it matters.** The second sentence is wrong about the record — the value was never a sha — and it
sends the operator hunting a missing object. The second half is also a second implementation of the
resolvability question check 6 already owns (`check-unattended.sh:220-224`), so a genuinely
unresolvable sha at `LANDED` reds under two ordinals. This is the
*second-implementation-is-not-a-second-opinion* class: two checks answering one question, and the
comment defending the arrangement is the tell.

**Fix.** Have the first half set `shape_bad=1` and gate the second on it —
`if [ "$ph" = LANDED ] && [ -n "$w" ] && [ "${shape_bad:-0}" = 0 ]` — which is what the comment
already claims. Then drop the duplicate resolvability branch at `:303`, leaving check 6 the single
owner of "a sha-shaped witness that resolves to nothing", and correct the comment to say the skip is
*explicit* rather than unnecessary.

**Left-shift gate.** In `check-unattended.test.sh`, assert the *count*, not the presence: one bad
record must produce exactly one `check 15 FAILED` line. Counting arms catch double-fire; `hit`-style
substring arms never can.

---

## F5 — MEDIUM — an `--abort` reason that merely mentions the bypass flag permanently reds the bar

**Where.** `tools/unattended/unattended.sh:767` (`park "$rel" abort …`), `park()` at
`unattended.sh:966-967` (`printf … reason %s >> "$1"`, unsanitized), against leg check 11 at
`tools/unattended/check-unattended.sh:353` (`grep -qF -- "$BYPASS_BAN" "$f"`, whole file). This repo
declares `BYPASS_BAN` as `--no-verify`. *Raw finding 8.*

**Claim.** The operator's free text lands verbatim in the file the leg greps whole, so a truthful
abort reason wedges the merge bar.

**Evidence.** Reproduced:
`--abort tRun --reason "the gate stayed red and I refused to push with --no-verify"` returned rc 0,
and the very next leg run printed "check 11 FAILED — a run-state file names the declared bypass flag …
`--no-verify` in memory/builds/tRun/RUN.md".

**Why it matters.** `--reason` is *mandatory* on `--abort` (`fail 33`, `unattended.sh:746`), and an
abort is exactly the situation where an operator writes about a bypass flag they *declined* to use. So
the exit that exists for a run which cannot meet its obligations wedges the bar on the record the verb
was invoked to produce, and the only remedy is hand-editing a file the kit generates. `dod_met`'s
`landed-via-lander` grep (`unattended.sh:951`) has the identical whole-file shape, so a later `--close`
on that record fails too. The same free text reaches `park()` from `--close --override --reason`.

**Fix.** Refuse the collision at the verb rather than letting it surface as a bar failure two steps
later: in `verb_abort` and `verb_close`'s override path, refuse when `[ -n "$BYPASS_BAN" ]` and the
reason contains it, saying the gate greps this file for that literal and the reason must name it
differently. Narrowing check 11 to the fact lines instead would weaken a landing rule to buy prose
freedom — the wrong trade.

**Left-shift gate.** One arm that runs the driver and then the leg in sequence: any verb that exits 0
must leave a tree the leg passes. Every confirmed *driver-writes-what-the-leg-reds* defect here (F2,
F5) is caught by that single composed arm, which no current arm performs — the driver tests and the
leg tests never meet.

---

## F6 — LOW — the S10 arm's verb population is a hand-written literal, so it cannot enforce the invariant its own comment claims

**Where.** `tools/unattended/unattended.test.sh:654` (the `for v in --preflight … --abort` loop),
checking the header docstring (`unattended.sh:5-12`) and the usage line (`unattended.sh:991`). The
dispatch `case` it never consults is `unattended.sh:971-986` — the verb arm is `unattended.sh:974`.
*Raw finding 13.*

**Claim.** A verb added to dispatch and omitted from the docstring or usage line joins no check and
reds nothing — which is the drift S10 was written to stop, for "the next verb".

**Evidence.** Nothing derives the set from dispatch, the one place a verb must appear to function.
`check-unattended.sh` enumerates no verbs; `SKILL.template.md` and the rendered `SKILL.md` spell them
but `adopt-unattended.sh --check` only compares those to each other and to `.unattended.conf`, never
to the driver; the third spelling (the unknown-argument refusal, `unattended.test.sh:650`) is pinned
as a frozen literal, which reds if a verb is *added* to it and stays green if one is *omitted*. Same
shape as the historical drift S10 fixed — the usage line two verbs behind for two releases.

**Fix.** Derive the population from the dispatch `case` — extract the `--*` alternatives from the
`VERB="$1"` arm at `unattended.sh:974` plus the standalone `--plan`/`--phase` arms
(`unattended.sh:978-985`) — and assert the derived set is non-empty
before iterating, so a failed extraction fails rather than passing by finding nothing. That is the
convention already used for the derived install-prefix kit alternation and the derived govkit
population.

**Left-shift gate (shared with F1 and F2 — the one gate worth adding).** Extend the same derivation to
the *phase writers*: extract every site matching `set_fact "$rel" phase` from `unattended.sh`, assert
the extracted set is non-empty, and for each writer's verb drive a terminal record through it and
require a refusal. Written that way, this diff reds on F1 and F2 before review, and the *next* writer
is covered without anyone remembering. One loop retires three findings and the omission class behind
them.

---

## Refuted (4 raw), recorded so they are not re-found

Four raw findings did not survive the adversarial skeptic and are not reported as defects: the
skeptic showed each either mis-read the code or named a path the shipped guards already close. Two
lenses (*assertion-between-two-derived-values*, *pin-copied-from-another-corpus*) produced no
surviving finding at all. Precision 0.69 is in family with the prior review's 0.68 on the specs.

One inaccuracy inside a *confirmed* finding is worth recording: raw 3 called `--preflight` "the only
write path with no terminal-record guard". That is false — `verb_close` lacks one too (F1) — but it
does not touch the defect, its reachability or its impact, and F2 is reported on the reproduced
behaviour rather than the claim.

## What is right, and load-bearing

Stated so a later pass does not re-litigate it: `--landed` re-observes the anchor via
`observe_anchor` rather than reading a local ref, refuses unless HEAD is an ancestor of the tip the
remote advertises, and correctly does *not* call `check_branch` (the lander refuses off the default
branch, so a branch assertion here would contradict the tool it delegates to). Check 15's split into a
shape half outside the anchor loop and an ancestry half inside it is the right shape for the reason the
comment gives — folding them would gate the shape half on three preconditions it does not need and run
it zero times on a clone with no resolvable default branch. Unit 2's narrowing is sound and necessary:
the merge-base genuinely cannot distinguish "built nothing" from "fully landed", and asking the
recorded base instead is the only question that separates them.
