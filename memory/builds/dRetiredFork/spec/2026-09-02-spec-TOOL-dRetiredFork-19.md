# TOOL-dRetiredFork-19 — a declared placeholder must be one its own adopter substitutes

**Status:** OPEN · rev-1 · 2026-09-02 · node d · Tier-2 · base b0108f13 · streams tooling · order 0 · ratified 2026-09-02

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-09-02-review-TOOL-dRetiredFork-3-21-and-depl-1-9-spec-audit-round3.md](../reviews/2026-09-02-review-TOOL-dRetiredFork-3-21-and-depl-1-9-spec-audit-round3.md) | spec-audit | DEPL-dRetiredFork-1 DEPL-dRetiredFork-2 DEPL-dRetiredFork-3 DEPL-dRetiredFork-6 DEPL-dRetiredFork-7 DEPL-dRetiredFork-8 DEPL-dRetiredFork-9 TOOL-dRetiredFork-3 TOOL-dRetiredFork-5 TOOL-dRetiredFork-8 TOOL-dRetiredFork-9 TOOL-dRetiredFork-11 TOOL-dRetiredFork-12 TOOL-dRetiredFork-13 TOOL-dRetiredFork-14 TOOL-dRetiredFork-15 TOOL-dRetiredFork-16 TOOL-dRetiredFork-17 TOOL-dRetiredFork-20 TOOL-dRetiredFork-21 |

<!-- /gen:spec-records -->

## 1. Goal

PROMOTED from spec-audit round 2, blocker 3. `TOOL-dRetiredFork-12` S1 was corrected to declare
`placeholders = ["KIT_DIR"]` and proved why: `TOOL_ROOT` cannot be rendered by the unattended
adopter, so an unresolved `{{TOOL_ROOT}}` brace would ship to every adopter. Its §4 Data model still
reads "Two tokens only, `KIT_DIR` and `TOOL_ROOT`", §10 still asserts the unit adopts that pair, and
§5's user-docs row still says "its two tokens". **§4 Data model is the section a builder implements
from**, so following the spec still ships the brace — the exact harm the correction was raised to
prevent.

Verified at HEAD: `tools/unattended/adopt-unattended.sh:222-228` substitutes seven tokens —
`KIT_DIR`, `MEMORY_ROOT`, `LANDER`, the three `KEEPALIVE_*` and `ANCHOR_SCOPE` — and `TOOL_ROOT` is
not among them. `grep -rln TOOL_ROOT tools/` returns memory-tree, workflows, `tools/lib/render-doc.sh`
and the install-prefix gate's fixtures, and nothing under `tools/unattended/`.

This unit carries both the document correction and the gate that makes the class unbuildable.

## 2. Scope (IN)

- **S1** — Rewrite `TOOL-dRetiredFork-12` §4 Data model WHOLESALE to "One token, `KIT_DIR`",
  carrying S1's reason and stating that `TOOL_ROOT` is computed only by
  `tools/memory-tree/adopt-memory-tree.sh` and is unavailable in this kit's adopter.
- **S2** — Rewrite that spec's §10 seam sentence to cite the memory-tree rendered-template family as
  a SHAPE precedent while this kit's adopter substitutes a narrower token set, and correct §5's
  "its two tokens".
- **S3** — The gate: for every `[[files]]` rule in every `tools/*/kit.toml` declaring `placeholders`,
  assert each named token is actually substituted by that kit's own adopter script, and RED on one
  that is not. The data is already declared on both sides; this is a join, not a heuristic.
- **S4** — Observe the RED before wiring: add `TOOL_ROOT` to a `placeholders` list in the unattended
  descriptor, confirm the gate reds naming the token and the adopter, and revert.
- **S5** — Run the candidate predicate over the whole tree BEFORE wiring and record hits AND
  near-misses. A kit whose adopter substitutes a token no rule declares is the other direction and is
  reported, not gated, in this unit.
- **S6** — The leg declares a wall-clock ceiling in `tools/gate-legs.json` and carries its
  `memory/project/testsuite-count-waivers.txt` row if its suite prints no assertion count.

## 3. Non-goals (OUT)

- Editing `tools/unattended/kit.toml` to add a `TOOL_ROOT` substitution. The token is unnecessary:
  all five literals in `playbook.fixture.md` sit under the kit dir, so `KIT_DIR` covers them.
- Making the gate a kit self-test. Owner ruling at `AGENTS.md:510` holds kit self-tests off the bar;
  this is a repo-subject leg over tracked descriptors, which is a different class.
- Any other spec-token check. Those are `TOOL-dRetiredFork-20`'s spec lint; this gate's subject is
  kit descriptors, not specs.

## 4. Design

### Data model

The gate reads two declared sets per kit: the union of `placeholders` across that kit's `[[files]]`
rules, and the set of `{{TOKEN}}` spellings its adopter script substitutes. The assertion is
one-directional — declared ⊆ substituted — because the reverse is legitimate: an adopter may
substitute a token into a file no rule declares a placeholder list for.

