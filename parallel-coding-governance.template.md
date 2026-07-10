# Parallel Multi-Node Coding — Governance Template

*Template **v2.1** · last updated 2026-07-04. One line per directive — every bullet is one imperative,
binding rule; a wrapped line is still one rule. v2.0 is a full rework (one-line format + new §4/§16 and
additions throughout — see `template-v2-rework-spec.md`): instantiated v1.x copies re-adopt
section-by-section (the format change defeats §-body diffing once); from v2.0 on, pull future improvements
by diffing your copy against this source per §-body again (ignore filled placeholders + the deleted
Customize block). Record your adopted version in your copy. History: the `…-v-N-N.md` snapshots alongside
+ this repo's git history. **v2.1 (2026-07-04):** the in-flight ledger is now sharded per node — one file per node tag behind a pointer (§3), consistent with §5's per-node-files rule; re-pull §3 + §5 and the `memory-tree` kit's ledger handling.*

<!-- governance-template: v2.1 -->

> **What:** a project-agnostic playbook for running Claude Code (or any agent) across several
> machines/sessions ("nodes") on one repo — fewer syncs and reviews, lower token spend, consistent output.
> **Use:** copy into the repo (e.g. `docs/PARALLEL.md`, or into `CLAUDE.md`), fill the placeholders
> per **Customize before use** (bottom), keep everything else verbatim. Rules are agent-facing imperatives.

## §0 — TL;DR (the load-bearing rules)

- **Session-scope every new ID** (slug = node tag + CamelCase adjective-noun) — collisions become impossible, not avoided (§2).
- **Own streams, not files; merge small and often** to local `main` (§3) — and isolate *runtimes* too: ports/DBs per session (§4).
- **Memory holds only the non-derivable**; per-node files, no shared mutable index (§5).
- **Gates are the merge bar; reviews cover what gates can't**; every confirmed finding becomes a gate or a documented check (§7, §8).
- **Never run more than 4 agents concurrently** — consolidate before you fan out; a wide burst trips the server rate limiter (§8, enforced by the `agent-cap` hook).
- **Verify before claiming done** — a check that exercises the change, never an assertion (§4, §8).
- **Consistency by construction**: build tokens, primitives, and factories *before* the screens/features that use them (§12, §13).
- **Chat carries signal, not narration**: payload first, one line per mechanical event, facts outrank format (§16).

## §1 — Work-unit lifecycle (start → done → land)

Keep units small: one stream/owner, no cross-stream contract change, reviewable as one Tier-1 diff — else split.

**Definition of Ready — run before touching code:**
- Sync: `fetch` + fast-forward local `main` (another node may be ahead); recreate/repair your worktree if needed (§3).
- Locate: read your stream's decision log + backlog (§6) and the in-flight ledger (§3); confirm your node tag (§2).
- Scope: clear acceptance criteria, one stream, small, gates named — if you can't state those, split or clarify first.
- Reserve: at your session's first work-unit, mint + grep-check a session slug (§2) and add a ledger row (§3).
- Large new feature (a Tier-2 change introducing substantial new capability — small/Tier-1 skips this): the DoR *is* a design pass — a written spec (goal · scope · non-goals · acceptance criteria) + a bounded menu of production-readiness recommendations (best-practice implementation + the extra tools/features it needs + the cross-cutting concerns: security · perf/scale · a11y · i18n · error/empty/loading states · observability · testing/gates · migration/rollback · `{{HELP_DIR}}` docs).
- Surface that menu and **get scope approval BEFORE building** (a menu to select from, not scope-creep licence); record the agreed spec per §6.
- Codebase map adopted (§5)? A design pass touching an UNDOSSIERED feature creates/refreshes that feature's dossier as a DoR item — the pass is already reading everything the dossier needs (marginal cost ≈ 0); this is the map's convergence forcing function.

**Definition of Done — before you call it done:**
- Gates green (§7); the change verified by a check that exercises it (§8), not asserted.
- Every confirmed finding left-shifted: a regression gate, or a §10 checklist entry if its class can't be gated (§7).
- User-facing change → its `{{HELP_DIR}}` page created/updated (§5).
- Codebase map adopted (§5)? New inventory keys claimed in the map tree — machine-enforced by its ratchet gate; dossier prose refreshed on touch — documented check; claim edits regen the generated artifacts in the same commit.
- Memory (non-derivable only), decision log/backlog, and ledger row updated — **on disk before the wrap-up message** (§16).

**Landing — merge protocol:**
- Land on local `main` first, verify, then push; the merge to shared `main` and the push each need an explicit ask (§8).
- Re-run the full gate suite after EVERY merge — a conflict-free merge is not a passing merge.
- Reconcile shared mutable files (backlogs, indexes) additively, never pick-a-side; diff the merge against BOTH parents (the "auto-took" class, §10). The per-node ledger needs no reconcile — each file has a single writer (§3).
- Land risky behavior dark: Tier-2 ships behind a default-OFF flag or as inert defaulted data, flipped on only after in-place verification — it merges without endangering other nodes and reverts cleanly.
- Migrations are reversible — test up/down/up.

## §2 — Nodes, identity & IDs

