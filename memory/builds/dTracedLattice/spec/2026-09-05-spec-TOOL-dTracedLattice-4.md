# TOOL-dTracedLattice-4 — an adopter's frozen gate copy is compared against the template that moved

**Status:** SPECCED · rev-1 · 2026-09-05 · node d · Tier-2 · base c4fcf5ad · streams tooling · order 4

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-09-05-build-TOOL-dTracedLattice-1-design-dossier.md](../build/2026-09-05-build-TOOL-dTracedLattice-1-design-dossier.md) | research | TOOL-dTracedLattice-1 TOOL-dTracedLattice-2 TOOL-dTracedLattice-3 TOOL-dTracedLattice-5 |

<!-- /gen:spec-records -->

## 1. Goal

`adopt-codebase-map.sh` copies the gate template into an adopting repo only when it is absent and
leaves it untouched thereafter, while `gen_map.py` is engine and does update on every kit upgrade. A
new generated artifact therefore starts being WRITTEN into upgraded adopters whose gate never
compares it, and nothing detects the divergence.

## 2. Scope (IN)

- **S1** A check that compares an installed `GATE_FILE` against the kit's template and reports the
  divergence, naming what the installed copy does not check.
- **S2** The check reports the ADOPTER-visible consequence rather than a diff: which generated
  artifacts the engine writes that the installed gate does not compare. A byte diff between two files
  a project is entitled to customise is noise; an uncompared artifact is the defect.
- **S3** A declared disposition for a legitimately customised gate — a project may edit its gate, so
  the check must distinguish customised from stale, or say plainly that it cannot.
- **S4** `tools/codebase-map/kit.toml` records this as a known hole with its compensating check, per
  `AGENTS.md` §7's rule that an exemption ships with the check that covers it.

## 3. Non-goals (OUT)

- Not auto-updating an adopter's gate. Overwriting a file a project owns is a different and more
  dangerous change, and `govkit` owns update policy.
- Not the general kit-upgrade mechanism; this unit is scoped to the one pair where an engine writes
  what a frozen gate must compare.
- Not the freshness gate's internal behaviour — `TOOL-dTracedLattice-2` owns that.

## 4. Design

### Inventory

The pair is `tools/codebase-map/test_codebase_map.template.py` (the source) and whatever
`.codebase-map.conf`'s `GATE_FILE` names (the installed copy). In this repository those resolve to
byte-identical files only because `GATE_FILE` happens to point inside the kit directory, which is why
gov's own tree shows no symptom and every adopter's does.

### Alternatives rejected

A byte-equality assert between template and installed copy. It reds every adopter who has legitimately
customised their gate, which S3 exists to avoid, and it tells a reader nothing about what is actually
uncovered.

### Rollout

S1 and S2 together — S1 without S2 is a diff nobody can act on. S3 decides the check's verdict
vocabulary and therefore lands with them. S4 last, recording whatever hole remains.

## 5. Production-readiness checklist

- security — N/A.
- perf / scale — one file read and one AST or text scan; negligible.
- a11y — N/A. i18n — N/A.
- error / empty / loading states — an adopter with no `GATE_FILE` configured is a legal state and
  must produce a named skip, not a crash and not a silent pass.
- observability — S2 is the observability item.
- risks — a check that cannot distinguish customised from stale becomes noise and gets ignored; S3
  addresses it, and if it cannot be addressed the honest outcome is to say so in the header.
- testing + left-shift gates — a fixture with an installed gate missing a tier the engine writes,
  observed RED first.
- migration / rollback — reporting only; nothing to migrate.
- user docs — `tools/codebase-map/README.md` adoption section gains the upgrade note.

## 6. Acceptance criteria

- **AC1** — When a fixture adopter's `GATE_FILE` lacks a tier that `gen_map.py` writes, the check
  FAILS naming that artifact, and this arm is observed RED before the fix lands.
- **AC2** — When the installed gate covers every artifact `gen_map.py` writes, the check passes even
  if it differs byte-for-byte from `test_codebase_map.template.py`, so a customised gate is not
  punished for being customised.
- **AC3** — When `GATE_FILE` is unset or names no existing file, the check reports a named `skipped`
  rather than passing silently.
- **AC4** — When `tools/codebase-map/kit.toml` is read, it declares this hole and names the check that
  compensates for it.

## 7. Gates

`codebase-map kit selftest` · `kit version markers` · `kit/dogfood doc parity` ·
`kit placeholders (a declared token its adopter substitutes)` ·
`harness arms (fail branches armed or pinned)`.

## 8. Open questions

- **Q1 — can customised be distinguished from stale at all?** Comparing the SET of artifacts each side
  handles is the proposed discriminator, and it is weaker than a diff: a gate that names an artifact
  but compares it wrongly passes. FACT-QUESTION · the probe is running the proposed discriminator over
  a fixture whose installed gate names every artifact and compares one of them with a broken predicate,
  and the observation is whether the check reports it. LIVENESS: the discriminator returns a failure on
  the AC1 fixture, so it can produce a negative. RESOLVED (agent, 2026-09-05, delegated): the
  discriminator ships with its limit stated in the check's own header rather than implied away.

## 9. Revision log

- rev-1 · 2026-09-05 · initial draft, from the dTracedLattice skeptic round.

## 10. Reuse audit

The seam this unit extends is the kit-declaration checking already performed by
`tools/check-kit-placeholders.py` and `tools/check-kit-versions.sh`, cited from
`python tools/codebase-map/reuse_lookup.py "assert an installed copy still matches the kit template"`,
which returns `check-kit-placeholders.py` through the `kit-placeholders` affordance seam. That is a
cross-kit textual join over declared surfaces, which is the same shape as S1, so this unit follows its
structure rather than inventing a second comparison idiom. Verified against source at writing time:
that checker reads declarations and asserts them against the tracked surface in both directions.

Recall terms used: adopter kit upgrade template installed gate copy frozen drift byte-compare
generated artifact govkit update withdrawal
