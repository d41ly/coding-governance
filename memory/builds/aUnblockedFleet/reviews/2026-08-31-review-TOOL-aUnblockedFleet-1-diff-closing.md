**Serves:** diff-review TOOL-aUnblockedFleet-1 TOOL-aUnblockedFleet-2 TOOL-aUnblockedFleet-3 TOOL-aUnblockedFleet-4 TOOL-aUnblockedFleet-5 TOOL-aUnblockedFleet-6

# Closing diff review — aUnblockedFleet: the tree-wide single-live rule, removed

*Tier-2 adversarial pass over the CODE diff, lenses aimed at `tools/unattended/*.sh` — shell logic,
the threshold changes, printf/awk byte correctness, and whether the two enforcement points still
agree with each other and with what the carriers now claim. Every finding below was re-verified
against the working tree by opening the cited lines, not by trusting a finder's quotation.*

**Reviewed range:** `117de044094bc7ac729358edfc24541ba3a1486a...HEAD`

## Verdict: CLEAN WITH FIXES

No blocker. One high, two mediums, five lows — eight distinct defects after dedupe, from nine
confirmed raw findings (ids 8 and 13 are the same defect found twice from different angles and are
merged below as F1). **The load-bearing claim of the build holds.** I re-derived it rather than
taking it: both enforcement points now report and neither refuses, the two thresholds agree, the
LANDING-on-remote exclusion is intact and still fails closed on both sides, and the four bare CR
bytes that commit `3ba95fa6` restored are back at 4 — byte-identical to the base blob — so the awk
regexes that the python text-mode edits broke are whole. The new printfs follow the file's existing
literal-newline convention and carry no format/argument mismatch.

What is wrong is entirely in the SEAM between the code and the things that describe it: one channel
whose stated justification is false, one gate header that now contradicts its own code, one test arm
that cannot fail, and four carriers still explaining the retired rule. Nothing here endangers a
merge; all eight are cheap.

**Review shape** — raw 15, confirmed 9, refuted 6, unverified 0, precision 0.60. **ROUND: 1.**

## Findings

| # | Sev | Site | Defect |
|---|-----|------|--------|
| F1 | high | `tools/unattended/check-unattended.sh:1189` | check 7's report goes to a channel a green bar discards, and the comment's reason for choosing it is false |
| F2 | medium | `tools/unattended/check-unattended.sh:23` | the leg's output contract still names two default-channel announcements; the diff added a third |
| F3 | medium | `tools/unattended/check-unattended.test.sh:645` | the arm proving "the leg still passes" never asserts the exit code |
| F4 | low | `tools/unattended/unattended.sh:1288` | the `-ge 1` threshold this unit changed is asserted by no arm in either suite |
| F5 | low | `tools/unattended/check-unattended.sh:717`, `:1119` | both new headers overclaim what stopped being enforced |
| F6 | low | `tools/unattended/unattended.test.sh:1554` | a comment asserts the retired rule; its twin in `unattended.sh` was rewritten in the same commit |
| F7 | low | `tools/unattended/unattended.sh:1588` | refusal 26's PRINTED message still justifies itself with the removed counter |
| F8 | low | `skills/session-kickoff/SKILL.md:245` | the kickoff hand-back still motivates `--abort` with the retired consequence |

---

### F1 — high — the leg half of this build produces no signal a bar reader ever sees

`tools/unattended/check-unattended.sh:1189-1197`

The comment above the new report picks the default channel over `report` on an explicit ground:
routed through `report` it "would be invisible on every ordinary bar, which is a check quietly
deleted." That reasoning is sound about `report` and false about the channel it chose.

`tools/run-gates/run-gates.sh:1196` is the ONLY site in the runner that echoes a leg's captured
stdout — `sed 's/^/    /' "$WORK/$i.out"` — and it sits inside `report_one`'s FAIL branch. The
`rc = 0` branch at `:1182` emits exactly one line, `GATE ok    unattended kit gate`, and nothing
else. `$WORK/$i.out` has two references in the whole file, so there is no verbose path. The
on-demand runner does not rescue it either: `tools/unattended/run-unattended-gates.sh:141` captures
`out=$("$@" 2>&1)` and on `rc = 0` prints only the label, the seconds, and the last `^PASS` line.

