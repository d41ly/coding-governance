# coding-governance — working guide

Project-agnostic governance + tooling for running Claude Code (or any agent) across several
machines/sessions on one repo. This repo **dogfoods its own kits**: it runs the memory-tree hygiene
gate, the kickoff-manifest ratchet, the template size gate, and the codebase-map coverage gate on
itself. The map lives at `memory/map/`; its first dossier is `memory/map/features/codebase-map.md`
and the other 69 inventory keys are still in the shrink-only `baseline.toml`.

*(Read by every AI tool: `AGENTS.md` is canonical; `CLAUDE.md` is a `@AGENTS.md` import — Claude Code
doesn't read AGENTS.md natively. Wired by `tools/agent-instructions/`.)*

## What ships here (the product)

- **`parallel-coding-governance.template.md`** — the governance playbook template (the operating
  ruleset; **≤32 KiB, strictly gated** by `tools/check-template-size.sh` — trim or externalize, never
  raise the limit). Companions: `.customize.md` (deploy-time placeholder catalog) and `.domain-rules.md`
  (the §4/§9/§10/§11/§12/§13 activity-scoped checklists the template references by §-stub).
- **`skills/session-kickoff/`** — the `/session-kickoff` engine + `MANIFEST-TEMPLATE.md` + the
  ratchet gate `manifest-check.sh` (+ its test). Installed per-machine via a junction (not in-repo).
- **`tools/`** — `lib/resolve-python.sh` (the one python-launcher resolver: it RUNS the candidate,
  because the MS-Store `python3` stub answers `command -v` and exits 9009) plus the copy-in kits:
  `memory-tree/`, `memory-recall/` (offline conf-driven retrieval
  over the memory tree + the rendered recall Skill and its opt-in `recall-opened` hook),
  `codebase-map/`, `drift-audit/` (does this repo's own RECORD of its state still match reality —
  five signals, stdlib+git, seconds, no agents; every signal carries a liveness assertion so a probe
  that cannot move prints DEAD PROBE instead of a reassuring 0), `hooks/agent-cap.js` (the fan-out guard: raw-primitive ban + the ≤5-verifier arity rule),
  `workflows/tier2-review.js`, `workflows/drift-audit-{code,state}.js`,
  `unattended/` (the unattended-run kit: the binding protocol, the four-verb driver, and the leg that
  reads the project's `.unattended.conf` declarations rather than restating them — a run that will
  merge and push with no owner turn replaces the explicit-ask checkpoint with a committed standing
  mandate it ASSERTS and cannot have written),
  `agent-instructions/`, `pytest-parallel-guardrails/` (bounded,
  attributable pytest-xdist runs: the four-knob ini recipe, the crashprobe worker-death
  attribution plugin, the aiosqlite closed-loop seam patch + forced-race gate), the
  `check-template-size.sh` gate, and `check-wiring.sh` (detects/auto-wires
  installed-but-unwired tools; SessionStart-driven).
- **`WIRE-INTO-PROJECT.md`** — the agent runbook for wiring the whole chain into a target repo.

## Layout

- Root: `README.md`, this charter, `WIRE-INTO-PROJECT.md`, the product template + its two companions.
- `tools/` — the deployable kits (copied into target repos).
- `skills/session-kickoff/` — the kickoff skill (stays at repo root for machine-junction discovery).
- `memory/` — this repo's dogfooded memory tree, FLAT: `README.md` · append-only `DECISIONS.md` ·
  `HYGIENE.md` · `TEMPLATE-SPEC.md` · the GENERATED `LIVE.md` + `ledger/<month>.md` ·
  `backlog/<FAMILY>.md` · `builds/<slug>/` · `gotchas/` · `guides/` · `map/` · `archive/` ·
  `project/` (the gate's five `*.txt` waiver registries and nothing else). Specs, reports, research
  and reviews live under a build's own folder, NOT the root. The `streams` enum is
  `playbook kickoff tooling deployer`. Version snapshots and the RETIRED session ledger live in
  `memory/archive/`.
- `.memory-tree.conf` · `.claude/SESSION-KICKOFF.md` · `.gitattributes` (LF discipline).

## Node registry

| Tag | Machine/user | Primary tree | Remote |
|-----|--------------|--------------|--------|
| `a` | daily-agent | `C:/projects/coding-governance` | `origin` (github `d41ly/coding-governance`) |
| `b` | agent5 @ `DESKTOP-3J1O6CD` | `C:/projects/coding-governance` | `origin` (github `d41ly/coding-governance`) |
| `c` | agent-0 @ `DESKTOP-8BKM8GN` | `C:/projects/coding-governance` | `origin` (github `d41ly/coding-governance`) |

IDs are `FAMILY-<slug>-<seq>` (`PLAY`/`KICK`/`TOOL`/`DEPL`); slug = node tag + CamelCase adjective-noun,
minted once per session. One append-only `memory/DECISIONS.md`; backlogs shard per family at
`memory/backlog/<FAMILY>.md`. Builds live at `memory/builds/<slug>/` — the discipline is a `streams`
value in each spec's status header, not a directory, so a build spanning two disciplines is one build.
Live work state is READ from the generated `memory/LIVE.md` (plus the `ledger/<month>.md` shards),
rendered by `gen_build_index.py` from build front matter and every spec's status header. There is no
authored session ledger: the sharded per-node one retired at playbook v2.4 / memory-tree kit 1.8 and
its shards sit frozen under `memory/archive/`.

## The gate suite (the merge bar) — `bash tools/run-gates.sh`

The full bar is green at the push boundary (earlier runs are diff-scoped); each leg rides the runner:
- `memory/` hygiene (19 checks, flat tree since kit 1.5; engine at kit 1.8) — `tools/memory-tree/check-memory-hygiene.sh`; checks 9, 13-16 and 17-19 delegate to `gen_build_index.py`, `corpus_ids.py` and `gotchas.py`
- recurring-bug-class checklist — `python tools/memory-tree/gotchas.py --for-diff <base>..<head>` prints the classes a diff can hit; run it before a review, not after
- harness meta-gate — `tools/memory-tree/check-arms.py` (every `fail` branch armed by a positive assertion naming its own failure text, or pinned shrink-only; keyed on the call site, pinned in both directions, excluded from its own scan)
- kickoff-manifest ratchet — `skills/session-kickoff/manifest-check.sh` (+ self-test)
- template size ≤32 KiB — `tools/check-template-size.sh`
- kit version markers — `tools/check-kit-versions.sh` (every kit's version constant present + the memory-tree marker/constant pair agrees)
- verdict epoch — `tools/memory-tree/check-verdict-epoch.sh` (+ self-test): the kit version DATES the engine's verdicts, so a diff that moves a non-comment line of `check-memory-hygiene.sh` must move `KIT_MEMORY_TREE_VERSION` too — `hygiene-parity.test.sh` derives its baseline floor from that constant, and a stale one made the floor point before the change
- row-keyed merge driver replay — `tools/memory-tree/merge-rows.test.sh` (the driver `tools/memory-tree/merge-rows.py`, launched through `tools/lib/pyrun.sh`, splits every line by SHAPE into ROW and STRUCTURE, hands structure to `git merge-file` positionally, key-merges only the row set, and recombines through a token skeleton — so `memory/DECISIONS.md` and `memory/backlog/*.md` auto-resolve an append-collision without duplicating, dropping or misfiling a row, and an unresolvable anchor grammar becomes a conflict rather than a silent take-ours). **The bar is mechanical: never worse than `git merge-file` on the same three blobs.** Every case runs a live control; conflicting where git resolves correctly is counted by name against a shrink-only constant (2 today: a row one side MOVED and the other DELETED, both directions), never hidden. Per-node: `bash tools/check-wiring.sh --fix` sets `merge.rows.driver`
- kit/dogfood doc parity — `tools/memory-tree/kit-dogfood-parity.test.sh` (the shipped `HYGIENE.template.md`/`SPEC-TEMPLATE.template.md` equal this repo's installed copies, modulo the `tools/` install prefix)
- python-launcher resolver — `tools/lib/resolve-python.test.sh` (one resolver that RUNS each candidate; every copy-installed kit carries it inline byte-identical, gated; the retired `command -v python3 || python` idiom is banned repo-wide)
- kit self-tests — `tools/hooks/agent-cap.test.sh`, `tools/agent-instructions/adopt-agent-instructions.test.sh`, `tools/pytest-parallel-guardrails/pytest-parallel-guardrails.test.sh`, `python tools/codebase-map/selftest.py`, `python tools/settings-merge.py --selftest`, `python tools/memory-recall/selftest.py`
- codebase-map adopter e2e — `tools/codebase-map/adopt-codebase-map.test.sh`: the adopter WRITES (conf, map tree, gate), so it is gated on the effects, not the exit code — it refuses before writing when the operator's tree is not the tree the kit dir resolves to, when the prefix is deeper than the gate template can resolve, and it never leaves a half-stamped conf. Added because a Tier-2 review found 4 of 7 defects, including a blocker, in the one file no leg executed
- **the review protocol is BINDING** — `memory/guides/REVIEW-PROTOCOL.md`: a review's verify stage spawns **at most 5 agents TOTAL** (the batch grows, the agent count never does) and **at most 5 run concurrently**. Enforced at the `Workflow` tool call by `tools/hooks/agent-cap.js` (it sees the inline `script`, which is where the rule actually gets broken) and on the bar by `tools/workflows/check-verifier-fanout.sh`, which delegates to that same hook rather than re-implementing it. Ready-made harness: `tools/workflows/tier2-review.js`.
- verifier fan-out — `tools/workflows/check-verifier-fanout.sh` (+ `.test.sh`) and the protocol's kit/dogfood parity, `tools/workflows/check-protocol-parity.test.sh`
- review-harness gates — `tools/workflows/check-review-join.sh` (no ref-keyed verdict join survives in any `tools/**/*.js` git can see — tracked OR untracked-and-unignored), `tools/workflows/check-workflow-syntax.js` (every workflow script parses as the async-function body its runtime evaluates), + `check-review-join.test.sh`
- run-gates canary — `tools/run-gates.test.sh` (the legs are single-sourced from `tools/gate-legs.json`; the canary asserts the manifest is well-formed and `run-gates.sh` hardcodes no leg command)
- branch guard self-test — `.githooks/pre-commit.test.sh` (the pre-commit refuses primary-tree commits off the default branch)
- pre-push self-test — `.githooks/pre-push.test.sh` (the pre-push runs the full bar on a default-branch push, blocks a red one)
- push-main self-test — `tools/push-main.test.sh` (the lander reconciles origin before the gate, retries a mid-gate race capped, aborts a conflict; the hook refuses a raw default-branch push)
- wiring-health self-test — `tools/check-wiring.test.sh` (`check-wiring.sh` detects/auto-wires unwired tools: `core.hooksPath`, agent-cap, the three-state `recall-opened` opt-in, and CRLF on the `eol=lf`-pinned `.claude/` renders — reported in `--check`, byte-rewritten in `--fix`)
- agent-instructions wiring — `tools/agent-instructions/adopt-agent-instructions.sh --check`
- memory-recall skill wiring — `tools/memory-recall/adopt-memory-recall.sh --check` (the rendered `.claude/skills/memory-recall/SKILL.md` still matches `.memory-tree.conf`)
- drift-audit selftest — `python tools/drift-audit/selftest.py` (every gateable signal exercised twice: silent on a clean fixture, firing on a minimal violating one)
- drift-audit wiring — `bash tools/drift-audit/adopt-drift-audit.sh --check` (the rendered Skill still matches `SKILL.template.md` + the conf; the project layer exists)
- drift-audit records — `python tools/drift-audit/drift_report.py --check` (record-vs-reality signals at or under their shrink-only pins in `tools/drift-audit/drift_signals.py`)
- **the unattended-run protocol is BINDING** — `memory/guides/UNATTENDED-PROTOCOL.md`: a run that will
  merge and push with no owner turn replaces the explicit-ask checkpoint with a committed standing
  mandate it ASSERTS and cannot have written. Three legs: `tools/unattended/check-unattended.sh`
  (eleven checks — the declarations parse, the CORE phase and DoD sets have not shrunk below their
  floor, every phase is in the vocabulary, every claim carries a PRESENT witness, at most one run is
  live, the run-state file's generated region still equals the build README slice it is a COPY of,
  the recorded BASE is the merge-base git reproduces, no run-state file names the bypass flag, and
  the shipped protocol equals the installed one), plus its sibling
  `tools/unattended/check-unattended.test.sh` and the driver's
  `tools/unattended/unattended.test.sh`. Both siblings are LEGS, not files someone remembers to run
- unattended skill wiring — `bash tools/unattended/adopt-unattended.sh --check` (the rendered
  `.claude/skills/unattended/SKILL.md` still matches `SKILL.template.md` + `.unattended.conf`, AND
  carries no surviving `{{`-shaped placeholder — template parity and placeholder completeness are
  two questions, and a conf that declares nothing for a key renders a Skill that is perfectly in
  sync and tells the agent to call `{{KEEPALIVE_CREATE}}`)
- codebase-map coverage + freshness — `python tools/codebase-map/test_codebase_map.py` (nine inventories over the gate legs, kits, hooks, workflow scripts, skills, gotcha classes, guides and backlog shards: a new moving part reds until a dossier claims it, and the generated artifacts byte-compare against a fresh render). The map is installed at the non-canonical `tools/` prefix, so `adopt-codebase-map.sh` refuses and `reuse_lookup.py`/`map_diff.py` need `CODEBASE_MAP_ROOT` — see `memory/map/features/codebase-map.md` §Gaps

The full bar's authoritative run is the tracked **`.githooks/pre-push`** hook: a push to the default
branch runs `tools/run-gates.sh` once and blocks a red push (classify on the remote ref; the validated
tree must be the pushed tip; `GOV_GATE_CMD` overrides the gate for testing; `--no-verify` bypasses).
Earlier runs (DoR, post-merge) are diff-scoped. The active hooks are the tracked `.githooks/` dir via
`core.hooksPath`, NOT an out-of-tree copy, so there is no staleness-drift class here (the
`WIRE-INTO-PROJECT.md` copy-install path would reintroduce it — a scoped follow-up). Wire into CI by
running `tools/run-gates.sh` in a workflow (needs a `workflow`-scoped push — a follow-up). A tracked
pre-commit fast leg is in `.githooks/` (install: `git config core.hooksPath .githooks`) — it also
enforces the §3 branch guard (refuses a primary-tree commit off the default branch; pin with
`GOV_DEFAULT_BRANCH`, override with `--no-verify`). A SessionStart hook in `.claude/settings.json`
runs `tools/check-wiring.sh --session`, which auto-sets an unset `core.hooksPath` (never clobbers a
set value) so a fresh clone self-heals instead of running with dormant gates.

## Conventions

- **LF** on all `.sh` + the memory-tree data files (`.gitattributes`); verify staged bytes on Windows.
- Kits live in `tools/`; the session-kickoff skill stays at `skills/` (machine-junction discovery).
- The template is the operating ruleset — keep it ≤32 KiB; anything activity-scoped or one-time goes
  in a companion, not the template.
- Follow the governance playbook (`parallel-coding-governance.template.md`) for the full multi-node
  rules — this repo is its reference dogfood.
- Commit freely; **merge to `main` and `git push` each need an explicit ask — or a committed standing
  mandate naming the build and both actions**, whose shape the merge bar validates. The mandate is
  ASSERTED, never written by the run that uses it, and must be reachable from the run's pinned BASE:
  a run that authors its own authorization has none. Rules: `memory/guides/UNATTENDED-PROTOCOL.md`.
