**Serves:** diff-review TOOL-dLoggedFlight-1 TOOL-dLoggedFlight-2 TOOL-dLoggedFlight-3 TOOL-dLoggedFlight-4 TOOL-dLoggedFlight-5 TOOL-dLoggedFlight-6 TOOL-dLoggedFlight-7 TOOL-dLoggedFlight-8 TOOL-dLoggedFlight-9 TOOL-dLoggedFlight-10 TOOL-dLoggedFlight-11 TOOL-dLoggedFlight-12 TOOL-dLoggedFlight-13

# dLoggedFlight — the CLOSING diff review, ROUND 2: a review of the fold

*This is an adversarial Tier-2 pass over the FIX for round 1's fifteen defects, not over the whole
diff again. Node `d`, 2026-09-16, on `branch/unattended-build-transparency-ea83a5` at HEAD
`37d4b899`. This is ROUND 2 of the closing review. Its shape was four primed finder lenses, then a
skeptic stage of five batches prompted to REFUTE each finding, then one synthesis pass, which is this
record. Round 1 is [the round-1 record](2026-09-14-review-TOOL-dLoggedFlight-1-closing-diff-review-round1.md).
None of its findings is raised again here, and where a finding below reopens one of them, it names
which. Every cited line was re-read at `37d4b899`. The severities in the table are this synthesis's
own adjudication, not the finders' grades. The figures this synthesis measured are listed under "What
this synthesis re-derived". Where a figure is a finder's or a skeptic's and was not measured again,
the text says so. The binding contracts are `memory/guides/UNATTENDED-PROTOCOL.md` and
`memory/guides/BUILD-METHOD.md`. Round-2 labels carry an `R2-` prefix, so `R2-B1` is never confused
with round 1's B1.*

**Range, ROUND 2:** `36d531b9...ff436b64`, the fold. It holds 23 commits: 22 fold commits in five
sequential slices, each spec-first with a section 9 line and staged-RED arms, plus the round-1 record
commit `69cddc90`. It touches 42 files, +3897/−374. Round 1 reviewed `9ce37fcc...36d531b9`, and this
range starts at that head. Two more subjects sit outside the range and were read separately:

- **The second origin/main reconcile's semantic joins**, in merge `de64de53`, read with
  `git show --cc` and against each parent. They are the resolution of
  `tools/unattended/SKILL.template.md`, the conf defaults in `tools/unattended/unattended.sh`, the
  trimmed run-log paragraph and `RUNLOG_SESSION_VARS` row in `tools/unattended/PROTOCOL.template.md`,
  `--audit` in `TREE_BLIND_VERBS` and `HEARTBEAT_VERBS` in `tools/runlog/model.py`, and the sixth
  exemption in `tools/unattended/runlog-writer.test.sh`. After the merge come `8096c38c` and
  `37d4b899`.
- **The spec text the build pass wrote**, the rev-5 and rev-6 section 9 lines, which no earlier round
  reviewed.

The run's pinned BASE is `a4007553`, the mandate commit. The first origin/main reconcile merge is
`9ed23769`, and its main-side tip `9ce37fcc` is round 1's base. The review is not pinned to
`a4007553`, because a range from there would include again everything both reconciles merged in from
main.

## Verdict: BLOCKED

The finding set is one BLOCKER, one HIGH, two MEDIUMs and five LOWs. That is nine distinct defects
from thirteen confirmed reports.

**The blocker shows that the fold closed round 1's instance of B1 and not its class.** The fold judges
idle gaps only where the transcripts read `present`, on the premise that every owner turn the guard
needs is then known. But `present` says an extract exists for every named session. It does not say
that the extract covers the window. The model reads a store extract before the live transcript and
never compares the extract's `tree_bytes` with anything. This synthesis measured the consequence on
this build's own model at HEAD by cutting the run's one session extract at a quarter, half and three
quarters of the window:

- Every cut still read the transcripts as `present`, so idle gaps were judged.
- Where the live model judges 0 idle gaps, the cuts judged 5, 2 and 2.
- In each cut, one of those gaps ends within two minutes after one of the run's real in-window owner
  turns, which the stale extract does not hold.
- The in-window owner count rendered as 2, 3 and 3, where the transcript holds 5.
- No render was refused. The renderer's refusal reads its owner turns from the same stale model, so
  it cannot see the turn it would have to protect.

That is round 1's blocker reproduced: an idle row whose end places an owner turn, in a record bound
for a public remote. The precondition is not hypothetical here. This clone's store holds an extract
for this run's one named session, written 2026-09-16. Its newest event is after today's window end,
so today's model is unaffected, but no step refreshes it before the close's render, which is the one
that rides the merge.

**The HIGH is the same class through a different row.** On a POSIX adopter, an owner's Esc during a
driver verb or a bar makes the EXIT trap write an unclean END, or a `verdict=NONE` gate line, within
milliseconds of the transcript's interrupt record. The model publishes that time as a killed-verb
anomaly or a gate row. The renderer's refusal compares whole seconds only, so the run's every render
is either refused or published with the interrupt placed to about a second.

**The rest of the design stands.** No confirmed finding disputes any of these rules:

- A run holds a tree from its first claiming call.
- One window bounds every timed set.
- A close is a clean END.
- The pushes proof is read at the window's end.
- A run with none of its own driver lines here reads `not-local`.
- A range names every unit.

Every finding sits at an edge of those rules. R2-B1 is about which source counts as covering the
window. R2-H1 is about which rendered rows an owner act causes. R2-M1 and R2-L1 are about which calls
name a session or place a run. R2-M2 is about which anomaly kinds need a transcript.

**What BUILD-METHOD prescribes for these counts.** Round 1 recorded `blockers 1`
(`memory/builds/dLoggedFlight/RUN.md:94`). A diff review re-arms only on a count strictly smaller than
the round before, and this round's count is also 1. So the `--review` verb should answer
NON-CONVERGENT, the loop stops, and every confirmed finding is disposed by severity. R2-B1 and R2-H1
are PROMOTED to units whose mechanisms close them, each audited as a spec. The two MEDIUMs and five
LOWs are FOLDED into their specs as rev-N bumps with section 9 lines. None may be parked, waived,
retired or re-reviewed. The verb decides this. This paragraph only reads the rule against the counts.

## Run integrity

- Lenses: **4 of 4** returned, **0 died**.
- Skeptic batches: **5 of 5** returned, **0 died**.
- Verdicts: **0** contradictory ones demoted to unverified, **0** spurious ones discarded, **0**
  duplicates.
- Unverified findings: **0**.

Every stage returned, so for this lens set the run is complete. A zero anywhere below is a result of
the lens set, not a gap left by an agent that died. In one respect it is still weaker than evidence of
absence: the five refuted reports were not handed to this synthesis, so this record cannot say which
surfaces they covered. That matters most for the build-pass spec text, which drew no confirmed
finding.

## Review shape

- Raw findings **18**, confirmed **13**, refuted **5**, unverified **0**, precision **0.72**.
- The 13 confirmed reports collapse to **9** distinct defects. Reports 2 and 5 are one defect
  (R2-H1). So are reports 3, 6 and 13 (R2-M1), and reports 8 and 15 (R2-L2). The pipeline's
  duplicate count of 0 counts only byte-identical reports, so merging these was this synthesis's
  decision.
- Precision rose from round 1's 0.60 to 0.72. Both are above the retune floor of about 0.5, so the
  lens set and the priming stay as they are.
- Severity is this synthesis's call. Report 1 arrived graded high, and its skeptic judged high an
  overstatement, because the precondition seemed to need a hand-run extract. This synthesis raised it
  to BLOCKER on two facts the skeptic did not have. The runlog Skill's own step 3 writes such an
  extract on the shipped default, and this clone's store holds one for this very run. Reports 2
  (medium) and 5 (high) merge at HIGH.

## Lens brief — the bug classes this range selected

`python tools/memory-tree/gotchas.py --for-diff 36d531b9..ff436b64` selects 27 classes over the 42
changed files: 22 by anchor, plus 5 universal ones. Seven of the nine defects are instances of a class
on that list:

- `withheld-value-recovered-from-a-derived-one`, the class round 1 filed for B1: R2-B1 and R2-H1.
- `join-key-widened-by-a-shared-location`, the class round 1 filed for H2: R2-M1 and R2-L1. The fold's
  own checklist named this class twice, over two different commits, and the fold parked both instances.
- `fold-text-is-unreviewed-surface`: R2-B1, R2-H1, R2-M1, R2-L1 and R2-L2 all trace to fold text, and
  R2-L3 and R2-L4 to the reconcile's text. The reconcile's resolution is fold text too.
- `amendment-leaves-its-other-half-standing` and `two-answers-to-one-question`: R2-L3, R2-L4, and
  R2-L2's spec-versus-code seam.

R2-M2 is round 1's M6 class, an unknown that reads as clean, left uncovered on a sibling. R2-L5 is
round 1's M7 class, `two-readers-of-one-config-one-re-derived`, in a reader outside the diff, which is
why no anchor selected it. R2-B1 also breaks the charter's section 7 rule that a guard sharing a
variable with the thing it guards is not a guard.

## Findings

| # | Severity | Location | Defect | Reports |
|---|---|---|---|---|
| R2-B1 | BLOCKER | `tools/runlog/model.py:712` | A store extract is read before the live transcript and never tested for freshness, so a stale one reads `present`, idle gaps are judged without the later owner turns and calls, and the render's refusal reads the same stale turns | 1 |
| R2-H1 | HIGH | `tools/runlog/model.py:1136` | A killed verb's anomaly and a killed bar's `NONE` gate row carry the kill's time, which an owner's interrupt sets to within milliseconds, and the refusal catches only the same second | 2, 5 |
| R2-M1 | MEDIUM | `tools/runlog/model.py:1489` | Read-only visits still name the run's sessions and still move a non-terminal window's end past themselves, so another session's owner turns, usage and calls become the run's | 3, 6, 13 |
| R2-M2 | MEDIUM | `tools/runlog/model.py:1146` | `destructive-git` and `red-behind-zero` vanish with no not-judged marker when the transcripts are not counted, so the Anomalies section reads clean | 17 |
| R2-L1 | LOW | `tools/runlog/model.py:1691` | `own_driver` counts read-only visits, so a `--status` after landing places another node's run on this node and its journals read `dead` | 14 |
| R2-L2 | LOW | `tools/runlog/model.py:1640` | The spec-mark split reads each spec at the era's end rather than the window's, and the rev-8 reason for leaving it does not hold | 8, 15 |
| R2-L3 | LOW | `tools/unattended/SKILL.template.md:29` | The reconcile dropped the tick's run-state-file condition and kept the claim that no slug exists before `--preflight` | 9 |
| R2-L4 | LOW | `tools/runlog/README.md:229` | The README, in two places, and the runlog dossier still list three tree-blind verbs after `--audit` joined the constant | 18 |
| R2-L5 | LOW | `tools/drift-audit/drift_report.py:114` | drift-audit's `load_conf` keeps the quotes before a trailing comment, round 1's M7 in a reader this build's drift signal consumes | 16 |