Before this unit, two live records produced `fail 7`, which dumped the leg's whole output to the
terminal and carried the EXCLUDED and UNAVAILABLE notices along with it. Now that check 7 cannot
fail — `grep -n 'fail 7 '` returns nothing — that dump can never fire, so the same suppression also
swallows the two pre-existing notices beside it. Those notices were given the default channel by
`TOOL-aPrimedKeepalive-4` precisely so a green run would show them; removing the only branch that
printed them silently undid that.

The bytes are not lost. They are persisted redacted to `<git-dir>/gate-logs/unattended_kit_gate.log`
at `run-gates.sh:1117-1121` and to `$RUNDIR/$i.out` at `:1129-1135`, both `chmod 600`, and they are
fully visible on a direct `bash tools/unattended/check-unattended.sh` run. So the signal is degraded,
not destroyed — which is why this is high and not a blocker. But `PROTOCOL.template.md:307` and its
rendered twin `memory/guides/UNATTENDED-PROTOCOL.md:307` say "the merge-bar leg REPORTS them", and on
a green bar it does not report them to anybody. The only operator-facing channel that survives is the
driver's `--preflight` announcement, which an agent does see.

This is also the exact residual `TOOL-aReapedTicket-5` was narrowed onto: its OPEN row says the
abandoned record is now surfaced only by "a REPORT an operator has to read," and on the default path
there is no path by which they read it.

**Fix (cheapest honest one).** Stop claiming otherwise. Rewrite the block header at `:1189-1191` to
say the report is persisted to the leg's `gate-logs/` entry and is NOT echoed by a green bar, and
amend the protocol sentence at `:307` in `PROTOCOL.template.md` (then re-render, or check 10's byte
diff reds) to name the driver's `--preflight` announcement as the operator-facing half. If the report
must actually be seen on the bar, that is a notice-passthrough in `run-gates.sh` — echo lines
matching a declared prefix from a green leg's `$WORK/$i.out` — which is a change to the runner, not
to this kit, and belongs in its own unit.

**Left-shift gate.** A leg-header claim about WHERE its output lands is checkable: add a canary to
`run-gates.sh`'s existing canary set asserting that no leg script's comments claim default-channel
visibility for a passing leg, or — narrower and cheaper — have `check-playbook.sh` grep the protocol
for "the merge-bar leg REPORTS" and require the same paragraph to name `gate-logs/`. The general
class ("a comment states a channel property the runner disproves") has no cheap mechanical form; the
specific pair does.

---

### F2 — medium — the leg's output contract now classifies its own green output as a violation

`tools/unattended/check-unattended.sh:23` (contract at `:12-13`, exceptions at `:15-29`)

The header still reads: "Exit 0 + no output = clean, EXCEPT for the two announcements named below.
Anything else printed is a violation." It then enumerates **TWO EXCEPTIONS, both named rather than
quietly taken** — (ONE) the REPORT-channel skips, which are gated on `GOV_UNATTENDED_REPORT=1` and
so are not default-channel output at all, and (TWO) exactly "check 7's EXCLUSION notice and its
UNAVAILABLE sibling."

The diff added a third unconditional default-channel `printf` at `:1192-1197`, labelled "REPORTED,
NEVER FAILED", and `git show 1f45b32c -- tools/unattended/check-unattended.sh` shows the header
paragraph untouched — only the version bump, the check-4 comment and the check-7 body moved.

The file pre-committed to this exact failure in writing. `:26-29` says routing an announcement "to
stdout without amending this paragraph would leave the header asserting something the code
disproves." It does.

Reachable on the real tree today, not hypothetically: `nlive` increments for every non-terminal
record at `:714`, the tree holds `aThawedCorpus` (LANDING) and `aUnblockedFleet` (BUILDING) as its
only two non-terminal `RUN.md` records, and only the check-7 LANDING-on-remote exclusion at `:1181`
drops one. The next concurrent BUILDING record fires the report. Nothing grades this mechanically —
`run-gates.sh` and `run-unattended-gates.sh` both grade exit status, and check 10 byte-diffs
`PROTOCOL.template.md` against the rendered guide, never this script's header — so the cost is an
operator or a future wrapper reading a clean run as red.

**Fix.** Change "the two announcements named below" to three, and add a third bullet to the
exceptions block naming check 7's concurrency report, with the same DEFAULT-channel justification the
code comment at `:1189-1191` already carries. Fold F1's correction into the same edit.

