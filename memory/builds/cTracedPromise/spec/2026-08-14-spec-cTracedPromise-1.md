# TOOL-cTracedPromise-1 — a closed spec has to point at a commit that changed the product

**Status:** OPEN · rev-2 · 2026-08-14 · node c · Tier-2 · base 37c05e1b · streams tooling

## 1. Goal

Add a sixth drift-audit signal that reds when a spec claims CLOSED and no single-parent commit,
reachable from either the default branch or the working tip, both names that unit and touches product
source. It closes the reverse of the direction `non_terminal_specs_cited_by_product_source` already
measures, so the pair covers both ways a spec status can lie about git.

## 2. Scope (IN)

- **S1** — `signal_closed_specs_untraceable` in `tools/drift-audit/drift_report.py`, appended to
  `SIGNALS`. Reports `value`, `of`, `live`, `unjudgeable` and `detail` on the contract the five
  existing signals use, and `gateable` per S5.
- **S2** — the oracle. For each spec whose status is `CLOSED` and whose STATUS-HEADER date is on or
  after `TRACE_CUTOFF`, at least one commit must carry the spec's own id OR its slug in its subject
  and touch a `TRACE_GLOBS` path. The commit set is
  `git log <base_ref> HEAD --no-merges --format=%s -- <TRACE_GLOBS>`.
- **S3** — the commit set unions BOTH tips. The spec population is read from the working tree, so the
  evidence must be too: a unit that flips its own spec to CLOSED on its branch has its certifying
  commits on that branch and nowhere else. Measured: replaying the 13 judged specs at the commit the
  default branch sat on just before each CLOSED flip landed, a base-only walk reds 2 of 13 correct
  closes. `drift-audit records` carries `guard = []` in `tools/drift-audit/kit.toml`, so it runs on
  every branch-scoped bar, which is exactly when that false red would fire.
- **S4** — `--no-merges`. A reconcile merge's subject names the branch being merged INTO, so a merge
  certifies whichever build it was merged into rather than the build that shipped. Measured: merges
  counted reads 0 misses, merges dropped reads 1, and the difference is entirely `TOOL-aMooredAnchor-1`
  resting on two conflict-resolving merge subjects. Dropping merges also removes the traversal
  ambiguity that default history simplification would otherwise leave in the answer.
- **S5** — `TRACE_CUTOFF` in `tools/drift-audit/drift_signals.py`, set to `2026-08-11`, carrying the
  commit and the reason in a comment. When it is absent or empty the signal returns
  `gateable: False`, so it is neither gated nor scored DEAD. This is an ENGINE behaviour, not a
  project declaration: `DECLARED_EMPTY` lives in each adopter's own layer and so reaches neither the
  selftest fixture nor an existing adopter, which is where the dead-and-undeclared red would land.
- **S6** — `TRACE_GLOBS` in the project layer: `PRODUCT_GLOBS` minus `.claude/` and
  `memory/guides/SESSION-KICKOFF.md`. Those two are product CONFIGURATION that a records or kickoff
  commit routinely touches, so leaving them in lets the house's own bookkeeping certify the
  bookkeeping. Absent in an adopter's layer, the engine falls back to `PRODUCT_GLOBS`.
- **S7** — `PINS["closed_specs_with_no_product_commit"] = 1`, seeded at the measured value, with
  `TOOL-aMooredAnchor-1` named in the comment as the oracle's known residual: its build commits are
  `59b4710` and its siblings, which predate by hours the subject convention it is being judged by.
- **S8** — `TRACE_CUTOFF` and `TRACE_GLOBS` documented in `tools/drift-audit/drift_signals.template.py`
  and shipped ABSENT, and a `[[hole]]` with `id = "drift-trace-cutoff"`, `kind = "authoring"`,
  `blocks_gate = true` in `tools/drift-audit/kit.toml`, discharged by a probe asserting the key is set
  and non-empty. Without the hole an adopter's unfilled cutoff leaves the signal permanently inert.
- **S9** — the selftest fixture. `make_repo()` gains `TRACE_CUTOFF` in its inline project layer, one
  post-cutoff CLOSED spec certified by a product-touching commit subject, one post-cutoff CLOSED spec
  with no such commit, and one pre-cutoff CLOSED spec. All three are distinct from the `aThing` spec
  the existing arms mutate. The new signal must NOT enter the fixture's `DECLARED_EMPTY`.
- **S10** — four arms in `tools/drift-audit/selftest.py`: silent when the certifying commit exists;
  fires when the only commit naming the spec touches nothing under `TRACE_GLOBS`; the pre-cutoff spec
  stays in `unjudgeable` while the post-cutoff one is judged in the same run; and a commit whose only
  mention of the slug is in a MERGE subject does not certify.
