# TOOL-aTetheredRecord-6 — the adopter path: the obligation ships with the step that arms it

**Status:** SPECCED · rev-2 · 2026-08-17 · node a · Tier-2 · base 96141aed · streams tooling

## 1. Goal

Make check 21 adoptable by a repo whose corpus nobody here can read. This repo satisfies the rule by
retrofitting 76 records because the owner put that in scope; an adopter has their own corpus, their
own budget, and no such decision. The kit must ship the rule together with the step that measures
their pin and the runbook section that describes their migration.

## 2. Scope (IN)

- **S1** — A step in `tools/memory-tree/adopt-memory-tree.sh`'s next-steps block, ORDERED as the
  migration actually runs: first the mechanical `none` pass over their existing records, then MEASURE
  `RECORD_UNBOUND_PIN` at the resulting count via
  `python <kit>/gen_build_index.py --print-bindings`, which reports it with no pin set. Never inherit
  this repo's number. Every path it prints is built from the script's own derived install prefix.
- **S2** — A migration section in `WIRE-INTO-PROJECT.md`, in the shape the existing kit-version
  section uses: the kit version boundary, a plain statement that an untouched tree holding records
  reds on first run, the numbered migration, and a worked example with a measured figure.
- **S3** — `AGENTS.md`'s gate-suite section names check 21 and what it enforces.

## 3. Non-goals (OUT)

- **No cutoff, and no shipped waiver seeded from this repo's population.** A registry seeded from
  gov's rows would name paths an adopter's tree does not have — the same reasoning the method-carrier
  registry already ships under, where the kit deliberately ships none.
- **No automatic retrofit tool.** Binding a record to a spec is a judgement about what a document was
  about. A script that guessed it would fabricate provenance at scale, which is the one failure the
  retrofit's precedence rule exists to prevent.
- **No `--check` verb for the adopter script.** It lacks one, alone among the kits, and adding it is
  a real fix with a real blast radius. Recommended separately.

## 4. Design

### The asymmetry, stated plainly

**For an adopter the first run is RED, and no value of the pin changes that.** Branch 1 names every
record carrying no line at all; `RECORD_UNBOUND_PIN` bounds branch 3, whose population is records
carrying an authored `none` with a reason. The two populations are DISJOINT — the parser returns
`absent` and `unbound` as different states precisely so a pin cannot excuse a record nobody ever
annotated. An earlier draft of this section claimed the pin made an adopter green on day one; that
was mechanically false, and it contradicted this unit's own S2.

Their migration is one mechanical pass writing `**Serves:** none — <reason>` onto each existing
record. It needs no judgement about what any document was about, which is what makes it mechanical
rather than a retrofit, and it is not a cutoff: nothing is exempted by date and every record stays
visible. They then MEASURE `RECORD_UNBOUND_PIN` at that count and drain it as they bind records for
real. The pin bounds the deliberate escape; it never bounds the absent line.

This is the honest reading of "no cutoffs" applied to a repo the owner does not own. The owner's
decision binds this corpus, which is retrofitted in full by `TOOL-aTetheredRecord-3`. If the owner
wants a genuinely green day one for adopters, that is a FIFTH scalar bounding branch 1 — a new fork
and an owner decision, recorded in `TOOL-aTetheredRecord-4`, not a spec edit here.

### Rollout

The step lands with the check, not after it. Every content ratchet this kit ships is armed from the
scaffolder's next-steps block, and all three candidate designs in the design pass forgot it — which
is the evidence that it is easy to forget and therefore belongs in scope rather than in a follow-up.

### Files touched (estimate)

`tools/memory-tree/adopt-memory-tree.sh`, `WIRE-INTO-PROJECT.md`, `AGENTS.md`, and the shipped
example conf.

### Alternatives rejected

**Ship the pin with this repo's measured value as a default.** Every pin in this kit is measured
against the adopting corpus and never inherited, because a pin copied from a larger tree is either
vacuous or permanently red. The shipped example carries a blank, which is the strictest value and
forces the measurement.

