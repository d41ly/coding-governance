# TOOL-dClosedLexicon-4 — a `**` file rule must not claim what another rule already owns

**Status:** CLOSED · rev-2 · 2026-08-16 · node d · Tier-2 · base f7306f35 · streams tooling

## 1. Goal

`govkit apply` destroys an adopter's project-owned files on every re-apply. Reproduced end to end
against `drift-audit`, which still carries the shape:

```
apply --target <t> --kits drift-audit     # 8 files
<adopter appends a line to tools/drift-audit/drift_signals.py>
apply --target <t> --kits drift-audit     # 8 files
grep -c 'MY ADOPTER PINS' …/drift_signals.py   ->  0
```

The descriptor says what it means — `drift_signals.py` is declared `project-owned`, and
`drift_signals.template.py` is a `seed` whose destination is `{kit}/drift_signals.py` — but the
`include = "**"` engine rule above them pools EVERY tracked file under `home`, writes it
unconditionally, and reaches that path first. `project-owned` is not in `LANDABLE_ROLES` at all, so
it lands nothing and protects nothing; `seed`'s "copied ONCE, then the target owns it" guard never
runs, because the file already exists by the time the seed rule is evaluated.

The declaration reads as "everything not otherwise claimed". This unit makes it mean that.

## 2. Scope (IN)

- **S1** — a `**` include resolves to every tracked file under `home` MINUS anything whose
  DESTINATION another rule in the same descriptor claims. Destination, and NOT source: see §4, where
  the source half was built, measured to under-land, and cut.
- **S2** — ONE spelling of destination resolution. The write loop computes destinations inline
  today; S1 needs the same answer before the loop runs, and two computations of one thing is the
  class this repo has a record about. Extract it, call it twice.
- **S3** — `tools/drift-audit/kit.toml` keeps its `**` rule, now correct by the engine's semantics
  rather than by enumeration. `tools/lexicon/kit.toml` — which enumerates its engine files precisely
  to dodge this defect — reverts to `**`, because the workaround's own cost is filed as
  `TOOL-dClosedLexicon-5` (a new kit file is silently undeployed until someone edits the list).
- **S4** — arms in `tools/govkit/selftest.py`: a re-apply preserves an adopter's edit to a
  project-owned file; a re-apply preserves a seeded file the target has edited; and a `**` rule still
  lands every file NOT otherwise claimed, so the fix cannot pass by shipping nothing.

## 3. Non-goals (OUT)

- An `exclude` key on `[[files]]`. It would work and it is worse: every descriptor author would have
  to remember it, and the defect returns for whoever does not. The wildcard's meaning is what was
  wrong, so the wildcard is what changes.
- Making `project-owned` landable. It is correctly non-landable — gov must never write an adopter's
  project layer. The bug is that another rule wrote it anyway.
- Last-write-wins rule ordering. It does not help: `project-owned` lands nothing, so there is no
  later write to win.
- Any change to `plan` or `check`. They are read-only and stay that way.

## 4. Design

### The exclusion is computed, not declared

For a rule R whose include contains `**`:

```
claimed = ⋃ over rules R' ≠ R of destinations(R')
pool(R) = { tracked files under home } − { s : dest(R, s) ∈ claimed }
```

**DESTINATION ONLY, and the first cut got this wrong.** rev-1 also excluded claimed SOURCES, on the
reasoning that `project-owned` names the file it owns. That is true and it does not matter: what
needs protecting is the PATH IN THE TARGET, and `dests_for` maps `drift_signals.py` to
`{kit}/drift_signals.py` for the project-owned rule just as it does for the seed rule. Excluding the
source as well silently stopped shipping `drift_signals.template.py` — whose own destination nothing
claims, and which an adopter's later re-seed depends on. MEASURED: 8 files landed before the change,
6 after, and the two that vanished were not the two being protected. This is the under-landing risk
§5 names, caught by AC3 rather than by review, which is why AC3 is asserted BEFORE the two protection
arms in the selftest: the cheapest way to pass them is to stop landing anything.

### Why not just reorder

`project-owned` is not landable, so no ordering makes it overwrite the engine rule's bytes. And a
seed rule that runs first would be correct only by accident — the next descriptor that lists its
rules in the other order would break again. An order-independent rule is the only kind a descriptor
author cannot get wrong by writing lines in a different sequence.

