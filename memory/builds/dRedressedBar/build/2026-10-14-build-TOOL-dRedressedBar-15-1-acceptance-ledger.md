# TOOL-dRedressedBar-15 — acceptance ledger

**Serves:** journal TOOL-dRedressedBar-15

This is the build pass of agent-cap's adopter at a per-kit prefix. `<p14>` is `109fbb4ab`, unit 14's
build pass, named by its `Pass:` trailer. `<p15a>` is `0a178ed8f`, the product commit, and `<p15>`
is `4d3cae332`, the mint commit. The product commit added `resolve_adopter_argv` to
`tools/govkit/govkit.py` after `target_context`. `_cmd_apply`'s CONFIGURE loop and `_cmd_update`'s
gained loop take their resolved argv from it, and the configured entry's own `d`, `ctx` and `_ctx_g`
still classify the exit. The comment above `_cfg_run` is restated for unit 14's early receipt. The
selfcheck bare-target block gained the cross-entry arm: the `via` rules, then the ownership join over
the `[adopt]`, `[check]`, `[[gate_leg]]` and `[[regenerate]]` argv elements, with its locals
prefixed `_xa_`. `tools/hooks/kit.toml`'s `[adopt]` table is now `via = "settings-merge"` alone.
`tools/govkit/selftest.py` gained the `[dRB-15]` checks on the `[dRB-14]` apply and seven
cross-entry scratch govs after the `bad_g` check. `memory/map/generated/symbols.json` carries the new
function. The mint commit moved the hooks kit from 1.39 to 1.40. This record and spec 15's status
cell are the pass's third commit.

No merge bar, no self-test suite and no gate leg ran in this pass, and no slice of the suite ran
either. scratch-guard refused `python tools/govkit/govkit.py selfcheck` over the worktree to this
role as row G1, the `govkit selfcheck` leg, so AC6 is observed here only by a stand-in, and the leg's
own run is owed to the close. Every other criterion was observed with a direct probe. Scratch
programs drove `python tools/govkit/govkit.py apply` over fresh `git init` targets under
`%TEMP%/drb15*`. Each target had `core.autocrlf false` and `DEPLOY_FULL`'s answers, plus the per-kit
table a criterion names. The green halves ran from the worktree. The red halves ran from a local
clone at `%TEMP%/drb15g14`, checked out at `<p14>`, and a second clone at `%TEMP%/drb15g15`, checked
out at `<p15>` and given one staged break. These probes stand in for `govkit selftest` (AC1, AC7),
`govkit selfcheck` (AC6), `kit epoch` (AC8), `encoding posture` and
`codebase-map coverage + freshness` (AC9), and `memory hygiene` (this ledger). The section 7
gates are owed to the close, with both `New arm:` lines' RED-first observations over `<p14>`'s engine. The `[dRB-14]` block's
check that exactly one line opens `govkit: kit 'agent-cap'` reads the same apply the `[dRB-15]`
checks read, and it is expected red at the close until unit 17's S1 narrows it.

**Evidences:** TOOL-dRedressedBar-15
- AC1 — `scripts/hooks/agent-cap.js` — at `<p15>`, the three-kit apply
  `apply --kits agent-cap,settings-merge,kickoff-manifest` over the per-kit-prefix target
  `%TEMP%/drb15d1` exited 0. Exactly one line opened `govkit apply — CONFIGURE settings-merge:` and
  exactly one opened `govkit apply — CONFIGURE agent-cap:`, and both ended `adopter exit 0`. No line
  opened `govkit: kit '`. The receipt held the row `scripts/hooks/agent-cap.js` with source
  `tools/hooks/agent-cap.js`. `.claude/settings.json`'s `PreToolUse` group with matcher
  `Workflow|Agent` held one command, `node "${CLAUDE_PROJECT_DIR}/scripts/hooks/agent-cap.js"`.
  Over the `<p14>` clone, in `%TEMP%/drb15r1`, the run exited 1. The agent-cap line ended
  `adopter exit 2`, and exactly one line opened `govkit: kit 'agent-cap'`. Its stderr tail read
  `python: can't open file '…\drb15r1\scripts\settings-merge.py': [Errno 2] No such file or directory`.
- AC2 — `adopter exit 0` — the default-prefix apply ran from the worktree into `%TEMP%/drb15a2` and
  from the `<p14>` clone into `%TEMP%/drb15r2`. Both exited 0. Each printed the same two lines
  carrying `CONFIGURE `, `govkit apply — CONFIGURE settings-merge: adopter exit 0` and
  `govkit apply — CONFIGURE agent-cap: adopter exit 0`. The two `.claude/settings.json` files had one
  sha256, `3e4dfb45…16310`.
- AC3 — `tools/hooks/agent-cap.js` — with `[kit.settings-merge] prefix = "scripts"`, the worktree's
  apply into `%TEMP%/drb15a3` exited 0, and both CONFIGURE lines ended `adopter exit 0`.
  `.claude/settings.json` held one command, `node "${CLAUDE_PROJECT_DIR}/tools/hooks/agent-cap.js"`.
  Over the `<p14>` clone, in `%TEMP%/drb15r3`, the run exited 1. The agent-cap line ended
  `adopter exit 2`, and its problem line carried `can't open file '…\drb15r3\tools\settings-merge.py'`.
