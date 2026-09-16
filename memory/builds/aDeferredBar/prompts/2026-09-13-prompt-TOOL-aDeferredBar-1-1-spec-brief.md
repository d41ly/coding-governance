# Spec brief — TOOL-aDeferredBar-1 — the instruction, at every carrier a build agent reads

**Serves:** journal TOOL-aDeferredBar-1

The writer authors `memory/builds/aDeferredBar/spec/2026-09-13-spec-TOOL-aDeferredBar-1.md` at
Tier 2 against `memory/TEMPLATE-SPEC.md`. The research record under `build/` settled the design;
this brief carries what the spec must decide and what it may not re-open. Read the research
record whole first.

## The mechanism, in one sentence

A build pass runs NO merge bar and NO self-test suite; it verifies with the one direct check its
spec names; the full bar runs once, after every unit is terminal, at the main loop. Stated at
every carrier a build agent reads, changed at each carrier's SOURCE and re-rendered.

## The write set (section 4 files table), derived by grep and not to be widened silently

1. `tools/workflows/unattended-unit.js` — the child PROMPT gains the ban and the substitute, in
   the same register as its existing driver-step sentences: no `run-gates.sh` in any form, no
   `GATE_FULL=` or `GATE_SELFTESTS=` prefix, no `run-selftests.sh`, no `run-unattended-gates.sh`,
   no `*.test.sh` suite; verify with the direct check the spec's acceptance names — a checker run
   on a staged break, a `--selftest` flag, a fixture — and return the need for a suite verdict to
   the parent in `summary` rather than running it. Its `gov:kit unattended-unit@1.0` engine
   identity moves to `1.1`.
2. `tools/workflows/unattended-build.js` — ONE sentence in `GROUND`, because it prefixes every
   stage agent: no stage of this program runs the merge bar or a self-test suite. And the SPEC
   writer prompt gains the acceptance rule: every criterion names a DIRECT observation, never a
   bar or suite invocation, because unit 2's gate refuses one and the unit that would run it
   stalls for hours. `gov:kit unattended-build@1.0` moves to `1.1`.
3. `tools/memory-tree/BUILD-METHOD.template.md` M6 — REPLACE the sentence *"Then the diff-scoped
   gates for what the pass touched; the full bar runs ONCE, at the push boundary."* with the rule:
   a pass runs no bar and no suite; the direct check the spec names is its verification; the bar
   runs ONCE at close; where a pass touched files a leg guards and the MAIN LOOP judges a bar
   necessary, the plain bar with no flag is the scoped form, at the main loop and never in a
   child. Render to `memory/guides/BUILD-METHOD.md`. **M1's budget is ≤27648 bytes and is NOT
   raised**: the file is 26439 bytes today; the replacement must fit, trimmed elsewhere in M6 if
   it does not. The `<!-- gov:kit memory-tree@2.74 -->` marker and `KIT_MEMORY_TREE_VERSION` in
   `tools/memory-tree/check-memory-hygiene.sh` move together to `2.75` — the pair is gated.
4. `tools/unattended/SKILL.template.md` — one bullet under "While it runs", rendered to
   `.claude/skills/unattended/SKILL.md` by `bash tools/unattended/adopt-unattended.sh`.
   `KIT_UNATTENDED_VERSION` in `tools/unattended/unattended.sh` moves `1.19` → `1.20`, and every
   render carrying `gov:kit unattended@` follows.
5. `memory/guides/SESSION-KICKOFF.md` line 263 — *"run the full bar, never a list"* is a
   push-boundary sentence read as a per-pass rule; qualify it in place. The manifest is watched
   and `memory/guides/BUILD-METHOD.md` is in its `watch:` line, so this unit owes a `last-audit`
   re-stamp and a `manifest-audit: delta …` line in the commit message.

NOT in the write set, and section 3 says why: `tools/unattended/PROTOCOL.template.md` sits at
its byte cap and the rule is a method rule, not a contract term; `tools/run-gates/run-gates.sh`
gains no leg-selection flag (the plain bar's guard scoping IS the scoped form); no adopter tree.

## What the acceptance criteria must look like — this unit obeys its own rule

Every criterion names a DIRECT observation with a backticked command: `grep -c` over a rendered
file for the sentence, `node --check`, `bash tools/check-kit-versions.sh`, `wc -c` under the
budget, `bash skills/session-kickoff/manifest-check.sh`, `python tools/check-spec-tokens.py`.
NOT ONE criterion may name `bash tools/run-gates/run-gates.sh`, a `GATE_*=` prefix, or a
`*.test.sh` suite as its observation. The §7 leg line names the legs that grade these files —
`build-method size`, `kit version markers`, `verdict epoch (kit version dates the engine)`,
`unattended skill wiring`, `workflow script syntax`, `kickoff-manifest ratchet`, `memory hygiene`,
`method carriers (every pointer declared)` — resolved against `tools/gate-legs.json` by
`python tools/check-spec-tokens.py --list` before you return.

## Forks already resolved by the research record — mark them RESOLVED (agent, 2026-09-13, delegated)

- **Protocol vs method as the carrier of the rule** → the method (M6), for the byte-cap reason.
- **A leg-selection flag on the runner** → not built; the manifest guard is the scoped form.
- **One sentence in GROUND vs per-stage prompts** → GROUND, once, plus the writer-prompt rule.

## Stamps this unit will meet, so it does not discover them one gate at a time

A watched kit file owes `last-audit` AND `last-body-change` in the manifest AND the kit version in
every carrier that spells it — the gate remedy names three of five. `bash tools/check-kit-versions.sh`
is direct and cheap, and so is each leg's own script run by hand; run those, never the bar.
