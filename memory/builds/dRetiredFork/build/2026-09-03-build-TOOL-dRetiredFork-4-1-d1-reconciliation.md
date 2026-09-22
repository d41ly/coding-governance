# TOOL-dRetiredFork-4 — the D1 reconciliation, and its evidence

**Serves:** journal TOOL-dRetiredFork-4

## S1 — inCMS's actual claim, obtained rather than paraphrased

From `C:/projects/incms/main/.claude/hooks/agent-cap.js:21-27`, verbatim:

> D1 - (ARCH-aFerriedToolkit-1) renderCodeView kept interpolation brace depth in ONE scalar that
> every `${` push zeroed, so a NESTED interpolation destroyed its parent's count, the parent closed
> at the next `}` it met, and the rest of the view was dropped with `unterminated` still false -
> rule 2 admitted a fan-out it denies one character apart. Measured on these 1.9 bytes: exit 0
> nested, exit 2 unnested.

**BOTH EARLIER REVISIONS ARGUED ABOUT THE WRONG FIXTURE.** rev-1 read this as "a marked
sequential-agent loop nested inside another loop". It is not: D1 is about NESTED TEMPLATE
INTERPOLATION. rev-2 then measured a nested LOOP (`tools/hooks/agent-cap.test.sh:357`), found the
opposite of rev-1's claim, and rescoped the unit on that refutation — but that fixture has nothing
to do with D1. The register row was never tested against the thing it actually says.

## S2 — run against gov HEAD, with both exit codes

The code shape D1 names IS present at HEAD: `tools/hooks/agent-cap.js:233` and `:639` both do
`stack.push('interp'); interpDepth = 0` — one scalar, zeroed on every push, not saved with the frame.

**A first fixture does not exercise it, and this is worth recording because it is the trap.** The
zeroing only matters when the OUTER interpolation already carries a non-zero brace depth when the
inner `${` arrives. With both depths at zero the inner push is a no-op and the parse is correct.
The fixture must open a brace inside the outer interpolation:

```
const s = `a ${ f({ k: `b ${ x } c` }) } d`; await parallel(D.map(d => () => agent(d.p)))
```

Invocation, against `tools/hooks/agent-cap.js` at HEAD:

```
python3 -c '...json.dumps({"tool_name":"Workflow","tool_input":{"script": <fixture>}})...' | node tools/hooks/agent-cap.js
```

| fixture | exit |
|---|---|
| same-line fan-out after a NESTED outer-depth interpolation | **2** |
| same-line fan-out after a FLAT outer-depth interpolation | **2** |
| the fan-out alone, as control | **2** |

inCMS measured `exit 0 nested, exit 2 unnested` on gov 1.9 bytes. gov HEAD denies all three.

**The view IS still corrupted — that half of D1 reproduces.** Running the shipped blankers directly:

| fixture | `renderLexedView` output |
|---|---|
| NESTED outer-depth | `["const s = \`   f({ k: \`   x  \`  \`", "MARKER"]` — the line's tail (`}) } d\``) is LOST |
| FLAT outer-depth | `["const s = \`   f({ k: 1 })  \`", "MARKER"]` — intact |

So the parent does close early and part of the line is dropped. What does NOT reproduce is the
FAIL-OPEN: `unterminated` stays false, the FOLLOWING line survives, and the fan-out is caught anyway
by a rule that matches raw text rather than the blanked view.

## S3 — disposition (b), with its evidence

**(b): the row does not reproduce at HEAD and is stale as a fail-open claim.**
`DEPL-dRetiredFork-7` strikes inCMS's `KIT_AGENT_CAP_DELTA` D1 row from that adopter's register.

Not (a): (a) requires a real gov defect of a different shape, and S3b binds any (a) successor to
`TOOL-aNumeralWarden-2`. That row is about the enclosing-opener WALK being defeated by two nested
wrappers or 59 lines of distance — a different mechanism from the interpolation-depth scalar, which
it does not mention. Forcing D1 onto it would file this measurement under a row that cannot carry it.

Not (c): the fixture is plain gov bytes and needs no adopter-local modification.

**The latent half is filed rather than dropped**: the scalar defect is real, measured, and currently
MASKED by rule overlap. `TOOL-dRetiredFork-24`.

## Acceptance ledger

**Evidences:** TOOL-dRetiredFork-4
- AC1 — `C:/projects/incms/main/.claude/hooks/agent-cap.js:21-27` — the D1 claim is recorded verbatim above with the invocation that runs it; `bash tools/hooks/agent-cap.test.sh` passes unchanged
- AC2 — `node tools/hooks/agent-cap.js` — three fixtures, exit 2 each, recorded above against inCMS's `exit 0 nested, exit 2 unnested`; the record states it agrees with neither the claim's fail-open half nor a clean bill, and says which half of D1 does reproduce
- AC3 — disposition (b) — named above with its evidence and with the reasons (a) and (c) were refused, naming the register row `DEPL-dRetiredFork-7` will strike
- AC4 — `memory/DECISIONS.md` — carries `TOOL-dRetiredFork-4`, and `bash tools/memory-tree/check-memory-hygiene.sh` exits 0 afterwards
