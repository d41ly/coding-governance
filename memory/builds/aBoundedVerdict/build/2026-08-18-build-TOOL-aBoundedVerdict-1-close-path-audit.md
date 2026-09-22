**Serves:** research TOOL-aBoundedVerdict-1

# Close-path audit — `--close`, its Definition of Done, and the review loop that feeds it

Subject: the unattended-run kit's close path in this worktree — `tools/unattended/unattended.sh`,
`tools/unattended/check-unattended.sh`, `tools/unattended/unattended.test.sh`,
`tools/unattended/SKILL.template.md`, `tools/unattended/PROTOCOL.template.md`,
`memory/guides/UNATTENDED-PROTOCOL.md`, `memory/guides/BUILD-METHOD.md`,
`tools/workflows/tier2-review.js`, and the record corpus they act on (49 build folders, 7 tracked
run-state files, 90 review records). Five lenses, five adversarial skeptic batches, one synthesis.
Throughout, an unqualified `unattended.sh:N` means `tools/unattended/unattended.sh:N` and
`check-unattended.sh:N` means `tools/unattended/check-unattended.sh:N`.

## Verdict

The close path is **structurally sound with local defects, plus one systemic problem** — and the
systemic one is what turns each local defect into the stall the owner reports. The architecture
holds: verbs are single-purpose, phases are a closed vocabulary, the DoD is a declaration rather
than a hardcoded list, every refusal carries a numbered ordinal, and all three blockers below are
one-line fixes (a `grep` filter at `unattended.sh:913`, a deleted redirect at `unattended.sh:1387`,
a bound on `unattended.sh:240`). What is systemic is the **message channel**: `--close` discards
refusals at three separate call sites (`unattended.sh:1387`, and the tail of `unattended.sh:1457`),
and only 2 of the 8 arms of `dod_met` ever populate `DOD_OUT` — so a blocked close reports *which
item* is unmet and almost never *why*. That silence is not an oversight the file is unaware of: it
is documented as a known scar twice, at `unattended.sh:1048-1050` ("`--close` suppresses it and
reports only the downstream unmet item") and at `unattended.sh:1461-1462` ("TOOL-aBranchedMandate-2
fixed that call site and did not grep for this one"). One class defect sits beside it: "a unit row"
is spelled three times in one file (`unattended.sh:913`, `:1078`, `:1339`), and all three spellings
are wrong in the same way.

## Confirmed findings

| id | class | severity | ref | what breaks | smallest fix |
|---|---|---|---|---|---|
| 1·8·27 | unsatisfiable | blocker | `unattended.sh:913` · `:1503` | `unit_rows`' `^\| \[` also matches the Records table, so `nonterminal_units` counts every review and journal record as an unfinished unit; `build-complete` fails on any build holding a record, and `closing-review-recorded` demands one — 49/49 corpus builds fail one or the other | filter to the Units table by link target: `grep -E '^\| \[[^]]*\]\(spec/'`, then route `:1078` and `:1339` through the same helper |
| 15·9·28 | silent | blocker | `unattended.sh:1387` · `:1404` | `>/dev/null 2>&1` destroys all eight `observe_anchor` refusals (checks 22-30); the only surviving output is the bare `authorization-reachable`, and `fail 21` forbids overriding that one item — a wedge with no stated cause and no forward move | drop the redirect: `observe_anchor \|\| true`, the form `--landed` (`:1063`) and `--preflight` (`:1181`) already use |
| 14·29·6 | unbounded | blocker | `unattended.sh:1387` · `:240` · `:298` | no transport bound anywhere in the kit and both streams discarded, so `--close`'s first substantive act can block indefinitely having printed zero bytes; up to three `ls-remote` calls per close under `ANCHOR_SCOPE=published`, plus two more inside the leg the bar runs | bound both call sites (`timeout`, or `http.lowSpeed*` + `ssh -o ConnectTimeout`) and echo one progress line before `:1387` |
| 4·10·16 | silent | high | `unattended.sh:1457` | the same redirect binds only to `check_authorization`, discarding its six refusals (`fail 6`, `fail 7`, four × `fail 20`) while `trusted_base`'s still print — the silenced set is exactly the operator-repairable half | delete `>/dev/null 2>&1` from `:1457` |
| 2 | vacuous | high | `unattended.test.sh:608` · `:677` | no arm in the suite has `build-complete` and `closing-review-recorded` both met; each item's green control overrides the other, so the control written to catch "`build-complete` stopped being satisfiable" is disarmed by its own override | one arm with a tracked `reviews/` record, a re-rendered fixture README, and no `--override` at all |
| 5 | silent | high | `unattended.sh:1499-1503` | `DOD_OUT=""` precedes the four-term AND chain, so all four failures (roster names no id · a roster id has no spec · the region is empty · a unit row is non-terminal) print one identical sentence | evaluate the four terms sequentially, each setting `DOD_OUT` from the substitution already computed |
| 3 | silent | high | `unattended.sh:1415` vs `:1535` | `parked-decisions-surfaced` is read from a line spelled `parked-surfaced:`, and the close-path refusal names only the item — so the operator writes a key nothing reads and re-runs forever | reuse `--abort`'s mapping (`:1127`) at `:1415`, or widen the grep at `:1535` to both spellings |
| 11 | other | high | `unattended.sh:1442` | `--close` is the only phase writer that skips `stage_or_fail`, so `LANDING` and the parked override rows sit outside the index the leg's population is read from, and `--landed`'s `check_clean` (`:1062`) refuses on `--close`'s own unstaged write with a message blaming the tree | `stage_or_fail "$rel" \|\| return 1` after `:1442`, as the other four writers do |
| 17 | unsatisfiable | high | `unattended.sh:231-235` | check 25 compares URL *strings*, so a fetch-https/push-ssh clone (`remote.*.pushurl`, `url.*.pushInsteadOf`) can never satisfy `authorization-reachable` — the one item with no override | compare normalised host+path; keep a literal mismatch as a warning, not a `return 1` |
| 21 | vacuous | high | `unattended.sh:1529-1531` | `closing-review-recorded` is a 7-hex substring test against the pinned BASE, but the fold-scoped round `M8` mandates names a *fold* commit — so the honest closing round fails it; 3 of 7 tracked builds have no matching record | accept any sha in `BASE..HEAD`, and require the matching record's `**Serves:**` to say `diff-review` |
| 22 | silent | high | `tier2-review.js:290` · `:349-356` | lens and skeptic deaths are counted, synth death is not: with `synth === null` the run returns `note:'complete'`, `report:null`, and every confirmed finding is lost with nothing logged | mirror the S1/S2 guard at the synth — set an `UNVERIFIED:` note and `log()` the confirmed list |
| 23 | unbounded | high | `tier2-review.js:71` · `:156` · `:69` | `base` is the only narrowing knob and reaches every lens verbatim; there is no round number and no prior-findings parameter, and `byDesign` is supplied by no caller in the tree, so round N re-reads the whole cumulative diff | add `priorFindings` to `args` and print it beside `byDesign`; give `BUILD-METHOD.md:187-190` a fix-round spelling with `base` = round N-1's end |
| 12 | other | medium | `unattended.sh:1387` · `:1390` | `refuse_if_terminal` is evaluated *after* the network call, so `--close` on an already-terminal record pays every round-trip before a refusal that needs no network | move `:1390` above `:1387` |
| 19 | unbounded | medium | `check-unattended.sh:211-212` · `unattended.sh:240` | `GIT_TERMINAL_PROMPT=0` bounds git's own prompt, not the configured helper — this node has `credential.helper=manager` with `credential.interactive` and `guiPrompt` unset — while the leg's comment claims the variable makes a credential prompt refuse rather than hang | add `credential.interactive=never` / an askpass at `:240`, `:298` and in the leg; correct the comment |
| 13 | other | medium | `unattended.sh:1533` · `:1535` | neither agent-attested key has a writer anywhere in the kit, so `--abort` — the documented sole exit from a wedged run — is reachable only by hand-editing the record the kit calls generated | an `--attest <item>` verb routing through `set_fact` + `stage_or_fail`, refusing a non-`agent` item |
| 20 | other | medium | `unattended.sh:1435` | the override `park` is the one caller with no bypass-flag guard (cf. `:629`, `:1113`, `:1578`), so a truthful `--reason` spelling `--no-verify` reds leg check 11 permanently on a record no verb rewrites | copy the existing guard into the validation loop at `:1393-1408`, before anything is written |
| 7 | vacuous | medium | `unattended.sh:1480-1481` | `landed-via-lander` is two conf-non-empty tests plus a grep `check-unattended.sh:452` already ran inside the same close, and nothing joins it to the lander actually used | give it an observation only the driver can make at `--landed`, or let check 11 own the predicate alone |
| 18 | other | medium | `unattended.sh:298` · `:319` | `\|\| return 2` collapses transport failure (128) into "answered, no matching ref" (2), so a network fault tells the operator to push a branch that is already pushed; `observe_anchor:241` splits the same pair correctly | keep the status and add a transport arm to `emit_branch_fail` |
| 30 | other | medium | `memory/guides/UNATTENDED-PROTOCOL.md:217` | §4's `records-current` Asserts cell still describes the retired fresh-render semantics and unit status headers the driver never reads; check 10 byte-diffs the shipped/installed pair and check 16 joins item *names* only, so both are green over it | rewrite the cell in both copies to the implemented invariant, and qualify `build-complete`'s clause with which file's region |
| 31 | vacuous | medium | `check-unattended.sh:322` | check 8 exempts `LANDED`/`ABORTED` and all seven tracked records are terminal, so it has zero subjects — while three of them carry 1280, 3082 and 4032 bytes of exactly the copied unit list it exists to refuse | drop the terminal exemption, or state in a comment why retired bytes are exempt |
| 24 | unsatisfiable | medium | `memory/guides/BUILD-METHOD.md:100-105` · `:214` | the verdict corpus is unparseable — 18 distinct `## Verdict` lines, 5 leading tokens, zero literal `## Verdict: CLEAN`, 32 of 90 records with no verdict line, 2 where it is a section heading — and M9 derives the wrap-up from that line | one token from a closed set as the record's first line, added to HYGIENE check 5's grammar for `diff-review`/`spec-audit` records |
| 25 | unsatisfiable | medium | `memory/builds/aBoundedVerdict/spec/2026-08-16-spec-TOOL-aBoundedVerdict-1.md:51-53` | S8's "when the remaining units do not depend on it" is vacuously true at the closing review, so the literal reading lands a BLOCKED diff and the intended one aborts without landing | delete S8 in the rev that implements the design pass; state the closing-round disposition as a positive predicate |
| 33 | other | medium | `tools/unattended/SKILL.template.md:172` | the artifact an agent reads at close time names no non-overridable item, and protocol §4's override paragraph carves out only the two attested ones; the sole statement of the carve-out is §1 line 71, scoped there to run *start* | one sentence in §4 and in the Skill's Close section |
| 26 | silent | low | `unattended.sh:1529-1531` | `closing-review-recorded` sets no `DOD_OUT`, so its four failure modes (no record · untracked record · wrong sha · no pinned base) are one indistinguishable line — and the likeliest, an unstaged review, is unguessable because the arm reads `--cached` | one `DOD_OUT` assignment in the arm, cleared on success as `build-complete` already does |

## The blockers

**1·8·27 — the unit-row selector.** `gen_build_index.py:604` emits a second table inside the same
`gen:build-index` marker pair, whose second cell is a *Kind* (`journal`, `spec-audit`,
`diff-review`, `—`) and therefore can never match `| CLOSED |`. Replaying the driver's own
`region`/`unit_rows`/`nonterminal_units` over the corpus: 297 rows match `^| [`, 124 of them link
into `build/`, `reviews/` or `prompts/`; every build with ≥1 tracked review has a non-empty
`nonterminal_units` (aBranchedMandate 7, aSealedCaravan 5, cBriefedPilot 5, dClosedLexicon 10), and
the six builds with an empty one are exactly the six with zero reviews — which fail
`closing-review-recorded` instead. The `spec/` link discriminator drops all 124 record rows and
keeps all 173 unit rows. Two secondary consequences: aBranchedMandate reached LANDED only because
its records were not yet committed at close time, so its README then carried no Records table; and
`--status`/`--resume` (`unattended.sh:1339`) prints a build journal as the "next unit" — for
aBranchedMandate, `2026-08-16-build-TOOL-aBranchedMandate-3-repro-c3.sh`. The comment at
`unattended.sh:911-912` records that pointing these helpers at the wrong region *already* made
`build-complete` unsatisfiable once, caught by its own green control; that control is now disarmed
(finding 2). The only exit is `--override build-complete` — the run authorizing itself past the one
item that means "the build is done".

**15·9·28 — the discarded anchor observation.** `fail()` is `echo` to stdout
(`unattended.sh:76`), so the redirect destroys checks 22 (injected git config), 23 (replace/graft
lever), 24 (remote count ≠ 1), 25 (fetch/push URL split), 27 (remote did not answer), 28 (no HEAD
symref), 29 (`GOV_DEFAULT_BRANCH` mismatch) and 30 (advertised tip absent locally) — eight, not
nine; there is no check 26. All eight return before `ASHA` is assigned, so the
`authorization-reachable` arm short-circuits on `[ -n "$ASHA" ]` and no `DOD_OUT` is set.
Reproduced on a throwaway fixture (bare origin with a dangling HEAD): shipped `--close` printed only
`check 13 FAILED — … authorization-reachable`; with the single redirect removed it printed
`check 28 FAILED — the remote answered but advertised no HEAD symref …` first. The comment at
`unattended.sh:1385-1386` justifies the `|| true` (the refusals are not fatal to `--close`) and says
nothing about the suppression, so the silence is undocumented at that site rather than deliberate.

**14·29·6 — the unbounded handshake.** `grep -rn 'timeout|lowSpeed|ConnectTimeout|GIT_HTTP|GIT_SSH'`
over `tools/unattended/` returns nothing outside the test files, and git has no `--timeout`;
`GIT_TERMINAL_PROMPT=0` bounds a credential prompt, not a transport. Measured against a blackhole IP
in a scratch repo, `observe_anchor`'s call ran until `timeout 8` killed it with no output. Under
this repo's declared `ANCHOR_SCOPE="published"` two further calls are reachable in one close —
`resolve_base` → `branch_tip_quiet` (`unattended.sh:298`) and `trusted_base`'s `_tb_alt`
(`unattended.sh:497`, reaching the same line 298) — and `check-unattended.sh:228` and `:230` add two
more inside `$GATE_CMD`, where under `.githooks/pre-push` a stall hangs the push rather than
reddening it. Two corrections to the raised form: `--close` opens with **one** network round-trip,
not two (the `ls-remote --get-url` at `unattended.sh:231` is offline by design, measured 0s against
the same unreachable URL), and `observe_anchor` is the third statement of `verb_close`, not the
first. Findings 12 and 14 are the same defect; 12 adds the independently fixable ordering point.

## The highs

**4·10·16.** A redirection on an `&&` list binds only to its last simple command — re-observed in a
scratch script — which is why the failure looks intermittent: `trusted_base`'s `fail 16`
(`unattended.sh:440`, `:444`, `:452`) and `fail 18` reach the operator on the same line where
`check_authorization`'s six do not. Reproduced: a fixture whose pinned BASE predates the build
folder printed only the item name as shipped, and `check 6 FAILED — no build README at the pinned
BASE … <sha>:memory/builds/fixbuild/README.md` with the redirect removed. `trusted_base`'s own
header comment (`unattended.sh:383-386`) says it was rebuilt to return via a global *because* a
captured refusal made `--close` print only the downstream symptom — and the very next call in the
chain re-introduces it.

**2.** `hit "$out" "close OK"` appears at `unattended.test.sh:466`, `:555`, `:566`, `:608`, `:653`,
`:677` and `:691`; four override both items, `:608` overrides `closing-review-recorded`, and `:677`
and `:691` carry `$crbc` (`:666`), which overrides `build-complete`. The fixture README template
(`:55-75`) emits only a Units table and `cropen()` (`:668-670`) writes `reviews/r1.md` without
re-rendering, so the record-row class is unreachable by construction: the suite passes by finding
nothing, and finding 1 rode the bar green.

**5.** Only the roster-region term (`unattended.sh:1496`) names itself — the shape
TOOL-aBranchedMandate-13 introduced and closed. The four surviving terms already compute their
values in command substitutions that are thrown away; only the messages are missing. This is why
the failing term is invisible, and why `--override build-complete` is the natural next move.

**3.** `--abort` carries the mapping (`unattended.sh:1127`) and a message that says "Write the
RECORD KEY, which is not always the item name" (`:1128`), with a comment at `:1124-1126` stating
that naming only the item "sends the operator to write a key nothing reads". `parked-surfaced`
appears in no operator-facing carrier: zero hits in `SKILL.template.md`,
`tools/unattended/PROTOCOL.template.md` or `memory/guides/UNATTENDED-PROTOCOL.md`, whose DoD table
(line 223) names only the item, and `scaffold_runmd` (`unattended.sh:758-772`) writes no such key.
Reported once already at
`memory/builds/cFinalBerth/reviews/2026-08-13-review-TOOL-cFinalBerth-1-2.md:148-174` and fixed only
in `--abort`. `memory/builds/aBranchedMandate/RUN.md:20-21` carries both keys with a note at line 35
saying they were written by hand — which is finding 13 observed in the field.

**11.** `stage_or_fail` has exactly four call sites (`unattended.sh:1080`, `:1136`, `:1303`,
`:1598`) and `verb_close` is not among them. The stall is escapable — an ordinary `git add`/commit
of the record clears `check_clean`, and the driver deliberately never commits
(`unattended.sh:752-757`) — but neither `SKILL.template.md:162-206` nor protocol §7 names a commit
step between `--close` and the lander, and `fail 2` (`unattended.sh:537`) blames the working tree
rather than the verb that dirtied it.

**17.** Measured both configurations: `git ls-remote --get-url` does not apply `pushInsteadOf` while
`git remote get-url --push` does, so the string compare cannot pass for either spelling. On the
fixture, `--close --override authorization-reachable` was refused by `check 21`. One narrowing to
the raised form: a third exit exists — unsetting the pushurl or the `pushInsteadOf` rule for the
run's duration — but for the ssh-push case that config is usually the landing push's only credential
path, so it trades a blocked verb for a failing push. Read the claim as "unmeetable for the clone as
configured". The function's own comment concedes check 25 is "A cost-raiser, NOT the property".

**21.** Replayed over all 7 tracked run-state files: aBranchedMandate 1 match, aDeclaredCeiling
none, aSealedCaravan none, aSiftedPlaybook 1, aWalkedCorpus 3, cBriefedPilot 3, dClosedLexicon none
with ten review records present, every round pinning a per-round base exactly as
`memory/guides/BUILD-METHOD.md:198` instructs. Only half of the raised finding survives: the
predicate's inability to tell a diff-review from a spec audit, or CLEAN from BLOCKED, is a
**deliberate** scope limit stated in the comment at `unattended.sh:1519-1521`, which records that
`^## Verdict: CLEAN` matches zero of the records it counted and that anchoring it would make the item
unsatisfiable against every review this repo has written — independently corroborating finding 24's
own measurement over 90 records. Do not
re-raise that half. What is a defect is the BASE-only join against a fold-scoped round.

**22.** `lensesDead` (`tier2-review.js:175`) and `skepticsDead` (`:228`) each get a counter with a
comment naming the burn it repays; the synth gets none, and the `note` ternary's only inputs are
`judged`, `lensesDead`, `skepticsDead` and `unverified.length`. The confirmed findings exist only
inside the synth prompt string and nothing after `:290` re-reads them. One addition:
`agents: LENSES.length + batches.length + 1` (`:347`) also counts the synth unconditionally, so a
dead-synth run over-reports its own agent count.

**23.** `grep -rn byDesign` hits only `tier2-review.js:30`, `:69`, `:158` and the two drift-audit
scripts — no caller supplies it, so every real invocation renders "BY DESIGN (do NOT re-report
these): none supplied". Corpus proof: `memory/builds/aWrittenMethod/reviews/…-1-2` and `…-1-3` are
both `**Serves:** diff-review` records over an identical `7f614a1...HEAD` range (25 files vs 38), so
round 3 re-read everything round 2 read. Three corrections: the cSettledDocket pair is *not* two
rounds of one review (`-1` is a spec-audit, `-2` a diff-review, legitimately sharing a base); the
narrowing *rule* is stated in prose at `BUILD-METHOD.md:198`, so the gap is a missing mechanism and
a missing second `Workflow` spelling, not a missing rule; and `closing-review-recorded` greps all of
`reviews/*.md`, so a fold-scoped round-2 record is not by itself a hard blocker on narrowing.

