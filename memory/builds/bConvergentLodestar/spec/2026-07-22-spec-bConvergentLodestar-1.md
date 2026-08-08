# TOOL-bConvergentLodestar-1 — reuse-convergence layer for codebase-map

**Status:** SPECCED · rev-2 · 2026-07-22 · node b · Tier-2 · base 7b01979ad7 · review wf_69de6d2e-926

## 1. Goal

`codebase-map` proves COVERAGE (what exists, who owns it) but never NON-REDUNDANCY, so a repo does not
*converge*: new work cannot reliably discover an existing seam, and — worse — when it reinvents one anyway,
nothing catches it, so features drift into permanent islands. This tool adds a convergence layer with two
linked halves: a **prevention** half (machine recall over every symbol + a forward reuse affordance per
feature + a behavior→seam lookup at DoR) that helps new work wire through existing seams, and a
**closing-loop** half (a machine detector for *shipped* reinvention — a new exported symbol that collides
with an existing high-fan-in seam and adds no reference edge to it — surfaced at review and routed to the
consolidation backlog). Convergence is the closing-loop signal trending toward zero, and it is computed
over ALL new code so a reinventer who skips the advisory lookup is still counted. Same portable-engine /
project-layer split as `codebase-map`; grounded in inCMS ARCH-bThriftyCompass-1 (CLOSED on `origin/main` —
the prevention-forward half), whose diagnosis established that identity coverage alone never converges an
existing repo.

## 2. Scope (IN)

