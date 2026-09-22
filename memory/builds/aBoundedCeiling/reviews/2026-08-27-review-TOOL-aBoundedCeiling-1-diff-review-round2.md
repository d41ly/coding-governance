## Verdict: BLOCKED

**Serves:** diff-review TOOL-aBoundedCeiling-1 TOOL-aBoundedCeiling-5 TOOL-aBoundedCeiling-6

One new defect, introduced by the arm the fold wrote to close round-1 finding 5, means this branch cannot run its own Definition-of-Done bar. Everything else surviving is a fix-and-go.

### Round 1's fifteen

| # | Round-1 finding | Now |
|---|---|---|
| 1 | BLOCKER — prefix assignment on `.` aborted the suite | **Closed.** Plain assignments at `unattended.test.sh:4535-4536`; suite PASSes 862 assertions. |
| 2 | BLOCKER — unarmed `fail` branch reds `check-arms` | **Closed.** The AC5 preflight arm was written, not pinned; `check-arms.py --check` is clean. |
| 3 | BLOCKER — default-`GATE_BOUND` NOTE became line 1 of every capture | **Closed.** `mkconf` declares `GATE_BOUND` (`unattended.test.sh:94`), and the NOTE got its own dedicated arm at `:4604-4621`. |
| 4 | HIGH — neither `run_bounded` call site driven | **Half closed.** `--preflight` got its arm; `--close`/`$GATE_CMD` did not. See F4. |
| 5 | HIGH — nothing asserts the runner applies a ceiling | **Closed as coverage, reopened as F1.** Arm 1e drives the real runner — in the real repository. |
| 6 | MEDIUM — arm 1c reds a `timeout`-less host | **Closed for 1c/1d, reintroduced by 1e and the new unattended arms.** See F2. |
| 7 | MEDIUM — driver selftest budget not re-declared | **Addressed** via the shrink option round 1 offered, but the shrink was also applied to the assertion thresholds. See F3. |
| 8 | MEDIUM — no liveness line for `GATE_BOUND` | **Mostly closed.** NOTE added at `unattended.sh:208`. Round 1's fix said "plus an arm"; there is none — nothing drives the driver with the probe dead. |
| 9 | LOW — two assertion floors left behind | **Half closed.** Unsharded unattended floors +6; `FLOOR_SHARD_2` and the run-gates floor untouched. See F5. |
| 10 | LOW — knob line and durable header both say unbounded | **Not closed, not deferred.** See F7. |
| 11 | LOW — ceilings-INERT notice on stdout | **Closed.** `run-gates.sh:383-388`, on stderr, independent of `PROF_TIMEOUT`. |
| 12 | LOW — the Skill tells adopters something false | **Closed.** Both halves of the byte-compared pair reworded in one commit. |
| 13 | LOW — `ceiling` undocumented for adopters | **Closed.** `tools/run-gates/README.md:125-148`, with the `max(60, 3x measured)` derivation and the antivirus measurement. |
| 14 | LOW — `UNATT_QUIET` undocumented escape hatch | **Closed.** Deleted; `grep -rn UNATT_QUIET tools/` is empty. |
| 15 | LOW — wiring breach path discards the check's output | **Not closed, not deferred.** See F8. |

---

### F1 — BLOCKER: arm 1e drives the real runner inside the real repository

`tools/run-gates/run-gates.test.sh:196` and `:208`

Both run `bash "$KITDIR/run-gates.sh"` with cwd still `$ROOT` (set at `:6`). Only the *manifest* is in `mktemp`; the git dir is the live one. Every sibling harness that executes the runner builds a scratch repo first, and `run-gates.evidence.test.sh:11-14` writes down why: *"Executing the real runner in place would re-run the whole bar recursively and clobber the live gate-last-summary.txt mid-run, so every case here drives it through `GATE_LEGS` with its own scratch `GIT_DIR`."* Arm 1e took the `GATE_LEGS` half and skipped the `GIT_DIR` half.