### R2-B1 — a stale store extract reads `present` (BLOCKER)

**Where.** Three places combine:

- `tools/runlog/model.py:710-717`: `resolve_run_sessions` loads `<store>/sessions/<sid>.json` first
  and falls back to the live transcript only when no extract exists. `:731-732` then reads `present`
  when every named session was found. The discovered path at `:699-708` reads `present` the same way.
- `:1598`: idle gaps are judged when `tr_state == "present"`. `:1602-1604` builds their spans from
  those extracts, and their owner-turn guard from `turns`, which are the same extracts' turns.
- `tools/runlog/record.py:840-846`: `scan_owner_times` reads its owner turns from the model it is
  checking.

**Defect.** An extract records its transcript's size as `tree_bytes`, and nothing in `model.py` reads
it. So an extract written before the window ended still reads `present`. It holds none of the owner
turns, tool calls or usage that came after it. Spec 8's rev-6 line rests the B1 fold on exactly the
premise this breaks: gaps are judged only where every owner turn the guard needs is known. The same
stale read renders the owner-turn counts, usage and attributed calls as known values. That is the
clean-looking zero M6 was folded to remove, in the facts that answer "what did it decide without
asking".

**Reached by.** Any render made after an extract was written and before the window ended. Two ordinary
routes create that state:

- On the shipped default, `RUNLOG_SESSION_VARS` is blank, so the journal names no session. A WHY
  question asked mid-run then sends the runlog Skill to its step 3,
  `extract --discover --slug <slug>` (`tools/runlog/SKILL.template.md:46-48`). The later close render
  reads that discovered extract as `present`.
- Anyone runs `extract --slug` or `--session` in a session that goes on working. That includes a
  long session holding more than one run, which is the case the `multi-run-session` anomaly exists
  for.

This synthesis measured it on this build. With the extract cut at 25%, 50% and 75% of the window,
the model judged 5, 2 and 2 idle gaps where the live one judges 0. In each cut, one gap ends within
two minutes after a real in-window owner turn, and two gaps lie inside the fold's own 900-second
guard. The in-window owner count read 2, 3 and 3 instead of 5, and no render was refused. This record
leaves out which gap and which turn, for B1's reason. This clone's store now holds an extract for the
run's one named session, written 2026-09-16, and the placement-2 render at the close is still ahead.

**Why BLOCKER.** It publishes, to a remote that cannot withdraw it, the value the closed schema exists
to withhold. It reverses the premise round 1's blocker was disposed on. And the backstop added to
catch exactly this cannot catch it, by construction. The precision is the reply latency to the next
journal or git event, not the second. The fold's own ratified guard treats reply latency as a leak:
the `IDLE_OWNER_GUARD_S` Decided line in `fce435b3` says so. Stale extracts also bring H1 back after
the cut, since busy stretches read idle again once their tool calls are missing.

**Fix.**

- Read the live transcript whenever `resolve_session_tree` finds one.
- Fall back to a store extract only when no transcript is local. Mark that session `partial` unless the
  extract covers the window: either its `tree_bytes` equals the transcript's current size, or an
  extraction time recorded in the extract is at or after the window's end.
- Judge idle gaps, and render the transcript-derived counts, only when every session's coverage
  reaches the window's end.
- Give the discovered-by-slug path the same test.
- Make the backstop independent. When a transcript is local, the `record` command re-reads its owner
  turns' seconds itself and hands them to the refusal, rather than grading the model with the model's
  own turns.

**Left-shift.**

- A model arm with a store extract cut before an in-window owner turn that sits beside a 20-minute
  driver silence, and the transcript holding the turn local. It expects no idle row near the turn and
  the transcript's owner count.
- The same arm with no local transcript. It expects `partial`, idle gaps not judged, and `-` counts.
- A refusal arm in which the model is handed stale turns and the text carries an idle row ending
  beside a turn the transcript holds. It expects the independent read to refuse.
- Add this instance to `memory/gotchas/withheld-value-recovered-from-a-derived-one.md`: a cache
  preferred over its source, with its freshness key never read.

### R2-H1 — a killed row carries an owner interrupt's time (HIGH)

**Where.**

- `tools/runlog/model.py:1136-1138`: a verb whose END reads `exit=unclean` becomes a `killed-verb`
  anomaly at `e["end"]`. `tools/runlog/record.py:587-590` renders that time in the Anomalies table.
