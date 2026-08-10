# TOOL-aUnmannedHelm-1 — the unattended-run kit: a mandate on disk, not a block of chat

**Status:** SPECCED · rev-2 · 2026-08-10 · node a · Tier-2 · base e7ec3365 · streams tooling+kickoff+playbook+deployer · ratified 2026-08-10

## 1. Goal

Turn the owner's hand-typed "build UNATTENDED per the RULES" block into a durable kit, so an
unattended run is launched by naming a build folder rather than by retyping a protocol that has
already drifted between runs. The kit is four layers — a run-state file that survives context
compaction and process death, a skill carrying the judgment protocol, a driver script owning the
mechanical legs, and a merge-bar leg so the protocol cannot rot — plus the three surfaces the owner
pulled into scope on 2026-08-10: the `/session-kickoff` hand-back contract, the `agent-cap` hook
beyond the `Workflow` tool, and an adopter path so other repos get the same affordance.

## 2. Scope (IN)

Seven units. Each becomes its own conforming sub-spec under `spec/` before its code is written;
this file is the master scope and the owner decision menu.

- **S1 · run-state.** `RUN.md` at a build-folder root, admitted by the memory-tree kit: extend check
  4's whitelist, add it to `index_set()` and check 8's population, bump
  `KIT_MEMORY_TREE_VERSION`, and move `memory/HYGIENE.md` with
  `tools/memory-tree/HYGIENE.template.md` in one commit. Hybrid file: a generated region rendered
  from the sources `gen_build_index.py` already reads, plus an authored region holding only the four
  underivable facts.
- **S2 · the protocol.** `memory/guides/UNATTENDED-PROTOCOL.md` (charter-cited, therefore binding
  and read-path-budgeted), shipped as `tools/unattended/UNATTENDED-PROTOCOL.template.md`. It encodes
  the owner's rules with the six corrections in §4. A new
  `parallel-coding-governance.domain-rules.md` §15 holds the project-agnostic form, reached by a
  one-line pointer inside the template's §1.
- **S3 · the driver.** `tools/unattended/` with `check-unattended.sh`, an `unattended.py` engine and
  four verbs: `--preflight` (worktree, branch guard, wiring `--fix`, BASE pin, keepalive scheduled
  and recorded, RUN.md written), `--resume` (print the resume point), `--status` (the one line a
  keepalive fire reads), `--close` (assert the DoD before the run may end, reap the keepalive).
- **S4 · the gate leg.** One leg, `bash tools/unattended/check-unattended.sh`, written with the
  `fail() {` helper deliberately so it joins the `check-arms.py` population, with a sibling
  `check-unattended.test.sh` carrying a positive `hit` per branch and a measured `ARMS_FLOORS`
  entry. Registered in `tools/gate-legs.json`, cited by script path in the charter's
  `## The gate suite` section, and claimed with every other new inventory key by one new dossier
  `memory/map/features/unattended-run.md`.
- **S5 · the skill.** `.claude/skills/unattended-build/SKILL.md`, rendered from
  `tools/unattended/SKILL.template.md` plus `.memory-tree.conf` by `adopt-unattended.sh`, with an
  `eol=lf` pin so `check-wiring.sh` repairs it.
- **S6 · session-kickoff.** Split Step 5's three bundled obligations (the card, the literal prompt
  string, the stop) and change only the stop: under a declared unattended mandate the engine hands
  the card to the driver instead of halting. Resolve the other five interactive exits. Place the
  unattended skill in the written precedence chain.
- **S7 · the adopter path.** `adopt-unattended.sh` carrying the codebase-map-grade write guards (a
  logical walk-up bounded by `.git`, the inode compare against the operator's tree, refusal before
  any write) plus its own e2e test on the six-arm precedent; the `.gitattributes` pins; and the
  prose wiring in `WIRE-INTO-PROJECT.md`, `parallel-coding-governance.customize.md` and
  `tools/check-kit-versions.sh`.

The agent-cap work that used to sit in S7 folded into `TOOL-aNumeralWarden-1` at F2, so this build
now DEPENDS on that spec reaching rev-3 and landing. The measurement that justifies the fold's
design stays here (§4), because it is this build's evidence and it is what the modality refusal is
keyed on.

