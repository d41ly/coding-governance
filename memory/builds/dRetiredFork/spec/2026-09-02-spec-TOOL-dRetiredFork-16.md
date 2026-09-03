# TOOL-dRetiredFork-16 — a project adds a check without editing a kit engine

**Status:** CLOSED · rev-4 · 2026-09-03 · node d · Tier-2 · base b0108f13 · streams tooling · order 5 · ratified 2026-09-02

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-09-03-build-TOOL-dRetiredFork-16-1-acceptance-ledger.md](../build/2026-09-03-build-TOOL-dRetiredFork-16-1-acceptance-ledger.md) | journal | — |
| [2026-09-03-prompt-TOOL-dRetiredFork-16-1-build-brief.md](../prompts/2026-09-03-prompt-TOOL-dRetiredFork-16-1-build-brief.md) | journal | — |
| [2026-09-02-review-TOOL-dRetiredFork-1-18-and-depl-1-7-spec-audit-round1.md](../reviews/2026-09-02-review-TOOL-dRetiredFork-1-18-and-depl-1-7-spec-audit-round1.md) | spec-audit | DEPL-dRetiredFork-1 DEPL-dRetiredFork-2 DEPL-dRetiredFork-3 DEPL-dRetiredFork-4 DEPL-dRetiredFork-5 DEPL-dRetiredFork-6 DEPL-dRetiredFork-7 TOOL-dRetiredFork-1 TOOL-dRetiredFork-2 TOOL-dRetiredFork-3 TOOL-dRetiredFork-4 TOOL-dRetiredFork-5 TOOL-dRetiredFork-6 TOOL-dRetiredFork-7 TOOL-dRetiredFork-8 TOOL-dRetiredFork-9 TOOL-dRetiredFork-10 TOOL-dRetiredFork-11 TOOL-dRetiredFork-12 TOOL-dRetiredFork-13 TOOL-dRetiredFork-14 TOOL-dRetiredFork-15 TOOL-dRetiredFork-17 TOOL-dRetiredFork-18 |
| [2026-09-02-review-TOOL-dRetiredFork-1-18-and-depl-1-7-spec-audit-round2.md](../reviews/2026-09-02-review-TOOL-dRetiredFork-1-18-and-depl-1-7-spec-audit-round2.md) | spec-audit | DEPL-dRetiredFork-1 DEPL-dRetiredFork-2 DEPL-dRetiredFork-3 DEPL-dRetiredFork-4 DEPL-dRetiredFork-5 DEPL-dRetiredFork-6 DEPL-dRetiredFork-7 TOOL-dRetiredFork-1 TOOL-dRetiredFork-2 TOOL-dRetiredFork-3 TOOL-dRetiredFork-4 TOOL-dRetiredFork-5 TOOL-dRetiredFork-6 TOOL-dRetiredFork-7 TOOL-dRetiredFork-8 TOOL-dRetiredFork-9 TOOL-dRetiredFork-10 TOOL-dRetiredFork-11 TOOL-dRetiredFork-12 TOOL-dRetiredFork-13 TOOL-dRetiredFork-14 TOOL-dRetiredFork-15 TOOL-dRetiredFork-17 TOOL-dRetiredFork-18 |
| [2026-09-02-review-TOOL-dRetiredFork-3-21-and-depl-1-9-spec-audit-round3.md](../reviews/2026-09-02-review-TOOL-dRetiredFork-3-21-and-depl-1-9-spec-audit-round3.md) | spec-audit | DEPL-dRetiredFork-1 DEPL-dRetiredFork-2 DEPL-dRetiredFork-3 DEPL-dRetiredFork-6 DEPL-dRetiredFork-7 DEPL-dRetiredFork-8 DEPL-dRetiredFork-9 TOOL-dRetiredFork-3 TOOL-dRetiredFork-5 TOOL-dRetiredFork-8 TOOL-dRetiredFork-9 TOOL-dRetiredFork-11 TOOL-dRetiredFork-12 TOOL-dRetiredFork-13 TOOL-dRetiredFork-14 TOOL-dRetiredFork-15 TOOL-dRetiredFork-17 TOOL-dRetiredFork-19 TOOL-dRetiredFork-20 TOOL-dRetiredFork-21 |

<!-- /gen:spec-records -->

## 1. Goal

