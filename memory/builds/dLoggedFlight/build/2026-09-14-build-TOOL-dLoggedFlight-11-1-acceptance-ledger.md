# Acceptance ledger — TOOL-dLoggedFlight-11

**Serves:** journal TOOL-dLoggedFlight-11

Tier-2 · node d · 2026-09-14 · the build pass of the unattended Skill's record steps and heartbeat,
against spec rev-5. The pass bumped the spec from rev-4 to rev-5 in its own commit, `98da82cf`, before
any code, and its section 9 line names each change. The unit changes Skill and protocol text only, so
it has no suite of its own. Each criterion is observed by an anchored grep or by a byte comparison
against an independent render, and each of those was seen to come back empty or unequal on a staged
break. What a gate leg observes is written as owed. No gate leg ran, per the owner's instruction of
2026-09-13, and no suite that existed under `tools/unattended/` before this build ran. What the landing
observes is owed to the landing, and the last section says where it will be recorded.

## The criteria

**Evidences:** TOOL-dLoggedFlight-11

- AC1 — `tools/unattended/adopt-unattended.sh` in its render mode, then an independent re-render
  compared byte for byte. The `--check` verdict itself is owed to the post-build gate run, in the
  `unattended skill wiring` leg. The kit's renderer, run without `--check`, rewrote
  `.claude/skills/unattended/SKILL.md` at 870 lines and 58098 bytes. A second render, written in
  Python from the same template and the values `.unattended.conf` declares, substituting the nine
  tokens in the renderer's order, is byte-identical to it, and no placeholder shape survives in it.
  The rendered section names `tools/runlog/runlog.py` at lines 765, 771 and 772 through the template's
  `{{TOOL_ROOT}}runlog/runlog.py`. The existence test `test -f tools/runlog/runlog.py` is line 771, and
  the stated skip is lines 765 to 768. Neither `.unattended.conf` nor the adopter is in the diff, so no
  conf key and no `render()` change were added. Counted with the install-prefix gate's own two
  patterns, the template holds 0 hits and 1 carried occurrence, as it did at HEAD, because a
  placeholder-led path is excluded by design.
  MET at the post-build run: `unattended skill wiring` is GREEN in 0.7 s, so the renderer's own
  `--check` agrees with the byte comparison this pass made by hand.
- AC2 — `grep -n 'Record the run' .claude/skills/unattended/SKILL.md` — prints 763, the heading, then
  842 and 865, the pointers from Mark it landed and from If it cannot finish. The section names the
  three placements at 786 (`--abort`), 787 (`--close`, before the merge) and 790 (`--landed`). The
  re-render into the SAME file by run key is at 790 and 791, and the check 34 warning is at 795 to 798.
  RED: the same grep over HEAD's rendered Skill prints nothing.
- AC3 — `--audit <slug>` in the keepalive section of `tools/unattended/SKILL.template.md`, re-observed at
  the second origin/main reconcile (2026-09-16), where main's stall probe replaced the `--status`
  heartbeat and the section now names the probe the run's heartbeat. Re-observed again at spec rev-7
  (2026-09-16, R2-L3): template lines 29 to 33 make the call once `--preflight` has written the run's
  record and say a check-51 refusal before then is not a signal to reap, and the rendered Skill carries
  the same lines at 29 to 33, which `tools/unattended/adopt-unattended.sh --check` read as in sync. RED:
  HEAD's template before the fold conditions the call on a slug existing. The original observation follows: template
  line 30 carries `bash {{KIT_DIR}}/unattended.sh --status <slug>`, which renders at line 30 of the
  Skill inside `## Before any path — schedule the keepalive NOW`. The wording that makes the call only
  once the run-state file exists is at 32 to 35. The Resume section gives its replacement job the same
  call at 688. RED: the keepalive slice and the Resume slice of HEAD's rendered Skill each hold none.