## 3. Non-goals (OUT)

- **A general job scheduler or a daemon.** The keepalive is the harness's own session-scoped cron and
  nothing else. Measured: those jobs are in-memory, die with the session, and fire only while the
  REPL is idle.
- **Reviving a dead session.** Out of reach of anything in this repo. The kit's answer to process
  death is that the record on disk is complete enough for a NEW session to resume; it does not
  attempt restart.
- **Teaching `agent-cap.js` to count agents.** Ruled out on measured evidence (§4). The arity
  guarantee moves to the record, the close assertion and the bar leg.
- **Editing `agent-cap.js`, its test, its wired copy or the review protocol's text.** All of it is
  `TOOL-aNumeralWarden-1`'s after the F2 fold. This build states the requirement and consumes the
  result; it does not touch the file. Two specs claiming one edit is how a half-applied change
  passes every gate.
- **A fourth declaration of the gate command.** The bar is already declared in the playbook, the
  kickoff manifest and `tools/gate-legs.json`; the kit reads, never restates.
- **Wiring `RUN.md` to the row-keyed merge driver.** The qualifying grammar is documented so the
  option stays open; the wiring waits for a second node demonstrably writing one RUN.md.
- **Retiring `STATUS.md`.** It stays the human overview. Follow-up if the two prove redundant.
- **`memory/project/in-flight/` reconciliation.** `drift_report.py` reads an authored run-state
  there that hygiene check 3 forbids. Real, pre-existing, and its own unit — filed to the backlog,
  not fixed here.

## 4. Design

### Data model — `RUN.md`

Lives at `memory/builds/<slug>/RUN.md`. Illegal today: check 4 whitelists exactly `README.md`,
`STATUS.md` and the four dirs, and a fixture run through the real engine reds with
`HYGIENE check 4 FAILED — build-folder naming/shape`. S1 extends the whitelist rather than dodging
it, because the kit is the product and an adopter needs the same affordance.

Two regions, split mechanically:

- **Generated**, delimited by a marker pair and rendered by the driver, reusing `apply_region()`'s
  contract verbatim (exactly one open marker, exactly one close, close after open, replace the
  slice — never a whole-file regex). It carries the unit list, per-unit status and the pinned BASE,
  all of which `gen_build_index.py` already derives from build front matter and spec status headers.
  A `--check` mode byte-compares it and rides the bar.
- **Authored**, holding ONLY the four facts nothing derives: the standing mandate verbatim, the
  phase, the keepalive id, and the parked decisions. It must never restate a unit status or a BASE
  sha — that is exactly the shape `TOOL-aFoldedQuarry-4` retired, and
  `memory/gotchas/two-answers-to-one-question.md` is `universal: true`, so every reviewer of this
  diff will be asked about it by machine.

The precedent is the argument. `memory/builds/aPrunedCeremony/STATUS.md` still says
`STATUS: IN-PROGRESS` with `- OPEN · final overview; delete watchdog cron`, while the generated
region of the same build's `README.md` correctly says `CLOSED · 6 unit(s)`. The authored half rotted
and the derived half did not, in the one file this build proposes to institutionalise.

**Phase** is its own closed enum, deliberately not the seven-token spec vocabulary — `CLOSED` there
already means "built AND landed", and there is no token for "built, reviewed, not merged", which is
the gap aPrunedCeremony invented `## Closing` for. Every phase claim carries a git-checkable witness
(a sha, a branch, a workflow id); a claim naming no witness is `unjudgeable` and never scores clean,
reusing `drift_report.py`'s judgeability discipline rather than inventing a second.

Two mechanical constraints on the authored half, both reproduced against the real engine: no
relative `.md` link may name a file that does not exist yet (check 2 reds), and no bare id may
appear before something anchors it (check 14 reds). So the unit list is minted as backlog rows
before RUN.md names it, and witnesses are shas and workflow ids, which are neither links nor
grammar-recognised ids.

### The six corrections to the owner's rules

The rules are sound in outline; these are the load-bearing edits, and S2 encodes them.

