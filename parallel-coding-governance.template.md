# Parallel Multi-Node Coding — Governance Template

*Template **v1.4** · last updated 2026-06-30. When you instantiate this in a repo, record the adopted
version in the copy; diff your copy against this source by `§` heading body (ignore filled `{{…}}` + the
deleted Customize block) to pull in improvements. Change history: the `…-v-N-N.md` snapshot files
alongside this one (this folder isn't a git repo).*

<!-- governance-template: v1.4 -->

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

1. **Session-scope every new ID** (slug = your node tag + a CamelCase adjective-noun) so concurrent sessions/nodes can't collide (§1). Collisions become *impossible*, not *avoided*.
2. **Partition work by stream ownership** so nodes touch disjoint files; **merge small and often** to local `main` (§2).
3. **Memory holds only what git + decision logs don't** — non-derivable state, gotchas, in-flight coordination. Per-node files, no shared mutable index (§3).
4. **Gates are the merge bar; reviews are for what gates can't check.** Tier review intensity to blast radius. Turn every confirmed finding into a permanent gate (§5, §6).
5. **Verify before claiming done** — a passing gate or an observed result, never an assertion (§6).
6. **Consistency by construction, not correction.** Build the design system (tokens + primitives) and the extension pattern (factories + one shared core) *before* the screens/features that use them, and gate raw values out — polishing inconsistency in afterward is the expensive path (§11, §12).

---

## §0.5 — Work-unit lifecycle (start → done → land)

The numbered sections are the *principles*; this is the *sequence* every unit of work runs through. Keep
units **small** = touches one stream/owner, needs no cross-stream contract change, reviewable as a single
Tier-1 diff (§6); if it would span streams or need its own Tier-2 review, split it.

**Before you start — Definition of Ready.** Run before touching code:
1. **Sync** — `fetch` + fast-forward local `main` (another node may be ahead); recreate/repair your worktree if needed.
2. **Locate** — read your stream's decision log + backlog (§4) and the **in-flight ledger** (§2); confirm your **node tag** (§1).
3. **Scope** — the unit has clear acceptance criteria, fits one stream/owner (§2), is small, and names the gate(s) it must pass (§5). If you can't state those, it isn't ready — split or clarify first.
4. **Reserve** — at your session's first work-unit, mint + grep-check a session slug (§1); add a ledger row (§2). No marker to bump.

For a **large/new feature** (a Tier-2 change with substantial new capability — small/Tier-1 skips this) the
DoR *is* a design pass: turn the user's instructions into a **written spec** (goal · scope · non-goals ·
acceptance criteria), then a **bounded checklist of production-readiness recommendations** (best-practice
implementation + the extra tools/features and cross-cutting concerns — security · perf/scale · a11y · i18n ·
error/empty/loading states · observability · testing+gates · migration/rollback · the `{{HELP_DIR}}` docs);
**get scope approval BEFORE building** (a menu to select from, not scope-creep licence); record the agreed
spec via the project's plan/decision convention (§4).