- `model.py:1553-1562`: a gate line joins with its own `t`, which a bar killed by a signal writes from
  its cleanup trap, reading `verdict=NONE` with the signal's rc (`tools/run-gates/run-gates.sh:1053`,
  `:1109`). `record.py:512` renders it.
- `model.py:1459`: a non-terminal window's end is `i["end"] or i["t"]` plus one second, so an unclean
  END that is the last event places the end too.
- `record.py:857`: the refusal compares whole seconds.

**Defect.** The driver has no TERM trap, on purpose, and its EXIT trap still writes the END
(`tools/unattended/unattended.sh:5202-5207`). A skeptic measured that trap running about 14 ms after
SIGTERM in a non-interactive bash, and the installed Claude Code binary kills a shell command with a
process-group SIGTERM on POSIX. The extractor counts `[Request interrupted by user` as an owner turn,
via `interrupt` (`tools/runlog/extract.py:585-586`, `:706-707`). So an owner's Esc during a foreground
driver verb or bar puts a rendered time within milliseconds of an owner turn. The model keeps idle
gaps away from owner turns, and keeps neither of these rows away.

**Reached by.** An owner interrupting a foreground driver call on a POSIX adopter. There are two
outcomes, and this synthesis did not measure how often each occurs:

- The END and the interrupt record share a second. The refusal then fires on every render of that
  run, so the one run the owner interrupted never gets a record, and a refused render blocks nothing.
  The refusal message also blames "an idle gap beside an owner turn" (`record.py:893-897`), which
  sends the reader to the wrong place.
- They straddle a second boundary. The record is published with a killed-verb row or a `NONE`/143
  gate row placing the interrupt to about a second, beside an in-window owner count of at least 1.

This repository's four registered nodes are Windows, where the kill is `taskkill /T /F` and runs no
trap. A killed call there leaves a START with no END, rendered at its START. So this repository
mostly escapes, and adopters do not. This clone's store holds 2 interrupt-class owner turns across its
31 session extracts, so the trigger is an ordinary act.

**Why HIGH and not BLOCKER.** Unlike R2-B1, this row is not computed from an owner turn. It is an
independent event the owner's act caused, and a Bash-tool timeout produces the same row with no owner
involved. The row's kind does not identify an interrupt. The leaking branch needs the kill to straddle
a second boundary, which a gap of milliseconds makes the less likely branch, though this synthesis did
not measure the split. And this repository's own nodes do not reach it. The evidence loss on the other
branch is real on every POSIX adopter.

**Fix.**

- In `build_run_model`, extend the rule `derive_idle_gaps` already applies. A killed-verb anomaly, a
  `NONE` gate row, or any unclean END used as an end, whose time lies within a short latency bound of
  an owner turn, is held off the committed rows and counted, as `near_owner` is.
- Where the anomaly needs a time, give it the verb's START.
- Do not let an unclean END close a window's rendered end.
- Keep the refusal narrow, but widen its comparison to a band for these row kinds only. Widening it
  for every UTC would refuse ordinary records whose verb row answered an owner turn within seconds,
  which trades one loss for another.
- Make the refusal message name the row kind it matched rather than an idle gap.
- This synthesis also recommends covering compaction rows in the same rule, for the reason under
  "The known residue" below.

**Left-shift.**

- An arm staging an interrupt owner turn, then 10 ms later an END with `exit=unclean` and a
  `verdict=NONE` gate line. Run it once in the same second and once across a second boundary. It
  expects no refusal and no rendered time within the band.
- The CLASS gate: a source arm that enumerates every timeline kind and anomaly kind the renderer emits
  a UTC for. It requires each to be either in the held-near-an-owner-turn set or declared independent
  of owner acts, in both directions, so the next kind that can be owner-caused cannot arrive unheld.

### R2-M1 — a read-only visit joins the run's sessions (MEDIUM)

**Where.**

- `tools/runlog/model.py:1419`: `seg` is every invocation of the slug in the journal segment, whoever
  made it.
- `:1459`: `last_event` takes `i["end"] or i["t"]` over all of `seg`, visits included, and for a
  build's last run `seg_end` is None.
- `:1488-1489`: `sids` is every session named by any in-window START.
- `:1578`, `:1705-1706` and `:1694`: that session's owner turns, usage and attribution follow.

**Defect.** The fold made `--status`, `--resume`, `--landed` and `--audit` blind for trees, and left
them naming sessions. The unit 8 ledger's residue says that after the window bound "a session whose
only call on the run comes after the run's end is no longer one of its sessions". That holds for
terminal windows only. For a non-terminal window, and the close's placement-2 render is one, a later
visit moves `last_event` past itself, so it always lands inside the window it moved.

**Reached by.** Another Claude session, which sets `CLAUDE_CODE_SESSION_ID`, runs
`unattended.sh --status <slug>`. The Skill documents that as the status check. Probed by a skeptic
through `derive_attribution` and `build_owner_positions`: a second session made an in-window
`--status`, 10 tool calls and 1 owner turn, and the model then read calls 11, attributed 11, all in
the run's phase, and in-window owner turns 1. The committed Summary then reports owner turns and cost
the run never had. A stalled run visited days later stretches its whole window to the visit.