1. **"Ratify the most FEATURE-RICH decisions" gains a bound.** Every fork resolving toward more work,
   compounding across sub-specs, with no counter-force, is a scope ratchet. The playbook already
   calls the readiness menu "a menu to select from, not scope-creep licence", and
   `aPrunedCeremony` RD7 records a template fork where "feature-rich" was not an available option at
   ~86 bytes of headroom. New rule: *ratify the most feature-rich option that fits the acceptance
   criteria and every named budget; when two fit, take the reversible one.*
2. **Review intensity matches tier, not file count.** A blanket adversarial review of every spec
   contradicts three rules of the BINDING `memory/guides/REVIEW-PROTOCOL.md`: match intensity to
   target richness, review light or skip over hardened code, and stop once the design is judged
   clean. Measured there: 47 agents / 3.65 M tokens unbatched against 9–10 / 0.81–1.25 M batched.
3. **Regrounding becomes state-driven and unconditional.** "If a context compaction occurred
   (<100k tokens in memory)" asks the model to read a number it cannot see, so it never fires.
   Replaced by: re-read RUN.md at every pass boundary, always.
4. **The keepalive gets a payload and an honest limit.** Its prompt becomes a re-entry protocol —
   read RUN.md, resume at the first non-terminal unit — not the word CONTINUE. Measured properties
   that belong in the protocol doc: jobs are session-only and in-memory, so nothing is orphaned by a
   crash and nothing survives one either; they fire only while the REPL is idle, so a busy session
   never pays for the interval; recurring jobs auto-expire after 7 days, which is a hard ceiling on
   one run. The interval takes an off-minute spelling so a fleet does not land on the same instant.
5. **"Minimum chat" becomes "write to disk".** Chat is not the cost, it is the record that is lost.
   The house rule already exists in template §16 — facts land on disk before the wrap-up, because a
   dead turn may lose prose but never facts.
6. **A stop condition and a parked-decisions channel.** A per-unit failure budget: after N failed
   attempts the unit is parked with its evidence and the run continues elsewhere rather than
   burning. A fork that genuinely needs the owner is resolved to the reversible default, written to
   the parked section with the question, the options seen and the reason, and surfaced in the
   wrap-up. Today the run's only options are guess or burn.

Additions the rules never had: preflight (worktree, branch guard, wiring), the immutable BASE pin
the closing diff review needs, the bar named (`tools/run-gates.sh` at the push boundary and
`gotchas.py --for-diff` BEFORE the review), merge reconciliation named (the row-keyed driver, the
additive rule, never reconcile a generated index, the auto-took class), the DoD write-back, and a
declared agent budget.

### `agent-cap` — measured, then decided

The central question was whether a `PreToolUse` hook can count fan-out. Both halves are now measured
on this node rather than argued.

- **The payload does carry a session key.** A throwaway probe captured `session_id`,
  `transcript_path`, `cwd`, `prompt_id`, `permission_mode`, `tool_use_id` and `hook_event_name`,
  plus `CLAUDE_CODE_SESSION_ID` in the environment. So the reconnaissance's blocking unknown is
  resolved: a per-session key exists, and `prompt_id` is stable across one user prompt's whole
  agentic run.
- **And counting still fails, for the other reason.** A four-call burst in one turn produced
  overlapping hook-process intervals, and two of the four processes read the same
  `seen_before = 1` — a read-then-decide counter would have counted three where four occurred, on
  the first attempt. Only one of six pairs overlapped, so the miscount is also nondeterministic,
  which is the worst property a gate can have. The append itself never lost a line: `O_APPEND` is
  sound, the READ is not.

Therefore: **`agent-cap.js` stays a static source scanner and does not count** — consistent with the
already-ratified "both enforcement points are STATIC", now with a measurement instead of an
inference. The matcher widens as a no-op commit first (the tool gate makes that provably safe),
then gains a per-call **modality** refusal: a direct `Agent` spawn is denied while RUN.md declares a
verify phase, requiring the harness there. Its honest hole — a session with no run-state file is
unguarded — is declared in the protocol doc, not implied away. The real arity guarantee lives in the
record, the close assertion and the bar leg. Reusing today's predicate on a prompt is rejected
outright: measured, rule 1 denies the English sentence "run these in parallel (five at a time)".

