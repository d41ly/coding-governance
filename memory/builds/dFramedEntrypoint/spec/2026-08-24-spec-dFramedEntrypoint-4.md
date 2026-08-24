# TOOL-dFramedEntrypoint-4 — the build-order verb becomes legal and hardened, and the roster renders order and tier

**Status:** CLOSED · rev-7 · 2026-08-24 · node d · Tier-2 · base 9ddcc5c9 · order 3 · streams tooling · ratified 2026-08-24

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-08-24-build-TOOL-dFramedEntrypoint-4-acceptance.md](../build/2026-08-24-build-TOOL-dFramedEntrypoint-4-acceptance.md) | journal | — |
| [2026-08-24-review-TOOL-dFramedEntrypoint-1-spec-audit-round1.md](../reviews/2026-08-24-review-TOOL-dFramedEntrypoint-1-spec-audit-round1.md) | spec-audit | TOOL-dFramedEntrypoint-1 TOOL-dFramedEntrypoint-2 TOOL-dFramedEntrypoint-3 TOOL-dFramedEntrypoint-5 TOOL-dFramedEntrypoint-6 TOOL-dFramedEntrypoint-7 TOOL-dFramedEntrypoint-8 |
| [2026-08-24-review-TOOL-dFramedEntrypoint-1-spec-audit-round2.md](../reviews/2026-08-24-review-TOOL-dFramedEntrypoint-1-spec-audit-round2.md) | spec-audit | TOOL-dFramedEntrypoint-1 TOOL-dFramedEntrypoint-2 TOOL-dFramedEntrypoint-3 TOOL-dFramedEntrypoint-5 TOOL-dFramedEntrypoint-6 TOOL-dFramedEntrypoint-7 TOOL-dFramedEntrypoint-8 |
| [2026-08-25-review-TOOL-dFramedEntrypoint-1-diff-review-round1.md](../reviews/2026-08-25-review-TOOL-dFramedEntrypoint-1-diff-review-round1.md) | diff-review | TOOL-dFramedEntrypoint-1 TOOL-dFramedEntrypoint-2 TOOL-dFramedEntrypoint-3 TOOL-dFramedEntrypoint-5 TOOL-dFramedEntrypoint-6 TOOL-dFramedEntrypoint-7 TOOL-dFramedEntrypoint-8 |

<!-- /gen:spec-records -->

## 1. Goal

The owner's ask is that build order be authored on the SPECS and computed in the README. The verb for
it already exists in the generator and is adopted by nobody: zero of 260 tracked units carry it, all 61
build-order regions render the empty-case sentence, the spec template's own tail rule forbids it, and
its regex misreads a malformed value as a valid step. This unit legalises the verb, hardens its parser,
renders order and tier as columns of the roster, and makes this build's own spec set its first adopter.

## 2. Scope (IN)

- **S1** — `memory/TEMPLATE-SPEC.md` gains the `order` verb in the status-header grammar, via
  `tools/memory-tree/SPEC-TEMPLATE.template.md` edited first and the live copy re-rendered. Its tail
  rule currently reads pointers-only, which forbids the verb the generator already parses; this closes
  a documented-versus-gated disagreement rather than adding a feature.
- **S2** — `ORDER_RE` is anchored so a malformed value is a REFUSAL, not a silent step. Measured today:
  a hexadecimal-looking value renders as step 0 and a digit-then-letter value renders as its digit.
- **S3** — the verb's validation lives in the GENERATOR, not in hygiene check 12: a positive
  integer, at most once per header. `_parse_order` refuses anything that looks like the verb and
  does not conform, and that refusal already rides `--check` and `--write`, which are unguarded
  merge-bar legs. AMENDED from check 12 during the build, for two reasons that only became
  visible with the code in front of me. A second validator in shell would give one verb two
  definitions, which is the two-answers-to-one-question class this build exists to remove; and it
  would cost an armed branch, an `ARMS_FLOORS` movement and a fixture in a 181-second self-test
  to re-state a refusal the generator already makes. The hygiene gate is also GUARDED while the
  generator's legs are not, so the generator is the stricter home.