- AC4 — `grep -n 'The committed record of a run is' memory/guides/UNATTENDED-PROTOCOL.md` — line 271,
  inside the section 2 run-log paragraph, and the same line of `tools/unattended/PROTOCOL.template.md`.
  The renderer's install left the two copies byte-identical at 59507 bytes and 682 lines each, with no
  CR, under `GUIDE_CAP_BYTES` 61440 and `GUIDE_CAP_LINES` 750. RED: the grep over HEAD's copy prints
  nothing, so byte identity alone would not have passed this criterion. Check 10 of
  `tools/unattended/check-unattended.sh` is owed to the post-build gate run, in the
  `unattended kit gate` leg.
  MET at the post-build run: `unattended kit gate` is GREEN in 175.9 s, so check 10 holds over the
  two copies.
- AC5 — `2f11f32d` — owed to the landing, and never met here. The orchestrator renders this run's
  record after `--close` and before the merge, runs `python tools/runlog/runlog.py check-records` on
  the merged tree before the push, and runs the full bar on that tree. Where the observation is
  recorded is the last section of this file.
  STILL OWED after the post-build run, which graded the bar at `9e948546` and landed nothing. No
  merge and no push has run, so no `check-records` output over a record keyed `2f11f32d` and no
  full bar on a merged tree exists. The landing still owes this line.
- AC6 — `pushes.log` — owed to the landing, and never met here. It is read in the primary clone's
  common dir after `tools/push-main.sh` runs from the primary tree. If the primary tree is busy, the
  run-state file carries a parked decision instead, and the landing is not forced.
  STILL OWED after the post-build run, for the same reason: the primary clone's common dir holds
  `driver.log` and `gates.log` and no `pushes.log` at all, because `tools/push-main.sh` has not
  run. The landing still owes this line.

## What else the pass carried

- The run-state file carries this unit's dispatch and brief rows, committed with the spec's rev-5.
- The build README's roster row reads CLOSED, and the build index shows the revision and status.
- No file, leg or inventory key was added, so the codebase map is unchanged. The unattended kit stays
  at 1.20, the move unit 2 made, so no version carrier moved.
- The build README's landing rule already names the route S6 describes. AC6 observes it at landing.

## What the parity comparison cannot see

Both copies of the protocol, and the Skill and its render, are compared to each other. A claim false
in both copies passes that comparison, so each claim the new text makes was read against its owner, at
`98da82cf`:

- `--status` is journaled: the driver skips its run-log START only for `--version` and `--plan`, at
  the dispatch case of `tools/unattended/unattended.sh`.
- `--status` on a slug with no run-state file refuses with check 10, in `verb_status`, so a fire
  before preflight writes a refusal, not a heartbeat.
- `--abort`, `--close` and `--landed` each stage the run-state file through `stage_or_fail`, and
  `--close` prints that the run-state file is to be committed before the lander runs. Those are the
  three commits the placements ride.
- Check 34 is `--landed`'s refusal when the lander marker names a commit other than HEAD.
- `record --write` prints the index command and a slug-only commit subject on stdout, a refusal on
  stderr with exit 2, and the no-record line for a run that served no spec-defined unit, in
  `cmd_record` of `tools/runlog/runlog.py`. A re-render finds the run's file by its key, per
  `tools/runlog/README.md`, section "The committed record".

## Staged RED

- The byte comparison. Changing one byte in a scratch copy of the template made the comparison report
  unequal and exit 1. Appending a CR line to a scratch copy of the installed protocol made it report
  unequal with a CR found, and exit 1. The first draft of the comparison was itself vacuous: its CR
  test and line count were written with doubled escapes, matched a literal backslash pair, and read
  `lines=0`. That reading exposed it, and it was rewritten with byte values before any verdict was
  taken from it.
- The baseline. Before any edit, the renderer run over the untouched tree left `git status` clean, so
  the comparison started from committed bytes the renderer reproduces.
