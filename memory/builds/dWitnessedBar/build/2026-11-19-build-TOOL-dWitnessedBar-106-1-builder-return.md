**Serves:** journal TOOL-dWitnessedBar-106

# TOOL-dWitnessedBar-106 — builder return 1 (run `wf_bb638a48-c67`), committed 217e87725

## Why

TOOL-dWitnessedBar-106 is built as its spec (rev-1) describes and committed as 217e87725 with a Pass: TOOL-dWitnessedBar-106 trailer. The spec's status header is set to CLOSED in that commit. Every claim the spec makes about current code held against the tree: blobs 13e24816, 45c73d4d, 25076c3d and f0103fb0; the cited lines of read_policy_at; no fail(); AC7's measure printing 1; POLICY_REL; and the catalogue's allowed lists. No divergence was found. One change the spec did not state is recorded as deviation 1061.

## Summary

Built and committed TOOL-dWitnessedBar-106 as 217e87725 on top of 8e5bf6088. No gate, suite, bar or --selftest ran. Probes I wrote myself stand in for the gates.

**What the commit does**
- **The hook (`.githooks/pre-push`):**
  - Adds `scan_policy_bytes`, which reads the three keys out of R's committed policy file as text, never running it.
  - Adds `derive_strictest`, which picks the strictest of the values it is given.
  - Declares `PP_BLOCKS_ORDER`, `PP_HELD_ORDER`, `PP_BYPASS_ORDER` and `PP_POLICY_REL` at column 0.
  - `read_policy_at` now has one exit after `PP_READ_AT=$sha`. It says when no python launcher resolves. Each key now reads the stricter of today's value and R's floor, and each raise is reported.
  - The header now describes the floor and carries a `WHAT THE FLOOR DOES NOT CHECK` paragraph. The bypass block's comment names the floor.
- **The suite (`.githooks/pre-push.test.sh`):** adds the floor harness, `run_floor_read`, and the arms for AC1 to AC8.
- **Docs:** `help/policy.md` gains one consumers bullet.
- **Generated and records:** the map is regenerated, both shell-role rows are widened through `ratchet.py widen` (widen 26), and the acceptance ledger is written. `gen_build_index --write` also rewrote `memory/LIVE.md`, `memory/backlog/TOOL.md`, the build README, the spec's records region and the dClosedLoop as-built view.

**Deviation 1061 (not stated in the spec):** TOOL-dWitnessedBar-3's IR AC11 arm cut only `read_policy_key` and `read_policy_at`. Now that `read_policy_at` calls the two new functions, that arm would have read an empty value. Its cut now reuses the same shared cut the floor harness uses, `_pp_read_fns`. No expected value in that arm changes.

**Shell-role rows:** the widen tool raises a row by one. Following the precedent of widens 21 and 25, I then set the count field to the measured lines: 1799 for the hook and 2415 for the suite. The main loop should confirm that edit is acceptable.

**Probes that ran** (scripts at `C:/Users/d41ly/AppData/Local/Temp/claude/06f17fbb3b45b392/0a586af7-47fb-45dc-b963-7ee82521f7da/scratchpad/probe106.sh` and `.../probe106e2e.sh`)
1. **Floor harness (stands in for the pre-push self-test, AC1 to AC5):** I cut the four functions and the order lines from the edited hook and ran them over a scratch repo with revisions A, R and R3 and the three kit copies kr, kb and kt. All plants matched every row of the spec's §4 arms table, and the messages AC1, AC2 and AC5 require appeared. The same probe over the base hook was red where the spec says it would be. I also checked the parser on its own: BOM, CRLF, comments, quoted table names, `[[ ]]` headers, trailing junk, unknown values and inline tables.
2. **End-to-end push (AC6):** a rebuilt refused bypass fixture whose tip removes the policy reader. The edited hook refused it (rc 1, `bypass-refused`) and the journal recorded `policy=refused`. The base hook let it through (rc 0) with `policy=allowed`.
3. **The arm's own snippets:** the AC8 parity check passed on the real catalogue and printed a mismatch on a planted order. The catalogue-narrowing snippet does narrow all three lists. The shared IR AC11 cut still reads `own-mixed-contended 10` at this repo's HEAD, the same as `policy.py`.
4. **Greps:** AC7's measure prints 0. AC9 prints 1 and 0. AC10 finds one line, line 29. AC11 prints 1. `bash -n` passes on both shell files, and the naming lexicon accepts the three new names.

**Owed at the close**
- **Arms and their red-first observation:** the suite's AC1 to AC8 arms, with each New arm's RED-first observation against the base hook, and the IR AC11 arm re-run with its new cut.
- **legs of §7:** `pre-push self-test`, `run-gates gov canary`, `measure-legs selftest`, `policy fixtures`, `recall floor`, `recall floor arms`, `codebase-map coverage + freshness`, `memory hygiene` and `spec tokens`, plus the portability leg the shell-role rows feed.
- **Suite budget:** the 1020s row should be re-read, since this unit adds one push fixture and about a dozen subshell reads. (DERIVED from the builder's probe)

**Checklist:** I ran `gotchas.py --for-diff HEAD~1..HEAD` and went through what it named. Each harness has a control that cannot pass by finding nothing, the AC7 cut must contain its anchor line, the parity check reads the real catalogue, and each ledger token sits on one line. Nothing else needed changing.

**Left alone:**
- The commit trailer follows the charter: `Co-Authored-By: Claude Opus 5`. That differs from the harness reminder's 5.5.
- The working-tree changes to `help/reference/drive.md` and `help/reference/units.md` were there before this pass. I left them unstaged.