Per F2 the hook edits land in `TOOL-aNumeralWarden-1`, which goes to rev-3 to carry the modality
refusal and re-reviews before code. What this build owes that spec is the interface it keys on: the
run-state file's phase field, its resolution rule from `__dirname` rather than cwd, and the declared
fail-open when no run-state file exists. What this build owes itself is that S4's leg still pins the
arity from the record, because the hook's guarantee is now someone else's schedule.

### The three ratified shapes (F1, F3, F4)

**F1 — the authorization amendment.** `AGENTS.md` and the playbook's §1 change from "an explicit
ask" to "an explicit ask, OR a committed standing mandate naming this build and both actions". The
mandate is RUN.md's authored region, so the authorization is a reviewable object in git rather than
a sentence in a dead transcript. Deliberately narrow: an ordinary session still needs the word, and
a mandate that does not name both actions does not grant them. The gate leg checks the SHAPE of the
claim (a mandate block naming the build slug and both verbs), never whether the owner meant it.

**F3 — the protocol travels, with config hooks.** The full judgment protocol is product and ships as
`tools/unattended/UNATTENDED-PROTOCOL.template.md`. Two declarations become project-configurable
rather than hard-coded: the **phase vocabulary** and the **DoD assertion set**. They follow the
kit-local project-layer precedent (`drift_signals.py`, `map_extractors.py`) — seeded once from a
template, project-owned, never overwritten on re-pull — because both are structured data that
`KEY=VALUE` cannot hold. The cost, stated rather than absorbed: a configurable enum is a new input
the gate must validate, so S4 grows an arm asserting the declared vocabulary is well-formed and that
the driver and the skill both read it rather than restating it. A configurable enum nobody validates
is two answers to one question with extra steps.

**F4 — `--close` blocks, with a recorded override.** It refuses while any DoD item is outstanding
(gates red, memory unwritten, manifest unstamped, map keys unclaimed, keepalive unreaped). It
asserts and refuses; it never repairs — the `check-wiring --session` scar is about a mode that
rewrote bytes, not about a mode that said no. The override takes a named item, never a blanket
skip, and writes the item plus its reason into RUN.md's parked section, so an overridden DoD item
surfaces in the wrap-up instead of vanishing. An override with no reason is refused, and the gate
leg treats an overridden item as outstanding for the purpose of the run's own record.

### Inventory — what the bar demands of a new kit

Derived from the gates, not from prose. Each is a landing requirement, not a nicety.

| Obligation | Why it reds if skipped |
|---|---|
| leg in `tools/gate-legs.json`, `argv[0]` in the launcher allow-set | the canary rejects a malformed leg |
| leg script path cited in the charter's `## The gate suite` | `handkept_inventories_disagreeing_with_source` goes 7 → 8 over its pin |
| one dossier claiming the leg, kit, guide and skill keys, artifacts re-rendered | `baseline.toml` additions are banned; coverage reds |
| sibling `.test.sh` with a positive `hit` per `fail` branch | the arms meta-gate conscripts any `.sh` defining `fail() {` |
| `eol=lf` pin on the rendered skill | a byte-comparing check reds every line on a Windows checkout |
| the inline `resolve_python` block, byte-identical; no bare launcher | the resolver leg byte-compares every tracked copy |
| `check-kit-versions.sh` entry | the charter claims every kit carries a version constant |
| `last-audit` re-stamp | `gate-legs.json` and `.memory-tree.conf` are both on the manifest's watch list |

### Alternatives rejected

- **A mode flag on `/session-kickoff`.** Its identity, posture and precedence chain are stated three
  times as an interactive launchpad, it ships as one per-machine junction adopters cannot partially
  take, and a flag makes one document carry two postures with every future edit needing to be
  correct in both.
- **The engine writing the READY record.** It would need the path from the manifest, which is a
  v1.2 marker bump and a forward-drift WARN on every adopter still at v1.1. The driver writes it
  instead: cheaper AND stronger, since a script writing a file beats a model transcribing chat.
