# Brief — dCountedConsumers: help/policy.md names the policy keys that have consumers today

**Serves:** research TOOL-dCountedConsumers-1

## The prompt

> go with your recommendations, there was no reason to park that

## The brief

### Goal
`help/policy.md` stops claiming that only two families of keys have consumers. Its consumer paragraph names every key family that a reader consumes today, and links the page that documents each one.

### Items
1. Rewrite the consumer paragraph at `help/policy.md:8-14` so that it names each key family a reader consumes today, with a link to its page. Today that is the agent limit (`agent-limit.md`), the size caps (`size-caps.md`), `help.enforce` (`docs-leg.md`) and the three `review.spec-audit` keys (`spec-audit.md`). Verify the list against the tree's readers rather than this brief. If any other key's consumer is found, add it.
2. Keep the paragraph's last claim in a true form: a value set for a key with no reader is checked but changes nothing.

### Acceptance
The paragraph names every consumed key family, with one link each. `python tools/govkit/docs_leg.py` exits 0 with no STALE, LINK or COMMAND line on `help/policy.md`. The `policy fixtures` leg stays green.

### Gates
docs, policy fixtures, memory hygiene, and the plain bar at the close.

### Non-goals
BUILD-METHOD M6's dispatch sentence, which TOOL-dIndexedDesign-36 owns. HYGIENE's deviation paragraph. Any catalogue row or key behaviour. Any other part of `help/policy.md`.

### Limitations
`help/policy.md` sits under the `policy fixtures` guard, so the unit's gates section names that leg. A key that is anchored once stays anchored on exactly one page.

### Reuse
The page's own pointer style: it already links `agent-limit.md` and `size-caps.md` for the two families it names. The recall query returned TOOL-dIndexedDesign-36, which owns M6, and TOOL-dFoldedAudit-18, whose F1 named this paragraph.

## Drawn from the session

> help/policy.md:8-14 says only two key families have consumers, which was already wrong (help.enforce) and is now wrong for the three review.spec-audit keys.
— agent, the parked-decision listing, 2026-11-02

## Owner confirmation

Asked: Start the build as scoped?

> Go