- **S11** — the signal-count numeral DELETED, not incremented, everywhere it is spelled in prose:
  `AGENTS.md`, `tools/drift-audit/README.md`, `tools/drift-audit/SKILL.template.md` and its rendered
  twin, `tools/drift-audit/drift_report.py`, `tools/drift-audit/drift_signals.template.py`,
  `WIRE-INTO-PROJECT.md`. `SIGNALS` is the only place the count cannot rot; the tables gain a row.
- **S12** — `KIT_DRIFT_AUDIT_VERSION` to `1.2` and every marker site with it, listed in §4.
- **S13** — `memory/map/generated/` re-rendered, and the `TOOL` backlog row for the dropped
  acceptance-witness unit written before this spec closes.

## 3. Non-goals (OUT)

- **Fidelity.** This unit measures that a link exists, never that the build matches the spec's design
  or its acceptance criteria. A build citing its unit correctly and implementing something else passes.
  That judgement stays with the M4 spec audit and the M8 closing review.
- **The §6 acceptance-witness rule.** Scoped at kickoff, deferred on cost rather than on evidence —
  see D1 in the build README, which states plainly that the measurement is SILENT on it. Backlog row
  per S13; built if the owner asks.
- **Retrofitting the 36 grandfathered CLOSED specs.** They landed under a subject convention that
  named the unit number or the slug.
- **The 18 non-terminal specs authored before the cutoff.** Keying on the status-header date rather
  than the filename date brings them into the population when they close, which is the point of the
  choice; but a spec whose header date never advances past the cutoff stays out. That is the honest
  residual, and §4 records the risk the header key trades in.
- **A CLOSED unit whose deliverable is `memory/` or the charter only.** Such a unit has no
  `TRACE_GLOBS` commit and will fire. The remedy is NOT to raise the pin: it is a per-spec row in a new
  shrink-only `memory/project/trace-waiver.txt`, added when the first real instance appears. Named
  here so the first occurrence is not resolved by the ratchet it would defeat.
- **A new gate leg.** The signal rides `drift-audit records` and `drift-audit selftest`, both on the
  bar. No entry is added to `tools/gate-legs.json`.
- **Reading commit BODIES.** Subject only. A body mention is how a later build refers to an earlier
  one, so accepting bodies would let any build certify every build it cites.
- **A new codebase-map dossier.** drift-audit sits unclaimed in the shrink-only
  `memory/map/baseline.toml`; a dossier would claim keys held there and red the coverage gate.

### The two questions this build was opened to answer

*How do we know a specced build was built from its spec?* Four mechanisms, and until this unit only
one was measured: the id-in-subject convention (`memory/guides/BUILD-METHOD.md`, unenforced), signal 2
of drift-audit (measured, opposite direction), the M4 and M8 reviews (judgement, recorded under each
build's `reviews/`), and the build status derived from spec headers by `gen_build_index.py` (authored,
never compared against git).

*What are the chances a build is invented?* Measured over all 49 CLOSED specs: none were. Every one
has a real commit trail. The apparent gaps under three progressively weaker oracles are the
pre-2026-08-11 subject convention, verified by reading the commits that landed three of them.

## 4. Design

### Data model

The signal returns the dict shape every other signal returns. `value` counts judged CLOSED specs with
no qualifying commit. `of` is the judged population. `unjudgeable` counts CLOSED specs skipped for
being before the cutoff, for carrying no parseable H1 id, or for carrying no parseable header date, so
the report distinguishes "nothing was wrong" from "nothing was looked at". `detail` rows carry the
spec path, id, slug and the date the cutoff was judged on.

### Inventory

| Item | Where | Change |
|---|---|---|
| `signal_closed_specs_untraceable` | `drift_report.py` | new, appended to `SIGNALS` |
| `_OWN_ID` | `drift_report.py` | second capture group for the slug; group 1 unchanged, so signal 2 is untouched |
| `_HEADER_DATE`, `TERMINAL` | `drift_report.py` | new pattern and frozenset holding `CLOSED` only |
| `Ctx.trace_cutoff`, `Ctx.trace_globs` | `drift_report.py` | read from the project layer, `trace_globs` falling back to `PRODUCT_GLOBS` |
| `TRACE_CUTOFF`, `TRACE_GLOBS`, `PINS` | `drift_signals.py` | new keys, pin at 1 |
| same two keys | `drift_signals.template.py` | documented, shipped absent |
| `[[hole]] drift-trace-cutoff` | `kit.toml` | new |
| `make_repo` + four arms | `selftest.py` | S9, S10 |
| signal table + count | `README.md`, `SKILL.template.md`, rendered `.claude/skills/drift-audit/SKILL.md` | row added, numeral deleted |
| signal count in prose | `AGENTS.md`, `WIRE-INTO-PROJECT.md`, `drift_report.py`, `drift_signals.template.py` | numeral deleted |
| `KIT_DRIFT_AUDIT_VERSION` 1.1 to 1.2 | `drift_report.py` constant and docstring, `drift_signals.py`, `drift_signals.template.py`, `selftest.py`, `adopt-drift-audit.sh`, `README.md`, and `version:` plus `gov:kit` in both `tools/workflows/drift-audit-*.js` | bumped together; `check-kit-versions.sh` cross-asserts all of them |
| generated map | `memory/map/generated/` | re-rendered |

