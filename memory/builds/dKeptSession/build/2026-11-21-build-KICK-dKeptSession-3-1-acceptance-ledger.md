# KICK-dKeptSession-3 — acceptance ledger

**Serves:** journal KICK-dKeptSession-3

No merge bar, no self-test suite, no gate leg, no `check_policy.py --fixture` case, no
`render_playbook.py --selftest` and no `instruction_units.py fixture` ran in this pass. The criteria
were observed on win32 at the pass's base `bcea1d47` by probes of the unit's own code: `policy.py
preset --diff` run as a command in scratch repositories under `%TEMP%`, each a one-commit repository
on `main` with no remote holding the policy text the criterion names, plus one holding no commit;
and an in-process probe script over `render_playbook.write_render_target`, `render`, `main`,
`instruction_units.run_map` and `render_instruction_map` that builds the targets the new arms build,
outside the selftest and the fixture. Each new name, `cmd_preset`, `render_preset_diff` and its nested
`render_value`, `read_preset_diff`, `derive_preset_section`, `check_preset_arms`, `run_preset_diff`
and `derive_preset_overrides`, was passed by `lexicon.py --suggest --as py.function`, and
`python tools/lexicon/lexicon.py` exited 0.

Owed to the close: every leg the spec's section 7 names, the `policy fixtures` run of the new
`preset-diff` case, the `playbook render selftest` run of `check_map_arms` and the new
`check_preset_arms`, and the `instruction units selftest` run of the `map-held` plant among them; the
two ceilings section 7 names, read against their rows of `selftest-budgets.txt`; and the RED-first
observation of each `New arm:` line: `preset-diff` on its two staged breaks, `check_map_arms` and
`check_preset_arms` on theirs, and `map-held` on its own, each green once restored.

**Evidences:** KICK-dKeptSession-3
- AC1 — `preset --diff --rev HEAD` over `preset = "strict"` with `[hooks]` `bypass = "allowed"`:
  exit 0, `- preset — strict` then the one line ``- `hooks.bypass` — allowed (strict: refused)``.
  Over `preset = "ours"` declaring `[presets.ours]` `extends = "strict"` and
  `"leases.expiry-hours" = 12`: exit 0, `- preset — ours` then `- no key differs`.
- AC2 — `--line` over the strict file: one line, `preset — strict · 1 key(s) differ: policy.py
  preset --diff`, 61 bytes (DERIVED, that run). Over a file naming `strict` with 13 keys moved off
  it (PINNED, `PRESET_DIFF_LINES` plus one), `derive_preset_overrides`' plant, `--section` printed
  the preset line, 12 key lines (PINNED, `PRESET_DIFF_LINES`) and `` - … (+1) — `policy.py preset
  --diff` ``; the default form printed all 13 (DERIVED, that run).
- AC3 — `render` over the fixture target selecting `["roles", "policy"]`, its engine's registry
  holding `policy` and its descriptor the `PRESET_SECTION` row, the template carrying S5's block and
  the policy file AC1's strict override: the body carried `## Policy preset — the posture and its
  exceptions` over the one-line region holding AC1's two lines, the `kit:policy` fence kept and its
  markers stripped as every kept fence's are.
- AC4 — `main --target <dir>` wrote the charter, exit 0; `leases.expiry-hours = 12` committed on
  `main`; `--check` exited 1 with `render-playbook: DRIFT — the charter region differs from a fresh
  render`; a second write exited 0 and `--check` 0, the charter listing
  ``- `leases.expiry-hours` — 12 (strict: 24)`` beside the `hooks.bypass` line.
- AC5 — `run_map` over the two-row registry target with no policy file: exit 0, its line before
  `[/AGENTS.md]` `preset — standard (the default) · 0 key(s) differ: policy.py preset --diff`, equal
  to the stdout of `policy.py preset --diff --line` run in that target, and the rendered charter held
  the same line as a `- ` item. `grep -rn "PRESET_LINE_PENDING\|presets join the policy reader"`
  over `tools/playbook/`, `AGENTS.md` and `help/` printed nothing, exit 1. Gov's own re-rendered
  `AGENTS.md` reads `preset — standard (the default) · 1 key(s) differ: policy.py preset --diff`,
  its one key `memory.staged-render`, which gov's policy file sets `on` (DERIVED, gov's file at
  `bcea1d47`).
- AC6 — `render_instruction_map` over the `map-held` plant's tree, a repository holding no commit:
  the last line was `preset — ` and `PRESET_LINE_UNREAD`, and stderr carried one line,
  opening `instruction-map: preset — unread · policy: refused ·`, naming the policy file at line zero and
  saying `refs/heads/main` names no commit in this repository.
- AC7 — `grep -n "preset --diff" policy.md charter.md` in `help/` printed `policy.md`'s bullet
  naming the charter's preset section beside the `script:tools/policy/policy.py#preset` anchor, and
  `charter.md`'s two lines of the map paragraph.
- AC8 — `MAP_PRESET_SECONDS` set to 0.001 in process (PINNED, the criterion's figure), `run_map`
  over the AC5 target: exit 0, its preset line the unread one, stderr `instruction-map: preset —
  unread · policy.py preset --diff did not answer within 0.001s`.
- The over-cap map case of `check_map_arms` still refuses with the shorter preset line: `instruction-map:
  2288 over MAP_CAP_BYTES` (DERIVED, that run). One `preset --diff` over gov's tree took 0.27 s
  (DERIVED, that run), under `MAP_PRESET_SECONDS`.