Two consequences, both reproduced rather than argued.

**The nesting deadlock.** The turnstile beacon is keyed on `git rev-parse --git-common-dir` (`run-gates.sh:406`), which resolves identically for the parent bar and this child. `run-gates.sh:539-543` predicts this by name — *"a caller that one day nests inside the SAME repo would deadlock against its own parent, and a marker it can read is cheaper than the incident"* — and the marker it exports, `GATE_TURNSTILE_HELD`, has exactly one occurrence tree-wide: that export. Nothing reads it, and arm 1e does not. The canary carries `chunk: selftests` and `ceiling: 3960` in `tools/gate-legs.json`, so this is reachable on precisely the run `AGENTS.md` calls the DoD bar: `GATE_FULL=1 GATE_SELFTESTS=1 bash tools/run-gates/run-gates.sh`. The parent's heartbeat refreshes only at a leg *completing* (`run-gates.sh:980`), so once the canary is the last outstanding leg the child waits `TS_TTL` = 1800 s and then reaps its own parent's beacon — voiding the one-bar-per-repo invariant for the rest of the run — or burns the leg's 3960 s ceiling and reds. Which of the two happens depends on scheduling, so it is also flaky. The standalone `PASS (134 assertions)` cannot see any of it: standalone, nothing holds the beacon.

**The durable-evidence clobbering.** This worktree's git dir holds the proof right now. `gate-last-failure.txt` — the record `AGENTS.md` tells operators to read, and which only the *next* RED run overwrites — currently reads `GATE FAIL  slow bounded  (timed out after 2s)` for a leg that does not exist in any manifest. `gate-ledger.tsv`'s top two rows are `slow bounded` and `quick`, in the file `AGENTS.md` names as the authoritative per-leg timing source and which `run-gates.sh:161` feeds back as the longest-first dispatch hint and `:893-900` as the `GATE_REUSE` lookup keyed by leg name. Secondary: the `:208` run is all-green under `GATE_FULL=1` and satisfies all five `gate-full-green` preconditions at `run-gates.sh:1256`, so on a clean tree it stamps the real sha and fingerprint with the *fixture's* `manifest_blob`. `.githooks/pre-push:147` reads that key, so it fails safe — but it is still a durable record naming a tree it never tested.

**Smallest fix:** wrap both invocations in a scratch repo the way `run-gates.evidence.test.sh:171-178` already does — `mktemp -d`, `git init -q`, `cd` there, then run. `$KITDIR/run-gates.sh` is absolute and `GATE_LEGS` is already explicit, so nothing else moves; `GD` (`run-gates.sh:95`) and the beacon key both follow cwd. `GATE_TURNSTILE=0` alone fixes the deadlock and leaves the evidence clobbering standing.

### F2 — MEDIUM: the new arms sit outside the `timeout`-host gate the same fold built

`tools/run-gates/run-gates.test.sh:171-217` · `tools/unattended/unattended.test.sh:4585-4591`

The hoisted gate closes at `:169` (`fi   # ---- end the HAVE_TIMEOUT gate on arms 1c/1d`) and arm 1e starts two lines later, ungated. With no runnable `timeout -k`, `run-gates.sh` sets `CEILINGS_LIVE=0`, `:938` forces `bound=0`, the 45 s sleeper exits 0, the `case` at `:197` falls through and `fail=1`. The fold's own SKIP text at `:131-133` states the rule it then breaks three lines later. The same shape landed in the sibling kit: with `GATE_BOUND_LIVE=0`, `unattended.sh:180-184` takes the unbounded branch, `slowwire.sh` sleeps its full 60 s, the check passes, and both the `hit` at `:4589` and the `-lt 25` at `:4591` fail. The revived sourced block at `:4535-4560` forces `GATE_BOUND_LIVE=1` on that same host and would take exit 127 against a `124|137` case.

