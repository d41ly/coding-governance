# Governance domain rules — runtime, cross-OS, architecture, security, recurring bugs & design system

Companion to `parallel-coding-governance.template.md`, holding six activity-scoped domain sections the
template references by section number rather than inlining (they apply only when a unit touches a
risky surface or runs a Tier-2 review). Deploy this file alongside the playbook; the template's §4, §9, §10, §11, §12 and §13 stubs point here. All are droppable-per-project (see the customize companion).

## §4 — Runtime isolation & the verification harness

- Concurrent sessions share machines: local review/preview stacks bind canonical+offset host ports (`{{PORT_OFFSET}}`) so simultaneous stacks can't collide — the runtime analogue of session-scoped IDs.
- Servers sharing one canonical port run one-at-a-time; free the port FIRST (a stale listener silently serves the WRONG code); kill the listener by port, never blanket-kill every process of that runtime.
- Know which config is baked at BUILD time vs read at runtime (`{{BUILD_TIME_BAKES}}`): changing a baked value means rebuilding the artifact with matching values, not restarting it.
- In a sibling-worktree layout, workspace/monorepo tooling launched from the worktrees' PARENT resolves a scope spanning ALL siblings and fails or fans out — launch commands must `cd` into exactly one worktree first.
- Maintain a proven full-stack verify recipe (`{{VERIFY_RECIPE}}`: throwaway DB → migrate → seed an admin → background services → drive the UI harness and assert) — a maintained artifact, not tribal knowledge.
- Pin the harness launch config PER NODE in the §2 registry; an un-pinned node creates it on first use and registers it in the same change.
- Document the harness's false-signal modes (stale snapshot after a backend restart, wedged screenshot, a probe reading 0 in headless contexts) so a bad reading isn't recorded as a result.
- Never record "can't verify — no <capability>" without checking the registry — capability myths outlive their facts; name the sanctioned harness instead.

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

