# TOOL-dLandedVerdict-1 — the signal for a spec that landed and never said so
**Status:** INPROGRESS · rev-1 · 2026-08-19 · node d · Tier-2 · base 098bebd9 · streams tooling

## 1. Goal

Add a drift-audit signal that reports a spec still carrying a non-terminal status although its unit's
work is already reachable from the default branch. It closes the hole left by
`non_terminal_specs_cited_by_product_source` and `closed_specs_with_no_product_commit`, whose shared
docstring claims the pair covers both ways a status can lie about git.

## 2. Scope (IN)

- **S1** — `landed_specs_left_non_terminal` in `tools/drift-audit/drift_report.py`, one function
  leading with a declared `.lexicon.conf` verb, registered in `SIGNALS`.
- **S2** — the predicate: a spec whose status token is in `NON_TERMINAL` and whose OWN id (H1 group 1,
  via the existing `_OWN_ID`) appears in the subject of a product commit reachable from the default
  branch.
- **S3** — `gateable: False`, threshold read as `tolerance` from `ctx.pins`, seeded in
  `drift_signals.py` `PINS` at the value measured at BASE with the measurement written beside it.
- **S4** — a `RATCHETS` row for the new pin, `weakens: "up"`, so a later raise must name both values.
- **S5** — a liveness assertion: a tree whose spec population or commit walk is empty reports DEAD
  rather than a reassuring 0.
- **S6** — arms in `tools/drift-audit/selftest.py`: silent on a clean fixture, firing on a minimal
  violating one, plus a not-gateable arm and a DEAD-probe arm.

## 3. Non-goals (OUT)

- Claiming a flagged spec SHOULD close. Five builds at BASE landed and must stay open; the signal
  reports candidates and says so in its docstring.
- Gating. Explicitly refused — see §8.
- Slug-keyed matching. Measured at 37 of 46 and reproduces the upstream 107-of-126 over-flag.
- Judging a spec with no parseable id or no status header. Those are counted as unjudgeable, never
  guessed.
- Any change to the two existing spec-status signals' predicates or pins.

## 4. Design

The signal is the third member of a family and reuses the family's machinery rather than adding any:
`_STATUS`, `_OWN_ID` and `NON_TERMINAL` already exist in `drift_report.py`, and the commit walk is
the one `signal_closed_specs_untraceable` performs.

### Data model

The walk is a `git log` over the default branch with `--no-merges`, `--full-history` and `--format=%s`,
path-restricted to `PRODUCT_GLOBS`. Both flags are inherited deliberately and their reasons are
recorded at the sibling's call site: `--no-merges` because a reconcile merge's subject names the
branch merged INTO and therefore certifies the wrong build, and `--full-history` because a
path-restricted walk drops a commit that is TREESAME with a parent, which lets a build's own product
commit vanish behind an unrelated merge.

The anchor is the DEFAULT BRANCH, not `HEAD`. This is the one place the new signal must differ from
its sibling. `signal_closed_specs_untraceable` walks from `base_ref` to `HEAD` so a unit closing its
own spec on its own branch can be certified by commits that exist only there. This signal asks the
opposite question — has the work reached the shared trunk — and a branch-local commit is precisely
what must NOT answer it, or every in-flight unit reads as landed on its own branch.

### Inventory

| carrier | change |
|---|---|
| `tools/drift-audit/drift_report.py` | the signal function; append to `SIGNALS` |
| `tools/drift-audit/drift_signals.py` | one `PINS` entry, one `RATCHETS` row |
| `tools/drift-audit/selftest.py` | one test function, registered in the runner |
| `AGENTS.md` | the drift-audit records leg's description names the new signal |

### Alternatives rejected

Slug-keying (37 of 46, over-flags siblings of a partially-landed build) and the
`**Serves:** diff-review` binding (15 of 46, blind to a closing review filed as `spec-audit`). Both
measured at BASE; the probes are recorded under `memory/builds/dLandedVerdict/build/`.

