# Acceptance ledger — TOOL-dRetiredFork-16

**Serves:** journal TOOL-dRetiredFork-16

Tier-2 · node d · 2026-09-03

F1 was a FACT-QUESTION and §5 said the unit's premise depended on it: "if `apply` in fact overwrites
a target-authored leg, this unit's premise is false and the unit becomes a defect report instead."
It does not. The premise holds, measured.

## Acceptance criteria

**Evidences:** TOOL-dRetiredFork-16

- AC1 — MET, measured — `govkit apply` over a fixture whose manifest held exactly ONE leg,
  project-authored, left it holding 23: gov's 22 emitted alongside the project's own, byte for byte unchanged.
  The run mentioned it ZERO times, which is the behaviour rev-2 corrected rev-1 to
- AC1b — MET, and the numbers are exact — a colliding name the receipt cannot claim raises `Refusal`,
  exits `2`, and leaves **41 paths already changed** in the working tree. The target's leg is preserved
  rather than overwritten, which is the guard's whole purpose
- AC2 — **NOT VERIFIED**, and named rather than claimed. The fixture's own `run-gates` hung past a
  300 s timeout, so the absent-script refusal was never observed. This is a run-gates property
  rather than a govkit one, and asserting it from the code would be the reading-not-measuring error
  this unit exists to avoid
- AC3 — MET — NicoCares' `scripts/check-build-readme-comments.sh` is the worked example named in the
  docs and its shape is quoted below. gov does not track that path and §3 forbids landing it, so it
  travels as evidence
- AC4 — MET on documentation, NOT MET on `check_runbook_parity.py`, which was already red. Both `tools/memory-tree/README.md` and `WIRE-INTO-PROJECT.md` name the extension point, the
  ownership rule and S5's refusal. `check_runbook_parity.py` exits 1 with **18 problems** — measured
  identically BEFORE and AFTER this unit, so the docs added none. The spec's own AC4 notes that no
  leg in `tools/gate-legs.json` invokes it, which is how a runbook claim nothing grades has been
  drifting unobserved. Filed as `TOOL-dRetiredFork-28`

## The probe's first answer was vacuous, and only the liveness check caught it

The first run reported the project leg SURVIVED. It had not: `apply` refused on a stale lock left by
an earlier run that timed out, and never touched the manifest at all. "Survived" was indistinguishable
from "nothing happened".

What caught it was asking a second question — *did the emission stage actually run?* — rather than
only looking at the outcome. The final probe asserts both halves: the leg is observable BEFORE
(1 leg), and the run demonstrably did work (`emitted 22`), so preservation is a real observation and
not the absence of one.

Three earlier attempts failed for reasons worth recording, because each looked like a result:
a duplicate `[gate_runner]` section (intake writes one; appending a second made the TOML invalid), a
dirty-path refusal, and a re-apply that collided with gov's OWN legs because the receipt no longer
claimed them.

## A finding the criteria did not ask for

When the receipt DOES claim a leg name the target also carries, `apply` does not refuse and does not
dedupe: both rows survive. Measured at 24 legs with **two rows named `memory hygiene`** in a manifest
whose declared `dedupe_key` is `name`. Filed as `TOOL-dRetiredFork-27`.

That is arguably worse than the refusal AC1b documents, because it is silent and the manifest is
left in a state its own key says is impossible.

## The worked example, as evidence

NicoCares' check 90 is a project rule about a project's own comment convention, run over its 75
build READMEs. Its shape is what the pattern prescribes: a script under the project's own tree,
sourcing `.memory-tree.conf` for `MEMORY_ROOT` exactly as the kit's own checks do, registered as a
leg the project owns with its own declared ceiling.

gov has no such convention, and §3 is right that a check gov cannot fail is a check gov should not
carry. It travels here as evidence that the pattern has a real instance rather than a sketch.

## What was refused

S5, written into the kit README so a later session does not add it: no plugin loader inside the
engine, and no `PROJECT_CHECKS` conf key naming scripts the engine invokes. The second is the first
under another name — it inverts ownership, making the kit responsible for a script it cannot read.