- AC4 — `apply --kits agent-cap,kickoff-manifest` — over `%TEMP%/drb15a4`, the worktree's
  `apply --kits settings-merge` exited 0 with
  `CONFIGURE settings-merge: adopter exit 2 — no-agent-cap-to-wire [accepted stop]`, and the target
  was committed with no settings.json. The second apply printed exactly one line opening
  `govkit apply — CONFIGURE agent-cap:`, ending `adopter exit 0`, and `.claude/settings.json` then
  held one command, carrying `tools/hooks/agent-cap.js`. In the `%TEMP%/drb15g15` copy at `<p15>`,
  the `via` line was deleted from `tools/hooks/kit.toml`, which is candidate C2, and committed. The
  same two applies, over `%TEMP%/drb15r4`, printed no `CONFIGURE agent-cap:` line, and no
  `.claude/settings.json` was written, so no `agent-cap.js` command.
- AC5 — `resolve_adopter_argv` — a python program run from `tools/govkit` imported `govkit`, read
  `read_descriptors`, and read each deploy with `load_deploy` from a scratch target. Over
  `%TEMP%/drb15a1`, with `[kit.agent-cap] prefix = "scripts"`, `resolve_adopter_argv` returned
  `['python', 'tools/settings-merge.py']` for both `agent-cap` and `settings-merge`. Over
  `%TEMP%/drb15a3`, with `[kit.settings-merge] prefix = "scripts"`, both returned
  `['python', 'scripts/settings-merge.py']`. From the `<p14>` clone the name was absent, and the
  inline resolution over `%TEMP%/drb15a1` returned `scripts/settings-merge.py` for agent-cap and
  `tools/settings-merge.py` for settings-merge.
- AC6 — `tools/hooks/kit.toml` — a stand-in, since the selfcheck leg is refused to this role. A
  scratch program reimplemented the ownership join over the real registry through
  `read_descriptors`, `planned_writes` and `target_context` at a bare target. With
  `tools/hooks/kit.toml` at `<p14>`'s bytes it read 29 of 29 entries, 105 offered elements (15
  `[adopt]`, 11 `[check]`, 67 `[[gate_leg]]`, 12 `[[regenerate]]`), 105 graded, and one hit:
  agent-cap's `[adopt]` naming `tools/settings-merge.py`, owned by `settings-merge`. With the
  descriptor at `<p15>`'s bytes, through `resolve_adopter_argv`, it read 105 offered, 105 graded and
  0 hits. The `python tools/govkit/govkit.py selfcheck` run, both halves, is owed to the close.
- AC7 — `govkit: cross-entry argv:` — seven scratch govs under `%TEMP%/drb15x`, shaped as
  `build_scratch_gov_kit` builds them with the `other` entry, each ran
  `<g>/tools/govkit/govkit.py selfcheck`. Each printed exactly one line opening
  `govkit: cross-entry argv:` and carrying `offered by`. The `argv` gov printed one line opening
  `govkit: entry 'demo': its [adopt] argv names 'tools/other.py'`, carrying `'other'`. The `via` gov
  printed no line opening `govkit: entry 'demo': its [adopt] argv` or
  `govkit: entry 'demo' declares [adopt] via`. The `nobody`, `norequire`, `noargv` and `beside` govs
  each printed one `via` line, carrying `names no registry entry`, `is not in its requires`,
  `declares no [adopt] argv of its own` and `sits beside an [adopt] argv` in turn. The `ungraded` gov
  printed a second line opening `govkit: cross-entry argv:` and carrying `none graded`. The same
  seven govs built around `<p14>`'s `govkit.py`, under `%TEMP%/drb15y`, printed no line opening
  `govkit: cross-entry argv:`.
- AC8 — `epoch: agent-cap · clean ·` — at `<p15a>`,
  `python tools/govkit/govkit.py epoch --base ebce889c7` printed
  `epoch: agent-cap · FAILED · last bump 671f25c711 precedes last move 0a178ed8f0`
  and no other non-clean entry. `python tools/govkit/govkit.py mint --base ebce889c7` printed one line
  carrying ` -> `, `mint: agent-cap · 1.39 -> 1.40`. At `<p15>` the epoch printed
  `epoch: agent-cap · clean · 1.40`, and `git grep -h "gov:kit agent-cap@" -- tools/hooks` printed
  three lines carrying `1.40`, the value of `KIT_AGENT_CAP_VERSION`.
- AC9 — `+def resolve_adopter_argv(` — `git diff <p14> <p15> -- tools/govkit/` filtered by
  `^[+-](def|class) ` printed that one line. `grep -c resolve_adopter_argv tools/govkit/govkit.py`
  printed 5, and `grep -n '_argv_g' tools/govkit/govkit.py` printed nothing. `tomllib` read
  `{'via': 'settings-merge'}` as `tools/hooks/kit.toml`'s `adopt` table.
  `python tools/codebase-map/gen_map.py --check` exited 0. `scan_text_io` counted 35 `subprocess`
  sites in `govkit.py`, and 24 `subprocess` and 1 `file-io` in `selftest.py`, exactly the rows
  `memory/project/encoding-posture-sites.txt` declares.
- AC10 — `memory/builds/dRedressedBar/build/` — this record, under that folder, carries
  `**Serves:** journal TOOL-dRedressedBar-15` and one line for each of AC1 to AC9 and AC11.
- AC11 — `_cfg_run = subprocess.run(` — a python program found one line opening that text in the
  worktree's `tools/govkit/govkit.py`, walked up the contiguous `#` lines and joined them. The cut
  carried no `before the receipt is written`, and it carried `ahead of CONFIGURE`,
  `RECEIPT rewrites`, `TOOL-dRedressedBar-14`, `TOOL-dRedressedBar-11 S3` and
  `TOOL-dRedressedBar-13`. The anchor line and the one after it were equal to the same two lines of
  `git show ffe73d97d:tools/govkit/govkit.py`. Over that file the cut sat at `:7811-7816`, carried
  `before the receipt is written`, and carried none of the other three.
