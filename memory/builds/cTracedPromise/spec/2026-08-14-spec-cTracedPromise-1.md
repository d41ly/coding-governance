# TOOL-cTracedPromise-1 — a closed spec has to point at a commit that changed the product

**Status:** OPEN · rev-1 · 2026-08-14 · node c · Tier-2 · base 37c05e1b · streams tooling

## 1. Goal

Add a sixth drift-audit signal that reds when a spec claims CLOSED and no commit reachable from the
default branch both names that unit and touches product source. It closes the reverse of the direction
`non_terminal_specs_cited_by_product_source` already measures, so the pair covers both ways a spec
status can lie about git.

## 2. Scope (IN)

- **S1** — `signal_closed_specs_untraceable` in `tools/drift-audit/drift_report.py`, appended to
  `SIGNALS`. Gateable. Reports `value`, `of`, `live` and `unjudgeable` on the same contract the five
  existing signals use.
- **S2** — the oracle: for each spec whose status is `CLOSED` and whose filename date is on or after
  the project layer's `TRACE_CUTOFF`, at least one commit reachable from the report's `base_ref` must
  carry the spec's own id OR its slug in its SUBJECT and touch a `PRODUCT_GLOBS` path in the same
  commit. A spec that fails this is a `suspect` row naming the file, the id and the slug.
- **S3** — `TRACE_CUTOFF` in `tools/drift-audit/drift_signals.py`, set to `2026-08-11`, carrying in a
  comment the commit and the reason that date and no other. Absent or empty in an adopter's layer, the
  signal judges nothing and reports `live: False`.
- **S4** — the same key documented in `tools/drift-audit/drift_signals.template.py`, shipped ABSENT
  with `closed_specs_with_no_product_commit` in that file's `DECLARED_EMPTY`, so a fresh adopter does
  not red on their first run for doing what the template told them.
- **S5** — `PINS["closed_specs_with_no_product_commit"] = 0` in this repo's project layer, seeded at
  the measured value over the 13 post-cutoff CLOSED specs.
- **S6** — two arms in `tools/drift-audit/selftest.py` over the existing fixture repo: the signal is
  silent when a CLOSED spec's slug names a product-touching commit, and fires when the only commit
  naming it touches nothing under `PRODUCT_GLOBS`.
- **S7** — a third arm proving the cutoff is not a muzzle: a CLOSED spec dated BEFORE the fixture's
  `TRACE_CUTOFF` stays unjudged while a spec dated on or after it is judged in the same run.
- **S8** — the charter's gate-suite bullet for `drift-audit records` updated from five signals to six,
  and `memory/map/features/` refreshed for the drift-audit dossier.

## 3. Non-goals (OUT)

- **Fidelity.** This unit measures that a link exists, never that the build matches the spec's design
  or its acceptance criteria. A build citing its unit correctly and implementing something else passes.
  That judgement stays with the M4 spec audit and the M8 closing review.
- **The §6 acceptance-witness rule.** Scoped at kickoff and dropped on the evidence in the build
  README's D1. Follow-up: a `TOOL` backlog row, built only if the owner asks.
- **Retrofitting the 36 pre-cutoff CLOSED specs.** They landed under a subject convention that named
  the unit number or the slug. Grandfathered by filename date, as `SPEC_FORMAT_CUTOFF` grandfathers
  spec shape. Never retrofit them.
- **A new gate leg.** The signal rides `drift-audit records` and `drift-audit selftest`, both already
  on the bar. No entry is added to `tools/gate-legs.json`.
- **Reading commit BODIES.** Subject only. A body mention is how a later build refers to an earlier
  one, so accepting bodies would let any build certify every build it cites.

### The two questions this build was opened to answer

Recorded here because the answer, not the code, is the deliverable the owner asked for.

