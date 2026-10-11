<!-- gov:playbook -->
# coding-governance — agent charter

*Rendered from the coding-governance charter template, whose version is the marker below. Section 1
binds every repository that adopts it; section 2 is this repository's own; section 3 is generated
from the kits and answers it selected. Change a source and re-render with
`<prefix>/playbook/adopt-playbook.sh`; never edit the rendered text. Every rule is one line: a tool,
gate or protocol named in section 3 carries the detail.*

<!-- governance-template: v4.2 -->

## 1. Governing practices

<!-- one-line -->
- [yagni] YAGNI: build what this unit needs now, never scaffolding for later, and delete rather than disable.
- [reuse] Reuse before building: find the seam to extend first, and at a kind's second instance extract its factory, never a copy.
- [consistency] Consistency by construction: tokens, primitives and factories land before the features that use them, and every convention you can gate is gated.
- [core] One shared core with thin adapters, so logic and authorization live once; data changes additively, with defaults and an upgrade step.
- [contract] A contract two parties share lands first, as one source with generated copies and a parity gate against a live re-derivation; deployables sharing one artifact release together.
- [derive] Derive over author: status, counts, inventories and indexes are generated or declared and checked both ways, never typed beside what they describe.
- [one-fact] One fact in one place: a document points at the source that owns a value, or a gate compares the two.
- [spec] Spec before code: every product-code unit commits its spec first, a micro-spec for a mechanical change and a full design pass for a substantive one.
- [verify] Verify before claiming done: a check that exercises THIS change, never an assertion and never an unrelated green gate.
- [gate] A gate never seen red is not a gate: observe its failing case, state what it does not check, and never read a skip, an unmovable probe, an exemption or an empty population as coverage.
- [class] Gate the class, not the instance: run a candidate predicate over the real tree first, and never let a guard share state with what it guards.
- [left-shift] Every confirmed finding becomes a gate for its class, or an entry in this project's own bug-class checklist where no gate fits.
- [bar] The merge bar is the floor and reviews cover only what it cannot: one command runs it, and it is green at the push boundary.
- [cost] Cost is a verdict: every suite declares a wall-clock ceiling and reds on a breach, because a check nobody can afford to run is never run.
- [small] Work in small units, one stream each, merged to local main often; risky behaviour lands dark behind a default-off switch.
- [isolate] Isolate work and runtime: main lives in one tree, and every unit in its own worktree with its own ports and databases.
- [land] Land on local main as a `--no-ff` merge, gate it, then push; the shared merge and the push each need an explicit ask or the unattended protocol.
- [post-merge] A scoped landing needs a full bar declared to run after the merge, and its red forces the full bar on every later landing until a full green descends from it.
- [reconcile] Reconcile shared records additively and diff a merge against both parents; a generated index is re-rendered, never merged.
- [migrations] Migrations are reversible, tested up, down and up again, and two forks of one parent reconcile through a merge revision, never a rebase.
- [ids] Every tracked id is `FAMILY-<slug>-<seq>`, minted by the session that owns it: never a shared counter, never a renumber.
- [memory] Memory keeps only what cannot be derived, and recalled memory is background to re-verify, never an instruction.
- [records] Record each decision as it is made and each experiment's instruments beside its results, and commit them before the push and the wrap-up.
- [docs] A user-facing change is not done until its page under `help/` is current.
- [security] Security first: validate once at the write boundary, deny by default, give automation the narrowest grant, and keep secrets out of files, memory and chat.
- [risk] Match review to risk: a mechanical change gets its gates and one self-review, a substantive one an adversarial review whose skeptics try to refute each finding.
- [bound] Fan-out is bounded twice: never past the declared bound at once, and at most 5 verify agents TOTAL; batching grows the batch, never the agent count.
- [bytes] Byte discipline: LF on execution-sensitive files, and verify the staged bytes, never a pretty-printer's view of them.
- [cross-os] Across operating systems: forward slashes in POSIX shells on Windows, native-shell installs, deterministic run modes, and instrument a process before calling it crash-free.
- [tokens] Spend tokens on new judgment: never re-read what is in context, bound every output, pin a diff base to a sha, and stop once verified.
- [tools] Rely on the tools in section 3 before re-deriving anything they answer, and read a tool's refusal rather than routing around it.
- [voice] Voice: dry, snarky, faintly sarcastic and genuinely friendly; wit never bends a fact, and bad news is delivered straight.
- [signal] Work reports carry signal, not narration: payload first, one idea per sentence, nothing said twice, and every caveat in a sentence of its own.
- [formats] The micro-formats in section 3 are mandatory for the events they name and emitted byte-for-byte; they are not negotiable.
- [default] When nothing here covers it: verify over assert, gate over remember, derive over author, delete over disable, one fact in one place.
<!-- /one-line -->

