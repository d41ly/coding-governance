**Serves:** diff-review TOOL-aBriskPreflight-1 TOOL-aBriskPreflight-2 TOOL-aBriskPreflight-3 TOOL-aBriskPreflight-4 TOOL-aBriskPreflight-5 TOOL-aBriskPreflight-6 TOOL-aBriskPreflight-7 TOOL-aBriskPreflight-10

# aBriskPreflight — Tier-2 CLOSING DIFF review, round 1

*Node `a`, 2026-10-12. This is the closing review of unattended build aBriskPreflight, synthesized
from a five-lens finder fan and four skeptic batches. The build cuts the cost of the unattended
preflight without weakening any check. Every changed arm's printed lines are meant to stay
byte-identical before and after on one tree. The cited `file:line` refs for findings 1, 3 and 11
were re-opened in this worktree at `ea5fd644` before this report was written.*

**Range reviewed: `d19938f350d5fe9f5d85c288dcf585cc313fd26f...ea5fd6440ff4be44dddff5f3e84787cac0bb18cc`**

The base `d19938f3` is the origin/main tip this run branch merged at `976a85a25`. base..HEAD is
therefore exactly this build's cumulative work. The run's pinned BASE `271a9004` predates that
merge, and a diff from it would carry other builds' landed code.

**Round: 1.**

## Verdict: CLEAN WITH FIXES

No blocker. There is one high, finding 11: the shipped ceilings rest on a K_w that leaves out a
recorded reading, so a healthy wiring check at a host state already on record can be killed and
refused at check 4. Two findings are medium. Finding 2 reds the memory-hygiene bar (checks 21 and 23)
at landing, so its fix is owed before the lander runs, not after. Finding 3 misreports the
profile command's duration in GB_WHY. The other seven confirmed findings are low. Three of them
(1, 4, 7) are one defect reported by three lenses: the uninitialised `_SJ_RC`/`_SJ_VIEW` cache.

## Review shape

Review shape: intensity full, raw 12, confirmed 10, refuted 2, unverified 0 (0 uncertain), precision 0.83.

| lens | returned | raw | confirmed | refuted | uncertain | unverified | precision |
|---|---|---|---|---|---|---|---|
| security | yes | 1 | 1 | 0 | 0 | 0 | 1.00 |
| correctness | yes | 0 | 0 | 0 | 0 | 0 | - |
| seams | yes | 3 | 3 | 0 | 0 | 0 | 1.00 |
| verification | yes | 6 | 5 | 1 | 0 | 0 | 0.83 |
| intent | yes | 2 | 1 | 1 | 0 | 0 | 0.50 |

Adjudicated tally, by item: 0 blocker, 1 high, 2 medium, 5 low (8 items). By raw confirmed
finding: 0 blocker, 1 high, 2 medium, 7 low (10 findings). The difference is the one merged low
item, which carries findings 1, 4 and 7.

**Run integrity.** Lenses 5/5 returned, 0 DIED. Skeptic batches 4/4 returned, 0 DIED. 0
contradictory verdicts were demoted to unverified, 0 spurious verdicts were discarded, and there
were 0 duplicates at the harness level (the three-lens overlap on 1/4/7 was merged here, at
synthesis). Fixes on confirmed findings: 7 judged sound, 3 judged UNSOUND, 0 none proposed, 0 NOT
JUDGED. Severity on confirmed findings: 0 UNGRADED by the skeptic, 2 RE-GRADED by the skeptic
(findings 2 and 5, both lowered). Unverified findings: 0 answered UNCERTAIN, 0 with no usable
verdict. No lens notes were supplied, so every lens ran on the kit's generic brief. The correctness
lens returned zero findings; with every lens and batch returned, that zero is a real negative for
this fan, but a generic-brief zero is weaker evidence than a primed one.

**Inputs.** 8 spec documents were supplied as `specs`, beside the range's commit messages. The
checklist had 50 items, each assigned to exactly one of 5 lenses: security 10, correctness 10,
seams 10, verification 10, intent 10. By-design items were the caller's byDesign.

## HIGH

### H1 — K_w drops the worst recorded fork reading, so the shipped ceilings understate their own rule (finding 11)