- **S1 — `## Reuse affordance` dossier section (forward reuse menu).** A new `AFFORDANCE_HEADING` constant
  (NOT added to `REQUIRED_HEADINGS`, which loops over every dossier with no exemption and would retro-red
  the fleet — review #22). A dedicated graced check requires the heading only for dossiers absent from an
  affordance-exempt list. Parsed unit: ALL leading consecutive `seam:` lines — `seam: <id> — reuse for
  <need-shape>; extend via <point>` — or the single line `none — <why feature-specific>`; the `-`/`–`/`—`
  delimiters are interchangeable and only the `seam:` prefix + an id token are load-bearing (review #20).
  Presence is gated; content quality is not (the un-gatable ceiling).
- **S2 — symbol recall index.** A generated `symbols.json` = `{"$comment", "symbols":[{id,kind,file}...]}`
  — id/kind/file ONLY, so it churns like `inventories.json` (on symbol add/remove), never on a live count
  (review #17). Per-language symbol extractors in the project layer either use a real parser OR enumerate
  every export form and RAISE `MapError` on an unmatched `export `/`def ` shape — a regex that silently
  skips `export default`/re-exports/`type`/decorated classes is the green-by-absence hole the kit bans
  (review #9/#16). A completeness self-check (parsed-symbol count vs export-keyword count) reds on
  under-enumeration. A repo declares its covered layers explicitly; an uncovered layer is recorded
  recall-dark, and the lookup announces it (S3) so "no seam fits" is never falsely confident (review #27).
- **S3 — `reuse-lookup` (behavior→seam entrypoint).** A portable CLI that deterministically assembles a
  candidate corpus — `inventories.json` keys, every `## Reuse affordance` `seam:` line, `symbols.json`
  ids/kinds, and `## Shared seams` prose — into a shortlist that is NOT a hard top-K lexical cut (the
  quantified-0%-behavioural recall gate, review #13/#19) but the union of token-stem matches AND a capped
  set of structural neighbours; an agent-instruction then reads the shortlist's sources and returns the
  seam to wire through or "no seam fits", printing "recall partial: layers X, Y have no symbol extractor"
  whenever a covered-layer gap could hide the answer. Fan-in is computed on demand HERE (not committed),
  scoped to import/identifier positions, to rank hot seams. This is bThriftyCompass S1's portable
  re-implementation, not a separate mechanism; inCMS retires `reuse-discovery.js` on re-adoption (§4 Rollout).
- **S4 — retroactive convergence.** (a) touch-triggered backfill: a dossier's affordance exemption is
  dropped mechanically off `map_diff` attribution — when a merge range's changed files match a dossier's
  globs, that dossier loses its exemption and must carry an affordance next time it is gated (no reliance
  on a human remembering, review #5/#32). (b) bounded big-bang: `gen_map.py --seed-affordances --top <N>`
  lists the N highest-fan-in seams no dossier yet declares, as the worklist, so the reinvention-prone
  active surface converges first.
- **S5 — the closing loop + convergence metric, as a `map_diff` mode (not a new CLI — `map_diff` already
  walks `<base>..<head>` and calls itself the convergence-visibility metric, review #31).** `map_diff
  --converge <base>..<head>` emits: `collision_flags` — each NEW exported symbol in the range whose id
  shares a token stem with an existing seam of fan-in ≥ threshold AND whose file adds no reference edge to
  that seam (a machine proxy for "built new instead of wiring through", computed over ALL new code, so
  bypass of the S3 lookup does not hide it); and `new_clones` — the verbatim-clone-ratchet count when that
  kit is adopted. Each `collision_flag` is a review-time WARN routed to the reinvention backlog (a soft
  force — NOT a hard gate, since a token-stem collision has false positives). A repo converges when
  `collision_flags` + `new_clones` trend toward zero. `affordance_coverage_%` and `dead_exports` are
  demoted to adoption/hygiene hints, explicitly OFF the convergence claim (review #0/#3/#18).

## 3. Non-goals (OUT)

- **No hard semantic gate.** The collision signal is a review WARN + a backlog row, never a merge blocker;
  a token-stem/structural collision has real false positives (a legitimately-new same-named symbol), and a
  hard gate on it trains `--no-verify`. The un-gatable-semantic-equivalence rule from ARCH-bThriftyCompass
  is retained; the closing loop is a soft force, and §1 claims exactly that, not more.
- **No resolved import/call graph.** Fan-in and the collision "reference edge" are import/identifier-scoped
  heuristics, not language-server-resolved; accurate enough for ranking + a review WARN, stdlib-only. A
  precise call graph is a named follow-up.
- **No auto-consolidation.** The loop SURFACES shipped reinvention to review + the backlog; folding is
  human work (the backlog burndown), never automated refactoring.
- **No forced `## 10` in the shared `TEMPLATE-SPEC`.** The reuse-decision record is a DoD line + an
  OPTIONAL per-repo spec section, not a fleet-wide nine→ten template change (the retro-red trap).
- **Not a `codebase-map` replacement, and it must not fork it.** It EXTENDS the engine — `AFFORDANCE_HEADING`
  beside `REQUIRED_HEADINGS`, a `symbols.json` renderer beside `inventories.json`, a `--converge` mode on
  `map_diff` — never a second dossier system or a second range-walker.
- **No embeddings / vector store.** Non-deterministic, non-stdlib, and it breaks the byte-compare freshness
  contract; token-stem + structural corpus assembly plus an agent read is portable and sufficient.

## 4. Design

### Data model

- **Affordance** (S1): under `## Reuse affordance`, all leading consecutive `seam:` lines, each
  `seam: <id> — reuse for <need>; extend via <point>` where `<id>` resolves to a `symbols.json` id or an
  inventory key; or the single token line `none — <why>`. Parser keys on the `seam:` prefix + id; delimiter
  and trailing clauses are free. A malformed block is a presence-pass but an `affordance_coverage_%` miss.
- **`symbols.json`** (S2): `{id, kind, file}` only, ids sorted, POSIX paths, LF — byte-deterministic like
  `inventories.json`; `kind ∈ {function, class, component, const-export}`. Fan-in is NOT in it.
- **Fan-in** (on demand, S3/S5): for a symbol id, the count of DISTINCT files that reference it in
  import/identifier position (comments/strings excluded), minus its own def file. A "seam" = fan-in ≥ a
  configured threshold (`.codebase-map.conf`, default e.g. 3). Fan-in over/under-count is bounded and
  documented (§5), never gated.
- **Collision flag** (S5): a symbol `S` new in `<base>..<head>` with an `export`/public `kind`, such that
  ∃ existing seam `E` (fan-in ≥ threshold) with `stem(S.id) == stem(E.id)` (or a configured structural
  match), AND no file in the range adds a reference edge to `E`. Emitted as `{new: S, resembles: E, file}`,
  a WARN, one backlog row per flag.
- **converge signals**: `collision_flags[]`, `new_clones` (int, or `null` if the clone kit is not adopted),
  plus the demoted hygiene hints `dead_exports`/`affordance_coverage_%`.

### Inventory

S2 adds a SYMBOL tier to the project's `map_extractors.py`, feeding `symbols.json` only (recall data —
never the ratchet, so a new symbol never fails CI). Each language supplies a symbol extractor that is
real-parser-backed or fail-closed:

| Language | Symbol extractor | Fail-closed rule | Reference scan (fan-in, on demand) |
|---|---|---|---|
| Python | `ast` top-level `def`/`class` (+ `__all__`) | `ast` parse error → `MapError` | import + attribute/name nodes across `*.py` |
| TS/JS | a real parser (tree-sitter/tsc) if available; else enumerate ALL `export …` forms | an unmatched `export ` line → `MapError` (never a silent skip) | import specifiers + identifier tokens |
| other | project supplies the pair, or the layer is listed recall-dark in `.codebase-map.conf` | — | — |

Covered layers are an explicit list; a recall-dark layer is declared, surfaced by the lookup, and counted
in `converge-report --coverage` so the gap is visible, not silent.

### Migration

Adding `## Reuse affordance` to `REQUIRED_HEADINGS` would retro-red every existing dossier (the
`test_dossier_prose_headings_pinned` loop has no exemption — review #22/#10). Instead: a separate
`AFFORDANCE_HEADING` + a `dossier-affordance` check that consults an `affordance-exempt` list (feature
names). Adoption seeds that list from the existing dossiers via a new `gen_map.py
--seed-affordance-baseline` (mirroring `--seed-baseline`), wired into `adopt-codebase-map.sh` so a fresh or
re-adopting repo is green by construction. The list only shrinks: a new dossier is never added to it, and
S4a drops entries mechanically on touch. `symbols.json` seeds like `inventories.json` (freshness gate green
on a fresh render).

### Rollout

1. **S2** — `symbols.json` `{id,kind,file}` + fail-closed symbol extractors + completeness self-check.
2. **S1** — `AFFORDANCE_HEADING` + graced check + `--seed-affordance-baseline`; zero existing dossier reds.
3. **S3** — `reuse-lookup` (corpus assembler + agent-instruction), fan-in on demand, recall-dark announced.
4. **S4** — `map_diff`-attribution exemption-drop + `--seed-affordances --top N`.
5. **S5** — `map_diff --converge` (collision_flags + new_clones + backlog routing).
6. **inCMS re-adoption** — adopt the kit, DELETE `reuse-discovery.js`, repoint CLAUDE.md's "Reuse audit
   before building" at `reuse-lookup` (so inCMS does not keep two behavior→seam lookups — review #6).

### Files touched (estimate)

| Path (under `codebase-map/` unless noted) | Change | Size |
|---|---|---|
| `map_lib.py` | +`AFFORDANCE_HEADING`, affordance-exempt load + graced check, `symbols.json` renderer ({id,kind,file}) | medium |
| `map_diff.py` | +`--converge` mode (collision_flags + new_clones + coverage hints); shared range helper | medium |
| `map_extractors.template.py` | +SYMBOL tier (real-parser-or-fail-closed) + covered-layers list + example pairs | medium |
| `gen_map.py` | +`--seed-affordances --top N`, +`--seed-affordance-baseline`, emit `symbols.json` | small |
| `reuse_lookup.py` (new) + `reuse-lookup.agent.md` (new) | corpus assembler (stem+structural shortlist, on-demand fan-in, recall-dark notice) + agent-instruction | ~150 lines + 1pg |
| `adopt-codebase-map.sh` | +seed the affordance-exempt list on `--scaffold`/re-adopt | small |
| `test_codebase_map.template.py` | +graced-affordance, +baseline-grace, +`symbols.json` freshness, +fail-closed symbol-extractor, +collision cases | medium |
| `README.md`, `INVENTORY-DERIVATION.md` (SYMBOL addendum), repo-root `WIRE-INTO-PROJECT.md` §3b | adopt steps + the DoD lines | doc |
| `selftest.py` | +the new contract checks | small |

### Alternatives rejected

- **A hand-kept capability→seam index** — the drift class this work kills; recall is generated (S2),
  affordances live with the feature (S1).
- **A hard semantic-similarity gate** — false-positives train `--no-verify`; the collision signal is a WARN.
- **Embeddings / a vector store** — non-deterministic, non-stdlib, breaks freshness byte-compare.
- **`fanin` inside `symbols.json`** — restales the freshness-gated artifact on nearly every commit (the
  mistake `render_inventories_json` avoids); computed on demand instead.
- **A standalone `converge-report` CLI** — `map_diff` already walks the range; a second range-walker is the
  tool reinventing itself. `--converge` is a mode.

## 5. Production-readiness checklist

- security — N/A — read-only static analysis; no runtime, secrets, or network.
- perf / scale — `symbols.json` render is a parse pass (gated, must be seconds — a fixture-repo timing is a
  build gate, not an assertion, review #7/#21); fan-in + collision are computed on demand OUTSIDE the gate
  (in the lookup / `--converge`), so per-commit gate cost stays flat. A concrete budget + timing lands in
  the build report.
- a11y / i18n — N/A — developer tooling.
- error / empty / loading — extractors fail-closed (`MapError`); empty corpus → "no seam fits"; a
  recall-dark layer → an explicit partial-recall notice, never a false "no seam".
- observability — `map_diff --converge` IS the convergence dashboard; collision WARNs land in the backlog.
- risks — collision-signal FALSE POSITIVES (a legit new same-named symbol) → WARN not gate + F8 tuning;
  fan-in under-count on registries/dynamic dispatch is a documented recall FLOOR (inCMS's most-reused seams
  are registered, not named — review #2/#28); over-count on common ids (`get`/`render`) mitigated by
  import/identifier scoping; affordance prose-rot is advisory, surfaced by coverage %.
- testing + left-shift — fail-closed unit tests (extractor RAISES on an unmodelled export/tree, mirroring
  `t_extractor_helpers_fail_closed`), `selftest.py`, a fixture-repo adopt + collision run; every confirmed
  finding becomes a selftest case.
- migration / rollback — the shrink-only affordance-exempt baseline + `--seed-affordance-baseline` make
  adoption and re-adoption non-blocking; rollback = drop `AFFORDANCE_HEADING`, the SYMBOL tier, and the
  `--converge` mode.
- user docs — `README.md` adopt steps, an `INVENTORY-DERIVATION.md` SYMBOL addendum, and the repo-root
  `WIRE-INTO-PROJECT.md` §3b DoD lines (affordance-on-touch + run `map_diff --converge` at review).

## 6. Acceptance criteria

- **AC1** — When a NEW dossier omits `## Reuse affordance`, the graced check fails naming it; a dossier on
  the affordance-exempt list passes; after its feature's files land in a `map_diff` range (exemption
  dropped) it fails until it carries a `seam:`/`none` block. Proves graced presence + mechanical touch-drop
  + no retro-red.
- **AC2** — When a symbol extractor meets an unmodelled export/tree it RAISES `MapError` (a fail-closed unit
  test, not a freshness-gate claim — the gate cannot see fail-open); and a regenerated `symbols.json`
  byte-matches across a Windows and a Linux run.
- **AC3** — On a FIXTURE repo with a planted `slugify` seam, `reuse-lookup "normalise a name to a slug"`
  ranks it into the shortlist above unrelated symbols; a no-home query returns "no seam fits"; and with the
  fixture's TS layer marked recall-dark, the lookup prints the partial-recall notice. (Portable — no
  dependence on any host repo's paths.)
- **AC4** — On a fixture range that adds `slugify2` (stem-colliding with the high-fan-in `slugify`, no new
  edge to it), `map_diff --converge` emits a `collision_flag` WARN + one backlog row; a range that folds a
  verbatim duplicate drops `new_clones`; neither `dead_exports` nor `affordance_coverage_%` is asserted as
  the convergence signal.
- **AC5** — `gen_map.py --seed-affordances --top 10` lists the 10 highest-fan-in seams no dossier declares,
  and nothing already declared.
- **AC6** — `codebase-map/selftest.py` is green, and `adopt-codebase-map.sh --scaffold` on a scratch repo
  yields a green gate by construction, including a seeded affordance-exempt baseline.

## 7. Gates

Keeps green: the existing `codebase-map` ratchet + freshness gate and the toolkit `check-memory-hygiene`
leg. Adds to the SAME gate file (no CI job — a test file is its own deployment): the graced-affordance
presence check, the `symbols.json` `{id,kind,file}` freshness byte-compare, and the fail-closed
symbol-extractor unit tests. `map_diff --converge` is a report + WARN, never a gate (F5) — a convergence
metric that hard-fails false-fails on legitimate churn.

## 8. Open questions

- **F1 — symbol extractor backing.** (a) real parser per language (tree-sitter/tsc/`ast`); (b) fail-closed
  enumeration of all export forms, no external parser. Recommendation: (a) where a stdlib/available parser
  exists (`ast` for Python), (b) as the fail-closed floor elsewhere — never a silent-skip regex.
- **F2 — affordance enforcement.** (a) graced presence (separate `AFFORDANCE_HEADING` + exempt list); (b)
  advisory, ungated. Recommendation: (a) — presence forces the decision; grace + `--seed-affordance-baseline`
  prevent retro-red.
- **F3 — lookup form.** (a) CLI corpus + agent-instruction; (b) bundled Workflow (not portable); (c)
  pure-CLI lexical. Recommendation: (a) — harness-agnostic, keeps the semantic leg.
- **F4 — big-bang scope.** (a) top-N by fan-in; (b) full sweep; (c) touch-only. Recommendation: (a).
- **F5 — convergence-metric home.** (a) `map_diff --converge` report + WARN; (b) a gate leg that fails on
  regression. Recommendation: (a) — a metric-as-gate false-fails on legitimate feature churn.
- **F6 — reuse-decision record.** (a) a DoD line + optional per-repo spec section; (b) force `## 10` into
  the shared `TEMPLATE-SPEC`. Recommendation: (a) — (b) retro-reds the spec fleet.
- **F7 (rev-2) — collision-WARN / backlog home.** Where each `collision_flag` lands: (a) appended to the
  project's reinvention backlog file at `map_diff --converge` time (durable, reviewable); (b) emitted to
  stdout only (ephemeral); (c) a per-node sharded log (in-flight-ledger style, no merge conflict).
  Recommendation: (a) — a backlog row is the consolidation worklist; dedupe by `{new, resembles}` so a
  re-run does not pile duplicates.
- **F8 (rev-2) — collision precision knobs.** How to define "collides with a seam" to keep WARN precision
  usable: (a) shared token stem + fan-in ≥ threshold; (b) + a structural signal (same kind + arity/shape);
  (c) + an affordance cross-check (S resembles a seam that DECLARES an affordance → stronger signal).
  Recommendation: (b), with (c) boosting confidence; expose the threshold in `.codebase-map.conf` and report
  the flag's confidence so a noisy repo can tune without a code patch.

## 9. Revision log

- rev-1 · 2026-07-22 · initial draft (node b, bConvergentLodestar). Extends `codebase-map` with recall,
  affordances, a lookup, backfill, and a metric.
- rev-2 · 2026-07-22 · folded the adversarial review `wf_69de6d2e-926` (5 blockers + ~15 majors confirmed).
  Load-bearing change: added the **shipped-reinvention closing loop** — the `collision_flag` signal
  (a new export colliding with a high-fan-in seam, no new edge) computed over ALL new code, surfaced as a
  review WARN routed to the backlog — so §1 claims a real force on the reinvention rate and S5 is
  falsifiable. Also: separated `AFFORDANCE_HEADING` from `REQUIRED_HEADINGS` (+ `--seed-affordance-baseline`)
  to stop the retro-red; `symbols.json` is `{id,kind,file}`-only with fan-in on demand (no freshness churn);
  symbol extractors are real-parser-or-fail-closed with a completeness check and declared recall-dark
  layers; `--converge` is a `map_diff` mode (no forked range-walker); `dead_exports`/`affordance_coverage_%`
  demoted off the convergence claim; ACs rebased on a fixture; +F7 (collision-WARN home) +F8 (collision
  precision).