**Fix.** Tree-blindness and session-naming are different questions, so they need two constants:

- **Naming sessions.** Take sessions only from in-window calls whose verb is not a pure read. The
  reads are `--status` and `--audit`. `--resume` continues the run and `--landed` is its own act, so
  both still name sessions.
- **Attribution.** In `derive_attribution`, an END from a session that made only reads is not an
  `own` point.
- **The non-terminal end.** A read moves it only when its session is one the run's claiming calls
  named, or when the journal records no session at all. The finders proposed excluding reads from
  `last_event` outright. That would put a stalled run's `--audit` heartbeats after its window, and
  `stalled` would never fire. The two stalled-streak fixtures `8096c38c` added should red on that
  spelling.
- **The ledger.** Strike the unit 8 ledger's park. Its first reason, "No review confirmed it", no
  longer holds.

**Left-shift.**

- An AC23 arm with a second session making an in-window `--status`, one owner turn, usage and tool
  calls. It expects none of them counted.
- A non-terminal arm with a foreign `--status` an hour after the run's last act. It expects the window
  end unmoved, and a stalled streak of the run's own `--audit` calls still inside the window.

### R2-M2 — tool-call anomalies vanish unjudged (MEDIUM)

**Where.** `tools/runlog/model.py:1146-1156` builds `red-behind-zero` and `destructive-git` from
`model["tools"]` alone, and that list is empty unless an extract is local (`:1570-1592`). The Anomalies
fact at `tools/runlog/record.py:266` is `{int} · shown {int} · aggregated {yes-no}`, with no judged
flag. The runlog Skill's "No local transcript" paragraph (`tools/runlog/SKILL.template.md:73-77`)
names usage, owner turns, attributed calls and idle gaps, but not these two kinds.

**Defect.** The M6 fold renders `-` for five transcript-derived counts and adds `idle gaps judged`. It
leaves the two anomaly kinds that only a transcript can fire with no marker. A run that did a
`git reset --hard`, or whose background bar reported rc 0 over a RED gate line, commits
`anomalies 0` when its transcripts are not local. The Skill routes "why it stopped" to that section.

**Reached by.** Every adopter on the shipped default, where the journal names no session. Round 1
established that reach for M6, and the fold's spec 9 rev-7 line restates it.

**Fix.** Declare each anomaly kind's sources once, as `ANOMALY_SOURCES` beside `ANOMALY_KINDS`. Render
a Coverage fact such as `tool-call anomalies judged {yes-no}` from the same `COUNTED_STATES` test the
counts use, or render the count as `-` for the unjudged kinds. Name both kinds in the Skill's
paragraph.

**Left-shift.** One arm iterates `ANOMALY_KINDS` against the declared sources in both directions, and
renders a not-counted model through each kind whose source is the transcripts, expecting the marker.
This is the class-level gate the fold's render arm stopped short of. It enumerated five facts where it
could have enumerated a table.

### R2-L1 — a visit places another node's run here (LOW)

**Where.** `tools/runlog/model.py:1691`: `own_driver = sum(len(i["lines"]) for i in seg)`.

**Defect.** The L2 fold's rule is that only the run's own lines place it on this node. A read-only
visit is not one of the run's own lines. For a build's last run, `seg_end` is None, so a `--status`
made on node a after node d's run landed puts two lines in `seg`, and `own_driver` becomes 2. With the
run's parked rows, LANDING write and LANDED move all inside a window after node a's journal epochs, the
driver, gates and pushes then read `dead`: the L2 symptom again, reintroduced by one read. The fold's
last commit, `ff436b64`, named the visit "inside another node's run" in the README (`:424-425`). This
case comes after the run, lasts forever, and is not named.

**Fix.** Count only claiming calls: `sum(len(i["lines"]) for i in seg if check_tree_claim(i))`, or the
read-verb constant R2-M1 introduces. Replace the README sentence rather than adding a second one.

**Left-shift.** Add a post-landing `--status` made on the viewing node to the L2 arm. It expects
`not-local` for all three journals.

### R2-L2 — the spec-mark split reads the era, not the window (LOW)

**Where.** `tools/runlog/model.py:1392` sets `era_end_rev` to HEAD for a build's last run, or to
`<next>^`. `:1638-1645` counts every section 8 mark at that rev beyond the `start^` baseline as
`inside`. `tools/runlog/record.py:738-739` renders `owner-inside` and `agent-inside` into the
committed record.

**Defect.** Spec 8 S4 splits marks by whether their commit falls inside the window, and S2 names only
the run-state history and the review records as reads left to the era. A RESOLVED mark added after the
run's end therefore counts as decided inside it: up to HEAD for a build's last run, and up to the next
run's start otherwise. Rev-8 left this for round 2 because "bounding the split changes S12's calls".
That reason does not hold. S12 counts git processes, and a spec blob requested at each record commit
rides the one `cat-file --batch` like every other request.

**Reached by.** Any re-render, or any Skill answer given after a later spec edit. Records rendered
right at the close or at `--landed` are barely affected.

**Fix.** Request each spec at every record commit in the same batch, and take the split at the last
record commit at or before the window's end. The disposition rule makes this a fold, and the fold
should change the code rather than amend S4 to match it, since the reason for leaving the code no
longer stands.

