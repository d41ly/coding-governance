# Parallel Multi-Node Coding — Governance Template

*Template **v1.0** · last updated 2026-06-18. When you instantiate this in a repo, record the adopted
version in the copy; diff your copy against this source later to pull in improvements. Change history: git.*

> **What this is.** A project-agnostic playbook for running Claude Code (or any agent) across **several
> machines/sessions ("nodes") at once** on the same repo, with **fewer memory syncs and code reviews**,
> lower token spend, and consistent high-quality output. Distilled from a real multi-node project (a
> block-based CMS) and its accumulated findings.
>
> **How to use.** Copy this into a new repo (e.g. as `docs/PARALLEL.md`, or paste the relevant sections
> into the repo's `CLAUDE.md`). Then fill the `{{PLACEHOLDERS}}` — see **Customize before use** at the
> bottom. Everything outside placeholders is the universal ruleset; keep it. Treat the rules as
> agent-facing instructions (imperative), the same way a `CLAUDE.md` is read each session.

---

## §0 — TL;DR (the load-bearing rules)

1. **Node-scope every new ID** so concurrent nodes can't collide (§1). Collisions become *impossible*, not *avoided*.
2. **Partition work by stream ownership** so nodes touch disjoint files; **merge small and often** to local `main` (§2).
3. **Memory holds only what git + decision logs don't** — non-derivable state, gotchas, in-flight coordination. Per-node files, no shared mutable index (§3).
4. **Gates are the merge bar; reviews are for what gates can't check.** Tier review intensity to blast radius. Turn every confirmed finding into a permanent gate (§5, §6).
5. **Verify before claiming done** — a passing gate or an observed result, never an assertion (§6).
6. **Consistency by construction, not correction.** Build the design system (tokens + primitives) and the extension pattern (factories + one shared core) *before* the screens/features that use them, and gate raw values out — polishing inconsistency in afterward is the expensive path (§11, §12).

---

## Work-unit lifecycle — start → done → land

The numbered sections are the *principles*; this is the *sequence* every unit of work runs through. Keep
units small enough to finish and merge in one sitting.

**Before you start — Definition of Ready.** Run before touching code:
1. **Sync** — `fetch` + fast-forward local `main` (another node may be ahead); recreate/repair your worktree if needed.
2. **Locate** — read your stream's decision log + backlog (§4) and the **in-flight ledger** (§2); confirm your **node tag** (§1).
3. **Scope** — the unit has clear acceptance criteria, fits one stream/owner (§2), is small, and names the gate(s) it must pass (§5). If you can't state those, it isn't ready — split or clarify first.
4. **Reserve** — allocate node-scoped IDs (§1), bump the marker, add a ledger row (§2).

**Before you call it done — Definition of Done.**
- Gates green (§5); the change is **verified, not asserted** (§6).
- Every confirmed finding is **left-shifted into a gate** (§5), not merely fixed.
- Memory updated (non-derivable only, §3); decision/backlog updated (§4); ledger row → merged/pushed (§2).

**Landing it — merge protocol.**
- Land on **local `main` first**, verify, then push; commit/push only when asked (§6).
- **Re-run the full gate suite after *every* merge** — a clean (conflict-free) merge is not a passing merge.
- Reconcile shared mutable files (backlogs, ledger, indexes) **additively — never pick-a-side**; then diff the
  merge against *both* parents to confirm no edit was silently dropped (the "auto-took" bug class, §8).
- **Land risky behavior dark** — new risky capability ships behind a **default-OFF flag** (or as inert,
  defaulted data) and is flipped on only after it's verified in place; migrations are **reversible** (test
  up/down/up). Risky work can then merge without endangering other nodes, and reverts cleanly.

---

## §1 — Nodes & identity

**Register every node once.** A "node" = one machine + working tree where the repo is developed. Each gets
a stable **one-letter lowercase tag** in a registry that lives in the repo (so every node sees it):

| Tag | Node — machine / primary tree |
|-----|-------------------------------|
| `{{TAG_A}}` | `{{MACHINE_A}}` — primary tree `{{PRIMARY_TREE_A}}` (where `main` stays checked out) |
| `{{TAG_B}}` | `{{MACHINE_B}}` — worktrees under `{{WORKTREE_ROOT_B}}` |

A new node takes the lowest free letter and adds a row in the same commit. A *tag* clash is a tiny,
once-per-machine reconcile; it prevents the recurring *ID* clashes below.

**Node-scoped IDs — REQUIRED on every new tracked id** (decisions, backlog items, tickets, TODO refs —
anything with a `FAMILY-NNN` shape):

