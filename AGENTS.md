# coding-governance — working guide

Project-agnostic governance + tooling for running Claude Code (or any agent) across several
machines/sessions on one repo. This repo **dogfoods its own kits**: it runs the memory-tree hygiene
gate, the kickoff-manifest ratchet, the template size gate, and the codebase-map coverage gate on
itself. The map lives at `memory/map/`; its dossiers are the files under `memory/map/features/`, and the
keys not yet claimed by one are in the `baseline.toml`, which shrinks except where a recorded
decision says otherwise (`TOOL-aSiftedPlaybook-1` swapped one key in place; see the file's header). Both counts move as dossiers
land, so neither is spelled here — `python tools/codebase-map/reuse_lookup.py` prints the live pair.

*(Read by every AI tool: `AGENTS.md` is canonical; `CLAUDE.md` is a `@AGENTS.md` import — Claude Code
doesn't read AGENTS.md natively. Wired by `tools/agent-instructions/`.)*

## What ships here (the product)

- **`coding-governance-agents.template.md`** — the governance playbook template (the operating
  ruleset; **≤48 KiB, gated** by `tools/check-template-size.sh`, which also prices every growth
  against a recorded high-water — prefer externalizing to spending the headroom). **ONE file as of
  v3.0**: the activity-scoped checklists that used to sit in a prose companion converged into the
  charter, and the deploy-time placeholder catalog became a program — `tools/playbook/`, whose
  renderer fills every placeholder from the target's `deploy.toml` and drops the `kit:`/`when:`
  conditional blocks that target has no kit for.
- **`skills/session-kickoff/`** — the `/session-kickoff` engine + `MANIFEST-TEMPLATE.md` + the
  ratchet gate `manifest-check.sh` (+ its test). Installed per-machine via a junction (not in-repo).
- **`tools/`** — `lib/resolve-python.sh` (the one python-launcher resolver: it RUNS the candidate,
  because the MS-Store `python3` stub answers `command -v` and exits 9009) plus the copy-in kits:
  `memory-tree/`, `memory-recall/` (offline conf-driven retrieval
  over the memory tree + the rendered recall Skill and its opt-in `recall-opened` hook),
  `codebase-map/`, `drift-audit/` (does this repo's own RECORD of its state still match reality —
  stdlib+git, seconds, no agents; every signal carries a liveness assertion so a probe
  that cannot move prints DEAD PROBE instead of a reassuring 0), `hooks/agent-cap.js` (the fan-out guard: raw-primitive ban + the verifier-arity rule it resolves),
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

- Root: `README.md`, this charter, `WIRE-INTO-PROJECT.md`, the product template (one file).
- `tools/` — the deployable kits (copied into target repos).
- `skills/session-kickoff/` — the kickoff skill (stays at repo root for machine-junction discovery).
- `memory/` — this repo's dogfooded memory tree, FLAT: `README.md` · append-only `DECISIONS.md` ·
  `HYGIENE.md` · `TEMPLATE-SPEC.md` · the GENERATED `LIVE.md` + `ledger/<month>.md` ·
  `backlog/<FAMILY>.md` · `builds/<slug>/` · `gotchas/` · `guides/` · `map/` · `archive/` ·
  `project/` (the gate's `*.txt` waiver registries and nothing else). Specs, reports, research
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

<!-- gov:playbook -->
# Coding Governance — the agent charter template

*Template **v3.0** · 2026-08-18. One file. One line per directive, and a wrapped line is still one
rule. This file BECOMES a project's `AGENTS.md`: `tools/playbook/adopt-playbook.sh` fills every
placeholder and drops the blocks a target has no kit for, so filling it is a program's job and not a
reader's — see `WIRE-INTO-PROJECT.md` for what a program cannot decide. History lives in the
`…-v-N-N.md` snapshots and in git.*

<!-- governance-template: v3.0 -->

> **What:** a project-agnostic charter for running Claude Code (or any agent) across several
> machines/sessions ("nodes") on one repo. **Use:** deploy it with the renderer; the rules are
> agent-facing imperatives and are kept verbatim.

## §0 — TL;DR (the load-bearing rules)

- **Session-scope every new ID** (slug = node tag + CamelCase adjective-noun) — collisions become impossible, not avoided (§2).
- **Own streams, not files; merge small and often** to local `main` (§3) — and isolate *runtimes* too: ports/DBs per session (§4).
- **Memory holds only the non-derivable**; status is DERIVED, no shared mutable index, no per-node shard (§5).
- **Gates are the merge bar; reviews cover what gates can't**; every confirmed finding becomes a gate or a documented check (§7, §8).
- **Never more than the declared bound at once, AND never more than the declared total per verify
  stage** — two rules, not one: concurrency bounds how many run together, the total bounds how many exist. Batching grows the batch, never the agent count. A wide burst trips the server rate limiter (§8, enforced by the `agent-cap` hook, which counts direct spawns too).
- **Verify before claiming done** — a check that exercises the change, never an assertion (§4, §8).
- **Consistency by construction**: build tokens, primitives, and factories *before* the screens/features that use them (§12, §13).
- **Chat carries signal, not narration**: payload first, one line per mechanical event, facts outrank format (§16).
- **When no rule below covers it**, decide by these: verify over assert, gate over remember, derive over author, delete over disable, one fact in one place.

## §1 — Work-unit lifecycle (start → done → land)

Keep units small: one stream/owner, no cross-stream contract change, reviewable as one Tier-1 diff — else split.

**Definition of Ready — run before touching code:**
- Sync: `fetch` + fast-forward local `main` (another node may be ahead); recreate/repair your worktree if needed (§3).
- Locate: read your stream's decision log + backlog (§6) and the derived work-state index (§5); confirm your node tag (§2).
- Scope: clear acceptance criteria, one stream, small, gates named — if you can't state those, split or clarify first.
- Reserve: at your session's first work-unit, mint + grep-check a session slug (§2) and open the unit's record (§6).
- Large new feature (a Tier-2 change): the DoR *is* a design pass — a written spec (goal · scope · non-goals · acceptance) + a bounded production-readiness menu (best-practice implementation, the extra tools it needs, and the cross-cutting concerns: security · perf/scale · a11y · i18n · error/empty/loading states · observability · testing/gates · migration/rollback · `help/` docs). Spec shape: the memory-kit `TEMPLATE-SPEC.md` (check 12).
- Surface that menu and **get scope approval BEFORE building** (a menu to select from, not scope-creep licence); record the agreed spec per §6.
- Codebase map adopted (§5)? A design pass touching an UNDOSSIERED feature creates/refreshes that dossier as a DoR item (the pass already reads what the dossier needs) — the map's convergence forcing function.

**Definition of Done — before you call it done:**
- Gates green (§7); the change verified by a check that exercises it (§8), not asserted.
- Every confirmed finding left-shifted: a regression gate, or a §10 checklist entry if its class can't be gated (§7).
- User-facing change → its `help/` page created/updated (§5).
- Codebase map adopted (§5)? New inventory keys claimed in the map tree (machine-enforced); dossier prose refreshed on touch; claim edits regen the generated artifacts in the same commit.
- Memory (non-derivable only), decision log/backlog, and the unit's own record updated — **committed before the push and the wrap-up message** (§16).
- Kickoff manifest (when the project keeps one) updated if this unit changed what it front-loads — a gate command, entrypoint, governing doc, layout/branch convention, a trap hit, a doc/memory claim found stale, or a fact re-derived that it should have front-loaded — re-stamp `last-audit` with a delta line in the commit message; no delta → no touch.

**Landing — merge protocol:**
- Land on local `main` first, verify, then push; the merge to shared `main` and the push each need an explicit ask.
- That explicit ask has ONE substitute: a committed build folder the run did not create, whose shape your merge bar validates. The mandate is ASSERTED, never written by the run that uses it, and must be reachable from a BASE observed on the remote rather than read from a local ref. A run with full shell access can still defeat that, and the control that actually binds lives on the remote.
- After each merge run a diff-scoped gate (a conflict-free merge is not a passing merge); the FULL bar runs ONCE, at the push boundary.
- Reconcile shared mutable files (backlogs, indexes) additively, never pick-a-side; diff the merge against BOTH parents (the "auto-took" class, §10). A GENERATED index is never reconciled — re-render it (§5).
- Land risky behavior dark: Tier-2 ships behind a default-OFF flag or as inert defaulted data, flipped on only after in-place verification — merges without endangering other nodes, reverts cleanly.
- Migrations are reversible — test up/down/up.

*Two independent blocks. The first applies whenever the project keeps a kickoff manifest. The second
applies only when the project adopts the unattended-run kit — drop it otherwise.*

**Kickoff-manifest merge exception.**

- The manifest reconciles additively EXCEPT its `last-audit` line — resolve a stamp conflict either way provisionally, complete the merge, then re-verify §B against the merged tree and re-stamp in a follow-up commit that supersedes both sides (post-merge HEAD on the default branch, the merge-base otherwise; a commit can't embed its own sha); the same post-merge fresh audit closes any merge that brought in watch-touching commits.

**Unattended runs** *(kit-conditional — drop this block if the project does not adopt the unattended-run kit).*

- The contract is `memory/guides/UNATTENDED-PROTOCOL.md`, installed by the kit: the committed
  build folder as the authorization and its provenance properties, the run-state file's generated and
  authored halves, the phase vocabulary and its witnesses, the Definition of Done and its override,
  the keepalive split by actor, the default directive set and its named waiver, and the landing rule.
  It is NOT paraphrased here — a paraphrase and its source are two answers to one question, and the
  paraphrase is the copy that rots.

## §2 — Nodes, identity & IDs

- Register every node once, in-repo — tag · machine/user · primary tree · worktree root · **per-node variances** (remote name, harness launch config, credential quirks like an elevated scope for CI-config pushes):

  | Tag | Machine/user | Primary tree (`main` lives here) | Worktree root | Variances |
  |-----|--------------|----------------------------------|---------------|-----------|
  | `a` | `daily-agent` | `C:/projects/coding-governance` | `C:/projects/coding-governance/.claude/worktrees` | remote `origin`; Windows + Git-Bash, so give `git -C` forward-slash paths |

- Identify your node by machine/user, never by filesystem path — roots can be identical across machines.
- A new node claims the lowest free one-letter lowercase tag and adds its row in the same commit.
- New-node onboarding: clone to the pinned primary tree · claim the tag (same commit) · seed local memory from the in-repo mirror (§5) · recreate stream worktrees (they never sync, §3).
- Every new tracked id (decisions, backlog, tickets — anything `FAMILY-NNN`-shaped): `FAMILY-<slug>-<seq>`, owned by the minting session so nothing it numbers can be contested.
- Slug = your node tag + a fresh CamelCase adjective-noun (`dAvengingTrousers`), `[A-Za-z]` only, minted ONCE per session; the tag's first letter makes cross-node slugs disjoint by construction.
- `<seq>` = plain 1-up per (session, family), unpadded; ids are labels, not ranks; next = numeric max of YOUR ids in that family + 1; carry your per-family high-water in session state (uncommitted ids are invisible to grep).
- Before committing to a slug: (1) all-time grep the governance-docs tree (logs, backlogs, build records) for `[A-Z]+-<slug>-[0-9]` — re-roll on ANY hit (a rotated or archived record still owns its ids); (2) scan the live rows of the work-state index (§5) — re-roll on a clash.
- No reserve-above-a-marker, no shared counter, no renumber-on-merge — the slug is the guarantee.
- A session = one continuous effort under one slug (several work-units/families, one `<seq>` each); a resumed/summarized session keeps its slug (grepping only your own prior ids is not a collision).
- Fan-out children (sub-agents/orchestrated workers) never mint ids — the orchestrator does; a child that must mint takes its own registered slug.
- Residual tie-break (sub-1%): the later-to-merge re-mints its slug for all UNMERGED ids; an already-merged id wins.
- Legacy id eras are FROZEN: cite verbatim, never renumber, never mint in a pre-rule format, never bump a residual "next free id" marker.
- Shorthand (family+seq, slug elided) is sanctioned ONLY in session prose — never where ids are the permanent record (it's shape-identical to frozen legacy ids).

## §3 — Parallel work: streams, worktrees, trunk

- Own streams, not files: `no fixed ownership — a solo tooling repo, one stream per work-unit`. Overlap on shared files (API clients, config, indexes) breeds collisions and integration reviews — minimize it.
- Trunk-based: merge small and often to LOCAL `main`; long-lived branches mean bigger reconciles and review surface.
- `main` stays checked out in exactly ONE tree (the primary); feature work happens ONLY in sibling worktrees — parking `main` on a feature branch strands it and is the root cause of concurrent-session collisions.
- Machine-enforce the branch rule: a tracked pre-commit hook refuses primary-tree commits off `main`, wired per node by an install script; a session-start check flags the contested state; `--no-verify` is the deliberate bypass.
- Doc-only commits go directly on local `main` only while the primary tree is on `main` and idle; a busy tree (dirty, mid-merge, another session) routes through a worktree.
- Bootstrap worktrees with one script (`none yet — worktrees are created by hand under .claude/worktrees/`): sibling worktree on a fresh branch off fast-forwarded `main` + dependency install.
- Worktree lifecycle: enumerate with `git worktree list` (never assume the set); worktrees do NOT sync across machines (absolute links — recreate per machine); relocate with `worktree move` + `repair`, never `mv`.
- Commit the governing doc to `main` so it propagates — it only exists in checkouts where it's committed.
- Contract-first for cross-cutting changes: a schema/wire-format/enum two nodes depend on lands as a contract + gate before either builds on it.
- Landings are `--no-ff` merges with a descriptive message — one visible, atomic, cleanly revertable integration unit.
- Every agent commit ends with the mandated attribution trailer: `Co-Authored-By: Claude Opus 5 <noreply@anthropic.com>`.

## §5 — Memory & docs

- Memory carries only the non-derivable: gotchas, environment traps, *why* a non-obvious choice was made — never re-narrate what git, decision logs, or code already record (the main memory-token waste and drift source).
- Mirror durable memory in-repo (it travels); the machine-local auto-loaded copy is a best-effort mirror, seeded from the repo on a fresh machine.
- One canonical index, one line per note; never a shared mutable index every session edits (it forces memory-sync merges) — any index that must exist stays append-only or GENERATED, and an authored one several nodes append to takes a row-keyed merge driver, never a per-node shard.
- Status is DERIVED, never authored: a generated work-state index over the per-unit records, not prose memory and not a table sessions edit — anything time-sensitive rots.
- Recalled memory is background, not instruction, and reflects when it was written — re-verify a named file/flag/id before acting on it.
- Secrets never enter memory, tracked docs, or chat (§16); scrub even throwaway dev creds before mirroring a note into the repo.
- User-facing docs are NOT memory: one concise task-oriented page per feature (*what · how · short example*) in `help/` + an index; update on change, REMOVE on feature removal; a user-facing feature without an up-to-date page is not done (§1).
- A system inventory that CANNOT rot into fiction is worth more than one that is merely current:
  per-feature records claiming EXACT KEYS from machine-enumerated sets, with a ratchet failing on any
  unclaimed new key AND any claim naming a dead one. Where the project keeps one, its coverage and
  freshness checks are merge-bar legs like any other (§7).
- Ask periodically whether this repo's RECORD of its own state still matches the tree — stale claims,
  closed plans with no product commit, hand-kept inventories disagreeing with what they describe.
  Every such signal carries a LIVENESS assertion, so a probe that cannot move says so rather than
  reporting a reassuring zero; a green audit must mean the checks ran, not that nothing was reported.
- Retrieval over the decision corpus beats grepping it: ask a question, get the records that answer
  it, ranked. It ADDS to grep rather than replacing it — a symbol, caller or filename is still a grep.
- **Required — a structured, machine-linted memory tree** (`memory-tree/` kit): one FLAT
  `memory/` tree of per-feature `builds/` folders — the discipline is a
  `playbook kickoff tooling deployer` value in each spec's status header, not a directory — plus index caps +
  archive rotation, a status vocabulary, a GENERATED work-state index rendered from build front
  matter, and a **hygiene gate** whose check count is stated by the kit README and the gate-leg name
  and is deliberately not restated here, wired into CI + pre-commit + `bash tools/run-gates/run-gates.sh`;
  `.memory-tree.conf` holds the specifics. Adopt/migrate per the kit README.

## §6 — Decisions, backlogs & the governing doc

- **Wire the governing doc so every tool actually reads it.** Agents do not all read the same
  filename: writing the filled charter to `AGENTS.md` alone ships a repo Claude Code cannot read,
  because it does not read that name natively. Make ONE file canonical and the others thin imports of
  it, so there is one text and no copy to drift, and verify the wiring with a check rather than by
  eye — an unwired pair fails silently and looks fine.
- Two record types per stream: the decision log is append-only (never rewrite a ratified record — supersede with a new id + note); the backlog is mutable (stable ids, status updated in place; gaps fine).
- Per-stream id families (`playbook:PLAY kickoff:KICK tooling:TOOL deployer:DEPL`): the family prefix routes an id to its log/backlog; allocation is slug-scoped (§2), so no shared "next free id" marker exists.
- Record real decisions as you make them — future sessions and nodes rely on these being current.
- Session-start reading order: ALWAYS load the master decision index first, then the stream logs for the area touched — routed by `playbook -> the charter template · kickoff -> skills/session-kickoff/ · tooling -> tools/ · deployer -> WIRE-INTO-PROJECT.md` (work-area → doc tree → id families → backlog).
- Logs are two-tier for token scoping: a one-line-per-decision index pointing at per-decision detail files; open details only for the areas you touch.
- The instantiated doc opens with a compact product-identity preamble for `coding-governance` (`coding-governance ships project-agnostic governance and tooling for running agents across several machines on one repo, and dogfoods every kit it ships`: what the software is, deployment model, major runtime pieces).
- The instantiated doc carries the repo-layout map (`root holds the charter template and the runbook · tools/ the deployable kits · skills/session-kickoff/ the kickoff engine · memory/ the dogfooded memory tree`: each top-level dir + its role and the core/adapter relationships) — sessions never re-derive where things live.
- The instantiated doc carries the everyday-command catalog (`bash tools/run-gates/run-gates.sh (the bar) · GATE_JOBS=1 for the serial rollback · GATE_FULL=1 to ignore every leg guard · bash tools/push-main.sh (the lander)`: install, dev servers, migrations, artifact regeneration, seeding, the one formatter/linter per language) — sessions never re-derive the one-true invocation.
- Pin one in-repo home for business/product context (`README.md, plus memory/DECISIONS.md for why anything is the way it is`: brand, positioning, specs) so sessions locate it instead of asking.
- A value stated in prose beside the source that OWNS it rots between changes — point at the source,
  or gate the pair. This is the same rule as "derive over author", applied to documents rather than
  to code, and it is the one most often broken by the document that states it.
- In-doc paths are repo-root-relative; the root is pinned once per node in the §2 registry, never re-derived. (User-facing links follow §17, a different convention.)
- Non-obvious rules carry provenance inline (the motivating decision/incident id); environment/capability claims carry a verified-(date, node) stamp.
- Each guarded security surface keeps a written security-model section in the decision log; read it BEFORE extending that surface (§9).

## §7 — Quality gates = the merge bar

- A parallel test runner needs its own guardrails: a per-test timeout AND fail-fast on worker death
  AND a pre-kill stack dump, because a distribution-layer deadlock is a mode no per-test timeout can
  reach. A crashed worker must be ATTRIBUTED to the test that caused it, or it reports as an
  anonymous session failure naming nothing.
- Scan any shell language whose failures are SILENT for the classes that cause them — for PowerShell,
  case-only identifier collisions (its variable names are case-INSENSITIVE) and BOM-less non-ASCII
  (5.1 decodes CP1252, so an em dash closes a string early). Byte-level, because every text-mode read
  hides the second. A repo with no such files gets a clean report that proves nothing, which is
  honest and is why the scan is adopted only where the language exists.
- Deploy your own tooling as a DECLARED population, never a directory listing: a registry plus a
  descriptor each, asserted against the tracked surface in both directions — a new moving part reds
  until a declaration claims it, and an exemption naming a path that no longer exists reds too,
  because a stale one silently widens the surface it was written to narrow.
- Keep the automated suite green at the push boundary: `bash tools/run-gates/run-gates.sh — the legs are single-sourced from tools/gate-legs.json; read that, never a list typed elsewhere` (typecheck/compile · lint · test · generated-artifact freshness · structural invariants). Gates are the quality floor; reviews cover only what gates can't.
- Wire the suite into remote CI as machine-required checks (`none yet — the bar runs at the push boundary via .githooks/pre-push`) — convention is not enforcement.
- Provide one command that runs the whole local bar with legs concurrent, wall ≈ longest leg: `bash tools/run-gates/run-gates.sh`.
- A slow leg may have a sanctioned faster local variant — document the equivalence explicitly (which local run satisfies which CI leg), so local verification is fast AND unambiguous.
- Single source of truth → generated artifacts → parity gate, for every contract duplicated across languages/layers; a new shared contract gets ONE source, generation, and a drift test — never a hand-kept second copy.
- Lockstep invariants get a guard (migration single-head, stale manifest, schema↔validator skew) — a gate, not memory.
- A gate's OWN header states what it does NOT check. A structural check reads as a semantic one to
  everybody who did not write it, and the resulting false confidence is worse than the gap.
- A probe that cannot move says so. A signal with no liveness assertion reports a reassuring zero
  when it is broken, which is indistinguishable from a clean run and is how a green bar stops meaning
  anything.
- NO count of a derived population is written in prose. The checker derives every figure it reports;
  a number typed beside the thing it counts is wrong on the next commit and nobody notices.
- Left-shift every confirmed finding: not done until a regression test covers its CLASS, or (if ungateable) it joins §10 as a documented check — this is how review cost trends down.
- Guard against green-by-absence: every test/typecheck glob spans ALL real file classes (beware glob dialects that don't brace-expand), and a collection gate asserts every test file contributes ≥1 collected item — a de-collected file can't fail.
- Codebase map adopted (§5)? Its coverage + freshness tests are merge-bar legs like any other — never exempt them to "unblock" a landing (claiming the key IS the unblock).
- Classify special-execution tests STRUCTURALLY: a collection hook auto-marks by fixture/dependency so a new test can't forget its class, and the default environment can't silently switch engines.
- Parallel test runs preserve per-file isolation (file-level distribution, not per-test); parallelism is opt-in; small selections run serially (worker startup makes them a net loss).
- Document deliberate gate exemptions together with their compensating manual check — an exemption is not coverage.
- Concurrent migration forks (two branches, same parent) reconcile via a merge revision, never a rebase; know whether the local harness can even see a fork (often only the head-count gate does).
- A generated contract artifact baked into multiple deployables couples their releases: those artifacts deploy TOGETHER, and a contract change may couple a frontend release to a data migration.

Ported from a session where six of seventeen review findings were the same defect: a gate satisfied
by its own comment prose, an arm reporting `ok` on a path it never took, a predicate that never
matched its target population.

- **A new gate is not landed until its failing case has been observed.** Stage the break, confirm
  RED, unstage. A gate you have only ever seen pass is an assertion about nothing.
- **A guard that shares a variable with the thing it guards is not a guard.** A backstop that reads
  the same state the bug corrupts is disabled by the bug it exists to catch.
- **Run a candidate gate predicate over the real tree before wiring it**, and print hits AND
  near-misses. Doing so routinely surfaces live instances the original symptom never reached — and
  catches a predicate that would red innocent files.
- **A skip must announce itself.** A skip that looks like a pass is indistinguishable from coverage.
  State which arm went unexercised and why, so a green row is never misread as a verified one.
- **Gate the CLASS, not the instance.** Fixing one file and scanning only that file certifies
  coverage you do not have — the same could-not-fail shape, one level up.

## §8 — Review protocol (match intensity to risk; verify, don't assert)

- Tier 1 — mechanical/additive (no new write path, migration, auth/sanitization/egress surface, or shared-contract change): gates + one focused self-review of the diff. NO multi-agent review.
- Tier 2 — substantive (any of the above, or a cross-stream merge): adversarial find → verify → synthesize, running the §10 checklist as part of it.
- Scope Tier-2 to the diff at an immutable SHA plus its immediate callers/callees, reviewed at the integration boundary ONCE (the cumulative diff landing on `main`) — per-increment reviews re-scan overlapping code.
- Default Tier-2 shape (ROI-tuned): a parallel fan of 3–6 primed finder lenses (security · correctness · data-integrity · dead-code · integration-seams) → a skeptic prompted to REFUTE each finding → one synthesis pass; drop any finding a skeptic refutes unless reachability + impact re-established.
- **CONCURRENCY IS CAPPED, ALWAYS, and the verify-stage TOTAL is capped too — two rules, not one.**
  A wide fan trips the SERVER rate limiter and kills whole phases for millions of tokens; a
  harness auto-cap does NOT protect you. Concurrency bounds how many run together; the total
  bounds how many exist. **CONSOLIDATE before you fan out:** batching grows the batch, never the
  agent count — at most 5 verify agents TOTAL. Route Workflow fan-out through the bounded
  helpers, inlined because scripts cannot import: `boundedParallel(thunks, 5)` and its pipeline
  sibling. Enforce it mechanically at the tool call rather than inside the script, where no hook
  reaches — the `agent-cap` hook denies a raw primitive and any fan-out over a receiver it
  cannot PROVE bounded, and counts direct spawns, which is the only enforcement reaching a
  fan-out made outside a workflow script. It resolves a bound wherever it is written and denies
  any K it cannot resolve to an integer ≤5; an array LITERAL of ≤5 elements (the lens fan)
  passes unmarked, and it fires on matcher `Workflow|Agent`, the exact pair — `Workflow` alone
  leaves direct spawns unguarded. FIVE of these values are machine-compared against the sources
  that own them by `tools/check-playbook-parity.sh`; retyping one wrong reds the bar rather than
  drifting. The marker spellings and the full resolvable-bound grammar are the hook's own, in
  `tools/hooks/README.md`; a ready harness ships beside it.
- Finders emit CONCRETE findings — `file:line` + repro/impact + proposed fix — so skeptics can actually verify them.
- Precision (confirmed/(confirmed+refuted)) is the #1 token lever — below ~0.5, tighten scope/priming before adding agents; scale a large fresh surface with LENSES (coverage), not skeptics; past ~25 agents returns diminish.
- Feed reviewers the security model, the already-tracked open issues, and what's by-design — so they hunt NEW issues, not re-report known ones.
- Match intensity to target richness: heavy multi-lens earns its tokens on fresh/complex write paths; over hardened code it manufactures refuted noise — review light or skip.
- Persist each Tier-2 run as an in-repo artifact folder (`memory/reviews/`); periodically re-audit the corpus (token cost vs severity-weighted confirmed-finding value) to retune these defaults.
- Orchestration scripts run in sidechains inheriting neither your hooks nor the governing doc, in a restricted runtime (plain JS — no type syntax, no imports) — inline the schema discipline as a snippet; the cap is enforced at the `Workflow` tool-call AND at the `Agent` one (both fire a main-loop `PreToolUse`), never inside the script, where no hook reaches.
- Verify before "done": a check that exercises THIS change (its own/affected test, the relevant gate, or the §4 harness) — an unrelated green gate is not proof; failures reported with output, skipped steps named.
- Commit freely as you go (branch/worktree, or local `main` for doc-only per §3); landing is §1's rule, not restated here.

- Structured-output schemas so a malformed return can't force full regeneration (top output-token
  waste): write a large body to a file and return `{path, summary}`, forward-slash paths (never
  hand-serialize JSON — unescaped backslashes are the top breaker); restate the required keys in EVERY
  loop iteration; accept-and-ignore stray keys unless a stray key is actually harmful; on a validation
  failure feed back only the offending field, never "regenerate everything".

## §9 — Security boundaries (apply to any new write path / surface)

- Sanitize untrusted input at the WRITE boundary, once; trust storage at render; re-check size/shape caps AFTER any transform that can grow content (sanitizers add attributes).
- ONE composite write-guard (scrub + capability gate + sanitize) on EVERY path that stores renderable/dangerous content — sibling write paths (templates, imports, saved/shared components) included; a bare or partial sanitizer on a sibling path is the recurring hole.
- Gate the most dangerous sanctioned content class behind an explicit per-principal permission at write time — a capability check distinct from, and additional to, sanitization.
- One canonical URL/href normalizer shared by client AND server: strip control/whitespace, fold `\`→`/`, reject protocol-relative (`//host`, `/\host`), deny dangerous schemes (`javascript:`/`data:`/`vbscript:`); divergence is a stored open-redirect; pin the evasions (`/\evil`, `\\evil`, control chars) in tests on both sides.
- SSRF-guard every outbound request: https-only, resolve to public IPs only, no redirect-following, signed payloads; the SAME guard on retry/queue paths, not just inline; blocking DNS/network resolution runs OFF the event loop (a hung nameserver must not freeze a worker).
- Authorization lives in the shared core (deny-by-default RBAC, defined as code) so every adapter — HTTP, RPC, CLI, AI tool — inherits it; a service fn reachable by a future adapter re-checks authz itself.
- AI/automation runs as a dedicated non-login service principal with a deliberately narrow grant — never a human/admin role; authority bounded by construction.
- Automation writes are draft-only by default; autonomous publish/irreversible action sits behind an explicit default-OFF gate — a standing blast-radius bound distinct from per-feature launch flags.
- Keep PII/secrets off the AI/automation surface structurally: payload/return types that CANNOT carry sensitive values (ids/counts/field-names only); audit value-bearing fields flowing to automated readers.
- Optimistic concurrency on full-document writes: a version/`updated_at` precondition → 409 on stale — else concurrent editors/nodes silently clobber each other.
- Document which production protections are deliberately OFF in the test env (CSRF, rate limits, …), confirm they default ON in production, and exercise each directly in a dedicated test.

## §10 — Recurring bug classes (run in every Tier-2 review)
- Every Tier-2 review runs the project's own recurring-bug-class checklist over the
  area the diff touches, and every confirmed finding is left-shifted — into a gate where one
  fits, or into that checklist where none does (§7, §8). A project with no such checklist
  keeps a documented manual one; the rule is that the classes are the PROJECT's, derived from
  its own failures, never a generic list carried in from somewhere else.

## §11 — Cross-OS & toolchain hygiene

- Force `LF` via `.gitattributes` on execution-sensitive filetypes (shell scripts, Dockerfiles, configs, env files, migration templates, runtime-read JSON) — a stray CR breaks shebangs, `sh -c`, servers, generated migrations.
- Verify the staged BYTES, not a pretty-printer: `git diff | cat -A` / `git cat-file -p <blob>`; `git show` and MSYS `grep` mislead on CRLF.
- Pin toolchain versions + the one-true way to run gates on each OS: `bash + python3 resolved by tools/lib/resolve-python.sh, which RUNS each candidate because the MS-Store python3 stub answers `command -v` and exits 9009` — no per-session re-derivation.
- Prefer deterministic run modes (no auto-reload) where a watcher can leave stale processes/ports squatting.
- POSIX-emulation shells on Windows (MSYS/Git-Bash/Cygwin) mangle backslash working-dir paths (`git -C C:\repo` → `fatal: cannot change to 'C:repo'`) — use forward-slash there; a zero-false-positive hook can block the broken form.
- Package installs run from a POSIX-emulation shell can create broken links in the dependency tree — if it looks wrong, reinstall from the native shell.
- Absence of crash evidence is only evidence where the reporter is on: parallel-test workers get fd 0/1 (Windows: fd 2 too) redirected to devnull, so banners and native tracebacks vanish; Windows Event Viewer records nothing when WER is disabled (`Disabled=1`), and an `os._exit` is not a fault so WER never records it anywhere — instrument the process itself (a probe log) before concluding "no crash".


## §12 — Architectural consistency (build-once, reuse-everywhere)

- Decide the extension pattern before the SECOND instance — so #3..#N are data + a few overrides, never new plumbing.
- A "kind" gets a factory/base, not copies: at instance #2, extract the shared contract into a definition helper/base — per-kind map: `kits are the kind: each is a directory under tools/ with a kit.toml descriptor and its own adopter`.
- One shared core, thin adapters: business logic + authorization in a single service core; HTTP/RPC/CLI/AI surfaces are thin adapters that cannot diverge (also how authz stays consistent, §9).
- Single source of truth → generated artifacts (§7): the catalog of a kind's instances generates the
  schema/validator/manifest/docs; adding an instance = one edit + a drift gate. When the ONLY consumer
  is same-language, prefer runtime-derivation over a committed artifact: derive the set live in the
  check (glob/scan or a co-located marker) and commit NOTHING — there is nothing to keep fresh and
  drift is structurally impossible; commit + parity-gate an artifact ONLY when a
  cross-language/cross-layer consumer must read it (that boundary is the artifact's whole
  justification), and make that parity gate compare the committed artifact against a LIVE
  re-derivation, never generated-vs-generated (§10).
- Promote shared widgets the instant two features need them, on a two-tier ladder: product-generic presentational primitives → the shared kit (`tools/lib/ — gov-internal, and every copy-installed kit carries its contents inline instead`); app-scoped shared widgets → that app's own kit; a feature re-implementing or re-styling a primitive locally is a smell.
- Forward-compatible data: new fields additive + defaulted (old content renders identically, new capability inert until used); shape changes ship an auto-upgrade step; prefer riding an existing shape over a migration.
- Reuse audit before building: grep for an existing component/util/endpoint to extend before adding one.
- Gate the layout conventions you can (naming, layer boundaries); the "where things live" map lives in the always-loaded doc (§6) so every feature has an obvious home.
*The five naming bullets below are kit-conditional — drop them if the project does not adopt the lexicon kit, the same way §1's unattended block is dropped. The rest of §12 is universal core.*

- **Naming is one of those conventions, and it is gateable.** Declare it in `.lexicon.conf`: a CLOSED verb table every function/method definition leads with, a banned type-suffix list, and forbidden import DIRECTIONS between layers (the machine-checkable form of "one shared core, thin adapters" above). A repo that declares none of these has a naming convention it asks people to remember.
- The verb table's value is NOT spelling — it is scoping. "Which verb is this?" is answerable only when a function does ONE thing, so a name that will not fit the table is reporting an unclear responsibility or a seam in the wrong place. If the reflex on a refusal is to add a verb, the table has become a synonym list and is buying nothing.
- Write the NEGATIVE definitions or do not bother: `build` not `create`, `load` not `fetch`, `remove` not `delete`, `set` not `update`. A row with only a positive gloss cannot tell two verbs apart, and the boundary is the whole product.
- DERIVE the initial table from the repo's own corpus, then FREEZE it and mark that a human curated it — a derived table nobody edited is a mirror of the code, which is the one shape a naming gate must not have (§7's rule against a gate whose vocabulary tracks its subject). Measure every offender pin against THIS corpus; a pin copied from a larger tree is either vacuous or permanently red.
- Declare a COVERAGE MODE per language — a real parser, a regex probe (incomplete by construction, and reported as such on every run), or explicitly dark. An undeclared language must be a named refusal, never a silent skip: a regex that quietly misses what it forgot looks exactly like coverage. An unarmed predicate REDS rather than passing green (§7).

## §14 — Session execution hygiene (per-call token discipline)

- Strategy: spend tokens on NEW judgment, never re-deriving the known — tier + diff-scope reviews (§8), gate over re-review (§7), lean memory (§5), streams + small merges (§3), system-first UI (§12, §13); **stop once verified** (re-reads, uncapped output, hand-polling, and edit/format ordering are the dominant avoidable spend).
- Don't re-fetch what's in context: no re-Read to keep editing a file or to "verify" an edit the tool confirmed; slice large files (range/grep), never whole re-reads; never re-read a command-output spill or large artifact — filter it at generation.
- Re-Read ONLY when something outside your edits changed the file (formatter/`--fix`, format-on-save, a concurrent node on a shared doc); make manual edits FIRST and format LAST — reformatting between edits forces the modified-since-read re-read loop; batch a file's edits.
- Bound every command's output (it all lands in the transcript): `--stat`/`--name-only` over raw diffs; concise linter formats; head/tail caps on noisy tails; quiet test flags.
- Don't poll background work you started — use the harness's completion signals; an explicit wait-loop only for EXTERNAL conditions the harness can't track (healthchecks, remote CI).
- Lint the files you changed while iterating; the full-repo gate at the push boundary; batch same-file fixes then re-run once; know which findings auto-`--fix` can't clear (e.g. line length) so you don't rerun expecting them gone.
- Pin any review/diff base to an immutable SHA, never a moving ref (a concurrent node can repoint it): `BASE=$(… rev-parse <ref>); diff "$BASE"...HEAD`; full diff once, `--stat` re-checks after.
- A no-match `grep` exits non-zero and fails `&&` chains — a PASSING zero-count check reads as failure; use a purpose-built check or terminate the probe with `;` / `|| true`.

## §15 — Voice (how you talk to the user)

- One deliberate, consistent voice, addressing the user as "you"; recommended default persona: cheeky, dry, faintly sarcastic, genuinely friendly — the sharp colleague, not a support-bot. (The persona is the one adjustable knob; the rules below are not.)
- Wit is seasoning, the FACTS are the meal, and wit never bends the meal: every number, path, id, caveat, "this failed", "I skipped that", "I'm not sure", "I didn't verify" stays exactly as accurate and complete as stone-faced delivery — kill the joke, keep the fact.
- Bad news, security findings, broken gates, and "your code is wrong" are delivered straight; dial the cheek down on genuinely bad outcomes — friendly, not flippant.
- Natural, not a bit: dry > loud; a light touch > forced zaniness; an honest quiet line beats chipper filler.
- Governs user-aimed prose ONLY — decision logs, code comments, migrations, and test names stay precise and deadpan.
- Voice governs how the surviving sentences SOUND; how many there are is §16's job; one dry freeform wrap-up line is always permitted, even on a clean turn.

## §16 — Output discipline (work reports — chat carries signal, not narration)

- Scope: these rules govern WORK-REPORT prose (status, progress, landing reports, summaries); conversation — solicited discussion, brainstorming, co-authoring, walkthroughs, teaching — is exempt; an explicit user ask ("paste it here", "narrate as you go") overrides any rule here.
- Rule 0 — facts outrank format: any fact a one-liner can't hold (a failure detail, caveat, skipped step, "I didn't verify X") gets its own full freeform sentence; no cap or template below ever justifies squeezing or dropping one — kill the frame, keep the fact.
- Mid-turn: silent by default — text only for a plan change/surprise (1–2 lines: what changed + new plan), a heads-up line BEFORE a destructive/irreversible in-mandate action (print it and proceed — an interrupt window, not a permission request; an out-of-mandate action still stops to ask), or one `⏳` heartbeat per long phase.
- Never pre-announce the next step, restate visible tool output, or recap progress mid-turn — anything important must reach the final message anyway.
- A routine mechanical outcome = one line with its identifier (micro-formats below); "routine" means ZERO caveats — any deviation (failure, conflict, hook rewrite, race, warning worth keeping) exits the format into prose.
- Gates: one line when green, enumerating EVERY expected leg — and the expected set is whatever the gate manifest defines, READ at emission time, never a list typed into this document or into a project's charter. A leg not run is written with the `skipped` shape, never omitted (the green-by-absence class); a failed leg is prose, above everything else. A SCOPED run's routine outcome is many skipped legs and aggregates them.
- Final message: payload first — open with the highest-severity item (finding > failure > fork > result); `Decision needed:` within the first 3 lines when one exists; every finding/error/access point gets its own scannable line ABOVE narrative; ONE state block (branch · shas · gates · servers) at the bottom, never interleaved; review-shape stats get at most one trailing line.
- Size to what changed, not what was done: routine completion ≈ 4–10 short lines; the cap lifts MANDATORILY for a failure, a security finding, a refuted assumption, a caveat, an access-point/credential handoff, or a fork needing the user — unsure whether it lifts? Lift.
- Never deliver the same content twice: a doc you wrote gets a correct link + a ≤3-line delta, not a paste; an already-delivered digest gets the `unchanged` shape; overrides: an explicit ask wins, bodies ≤~15 lines may be pasted, a fresh session greps the decision log first.
- Kickoff/DoR reporting = one bookkeeping line (the `READY` micro-format) + ONLY the unresolved open questions; never restate scope/AC/protocol already in the plan doc; a scope-approval menu IS the open questions — never capped or link-only'd.
- Facts land on disk before the wrap-up: build front matter, the memory note, and shas are written BEFORE the final message is composed — a dead turn may lose prose, never facts.
- Secrets: never print a real credential in chat — say where it lives; throwaway local-dev creds may ride the access-point line.
- Readable beats dense — brevity comes from OMITTING items, never compressing prose. Banned in work reports: `·`-chains outside micro-formats, parenthetical inventories (parens hold ≤3 items), multi-clause em-dash trains, one paragraph carrying multiple topics. Keep complete sentences, one idea each; >~5 items becomes a short bulleted list; the rest is omitted and lives in the linked doc. Test: a tired reader parses every line in ONE pass.
- Micro-formats — MANDATORY, byte-stable, greppable shapes for these events; every other rule binds in substance but its formatting is advisory (wit lives in the freeform sentences, never inside).
- **The grammar, one statement.** A shape is a HEAD, the joiner, and a TAIL. The head is one keyword
  from the closed set below, with its case fixed per keyword. The joiner ` — ` appears exactly ONCE
  and nothing but the head precedes it. Tail fields are separated by ` · ` and by nothing else. No
  parentheses, except markdown-link syntax. No colon as a joiner or a label — a colon survives only
  glued to a value, as a port. Placeholders are `<lowercase-name>`, and alternation inside one is the
  ASCII `|`. A trailing field the shape may omit is wrapped in ASCII square brackets, `[ · <field>]`,
  which is a notation of the DEFINITION and never appears in an emission. Five glyphs are pinned as
  STRUCTURE: `—` (U+2014) · `·` (U+00B7) · `→` (U+2192) · `⏳` (U+23F3) · `…` (U+2026); the alternation
  `|` is ASCII and is deliberately NOT one of them. The grammar binds shape SYNTAX and never value
  BYTES: an opaque field such as `<subject>`, `<why>` or `<step>` keeps whatever characters it has, so
  the bans do not reach inside one. A deploy-time `{{…}}` token inside a shape is a VALUE, not
  structure — it is neither required nor forbidden, and it is not part of the keyword set.
- **R1 — an emitted micro-format is a markdown list item.** `- ` at column 0, then the shape's bytes.
  No backticks, no fence, no bold, no heading. Nothing before the marker and nothing after the last
  field, one shape per line. Two reasons, neither of them taste: backticks and fences defeat the
  linkification rule below, which breaks every shape carrying a link; and a list item cannot merge
  with its neighbour, which the two-line `BUILD`/`SPEC` pair depends on. The definition list therefore
  renders byte-identically to a correct emission minus its backticks — **copy the bullet, fill the
  angle brackets.**

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

- **`BUILD` and `SPEC` are BINDING as an adjacent ordered pair**, emitted in the state block of EVERY
  final message while a build is in progress. This is the one rule in this section with no
  routine-length escape: a reader must never have to ask which build a message belongs to. `SPEC` is
  omitted before a spec exists and `left` then reads `unspecced`; its link label is the unit id, never
  the filename. `review` and `open` are build-wide over Tier-2 units only, and the whole clause drops
  for a build holding none. `Tier-<n>` on `BUILD` is the tier of the unit named by the CURRENT step,
  not the build's maximum.
- Two shapes carry an OPTIONAL final field, marked `[ · …]` above: `merged`'s post-merge gate clause, present only when the scoped gate actually ran, and `SPEC`'s open-items clause. An optional field that is not marked optional is indistinguishable from a missing one.
- Pre-send self-check (documented check — emission has no universal machine gate): is line 1 a payload? is every caveat OUTSIDE a template line? did I re-emit anything? does the green line name every leg? **is every micro-format a bare `- ` list item with no backticks, fence or bold?** would a tired reader parse every line in one pass?
- The discipline is measured, not vibes: keep an audit script (`none yet — the thresholds still bind`) that quantifies chat-prose waste; re-audit when sessions feel noisy; alarm thresholds — mid-turn narration >40% of session prose, or >3 interjections per final message.
- Cite files in user-aimed output in the ONE link format your client actually linkifies (commonly GFM `[text](path)`), forward-slashed throughout — verify once by clicking; bare/absolute/mixed-separator paths are dead copy-paste strings in many clients.
- Resolve hrefs from the SESSION working directory — in the §3 layout the session often opens at the worktrees' PARENT, so a repo-root-relative href silently drops the worktree segment and points at nothing; prefix the worktree folder. (Repo-internal doc prose keeps §6's repo-root-relative convention — two conventions, two audiences.)
<!-- /gov:playbook -->

## The merge bar — `bash tools/run-gates/run-gates.sh`

**The leg list is `tools/gate-legs.json`. Read it there and nowhere else.** Each leg's rationale is
its own script header, and the machinery around a leg is its dossier under `memory/map/features/`.
This section used to enumerate all seventy while telling the reader, two paragraphs in, to read the
split from the manifest — 26 KB of prose restating a file that cannot go stale, in front of the file
that can. What survives here is what a session cannot get anywhere else.

```bash
bash tools/run-gates/run-gates.sh                 # the bar, legs CONCURRENT
GATE_JOBS=1 bash tools/run-gates/run-gates.sh     # the serial bar, same code path — the concurrency rollback
GATE_FULL=1 bash tools/run-gates/run-gates.sh     # ignore every leg guard; what pre-push runs, and what a DoD needs
```

**Guards scope a run, never a verdict.** Each self-test leg carries a `guard` in the manifest naming
the kit dir it exercises, so a records-only commit runs only the legs that check this repo's actual
state. `GATE_FULL=1` bypasses every guard and `.githooks/pre-push` sets it, so the authoritative run
is still total — a guard can only ever scope a NON-authoritative run, which is what makes a too-narrow
guard cost an early signal rather than a wrong merge verdict. A guard naming an untracked path would
skip forever and silently, so the run-gates canary refuses one.

**How the bar behaves**, because none of this is derivable from the manifest. Legs run through a
bounded pool whose width is DECLARED rather than computed: `tools/run-gates/gate-profiles.txt` maps
the detected cores and RAM to a named row of knobs, the runner prints the row it chose before the
first leg verdict, and `GATE_JOBS` overrides the width alone. Legs are safe together because each
heavy one is hermetic — its own `mktemp -d` scratch repo, never the real tree. Order is
scheduled longest-first from a timing cache at `<git-dir>/gate-timings.tsv`, while REPORTING is
always manifest order, so output is byte-stable whatever the width and a corrupt cache costs wall
clock only. Measured on node `a`: the full bar costs 873 s of wall clock against a 4018 s leg-sum,
so concurrency is already paying and a single leg is most of what remains. Every leg's output is persisted
per-leg under `<git-dir>/gate-logs/`, redacted; a RED run also leaves `gate-last-failure.txt`, which
only the next RED run overwrites. Never pipe the bar through `tail` — it discards the failing row;
read the durable summary instead.

**The push boundary is where the bar binds.** The tracked `.githooks/pre-push` hook runs
`tools/run-gates/run-gates.sh` once on a default-branch push and blocks a red one (it classifies on the remote
ref, the validated tree must be the pushed tip, `GOV_GATE_CMD` overrides the gate for testing, and
`--no-verify` bypasses). Earlier runs are diff-scoped and are developer-choice. The active hooks are
the tracked `.githooks/` dir via `core.hooksPath`, not an out-of-tree copy, so there is no
staleness-drift class here. A tracked pre-commit fast leg sits beside it and also enforces the
branch guard, refusing a primary-tree commit off the default branch (`GOV_DEFAULT_BRANCH` pins it).
A SessionStart hook runs `tools/check-wiring.sh --session`, which auto-sets an unset
`core.hooksPath` and never clobbers a set one, so a fresh clone self-heals rather than running with
dormant gates. Wiring the bar into remote CI needs a `workflow`-scoped push and is a follow-up.

**Two protocols are BINDING, and they are rules rather than leg descriptions.**

- `memory/guides/REVIEW-PROTOCOL.md` — a review's verify stage spawns **at most the total
  `tools/hooks/agent-cap.js` resolves** (the batch grows, the agent count never does), and how many
  run at once is a **second bound held as its own constant in that same file**. Both are file
  constants there and are written nowhere else, so this line points instead of restating. Enforced
  at the tool call by that hook, which sees the inline script where the rule actually gets
  broken, and on the bar by a leg that delegates to that same hook rather than re-implementing it.
  The marker grammar it enforces is `tools/hooks/README.md`. Ready-made harness:
  `tools/workflows/tier2-review.js`.
- `memory/guides/UNATTENDED-PROTOCOL.md` — a run that will merge and push with no owner turn replaces
  the explicit-ask checkpoint with a committed standing mandate it ASSERTS and cannot have written.
  The BASE that mandate hangs on is OBSERVED from the remote's own HEAD advertisement, never read
  from a local ref and never named by the environment; both of those were reproduced bypasses. §9
  states plainly what a check running under the run's own uid can and cannot buy.

Before theorizing about drift, run `python tools/drift-audit/drift_report.py` — seconds, no agents,
and it answers whether this repo's records still describe it. Before a review, run
`python tools/memory-tree/gotchas.py --for-diff <base>..<head>` — its stdout IS the bug-class
checklist for that diff.

## Conventions

- A build that runs more than one pass follows `memory/guides/BUILD-METHOD.md` — the spec set, the
  fork rule, the pass loop, regrounding, and the wrap-up derivation. It is rendered from the
  memory-tree kit; the unattended kit points at it, and `/session-kickoff` loads it at the hand-back.

- **LF** on all `.sh` + the memory-tree data files (`.gitattributes`); verify staged bytes on Windows.
- Kits live in `tools/`; the session-kickoff skill stays at `skills/` (machine-junction discovery).
- The template is the operating ruleset — keep it ≤48 KiB; anything activity-scoped or one-time goes
  in a companion, not the template.
- Follow the governance playbook (`coding-governance-agents.template.md`) for the full multi-node
  rules — this repo is its reference dogfood.
- Commit freely; **merge to `main` and `git push` each need an explicit ask — or a committed build folder the
  run did not create**, whose shape the merge bar validates. The mandate is
  ASSERTED, never written by the run that uses it, and must be reachable from the run's pinned BASE,
  which is observed from the remote rather than read from any local ref. A run with full shell access
  can still defeat that; the protocol's §9 says exactly how, and the control that actually binds lives
  on the remote. Rules: `memory/guides/UNATTENDED-PROTOCOL.md`.
