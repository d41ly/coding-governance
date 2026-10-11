# TOOL-aOrientedCast-11 — a role agent runs no gate, and the write gate's hook refuses one

**Status:** CLOSED · rev-2 · 2026-10-12 · node a · Tier-2 · base 646d4a73 · streams tooling · order 11 · ratified 2026-10-11

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-11-build-TOOL-aOrientedCast-11-1-acceptance-ledger.md](../build/2026-10-11-build-TOOL-aOrientedCast-11-1-acceptance-ledger.md) | journal | — |
| [2026-10-11-prompt-TOOL-aOrientedCast-10-0-owner-addendum.md](../prompts/2026-10-11-prompt-TOOL-aOrientedCast-10-0-owner-addendum.md) | research | TOOL-aOrientedCast-10 |
| [2026-10-11-prompt-TOOL-aOrientedCast-10-1-spec-brief.md](../prompts/2026-10-11-prompt-TOOL-aOrientedCast-10-1-spec-brief.md) | journal | TOOL-aOrientedCast-10 |

<!-- /gen:spec-records -->

## 1. Goal

The owner ruled that gates are the main session's job at the merge or push threshold and never an
agent's: a spec writer may run the memory hygiene gate and the lexicon, a builder the lexicon, and
every other agent nothing. Today a subagent may run any leg, and the texts handing agents their work
tell them to verify with a `--selftest` flag. This unit adds a Bash and PowerShell arm to
`scratch-guard.js` that refuses a gate run from any payload carrying an `agent_type`, reads each
role's allowlist from the policy file `TOOL-aOrientedCast-10` creates through `.claude/roles.json`,
and rewrites every text that hands an agent its work to say the same.

## 2. Scope (IN)

- **S1** — The policy file gains a `[gates]` table: one entry per role slot, a list of gate-leg
  names that role may run. Gov's copy names `memory hygiene` and `lexicon naming predicates` for
  `gov-spec-writer`, and `lexicon naming predicates` for `gov-builder`. `load_policy` validates it
  as §4 "Refusals" states, and `check_roles.py`'s R12 reports it. Observed by AC4.
- **S2** — `render_agents.py` writes the allowlists into `.claude/roles.json`: a top-level `gates`
  object holding `manifest`, the gate manifest's repo-relative path or null, and a `gates` list on
  every role, empty where the policy names none, in the shape of §4 "Data model". Observed by AC4.
- **S3** — `loadRoleIndex` in `scratch-guard.js`, which `TOOL-aOrientedCast-6` exports, grades the two
  new keys' shape when present and reads them as absent otherwise. Observed by AC3.
- **S4** — `checkRoleGate(cmd, data)` in `scratch-guard.js`, evaluated on a `Bash` or `PowerShell`
  payload after the scratch verdict and the orientation check, in the order of §4 "The evaluation
  order". It refuses a simple command that is a gate-leg argv the role's allowlist does not name, the
  bar runner, the self-test runner, the unattended gates runner, a `*.test.sh` or `selftest.py`
  script, or a script carrying `--selftest`, as §4 "The rows" states. Observed by AC1 and AC2.
- **S5** — Arming, as §8 F3 resolved it: no `agent_type`, no index, or no candidate in the command
  admits as today; a broken index refuses a candidate; a manifest the index names that does not read
  leaves the leg row unarmed with one witness line, while the other rows still bind. Observed by AC3.
- **S6** — A throw inside the arm refuses, naming the error, on a payload carrying an `agent_type`
  (§8 F5). NOT OBSERVED by a criterion of its own: once every input is guarded no payload reaches a
  throw, so the catch is a backstop; the builder stages one throw when the arm is first observed.
- **S7** — The refusal names the agent type, the simple command, the row and leg that matched, the
  role's allowlist and the index, and says the main loop runs gates at the merge or push threshold, so
  the agent returns the need. Observed by AC1.
- **S8** — The file header states the arm, its order and its ceiling, and `tools/hooks/README.md`
  gains a section saying the same. The ceiling sentence: textual matching cannot see a gate reached
  through an interpreter, an alias, a function or an assembled path, and the push-boundary bar is
  still the guarantee. NOT OBSERVED by a criterion: prose, read by the review against §4.
- **S9** — The texts that hand agents their work say the rule, each named in §4 "The texts": the role
  blocks of `gov-builder`, `gov-spec-writer`, `gov-spec-reviewer`, `gov-diff-reviewer`, `gov-skeptic`
  and `gov-synthesizer`; the unit harness's pass paragraph; the build harness's ground text and its
  untyped spec-writer prompt; and the build method's M6 sentence, with one M8 sentence it points at.
  Gov's agent types, the build harness's render and the build method's render are regenerated.
  Observed by AC5 and AC6.