- **Where:** `memory/builds/aBriskPreflight/build/2026-10-11-build-TOOL-aBriskPreflight-7-ceilings.sh:40`.
  `kw` is raised only inside the timed-row branch, for `cw-after-N` / `ab-AN-N` labels with rc=0.
  The `$1 == "host"` branch records `hs`/`hk` and never updates `kw`.
- **Defect:** ab-AO-2's host row (fork=2.53 s, node a, 2026-10-11) sits in the `ab-rows.log` the
  instrument reads, and it is dropped. `kw` ends at max(0.91, 1.06) = 1.06. Spec 7 section 4 defines
  K_w as "the larger of 0.91 s and every K_m in the rows". It prices every fork at the worst recorded
  on this node. The README and the driver comment repeat "the worst on record". The 0.91 s floor
  comes from `hook-base`, a base-arm row, so the rule does not limit itself to after-arm rows.
- **Impact:** With K_w = 2.53 the spec's formula gives WIRING_CEILING 840 instead of the shipped 570.
  PREFLIGHT_CEILING comes to about 4200, at or above GATE_BOUND 3600, so the instrument would exit 1
  and the unit would park. Re-pricing cw-after-1 at ab-AO-2's recorded state gives about 662 s, above
  the 570 s kill. A healthy wiring check at a host state already on record that day is therefore
  killed and refused at check 4, and the whole preflight must be re-run. This breaks spec 7's
  promise that a healthy run breaches only on a host slower than any reading on record. The shipped
  constants also misstate their own derivation, which will mislead the next re-derivation.
- **Fix (judged SOUND by the skeptic):** Either update `sw` and `kw` from every `host` row the
  instrument reads (the `$1 == "host"` branch), which is what "worst on record" says, and re-derive
  the constants (the unit parks if PREFLIGHT_CEILING reaches GATE_BOUND, as the spec intends). Or rev
  the spec so K_w is defined over the after-arm rows only, and record why the old-arm 2.53 s reading
  is excluded. Keep the README and the driver comment in step with whichever rule is chosen.
