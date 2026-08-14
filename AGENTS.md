# coding-governance — working guide

Project-agnostic governance + tooling for running Claude Code (or any agent) across several
machines/sessions on one repo. This repo **dogfoods its own kits**: it runs the memory-tree hygiene
gate, the kickoff-manifest ratchet, the template size gate, and the codebase-map coverage gate on
itself. The map lives at `memory/map/`; its dossiers are the files under `memory/map/features/`, and the
keys not yet claimed by one are in the shrink-only `baseline.toml`. Both counts move as dossiers
land, so neither is spelled here — `python tools/codebase-map/reuse_lookup.py` prints the live pair.

*(Read by every AI tool: `AGENTS.md` is canonical; `CLAUDE.md` is a `@AGENTS.md` import — Claude Code
doesn't read AGENTS.md natively. Wired by `tools/agent-instructions/`.)*

## What ships here (the product)

- **`parallel-coding-governance.template.md`** — the governance playbook template (the operating
  ruleset; **≤32 KiB, strictly gated** by `tools/check-template-size.sh` — trim or externalize, never
  raise the limit). Companions: `.customize.md` (deploy-time placeholder catalog) and `.domain-rules.md`
  (the §1/§4/§7–§13 activity-scoped checklists the template references by §-stub — §1 is the newest,
  holding the kickoff-manifest merge exception the byte-gated template externalized, plus the
  kit-conditional unattended-run rules).
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
  `project/` (the gate's six `*.txt` waiver registries and nothing else). Specs, reports, research
  and reviews live under a build's own folder, NOT the root. The `streams` enum is
  `playbook kickoff tooling deployer`. Version snapshots and the RETIRED session ledger live in
  `memory/archive/`.
- `.memory-tree.conf` · `memory/guides/SESSION-KICKOFF.md` · `.gitattributes` (LF discipline).

## Node registry

| Tag | Machine/user | Primary tree | Remote |
|-----|--------------|--------------|--------|
| `a` | daily-agent | `C:/projects/coding-governance` | `origin` (github `d41ly/coding-governance`) |
| `b` | agent5 @ `DESKTOP-3J1O6CD` | `C:/projects/coding-governance` | `origin` (github `d41ly/coding-governance`) |
| `c` | agent-0 @ `DESKTOP-8BKM8GN` | `C:/projects/coding-governance` | `origin` (github `d41ly/coding-governance`) |
| `d` | d41ly | `C:/projects/coding-governance` | `origin` (github `d41ly/coding-governance`) |

IDs are `FAMILY-<slug>-<seq>` (`PLAY`/`KICK`/`TOOL`/`DEPL`); slug = node tag + CamelCase adjective-noun,
minted once per session. One append-only `memory/DECISIONS.md`; backlogs shard per family at
`memory/backlog/<FAMILY>.md`. Builds live at `memory/builds/<slug>/` — the discipline is a `streams`
value in each spec's status header, not a directory, so a build spanning two disciplines is one build.
Live work state is READ from the generated `memory/LIVE.md` (plus the `ledger/<month>.md` shards),
rendered by `gen_build_index.py` from build front matter and every spec's status header. There is no
authored session ledger: the sharded per-node one retired at playbook v2.4 / memory-tree kit 1.8 and
its shards sit frozen under `memory/archive/`.

## The gate suite (the merge bar) — `bash tools/run-gates.sh`

The full bar is green at the push boundary; earlier runs are diff-scoped, and now MECHANICALLY so.
Each self-test leg carries a `guard` in `tools/gate-legs.json` naming the kit dir it exercises, so a
records-only commit skips them and runs only the legs that check this repo's actual state — read the
split FROM the manifest, never from here. **`GATE_FULL=1` bypasses every guard, and
`.githooks/pre-push` sets it**, so the authoritative run is still total: a guard can only ever scope a
NON-authoritative run, which is what makes a too-narrow guard cost an early signal rather than a wrong
merge verdict. A guard naming an untracked path would skip forever and silently, so the run-gates
canary refuses one.
The runner executes legs **CONCURRENTLY** through a bounded pool, width `min(8, nproc)`, overridable
with `GATE_JOBS`; `GATE_JOBS=1` is the serial bar through the same code path and is the rollback for
any suspected concurrency problem. Legs are safe to run together because each heavy one is already
hermetic — it builds its own `mktemp -d` scratch repo and never writes into the real tree. Execution
order is scheduled longest-first from a timing cache the runner writes at `<git-dir>/gate-timings.tsv`;
REPORTING is always manifest order, so output is byte-stable whatever the width, and a corrupt or
absent cache costs wall clock only. Measured on node `a`: 335s serial to ~95s at width 8. Every leg's
output is persisted per-leg under `<git-dir>/gate-logs/`, redacted, and a RED run also leaves
`gate-last-failure.txt`, which only the next RED run overwrites. Each leg:
- `memory/` hygiene (20 checks, flat tree since kit 1.5; the engine's kit version is `KIT_MEMORY_TREE_VERSION` and is deliberately not repeated here — a version written in prose rots between bumps, and this one rotted twice in a day) — `tools/memory-tree/check-memory-hygiene.sh`; checks 9, 13-16, 17-19 and 20 delegate to `gen_build_index.py`, `corpus_ids.py`, `gotchas.py` and `row_grammar.py`
- recurring-bug-class checklist — `python tools/memory-tree/gotchas.py --for-diff <base>..<head>` prints the classes a diff can hit; run it before a review, not after
- harness meta-gate — `tools/memory-tree/check-arms.py` (every `fail` branch armed by a positive assertion naming its own failure text, or pinned shrink-only; keyed on the call site, pinned in both directions, excluded from its own scan)
- kickoff-manifest ratchet — `skills/session-kickoff/manifest-check.sh` (+ self-test)
- template size ≤32 KiB — `tools/check-template-size.sh`; the kickoff engine rides the same script at a
  MEASURED 18 KiB — `tools/check-template-size.sh skills/session-kickoff/SKILL.md 18432` (the limit is a
  positional because a leg cannot set an env var: the runner execs argv with no shell)
- kit version markers — `tools/check-kit-versions.sh` (every kit's version constant present + the memory-tree marker/constant pair agrees)
- verdict epoch — `tools/memory-tree/check-verdict-epoch.sh` (+ self-test): the kit version DATES the engine's verdicts, so a diff that moves a non-comment line of `check-memory-hygiene.sh` must move `KIT_MEMORY_TREE_VERSION` too — `hygiene-parity.test.sh` derives its baseline floor from that constant, and a stale one made the floor point before the change
- row-keyed merge driver replay — `tools/memory-tree/merge-rows.test.sh` (the driver `tools/memory-tree/merge-rows.py`, launched through the kit's own `merge-rows.sh` (which carries the resolver inline, so a copy-installed kit can start it; `tools/lib/` is gov-internal and ships nothing), splits every line by SHAPE into ROW and STRUCTURE, hands structure to `git merge-file` positionally, key-merges only the row set, and recombines through a token skeleton — so `memory/DECISIONS.md` and `memory/backlog/*.md` auto-resolve an append-collision without duplicating, dropping or misfiling a row, and an unresolvable anchor grammar becomes a conflict rather than a silent take-ours). **The bar is mechanical: never worse than `git merge-file` on the same three blobs.** Every case runs a live control; conflicting where git resolves correctly is counted by name against a shrink-only constant (2 today: a row one side MOVED and the other DELETED, both directions), never hidden. Per-node: `bash tools/check-wiring.sh --fix` sets `merge.rows.driver`
- kit/dogfood doc parity — `tools/memory-tree/kit-dogfood-parity.test.sh`
- method carriers — `tools/memory-tree/check-method-carriers.sh` (+ `tools/memory-tree/check-method-carriers.test.sh`): every file outside `memory/` that POINTS AT the build method is declared in a per-repo registry beside the other waiver lists, and points rather than copies. The kit ships no registry — an adopter's is SEEDED from their own measured population by `adopt-memory-tree.sh`, because gov's rows would name paths their tree does not have. Structural only: it catches a copied `## M<n>` section, not a fluent paraphrase, and says so (the shipped `HYGIENE.template.md`/`SPEC-TEMPLATE.template.md`, RENDERED for this install's prefix, equal this repo's installed copies — the gate performs the same substitution the adopter does, so what it grades is what an adopter receives; a surviving placeholder is its own arm)
- python-launcher resolver — `tools/lib/resolve-python.test.sh` (one resolver that RUNS each candidate; every copy-installed kit carries it inline byte-identical, gated; the retired `command -v python3 || python` idiom is banned repo-wide)
- kit self-tests — `tools/hooks/agent-cap.test.sh`, `tools/agent-instructions/adopt-agent-instructions.test.sh`, `tools/pytest-parallel-guardrails/pytest-parallel-guardrails.test.sh`, `python tools/codebase-map/selftest.py`, `python tools/settings-merge.py --selftest`, `python tools/memory-recall/selftest.py`
- codebase-map adopter e2e — `tools/codebase-map/adopt-codebase-map.test.sh`: the adopter WRITES (conf, map tree, gate), so it is gated on the effects, not the exit code — it refuses before writing when the operator's tree is not the tree the kit dir resolves to, when the prefix is deeper than the gate template can resolve, and it never leaves a half-stamped conf. Added because a Tier-2 review found 4 of 7 defects, including a blocker, in the one file no leg executed
- **the review protocol is BINDING** — `memory/guides/REVIEW-PROTOCOL.md`: a review's verify stage spawns **at most 5 agents TOTAL** (the batch grows, the agent count never does) and **at most 5 run concurrently**. Enforced at the `Workflow` tool call by `tools/hooks/agent-cap.js` (it sees the inline `script`, which is where the rule actually gets broken) and on the bar by `tools/workflows/check-verifier-fanout.sh`, which delegates to that same hook rather than re-implementing it. Ready-made harness: `tools/workflows/tier2-review.js`.
- install prefix — `tools/check-install-prefix.sh` (+ `tools/check-install-prefix.test.sh`): nothing this repo SHIPS may spell a root-install kit path. Kits install at `tools/<kit>/` in a target (ONE segment — the codebase-map gate template resolves no deeper), every engine derives its own prefix, and what actually strands an adopter is a path SPELLED in something they receive: a runbook step, a usage header, a remedy string, a rendered artifact. Those fail quietly — a `tools/` install used to scaffold the adopter's own committed hygiene rule-set document with seven dead kit paths while the hygiene gate exited 0. The kit-name alternation is DERIVED from the tracked `tools/*` dirs; `*.test.sh`/`selftest.py` are excluded because they build root installs on purpose to prove the dual-spelling support kept for the not-retrofitted adopters; deliberate spellings live in the shrink-only `tools/install-prefix-waivers.txt` (11 today) and a waiver whose hit is gone reds as stale
- verifier fan-out — `tools/workflows/check-verifier-fanout.sh` (+ `.test.sh`) and the protocol's kit/dogfood parity, `tools/workflows/check-protocol-parity.test.sh`
- review-harness gates — `tools/workflows/check-review-join.sh` (no ref-keyed verdict join survives in any `tools/**/*.js` git can see — tracked OR untracked-and-unignored), `tools/workflows/check-workflow-syntax.js` (every workflow script parses as the async-function body its runtime evaluates), + `check-review-join.test.sh`
- run-gates canary — `tools/run-gates.test.sh` (the legs are single-sourced from `tools/gate-legs.json`; the canary asserts the manifest is well-formed and `run-gates.sh` hardcodes no leg command)
- run-gates evidence — `tools/run-gates.evidence.test.sh` (a red leg's own output survives on disk under `<gitdir>/gate-logs/`, the durable summary POINTS at it, and `gate-last-failure.txt` outlives a green re-run; drives the runner through `GATE_LEGS` so it never re-enters the real bar)
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
  mandate it ASSERTS and cannot have written. The BASE that mandate hangs on is OBSERVED from the
  remote's own HEAD advertisement, never read from a local ref and never named by the environment —
  both of those were reproduced bypasses — and §9 of the protocol states plainly what a check running
  under the run's own uid can and cannot buy. Three legs: `tools/unattended/check-unattended.sh`
  (fifteen checks — the declarations parse, the CORE phase and DoD sets have not shrunk below their
  floor, every phase is in the vocabulary, every claim carries a PRESENT witness, at most one run is
  live, the run-state file's generated region still equals the build README slice it is a COPY of,
  the recorded BASE is the merge-base git reproduces, no run-state file names the bypass flag, the
  mandate at that BASE is asserted by the bar and not only by the driver, and the shipped protocol
  equals the installed one), plus its sibling
  `tools/unattended/check-unattended.test.sh` and the driver's
  `tools/unattended/unattended.test.sh`. Both siblings are LEGS, not files someone remembers to run
- unattended adopter e2e — `bash tools/unattended/adopt-unattended.test.sh`: the adopter WRITES, so
  it is gated on the EFFECTS in BOTH trees, never on the exit code. It refuses a foreign repo and an
  install prefix carrying whitespace (the kit path is interpolated into shell commands in the
  rendered Skill) before it reads anything, and it ADOPTS through a junction inside the adopting
  repo — the walk is logical, never physical. The junction arm skips LOUDLY where the host cannot
  create a link, because a copy would score a refusal as success
- unattended skill wiring — `bash tools/unattended/adopt-unattended.sh --check` (the rendered
  `.claude/skills/unattended/SKILL.md` still matches `SKILL.template.md` + `.unattended.conf`, AND
  carries no surviving `{{`-shaped placeholder — template parity and placeholder completeness are
  two questions, and a conf that declares nothing for a key renders a Skill that is perfectly in
  sync and tells the agent to call `{{KEEPALIVE_CREATE}}`)
- codebase-map coverage + freshness — `python tools/codebase-map/test_codebase_map.py` (nine inventories over the gate legs, kits, hooks, workflow scripts, skills, gotcha classes, guides and backlog shards: a new moving part reds until a dossier claims it, and the generated artifacts byte-compare against a fresh render). The map is installed at the non-canonical `tools/` prefix, so `adopt-codebase-map.sh` refuses; the query tools need no environment set — see the map's own dossier under `memory/map/features/` for the remaining gaps
- govkit registry — `python tools/govkit/govkit.py selfcheck`: the deployable population is a
  DECLARATION (`tools/govkit/registry.toml` plus a descriptor per entry), never a directory listing,
  and the leg asserts it against the tracked SURFACE in both directions — every depth-1 path under
  `tools/`, everything under `.githooks/` and `skills/session-kickoff/`, and the shipped root playbook
  files is an entry, a member of exactly one entry's file rules, or an exemption carrying a reason. An
  exemption naming a path that no longer exists reds, because a stale one silently widens the surface
  it was written to narrow. **No population count is written in the spec or the registry** — the leg
  derives every one, after the spec twice stated a figure the tree then moved underneath. Its first
  run over the real tree found seven problems, three of them real, which is why a new predicate is run
  before it is trusted rather than after. `plan` and `check` are READ-ONLY and their leg is
  `python tools/govkit/selftest.py`, whose arms assert a specific MESSAGE or on-disk effect and
  never an exit code alone — including the on-disk arm that `plan` leaves the target byte-identical
  a read-only verb that writes is the whole risk of that verb. It found two real defects on its
  first run, one of them a token regex matching the `{k}` inside a shell `${k}`

- **the self-test legs** — harnesses that ride the bar as their own leg, so a gate and the proof it
  can fail are both visible: `tools/memory-tree/check-memory-hygiene.test.sh` ·
  `tools/memory-tree/check-verdict-epoch.test.sh` · `skills/session-kickoff/manifest-check.test.sh` ·
  `tools/workflows/check-verifier-fanout.test.sh` · `tools/workflows/check-review-join.test.sh`, plus
  the engines carrying their arms in a `--selftest` mode rather than a sibling file —
  `tools/memory-tree/gen_build_index.py`, `tools/memory-tree/corpus_ids.py` and
  `tools/memory-tree/row_grammar.py`. This is the list the charter-completeness signal reads, not a
  claim that no other leg has a harness — a self-test nobody cites is a leg nobody notices going quiet.

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

- A build that runs more than one pass follows `memory/guides/BUILD-METHOD.md` — the spec set, the
  fork rule, the pass loop, regrounding, and the wrap-up derivation. It is rendered from the
  memory-tree kit; the unattended kit points at it, and `/session-kickoff` loads it at the hand-back.

- **LF** on all `.sh` + the memory-tree data files (`.gitattributes`); verify staged bytes on Windows.
- Kits live in `tools/`; the session-kickoff skill stays at `skills/` (machine-junction discovery).
- The template is the operating ruleset — keep it ≤32 KiB; anything activity-scoped or one-time goes
  in a companion, not the template.
- Follow the governance playbook (`parallel-coding-governance.template.md`) for the full multi-node
  rules — this repo is its reference dogfood.
- Commit freely; **merge to `main` and `git push` each need an explicit ask — or a committed build folder the
  run did not create**, whose shape the merge bar validates. The mandate is
  ASSERTED, never written by the run that uses it, and must be reachable from the run's pinned BASE,
  which is observed from the remote rather than read from any local ref. A run with full shell access
  can still defeat that; the protocol's §9 says exactly how, and the control that actually binds lives
  on the remote. Rules: `memory/guides/UNATTENDED-PROTOCOL.md`.