**Before you call it done — Definition of Done.**
- Gates green (§5); the change is **verified, not asserted** (§6).
- Every confirmed finding is **left-shifted** (§5) — a gate, or (if its class can't be gated) a §8 checklist entry — not merely fixed.
- **If the change is user-facing**, its `{{HELP_DIR}}` page is created/updated (§3).
- Memory updated (non-derivable only, §3); decision/backlog updated (§4); ledger row current (§2). Commit is automatic; the merge to `main` + push happen only when asked (§6).

**Landing it — merge protocol.**
- Land on **local `main` first**, verify, then push; commit/push only when asked (§6).
- **Re-run the full gate suite after *every* merge** — a clean (conflict-free) merge is not a passing merge.
- Reconcile shared mutable files (backlogs, ledger, indexes) **additively — never pick-a-side**; then diff the
  merge against *both* parents to confirm no edit was silently dropped (the "auto-took" bug class, §8).
- **Land risky behavior dark** — any **Tier-2 change** (§6) ships behind a **default-OFF flag** (or as inert,
  defaulted data), flipped on only after it's verified in place; migrations are **reversible** (test up/down/up).
  Risky work can then merge without endangering other nodes, and reverts cleanly.

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

**Session-scoped IDs — REQUIRED on every new tracked id** (decisions, backlog items, tickets, TODO refs —
anything with a `FAMILY-NNN` shape). Every id is owned by the **session** that mints it, so nothing it numbers
can be contested:

- **Format `FAMILY-<slug>-<seq>`** — family, your *session slug*, then a per-`(session, family)` counter
  (e.g. `ABL-dAvengingTrousers-3`, `DES-aMasterfulNinjas-12`). The only `-` in an id are its two structural separators.
- **The slug = your node tag (§1 registry) + a fresh CamelCase adjective-noun** (`dAvengingTrousers`), charset
  `[A-Za-z]` only — the node-tag letter + CamelCase words, **no hyphen/space/digit/punctuation**. Mint it ONCE at
  your session's first work-unit; it labels every id the session creates, across every family. The node-tag first
  letter makes cross-node slugs disjoint *by construction*.
- **`<seq>` is a plain 1-up counter within `(your session, that family)`**, from `1`, unpadded. Ids are labels,
  not ranks (`-2` precedes `-10` lexically — nothing sorts them) — to get your next, take the numeric max of YOUR
  ids in that family **+ 1**. Record your per-family high-water in your ledger row (§2) so a resumed / cross-tree
  session re-derives it from one place, not from grep (uncommitted ids are invisible to grep).
- **No reserve-above-a-marker, no shared counter to bump, no renumber-on-merge** — the slug *is* the guarantee.
  Two cheap one-time checks at your first work-unit guard same-node / all-time collisions, **before** you commit to a slug:
  1. **All-time** — grep the tracked governance-docs tree (decision logs, backlogs, journals, the ledger) for
     `[A-Z]+-<slug>-[0-9]`. Re-roll on any hit: ids are permanent, so a retired slug whose ledger row was pruned still owns its ids.
  2. **Concurrency** — glance at the live in-flight ledger rows (§2); re-roll on a clash with an in-flight session
     whose ids aren't committed yet.
  Then add your ledger row. That's the whole protocol.
- **A session = one continuous effort under one slug** (it may span several work-units and touch several families
  — one `<seq>` each). A **resumed / summarized** session keeps its slug (the all-time grep hits only your own
  prior ids — keep it, don't re-roll). **Fan-out children** (sub-agents / orchestrated workers) do NOT mint ids —
  the orchestrator does; a child that must mint takes its own registered slug.
- **Forward-only** (append-only logs must not be renumbered). **Residual tie-break:** if two sessions still land
  the same slug (sub-1%, caught above), the later-to-merge re-mints its slug for all UNMERGED ids; an already-merged
  decision-log id wins.

The node registry above stays: the tag seeds the slug's first letter and keeps cross-node slugs disjoint.

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

  | Node | Slug | Branch / worktree | Streams touched | Seq high-water | Status |
  |------|------|-------------------|-----------------|----------------|--------|
  | … | `dAvengingTrousers` | … | … | one token per family, e.g. `ABL-3 DES-12` | `in-flight`/`merged`/`pushed:<sha>` |

  Keep cells terse — Status is one of `{in-flight | merged | pushed:<sha>}` plus at most one short clause; full
  narrative belongs in the journal/decision log, never here. The **Seq high-water** cell is each family's max
  `<seq>` this session (§1) — your one source for the next id, so a resumed/cross-tree session needn't grep for it.
  **Prune to stop unbounded growth:** stamp the merge SHA on a pushed row, and when starting work delete any pushed
  row already in your history (`git merge-base --is-ancestor <sha> HEAD`). With session-scoped slugs this is the
  *only* coordination artifact you need.
- **Contract-first for cross-cutting/shared changes.** A change two nodes both depend on (a schema, a wire
  format, a shared enum) lands as a *contract* first, with a gate, before either node builds on it.

---

## §3 — Memory discipline (cut sync cost without losing context)

- **Memory carries only the non-derivable.** Gotchas, where things stand, in-flight coordination, *why* a
  non-obvious choice was made. **Do NOT re-narrate** what git history, decision logs, or the code already
  record — that duplication is the main memory-token waste and the main source of drift.
- **Mirror durable memory in-repo** (version-controlled, so it travels across machines); the machine-local
  auto-loaded copy is a best-effort mirror. One canonical index, **one line per note**.
- **User-facing docs are NOT memory.** Keep concise, task-oriented end-user docs (*what it does · how to use
  it · a short example*) in a tracked `{{HELP_DIR}}` (one page per feature, synced like the repo), in lockstep
  with the feature — DISTINCT from this agent-facing memory/decision-logs, which never double as user docs. A
  user-facing feature without an up-to-date page is not done (§0.5).
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
- **Per-stream ID families** (`{{ID_FAMILIES}}`, e.g. `ARCH/ABL`, `DB/DBL`, …) — the family prefix just routes
  an id to its log/backlog. Allocation is session-slug-scoped (§1), so a stream needs **no shared `Next free id`
  marker** (the slug owns the counter; the per-session high-water lives in the ledger row, §2) — one less
  shared-mutable artifact to merge-reconcile.
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
  merge, shared-contract change): full adversarial review (run the §8 recurring-bug-class checklist as part of it).

**For Tier-2, use the find → verify → synthesize pattern:**
1. **Dimension finders** (security, correctness, data-integrity, dead-code, integration-seams) read the code
   and emit *concrete* findings (`file:line` + repro/impact + proposed fix). **Scope to the diff** and its
   immediate callers/callees — don't re-derive known-good subsystems.
2. **Adversarially verify each finding** with **at least one** independent skeptic prompted to *refute* it (two
   for security / data-integrity findings) — re-read the code, check reachability, re-grade severity. **Drop any
   finding a skeptic refutes unless you can re-establish reachability + impact; when in doubt, drop it.**
3. **Feed reviewers the context that prevents waste:** the security model, the **already-tracked open issues**,
   and what is **by-design / out-of-scope** — so they hunt *new* issues and don't re-report known ones.
4. **Review at the integration boundary, once** (the cumulative diff landing on `main`), not per-increment —
   per-increment reviews re-scan overlapping code.

**Right-size the fan-out (ROI-tuned defaults).** An ROI audit of one project's review corpus — token cost vs.
severity-weighted *confirmed*-finding value, per run — converged on a default Tier-2 shape: a **parallel** fan
of **3–6 primed finder lenses → adversarial verification per finding (the verify step above) → one synthesis
pass**, **~11–25 agents total**. What actually moved value-per-token:
- **Precision (confirmed / (confirmed + refuted)) is the #1 lever** — each refuted finding ≈ a finder plus its
  skeptics spent for nothing. If a stream trends below ~0.5, the finders are over-firing: tighten scope or
  priming *before* adding agents.
- **Diminishing returns past ~25 agents** — per-finding token cost rises sharply and precision dips; bigger
  fan-outs mostly re-find the same issues. Scale a large *fresh* surface by adding **lenses** (coverage), not
  **skeptics** (verification precision saturates early).
- **The synthesis / extra-verify phase pays for itself** (find → verify → **synthesize**) — it kills marginal
  findings before they're recorded, lifting precision more than another finder would.
- **Match intensity to target richness** — heavy multi-lens earns its tokens on fresh / complex / high-blast-radius
  write paths; over already-hardened code it manufactures defense-in-depth noise that skeptics then refute, so
  review light (or skip the heavy pass) there.

**When the review (or any fan-out) runs as a multi-agent workflow with structured / JSON-schema output,
design the schema so a malformed return can't force a full regeneration** — the largest *output*-token waste
in a transcript audit was sub-agents hand-serializing huge JSON bodies that broke on an unescaped path
separator or special char, then regenerating the whole thing:
1. **Never make an agent hand-serialize a large body as JSON.** For long prose, have it write the body to a
   file and return only `{path, summary}` (use forward-slash paths — unescaped backslashes are a top cause of
   broken JSON).
2. **Re-state the schema's exact required keys in the prompt on EVERY loop iteration** — an agent iterating
   over many items forgets the shape between them and re-fails identically.
3. **Avoid strict "no extra properties" rejection unless a stray key is harmful** — accept-and-ignore beats
   reject-and-regenerate.
4. **On a validation failure, feed back only the offending field**, not "regenerate everything."
5. These outputs come from **sub-agent sidechains that don't inherit your hooks / `CLAUDE.md`**, so the
   discipline must live with the **orchestrator that defines the schema** — and since orchestration scripts
   often can't import shared code, inline it as a reusable snippet, not a library.

**Verify before "done."** Never claim a change works until a check that *exercises it* (its own/affected test,
the relevant gate, or the preview for UI) proves it — an unrelated green gate is not proof. If tests fail, say
so with the output; if a step was skipped, say so.

**Commit automatically; merge to `main` and push only when asked.** Commit freely as you go (on your branch /
worktree, or local `main` for doc-only changes). **Landing on the shared `main` and `git push` to the remote
each require an explicit ask** — that's how work reaches other nodes.

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
- **ID-scheme drift** (documented check — no machine gate fits). New ids are session-scoped `FAMILY-<slug>-<seq>`
  (§1): don't reuse a slug the all-time grep already finds, don't mint a pre-rule un-slugged id, and don't
  renumber an append-only record. A pruned ledger row still owns its ids (they're permanent).

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
- **In a POSIX-emulation shell on Windows** (MSYS / Git-Bash / Cygwin), native backslash paths passed to a
  tool's working-dir flag are mangled — e.g. `git -C C:\repo` becomes `fatal: cannot change to 'C:repo'`. Use
  forward-slash (`/c/repo`) or quoted (`"C:/repo"`) paths in that shell; the native Windows shell takes
  backslashes fine. A zero-false-positive PreToolUse hook can block the broken form, since a backslash drive
  path never works there.

---

## §10 — Token-efficiency principles (consolidated)

Spend tokens on *new* judgment, never on re-deriving what's already known: tier + diff-scope reviews (§6);
gate over re-review — left-shift findings (§5); keep memory + ledger lean (§2, §3); own streams + merge small
(§2); design-system-first so screens are consistent by construction (§11, §12); **stop once verified** (§6);
cut per-call waste — never re-read or re-dump what's already in context (§13).

---

## §11 — Architectural consistency (build-once, reuse-everywhere)

**Principle: decide the extension pattern before the *second* instance.** Rework comes from N ad-hoc
implementations of "the same kind of thing" later forced into one shape (e.g. dozens of bespoke components
consolidated late into one extensible factory). Establish the canonical pattern at instance #2 so #3..#N are
*data + a few overrides*, not new plumbing.

- **A "kind" gets a factory/base, not copies.** The moment a second block / admin page / entity / endpoint
  family appears, extract the shared contract into a definition helper or base (e.g. a `defineX()` factory, a
  base CRUD service, a shared list-page shell) — the per-kind map is `{{KIND_FACTORY_MAP}}`. New instances declare data + overrides; they don't re-plumb.
- **One shared core, thin adapters.** Business logic + authorization live in a single service core; HTTP / RPC
  / CLI / AI-tool surfaces are thin adapters over it. New surfaces reuse the core and *cannot* diverge behavior
  (it's also how authz stays consistent — §7).
- **Single source of truth → generated artifacts** (see §5). The catalog of "all instances of a kind" is one
  source that generates the wire schema / validator / manifest / docs. Adding an instance = one edit; the rest
  derives, and a parity/snapshot gate fails on drift, so editor/renderer/validator can't disagree.
- **Promote shared widgets to a kit the instant two features need them.** Presentational primitives (buttons,
  fields, badges, cards, the color/contrast inputs) live in ONE shared kit (`{{SHARED_PRIMITIVES_LOCATION}}`); features *compose* them. A
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
*cannot* drift. Author the system up front as a **visual-contract doc (`{{VISUAL_CONTRACT_DOC}}`) + a token layer (`{{TOKENS_LOCATION}}`)**, and gate raw values out:

- **Tokens for everything, raw values nowhere.** Define and name: color *roles* (bg / surface / fg / muted /
  accent / border / ring, for light AND dark), a **spacing scale** (`{{SPACING_SCALE}}`), a **type scale**
  (`{{TYPE_SCALE}}`), radius, shadow, **breakpoints** (`{{BREAKPOINTS}}`), z-index, motion/duration.
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
  minimum touch-target (`{{MIN_TOUCH_TARGET}}`, e.g. ≥44px). No "make it responsive later."
- **Layout & rhythm via shared primitives.** Stack / Cluster / Grid / page-shell primitives own spacing,
  max-width and gutters (drawn from the scale); features place content *into* them instead of setting margins.
  One place defines page rhythm.
- **Typography via the type scale + a few text components** (Heading / Body / Eyebrow / Caption), not ad-hoc
  font sizes/weights. Enforce heading hierarchy (one H1 per page).
- **States are part of the spec, up front** — empty, loading, error, disabled, long-content / overflow, focus,
  i18n/RTL width. Bake them into the primitive so every feature gets them for free (and they aren't re-reviewed).
- **Accessibility lives in the primitives** — focus-visible rings, `aria-*`, label associations, reduced-motion.
  Features inherit a11y; they don't re-add (and re-review) it.
- **A reference gallery / visual harness** (`{{GALLERY_ROUTE}}`) — one route/story set rendering every primitive, block, and state in
  light + dark at key breakpoints. Review the *system* once, centrally; per-screen regressions become obvious
  instead of hunted screen-by-screen.

> **Why this saves the most tokens:** screens built on a finished token+primitive system are consistent *by
> default* — you stop paying for contrast sweeps, spacing fixes, and per-screen polish, and reviews check
> "does it use the system?" instead of re-deriving every margin and color.

## §13 — Session execution hygiene (per-call token discipline)

§10 is the *strategy* (never re-derive known judgment); this is the *per-tool-call mechanics* that stop an agent
re-spending tokens on its own outputs — the dominant avoidable spend in a transcript audit (re-reads, uncapped
command output, hand-polling, edit/format ordering). The principles are harness/OS-agnostic; swap in your tool names.

- **Don't re-fetch what's already in context.** Agent harnesses track file state across the agent's own edits,
  so re-Reading a file just to keep editing it — or to "verify" an edit the tool already confirmed — is pure
  waste. Re-Read only when the file actually changed (next bullet). Need one slice of a large file? read a range
  or `grep` it; don't re-read it whole. **Never re-Read a command-output spill / large generated artifact** —
  filter it at generation (`grep`/`head`) instead of dumping it back in.
- **Re-Read before editing ONLY when something outside your own edits changed the file:** after you ran a
  formatter or `--fix` on it, when a format-on-save hook is active, or when a concurrent node may have edited a
  shared file. Make manual edits FIRST and run the formatter/`--fix` LAST (or re-Read after it) — reformatting
  *between* two edits is the classic "file modified since read → forced re-read" loop. Batch a file's edits
  before any reformat step; use a multi-edit primitive if your harness has one.
- **Bound every command's output — it all enters the transcript whether or not it's read.** Never pipe a raw
  full diff in; use `--stat`/`--name-only`, then read only the hunks you need. Cap noisy tails: the linter's
  terse/concise format; head/tail to the last N lines for build/typecheck; quiet flags for tests.
- **Don't poll background work — prefer completion signals.** If the harness auto-notifies on task completion
  (or offers a blocking wait/monitor primitive), use that; never repeatedly tail/grep a running task's output
  file (read it once, after it finishes). Reserve an explicit wait-loop for *external* conditions the harness
  can't track (a healthcheck, a remote CI run).
- **Lint/check the files you changed while iterating; reserve the full-repo gate for merge.** When a check
  reports many fixable items in one file, fix them in a SINGLE batch then re-run once — don't fix-one-then-recheck.
  Know which findings the auto-`--fix` can't resolve (e.g. line length needing a manual wrap) so you don't re-run
  expecting them to clear.
- **Pin a review/diff base to an immutable SHA, not a moving ref** — a concurrent node can repoint the shared
  base mid-task: `BASE=$(… rev-parse <ref>); diff "$BASE"...HEAD`. Run the full diff once; re-check with `--stat`
  only. (Cross-OS path-form gotchas for VCS `-C`/working-dir flags live in §9.)
- **Don't let a no-match `grep` fail an `&&` chain.** `grep`/`grep -c` exits non-zero on zero matches, so a
  *passing* check short-circuits the chain and reads as failed. Use a purpose-built check, or terminate the
  probe with `;` / `|| true`.

## §14 — Voice (how you talk to the user)

When you write **to the user** (chat responses, summaries, PR/commit prose addressed at them), use one
**deliberate, consistent voice**, and address the user directly as **"you"** (second person). The recommended
default persona is **cheeky, dry, faintly sarcastic but genuinely friendly** — the sharp colleague who ribs you
while shipping the fix, not a support-bot reading a script off a card; reading back through a session should feel
a little *fun*, not like skimming a compliance report. *(The persona is the one knob here — swap in a different
tone if it suits your project; the rules below are what's universal and non-negotiable.)*

**The wit is seasoning; the FACTS are the meal — and the wit NEVER bends the meal.** Tone may flavor *how* you
say a thing; it may never change *what's true*. Every number, path, `id`, caveat, "this failed", "I skipped
that", "I'm not sure", and "I didn't verify it yet" stays exactly as accurate, complete, and un-sugar-coated as
it would be stone-faced. If a joke would blur a fact, **kill the joke, keep the fact** — no rounding-for-the-
punchline, no false confidence for a snappier line. Bad news, security findings, broken gates, and "your code is
wrong" get delivered *straight* — be wry about the situation, never evasive about the truth. Read the room: when
you're delivering a genuinely bad outcome, dial the cheek down — friendly, not flippant.

Keep it natural, not a bit: dry > loud, a light touch > forced zaniness, and an honest quiet line beats a
chipper "Sure! Happy to help!! 🎉". **This governs prose aimed at the user only.** Decision logs, code comments,
migrations, and test names stay as precise and deadpan as they already are — a joke does not belong in a migration.

## §15 — User-facing file references (make them clickable)

When you cite a file in **output aimed at the user** (chat, summaries, reviews), format it so the client renders
it as a **link they can open in one click** — not a raw string to copy-paste and hunt down. Two failure modes recur:

- **Resolve the href from the SESSION working directory — which, in the §2 layout, is NOT the repo root.** When
  worktrees are siblings under a root and the session opens at the **worktree _parent_** (cwd = the root, not a
  worktree), a path written relative to the *repo root* (`docs/foo.md`) silently **drops the worktree-folder
  segment** and points at nothing. Prefix the worktree folder, forward-slashed: `[foo.md](main/docs/foo.md)`.
  *(Repo-internal doc prose may keep its own repo-root-relative convention — this rule governs references shown to
  the **user**.)*
- **Use the one link format your client actually linkifies, and verify it by clicking.** Some clients linkify
  **only inline-link markup** (commonly GFM `[text](path)`) and leave bare or absolute paths inert
  (copy-paste-only); a mixed-separator string (`C:\…/…`) is a frequent non-linkifying culprit. Standardize on the
  format that clicks, forward-slashed throughout — don't assume it works, confirm once.

## Customize before use

**Who does this:** the agent (Claude), as a one-time setup pass — it **reads the repo** to fill the
discoverable placeholders, **asks the user only for what isn't in the code** (the items tagged *(ask user)*
below — the node fleet and the stream-ownership policy), **proposes-and-flags anything it had to infer**, then
**deletes this block**. After filling, `grep '{{'` to confirm no placeholder survived.

- `{{PROJECT_NAME}}` — the repo this governs.
- `{{HELP_DIR}}` (§3, §0.5) — the tracked user-facing docs folder (one task-oriented page per feature).
- **Node registry** (§1) *(ask user)* — `{{TAG_A}}`/`{{MACHINE_A}}`/`{{PRIMARY_TREE_A}}`, `{{TAG_B}}`/`{{MACHINE_B}}`/`{{WORKTREE_ROOT_B}}`, … one row per node.
- `{{ID_FAMILIES}}` (§4) — the stream → id-family map (e.g. `ARCH/ABL`, `DB/DBL`, `UI/UBL`).
- `{{STREAM_X}}` / `{{STREAM_Y}}` (§2) *(ask user)* — the stream-ownership assignment per node.
- `{{GATE_COMMANDS}}` (§5) — the exact commands that form the merge bar (typecheck/lint/test/freshness/migration-head).
- `{{TOOLCHAIN_NOTES}}` (§9) — pinned versions + the one-true way to run gates per OS.
- **Architecture map** (§11): `{{KIND_FACTORY_MAP}}` — for each "kind" (block / page / entity / endpoint), its
  canonical factory/base + where instances live; `{{SHARED_PRIMITIVES_LOCATION}}` (the one kit features compose).
- **Design system** (§12): `{{TOKENS_LOCATION}}` + the `{{SPACING_SCALE}}` / `{{TYPE_SCALE}}` / `{{BREAKPOINTS}}`
  / `{{MIN_TOUCH_TARGET}}`; `{{GALLERY_ROUTE}}` (the visual harness); `{{VISUAL_CONTRACT_DOC}}` (the design rules /
  which-token-on-which-surface / do's-and-don'ts, authored *before* screens).

Drop §7 (no outbound calls / HTML authoring) or §9 (single-OS) when they don't apply; everything else —
§0, §0.5, §1–§6, §8, §10–§15 — is universal core: keep it verbatim (§8's cross-refs in the lifecycle and §6
assume it's present). The one exception is **§14's persona** — the cheeky-dry default is adjustable per project,
but its facts-over-wit / bad-news-straight / user-facing-prose-only rules are not.
