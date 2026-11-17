# TOOL-dDeclaredLoop-2 — acceptance ledger

**Serves:** journal TOOL-dDeclaredLoop-2

No merge bar, no self-test suite and no gate leg ran in this pass, and `guard.py --selftest`, the new
leg's command, was not run as a command. The criteria were observed on node `d` (win32) by probes of
the unit's own code: each of the sixteen plants of `guard.py --fixture --plant <case>` run one at a
time by direct CLI, every scenario printing `held`; `policy_edit.py` run by a scratch probe in a
repository planted as the guard's fixture plants its own; `floor.py get`; the instruction command's
AC13 call over this tree; a payload fed to `scratch-guard.js`; a scratch probe driving a real push
through a copy of `.githooks/pre-push` and a real commit through a copy of `.githooks/pre-commit`,
each over stand-in loop kit files; the `sed` and `cmp` cut AC10 spells; the instruction command's
`flow-only`, `proof-values`, `record`, `rerender`, `owner-propose`, `command-for-all` and `guard`
plants; and the naming lexicon's `--check`, which ran and passed with the verb offender count
unchanged.

Timing, for the budget row: the sixteen plants run one after another took 60 s PINNED 2026-11-15 by
direct CLI.

A finding the build met and did not change, since the proof is the owner's settlement of
dOrderedCharter-15 §8 F4 and AC10 holds the block to it: on Windows, standard error redirected to
`NUL` reads as a terminal, `sys.stderr.isatty()` answering true, so `check_terminal_proof` holds for a
command run as `2>/dev/null`; a file or a pipe reads false. The pre-commit hook's `[ -t 2 ]` still
judges the commit, so a policy write made that way is refused at the commit off a live run's branch.

Owed to the close: every leg the spec's section 7 names, with the `pre-push run-log line` leg owing
one exempt row for the push arm's new exit site, deviation 24's gap; the RED-first observation of each
`New arm:` line: `loop guard fixtures` with `raise-admitted` red under a verdict forced to refuse; the
`guarded_write_py` parity row with one copy edited; the scratch-guard rows with `checkPolicyFile`'s
call taken out; the pre-commit row with the block's verdict put back to the minimal guard; the
pre-push rows with the push arm's call and the floor read taken out; and the budget row read against
the leg's own timing.

The close's RED-first observation, made by the main loop on 2026-11-17 at `c7cbca292` in scratch
worktrees outside the repository: each staged break applied, the arm run, the break restored and the
arm run again, the green half also read off every loop leg run whole at that commit.
`python tools/loop/guard.py --fixture --plant raise-admitted` with the verdict forced to refuse exited 3, and
0 once restored: RED observed.
Not observed: the arm in `tools/hooks/scratch-guard.test.sh`, a suite arm, left unrun for the owner's opt-in
slow-suite run.
Not observed: the arm in `tools/lib/resolve-python.test.sh`, a suite arm, left unrun for the owner's opt-in
slow-suite run.
Not observed: the arm in `.githooks/pre-commit.test.sh`, a suite arm, left unrun for the owner's opt-in
slow-suite run.
Not observed: the arm in `.githooks/pre-push.test.sh`, a suite arm, left unrun for the owner's opt-in
slow-suite run.