- **A sibling skill under `skills/`.** Junctioned discovery means a new install step on all three
  nodes and no dogfooding from the worktree that writes it. A rendered project-local skill gets the
  existing CRLF repair and the adopter path for free.
- **The protocol in the playbook template.** 685 bytes free buys one §-stub, not a section. The
  rules go to the companion; a one-line pointer inside §1 costs less than a new stub.
- **A counting hook, a per-call batch-declaration lint, and a presence test for the run-state file.**
  The first fails open on the burst it exists to catch (measured); the second can only ban a
  spelling when the defect is a provenance; the third cannot red once landed.

### Files touched (estimate)

New: `tools/unattended/` (engine, gate, both tests, adopter, two templates, README),
`memory/guides/UNATTENDED-PROTOCOL.md`, `memory/map/features/unattended-run.md`,
`.claude/skills/unattended-build/SKILL.md`. Edited: `tools/memory-tree/check-memory-hygiene.sh` and
its two doc twins, `tools/hooks/agent-cap.js` and its test and wired copy, `tools/check-wiring.sh`
and its test, `tools/gate-legs.json`, `tools/check-kit-versions.sh`, `.memory-tree.conf`,
`.gitattributes`, `skills/session-kickoff/SKILL.md`, the playbook template and both companions,
`AGENTS.md`, `WIRE-INTO-PROJECT.md`, the regenerated map artifacts.

## 5. Production-readiness checklist

- **security** — the driver WRITES (a conf stanza, a rendered skill, RUN.md), so it takes the
  codebase-map-grade guards: logical walk-up bounded by `.git`, an inode compare refusing when the
  operator's tree is not the tree the kit resolves to, and refusal before any write. The keepalive
  prompt is data the run wrote, so the protocol states it is not an instruction channel.
- **perf / scale** — legs run sequentially, so the new leg adds its own wall time to a 213 s bar;
  target under 2 s, and no `guard` (39 of 40 legs are unguarded and a guard makes a leg invisible on
  branches that do not touch it).
- **a11y** — N/A, no user interface.
- **i18n** — N/A.
- **error / empty / loading states** — every refusal names the message, never the exit code; a skip
  announces itself; an empty population is a failure, not a pass.
- **observability** — RUN.md is the observable; `--status` is the one line a keepalive fire reads.
- **risks** — the dominant one is a false deny under an unattended run, where nobody can override it
  and the run stalls where it is most expensive. Mitigation: the modality refusal is narrow, the
  matcher widens as a measured no-op first, and the deny string is distinguishable so the arm can
  name the branch. Second risk: two answers to one question if the authored region restates
  anything derivable.
- **testing + left-shift gates** — four checks that can actually red (protocol parity with a content
  rider, rendered-skill drift, run-state schema with git-refutable references and a population
  guard, skill-versus-driver phase-set equality) plus an adopter e2e on the codebase-map precedent.
- **migration / rollback** — additive. The hygiene whitelist entry, the leg and the skill each
  revert independently; no existing build folder is required to grow a RUN.md.
- **user docs** — `WIRE-INTO-PROJECT.md` adopt section, a `customize.md` conditional-sections row,
  the kit README, and the charter's gate-suite citation.

## 6. Acceptance criteria

- **AC1** — When a build folder holds a `RUN.md`, `bash tools/run-gates.sh` is green; when the same
  file is renamed to any non-whitelisted name, hygiene check 4 reds naming it.
- **AC2** — When the generated region is hand-edited, the `--check` leg reds and names the drift;
  when the driver re-renders, it goes green, and a second render is byte-identical.
- **AC3** — When the authored region restates a unit status or a BASE sha, the gate reds. Both the
  passing and the failing case are observed before the gate is trusted.
- **AC4** — When a run-state file names a phase outside the enum, a `base_sha` that is not an
  ancestor of the build's branch, or a spec path git no longer tracks, the leg reds on each,
  separately. When no run-state file exists anywhere, the population guard reds rather than passing.
- **AC5** — When the shipped protocol template and the installed guide diverge, the parity leg reds;
  when both are gutted of the rule they exist to state while staying equal, the content rider reds.
- **AC6** — When a phase name is added to the skill without teaching the driver, the phase-set
  equality check reds; and the reverse.