`nc carve-out 6/20` is an entire NicoCares-authored check — roughly 22 lines plus a two-fixture arm,
over a live population of 75 build READMEs — living INSIDE `check-memory-hygiene.sh` because there
was nowhere else to put it. A project with a rule gov does not have currently has exactly one option:
edit the kit engine and re-merge it on every release. That is the class this build exists to end, and
no amount of conf keys reaches it, because the project is adding BEHAVIOUR and not a value.

## 2. Scope (IN)

- **S1** — Document the extension point that already exists, and its LIMITS, both measured. The
  guard is at `tools/govkit/govkit.py:4680` with its raise at `:4681-4683` — rev-1 cited `:4676`,
  four lines short — and it fires ONLY on a name collision. Two behaviours follow and neither is
  "declines and reports": a colliding name raises `Refusal`, whose nearest handler is `main`'s at
  `:7382`, reached AFTER the write and stage loop at `:4300-4341`, so the verb aborts at exit 2
  with a partially applied install; a NON-colliding project leg is carried in `existing` and
  rewritten at `:4734-4736` with no report at all.
- **S2** — A worked pattern in `tools/memory-tree/README.md` and `WIRE-INTO-PROJECT.md`: a project
  check is its own script under the project's own tree, sourcing `.memory-tree.conf` for
  `MEMORY_ROOT` exactly as the kit does, and registered as a leg the project owns.
- **S3** — Verify S1 by measurement rather than by reading: install a fixture, add a
  project-authored leg to its manifest, run `govkit apply`, and confirm the leg survives. This is a
  `FACT-QUESTION` and the observation decides it.
- **S4** — NicoCares' check 90 is written out as the worked example — `scripts/check-build-readme-comments.sh`
  — and named in the record, so the pattern ships with a real instance rather than a sketch.
- **S5** — A named refusal for the thing that must NOT be built: a plugin loader inside the kit
  engine. Stated in the README so a later session does not add one.

## 3. Non-goals (OUT)

- A hook or plugin mechanism inside `check-memory-hygiene.sh`. A kit engine that loads project code
  is a kit engine whose behaviour the kit cannot state, and every gate it runs becomes ungradeable.
- Absorbing check 90 into gov. It is a genuine project rule about a project's own comment
  convention; gov has no such convention and a check gov cannot fail is a check gov should not carry.
- Any change to how the gate runner discovers legs. The manifest is already the seam.

## 4. Design

### Migration

Nothing in gov changes behaviourally. The unit's deliverable is a documented, MEASURED contract plus
one worked example, which is why its risk is low and its value is high: it removes the last reason
an adopter has to edit an engine at all.

### Alternatives rejected

A `PROJECT_CHECKS` conf key naming scripts the kit invokes. It inverts the ownership — the kit would
then be responsible for a script it cannot read — and it re-creates the loader in S5's refusal under
a different name.

## 5. Production-readiness checklist

- security — a project-authored leg runs project-authored code under the project's own bar, which is
  where it belongs. gov executes nothing new.
- perf / scale — the project's leg costs what the project decides; the gate runner already bounds
  legs by declared ceiling.
- a11y — N/A.
- i18n — N/A.
- error / empty / loading states — a project leg that cannot find its subject must REFUSE, and the
  worked example demonstrates that rather than describing it.
- observability — the gate runner already names every leg it runs and every leg it skips.
- risks — the documented contract is only as true as S3's measurement. If `apply` in fact overwrites
  a target-authored leg, this unit's premise is false and the unit becomes a defect report instead.
  That inversion is why S3 is scoped as a probe with an observable negative.
- testing + left-shift gates — S3's fixture run; no new gov leg.
- migration / rollback — documentation plus one example; nothing to roll back.
- user docs — this unit is largely user docs, in `tools/memory-tree/README.md` and
  `WIRE-INTO-PROJECT.md`.

## 6. Acceptance criteria

- **AC1** — When a fixture target's gate manifest carries a project-authored leg whose name does
  NOT collide with a gov leg and `govkit apply` runs, the leg is still present afterwards. The run
  reports nothing about it, which is the measured behaviour and not the one rev-1 asserted.
- **AC1b** — When the project-authored leg's name DOES collide, the run raises and exits `2` with
  the install partially applied. Recorded as the extension point's limit; whether it should be a
  pre-write refusal is filed rather than fixed here.
- **AC2** — When the same leg's script is absent, the target's gate runner REFUSES naming it, rather
  than skipping silently. Observed via the target's own `bash tools/run-gates/run-gates.sh`.
