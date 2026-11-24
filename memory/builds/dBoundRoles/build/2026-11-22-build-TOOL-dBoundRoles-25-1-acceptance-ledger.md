**Serves:** journal TOOL-dBoundRoles-25

# TOOL-dBoundRoles-25 — acceptance ledger

Each criterion of section 6, read by the pass that built the unit with a probe of the code it changed, on the worktree
before the pass commit at base `43808717e`: the pack `tools/roles/spawn-guard.js` and the step program
`tools/govkit/steps/spawn_guard_pack.py` run by their own CLIs over gov's tree and over scratch targets under the host
temp folder; `tools/settings-merge.py` run with no `--fragment` in scratch targets with and without the roles kit; the
review kit's `check-verifier-fanout.js` and `check-review-join.js` run over the shipped harnesses with the retired hook
deleted; `leg_factory.py --write`, `--list` and `--check`; and the charter render. No gate, suite or bar ran in the pass,
and a worktree-isolated agent may run no git command outside its worktree, so no fixture repository was built: each
`New arm:` arm section 7 declares, its RED-first observation on its staged break, and the legs section 7 lists are owed to
the main loop at the close.

## S1 — the inventory at the build run's base

Read from `tools/hooks/agent-cap.js@8eab6c4f` before anything moved, by its `RULE` comments, the body of
`tools/hooks/agent-cap.js#main` and its `module.exports`, with the main loop's decision
`2026-11-23-build-TOOL-dBoundRoles-25-2-main-loop-decision` placing the exports section 4 missed:

| What the file ran or exported | Its home after this pass |
|---|---|
| the `--only=` refusal, then rule 6 (`checkHandoffSpawn`, `checkHarnessCall`, `resolveHarnessEntry`), rule 8 (`checkEffortLevel`, `resolveModelProfile`, `readSessionModel`), rule 7 (`checkSettingsInForce`, `readSettingsLayers`), then `checkOptinPackPresent`, in that order | `tools/roles/spawn-guard.js#main`, in the same order |
| `TYPED_INPUTS`, `resolvePromptsAuthor` (decision 4) | `tools/roles/spawn-guard.js`, exported with `resolveModelProfile` and `checkEffortLevel` |
| `MAX_VERIFIERS`, `renderCodeView`, `renderStrippedView`, `renderBlankedLiterals`, `runBothViews`, `resolveHarnessName`, `readWriterBound` | `tools/workflows/script-views.js`, required by both review gates from beside them |
| `extractWorkflowArgs`, `extractBuildSlug`, `extractHandoffMarker` with `HANDOFF_MARK_RE`, `resolvePolicyHelper`, `resolveKitDir` | `tools/hooks/scratch-guard.js#module.exports` |
| `KIT_AGENT_CAP_VERSION` | `tools/hooks/scratch-guard.js`, at `1.52` |

No rule or export the table above leaves unplaced, and none of rules 0 to 5 is in the file, so section 8's F6 stop does
not hold. Its importers, by `git grep -n -F 'agent-cap.js' -- tools skills` at the base, are the S8 readers each disposed
in this commit.

## The harnesses that differ from their landed blob (section 4, Rollout)

`git diff --name-only a315474f` over the index's `harnesses`, the landed revision this pass read through the policy kit,
prints `tools/workflows/tier2-review.js`, `tools/workflows/unattended-build.js` and `tools/workflows/unattended-unit.js`
(DERIVED at `43808717e`): once this commit is wired every `Workflow` call to each is refused until it lands, and the main
loop runs each at its landed bytes, `git show <L>:<rel>` over the working-tree file and `git checkout -- <rel>` after.