**Left-shift gate.** This one IS mechanical and cheap: a self-test arm that derives the count of
unconditional default-channel `printf` sites in the script and compares it to the number the header
paragraph names, failing when they diverge. That gates the class (any future fourth announcement),
not the instance. `AGENTS.md` §7 already makes "a gate's OWN header states what it does NOT check"
load-bearing; this is the enforcement it never got.

---

### F3 — medium — the arm written to prove the leg still passes cannot fail if the leg reds

`tools/unattended/check-unattended.test.sh:645`

The arm's stated purpose is "check 7 REPORTS two non-terminal run-state files and the leg still
passes." It calls `out=$(run)` and then makes three assertions, all on the captured text. `run()` at
`:222` is `bash "$SCRIPT" 2>&1` — the exit status is discarded. `hit()` and `miss()` at `:57-58` are
pure `grep -qF` over that text and never touch `$?`.

So a leg that emits the concurrency report and then exits 1 — for check 7 or for anything else the
two-live-record fixture trips — passes this arm silently. The load-bearing behavioural claim of
`TOOL-aUnblockedFleet-2` is untested by the arm written to test it. The `miss "$out" "more than one
run-state file is non-terminal"` only catches a verbatim revival of the retired message; it says
nothing about the exit code.

The suite already holds the correct idiom for a report-only check, in the same file. Check 23's arm
at `:2536-2539` does `out=$(run); rc=$?`, then `same "check 23 reports without failing the leg, exit
code" "$rc" "0"` and `miss "$out" "FAILED"` — and its own comment gives the reason: a check that is
silent AND exits 0 is indistinguishable from one that is working.

**Fix.** Change `:645` to `out=$(run); rc=$?` and add `same "check 7 reports two live records without
failing the leg, exit code" "$rc" "0"` plus `miss "$out" "FAILED"`, matching the check-23 precedent
verbatim. `fail()` at `check-unattended.sh:93` emits `UNATTENDED check N FAILED — …` on every
refusal, so the `miss` catches any refusal, not only check 7's.

**Left-shift gate.** Extend `tools/unattended/check-arms.py` — or add a sibling predicate to it — that
flags any arm whose comment claims the leg PASSES or REPORTS while the arm makes no `same … "$rc"`
assertion. That is a grep-able pair (a comment verb and a missing assertion form) and it gates the
class across both suites, not this one arm.

---

### F4 — low — the one predicate this line changed is graded by nothing

`tools/unattended/unattended.sh:1288`

The UNAVAILABLE-notice threshold moved from `-gt 1` to `-ge 1`, and the comment at `:1282-1287`
explains why at length: left at `-gt 1` the notice goes mute in exactly the state the LANDING
exclusion exists for, which is green-by-absence inside the sentence written to prevent it. The
reasoning is right and the change is right.

No arm asserts it. `grep -rn UNAVAILABLE tools/unattended/` returns three source hits
(`check-unattended.sh:23`, `check-unattended.sh:1162`, `unattended.sh:1289`) and zero test hits.
Every new arm runs with an anchor observed, so the `[ -z "$anc" ]` branch is never taken by any of
them.

Unit 1's spec AC6 explicitly required "BOTH the announcement and the UNAVAILABLE notice, asserted by
two `hit` arms over one fixture" and called it "the one that fails if the two thresholds drift
apart." Those arms were never written. The acceptance ledger's AC6 names
`bash tools/unattended/unattended.test.sh` as its observation token but gives line proximity as its
reasoning — "the two thresholds are one line apart and cannot drift silently" — which is not an
observation of the branch. No fallback grader exists either: `check-arms.py`'s own docstring
restricts its population to `fail <n> "` branches, and this is a bare `printf`.

A regression to `-gt 1` — exactly the drift the comment was written to prevent — would be caught by
nothing, and §7's rule is that a branch whose behaviour has never been observed is an assertion about
nothing. The ledger records an unmet criterion as evidenced.

**Fix.** Add one arm beside the new announcement fixtures with the anchor observation defeated
(unreachable remote, or no advertised default branch), asserting BOTH the `live-run exclusion is
UNAVAILABLE` line and the `1 concurrent unattended run(s)` line over a single competitor — the single
fixture that separates `-ge 1` from `-gt 1`. Then correct unit 1's AC6 in the acceptance ledger to
cite that arm rather than line proximity.

