**Serves:** research PLAY-dOrderedCharter-40

# Brief: spec 40 — move it into order 37, beside deferred unit 39, so the order gate admits it

## The prompt

> why are the specs being reviews (and 11 times at that) instead of building?

— owner, 2026-11-09. Unit 40's dispatch was refused twice by the order gate: PLAY-dOrderedCharter-39, at order 37, is DEFERRED
behind parked PLAY-dOrderedCharter-31 and can neither build nor turn terminal in this run, and the gate counts a deferral as
blocking every later order. Unit 40 consumes nothing at order 37 except PLAY-dOrderedCharter-37, and nothing consumes unit 40 at
order 37. Units sharing an order value are one parallel group, sorted inside by their edges, and do not block each other.

## The brief

### Goal

Move spec 40's build-order verb from `order 38` to `order 37`, so it shares a group with units 37 and 39.

### Items

1. Change only the `order` cell of spec 40's **Status:** line, bump its rev by one, dated 2026-11-09, status kept `DEFERRED`, and add
   one revision-log line naming this brief and saying no design text moved.
2. Confirm against HEAD that every `consumes-from` edge of spec 40 points at a unit at order 37 or lower, that no unit at order 37
   consumes unit 40, and that unit 40's hands-off edges still point at later orders. Name any edge that breaks in your return rather
   than edit around it.
3. Where spec 40's text states its own order as 38, correct it; cite nothing new.

### Acceptance

- Spec 40's Status line reads `order 37`, with a rev-5 log line, and nothing else in the spec moved but a stated order.

### Gates

None run: the main loop sweeps the spec before its commit.

### Non-goals

- No code, no design change, no edit to any other spec or file.