- The greps. Each grep of AC2, AC3 and AC4 printed nothing against HEAD's copies.
- The template predicates the kit gate reads, checked by hand since no gate ran. Check 18's
  `--preflight` line still precedes `/session-kickoff`, at 184 and 194 where HEAD had 175 and 185.
  Check 16's table-row shape still counts 17 rows, and no line the diff adds carries a pipe. Check
  31's route extractor reads only `workflows/*.js` tokens, and the new section adds none.

## The checklist over the build

`gotchas.py --for-paths` over the commit's paths named ten classes before it was committed.

- `two-answers-to-one-question` was violated in the first draft and is fixed. The Skill restated the
  driver's set of unjournaled verbs, the run key's shape and the render's exit code. Each now points
  at its owner: protocol section 2 and the runlog kit. The number 34 stays because AC2 requires it.
- `second-implementation-is-not-a-second-opinion`: the independent render shares the renderer's
  inputs, so it proves parity and not truth. Truth was read against the driver and the runlog
  command line, in the section above.
- `heredoc-escape-reaches-the-regex` bit the scratch comparison script, as Staged RED records. No
  tracked file was written through a heredoc.
- `inline-fence-swallows-the-rest-of-the-file`: the one new fence in the Skill sits on lines of its
  own, and neither the spec nor this ledger carries one.
- `fixture-passes-by-finding-nothing` and `staged-break-substitutes-a-synthetic-value`: every control
  edits a copy of the real file, and every grep was seen empty on HEAD.
- `amendment-leaves-its-other-half-standing`: rev-5 amended S3, S4, section 4 and AC3. Sections 1, 5
  and 10 were re-read against them. Section 4's "prescribes no job prompt today" describes the spec's
  own base.
- `fold-text-is-unreviewed-surface`: rev-5 and the new Skill text are prose no review has read. The
  build's closing diff review reads them.
- `bounded-through-a-pipe-is-unbounded` and `empty-field-collapses-unless-it-is-last`: no shell was
  written.

## Owed to the post-build gate run

Every leg of the spec's section 7, and the run records each verdict after it:

- `unattended skill wiring`, which is AC1's `--check` and is the byte comparison this pass made by
  hand.
- `unattended kit gate`, whose check 10 is AC4's byte identity, and whose checks 16, 18, 20, 26 and 31
  read the template this pass changed.
- `kit version markers`, over the unattended markers this pass left at 1.20.
- `memory hygiene`, over the spec, this ledger and the protocol's size under the guide cap.

The post-build run happened at `9e948546`, the whole bar with every guard lifted and the kit
self-tests on: 111 legs ran and 110 are GREEN, in 690.8 s of wall at width 8 against the profile's
declared 21600 s. Every leg listed above is GREEN: `unattended skill wiring` in 0.7 s,
`unattended kit gate` in 175.9 s, `kit version markers` in 2.4 s and `memory hygiene` in 29.1 s.
`kit version markers` is green at unattended 1.25, not the 1.20 written above - later units moved
the markers. The run's one RED, `govkit selftest`, is on none of these legs: its 30 failing
assertions are the IDENTICAL set `origin/main` carries, pre-existing, untouched by this build and
being fixed in a separate session. It is not called green here.

## Owed to the landing

AC5 and AC6 are observed by the run itself at its landing, never by this pass. The orchestrator
records both in this ledger, replacing each owed line with what it observed, in the LANDED record
commit. AC5's line then names the `check-records` output over the record keyed `2f11f32d` and the full
bar's verdict on the merged tree. AC6's line names the START and END lines in `pushes.log` for the
merge commit. If the landing is parked because the primary tree is busy, the parked decision in the
run-state file is the record instead, and both lines stay owed.

The post-build run does not discharge this. It graded the bar at `9e948546` inside this worktree
and landed nothing, so AC5 and AC6 stay owed to the landing exactly as written above.