- **S4** — the roster table rendered into the nested units region gains an ORDER column and a TIER
  column. Tier is already captured by the header regex and discarded one line later; order is already
  in the unit record and reaches only the order region.
- **S5** — the roster sorts by order, then by id, with unordered units last under a stated residual
  line. The current sort is by path, and the change must be stated because it alters which unit the
  status verb names as next.
- **S6** — this build's own eight specs adopt the verb, making the build-order region non-empty for the
  first time in the corpus and this build its own first adopter.
- **S7** — selftest arms for the hardened parser, the two new columns, the sort, and the residual line.
- **S-EPOCH** — this unit moves `tools/memory-tree/gen_build_index.py`, which is inside the
  verdict-epoch gate's scan set, so its landing carries a `KIT_MEMORY_TREE_VERSION` bump. The carrier
  set is DERIVED, never read off the epoch gate's remedy text: bump the constant and its inline marker
  in the engine, then every carrier `git grep -l 'gov:kit memory-tree@'` returns over tracked paths
  outside `memory/builds/` and `memory/archive/`, then re-render the live copies with
  `bash tools/memory-tree/kit-dogfood-parity.test.sh --render`. The remedy string names three paths and
  the parity harness three pairs; their union is five, and there are SEVEN carriers — the two it cannot
  reach are kit SOURCES rather than dogfood copies. Following the remedy exactly reds the unguarded
  `kit version markers` leg, which is `TOOL-dSettledRoster-4` in the backlog, recorded as having cost a
  full-bar cycle twice. The rule binds per PUSH RANGE, not per commit: units landing in one push need
  one correctly-placed bump, on the LAST engine-moving commit in that range. It is stated in every
  engine-moving unit rather than once, because a rule written in one spec is a rule the other seven do
  not carry.

## 3. Non-goals (OUT)

- The verb is NOT made mandatory. Requiring it needs a dated cutoff, and this build's fork-1 ruling
  refused date keys for the README class; whether a spec-class cutoff is different is a separate
  question with a separate population, and it is not decided here.
- No PREDECESSOR DAG. An integer with ties expresses a total order with parallel groups, which is a
  linear extension of a dependency graph and not the graph. Two builds in the corpus hand-author
  richer constraints — a predecessor list and a co-landing pair — and neither survives the projection.
  The open backlog row asking for a derivable dependency field stays OPEN, narrowed by a note.
- No change to the build-order REGION's rendering beyond what S5's sort implies. The region already
  renders steps and parallel groups correctly.
- No back-fill of the verb onto landed specs. A ratified record is not rewritten.

## 4. Design

### Data model

The verb is a status-header field, `order` followed by a positive integer, positioned after `base` and
alongside the existing optional fields. Units sharing a value are the parallel group. A unit with no
verb is unordered and appears in the residual line the order region already emits.

### Inventory

The roster row becomes six cells: unit link, order, tier, status, rev, last change. The cost is measured rather than assumed, and it is not uniform: two ASCII cells add eight bytes, but
an em-dash in an unfilled ORDER cell is three bytes in UTF-8, so a row's growth depends on its
contents. The declared tier is in CHARACTERS while the widest-row figure of 230 was taken in bytes,
so the two are not directly comparable and the acceptance measurement states its unit. Headroom is
ample either way — the gap is over a hundred — but the arithmetic is re-derived at AC8 rather than
carried from this paragraph. The row-width worry recorded against this table was mis-attributed: no
generated unit row is over cap, and every over-cap generated line is a records row belonging to unit 5.

### Migration

None for landed specs. The corpus renders exactly as it does today except for two additional columns and this build's own
eight specs, which adopt the verb. Only the ORDER cell can be an em-dash: tier is a MANDATORY named
group of the status-header regex and only a header-carrying spec produces a roster row at all, so the
TIER cell always renders 1 or 2.