### The commit walk

One `git log` over both tips, `--no-merges`, path-restricted to `TRACE_GLOBS`, `--format=%s`. Matching
is a word-boundary search for the id and for the slug.

`WONTDO` is excluded from `TERMINAL`: an abandoned unit is expected to have no product commit, so
judging it would manufacture a false positive out of a correct record.

The slug is accepted alongside the id because it is what the corpus actually carries. Over the judged
population the id-only key misses 3 of 13 — `TOOL-aMooredAnchor-1`, `TOOL-aMouldedFolio-2` and
`TOOL-aStandingWrit-1` — against the slug-or-id key's 1. The id-only key is the stronger, unit-level
claim and is the tightening this signal should take once every build carries id subjects; that is F1
and a backlog row, not this unit.

### Why the header date and not the filename date

`memory/TEMPLATE-SPEC.md` states that the status header is updated in place on every state change and
that its date is the last-change date, so for a CLOSED spec it IS the close date. The filename date is
the WRITE date, and keying on it exempts 18 currently in-flight specs forever even though every one of
them will close under the post-cutoff convention. Measured, the swap costs nothing today: both keys
yield the same 13-spec population and the same verdicts. The risk it trades in, recorded rather than
hidden: touching a grandfathered CLOSED spec's header advances its date and pulls it into the
population, where it will red for want of a convention it never had. That red is visible and its
remedy is the §3 waiver row.

### Rollout

The cutoff makes this inert for every spec that landed before the convention did. The signal starts at
its pin of 1 over a live population of 13 and reds on the next CLOSED spec, at or after the cutoff,
with no product commit behind it.

### Files touched (estimate)

Ten source and doc files, one kit descriptor, one generated map tree. No new source file, no new gate
leg, no new conf.

### Alternatives rejected

- **Key on the id alone.** Reads 3 misses of the 13 judged, against 1. The right key eventually, and
  a ratchet this unit does not turn. The figure of 38 that an earlier revision cited was measured over
  the 49-spec corpus this signal never judges, which is the `pin-copied-from-another-corpus` class
  applied to a design fork.
- **Read the spec population from `base_ref` too.** Symmetric, and it would make the signal silent on
  a branch — which also makes it useless as a gate, since the only moment it could catch a bad close
  is before that close lands.
- **Accept any commit naming the unit, product-touching or not.** Nearly unfalsifiable: the commit
  that adds a build's own spec file usually names the slug in its subject.
- **Count merge commits.** Reads 0 misses today, and the 0 is an artifact of reconcile subjects naming
  the merge target.
- **Reuse `PRODUCT_GLOBS` unchanged.** It holds `.claude/` and the kickoff manifest, so a records
  commit certifies the record. Today the narrowing changes no verdict; it is a correctness fix taken
  before it costs something, not after.
- **Put the cutoff in `.memory-tree.conf`.** That conf belongs to the memory-tree kit, and this kit
  declares no conf of its own.

## 5. Production-readiness checklist

- security — N/A. Read-only over git and the working tree; no new input crosses a trust boundary.
- perf / scale — one extra path-restricted `git log` per report. The report's budget is seconds.
- a11y — N/A. A terminal table and a JSON document.
- i18n — N/A. Identifiers and paths only.
- error / empty / loading states — an absent `TRACE_CUTOFF` yields `gateable: False`; an unparseable
  id or header date increments `unjudgeable` rather than being guessed at.
- observability — the signal prints on the standard report row and in `--json` detail.
- risks — the false-negative risk is §3 and D2 of the build README. The header-date key can pull a
  grandfathered spec into the population if its header is touched, remedied by the §3 waiver row. The
  vacuity risk is answered by S10, which forces the signal to fire.
- testing + left-shift gates — four selftest arms on `drift-audit selftest`; the pin on
  `drift-audit records`; the unfilled-cutoff class left-shifted into a `kit.toml` hole.
- migration / rollback — delete the function from `SIGNALS` and the keys from the project layer. No
  state. Adopters take it on the next kit pull, inert until they fill the hole.
- user docs — the signal tables in `README.md` and `SKILL.template.md`, and the charter bullet.

## 6. Acceptance criteria

- **AC1** — When `python tools/drift-audit/drift_report.py` runs on this tree, the row
  `closed_specs_with_no_product_commit` prints value 1 against an `of` equal to the count `--json`
  reports for it, with status `ok (pin 1, drain it)` and NOT `DEAD PROBE`. The population is stated as
  a shape because this unit's own spec moves it.
