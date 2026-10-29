**Serves:** journal TOOL-dSafePassage-84

# TOOL-dSafePassage-84 — acceptance ledger

The unit as built, at spec rev-3. Product writes: `tools/govkit/govkit.py` (S1 the nested
`derive_walk_hold`, S2 the preview's call, S3 the write run's call), `tools/govkit/selftest.py` (S4
the `[dSP-84 AC2]` and `[dSP-84 AC5]` checks, S5 the fixture table row and its `dSP-84` tag),
`tools/govkit/upgrade_steps.py` (S5 the `scoped-read-only` plant) and `help/upgrade-steps.md` (S6).

HOW EACH CRITERION WAS OBSERVED. No gate, suite or bar ran in this pass. Each AC was observed on node
a (Windows 11): the greps over this worktree's working copy, and §4's two probes and the `update`
fixture plants from the root of a `git clone --shared` of this branch's HEAD under `%TEMP%/p84c`, with
the unit's uncommitted diff applied and committed there, so the gov tree the probes read was clean.

Owed at the close: the RED-first observation of each of §7's three `New arm:` lines — the
`[dSP-84 AC2]` check (staged red by `govkit.py` at `460ffb587`), the `[dSP-84 AC5]` check (staged red
by the write site calling `derive_walk_hold(0)`) and the `scoped-read-only` plant's `dSP-84` row
(staged red by a preview arm `elif (_sw_hold := derive_walk_hold(0)) and not kits:`) — and the §7
legs at the bar.

**Evidences:** TOOL-dSafePassage-84
- AC1 — the spec's three `git grep`s — printed `govkit.py:10573` (the definition), `:10622` (the preview) and `:11734` (the write run); nothing for `elif kits`; and `1`.
- AC2 — `python <scratch>/preview_probe.py 2` — printed `0 True False True` and `govkit update — steps: not walked — the receipt is at schema 2, and its first step starts from 3: a clean \`update --write\` lifts it to 3, and the next one walks them · 3 pending`.
- AC3 — `python tools/govkit/upgrade_steps.py fixture update --plant scoped-read-only` — exit 0, `govkit update — steps: not walked — a --kits run walks no step, since a subset would run a later step before an earlier one · 2 pending`, `update: step canaries none`, no `would walk`, no `update: FAILED`.
- AC4 — `python <scratch>/preview_probe.py 3` — printed `0 True True False` and `govkit update — steps: 3 pending`; `fixture update --plant read-only` exit 0 with `would walk fx/s1` and `would walk fx/s2`. `--plant scoped` exit 0, its not-walked line unchanged.
- AC5 — `python <scratch>/findings_probe.py` — printed `1 4 []` and `govkit update — steps: not walked — this run already has 1 finding(s) · 3 pending`.
- AC6 — the spec's three `git grep`s — each printed one line, `help/upgrade-steps.md:229`, `:235` and `:236`, in the read-only bullet.
- AC7 — `git grep -n -F "[dSP-84 AC"` printed `selftest.py:4921` and `:4933`, both inside `check_receipt_schema`; `scoped-read-only` printed `upgrade_steps.py:3627`, `:4421`, `:4424` and `selftest.py:4525`, `:4545`.