- **S10** — The arms live in `tools/hooks/scratch-guard.test.sh` over its fixture repository, with a
  role index and a manifest written for the new arms and absent for every arm that exists today;
  `FLOOR_ASSERTIONS` moves by the count added. Observed by AC1, AC2 and AC3 as direct probes in the
  pass, and RED-first by the main loop at the close (§7).
- **S11** — The watched build method owes the kickoff manifest a `last-audit` re-stamp naming its
  parent in this unit's commit. Observed by AC6.

## 3. Non-goals (OUT)

- Refusing a gate to the main loop. It carries no `agent_type`, and the gates are its job.
- `tools/unattended/gate-guard.js`. It keeps its phase gate unchanged: the flagged bar and every suite,
  for every caller the main loop included, before `VERIFYING` in an unattended run (§8 F1).
- `memory/TEMPLATE-SPEC.md`'s direct-check paragraph and `tools/check-spec-tokens.py`'s `bar` reason.
  Both name the observation a criterion makes, a checker on a staged break or a `--selftest` flag,
  without naming who makes it, and both stay true once that observer is the main loop at the close.
- Proving an agent did not reach a gate by another route. The arm stops forgetting, not evasion.
- A waiver, an environment knob or a warn phase. Enforcement starts at landing, by the owner's ruling.
- A kit version bump beyond one per kit. This unit is the build's last to move the hooks, roles,
  workflows and memory-tree kits, so it bumps each once, on every carrier: hooks 1.32 to 1.33, the
  review harness 1.45 to 1.46, memory-tree 2.139 to 2.140, roles 1.0 to 1.1 (rev-2).

**The build method is a governance carrier, changed here by the owner's instruction.** The owner's
addendum of 2026-10-11, quoted in
`memory/builds/aOrientedCast/prompts/2026-10-11-prompt-TOOL-aOrientedCast-10-0-owner-addendum.md`,
rules that agents run no gate beyond the two named, and the build method's M6 sentence says the
opposite of that today. M3's veto 2 keeps a carrier change for the owner, and this one is his.

**This run's passes meet the arm only once it lands.** This session's hooks run from the primary tree,
so the arm binds this session once the landing merge is in that tree's working copy. Until then the
run's passes follow the rule from their ground text, as the addendum records.

**What it is built on.** Besides the edge below, this unit extends `TOOL-aOrientedCast-3`'s renderer
and the index it writes, `TOOL-aOrientedCast-6`'s exported `loadRoleIndex` and the suite fixture its
arms build, and the unit harness prompt `TOOL-aOrientedCast-4` typed. It builds after
`TOOL-aOrientedCast-7` only because both edit the hooks kit. Those specs were written before this
unit existed and declare no edge to it, and a one-sided edge reds the hygiene gate's join, so the
dependency is stated here rather than as an edge.

### Edges

- **consumes-from** `TOOL-aOrientedCast-10` — the policy file, `load_policy` and R12, which this unit
  extends with `[gates]`. Without them the allowlist has no home the owner edits.
- **hands-off** external — a gate reached through an interpreter, an alias or a slice of a suite in a
  temporary script, which only the push-boundary bar sees.
- **hands-off** external — the specs of this build still open whose criteria name a suite slice or a
  `--selftest` run; under the rule their passes observe by probe, and the slice's verdict moves to the
  close.

## 4. Design

### Evidence

Read at `646d4a73` plus this build's commits to `6ca3cb2d8`, on 2026-10-11, node a.

- `.claude/settings.json` wires `scratch-guard.js` on `Bash|PowerShell|Edit|Write|MultiEdit|NotebookEdit`
  and `gate-guard.js` on `Bash|PowerShell`. The hooks kit ships with every default install
  (`tools/govkit/registry.toml`, the `agent-cap` entry of `[selection] default`); the unattended kit,
  which holds `gate-guard.js`, does not.
- `scratch-guard.js`'s Bash path runs the scratch verdict, then `checkOriented`, each under a
  fail-open catch (`tools/hooks/scratch-guard.js:1100-1130`); its write gate fails closed
  (`:1084-1099`). `checkOriented` exempts any payload with `agent_id` (`:724`). It already holds a
  quote-blanking command view and an original-text token reader (`:221-286`) and the toplevel walk
  (`:592-606`).