**Left-shift.** An arm with a RESOLVED mark committed after the window. It expects the mark not
counted inside, with the git-call count still 6.

### R2-L3 — the reconcile dropped the tick's guard (LOW)

**Where.** `tools/unattended/SKILL.template.md:29-31`, from merge `de64de53`.

**Defect.** The build's paragraph told the agent to make the tick's call only once the run-state file
exists. The resolution took main's text instead, which says "before `--preflight` no slug exists and
the tick does nothing", and then made that tick the run's heartbeat. On the slug path the slug is known
before `--preflight`. `print_audit` refuses with check 51 when there is no `RUN.md`
(`tools/unattended/unattended.sh:3018`). On a build whose previous record is terminal, it refuses with
a message saying the keepalive "should have been reaped" (`:3021`). So a tick before preflight
journals a refusal where the Skill promises a heartbeat, and on a re-run build it tells the agent to
reap the keepalive `--preflight` is about to need.

**Reached by.** A tick firing while a slug-path session sits between scheduling and preflight. That
window is narrow, which is why this is LOW.

**Fix.** Restore the condition: the tick runs `--audit <slug>` only once this session's `--preflight`
has written the run's record. Add that a check-51 refusal before then is expected and is not a signal
to reap. The Resume section's replacement job (`:733-735`) already states the condition correctly.

**Left-shift.** File the reconcile under `fold-text-is-unreviewed-surface`: a merge resolution that
keeps one side's sentence and the other side's mechanism is fold text no round reads unless it is
named in scope, as it was here.

### R2-L4 — three copies still list three blind verbs (LOW)

**Where.** `tools/runlog/README.md:229-231` ("Those three can run from any tree") and `:430-431`, and
`memory/map/features/runlog.md:114`. The constant is `tools/runlog/model.py:91`, and spec 8 rev-11
added `--audit` to it.

**Defect.** This is `two-answers-to-one-question`. The kit README is where an adopter learns which
calls claim a tree. It now says a keepalive tick's `--audit` from the primary tree claims it, which is
the H2 misreading the rule exists to prevent. Only `model.py` and `selftest.py` read the constant, and
`8096c38c` touched only the fixture.

**Fix.** Point at `TREE_BLIND_VERBS` rather than listing its members, in all three places. The
model's own `METHOD["trees"]` already interpolates the constant (`model.py:152-154`), and that is the
pattern to copy.

**Left-shift.** With pointers there is no copy left to gate. If a list has to stay, add a selftest arm
that reads the named verbs out of each sentence and compares them with the constant in both
directions.

### R2-L5 — drift-audit's conf reader keeps the quotes (LOW)

**Where.** `tools/drift-audit/drift_report.py:114-117`, consumed by this build's signal at `:1868`.

**Defect.** A value is unquoted only when its first and last characters match. So
`MEMORY_ROOT="memory"  # note` reads as `"memory"`, while bash, the memory-tree engine and the fold's
runlog reader all read `memory`. A skeptic reproduced this. Every drift signal then globs a
`"memory"/builds/` path. This build's `run_records_nonterminal_but_merged` reports DEAD PROBE, and the
other signals go blind. The failure is loud and report-only.

**The fold's Decided line on this** (`1691ef73`) calls the reader "outside this build's diff and
version". The reader is outside the diff, but the defect reaches the signal unit 13 shipped. And the
severity rule has no park route, so a LOW is folded.

**Fix.** Port `_read_conf_key`'s rule. A quoted value ends at its matching quote, and an unquoted value
ends at a `#` that begins a word. The fold goes into spec 13, with drift-audit's version step.

**Left-shift.** Add `KEY="v"  # note` and `KEY='v' # note` to drift-audit's bash-sourcing parity
fixture (`tools/drift-audit/selftest.py:117-126`), graded by bash.

## The known residue, adjudicated

1. **The B1 class, two more paths.**
   - **The killed-verb path is CONFIRMED** as R2-H1, and the finders widened it to a killed bar's
     `NONE` row.
   - **The manual `/compact` path is not among the confirmed reports**, so it is outside the tally.
     This synthesis measured it anyway. This clone's store holds 44 main-session compactions across 31
     extracts, and 10 of them are manual. For each manual one, the nearest owner turn lies between
     0.4 s and 142 s from the compaction row, and one of the ten lies within a second. The row does
     not render its trigger, so a manual compaction reads as an automatic one. Placing the owner's
     command therefore takes the owner-turn count and inference, not a derivation.
   - **The synthesis sizes it** as a residue of R2-H1's class at coarser precision. The one case
     within a second is the refusal's evidence-loss branch again, and every case lies inside the
     fold's own 900-second guard. It belongs in R2-H1's promoted unit, not in a separate finding.
2. **The H2 class, the session key.** CONFIRMED as R2-M1, sized MEDIUM. The park in the unit 8 ledger
   gave three reasons. The first, that no review had confirmed it, is now false. The second, that M1's
   slice would rework those facts, has been spent. The third, that spec 8 would need a rule no audit
   has read, is what a fold's rev-N line and the next audit are for.