**Evidences:** TOOL-dBoundRoles-25
- AC1 — `BLOCKED by spawn-guard:` — an `Agent` payload whose prompt carried no marker, its cwd gov's worktree with its role index, made `node tools/roles/spawn-guard.js` exit 2, stderr opening `BLOCKED by spawn-guard: rule 6`. OWED: the admitted rendered handoff, the rows of `tools/roles/spawn-guard.test.sh` that carry it, at the close.
- AC2 — `role-sha` — `tools/roles/spawn-guard.js#checkHandoffSpawn` holds the compare unchanged from the retired hook, moved by the transform that rewrote only the scratch-guard requires and the prefix. OWED: the suite's `rule6 BR6 AC4` rows at the close.
- AC3 — `shapes` — no shape check exists in rule 6 at the base: `tools/roles/spawn-guard.js#checkHarnessCall` reads each `args.roles` value as an agent-true role and no index `shapes`, which TOOL-dBoundRoles-43 S2 records (no unit builds a shape refusal). Not observable; handed to TOOL-dBoundRoles-43.
- AC4 — `sha8` — over gov's worktree, `checkHarnessLanded` refused `tools/workflows/unattended-unit.js`, edited and committed on this branch and not landed, naming the path and `a315474f`, and admitted `tools/workflows/drift-audit-code.js` and `tools/workflows/orient-counterfactual.js`, each at its landed blob. OWED: the suite's `BR25 AC4` rows over a fixture with a bare remote, RED first against an admission comparing with HEAD, at the close.
- AC5 — `is not landed` — `checkHarnessLanded` over `tools/roles/spawn-guard.js`, present in the working tree and absent at the landed revision, answered `harness tools/roles/spawn-guard.js is not landed at a315474f`. OWED: the suite's `BR25 AC5` row at the close.
- AC6 — `tier2-review.js` — OWED: the suite's `BR25 AC6` rows, an adopter at prefix `scripts` and its CRLF checkout, at the close; the probe above read gov's own checkout, which `core.autocrlf` sets, and admitted the harnesses at their landed blobs.
- AC7 — `CLAUDE_CODE_MAX_CONCURRENT_SUBAGENTS` — rule 7 moved with its deny text; over gov's worktree a `Workflow` call from a folder in no checkout was refused by rule 7 under the pack's prefix. OWED: the suite's `rule7 BR25 AC7` rows naming the file and both numbers at the close.
- AC8 — `spawn-guard.js` — the retired suite's arms over moved rules are carried into `tools/roles/spawn-guard.test.sh`, each retargeted at a copy of the pack beside a copy of scratch-guard.js, its admitted harness calls run through a copy beside a policy kit with every declared harness committed on the fixture's landed branch; its arms over the retired hook's own copies and its frozen-views byte arm did not move, the latter carried into the review kit's suite. OWED: the suite's run at the close, which this pass could not run.
- AC9 — `extractWorkflowArgs` — `node -e` printed `function` for `extractWorkflowArgs`, `extractBuildSlug` of `tools/hooks/scratch-guard.js` and for `runBothViews`, `renderCodeView`, `renderStrippedView`, `renderBlankedLiterals` of `tools/workflows/script-views.js`; with `tools/hooks/agent-cap.js` deleted, `check-verifier-fanout.js --hook tools/hooks/scratch-guard.js` and `check-review-join.js` each exited 0 over the shipped harnesses. The S1 table names each row's home.
- AC10 — `UNWIRED` — `python -c` over gov's `.claude/settings.json` reads the `Workflow|Agent` group's command naming `tools/roles/spawn-guard.js` and none naming `agent-cap.js`, written by the step's up on gov's tree. OWED: `tools/check-wiring.sh` printing the pack wired and its new arm's `UNWIRED` row in `tools/check-wiring.test.sh`, at the close.
- AC11 — `spawn-guard.fragment.json` — `python scripts/settings-merge.py` with no `--fragment` in a scratch target holding the roles kit's fragment and pack at `scripts/roles/` wired `node "${CLAUDE_PROJECT_DIR}/scripts/roles/spawn-guard.js"` and exited 0; in a target holding no roles kit it exited 2 naming the fragment and each place it looked, writing nothing. OWED: the govkit selftest's `spawn-step-AC11` rows at the close.
- AC12 — `witness` — over a scratch target wiring the retired hook beside a foreign command, the witness exited 1, the up exited 0 leaving `spawn-guard.js` wired, the foreign command kept and no `agent-cap.js` command, and the witness then exited 0. A killed up, staged as the before bytes with the pack's wire call alone applied and the image kept, left both commands wired and the witness at 1; a re-run converged byte for byte on the image's after-state. OWED: the govkit selftest's `spawn-step-AC12` rows, RED first against an up that unwires before it wires, at the close.
- AC13 — `cmp` — the down after that up left `.claude/settings.json` identical to the before bytes under `cmp`; an edit after a second up made the down exit 1 naming the file, the edit kept. OWED: the govkit selftest's `spawn-step-AC13` rows at the close.
- AC14 — `KIT_AGENT_CAP_VERSION = ` — AMENDED by `TOOL-dBoundRoles-58`, its text restated in `memory/builds/dBoundRoles/build/2026-11-24-build-TOOL-dBoundRoles-58-deviation-583.md`, `TOOL-dBoundRoles-42` S4 the population and `TOOL-dBoundRoles-44` S1 the memory half: `git ls-files` over both retired files prints nothing; `git grep -l -F 'agent-cap.js' -- ':!memory' ':!.governance/steps'` prints `tools/govkit/fixtures/adopter-ic-2cff5855.receipt.json`, `tools/govkit/steps/spawn_guard_pack.py` and `tools/hooks/kit.toml` (DERIVED on the staged tree); the govkit selftest's step cases spell the old file from parts, so it prints no line there; and `grep -c 'KIT_AGENT_CAP_VERSION = '` over `tools/hooks/scratch-guard.js` prints 1. Under `memory/` the grep prints only the append-only records and ledgers unit 42 classes.
- AC15 — `agent-cap hook` — after `adopt-playbook.sh --target .`, `grep -c 'agent-cap hook' AGENTS.md` prints 0, and the `kit:roles` block of the charter template holds the spawn-guard line.
- AC16 — `step_gate.py` — OWED: the step gate over the pass's parent at the close; the row's `surfaces` name the retired file as `installable:` and `file:`.
- AC17 — `landed` — `grep -n 'landed' help/roles.md` prints the bullet under "What the hooks refuse" naming a harness not at its landed blob, beside its usage anchor `hook:spawn-guard`.
- AC18 — `spawn-guard self-test` — `leg_factory.py --list` printed `spawn-guard self-test` declared in `tools/govkit/registry.toml` and no `agent-cap self-test`; `--check` exited 0, and the rendered row of `tools/gate-legs.json` carries `enforces = ["practice.gate"]`.

## Amended by TOOL-dBoundRoles-44

- S1 of TOOL-dBoundRoles-44, amended — the `memory/` half of the reader grep above, `git grep -l -F 'agent-cap.js' 8b8b1374c -- memory ':!memory/builds' ':!memory/ledger'` at the build run's base, prints only files a class of `TOOL-dBoundRoles-42`'s table takes, its population `TOOL-dBoundRoles-42` S4. Each is listed with its class in `memory/builds/dBoundRoles/build/2026-11-22-build-TOOL-dBoundRoles-44-2-acceptance-ledger.md`, and none stands outside a class.
- S9 of TOOL-dBoundRoles-44, amended — the close's swap check: a harness this build edited runs at its landed bytes only under the build README's trap-guarded swap, and the exit of `git diff --quiet -- <rel>` after the restore is recorded here, one line per swapped harness, at the close under a `Pass: none` commit, where the swap happens (`TOOL-dBoundRoles-51` S2). At TOOL-dBoundRoles-44's pass commit no harness has been swapped: this session's spawn hook runs from the primary tree, which holds no spawn guard of this run.
