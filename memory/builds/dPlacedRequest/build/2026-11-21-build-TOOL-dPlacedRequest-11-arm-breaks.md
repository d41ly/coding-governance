**Serves:** journal TOOL-dPlacedRequest-11

# TOOL-dPlacedRequest-11 — the staged breaks the close's arm observations used

The build method owes each `New arm:` line a RED reading on its staged break and a GREEN one once restored. These ran
at VERIFYING in scratch clones of `2db4a921f` on node d, LF-normalised, with `TMPDIR` in POSIX form. A break is a text
replacement applied by a scratchpad helper, or a file checked out at an older commit: `9e21ac760` is the run's pinned
BASE, and `95c3103ad` is the tree the closing review read. The unattended kit's suites are waived for this landing
(README rule), so its 47 arm lines are not observed here (PINNED). The GREEN readings of the manifest-check, push-main,
run-selftests and pre-push suites' arms are the flagged bar's, on the prepared merge.

## The breaks

```json
{
 "u4-continue-closed": {
  "file": "tools/loop/placement.py",
  "old": "        if terminal:\n            return \"the build %s is %s, not live\" % (build, status)\n        return read_build_lease(root, build)",
  "new": "        if False:\n            return \"the build %s is %s, not live\" % (build, status)\n        return read_build_lease(root, build)"
 },
 "u10-predicate-rerun": {
  "file": "tools/loop/placement.py",
  "old": "    failed += [\"scenario-predicate %s\" % t for t in named if t not in want]\n",
  "new": "    pass\n"
 },
 "u5-relayed-consent": {
  "file": "tools/loop/placement.py",
  "old": "    if rc == 0:\n        return None\n    said = \" / \".join(lines) or err or \"exit %d\" % rc\n    return (\"relayed: %s\" % said)",
  "new": "    if True:\n        return None\n    said = \" / \".join(lines) or err or \"exit %d\" % rc\n    return (\"relayed: %s\" % said)"
 },
 "u5-audit-cause-placement": {
  "file": "tools/loop/breakpoints.py",
  "old": "\"owed\" if PLACED_REVIEWS[name] == \"design\" else \"placement\"",
  "new": "\"placement\""
 },
 "u5-placed-unhooked": {
  "file": "tools/loop/breakpoints.py",
  "old": "                              \"placed\": read_placed_breakpoints(build, root)})",
  "new": "                              \"placed\": []})"
 },
 "u14-draw-removed": {
  "file": "tools/loop/placement.py",
  "old": "    draw = functools.partial(run_request_draw_verb, root, args.request, cause) if cause else None\n",
  "new": "    draw = None\n"
 },
 "u21-route-leases-first": {
  "file": "tools/loop/claim.py",
  "old": "    if cause in TERMINAL_CAUSES:\n        return \"refuse\"\n    if cause in WAIT_CAUSES:\n        return \"wait\"\n    if cause == \"overlap\":",
  "new": "    if leases == \"warn\":\n        return \"noted\"\n    if cause in TERMINAL_CAUSES:\n        return \"refuse\"\n    if cause in WAIT_CAUSES:\n        return \"wait\"\n    if cause == \"overlap\":"
 },
 "u19-raw-bytes-key": {
  "file": "tools/loop/request.py",
  "old": "    return hashlib.sha256(norm.encode(\"utf-8\")).hexdigest()[:KEY_HEX]",
  "new": "    return hashlib.sha256(text.encode(\"utf-8\")).hexdigest()[:KEY_HEX]"
 },
 "u7-run-refuted": {
  "file": "tools/loop/probe.py",
  "old": "answers.append(\"confirmed\" if (ran[1], ran[2]) == (code, digest) else \"refuted\")",
  "new": "answers.append(\"confirmed\")"
 },
 "u8-seed-bad": {
  "file": "tools/loop/loop_lib.py",
  "old": "        elif not (isinstance(actor, str) and actor.startswith(\"role:\")):\n            refusals.append(\"the item %s seed %r sits on the actor",
  "new": "        elif False:\n            refusals.append(\"the item %s seed %r sits on the actor"
 },
 "u6-unfold-unregistered": {
  "file": "tools/loop/loop_lib.py",
  "old": "refusals.append(\"the item %s unfolds %r, which is no ns of the namespace registry\" % (tag, word))",
  "new": "pass"
 },
 "u7-role-no-probe": {
  "file": "tools/loop/loop_lib.py",
  "old": "refusals.append(\"the item %s, a role item, carries no probe outcome: it could not ask for a test\" % tag)",
  "new": "pass"
 },
 "u21-patch-no-parents": {
  "file": "tools/memory-tree/gen_build_index.py",
  "old": "        head.append(f\"parents: {args['origin']}\")\n",
  "new": "        pass\n"
 },
 "u1-fleet-tag-any-user": {
  "file": "tools/playbook/render_playbook.py",
  "old": "    u = user.strip().lower()\n    for row in rows:\n        if u and row['user'].strip().lower() == u:",
  "new": "    u = user.strip().lower()\n    return rows[0]['tag']\n    for row in rows:\n        if u and row['user'].strip().lower() == u:"
 },
 "u9-abort-on-refused": {
  "file": "tools/govkit/steps/kickoff_facts_to_overlay.py",
  "old": "    for n, finding in refused:\n        print(f\"{SAY}: up · bullet {n} stays in {SECTION} as guide text · {finding}\")\n",
  "new": "    for n, finding in refused:\n        print(f\"{SAY}: up refused · bullet {n} · {finding}\")\n        return 1\n"
 },
 "u2-silent-checker-as-card": {
  "file": "tools/hooks/scratch-guard.js",
  "old": "const out = r && !r.error && r.status === 0 ? String(r.stdout || '').trim()",
  "new": "const out = r ? (String(r.stdout || '').trim() || '/c/no-card-answered')"
 },
 "u43-no-kill-signal": {
  "file": "tools/hooks/scratch-guard.js",
  "old": "r = spawnSync(bash, [engine, '--card', '--path', '--session', sid], { cwd, encoding: 'utf8', timeout: CARD_PATH_BOUND_MS, killSignal: 'SIGKILL', stdio: ['ignore', 'pipe', 'pipe'], windowsHide: true })",
  "new": "r = spawnSync(bash, [engine, '--card', '--path', '--session', sid], { cwd, encoding: 'utf8', stdio: ['pipe', 'pipe', 'pipe'], windowsHide: true })"
 },
 "u34-bare-bash": {
  "file": "tools/hooks/scratch-guard.js",
  "old": "  const bash = found.bash\n",
  "new": "  const bash = 'bash'\n"
 },
 "u34-no-fold": {
  "file": "tools/hooks/scratch-guard.js",
  "old": "    let native = buildNativePath(out)\n",
  "new": "    let native = out\n"
 },
 "u99-every-host-row": {
  "file": "tools/hooks/scratch-guard.test.sh",
  "old": "[ \"$sg_got\" = \"card — the stub card\" ] && { echo \"ok   AC28 a bash first on PATH that cannot run the checker is passed over, and the card is read\"; pass=$((pass+1)); } \\\n  || { echo \"FAIL AC28 a bash first on PATH that cannot run the checker is passed over, and the card is read: $sg_got\"; fail=$((fail+1)); }\n",
  "new": ""
 },
 "u99-sg-win-empty": {
  "file": "tools/hooks/scratch-guard.test.sh",
  "old": "MINGW*|MSYS*|CYGWIN*) sg_win=1;",
  "new": "MINGW*|MSYS*|CYGWIN*) sg_win=\"\";"
 },
 "u11-clear-any-push": {
  "file": ".githooks/pre-push",
  "old": "[ -z \"$PUSH_REFUSAL\" ] || [ -z \"$main_local\" ] || rm -f \"$PUSH_REFUSAL\"",
  "new": "[ -z \"$PUSH_REFUSAL\" ] || rm -f \"$PUSH_REFUSAL\""
 },
 "u34-base-missing-predicate": {
  "file": ".githooks/pre-push",
  "old": "&& { [ \"${_sg_rows[_sg_i + 1]}\" = \"${_sg_cands[_sg_i / 3]%% *}^ missing\" ] || [ \"${_sg_rows[_sg_i + 2]}\" = \"tree 0\" ]; }",
  "new": "&& [ \"${_sg_rows[_sg_i + 1]}\" = \"${_sg_cands[_sg_i / 3]%% *}^ missing\" ]"
 },
 "u11-post-merge-byte": {
  "file": "tools/run-gates/post-merge.sh",
  "old": "# parented on the tip its caller read, so",
  "new": "# parented on the tip its caller reads, so"
 },
 "u13-helper-removed": {
  "file": "tools/lib/gov-feed.sh",
  "old": "FEED_WRITER_HELPER_FNS=\"add_feed_event write_feed_success write_gov_ref\"",
  "new": "FEED_WRITER_HELPER_FNS=\"add_feed_event write_gov_ref\""
 },
 "u34-cands-reorder": {
  "file": "tools/hooks/scratch-guard.js",
  "old": "const cands = [process.env.GOV_BASH || '', ...onPath,",
  "new": "const cands = [...onPath, process.env.GOV_BASH || '',"
 },
 "u98-registry-renamed": {
  "file": "tools/playbook/fleet.toml",
  "old": "user = \"daily-agent\"",
  "new": "user = \"daily-agent-renamed\""
 },
 "u99-substring-tag": {
  "file": "tools/run-gates/run-selftests.sh",
  "old": "        [ \"$user\" != \"$tok\" ] || { printf '%s' \"${BASH_REMATCH[1]}\"; return 0; }",
  "new": "        case \"$user\" in *\"$tok\"*) printf '%s' \"${BASH_REMATCH[1]}\"; return 0 ;; esac"
 }
}
```