**Evidences:** TOOL-dDeclaredLoop-2
- AC1 — `raise-admitted` — `python guard.py --fixture --plant raise-admitted` printed `policy-edit: wrote .governance/policy.toml`, the change record, `Gov-Policy: policy.budgets."AGENTS.md" 100 -> 120`, then `policy-guard: admitted` and `loop-guard: admitted · policy-file.guard = owner-only · the minimal guard admits it`; exit 0, both scenarios held.
- AC2 — `raise-no-record` — exit 1, `loop-guard: refused · .governance/policy.toml · budgets."AGENTS.md" changed, and no staged change record names policy.budgets`, while the minimal guard admitted the shape.
- AC3 — `raise-lowered` — exit 1, the minimal guard's `policy-guard: refused · .governance/policy.toml · budgets."AGENTS.md" is a lowering: 100 -> 90` passed through.
- AC4 — `floor-off-agent` — exit 1 under `owner-only`, `agents-with-reason` and `agents-within-mandate`, each printing `floor.no-actor-witness: the guard's own switch, refused under floor.guard-self`; `floor-off-run` printed `loop-guard: admitted · guard-self · the guarded paths list, floor.no-actor-witness · the run-branch of memory/builds/tRun/RUN.md` and exited 0 with both records staged, then exited 1 naming `kit.policy` and `policy.floor` without them.
- AC5 — `other-write-owner-only` — exit 1, `policy-file.guard = owner-only admits an agent's write only as one cap raised`.
- AC6 — `with-reason-admitted` — exit 0 with the decision row; `with-reason-no-row` exit 1 naming `policy-file.guard = agents-with-reason`.
- AC7 — `mandate-live` — exit 0; `mandate-none` exit 1; `owner-only-live` exit 0, each over a run-state record and driver planted as the policy kit's `guard-run-live` case plants them.
- AC8 — `set review.max-rounds 4` — in a scratch repository on `main`, which no run names, with standard error a file: the proposal printed, `not proven · ... nothing written`, exit 1, the tree unchanged; `set-run-live` printed `Proof: none — run mandate memory/builds/tRun/RUN.md` for `review.max-rounds` and for `floor.guard-self`, exit 0 twice.
- AC9 — `raise AGENTS.md 120` — wrote the RAISED comment, the record and one `Gov-Policy:` line in `raise-admitted`; with `AGENTS.md` planted at 90 bytes PINNED 2026-11-15 it printed `condition 1 · AGENTS.md measures 90 bytes, CR-stripped, not above its cap 100`, exit 2, the tree unchanged.
- AC10 — `guarded_write_py` — the three blocks cut with the spec's `sed` compared equal by `cmp`; in the canonical's block `grep -c 'sys.stderr.isatty()'` printed 1 and `grep -c 'stdin'` printed 0; a `python -c` probe saw `write_guarded` put back a prior file's bytes and remove a new one when its record raised, and admit a callable writer.
- AC11 — `push-no-trailer` — exit 1, `loop-guard: push · refused · commit <sha8> · .governance/policy.toml · review.max-rounds changed with no Gov-Policy: ... trailer`; over this branch's own range from `origin/main` the arm read every commit and found none changing the file, exit 0.
- AC12 — `proof-signed-refuse` — exit 2 naming `point.instruction.signed-proof`; `proof-signed-fallback` printed `loop-guard: fallback · ... read as the catalogue default tty-cli`; `python floor.py get guard-self` printed `on` in this repository, whose policy file holds no `[floor]` table, and `get bogus` exited 2.
- AC13 — `point.instruction.guard` — `grep -n` printed the `layer.flow` row's `declares` line; the `add --manifest overlay --tag repo.probe` call with standard error a file exited 1 printing `instructions-edit: not proven`, the tree unchanged.
- AC14 — `policy_edit.py` — a PreToolUse Write payload for `.governance/policy.toml` fed to `node tools/hooks/scratch-guard.js` printed the deny naming `policy_edit.py`, exit 2; the same payload for `.governance/deploy.toml` exited 0.
- AC15 — `lg_kit` — `grep -n 'lg_kit' .githooks/pre-commit` prints `lg_kit=loop` and `lg=$(resolve_kit_gate "$lg_kit" guard.py)` ahead of the minimal guard's; a scratch commit through a copy of the hook ran the stand-in loop guard, `LOOP VERDICT RAN`, and not the policy stand-in, and with the loop stand-in removed ran the policy one.
- AC16 — `policy_edit.py` — `help/policy.md` names it under "Who may change the policy file", with its three verbs' usage anchors, the push check and the floor table.
- AC17 — `floor-readers` — `check_site_witnesses()` refused `fx-floor-witness` and `check_transition_channels` found the move owing a record under the floor all on; once the landed revision set both members off, the site line carried `floor: no-actor-witness off · reported`, the check printed `floor: record-changes off`, and both passed; four scenarios held.
- AC18 — `loop guard fixtures` — `python -m json.tool tools/gate-legs.json` parses and the row carries `"enforces": ["principle.p10"]`; the `principle.p10` row left `tools/playbook/core-pending.txt`. `core.py meta-check` is a gate leg's command and is owed to the close.
- AC19 — `policy-unrecorded` — a scratch push through a copy of `.githooks/pre-push` with a stand-in loop guard exiting 1 was refused with that token; over a STUB bar exiting 1 a stand-in `floor.py` printing `off` let the push through printing `floor: verdict-before-move off` and `no gate-bar-green written`, none written; printing `on` refused as `gate-red`.