- **Left-shift gate:** Give the instrument a self-test fixture with a host row whose fork cost
  exceeds every timed-row K_m, and assert the printed K_w equals that host value. Stage the break
  (drop the host branch's update) and confirm it reds.

## MEDIUM

### M1 — 15 build records carry no Serves line; hygiene checks 21 and 23 red at landing (finding 2)

*Finder graded high; the skeptic's binding grade is medium. I agree: the defect is missing record
metadata that reds a visible gate, and it ships no wrong behaviour and no false certification.*

- **Where:** `memory/builds/aBriskPreflight/build/2026-10-11-build-TOOL-aBriskPreflight-7-ceilings.sh:1`
  and 14 siblings: the `.sh` instruments, `.py` tracers and `.log` row files of units 1, 3, 4, 5, 6
  and 7 (for example `-1-host-state.sh`, `-1-runs.log`, `-4-probes-ab.sh`, `-5-walk-probe.sh`,
  `-6-claim-push.sh`, `-7-ab-prep.sh`, `-7-ab-rows.log`, `-7-ceiling-rows.log`).
- **Defect:** None has a `**Serves:**` line in its first 12 unfenced lines.
  `.memory-tree.conf` sets no `RECORD_SERVES_CUTOFF`, and the names carry an ISO date, so
  `RECORD_UNDATED_ARTIFACTS` does not exempt them. The same hygiene run fails check 23: units 4 and 7
  are terminal, but no journal record evidences TOOL-aBriskPreflight-4/AC1..AC10 or
  TOOL-aBriskPreflight-7/AC1..AC12.
- **Impact:** `check-memory-hygiene.sh` prints `HYGIENE check 21 FAILED` and `HYGIENE check 23
  FAILED` at `ea5fd644`, so the bar reds when this build lands. Each instrument's link to its unit is
  readable only from the filename ordinal.
- **Fix (judged SOUND by the skeptic):** Put a comment-marked `# **Serves:** research
  TOOL-aBriskPreflight-<n>` line in the first 12 lines of each `.sh` and `.py` record. Use the same
  form for each `.log`, or move the rows into a fenced block inside the unit's `.md` record and delete
  the bare `.log`. Add a journal record with an `**Evidences:**` acceptance ledger for
  TOOL-aBriskPreflight-4 and -7, as `-6-acceptance-ledger.md` does for unit 6. Re-run
  `check-memory-hygiene.sh` and confirm checks 21 and 23 pass.
- **Left-shift gate:** The gate exists (checks 21 and 23); the gap is that a build pass can commit a
  record without running it. Run `gen_build_index.py --print-bindings` scoped to the build folder in
  the pass's diff-scoped gates, so an unbound record reds in the pass that wrote it, not at the close.

### M2 — RB_TOOK now measures start-to-read, and GB_WHY prints it as the profile command's duration (finding 3)

- **Where:** `tools/unattended/unattended.sh:9471`, fed by `read_bounded` (around line 298).
- **Defect:** After the `init_bounded`/`read_bounded` split, `RB_TOOK` is the read time minus the
  start second in the handle. `init_preflight_probes` starts the profile beside the wiring check, but
  `derive_gate_backstop` reads it only after `check_wiring`, `check_method`, `check_waivers`,
  `check_single_live`, `check_cross_run_overlap` and `check_lander_mode`.
- **Impact:** A GATE_PROFILE_CMD that exits non-zero in under a second, behind a 500 s wiring check,
  is reported as `exited <rc> after ~500s`. `write_preflight_record` prints that GB_WHY on the
  no-fact path. The line differs from the pre-change line, against the byte-identity intent. Spec 4
  line 154 says the only probe whose RB_TOOK preflight prints is the wiring check's, and line 249
  rejects the end-stamp alternative on that false premise. No verdict changes.
- **Fix (the finder's fix was judged UNSOUND; this is the skeptic's corrected fix):** Capture the
  stamp path before the wrapper unsets `RB_UP`, and stamp the end with a builtin so no process is
  added: `: >"$RB_UP"; _rbe=$RB_UP.end; unset RB_UP; "$@"; _rbr=$?; printf "%(%s)T\n" -1 >"$_rbe";
  exit $_rbr` (the same change in both launch lines). In `read_bounded`, after the wait, read
  `$_d/up.end` when it exists and set `RB_TOOK` to that second minus `_s`; otherwise keep the
  read-time figure. Correct spec 4 lines 152-155 and 249. Alternatively, drop `after ${RB_TOOK}s`
  from GB_WHY when it was read from a `PF_PROBE_PROFILE` handle.
- **Left-shift gate:** Add an `unattended.test.sh` arm: a fast-failing profile stub behind a slow
  wiring stub, asserting GB_WHY does not report the wiring stub's duration. Stage the break (revert
  to read-time RB_TOOK) and confirm it reds.

## LOW

### L1 — `_SJ_RC`/`_SJ_VIEW` are not initialised at file scope, so an inherited value is taken as a built view (findings 1, 4, 7)

*Reported independently by the security, seams and verification lenses; merged here as one defect.*

- **Where:** `tools/check-wiring.sh:385` tests `${_SJ_RC:-}`; the view is read at line 411. Line 95
  initialises `_SETTINGS_CACHE=""`, and `_FRAG_*` (line 155) and `_KF_*` (line 568) are reset at file
  scope too. These two are not. Neither variable exists at base `d19938f3`.
- **Impact:** An exported `_SJ_RC=0` with a crafted `_SJ_VIEW` skips `settings_json` and the file
  read entirely. The agent-cap, scratch, recall, card and scratch-guard-gated arms grade the injected
  text and print the ordinary `ok settings` line, even over a missing settings file; under
  `--preflight` that green is check 4's verdict. An inherited `_SJ_RC=2` makes every arm UNWIRED over
  a correct file. Reachability is small: nothing in the repo exports a `_SJ_*` name, and whoever
  controls the hook's environment can already redirect `GOV_SETTINGS_JSON` or `PATH`. This is
  hygiene with no new privilege.
