**Serves:** journal TOOL-dSafePassage-8

# TOOL-dSafePassage-8 — acceptance ledger

The unit as built, at spec rev-5. In `tools/govkit/govkit.py`: `test_source_target` holds where the
target resolves to the gov checkout; there `_cmd_update` no longer refuses and runs SOURCE mode. It
refuses `--kits`, `--rollback`, a receipt not in source mode and an unresolvable `--to`; read-only it
names the pending steps; with `--write` it takes `demand_writable_target` (no file row is claimed,
since source mode writes none), rewrites `.governance/install.json` whole as `{"schema", "mode":
"source", "gov_source": ".", "prefix", "kits", "files", "steps"}` through `write_atomic` only where
its bytes move, `files` one unhashed `{path, kit, role, source}` row per distinct destination
`planned_writes` derives with no unresolved token, `schema` and `steps` from
`derive_receipt_schema`; then `run_step_walk` over `derive_pending_steps` (deviation 166), then
`check_gov_first`, each miss an `r.fail`. `target_context` grades and enters an `[answers]` value
only where the entry's own descriptor names its `{token}`; `planned_writes` resolves, in source
mode, a destination naming an unanswered token to the row's source. In
`tools/govkit/upgrade_steps.py`: `check_gov_first`. In `tools/push-main.sh`: `run_gov_first`, called
in `cmd_prepare` after the mint and before the regeneration (the regeneration's untracked snapshot
now taken before it), and in the attended landing after the mint commit as its own `steps: gov first
onto <remote>/<branch> at <sha8>[ for <unit>]` commit with `Pass: none`.
`tools/run-gates/check-receipt.py`: `derive_source_rows`, a named `SKIP` for a source receipt's
unhashed rows, and two in-file fixture arms. `tools/memory-tree/check-verdict-epoch.sh`: the comment.
`refusal_join.py` `BRANCH_PIN` 320 -> 324.

HOW EACH CRITERION WAS OBSERVED. No gate, suite or bar ran in this pass, save the AC9 run below. Each
AC was observed on node d (Windows, Python 3.15.2) over scratch clones of this worktree under
`%TEMP%` carrying the working files, by the unit's own CLI and the lander.

SPEC NOTE, no departure in the code. §4's readers table says `tools/lib/render-doc.sh` reads a source
receipt's rendered rows as "gov's own rendered paths", and its closing sentence that each row answers
what the probe answers today. For that reader there is no probe: with no receipt it states a phrase.
Measured in the AC5 fixture, the prepared merge's regeneration re-rendered four lines of
`memory/guides/BUILD-METHOD.md` from "the unattended-run protocol of this repo" to
`memory/guides/UNATTENDED-PROTOCOL.md`, so the first landing after this build moves that rendered
text. The `files` rows leave out the plan's one `UNRES.` row, `.gitattributes:{playbook_path}`, which
the plan's legend calls "not a path".

Owed at the close: `govkit selftest` (with `check_source_mode`'s `[dSP-8]` rows), `push-main
self-test` (arms 34 and 35, and arm 25's gov-first skip line), `receipt sync` (check-receipt.py's two
new fixture arms), each with its RED-first observation; `govkit refusal join`, `govkit acceptance
matrix`, `govkit selfcheck`, `recall floor arms`, `verdict epoch`, `verdict-epoch self-test`, `kit
epoch`, `spec tokens`, `memory hygiene`.

**Evidences:** TOOL-dSafePassage-8
- AC1 — `python tools/govkit/govkit.py plan --target .` in this worktree exited 0 with `NOTHING was written`, and `git status --porcelain` named only this pass's own edits before and after; the base exited 2 on `answers.stream_ownership` (its `—`).
- AC2 — `govkit.py plan --target <scratch target>` with gov's deploy file: `memory_root = "x; touch PWNED"` exited 2 naming `answers.memory_root`, no `PWNED` file; `stream_ownership = "a; b"` exited 1 with output byte-identical to the run without the key (both name only the unanswered `playbook_path`).
- AC3 — `govkit.py update --target . --write` in a scratch clone with no receipt exited 0 and wrote a receipt with `"mode": "source"`, schema 4, no `gov_commit`; its `steps` ids equalled `read_steps` at HEAD both ways, each applied; its 337 `files` paths equalled the 337 destinations `plan --target .` lists, none carrying `sha256`, `oid` or `gov_oid`; `git status --porcelain` named no path under `.governance/outbox/`, the lock gone.
- AC4 — a planted row in the clone's `steps.toml`, committed, `up` exiting 0 and `witness` exiting 1: `update --target . --write` exited 1 with `step govkit/planted-witness-fails · failed · witness does not hold after up`, the three rows before it `applied`. Separately, a committed row applied on one run, its `witness` then committed as exit 1: the next run exited 1 with `gov first: govkit/planted-later-red: listed applied, and its witness does not hold on gov's tree`.
- AC5 — `bash tools/push-main.sh --prepare --slug fx` in a fixture (a clone, its bare remote, a run branch): exited 0, `push-main: prepared`, the merge's tree holding `.governance/install.json` with every declared id `applied`; with the plant on a branch it exited 1 naming `govkit/planted-witness-fails`, the branch at its old sha and checked out.
- AC6 — `run_gov_first` cut from `tools/push-main.sh`: no deployer beside the lander, with or without a python, printed `steps were NOT run on gov first` once, with its reason (no govkit deployer beside this lander), and returned 0; a deployer beside it with the resolver refusing returned 1.
- AC7 — `python tools/run-gates/check-receipt.py <scratch tree>` on AC3's receipt with `tools/memory-tree/gen_build_index.py` deleted printed `SKIP  337 unhashed row(s) of a source-mode receipt` and exited 0; with a `sha256` on that row it exited 1 with `MISSING   tools/memory-tree/gen_build_index.py`. `git grep -n 'gov has no receipt' -- tools/memory-tree/check-verdict-epoch.sh` prints nothing.
- AC8 — AC3's command run a second time printed `steps: 0 pending · 0 applied · 0 skipped`, exited 0, and `sha256sum -c` over the receipt read `OK`.
- AC9 — `bash tools/check-wiring.sh` and `bash tools/check-install-prefix.sh` in AC3's clone with its receipt and again with it removed: each exited 1 both times (the clone's own state) with byte-identical output. These are gate legs, run once before the role hook refused a later run of them; the main loop owes the observation through `check_source_mode`.