### Alternatives rejected

**A second `group` verb for the parallel set.** Rejected in the record that designed the verb, because
ties in one integer already express the group and a second verb would need its own contradiction
refusals to render an identical region.

**Authoring order in the README instead.** That is what the corpus does today by hand, in 10 sections
across 9 READMEs totalling 15,541 bytes of ordering rationale, and it is the duplication this build
exists to remove. The larger 50,980-byte figure measured across 33 READMEs is the hand-authored ROSTER
class, which is a different duplication and is removed by the canon rather than by this verb. The owner's ask states the inverse
directly: the markers belong to the specs.

### Files touched (estimate)

`tools/memory-tree/SPEC-TEMPLATE.template.md` edited FIRST with `memory/TEMPLATE-SPEC.md` re-rendered ·
`tools/memory-tree/gen_build_index.py` for the parser, the columns, the sort and the arms ·
`tools/memory-tree/check-memory-hygiene.sh` for the check-12 validation and its arms ·
`memory/project/unarmed-branches.txt` if branch ordinals shift · this build's eight spec headers ·
`memory/backlog/TOOL.md` for the narrowing note on the dependency row · the `build-readme-surface`
dossier.

## 5. Production-readiness checklist

- security — N/A.
- perf / scale — one regex per spec header, already run; two cells per rendered row.
- a11y — N/A.
- i18n — N/A.
- error / empty / loading states — a build with no adopter renders the ORDER column as em-dashes, the
  TIER column always renders a value, and the order region keeps its empty-case sentence; the residual
  line names every unordered unit so a partial adoption never reads as a complete order.
- observability — the residual line is the observability, and it already exists.
- risks — the sort change alters which unit the status verb names as next. Stated in S5 rather than
  discovered; the new order is the build order, which is the more useful answer, but it is a behaviour
  change and is recorded as one.
- testing + left-shift gates — the hardened parser needs arms for both malformed shapes measured, and
  a check-12 arm needs a fixture because no tracked spec carries the verb until S6 lands.
- migration / rollback — rollback is reverting two cells and the sort key; the verb itself is additive
  and inert without adopters.
- user docs — the verb's grammar lands in `memory/TEMPLATE-SPEC.md` via its template.

## 6. Acceptance criteria

- **AC1** — When a spec status header carries a malformed order value, `python tools/memory-tree/gen_build_index.py --check`
  refuses it by name rather than rendering a step, demonstrated against both shapes measured today.
- **AC2** — When a spec carries a valid order verb, the roster row for that unit shows the value in its
  ORDER cell after `python tools/memory-tree/gen_build_index.py --write`.
- **AC3** — When a spec carries no order verb, its ORDER cell renders an em-dash and its id appears in
  the `gen:build-order` region's residual line.
- **AC4** — When a build's specs carry mixed tiers, each roster row shows that spec's own tier, matching
  the value in its `**Status:**` header.
- **AC5** — When the roster renders for a build whose units carry order values, the rendered
  `gen:build-units` table in that build's README lists the rows in order-then-id sequence with
  unordered units last, read from the file after `--write`. Not from `--check`, which reports only
  WHICH artifacts are stale and never their row order.
- **AC6** — When `bash tools/memory-tree/check-memory-hygiene.sh` runs against a spec whose header
  carries the verb twice, check 12 exits non-zero naming that header.
- **AC7** — When this build's eight specs carry the verb, the `gen:build-order` region of
  `memory/builds/dFramedEntrypoint/README.md` renders a step table rather than the empty-case sentence.
- **AC8** — When the widest rendered unit row in the corpus is measured after the change, it is under
  the `BUILD_README_ENTRY_CAP_CHARS` tier, recorded with the command that measured it.
- **AC9** — When `python tools/memory-tree/gen_build_index.py --selftest` runs, every arm added here
  passes. The bare bar does not exercise them, so this unit's Definition of Done names
  `GATE_FULL=1 GATE_SELFTESTS=1 bash tools/run-gates/run-gates.sh`.