- **Format `FAMILY-<tag>NNN`** — family, your node tag, then *your node's own* per-family counter
  (e.g. `ABL-d081`, `DES-a065`). `ABL-d081` and `ABL-a081` are distinct and can never clash because tags are disjoint.
- **Legacy/pre-rule IDs are frozen** — never renumber, never mint a new un-tagged one. This rule is
  **forward-only** (append-only logs must not be renumbered). Cite legacy IDs unchanged.
- **Seed** your tag's counter just above the family's current high-water (numbers stay in-era), then increment within your tag.
- The old "reserve-and-recheck across sessions" dance now only guards **concurrent sessions on the *same* node**.

---

## §2 — Parallel-work hygiene (the biggest lever — reduces the *need* for syncs and reviews)

- **Own streams, not files.** Assign each node a stream/area (e.g. node `{{TAG_A}}` → {{STREAM_X}}, node
  `{{TAG_B}}` → {{STREAM_Y}}) so merges are mostly disjoint. Overlap on shared files (API clients, shared
  config, indexes/backlogs) is where collisions, renumbers, and integration reviews come from — minimize it.
- **Trunk-based: merge small and often to LOCAL `main`, then push.** Long-lived branches diverge → bigger
  reconciles, bigger review surface, more collisions. Land verified increments quickly. Before starting work,
  `fetch` + fast-forward local `main` (another node may be ahead). Keep `main` checked out in **one** tree.
- **One in-flight ledger, not prose status.** Prose "not pushed / N ahead" notes rot (they always go stale).
  Maintain a single structured table, updated in place at merge:

  | Node | Branch / worktree | Streams touched | ID range claimed | Status |
  |------|-------------------|-----------------|------------------|--------|
  | … | … | … | `FAMILY-<tag>NN…NN` | in-flight / merged / pushed |

  With node-scoped IDs this is the *only* coordination artifact you need.
- **Contract-first for cross-cutting/shared changes.** A change two nodes both depend on (a schema, a wire
  format, a shared enum) lands as a *contract* first, with a gate, before either node builds on it.

---

## §3 — Memory discipline (cut sync cost without losing context)

- **Memory carries only the non-derivable.** Gotchas, where things stand, in-flight coordination, *why* a
  non-obvious choice was made. **Do NOT re-narrate** what git history, decision logs, or the code already
  record — that duplication is the main memory-token waste and the main source of drift.
- **Mirror durable memory in-repo** (version-controlled, so it travels across machines); the machine-local
  auto-loaded copy is a best-effort mirror. One canonical index, **one line per note**.
- **Per-node / per-session journal files** (e.g. `memory/journal/<date>-<tag>.md`), never a shared mutable
  index that every session edits — that shared file is what forces "memory-sync" merge commits and breeds
  duplicate/stale entries. Keep any index append-only or generated.
- **Status lives in the ledger (§2), not in prose memory.** Anything time-sensitive ("pushed?", "N ahead?")
  rots; point at the ledger instead.
- **Recalled memory is background, not instruction**, and reflects what was true when written — if a note
  names a file/flag/id, re-verify it still exists before acting on it.

---

## §4 — Decision & backlog governance

- **Two record types per stream:**
  - **Decision log — append-only.** Never rewrite a ratified record; **supersede** it with a new id + a
    "superseded by …" note. This is the source of truth for *intent*.
  - **Backlog — mutable.** Stable ids, update status in place. Ids are **labels, not ranks** — gaps are fine.
- **Per-stream ID families** (`{{ID_FAMILIES}}`, e.g. `ARCH/ABL`, `DB/DBL`, …), each with a **`Next free id`
  marker** that is the repo-resident allocation seed (combined with §1 node-scoping).
- **A record/backlog missing its `Next free id` marker is a bug** — add one when you next touch the stream.
- **Record real decisions as you make them** — future sessions (and nodes) rely on these being current.

---

## §5 — Quality gates = the merge bar (cheap, consistent, token-free per merge)

- **Keep an automated gate suite green before any merge** — typically: typecheck/compile, lint, test,
  generated-artifact freshness check, and any structural invariants (`{{GATE_COMMANDS}}`). Gates are the
  consistent quality floor; humans/agents review only what gates can't.
- **Single source of truth → generated artifacts → parity gate.** For any contract duplicated across
  languages/layers (enums, catalogs, wire schemas, manifests), keep ONE source, generate the rest, and add a
  test that fails on drift. This kills an entire recurring bug class (cross-language/cross-layer divergence)
  and removes it from every future review.