## The three owner symptoms

### "`--close` hangs and prints no output"

Explained by **14·29·6** and **12**: the verb's first substantive act is an unbounded remote
handshake with both streams discarded, up to three are reachable per close under this repo's
`ANCHOR_SCOPE="published"`, the whole DoD loop prints only on failure, and the first byte on a clean
run is `close OK` at `unattended.sh:1443`. The already-known `DOD_OUT=$($GATE_CMD 2>&1)` capture at
`unattended.sh:1465` explains a multi-minute silence *after* item one; these findings explain the
silence *before* it, on a path with no attribution at all.

**Not explained: the hang itself was never observed.** `git ls-remote --symref --exit-code origin
HEAD` returns in well under a second on this clone today. What is measured is the absence of any
bound (nothing in `tools/unattended/` sets one), the discard, and the ordering. The blackhole-IP
reproduction shows the call *can* run unbounded, not that the owner's hang did. Finding 19's
credential-helper mechanism is likewise part-inferred: helpers were observed to run despite
`GIT_TERMINAL_PROMPT=0`, and GCM's own autodetect probe was observed to fire, but GCM returned empty
rather than presenting a blocking dialog — so "a GUI prompt nobody will answer" remains a
possibility, not a finding. And no hang inside the DoD loop other than the bar's own runtime was
looked for.