- `gate-guard.js` denies, at command position in a blanked view, the flagged bar (D1), a word ending
  `run-selftests.sh` (D2) or `run-unattended-gates.sh` (D3), and a `.test.sh` or `selftest.py` script
  (D4), opening one `bash -c` body (D5), and only while an unattended run on the branch is before
  `VERIFYING` (`tools/unattended/gate-guard.js:19-46`, `:388-392`). It admits a `--selftest` flag on
  any other file, the plain bar, and everything in an attended session (`:34-37`, `:47-50`). It copies
  `buildHeredocView` rather than requiring this kit, because a sibling require is banned (`:139-143`).
- The gate manifest is `<tool root>/gate-legs.json`, and the runner resolves a leg's `{prefix}`
  against the tool root (`tools/run-gates/run-gates.sh:216`, `:1988-1996`). A shipped kit file
  already reads it from its derived tool root (`tools/drift-audit/drift_signals.py:179`). Its 134
  rows are each `name`, `argv`, `chunk`, `subject` and `ceiling`; `{prefix}` is the only token, and
  some rows spell a repo-relative path instead (`.githooks/…`, `skills/session-kickoff/…`).
- The leg names the allowlist uses exist: `memory hygiene` runs `bash {prefix}/memory-tree/check-memory-hygiene.sh`
  and `lexicon naming predicates` runs `python {prefix}/lexicon/lexicon.py`.
- Measured over the manifest, the near-misses of a prefix match: `kickoff-manifest ratchet` runs
  `bash skills/session-kickoff/manifest-check.sh` bare, so every `manifest-check.sh --card …` the
  orienter's kickoff runs would match it; `lexicon naming predicates` would match every
  `lexicon.py --suggest`; the bare `check-template-size.sh` row would match its four file-argument
  siblings. A match on the script alone would also refuse `gotchas.py --for-diff`, which M6 has every
  pass run, because `gotchas.py --selftest` is a leg.
- A main-loop payload carries no `agent_type`; a subagent's carries `agent_type` and `agent_id`; a
  session launched as an agent carries `agent_type` alone; an untyped `Workflow` agent reads
  `workflow-subagent` (`memory/builds/aOrientedCast/build/2026-10-11-build-TOOL-aOrientedCast-3-agent-type-probe.md:39-51`).