**Let an existing adopter discover the rule on their next gate run.** The scaffolder exits early for
an already-adopted tree, so a rule added after their adoption never reaches them through the script
at all. The runbook section is how it reaches them, and this is a known gap in the kit rather than
one this unit introduces.

## 5. Production-readiness checklist

- security — N/A.
- perf / scale — N/A; documentation and one scaffolder step.
- a11y — N/A.
- i18n — N/A.
- error / empty / loading states — a scaffolded tree with no records has a blank pin and a check that
  skips on its population guard; that is the state the acceptance criteria assert.
- observability — the gate reports the adopter's remaining BRANCH-1 count on every run; that is the number that falls during their migration, not the unbound count.
- risks — the install-prefix class: a kit path spelled rather than derived lands a dead path in the
  adopter's committed tree, and the byte-compare guarding that file agrees with it. Every path this
  unit adds is derived, and the gate for that is a named acceptance criterion.
- testing + left-shift gates — the install-prefix gate and the scaffold-into-an-empty-repo case.
- migration / rollback — documentation; revertible.
- user docs — this unit IS the user docs.

## 6. Acceptance criteria

- **AC1** — When `bash tools/check-install-prefix.sh` runs, it is green: nothing this unit adds
  spells a root-install kit path.
- **AC2** — When the adopter script scaffolds into an empty scratch repo and
  `bash tools/memory-tree/check-memory-hygiene.sh` is run there with a blank pin, it exits 0.
- **AC2b** — When it scaffolds into a scratch repo that ALREADY holds one build, one spec and two
  records with no binding line, `bash tools/memory-tree/check-memory-hygiene.sh` exits 1 naming
  branch 1 — and exits 0 after the mechanical `none` pass with the pin measured at 2. AC2 alone
  exercises the empty tree, where the population guard skips the check entirely, so it cannot observe
  the case this unit exists for.
- **AC3** — When the next-steps block emitted by `tools/memory-tree/adopt-memory-tree.sh` is read,
  its measurement step names the gate command built from the script's derived prefix, and states that
  the pin is measured rather than inherited.
- **AC4** — When `python tools/drift-audit/drift_report.py --check` runs, it is green.
- **AC5** — When `AGENTS.md`'s gate-suite section is read, check 21 is named there, satisfying the
  charter-names-every-leg signal for the renamed leg.
- **AC6** — When `bash tools/run-gates.sh` runs, every leg is green.

## 7. Gates

`install prefix` · `drift-audit records` · `memory hygiene` · `agent-instructions wiring` ·
`bash tools/run-gates.sh` at the push boundary.

## 8. Open questions

none — the asymmetry in §4 is a design decision recorded there, not a fork. It follows directly from
the owner's no-cutoff ruling applying to this corpus and from the kit's standing rule that every pin
is measured against the adopting tree.

## 9. Revision log

- rev-1 · 2026-08-16 · initial draft, from the adversarial design pass recorded under this build's
  `build/` folder.
- rev-2 · 2026-08-17 · folded the M4 audit, which held this unit BLOCKED. §4 claimed a measured pin
  made an adopter's tree green on day one. It cannot: `absent` and `unbound` are disjoint populations
  and the pin bounds only the second, so an untouched adopter tree reds on branch 1 whatever the pin
  says — and the same document already told the runbook to say so, in S2. Only one of the two could
  ship. The adopter's first run is now stated as RED, with the mechanical `none` pass as their
  migration, S1 reordered to match, and AC2b covering the non-empty tree AC2 structurally could not
  reach.

## 10. Reuse audit

Three shipped patterns carry this unit unchanged: the scaffolder's next-steps block, which is where
every other content ratchet in this kit is armed; the per-repo measured-pin convention, which the
repo conf documents for each of its existing pins; and the runbook's kit-version section, whose shape
S2 copies. The one thing deliberately NOT reused is the seeded-registry pattern from the
method-carrier gate — that gate ships no registry and scaffolds the adopter's from their own measured
population, and a seeded registry was rejected here in favour of a scalar pin. Recall terms:
`build slug spec artifact filename header adversarial review closeout journal bookkeeping convergence
naming hygiene`.