- **Fix (judged SOUND by the skeptic, all three times):** Next to `_SETTINGS_CACHE=""` at line 95,
  add `_SJ_RC=""; _SJ_VIEW=""`, before the parent's `matchers_of || :` prime. settings-merge.py's arm
  17 lifts the function alone, reads `${_SJ_RC:-}`, and still builds the view on its first call.
- **Left-shift gate:** Add a `check-wiring.test.sh` arm that runs with `_SJ_RC=0 _SJ_VIEW=...`
  exported over a missing settings file and expects UNWIRED, plus one with `_SJ_RC=0 _SJ_VIEW=`
  over a correct file that expects the agent-cap arm `ok`. The class gate: a cache global introduced
  in a sourced/hooked script is reset at file scope, checkable by grepping `${_X:-}`-tested globals
  against file-scope assignments.

### L2 — The 8000-character chunk flush in the declared-index harvest is never exercised (finding 5)

*Finder graded medium; the skeptic's binding grade is low. I agree: the flush branch is correct
today, so this is a coverage gap over correct code.*

- **Where:** `tools/check-wiring.sh:1380`. This repo's declared index list is 122 paths, 4787
  characters, and the suite has no state past 8000. Spec 1's AC4 stage-breaks only the post-loop
  remainder `sed`.
- **Impact:** If the flush breaks, rows in the second and later chunks are never harvested, and the
  family-drift arm prints `ok` over an undeclared family. The repo's own list will cross 8000 with no
  arm having run the path.
- **Fix (the finder's fix was judged UNSOUND; this is the skeptic's corrected fix):** Add a
  `check-wiring.test.sh` state whose merge=rows indexes, declared with long paths, total more than
  8000 characters. Put one undeclared family prefix only in an index in the FIRST chunk (reached only
  through the in-loop flush `sed`) and another only in the LAST chunk (reached through the post-loop
  `sed`). Assert the `UNWIRED  merge ... does not declare` line names both. For liveness, add a
  staged-break twin that rewrites the in-loop flush `sed -n -e "$expr" -- "$@";` to `:;` and asserts
  the first-chunk family is now absent. Keep paths short enough for Windows MAX_PATH by using many
  paths rather than a few very long ones.
- **Left-shift gate:** The corrected fix is itself the gate.

### L3 — "BP4 AC4 every row names one driver pid" cannot fail (finding 6)

- **Where:** `tools/unattended/unattended.test.sh:8836`. `write_proc_record` (unattended.sh:1661)
  writes field 3 as `$$`, every row comes from `init_bounded` in the one driver, and `pf_fixture`
  deletes `tRun.procs` first, so `sort -u | wc -l` is always 1 whenever any row exists.
- **Impact:** Test strength only. The assertion reads as coverage of AC4's pid clause and grades
  none of it.
- **Fix (the finder's fix was judged UNSOUND; this is the skeptic's corrected fix):** Replace the
  assertion with one that can go red. Check that field 1 of the four rows holds four distinct,
  all-numeric values. Check that field 3 is numeric, the same on every row, and different from every
  field-1 value. Otherwise delete the assertion and note in the arm that AC4's pid clause is graded
  only by row presence.
- **Left-shift gate:** Stage a break (write a constant into field 1) and confirm the new assertion
  reds before landing it, per §7's observed-failing rule.

### L4 — The straggler-layer skip predicate has no durable arm proving it matches (finding 8)

- **Where:** `.githooks/pre-push:813` (predicate at 801-819). The S4 arms at
  `straggler-guard.test.sh:307-319` push a branch or a tag carrying a delta, so they prove only that
  the layer still runs.
- **Impact:** If the predicate stops matching the claim shape (a different batch-check line, a
  reordered query, an off-by-one in the row walk), it fails safe: the layer runs as before. Unit 6's
  cost cut disappears silently, with every suite green. The dropped "checked nothing" line on a claim
  push is also untested.
- **Fix (judged SOUND by the skeptic):** In `straggler-guard.test.sh`, add a claim-only push
  (`commit-tree` over `mktree </dev/null` to `refs/gov/runs/x`) in a clone whose `straggler-guard.sh`
  is replaced by a stub that touches a marker when sourced. Assert the push succeeds and the marker
  is absent. Add a LIVENESS twin where the claim has a non-empty tree and the marker appears.