## 7. Gates

`build-index selftest` · `memory hygiene` · `build README slot contract` · the spec-template parity
harness · `check-arms.py` floors if check-12 branches move · `check-kit-versions.sh` (leg `kit version
markers`, unguarded) · `check-verdict-epoch.sh` · `kit/dogfood doc parity`.

## 8. Open questions

- **F1 — does the order verb become MANDATORY for new specs, and if so keyed on what?** The README
  class refused date keys because they exempt everything on the day they are set; the spec class has a
  filename date and an existing precedent for exactly this shape. RESOLVED (agent, 2026-08-24, delegated): not
  in this unit. Making it mandatory needs a dated cutoff over the SPEC class, which is a different
  population with its own measurement, and taking it here would widen the unit past the one mechanism
  M2 allows it.
- **F2 — should an order value be required to be contiguous from one?** Gaps render silently today.
  Against requiring it: a gap is how a retired unit leaves an order without renumbering the rest, and
  renumbering is the class this repo's id rules already refuse. RESOLVED (agent, 2026-08-24, delegated): permit
  gaps, stated in the grammar so the silence is a decision rather than an omission.

## 9. Revision log

- rev-1 · 2026-08-24 · initial draft. The order verb's non-adoption, the parser defect and the
  documented-versus-gated disagreement are all from this build's derivation research and its
  verification.
- rev-2 · 2026-08-24 · folded spec-audit round 1. The ordering-rationale figure is corrected: the
  paragraph cited the hand-authored roster class (50,980 B over 33 READMEs) for a claim about order
  rationale (15,541 B over 9). The tier cell is corrected to always render, since tier is a
  mandatory group of the header regex and only a header-carrying spec makes a row. The held selftest
  leg gains an explicit invocation.
- rev-3 · 2026-08-24 · folded the factual corrections from round 1's LOW tier. The row-cost
  arithmetic stops mixing units: the tier is declared in characters, the 230 figure was bytes, and
  an em-dash is three bytes rather than one. The measurement moves to AC8 and states its unit.
- rev-4 · 2026-08-24 · folded spec-audit round 2. The kit-version carrier set becomes a derivation,
  and `kit version markers` joins the gate list.
- rev-5 · 2026-08-24 · every open fork in section 8 resolved under the standing mandate's delegated resolver authority, by M3's rule: the most feature-rich survivor after the three vetoes. No option was taken that needed a new dependency, install location or public surface. The one question this build refuses is not a spec fork and is parked on the run-state file instead.
- rev-6 · 2026-08-24 · S3 AMENDED mid-build: the order verb's validation moves from hygiene check 12 to the generator's own `_parse_order`. One verb with two validators is the class this build removes, and the shell home would cost an arm, a floor movement and a fixture to restate a refusal the generator already makes on an unguarded leg. M2's rule is to change the spec first and then the code, which is the order this took.
- rev-7 · 2026-08-24 · BUILT and CLOSED. The verb is legal, anchored on both sides and refused when malformed or doubled; the roster carries Order and Tier and sorts by build order; this build is the verb's first adopter and the first non-empty build-order region in the corpus. Eleven arms, 84 to 95, with the old regex staged back to watch two of them fail. Two defects of mine were caught by running rather than reading: the duplicate refusal was unreachable below an early return, and the sort arm measured the wrong string. Ledger: `build/2026-08-24-build-TOOL-dFramedEntrypoint-4-acceptance.md`.

## 10. Reuse audit

The seam is `HDR_RE` and `parse_spec` in `tools/memory-tree/gen_build_index.py`, which already capture
both values this unit renders — tier as a named group discarded immediately after the match, order into
the unit record where only the order region reads it. No new parsing is built and no new seam is
created: the change is one dict key, two rendered cells and one sort key, and the reuse audit's real
finding is that the data was already there and only the rendering was missing.