*How do we know a specced build was built from its spec?* Four mechanisms, and until this unit only
one was measured: the id-in-subject convention (`memory/guides/BUILD-METHOD.md`, unenforced), signal 2
of drift-audit (measured, opposite direction), the M4 and M8 reviews (judgement, recorded under each
build's `reviews/`), and the build status derived from spec headers by `gen_build_index.py` (authored,
never compared against git).

*What are the chances a build is invented?* Measured over all 49 CLOSED specs in the tree: none were.
Every one has a real commit trail. The apparent gaps of 35, 18 and 12 under three progressively
weaker oracles are all the pre-2026-08-11 subject convention, verified by reading the commits that
landed three of them rather than by inference.

## 4. Design

### Data model

The signal returns the dict shape every other signal returns. `value` is the count of CLOSED specs at
or after the cutoff with no qualifying commit. `of` is the judged population. `unjudgeable` counts the
CLOSED specs skipped for being before the cutoff or for carrying no parseable H1 id, so the report
distinguishes "nothing was wrong" from "nothing was looked at". `detail` rows carry the spec path, the
id, the slug and the date.

### Inventory

| Item | Where | Change |
|---|---|---|
| `signal_closed_specs_untraceable` | `tools/drift-audit/drift_report.py` | new function, appended to `SIGNALS` |
| `_OWN_ID` | `tools/drift-audit/drift_report.py` | second capture group for the slug; the existing signal reads group 1 and is unaffected |
| `TERMINAL` | `tools/drift-audit/drift_report.py` | new frozenset holding `CLOSED` only |
| `TRACE_CUTOFF` | `tools/drift-audit/drift_signals.py` | new, `2026-08-11` |
| `PINS` | `tools/drift-audit/drift_signals.py` | one row at 0 |
| `TRACE_CUTOFF`, `DECLARED_EMPTY` | `tools/drift-audit/drift_signals.template.py` | documented, shipped absent and declared |
| three arms | `tools/drift-audit/selftest.py` | S6 and S7 |
| gate-suite bullet | `AGENTS.md` | five signals becomes six |

### The commit walk

One `git log` over `base_ref` restricted to `PRODUCT_GLOBS` with `--format` carrying the subject,
producing the set of subjects belonging to product-touching commits. `WONTDO` is deliberately excluded
from `TERMINAL` here: an abandoned unit is expected to have no product commit, so including it would
manufacture a false positive out of a correct record.

Matching is a word-boundary search for the id and for the slug. The slug is accepted because the
measured corpus carries it far more often than the id, and because a slug hit here cannot over-certify
the way it does in signal 2: that signal asks whether ANY citation exists and a slug would certify
every sibling at once, while this one asks whether a build happened at all, which is a build-level
question the slug answers correctly.

### Rollout

The cutoff makes this inert for every spec that landed before the convention did, so the signal starts
green over a live population of 13 and reds on the next CLOSED spec with no product commit behind it.

### Files touched (estimate)

Four source files, one charter section, one map dossier. No new file, no new gate leg.

### Alternatives rejected

- **Key on the id alone.** Reads 38 of 49 CLOSED specs as untraceable, all false. It is the correct
  key for signal 2 and the wrong one here.
- **Accept any commit naming the unit, product-touching or not.** Nearly unfalsifiable: the commit
  that adds a build's own spec file usually names the slug in its subject, so the signal would pass on
  the record-writing commit alone and could not distinguish a built unit from a written one.
- **Put the cutoff in `.memory-tree.conf`.** That conf belongs to the memory-tree kit, and this kit
  declares no conf of its own. A repo-shaped constant belongs in the project layer beside `PINS`.
- **A new gate leg.** Nothing to run that the two existing drift-audit legs do not already run.

## 5. Production-readiness checklist

- security — N/A. Read-only over git and the working tree; no new input crosses a trust boundary.
- perf / scale — one extra `git log` per report, path-restricted. The report's budget is seconds.
- a11y — N/A. A terminal table and a JSON document.
- i18n — N/A. Identifiers and paths only.
- error / empty / loading states — an absent `TRACE_CUTOFF` yields `live: False`; a spec with no
  parseable id increments `unjudgeable` rather than being guessed at.