**Left-shift gate.** Widen `check-arms.py`'s population from `fail <n> "` branches to include bare
`printf` sites that emit an operator-facing `unattended: ` line, so an un-asserted announcement reds
the way an un-asserted refusal already does. That closes the whole hole this finding sits in rather
than the one predicate.

---

### F5 — low — both new headers overclaim what stopped being enforced

`tools/unattended/check-unattended.sh:717` and `:1119`

`:716-717` says the archived-must-be-terminal branch "is the ONLY check in this leg that still
refuses on a run-state phase." `:1119` says "The one property still enforced over run-state phases is
check 4's, that an ARCHIVED record is terminal."

Both are contradicted in the same file. `fail 4` also fires on a run-state file that declares no
phase (`:708`) and on one whose phase is outside the effective vocabulary (`:712`) — both refuse
purely on the phase — and check 9 gates a refusal on the phase at `:870-873`
(`case "$ph" in LANDING|LANDED|VERIFYING)` guarding the `base == HEAD` refusal).

Under a check-NUMBER reading, `:717` is defensible: its siblings at `:708` and `:712` are all
`fail 4`, so "the only check" is arguably true even though "refuses on a run-state phase" is not.
`:1119` has no such defence — phase-in-vocabulary is a distinct property still enforced over
run-state phases, so "the one property" is plainly false. That asymmetry is why this stays low.

It still matters. §7 makes a gate header's own statement of scope load-bearing, and the false
confidence from an overclaiming header is the class this repo left-shifted. Here it is the header of
the check that just stopped enforcing anything, which is the worst place for it.

**Fix.** Narrow both sentences to the property actually meant. At `:1119`: "the only remaining refusal
keyed on how many records are LIVE." At `:717`: "the only branch of this leg that still refuses a
record for the phase it CLAIMS while archived." Or enumerate `:708`, `:712` and `:873` alongside.

**Left-shift gate.** No cheap mechanical form — "does this English sentence overstate the code" is not
gate-able. This one goes on the §10 recurring-class checklist instead, as the documented manual check
§7 requires when a class cannot be gated: *a header sentence containing ONLY / the one / the sole,
about a property of the enclosing file, is re-derived against the file before the diff lands.*

---

### F6–F8 — low — one retired rule, four carriers, three still explaining it

These are three sites of one class, the multi-site-fix-parity class this repo already tracks as
`TOOL-aScannedThrottle-9`, where the copies end up in open disagreement rather than wrong together.
They share a fix and a gate, so they are grouped.

The rule that went away: check 7 no longer refuses on the live count. `grep -n 'fail 7 '
tools/unattended/check-unattended.sh` returns nothing, `check-unattended.sh:1113` states check 7 "no
longer asserts anything about how many," and the backlog settles the vocabulary at
`TOOL-aBoundedVerdict-24` — "A run parked at LANDING is now reported, not enforced against." The
distinction between *measured against a counter* and *appears in a report* is the whole change.

**F6 — `tools/unattended/unattended.test.sh:1553-1554`.** A comment still asserts, present tense, that
"one `--phase` call returns a LANDED run to the single-live counter that leg check 7 reds on." Its
exact twin at `unattended.sh:2065-2069` was rewritten in the SAME commit to say the opposite: "Since
TOOL-aUnblockedFleet-1 neither `check_single_live` nor leg check 7 refuses on that count, so what
this guard now protects is the RECORD's own honesty rather than the fleet's." The test file was
edited in this build (31 lines per `git diff --stat 86148e20..HEAD`), yet the stale line survived an
edit to its own file. Unit 3's AC6 grepped three alternate spellings — "the bar reds on the second
one", "At most one run-state file may be non-terminal", "returns the run to check_single_live" — and
none matches this one, so its "returned nothing" is a true result over an incomplete pattern set
rather than evidence the retired rule is gone.

**F7 — `tools/unattended/unattended.sh:1588`.** Refusal 26's message, verbatim: "…every later run is
measured against the counter this record left…". This is prose the driver PRINTS, not a comment, so
it reaches an operator at the moment they are deciding whether the refusal is worth working around.
The harm it names no longer refuses anything. The refusal's other stated ground — a finished record is
not something to move, re-open or re-pin — remains sound, so the stale clause is the weaker half
presented as the sharper one. The string is pinned by `unattended.test.sh:1556`, and the comment
above that assertion is F6. One correction to how this was first framed: that suite is NOT on the
merge bar — `tools/gate-legs.json` carries only `check-unattended.sh`, `check-playbook.sh` and the
skill-wiring leg — so the assertion is on-demand via `run-unattended-gates.sh`, not gated on every
push. That weakens "now gated by an assertion" without touching the defect.

