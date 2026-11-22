**Serves:** journal TOOL-dBoundRoles-65 TOOL-dBoundRoles-66 TOOL-dBoundRoles-67 TOOL-dBoundRoles-68 TOOL-dBoundRoles-69

# Brief — dBoundRoles: batch q of the behaviour re-ground, build orders 32 to 39

## The prompt

> /unattended dBoundRoles

— owner, 2026-11-22, starting this build run. The first two units this run dispatched each diverged before their code
on claims their specs make about current code that stopped holding after the spec run: other builds landed between the
specs' base `4ed9e567` and the run's base `8b8b1374`. The spec checker cannot see those claims. This batch re-grounds
its specs before their builders are dispatched, so each builder can build its spec as written.

## The brief

### Goal

Revise each spec named below in place, as a rev bump with one revision-log line each, so every claim it makes about
current code holds at HEAD.

### Items

1. For each spec, read the code it cites and verify every claim it makes about that code at HEAD: each path, symbol,
   line, count, signature, return shape, call order and behaviour, and each reader list (a grep of HEAD for every
   reader of a name the unit changes). Re-point a moved citation; re-ground a sentence whose code changed in behaviour;
   add a reader or file the unit's change reaches that its Files touched omits; correct a count.
2. A claim about code that an EARLIER unit of this build adds or changes is not stale. TOOL-dBoundRoles-14, TOOL-dBoundRoles-2 and TOOL-dBoundRoles-1 are built and CLOSED (at `7a58950fb`, `8795c820a` and `3b479f2fe`); the units of orders 4 to 31 are re-grounded and not yet built; every unit before yours in build order is in one of those positions. Spell `check_return`, never `validate_return`. Check such a claim
   against the earlier unit's spec, not HEAD, and say in the revision-log line where you did.
3. A stale claim whose fix is a choice rather than a correction is a fork: write it in §8 with its options and resolve
   it by M3's rule as a delegated agent resolution, `widens:` and `relaxes:` each a value or `none`. Never widen a
   unit's mechanism to fit; never change a criterion's number.
4. Cite code as `path#symbol` or `path@<blob8>:<line>`, never a bare `path:line`, and put a pin (a sha, a `path:line`
   or `DERIVED`) on any line quoting a count. Keep every criterion passable on a correct build and red on the break it
   names. Keep each status `DEFERRED`; one revision-log line per spec names this brief by its file stem.
5. `python tools/check-spec-tokens.py --spec <path>` and `check-memory-hygiene.sh --only 12 --spec <path>` exit 0 for
   each before you return. Return, per spec, what you changed and any fork you resolved.
6. The specs, in build order:
   - `TOOL-dBoundRoles-65` (`memory/builds/dBoundRoles/spec/2026-10-26-spec-TOOL-dBoundRoles-65.md`)
   - `TOOL-dBoundRoles-66` (`memory/builds/dBoundRoles/spec/2026-10-26-spec-TOOL-dBoundRoles-66.md`)
   - `TOOL-dBoundRoles-67` (`memory/builds/dBoundRoles/spec/2026-10-26-spec-TOOL-dBoundRoles-67.md`)
   - `TOOL-dBoundRoles-68` (`memory/builds/dBoundRoles/spec/2026-10-26-spec-TOOL-dBoundRoles-68.md`)
   - `TOOL-dBoundRoles-69` (`memory/builds/dBoundRoles/spec/2026-10-26-spec-TOOL-dBoundRoles-69.md`)

### Acceptance

Each spec carries the next rev and one revision-log line naming this brief; both checks exit 0 for each; the return
names every changed claim and every fork resolved.

### Gates

memory hygiene · spec tokens (a spec's own names resolve)

### Non-goals

No spec outside this batch. No product code. No register under `memory/project/`.

### Limitations

The write grant is this batch's spec files alone:
- `memory/builds/dBoundRoles/spec/2026-10-26-spec-TOOL-dBoundRoles-65.md`
- `memory/builds/dBoundRoles/spec/2026-10-26-spec-TOOL-dBoundRoles-66.md`
- `memory/builds/dBoundRoles/spec/2026-10-26-spec-TOOL-dBoundRoles-67.md`
- `memory/builds/dBoundRoles/spec/2026-10-26-spec-TOOL-dBoundRoles-68.md`
- `memory/builds/dBoundRoles/spec/2026-10-26-spec-TOOL-dBoundRoles-69.md`

### Reuse

Each spec's own §10.