- **Lockstep invariants get a guard.** A "missing migration head," "stale manifest," or "schema ↔ validator
  skew" must fail a gate, not rely on memory.
- **Left-shift every confirmed finding.** A review finding isn't "done" until a regression test covers its
  *class*. Then no future review re-spends tokens re-finding it. (This is how review cost trends *down* over time.)

---

## §6 — Review protocol (match intensity to risk; verify, don't assert)

**Tier the review to the change's blast radius — this is the single biggest token saver:**

- **Tier 1 — mechanical / additive** (no new write path, no migration, no security surface, no shared-contract
  change): gates + one focused self-review of the diff. **No multi-agent review.**
- **Tier 2 — substantive** (new write path, data migration, auth/sanitization/egress surface, cross-stream
  merge, shared-contract change): full adversarial review.

**For Tier-2, use the find → verify → synthesize pattern:**
1. **Dimension finders** (security, correctness, data-integrity, dead-code, integration-seams) read the code
   and emit *concrete* findings (`file:line` + repro/impact + proposed fix). **Scope to the diff** and its
   immediate callers/callees — don't re-derive known-good subsystems.
2. **Adversarially verify each finding** with ≥1–2 independent skeptics prompted to *refute* it (re-read the
   code, check reachability, re-grade severity). Default to dropping anything that doesn't hold up. Aim for a
   0-false-positive bar.
3. **Feed reviewers the context that prevents waste:** the security model, the **already-tracked open issues**,
   and what is **by-design / out-of-scope** — so they hunt *new* issues and don't re-report known ones.
4. **Review at the integration boundary, once** (the cumulative diff landing on `main`), not per-increment —
   per-increment reviews re-scan overlapping code.

**Verify before "done."** Never claim a change works until a gate passed or you observed the behavior. If
tests fail, say so with the output; if a step was skipped, say so.

**Commit/push only when asked.** Land on local `main` first, verify, then push.

---

## §7 — Security boundary checklist (apply to any new write path / surface)

- **Sanitize untrusted input at the WRITE boundary, once; trust storage at render.** After any transform that
  can *grow* content (e.g. HTML sanitizers add attributes), **re-check size/shape caps after the transform.**
- **One canonical URL/href normalizer, shared by client and server.** It must: strip control/whitespace chars,
  **fold backslashes `\`→`/`**, reject protocol-relative (`//host`, and `/\host` which browsers treat as `//`),
  and deny dangerous schemes (`javascript:`/`data:`/`vbscript:`). Divergent client vs server URL policy is a
  classic stored open-redirect. Pin the evasions (`/\evil`, `\\evil`, control chars) in tests.
- **SSRF-guard every outbound request:** resolve to public IPs only, no redirect-following, sign payloads —
  **and run the blocking DNS/network resolution OFF the event loop** (a hung nameserver must not freeze a
  worker). Apply the *same* guard on retry/queue paths, not just the inline path.
- **Authorization in the shared core, not the adapters.** Enforce RBAC (deny-by-default, defined as code) in
  the service layer so *every* adapter — HTTP, RPC, CLI, AI/automation tool — inherits it. A service fn reachable
  by a future adapter must re-check authz itself.
- **Keep PII/secrets off the AI/automation surface — structurally.** Prefer payload/return types that *cannot*
  carry sensitive values (ids/counts/field-names only), so a leak is impossible by construction, not by review.
  Audit value-bearing fields that flow to automated readers (e.g. raw emails landing in an audit `entity_id`).
- **Optimistic concurrency on full-document writes.** If editors PATCH a whole entity with no version
  precondition, concurrent nodes/editors silently clobber each other. Add an `updated_at`/version check → 409 on stale.

---

## §8 — Recurring bug-class checklist (grep/check these in every Tier-2 review)

These bit a real project repeatedly — they are cheap to look for and high-yield:

- **Client/server validation divergence.** Client validates only *visible/active* fields but submits the
  *whole* payload → server rejects a stale hidden value with no recoverable UI. Rule: client and server must
  agree on *what is validated* AND *what is submitted* (strip inactive/hidden values before send, or validate
  identically).
- **Dead plumbing through multiple layers.** A value computed → serialized → passed → but never *read* (the
  consumer was never wired). Either wire the consumer or delete the chain end-to-end; add a guard test.