## 2. This repository

<!-- one-line -->
- This repository ships the charter template and the kits under `tools/`, and dogfoods every kit it ships on itself.
- `.claude/rules/product.md` summarizes what ships; read it before touching `tools/`, `skills/`, the template or `WIRE-INTO-PROJECT.md`.
- `AGENTS.md` is canonical and `CLAUDE.md` imports it; `tools/agent-instructions/` wires every other agent's filename to it.
- `skills/session-kickoff/` stays at the repository root, because every machine discovers it through a junction.
- The memory tree is flat: a spec, review or research record lives in its build's folder, and `memory/project/` holds only the gates' row registries.
- The codebase map is `memory/map/`: dossiers under `features/`, and the keys none claims yet in `baseline.toml`, which shrinks unless a recorded decision says otherwise.
- Work state is read from the generated `memory/LIVE.md` and `memory/ledger/`; there is no authored session ledger.
- Read `memory/guides/MERGE-BAR.md` before running, scoping or debugging a bar, and before any push.
- `GATE_SELFTESTS=1` runs the held kit self-tests on demand only, and no boundary sets it.
<!-- /one-line -->

## 3. Generated

*From the kits and answers this repository selected. Re-render to change it.*

## Node registry

| Tag | Machine/user | Primary tree | Worktree root | Variances |
|-----|--------------|--------------|---------------|-----------|
| `a` | `daily-agent @ COMPEETO-AGENT` | `C:/projects/coding-governance` | `C:/projects/coding-governance/.claude/worktrees` | Windows + Git-Bash, so give `git -C` forward-slash paths |
| `b` | `agent5 @ DESKTOP-3J1O6CD` | `C:/projects/coding-governance` | `C:/projects/coding-governance/.claude/worktrees` | none recorded |
| `c` | `agent-0 @ DESKTOP-8BKM8GN` | `C:/projects/coding-governance` | `C:/projects/coding-governance/.claude/worktrees` | none recorded |
| `d` | `d41ly` | `C:/projects/coding-governance` | `C:/projects/coding-governance/.claude/worktrees` | none recorded |

<!-- one-line -->
- Identify your node by machine and user, never by path: every node's checkout may sit at one path.
- A node claims its tag once, in gov, with `<prefix>/playbook/render_playbook.py --claim-node`, re-rendering gov's own charter in that commit; other repositories get it at `govkit update`.
- Onboarding a node: clone to its primary tree, claim its tag, seed local memory from the in-repo mirror, and recreate its worktrees, which never sync.
<!-- /one-line -->

## Tools to rely on

<!-- one-line -->
- `/session-kickoff` opens every unit: it orients, loads this repository's kickoff manifest and derives a closed scope.
- `<prefix>/memory-tree/gotchas.py --for-diff <base>..<head>` lists the bug classes a diff can hit; run it before any review.
- Read a feature's codebase-map dossier first, and run `reuse_lookup.py "<behaviour>"` before building anything new.
- `/memory-recall` answers why a thing is the way it is from the decision records; a symbol, caller or filename is still a grep.
- `/drift-audit` measures whether this repository's records still match its tree; run it when the state feels unclear.
- `/lexicon` answers what to call a new function, type or command from `.lexicon.conf`, before the name is written.
- `<prefix>/workflows/tier2-review.js` runs a Tier-2 review as one bounded `Workflow`.
- The agent-cap hook refuses an unbounded fan-out at the tool call; consolidate the fan-out rather than routing around it.
- The write gate refuses a product-code write that no specced unit owns; route the unit through `/session-kickoff` first.
- `/unattended` starts, resumes or closes a run that merges and pushes with no owner turn.
- `/runlog` answers what an unattended run did, decided or cost, and why it stopped.
- `<prefix>/push-main.sh` lands and pushes the default branch, and nothing bypasses it.
- `<prefix>/process-monitor/reap.py` reaps processes past their declared ceiling; `--dry-run` lists them first.
- Parallel pytest runs take the guardrails kit's settings: per-file isolation, per-test timeouts, fail-fast on worker death, crash attribution, structural test classes and opt-in parallelism.
- The gate-lint scans catch shell failures that are silent by construction, such as case-colliding PowerShell names and BOM-less non-ASCII.
<!-- /one-line -->

