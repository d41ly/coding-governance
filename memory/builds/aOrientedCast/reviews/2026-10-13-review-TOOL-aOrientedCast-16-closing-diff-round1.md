**Serves:** diff-review TOOL-aOrientedCast-16 TOOL-aOrientedCast-17 TOOL-aOrientedCast-18 TOOL-aOrientedCast-19 TOOL-aOrientedCast-20 TOOL-aOrientedCast-21 TOOL-aOrientedCast-22 PLAY-aOrientedCast-2 PLAY-aOrientedCast-3

# Tier-2 closing diff review — aOrientedCast addenda 2 and 3, ROUND 1

*Round 1 of the closing review (BUILD-METHOD M8) of aOrientedCast's second and third owner
addenda: units TOOL-aOrientedCast-16 to -22 and PLAY-aOrientedCast-2 and -3, built on local main
53b25884. The roles kit's agents now cite the charter's section 1 rule tags and carry its Protocols
and Facts sections. Roles declare `mandatory` and `output`, and the playbook renders a derived
ROLE_ROSTER from them. An inline stand-in for a role needs an owner waiver row, graded as R15. The
charter gains the `[roles]` and `[agents]` rules, a generated Agent roles section, the `agent` and
`returned` micro-formats and a 20480-byte ceiling. `handoff.py agents` derives dispatch and return
lines into a per-build agent ledger, format-guard refuses a final message that drops one, and
gate-guard refuses AskUserQuestion from a session holding a live unattended run's lease. Node `a`,
2026-10-13.*

Reviewed range: `53b258844a56b00b4489405aff7cd575e4a80b37...4795172cba8a5817df9e70d09d6f29d89f4cc024` · ROUND 1

## Verdict: CLEAN WITH FIXES

No blocker and no high survived. Fourteen findings were confirmed and two refuted, and they come
down to fourteen items: seven medium and seven low. The worst behavioural defects are two false
outcomes in the new guards. gate-guard refuses AskUserQuestion to a session whose run has already
landed in place (M3), and format-guard trusts tool-use ids quoted inside an agent's own result text
(M1). A third lets a final message drop its agent lines silently after a Skill call (M2). Three
mediums are persisted-coverage gaps in the new checks. Every item below carries its fix and a
left-shift gate suggestion.

## Review shape

Intensity full, raw 16, confirmed 14, refuted 2, unverified 0 (0 uncertain), precision 0.88.

| lens | returned | raw | confirmed | refuted | uncertain | unverified | precision |
|---|---|---|---|---|---|---|---|
| security | yes | 2 | 1 | 1 | 0 | 0 | 0.50 |
| correctness | yes | 2 | 2 | 0 | 0 | 0 | 1.00 |
| seams | yes | 3 | 3 | 0 | 0 | 0 | 1.00 |
| verification | yes | 4 | 4 | 0 | 0 | 0 | 1.00 |
| intent | yes | 5 | 4 | 1 | 0 | 0 | 0.80 |

Adjudicated tally by item: 0 blocker, 0 high, 7 medium, 7 low. By raw confirmed finding: 0
blocker, 0 high, 7 medium, 7 low. No two confirmed findings describe one defect, so every item
holds exactly one id. Ids 5 and 11 share `gate-guard.js:702` but are different defects: id 5 is a
wrong refusal, and id 11 is a missing test arm.

### Run integrity

- Lenses: 5/5 returned, 0 died.
- Skeptic batches: 4/4 returned, 0 died.
- Verdicts: 0 contradictory verdicts demoted to unverified, 0 spurious verdicts discarded, 0
  duplicates.
- Fixes on confirmed findings: 14 judged sound, 0 judged unsound, 0 none proposed, 0 not judged.
- Severity on confirmed findings: 0 ungraded by the skeptic, 3 re-graded by the skeptic (ids 3, 5
  and 8, each high to medium).
- Unverified findings: 0 answered uncertain, 0 with no usable verdict.
- Lens notes: none supplied, so every lens ran on the kit's generic brief.

Every counter that matters is zero, so this run is complete. Roles: the finders ran as
gov-diff-reviewer, the skeptic batches as gov-skeptic, and the synthesis as gov-synthesizer. Nine
spec documents were supplied as `specs`, beside the range's commit messages. The checklist held 36
items, each assigned to exactly one lens: security 8, correctness 7, seams 7, verification 7,
intent 7. By-design items came from the caller's byDesign. The stated security model holds that the
hooks guard an LLM's own tool calls, fail open on unreadable input, and are no boundary against a
hostile user, so every hook finding below is graded as a wrong refusal or a missed refusal, not as
a breach.

## Findings