**Smallest fix:** move the `fi` at `:169` down past `rm -rf "$_cd"` at `:217` and name 1e in the SKIP text; give the unattended block its own `timeout -k 1s 1 true` probe with an announced SKIP.

### F3 — MEDIUM: the thresholds were cut below this file's own recorded observation, and the observation was deleted

`tools/unattended/unattended.test.sh:4546`, `:4556` · `tools/run-gates/run-gates.test.sh:147`, `:151`

The fold deleted *"Measured on node `a` at 12 s under heavy ambient load"* and set the allowance to `-lt 7`. That 12 s was the **correct** construct's wall clock under load against the same 2 s bound — it is kill-path and scheduling overhead, not sleeper length, so it does not shrink when the sleeper goes 60 s to 10 s. With a 10 s sleeper the valid window is (correct-worst-case, 10), and the only recorded correct-worst-case is 12: an empty window. On the node that produced that measurement the arm now reds on correct code and cannot discriminate at all. The fold's own new `tools/run-gates/README.md:142` makes this exact argument about ceilings.

Round 1 asked for the *control* to shrink; the control is what cost the 62 s, and the two assertion thresholds did not need to move with it.

**Smallest fix:** keep the 10 s control and its `-ge 7` / `-le 6`, restore `-lt 20` at `:4546`/`:4556` and `-gt 20` at `run-gates.test.sh:147`, and put the deleted 12 s measurement back beside them.

### F4 — MEDIUM: round-1 finding 4 is half closed — the `--close` seam is still asserted by inspection

`tools/unattended/unattended.sh:2793-2800`

`grep -n 'mkconf ' unattended.test.sh` returns exactly one fixture with a small bound: `:4586`, whose second positional (`GATE_CMD`, per the signature at `:87-94`) is `true`. So `run_bounded $GATE_CMD && { DOD_OUT=""; return 0; }`, the `local _grc=$?` at `:2794`, and the breach wording at `:2800` are undriven — `grep -rn "merge bar did not answer" tools/` returns that one source line and nothing in any test. `check-arms.py` is structurally blind here because this branch sets `DOD_OUT` rather than calling `fail`, which round 1 already noted. AC5's own text says why this is the one to have: *"the helper has one exercised call site and one asserted only by inspection, which is how the sibling seam went unbounded the first time."*

I read `:2791-2800` and found no live bug in it — this is uncovered branch, not broken code, which is why it is not a blocker.

**Smallest fix:** one arm beside `:4586` — `mkconf "true" "bash slowgate.sh" "" "2"`, `fixture`, `run --close tRun`, then `hit` on `"the merge bar did not answer within the declared"` plus an elapsed assertion.

### F5 — LOW: two of the three assertion floors did not move

`tools/run-gates/run-gates.test.sh:45` · `tools/unattended/unattended.test.sh:4682`

`FLOOR_ASSERTIONS=129` against an executed 134, and `FLOOR_SHARD_2=471` untouched although every new arm sits above the `fi   # ---- end REGION TWO` marker at `:4623` and is therefore paid by shard 2. The fold applied the re-pin convention to the two unsharded unattended floors and to `run-gates.gov.test.sh` earlier in the branch, and skipped these two. Round 1 named both.

**Smallest fix:** `FLOOR_ASSERTIONS=132` (not 134 — 1c/1d skip on a `timeout`-less host, so the floor is the skipped-host count; say so on the line) and `FLOOR_SHARD_2=477` after measuring a shard-2 run.

### F6 — LOW: arm 1c's header describes a fixture the fold replaced

`tools/run-gates/run-gates.test.sh:124-125`

Still reads *"compared against a 60 s sleeper, a 30x margin"* over code that sleeps 10 (`:138`, `:144`) against thresholds of 6 (`:147`, `:151`) — a 3x margin. The fold rewrote the equivalent sentence in `unattended.test.sh` when it made the identical change and left this one. A value stated in prose beside the source that owns it, which is the class this diff's own gotcha checklist selected.

