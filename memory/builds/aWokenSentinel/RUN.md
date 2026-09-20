# aWokenSentinel - run state

Created by `unattended.sh --preflight`. The unit list is NOT copied here — it is DERIVED
from the build README on every read, so it cannot go stale between them. This file holds
only what nothing else does: the phase and its witness, the keepalive id, the pinned BASE
with its anchor evidence, and the parked decisions.

<!-- run:generated -->
<!-- /run:generated -->

## Run facts
witness: 8bdcb035282b81bd111c9d2af652ab173a3c3230
phase: BUILDING
branch-sha: 5f9648d61c020cf3ba902d3c6acc4e8b4992ab2b
branch-ref: refs/heads/branch/unattended-kit-keepalive-a29498
mode: prompt
run-branch: refs/heads/branch/unattended-kit-keepalive-a29498
anchor-kind: run-branch
keepalive: f1209d79
anchor-url: https://github.com/d41ly/coding-governance.git
anchor-sha: 4cf0944dbdce94714870f26760936bc5edabc64e
anchor-ref: refs/heads/main
base: 5f9648d61c020cf3ba902d3c6acc4e8b4992ab2b

## Parked

2026-09-16T12:00:05Z rescope · item add TOOL-aWokenSentinel-7 · reason Measured 2026-09-16: the Stop hook's stdin carries session_crons, the cron store no script can reach. keepalive-reaped stops being an attestation (TOOL-aPromptedMandate-11, OPEN since 08-18) and becomes a check against the last stop the hook recorded. Discovered by unit 3's probe; a second mechanism, so its own unit, ordered last.

2026-09-20T10:27:09Z review · item aWokenSentinel-spec-set-r1 · reason verdict BLOCKED · blockers 3 · BOUNDED · disposition promote

2026-09-20T10:36:24Z rescope · item add TOOL-aWokenSentinel-8 · reason spec-audit round 1 B1 BLOCKER (raw 18, 29, 43): the --landed refusal's remedy ends a turn spec 3's decision table ALLOWS at FINISHED-UNSTAMPED, so every wired landing wedges at LANDING; promoted to the stop-guard's landing-unstamped BLOCK row, which is the continuation the remedy promises

2026-09-20T10:36:25Z rescope · item add TOOL-aWokenSentinel-9 · reason spec-audit round 1 H1 HIGH (raw 1, 21, 30, 44): spec 7's second --status line reds the suite's whole-output reader at unattended.test.sh:1874 and the driver header's one-line promise; promoted to the listing as a FIELD on the one status line, with the one-line promise made an arm

2026-09-20T10:36:26Z rescope · item add TOOL-aWokenSentinel-10 · reason spec-audit round 1 H2 HIGH (raw 19, 31): STOP_GUARD_BLOCKS reaches the conf example with no protocol section 8 row and no unit owning the root-conf line, so check 22 reds from the hook's commit to the close; promoted to the knob's declaration set across every carrier check 22 and spec 6 AC6 read

2026-09-20T10:36:26Z rescope · item add TOOL-aWokenSentinel-11 · reason spec-audit round 1 H3 HIGH (raw 4, 20, 34): spec 5 spells the sidecar root inline and spec 7's AC12 pins the driver's rev-parse count at 1 with no unit scoped to fix the second spelling; promoted to a kit-gate check that the driver holds ONE sidecar-root derivation, binding every unit

2026-09-20T10:36:27Z rescope · item add TOOL-aWokenSentinel-12 · reason spec-audit round 1 H4 HIGH (raw 22): the resume tick kills a live tree before consulting login, so a logged-out node kills a session it cannot resume; promoted to the login-before-kill order with the arm that observes a surviving process under a logged-out CLI

2026-09-20T10:36:28Z rescope · item add TOOL-aWokenSentinel-13 · reason spec-audit round 1 H5 HIGH (raw 26, 33): the tick's read_bound_key calls read the calling shell with no conf sourced and CONF unset, so every tick takes the defaults and the NOTE names no file; promoted to the tick sourcing the root conf before its bound reads, with arms under a declared key

2026-09-20T10:36:28Z rescope · item add TOOL-aWokenSentinel-14 · reason spec-audit round 1 H6 HIGH (raw 32): both real-driver arms borrow adopt-unattended.test.sh's seed(), which never commits, so --liveness fails 52 on an unborn HEAD and spec 3 AC11 and spec 4 AC10 can never go green; promoted to the seed committing once so every borrower inherits a born HEAD

