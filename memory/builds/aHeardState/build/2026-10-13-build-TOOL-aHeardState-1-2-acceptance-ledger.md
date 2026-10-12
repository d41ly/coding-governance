# aHeardState — the acceptance ledger, every unit

**Serves:** journal TOOL-aHeardState-1 TOOL-aHeardState-2 TOOL-aHeardState-3 TOOL-aHeardState-4 TOOL-aHeardState-5 TOOL-aHeardState-6 TOOL-aHeardState-7 TOOL-aHeardState-8

The suite rows below were observed at VERIFYING, on 2026-10-13 at `9ea94713`, from one run of
`tools/hooks/format-guard.test.sh`: 73 passed, 0 failed, about 16 s. The runlog selftest was not run.
The owner's ruling of 2026-10-06 leaves the owed kit suites to a run from the merged tree, so the
runlog rows below rest on direct CLI observations.

**Evidences:** TOOL-aHeardState-1
- AC1 — `last_assistant_message` — a pair-less payload under a routed fixture card blocks naming "no BUILD line", and with `stop_hook_active: true` prints nothing (direct check, then the suite's AC1 arms).
- AC2 — `##` — backticked, indented, bold, `##`-heading and fenced pairs each block naming rule r1 (suite, five arms).
- AC3 — `SPEC` — SPEC before BUILD, and a blank line between them, each block naming the [pair] rule (suite).
- AC4 — `node format-guard.js` — a well-formed adjacent bare pair exits 0 with empty stdout and stderr (direct check and suite).
- AC5 — `## route` — no card, a card without `## route`, an unlisted build, `agent_id` and SubagentStop each allow silently on both streams (suite).
- AC6 — `<git-dir>/format-guard/<sid>.head` — the first armed stop writes the sidecar; an unreported commit blocks naming its sha; committed and merged lines naming it allow; a wrong sha blocks (suite).
- AC7 — `<!-- microformats -->` — a fence-less fixture charter allows with a witness naming the fence; a BUILD definition with a fourth field blocks a message the real charter passes (suite).
- AC8 — `left` — a BUILD line without its left field blocks quoting the charter shape (suite).
- AC9 — `node format-guard.js` — non-JSON stdin exits 0 with empty stdout (suite).
- AC10 — `python tools/settings-merge.py --fragment format-guard.fragment.json --check` — settings-merge reports the fragment already wired, and check-hook-destinations lists it ok and clean.
- AC11 — amended rev-2 — the in-tree observation on the real card, LIVE.md, charter and HEAD replaces the end-to-end turn, which drew no feedback because this session's hooks load from its launch tree; `2026-10-12-build-TOOL-aHeardState-1-1-live-witness.md` records both, and the harness half is the owner's.

**Evidences:** TOOL-aHeardState-2
- AC1 — `python tools/runlog/runlog.py prose --session 86a064cd-3532-4202-93cd-dd26651975d3` — 34 turns, narration 47.7% ALARM, pair 15/32, exit 0, on 2026-10-13.
- AC2 — `runlog.py prose --transcript` — the mixed, alarm and calm scenarios print their pinned figures through the CLI; after TOOL-aHeardState-8, mixed reads 16.9% of 367 with interjections mean 1.7 and max 4.
- AC3 — `ALARM` — the alarm scenario reads ALARM on both marks and the calm one ok on both.
- AC4 — `--charter` — a fence-less charter prints "pair — unknown · no microformats fence in …".
- AC5 — `runlog.py prose` — an unknown session id exits 2 naming `C:/Users/daily-agent/.claude/projects`.
- AC6 — `format-guard.js` — the parity arm's eleven messages read the same verdict in both readers, holding an allow and a block (suite).

**Evidences:** TOOL-aHeardState-3
- AC1 — `python tools/govkit/govkit.py selfcheck` — it named the unpinned leg before `--write` and names no missing pin after it.
- AC2 — `tools/run-gates/selftest-budgets.txt` — the `format-guard self-test` row sits beside scratch-guard's, re-declared at 30 from two 16 s readings.

**Evidences:** TOOL-aHeardState-4
- AC1 — `python tools/check-spec-tokens.py --list` — it counted `tools/hooks/` at 6 legs before the edit and lists no such broad guard after it; govkit selfcheck names no guard in zero classes.

**Evidences:** TOOL-aHeardState-5
- AC1 — `tools/gate-legs.json` — the leg's guard reads the three hook files, `tools/runlog/prose.py`, `tools/runlog/extract.py` and `tools/lib/`, and `run-gates.sh --print-profile` still parses the manifest.

**Evidences:** TOOL-aHeardState-6
- AC1 — `python tools/memory-tree/gotchas.py --for-paths tools/gate-legs.json` — the checklist names held-suite-guard-misses-a-sibling-kit.

**Evidences:** TOOL-aHeardState-7
- AC1 — `format-guard.js` — after a commit, a chained stop prints nothing and the next unchained stop names commit aea294edb (direct check), and the suite's three chained-stop arms pass.

**Evidences:** TOOL-aHeardState-8
- AC1 — `format-guard.js` — HEAD's hook blocked "```npm test``` passed." above a bare pair as r1; the fixed hook and `prose.check_pair` allow it, and the suite's inline arm and parity message pass.
- AC2 — `format-guard.js` — a HEAD naming a missing ref allows with "HEAD is unreadable under …" on stderr (direct check and suite).
- AC3 — `format-guard.js` — the reason carries "not yet terminal" and "committed or merged line" (direct check and suite).
- AC4 — `runlog.py prose --charter` — a UTF-16 charter exits 0 with "pair — unknown · … is not readable as UTF-8".
- AC5 — `along no first-parent path` — the linked worktree, missing message, spec-less route, reset and unreadable-HEAD arms all pass in the suite, the worktree sidecar under `.git/worktrees/wt/format-guard/`.
- AC6 — `prose-charter.md` — `runlog.py prose` against the fixture charter reads the extended mixed scenario as 16.9% of 367, interjections unchanged, so the two-block message counts once and the sidechain record not at all.