**Smallest fix:** rewrite `:121-126` to name the sleeper and threshold the code actually uses.

### F7 — LOW: round-1 finding 10 untouched, with a live reproduction now on disk

`tools/run-gates/run-gates.sh:381-389`, `:765`, `:864`

The fixture run arm 1e left behind in this worktree's git dir contains, in one file: `gate profile: capable  (… width 8, timeout off; detected)` followed by `GATE FAIL  slow bounded  (timed out after 2s)`. `prof_t` is built from `PROF_TIMEOUT`, which every `gate-profiles.txt` row sets to 0; `:864` writes `leg_timeout 0` into the durable header whose own comment says a later reader needs the per-leg timeout; and the unbounded count prints at `:765`, before the guard/reuse passes, so a diff-scoped run counts legs it will skip, hold or reuse. The fold fixed only the INERT-notice half, which was finding 11. Reporting accuracy, no wrong verdict — but it is an unrecorded omission, not a judged deferral: nothing about it appears in either commit message, in `RUN.md` (which gained only the review line), or in the `TOOL` backlog.

**Smallest fix:** fold the ceiling regime into `prof_t`, record the effective regime rather than `PROF_TIMEOUT` at `:864`, move the count below the guard/reuse passes, and correct spec-1 S6/AC3 to say stderr.

### F8 — LOW: round-1 finding 15 untouched, also unrecorded

`tools/unattended/unattended.sh:1079-1083`

`wout=$RB_OUT` at `:1079`; the breach branch calls `fail 4` and `return 1`, so control never reaches the shared printer at `:1090`, whose comment at `:1085` claims the declared check's output is *"indented under the refusal rather than discarded"*. True on the ordinary-failure path at `:1084, false on the breach path this branch added.

**Smallest fix:** print `$wout` before the `return 1`.

---

## What the fold got right

- **The three blockers are genuinely dead, not pinned.** The prefix assignment became two plain lines with the failure recorded above them; the unarmed branch was cleared by *writing* the AC5 arm rather than adding a row to `unarmed-branches.txt`; and the NOTE problem was fixed at the fixture (`mkconf` now declares `GATE_BOUND`) with a dedicated arm for the one case that wants the NOTE. That last split is the right shape — every other fixture declares the key, so exactly one arm can see the default.
- **Finding 5 was answered at the level round 1 asked for.** Arm 1e drives the *runner*, not the construct, with a no-ceiling control and a mixed-manifest report arm. The staged deletion that stayed green now goes red. The design is correct; only the execution environment is wrong, and F1's fix does not touch a line of the assertions.
- **It refused the cheap outs twice more.** Finding 6 got a hoisted probe and an announced SKIP rather than a deleted arm, and the pre-existing `HAVE_TIMEOUT` probe at `:1021` was replaced by a pointer instead of being duplicated.
- **It found and fixed a red it did not cause** — the stale byte-pin at `run-gates.test.sh:734` inherited from `325d5f55` — and then wrote up the general defect behind it as `TOOL-aBoundedCeiling-10`: a held self-test cannot notice its own drift. That is the class, not the instance.
- **The paired documentation edits were made as pairs.** The Skill sentence moved in `SKILL.template.md` and its byte-compared render in the same commit; the `ceiling` README section carries the `max(60, 3x measured)` rule and the antivirus measurement that justifies the 60 s floor, so the number is derived rather than asserted.
- **`UNATT_QUIET` was deleted rather than documented.** Delete over disable, applied without argument.

The pattern across F1, F2 and F3 is the same one round 1 named and is worth saying plainly: the *mechanism* work on this branch has been careful throughout, and the *test layer* keeps being written as though the host and the repository were inert backdrops. Arm 1e is the sharpest instance — a correct assertion, run in the one place the tree had already written down that it must not run.