- **AC7** — When `adopt-unattended.sh` is run from a different repo, from an unsupported install
  prefix, or through a junctioned kit dir, it refuses AND writes nothing into either tree — asserted
  on the absence of the writes, not on the exit code.
- **AC8** — When a project's declared phase vocabulary or DoD assertion set holds a malformed entry,
  the gate leg reds naming the entry; when the driver or the skill restates a phase name rather than
  reading the declaration, the phase-set equality check reds. A second `--scaffold` never overwrites
  a seeded declaration, asserted on the bytes.
- **AC9** — When `--close` is overridden for a named DoD item, that item and its reason land in
  RUN.md's parked section and in the wrap-up. When the override carries no reason, or is given as a
  blanket skip rather than a named item, `--close` refuses.
- **AC12** — When RUN.md's mandate block omits the build slug or either authorized verb, the gate
  leg reds naming what is missing; when it names all three, the leg is green. Both cases are
  observed before the leg is trusted.
- **AC13** — When `TOOL-aNumeralWarden-1` has not yet landed, S4's leg still reds on a run-state
  record whose verifier count exceeds the cap. The arity guarantee does not depend on the hook's
  schedule, which is the whole reason it lives in three layers.
- **AC10** — A full unattended run of a throwaway two-unit build completes from `--preflight` to
  `--close` with zero owner turns, survives a forced re-read of RUN.md as its only context, and
  `--close` refuses while any DoD item is outstanding.
- **AC11** — `python tools/drift-audit/drift_report.py --check` stays at or under its pins, and the
  codebase-map coverage gate is green with no `baseline.toml` addition.

## 7. Gates

The standing bar (`bash tools/run-gates.sh`, 40 legs today) plus one new leg,
`bash tools/unattended/check-unattended.sh`. Newly relevant existing legs: the verdict-epoch leg
(S1 moves a non-comment line of the hygiene engine), kit/dogfood parity (the HYGIENE twins),
`check-arms.py` with a new measured `ARMS_FLOORS` entry, the codebase-map coverage gate, the
drift-audit records leg, the resolver leg, `check-kit-versions.sh`, and the manifest ratchet
(`gate-legs.json` and `.memory-tree.conf` are both watched, so `last-audit` re-stamps).
`python tools/memory-tree/gotchas.py --for-diff <base>..<head>` runs BEFORE each review; it emits
`two-answers-to-one-question` unconditionally, which is the checklist entry this build most needs.

## 8. Open questions

### F1 — does the committed mandate satisfy the "explicit ask" for merge and push?

RESOLVED (owner, 2026-08-10): amend narrowly. Design in §4, "The three ratified shapes".

`AGENTS.md` and the playbook's §1 both require an explicit ask for the merge to shared `main` and
for the push. An unattended run ends with both. The `aDeployScout` research gestures at
"committed = the standing authorization for unattended re-runs", but that is research, not a
ratified rule, so today the run is charter-violating on its last two steps no matter what the kit
does. **Recommendation: amend both documents narrowly** — an explicit ask, *or* a committed standing
mandate naming this build and both actions — because the alternative is either a rule everyone
knowingly breaks or an unattended run that cannot finish. This is a charter change and is the one
fork that must be ratified before any code.

### F2 — sequencing against `TOOL-aNumeralWarden-1`

RESOLVED (owner, 2026-08-10): FOLD, against the recommendation. The agent-cap half of S7 moves into
`TOOL-aNumeralWarden-1`, which goes to rev-3 and re-reviews; the adopter half stays here as S7. This
build now depends on that spec landing, and its two open forks are on this critical path. The
recommendation's cost stands and is accepted: one review will cover two unrelated predicates, so
that review is scoped by predicate rather than by file.

That spec is SPECCED at rev-2 and already claims `KIT_AGENT_CAP_VERSION` 1.1 → 1.2, the hook's
header, the wired copy, the test's arms and the BINDING protocol text, with two of its own forks
still open. Two specs must not both claim those edits. **Recommendation: land aNumeralWarden-1
first and sequence S7 after it**, rather than folding; folding makes one review cover two unrelated
predicates. S7 is then BLOCKED, not OPEN, until it lands.