### Data model

None. No descriptor key is added or removed; `tools/lexicon/kit.toml` loses an enumeration it only
had as a workaround.

### Files touched (estimate)

`tools/govkit/govkit.py`, `tools/govkit/selftest.py`, `tools/lexicon/kit.toml`. No version bump for
`drift-audit` — its descriptor is unchanged; what changes is how the engine reads it.

### Alternatives rejected

- **An `exclude` key** — §3.
- **Excluding by source only** — silently leaves the `seed` case broken, which is the half that
  looks most protected because `seed` carries an explicit "copied ONCE" guard.
- **Refusing a `**` rule that overlaps another** — a refusal makes the two live descriptors
  un-appliable until edited, and the overlap is the NORMAL way to say "everything else".

## 5. Production-readiness checklist

- security — N/A. Local file writes into an operator-named target.
- perf / scale — one extra pass over a descriptor's rules; the pool is already materialised.
- a11y / i18n — N/A.
- error / empty / loading states — a descriptor whose every file is claimed yields an EMPTY `**`
  pool, which is legal and lands nothing extra.
- observability — `plan` output already lists destinations per role, so the exclusion is visible
  before any write.
- risks — the real one is under-landing: an exclusion that is too broad silently stops deploying a
  file. S4's third arm exists for exactly that and is why the fix cannot pass by shipping nothing.
- testing + left-shift gates — S4, in `tools/govkit/selftest.py`.
- migration / rollback — none needed; no descriptor changes shape.
- user docs — the wildcard's meaning is stated at the code that implements it.

## 6. Acceptance criteria

- **AC1** — When `apply` runs twice against one target with an adopter edit to a `project-owned`
  file in between, the edit survives. (Today: destroyed. Reproduced above.)
- **AC2** — When the same happens to a file a `seed` rule owns, the edit survives.
- **AC3** — When a descriptor's `**` rule covers files no other rule claims, those files are still
  landed — the fix does not pass by deploying nothing.
- **AC4** — When `python tools/govkit/govkit.py selfcheck` and `python tools/govkit/selftest.py`
  run, both are green, and `tools/lexicon/kit.toml`'s reverted `**` lands the same file set the
  enumeration did.
- **AC5** — When `bash tools/run-gates.sh` runs on the landing commit, it is green.

## 7. Gates

Existing legs that must stay green: `python tools/govkit/govkit.py selfcheck`,
`python tools/govkit/selftest.py`, `python tools/codebase-map/test_codebase_map.py`. This unit adds
no leg; it adds arms to one that already rides the bar.

## 8. Open questions

- **F1 — should `tools/lexicon/kit.toml` revert to `**`?** RESOLVED (agent, 2026-08-16, delegated):
  yes, per S3. The enumeration was written as a workaround for this exact defect and carries its own
  cost, already filed as `TOOL-dClosedLexicon-5`. Reverting it is what proves the fix on a second
  descriptor rather than only on the one that motivated it.

## 9. Revision log

- rev-2 · 2026-08-16 · BUILT and CLOSED. S1 narrowed from "source or destination" to DESTINATION
  ONLY: the source half was implemented, measured to under-land by two files, and cut — §4 carries
  the measurement. Every AC verified, and the two protection arms verified by REVERTING the fix and
  watching the named arm red. `tools/lexicon/kit.toml` reverts to `**` per S3, which closes
  `TOOL-dClosedLexicon-5` and proves the fix on a second descriptor rather than only on the one that
  motivated it.
- rev-1 · 2026-08-16 · initial draft, written after reproducing the clobber end to end against
  `drift-audit` rather than from the backlog row's description.

## 10. Reuse audit

`python tools/codebase-map/reuse_lookup.py "deploy file rules into a target repo"` ranks
`registry.toml` and `govkit` itself; there is no second implementation of file-rule resolution to
reuse or to converge with. The seam this unit CREATES is S2's destination resolver, which is
extracted from the write loop rather than written fresh — the same shape `check-verifier-fanout.sh`
uses to keep one predicate with two entry points. No existing seam covers wildcard-minus-claimed,
which is the whole of what changes.