## The readings

| Unit | Arm | Break | RED | GREEN |
|---|---|---|---|---|
| TOOL-dPlacedRequest-4 | `tools/loop/placement.py` | `u4-continue-closed` | FAIL continue-closed | placement fixtures PASS |
| TOOL-dPlacedRequest-10 | `tools/loop/placement.py` | `u10-predicate-rerun` | FAIL predicate-fails | placement fixtures PASS |
| TOOL-dPlacedRequest-5 | `tools/loop/placement.py` | `u5-relayed-consent` | FAIL relayed | placement fixtures PASS |
| TOOL-dPlacedRequest-5 | `tools/loop/placement.py` | `u5-audit-cause-placement` | FAIL audit-request-owed-only | placement fixtures PASS |
| TOOL-dPlacedRequest-5 | `tools/loop/breakpoints.py` | `u5-placed-unhooked` | FAIL placed | breakpoint fixtures PASS |
| TOOL-dPlacedRequest-14 | `tools/loop/budget.py` | `u14-draw-removed` | FAIL placement-loop | budget fixtures PASS |
| TOOL-dPlacedRequest-21 | `tools/loop/claim.py` | `u21-route-leases-first` | FAIL refusals | claim fixtures PASS |
| TOOL-dPlacedRequest-100 | `tools/loop/claim.py` | driver at `95c3103ad` | stale-holder MISSED, exit 4, epoch unmoved | claim fixtures PASS |
| TOOL-dPlacedRequest-19 | `tools/loop/request.py` | `u19-raw-bytes-key` | FAIL normalised-pair | request fixtures PASS |
| TOOL-dPlacedRequest-7 | `tools/loop/probe.py` | `u7-run-refuted` | FAIL run-refuted | probe fixtures PASS |
| TOOL-dPlacedRequest-8 | `tools/loop/loop_lib.py` | `u8-seed-bad` | FAIL seed-bad, and the other seed plants | loop definition fixtures PASS |
| TOOL-dPlacedRequest-6 | `tools/loop/loop_lib.py` | `u6-unfold-unregistered` | FAIL unfold-unregistered | loop definition fixtures PASS |
| TOOL-dPlacedRequest-7 | `tools/loop/loop_lib.py` | `u7-role-no-probe` | the selftest exits 1 | loop definition fixtures PASS |
| TOOL-dPlacedRequest-21 | `tools/memory-tree/gen_build_index.py` | `u21-patch-no-parents` | the placed patch arm FAILs | build-index selftest PASS |
| TOOL-dPlacedRequest-1 | `tools/playbook/render_playbook.py` | `u1-fleet-tag-any-user` | the fleet-tag arm FAILs | playbook selftest PASS |
| TOOL-dPlacedRequest-9 | `tools/govkit/steps/kickoff_facts_to_overlay.py` | `u9-abort-on-refused` | FAIL refused, AC6 | the step's fixture PASS |
| TOOL-dPlacedRequest-2 | `tools/hooks/scratch-guard.test.sh` | `u2-silent-checker-as-card` | FAIL AC10 | scratch-guard PASS |
| TOOL-dPlacedRequest-43 | `tools/hooks/scratch-guard.test.sh` | `u43-no-kill-signal` | FAIL AC18, three rows | scratch-guard PASS |
| TOOL-dPlacedRequest-34 | `tools/hooks/scratch-guard.test.sh` | `u34-bare-bash`, `u34-no-fold` | FAIL AC28 | scratch-guard PASS |
| TOOL-dPlacedRequest-95 | `tools/hooks/scratch-guard.test.sh` | hook at `95c3103ad` | FAIL AC1, all three fixtures | scratch-guard PASS |
| TOOL-dPlacedRequest-99 | `tools/hooks/scratch-guard.test.sh` | `u99-every-host-row`, `u99-sg-win-empty` | NOT RED: the suite stays green | scratch-guard PASS |
| TOOL-dPlacedRequest-11 | `tools/lib/resolve-python.test.sh` | `u11-post-merge-byte` | FAIL `gov_ref_sh` copy drifted | flagged bar |
| TOOL-dPlacedRequest-13 | `tools/lib/resolve-python.test.sh` | `u13-helper-removed` | FAIL the feed-writer census | flagged bar |
| TOOL-dPlacedRequest-34 | `tools/lib/resolve-python.test.sh` | `u34-cands-reorder` | FAIL the readCard order row | flagged bar |
| TOOL-dPlacedRequest-11 | `.githooks/pre-push.test.sh` | `u11-clear-any-push` | FAIL 8b | pre-push PASS |
| TOOL-dPlacedRequest-34 | `.githooks/pre-push.test.sh` | `u34-base-missing-predicate` | FAIL 9c | pre-push PASS |
| TOOL-dPlacedRequest-99 | `tools/run-gates/run-selftests.test.sh` | runner at `95c3103ad` | FAIL S5, four arms | flagged bar |
| TOOL-dPlacedRequest-99 | `tools/run-gates/run-selftests.test.sh` | `u99-substring-tag` | FAIL S2 | flagged bar |
| TOOL-dPlacedRequest-15, -29, -34, -43, -99 | `tools/push-main.test.sh` | lander at `9e21ac760` | FAIL arms 42 to 56 and the floor | flagged bar |
| TOOL-dPlacedRequest-98 | `tools/push-main.test.sh` | suite at `95c3103ad`, registry renamed | the skip line for 42-53 | flagged bar |
| TOOL-dPlacedRequest-1, -2, -9, -16, -49, -52, -56, -99 | `skills/session-kickoff/manifest-check.test.sh` | engine at `9e21ac760` | FAIL rows naming each unit | flagged bar |
| TOOL-dPlacedRequest-33, -34, -43 | `skills/session-kickoff/card-store.fixture.sh` | engine at `9e21ac760` | FAIL each owned plant | flagged bar |

## Findings

- **TOOL-dPlacedRequest-99's floor arm cannot red.** The scratch-guard suite executes more assertions than its pinned
  floor, so deleting the every-host AC28 row with the fold row forced off still passes; the floor that holds on every
  host is the measured count less the Windows-only row. Unit 99 is CLOSED, so this stands as a departure and an ask.
- **Three push-main arms fail under every lander tried**: 37, 39 and 40 red with the lander at the run's BASE, at
  `55fd5b426` and with the suite of `95c3103ad`, so they do not read this build's lander changes; the flagged bar's
  HEAD reading decides whether they are red at HEAD.
- **The resolve-python suite reds six rows at HEAD in the clone** that no commit of this build touched: three inline
  `resolve_python` copies, one `guarded_write_py` copy and the two idiom bans. They are inherited from the base.
- **The kickoff suite's card fixture could not clone the scratch clone** into two worktrees under the scratch
  root; the flagged bar reads that row in the run's own worktree.