2026-09-20T11:42:58Z review · item aWokenSentinel-spec-set-r2 · reason verdict BLOCKED · blockers 2 · BOUNDED · disposition promote

2026-09-20T12:00:28Z rescope · item add TOOL-aWokenSentinel-15 · reason spec-audit round 2 B1 BLOCKER (raw 1, 20, 32, 47) and B2 BLOCKER (raw 2, 21, 33, 46): specs 8 and 14 were audited as uncommitted rev-2 working-tree text while the commission pinned their HEAD blobs, so every lens read a text the pin does not name; the rev-2 folds are committed with this disposal and the class is promoted to a blob-pin pre-flight in the build harness's resolver stage, which refuses to dispatch a lens while any subject's working-tree hash differs from its committed blob

2026-09-20T12:00:46Z rescope · item add TOOL-aWokenSentinel-16 · reason spec-audit round 2 H1 HIGH (raw 48): unit 8's loop closes only if the re-run --landed reaches LANDED, and on the no-ff landing the charter mandates check 34 refuses every time because the run worktree's HEAD is the merge's second parent while the marker names the merge (OPEN TOOL-dUnstalledConvoy-38), so the row would spend the shared block budget and wedge the record at LANDING by a longer route; promoted to check 34 accepting a marker whose commit is on the remote default branch and has the witness as an ancestor, with the no-ff fixture arm that is RED today

2026-09-20T12:00:47Z rescope · item add TOOL-aWokenSentinel-17 · reason spec-audit round 2 H2 HIGH (raw 34, 49) and H3 HIGH (raw 3): spec 9 states the status line's field order backwards from the driver's printf, whose suffixes print after next, so the suite's whole-line reader at unattended.test.sh:1874 survives only on a fixture with no suffix, and spec 9's one-line arm cannot red against its named break because the base driver prints one line either way; promoted to the driver suite reading --status by field through one extraction helper armed on a suffixed fixture, and a one-line assertion armed against a two-line driver copy

2026-09-20T12:00:48Z rescope · item add TOOL-aWokenSentinel-18 · reason spec-audit round 2 H4 HIGH (raw 4): spec 13's NOTE-path liveness arm cannot red against its named break, since removing only the source line leaves CONF set and the no-conf refusal in place, so the defect's own signature (an empty path in the NOTE) is never produced; promoted to read_bound_key refusing with exit 2 any caller that set no CONF, so a bound read from a shell that named no conf is a refusal rather than a silent default, observed on a tick copy with the whole conf block removed

2026-09-20T12:00:48Z rescope · item add TOOL-aWokenSentinel-19 · reason spec-audit round 2 H5 HIGH (raw 5): spec 14 S2 and its risks row point at AC2, which runs the adopter's --check and no arm of the suite the committed seed feeds, and that suite sits on no bar leg; promoted to adopt-unattended.test.sh declaring a shrink-only FLOOR_ASSERTIONS on the executed count, with the close's run-unattended-gates.sh adopter row named as the observer of every arm the seed feeds and read from its log, never through tail

