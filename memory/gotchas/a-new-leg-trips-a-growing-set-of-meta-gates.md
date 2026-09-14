---
name: a-new-leg-trips-a-growing-set-of-meta-gates
description: adding one gate leg trips a set of meta-gates that grows as new ones land, and a check inside an existing gate is far cheaper — but not free
kind: class
---

# A new leg trips a growing set of meta-gates; a new check inside a leg is the cheaper unit

## Symptom

A gate leg is added to `tools/gate-legs.json`, its own script goes green, and the bar reds in
three places the author never touched: a kit descriptor, a coverage inventory, an arms floor. Each
red is a different meta-gate asking "is this new moving part declared?", and the set of them grows
with every unit that adds one, so the list a session remembers is always one short.

## Where it bit

Every leg since the codebase-map coverage assert and the kit descriptors landed. A leg needs a
`[[gate_leg]]` in its kit's `kit.toml`, else an `[[exempt_leg]]`; the coverage leg claims its name
in a dossier; the run-gates canary checks its guard names a tracked path; the arms floor counts its
`fail` sites. Running the one script you wrote proves nothing about the four that grade it.

## The fix

**Run the full bar, never a list**, after adding a leg — `bash tools/run-gates/run-gates.sh` with
`GATE_FULL=1` if the leg is guarded — because the set of meta-gates is not enumerable from memory
and is enumerable from the bar. That is a PUSH-BOUNDARY sentence: inside a build pass run each
meta-gate's own script by hand and never the bar, which is the main loop's after the build is
complete (`memory/guides/BUILD-METHOD.md` M6; `gate-guard.js` refuses the flagged forms there).

**Prefer a new CHECK inside an existing gate to a new LEG.** A check inside
`tools/memory-tree/check-memory-hygiene.sh` costs neither the codebase-map coverage assert nor
drift-audit's leg signal, since both key on `tools/gate-legs.json` and neither moves. It still
costs `ARMS_FLOORS` in `.memory-tree.conf`, an arm per `fail` call site (not per check number),
and the leg's own name if that name states a count.

Gated by the meta-gates themselves — that is the class: each is correct alone, and the trap is
that their union is discovered by running it rather than known in advance.
