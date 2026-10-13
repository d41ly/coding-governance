# TOOL-aSweptBar-2 — the foreign-prefix probe contract: three engine self-tests declared whole, and format-guard's suite takes the probe stop

**Status:** CLOSED · rev-1 · 2026-10-13 · node a · Tier-1 · base 53b25884 · streams tooling · order 1

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-13-prompt-TOOL-aSweptBar-1-brief.md](../prompts/2026-10-13-prompt-TOOL-aSweptBar-1-brief.md) | research | TOOL-aSweptBar-1 TOOL-aSweptBar-3 TOOL-aSweptBar-4 TOOL-aSweptBar-5 TOOL-aSweptBar-6 |
| [2026-10-13-review-TOOL-aSweptBar-1-6-closing-diff-round1.md](../reviews/2026-10-13-review-TOOL-aSweptBar-1-6-closing-diff-round1.md) | diff-review | TOOL-aSweptBar-1 TOOL-aSweptBar-3 TOOL-aSweptBar-4 TOOL-aSweptBar-5 TOOL-aSweptBar-6 |

<!-- /gen:spec-records -->

## 1. Goal

The foreign-prefix parity leg reds four rows over `53b25884` as undeclared whole runs: each printed
no probe marker, so each ran every arm. Three are `--selftest` modes of shipped engines, which the
leg's own declaration already handles for their siblings, and one is a suite that never got the
probe stop. This unit closes all four, so the leg asks its prefix question of every row again.

## 2. Scope (IN)

- **S1** — `WHOLE_RUN` in `tools/run-gates/foreign-prefix.gov.test.sh` gains `held-halves selftest`,
  `roles render selftest` and `routed-commits selftest`, each carrying the reason the existing
  `--selftest` rows carry, byte for byte. Observed by AC1.
- **S2** — `tools/hooks/format-guard.test.sh` takes the two-line one-arm stop that
  `tools/hooks/scratch-guard.test.sh:179` and the line after it carry, byte for byte, placed after the
  last AC1 check and before the `# AC2` comment. Observed by AC2.

## 3. Non-goals (OUT)

- No probe site inside `held_halves.py`, `render_agents.py` or `routed_commits.py`. Each is a shipped
  engine, so a site there would be adopter-facing, which is the reason the `WHOLE_RUN` rows exist.
- format-guard's resolver heredoc at line 62 belongs to `TOOL-aSweptBar-4`, and its fork idioms to
  `TOOL-aSweptBar-5`. Both units are ordered after this one, so each edits the file this unit leaves.
- The other reds in the same leg log stay with their owners. The roles adopter self-test is
  aOrientedCast's, and the unattended driver's shard 8/8 is `TOOL-aSweptBar-1` S5.
- Whether the three rows pass at the second and third prefixes is not this unit's question. The leg
  fails fast at the prefix grain, so the bar never reached those prefixes. A red there is a real prefix
  defect, and it goes to the main loop.

## 4. Design

The leg classifies a row as whole when its name equals a `WHOLE_RUN` entry's text before the first
`|` (`tools/run-gates/foreign-prefix.gov.test.sh:191`). `check_declarations` at line 258 reds an
entry that names no row of the loaded population, so each name must be the row's exact name. All
three appear in the bar's leg log under these names. Each is a gate leg whose argv ends `--selftest`:
`held_halves.py` ships as an engine under the run-gates kit's `**` rule, and `render_agents.py` and
`routed_commits.py` ship with their kits. They are the same class as the `--selftest` rows already
declared, so they take the same reason rather than a new one.

The format-guard stop is copied, not re-worded. A probe run then prints the marker, its `PASS` line
and exits, after the four AC1 checks have driven `format-guard.js` through `run_stop`. That puts the
stop after an arm that ran the subject, as the scratch-guard comment requires. The placement before
`# AC2` is the one the brief records aHeardState asking for. No assertion is added, so the suite's
`FLOOR_ASSERTIONS` of 73 does not move.

### Files touched (estimate)

- `tools/run-gates/foreign-prefix.gov.test.sh`
- `tools/hooks/format-guard.test.sh`

### Alternatives rejected

- A probe site in each engine's `--selftest` path: it ships to adopters, and the declared reason for
  the ten existing rows is exactly that.
- Placing format-guard's stop above the AC1 checks: a probe that stops before the hook runs passes
  without touching its subject, which is the gap the leg's header names as unchecked.

## 5. Acceptance criteria

- **AC1** — When `git diff 53b25884 -- tools/run-gates/foreign-prefix.gov.test.sh` runs, it adds
  exactly three `WHOLE_RUN` entries, `held-halves selftest`, `roles render selftest` and
  `routed-commits selftest`, each with the reason `a --selftest mode of a shipped engine, so a probe
  site would be adopter-facing`. Each name equals a `"name"` in `tools/gate-legs.json`, which
  `grep -c '"name": "held-halves selftest"' tools/gate-legs.json` and its two siblings answer with 1.
  Red when: a name differs from its row by a byte and `check_declarations` reds the entry as naming
  no row, or a row stays undeclared and the leg reds it as an undeclared whole run.
- **AC2** — When the two lines after `grep -n '^# FOREIGN_PREFIX_PROBE' tools/hooks/format-guard.test.sh`
  are compared with `sed -n 179,180p tools/hooks/scratch-guard.test.sh`, they are identical. The stop's
  line number falls between the line of `AC1 stop_hook_active true allows` and the line of `# AC2`.
  Red when: the stop sits above the first AC1 check, so a probe never runs the hook, or below `# AC2`.

## 6. Gates

`foreign-prefix parity (every self-test at three prefixes)` · `format-guard self-test` · `agent-cap self-test` · `scratch-guard self-test` · `verifier fan-out self-test` · `review-join self-test` · `hook destinations self-test`

New arm: tools/run-gates/foreign-prefix.gov.test.sh · covers AC1 AC2 · delete one of the three new WHOLE_RUN entries and the leg reds that row as an undeclared whole run; delete format-guard's stop and the leg reds format-guard self-test the same way; the leg's `--kit` selector runs one row per observation · none

## 7. Open questions

none

## 8. Revision log

- rev-1 · 2026-10-13 · initial draft from the build brief, the four rows read from the bar's leg log.

## 9. Reuse audit

`tools/codebase-map/reuse_lookup.py "re-arm a suite arm a landing disarmed so its staged break reds
again"` returned name-stem neighbours only, such as `arm`, `armed` and `run_arms`, so no existing seam
fits as a helper and none is minted. The seams this unit extends are the leg's own: the `WHOLE_RUN`
declaration with its existing `--selftest` reason, and the probe stop at
`tools/hooks/scratch-guard.test.sh:179`, which `tools/hooks/agent-cap.test.sh:146` already copies.
The recall probe returned the TOOL-aRepatriatedFork-52 acceptance ledger, which observed both
directions of this contract when the probe stop was introduced.

Recall terms used: `python tools/memory-recall/query.py "why did suite arms go red after landings
merged without a bar, and which fixture or helper re-arms them" --terms "bar-less landing stale
fixture arm disarmed probe marker WHOLE_RUN cover pass gate-bar-green reuse digest GATE_FULL key"`
