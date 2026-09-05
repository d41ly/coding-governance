<!-- gov:kit unattended@1.18 -->
# Fixture playbook — the kit's own, so the leg's population is never empty

**This is a FIXTURE, not an example to copy.** It exists because `check-playbook.sh` carries the
mode's whole enforcement, and a leg with an empty population prints a green that means the opposite
of what it looks like. It is deliberately minimal: it demonstrates the SHAPE the canon requires and
makes no claim to be a good playbook about anything.

```toml
step_selector = "^[*][*]F[0-9]+[.]"
step_floor    = 3
outputs       = ["{{KIT_DIR}}/fixture-pieces/**"]
grain         = "{{KIT_DIR}}/fixture-pieces/*/piece.md"
records       = "{{KIT_DIR}}/fixture-records"
piece_checks  = ["fixture-shape"]
set_checks    = ["fixture-distinct"]
legs          = { fixture-shape = "{{KIT_DIR}}/check-playbook.sh", fixture-distinct = "{{KIT_DIR}}/check-playbook.sh" }
coverage      = "resolvable"
curated       = "the playbook-mode build, node d, 2026-08-21"
```

## 1. Identity and provenance

Ratified as the kit's population fixture on 2026-08-21 by the build that introduced this leg.
Its evidence is that build's spec set; it has no owner acceptance because it produces nothing anybody ships.

## 2. Ground rules

A fixture may never be cited as a worked example of a real playbook. Every sentence quoted in it is
PROHIBITED OUTPUT, which is the canon's own rule applied to the file that demonstrates the canon.

## 3. Inputs and preconditions

None beyond a checkout. `none — a fixture takes no input; it exists to be graded, not run.`

## 4. Outputs

One piece is a directory under the declared output root carrying a `piece.md`. The grain matches
that file, so a piece is one directory and never one file of three.

## 5. The step checklist

**F1. Read the canon before writing a step.** `CHECK the canon is prose and no machine reads intent · witness the section this step was written against`

**F2. Tag every step.** `GATE fixture-shape` — an untagged step reds, because what enforces a step
being unstated is how every later reader assumes something different.

**F3. Do not copy this file.** `CHECK a machine cannot tell a copy from an independent playbook that happens to agree`

## 6. The producer recipe

`none — a fixture produces nothing, so there is no scaffold to fix.`

## 7. Per-piece checks

`fixture-shape` — the piece carries the shape section 4 describes. Verdict is PASS, FAIL or
N/A-with-reason, never a score.

## 8. Set-scoped checks

`fixture-distinct` — no two pieces are byte-identical. Trivial, and it is here because a set-scoped
population that is empty in the file demonstrating the canon would teach exactly the wrong lesson.

## 9. Declared gate legs

Both names resolve to this kit's own leg, which is what `coverage = "resolvable"` claims. A registry
entry whose target does not resolve reds under that mode.

## 10. Ruled out — do not re-try

- **A fixture with no steps.** Tried while writing unit 3: the step floor then has nothing to
  measure and the selector arm passes over an empty selection, which is the defect the floor exists
  to catch. Ruled out 2026-08-21.
- **Using a real playbook from another repository as the fixture.** It would tie this kit's gate to
  another project's editorial decisions, and a pin copied from another corpus is either vacuous or
  permanently red.

## 11. Measured failure modes

Measured while building unit 3: reading tags LINE-WISE rather than over a step's window missed every
line-wrapped tag, which is a live defect in the corpus this canon was derived from — two invariants
there have never once been validated by their own gate.

## 12. Corrections to this file

None yet. When this file is wrong, the correction goes here, dated, naming the id that made it.