- **AC2** — When the fixture's post-cutoff CLOSED spec has no product-touching commit naming it,
  `python tools/drift-audit/selftest.py` shows that arm firing with value 1; when a commit touching
  `src/` and naming its slug is added, the same arm returns 0.
- **AC3** — When the fixture's pre-cutoff CLOSED spec is judged in the same run, it appears in
  `unjudgeable` and not in `value`, proving the cutoff grandfathers rather than blinds.
- **AC4** — When the only commit naming the fixture's uncertified spec is a MERGE whose subject names
  its slug, the signal still counts it a miss.
- **AC5** — When `python tools/drift-audit/drift_report.py --check` runs on this tree it exits 0; when
  the pin is lowered to 0 in a scratch copy it exits 1 naming the signal.
- **AC6** — When `GATE_FULL=1 bash tools/run-gates.sh` runs on this branch BEFORE the merge, all 54
  legs are green and the leg count is unchanged. Stated on the branch deliberately: S3 exists so this
  is true there, and an earlier revision of this signal would have failed it.
- **AC7** — When `python tools/drift-audit/drift_report.py` runs with `TRACE_CUTOFF` removed from the
  project layer in a scratch copy, the signal reports `gateable: False` and `--check` still exits 0.

## 7. Gates

`drift-audit selftest` · `drift-audit records` · `drift-audit wiring` · `memory hygiene (20 checks)` ·
`kit version markers` · `codebase-map coverage + freshness` · `harness meta-gate (check-arms)` ·
`govkit selfcheck` · `kickoff-manifest ratchet`, and the full bar at the push boundary.

## 8. Open questions

- **F1 — slug-or-id, or id only?** Over the judged population the id-only key misses 3 of 13 and the
  slug-or-id key misses 1. Id-only is the unit-level claim and the stronger ratchet.
  RESOLVED (agent, 2026-08-14, delegated): slug-or-id, pin 1, with the id-only tightening filed as a
  backlog row. Three known-false reds on the first run of a new predicate is how a signal gets
  disbelieved; the tightening is cheap once id subjects are universal.
- **F2 — is `2026-08-11` the right cutoff?** A cutoff of `2026-08-12` reads 0 misses over 3 judged
  specs, dropping ten from the population to avoid investigating three entries.
  RESOLVED (agent, 2026-08-14, delegated): `2026-08-11`, the day the convention landed. The three
  entries were investigated and are convention-era false positives, not rot. Choosing a date because
  it makes a signal read zero is the vacuous-selector class.
- **F3 — should `WONTDO` be judged?** RESOLVED (agent, 2026-08-14, delegated): no. An abandoned unit
  correctly has no product commit; judging it puts a permanent false positive in the population.
- **F4 — the `memory/`-only-deliverable class.** No instance exists today, so the waiver registry is
  specified in §3 but NOT created. RESOLVED (agent, 2026-08-14, delegated): specify, do not build. An
  empty shrink-only list is a ratchet that can never turn, and creating one now would need its own
  `DECLARED_EMPTY` entry to avoid reding signal 3.

## 9. Revision log

- rev-1 · 2026-08-14 · initial draft, written against the measurement in the build README.
- rev-2 · 2026-08-14 · folded the M4 audit (`wf_b8f7a1f2-240`): 28 confirmed findings of 35 raised,
  four of them blockers. The base-only walk became a union of both tips (S3), merges were dropped and
  the pin re-seeded 0 to 1 (S4, S7), the cutoff moved from the filename date to the status-header date,
  the evidence globs narrowed off `PRODUCT_GLOBS` (S6), the absent-cutoff case moved from a project
  declaration to an engine `gateable` (S5), the fixture and its four arms were specified (S9, S10),
  the signal-count numeral was deleted rather than incremented (S11), the version bump was resolved
  (S12), the non-existent dossier was dropped from acceptance, and every count measured over the
  49-spec corpus was restated over the 13 this signal judges. All four forks resolved under the
  delegated authority of the session mandate.

## 10. Reuse audit

`python tools/codebase-map/reuse_lookup.py "spec compliance verification"` returned `signal_spec_status`
(`tools/drift-audit/drift_report.py`) and `parse_spec` (`tools/memory-tree/gen_build_index.py`) as the
ranked candidates, both fan-in 0. The seam this unit wires through is `signal_spec_status`: the new
function is its mirror and reuses its `_STATUS` and `_OWN_ID` patterns, the `Ctx` declarations and the
`Git` helper, adding only the commit walk. `parse_spec` was rejected as a seam — it reads build front
matter for the index renderer and would drag the memory-tree kit into a drift-audit signal, which the
kit's no-cross-import rule forbids.