### M1 [medium] — format-guard reads tool-use ids from the agent's own result text (id 1)

`tools/hooks/format-guard.js:355`. The agent arm builds `note` as JSON.stringify of the whole task
notification (lines 349-355) and matches every `<tool-use-id>` tag in it. That includes the
`<result>` body, which is the sub-agent's free text. A real notification puts its header
(`<task-id>`, `<tool-use-id>`, `<output-file>`, `<status>`, `<summary>`) before `<result>`. When a
returning agent quotes the id of another real Agent call from this session, `readResult` resolves
it from the transcript, and the turn is made to owe a `returned` line for an agent it did not
receive. A quoted Workflow call's id makes the turn owe both lines for every agent of that run. The
Stop is refused once on that false requirement, and the model is pushed to print `returned` lines
for agents that may not have returned. The quote must be a real id from this session. None of 4018
sampled real notifications quote one, so the path is narrow, but reviewer and researcher agents
quote transcripts often.

- Fix (judged SOUND by the skeptic): read only the notification's header. Take the first
  `<tool-use-id>` that comes before `<result>`, or cut everything from `<result>` to the last
  `</result>` before matching.
- Left-shift gate: a `format-guard.test.sh` arm in which a notified agent's result quotes another
  call's tool-use id, asserting that no line is required for that call.

### M2 [medium] — a Skill call mid-turn hides the turn's earlier agents (id 3)

`tools/hooks/format-guard.js:284`. `scanTurnRecords` opens the turn at any typed user record.
`checkTyped` (lines 265-270) accepts any non-sidechain `user` record holding text blocks and no
tool_result, with no `isMeta` or `isCompactSummary` exclusion. After every Skill call the harness
inserts an `isMeta: true` user text record ("Base directory for this skill: …"), and 304 such
records exist in real transcripts. Scanning backward, that record becomes the opener, and the scan
stops at the Skill tool_use. An Agent or Workflow dispatched earlier in the same turn therefore
falls outside the scanned turn. A probe with owner prompt, Agent call and completed result, Skill
call, its result, the isMeta record and a final message gave `{"required":[],"witnesses":[]}`. The
same transcript without the Skill records required both lines. A final message that drops its
`agent` or `returned` line passes silently, and the header's NOT-CHECKED list does not name the
gap. The finder graded high. The skeptic re-graded it medium, because the ledger is derived from
the transcripts on its own, so the loss is contained to the chat line.

