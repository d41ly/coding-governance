# aSmoothedDispatch — acceptance ledger, units 1 to 9

**Serves:** journal TOOL-aSmoothedDispatch-1 TOOL-aSmoothedDispatch-2 TOOL-aSmoothedDispatch-3 TOOL-aSmoothedDispatch-4 TOOL-aSmoothedDispatch-5 TOOL-aSmoothedDispatch-6 TOOL-aSmoothedDispatch-7 TOOL-aSmoothedDispatch-8 TOOL-aSmoothedDispatch-9

The main loop observed the owed arms at the close, on frozen clones at `55d65f5c8` and `b1e48cc59`. Each staging restored one product file to the commit before its unit, or applied one patch the spec names, then ran the suite or unattended shard holding the arms and compared its FAIL lines with the tip run's. Breaks that edit different code and red different arms shared one run (`c3a`, `c3b`, `c3c`, `c4a`); the five predicate variants and the three key-hash variants each had their own. The tip and the base `ae6735c1f` ran shards 2, 3 and 4. At `b1e48cc59` every FAIL line in those shards is also printed at the base. The instruments are the scratch scripts `green.sh`, `red.sh`, `red2.sh`, `patch.py` and `gen.py`.

**Evidences:** TOOL-aSmoothedDispatch-1
- AC1 — `GOV_RUNLOG=0 bash $SCRATCH/sd1probe.sh --dispatch tX --pass TOOL-tX-1 --writes a b c` — the builder's pass probe printed three `arg[` lines and rc 0 after the change, and check 14 naming `b` before it; the region-four arms observed RED on its staged break at the close and GREEN at the tip `b1e48cc59` (staging `u1`, the one-value arm restored: `work/one work/two work/three` went missing and `unknown argument` appeared)
- AC2 — `--writes "a b" --writes c` — the builder's pass probe printed `a`, `b`, `c` for the space-joined and the tab-and-newline values; the region-four arms observed RED on its staged break at the close and GREEN at the tip `b1e48cc59` (staging `u1`)
- AC3 — `--writes ""` — the builder's pass probe printed one `arg[]` for each no-field form; the suite arms for flag-next and end-of-argv came with unit 8 and were observed RED on its staged break at the close and GREEN at the tip `b1e48cc59` (staging `c4a`)
- AC4 — `--writes $'two\rwords/x.sh'` — the builder's pass probe kept the carriage-return value as one path; unit 9 moved the arm's byte into a variable, and the arm was observed RED on its staged break at the close and GREEN at the tip `b1e48cc59` (staging `c4a`, the split's IFS widened to `\r`)
- AC5 — `grep -c 'one path per' tools/unattended/VERBS.template.md` — the builder's grep printed 0, and `cmp` of the verb carrier's two copies exited 0
- AC6 — `grep -c 'TOOL-aSmoothedDispatch-1' tools/unattended/unattended.test.sh` — the builder's greps printed 3 and 0; the old space-holding arm is gone from the suite

**Evidences:** TOOL-aSmoothedDispatch-2
- AC1 — `remove_run_state_writes` — the builder's pass probe printed `a memory/builds/s memory/builds/s/RUN.md.bak removed=1` and `a b removed=`
- AC2 — `verb_dispatch` — the builder's pass probe's pipeline printed the matches in order (five lines, the extra one the second `_rw_keep[@]` use, order held) and the old message count 0
- AC3 — `dispatch declared` — the condition-3 arm printed `dispatch declared` and the note at the tip; observed RED on its staged break at the close and GREEN at the tip `b1e48cc59` (staging `u2-call`, the call deleted: the note went missing and the parked row named the run-state file)
- AC4 — `no --writes path except the run's run-state file` — the arm printed the refusal at the tip; observed RED on its staged break at the close and GREEN at the tip `b1e48cc59` (staging `u2-call`, and staging `c4a` with the equality swapped for `overlaps` for the containing-path arm)
- AC5 — `tr -s '\n ' ' ' < tools/unattended/VERBS.template.md | grep -o 'run-state file is removed from the declaration' | wc -l` — the builder's grep counted the sentence once, and `cmp` of the two verb carrier copies exited 0

**Evidences:** TOOL-aSmoothedDispatch-3
- AC1 — `GOV_RUNLOG=0 bash tools/unattended/unattended.sh --help; echo "rc=$?"` — the builder's pass probe printed the verb line and `rc=0`; the suite arms observed RED on its staged break at the close and GREEN at the tip `b1e48cc59` (staging `u3`: `--help exits 0: expected [0], got [1]`)
- AC2 — `diff <(GOV_RUNLOG=0 bash tools/unattended/unattended.sh -h) <(GOV_RUNLOG=0 bash tools/unattended/unattended.sh --help)` — the builder's pass probe's `diff` was empty; the suite arm observed RED on its staged break at the close and GREEN at the tip `b1e48cc59` (staging `u3`)
- AC3 — `--help` — the builder's pass probe found the `--help` list identical to check 14's refusal list
- AC4 — `grep -c '^#   unattended.sh --help ' tools/unattended/unattended.sh` — the builder's pass probe's grep printed 1, and the suite carries 4 `--help` lines; the suite's `unattended.sh --help` arm observed RED on its staged break at the close and GREEN at the tip `b1e48cc59` (staging `u3`)
- AC5 — `usage:` — the builder's pass probe printed `usage:` and `rc=2`, and the tip run of region two kept that arm green

**Evidences:** TOOL-aSmoothedDispatch-4
- AC1 — `bash "$SCRATCH/sd4.sh"` — the builder's pass probe printed `verdict clean 0` and `verdict foreign 0`; the region-three foreign-only arm observed RED on its staged break at the close and GREEN at the tip `b1e48cc59` (staging `u4`, the inline block restored)
- AC2 — `bash "$SCRATCH/sd4.sh"` — the builder's pass probe printed `verdict own 1` and `verdict both 1`; unit 8's both-hits arm observed RED on its staged break at the close and GREEN at the tip `b1e48cc59` (staging `c3a`)
- AC3 — `bash "$SCRATCH/sd4.sh"` — the builder's pass probe printed each refusal row; unit 8's verdict arms observed RED on its staged break at the close and GREEN at the tip `b1e48cc59` (stagings `c3b` undercount, `c3c` stale, `s3-unattributed`, `s3-nosummary`)
- AC4 — `bash "$SCRATCH/sd4.sh"` — the builder's pass probe printed `cache unchanged runs 1 skipped 1`; the cache arm observed RED on its staged break at the close and GREEN at the tip `b1e48cc59` (staging `u4`: `spec-token check skipped` went missing)
- AC5 — `bash "$SCRATCH/sd4.sh"` — the builder's pass probe printed the re-run counts; unit 8's cache steps b and c observed RED on its staged break at the close and GREEN at the tip `b1e48cc59` (stagings `c3a` with `$fp` dropped and `c3b` with `$hd` dropped)
- AC6 — `bash "$SCRATCH/sd4.sh"` — the builder's pass probe printed `cache refused runs 7`; unit 8's step e observed RED on its staged break at the close and GREEN at the tip `b1e48cc59` (staging `c3a`, the record write moved above the verdict)
- AC7 — `bash "$SCRATCH/sd4.sh"` — the builder's pass probe printed `cache off runs 10 said 2`; unit 8's step f observed RED on its staged break at the close and GREEN at the tip `b1e48cc59` (staging `c3a`: `a cache-off dispatch writes no spec-token key: expected [none], got [written]`)
- AC8 — `grep -c 'run_spec_token_check "$slug" || return 1' tools/unattended/unattended.sh` — the builder's grep printed 1
- AC9 — `cmp tools/unattended/VERBS.template.md memory/guides/UNATTENDED-VERBS.md` — `cmp` exited 0 and the protocol stayed one byte under its ceiling

**Evidences:** TOOL-aSmoothedDispatch-5
- AC1 — `scratch` — the checker suite's `--spec` arms observed RED on its staged break at the close and GREEN at the tip `b1e48cc59` (staging `t-u5`, the checker at `ae6735c1f`: `SD5 AC1 --spec grades an UNTRACKED spec and REDS on its leg — expected rc 1, got 0`)
- AC2 — `--spec` — the suite's arms observed RED on its staged break at the close and GREEN at the tip `b1e48cc59` (staging `t-u5`)
- AC3 — `python tools/check-spec-tokens.py --spec` — the suite's four refusal arms observed RED on its staged break at the close and GREEN at the tip `b1e48cc59` (staging `t-u5`: `--spec with no value REFUSES with exit 2 — expected rc 2, got 1` and its siblings)
- AC4 — `**hands-off**` — the suite's hands-off arm observed RED on its staged break at the close and GREEN at the tip `b1e48cc59` (staging `t-u5`)
- AC5 — `memory/project/spec-token-waivers.txt` — the suite's stale-row arm observed RED on its staged break at the close and GREEN at the tip `b1e48cc59` (staging `t-u5`)
- AC6 — `python tools/check-spec-tokens.py` — the unscoped run kept its full output at the tip, and the token suite passed there (rc 0, 550 s)
- AC7 — `agent_type` — the hook suite's G-AC2 allow row went RED under `checkGateLeg` prefix matching (staging `g-u5prefix`), and the G-AC1 deny row under the widened fixture allowlist (staging `g-u5allow`); the suite-deny row was never seen RED, since allowlisting the leg leaves a suite refused
- AC8 — `grep -n -- "--spec" tools/check-spec-tokens.py` — the builder's grep found the flag at docstring lines 243 and 252, above the first import

**Evidences:** TOOL-aSmoothedDispatch-6
- AC1 — `RUN.md` — the hook suite's D-AC1 row observed RED on its staged break at the close and GREEN at the tip `b1e48cc59` (staging `g-u6rev`, the hook at `af3ec143c`)
- AC2 — `RUN.md` — the D-AC2 rows passed at the tip and at `af3ec143c` alike, because the base hook refuses the same card; never seen RED, recorded as unseen
- AC3 — `RUN.md` — the D-AC3 row observed RED on its staged break at the close and GREEN at the tip `b1e48cc59` (staging `g-u6any`, the fallback admitting any dispatched unit, and staging `g-u6rev`)
- AC4 — `agent_type=gov-builder` — both D-AC4 rows observed RED on its staged break at the close and GREEN at the tip `b1e48cc59` (staging `g-u6rev`)
- AC5 — `TOOL-x-1 is buildable` — the D-AC5 row observed RED on its staged break at the close and GREEN at the tip `b1e48cc59` (staging `g-u6rev`)
- AC6 — `node -p "require('./tools/hooks/scratch-guard.js').RUN_STATE_FILE"` — the D-AC6 row observed RED on its staged break at the close and GREEN at the tip `b1e48cc59` (staging `g-u6rev`: `RUN_STATE_FILE is 'undefined'`)
- AC7 — `grep -n "dispatch" tools/hooks/README.md` — the builder's grep hit 12 README lines naming the dispatch fallback

**Evidences:** TOOL-aSmoothedDispatch-7
- AC1 — `grep -n -F -- "--spec" tools/roles/house/gov-spec-writer.md` — the builder's grep printed the command line, and the overlay states each point S1 names
- AC2 — `grep -n -E "tools/|^#|[{][{]|BUILD-METHOD|TEMPLATE-SPEC|HYGIENE[.]md|REVIEW-PROTOCOL|UNATTENDED-PROTOCOL" tools/roles/house/gov-spec-writer.md` — the builder's grep printed nothing
- AC3 — `python tools/roles/render_agents.py --write` — `render_agents.py --check` exited 0 and only the spec-writer agent file moved
- AC4 — `.claude/roles.json` — `.claude/roles.json` gives the spec writer only those two gates, and the hook admitted the one-spec call
- AC5 — `python tools/check-spec-tokens.py --spec memory/builds/aSmoothedDispatch/spec/2026-11-10-spec-TOOL-aSmoothedDispatch-7.md` — the one-spec run on unit 7's spec printed its scope line and exited 0; at the close spec 9's writer ran it on its own spec before returning (`e8b0ea8f5`)

**Evidences:** TOOL-aSmoothedDispatch-8
- AC1 — `grep -c 'spec-tokens: HIT' tools/roles/house/gov-spec-writer.md .claude/agents/gov-spec-writer.md` — the builder's greps printed 0 0 then 1 1, and `render_agents.py --check` exited 0
- AC2 — `grep -nF 'print(f"spec-tokens: {f} [{kind}] ' tools/check-spec-tokens.py` — the docstring grep printed the line; the checker suite's overlay arm observed RED on its staged break at the close and GREEN at the tip `b1e48cc59` (staging `t-u8`, the overlay put back to the HIT sentence)
- AC3 — `bash "$SCRATCH/sd8.sh"` — the builder's pass probe printed the six rows; the five verdict arms observed RED on its staged break at the close and GREEN at the tip `b1e48cc59` across stagings `c3a`, `c3b`, `c3c`, `s3-unattributed` and `s3-nosummary`
- AC4 — `grep -c 'TOOL-aSmoothedDispatch-8 AC4' tools/unattended/unattended.test.sh` — the grep printed 6; cache steps a to f observed RED on its staged break at the close and GREEN at the tip `b1e48cc59` across stagings `c3a` (a, b, e, f), `c3b` (c) and `c3c` (d)
- AC5 — `grep -c 'TOOL-aSmoothedDispatch-8 AC5' tools/unattended/unattended.test.sh` — the grep printed 4; the four arms observed RED on its staged break at the close and GREEN at the tip `b1e48cc59` (staging `c4a`)
- AC6 — `grep -n 'route.units.some' tools/hooks/scratch-guard.js` — the grep printed one line; the hook suite's arm observed RED on its staged break at the close and GREEN at the tip `b1e48cc59` (staging `g-u8`: `the context still names a dispatch row`)
- AC7 — `python tools/check-spec-tokens.py --legs-for tools/unattended/unattended.sh` — `--legs-for` named the scratch-guard self-test for the driver and not for its library
- AC8 — `grep -c 'scratch-guard self-test' memory/builds/aOrientedCast/spec/2026-10-13-spec-TOOL-aOrientedCast-28.md` — the grep counted the leg in the revised foreign spec, and `--spec` on it exited 0 at rev-3

**Evidences:** TOOL-aSmoothedDispatch-9
- AC1 — `grep -c "^_rf_exempt='brief|check 49: .*hash'\$" tools/unattended/unattended.test.sh` — the greps print 1 and 0; the region-two matrix observed RED on its staged break at the close and GREEN at the tip `b1e48cc59` (staging `u9-ac1`, the row put back: `the exemption for --dispatch is stale`), and the tip run of region two equals the base's FAIL lines
- AC2 — `grep -cF -- "--writes \$'" tools/unattended/unattended.test.sh` — the greps print 0 and 1
- AC3 — `grep -c 'TOOL-aSmoothedDispatch-9 AC3' tools/unattended/unattended.test.sh` — the grep prints 2; both arms observed RED on its staged break at the close and GREEN at the tip `b1e48cc59` (staging `c4a`, IFS widened to `\r`), and the tip run of region four equals the base's FAIL lines