### F3 — how much of the protocol is project-agnostic?

RESOLVED (owner, 2026-08-10): all of it, plus config hooks — the phase vocabulary and the DoD
assertion set become project-owned declarations. Design and its added gate obligation in §4.

The domain-rules §15 form travels to adopters; the `memory/guides/` form is this repo's installed
copy. **Recommendation: the full judgment protocol travels** (it is the product), and only the gate
command and the id/family grammar are read from conf. The alternative — a thin travelling rule and
a fat local one — recreates the hand-kept-second-copy defect the parity gates exist to remove.

### F4 — does `--close` block the run, or only report?

RESOLVED (owner, 2026-08-10): blocks, with a named and recorded override. Design in §4; AC9 pins
the refusal of a reasonless or blanket override.

`check-wiring.sh` was narrowed to report-only in its session-scoped mode after it rewrote
`.claude/settings.json` and stripped CR bytes out of a PNG. **Recommendation: `--close` BLOCKS**,
because it is the only thing standing between a half-finished run and a push, and unlike the
session hook it runs at an explicit boundary rather than on every session start. It asserts and
refuses; it does not repair.

### F5 — one build or two?

RESOLVED (owner, 2026-08-10): one build, one sub-spec per unit. Seven units, not the six named when
the fork was put — the `/session-kickoff` unit was omitted from that count in error; the answer is
unaffected, since the choice was between one build and a split.

Seven units spanning four streams is large. **Recommendation: one build, seven sub-specs**, because
the units share one contract (RUN.md's shape) and splitting would put that contract in one build and
its three consumers in another. Named here so the owner can split it instead.

## 9. Revision log

- rev-1 · 2026-08-10 · initial draft. Grounded on a five-lens reconnaissance of the kickoff
  hand-back, the agent-cap matcher, the adopter contract, the memory-tree hygiene surface and the
  gate/arms/byte budgets, plus two direct measurements on this node: the `PreToolUse` payload keys,
  and a four-call burst proving hook processes overlap and a read-then-decide counter miscounts.
- rev-2 · 2026-08-10 · all five forks ratified by the owner. F2 went against the recommendation
  (fold rather than sequence), so S7 splits: the agent-cap half moves to `TOOL-aNumeralWarden-1` and
  this build gains a dependency on it. F3 and F4 each took the more feature-rich option, so §4 gains
  the config-hook and recorded-override designs and §6 gains AC8, AC9, AC12 and AC13. F1 amends the
  charter's explicit-ask rule narrowly. Unit count corrected 6 → 7 in F5.

## 10. Reuse audit

`python tools/codebase-map/reuse_lookup.py "unattended autonomous session driver with status file
and watchdog"` returns no seam — the closest hits are `derive_status` in `gen_build_index.py` and
`signal_spec_status` in `drift_report.py`, both fan-in 0, and no affordance seam matches. A
tree-wide grep for "unattended" over tracked files hits nine files, every one a *record of* a past
run and none a rule for a future one. So the kit is genuinely new, but it is assembled from existing
seams rather than invented:

- `gen_build_index.py` `apply_region()` — the generated-region splice contract, reused verbatim.
- `gen_build_index.py`'s derivation — the unit list, per-unit status and BASE come from the two
  sources it already reads; the driver renders, it does not re-derive.
- `drift_report.py`'s judgeability discipline — a claim naming no sha is `unjudgeable` and never
  scores clean; reused for phase claims.
- `check-protocol-parity.test.sh` — the parity-plus-content-rider shape for the protocol doc.
- `adopt-memory-recall.sh` and `adopt-codebase-map.sh` — the render-and-diff `--check` arm, the
  leftover-placeholder guard, the literal `python3` in a committed render, and the write guards.
- `adopt-codebase-map.test.sh` — the three adopter-test disciplines and its six arm classes.
- `check-memory-hygiene.sh` `pop_guard` — the empty-population-is-a-failure precondition.
- `tools/workflows/tier2-review.js` — the review harness the protocol points at, not a new one.
- `tools/hooks/agent-cap.js` — extended, never re-implemented; one predicate, two entry points.
