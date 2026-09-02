# TOOL-dRetiredFork-10 — three workflows gates anchor their locator and population on a basename

**Status:** OPEN · rev-1 · 2026-09-02 · node d · Tier-2 · base b0108f13 · streams tooling · order 2

<!-- gen:spec-records -->

*No record names this unit.*

<!-- /gen:spec-records -->

## 1. Goal

Stop `tools/workflows/check-review-join.sh`, `check-verifier-fanout.sh` and
`check-workflow-syntax.js` spelling `tools/` in their population and their hook path. Those three
literals generate `nc carve-out 10/20`, `11/20` and `12/20` and inCMS rows 16, 17 and 18 — six
declared divergence rows across two adopters, for a path each script can resolve from its own
location.

## 2. Scope (IN)

- **S1** — Each script derives its own directory (`HERE`) and resolves the agent-cap hook by probing
  `$HERE/hooks/agent-cap.js`, then `$HERE/../hooks/agent-cap.js`, then `$ROOT/.claude/hooks/agent-cap.js`,
  and REFUSES when none resolves.
- **S2** — Each script's population is anchored on a BASENAME plus the marker it already applies,
  never on a rooted path prefix. `check-workflow-syntax.js` already applies `MARKER` at line 67 and
  its prefix filter is genuinely redundant; the other two do NOT, so their filter is replaced by
  basename anchoring rather than deleted.
- **S3** — Each script's `SELF_EXCLUDE` is anchored the same way, because an exclusion spelled with
  a prefix is the same class as the population it scopes and parametrising one without the other
  converts a fork into a red bar.
- **S4** — The predicate is run over gov's tree BEFORE wiring, printing hits AND near-misses, and
  the record names what it caught.
- **S5** — Bump the review-harness and agent-cap versions with their paired markers.

## 3. Non-goals (OUT)

- **Deleting the prefix filter outright.** Measured and refused: `check-review-join.sh:56` and
  `check-verifier-fanout.sh:45` apply no marker filter, so deleting `grep -E '^tools/.*\.js$'`
  widens review-join's population from 7 files to 10 and admits `.claude/hooks/agent-cap.js`, whose
  own ban table trips the predicate. The bar goes red. Basename anchoring is the form.
- **A rooted `^\.claude/worktrees/` exclusion.** It is a new rooted literal introduced by the same
  edit that removes one, and it misses the nested case `.git/info/exclude` already anticipates.
  Basename anchoring is immune for free.
- ARM 2 of inCMS's review-join row. That is `TOOL-dRetiredFork-7`.

## 4. Design

### Inventory

| script | literal sites | what replaces them |
|---|---|---|
| `check-review-join.sh` | population, hook path, self-exclude | basename anchor plus the `HERE` probe chain |
| `check-verifier-fanout.sh` | population, hook path, self-exclude, message | the same, plus the message reads the resolved path |
| `check-workflow-syntax.js` | population filter, empty-population message | the existing `MARKER` becomes the population |

### Migration

The probe chain must reach BOTH measured layouts. NicoCares installs hooks at `scripts/hooks/`;
inCMS has no `scripts/hooks/` at all and its only copy is `.claude/hooks/agent-cap.js`. A two-rung
chain that resolves in gov and NicoCares strands inCMS, which is why the third rung is mandatory and
why this was caught only by testing the derivation against both trees.

### Alternatives rejected

Two conf keys for the population glob and the hook path. Rejected for the reason S1 exists: an
adopter cannot read a key their installed kit predates, and a derivation reaches every layout
including one nobody has enumerated, such as swydee's repo-root install.

## 5. Production-readiness checklist

- security — the resolved hook path must not accept a value that leaves its argument; the probe
  chain is closed and derives from `$0`, so no external value reaches it.
- perf / scale — one directory resolution and one existence probe per run.
- a11y — N/A.
- i18n — N/A.
- error / empty / loading states — an unresolvable hook REFUSES; an empty population REFUSES. Both
  already exist in two of the three scripts and must exist in all three after this unit.
- observability — each script prints the resolved hook path and its population size.
- risks — a basename anchor is wider than a path prefix and may admit a file the prefix excluded.
  This is exactly what S4's pre-wiring run exists to find, and it is not optional.
- testing + left-shift gates — the three scripts' own suites, plus a foreign-prefix fixture.
- migration / rollback — reverting restores the literals; no adopter state changes.
- user docs — `tools/workflows/README.md` states the resolution order once, for all three.

## 6. Acceptance criteria

- **AC1** — When run in gov's tree, each of the three scripts produces a verdict and a population
  size byte-identical to its pre-change run. Compared across `bash tools/workflows/check-review-join.sh` runs.
- **AC2** — When run in a fixture installed at `scripts/`, each resolves its hook and its population
  and exits `0`; the pre-change scripts found an empty population there.
- **AC3** — When run in a fixture whose only hook copy is at `.claude/hooks/agent-cap.js`, each
  resolves it — the inCMS layout, which a two-rung chain strands.
- **AC4** — When no hook resolves, each script REFUSES naming the probes it tried. Observed via `bash tools/workflows/check-verifier-fanout.sh`.
- **AC5** — The pre-wiring predicate run over gov's tree is recorded with its hits and near-misses,
  and `bash tools/workflows/check-review-join.sh` still reports a 7-file population.
- **AC6** — `bash tools/check-kit-versions.sh` exits `0` after the bumps.

## 7. Gates

`review join` · `verifier fan-out` · `workflow syntax` · `agent-cap self-test` · `kit versions` ·
`install prefix (shipped surface)`.

## 8. Open questions

- **F1 — does the third probe rung stay `.claude/hooks/`, or become a declared locator?** The rung
  is a literal, and this unit's own rule bans literals. It is defensible as the harness's own
  convention rather than an install prefix. Recommendation: keep it, and say in the header that it is
  the harness convention and not a kit path — but this is a fork the owner should see, because it is
  the one place the unit does not practise what it enforces.

## 9. Revision log

- rev-1 · 2026-09-02 · initial draft. Records the refuted filter-deletion approach in §3 so a later
  session does not re-propose it.

## 10. Reuse audit

The seam is `kit_rel` in `tools/memory-tree/gen_build_index.py` — `reuse_lookup.py` reports it as a
fan-in-4 SEAM and it is the corpus's existing answer to "where does this kit live", extended here
from a variable to a probe chain. `derive_carried` and its siblings in `tools/govkit/govkit.py` are
the deployer-side counterpart and are deliberately NOT reused: they transform recorded bytes, while
this resolves a live path.

Recall terms used: `carve-out`, `install-prefix`, `KIT_REL`, `carried`, `relocate`, `rung`,
`adopter`, `divergence`, `repath`, `govkit`, `receipt`, `unattributed`, `derive`, `prefix`.