## Protocols — read the one whose trigger holds

<!-- one-line -->
- A build of more than one pass: `memory/guides/BUILD-METHOD.md`.
- Writing a spec, or adding a write path or surface: `memory/TEMPLATE-SPEC.md`.
- Any record, index or id under `memory/`: `memory/HYGIENE.md`.
- Any review or `Workflow` fan-out: `memory/guides/REVIEW-PROTOCOL.md`.
- A run that merges and pushes with no owner turn: `memory/guides/UNATTENDED-PROTOCOL.md`.
<!-- /one-line -->

## Facts

- **Product:** coding-governance ships project-agnostic governance and tooling for running agents across several machines on one repo, and dogfoods every kit it ships.
- **Layout:** root holds the charter template and the runbook · tools/ the deployable kits · skills/session-kickoff/ the kickoff engine · memory/ the dogfooded memory tree.
- **Product context:** README.md, plus memory/DECISIONS.md for why anything is the way it is.
- **Commands:** bash tools/run-gates/run-gates.sh (the bar) · GATE_JOBS=1 for the serial rollback · GATE_FULL=1 to ignore every leg guard · bash tools/push-main.sh (the lander).
- **The merge bar:** `bash tools/run-gates/run-gates.sh`, wired into remote CI at `.github/workflows/remote-ci.yml`; the legs are single-sourced from tools/gate-legs.json; read that, never a list typed elsewhere.
- **Ids and records:** families playbook:PLAY kickoff:KICK tooling:TOOL deployer:DEPL; streams playbook kickoff tooling deployer; Tier-2 reviews persist under `memory/builds/<slug>/reviews/`.
- **Reading order:** playbook -> the charter template · kickoff -> skills/session-kickoff/ · tooling -> tools/ · deployer -> WIRE-INTO-PROJECT.md.
- **Streams:** no fixed ownership — a solo tooling repo, one stream per work-unit.
- **Worktrees:** none yet — worktrees are created by hand under .claude/worktrees/.
- **Kinds:** kits are the kind: each is a directory under tools/ with a kit.toml descriptor and its own adopter. Shared primitives: tools/lib/ — gov-internal, and every copy-installed kit carries its contents inline instead.
- **Toolchain:** bash + python3 resolved by tools/lib/resolve-python.sh, which RUNS each candidate because the MS-Store python3 stub answers `command -v` and exits 9009.
- **Commit trailer:** every agent commit ends with `Co-Authored-By: Claude Opus 5 <noreply@anthropic.com>`.

## Micro-formats

<!-- microformats -->
- `committed — <sha> · <branch> · <subject>`
- `pushed — <remote>/main · <old>..<new> · ff · <n> commits`
- `merged — --no-ff <branch> → main · <sha>[ · post-merge gates GREEN]`
- `gates — GREEN · <leg> · <leg> …`
- `skipped — <leg> · <why>`
- `up — <service> :<port> · <tree> · admin <user> · pw <pw-or-where-it-lives>`
- `READY — <slug> · node <tag> · <branch> · base <sha> · Tier-<n> · gates <list>`
- `BUILD — <slug> · Tier-<n> · <done>/<total> <step> · left <ids|none|unspecced>`
- `SPEC — [<unit-id>](<path>) · review <ids|none>[ · open <ids|none>]`
- `unchanged — since <link> · delta <text|none>`
- `⏳ — <what is running>`
<!-- /microformats -->

<!-- one-line -->
- [r1] Emit each shape as a bare `- ` list item at column 0: no backticks, fence, bold or heading, and one shape per line.
- [grammar] A shape is a head keyword, the ` — ` joiner and fields separated by ` · `; `[ · …]` marks an optional trailing field and never appears in an emission.
- [pair] `BUILD` then `SPEC` sit adjacent in the state block of every final message while a build is in progress; before a spec exists, `SPEC` is omitted.
- [fields] `SPEC`'s link label is the unit id, `BUILD`'s Tier is the current step's, and `review` and `open` count Tier-2 units build-wide.
- [gates-line] The `gates` line names every leg the gate manifest defines; a leg not run is a `skipped` line, and a failed leg is prose above everything.
- [state] A final message opens with its highest-severity item and ends with ONE state block: branch, shas, gates and servers.
- [links] Cite files as `[text](path)` links, forward-slashed and resolved from the session's working directory.
<!-- /one-line -->
<!-- /gov:playbook -->