- The texts that say the opposite today: the builder's block (`tools/roles/agents/gov-builder.agent.md:14-15`,
  `:28-31`), the spec writer's (`tools/roles/agents/gov-spec-writer.agent.md:30-32`), the spec
  reviewer's (`tools/roles/agents/gov-spec-reviewer.agent.md:26-27`), the skeptic's
  (`tools/roles/agents/gov-skeptic.agent.md:24`), the unit harness's pass paragraph
  (`tools/workflows/unattended-unit.js:251-258`), the build harness's ground text and untyped
  spec-writer prompt (`tools/workflows/unattended-build.template.js:825-827`, `:846-848`, `:932-934`),
  and M6 (`tools/memory-tree/BUILD-METHOD.template.md:194-200`, rendered to
  `memory/guides/BUILD-METHOD.md` by the memory-tree adopter's `--render`). The review harness already
  tells every judge to run no bar, suite, runner or `--selftest` flag
  (`tools/workflows/tier2-review.template.js:613`).
- `memory/guides/BUILD-METHOD.md` measures 28818 bytes against its 30720-byte budget, and the kickoff
  manifest watches it (`memory/guides/SESSION-KICKOFF.md:5`).
- The owner's earlier ruling `TOOL-aProbedUnit-8` (2026-09-14) put every gate at the session's close;
  this addendum narrows the exceptions to the two legs named.

### Data model

The policy file's new table, beside `TOOL-aOrientedCast-10`'s `[effort]`:

```toml
[gates]                       # the gate legs a role may run, by manifest name; every other role runs none
gov-spec-writer = ["memory hygiene", "lexicon naming predicates"]
gov-builder = ["lexicon naming predicates"]
```

The index after this unit, every other key as `TOOL-aOrientedCast-3` writes it:

```json
{ "gates": { "manifest": "tools/gate-legs.json" },
  "harnesses": ["…"],
  "roles": { "gov-builder": { "agent": true, "gates": ["lexicon naming predicates"],
                              "workflow": "build", "writes": "product" } } }
```

`render_agents.py` derives `manifest` as the tool root's `gate-legs.json`, the location the runner and
the drift kit already read, folded relative to the toplevel; null when no file is there, with a `note`
line. A role the policy does not name gets `"gates": []`.

### Refusals

`load_policy` adds, for `[gates]`: a key naming no role file or an `agent: false` role; a value that
is not a list of strings; a name the manifest holds no leg for, checked only when the manifest reads,
and a `note` otherwise.

### The rows

A SIMPLE COMMAND is a segment of the command split at `;`, `|`, `&`, `(`, `)` and a newline in the
blanked view, read from the original text. Its HEAD is the first word after any leading `NAME=value`,
`env`, `export`, `nohup`, `time` and `timeout` with its options and duration, then a launcher (`bash`,
`sh`, `python`, `python3`, `python3.<n>`, `py`, `node`) with one option; `-c` on `bash` or `sh` scans
its body once as a command of its own, `-n` executes nothing and ends the segment, and `-c` or `-m` on
a Python launcher ends it. The ARGV is the head and every word after it.

| Row | Matches | Admitted when |
|---|---|---|
| G1 leg | the argv equals a manifest leg's argv from its first path-bearing word on, `{prefix}` resolved to the manifest's directory, each path resolved against the payload `cwd` and compared in `buildComparablePath`'s form relative to the toplevel | the role's allowlist names that leg |
| G2 runner | the head's basename is `run-gates.sh`, `run-selftests.sh` or `run-unattended-gates.sh`, in any form | never |
| G3 suite | the head ends `.test.sh` or `selftest.py`, or the head is a script and `--selftest` is among its words | the words carry `--render`, `--list` or `--help`, or the simple command is a G1 leg the allowlist names |

A simple command that is an allowlisted G1 leg is admitted whole. Any other hit refuses the call. G2
and G3 spell file shapes by role, as `gate-guard.js` and the unit harness's prompt already do, so no
path into a sibling kit is written (§8 F4).

### The evaluation order

`checkRoleGate` returns null to admit, `{ witness }` to admit with one stderr line, or `{ deny }`:

1. `agent_type` absent or empty → null.
2. No simple command has a head that is a launched script, a path-bearing word or a G2 or G3 shape →
   null, with no file read.
3. No toplevel above the payload `cwd` → null.
4. `loadRoleIndex(toplevel)`: absent → null; broken → deny naming the index.
5. The allowlist: the index's `gates` list for `agent_type`, else empty, so a type the index does not
   name, `workflow-subagent` and every built-in among them, may run nothing.
6. `readGateLegs(toplevel, index)`: the manifest's legs with their argv resolved; null `manifest`, an
   absent file or a parse failure leaves G1 unarmed and returns a witness naming it.
7. Each simple command against the rows; the first refused one → deny; else null, or the witness of
   step 6.

`main` calls it after `checkOriented` under its own catch, which denies on a throw when the payload
carries an `agent_type` (§8 F5).

### The probe payloads

The criteria pipe one JSON payload per line below into `node tools/hooks/scratch-guard.js`, with
`tool_name` `Bash` (the PowerShell line `PowerShell`), `cwd` the toplevel and `agent_type` as the
column says, and read its exit code. Kept in a fence because these are payload data, not commands
anyone runs.

```text
# REFUSED, exit 2 naming the row, for gov-builder
bash tools/run-gates/run-gates.sh
GATE_SELFTESTS=1 bash tools/run-gates/run-gates.sh
bash tools/run-gates/run-selftests.sh --pooled
bash tools/unattended/run-unattended-gates.sh --checks
bash tools/hooks/agent-cap.test.sh
python tools/govkit/selftest.py
python3 tools/memory-tree/gotchas.py --selftest
python tools/roles/check_roles.py                         # G1, naming roles catalogue
bash -c 'bash tools/hooks/agent-cap.test.sh'
$env:GATE_FULL=1; bash tools/run-gates/run-gates.sh       # PowerShell
# BY ROLE
bash tools/memory-tree/check-memory-hygiene.sh            # 0 gov-spec-writer · 2 gov-builder, workflow-subagent
python tools/lexicon/lexicon.py                           # 0 gov-builder, gov-spec-writer · 2 gov-skeptic
# NEAR-MISSES, exit 0 for gov-builder
python3 tools/memory-tree/gotchas.py --for-diff HEAD~1..HEAD
python3 tools/lexicon/lexicon.py --suggest checkRoleGate --as js.function
bash tools/workflows/check-protocol-parity.test.sh --render
bash -n tools/hooks/agent-cap.test.sh
git log --oneline -- tools/hooks/agent-cap.test.sh
grep -n run-gates.sh AGENTS.md
git commit -m "names bash tools/run-gates/run-gates.sh"
# NEAR-MISS, exit 0 for gov-orienter
bash skills/session-kickoff/manifest-check.sh --card --path
```

### Refusal text

`renderGateDeny` opens `BLOCKED by scratch-guard: a role agent runs no gate`, names the agent type,
the simple command, the row, and the leg by name where G1 matched, then the type's allowlist and the
index path. It ends: gates run in the main session at the merge or push threshold, so return the need
in your result, and verify your change with a fixture or a probe of your own code. It names no file of
another kit.

### The texts

Each says the rule once and points at M6 rather than restating the allowlist, whose one home is the
policy file.

| Text | Change |
|---|---|
| `gov-builder` block | verify with a fixture or a probe of the code you changed, such as a `python -c` or `node -e` call or your unit's CLI over a scratch fixture; run no gate, suite, slice of one or `--selftest` beyond the lexicon; name each arm whose red-first observation the close owes |
| `gov-spec-writer` block | criteria name observations a pass can make without a gate, and a new arm is declared under `New arm:`; you may run the memory hygiene gate and the lexicon over your specs and nothing else |
| `gov-spec-reviewer`, `gov-skeptic` blocks | a criterion's or a finding's command that is a gate, a suite or a `--selftest` is described, not run |
| `gov-diff-reviewer`, `gov-synthesizer` blocks | one sentence: you run no gate (M6) |
| unit harness pass paragraph | the direct check becomes a fixture or a probe of the unit's own code; the lexicon is the one leg a builder runs; a new arm's red-first is the close's |
| build harness ground text and untyped spec-writer prompt | the same, in their two sentences and in the criterion clause |
| build method M6 | an agent pass verifies with a fixture or a probe of its own code and runs no gate beyond what its role's allowlist names, which a hook enforces; a new arm's red-first observation is the main loop's at the close. It names no kit, since a sibling kit in a rendered template is a token |
| build method M8 | before the bar, the main loop observes each `New arm:` line of the build's specs RED on its staged break and GREEN restored, and records it in that unit's acceptance ledger under a `Pass: none` commit |

The M8 sentence is the existing record, the acceptance ledger, which `TOOL-aOrientedCast-8` already
wrote after its pass under `Pass: none`. No new record kind is made.

### Inventory

| Identifier | Kind | Cell |
|---|---|---|
| `checkRoleGate` | function, the arm's verdict | `js.function`; `lexicon.py --suggest checkRoleGate --as js.function` answered OK |
| `scanCommandHeads` | function, the simple commands and their argv | `js.function`; answered OK |
| `readGateLegs` | function, the manifest's legs with resolved argv | `js.function`; answered OK |
| `checkGateLeg` | function, G1 for one argv | `js.function`; answered OK; the canon refused `matchGateLeg` for `match` |
| `renderGateDeny` | function, the refusal text | `js.function`; answered OK |
| `run_role_bash`, `write_gate_manifest` | self-test helpers | `sh.function`; each answered OK |

### Rollout

Lands at order 11, after `TOOL-aOrientedCast-6` and `TOOL-aOrientedCast-7`, the other two units
editing the hooks kit. Two commits carry it (rev-2). The first holds the policy table, the library
and checker, the renderer, the hook and its arms, the README sections, the role blocks, the two
harnesses and the build harness's render, the build method's template and render, the four kits'
version bumps with the `/build` Skill's render, the kickoff manifest's re-stamp and the regenerated
symbols. The second holds gov's re-rendered agent types and index under its own `--dispatch`, because `--dispatch`
refuses a generated index declared beside its generator (check 49), and flips this spec CLOSED. A hook script is read afresh on every call, so the arm binds every session
whose hooks run from a tree holding this commit, from its next subagent shell call; in gov that is the
landing merge in the primary tree. From then this session's own subagents, and every `Workflow`
sidechain agent, are refused gates; the close's bar and the red-first observations run in the main
loop and are untouched. At an adopter the next `govkit update` brings the arm with the hooks kit, and
the allowlists with the roles kit's re-render; the seed's `[gates]` table reaches an adopter that
received the policy before this unit only by its owner's edit, and until then every role's allowlist
is empty, the strict reading.

### Files touched (estimate)

`tools/roles/house/policy.toml` · `tools/roles/roles_lib.py` · `tools/roles/render_agents.py` · `tools/roles/check_roles.py` · `tools/roles/README.md` · `tools/roles/agents/` · `.claude/agents/` · `.claude/roles.json` · `tools/hooks/scratch-guard.js` · `tools/hooks/scratch-guard.test.sh` · `tools/hooks/README.md` · `tools/workflows/unattended-unit.js` · `tools/workflows/unattended-build.template.js` · `tools/workflows/unattended-build.js` · `tools/memory-tree/BUILD-METHOD.template.md` · `memory/guides/BUILD-METHOD.md` · `memory/guides/SESSION-KICKOFF.md` · `memory/map/features/agent-cap.md` · `memory/map/features/roles.md` · `memory/map/generated/symbols.json` · and for the version bumps (rev-2) `tools/hooks/agent-cap.js` · `tools/workflows/tier2-review.template.js` · `tools/workflows/tier2-review.js` · `tools/memory-tree/check-memory-hygiene.sh` · the memory-tree kit's four doc templates and their renders · `tools/roles/SKILL.template.md` · `.claude/skills/build/SKILL.md`

### Alternatives rejected

- **The arm in `gate-guard.js`.** It holds the deeper command grammar, but it ships only with the
  unattended kit, binds only inside a run before `VERIFYING`, and cannot require `loadRoleIndex`, so it
  would bind no attended session and no default adopter and would need a second index reader (§8 F1).
- **The manifest's legs copied into the index.** Every leg added later would stale the index and red
  the render leg until a re-render; the path alone moves only when the manifest does.
- **A prefix or script-only leg match.** §4 "Evidence" measures both refusing a command the kickoff or
  M6 requires of an agent (§8 F2).
- **Keying the rule on `agent_id`.** A session launched as a role carries `agent_type` alone and is a
  role agent all the same.

## 5. Production-readiness checklist

- security — One more read of `.claude/roles.json` and of the manifest, only on a subagent shell call
  that holds a candidate; the payload is never put into a shell or a regex. The arm stops forgetting,
  not evasion, and the header says what passes it.
- perf / scale — Step 2 reads no file for the common call. A candidate costs one index parse and one
  manifest parse of about 60 KB, inside the node spawn the hook already pays.
- error / empty / loading states — An absent index admits; a broken one refuses a candidate; an
  unreadable manifest leaves the leg row unarmed and says so in a witness; a throw refuses.
- observability — Each refusal names the command, row, leg, type, allowlist and index; the witness
  names an unarmed leg row.
- risks — A role agent that needs a gate verdict now returns the need, so a pass that cannot be
  verified without one stalls to the close rather than running it; the role texts say so. A defect in
  the walker refuses a subagent's legitimate command; the near-miss probes of AC1 guard the known ones.
- testing — The arms of §7 in the hook's suite, observed RED-first at the close, and the direct probes
  of §6 in the pass.
- migration — Gov re-renders its index in this commit. An adopter's index gains the keys at its next
  update.
- user docs — The hooks README section, the roles README's note on `[gates]`, and the refusal text.

## 6. Acceptance criteria

No criterion runs a gate leg, a suite or a `--selftest` flag: each pipes a payload into the hook,
calls the unit's own code, or reads a rendered file. The hook's suite arms are under `New arm:` in §7.

- **AC1** — When `node tools/hooks/scratch-guard.js` reads, from this repository after the render,
  each REFUSED and BY ROLE payload of §4 "The probe payloads", every REFUSED line exits 2 naming its
  row for `gov-builder`, the `check_roles.py` line naming `roles catalogue`; the hygiene line exits 0
  for `gov-spec-writer` and 2 for `gov-builder` and `workflow-subagent`; the lexicon line exits 0 for
  `gov-builder` and `gov-spec-writer` and 2 for `gov-skeptic`. Every line exits 0 with no
  `agent_type`.
  Red when: a role agent runs a runner, a suite or a leg its allowlist does not name, an allowlisted
  leg is refused, or the main loop meets the arm.
  fixture: this repository once its index carries `gates`; the tree holds none at `646d4a73`.
- **AC2** — When `node tools/hooks/scratch-guard.js` reads each NEAR-MISS payload of §4 "The probe
  payloads" for the type its heading names, every one exits 0 with empty stderr.
  Red when: the walker reads a mention as a run, or a prefix match refuses a command the kickoff or
  M6 requires of an agent.
- **AC3** — When `node tools/hooks/scratch-guard.js` reads a `gov-builder` payload for the first
  REFUSED line of §4 "The probe payloads" in a scratch repository with no index it exits 0; with an
  index holding `{` it exits 2 naming the index, while `ls` exits 0; with an index whose
  `gates.manifest` names no file, a leg's exact argv exits 0 with a witness line naming the unarmed
  leg row, and the runner line still exits 2.
  Red when: an absent index arms the rule, a broken one admits a candidate, a non-candidate reads the
  index, or an unreadable manifest silences every row.
  fixture: a scratch repository under a short `%TEMP%` root, built in the pass.
- **AC4** — When `python tools/roles/render_agents.py --write` runs in gov, a `json.load` of
  `.claude/roles.json` holds `gates.manifest` equal to `tools/gate-legs.json`, `gov-spec-writer`'s
  `gates` equal to the two names, `gov-builder`'s to the one, and an empty list on every other role.
  With the policy's builder entry staged to name `nope`, a `python -c` call of `load_policy` raises
  naming `nope`, `python tools/roles/render_agents.py --check` exits 2, and a `python -c` call of
  `check_roles.check_roles` over a scratch copy of the kit returns one R12 defect naming it.
  Red when: the index loses an allowlist, or a misspelt leg name passes.
- **AC5** — When `grep -c "selftest. flag, a fixture"` runs over
  `tools/workflows/unattended-unit.js`, `tools/workflows/unattended-build.template.js`,
  `tools/roles/agents/gov-builder.agent.md` and `tools/roles/agents/gov-spec-writer.agent.md`, each
  prints 0; `python tools/roles/render_agents.py --check` exits 0, so `.claude/agents/` carries the
  new blocks; and the build harness's render equals its template rendered.
  Red when: a text still orders an agent to run a `--selftest` flag, or a rendered copy lags its
  source.
- **AC6** — When `wc -c memory/guides/BUILD-METHOD.md` runs it prints at most 30720; `grep -c "New
  arm:" memory/guides/BUILD-METHOD.md` prints at least 1; the template and the render carry the same M6
  and M8 sentences; and the `last-audit` line of `memory/guides/SESSION-KICKOFF.md` differs from its
  parent's.
  Red when: the method outgrows its budget, M8 never asks the main loop for the red-first
  observations, or the watched method moves unstamped.

## 7. Gates

`scratch-guard self-test` · `agent-cap self-test` · `hook destinations self-test` · `review-join self-test` · `verifier fan-out self-test` · `tier2-review self-test` · `unattended-build self-test` · `harness arms (fail branches armed or pinned)` · `workflow script syntax` · `roles catalogue` · `roles render wiring` · `roles render selftest` · `check-wiring self-test` · `kit/dogfood doc parity` · `method carriers (every pointer declared)` · `build-method size` · `kickoff-manifest ratchet` · `hook destinations (every declared hook path ships)` · `install-prefix (shipped surface)` · `lexicon naming predicates` · `codebase-map coverage + freshness` · `kit epoch (shipped bytes move, the version moves)` · `govkit selfcheck` · `recall floor` · `recall floor arms` · `memory hygiene` · `spec tokens (a spec's own names resolve)`

New arm: tools/hooks/scratch-guard.test.sh · covers AC1 AC2 AC3 · a role-gate block over the fixture repository, against a hook whose arm admits every subagent call, whose walker reads a mention as a run, or whose arming refuses with no index · `FLOOR_ASSERTIONS` raised by the assertions added
New arm: tools/roles/render_agents.py --selftest · covers AC4 · arm 12, an index whose role `gates` or `manifest` is staged out of the render · none

Both arms are written in the pass and observed RED and then GREEN by the main loop at the close (M8),
which is the observation this unit itself moves there. No pass runs a leg above.

## 8. Open questions

- **F1 — Which hook carries the arm?**
  Options: (a) `scratch-guard.js` in the hooks kit; (b) `gate-guard.js` in the unattended kit; (c) a
  shared command walker moved into one kit and required by both.
  (a) ships with every default install, already runs on `Bash|PowerShell`, and reads the index through
  `loadRoleIndex`; its cost is a smaller command walker than `gate-guard.js` holds. (b) binds only
  where the unattended kit is installed and only inside a run before `VERIFYING`, so no attended
  session and no default adopter; it would need a second index reader. (c) requires a sibling kit's
  file, which the install-prefix ban refuses, or moves the unattended kit's predicate, a public surface
  M3's veto 2 keeps for the owner.
  Recommendation: (a); (b) fails the goal's attended reach and (c) is vetoed. `gate-guard.js` keeps
  its phase gate for every caller.
  RESOLVED (agent, 2026-10-11, delegated): (a). The arm is `checkRoleGate` in `scratch-guard.js`, and
  `gate-guard.js` is unchanged.
- **F2 — What does "matches a leg's argv" mean?**
  Options: (a) the command's argv from its script on equals the leg's; (b) the leg's argv is a prefix
  of the command's; (c) the script alone.
  §4 "Evidence" measures (b) refusing the orienter's `manifest-check.sh --card …` calls and every
  `lexicon.py --suggest`, and (c) refusing `gotchas.py --for-diff`, which M6 requires of every pass.
  (a) admits a scoped variant of a leg, such as a file argument the leg does not carry, which the
  header states as part of the textual ceiling; the runner and suite rows still catch every expensive
  class whatever its arguments.
  Recommendation: (a).
  RESOLVED (agent, 2026-10-11, delegated): (a), as §4 "The rows" states G1.
- **F3 — How is the arm armed?**
  Options: (a) as `TOOL-aOrientedCast-6` and `TOOL-aOrientedCast-7` resolved: an absent index adds no
  arm, a broken one refuses; (b) an absent index arms the runner and suite rows for every subagent,
  with no allowlist. (b) changes every repository without the roles kit, where no allowlist exists
  for the owner to grant even the lexicon, and makes the three hooks disagree on one index.
  Recommendation: (a).
  RESOLVED (agent, 2026-10-11, delegated): (a), as S5 is written.
- **F4 — Where do the runner and suite shapes live?**
  Options: (a) as file-shape literals in the hook, the shapes `gate-guard.js` and the unit harness's
  prompt already spell; (b) rendered into the index from a declaration in the roles kit, which would
  need a key `workflows.toml` does not have or a list in the seeded policy that an update never
  refreshes. (b) adds a catalogue key, a public surface; and a seeded list would let an owner's file
  fall behind a new runner.
  Recommendation: (a).
  RESOLVED (agent, 2026-10-11, delegated): (a). The leg row alone reads the manifest, through the
  index's path.
- **F5 — Does a throw inside the arm admit or refuse?**
  Options: (a) refuse when the payload carries an `agent_type`, as the write gate refuses on a throw;
  (b) admit, as the scratch and orientation checks do. Under (b) a defect in the arm is a silent off,
  which the owner's no-bypass ruling forbids; under (a) it refuses every role agent's shell call that
  reaches it, which is loud and found at once.
  Recommendation: (a).
  RESOLVED (agent, 2026-10-11, delegated): (a), as S6 is written.

## 9. Revision log

- rev-1 · 2026-10-11 · initial draft.
- rev-2 · 2026-10-12 · §3 · §4 Rollout · Files touched. The build pass's dispatch carried the run's
  instruction that this unit, the build's last to move the hooks, workflows and memory-tree kits,
  bumps each once; the roles kit, created in this build and moved after its 1.0, owes the same, so
  the non-goal now names the four bumps. `--dispatch` refused gov's re-rendered agent types beside
  `render_agents.py` (check 49), so the re-render lands in a second commit of the pass, as
  `TOOL-aOrientedCast-10`'s did.

## 10. Reuse audit

`python tools/codebase-map/reuse_lookup.py "refuse a Bash command at command position that runs a
gate leg argv, the bar runner or a self-test suite when the payload carries an agent type"` ranked
generic names, `run`, `legs`, `leg` and `run_arms`, and no seam that reads a tool payload. The seams
extended are in the hooks kit: `main`'s Bash path, `buildCommandView`, `readTokenAt`,
`resolveToplevel` and `buildComparablePath` in `tools/hooks/scratch-guard.js`, and
`TOOL-aOrientedCast-6`'s `loadRoleIndex`; and in the roles kit, `load_policy` and the index writer
`TOOL-aOrientedCast-10` and `TOOL-aOrientedCast-3` built. The row shapes are `gate-guard.js`'s
`resolveFileRow`, restated by shape because a sibling require is banned (§8 F4).

`python tools/memory-recall/query.py "refuse a subagent running the merge bar, a self-test suite or a
gate leg from inside a build pass"` surfaced the owner's ruling `TOOL-aProbedUnit-8`, aDeferredBar's
`gate-guard.js` and its record that a `test_*.py` shape is a declared exemption, the unattended verbs'
"no merge bar and no self-test suite inside a pass", and `TOOL-aDeferredBar-1`'s sentences in the
carriers this unit rewrites.

Recall terms used: `gate-guard self-test suite run-selftests GATE_SELFTESTS subagent agent_id PreToolUse Bash unit pass direct check selftest`