- Register every node once, in-repo — tag · machine/user · primary tree · worktree root · **per-node variances** (remote name, harness launch config, credential quirks — e.g. pushes touching CI config needing an elevated scope/alternate transport):

  | Tag | Machine/user | Primary tree (`main` lives here) | Worktree root | Variances |
  |-----|--------------|----------------------------------|---------------|-----------|
  | `{{TAG_A}}` | `{{MACHINE_A}}` | `{{PRIMARY_TREE_A}}` | `{{WORKTREE_ROOT_A}}` | `{{VARIANCES_A}}` |

- Identify your node by machine/user, never by filesystem path — roots can be identical across machines.
- A new node claims the lowest free one-letter lowercase tag and adds its row in the same commit.
- New-node onboarding (one-time): clone to the pinned primary tree · claim the tag (same commit) · seed local memory from the in-repo mirror (§5) · recreate stream worktrees (they never sync, §3).
- Every new tracked id (decisions, backlog items, tickets — anything `FAMILY-NNN`-shaped): `FAMILY-<slug>-<seq>` — owned by the minting session, so nothing it numbers can be contested.
- Slug = your node tag + a fresh CamelCase adjective-noun (`dAvengingTrousers`), charset `[A-Za-z]` only — minted ONCE per session; the tag's first letter makes cross-node slugs disjoint by construction.
- `<seq>` = plain 1-up per (session, family), unpadded; ids are labels, not ranks; next id = numeric max of YOUR ids in that family + 1; record per-family high-water in your ledger row (uncommitted ids are invisible to grep).
- Before committing to a slug: (1) all-time grep the governance-docs tree (decision logs, backlogs, journals, the ledger) for `[A-Z]+-<slug>-[0-9]` — re-roll on ANY hit (a pruned ledger row still owns its ids); (2) glance at live rows across all node ledger files — re-roll on a clash.
- No reserve-above-a-marker, no shared counter, no renumber-on-merge — the slug is the guarantee.
- A session = one continuous effort under one slug (several work-units/families, one `<seq>` each); a resumed/summarized session keeps its slug (the grep hitting only your own prior ids is not a collision).
- Fan-out children (sub-agents/orchestrated workers) never mint ids — the orchestrator does; a child that must mint takes its own registered slug.
- Residual tie-break (sub-1%): the later-to-merge re-mints its slug for all UNMERGED ids; an already-merged id wins.
- Legacy id eras are FROZEN: cite verbatim, never renumber, never mint in a pre-rule format, never bump a residual "next free id" marker.
- Shorthand (family+seq, slug elided) is sanctioned ONLY in session prose and ledger seq cells — never where ids are the permanent record (it's shape-identical to frozen legacy ids).

## §3 — Parallel work: streams, worktrees, trunk, ledger

- Own streams, not files: `{{STREAM_OWNERSHIP}}`. Overlap on shared files (API clients, config, indexes) is where collisions and integration reviews come from — minimize it.
- Trunk-based: merge small and often to LOCAL `main`; long-lived branches = bigger reconciles and review surface.
- `main` stays checked out in exactly ONE tree (the primary); feature work happens ONLY in sibling worktrees — parking `main` on a feature branch strands it and is the root cause of concurrent-session collisions.
- Machine-enforce the branch rule: a tracked pre-commit hook refuses primary-tree commits off `main`, wired per node by an install script; a session-start check flags the contested state; `--no-verify` is the deliberate bypass.
- Doc-only commits directly on local `main` only while the primary tree is on `main` and idle; busy tree (dirty, mid-merge, another session) → route through a worktree.
- Bootstrap worktrees with one script (`{{WORKTREE_SCRIPT}}`): sibling worktree on a fresh branch off fast-forwarded `main` + dependency install.
- Worktree lifecycle: enumerate with `git worktree list` (never assume the set); worktrees do NOT sync across machines (absolute links — recreate per machine); relocate with `worktree move` + `repair`, never `mv`.
- Commit the governing doc to `main` so it propagates — it only exists in checkouts where it's committed.
- Shard the in-flight ledger per node — one file per node tag behind a thin pointer (exactly like the per-node journals, §5), NEVER one shared table: each node writes ONLY its own file, so the ledger is conflict-free by construction (the same disjoint-by-tag property as the session slug) and no merge ever touches it. A single shared ledger is the shared-mutable index §5 forbids — it forces a conflict on every land, and additive resolution silently leaves stale rows.
- Row shape `| node | slug | branch/worktree | streams | seq high-water | status |`; status ∈ `{in-flight | merged | pushed:<sha>}` + at most one short clause; narrative belongs in the journal, never here. Read ALL node files for the who's-touching-what / slug-collision scan (§2); write only your own.
- Self-prune on session start: after fast-forwarding `main`, delete your OWN `pushed:/merged:<sha>` rows whose sha is an ancestor of `main` (`git merge-base --is-ancestor <sha> main`) — they're derivable from history; never touch another node's file.
- Contract-first for cross-cutting changes: a schema/wire-format/enum two nodes depend on lands as a contract + gate before either builds on it.
- Landings are `--no-ff` merges with a descriptive message — one visible, atomic, cleanly revertable integration unit.
- Every agent commit ends with the mandated attribution trailer: `{{COMMIT_TRAILER}}`.

## §4 — Runtime isolation & the verification harness

- Concurrent sessions share machines: local review/preview stacks bind canonical+offset host ports (`{{PORT_OFFSET}}`) so simultaneous stacks can't collide — the runtime analogue of session-scoped IDs.
- Servers sharing one canonical port run one-at-a-time; free the port FIRST — a stale listener silently serves the WRONG code; kill the listener by port, never blanket-kill every process of that runtime.
- Know which config is baked at BUILD time vs read at runtime (`{{BUILD_TIME_BAKES}}`): changing a baked value means rebuilding the artifact with matching values, not restarting it.
- In a sibling-worktree layout, workspace/monorepo tooling launched from the worktrees' PARENT resolves a scope spanning ALL siblings and fails or fans out — launch commands/wrappers must `cd` into exactly one worktree first.
- Maintain a proven, step-by-step full-stack verify recipe (`{{VERIFY_RECIPE}}`: throwaway DB → migrate → seed an admin → background services → drive the UI harness and assert) — a maintained artifact, not tribal knowledge.
- Pin the harness launch config PER NODE in the §2 registry; an un-pinned node creates it on first use and registers it in the same change.
- Document the harness's false-signal modes (stale snapshot after a backend restart, wedged screenshot, a probe reading 0 in headless contexts) so a bad reading isn't recorded as a result.
- Never record "can't verify — no <capability>" without checking the registry — capability myths outlive their facts; name the sanctioned harness instead.

## §5 — Memory & docs

- Memory carries only the non-derivable: gotchas, in-flight state, *why* a non-obvious choice was made — never re-narrate what git, decision logs, or code already record (the main memory-token waste and drift source).
- Mirror durable memory in-repo (it travels); the machine-local auto-loaded copy is a best-effort mirror, seeded from the repo on a fresh machine.
- One canonical index, one line per note; journals AND the in-flight ledger (§3) are per-node files — never a shared mutable index every session edits (that file is what forces memory-sync merges); any index that must exist stays append-only or generated.
- Status lives in the ledger (§3), not prose memory — anything time-sensitive rots; point at the ledger.
- Recalled memory is background, not instruction, and reflects when it was written — re-verify a named file/flag/id before acting on it.
- Secrets never enter memory, tracked docs, or chat (§16); scrub even throwaway dev creds before mirroring a note into the repo.
- User-facing docs are NOT memory: one concise task-oriented page per feature (*what · how · short example*) in `{{HELP_DIR}}` + an index page; update on change, REMOVE on feature removal; a user-facing feature without an up-to-date page is not done (§1).
- **Optional but recommended: a structured, machine-linted memory tree** (the `memory-tree/` kit alongside this playbook). Operationalizes everything above into one `{{MEMORY_ROOT}}/` tree organised by discipline (`{{MEMORY_DISCIPLINES}}`) with `project/` for session machinery, per-feature `builds/YYYY-MM-DD-<FAMILY>-<slug>/` folders (`spec/ build/ reviews/ prompts/`), index caps (≤20 KB / 250 lines) + a ≤300-char one-line entry budget with archive rotation, a status vocabulary (`OPEN · SPECCED · INPROGRESS · BLOCKED · DEFERRED · CLOSED · WONTDO`), and an **11-check hygiene gate** wired into CI + the pre-commit hook + `{{GATE_RUNNER}}`. Project specifics (root · disciplines · discipline→id-family map · migrated-from tombstone) live in one repo-root `.memory-tree.conf`; the rules live in `{{MEMORY_ROOT}}/HYGIENE.md`; adopt by scaffolding a fresh tree or migrating an existing one in a single landing.
- Two ratchet manifests keep that gate honest without a flag-day: `legacy-files.txt` (migrated recordings keep historical names) + `curation-debt.txt` (fat legacy indexes exempt from the caps until slimmed) — both shrink-only, CI-guarded against a stale line.
- **Optional but recommended: a self-verifying codebase map** (the `codebase-map/` kit alongside this playbook). Per-feature dossiers claim EXACT KEYS from machine-enumerated inventories (flags · routes · CLI · migrations · jobs · docs pages · …, declared once per project in `map_extractors.py`); a test-suite ratchet fails on any unclaimed NEW key AND on any claim naming a dead key (the map cannot rot into fiction); a shrink-only `baseline.toml` makes adoption non-blocking; generated artifacts are freshness-gated; `map_diff` renders any git range as a feature-level changelog (the "what did the parallel sessions land" answer). Path globs are digest-only — never gated. Zero CI changes: the gate rides the suite that already gates the merge bar. Adopt per `codebase-map/README.md`; derive inventories per `codebase-map/INVENTORY-DERIVATION.md`.

## §6 — Decisions, backlogs & the governing doc

- Two record types per stream: the decision log is append-only (never rewrite a ratified record — supersede with a new id + note); the backlog is mutable (stable ids, status updated in place; ids are labels, gaps fine).
- Per-stream id families (`{{ID_FAMILIES}}`): the family prefix routes an id to its log/backlog; allocation is slug-scoped (§2), so no shared "next free id" marker exists.
- Record real decisions as you make them — future sessions and nodes rely on these being current.
- Session-start reading order: ALWAYS load the master decision index first, then the stream logs for the area touched — routed by `{{DOC_ROUTING_TABLE}}` (work-area → doc tree → id families → backlog).
- Logs are two-tier for token scoping: a one-line-per-decision index pointing at per-decision detail files; open details only for the areas you touch.
- The instantiated doc opens with a compact product-identity preamble for `{{PROJECT_NAME}}` (`{{PRODUCT_PREAMBLE}}`: what the software is, deployment model, major runtime pieces, what stays instance-agnostic).
- The instantiated doc carries the repo-layout map (`{{REPO_LAYOUT_MAP}}`: each top-level dir + its role and the core/adapter relationships) — sessions never re-derive where things live.
- The instantiated doc carries the everyday-command catalog (`{{COMMAND_CATALOG}}`: install, dev servers, migrations, artifact regeneration, seeding, the one formatter/linter per language) — sessions never re-derive the one-true invocation.
- Pin one in-repo home for business/product context (`{{PRODUCT_CONTEXT_HOME}}`: brand, positioning, product specs) so sessions locate it instead of asking.
- In-doc paths are repo-root-relative; the root is pinned once per node in the §2 registry, never re-derived. (User-facing links follow §17, a different convention.)
- Non-obvious rules carry provenance inline (the motivating decision/incident id); environment/capability claims carry a verified-(date, node) stamp.
- Each guarded security surface keeps a written security-model section in the decision log; read it BEFORE extending that surface (§9).

## §7 — Quality gates = the merge bar

- Keep the automated suite green before any merge: `{{GATE_COMMANDS}}` (typecheck/compile · lint · test · generated-artifact freshness · structural invariants). Gates are the quality floor; reviews cover only what gates can't.
- Wire the suite into remote CI as machine-required checks (`{{CI_FILE}}`) — convention is not enforcement.
- Provide one command that runs the whole local bar with legs concurrent, wall ≈ longest leg: `{{GATE_RUNNER}}`.
- A slow leg may have a sanctioned faster local variant — document the equivalence explicitly (which local run satisfies which CI leg), so local verification is fast AND unambiguous.
- Single source of truth → generated artifacts → parity gate, for every contract duplicated across languages/layers; a new shared contract gets ONE source, generation, and a drift test — never a hand-kept second copy.
- Lockstep invariants get a guard (migration single-head, stale manifest, schema↔validator skew) — a gate, not memory.
- Left-shift every confirmed finding: not done until a regression test covers its CLASS, or (if ungateable) it joins §10 as a documented check — this is how review cost trends down.
- Guard against green-by-absence: every test/typecheck glob spans ALL real file classes (beware glob dialects that don't brace-expand), and a collection gate asserts every test file contributes ≥1 collected item — a de-collected file can't fail.
- Codebase map adopted (§5)? Its coverage + freshness tests are merge-bar legs like any other — they ride the existing suite; never exempt them to "unblock" a landing (claiming the key IS the unblock).
- Classify special-execution tests STRUCTURALLY: a collection hook auto-marks by fixture/dependency so a new test can't forget its class, and the default environment can't silently switch engines.
- Parallel test runs preserve per-file isolation invariants (file-level distribution, not per-test); parallelism is opt-in; small selections run serially (worker startup makes them a net loss).
- Document deliberate gate exemptions together with their compensating manual check — an exemption is not coverage.
- Concurrent migration forks (two branches, same parent) reconcile via a merge revision, never a rebase; know whether the local test harness can even see a fork (often only the head-count gate does).
- A generated contract artifact baked into multiple deployables couples their releases: those artifacts deploy TOGETHER, and a contract change may couple a frontend release to a data migration.

## §8 — Review protocol (match intensity to risk; verify, don't assert)

- Tier 1 — mechanical/additive (no new write path, migration, auth/sanitization/egress surface, or shared-contract change): gates + one focused self-review of the diff. NO multi-agent review.
- Tier 2 — substantive (any of the above, or a cross-stream merge): adversarial find → verify → synthesize, running the §10 checklist as part of it.
- Scope Tier-2 to the diff at an immutable SHA plus its immediate callers/callees, reviewed at the integration boundary ONCE (the cumulative diff landing on `main`) — per-increment reviews re-scan overlapping code.
- Default Tier-2 shape (ROI-tuned): a parallel fan of 3–6 primed finder lenses (security · correctness · data-integrity · dead-code · integration-seams) → a skeptic prompted to REFUTE each finding → one synthesis pass; drop any finding a skeptic refutes unless reachability + impact re-established. Total agents may be many; **concurrency is HARD-CAPPED at 4** (next bullet).
- **CONCURRENCY ≤ 4, ALWAYS — the #1 rate-limit lever.** Large concurrent bursts (a ~40-agent review fan) saturate server throughput and trip the SERVER rate limiter, killing whole phases for millions of tokens; the harness auto-cap (`min(16, cores-2)` ≈ 14) does NOT protect against this. Route ALL Workflow fan-out through cap-4 helpers `boundedParallel(thunks, 4)` / `boundedPipeline(items, 4, …stages)` — inline them (scripts can't import; each helper's `parallel(`/`pipeline(` line carries a `gov:bounded-fanout` marker). **CONSOLIDATE before you fan out:** one BATCHED skeptic per ~5 findings (not one-per-finding), and merge cheap lenses — fewer total agents beats a wide fan. Enforce it mechanically: install the `agent-cap.js` PreToolUse hook (matcher `Workflow`) — it DENIES any script calling the raw primitives — and run the ready `workflows/tier2-review.js` harness (~7–9 agents, ≤4 concurrent). Install: WIRE-INTO-PROJECT §5.
- Finders emit CONCRETE findings — `file:line` + repro/impact + proposed fix — so skeptics can actually verify them.
- Precision (confirmed/(confirmed+refuted)) is the #1 token lever — below ~0.5, tighten scope/priming before adding agents; scale a large fresh surface with LENSES (coverage), not skeptics (precision saturates); past ~25 agents returns diminish.
- Feed reviewers the security model, the already-tracked open issues, and what's by-design — so they hunt NEW issues, not re-report known ones.
- Match intensity to target richness: heavy multi-lens earns its tokens on fresh/complex write paths; over hardened code it manufactures refuted noise — review light or skip.
- Persist each Tier-2 run as an in-repo artifact folder (`{{REVIEW_DIR}}`); periodically re-audit the corpus (token cost vs severity-weighted confirmed-finding value) to retune these defaults.
- Design structured-output schemas so a malformed return can't force a full regeneration (the top output-token waste in workflow audits) — the three rules below.
- Never make an agent hand-serialize a large body as JSON: it writes the body to a file and returns `{path, summary}`, forward-slash paths (unescaped backslashes are the top JSON breaker).
- Restate the schema's exact required keys in EVERY loop iteration's prompt — an agent looping over items forgets the shape and re-fails identically.
- Accept-and-ignore stray keys unless a stray key is actually harmful; on a validation failure feed back only the offending field, never "regenerate everything".
- Orchestration scripts run in sidechains that inherit neither your hooks nor the governing doc, in a restricted runtime (plain JS — no type syntax, no imports) — the schema discipline lives with the orchestrator; inline it as a snippet. This is exactly why the ≤4 cap is enforced at the `Workflow` *tool-call* (a main-loop `PreToolUse` fires there, via `agent-cap.js`) and never inside the script, where no hook reaches.
- Verify before "done": a check that exercises THIS change (its own/affected test, the relevant gate, or the §4 harness) — an unrelated green gate is not proof; failures reported with output, skipped steps named.
- Commit freely as you go (branch/worktree, or local `main` for doc-only per §3); landing on shared `main` and `git push` each require an explicit ask.

## §9 — Security boundaries (apply to any new write path / surface)

- Sanitize untrusted input at the WRITE boundary, once; trust storage at render; re-check size/shape caps AFTER any transform that can grow content (sanitizers add attributes).
- ONE composite write-guard (scrub + capability gate + sanitize) on EVERY path that stores renderable/dangerous content — sibling write paths (templates, imports, saved/shared components) included; a bare or partial sanitizer on a sibling path is the recurring hole.
- Gate the most dangerous sanctioned content class behind an explicit per-principal permission at write time — a capability check distinct from, and additional to, sanitization.
- One canonical URL/href normalizer shared by client AND server: strip control/whitespace chars, fold `\`→`/`, reject protocol-relative (`//host` and `/\host`), deny dangerous schemes (`javascript:`/`data:`/`vbscript:`); divergence is a stored open-redirect; pin the evasions (`/\evil`, `\\evil`, control chars) in tests on both sides.
- SSRF-guard every outbound request: https-only, resolve to public IPs only, no redirect-following, signed payloads; the SAME guard on retry/queue paths, not just inline; blocking DNS/network resolution runs OFF the event loop (a hung nameserver must not freeze a worker).
- Authorization lives in the shared core (deny-by-default RBAC, defined as code) so every adapter — HTTP, RPC, CLI, AI tool — inherits it; a service fn reachable by a future adapter re-checks authz itself.
- AI/automation runs as a dedicated non-login service principal with a deliberately narrow grant — never a human/admin role; authority bounded by construction.
- Automation writes are draft-only by default; autonomous publish/irreversible action sits behind an explicit default-OFF gate — a standing blast-radius bound on the agent surface, distinct from per-feature launch flags.
- Keep PII/secrets off the AI/automation surface structurally: payload/return types that CANNOT carry sensitive values (ids/counts/field-names only); audit value-bearing fields flowing to automated readers.
- Optimistic concurrency on full-document writes: a version/`updated_at` precondition → 409 on stale — else concurrent editors/nodes silently clobber each other.
- Document which production protections are deliberately OFF in the test env (CSRF, rate limits, …), confirm they default ON in production, and exercise each directly in a dedicated test.

## §10 — Recurring bug classes (run in every Tier-2 review)

- Client/server validation divergence: client validates only visible/active fields but submits the whole payload → strip inactive values before send, or validate identically.
- Dead plumbing: a value computed → serialized → passed → never read; wire the consumer or delete end-to-end + guard test.
- Index that doesn't serve its query: a composite led by an inequality, or column order mismatching predicate + `ORDER BY`, can't seek/sort — verify against the real query shape.
- Stale caches: invalidated on create but not rename/delete/restore — reset on ALL mutation paths.
- Cross-language catalog drift in "zero-drift" modules, and coercion/format divergence at ANY cross-language boundary (e.g. numeric stringification differing per runtime) — normalize on one side and guard with a parity test (§7).
- Half-applied merges: one branch's fix silently dropped when the other's version auto-took; duplicate/conflicting symbol definitions — diff the merge against both parents.
- Guard on the primary write path but a bare/partial sanitizer on a SIBLING path to the same stored data (templates, imports, saved/shared components) — verify every such path routes through the §9 composite guard.
- Check-then-insert racing a concurrent bulk-UPDATE (read-committed: the bulk statement's snapshot never sees the in-flight child, defeating the containment) — lock the parent row on BOTH the insert and bulk-mutate paths (the lock may be a no-op on the dev DB engine — verify serialization on the production engine).
- Never cache a degraded/failed response (rate-limit, 5xx, flag-off blip) as the permanent answer — mark degraded ≠ genuinely empty, and skip caching it, or one transient failure suppresses the feature all session.
- Stale async response race: guard success-path state writes with a request-identity check and abort superseded in-flight requests, or a late response clobbers fresher results.
- Blocking/synchronous work on a hot path or event loop (I/O, DNS, heavy transforms) — find it and off-load it.
- Verify the COMPUTED value, never the declaration: styling/config declarations can silently resolve to nothing (conflicting caps, percentage sizes against indefinite bases, no-op utility values) — measure the rendered result.
- Scale-to-fit frames measure their container SYNCHRONOUSLY at first commit (layout-effect/callback ref), never defaulting until a resize observer fires (unreliable in throttled/preview contexts); a CSS max-width cap fights the scale model (double-shrinks) — rely on the container's overflow clip, and verify rendered width ≤ container at a narrow viewport.
- A component defined inside another's render body mints a new type per parent render → full remount per keystroke (focus loss, un-typeable forms) — hoist to module scope.
- Window-scrollbar toggling between short/tall pages shifts centered, window-scrolled layouts (one trigger, two symptoms: horizontal recenter + header reflow) — stabilize the scrollbar gutter; never let a page depend on scrollbar presence (a no-op on overlay-scrollbar platforms — it can't be eyeballed there, so don't remove the gutter rule on that evidence).
- Transient overlays (autocomplete, popups) dismiss on focus-out via a related-target-scoped blur check, per the platform a11y authoring practices.
- ID-scheme drift (documented check): new ids are `FAMILY-<slug>-<seq>` (§2); no reused slugs, no pre-rule formats, no renumbering append-only records.
- Where the needed runner/harness doesn't exist, push ALL logic into pure, machine-gated helpers and keep the un-testable wiring deliberately thin — only that residue ships as a documented check.
- Documented checks (no machine gate fits) are labeled so, record WHY no gate fits + the concrete manual recipe (grep pattern, measurement), and graduate to a gate when the missing harness lands.

## §11 — Cross-OS & toolchain hygiene

- Force `LF` via `.gitattributes` on execution-sensitive filetypes (shell scripts, Dockerfiles, configs, env files, migration templates, runtime-read JSON) — a stray CR breaks shebangs, `sh -c`, servers, generated migrations.
- Verify the staged BYTES, not a pretty-printer: `git diff | cat -A` / `git cat-file -p <blob>`; `git show` and MSYS `grep` mislead on CRLF.
- Pin toolchain versions + the one-true way to run gates on each OS: `{{TOOLCHAIN_NOTES}}` — no per-session re-derivation.
- Prefer deterministic run modes (no auto-reload) where a watcher can leave stale processes/ports squatting.
- POSIX-emulation shells on Windows (MSYS/Git-Bash/Cygwin) mangle backslash working-dir paths (`git -C C:\repo` → `fatal: cannot change to 'C:repo'`) — use forward-slash there; a zero-false-positive hook can block the broken form.
- Package installs run from a POSIX-emulation shell can create broken links in the dependency tree — if it looks wrong, reinstall from the native shell.

## §12 — Architectural consistency (build-once, reuse-everywhere)

- Decide the extension pattern before the SECOND instance — so #3..#N are data + a few overrides, never new plumbing.
- A "kind" gets a factory/base, not copies: at instance #2, extract the shared contract into a definition helper/base — per-kind map: `{{KIND_FACTORY_MAP}}`.
- One shared core, thin adapters: business logic + authorization in a single service core; HTTP/RPC/CLI/AI surfaces are thin adapters that cannot diverge (also how authz stays consistent, §9).
- Single source of truth → generated artifacts (§7): the catalog of a kind's instances generates the schema/validator/manifest/docs; adding an instance = one edit + a drift gate.
- Promote shared widgets the instant two features need them, on a two-tier ladder: product-generic presentational primitives → the shared kit (`{{SHARED_PRIMITIVES_LOCATION}}`); app-scoped shared widgets → that app's own kit; a feature re-implementing or re-styling a primitive locally is a smell.
- Forward-compatible data: new fields additive + defaulted (old content renders identically, new capability inert until used); shape changes ship an auto-upgrade step; prefer riding an existing shape over a migration.
- Reuse audit before building: grep for an existing component/util/endpoint to extend before adding one.
- Gate the layout conventions you can (naming, layer boundaries); the "where things live" map itself lives in the always-loaded doc (§6) so every feature has an obvious home.

## §13 — Visual consistency (design system FIRST, before screens)

- Build the design system — tokens + primitives — BEFORE screens; screens consume tokens and never hardcode values; author the visual contract up front (`{{VISUAL_CONTRACT_DOC}}` + token layer `{{TOKENS_LOCATION}}`).
- Tokens for everything: color roles (bg/surface/fg/muted/accent/border/ring, light AND dark), spacing `{{SPACING_SCALE}}`, type `{{TYPE_SCALE}}`, radius, shadow, breakpoints `{{BREAKPOINTS}}`, z-index, motion; a lint/gate flags raw hex/px in feature code.
- Semantic, surface-aware color — never a raw palette stop on an arbitrary surface: each surface declares a matched bg+fg pair components inherit; make illegible pairings impossible by construction; provide a contrast helper that auto-picks a readable fg for any accent (computed, not eyeballed).
- Contrast is a standing gate, not a review item: assert WCAG AA (4.5:1 text, 3:1 non-text) over token combinations + a route scan, in light AND dark.
- Mobile-first: base styles for the smallest viewport, layered up; "done" = checked at the smallest AND a large breakpoint; touch targets ≥ `{{MIN_TOUCH_TARGET}}`.
- Layout & rhythm via shared primitives (Stack/Cluster/Grid/page-shell own spacing, max-width, gutters); typography via the type scale + a few text components, enforcing heading hierarchy (one H1 per page) — features place content into them.
- States (empty/loading/error/disabled/long-content/focus/i18n-RTL width) and a11y (focus-visible rings, `aria-*`, label associations, reduced-motion) live in the primitives — inherited, never re-added per screen.
- A living reference gallery/harness (`{{GALLERY_ROUTE}}`) mounts the REAL components reading the REAL tokens across states/modes/breakpoints, and is the PRIMARY authority for design work: new/changed UI conforms to it unless a task notes an exception; it *reflects* the system, never redesigns it — a reference/reality disagreement IS the bug; review the system centrally, not per screen.

## §14 — Session execution hygiene (per-call token discipline)

- Strategy: spend tokens on NEW judgment, never re-deriving the known — tier + diff-scope reviews (§8), gate over re-review (§7), lean memory/ledger (§3, §5), streams + small merges (§3), system-first UI (§12, §13); **stop once verified** (per-call waste — re-reads, uncapped output, hand-polling, edit/format ordering — was the dominant avoidable spend in a transcript audit).
- Don't re-fetch what's in context: no re-Read to keep editing a file or to "verify" an edit the tool confirmed; slice large files (range/grep), never whole re-reads; never re-read a command-output spill or large generated artifact — filter it at generation.
- Re-Read ONLY when something outside your edits changed the file (formatter/`--fix`, format-on-save hook, a concurrent node on a shared doc); make manual edits FIRST and format LAST — reformatting between edits forces the modified-since-read re-read loop; batch a file's edits.
- Bound every command's output (it all lands in the transcript, read or not): `--stat`/`--name-only` over raw diffs, then read only needed hunks; concise linter formats; head/tail caps on noisy tails; quiet test flags.
- Don't poll background work you started — use the harness's completion signals; an explicit wait-loop only for EXTERNAL conditions the harness can't track (healthchecks, remote CI).
- Lint the files you changed while iterating; the full-repo gate at merge; batch same-file fixes then re-run once; know which findings auto-`--fix` can't clear (e.g. line length) so you don't rerun expecting them gone.
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
- Mid-turn: silent by default — text only for a plan change/surprise (1–2 lines: what changed + new plan), a heads-up line BEFORE a destructive/irreversible in-mandate action (print it and proceed — an interrupt window for an attended user, not a permission request; an out-of-mandate action still stops to ask), or one `⏳` heartbeat line per long phase.
- Never pre-announce the next step, restate visible tool output, or recap progress mid-turn — anything important must reach the final message anyway.
- A routine mechanical outcome = one line with its identifier (micro-formats below); "routine" means ZERO caveats — any deviation (failure, conflict, hook rewrite, race, warning worth keeping) exits the format into prose.
- Gates: one line when green, enumerating EVERY expected leg (the standing merge bar + any gates named at DoR); a leg not run is written `skipped: <leg> — <why>`, never omitted (the green-by-absence class); a failed leg = prose, above everything else.
- Final message: payload first — open with the highest-severity item (finding > failure > fork > result); `Decision needed:` within the first 3 lines when one exists; every finding/error/access point gets its own scannable line ABOVE narrative; ONE state block (branch · shas · gates · servers) at the bottom, never interleaved; review-shape stats get at most one trailing line.
- Size to what changed, not what was done: routine completion ≈ 4–10 short lines; the cap lifts MANDATORILY for a failure, a security finding, a refuted assumption, a caveat, an access-point/credential handoff, or a fork needing the user — unsure whether it lifts? Lift.
- Never deliver the same content twice: a doc you wrote gets a correct link + a ≤3-line delta, not a paste; an already-delivered digest gets `unchanged since <link> — delta: <…|none>`; overrides: an explicit ask always wins, bodies ≤~15 lines may be pasted, a fresh/resumed session greps the journal before assuming "already delivered".
- Kickoff/DoR reporting = one bookkeeping line (the `READY` micro-format) + ONLY the unresolved open questions; never restate scope/AC/protocol already in the plan doc; a scope-approval menu IS the open questions — never capped or link-only'd.
- Facts land on disk before the wrap-up: ledger row, journal/memory note, and shas are written BEFORE the final message is composed — a dead turn may lose prose, never facts.
- Secrets: never print a real credential in chat — say where it lives; throwaway local-dev creds may ride the access-point line.
- Readable beats dense — brevity comes from OMITTING items, never from compressing prose: cramming the same inventory into fewer, denser lines violates this section (the "wall of barely punctuated text" failure). Banned in work reports: `·`-chains outside micro-formats, parenthetical inventories (parens hold ≤3 items), multi-clause em-dash trains, one paragraph carrying multiple topics. What survives the cut is complete sentences, one idea per sentence/bullet; >~5 items becomes a short bulleted list, one readable sentence each; everything past that is omitted and lives in the linked doc. Test: a tired reader parses every line in ONE pass.
- Micro-formats — MANDATORY, byte-stable, greppable shapes for these mechanical events; every other rule in this section binds in substance but its exact formatting is advisory (wit lives in the freeform sentences around the templates, never inside):
  - `committed <sha> <branch> — <subject>`
  - `pushed <remote>/main <old>..<new> (ff, N commits)`
  - `merged --no-ff <branch> → main <sha> · post-merge gates GREEN`
  - `gates GREEN — <every leg, with tallies>` · `skipped: <leg> — <why>`
  - `up — <service> :<port> (<tree>) · … · admin <user> / <pw-or-where-it-lives>`
  - `READY — <slug> · node <tag> · <branch> off <sha> · Tier-N · gates: <list>`
  - `⏳ <what's running> (~<est>) — results land in the final message`
- Pre-send self-check (documented check — prose has no machine gate): is line 1 a payload? is every caveat OUTSIDE a template line? did I re-emit anything? does the green line name every leg? would a tired reader parse every line in one pass (no `·`-chains or paren-inventories outside micro-formats)?
- The discipline is measured, not vibes: keep an audit script (`{{PROSE_AUDIT}}`) that quantifies chat-prose waste; re-audit when sessions feel noisy; alarm thresholds — mid-turn narration >40% of session prose, or >3 interjections per final message.

## §17 — User-facing file references (make them clickable)

- Cite files in user-aimed output in the ONE link format your client actually linkifies (commonly GFM `[text](path)`), forward-slashed throughout — verify once by clicking; bare/absolute/mixed-separator paths are dead copy-paste strings in many clients.
- Resolve hrefs from the SESSION working directory — in the §3 layout the session often opens at the worktrees' PARENT, so a repo-root-relative href silently drops the worktree segment and points at nothing; prefix the worktree folder. (Repo-internal doc prose keeps §6's repo-root-relative convention — two different conventions, two different audiences.)

## Customize before use

- Who: the agent, one-time — read the repo to fill discoverable placeholders; ask the user ONLY for what isn't in the code (the *(ask user)* items); propose-and-flag anything inferred; delete this block; then `grep '{{'` to confirm none survived.
- `{{PROJECT_NAME}}` — the repo this governs (discoverable, not an ask).
- Fleet *(ask user)*: node registry rows `{{TAG_A}}`/`{{MACHINE_A}}`/`{{PRIMARY_TREE_A}}`/`{{WORKTREE_ROOT_A}}`/`{{VARIANCES_A}}` (… one row per node) · `{{STREAM_OWNERSHIP}}` (stream → node).
- Records & docs: `{{ID_FAMILIES}}` · `{{DOC_ROUTING_TABLE}}` · `{{PRODUCT_PREAMBLE}}` · `{{REPO_LAYOUT_MAP}}` · `{{COMMAND_CATALOG}}` · `{{PRODUCT_CONTEXT_HOME}}` · `{{HELP_DIR}}` · `{{REVIEW_DIR}}`.
- Memory tree (only if adopting the `memory-tree/` kit — else drop these + the two §5 memory-tree lines): `{{MEMORY_ROOT}}` (default `memory`) · `{{MEMORY_DISCIPLINES}}` (the space-separated discipline folders + their discipline→FAMILY id map, written into the repo-root `.memory-tree.conf`; `{{ID_FAMILIES}}` supplies the families). Adopt: `memory-tree/adopt-memory-tree.sh --scaffold` (new) or a one-landing migration (existing).
- Gates & git: `{{GATE_COMMANDS}}` · `{{CI_FILE}}` · `{{GATE_RUNNER}}` · `{{COMMIT_TRAILER}}` · `{{WORKTREE_SCRIPT}}` · `{{TOOLCHAIN_NOTES}}`.
- Runtime & verification: `{{PORT_OFFSET}}` · `{{BUILD_TIME_BAKES}}` · `{{VERIFY_RECIPE}}`.
- Architecture & design system: `{{KIND_FACTORY_MAP}}` · `{{SHARED_PRIMITIVES_LOCATION}}` · `{{TOKENS_LOCATION}}` · `{{SPACING_SCALE}}` · `{{TYPE_SCALE}}` · `{{BREAKPOINTS}}` · `{{MIN_TOUCH_TARGET}}` · `{{GALLERY_ROUTE}}` · `{{VISUAL_CONTRACT_DOC}}`.
- Output discipline: `{{PROSE_AUDIT}}` (the audit script location, or "none yet — thresholds still bind").
- Droppable when inapplicable: §9 lines about outbound calls / stored HTML (no such surface) · §11 (single-OS teams) · §4's harness lines (no UI) · §13 (no UI at all); §15's persona is adjustable per project — its facts-over-wit rules are not. Everything else is universal core: keep it verbatim.
