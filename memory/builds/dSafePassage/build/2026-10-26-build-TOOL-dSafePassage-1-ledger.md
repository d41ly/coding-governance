**Serves:** journal TOOL-dSafePassage-1

# TOOL-dSafePassage-1 — acceptance ledger

The unit as built: the step reader `tools/govkit/upgrade_steps.py` (`read_steps`, `read_retired`,
`derive_introduced`, `resolve_claim`, `check_frozen`, `write_before_image`, `write_from_before_image`,
`render_policy_text`, `cmd_list`, `cmd_frozen`, `main`, `StepRow`, `RetiredRow`), the empty
`tools/govkit/steps.toml`, the step program `tools/govkit/steps/fanout_cap.py` and its `[[upgrade]]`
row in `tools/hooks/kit.toml`, `derive_push_base` extracted from `cmd_epoch`, `Refusal` moved into the
reader and bound back in `govkit.py`, `update` and `check` reading succession through `resolve_claim`,
the leg `step-rows-frozen` with its `[[exempt_leg]]` row and subject pin, the help page, and the
selftest arms `check_upgrade_steps`, `check_succession` and `check_fanout_step`.

HOW EACH CRITERION WAS OBSERVED. No gate, suite or bar ran in this pass. AC1, AC17 and AC18 were read
off gov's own tree. AC2 to AC12 and AC16 were observed by the three new arm BODIES, executed outside
the suite by a scratch stand-in for the suite's `check`, `git`, `settle` and `make_target` helpers,
over scratch govs and targets under the node's temp directory; every line printed `ok`. Those arms'
RED-first observation and the `govkit selftest` leg itself are the close's (the spec's `New arm:`
line). The step's own probe ran its three argvs under `-I`, as the runner will.

**Evidences:** TOOL-dSafePassage-1
- AC1 — `python tools/govkit/upgrade_steps.py list` — on gov's tree it printed `upgrade-steps: 1 · agent-cap/fanout-cap-to-agents-in-flight · unlanded · tools/hooks/kit.toml` (landed ref `origin/main`); over a scratch gov whose one commit adds a `tools/govkit/steps.toml` row and a descriptor row, `check_upgrade_steps` printed `ok` for the steps-file row listed first, both at that commit.
- AC2 — `upgrade_steps.py list` — `check_upgrade_steps` planted, one per run, an unknown key, an authored `introduced`, a `{bogus}` placeholder, `argv[0]` of `node`, an untracked `{gov}/` program, a duplicate id, another entry's `<entry>` in a descriptor, a registry entry's `<entry>` in `tools/govkit/steps.toml`, a `surfaces` item with no colon and a `[[retired]]` successor that is not live: each exited 2 naming its file, `[[upgrade]]` or `[[retired]]` row number and key, and the well-formed control listed at exit 0.
- AC3 — `upgrade_steps.py list` — on a scratch gov whose branch added a second row and merged `main` into itself, the landed row read `main`'s commit X and the branch row `unlanded`; after `main` merged the branch at M the second row read M, not its branch commit (`ok` both).
- AC4 — `upgrade_steps.py frozen --base <main sha>` — on branch commits off `main`: an edited landed `down` argv exited 1 naming `demo/first` and the field `down`, a removed landed row exited 1 printing `the landed [[upgrade]] row is gone`, one edited byte of the landed `{gov}/` program exited 1 naming `tools/govkit/steps/s1.py`, and the removal with a `[[retired]]` row naming the id and its successor exited 0 printing `1 landed row(s)`.
- AC5 — `upgrade_steps.py frozen --base <main sha>` — a correction under a new id beside the unchanged landed row exited 0 printing `0 problem(s)`; over a base holding no rows it exited 0 printing `0 landed row(s)`; on gov's own tree the leg's argv printed `step-rows-frozen: 0 landed row(s) at 60d90cb7 · 0 problem(s)`.
- AC6 — `govkit.py update --target <t>` — on a scratch gov that installed `old` at A and retired it to `new` at B, the run printed `govkit update — retired old: claimed by its successor new`, no `no longer a registry entry`, exit 0; with `--write` the receipt's `kits` read `["new"]` and every sourced row's kit `new`.
- AC7 — `govkit.py update --target <t> --write` — with the successor `none`, each of `old`'s rows printed `withdrawn          [engine       ] <path>` with an `update-withdrawn-*` order under `.governance/outbox/`, every file still on disk, exit 0.
- AC8 — `govkit.py update --target <t>` — a receipt claiming `ghost`, neither live nor `[[retired]]`, exited 2 printing `claims kit 'ghost', which is no longer a registry entry`, the receipt's bytes unchanged.
- AC9 — `govkit.py check --target <t>` — on AC6's receipt it printed `old: retired, successor new` and no `claims kit 'old'`; on AC8's it exited 1 printing `the receipt claims kit 'ghost', which is not a registry entry`.
- AC10 — `python policy.py get runtime.agents-in-flight --rev <sha>` — over a scratch target with the scaffold policy file and a committed `.agent-cap.conf` of `FANOUT_CAP=2`, the up exited 0, the limit read 2 at the commits before and after, the file was gone, the policy file held `agents-in-flight = 2`, and the `witness` exited 1 before and 0 after.
- AC11 — `fanout_cap.py down` — after an up over a BOM-led CRLF `.agent-cap.conf`, `.agent-cap.conf` and `.governance/policy.toml` were byte-identical to the before state and `.governance/steps/agent-cap/` was gone; after an up killed once its before-image was written it exited 0 leaving the before state; over a policy file edited after the up it exited 1 naming `.governance/policy.toml` and changed nothing.
- AC12 — `fanout_cap.py up` — a conf holding `FANOUT_CAP=abc`, and one adding `OTHER=1`, each exited 1 naming `.agent-cap.conf` with the target's files, before-image included, unchanged.
- AC16 — `python tools/govkit/upgrade_steps.py list --window` — on gov's tree before the landing it printed `window: .agent-cap.conf · open`; on a scratch gov a home only an unlanded step's `surfaces` names printed `open` while the landed step's printed `closed by demo/first`, and after `main` merged it, `closed by lib/second`. The gov-tree half, `.agent-cap.conf` closed by its step once this unit is on `main`, is observable only after the landing.
- AC17 — `tools/gate-legs.json` — read with `json`: the row `step-rows-frozen` carries `["python", "{prefix}/govkit/upgrade_steps.py", "frozen"]`; `tools/govkit/registry.toml` read with `tomllib` carries the `[[exempt_leg]]` row named `step-rows-frozen`. `govkit selfcheck` itself is the close's.
- AC18 — `help/README.md` — `grep` found its link to `help/upgrade-steps.md`, and that page names `[[upgrade]]`, `[[retired]]` and `runtime.agents-in-flight`.

The `New arm:` lines of this unit were observed at the close, each RED on its staged break and GREEN restored; a line counts observed when its break reds at least one of its arms. Observed by a researcher in scratch clones of `83817478f` (batch b, `2026-10-28-prompt-TOOL-dSafePassage-1-close-arms-b-researcher.md`), each break staged alone and restored: `check_upgrade_steps`, whole function. Break: the unknown-key refusal in `read_steps` disabled (`if False and k not in STEP_KEYS:`). RED: `FAIL [dSP-1 AC2] an unknown key exits 2 naming its file, row and key — rc=0 upgrade-steps: 1 step row(s) · 0 retired row(s) · landed ref main`. GREEN restored: FAILURES=0, 57 ok.
