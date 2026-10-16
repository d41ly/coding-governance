# TOOL-dRedressedBar-14 — acceptance ledger

**Serves:** journal TOOL-dRedressedBar-14

This is the build pass of the first-apply-at-a-per-kit-prefix defect. It changed two product files.
`_cmd_apply` in `tools/govkit/govkit.py` now writes `.governance/install.json` between HOOKPROBE and
CONFIGURE. It writes one dict, `_rcpt_doc`, built from unit 12's carry, which is now bound there once.
The three keys later steps fill take the prior receipt's values, or the empty ones. One line follows
the write:
`govkit apply — receipt written ahead of CONFIGURE: <n> row(s), <k> kit(s); RECEIPT rewrites it`.
The RECEIPT step updates the same dict with `files` re-derived and this run's
`orders`, `after` and `gate_runner`, then writes it. `install.sums` and the `STEP_RECEIPT` counts
read that dict's lists. `tools/govkit/selftest.py` gains the `[dRB-14]` block after the `[dRB-12]`
block. The pass also wrote this ledger and spec 14's status cell. The spec-11 correction is the
spec-writer pass `<w14>`, `07c83c534`. `<p13>` is `8df39101b`, named by its `Pass:` trailer. Unit
16's build pass, `8139d0637`, sits between `<p13>` and this pass.

No merge bar, no self-test suite and no gate leg ran in this pass, and no slice of the suite ran
either. Every criterion was observed with a direct probe. Scratch programs drove
`python tools/govkit/govkit.py apply` over fresh `git init` targets under `%TEMP%/b14*`. Each target
had `core.autocrlf false` and `DEPLOY_FULL`'s answers, plus `[kit.agent-cap] prefix = "scripts"`
where a criterion adds it. The green half ran against the tip worktree. The red half ran against a
local clone at `%TEMP%/b14c`, checked out at `<p13>`. A second clone, `%TEMP%/b14s`, was checked out
at `07c83c534` and given the tip's engine with one staged break, and it served AC3 and AC4. The
`[dRB-14]` block itself was read statically: `ast` found six `check` calls whose label is a string
constant opening `[dRB-14]`, and one of them carries `kit 'agent-cap'`. Its settings comprehension,
copied verbatim, read true over the tip's target and false over `<p13>`'s. These probes stand in
for `govkit selftest` (AC1's readings), the encoding-posture leg (AC5) and `memory hygiene` (this
ledger). The section 7 gates are owed to the close, with the `New arm:` line's RED-first
observation of the `[dRB-14]` block over `<p13>`'s engine.

**Evidences:** TOOL-dRedressedBar-14
- AC1 — `scripts/hooks/agent-cap.js` — at the tip, the three-kit apply,
  `apply --kits agent-cap,settings-merge,kickoff-manifest`, over the per-kit-prefix target
  `%TEMP%/b14t` exited 1. Output line 12 was
  `govkit apply — receipt written ahead of CONFIGURE: 18 row(s), 3 kit(s); RECEIPT rewrites it`.
  Line 13, the first carrying `CONFIGURE `, was the one line opening
  `govkit apply — CONFIGURE settings-merge:`, and it ended `adopter exit 0`. The receipt held the
  row `scripts/hooks/agent-cap.js` with source `tools/hooks/agent-cap.js`. `.claude/settings.json`'s
  `PreToolUse` group with matcher `Workflow|Agent` held one command,
  `node "${CLAUDE_PROJECT_DIR}/scripts/hooks/agent-cap.js"`. No line opened
  `govkit: kit 'settings-merge'`. One line opened `govkit: kit 'agent-cap'`, and its stderr tail named
  `scripts\settings-merge.py`, which python could not open (§8 F1, unit 15). Over the `<p13>` clone,
  in `%TEMP%/b14r`, the run exited 1 and printed
  `CONFIGURE settings-merge: adopter exit 2 — no-agent-cap-to-wire [accepted stop]`
  and no ahead line. Its settings.json held no `Workflow|Agent`
  group, and `agent-cap.js` appears in it 0 times. The tip worktree before this pass's edit read the
  same at `%TEMP%/b14h`.