**F8 — `skills/session-kickoff/SKILL.md:245`.** The kickoff engine's unattended hand-back still
motivates `--abort` with "a run that stops without it stays non-terminal forever, and every later run
is measured against a counter that still includes yours." `git log -S` shows this sentence and the
unattended kit's own analogous one were introduced by the SAME commit `26df2337`; commit `1f45b32c`
rewrote the kit's copy to "which no longer reds anyone's bar, but does put your unfinished run in
every later run's concurrency report" and left this one untouched. It is a different kit, so it sat
outside unit 3's grep roots of `tools/unattended/ .claude/skills/unattended/ memory/guides/`. This is
live hand-back text an unattended agent reads when deciding whether to abort: it over-motivates a
correct action rather than causing a wrong one, and the real remaining reason (the record is
otherwise reported forever, with no staleness bound) goes unstated.

**Fix.** One edit each, all three saying the same thing the kit's SKILL now says: the record is not
refused, it is reported in every later run's concurrency announcement, which is why `--abort` is
still the right verb. For F7, drop the counter clause and keep the record-integrity ground, and
update the pinned `hit` string at `unattended.test.sh:1556` in the same edit.

**Left-shift gate.** One gate covers all three and the next one. Unit 3's AC6 grep already exists as
a pattern set over a root set; both were too narrow. Promote it from a one-time acceptance check into
a standing leg predicate: the pattern set gains the spellings F6 and F7 use ("single-live counter",
"measured against the counter", "measured against a counter"), and the root set widens from the three
unattended paths to every tracked carrier that mentions the kit — which is what pulls
`skills/session-kickoff/` in. A grep-based leg over a declared root set is the cheap form here, and
the population is small enough that it costs nothing on the bar.

---

## What I checked and did not find

Stated because a review that reports only hits is indistinguishable from one that only looked where
the findings were.

- **The two enforcement points agree.** `check_single_live()` in `unattended.sh` and check 7 at
  `check-unattended.sh:1113-1198` both count non-terminal records, both apply the LANDING-on-remote
  exclusion, both fail closed when the anchor cannot be resolved, and neither refuses. The driver's
  report additionally names each record's witness where the leg's names only the phase — an asymmetry,
  not a defect, and the driver is the channel an operator actually reads (F1).
- **Byte-level correctness of the new printfs.** Format strings and argument counts match at
  `check-unattended.sh:1193`, `:1195`, `unattended.sh:1289`, `:1295`, `:1297`. The literal embedded
  newline inside the single-quoted format at `check-unattended.sh:1193-1196` is this file's
  pre-existing convention — the base blob's UNAVAILABLE printf at `117de044:1147` has the same shape —
  and is not a text-mode-edit artifact.
- **The CR damage is genuinely repaired.** `tr -cd '\r' | wc -c` gives 4 on both
  `117de044:tools/unattended/check-unattended.sh` and the working tree, so the four awk regexes
  matching `/\r$/` at `:635`, `:1107` and the two at `:1575-1576` are intact. Commit `3ba95fa6` closed
  it and the count is the proof.
- **The threshold pair.** `unattended.sh:1288` is `-ge 1` (the UNAVAILABLE notice, fires alongside a
  single announced competitor) and `:1294` gates the announcement at `-lt 1`; `check-unattended.sh`
  uses `-gt 1` at both `:1161` and `:1192`. The asymmetry is deliberate and correct — the driver
  announces competitors OTHER than itself, the leg counts every live record including the running
  build — and the driver's comment at `:1281-1287` is the only place that explains it. F4 is that
  nothing tests it, not that it is wrong.

## Provenance

Reviewed at `117de044094bc7ac729358edfc24541ba3a1486a...HEAD`, eleven commits, 25 files. Lenses ran
over the code diff in `tools/unattended/*.sh` with the carrier set as secondary surface. Six raw
findings were refuted by the skeptic pass and are not carried here. Zero findings came back
unverified.