- observability — the signal prints on the standard report row and in `--json` detail.
- risks — the false-negative risk is stated in §3 and D2 of the build README; the vacuity risk is
  answered by S6 and S7, which force it to fire.
- testing + left-shift gates — three selftest arms, riding `drift-audit selftest`; the pin rides
  `drift-audit records`.
- migration / rollback — delete the function from `SIGNALS` and the key from `PINS`. No state.
- user docs — `tools/drift-audit/README.md` signal list, and the charter bullet.

## 6. Acceptance criteria

- **AC1** — When `python tools/drift-audit/drift_report.py` runs on this tree, the row
  `closed_specs_with_no_product_commit` prints `0` of `13` with status `ok`, and NOT `DEAD PROBE`.
- **AC2** — When a CLOSED spec dated on or after the cutoff has its slug and id removed from every
  product-touching commit subject in a scratch fixture, `python tools/drift-audit/selftest.py` shows
  the arm firing with value 1.
- **AC3** — When that same fixture spec is re-dated to before the fixture's `TRACE_CUTOFF`, the signal
  returns to 0 and reports the spec in `unjudgeable`, proving the cutoff grandfathers rather than
  blinds.
- **AC4** — When `python tools/drift-audit/drift_report.py --check` runs on this tree, it exits 0, and
  when the pin is lowered below the measured value in a scratch copy it exits 1 naming the signal.
- **AC5** — When `GATE_FULL=1 bash tools/run-gates.sh` runs, all 54 legs are green and no leg count
  changes.
- **AC6** — When `python tools/codebase-map/test_codebase_map.py` runs, it is green: the drift-audit
  dossier claims the new signal and the generated artifacts byte-compare against a fresh render.

## 7. Gates

`drift-audit selftest` · `drift-audit records` · `drift-audit wiring` · `memory hygiene (20 checks)` ·
`codebase-map coverage + freshness` · `harness meta-gate (check-arms)` · `kit version markers` ·
`kickoff-manifest ratchet`, and the full bar at the push boundary.

## 8. Open questions

- **F1 — should the signal accept the slug, or only the id?** Accepting the slug makes it a
  build-level claim; the id would make it unit-level and read 38 false positives on this corpus.
  Recommendation: accept both, as designed. The unit-level version is a ratchet that could be tightened
  later once every build carries id subjects, and the backlog row should say so.
- **F2 — is `2026-08-11` the right cutoff, or should it be `2026-08-12`?** The later date makes the
  signal read 0 over 3 rather than 0 over 13, which is a smaller live population chosen only to avoid
  investigating two entries. Recommendation: `2026-08-11`, the day the convention landed, since both
  boundary entries were investigated and are false positives of the id-only oracle, not of this one.
- **F3 — should `WONTDO` be judged?** Recommendation: no, as designed. An abandoned unit correctly has
  no product commit, and judging it would put a permanent false positive in the population.

## 9. Revision log

- rev-1 · 2026-08-14 · initial draft, written against the measurement in the build README.

## 10. Reuse audit

`python tools/codebase-map/reuse_lookup.py "spec compliance verification"` returned `signal_spec_status`
(`tools/drift-audit/drift_report.py`) and `parse_spec` (`tools/memory-tree/gen_build_index.py`) as the
ranked candidates, both fan-in 0. The seam this unit wires through is `signal_spec_status`: the new
function is its mirror and reuses its `_STATUS` and `_OWN_ID` patterns, the `Ctx.product_globs`
declaration and the `Git` helper, adding only the commit walk. `parse_spec` was rejected as a seam —
it reads build front matter for the index renderer and would drag the memory-tree kit into a
drift-audit signal, which the kit's no-cross-import rule forbids.