- **Left-shift gate:** The fix is the gate.

### L5 — No arm covers derive_wiring_bound's equal-pair rule (finding 9)

- **Where:** `tools/unattended/unattended.sh:2886` (`derive_wiring_bound`, 2884-2891) gives an equal
  WIRING_CEILING/GATE_BOUND pair to GATE_BOUND through `-lt`. The BP7 arms
  (`unattended.test.sh:8636-8650`, `8700-8727`) cover only ceiling < bound and bound < ceiling.
- **Impact:** A drift from `-lt` to `-le` would re-word check 4's refusal for an equal pair, breaking
  the rule that the driver's refusals keep their text, and every suite would stay green.
- **Fix (judged SOUND by the skeptic):** Add one case to the BP7 AC1 block: mutate WIRING_CEILING to
  "2" under a conf with GATE_BOUND="2". Assert the output carries `did not answer within the declared
  2s bound` and no `wall-clock ceiling`.
- **Left-shift gate:** The fix is the gate; stage `-le` and confirm it reds.

## Refuted

Two findings were refuted and are not owed: finding 10 (the AC7 NOTE guard is already covered by the
byte-exact `--version` arm at `unattended.test.sh:2712`) and finding 12 (the ceilings instrument's
diff against the driver is a pass-time check the records describe as such, not a standing gate). Their
reasons are in the appendix.

review-shape kind=diff-review round=1 intensity=full at=synth raw=12 confirmed=10 refuted=2 unverified=0 blocker=0 high=1 medium=2 low=7 agents=10 out-tokens=253733

## Appendix — every finding