### "`build-complete` seems unsatisfiable at all"

Explained by **1·8·27**, and the word "seems" understates it: it *is* unsatisfiable, jointly with
`closing-review-recorded`, on every one of the 49 builds in this corpus. **5** explains why it reads
as unconditional rather than as one bad term — the failing term is invisible — and **2** explains
why nothing caught it: the one green control written as a tripwire for exactly this
("If this ever needs one, the item has stopped being satisfiable", `unattended.test.sh:606-607`)
carries the override that disarms it. No gate leg checks `build-complete` at all
(`grep build-complete tools/unattended/check-unattended.sh` is empty), so the bar is green over it.

**Not explained:** term 2 (`missing_units` — a roster id with no spec file) was not shown to fail on
any corpus build, so if the owner met `build-complete` unmet on a *fresh* build with an unrostered
or unspecced id, that is a correct refusal wearing the same silent message, not this defect. The
adjacent items have their own separate causes and should not be folded into this symptom:
`records-current` (**30**) and `authorization-reachable` (**15·9·28**, **17**).

### "Adversarial rounds past the first are not aimed at the previous fold"

Explained by **23**: the harness has no round number and no prior-findings parameter, `base` reaches
every lens verbatim through `diffCmd` (`tier2-review.js:71` → `:156`), and the one
"don't re-report" channel is never populated by any caller. **24** and **25** explain why the loop
does not terminate instead of narrowing: no verdict on disk is machine-legal, so no exit rule can
read one, and the cap that was meant to bound it has a vacuous guard at the closing round.