### Migration

gov's own tree is the first subject. S5's pre-wiring run decides whether any existing declaration is
already violating, and if one is, that repair is its own commit before the gate is wired.

### Alternatives rejected

Checking rendered OUTPUT for surviving `{{` braces instead. That catches the same class one stage
later, only for kits an adopter actually renders, and only after the brace has shipped — which is
the failure mode rather than a check on it.

## 5. Production-readiness checklist

- security — the gate reads tracked declarations and runs no adopter; no new execution surface.
- perf / scale — one pass over `tools/*/kit.toml` plus one grep per adopter script.
- a11y — N/A.
- i18n — the adopter scripts are shell and the descriptors TOML; read bytes, not text-mode lines,
  so a lone CR cannot rewrite a token boundary.
- error / empty / loading states — a kit declaring NO placeholders anywhere is legal and must not
  red; a run whose population of declaring rules is EMPTY must REFUSE, because a gate that scanned
  nothing reports the same zero as a clean tree.
- observability — the run names how many rules it graded and how many kits declared none.
- risks — a false red blocks every contributor. S5's pre-wiring run over the real tree is the
  mitigation and is not optional.
- testing + left-shift gates — S4's observed RED plus the near-miss record from S5.
- migration / rollback — additive leg; reverting is removing the row from `tools/gate-legs.json`.
- user docs — `WIRE-INTO-PROJECT.md`'s kit-authoring notes gain the rule in one sentence.

## 6. Acceptance criteria

- **AC1** — `TOOL-dRetiredFork-12` §4 Data model names exactly one token, and
  `grep -c 'TOOL_ROOT' memory/builds/dRetiredFork/spec/2026-09-02-spec-TOOL-dRetiredFork-12.md`
  returns hits only in prose explaining why it is absent, never in a declaration.
- **AC2** — When `TOOL_ROOT` is added to a `placeholders` list in `tools/unattended/kit.toml`, the
  new gate exits non-zero naming the token and the adopter that does not substitute it; the RED is
  observed before the gate is wired.
- **AC3** — When every declared token is substituted, the gate exits `0` and names the number of
  rules graded.
- **AC4** — When no `tools/*/kit.toml` rule declares a `placeholders` list, the gate REFUSES rather
  than passing.
- **AC5** — The pre-wiring run over `tools/*/kit.toml` is recorded with its hits and near-misses,
  and every near-miss is dispositioned.
- **AC6** — `bash tools/run-gates/run-gates.sh` includes the leg with a declared ceiling, and
  `bash tools/check-testsuite-counts.sh` exits `0`.

## 7. Gates

`memory hygiene` · `unattended kit gate` · `install-prefix (shipped surface)` ·
`testsuite counts (every bar self-test prints one)` · `govkit selfcheck`.

## 8. Open questions

- **F1 — does the gate read the adopter script textually, or run it?** Textual grep for `{{TOKEN}}`
  spellings is cheap and cannot execute an adopter in gov's own tree, which S3's non-goal requires.
  It misses a token substituted through a variable. Recommendation: textual, and state that limit in
  the gate's own header, because a structural check that reads as a semantic one is the class
  `AGENTS.md` §7 names.
- **F2 — is the reverse direction ever worth gating?** An adopter substituting a token no rule
  declares is legitimate today and S5 reports it. Recommendation: report only, and revisit if the
  report is ever non-empty for a reason nobody can explain.

**RESOLVED (owner, 2026-09-02): every fork above is settled by its own stated Recommendation.** The owner ratified them as written on 2026-09-02 with the instruction to fold the recommendations. No fork is resolved against its recommendation and none by silence; where a later measurement contradicts a ratified pick, that is a new fork with a new id.

## 9. Revision log

- rev-1 · 2026-09-02 · initial draft. PROMOTED from spec-audit round 2 blocker 3 under BUILD-METHOD
  M4's disposition rule. The seven substituted tokens and `TOOL_ROOT`'s absence from
  `tools/unattended/` were measured at `b0108f13`, not taken from the review.

## 10. Reuse audit

The seam is the kit-descriptor reader every govkit verb already uses to resolve `[[files]]` rules,
plus `tools/lib/render-doc.sh`, which is the corpus's one existing token substituter and the reason
`TOOL_ROOT` is spelled in only two kits. `python tools/codebase-map/reuse_lookup.py "resolve a
document's backticked tokens against the tree that owns them"` reports `resolve` at fan-in 25 and
`owners_of` at fan-in 3 as the resolution seams; neither joins a declaration to a substituter, so
this gate adds that join and reuses the descriptor reader rather than parsing TOML afresh.

Recall terms used: `placeholder`, `KIT_DIR`, `TOOL_ROOT`, `rendered`, `adopter`, `descriptor`,
`kit.toml`, `render-doc`, `substitute`, `unresolved brace`, `token`, `prefix`.