- Client/server validation divergence: client validates only visible/active fields but submits the whole payload → strip inactive values before send, or validate identically.
- Dead plumbing: a value computed → serialized → passed → never read; wire the consumer or delete end-to-end + guard test.
- Index that doesn't serve its query: a composite led by an inequality, or column order mismatching predicate + `ORDER BY`, can't seek/sort — verify against the real query shape.
- Stale caches: invalidated on create but not rename/delete/restore — reset on ALL mutation paths.
- Cross-language catalog drift in "zero-drift" modules, and coercion/format divergence at ANY cross-language boundary (e.g. numeric stringification differing per runtime) — normalize on one side, guard with a parity test (§7).
- Half-applied merges: one branch's fix silently dropped when the other's version auto-took; duplicate/conflicting symbol definitions — diff the merge against both parents.
- Guard on the primary write path but a bare/partial sanitizer on a SIBLING path to the same stored data (templates, imports, saved/shared components) — verify every such path routes through the §9 composite guard.
- Check-then-insert racing a concurrent bulk-UPDATE (read-committed: the bulk statement's snapshot never sees the in-flight child) — lock the parent row on BOTH the insert and bulk-mutate paths (the lock may be a no-op on the dev DB engine — verify serialization on the production engine).
- Never cache a degraded/failed response (rate-limit, 5xx, flag-off blip) as the permanent answer — mark degraded ≠ genuinely empty and skip caching it, or one transient failure suppresses the feature all session.
- Stale async response race: guard success-path state writes with a request-identity check and abort superseded in-flight requests, or a late response clobbers fresher results.
- Blocking/synchronous work on a hot path or event loop (I/O, DNS, heavy transforms) — find it and off-load it.
- A parallel test runner can deadlock in its OWN distribution/IPC layer after a worker crash — a mode no per-test timeout can reach (it only arms while a test executes). Any `-n auto` suite needs a per-test timeout AND fail-fast on worker death (`--max-worker-restart=0`) AND a pre-kill stack dump (`faulthandler_timeout` below the per-test bound); on Windows a "worker crashed" is your own timeout's `os._exit` until proven otherwise, and a session budget only reds a slow-but-COMPLETING run — it bounds no hang.
- A helper THREAD posting a result to a per-test event loop that already closed must not die trying (the aiosqlite class: a double `call_soon_threadsafe` raise escapes the worker loop, the thread dies, every later op on that connection hangs forever) — loop-side drains cannot win the race, so guard the post at the seam (drop the undeliverable delivery, keep the thread alive) and gate it with a test that FORCES the race deterministically.
- Verify the COMPUTED value, never the declaration: styling/config declarations can silently resolve to nothing (conflicting caps, percentage sizes against indefinite bases, no-op utility values) — measure the rendered result.
- Scale-to-fit frames measure their container SYNCHRONOUSLY at first commit (layout-effect/callback ref), never defaulting until a resize observer fires (unreliable in throttled/preview contexts); a CSS max-width cap fights the scale model (double-shrinks) — rely on the container's overflow clip, verify rendered width ≤ container at a narrow viewport.
- A component defined inside another's render body mints a new type per parent render → full remount per keystroke (focus loss, un-typeable forms) — hoist to module scope.
- Window-scrollbar toggling between short/tall pages shifts centered, window-scrolled layouts (horizontal recenter + header reflow) — stabilize the scrollbar gutter; never let a page depend on scrollbar presence (a no-op on overlay-scrollbar platforms — can't be eyeballed there, so don't drop the gutter rule on that evidence).
- Transient overlays (autocomplete, popups) dismiss on focus-out via a related-target-scoped blur check, per platform a11y authoring practices.
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
- Absence of crash evidence is only evidence where the reporter is on: parallel-test workers get fd 0/1 (Windows: fd 2 too) redirected to devnull, so banners and native tracebacks vanish; Windows Event Viewer records nothing when WER is disabled (`Disabled=1`), and an `os._exit` is not a fault so WER never records it anywhere — instrument the process itself (a probe log) before concluding "no crash".

## §12 — Architectural consistency (build-once, reuse-everywhere)

- Decide the extension pattern before the SECOND instance — so #3..#N are data + a few overrides, never new plumbing.
- A "kind" gets a factory/base, not copies: at instance #2, extract the shared contract into a definition helper/base — per-kind map: `{{KIND_FACTORY_MAP}}`.
- One shared core, thin adapters: business logic + authorization in a single service core; HTTP/RPC/CLI/AI surfaces are thin adapters that cannot diverge (also how authz stays consistent, §9).
- Single source of truth → generated artifacts (§7): the catalog of a kind's instances generates the schema/validator/manifest/docs; adding an instance = one edit + a drift gate.
- Promote shared widgets the instant two features need them, on a two-tier ladder: product-generic presentational primitives → the shared kit (`{{SHARED_PRIMITIVES_LOCATION}}`); app-scoped shared widgets → that app's own kit; a feature re-implementing or re-styling a primitive locally is a smell.
- Forward-compatible data: new fields additive + defaulted (old content renders identically, new capability inert until used); shape changes ship an auto-upgrade step; prefer riding an existing shape over a migration.
- Reuse audit before building: grep for an existing component/util/endpoint to extend before adding one.
- Gate the layout conventions you can (naming, layer boundaries); the "where things live" map lives in the always-loaded doc (§6) so every feature has an obvious home.

## §13 — Visual consistency (design system FIRST, before screens)

- Build the design system — tokens + primitives — BEFORE screens; screens consume tokens and never hardcode values; author the visual contract up front (`{{VISUAL_CONTRACT_DOC}}` + token layer `{{TOKENS_LOCATION}}`).
- Tokens for everything: color roles (bg/surface/fg/muted/accent/border/ring, light AND dark), spacing `{{SPACING_SCALE}}`, type `{{TYPE_SCALE}}`, radius, shadow, breakpoints `{{BREAKPOINTS}}`, z-index, motion; a lint/gate flags raw hex/px in feature code.
- Semantic, surface-aware color — never a raw palette stop on an arbitrary surface: each surface declares a matched bg+fg pair components inherit; make illegible pairings impossible by construction; a contrast helper auto-picks a readable fg for any accent (computed, not eyeballed).
- Contrast is a standing gate, not a review item: assert WCAG AA (4.5:1 text, 3:1 non-text) over token combinations + a route scan, in light AND dark.
- Mobile-first: base styles for the smallest viewport, layered up; "done" = checked at the smallest AND a large breakpoint; touch targets ≥ `{{MIN_TOUCH_TARGET}}`.
- Layout & rhythm via shared primitives (Stack/Cluster/Grid/page-shell own spacing, max-width, gutters); typography via the type scale + a few text components enforcing heading hierarchy (one H1 per page) — features place content into them.
- States (empty/loading/error/disabled/long-content/focus/i18n-RTL width) and a11y (focus-visible rings, `aria-*`, label associations, reduced-motion) live in the primitives — inherited, never re-added per screen.
- A living reference gallery (`{{GALLERY_ROUTE}}`) mounts the REAL components reading the REAL tokens across states/modes/breakpoints, and is the PRIMARY authority for design work: new/changed UI conforms to it unless a task notes an exception; it *reflects* the system, never redesigns it — a reference/reality disagreement IS the bug; review the system centrally, not per screen.