3. **The S4 spec-mark split at the era's end.** CONFIRMED as R2-L2, sized LOW. The rev-8 reason for
   deferring it is refuted above: the fix adds blobs, not processes.
4. **drift-audit's `load_conf` quotes.** CONFIRMED as R2-L5, sized LOW, and disposed by the severity
   rule as a fold despite the fold's Decided line.

## The fold's deliberate departures, assessed

Each departure is a Decided trailer in the range.

1. **Idleness is judged only when the transcripts read `present`** (`fce435b3`). The direction stands.
   A `partial` transcript does hide a session's calls, and the driver knows no owner turn. The
   predicate is wrong, though: `present` must mean the sources cover the window, not that they exist.
   That gap is R2-B1.
2. **A merge naming only the slug moves no window end** (`c116ffe1`). This stands. A subject is text
   anyone's commit can carry, which is the shared-location class. It has a cost, which the README
   (`:209-210`) states the rule for but not the consequence of. A run that reconciles and then dies
   has its window close before that merge, and the merge drops off its timeline. Not counted.
3. **Transcript events do not move a non-terminal end** (`0cfce210`). This stands, and it also avoids
   a circularity, since the sessions are named from the window. Its reason, that the rendering
   session keeps working after the run, is equally a reason against read-only visits moving the end.
   The fold applied it to one source and not to the other. That is R2-M1's window half.
4. **The claim rule is wider than preflight plus unit-bearing verbs** (`0cfce210`). This stands for
   `--phase`, `--close` and `--park`, which do run in the run's own tree. But the rule is a DENYLIST:
   a verb nobody classified claims its tree. The reconcile demonstrated it. `--audit` arrived from
   main as a claiming verb, and it was caught only because someone read the join, while the prose
   copies were not caught (R2-L4). Recommended: a source arm, like `test_model_driver_sets`, that
   reads the driver's dispatch labels and requires every verb to be named either blind or claiming,
   in both directions, so the next verb main adds reds until it is classified.
5. **The hold ends at the next run's claim** (`0cfce210`). This stands. No confirmed finding disputes
   it, and the README names its residue, two runs claiming one tree in one stretch.
6. **No schema-leg rule for M6** (`1691ef73`). The reason is sound: spec 10 section 3 keeps content
   truth out of the leg. But the render arm that replaced the rule enumerated five facts and idle
   gaps, and R2-M2 is the sibling it did not enumerate. The class-level left-shift needs no schema
   leg. It needs a declared source per Summary fact and per anomaly kind, driven through the renderer
   by one arm.

## The second reconcile's semantic joins, assessed

- **The tick in `tools/unattended/SKILL.template.md`.** Choosing main's `--audit` probe as the one tick
  and the heartbeat stands, because the driver journals every verb except `--version` and `--plan`
  (`tools/unattended/unattended.sh:5469-5470`). The resolution dropped the run-state-file condition,
  which is R2-L3. The two sentences appended to main's paragraph also run past the file's wrap width.
  That is cosmetic and not counted.
- **The conf defaults in `tools/unattended/unattended.sh:336-343`.** These are sound. Main's
  `SPEC_TOKENS_CLI`, `UNIT_STALL_BOUND` and `REVIEW_ROUNDS` keep their defaults on the two lines the
  `-A1` source arm reads. `RUNLOG_SESSION_VARS` defaults beside them, and `GOV_RUNLOG` is copied
  before the conf is sourced, so a committed conf cannot switch off the run's own log. No finding.
- **The protocol trim in `tools/unattended/PROTOCOL.template.md:268-274`.** The paragraph kept the
  skipped verbs, the END's fields, the evidence-never-input rule, the switch, the session key and
  render-by-Skill. It dropped three facts: that a START with no END is a killed call, that the log is
  never tracked or pushed, and the three render placements. The first survives in the driver's header
  (`unattended.sh:5205-5207`), and the third in the unattended Skill. The `RUNLOG_SESSION_VARS` row
  dropped "an unset one writes nothing". None of these is a defect in what ships. It does move
  contract text into its implementations. Not counted.
- **`--audit` in `TREE_BLIND_VERBS` and `HEARTBEAT_VERBS`.** Sound. `8096c38c` staged RED on each
  set, and both stalled-streak fixtures fire. The copies left behind are R2-L4, and the denylist shape
  is departure 4.
- **The sixth exemption in `tools/unattended/runlog-writer.test.sh`.** Sound. `8096c38c` also replaced
  a typed "all five" with the list's own length, which is the charter's rule against typing a count of
  a derived population, applied.
- **`37d4b899`.** Sound. The budget row went from 69 s to 93 s, from a worst reading of 62 s times the
  file's 1.5.

## The build-pass spec text

Ten specs carry a section 9 line the build pass wrote:

- units 1, 2, 3 and 6 at rev-5 and rev-6;
- units 4, 8, 9, 10, 11 and 13 at rev-5.

Unit 5's build-pass line is its rev-3. Units 7 and 12 carry none. Round 1 traced two defects to build-
pass text, M2 and M5 in spec 8's rev-5, and both were folded.

No confirmed round-2 finding traces to a build-pass line. The confirmed findings trace to fold and
reconcile text instead:

- R2-B1 to spec 8 rev-6, "only where the transcripts read `present`".
- R2-H1 to spec 9 rev-6, which refuses a time "in an owner turn's second".
- R2-M1 to the narrowing in spec 8 rev-7 and rev-8.
- R2-L1 to rev-10.
- R2-L2 to rev-8's "left to round 2".
- R2-L4 to rev-11.
- R2-L3 to the merge.

Because the refuted reports were not handed over, the zero for build-pass text is a result of this
lens set and not evidence of absence.

## The fold, checked against round 1

"No confirmed finding" below means the lens set confirmed none against the fold of that item. It is
not this synthesis's certificate that the item is closed, except where a measurement is cited.

| Round 1 | Fold | Standing after round 2 |
|---|---|---|
| B1 | idle gaps never beside an owner turn, and a render refusal | The instance is closed. The class is open through R2-B1 and R2-H1 |
| H1 | idle gaps over every source | Measured closed on this build's live model: 0 idle gaps where round 1 had 23. R2-B1 brings it back after a stale extract's cut |
| H2 | trees a run holds | No confirmed finding against the tree key. Its siblings are R2-M1 (sessions) and R2-L1 (placement) |
| M1 | attribution inside the window | Measured: attributed-call population 7702 equals the model's 7702 in-window tool calls |
| M2 | pushes proof at the window's end | No confirmed finding |
| M3 | a close is a clean END | No confirmed finding. R2-H1 is the unclean END's time, not its rc |
| M4 | own commits bounded by the window | No confirmed finding |
| M5 | non-terminal end over every owned source | Measured: 0 of 163 timeline events outside the window, and gates `partial` with 3 lines where round 1 read `absent`. R2-M1 is the visit edge |
| M6 | unknown counts render `-` | No confirmed finding against the five facts. The sibling is R2-M2 |
| M7 | the runlog conf reader | No confirmed finding. drift-audit's copy is R2-L5 |
| L1 | a typed URL never reaches the push journal | No confirmed finding |
| L2 | `not-local` on the run's own lines | The visit edge is R2-L1 |
| L3 | a moved root refused by name | No confirmed finding |
| L4 | one slug grammar | No confirmed finding |
| L5 | a range names every unit | No confirmed finding |

## Synthesis observations, outside the tally

These are not skeptic-verified, are not in the finding table, and are not counted in the verdict.

- **O1: an operational hazard for this run's own close.** Until R2-B1's unit lands, any render of
  this run on node `d` reads the store extract written 2026-09-16 instead of the live transcript.
  Refreshing it immediately before a render, or removing it, avoids the stale read. Because R2-B1 is
  promoted, its unit must close before this run can, so the hazard applies only to renders made
  before that.
- **O2: widening the refusal is not free.** Round 2's finders proposed a band around owner turns for
  every UTC. Every verb row that answers an owner turn within a few seconds would then refuse the
  record. That trades a leak for evidence loss, the other branch of R2-H1. The band belongs on the
  row kinds an owner act causes, with the model holding those rows, as R2-H1's fix says.
- **O3: the reconcile moved contract text into implementations**, as described under the protocol
  trim. If the protocol's cap forces the trim again, prefer a pointer to the runlog kit README's model
  section over silent omission.

## What this synthesis re-derived

Everything below was measured in this worktree at `37d4b899`, on a clean tree:

- Every file:line in the table and in the findings, read at that commit, including the merge
  resolutions through `git show --cc de64de53` and `git diff de64de53^1 de64de53`.
- The ranges: `36d531b9..ff436b64` holds 23 commits and changes 42 files, +3897/−374. The bug-class
  checklist selects 27 classes: 22 by anchor, 5 universal.
- The model, built through `build_run_model` both with this clone's store and with no store:
  - run 1 of 1, phase VERIFYING, non-terminal, closed by last-activity;
  - driver `partial` with 70 lines, gates `partial` with 3 lines, pushes `absent`, transcripts
    `present`;
  - one named session, and one store extract for it, written 2026-09-16, whose newest event is after
    the current window end;
  - identical answers with and without the store: idle gaps judged with 0 gaps, owner turns launch 1,
    pre-run 1, in-window 5 and post-close 0, 7702 in-window tool calls with 7702 in attribution's
    population, and 8 anomalies of the kinds `destructive-git` and `red-behind-zero`;
  - 6 git calls, and 0 of 163 timeline events outside the window.
- The record, rendered in memory and not written: 23890 bytes, reading
  `anomalies: 8 · shown 8 · aggregated no` and `idle gaps: judged yes · near an owner turn 1`. No
  refusal.
- R2-B1's staleness, by copying the session extract into a scratch store cut at 25%, 50% and 75% of
  the window: transcripts `present` each time, idle gaps 5, 2 and 2, two gaps inside the 900-second
  guard, one gap ending within 120 s after a real in-window owner turn, in-window owner counts 2, 3
  and 3, and no refusal.
- The compaction residue, over this clone's 31 store extracts: 44 main-session compactions, 10
  manual, with nearest-owner-turn distances from 0.4 s to 142 s; and 2 interrupt-class owner turns.
- The spec revision lines named under "The build-pass spec text", and the Decided trailers of every
  commit in the range.