- Fix (judged SOUND by the skeptic): in `checkTyped`, do not count a record that opens nothing as a
  turn opener. Skip `rec.isMeta === true` records that follow a tool_result (the Skill expansion
  carries the Skill call's id as `sourceToolUseID`), and skip `isCompactSummary` records. An
  alternative is to keep scanning back past a run of openers that sits directly after a
  tool_result. If the gap is kept instead, name it in the header's WHAT THIS DOES NOT CHECK.
- Left-shift gate: a `format-guard.test.sh` arm with the Skill-mid-turn transcript above,
  expecting a block that names the agent.

### M3 [medium] — gate-guard refuses a question to a session whose run already landed (id 5)

`tools/unattended/gate-guard.js:702`. `checkAsk` decides that a leased run is live by testing its
`phase:` fact against the pair LANDED and ABORTED. The driver's `derive_liveness`
(`unattended.sh:8722-8731`) also treats a LANDING record as TERMINAL when the landed log names its
landing commit, and a HELD hand-off whose commit is on the advertised tip. Under in-place landing
the committed record keeps `phase: LANDING` permanently. Reproduced: an AskUserQuestion payload for
session abecbd71 was refused with "this session holds the lease of the unattended run
aBatchedMinors, at LANDING" and exit 2, while `.git/unattended/landed.aBatchedMinors.log` names
35438ba0 landed on main and `unattended.sh --liveness aBatchedMinors` prints `verdict: TERMINAL`.
aBenchedProbe and aHalvedInstall are in the same state. Such a session can never ask the owner
anything again, its remedy tells it to `--park` a finished run, and stop-guard gives the opposite
answer about the same run. The finder graded high. The skeptic re-graded it medium, because the
effect is a false refusal with a misleading remedy, and no wrong result or data loss ships.

- Fix (judged SOUND by the skeptic): use the driver's liveness answer instead of re-deriving it.
  Treat a lease as live only when `unattended.sh --liveness <slug>` returns a verdict other than
  TERMINAL, the way stop-guard's `runLiveness`/`parseLiveness` does, and fail open when that probe
  cannot be read. An alternative is to keep the phase test but also treat a LANDING record as
  terminal when `<common-dir>/unattended/landed.<slug>.log` holds a line naming its landing commit.
- Left-shift gate: a `gate-guard.test.sh` arm that stages a LANDING record with a matching
  landed-log line and asserts exit 0, observed RED against the current code before the fix lands.

### M4 [medium] — handoff.py and agent-cap normalise the marker line differently (id 6)

`tools/roles/handoff.py:815`. agent-cap's rule 6 (`agent-cap.js:2121`) admits a handoff prompt
after folding CRLF and trimming both ends, so a prompt that opens with a blank line before the
marker is admitted. `handoff.py agents --handoff` compares only the raw first line, with a trailing
`\r` removed, against the marker. For `'\n<marker>\n\n## Task…'` that first line is empty, so
`handoff.py` exits 1 with "no Agent call … opens its prompt with the marker line". format-guard
(`format-guard.js:374-375`) still requires an `agent` line for that dispatch and tells the session
to paste what `handoff.py agents --handoff` prints. The tooling remedy fails, the only way out is a
hand-typed line that the charter's `[agents]` rule forbids, and the dispatch never reaches the
agent ledger. The finder's second case, a trailing space after `-->`, does not hold: agent-cap's
`HANDOFF_MARK_RE` ends in `-->$`, so rule 6 denies that call and no such dispatch exists. The path
needs the model to prefix a newline, so the effect is contained.

- Fix (judged SOUND by the skeptic): use agent-cap's normalisation in the matcher. Compare
  `prompt.replace('\r\n','\n').strip().split('\n')[0].rstrip()` against the marker line.
- Left-shift gate: a `handoff.py` self-test arm whose prompt has a leading blank line before the
  marker, asserting it matches. The finder also proposed a trailing-space case in the same arm.
  Since agent-cap refuses that prompt, the arm should assert only that the two readers agree on it.

### M5 [medium] — the new check_roles rules and the stand-in refusal have no fixture arm (id 8)

`tools/roles/check_roles.py:360`. None of the rules this diff adds to `check_roles.py` has a
persisted arm in any suite: R13, R14, R15, and R0's new MEMORY_ROOT refusal. Neither does
`handoff.py`'s `--stand-in` refusal (`handoff.py:1007-1015`). The only gate that runs the checker
is the `roles catalogue` leg (`gate-legs.json:1647`), and it grades gov's own tree, where R15's
population is empty. Gov has no `memory/project/role-stand-in-waiver.txt` and no `*-stand-in.md`,
and `git ls-files | grep -i stand-in` prints nothing. R15 could stop emitting defects, R13 or R14
could never fire, or `--stand-in` could stop refusing, and every leg would stay green. The `roles
catalogue` leg reads as certifying the waiver rule but has never run it on a non-empty population.
Specs 17 and 19's staged breaks were one-off observations with floor `none`. The finder graded
high. The skeptic re-graded it medium: a regression could land green, but no wrong result ships
now. R1 to R12 also lack fixture arms, which suggests a convention rather than a slip unique to
this diff.

- Fix (judged SOUND by the skeptic): add a `--selftest` to `check_roles.py`, or arms in
  `adopt-roles.test.sh`, that build a scratch tree and assert each of the following.
  - A tailed stand-in handoff with no waiver row gives exit 1 with one R15 line naming it.
  - Adding the row gives exit 0 with one `stand-in waiver` note.
  - A row with no declaration gives a stale R15.
  - Each malformed row kind from spec 19's AC1 gives its own R15 line.
  - A conf with no MEMORY_ROOT gives exit 2.
  - A mandatory role under a hookless entry with no `unenforced — ` clause gives R13.
  - A spec writer whose `output` omits its folder gives R14.
  - `handoff.py render --stand-in` with no row exits 1 and writes no file.

  Raise the floor by the count.
- Left-shift gate: observe each arm RED against its staged break before landing. Add the class
  "a check run only over a population that is empty in the gate's tree" to the section 10
  checklist.

### M6 [medium] — `handoff.py agents --run` has no persisted check (id 9)

`tools/roles/adopt-roles.test.sh:223`. Arm 9 writes a Workflow call, run `wf_00000001-aaa`'s
journal and the transcripts and meta files of agents a2 and a3 (lines 208-217), but its only two
`agents` invocations (lines 223 and 227) both pass `--handoff`. Nothing in any suite runs the
`--run` branch of `print_agent_lines` (`handoff.py:829-865`). That branch covers journal parsing,
unit from label, build from slug, the session card fallback, the prompt link from `briefPath`, and
the `committed <sha>` and failed outcomes. It is the route every unattended unit agent takes, and
the one format-guard's refusal tells the main loop to use. A regression there would print wrong,
`unknown` or no lines and stay green. Spec 20's AC3, AC4 and AC6, including the second-ledger
refusal, were likewise observed only once.

- Fix (judged SOUND by the skeptic): in arm 9, run
  `handoff.py agents --run wf_00000001-aaa --session "$A9S"` against the fixture already written.
  Assert AC2's three exact lines: a2's `agent` line, a2's line
  `- returned — gov-builder · committed abc123def · 45s · 1.5k out · run wf_00000001-aaa/a0000000000000002`,
  and a3's `agent` line with `commit:specs:tFix`, writes none and gates none, with no `returned`
  line for a3. Then assert the ledger gained exactly those three. Raise FLOOR_ASSERTIONS to match.
- Left-shift gate: the arm above. A fixture written by a test arm but read by none of its
  assertions is a signal worth a reviewer checklist line.

### M7 [medium] — three live routes of format-guard's agent arm are untested (id 10)

`tools/hooks/format-guard.js:352`. Three real routes have no arm. The first is a notification
delivered through a `queued_command` attachment (around line 352). This session's own transcript
holds eight. The second is a foreground Agent result with status `completed`, which owes a
`returned` line (line 376). The third is a Workflow result that is not `async_launched` (line 378).
Every scenario in `format-guard.test.sh` (lines 322-329) uses an `async_launched` result and a
user-record notification. Deleting the queued_command branch, deleting
`if (r.status === 'completed') addRequired('returned', …)`, or hard-coding `addRun`'s
`withReturned` to false each passes all 28 new assertions. The hook would then silently stop
requiring the `returned` line on those live paths.

- Fix (judged SOUND by the skeptic): add three `write_transcript` scenarios.
  - A turn whose notification arrives as `{type:'attachment', attachment:{type:'queued_command', prompt:'<task-notification>…<tool-use-id>t1</tool-use-id>…'}}`.
  - An Agent result `{status:'completed', agentId:'a1'}` in the same turn, which owes both lines and
    blocks on only the `agent` line.
  - A Workflow result with no async status, which owes the journal's `returned` lines at dispatch.

  Assert block and allow for each, and raise FLOOR_ASSERTIONS by the count.
- Left-shift gate: the three arms above, each observed RED against its named mutation.

### L1 [low] — format-guard's header and README misstate the parse-failure rule (id 4)

`tools/hooks/format-guard.js:48`. The header (lines 47-49) and `tools/hooks/README.md:457` both say
that unparsable lines in the turn "each allow the arm with one witness line". The code (`checkStop`,
around line 469) writes one combined witness, `N line(s) … did not parse and were skipped`, and
still grades the parsed records. A probe with one torn line still blocked. The code matches spec
21's Degraded inputs section; only the two docs are wrong. A maintainer trusting them would expect a
damaged transcript to allow.

- Fix (judged SOUND by the skeptic): reword the header and the README. An unparsable line in the
  turn is counted into one witness line and the arm still grades the parsed records. Only a missing
  `transcript_path`, an unreadable transcript or journal, or a run id off its shape allows the arm.
- Left-shift gate: none mechanical. A reviewer checklist line asking that a hook header's
  degraded-input list be read against the spec's Degraded inputs section.

### L2 [low] — the unattended README says the widened matcher waits for a restart (id 7)

`tools/unattended/README.md:111`. The new paragraph says "A session started before the settings
merge keeps the narrower matcher until it restarts." Hooks settings are re-read on the next tool
call, as `memory/gotchas/settings-edit-takes-effect-mid-session.md` records from a 2026-08-10
measurement. So once the settings merge widens gate-guard's matcher to AskUserQuestion, an
already-running session is guarded from its next call. Spec 22 lines 191 and 228 repeat the claim,
and AC7's "after the merge and a restart" depends on it. Operators are told an in-flight session is
unguarded when it is not. Behaviour does not change.

- Fix (judged SOUND by the skeptic): say the widened matcher applies to every session, including one
  already running, from its next tool call, citing the gotcha. Drop "and a restart" from AC7's
  precondition in the spec.
- Left-shift gate: none mechanical. Spec review should check claims about hook timing against the
  gotchas folder.

### L3 [low] — gate-guard's absent-phase filter and fail-open catch have no arm (id 11)

`tools/unattended/gate-guard.js:702`. `run-lease.js` `scanLeases` (line 161) reports a record with
no `phase:` line as `'absent'`, and `checkAsk` (lines 695-704) filters those out so the leaseholder
may ask. The fail-open catch around `checkAsk` is the second behaviour. Q1 to Q6 in
`gate-guard.test.sh` (lines 568-584) cover BUILDING, HELD, LANDED, ABORTED, a session that reads
absent and a missing conf. No fixture drops the phase line, and none makes `checkAsk` throw.
Dropping the filter would red nothing. This is a test gap with no behaviour defect.

- Fix (judged SOUND by the skeptic): add a Q arm that runs `build_fixture BUILDING`, deletes the
  `phase:` line with sed, and asserts that the leaseholder's AskUserQuestion exits 0 with empty
  stderr. Count it in FLOOR_ASSERTIONS.
- Left-shift gate: the arm above, observed RED with the filter removed.

### L4 [low] — a third reader of the micro-format fence re-derives it differently (id 12)

`tools/roles/roles_lib.py:226`. `extract_microformat_shapes` (lines 220-234), new in this diff,
finds the fence markers with a substring `text.find` and keeps the first definition of a repeated
head (`setdefault` at line 234). `format-guard.js` `readCharterShapes` (lines 167-181) and runlog
`prose.read_charter_shapes` require each marker as a whole line and keep the last definition. A
scratch charter with a second `agent` definition made `roles_lib` and format-guard return different
shapes, so every line `handoff.py agents` derives would be refused at the stop. `check-microformats.sh`
refuses a duplicated fence pair but has no repeated-head check. Today's `AGENTS.md` has neither
shape, so the path is narrow and contained.

- Fix (judged SOUND by the skeptic): read the fence the way the two existing readers do, with whole-line
  markers and the last definition winning. An alternative is to refuse a repeated head in all three
  readers.
- Left-shift gate: a parity arm that feeds one duplicated-head charter to `extract_microformat_shapes`
  and `readCharterShapes` and asserts they return the same definition. A repeated-head refusal in
  `check-microformats.sh` closes the class at the source.

### L5 [low] — spec 21's AC2 names a break the built hook does not report that way (id 13)

`memory/builds/aOrientedCast/spec/2026-10-13-spec-TOOL-aOrientedCast-21.md:277`. AC2's second
clause says a line "with its last field cut" blocks with "does not match its charter shape".
`checkAgentLines` (`format-guard.js:396-415`) treats a row as bare only when its last ` · ` field
ends with `/<agent-id>`. Cutting `run direct/a1` therefore reports "no agent line for agent a1,
which this turn dispatched". The suite stages a different break, the run label rewritten to
`direct/a1`, to get the shape message. The spec, closed at rev-1, was never amended; the deviation
lives only in commit 6fb62ffa5's Decided trailer. A close run literally against AC2 reds.

- Fix (judged SOUND by the skeptic): amend AC2 in a rev-2 to say what the build does. A bare line
  that ends `/a1` but drops a middle field reports "does not match its charter shape", and a line
  with its run field removed reports "no agent line". Name the suite's staged break as the
  observation.
- Left-shift gate: a close-time check that every Decided trailer recording a criterion deviation
  is matched by a spec revision.

### L6 [low] — spec 22's AC6 grep always matches the records (id 14)

`memory/builds/aOrientedCast/spec/2026-10-13-spec-TOOL-aOrientedCast-22.md:263`. AC6 says
`git grep -l "gov:kit unattended@1.104"` prints nothing, but the command has no pathspec. At
4795172cb it lists the spec itself, which quotes the string at lines 198 and 263, and the unit's
acceptance ledger. So the criterion never holds for a correct build, and reading it loosely would
also miss a real carrier left at 1.104.

- Fix (judged SOUND by the skeptic): add a pathspec that excludes the records, for example
  `git grep -l "gov:kit unattended@1.104" -- ':!memory/builds'`, or list the carrier paths
  (`tools/unattended`, `memory/guides`, `.claude/skills/unattended`) as TOOL-20 AC9 and TOOL-21 AC9
  already do.
- Left-shift gate: spec review should refuse a "prints nothing" grep criterion whose pattern the
  spec itself quotes without a pathspec.

### L7 [low] — the roles dossier understates the kit's outside contracts (id 16)

`memory/map/features/roles.md:124`. The Constraints bullet, rewritten in this diff, says the
section 1 rule lines and the Protocols and Facts sections "are the only contract read from outside
the kit". TOOL-aOrientedCast-20 added `roles_lib.extract_microformat_shapes`, which reads the
governing doc's `<!-- microformats -->` fence, and `handoff.py agents`, which reads session
transcripts, subagent meta and workflow journals. The dossier's own line 61 describes those shapes
being filled. The next change to the fence or the transcript fields looks safe to whoever trusts
the dossier. This is documentation only.

- Fix (judged SOUND by the skeptic): extend the bullet to list every outside contract. Name the
  section 1 rule tags and the carried sections (TOOL-16), and the `agent` and `returned` definitions
  in the micro-format fence. Name the transcript, subagent meta and workflow journal fields
  `handoff.py agents` reads (TOOL-20), saying the transcript is a reading, not a contract.
- Left-shift gate: a dossier review step that greps the kit for reads of files outside it and
  compares the list with the Constraints bullet.

review-shape kind=diff-review round=1 intensity=full at=synth raw=16 confirmed=14 refuted=2 unverified=0 blocker=0 high=0 medium=7 low=7 agents=10 out-tokens=191145

## Appendix — every finding

| id | lens | ref | severity | skepticSeverity | verdict | reason | fixVerdict | classes |
|---|---|---|---|---|---|---|---|---|
| 1 | security | tools/hooks/format-guard.js:355 | medium | medium | confirmed | In format-guard.js:349-355 at 4795172cb, `note` is JSON.stringify of the whole notification content, and `matchAll(/<tool-use-id>…/g)` runs over all of it, including the `<result>` body. I sampled a real record: the header (`<task-id>`, `<tool-use-id>`, `<output-file>`, `<status>`, `<summary>`) comes before `<result>`, and the result holds the agent's free text. A quoted id that names a real Agent or Workflow call of this session is resolved by `readResult` from the session's own transcript line. It then adds a `returned` requirement, or both lines for every agent of the run, for an agent this turn did not receive. The Stop is refused once on that false requirement. The quote must be a real id from this session, because a made-up id resolves nothing. In 4018 real notifications I found none that quote an id, so the path is narrow. Still, the agent's text is unconstrained and the effect is a real wrong refusal, bounded once per turn end. | sound | - |
| 2 | security | tools/roles/handoff.py:585 | medium | - | refuted | The mechanism is real and new in this diff (the base handoff.py has no NOTIFICATION_RE). The non-greedy findall at handoff.py:585 over a result that quotes two complete notification blocks does record the second quoted id. The claimed consequence is a `returned` line for an agent that may still be running, and that needs a quoted notification naming the real tool-use id of a still-running Agent call in this session. No genuine notification record exists for such a call, so it cannot be quoted. Quoting a genuine notification names an agent that did return, with its real status, and the ledger line stays true. Only fabricated text or an id collision gives the wrong record. The quoted text must also be in a notification body: tool_result blocks are not read into `texts`. Typed user strings are the owner's own input, which the security model does not treat as a boundary. I sampled 4018 real notifications and none quote a tool-use id inside `<result>`. I could not establish the consequence on a reachable path, and the finding is graded medium, so it is refuted. | sound | - |
| 3 | correctness | tools/hooks/format-guard.js:284 | high | medium | confirmed | In format-guard.js:265-270, checkTyped returns true for any non-sidechain `user` record whose content holds text blocks and no tool_result. It has no isMeta or isCompactSummary exclusion, and no hook file checks either flag. I found 304 real records with the shape `type:user, isMeta:true, content:[{type:text, text:'Base directory for this skill: …'}]`. Scanning backward, that record becomes the opener. The Skill tool_result before it is pushed, and the assistant Skill tool_use then triggers `checkSpoke` with opener>=0, which breaks the scan. Any Agent or Workflow dispatched earlier in the same turn is therefore outside the turn, and nothing is required. The header's NOT-CHECKED list does not name this gap. Agent then Skill in one turn is reachable. The effect is a silent allow of a final message missing its agent or returned line. That is contained, because the ledger is derived from the transcripts on its own, so I grade it medium, not high. | sound | - |
| 4 | correctness | tools/hooks/format-guard.js:48 | low | low | confirmed | The header at format-guard.js:47-49 and tools/hooks/README.md:457 both say that lines in the turn that do not parse 'each allow the arm with one witness line'. The code (checkStop, around line 469) only pushes one combined witness, `N line(s) of this turn … did not parse and were skipped`, and then still grades the parsed records. Spec 21's Degraded inputs section says a parse failure is 'counted into one witness line' and does not allow the arm. The code matches the spec and both docs misstate it. Behaviour is unaffected. | sound | - |
| 5 | seams | tools/unattended/gate-guard.js:702 | high | medium | confirmed | I reproduced it. Piping an AskUserQuestion payload with session_id abecbd71-... into node tools/unattended/gate-guard.js printed 'BLOCKED by gate-guard: this session holds the lease of the unattended run aBatchedMinors, at LANDING (memory/builds/aBatchedMinors/RUN.md)' and exited 2. That RUN.md has 'phase: LANDING' and 'session: abecbd71-...'. <common-dir>/unattended/landed.aBatchedMinors.log names 35438ba0 landed on refs/heads/main. Running `unattended.sh --liveness aBatchedMinors` printed 'state: terminal' and 'verdict: TERMINAL'. checkAsk (gate-guard.js:695-706) filters only on PHASES_TERMINAL = ['LANDED','ABORTED']. derive_liveness (unattended.sh, around 8722) also treats a LANDING record as terminal when the landed log names its landing commit, so the two guards disagree, as the finding says. The check is new in this diff. Spec 22's F2 chose phase-against-terminal-pair, but nothing in the spec or the by-design list covers an in-place-landed LANDING record. Graded medium, not high: the effect is a false refusal whose remedy (--park) is misleading. It ships no wrong result and loses no data. | sound | - |
| 6 | seams | tools/roles/handoff.py:815 | medium | medium | confirmed | Only half the claim holds. The trailing-space case is wrong. agent-cap's extractHandoffMarker (agent-cap.js:2045) tests each raw line, with CR removed but otherwise untrimmed, against HANDOFF_MARK_RE, which ends in `-->$` (agent-cap.js:2041). '<marker> ' therefore yields zero marks, and rule 6 denies the call ('exactly one is required'), so no such dispatch exists. The finder's probe copied only the got[0] comparison and missed this. The leading-blank-line case is real. For '\n<marker>\n\n## Task...', extractHandoffMarker finds exactly one mark on line 2, and got = prompt.replace(CRLF).trim()... puts the marker at got[0], so agent-cap admits the call. handoff.py:815 then compares str(prompt).split('\n',1)[0].rstrip('\r'), which is '', against marker.group(0) and finds no hit, so it raises 'no Agent call ... opens its prompt with the marker line'. format-guard (format-guard.js:374-375) requires an agent line for every Agent result that carries agentId, so the turn is blocked, and the tooling remedy fails. The code is new in this diff. The path needs the model to prefix a newline, and a hand-typed line passes the format check, so the effect is contained. | sound | two-guards-one-question-two-answers |
| 7 | seams | tools/unattended/README.md:111 | low | low | confirmed | tools/unattended/README.md:111 reads 'A session started before the settings merge keeps the narrower matcher until it restarts.' The diff adds this line. It contradicts memory/gotchas/settings-edit-takes-effect-mid-session.md, which records a 2026-08-10 measurement that hooks settings are re-read on the next tool call and not snapshotted at session start. No gotcha or README in the repo records the opposite. Spec 22 lines 191 and 228 repeat the claim, and AC7 assumes a restart. The error is in documentation only and changes no behaviour, so it is low. | sound | settings-edit-takes-effect-mid-session |
| 8 | verification | tools/roles/check_roles.py:360 | high | medium | confirmed | I verified the gap. A grep for check_roles, R13, R14, R15, stand-in and waiver across adopt-roles.test.sh, render_agents.py (--selftest), check-wiring.test.sh, scratch-guard.test.sh and govkit/selftest.py found only scratch-install runs of check_roles.py that expect exit 0 (selftest.py:2834) and the hook allowlist arms. The other R15 hits belong to lexicon and run-gates and are unrelated codes. `git ls-files \| grep -i stand-in` prints nothing, so the R15 join (check_roles.py:359-375) and the stale-row direction run over an empty population in the only leg that runs the checker ('roles catalogue', gate-legs.json:1647). handoff.py's --stand-in refusal (handoff.py:1007-1015) has no arm either. Specs 17 and 19 name 'New arm: tools/roles/check_roles.py', meaning a one-time staged break against gov's tree with floor 'none'. That is a one-off observation and leaves nothing behind to catch a regression. The by-design list (item 8 covers only not running gates) does not excuse the missing persisted coverage. Graded medium, not high: the gap would let a regression land green, but it ships no wrong result now. The older rules R1-R12 also lack fixture arms, which suggests a convention rather than a slip unique to this diff. | sound | vacuous-selector-empty-population |
| 9 | verification | tools/roles/adopt-roles.test.sh:223 | medium | medium | confirmed | At 4795172cb, arm 9 of adopt-roles.test.sh writes the wf_00000001-aaa journal and the transcripts and meta files of agents a2 and a3 (lines 208-217). The only agents invocations are at lines 223 and 227, and both pass --handoff. git grep for 'agents --run' under tools/ finds only format-guard.js:428 (the refusal text) and SKILL.template.md:28. No test file runs it. Spec 20's AC2 (lines 393-398) names exactly the --run output this fixture was built for, so the journal branch has no persisted check. The effect is a test gap with no wrong output shipped, so medium. | sound | - |
| 10 | verification | tools/hooks/format-guard.js:352 | medium | medium | confirmed | In format-guard.js at 4795172cb, the queued_command attachment branch (around line 352), the `r.status === 'completed'` returned-line requirement for a foreground Agent result, and `addRun(r.runId, r.status !== 'async_launched', ...)` for a non-async Workflow are all real code paths. Every scenario in format-guard.test.sh (lines 322-329) uses an `async_launched` result. Its only notification shape is a user record with origin.kind 'task-notification'. None of the three routes is covered, so the mutations the finder lists would leave the suite green. Contained to missed refusals. | sound | - |
| 11 | verification | tools/unattended/gate-guard.js:702 | low | low | confirmed | run-lease.js scanLeases (line 161) reports `phase: readFact('phase') \|\| 'absent'`, and checkAsk (gate-guard.js:695-704) filters out `l.phase !== 'absent'`. The Q arms in gate-guard.test.sh (568-584) cover BUILDING, HELD, LANDED, ABORTED, a session that reads absent, and a missing conf. No fixture drops the phase: line, and none makes checkAsk throw. Dropping the filter would red nothing. This is a test gap with no behaviour defect. | sound | - |
| 12 | intent | tools/roles/roles_lib.py:226 | low | low | confirmed | roles_lib.extract_microformat_shapes (lines 220-234) was added by this diff. It finds the markers with a substring text.find and keeps the first definition via shapes.setdefault. format-guard.js readCharterShapes (167-181) uses whole-line lines.indexOf and `shapes[head] = ...`, which keeps the last. check-microformats.sh refuses a duplicated fence pair but has no repeated-head check. A charter with a repeated head therefore makes handoff.py:782 derive lines against one shape while format-guard grades them against another. Today's AGENTS.md has each marker only as a whole line (55, 69) and no repeated head. That makes the path narrow and contained, so low. | sound | two-readers-of-one-config-one-re-derived |
| 13 | intent | memory/builds/aOrientedCast/spec/2026-10-13-spec-TOOL-aOrientedCast-21.md:277 | low | low | confirmed | In tools/hooks/format-guard.js:396-415, checkAgentLines treats a row as bare only when the text after its last ' · ' ends with '/<agentId>'. Cutting the last field ('run direct/a1') of the AC1 line therefore leaves no bare candidate. The 'loose' test then fails too, because no '/a1' remains, so the reason is 'no agent line for agent a1, which this turn dispatched', not 'does not match its charter shape'. The spec (Status CLOSED · rev-1, :3) still says at :277-278 that cutting the last field gives the shape message. The deviation is recorded only in commit 6fb62ffa5's Decided trailer, which says the observation was taken with the run field rewritten to direct/a1. The effect is confined to the spec record: a close run literally against AC2 would red. | sound | - |
| 14 | intent | memory/builds/aOrientedCast/spec/2026-10-13-spec-TOOL-aOrientedCast-22.md:263 | low | low | confirmed | I ran `git grep -l "gov:kit unattended@1.104" 4795172cb`. It lists memory/builds/aOrientedCast/build/2026-10-13-build-TOOL-aOrientedCast-22-1-acceptance-ledger.md and the TOOL-22 spec itself, which quotes the string at :198 and :263. AC6's 'prints nothing' can never hold for a correct build. The effect is confined to how the criterion is observed. | sound | - |
| 15 | intent | memory/builds/aOrientedCast/spec/2026-10-13-spec-TOOL-aOrientedCast-17.md:71 | low | - | refuted | TOOL-17's spec closed at d799ef46d (02:45). TOOL-19's rev-2 handoff came later, at 1768864c0 (04:22). So §3 and §4 described the set correctly when the unit closed, and §4 dates its reading ('Read on 2026-10-13'). The rule §4 states (the highest-order unit touching tools/roles/ moves the kit) is the rule TOOL-20 applied. TOOL-20's spec at :318-319 cites that rule and records that 'TOOL-aOrientedCast-19's rev-2 handed the move here', and TOOL-19 rev-2 (:52, :342, :411) names TOOL-20 too, so the move has one stated owner in the live records. TOOL-17's own rev obligation covers only a retirement 'before this one closes'. What remains is a dated historical note in a closed record, not two live answers. | sound | two-answers-to-one-question |
| 16 | intent | memory/map/features/roles.md:124 | low | low | confirmed | memory/map/features/roles.md:122-125, rewritten in this diff from the base's :113, still says the section 1 rule lines and the Protocols and Facts sections 'are the only contract read from outside the kit'. TOOL-20 added roles_lib.extract_microformat_shapes (tools/roles/roles_lib.py:220), which is absent at base 53b25884. It reads the governing doc's <!-- microformats --> fence, a second contract from outside the kit, and the dossier's own :61 describes handoff.py agents filling those shapes. The transcript reading is explicitly no contract (handoff.py:66), but the fence is one, so the bullet is now false. The effect is documentation only. | sound | a-folded-field-leaves-its-row-shape-docs-behind |