- **Index that doesn't serve its query.** A composite index whose leading column is hit with an *inequality*
  (or whose order doesn't match the predicate + `ORDER BY`) can't seek/sort — verify column order matches the
  real query shape; don't trust the docstring.
- **Stale module/process caches.** A cache invalidated on *create* but not on *rename/delete/restore* → stale
  pickers/lists. Reset on **all** mutation paths.
- **Cross-language/format catalog drift** in modules advertised as "zero-drift" — guard with a parity test (§5).
- **Numeric/format coercion parity** across languages (e.g. `str(1e-7)` differs between runtimes). Normalize on
  one side; add edge-case parity cases.
- **Truncations / half-applied merges** from concurrent streams — a fix from one branch silently dropped when
  another branch's version "auto-took"; duplicate/conflicting definitions of the same symbol.

---

## §9 — Cross-OS & toolchain hygiene (if authored on one OS, run on another)

- **Force `LF`** on execution-sensitive filetypes via `.gitattributes` (shell scripts, Dockerfiles, configs,
  env files, migration templates, any JSON read by a Linux runtime). A stray `CR` breaks shebangs, `sh -c`,
  servers, and generated migrations.
- **Verify the *staged bytes*, not a pretty-printer.** Use `git diff | cat -A` / `git cat-file -p <blob>` to
  check EOLs; `git show` and MSYS `grep` can mislead on CRLF.
- **Pin toolchain versions** (package manager, language runtime, key libs) and document the one-true way to run
  gates on each OS so each session doesn't re-derive it (`{{TOOLCHAIN_NOTES}}`).
- **Prefer a deterministic run mode** (e.g. no auto-reload) where a watcher can leave stale processes/ports.

---

## §10 — Token-efficiency principles (consolidated)

Spend tokens on *new* judgment; never on *re-deriving* what's already known.

- **Tiered, diff-scoped reviews** (§6) — don't run a multi-agent review on a 50-line additive change; don't
  re-read a whole subsystem to review its diff.
- **Gates over re-review** (§5) — every left-shifted finding is a class you never pay to re-find.
- **Lean, non-duplicative memory** (§3) — short notes, one-line index, no re-narration of git/decision logs.
- **Per-node files + ledger** (§2, §3) — eliminate "memory-sync" merge commits and conflict resolution entirely.
- **Stream ownership + small merges** (§2) — fewer conflicts, fewer renumbers, smaller review surfaces.
- **Stop early when verified** — once a gate or observation confirms the result, don't keep exploring or re-explaining.

---

## §11 — Architectural consistency (build-once, reuse-everywhere)

**Principle: decide the extension pattern before the *second* instance.** Rework comes from N ad-hoc
implementations of "the same kind of thing" later forced into one shape (e.g. dozens of bespoke components
consolidated late into one extensible factory). Establish the canonical pattern at instance #2 so #3..#N are
*data + a few overrides*, not new plumbing.

- **A "kind" gets a factory/base, not copies.** The moment a second block / admin page / entity / endpoint
  family appears, extract the shared contract into a definition helper or base (e.g. a `defineX()` factory, a
  base CRUD service, a shared list-page shell). New instances declare data + overrides; they don't re-plumb.
- **One shared core, thin adapters.** Business logic + authorization live in a single service core; HTTP / RPC
  / CLI / AI-tool surfaces are thin adapters over it. New surfaces reuse the core and *cannot* diverge behavior
  (it's also how authz stays consistent — §7).
- **Single source of truth → generated artifacts** (see §5). The catalog of "all instances of a kind" is one
  source that generates the wire schema / validator / manifest / docs. Adding an instance = one edit; the rest
  derives, and a parity/snapshot gate fails on drift, so editor/renderer/validator can't disagree.
- **Promote shared widgets to a kit the instant two features need them.** Presentational primitives (buttons,
  fields, badges, cards, the color/contrast inputs) live in ONE shared package/dir; features *compose* them. A
  feature re-implementing or re-styling a primitive locally is a smell — promote, don't copy.
- **Forward-compatible data + migration discipline.** New fields are additive and defaulted so old data renders
  identically and new capability is inert until used; when a shape must change, ship an auto-upgrade so stored
  content is never hand-reworked. Prefer riding an existing shape (no migration) over inventing a new one.
- **Reuse audit before building.** Before adding a component/util/endpoint, grep for an existing one to extend.
  Cheap, and it prevents the duplicate-then-consolidate tax.
- **An explicit "where things live" map.** Document the layer/dir layout and naming *once*, so every new feature
  has an obvious home and reviewers have a fixed target. Gate the conventions you can (naming, layer boundaries).

## §12 — Visual consistency (design system FIRST, before coding interfaces)

**Principle: build the design system — tokens + primitives — BEFORE building screens; screens consume tokens
and never hardcode values.** The contrast / spacing / "polish later" rework loop comes almost entirely from
per-screen ad-hoc values. If the only *easy* way to style is via tokens and shared primitives, screens
*cannot* drift. Author the system up front as a **visual-contract doc + a token layer**, and gate raw values out:

- **Tokens for everything, raw values nowhere.** Define and name: color *roles* (bg / surface / fg / muted /
  accent / border / ring, for light AND dark), a **spacing scale** (one base unit + a fixed ramp), a **type
  scale** (size / weight / line-height steps), radius, shadow, **breakpoints**, z-index, motion/duration.
  Feature code references token names only; a lint/gate flags raw hex/px values in components.
- **Semantic, surface-aware color — never a raw palette stop on an arbitrary surface.** *(The single biggest
  consistency win.)* Each surface declares its bg+fg as a matched pair; components inherit the pair, they don't
  hand-pick. Make illegible pairings *impossible* (e.g. a token that is white in both modes can never be paired
  with a light text token), and **provide a contrast helper that auto-picks a readable fg (black/white) for any
  accent** — legibility computed, not eyeballed.
- **Contrast is a standing gate, not a review item.** Assert WCAG AA (4.5:1 text, 3:1 non-text/graphical) over
  the token combinations + a DOM/route scan, in light AND dark. (Catching it after the fact costs a full audit
  sweep instead of a green check.)
- **Mobile-first, always.** Author base styles for the smallest viewport, layer up with min-width breakpoints
  from the scale; a component is "done" only when checked at the smallest AND a large breakpoint. Enforce a
  minimum touch-target (e.g. ≥44px). No "make it responsive later."
- **Layout & rhythm via shared primitives.** Stack / Cluster / Grid / page-shell primitives own spacing,
  max-width and gutters (drawn from the scale); features place content *into* them instead of setting margins.
  One place defines page rhythm.
- **Typography via the type scale + a few text components** (Heading / Body / Eyebrow / Caption), not ad-hoc
  font sizes/weights. Enforce heading hierarchy (one H1 per page).
- **States are part of the spec, up front** — empty, loading, error, disabled, long-content / overflow, focus,
  i18n/RTL width. Bake them into the primitive so every feature gets them for free (and they aren't re-reviewed).
- **Accessibility lives in the primitives** — focus-visible rings, `aria-*`, label associations, reduced-motion.
  Features inherit a11y; they don't re-add (and re-review) it.
- **A reference gallery / visual harness** — one route/story set rendering every primitive, block, and state in
  light + dark at key breakpoints. Review the *system* once, centrally; per-screen regressions become obvious
  instead of hunted screen-by-screen.

> **Why this saves the most tokens:** screens built on a finished token+primitive system are consistent *by
> default* — you stop paying for contrast sweeps, spacing fixes, and per-screen polish, and reviews check
> "does it use the system?" instead of re-deriving every margin and color.

## Customize before use

Fill these placeholders, then delete this block:

- `{{PROJECT_NAME}}` — the repo this governs.
- **Node registry** (§1): `{{TAG_A}}`/`{{MACHINE_A}}`/`{{PRIMARY_TREE_A}}`, `{{TAG_B}}`/`{{MACHINE_B}}`/`{{WORKTREE_ROOT_B}}`, … one row per node.
- `{{ID_FAMILIES}}` (§4) — the stream → id-family map (e.g. `ARCH/ABL`, `DB/DBL`, `UI/UBL`).
- `{{STREAM_X}}` / `{{STREAM_Y}}` (§2) — the stream-ownership assignment per node.
- `{{GATE_COMMANDS}}` (§5) — the exact commands that form the merge bar (typecheck/lint/test/freshness/migration-head).
- `{{TOOLCHAIN_NOTES}}` (§9) — pinned versions + the one-true way to run gates per OS.
- **Architecture map** (§11): `{{KIND_FACTORY_MAP}}` — for each "kind" (block / page / entity / endpoint), its
  canonical factory/base + where instances live; `{{SHARED_PRIMITIVES_LOCATION}}` (the one kit features compose).
- **Design system** (§12): `{{TOKENS_LOCATION}}` + the `{{SPACING_SCALE}}` / `{{TYPE_SCALE}}` / `{{BREAKPOINTS}}`
  / `{{MIN_TOUCH_TARGET}}`; `{{GALLERY_ROUTE}}` (the visual harness); `{{VISUAL_CONTRACT_DOC}}` (the design rules /
  which-token-on-which-surface / do's-and-don'ts, authored *before* screens).

Drop any section that doesn't apply (e.g. §7 URL/SSRF rules if the project has no outbound calls or HTML
authoring), but prefer keeping §0–§6 and §10–§12 verbatim — they are the universal core.