## 5. Production-readiness checklist

- security — N/A. Read-only over tracked records and git history; the engine writes nothing.
- perf / scale — one extra `git log` is avoided: the walk is shared with the sibling signal.
- a11y — N/A. Not a user interface.
- i18n — N/A. Not a user interface.
- error / empty / loading states — an empty spec population or empty walk reports DEAD, per S5.
- observability — the signal's `detail` names every flagged spec by path and id.
- risks — a false positive costs a reader one lookup, never a blocked merge, because the signal is
  report-only. That asymmetry is why report-only was chosen.
- testing + left-shift gates — S6's arms; the `drift-audit selftest` and `drift-audit records` legs.
- migration / rollback — none. An adopter with no pin falls back to tolerance 0 and the signal still
  reports rather than gates, so an absent pin cannot red anyone's first run.
- user docs — the charter's gate-suite bullet, per the Inventory table.

## 6. Acceptance criteria

- **AC1** — When `python tools/drift-audit/drift_report.py` runs at BASE, a
  `landed_specs_left_non_terminal` line appears with a non-zero value and `detail` naming
  `aTetheredRecord` and `cKeyedLaunchpad` specs by path.
- **AC2** — When the signal is inspected under `--json`, its `gateable` field is `false`, so
  `python tools/drift-audit/drift_report.py --check` cannot red on it at any value.
- **AC3** — When `python tools/drift-audit/selftest.py` runs, it exercises the signal on a clean
  fixture (silent) and on a minimal violating fixture (fires), and both arms print.
- **AC4** — When a fixture has no spec population at all, the signal reports `live: false` — the
  `DEAD PROBE` line — rather than a value of `0`.
- **AC5** — When the pin in `tools/drift-audit/drift_signals.py` is raised with no adjacent comment
  naming the old and new values, `python tools/drift-audit/drift_report.py --check` reports a ratchet
  finding for it.

## 7. Gates

`bash tools/run-gates.sh` with `GATE_FULL=1`. The legs this unit moves: `drift-audit selftest`,
`drift-audit records`, `codebase-map coverage + freshness` (a new definition enters `symbols.json`),
and `memory/ hygiene`. `python tools/lexicon/lexicon.py` must not gain a verb offender — the function
name leads with a declared verb for that reason.

## 8. Open questions

none — the forks below are RESOLVED and kept for the record.

- **Gateable or report-only.** RESOLVED (owner, 2026-08-19): report-only with a shrink-only pin.
  Five builds at BASE are landed and legitimately non-terminal, and `drift-audit records` is an
  unguarded merge-bar leg, so a gateable version is a standing refusal on honest states.
- **Which key — id, slug, or the record binding.** RESOLVED (agent, 2026-08-19, delegated by the
  spec's own measurement): the unit id. The other two were measured and both fail; the slug arm
  reproduces a failure already recorded in the sibling's source comments.
- **Anchor the walk at the default branch or at `HEAD`.** RESOLVED (agent, 2026-08-19): the default
  branch, and this differs from the sibling on purpose. §4 records why.

## 9. Revision log

- rev-1 · 2026-08-19 · initial draft. Predicate chosen by measurement over three candidates; scope
  and gateability resolved by the owner the same day.

## 10. Reuse audit

A `tools/codebase-map/reuse_lookup.py` pass for the behaviour phrase "detect a build whose product
work landed on the default branch while its spec records stay non-terminal" returned
`build_live_backlog_rows` (`tools/drift-audit/drift_report.py`) as the closest seam, and that is the
seam this unit extends: the report-only, `tolerance`-read, liveness-asserting shape it established is
copied rather than re-invented. The predicate reuses `_STATUS`, `_OWN_ID` and `NON_TERMINAL` from the
same module and shares `signal_closed_specs_untraceable`'s commit walk. Recall terms used: spec
status header, terminal, wrap-up, generated index, drift signal, product commit, backlog row,
rotation.