2026-09-20T12:00:49Z rescope · item add TOOL-aWokenSentinel-20 · reason spec-audit round 2 H6 HIGH (raw 36): spec 11 rests on a count is 1 by unit 2's AC7 that spec 2 never pins, and a header comment carrying the literal makes the unmodified driver read 2 at unit 11's order with no unit able to fix it; promoted to resolve_sidecar_dir living in lib-unattended.sh, the ratified home for a spelling two scripts share (the lib header's pointer, dUnstalledConvoy seq 22), so the driver and the tick source one derivation and unit 11's check counts code lines across driver, lib and tick and requires exactly one, in the lib

2026-09-20T13:19:35Z rescope · item add TOOL-aWokenSentinel-21 · reason spec-audit round 3 H1 HIGH (raw 26): spec 15 places its dirty-tree compare after and outside the resolver branch, so every caller-supplied {path, blob} subject reads undefined against its blob and the harness suite's fifteen supplied-subject fixtures throw Commit the fold, and nothing runs that suite to see it; the compare is folded inside the resolver branch and the class is promoted to the harness suite joining the declared self-test population with a leg row, a budgets row, a registry exemption and a shrink-only FLOOR_ASSERTIONS, so the fixtures are an executed regression arm

2026-09-20T13:19:51Z rescope · item add TOOL-aWokenSentinel-22 · reason spec-audit round 3 H2 HIGH (raw 5, 17, 27): spec 16 replaces check 34's equality with four fail 34 sentences, arms two of them, calls them the two new sentences in section 7, and lists the harness arms leg among its gates, which check-arms.py reds at the close on the two unarmed branches (the marker with no sha, the commit the advertised default branch does not reach); spec 16 is folded to seven branches of one check with its third read pinned, and the two missing arms are promoted to their own unit over the suite's marker fixture so every check-34 branch is armed before the close

2026-09-20T13:19:52Z rescope · item add TOOL-aWokenSentinel-23 · reason spec-audit round 3 H3 HIGH (raw 28): spec 17's check_status_one_line counts stdout with printf '%s\n' piped to wc -l, which prints 1 on an EMPTY capture, so a verb that wrote nothing reads as one line and the empty case its section 5 says reds cannot fail, the green-by-absence class the unit exists to close; the helper is folded to grep -c '' with a third reading against a driver copy whose status printf is deleted, and the class is promoted to a kit-gate check that no shell file in the kit counts a captured variable's lines through printf or echo into wc -l, with the class recorded under memory/gotchas/

2026-09-20T13:19:52Z rescope · item add TOOL-aWokenSentinel-24 · reason spec-audit round 3 H4 HIGH (raw 18): spec 18 spells its second arm's staged break two incompatible ways (section 3 removes the two read_bound_key calls with the block, S3 and AC2 keep them) and spec 13 defines the same BLOCK copy as its whole seven-line section 4 block while its S3 says four lines and its files-touched row says five, so the sibling agreement lands on a reading that cannot print the guard's sentence; both specs are folded to one anchored sed range with the calls kept, and the break is promoted to one suite helper, build_tick_without_conf_block in resume-tick.test.sh, which produces the copy from the CONF= and source-line anchors and asserts its shape, so the two arms stage one break by name and no count is spelled in either document

2026-09-20T13:45:29Z review · item aWokenSentinel-spec-set-r3 · reason verdict CLEAN · blockers 0 · CONVERGED · disposition promote

2026-09-20T16:43:29Z rescope · item add TOOL-aWokenSentinel-25 · reason spec-audit round 4 H1 HIGH (raw 12, 22, 33): spec 22 writes each arm's first hit as a readable prefix of the branch sentence and says that is what check-arms.py reads as an arm, but signature() runs past the sentence to the first interpolation (123 and 115 characters) and classify() arms on whole-signature containment, so both branches the unit exists to arm read UNARMED and AC4's fragment greps pass on them; the literals are folded to the full signatures and the class is promoted to check-arms.py naming a STRANDED prefix beside its UNARMED row and printing the whole signature, because --report truncates rows at 72 characters and the gotcha's copy-the-row remedy therefore strands every arm over a long message

2026-09-20T16:43:29Z rescope · item add TOOL-aWokenSentinel-26 · reason spec-audit round 4 H2 HIGH (raw 1, 23): spec 22's pushed control lands the record and moves origin main, and the accepting arm that follows in the marker region has no setup of its own, so it runs --landed on a LANDED record, its three miss lines pass on the check-26 refusal and its phase LANDED count reads the control's write, green by absence with nothing in section 6 watching it; the control's after-state restoration is folded into spec 22 and the class is promoted to the accepting arm asserting its own entry state, a committed LANDING record with HEAD advertised, before it runs, so any arm inserted above it that lands the record reds here naming the cause

2026-09-20T16:43:30Z rescope · item add TOOL-aWokenSentinel-27 · reason spec-audit round 4 H3 HIGH (raw 18, 29), H4 HIGH (raw 20, 30) and H5 HIGH (raw 19): spec 21 adds a leg to the manifest and names none of the three unguarded meta-gates that red on a new leg from the landing commit, the testsuite counts leg wanting the PASS line its section 3 refuses, the codebase map wanting the gate-legs key claimed in a dossier with the generated map re-rendered, and govkit selfcheck wanting a row in the GENERATED subject-pins.tsv; spec 21 is folded to drop the non-goal and the enrolment in all three is promoted to one unit ordered after it, with each meta-gate's own checker as the direct observation

2026-09-20T16:43:31Z rescope · item add TOOL-aWokenSentinel-28 · reason spec-audit round 4 H6 HIGH (raw 2): spec 23 bans three spellings of the added-newline line count, printf, echo and the here-string, and its S3 and AC1 stage only the printf line, so the here-string branch of the regex, a separate alternation with the variable on the other side of wc -l, has no RED observation and the class gate lands with two of three cases never seen to fail; spec 23 keeps the printf staging and the echo and here-string arms are promoted to their own unit over the same suite copy, each observed RED and GREEN restored with the near-miss beside them

2026-09-20T17:03:15Z review · item aWokenSentinel-spec-set-r4 · reason verdict CLEAN · blockers 0 · CONVERGED · disposition promote

2026-09-20T17:09:24Z dispatch · item 90a83aba TOOL-aWokenSentinel-1 · reason tools/unattended/unattended.sh tools/unattended/unattended.test.sh tools/unattended/PROTOCOL.template.md memory/guides/UNATTENDED-PROTOCOL.md tools/unattended/VERBS.template.md memory/guides/UNATTENDED-VERBS.md memory/builds/aWokenSentinel/spec/2026-09-16-spec-TOOL-aWokenSentinel-1.md memory/builds/aWokenSentinel/README.md memory/builds/aWokenSentinel/build/2026-09-16-build-TOOL-aWokenSentinel-1-1-acceptance-ledger.md memory/LIVE.md memory/ledger/2026-09.md

2026-09-20T17:09:30Z brief · item TOOL-aWokenSentinel-1 · reason d290ac894ee8 memory/builds/aWokenSentinel/prompts/2026-09-16-prompt-TOOL-aWokenSentinel-1-1-build-brief.md

2026-09-20T17:28:15Z dispatch · item e1b1b51d TOOL-aWokenSentinel-2 · reason tools/unattended/unattended.sh tools/unattended/unattended.test.sh tools/unattended/VERBS.template.md memory/guides/UNATTENDED-VERBS.md tools/unattended/SKILL.template.md .claude/skills/unattended/SKILL.md tools/unattended/PROTOCOL.template.md memory/guides/UNATTENDED-PROTOCOL.md .unattended.conf tools/unattended/.unattended.conf.example tools/unattended/kit.toml memory/guides/SESSION-KICKOFF.md memory/builds/aWokenSentinel/spec/2026-09-16-spec-TOOL-aWokenSentinel-2.md memory/builds/aWokenSentinel/README.md memory/builds/aWokenSentinel/build/2026-09-16-build-TOOL-aWokenSentinel-2-1-acceptance-ledger.md memory/LIVE.md memory/ledger/2026-09.md

2026-09-20T17:28:21Z brief · item TOOL-aWokenSentinel-2 · reason bcff21c34106 memory/builds/aWokenSentinel/prompts/2026-09-16-prompt-TOOL-aWokenSentinel-2-1-build-brief.md

2026-09-20T18:02:02Z dispatch · item 0e3f3fe2 TOOL-aWokenSentinel-20 · reason tools/unattended/lib-unattended.sh tools/unattended/unattended.sh memory/builds/aWokenSentinel/spec/2026-09-20-spec-TOOL-aWokenSentinel-20.md memory/builds/aWokenSentinel/README.md memory/builds/aWokenSentinel/build/2026-09-20-build-TOOL-aWokenSentinel-20-1-acceptance-ledger.md memory/LIVE.md memory/ledger/2026-09.md

2026-09-20T18:02:07Z brief · item TOOL-aWokenSentinel-20 · reason ee92fce91cf2 memory/builds/aWokenSentinel/prompts/2026-09-20-prompt-TOOL-aWokenSentinel-20-1-build-brief.md

2026-09-20T18:09:27Z dispatch · item 85c7761f TOOL-aWokenSentinel-11 · reason tools/unattended/check-unattended.sh tools/unattended/check-unattended.test.sh memory/builds/aWokenSentinel/spec/2026-09-20-spec-TOOL-aWokenSentinel-11.md memory/builds/aWokenSentinel/README.md memory/builds/aWokenSentinel/build/2026-09-20-build-TOOL-aWokenSentinel-11-1-acceptance-ledger.md memory/LIVE.md memory/ledger/2026-09.md

2026-09-20T18:09:33Z brief · item TOOL-aWokenSentinel-11 · reason 1c07e4bd7420 memory/builds/aWokenSentinel/prompts/2026-09-20-prompt-TOOL-aWokenSentinel-11-1-build-brief.md

2026-09-20T18:28:17Z dispatch · item 807a39b4 TOOL-aWokenSentinel-14 · reason tools/unattended/adopt-unattended.test.sh memory/gotchas/borrowed-seed-inherits-its-head-state.md memory/gotchas/INDEX.md memory/builds/aWokenSentinel/spec/2026-09-20-spec-TOOL-aWokenSentinel-14.md memory/builds/aWokenSentinel/README.md memory/builds/aWokenSentinel/build/2026-09-20-build-TOOL-aWokenSentinel-14-1-acceptance-ledger.md memory/LIVE.md memory/ledger/2026-09.md

2026-09-20T18:28:22Z brief · item TOOL-aWokenSentinel-14 · reason 9c8b61f42a08 memory/builds/aWokenSentinel/prompts/2026-09-20-prompt-TOOL-aWokenSentinel-14-1-build-brief.md

2026-09-20T18:35:33Z dispatch · item cc728357 TOOL-aWokenSentinel-3 · reason tools/unattended/stop-guard.js tools/unattended/run-lease.js tools/unattended/stop-guard.fragment.json tools/unattended/stop-guard.test.sh .claude/settings.json tools/unattended/adopt-unattended.sh tools/unattended/adopt-unattended.test.sh tools/unattended/kit.toml tools/run-gates/selftest-budgets.txt tools/install-prefix-carried.txt memory/map/generated/symbols.json memory/builds/aWokenSentinel/spec/2026-09-16-spec-TOOL-aWokenSentinel-3.md memory/builds/aWokenSentinel/README.md memory/builds/aWokenSentinel/build/2026-09-16-build-TOOL-aWokenSentinel-3-1-acceptance-ledger.md memory/LIVE.md memory/ledger/2026-09.md

2026-09-20T18:35:39Z brief · item TOOL-aWokenSentinel-3 · reason 05db5e225f7d memory/builds/aWokenSentinel/prompts/2026-09-16-prompt-TOOL-aWokenSentinel-3-1-build-brief.md

2026-09-20T18:57:27Z dispatch · item cc728357 TOOL-aWokenSentinel-3 · reason memory/map/generated/inventories.json memory/map/generated/MAP.md

2026-09-20T19:02:19Z dispatch · item cc728357 TOOL-aWokenSentinel-3 · reason memory/map/features/unattended.md

2026-09-20T19:10:40Z dispatch · item 654322ff TOOL-aWokenSentinel-16 · reason tools/unattended/unattended.sh

2026-09-20T19:10:53Z dispatch · item 654322ff TOOL-aWokenSentinel-16 · reason tools/unattended/unattended.test.sh

2026-09-20T19:11:06Z dispatch · item 654322ff TOOL-aWokenSentinel-16 · reason memory/builds/aWokenSentinel/spec/2026-09-20-spec-TOOL-aWokenSentinel-16.md

2026-09-20T19:11:20Z dispatch · item 654322ff TOOL-aWokenSentinel-16 · reason memory/builds/aWokenSentinel/README.md

2026-09-20T19:11:34Z dispatch · item 654322ff TOOL-aWokenSentinel-16 · reason memory/builds/aWokenSentinel/build/2026-09-20-build-TOOL-aWokenSentinel-16-1-acceptance-ledger.md

2026-09-20T19:11:49Z dispatch · item 654322ff TOOL-aWokenSentinel-16 · reason memory/LIVE.md

2026-09-20T19:12:04Z dispatch · item 654322ff TOOL-aWokenSentinel-16 · reason memory/ledger/2026-09.md

2026-09-20T19:12:08Z brief · item TOOL-aWokenSentinel-16 · reason 7e2ccfcec72e memory/builds/aWokenSentinel/prompts/2026-09-20-prompt-TOOL-aWokenSentinel-16-1-build-brief.md