- AC2 — `cmp` — the default-prefix apply ran from the tip into `%TEMP%/b14d1` and from the `<p13>`
  clone into `%TEMP%/b14d2`. Both exited 0. Each printed two `CONFIGURE` lines, for settings-merge
  and agent-cap, ending `adopter exit 0`. `cmp` found the two `.claude/settings.json` files equal.
  With each output's `[3/LAND]` line dropped, `diff` printed one hunk, `10a11`, which adds the line
  `govkit apply — receipt written ahead of CONFIGURE: 18 row(s), 3 kit(s); RECEIPT rewrites it`.
- AC3 — `guard/agent-cap.js` — spec 11's AC3 fixture A was built as that criterion states, at
  `%TEMP%/b14fa`. At the tip, its second `apply --kits settings-merge` exited 1 and printed the ahead
  line. Exactly one line opened `govkit: kit 'settings-merge'`, and it carried `cannot read`. No line
  carried `no-agent-cap-to-wire`, and the CONFIGURE line read `adopter exit 2`. In the `%TEMP%/b14s`
  copy, the S1 write took `selection` and `rows` in place of the carried lists. Over that copy, in
  `%TEMP%/b14fs`, the same second apply exited 0 and printed
  `CONFIGURE settings-merge: adopter exit 2 — no-agent-cap-to-wire [accepted stop]`.
- AC4 — `drb14 staged fault` — the `%TEMP%/b14s` copy got the line
  `raise RuntimeError("drb14 staged fault")` after `inert = read_inert_kits(deploy)`. Its AC1 apply
  over the per-kit-prefix target
  `%TEMP%/b14f4` exited 1 on the uncaught RuntimeError. It left `.governance/install.json` claiming
  `kickoff-manifest`, `settings-merge` and `agent-cap`. All 13 of its `engine` rows carried an `oid`,
  and its `orders` was `[]`. Then the tip's unpatched apply ran over the same uncommitted target and
  exited 1, from agent-cap's argv. No line carried `already carries` or `DIRTY`, and exactly one line
  opened `govkit apply — CONFIGURE settings-merge:`, reading `adopter exit 0`. With the same patch
  over the `<p13>` clone, in `%TEMP%/b14f5`, the faulted apply exited 1 and left no receipt. The
  re-run exited 2 on a line opening
  `govkit: the target already carries agent-cap (at scripts/hooks/agent-cap.js), kickoff-manifest`.
  It ran from the patched
  clone, and that refusal fires at the foreign check, ahead of the patched line.
- AC5 — `scan_text_io` — `git diff 8df39101b -- tools/govkit/` over the worktree printed no `def`
  or `class` line. `grep -c '_rcpt_doc' tools/govkit/govkit.py` printed 9. The comment above the S1
  write carries `per-kit` and `RECEIPT`. `scan_text_io` from `tools/gate-lint/encoding_posture.py`
  counted 35 `subprocess` sites in `govkit.py`, and 24 `subprocess` and 1 `file-io` in `selftest.py`.
  Those are exactly the rows `memory/project/encoding-posture-sites.txt` declares.
- AC6 — `git diff <w14>~1 <w14> -- memory/builds/dRedressedBar/spec/` — for `07c83c534`, spec 11's
  header moved from `rev-5` to `rev-6`, CLOSED on both sides. One revision line was added, and it
  opens `- rev-6 · 2026-10-14 · §4 · a records fix for TOOL-dRedressedBar-14`. Spec 11's
  `## 4. Design` cut at `<w14>`, joined, names `TOOL-dRedressedBar-14` twice. Before this pass's
  commit, `git diff --cached --name-only` under `memory/builds/dRedressedBar/spec/` named spec 14
  alone. This ledger carries `**Serves:** journal TOOL-dRedressedBar-14`.