- **AC3** — NicoCares' `scripts/check-build-readme-comments.sh` is quoted VERBATIM in this build's
  record together with its fixture and its red output. gov does not track that path and §3's own
  non-goal forbids landing it here, so the example travels as evidence rather than as a file. It
  sources
  `.memory-tree.conf`, and reds on the fixture that motivated NicoCares' check 90.
- **AC4** — `tools/memory-tree/README.md` and `WIRE-INTO-PROJECT.md` both name the extension point, the ownership rule and the refusal in
  S5, and `python tools/govkit/check_runbook_parity.py` still exits `0`. It is a python program and
  rev-1 invoked it with `bash`; it is also invoked by NO leg in `tools/gate-legs.json`, so this
  direct invocation is the only thing exercising the runbook claim anywhere in the build.
## 7. Gates

`govkit selfcheck` · `memory hygiene`.

## 8. Open questions

- **F1 — FACT-QUESTION · does `apply` really preserve a target-authored leg?** The probe is S3:
  install a fixture, add a leg, run `apply`, look. The liveness assertion is that the fixture's leg
  must be observable BEFORE the run, so a run that deleted the manifest entirely is distinguishable
  from one that preserved the leg. UNRESOLVED until run; the unit's shape depends on the answer.
- **F2 — does a project leg get a declared wall-clock ceiling like a kit leg?** The runner already
  reds a leg arriving without one. Recommendation: yes, and say so in the worked example, because an
  adopter discovering that rule from a red bar is a worse first experience than reading it.

**RESOLVED (owner, 2026-09-02): every fork above is settled by its own stated Recommendation.** The owner ratified them as written on 2026-09-02 with the instruction to fold the recommendations. No fork is resolved against its recommendation and none by silence; where a later measurement contradicts a ratified pick, that is a new fork with a new id.

## 9. Revision log

- rev-1 · 2026-09-02 · initial draft, from `nc carve-out 6/20` and the `owned`/`emitted` refusal at
  `tools/govkit/govkit.py:4627` and `:4676`.
- rev-2 · 2026-09-02 · folded spec-audit round 1, findings H11 and L1. H11: rev-1's AC1 required a "declines and reports"
  behaviour the code has in neither branch — a colliding name aborts at exit 2 after a partial
  write, a non-colliding one is preserved silently — and it pre-answered F1, which S3 declares a
  fact-question. L1: the citation was four lines short and a python program was invoked with `bash`.
- rev-3 · 2026-09-02 · folded spec-audit round 2, finding 19. AC3 required a path gov does not track and §3's
  own non-goal forbids creating; the worked example now travels as quoted evidence. AC4 gained the
  second carrier S2 names.

- rev-4 . 2026-09-03 . BUILT. F1 ANSWERED BY MEASUREMENT: a fixture manifest holding ONE
  project-authored leg came out of `apply` holding 23, the project row byte-identical and mentioned
  zero times. The premise holds; the unit is not a defect report. AC1b is exact -- a colliding name
  the receipt cannot claim exits 2 with 41 paths already changed, and the target leg preserved.

  THE PROBE'S FIRST ANSWER WAS VACUOUS. It reported SURVIVED after a run that had refused on a stale
  lock and never touched the manifest, which is indistinguishable from success by outcome alone.
  Caught by asking whether the emission stage ran, not by looking harder at the result.

  AC2 is NOT VERIFIED and named as such: the fixture runner hung past 300 s, so the absent-script
  refusal was never observed, and asserting it from the code is the error this unit exists to avoid.
  AC4 is met on documentation and not on its checker: `check_runbook_parity.py` exits 1 with 18
  problems, measured identically before and after, and no leg invokes it -- filed as -28. A finding
  no criterion asked for: when the receipt DOES claim a colliding name, both rows survive, leaving
  two legs named `memory hygiene` in a manifest keyed by name -- filed as -27.

## 10. Reuse audit

The seam is the gate manifest itself plus `govkit`'s `owned` computation from `gate_runner.emitted` —
`reuse_lookup.py` reports the `govkit` affordance seam covering `registry.toml` and the leg-emission
surface, and this unit documents and measures that existing refusal rather than adding a mechanism
beside it. No new seam is created, which is the point.

Recall terms used: `gate_runner`, `emitted`, `owned`, `leg`, `manifest`, `project check`,
`extension point`, `carve-out`, `adopter`, `apply`, `overwrite`, `ceiling`.