**Not explained: the rule is not missing, only the mechanism is.** `BUILD-METHOD.md:198` says
plainly to re-review the fix rather than the diff, so this is not a case of nobody having decided —
it is a case of nothing carrying the decision to the agent. Nor is agent *compliance* measured: the
corpus evidence is one confirmed two-round pair with a byte-identical range (aWrittenMethod), which
is an existence proof, not a rate — 7 of 90 records carry a range token at all, and one of the two
candidate pairs turned out to be a spec-audit plus a diff-review rather than two rounds. Finding
**22** is a different failure of the same loop (a round that produces no record at all) and does not
speak to aim.

## Refuted

- **32** — "the driver's *the leg spells this the same way* claim is false: the leg omits
  `records-current`'s third conjunct and skips the check when the build README is missing"
  (`unattended.sh:1476`, `:1479`, `check-unattended.sh:323`). **Died on impact:** a broken README
  marker pair does *not* leave the bar green — `gen_build_index.py:850-860` raises for absent,
  duplicated or transposed `gen:build-index` pairs, deliberately non-skippable per the comment at
  `:1030` ("deleting four marker lines from a build README left `--check`, `--check-format` and the
  whole hygiene gate green"), and two unguarded legs run it over the whole corpus. The parity comment was also misread:
  its antecedent is checking `region`'s exit status rather than only its stdout, which the leg does
  spell the same way.

## Unverified — OUTSTANDING

**None outstanding.** Every raised finding reached a verdict: 33 raised, 32 confirmed, 1 refuted, 0
left unjudged. Coverage caveats, recorded so a later pass can price this: 0 dead lenses of 5, 0 dead
skeptic batches of 5, 0 contradictory verdicts, 0 spurious verdicts — so no finding here is
outstanding for want of an adversarial pass.

## What this audit did NOT cover

- **The non-close verbs**, except where they intersect the close path: `--preflight`, `--plan`,
  `--phase`, `--waive`, `--park`, and `--status`/`--resume` beyond the selector consequence in
  finding 1·8·27. `--landed` was read only as `--close`'s successor.
- **The adopter path**: `adopt-unattended.sh`, its e2e harness, the rendered-Skill parity legs, and
  the junction walk. Nothing was measured in an adopting tree; every measurement is against this
  worktree.
- **The keepalive mechanism** itself (`KEEPALIVE_CREATE`, the reap), and the `.unattended.conf`
  declaration set beyond `LANDER`, `BYPASS_BAN` and `ANCHOR_SCOPE`.
- **The mandate's security property.** No attempt was made to defeat the mandate from inside a run;
  §9's stated limits were read, not re-tested. Findings 13 and 20 touch the write-side asymmetry
  only as usability defects.
- **The other seventeen checks** of `check-unattended.sh`, apart from 8, 10, 11 and 16.
- **The rest of the bar** — the other legs, their guards, and the runtime that makes `gates-green`
  slow — is taken as given, not measured.
- **Non-`bash` shells, CRLF, and the python resolver.** All reproductions ran in Git Bash on node
  `c`; finding 19's credential observations are node-`c`-specific by construction.
- **Live agent behaviour.** `tier2-review.js` was read and its return value reproduced by
  expression; no tier-2 review was executed, and no lens or skeptic prompt was graded.
- **Remedies.** Every "smallest fix" above is a proposal that was reasoned about, not applied and
  not tested. No file in the kit was modified by this audit; the design pass owns the fix set and
  its ordering.