| id | lens | ref | severity | skepticSeverity | verdict | reason | fixVerdict | classes |
|---|---|---|---|---|---|---|---|---|
| 1 | security | tools/check-wiring.sh:385 | low | low | confirmed | At ea5fd644, tools/check-wiring.sh:385 tests `${_SJ_RC:-}`, and line 411 reads `${_SJ_VIEW:-}`. Neither variable is assigned at file scope. Line 95 initialises `_SETTINGS_CACHE=""`, but nothing does the same for these two, and nothing else in the repo sets or clears them. An inherited `_SJ_RC=0` with an exported `_SJ_VIEW` therefore skips settings_json and the file read entirely, and the arms grade the injected text. The base had no such cache (git show d19938f3 has no _SJ_RC), so this diff introduced the seam. The consequence is contained. Anyone who can set the hook's environment can already redirect GOV_SETTINGS_JSON or PATH, so this is hygiene with no new privilege. Low. | sound | - |
| 2 | seams | memory/builds/aBriskPreflight/build/2026-10-11-build-TOOL-aBriskPreflight-7-ceilings.sh:1 | high | medium | confirmed | I ran `gen_build_index.py --print-bindings` and `check-memory-hygiene.sh` at ea5fd644. Both print exactly the 15 listed .sh, .py and .log records as `A ... no Serves line in the first 12 unfenced lines`. The hygiene run prints `HYGIENE check 21 FAILED` listing all 15. It also prints `HYGIENE check 23 FAILED` for TOOL-aBriskPreflight-4/AC1..AC10 and TOOL-aBriskPreflight-7/AC1..AC12. No RECORD_SERVES_CUTOFF is set, and the legacy set does not cover them. Every file was added by this build. The comment-marked `# **Serves:** journal TOOL-x-n` form is prior art (aBranchedMandate-3-repro-c3.sh), and gen_build_index's selftest accepts `#!/bin/sh\n# **Serves:** ...`, so the fix works. Severity is medium, not high. The defect is missing record metadata that turns the hygiene bar red; it ships no wrong behaviour and no false certification, and its effect is a visible, contained gate failure. | sound | record-without-serves-or-with-a-round-counter |
| 3 | seams | tools/unattended/unattended.sh:9471 | medium | medium | confirmed | read_bounded (unattended.sh:298) sets RB_TOOK to the read time minus the start second recorded in the handle. The --preflight block (7279-7293) starts the profile in init_preflight_probes. It reads the profile only in derive_gate_backstop, after check_wiring, check_method, check_waivers, check_single_live, check_cross_run_overlap and check_lander_mode. When the profile exits non-zero, line 9471 sets GB_WHY to say it 'exited $_db_rc after ${RB_TOOK}s'. Line 7630 then prints GB_WHY on the preflight's no-fact path. So a fast-failing profile is reported with the wiring check's wall time. Spec 4 says at line 154 that the one probe whose RB_TOOK preflight prints is the wiring check's. At line 249 it rejects the end-stamp alternative on that premise, and the premise is false. Only an informational duration is wrong, with no verdict change, so medium. | unsound | one-value-field-records-a-mixed-outcome |
| 4 | seams | tools/check-wiring.sh:385 | low | low | confirmed | This diff introduced the problem. At ea5fd64, tools/check-wiring.sh:385 tests `${_SJ_RC:-}`, and nothing at file scope sets _SJ_RC or _SJ_VIEW. Its sibling `_SETTINGS_CACHE=""` at line 95 is reset at file scope, so these two are inconsistent with it. Neither variable exists at base d19938f3. A value imported from the environment therefore skips the build at the line-797 prime, and every matchers_of caller (lines 876, 946, 1053-1073, 1584, 1684) grades the injected view. No in-repo caller can trigger this by accident: nothing exports _SJ_* and no `set -a` sources this script. It takes a deliberately set environment, and whoever controls the environment can already point GOV_SETTINGS_JSON at a crafted file. So the defect is real but its practical consequence is small, which makes it low. | sound | - |
| 5 | verification | tools/check-wiring.sh:1380 | medium | low | confirmed | The claim is true. tools/check-wiring.test.sh has no state that pushes the declared-index list past 8000 characters; a grep for 8000/flush/chunk finds nothing. Spec 1's AC4 only stage-breaks the post-loop remainder `sed`, never the in-loop flush. Reading the flush branch (`sed -n -e "$expr" -- "$@"; set --; len=0`, then appending p), it is correct today. Even the plausible breakages, such as skipping the `len` reset or the `set --`, still produce correct output. The finding is therefore a coverage gap over correct code, with no current behavioural effect: low, not medium. | unsound | - |
| 6 | verification | tools/unattended/unattended.test.sh:8836 | low | low | confirmed | write_proc_record (unattended.sh:1661) writes field 3 as `$$`. Every row comes from init_bounded (line 287) inside the one driver, and pf_fixture deletes tRun.procs first, so `sort -u \| wc -l` is always 1 whenever any row exists. The only way it reads anything else is an empty ledger (0), and the row-content assertion just above already reds on that. The assertion is redundant and grades none of AC4's pid clause. It affects test strength only, not runtime behaviour, so it is low. | unsound | - |
| 7 | verification | tools/check-wiring.sh:385 | low | low | confirmed | This diff introduces _SJ_RC and _SJ_VIEW; neither exists at base d19938f3. At tools/check-wiring.sh:385, matchers_of builds the view only when `${_SJ_RC:-}` is empty. Nothing assigns either variable at file scope. In contrast, _SETTINGS_CACHE (line 95), _FRAG_* (line 155) and _KF_* (line 568) are all reset there. So an exported _SJ_RC=0 in the environment skips building the view, and every arm then reads the inherited _SJ_VIEW. The finding is accurate. In practice it is barely reachable: something would have to export a private, underscore-prefixed name, and nothing in the repo does. The effect stays inside this one check, so low. | sound | fixture-inherits-ambient-machine-state |
| 8 | verification | .githooks/pre-push:813 | low | low | confirmed | This diff adds the skip predicate at .githooks/pre-push:801-819 and two S4 arms at straggler-guard.test.sh:307-319. Both arms push a branch or a tag that carries a delta, so they only prove the layer still runs. No suite pushes a claim alone and checks that the library was not sourced. The spec's Gates section lists only the S4 arm, and the skip is shown only by the one-shot AC1 A/B record. If the predicate stops matching, it fails safe: the layer runs as before. So the consequence is a silent loss of the cost cut and nothing else. That is low. | sound | - |
| 9 | verification | tools/unattended/unattended.sh:2886 | low | low | confirmed | derive_wiring_bound (unattended.sh:2884-2891) gives an equal pair to GATE_BOUND through `-lt`, and spec S2 states that an equal GATE_BOUND keeps today's refusal byte for byte. The BP7 arms cover only ceiling 2 vs GATE_BOUND 600 and the default 570 vs GATE_BOUND 2 (test.sh:8636-8650, 8700-8727). No arm sets them equal, so a drift from `-lt` to `-le` would re-word check 4's refusal for an equal pair and every suite would stay green. Only the tested contract is missing, so low. | sound | - |
| 10 | verification | tools/unattended/unattended.test.sh:8784 | low | - | refuted | The claim that dropping the guard would turn nothing red is wrong. The AC7 NOTE prints on the `--version` path: the AC7 arm itself captures it from `bash "$SCRIPT" --version 2>&1 >/dev/null`. The existing arm at tools/unattended/unattended.test.sh:2712 runs `same "--version prints the kit version the driver declares" "$(run --version)" "unattended <ver>"`, and `run` (line 532) merges stderr with 2>&1. On a host with a working `timeout -k`, a NOTE printed every run would break that byte-exact arm, along with the other exact-output `same` arms that go through `run`. A live-host negative already exists, so the missing `miss` arm leaves no gap. | sound | containment-tested-one-way |
| 11 | intent | memory/builds/aBriskPreflight/build/2026-10-11-build-TOOL-aBriskPreflight-7-ceilings.sh:40 | high | high | confirmed | In the instrument, sw and kw are raised only inside the timed-row branch, and only for labels matching cw-after-N or ab-AN-N with rc=0. The `$1 == "host"` branch records hs and hk but never updates kw. So ab-AO-2's host row (fork=2.53, node a, 2026-10-11), which sits in the ab-rows.log the instrument reads, is dropped, and kw ends at max(0.91, 1.06 from ab-AN-2) = 1.06. Spec 7 section 4 sets K_w as 'the larger of 0.91 s and every K_m in the rows'. Its margin paragraph prices every fork at 'the worst recorded on this node' and promises a healthy run breaches only on a host 'slower per process than any reading on record'. The README line ~304 also says 'the worst on record'. The 0.91 s floor itself comes from `hook-base`, a base-arm row, so the rule clearly does not limit readings to after-arm rows. Nothing in the spec or the records explains excluding the AO rows. I re-ran the arithmetic on the committed rows. Wiring: 142.2 + 137*1.604 + 193*(1.06-0.07) = 553 -> 570, as shipped; with K_w = 2.53 it is 836.7 -> 840. Preflight: 1041.7 + 1090.5 + 762*0.99 + 164.5 = 3051 -> 3060, as shipped; with 2.53 it is about 4171 -> 4200, at or above GATE_BOUND 3600, so the instrument would exit 1 and the unit would park. Re-pricing cw-after-1 at ab-AO-2's recorded state gives 142.2 + 137*(1.224-0.896) + 193*(2.53-0.07) = about 662 s, above the 570 s kill. So a healthy wiring check at a host state already recorded that day is killed and refused at check 4. That refusal is a wrong result on a narrow path. The shipped constants also misstate their own derivation rule, which will mislead the next re-derivation. | sound | - |
| 12 | intent | tools/unattended/unattended.sh:659 | medium | - | refuted | No gate or arm runs the instrument; `git grep` finds it only in RUN.md. But the records do not describe a standing enforcement, which the finding claims. AC8 is conditional ('When the ceilings instrument runs, its three lines are byte-identical...'). Spec section 5 lists 'the instrument's diff against the driver' as testing done at the pass. The spec sentence 'The instrument's diff against the driver refuses a retyped constant' describes what that diff detects, next to the rule that a change is a rev bump with new rows. The driver comment ('a changed value is a re-derivation there, never a retype here') and README line ~307 ('a changed value is a re-derivation there') state a rule and claim no automated check. The kit cannot name a build-record path, so an in-kit gate is out of reach by construction. What remains is at most a wording nuance in one spec sentence, with no effect on behaviour. Graded medium and not established as a defect, so refuted. | sound | observed-by-claim-no-arm-discharges |
